import pandas as pd

from sklearn.model_selection import train_test_split
from adam_acquire import get_titanic


def drop_cols(df):
    
    return df.drop(columns = ['pclass', 'passenger_id', 'embarked', 'deck'])


def train_val_test(df, strat, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed,
                                       stratify = df[strat])
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed,
                                 stratify = val_test[strat])
    
    return train, val, test


def impute_vals(train, val, test):
    
    town_mode = train.embark_town.mode()
    
    train.embark_town = train.embark_town.fillna(town_mode)
    val.embark_town = val.embark_town.fillna(town_mode)
    test.embark_town = test.embark_town.fillna(town_mode)
    
    med_age = train.age.median()
    
    train.age = train.age.fillna(med_age)
    val.age = val.age.fillna(med_age)
    test.age = test.age.fillna(med_age)
    
    return train, val, test


def titanic_pipeline():
    
    df = get_titanic()
    
    df = drop_cols(df)
    
    train, val, test = train_val_test(df, 'survived')
    
    train, val, test = impute_vals(train, val, test)
    
    return train, val, test