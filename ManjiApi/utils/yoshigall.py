import aiohttp
from bs4 import BeautifulSoup, element
import bs4


class YoshiGall:
    @staticmethod
    async def request(path: str, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        url = "https://gall.dcinside.com/mgallery/board" + path
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, **kwargs) as r:
                if r.status != 200:
                    return None
                html = await r.text()
                return html

    @staticmethod
    def tag2list(tag: bs4.element.Tag):
        result = []
        p = tag.findAll("p")
        for i in p:
            for c in i.contents:
                result.append(str(c))
        return result

    @staticmethod
    def parse_lists(html: str):
        soup = BeautifulSoup(html, "html.parser")

        tbody = soup.find("tbody")
        result = {"status": 200, "total": len(tbody.findAll("tr")), "lists": []}
        for tr in tbody.findAll("tr", {"class": "ub-content us-post"}):
            gall_tit = tr.find("td", {"class": "gall_tit ub-word"})
            a = gall_tit.findAll("a")

            post_id = tr.find("td", {"class": "gall_num"}).text
            title = a[0].text
            reply = "[0]" if len(a) == 1 else a[1].text
            writer = tr.find("span", {"class": "nickname in"}).text
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

    async def request_view(self, no: int):
        return await self.request("/view", params={"id": "yoshimitsu", "no": str(no)})

    async def request_list(self, page: int):
        return await self.request(
            "/lists",
            params={"id": "yoshimitsu", "search_head": "10", "page": str(page)},
        )

    async def request_search(self, keyword: str, search_mode: str, page: int):
        return await self.request(
            "/lists",
            params={
                "id": "yoshimitsu",
                "s_type": search_mode,
                "s_keyword": keyword,
                "page": str(page),
            },
        )

    async def post_view(self, no: int):
        html = await self.request_view(no)
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("meta", {"name": "title"})["content"]
        author = soup.find("meta", {"name": "author"})["content"]
        content_tag = soup.find("div", {"class": "write_div"})
        content = self.tag2list(content_tag)

        result = {
            "status": 200,
            "content": {
                "title": title,
                "author": author,
                "content": content,
            },
        }
        return result

    async def tt_list(self, page: int):
        html = await self.request_list(page)
        return self.parse_lists(html)

    async def search_list(self, keyword: str, search_mode: str, page: int):
        html = await self.request_search(keyword, search_mode, page)
        return self.parse_lists(html)
