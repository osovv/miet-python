from lab_1_1_1 import remove_virus

def test_example_1():
    assert remove_virus('python', 'py') == 'thon'

def test_example_2():
    assert remove_virus('tuple', 'Up') == 'tle'

def test_example_3():
    assert remove_virus('Queues', 'ue') == 'Qs'
