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
    "params, area",
    [
        ({"a": 3, "b": 4, "c": 5}, 6.0),
        ({"a": 7, "b": 9, "c": 14}, 26.8328),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_positive_calc(params, area):
    response = client.post("/area-abc", json=params)

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["area"] == pytest.approx(area)


@pytest.mark.integration
@pytest.mark.parametrize(
    "params",
    [
        {"a": 4, "b": 7, "c": 12},
        {"a": 5, "b": 2, "c": 1},
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_negative_invalid_triangule(params):
    response = client.post("/area-abc", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    assert body["detail"] == "Não existe triangulo com esse lados."


@pytest.mark.integration
@pytest.mark.parametrize(
    "params, area",
    [
        ({"b": 3, "h": 4}, 6.0),
        ({"b": 5, "h": 5}, 12.5),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_positive_area_bh(params, area):
    response = client.post("/area-bh", json=params)

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["area"] == pytest.approx(area)


@pytest.mark.integration
@pytest.mark.parametrize(
    "params",
    [
        ({"b": -3, "h": 4}),
        ({"b": 5, "h": -5}),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_negative_invalid_triangule_bh(params):
    response = client.post("/area-bh", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    assert body["detail"] == "Não existe triangulo com esse lados."


@pytest.mark.integration
@pytest.mark.parametrize(
    "params, perimetro",
    [
        ({"a": 3, "b": 4, "c": 5}, 12),
        ({"a": 7, "b": 9, "c": 14}, 30),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_positive_perimetro(params, perimetro):
    response = client.post("/perimetro", json=params)

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["perimetro"] == pytest.approx(perimetro)
