import requests
import streamlit as st

def app():

    def ML_model():
        b1 = st.button("Train the model")
        if b1:
            res = requests.get('http://127.0.0.1:5000/train')
            if res.status_code == 200:
                st.write('Model is trained!!')
            else:
                st.write("Error Occurred while training the Model!!")

    ML_model()