import plotly.express as px
import streamlit as st
import pandas as pd
df=pd.read_csv('./data/imdb_top_1000.csv')

st.set_page_config(page_title='Movies Dashboard', page_icon=':bar_chart:', layout='wide')
menu=st.sidebar.selectbox('Menu',['Home','Release Year'])
items_per_page = 10
total_items = len(df)
total_pages=(total_items // items_per_page) + (1 if total_items % items_per_page > 0 else 0)



if menu == 'Home':
    st.title('Welcome to the Movies Dashboard')
    # Sidebar for pagination
    page = st.sidebar.number_input('Page', min_value=1, max_value=total_pages, value=1)
    # Calculate start and end indices of the dataframe to display
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    st.dataframe(df.iloc[start_idx:end_idx])
elif menu == 'Release Year':
    st.title('Movies by Release Year')
    release_year=st.selectbox('Release Year',df['Released_Year'].unique())
    filter_df=df['Released_Year']==release_year
    total_items = len(df[filter_df])
    total_pages=(total_items // items_per_page) + (1 if total_items % items_per_page > 0 else 0)
    page = st.number_input('Page', min_value=1, max_value=total_pages, value=1)
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    st.dataframe(df[filter_df][start_idx:end_idx])
