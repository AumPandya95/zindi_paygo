from typing import Optional

import pandas as pd

__all__ = ['SubmissionFile']


class SubmissionFile:
    """
    Create and return the file in the submission format and for calculating RMSE.

    Steps
    -----
        - Two dfs will be created; one with target cols and one with Pred cols
        - The two will be converted to submission acceptable formats and merged
    """
    def __init__(
            self,
            validation_data: pd.DataFrame,
            type_of_data: str
    ) -> None:
        self.validation_data = validation_data
        self.type_of_data = type_of_data

    def transform_target(self):
        """Transform target cols into the submission format."""
        transformed_frame = self.validation_data.melt(
            id_vars=["ID"], value_vars=["m1", "m2", "m3", "m4", "m5", "m6"], var_name="temp", value_name="Target"
        )
        transformed_frame["ID"] = transformed_frame[["ID", "temp"]].agg(" x ".join, axis=1)
        transformed_frame.drop(columns=["temp"], inplace=True)
        transformed_frame.sort_values(by=["ID"], ascending=True, inplace=True)

        return transformed_frame

    def transform_prediction(self):
        """Transform prediction cols into the submission format."""
        transformed_frame = self.validation_data.melt(
            id_vars=["ID"], value_vars=["m1_pred", "m2_pred", "m3_pred", "m4_pred", "m5_pred", "m6_pred"],
            var_name="temp", value_name="Prediction"
        )
        transformed_frame["temp"].replace(
            {
                "m1_pred": "m1",
                "m2_pred": "m2",
                "m3_pred": "m3",
                "m4_pred": "m4",
                "m5_pred": "m5",
                "m6_pred": "m6"
            }, inplace=True)
        transformed_frame["ID"] = transformed_frame[["ID", "temp"]].agg(" x ".join, axis=1)
        transformed_frame.drop(columns=["temp"], inplace=True)
        transformed_frame.sort_values(by=["ID"], ascending=True, inplace=True)

        return transformed_frame

    def execute(
            self,
            save: Optional[bool] = False,
            save_name: Optional[str] = None
    ):
        """
        Convert data with predictions to final output.
        Parameters
        ----------
        save: bool
            If True, save the submission file in the data/submissions/ directory
        save_name: str
            If save = True then specify the name with which to save the file

        Returns
        -------

        """
        pred_frame = self.transform_prediction()
        if self.type_of_data == "test":
            submission_frame = pred_frame
        else:
            target_frame = self.transform_target()
            submission_frame = pd.merge(target_frame, pred_frame, how="left", on=["ID"])

        if save:
            pass  # save the file, given the save_name

        return submission_frame


if __name__ == '__main__':
    import os
    from pathlib import Path
    import pandas as pd

    file_path = os.path.join(Path(__file__).parent.parent.parent, "data/Train.csv")
    data = pd.read_csv(file_path, sep=",")
    create_submission = SubmissionFile(validation_data=data,
                                       type_of_data="train")
    submission_data = create_submission.execute()
