import pandas as pd


def replace_str(data, col, str1, str2):
    """
    Updates the dataframe to replace string values in the specified column.

    Parameters
    ----------
    data: pd.DataFrame
        The data from which to replace the string value.
    col: str
        The name of the column from which to replace the string value.
    str1: str
        The string to search for.
    str2: str
        The string to replace the old one with.

    Returns
    -------
    data: pd.DataFrame
        An updated dataframe that includes the replaced strings.

    Raises
    ------
    TypeError
        If the input argument data is not of instance pd.DataFrame
    TypeError
        If the input argument col is not of type str
    Exception
        If the input argument col does not exist in the dataframe
    TypeError
        If the input argument str1 is not of type str
    TypeError
        If the input argument str2 is not of type str

    Examples
    --------
    >>> replace_str(pd.DataFrame(["$1","$5","2"], columns=['Numbers']), 'Numbers', '$', '')

    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Please use a DataFrame for the data input parameter.")

    if type(col) is not str:
        raise TypeError("Please use a string for the col input parameter.")

    if not col in data:
        raise Exception("Input for col parameter does not exist in dataframe.")

    if type(str1) is not str:
        raise TypeError("Please use a string for the str1 input parameter.")

    if type(str2) is not str:
        raise TypeError("Please use a string for the str2 input parameter.")

    data[col] = data[col].str.replace(str1, str2, regex=True)
    return data
