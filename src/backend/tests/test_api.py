import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


@pytest.mark.integration
def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Api is OK!"}


@pytest.mark.integration
@pytest.mark.parametrize(
    "a,b,c, area",
    [
        (3, 4, 5, 6.0),
        (7, 9, 14, 26.8328),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_positive_calc(a, b, c, area):
    response = client.post("/area", json={"a": a, "b": b, "c": c})

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["area"] == pytest.approx(area)


@pytest.mark.integration
@pytest.mark.parametrize(
    "a,b,c",
    [
        (4, 7, 12),
        (5, 2, 1),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_negative_invalid_triangule(a, b, c):
    response = client.post("/area", json={"a": a, "b": b, "c": c})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    assert body["detail"] == "Não existe triangulo com esse lados."
