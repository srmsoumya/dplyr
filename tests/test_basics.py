from dplyr import Dplyr

def test_empty_list():
    assert len(Dplyr([])) == 0