import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class FeatureEncoding:
    def __init__(self, cat_df, mode="train", encoding_model=None):
        # TODO: Add modes here and save feature encoding in the objects
        self.features_list = ["MainApplicantGender", "Region", "Occupation", "rateTypeEntity"]
        self.cat_df = cat_df
        self.mode = mode
        self.encoding_model = encoding_model

    def one_hot_encoding(self, encoder):
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

    # def execute(self):
    #     if self.mode in ("dev", "train"):
    #         enc = OneHotEncoder(handle_unknown='ignore')
    #         enc.fit(self.df)
    #
    #     self.encode(self.df, self.features_list)
    #
    # def encode(self, df, features_list):
    #     for feature in features_list:
    #         df = self._encode_and_bind(df, feature)
    #     return df
    #
    # @staticmethod
    # def _encode_and_bind(df, feature_name):
    #     dummies = pd.get_dummies(df[[feature_name]])
    #     res = pd.concat([df, dummies], axis=1)
    #     res = res.drop([feature_name], axis=1)
    #     return res
