import pandas as pd
from replace_str import replace_str


def test_replace_str():
    helper_data = pd.DataFrame(["$7", "8$", "9"], columns=["Numbers"])
    assert isinstance(replace_str(helper_data, "Numbers", "$", ""), pd.DataFrame)
    assert replace_str(helper_data, "Numbers", "$", "").equals(
        pd.DataFrame(["7", "8", "9"], columns=["Numbers"])
    )
    assert replace_str(helper_data, "Numbers", "$", "").shape == (3, 1)
