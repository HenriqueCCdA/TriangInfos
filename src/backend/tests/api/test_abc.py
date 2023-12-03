import pytest
from fastapi import status

from api.app import app

URI = app.url_path_for("calc_abc")


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
def test_positive_calc(client, params, area):
    response = client.post(URI, json=params)

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
def test_negative_invalid_triangle(client, params):
    response = client.post(URI, json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    error = body["detail"]

    assert error["msg"] == "There is no triangle with these sides."
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
def test_negative_edges_must_be_gt_zero(client, params):
    response = client.post(URI, json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    error = body["detail"][0]

    assert error["msg"] == "Input should be greater than 0"
    assert error["type"] == "greater_than"
    assert error["input"] == -1
