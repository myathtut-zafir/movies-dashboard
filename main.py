import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('./data/imdb_top_1000.csv')

st.set_page_config(page_title='IMDB Movies Dashboard', page_icon='🎬', layout='wide')
menu=st.sidebar.selectbox('Menu',['Home','Filter By Release Year',"Filter By Artist","Bar Chart"])
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
elif menu == 'Filter By Release Year':
    st.title('Movies by Release Year')
    release_year=st.selectbox('Release Year',df['Released_Year'].unique())
    filter_df=df['Released_Year']==release_year
    total_items = len(df[filter_df])
    total_pages=(total_items // items_per_page) + (1 if total_items % items_per_page > 0 else 0)
    page = st.number_input('Page', min_value=1, max_value=total_pages, value=1)
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    st.dataframe(df[filter_df][start_idx:end_idx])
elif menu == 'Bar Chart':
    st.title('Release Year By Bar Chat')
    df_count=df.groupby('Released_Year')['Series_Title'].value_counts().reset_index(name='Count')
    fig = px.bar(df_count, x='Released_Year', y='Count', title='Movies by Release Year')
    st.plotly_chart(fig,use_container_width=True)
elif menu == "Filter By Artist":
    st.title('Movies Filter by Artist')
    df['All_Stars'] = df[['Star1', 'Star2', 'Star3']].apply(lambda x: ', '.join(set(x.dropna())), axis=1)
    unique_stars = set()
    df[['Star1', 'Star2', 'Star3','Star3']].apply(lambda x: unique_stars.update(x.dropna()), axis=1)
    unique_stars = sorted(unique_stars)  # Sort the unique star names
    selected_star = st.selectbox('Select a Star', unique_stars)
    filter_df=df[['Star1', 'Star2', 'Star3','Star3']].apply(lambda x:selected_star in x.values,axis=1)
    st.dataframe(df.loc[filter_df, ['Series_Title', 'Released_Year','Genre','All_Stars']])
    
