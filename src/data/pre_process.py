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
        encoder = OneHotEncoder(handle_unknown="ignore")
        encoder.fit(categorical_frame)

        final_array = encoder.transform(categorical_frame).toarray()

        return final_array, encoder
    else:
        if fitted_encoder:
            final_array = fitted_encoder.transform(categorical_frame).toarray()

            return final_array, fitted_encoder
        else:
            raise Exception(
                "No fitted encoder object provided to transform the test/ validation data set."
            )


if __name__ == "__main__":
    # frame = pd.DataFrame([[1, 2, 3, 4], [5, 2, 10, 14]], columns=['a', 'b', 'c', 'd'])
    frame = np.array([[1, 2, 3, 4], [5, 2, 10, 14]])
    fin, enc = one_hot_encoding(categorical_frame=frame, conv=True)
    print(list(fin.columns))
    # 1 5 2 3 10 4 14

    fin, enc = one_hot_encoding(categorical_frame=frame, conv=False)
    print(fin)

    fr, en = one_hot_encoding(categorical_frame=np.array([[6, 2, 10, 14],
                                                          [1, 2, 3, 14]]),
                              type_of_data='test',
                              fitted_encoder=enc,
                              conv=True)
    print(fr)
