from urlextract import URLExtract
from wordcloud import WordCloud
import string
from collections import Counter
import pandas as pd
import emoji


def n():
    # def fetch_num_msg(selected_user, data):
    #     if selected_user == "Overall":
    #         return data.shape[0]

    #     else:
    #         return data[data["User"] == selected_user].shape[0]


    # def fetch_words(selected_user, df):
    #     words = []
    #     if selected_user != "Overall":
    #         df = df[df["User"] == selected_user]

    #         for message in df["Messages"]:
    #             words.extend(message.split())

    #         return len(words)

    #     else:
    #         for message in df["Messages"]:
    #             words.extend(message.split())
    #         return len(words)
    pass

def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

    # stroing num of msg 
    num_msg = df.shape[0]

    # stroing num of words
    words = []
    
    # finding number of media shared
    # media_omitted_count = df['Messages'].str.contains('<Media omitted>', na=False).sum()
    media_omitted_count = df['Messages'].astype(str).str.contains('<Media omitted>', na=False).sum()



    # finding no. of links shared and words used during convo
    extractor = URLExtract()
    urls = []

    for message in df["Messages"]:
        words.extend(message.split())

        urls.extend(extractor.find_urls(message))
    
    return num_msg , len(words), media_omitted_count , len(urls)
        


# group level analysis finding busiest user
def busy_user(df):
    # top 5 user stored in x 
    x = df['User'].value_counts().head()

    df = round((df['User'].value_counts()/df.shape[0])*100 , 2).reset_index().rename(columns = {"count": "Percentage"})

    return x,df



# method for most common words and emojis

def common_words(selected_user,df):

    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

    # removing group notification
    temp = df[df['User'] != 'group_notification']
    # removing media ommited message
    temp = temp[~temp['Messages'].str.contains('<Media omitted>', na=False)].reset_index()

    word_list = []
    emoji_list = []

    try:
        f = open('stop_hinglish.txt' , 'r')
        stop_words = f.read()

        for text in temp["Messages"]:
            for word in text.lower().split():
                # checking for stopwords and punctuation
                if word not in stop_words and word not in string.punctuation:
                    word_list.append(word)

                # checking for emojis present in data
                if word in emoji.EMOJI_DATA:
                    emoji_list.extend(word)


    except Exception as e:
        raise RuntimeError("An error occurred") from e
    
    return_df_word = pd.DataFrame(Counter(word_list).most_common(20))
    return_df_emoji = pd.DataFrame(Counter(emoji_list).most_common(20))
    
    return  return_df_word, return_df_emoji, temp


# method to create wordcloud
def wc_generator(df):

    wc = WordCloud(width=300,height=300,min_font_size=10,background_color='white')

    # word cloud will be formed from messages column in df where 

    wc_df = wc.generate(df["Messages"].str.cat(sep = " "))

    # .str.cat(sep=" "): This method concatenates all strings in the column into a single string, using the separator specified by sep. In this case, sep=" " means that each string will be separated by a space.

    return wc_df



# method to create lineplot showing their activeness in group or text

def activity_timeline(selected_user , df):

    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

    
    timeline = df.groupby(["Month","Month_num","Year"]).count()["Messages"].reset_index()
    timeline = timeline.sort_values(by = ["Year","Month_num"]).reset_index(drop = True)
    timeline['Year'] = timeline['Year'].astype(str)
    timeline['Time'] = timeline['Month'] + "-" + timeline['Year']

    return timeline


def activity_count(selected_user , df):
    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

    monthly_index = df["Month"].value_counts().index
    monthly_values = df["Month"].value_counts().values

    weekly_index = df["Week_Day"].value_counts().index
    weekly_values = df["Week_Day"].value_counts().values

    return  weekly_index, weekly_values , monthly_index, monthly_values


    
