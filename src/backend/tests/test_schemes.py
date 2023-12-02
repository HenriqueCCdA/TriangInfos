import pytest
from pydantic import ValidationError

from api.schemes import BaseHeight, Edges


def test_edges_must_be_positive():
    with pytest.raises(ValidationError):
        Edges(a=-1.0, b=1.0, c=1.0)


def test_bg_must_be_positive():
    with pytest.raises(ValidationError):
        BaseHeight(b=-1.0, h=1.0)
