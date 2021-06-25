import functools

import numpy as np
import pandas as pd


def conv_to_df(func):
    @functools.wraps(func)
    def check_and_return_df(*args, **kwargs):
        frame = kwargs.get("categorical_frame")
        encoded_arr, encoder = func(*args, **kwargs)
        # two pipelines for pd.DataFrame and np.ndarray
        if isinstance(frame, pd.DataFrame):
            enc_columns = []
            for column in frame.columns:
                # Each column's categories need to be sorted as this is how OHE is implemented
                enc_columns.extend(sorted(frame[column].unique()))
            encoded_arr = pd.DataFrame(encoded_arr, columns=enc_columns)
        else:  # if isinstance(frame, np.ndarray)
            if kwargs.get("conv"):
                enc_columns = []
                for column_idx in range(frame.shape[1]):
                    enc_columns.extend(sorted(np.unique(frame[:, column_idx], axis=0)))
                encoded_arr = pd.DataFrame(encoded_arr, columns=enc_columns)

        return encoded_arr, encoder

    return check_and_return_df
