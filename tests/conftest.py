from pytest import fixture
from sanic.app import Sanic
from sanic_testing import TestManager
from ManjiApi.server import manjiapi


@fixture
def app() -> Sanic:
    TestManager(manjiapi)
    return manjiapi
