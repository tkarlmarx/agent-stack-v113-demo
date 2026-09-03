from main import add


def test_add():
    assert add(2, 3) == 5


def test_add_is_commutative():
    assert add(2, 3) == add(3, 2)
