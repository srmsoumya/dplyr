from string import ascii_lowercase

import pytest

from dplyr import Dplyr


@pytest.fixture(scope="module")
def blob():
    data = [{"i": i, "k": k, "j": [i, i]} for i, k in enumerate(list(ascii_lowercase))]
    return Dplyr(data)
