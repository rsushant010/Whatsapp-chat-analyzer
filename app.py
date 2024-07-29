import streamlit as st
import preprocessor,helper

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # using utf-8 decoding
    data = bytes_data.decode('utf-8')

    # shows all the data in text format
    # st.text(data)

    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # fetching users in chat/data
    userList = df['User'].unique().tolist()
    userList.remove('group_notification')
    userList.sort()
    userList.insert(0,"Overall")

    # getting the value selected from drop down menu
    selected_user  = st.sidebar.selectbox('Get analysis for : ',userList)

    if st.sidebar.button("Show Analysis"):
        num_stats, word_stats, media_stats, url_stats = helper.fetch_stats(selected_user,df)
         
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Messages")
            st.title(num_stats)

        with col2:
            st.header("Words")
            st.title(word_stats)

        with col3:
            st.header("Media")
            st.title(media_stats)

        with col4:
            st.header("URL")
            st.title(url_stats)


# creating new columns for list of busiest user and visualization
        if selected_user == "Overall":
            st.title("Busiest Users")
            st.columns(2)
