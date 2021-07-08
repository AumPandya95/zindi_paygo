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
    def one_hot_encoding(self, categorical_frame: Union[np.ndarray, pd.DataFrame], mode: str = "train",
                         conv: Optional[bool] = True, drop: Optional[str] = None, handle_unknown: str = "ignore"
                         ) -> Tuple[Union[np.ndarray, pd.DataFrame], Optional[EncoderType]]:
        """
        Return the encoded categorical columns.
        Parameters
        ----------
        categorical_frame: np.array
            The categorical features from the train/ test set
        mode: str :: ["train", "test", "validation"]
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
        if mode in ("train", "dev"):
            self.encoder_obj = OneHotEncoder(drop=drop, handle_unknown=handle_unknown)
            self.encoder_obj.fit(categorical_frame)
            final_array = self.encoder_obj.transform(categorical_frame).toarray()
            return final_array
        else:
            if self.encoder_obj:
                final_array = self.encoder_obj.transform(categorical_frame).toarray()
                return final_array, self.encoder_obj

            raise Exception(
                "Encoder Object is empty"
            )

#
# if __name__ == "__main__":
#     # frame = pd.DataFrame([[1, 2, 3, 4], [5, 2, 10, 14]], columns=['a', 'b', 'c', 'd'])
#     frame = np.array([[1, 2, 3, 4], [5, 2, 10, 14]])
#     fin, enc = one_hot_encoding(categorical_frame=frame, conv=True)
#     print(list(fin.columns))
#     # 1 5 2 3 10 4 14
#
#     fin, enc = one_hot_encoding(categorical_frame=frame, conv=False)
#     print(fin)
#
#     fr, en = one_hot_encoding(categorical_frame=np.array([[6, 2, 10, 14],
#                                                           [1, 2, 3, 14]]),
#                               mode='test',
#                               encoder_obj=enc,
#                               conv=True)
#     print(fr)
