from dplyr import Dplyr

def test_can_collect_all(blob):
    assert len(blob.pipe(lambda x: x['i'] < 26)) == 26

def test_can_collect_half(blob):
    assert len(blob.pipe(lambda x: x['i'] < 5)) == 5

def test_can_collect_none(blob):
    assert len(blob.pipe(lambda x: x['i'] < 0)) == 0