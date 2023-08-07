import os

import numpy as np
import pandas as pd

from env import get_connection

def get_db_connection(database):
    return get_connection(database)


# Get titanic data from codeup db
def new_titanic_data():
    # Create SQL query.
    sql_query = 'SELECT * FROM passengers'
    # Read in dataframe from Codeup db
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    return df


def get_titanic_data():
    if os.path.isfile('titanic_df.csv'):
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('titanic_df.csv', index_col=0)  
    else:  
        # Read data from db into a dataframe
        df = new_titanic_data() 
        # Write dataframe to a csv file
        df.to_csv('titanic_df.csv')
    return df


def new_iris_data():
    sql_query = ("SELECT species_id, species_name, sepal_length, sepal_width, petal_length, petal_width FROM measurements JOIN species USING(species_id)")
    # Read in datafr from Codeup db.
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    return df


def get_iris_data():
    if os.path.isfile('iris_df.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('iris_df.csv', index_col=0)
    else:   
        # Read fresh data from Codeup db into a dataframe
        df = new_iris_data() 
        # Cache data
        df.to_csv('iris_df.csv')
    return df


def new_telco_data():
    sql_query = ("SELECT * from customers JOIN contract_types USING (contract_type_id) JOIN internet_service_types USING (internet_service_type_id) JOIN payment_types USING (payment_type_id)")
    # Read in dataframe from Codeup db
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df


def get_telco_data():
    if os.path.isfile('telco.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
    else:
        # Read fresh data from db into a dataframe
        df = new_telco_data()
        # Cache data
        df.to_csv('telco.csv')
    return df