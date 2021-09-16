from typing import Any, Optional

from aiohttp.client import ClientSession
from ManjiApi.request.base import BaseRequest


class FrameDataRequest(BaseRequest):
    def __init__(self, session: Optional[ClientSession]) -> None:
        super().__init__(session)

    @property
    def url(self) -> str:
        return "https://raw.githubusercontent.com/ombe1229/yoshimitsu_frame_data/master/yoshimitsu_ko.json"

    @classmethod
    async def setup(cls, **kwargs: Any) -> "FrameDataRequest":
        session = ClientSession(**kwargs)
        framedata_request = cls(session)
        return framedata_request

    async def get_skill_list(self) -> Optional[dict]:
        resp = await self.get(self.url, "json")
        if resp.status != 200:
            return None
        return resp.returned

    async def get_skill_by_num(self, num: int) -> Optional[dict]:
        resp = await self.get_skill_list()
        if len(resp) < num + 1:
            return None
        return resp[num]
