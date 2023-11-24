import pytest

from api.services import Triang3Edges, TriangBase, TriangBaseHeight


def test_triang_abc():
    msg = (
        "Can't instantiate abstract class TriangBase without an implementation for abstract methods 'area', 'is_valid'"
    )

    with pytest.raises(TypeError, match=msg):
        TriangBase()


@pytest.mark.integration
@pytest.mark.parametrize(
    "a,b,c,area",
    [
        (3, 4, 5, 6.0),
        (7, 9, 14, 26.8328),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_triang_3edges_area(a, b, c, area):
    triang = Triang3Edges(a, b, c)

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
def test_is_valid_3edges(a, b, c, valid):
    triang = Triang3Edges(a, b, c)

    assert triang.is_valid() is valid


@pytest.mark.integration
@pytest.mark.parametrize(
    "b,h,area",
    [
        (2, 2, 2.0),
        (4, 5, 10.0),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_triang_bh_area(b, h, area):
    triang = TriangBaseHeight(b, h)

    assert triang.area() == pytest.approx(area)


@pytest.mark.integration
@pytest.mark.parametrize(
    "b,h,valid",
    [
        (4, -7, False),
        (-5, 2, False),
        (3, 4, True),
    ],
)
def test_is_valid_bh(b, h, valid):
    triang = TriangBaseHeight(b, h)

    assert triang.is_valid() is valid


@pytest.mark.integration
@pytest.mark.parametrize(
    "a,b,c,perimetro",
    [
        (3, 4, 5, 12.0),
        (7, 9, 14, 30.0),
    ],
    ids=[
        "triag1",
        "triag2",
    ],
)
def test_triang_3edges_perimetro(a, b, c, perimetro):
    triang = Triang3Edges(a, b, c)

    assert triang.perimetro() == pytest.approx(perimetro)
