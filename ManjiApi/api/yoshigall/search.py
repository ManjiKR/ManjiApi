from ManjiApi.sanic import ManjiApiRequest
from sanic.views import HTTPMethodView
from sanic.blueprints import Blueprint
from sanic.response import HTTPResponse, json
from sanic_openapi.openapi3.openapi import summary, tag


yoshigall_search = Blueprint("yoshigall_search", url_prefix="/search")


class YoshiGallSearchView(HTTPMethodView):
    @summary("Get search result list")
    @tag("yoshigall")
    async def get(self, request: ManjiApiRequest) -> HTTPResponse:
        if keyword := request.args.get("keyword"):
            if search_result := await request.app.ctx.yoshigall_request.get_search(
                keyword,
                request.args.get("search_mode"),
                request.args.get("page"),
            ):
                return json({"status": 200, **search_result})
            return request.app.ctx.response.not_found
        return json({"status": 400, "message": "no keyword"}, 400)


yoshigall_search.add_route(YoshiGallSearchView.as_view(), "")
