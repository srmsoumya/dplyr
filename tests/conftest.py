import pytest
from dplyr import Dplyr
from string import ascii_lowercase

@pytest.fixture(scope="module")
def blob():
    data = [{'i': i, 'k': k, 'j': [i,i]} for i,k in enumerate(list(ascii_lowercase))]
    return Dplyr(data)