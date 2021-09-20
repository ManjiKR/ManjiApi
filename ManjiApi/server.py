from ManjiApi.response import Response
from ManjiApi.sanic import ManjiApi
from ManjiApi import __version__

from ManjiApi.request.base import BaseRequest
from ManjiApi.request.frame_data import FrameDataRequest
from ManjiApi.request.yoshimitsu_gallery import YoshiGallRequest

from ManjiApi.api import api_endpoint

from aiohttp.client import ClientSession
from asyncio.events import AbstractEventLoop
from sanic.app import Sanic
from sanic_openapi import openapi3_blueprint


manjiapi = Sanic("ManjiApi")
manjiapi.blueprint(api_endpoint)
manjiapi.blueprint(openapi3_blueprint)


@manjiapi.main_process_start
async def start(manjiapi: ManjiApi, loop: AbstractEventLoop) -> None:
    manjiapi.config.FALLBACK_ERROR_FORMAT = "json"
    manjiapi.config.API_VERSION = __version__
    manjiapi.config.API_TITLE = "ManjiApi"
    manjiapi.config.API_DESCRIPTION = "Tekken 7 yoshimitsu api"
    manjiapi.config.API_LICENSE_NAME = "Apache 2.0"
    manjiapi.ctx.base_request = BaseRequest(ClientSession())
    manjiapi.ctx.yoshigall_request = await YoshiGallRequest.setup()
    manjiapi.ctx.framedata_request = await FrameDataRequest.setup()
    manjiapi.ctx.response = Response


@manjiapi.main_process_stop
async def stop(manjiapi: ManjiApi, loop: AbstractEventLoop) -> None:
    await manjiapi.ctx.base_request.close()
    await manjiapi.ctx.yoshigall_request.close()
    await manjiapi.ctx.framedata_request.close()
