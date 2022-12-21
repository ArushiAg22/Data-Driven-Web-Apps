import pandas as pd
import streamlit as st
import seaborn as sns

def app():
    # df = pd.read_csv('../WA_Fn-UseC_-HR-Employee-Attrition.csv')

    df = st.session_state["df"]

    def multivariate_plots(df):
        a1 = sns.histplot(data=df, x='Gender', hue='BusinessTravel', multiple='dodge')
        fig = a1.figure
        st.pyplot(fig)
        a2 = sns.histplot(data=df, x='Age', hue='Attrition', multiple='dodge')
        fig = a2.figure
        st.pyplot(fig)
        a3 = sns.histplot(data=df, x='PercentSalaryHike', hue='Attrition', multiple='dodge')
        fig = a3.figure
        st.pyplot(fig)

    multivariate_plots(df)