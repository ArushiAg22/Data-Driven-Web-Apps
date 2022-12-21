import streamlit as st
import requests

def app():

    st.title("Make Predictions")

    age = st.text_input("age")
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.text_input("bmi")
    children = st.text_input("children")
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

    if sex == "female":
        new_sex = 0
    else:
        new_sex = 1

    if smoker == "no":
        new_smoker = 0
    else:
        new_smoker = 1

    if region == "Northeast":
        new_region = 0
    elif region == "Northwest":
        new_region = 1
    elif region == "Southeast":
        new_region = 2
    else:
        new_region = 3

    col1, col2 = st.columns([1, 1])

    with col1:
        b2 = st.button("Predict")
    with col2:
        b3 = st.button("Predict and add the data")

    if b2:
        res = requests.post('http://127.0.0.1:5000/predict', json={"data": [age, new_sex, bmi, children, new_smoker, new_region]})
        data = res.json()["data"]
        st.write('Predicted Insurance cost is ', data[6])

    if b3:
        res = requests.post('http://127.0.0.1:5000/predict', json={"data": [age, new_sex, bmi, children, new_smoker, new_region]})
        data = res.json()["data"]
        data[0] = int(data[0])
        data[1] = sex
        data[2] = float(data[2])
        data[3] = int(data[3])
        data[4] = smoker
        data[5] = region
        st.write('Predicted Insurance cost is ', data[6])
        res = requests.post('http://127.0.0.1:5000/add', json={"data": data})
