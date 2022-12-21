import pandas as pd
import requests
import streamlit as st

def app():

    def disp():
        st.header('**Input DataFrame**')
        res = requests.get('http://127.0.0.1:5000/getdata')
        data = res.json()["data"]
        df = pd.DataFrame(data, columns=["age", "sex", "bmi", "children", "smoker", "region", "charges"])

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            b1 = st.button("Last 10 rows", key='1')
        with col2:
            b2 = st.button("First 10 rows", key='2')
        with col3:
            b3 = st.button("Display All", key='3')

        if b1:
            end = df.tail(10)
            st.table(end)
        if b2:
            start = df.head(10)
            st.table(start)
        if b3:
            st.table(df)

    disp()