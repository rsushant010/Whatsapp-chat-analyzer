from urlextract import URLExtract

def fetch_num_msg(selected_user, data):
    if selected_user == "Overall":
        return data.shape[0]

    else:
        return data[data["User"] == selected_user].shape[0]


def fetch_words(selected_user, df):
    words = []
    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

        for message in df["Messages"]:
            words.extend(message.split())

        return len(words)

    else:
        for message in df["Messages"]:
            words.extend(message.split())
        return len(words)
    

def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df["User"] == selected_user]

    # stroing num of msg 
    num_msg = df.shape[0]

    # stroing num of words
    words = []
    
    # finding number of media shared
    media_omitted_count = df['Messages'].str.contains('<Media omitted>', na=False).sum()


    # finding no. of links shared and words used during convo
    extractor = URLExtract()
    urls = []

    for message in df["Messages"]:
        words.extend(message.split())

        urls.extend(extractor.find_urls(message))
    



    return num_msg , len(words), media_omitted_count , len(urls)
        

