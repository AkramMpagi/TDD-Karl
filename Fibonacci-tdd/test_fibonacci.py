from fibonacci import fibonacci


def test_fibonacci_1():
    assert fibonacci(1) == [0]


def test_fibonacci_2():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_3():
    assert fibonacci(3) == [0, 1, 1]

def test_fibonacci_20():
    assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]