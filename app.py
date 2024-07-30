import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt



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
         
        col1, col2, col3, col4 = st.columns([1.2,1,1,1])
        # values inside these braces are the width of column respectively 

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
            col1, col2 = st.columns(2)

            # Create a figure and axes for the first plot
            fig1, ax1 = plt.subplots()
            x, new_df = helper.busy_user(df)

            with col1:
                # Plot the bar chart
                ax1.bar(x.index, x.values, color='red')
                ax1.set_xticks(x.index)
                ax1.set_xticklabels(x.index, rotation='vertical')
                st.pyplot(fig1)

            # Create a figure and axes for the second plot
            fig2, ax2 = plt.subplots()

            with col2:
                # Plot the pie chart
                ax2.pie(x, labels=x.index, autopct="%0.2f")
                st.pyplot(fig2)

            # Display the dataframe
            # st.dataframe(new_df)


# getting updated dataframe and top word list
        common_word_df,updated_df = helper.common_words(selected_user,df)


# creating wordcloud
        wc_img = helper.wc_generator(updated_df)

        fig,axes = plt.subplots()
        # axes.imshow displays the previously generated image or graph
        axes.imshow(wc_img)

        st.pyplot(fig)

# plotting mostcommon words
        # st.dataframe(common_word_df)
        fig,ax = plt.subplots()

        ax.barh(common_word_df[0],common_word_df[1])
        plt.xticks(rotation = 'vertical')

        st.title("Most Common Words")
        st.pyplot(fig)

        
        
            

                
