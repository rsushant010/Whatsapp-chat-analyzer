import streamlit as st
import preprocessor,helper,backend,word_level_analysis
import matplotlib.pyplot as plt


import streamlit as st



# def homepage(df):
#     # fetching users in chat/data
#     userList = df['User'].unique().tolist()
#     userList.remove('mm')
#     userList.sort()
#     userList.insert(0,"Overall")

def homepage(df):
    # fetching users in chat/data
    
    userList = df['User'].unique().tolist()
    userList = [user for user in userList if user.lower() != 'group_notification']   
    
    # if 'group_notification' in userList:
    
    userList.remove('group_notification')
    userList.sort()
    userList.insert(0, "Overall")

# getting the value selected from drop down menu
    selected_user  = st.sidebar.selectbox('Get analysis for : ',userList)
    search_input = st.sidebar.text_input("Search in your chats:", "")
    search_button = st.sidebar.button("Show Analysis")

    # if search_button:
    #     backend.backend(selected_user,df)

    # if search_button:
    #     backend.backend(selected_user,df)

    if search_input and search_button:
        word_level_analysis.word_level(selected_user,search_input,df)

    elif search_button:
        backend.backend(selected_user,df)


    

    
