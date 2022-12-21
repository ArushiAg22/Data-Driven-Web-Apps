import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def app():
    df = pd.read_csv('/Users/arushiagarwal/Desktop/Designing Data-driven Webapps/690_Project/WA_Fn-UseC_-HR-Employee-Attrition.csv')

    continuous = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 'MonthlyRate',
                 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
                 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']

    st.title("Interactive Slider")

    feature = st.selectbox("Select the feature", continuous)
    end = df[feature].max()
    st.write(end)
    if (end < 101):
        max = 100
    elif (end < 1501):
        max = 1500
    else:
        max = 30000
    slid = st.slider('Value', min_value=0, max_value=max, value=0)
    st.write("Slider Value is: ", slid)

    colors = ['#3742fa', '#FDB927']
    def plot_stats_pie(min_value, col):
        num_above = len(df.loc[(df[col] >= min_value)])
        num_below = len(df.loc[(df[col] < min_value)])
        num = num_above + num_below

        nums = [num_above, num_below]
        labels = ["Above", "Below"]

        st.write(f"{num}    Total Employees")
        st.write(f"{num_above}  No. of Employees Above")
        st.write(f"{num_below}  No. of Employees Below")

        fig1, ax1 = plt.subplots()
        ax1.pie(nums, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    plot_stats_pie(slid, feature)