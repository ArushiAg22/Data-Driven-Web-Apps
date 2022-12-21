import streamlit as st
import pandas as pd
from multiapp import MultiApp
from apps import univariate, multivariate, ml, interactive          # import your app modules here

app = MultiApp()

# Web App Title
st.markdown('''
# **The Employee Attrition App**
''')

# Adding all the applications here
app.add_app("Univariate Analysis", univariate.app)
app.add_app("Mulitvariate Analysis", multivariate.app)
app.add_app("Model", ml.app)
app.add_app("Interactive", interactive.app)

uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def data():
    if uploaded_file is not None:
        # @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
        df = load_csv()
        return df

st.write("---")

if "df" not in st.session_state:
    st.session_state["df"] = ""
st.session_state["df"] = data()

# The main app
rad = st.sidebar.radio("", ["Data", "Data Analysis"])
if rad == 'Data':
    st.header('**Input DataFrame**')
    st.write(st.session_state["df"])
    st.write('---')

if rad == "Data Analysis":
    app.run()