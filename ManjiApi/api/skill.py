from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

from ManjiApi.utils.skill_data import SkillData

skill_data = SkillData()
skill = Blueprint(__name__, url_prefix="/skill")


@skill.get("/all")
@doc.description("모든 스킬 정보를 불러옵니다.")
async def all_skills(request):
    resp = await skill_data.get_all_skills()
    return json(resp, 200)


@skill.get("/<num:int>")
@doc.description("번호에 해당하는 스킬 정보를 불러옵니다.")
async def get_skill(request, num):
    resp = await skill_data.get_skill_by_num(num)
    if resp:
        return json({"status": 200, "info": resp}, 200)
    else:
        return json({"status": 400, "message": "number is too big (max is 411)"}, 400)
