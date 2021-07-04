from src.utils import split, length_calc, mean_calc, sum_calc, min_calc, max_calc, std_dev_calc, median_calc, convert, \
    back_feature
import pandas as pd


class FeatureEngineering:
    def __init__(self, df):
        self.df = df

    def execute(self):
        self.df = self.payment_features(self.df)
        self.df = self.back_features(self.df)
        self.df = self.date_features(self.df)

        return self.df

    def payment_features(self, df):
        # TODO: Write checks for base columns like SplitTransactionsHistory
        try:
            df["SplitPaymentsHistory"] = df.apply(lambda row: split(row["PaymentsHistory"]), axis=1)
            df["SplitTransactionDates"] = df.apply(lambda row: split(row["TransactionDates"], type_of_value='date'),
                                                   axis=1)
            df["nb_payments"] = df.apply(lambda row: length_calc(row["SplitPaymentsHistory"]), axis=1)
            df["amount_paid"] = df.apply(lambda row: sum_calc(row["SplitPaymentsHistory"]), axis=1)
            df["percent_amt_paid"] = df["amount_paid"] / df["TotalContractValue"]
            df["mean_amt_paid"] = df.apply(lambda row: mean_calc(row["SplitPaymentsHistory"]), axis=1)
            df["median_amt_paid"] = df.apply(lambda row: median_calc(row["SplitPaymentsHistory"]), axis=1)
            df["max_amt_paid"] = df.apply(lambda row: max_calc(row["SplitPaymentsHistory"]), axis=1)
            df["min_amt_paid"] = df.apply(lambda row: min_calc(row["SplitPaymentsHistory"]), axis=1)
            df["stddev_amt_paid"] = df.apply(lambda row: std_dev_calc(row["SplitPaymentsHistory"]), axis=1)
            df["nb_skipped_months"] = df.apply(
                lambda row: self._nb_missing_payments(
                    row["SplitTransactionDates"], row.FirstPaymentDate, row.LastPaymentDate
                ), axis=1
            )
        except KeyError:
            raise Exception("Column Missing")

        return df

    def back_features(self, df, nb_back_features=5):
        for i in range(1, nb_back_features + 1):
            df = self._add_back_feature(df, i)
        return df

    @staticmethod
    def date_features(df):
        df["RegistrationDateParsed"] = pd.to_datetime(df["RegistrationDate"], infer_datetime_format=True)
        df["ExpectedTermDateParsed"] = pd.to_datetime(df["ExpectedTermDate"], infer_datetime_format=True)
        df["FirstPaymentDateParsed"] = pd.to_datetime(df["FirstPaymentDate"], infer_datetime_format=True)
        df["LastPaymentDateParsed"] = pd.to_datetime(df["LastPaymentDate"], infer_datetime_format=True)

        df["RegistrationDate"] = pd.to_datetime(df["RegistrationDate"], infer_datetime_format=True).dt.date
        df["ExpectedTermDate"] = pd.to_datetime(df["ExpectedTermDate"], infer_datetime_format=True).dt.date
        df["FirstPaymentDate"] = pd.to_datetime(df["FirstPaymentDate"], infer_datetime_format=True).dt.date
        df["LastPaymentDate"] = pd.to_datetime(df["LastPaymentDate"], infer_datetime_format=True).dt.date
        df["LastFirstDuration"] = (df.LastPaymentDate - df.FirstPaymentDate).astype("timedelta64[M]")
        df["ExpectedFirstDuration"] = (df.ExpectedTermDate - df.FirstPaymentDate).astype("timedelta64[M]")
        df["LastRegistrationDuration"] = (df.LastPaymentDate - df.RegistrationDate).astype("timedelta64[M]")

        df["FirstPaymentMonth"] = df["FirstPaymentDateParsed"].dt.month
        df["LastPaymentMonth"] = df["LastPaymentDateParsed"].dt.month
        df["RegistrationMonth"] = df["RegistrationDateParsed"].dt.month

        # # Sine
        # df["FirstPaymentMonthSin"] = np.sin((df.FirstPaymentMonth-1)*(2.*np.pi/12))
        # df["LastPaymentMonthSin"] = np.sin((df.LastPaymentMonth-1)*(2.*np.pi/12))
        # df["RegistrationMonthSin"] = np.sin((df.RegistrationMonth-1)*(2.*np.pi/12))

        # # Cos
        # df["FirstPaymentMonthCos"] = np.cos((df.FirstPaymentMonth-1)*(2.*np.pi/12))
        # df["LastPaymentMonthCos"] = np.cos((df.LastPaymentMonth-1)*(2.*np.pi/12))
        # df["RegistrationMonthCos"] = np.cos((df.RegistrationMonth-1)*(2.*np.pi/12))
        return df

    @staticmethod
    def _nb_missing_payments(transaction_dates, first_payment_date, last_payment_date):
        payment_dates = set([convert(x) for x in transaction_dates])
        payment_dates_range = set([str(x) for x in pd.period_range(first_payment_date, last_payment_date, freq="M")])

        return len(payment_dates_range - payment_dates) - 6

    @staticmethod
    def _add_back_feature(df, n=1):
        df[f"b{n}"] = df.apply(lambda row: back_feature(row["SplitPaymentsHistory"], n), axis=1)
        return df
