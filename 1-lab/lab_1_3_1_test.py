from lab_1_3_1 import count_seats_prices


def test_example_1():
    assert count_seats_prices([
        (1, 1, 1000),
        (1, 1, 1000),
        (1, 2, 2000),
        (1, 2, 3000)
        ]) == [
            (1, 1, 1),
            (1, 2, 2)
        ]


def test_example_2():
    assert count_seats_prices([
        (1, 1, 1000),
        (1, 1, 2000),
        (1, 1, 2000)
        ]) == [
            (1, 1, 2)
        ]
