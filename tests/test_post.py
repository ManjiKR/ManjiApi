from sanic_testing.manager import TestManager

url = "/api/yoshigall/post/"


def test_post(app: TestManager):
    _, response = app.test_client.get(url + "5139")
    assert response.status == 200


def test_post_404(app: TestManager):
    _, response = app.test_client.get(url + "99999")
    assert response.status == 404
