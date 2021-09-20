from sanic.views import HTTPMethodView
from ManjiApi.sanic import ManjiApiRequest
from sanic.blueprints import Blueprint
from sanic.response import HTTPResponse, json
from sanic_openapi.openapi3.openapi import summary, tag


yoshigall_post = Blueprint("yoshigall_post", url_prefix="/post")


class YoshiGallPostView(HTTPMethodView):
    @summary("Get post data")
    @tag("yoshigall")
    async def get(self, request: ManjiApiRequest, post_id: int) -> HTTPResponse:
        if post_info := await request.app.ctx.yoshigall_request.get_post(post_id):
            return json({"status": 200, **post_info})
        return request.app.ctx.response.not_found


yoshigall_post.add_route(YoshiGallPostView.as_view(), "/<post_id:int>")
