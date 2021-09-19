from sanic_testing.manager import TestManager

url = "/api/skill/skill/"


def test_skill(app: TestManager):
    _, response = app.test_client.get(url + "0")
    assert response.status == 200


def test_skill_not_found(app: TestManager):
    _, response = app.test_client.get(url + "9999")
    assert response.status == 404
