# from typing import Union, Optional, Tuple
from typing import Union, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.decorators import conv_to_df

EncoderType = OneHotEncoder


class FeatureEncoding:
    def __init__(self):
        self.encoder_obj = None

    @conv_to_df
    def one_hot_encoding(
            self,
            categorical_frame: Union[np.ndarray, pd.DataFrame],
            type_of_data: str = "train",
            conv: Optional[bool] = True,
            drop: Optional[str] = None,
            handle_unknown: str = "ignore"
    ) -> Tuple[Union[np.ndarray, pd.DataFrame], Optional[EncoderType]]:
        """
        Return the encoded categorical columns.
        Parameters
        ----------
        categorical_frame: np.array
            The categorical features from the train/ test set
        type_of_data: str :: ["train", "test", "validation"]
            if data is train then the encoder will be fit on the data
        conv: bool
            Whether to convert the encoded array to a dataframe
        drop: str :: [None, "first"]
            Specifies a methodology to use to drop one of the categories per feature.
        handle_unknown: str :: ["ignore", "error"]
            Whether to raise an error or ignore if an unknown categorical feature is present during transform.
        Returns
        -------
        encoded_features: np.array
        """
        if type_of_data == "train":
            self.encoder_obj = OneHotEncoder(drop=drop, handle_unknown=handle_unknown)
            self.encoder_obj.fit(categorical_frame)
            final_array = self.encoder_obj.transform(categorical_frame).toarray()

            return final_array
        else:
            if self.encoder_obj:
                final_array = self.encoder_obj.transform(categorical_frame).toarray()
                return final_array
            else:
                raise Exception(
                    "No fitted encoder object provided to transform the test/ validation data set."
                )
