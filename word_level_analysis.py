import streamlit as st
import backend
import matplotlib.pyplot as plt

def word_level(selected_user,search_input,df):
    if selected_user!= "Overall":
        df = df[df["User"] == selected_user]

    df["Messages"] = df["Messages"].str.lower()
    search_input = search_input.lower()

    filtered_df = df[df['Messages'].str.contains(search_input, na=False)]

    backend.backend(selected_user,filtered_df)
    

    