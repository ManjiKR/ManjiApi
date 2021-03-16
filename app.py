from sanic import Sanic
from sanic_openapi import swagger_blueprint
from rich.logging import RichHandler
import logging

from ManjiApi.api.skill import skill


accessHandler = RichHandler(rich_tracebacks=True)
accessHandler.setFormatter(
    logging.Formatter("%(name)s :\t%(request)s %(message)s %(status)d %(byte)d")
)

genericHandler = RichHandler(rich_tracebacks=True)
genericHandler.setFormatter(logging.Formatter("%(name)s :\t%(message)s"))

logging.getLogger("sanic").setLevel(logging.INFO)

logging.getLogger("sanic.root").addHandler(genericHandler)

errorLogger = logging.getLogger("sanic.error")
errorLogger.propagate = True
errorLogger.addHandler(genericHandler)

accessLogger = logging.getLogger("sanic.access")
accessLogger.propagate = True
accessLogger.addHandler(accessHandler)

app = Sanic(__name__, configure_logging=False)
app.blueprint(skill)
app.blueprint(swagger_blueprint)

app.config.FALLBACK_ERROR_FORMAT = "json"
app.config["API_VERSION"] = "0.1.0"
app.config["API_TITLE"] = "Manji Api"
app.config["API_LISENCE_NAME"] = "Apache 2.0"

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
