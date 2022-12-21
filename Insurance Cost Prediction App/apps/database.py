import sqlite3
import pandas as pd

def database():
    try:
        insurance = pd.read_csv("../insurance.csv")
        conn = sqlite3.connect('insurance.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE insurance (age,sex,bmi,children,smoker,region,charges)''')
        insurance.to_sql('insurance', conn, if_exists='append', index = False)
        return 'Insurance Cost Prediction App'
    except:
        return 'Insurance Cost Prediction App'