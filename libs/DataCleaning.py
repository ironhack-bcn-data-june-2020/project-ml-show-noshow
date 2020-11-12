#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

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

            
def fill_missing_values_with_knn(df):
    imputer = KNNImputer()
    return imputer.fit_transform(df)


def transform_date(df, col):
    df['AppointmentDay_DOW']=df[col].dt.day_name()
    df['AppointmentDay_month'] = df[col].dt.month_name()
    return df