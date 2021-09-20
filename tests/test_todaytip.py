from sanic_testing.manager import TestManager


url = "/api/yoshigall/todaytip"


def test_todaytip(app: TestManager):
    _, response = app.test_client.get(url + "/1")
    assert response.status == 200
