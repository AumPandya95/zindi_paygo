import pandas as pd


class FeatureEncoding:
    def __init__(self, df):
        # TODO: Add modes here and save feature encoding in the objects
        self.features_list = ["MainApplicantGender", "Region", "Occupation", "rateTypeEntity"]
        self.df = df

    def execute(self):
        self.encode(self.df, self.features_list)

    def encode(self, df, features_list):
        for feature in features_list:
            df = self._encode_and_bind(df, feature)
        return df

    @staticmethod
    def _encode_and_bind(df, feature_name):
        dummies = pd.get_dummies(df[[feature_name]])
        res = pd.concat([df, dummies], axis=1)
        res = res.drop([feature_name], axis=1)
        return res
