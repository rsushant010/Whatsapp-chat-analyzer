import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt


def backend(selected_user,df):
  
        num_stats, word_stats, media_stats, url_stats = helper.fetch_stats(selected_user,df)
         
        st.title("Top Statistics")
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



# displaying monthly activeness [we are not using temp_df as then we will not include media omitted but they are also important in our analysis]

        timeline = helper.activity_timeline(selected_user,df)
        
# weekly and monthly activity plot

        st.title("Monthly Timeline")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(timeline['Time'], timeline['Messages'], marker='o', linestyle='-', color='r')
        ax.set_xlabel('Time')
        ax.set_ylabel('Messages')
        ax.set_title('Messages Over Time')
        ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability
        # ax.grid(True)

        st.pyplot(fig) 


# plotting weekly and monthly activity
        st.title("Activity Map")
        col1 , col2 = st.columns(2)
        weekly_index, weekly_values , monthly_index, monthly_values = helper.activity_count(selected_user,df)
        
        with col1:
            st.title("Busy Days")
            fig, ax = plt.subplots()
            ax.bar(weekly_index, weekly_values)
            ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability
            st.pyplot(fig)

        with col2:
            st.title("Busy Months")
            fig, ax = plt.subplots()
            ax.bar(monthly_index, monthly_values, color = "orange")
            ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability
            st.pyplot(fig)

# displaying the dataframe
        st.title("Message Data Frame")
        if selected_user != "Overall":
            user_df = df[df['User'] == selected_user].reset_index(drop=True)
        else:
            user_df = df.reset_index(drop=True)

        # Adjust the index to start from 1
        user_df.index += 1

        # Display the DataFrame with the modified index
        st.dataframe(user_df)

        
# getting updated dataframe and top word list
# temp_df is the dataframe without media omitted values in it
        common_word_df,common_emoji_df,temp_df = helper.common_words(selected_user,df)

        

         
# creating wordcloud
        if common_word_df.shape[0] > 1 and temp_df.shape[0] > 1:
            wc_img = helper.wc_generator(temp_df)

            st.title("Wordcloud")
            fig,axes = plt.subplots(figsize = (4,6))
            # axes.imshow displays the previously generated image or graph
            axes.imshow(wc_img)

            st.pyplot(fig)


# plotting mostcommon words
        # st.dataframe(common_word_df)
            fig,ax = plt.subplots()

            ax.barh(common_word_df[0],common_word_df[1],color = "darksalmon")
            plt.xticks(rotation = 'vertical')

            st.title("Most Common Words")
            st.pyplot(fig)

        else :
            # st.title("Not Suffiecient Words Found to Plot WordCloud")
             st.write("Not enough words found to generate a meaningful word cloud. Please select another user with more textual content.")

# displaying most common emojis and plotting 
        if common_emoji_df.shape[0] > 0:
            st.title('Common Emojis List and Plot')
            col1, col2 = st.columns([1,3] , vertical_alignment="bottom")

            with col1:
                st.dataframe(common_emoji_df)

            with col2:
                fig,ax = plt.subplots()

                # ax.pie(common_emoji_df[1][:10], labels=common_emoji_df[0][:10], autopct="%0.2f")
                # st.pyplot(fig)

                ax.barh(common_emoji_df[0],common_emoji_df[1])
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)

        else :
            st.title("Not Enough Emojis Found To Plot")
       
