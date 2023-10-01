from lab_1_2_1 import count_operations

def test_example_1():
    assert count_operations([2, 2]) == 2

def test_example_2():
    assert count_operations([4, 4, 5, 5]) == 5

def test_example_3():
    assert count_operations([4, 2, 4]) == 6
