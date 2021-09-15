from ManjiApi.request.yoshimitsu_gallery import YoshiGallRequest
from aiohttp.client import ClientSession
from ManjiApi.request.base import BaseRequest
from asyncio.events import AbstractEventLoop
from sanic import Sanic


manjiapi = Sanic("ManjiApi")


@manjiapi.main_process_start
async def start(manjiapi, loop: AbstractEventLoop) -> None:
    manjiapi.ctx.base_request = BaseRequest(ClientSession())
    manjiapi.ctx.yoshigall_request = await YoshiGallRequest.setup()


@manjiapi.main_process_stop
async def stop(manjiapi, loop: AbstractEventLoop) -> None:
    await manjiapi.ctx.base_request.close()
    await manjiapi.ctx.yoshigall_request.close()
