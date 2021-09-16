from sanic.blueprints import Blueprint

from ManjiApi.api.yoshigall.post import yoshigall_post
from ManjiApi.api.yoshigall.todaytip import yoshigall_todaytip
from ManjiApi.api.yoshigall.search import yoshigall_search


yoshigall_endpoint = Blueprint.group(
    yoshigall_post, yoshigall_todaytip, yoshigall_search, url_prefix="/yoshigall"
)
