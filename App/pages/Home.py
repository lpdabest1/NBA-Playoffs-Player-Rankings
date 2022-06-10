from operator import index
import py_compile
import streamlit as st 
import pandas as pd
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string().decode("utf-8")
    return content

bucket_name = "nba-playoff-player-data"
file_path = "nba_playoff_players.csv"

content = read_file(bucket_name, file_path)

# Print results.
for line in content.strip().split("\n"):
    name, pet = line.split(",")
    st.write(f"{name} has a :{pet}:")


st.markdown(
"""
This Application focuses on comparing the best playoff performances in the NBA of the past 20 seasons.

"""
)


nba_data = pd.read_csv('App/data-scraper/nba_playoff_players.csv')
nba_data_test = pd.DataFrame(nba_data)
st.write("non-google dataframe")
st.dataframe(nba_data)

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """


#st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
#st.dataframe(nba_data)