from sanic.views import HTTPMethodView
from ManjiApi.sanic import ManjiApiRequest
from sanic.blueprints import Blueprint
from sanic.response import HTTPResponse, json
from sanic_openapi.openapi3.openapi import summary, tag


skill_skill = Blueprint("skill_skill", url_prefix="/skill")


class SkillSkillView(HTTPMethodView):
    @summary("Get skill data by number")
    @tag("skill")
    async def get(self, request: ManjiApiRequest, num: int) -> HTTPResponse:
        if skill_info := await request.app.ctx.framedata_request.get_skill_by_num(num):
            return json({"status": 200, **skill_info})
        return request.app.ctx.response.not_found


skill_skill.add_route(SkillSkillView.as_view(), "/<num:int>")
