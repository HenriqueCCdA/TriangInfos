import pytest

from api.services import Triang


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
def test_triang(a, b, c, area):
    triang = Triang(a, b, c)

    assert triang.area() == pytest.approx(area)


@pytest.mark.integration
@pytest.mark.parametrize(
    "a,b,c,valid",
    [
        (4, 7, 12, False),
        (5, 2, 1, False),
        (3, 4, 5, True),
    ],
)
def test_is_valid(a, b, c, valid):
    triang = Triang(a, b, c)

    assert triang.is_valid() is valid
