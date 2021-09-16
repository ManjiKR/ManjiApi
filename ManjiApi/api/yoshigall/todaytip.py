from sanic.response import HTTPResponse, json
from ManjiApi.sanic import ManjiApiRequest
from sanic.blueprints import Blueprint
from sanic.views import HTTPMethodView


yoshigall_todaytip = Blueprint("yoshigall_todaytip", url_prefix="/todaytip")


class YoshiGallTodayTipView(HTTPMethodView):
    async def get(self, request: ManjiApiRequest, page: int) -> HTTPResponse:
        if todaytip := await request.app.ctx.yoshigall_request.get_todaytip(page):
            return json({"status": 200, **todaytip})
        return json({"h": 0})
