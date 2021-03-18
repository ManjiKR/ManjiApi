import aiohttp
from bs4 import BeautifulSoup


class YoshiGall:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        self.view_url = (
            "https://gall.dcinside.com/mgallery/board/view/?id=yoshimitsu&no="
        )
        self.lists_url = "https://gall.dcinside.com/mgallery/board/lists/?id=yoshimitsu&search_head=10&page="

    async def get(self, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as r:
                if r.status != 200:
                    return None
                html = await r.text()
                return html

    async def get_view_by_no(self, no: int):
        url = self.view_url + str(no)
        html = await self.get(url)
        return html
