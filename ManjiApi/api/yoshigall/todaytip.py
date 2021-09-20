from sanic.response import HTTPResponse, json
from ManjiApi.sanic import ManjiApiRequest
from sanic.blueprints import Blueprint
from sanic.views import HTTPMethodView
from sanic_openapi.openapi3.openapi import summary, tag


yoshigall_todaytip = Blueprint("yoshigall_todaytip", url_prefix="/todaytip")


class YoshiGallTodayTipView(HTTPMethodView):
    @summary("Get todaytip list")
    @tag("yoshigall")
    async def get(self, request: ManjiApiRequest, page: int) -> HTTPResponse:
        if todaytip := await request.app.ctx.yoshigall_request.get_todaytip(page):
            return json({"status": 200, **todaytip})
        return request.app.ctx.response.not_found


yoshigall_todaytip.add_route(YoshiGallTodayTipView.as_view(), "/<page:int>")
