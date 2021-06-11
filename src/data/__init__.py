
r"""
This module deals with the raw data.

Raw data is read, processed and converted into expected data output.
The final data is then stored in the main data folder's processed directory.

The processed data sets are then used in the jupyter notebooks present in the notebooks directory.
"""
__all__ = ['extract_data']

from src.data.extraction import extract_data
