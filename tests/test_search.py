from sanic_testing.manager import TestManager


url = "/api/yoshigall/search"


def test_search(app: TestManager):
    _, response = app.test_client.get(url + "?keyword=투투")
    assert response.status == 200


def test_search_no_keyword(app: TestManager):
    _, response = app.test_client.get(url)
    assert response.status == 400
