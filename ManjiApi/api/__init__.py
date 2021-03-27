from sanic import Blueprint
from sanic_openapi import swagger_blueprint

from ManjiApi.api.gallery import gallery
from ManjiApi.api.skill import skill

bp_group = Blueprint.group(gallery, skill, swagger_blueprint, url_prefix="/api")
