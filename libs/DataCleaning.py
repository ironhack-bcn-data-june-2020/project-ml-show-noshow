#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

def transform_dates_to_date_dtype(df,columns):
    '''
    This function converts the columns provided from the received dataframe to Date format.
    INPUTS: 
        df: Pandas Dataframe
        columns: Strings List containing the columns that will be converted to datetime format.
    OUTPUTS:
        None
    '''
    for col in columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except: #TODO CAPTURE ERROR TYPE
            print('AN ERROR OCURRED')