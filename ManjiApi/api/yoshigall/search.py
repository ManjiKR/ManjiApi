from ManjiApi.sanic import ManjiApiRequest
from sanic.views import HTTPMethodView
from sanic.blueprints import Blueprint
from sanic.response import HTTPResponse, json


yoshigall_search = Blueprint("yoshigall_search", url_prefix="/search")


class YoshiGallSearchView(HTTPMethodView):
    async def get(self, request: ManjiApiRequest) -> HTTPResponse:
        keyword = request.args.get("keyword")
        search_mode = request.args.get("search_mode")
        page = request.args.get("page")
        if search_result := await request.app.ctx.yoshigall_request.get_search(
            keyword, search_mode, page
        ):  # TODO: Optional
            return json({"status": 200, **search_result})
        return request.app.ctx.response.not_found


yoshigall_search.add_route(YoshiGallSearchView.as_view(), "")
