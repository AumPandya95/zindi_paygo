import statistics
from copy import deepcopy
from datetime import datetime

import numpy as np


def split(ip_string, type_of_value=None):
    if isinstance(ip_string, str):
        if type_of_value == "date":
            result = ip_string.strip("][").split(",")
        else:
            result = [float(num) for num in ip_string.strip("][").split(",")]
    elif ip_string in (None, np.nan):
        result = np.nan
    else:
        raise Exception("Undetected Input")

    return result


def length_calc(input_val):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        result = len(input_val)
    else:
        raise Exception("Undetected Input")

    return result


def sum_calc(input_val):
    if input_val in (None, np.nan):
        result = 0

    elif isinstance(input_val, list):
        result = 0
        for ele in input_val:
            result += float(ele)
            result = round(result, 2)
    else:
        raise Exception("Undetected Input")

    return result


def mean_calc(input_val):
    if input_val in (None, np.nan):
        result = 0

    elif isinstance(input_val, list):
        result = 0
        for ele in input_val:
            result += float(ele)
        result = result / len(input_val)
        result = round(result, 2)
    else:
        raise Exception("Undetected Input")

    return result


def median_calc(input_val):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        result = statistics.median(map(float, input_val))
        result = round(result, 2)
    else:
        raise Exception("Undetected Input")

    return result


def max_calc(input_val):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        result = max(map(float, input_val))
    else:
        raise Exception("Undetected Input")

    return result


def min_calc(input_val):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        result = min(map(float, input_val))
    else:
        raise Exception("Undetected Input")

    return result


def std_dev_calc(input_val):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        result = statistics.stdev(map(float, input_val))
        result = round(result, 2)
    else:
        raise Exception("Undetected Input")

    return result


def back_feature(input_val, n=1):
    if input_val in (None, np.nan):
        result = 0
    elif isinstance(input_val, list):
        if len(input_val) >= n:
            result = round(float(input_val[-1 * n]), 2)
        else:
            result = 0
    else:
        raise Exception("Undetected Input")

    return result


def convert(ip_str):
    ip_str = ip_str.replace("'", "").strip()
    ip_str = str(datetime.strptime(ip_str, "%m-%Y").strftime("%Y-%m"))
    return ip_str


def add_predicted_payment(original_struct, value_to_add):
    print(original_struct)
    if isinstance(original_struct, str):
        result = split(original_struct)
        result.append(value_to_add)
    elif isinstance(original_struct, list):
        result = original_struct
        result.append(value_to_add)
    else:
        raise Exception("Invalid Input")

    return result


def add_payment(og_list, new_payment):
    if og_list in (None, np.nan):
        og_list = np.nan
    else:
        og_list_deepcopy = deepcopy(og_list)
        og_list_deepcopy.append(new_payment)
    return og_list_deepcopy
