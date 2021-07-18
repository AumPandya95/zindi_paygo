import os
from pathlib import Path

import pandas as pd
import numpy as np

ROOT_PATH = str(Path(__file__)).split('src')[0]
TRAIN_PATH = os.path.join(ROOT_PATH, "data/raw/Train.csv")
METADATA_PATH = os.path.join(ROOT_PATH, "data/raw/metadata.csv")
TEST_PATH = os.path.join(ROOT_PATH, "data/raw/Test.csv")


def split_data(train, target, set_seed=10):
        from sklearn.model_selection import train_test_split
        seed=set_seed
        X_train, X_test, y_train, y_test = train_test_split(train, target, test_size=0.45, random_state=seed)

        return X_train, X_test, y_train, y_test


class DataIngestion:
    def __init__(self, mode="dev"):
        self.mode = mode
        self.train_path = TRAIN_PATH
        self.meta_data_path = METADATA_PATH
        self.test_path = TEST_PATH

    @staticmethod
    def _merge(df1, df2):
        return df1.merge(df2, how="left", on="ID")

    @staticmethod
    def _read_file(path):
        return pd.read_csv(path, sep=",")

    def execute(self, train_size=0.55):
        metadata = self._read_file(self.meta_data_path)
        if self.mode == "train":
            train_df = self._read_file(self.train_path)

            return self._merge(train_df, metadata)

        elif self.mode == "dev":
            np.random.seed(set_seed)  # Necessary for reproducible results
            train_df = self._read_file(self.train_path)
            merged = self._merge(train_df, metadata)

            return merged

        elif self.mode == "test":
            test_df = self._read_file(self.test_path)

            return self._merge(test_df, metadata)

        else:
            raise Exception("Incorrect mode passed")
