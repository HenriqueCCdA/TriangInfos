import pytest
from fastapi import status

from api.app import app

URI = app.url_path_for("perimetro")


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
def test_positive_perimetro(client, params, perimetro):
    response = client.post(URI, json=params)

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["perimetro"] == pytest.approx(perimetro)


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
def test_negative_edges_must_be_gt_zero(client, params):
    response = client.post(URI, json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    error = body["detail"][0]

    assert error["msg"] == "Input should be greater than 0"
    assert error["type"] == "greater_than"
    assert error["input"] == -1
