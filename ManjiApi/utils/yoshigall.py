import aiohttp
from bs4 import BeautifulSoup, element
import bs4


class YoshiGall:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        self.view_url = (
            "https://gall.dcinside.com/mgallery/board/view/?id=yoshimitsu&no="
        )
        self.lists_url = "https://gall.dcinside.com/mgallery/board/lists/?id=yoshimitsu&search_head=10&page="

    @staticmethod
    def tag2str(tag: bs4.element.Tag):
        """
        지울거
        """
        result = ""
        p = tag.findAll("p")
        for i in p:
            result += str(i)
        return result

    @staticmethod
    def tag2list(tag: bs4.element.Tag):
        result = []
        p = tag.findAll("p")
        for i in p:
            for c in i.contents:
                result.append(c)
        return result

    async def get(self, url: str):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as r:
                if r.status != 200:
                    return None
                html = await r.text()
                return html

    async def get_view_by_no(self, no: int):
        url = self.view_url + str(no)
        html = await self.get(url)
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("meta", {"name": "title"})["content"]
        author = soup.find("meta", {"name": "author"})["content"]
        content_tag = soup.find("div", {"class": "write_div"})
        content_list = self.tag2list(content_tag)
        print(content_list)

        result = {
            "status": 200,
            "content": {
                "title": title,
                "author": author,
                "content": self.tag2str(content_tag),
            },
        }
        return result
