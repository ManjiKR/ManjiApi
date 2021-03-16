from sanic import Blueprint
from sanic.response import json

from ManjiApi.utils.skill_data_requester import YoshiRequester

requester = YoshiRequester()
skill = Blueprint(__name__, url_prefix="/skill")


@skill.get("/all")
async def all_skills(request):
    resp = await requester.get_all_skills()
    return json(resp, 200)


@skill.get("/<num:int>")
async def get_skill(request, num):
    resp = await requester.get_skill_by_num(num)
    if resp:
        return json({"info": resp}, 200)
    else:
        return json({"status": 400, "message": "number is too big (max is 411)"}, 400)