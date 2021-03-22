from sanic import Sanic
from sanic_openapi import swagger_blueprint

from ManjiApi.api.skill import skill
from ManjiApi.api.gallery import gallery


app = Sanic(__name__, configure_logging=False)
app.blueprint(skill)
app.blueprint(gallery)
app.blueprint(swagger_blueprint)

app.config.FALLBACK_ERROR_FORMAT = "json"
app.config["API_VERSION"] = "0.1.2"
app.config["API_TITLE"] = "Manji Api"
app.config["API_LISENCE_NAME"] = "Apache 2.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
