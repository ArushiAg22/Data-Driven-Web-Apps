import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import sqlite3
import pickle

def ML_model():
    conn = sqlite3.connect('insurance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from insurance;")
    result = cursor.fetchall()
    data = [list(i) for i in result]
    df = pd.DataFrame(data, columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'])
    print(df)

    le = LabelEncoder()
    cols = ['sex', 'smoker', 'region']
    for col in cols:
        df[col] = le.fit_transform(df[col]).astype('str')

    features = df.columns[:-1]
    target = df.columns[-1]
    X = df[features].values
    y = df[target].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

    rf = RandomForestRegressor(n_estimators=200, random_state=8)
    rf.fit(X_train, y_train)            # Fitting the train data to 'random Forest Regressor'
    print("Got to here too")
    train_y_pred = rf.predict(X_train)
    test_y_pred = rf.predict(X_test)

    r2_train_score = rf.score(X_train, y_train)
    r2_test_score = rf.score(X_test, y_test)

    file = open('rf_model.pkl', 'wb')
    pickle.dump(rf, file)  # save the model
    file.close()
    return str(r2_train_score)
