from square import get_square, get_add

def test_get_square():
    a = 5
    res = get_square(a)

    assert res == 25

def test_get_add():
    a = 5
    res = get_add(a)

    assert res == 10