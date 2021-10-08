import pytest


@pytest.mark.parametrize("n,expected", [(0, 0), (5, 5), (10, 10), (26, 26), (1000, 26)])
def test_head_tail(blob, n, expected):
    assert len(blob.head(n)) == expected
    assert len(blob.tail(n)) == expected
