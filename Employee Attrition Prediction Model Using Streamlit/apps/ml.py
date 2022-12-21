import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import streamlit as st

def app():
    # df = pd.read_csv('../WA_Fn-UseC_-HR-Employee-Attrition.csv')

    df = st.session_state["df"]
    st.header("Train ML Model")
    options = df.columns
    choice = st.selectbox("Select Target Variable", options)

    df1= df.loc[:, df.columns != choice]

    features = df1.columns
    def ML_model(df):
        le = LabelEncoder()
        for col in features:
            df[col] = le.fit_transform(df[col]).astype('str')
        b1 = st.button('Start training the model')
        if b1:
            X = df[features]
            y = df[choice]
            y.replace({'No': 0, 'Yes': 1}, inplace=True)
            y.to_numpy()

            st.write("Dividing the model into Train and Test datasets.\n\n")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5, stratify=y)

            rf = RandomForestClassifier(n_estimators=3000, max_depth=4, max_leaf_nodes=6, random_state=3)
            st.write("Fitting the model!!\n\n")
            rf.fit(X_train, y_train)  # Fitting the train data to 'random Forest Classifier'

            st.write("Starting the predictions\n\n")
            # Finding the predictions of random forest classifier for train and test subsets

            train_y_pred = rf.predict(X_train)
            test_y_pred = rf.predict(X_test)

            train_score = metrics.accuracy_score(y_train, train_y_pred)  # Compute train accuracy
            test_score = metrics.accuracy_score(y_test, test_y_pred)  # Compute test accuracy
            train_report = classification_report(y_train, train_y_pred)  # Generate classification report for train data
            test_report = classification_report(y_test, test_y_pred)  # Generate classification report for test data

            st.write('Train Score: \n\n', train_score)
            st.write('Random Forest Classifier Train Classification Report: \n\n', train_report)
            st.write('Test Score: \n\n', test_score)
            st.write('Random Forest Classifier Test Classification Report: \n\n', test_report)
            if (train_score > 0.80 and test_score > 0.80):
                st.write("The model is good :thumbsup:")

    ML_model(df)