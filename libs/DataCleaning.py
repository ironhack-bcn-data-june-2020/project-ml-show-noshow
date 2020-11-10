#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
# In[1]:


def clean_df(df):
    return df

# In[ ]:
from sklearn.preprocessing import OrdinalEncoder
def EncodeAlcoholism(df):
    
    '''Alcoholism_Num (None= 0 and Low = 1, Moderate=2  High=3) '''
    enc= OrdinalEncoder(categories=[["None","Low","Moderate","High"]])
    df["Alcoholism_Num"]=enc.fit_transform(df["Alcoholism"].values.reshape(-1,1)).reshape(df.shape[0])
    return df
=======

def iqr(dataset, column): # Esta funcion detecta los outliers
    Q1 = np.percentile(dataset[column], 25)
    Q3 = np.percentile(dataset[column], 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    return lower, upper
=======
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
>>>>>>> f58b10217c1e6c3e3749fde319ccc4f20f0856f9
