from src.math_operations import add ,sub


def test_add():
    assert add(2,3) == 5
    assert add(6,3) == 9

def test_sub():
    assert sub(5,4) == 1
    assert sub(5,6) == -1