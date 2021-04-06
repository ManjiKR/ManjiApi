from sanic import Sanic

from ManjiApi.api import bp_group


app = Sanic(__name__, configure_logging=False)
app.blueprint(bp_group)

app.config.FALLBACK_ERROR_FORMAT = "json"
app.config["API_VERSION"] = "0.3.5"
app.config["API_TITLE"] = "Manji Api"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
