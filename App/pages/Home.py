from operator import index
import py_compile
import streamlit as st 
import pandas as pd





st.markdown(
"""
This Application focuses on comparing the best playoff performances in the NBA of the past 20 seasons.

"""
)


nba_data = pd.read_csv('App/data-scraper/nba_playoff_players.csv')
nba_data_test = pd.DataFrame(nba_data)
st.dataframe(nba_data)

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """


st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
st.dataframe(nba_data)