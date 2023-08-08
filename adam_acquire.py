import os

import pandas as pd

from env import get_connection


def get_titanic():
    
    filename = 'titanic.csv'
    
    if os.path.isfile(filename):
        
        return pd.read_csv(filename)
    
    else:
        
        url = get_connection('titanic_db')
        
        query = '''
                SELECT *
                FROM passengers
                '''
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index = 0)
        
        return df