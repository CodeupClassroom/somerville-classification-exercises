import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

# ------------------- IRIS DATA -------------------

def prep_iris(df):
    df = df.drop(columns= (['species_id', 'measurement_id']))
    df = df.rename(columns = {'species_name': 'species'})
    return df

# ------------------- TITANIC DATA -------------------

def prep_titanic(titanic):
    titanic = titanic.drop(columns=['class', 'embarked', 'passenger_id', 'deck'])
    titanic = titanic.dropna()
    return titanic

# ------------------- TELCO DATA -------------------

def prep_telco(telco):
    telco = telco.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    return telco

# ------------------- SPLIT DATA -------------------

def split_data(df, target):
    train, test = train_test_split(df, train_size = 0.5, random_state=42, stratify=df[target])
    train, val = train_test_split(train, train_size = 0.7, random_state=42, stratify=train[target])
    return train, val, test