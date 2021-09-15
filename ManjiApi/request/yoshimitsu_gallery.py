from typing import Any, Optional, Union
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup, element
from ManjiApi.request.base import BaseRequest


class YoshiGallRequest(BaseRequest):
    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__(session)

    @property
    def url(self) -> str:
        return "https://gall.dcinside.com/mgallery/board"

    @property
    def headers(self) -> dict[str, str]:
        return {"User-Agent": self.user_agent}

    @classmethod
    async def setup(cls, **kwargs: Any) -> "YoshiGallRequest":
        session = ClientSession(**kwargs)
        yoshigall_request = cls(session)
        yoshigall_request.headers.update(yoshigall_request.headers)
        return yoshigall_request

    @staticmethod
    def tag2list(tag: element.Tag):
        result = list(map(lambda i: str(i.contents[0]), tag.findAll("p")))
        return result

    @staticmethod
    def parse_list(
        html: str,
    ) -> dict[str, Union[int, list[dict[str, Union[str, int]]]]]:
        soup = BeautifulSoup(html, "html.parser")

        tbody = soup.find("tbody")
        result = {"total": len(tbody.findAll("tr")), "post_list": []}
        for tr in tbody.findAll("tr", {"class": "ub-content us-post"}):
            gall_tit = tr.find("td", {"class": "gall_tit ub-word"})
            a = gall_tit.findAll("a")

            post_id = tr.find("td", {"class": "gall_num"}).text
            title = a[0].text
            reply = "[0]" if len(a) == 1 else a[1].text
            writer = tr.find("span", {"class": "nickname"}).text
            date = tr.find("td", {"class": "gall_date"}).text
            views = tr.find("td", {"class": "gall_count"}).text
            recommend = tr.find("td", {"class": "gall_recommend"}).text

            post_info = {
                "id": int(post_id),
                "title": title,
                "writer": writer,
                "date": date,
                "recommend": int(recommend),
                "reply": int(reply[1:-1]),
                "views": int(views),
            }
            result["lists"].append(post_info)
        return result

    def parse_post(self, html: str) -> dict[str, str]:
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("meta", {"name": "title"})["content"]
        author = soup.find("meta", {"name": "author"})["content"]
        content_tag = soup.find("div", {"class": "write_div"})
        content = self.tag2list(content_tag)

        return {
            "title": title,
            "author": author,
            "content": content,
        }

    async def get_post(self, post_id: int) -> Optional[dict]:
        resp = await self.get(
            self.url + "/view",
            "text",
            params={"id": "yoshimitsu", "no": str(post_id)},
            headers=self.headers,
        )
        if resp.status != 200:
            return None
        return self.parse_post(resp.returned)

    async def get_todaytip(
        self, page: int
    ) -> Optional[dict[str, Union[int, list[dict[str, Union[str, int]]]]]]:
        resp = await self.get(
            self.url + "/lists",
            "text",
            params={"id": "yoshimitsu", "search_head": "10", "page": str(page)},
            headers=self.headers,
        )
        if resp.status != 200:
            return None
        return self.parse_list(resp.returned)

    async def get_search(
        self,
        keyword: str,
        search_mode: Optional[str] = "search_subject_memo",
        page: Optional[int] = 1,
    ) -> Optional[dict[str, Union[int, list[dict[str, Union[str, int]]]]]]:
        resp = await self.get(
            self.url + "/lists",
            "text",
            params={
                "id": "yoshimitsu",
                "s_type": search_mode,
                "s_keyword": keyword,
                "page": str(page),
            },
        )
        if resp.status != 200:
            return None
        return self.parse_list(resp.returned)
