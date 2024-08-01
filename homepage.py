import streamlit as st
import preprocessor,helper,backend,word_level_analysis
import matplotlib.pyplot as plt


import streamlit as st

def show_intro_page():
    
    st.title("Welcome to the WhatsApp Chat Analysis App")

    st.markdown(
        """
        **Get started with analyzing your WhatsApp chat data!**

        This app lets you:
        - **Upload** a text file of your chat.
        - Perform **word-level analysis** to gain insights.

        To proceed, click the **"Proceed"** button below.

        **How it works:**
        1. Upload your chat file.
        2. Click **"Proceed"** to start the analysis.

        """
    )
    if st.button("Proceed"):
        # Set a flag in session state to indicate that the intro page has been seen
        st.session_state.show_intro = False
        # Use st.experimental_rerun to reload the app and display the analysis page
        st.experimental_rerun()

# Initialize session state if it does not exist
if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

# Reset the intro page flag on each reload
if st.session_state.show_intro:
    show_intro_page()



def homepage(df):
    # fetching users in chat/data
    userList = df['User'].unique().tolist()
    userList.remove('group_notification')
    userList.sort()
    userList.insert(0,"Overall")

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


    

    