import pytest
from fastapi import status


@pytest.mark.integration
def test_root(client):
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Api is OK!"}
