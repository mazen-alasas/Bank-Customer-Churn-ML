import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def drop_columns(df, columns):
    df = df.drop(columns, axis = 1)
    return df


def encode_categorical_columns(df):
    df = df.replace({
            'Geography': {'France': 1, 'Spain': 2, 'Germany': 3},
            'Gender'   : {'Male' : 0, 'Female' : 1},  
            'HasCrCard': {'Yes': 1, 'No': 0},
            'IsActiveMember': {'Yes': 1, 'No': 0}
         })
    return df


def scale_columns(df, columns):
    return MinMaxScaler().fit_transform(df[columns])