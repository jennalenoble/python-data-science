def exponent_a_list(numerical_list, exponent=2):
    """
    Creates a new list containing specifiec exponential values of the input list.

    Parameters
    ----------
    numerical_list: list
        The list from which to calculate exponential values from
    exponent: int or float, optional
        The exponent value (the default is 2, which implies the square).

    Returns
    -------
    new_exponent_list: list
        A new list containing the exponential value specified of each
        of the elements from the input list

    Raises
    ------
    TypeError
        If the input argument numerical_list is not of type list

    """
    new_exponent_list = list()

    if type(numerical_list) is not list:
        raise Exception("You are not using a list for the numerical_list input.")

    for number in numerical_list:
        new_exponent_list.append(number**exponent)

    return new_exponent_list
