from sanic_testing.manager import TestManager

url = "/api/skill/all_skills"


def test_all_skills(app: TestManager):
    _, response = app.test_client.get(url)
    assert response.status == 200
