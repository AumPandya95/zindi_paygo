r"""
This module deals with the raw data.

Raw data is read, processed and converted into expected data output.
The final data is then stored in the main data folder's processed directory.

The processed data sets are then used in the jupyter notebooks present in the notebooks directory.
"""
__all__ = [
    'one_hot_encoding', 
    'SubmissionFile', 
    'DataIngestion',
    'split_data']

from src.data.pre_process import one_hot_encoding
from src.data.validation_file import SubmissionFile
from src.data.ingestion import *
