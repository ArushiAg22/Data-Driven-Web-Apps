import pandas as pd
import streamlit as st
import seaborn as sns

def app():
    df = pd.read_csv('/Users/arushiagarwal/Desktop/Designing Data-driven Webapps/690_Project/WA_Fn-UseC_-HR-Employee-Attrition.csv')

    # df = st.session_state["df"]

    catagorical = ['Attrition', 'BusinessTravel', 'Department', 'Education', 'EducationField', 'EnvironmentSatisfaction',
                   'Gender', 'JobInvolvement', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel',
                   'WorkLifeBalance', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'OverTime']
    continuous = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate',
                 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
                 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']

    st.header("Univariate Plots")
    radio_params = ['Categorical Variables', 'Continuous Variables']
    choice = st.radio("Select the variable type", radio_params)

    if (choice == 'Categorical Variables'):
        st.subheader("Select Categorical Variable for the Count plot")
        select_pos = st.selectbox('Feature', catagorical)
        st.write("-----")

        def count_plot(df, x):
            a = sns.countplot(data=df, x=x)
            fig = a.figure
            st.pyplot(fig)

        count_plot(df, df[select_pos])
    else:
        st.subheader("Select a Continuous Variable for the KDE plot")
        select_pos = st.selectbox('Feature', continuous)
        st.write("-----")

        def kde_plot(df, x):
            b = sns.kdeplot(data=df, x=x)
            fig = b.figure
            st.pyplot(fig)

        kde_plot(df, df[select_pos])