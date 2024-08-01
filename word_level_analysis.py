import streamlit as st
import backend
import matplotlib.pyplot as plt
import pandas as pd

def word_level(selected_user,search_input,df):
    if selected_user!= "Overall":
        df = df[df["User"] == selected_user]

    temp_df = pd.DataFrame()

    temp_df["Messages"] = df["Messages"].str.lower()
    search_input = search_input.lower()

    filtered_df = df[temp_df["Messages"].str.contains(search_input, na=False)]

    backend.backend(selected_user,filtered_df)
    

    