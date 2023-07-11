from exponent_a_list import exponent_a_list

def test_exponent_a_list():
    assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
    assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
    assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output exponent = 3"
    assert exponent_a_list([], 3) == [], "incorrect output for empty list"
    assert exponent_a_list([1, 2, 3], 0) == [1, 1, 1], "incorrect output exponent 0"
    assert exponent_a_list([1, 2], -2) == [1, 0.25], "incorrect output for a negative exponent"