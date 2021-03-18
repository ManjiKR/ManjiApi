from sanic import Blueprint
from sanic.response import text

from ManjiApi.utils.yoshigall import YoshiGall

yoshi_gall = YoshiGall()
gallery = Blueprint(__name__, url_prefix="/gallery")


@gallery.get("/view/<no:int>")
async def get_post_info(request, no):
    html = await yoshi_gall.get_view_by_no(no)
    return text(html)
