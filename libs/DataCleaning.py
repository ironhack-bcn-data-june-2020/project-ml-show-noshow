#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn import preprocessing

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


def transform_date(df, col, col2):
    df['AppointmentDay_DOW']=df[col].dt.day_name()
    df['AppointmentDay_Day_number'] = df[col].dt.day
    df['AppointmentDay_month'] = df[col].dt.month_name()
    df['Difference_Days_App_Date_and_Sched_Day'] = ((df[col] - df[col2]).dt.days).clip(0,inplace=False)

def set_negatives_to_zero(df,col):
    df[df[col] < 0]
    
def label_encoder(df,col):
    le = preprocessing.LabelEncoder()
    transformed = le.fit_transform(df[col])
    df[col] = transformed