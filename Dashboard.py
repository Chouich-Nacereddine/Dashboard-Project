import streamlit as st
# import plotly.express as px
import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Dashboard!!!", page_icon=":_bar_chart",layout="wide")

st.title(":bar_chart: Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(":open_file_folder:", filename)
    df = pd.read_excel(filename)
# else:
#     os.chdir(r"C:\Users\nchouich\OneDrive - Capgemini\Bureau\Dashboard-Project")
#     df = pd.read_excel("Data.xlsx")   

col1 , col2 = st.columns((2))
df["Date"] = pd.to_datetime(df["Date"])

# Getting the min && max date
startDate = pd.to_datetime(df["Date"]).min()
endDate = pd.to_datetime(df["Date"]).max()


with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()


filter_choice1 = st.sidebar.selectbox(
    "Choose Your Filter: ",
    ("All", "Instagram (mins)", "YouTube (mins)", "Video Games (mins)","Studies (mins)","Sports (mins)","Family (mins)","Worship (mins)")
)


if filter_choice1 == 'All':
    st.bar_chart(df , x='Date' , y=["Instagram (mins)", "YouTube (mins)", "Video Games (mins)","Studies (mins)","Sports (mins)","Family (mins)","Worship (mins)"])
else:
    st.bar_chart(df , x='Date' , y=filter_choice1)
        

col3 , col4 = st.columns((2))

with col3:
    st.line_chart(df, x='Date' , y=["Instagram (mins)", "YouTube (mins)", "Video Games (mins)","Studies (mins)","Sports (mins)","Family (mins)","Worship (mins)"])


with col4:
    if filter_choice1 == 'All':
        st.line_chart(df, x='Date', y="Instagram (mins)") 
    else:
        st.line_chart(df, x='Date', y=filter_choice1)
