from sanic.blueprints import Blueprint

from ManjiApi.api.yoshigall import yoshigall_endpoint
from ManjiApi.api.skill import skill_endpoint

api_endpoint = Blueprint.group(yoshigall_endpoint, skill_endpoint, url_prefix="/api")
