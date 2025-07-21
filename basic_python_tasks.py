def test_greeting():

    name = "Anna"
    age = 25

    output = ""

    assert output == "Hello, Anna! You're 25 years old."


def test_rectangle():

    a = 10
    b = 20

    perimeter = 0

    assert perimeter == 60


    area = 0

    assert area == 200


def test_circle():

    r = 23

    area = 0

    assert area == 1661.9025137490005

    length = 0

    assert length == 144.51326206513048


def test_random_list():

    l = []

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():

    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = {}

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second