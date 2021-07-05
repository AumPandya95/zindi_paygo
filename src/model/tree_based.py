from typing import Union

import numpy as np
import pandas as pd
import xgboost as xgb


class ModelXgBoost:
    def __init__(
            self,
            train_array: Union[np.ndarray, pd.DataFrame],
            train_target: Union[np.ndarray, pd.DataFrame],

    ) -> None:
        self.train_array = train_array
        self.train_target = train_target
        self.trained_model = None

    def train_model(
            self,
            **tuned_params
    ) -> None:
        """Train the model on given data using Scikit-learn API of XGBoost."""
        model = xgb.XGBRegressor(use_label_encoder=False,
                                 tree_method="gpu_hist",
                                 verbosity=0,
                                 objective="reg:squarederror",
                                 reg_lambda=0,
                                 reg_alpha=50)
        self.trained_model = model.fit(self.train_array, self.train_target)
        return

    def get_imp_features(
            self
    ):
        """Get a table of important features in terms of Gain, Cover and Weight."""
        metrics = ["gain", "cover", "weight", "total_gain", "total_cover"]
        out_metric = dict()
        for _metric in metrics:
            value = self.trained_model.get_booster().get_score(importance_type=_metric)
            out_metric[_metric] = value

        return out_metric
