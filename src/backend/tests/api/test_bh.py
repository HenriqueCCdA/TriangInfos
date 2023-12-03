import pytest
from fastapi import status


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
def test_positive_area_bh(client, params, area):
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
def test_negative_invalid_triangle_bh(client, params):
    response = client.post("/area-bh", json=params)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    body = response.json()

    assert body["detail"][0]["msg"] == "Input should be greater than 0"
