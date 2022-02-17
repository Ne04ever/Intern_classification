import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from hr_analytics_variables import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Importing data
eda_data = pd.read_csv(r'https://raw.githubusercontent.com/Farrukh-Ullah/python_project/master/notebooks/clean.csv')
data = pd.read_csv(r'https://raw.githubusercontent.com/Farrukh-Ullah/python_project/master/notebooks/df.csv', index_col=False)
df = pd.read_csv(r'https://raw.githubusercontent.com/Farrukh-Ullah/python_project/master/notebooks/model_df.csv')
pt1 = pd.pivot_table(eda_data, index='target',columns = 'experience_lvl', values='city_dev_perc')
pt2 = pd.pivot_table(eda_data, index=['target','company_class',], values='city_dev_perc')
pt3 = pd.pivot_table(eda_data, index=['target','gender',], values='training_hours')
pt4 = pd.pivot_table(eda_data, index=['target','company_class',], values='training_hours')

eda_df = eda_data[['gender', 'relevent_experience','enrolled_university', 'education_level', 'major_discipline', 'company_type', 'last_new_job','training_hours', 'target', 'city_id', 'city_dev_perc','experience_lvl', 'experience','company_class']]

intern_stays = eda_df.loc[eda_df['target'] == 0]
bar_chart = intern_stays[
    ['gender', 'relevent_experience', 'enrolled_university', 'education_level', 'major_discipline', 'company_type',
    'last_new_job', 'experience_lvl', 'company_class']]

model_df = pd.get_dummies(df)
# Models part
lr = LogisticRegression()
x = model_df.drop('target', axis=1)
y = model_df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
scaler = preprocessing.StandardScaler().fit(x_train)
scaler = preprocessing.StandardScaler().fit(x_train)
scaler.mean_
scaler.scale_
x_scaled = scaler.transform(x_train)
lr.fit(x_scaled, y_train)
pred = lr.predict(x_test)
rf = RandomForestRegressor()
rf.fit(x_train, y_train)
pred1 = rf.predict(x_test)






def set_home():
    st.image("https://storage.googleapis.com/kaggle-datasets-images/1019790/1719283/f7505a4e4d6e9c141aa2196a7a77ddf7/dataset-cover.png")
    st.write(intro, unsafe_allow_html=True)
    st.write(intro_herramientas_fuentes, unsafe_allow_html=True)


def set_data():
    st.title("DataFrame:")
    st.write("This dataset designed to understand the factors that lead a person to leave current job. By using classification models we will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.")
    st.write(">***21287 entries | 15 columns***")
    st.dataframe(data)
    st.write(">***Let's analyize the dataframe.***")
    st.dataframe(data.describe())
    st.text("")
    st.title("*Target Distribution:*")
    st.write("By analyizing the target distribution we can understand that the 75% of the candidates stays in the comapany.")
    col1, col2 = st.columns(2)
    with col1:
        total = eda_df['target'].value_counts()
        fig1 = total.plot.pie(shadow=True, explode=(0, 0.1), startangle=0, autopct='%1.1f%%')
        labels = ['intern stays', 'intern leaves']
        plt.legend(labels)
        plt.axis('equal')
        st.pyplot(fig1.figure)
    with col2:
        st.markdown(' ')
    st.write(">***Now we will analyize which factors effects these interns decisions.***")

def set_analysis():
    st.title("*Analyizing Candidates Who Will Stay:*")
    st.write("*We are focusing on candidates who stay and work for the company after the training, lets analyze which factors effects their decission.*")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1: Relevant Experience of the Candidates")
        st.markdown('Distribution of the relevant experience of the candidates.')
        num = bar_chart['relevent_experience'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    with col2:
        st.markdown("#### 2: Education Level of the Candidates")
        st.markdown('Most candidates have done their masters, but very few only have completed primary education.')
        num = bar_chart['education_level'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 3: Major Discipline of the Candidates")
        st.markdown('From this distribution graph, we can understand that a large no. of candidates are from the science and endgeneering background.')
        num = bar_chart['major_discipline'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    with col2:
        st.markdown("#### 4: Company Types of the Candidates")
        st.markdown('The companies are distributed into 6 types and most of the candidates choose private companies.')
        num = bar_chart['company_type'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 5: Last New Job of the Candidates")
        st.markdown('Distribution of last new job of the candidates.')
        num = bar_chart['last_new_job'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    with col2:
        st.write("#### 6: Experience Level of the Candidates")
        st.markdown('The candidates are distributed to mainly 4 levels according to their experience.')
        num = bar_chart['experience_lvl'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    col1, col2 = st.columns(2)
    with col1:
        st.write("#### 7: Company Class of the Candidates")
        st.markdown('Distribution of company class of the candidates.')
        num = bar_chart['company_class'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        st.bar_chart(num)

    with col2:
        st.markdown("#### 8: Gender of the Candidates")
        st.markdown('Distribution of gender.')
        ##st.write("*From this graph you can understand that most*")
        num = bar_chart['gender'].value_counts()
        plt.ylabel("No of interns")
        plt.xticks(rotation=90)
        labels = ['0 Male', '1 Female', '2 Other']
        plt.legend(labels)
        st.bar_chart(num)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 9: City development Percentage, Histogram")
        qwd = intern_stays.city_dev_perc.hist()
        plt.ylabel('No. of interns', size='x-large')
        plt.xlabel('City_dev_perc', size='x-large')
        plt.title('City development Percentage, Histogram', size='x-large')
        st.pyplot(qwd.figure)

    with col2:
        st.markdown(' ')

def set_Piyottbl():
    st.title("*Pivot Tables:*")
    st.write("*Now let summarize the data by creating the pivot tables.*")
    st.write("#### Pivot Table: 1")
    st.write("This pivot table shows the average city development percentage for candidates of different experience levels.")
    st.dataframe(pt1)

    st.write("#### Pivot Table: 2")
    st.write("This pivot table shows the city development for each company class.")
    st.dataframe(pt2)

    st.write("#### Pivot Table: 3")
    st.write("This pivot table shows the average training hours for each gender")
    st.dataframe(pt3)

    st.write("#### Pivot Table: 4")
    st.write("This pivot table shows the training hours for different company classes.")
    st.dataframe(pt4)

def set_classmod():
    st.title("*Classification Model*")
    st.write("We applied two classification models, logistics regression and random forest model. They gave a mean absolute error of ***0.563*** and ***0.283*** For the models. These results can be improved further by optimizing")
    st.subheader("*Prediction Using Regression Model*")
    st.write("##### Accuracy:")
    st.write(mean_absolute_error(y_test, pred))
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.subheader("*Prediction Using Random Forest*")
    st.write("##### Accuracy:")
    st.write(mean_absolute_error(y_test, pred1))














