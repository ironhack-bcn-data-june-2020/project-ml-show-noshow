#!/usr/bin/env python
# coding: utf-8

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


def iqr(dataset, column): # Esta funcion detecta los outliers
    Q1 = np.percentile(dataset[column], 25)
    Q3 = np.percentile(dataset[column], 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    return lower, upper
