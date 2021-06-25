from typing import Union, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.decorators import conv_to_df

EncoderType = OneHotEncoder


@conv_to_df
def one_hot_encoding(
        categorical_frame: Union[np.ndarray, pd.DataFrame],
        type_of_data: str = "train",
        fitted_encoder: Optional[EncoderType] = None,
        conv: Optional[bool] = True
) -> Tuple[Union[np.ndarray, pd.DataFrame], Optional[EncoderType]]:
    """
    Return the encoded categorical columns.
    Parameters
    ----------
    categorical_frame: np.array
        The categorical features from the train/ test set
    type_of_data: str :: ["train", "test", "validation"]
        if data is train then the encoder will be fit on the data
    fitted_encoder: OneHotEncoder
        if type_of_data is not "train" then the fitted_encoder is required to transform "test" or "validation" data sets
    conv: bool
        Whether to convert the encoded array to a dataframe
    Returns
    -------
    encoded_features: np.array
    """
    if type_of_data == "train":
        encoder = OneHotEncoder()
        encoder.fit(categorical_frame)

        final_array = encoder.transform(categorical_frame)

        return final_array, encoder
    else:
        if fitted_encoder:
            final_array = fitted_encoder.transform(categorical_frame)

            return final_array
        else:
            raise Exception(
                "No fitted encoder object provided to transform the test/ validation data set."
            )

