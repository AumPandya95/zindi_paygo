from typing import Union, Dict, Optional

import numpy as np
import pandas as pd
import xgboost as xgb

from src.decorators import optimise_hyper_params


class ModelXgBoost:
    def __init__(
            self,
            train_array: Union[np.ndarray, pd.DataFrame],
            train_target: Union[np.ndarray, pd.DataFrame],

    ) -> None:
        self.train_array = train_array
        self.train_target = train_target
        self.trained_model = None

    @optimise_hyper_params
    def train_model(
            self,
            optimise_model: bool = False,
            params: Optional[Dict] = None,
            **tuned_params
    ) -> Union[xgb.XGBRegressor, None]:
        """
        Train the model on given data using Scikit-learn API of XGBoost.
        If optimise_model is True then the method returns the RandomizedSearchCV object which can be used to get the
        best params and be passed as `tuned_params` in a second call to the method.

        Parameters
        ----------
        optimise_model: bool
            Whether optimisation is required for the model
        params: dict, Optional
            hyper parameter ranges for the SearchCV to iterate on to find the best model. This is only valid and
            required if optimise_model is True.
        tuned_params: dict
            The tuned hyper parameters to be passed to the model

        Returns
        -------
            trained_model: if optimise_model is False
            model: [Best Model object] if optimise_model is True
        Notes
        -----
            - Best model can be accessed by `model.best_estimator_`
            - Best model params can be accessed by `model.best_params_`
        """
        model = xgb.XGBRegressor(use_label_encoder=False,
                                 verbosity=0,
                                 objective="reg:squarederror",
                                 reg_lambda=tuned_params.get('reg_lambda', 0),
                                 reg_alpha=tuned_params.get('reg_alpha', 50))
        if not optimise_model:
            self.trained_model = model.fit(self.train_array, self.train_target)
            return
        else:
            return model

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
