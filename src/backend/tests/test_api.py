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
def test_negative_invalid_triangle(params):
    response = client.post("/area-abc", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    error = body["detail"]

    assert error["msg"] == "Não existe triangulo com esse lados."
    assert error["type"] == "invalid_triangle"
    assert error["input"] == params


@pytest.mark.integration
@pytest.mark.parametrize(
    "params",
    [
        {"a": -1, "b": 1, "c": 1},
        {"a": 1, "b": -1, "c": 1},
        {"a": 1, "b": 1, "c": -1},
    ],
    ids=[
        "a<0",
        "b<0",
        "c<0",
    ],
)
def test_negative_edges_must_be_gt_zero(params):
    response = client.post("/area-abc", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    error = body["detail"][0]

    assert error["msg"] == "Input should be greater than 0"
    assert error["type"] == "greater_than"
    assert error["input"] == -1


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
def test_negative_invalid_triangle_bh(params):
    response = client.post("/area-bh", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    assert body["detail"][0]["msg"] == "Input should be greater than 0"


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
