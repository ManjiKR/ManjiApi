from sanic.views import HTTPMethodView
from ManjiApi.sanic import ManjiApiRequest
from sanic.blueprints import Blueprint
from sanic.response import HTTPResponse, json


skill_all_skills = Blueprint("skill_all_skills", url_prefix="/all_skills")


class SkillAllSkillsView(HTTPMethodView):
    async def get(self, request: ManjiApiRequest) -> HTTPResponse:
        if skill_list := await request.app.ctx.framedata_request.get_skill_list():
            return json({"status": 200, "skills": skill_list})
        return request.app.ctx.response.not_found


skill_all_skills.add_route(SkillAllSkillsView.as_view(), "")
