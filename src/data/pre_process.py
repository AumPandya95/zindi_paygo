from typing import Union

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.decorators import conv_to_df


@conv_to_df
def one_hot_encoding(
        categorical_frame: Union[np.ndarray, pd.DataFrame],
        conv: bool = True
) -> np.array:
    """
    Return the encoded categorical columns.
    Parameters
    ----------
    categorical_frame: np.array
        The categorical features from the train/ test set
    conv: bool
        Whether to convert the encoded array to a dataframe
    Returns
    -------
    encoded_features: np.array
    """
    encoder = OneHotEncoder()
    encoder.fit(categorical_frame)

    final_array = encoder.transform(categorical_frame)

    return final_array
