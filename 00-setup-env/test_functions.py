from functions import xor, count_unique


def test_xor():
    a, b = [0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1]
    assert xor(a, b) == [0, 1, 1, 0, 0, 0]
    a, b = [0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0]
    assert xor(a, b) == [0, 1, 1, 0, 1, 1]


def test_count_unique():
    a, b = [1, 2, 3, 1, 2, 1], [4, 5, 1, 3, 3]
    assert count_unique(a, b) == 5
    a, b = [0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0]
    assert count_unique(a, b) == 2
