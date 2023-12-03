import pytest
from fastapi import status

from api.app import app

URI = app.url_path_for("index")


@pytest.mark.integration
def test_root(client):
    response = client.get(URI)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Api is OK!"}
