from sanic import Blueprint

from ManjiApi.api.gallery import gallery
from ManjiApi.api.skill import skill

bp_group = Blueprint.group(gallery, skill, url_prefix="/api")
