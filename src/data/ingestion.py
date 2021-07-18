import pandas as pd
import numpy as np
TRAIN_PATH = "../data/raw/Train.csv"
METADATA_PATH = "../data/raw/metadata.csv"
TEST_PATH = "../data/raw/Test.csv"


class DataIngestion:
    def __init__(self, mode="dev"):
        self.mode = mode
        self.train_path = TRAIN_PATH
        self.meta_data_path = METADATA_PATH
        self.test_path = TEST_PATH

    def execute(self, set_seed=0, train_size=0.55):
        metadata = self._read_file(self.meta_data_path)
        if self.mode == "train":
            train_df = self._read_file(self.train_path)
            return self._merge(train_df, metadata)
        elif self.mode == "dev":
            np.random.seed(set_seed)  # Necessary for reproducible results
            train_df = self._read_file(self.train_path)
            merged = self._merge(train_df, metadata)
            mask = np.random.rand(len(merged)) <= train_size
            train, test = merged[mask], merged[~mask]
            return train, test
        elif self.mode == "test":
            test_df = self._read_file(self.test_path)
            return self._merge(test_df, metadata)
        else:
            raise Exception("Incorrect mode passed")

    @staticmethod
    def _merge(df1, df2):
        return df1.merge(df2, how="left", on="ID")

    @staticmethod
    def _read_file(path):
        return pd.read_csv(path, sep=",")
