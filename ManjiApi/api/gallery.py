from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

from ManjiApi.utils.yoshigall import YoshiGall

yoshi_gall = YoshiGall()
gallery = Blueprint(__name__, url_prefix="/gallery")


@gallery.get("/view/<no:int>")
@doc.description("번호에 해당하는 요마갤 글을 불러옵니다.")
async def get_post_info(request, no):
    resp = await yoshi_gall.get_view_by_no(no)
    return json(resp)


@gallery.get("/tt/lists/<page:int>")
@doc.description("요마갤 하루팁 말머리 리스트를 불러옵니다.")
async def get_lists(request, page):
    resp = await yoshi_gall.get_lists_page(page)
    return json(resp)
