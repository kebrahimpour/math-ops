from basic_ops.add.add import add

def test_addition():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0