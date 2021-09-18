from typing import Any, Literal, Optional
from aiohttp import ClientSession
from dataclasses import dataclass


@dataclass
class Response:
    status: int
    returned: Any


class BaseRequest:
    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self.session = session

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    @property
    def user_agent(self) -> str:
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"

    async def request(
        self,
        method: Literal["GET", "POST"],
        url: str,
        return_method: Literal["json", "text"],
        **kwargs: Any,
    ) -> Any:
        async with self.session.request(method, url, **kwargs) as response:
            return Response(
                response.status,
                await response.json(content_type=None)
                if return_method == "json"
                else await response.text(),
            )

    async def get(
        self, url: str, return_method: Literal["json", "text"], **kwargs
    ) -> Response:
        return await self.request("GET", url, return_method, **kwargs)
