from sanic.blueprints import Blueprint

from ManjiApi.api.yoshigall import yoshigall_endpoint


api_endpoint = Blueprint.group(yoshigall_endpoint, url_prefix="/api")
