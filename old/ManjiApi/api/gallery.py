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
    # search_subject_memo
    # search_subject
    # search_memo
    # search_name
    args = request.args
    if not args.get("keyword"):
        return json({"status": 400, "message": "no keyword"})
    resp = await yoshi_gall.search_list(
        args.get("keyword"), args.get("search_mode"), args.get("page")
    )
    return json(resp)
