from ManjiApi.sanic import ManjiApi

from ManjiApi.request.base import BaseRequest
from ManjiApi.request.frame_data import FrameDataRequest
from ManjiApi.request.yoshimitsu_gallery import YoshiGallRequest

from ManjiApi.api import api_endpoint

from aiohttp.client import ClientSession
from asyncio.events import AbstractEventLoop
from sanic.app import Sanic


manjiapi = Sanic("ManjiApi")
manjiapi.blueprint(api_endpoint)


@manjiapi.main_process_start
async def start(manjiapi: ManjiApi, loop: AbstractEventLoop) -> None:
    manjiapi.ctx.base_request = BaseRequest(ClientSession())
    manjiapi.ctx.yoshigall_request = await YoshiGallRequest.setup()
    manjiapi.ctx.framedata_request = await FrameDataRequest.setup()


@manjiapi.main_process_stop
async def stop(manjiapi: ManjiApi, loop: AbstractEventLoop) -> None:
    await manjiapi.ctx.base_request.close()
    await manjiapi.ctx.yoshigall_request.close()
    await manjiapi.ctx.framedata_request.close()
