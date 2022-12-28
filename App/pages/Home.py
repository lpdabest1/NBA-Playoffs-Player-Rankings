from operator import index
import py_compile
import streamlit as st 
import pandas as pd
import csv



st.markdown(
"""
This Application focuses on comparing the best playoff performances in the NBA of the past 20 seasons.

"""
)



nba_data = pd.read_csv("App/pages/nba_playoff_players.csv")
nba_data_test = pd.DataFrame(nba_data)
st.write("This dataframe allows for user input when wanting to view data according to a specific year. Note: The default is 2021.")


# User input for correct season to select for playoff statistics
current_year = 2022
st.sidebar.header('User Customization')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2006,2022))))


if selected_year in nba_data_test.Season:
    st.dataframe(nba_data_test[nba_data_test['Season'] == selected_year])

#st.dataframe(nba_data)


#st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
#st.dataframe(nba_data)

