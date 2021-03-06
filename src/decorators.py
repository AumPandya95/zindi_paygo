import functools

import numpy as np
import pandas as pd


def conv_to_df(func):
    @functools.wraps(func)
    def check_and_return_df(self, *args, **kwargs):
        frame = kwargs.get("categorical_frame")
        encoded_arr = func(self, *args, **kwargs)
        # two pipelines for pd.DataFrame and np.ndarray
        if isinstance(frame, pd.DataFrame):
            if kwargs.get("type_of_data", False) == "train":
                enc_columns = []
                for column in frame.columns:
                    # Each column's categories need to be sorted as this is how OHE is implemented
                    if kwargs.get("drop", None):
                        enc_columns.extend(sorted(frame[column].unique())[1:])
                    else:
                        enc_columns.extend(sorted(frame[column].unique()))
            else:
                if kwargs.get("drop", None):
                    enc_columns = [categories for feat, cat_arr in enumerate(self.encoder_obj.categories_)
                                   for categories in cat_arr[self.encoder_obj.drop_idx_[feat] + 1:]]
                else:
                    enc_columns = [
                        categories for cat_arr in self.encoder_obj.categories_ for categories in cat_arr]
            encoded_arr = pd.DataFrame(encoded_arr, columns=enc_columns)
        else:  # if isinstance(frame, np.ndarray)
            if kwargs.get("conv"):
                if kwargs.get("type_of_data", False) == "train":
                    enc_columns = []
                    for column_idx in range(frame.shape[1]):
                        enc_columns.extend(
                            sorted(np.unique(frame[:, column_idx], axis=0)))
                else:
                    enc_columns = [
                        categories for cat_arr in self.encoder_obj.categories_ for categories in cat_arr]
                encoded_arr = pd.DataFrame(encoded_arr, columns=enc_columns)

        return encoded_arr

    return check_and_return_df


def optimise_hyper_params(func):
    @functools.wraps(func)
    def search_space(self, *args, **kwargs):
        optimisation_required = kwargs.get("optimise_model")
        if not optimisation_required:
            func(self, *args, **kwargs)
            return
        else:
            if kwargs.get("opt_method", None) == "random_search":
                from sklearn.model_selection import RandomizedSearchCV
                model = func(self, *args, **kwargs)
                search_step = RandomizedSearchCV(model,
                                                 param_distributions=kwargs.get(
                                                     "params"),
                                                 n_iter=5,
                                                 scoring="neg_mean_squared_error",
                                                 n_jobs=-1,
                                                 cv=5,
                                                 verbose=3)
            else:
                from sklearn.model_selection import GridSearchCV
                model = func(self, *args, **kwargs)
                search_step = GridSearchCV(estimator=model,
                                           param_grid=kwargs.get(
                                               "params"),
                                           cv=5,
                                           scoring="neg_mean_squared_error",
                                           n_jobs=-1,
                                           verbose=3)

            fitted_model = search_step.fit(self.train_array, self.train_target)
            print('best params', fitted_model.best_params_)
            return fitted_model

    return search_space
