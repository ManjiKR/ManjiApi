from sanic import Blueprint
from sanic.response import json

from ManjiApi.utils.yoshigall import YoshiGall

yoshi_gall = YoshiGall()
gallery = Blueprint(__name__, url_prefix="/gallery")


@gallery.get("/view/<no:int>")
async def get_post_info(request, no):
    resp = await yoshi_gall.post_view(no)
    return json(resp)


@gallery.get("/tt/lists/<page:int>")
async def get_lists(request, page):
    resp = await yoshi_gall.tt_list(page)
    return json(resp)


@gallery.get("/search")
async def get_search(request):
    print(request.args)
