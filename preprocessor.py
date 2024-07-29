import pandas as pd
import re


def preprocess(data):

    # pattern to extract text part
    pattern_text = r'-\s*(.*)'
    messages = re.findall(pattern_text, data)

    # pattern to extract date & time part
    pattern_date = r'(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2})\s([A-Za-z]{2})'

    dates = (re.findall(pattern_date, data))
    datetime = [f"{date} {time} {period}" for date, time, period in dates]
    datetime = pd.to_datetime(datetime, format='%m/%d/%y %I:%M %p')

    # creating dataframe
    df = pd.DataFrame({'DateTime': datetime, 'Messages': messages})

    # function to extract name and chat
    users = []
    messages = []

    def extractor(msg):
        entry = re.split(':', msg, maxsplit=1)
        # print('entry1 :',len(entry))
        if len(entry) > 1:  # user name
            # print('entry1 :',entry[1])
            users.append(entry[0])
            messages.append(" ".join(entry[1:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['Messages'] = df['Messages'].apply(extractor)

    df['User'] = users
    df['Messages'] = messages

    df['Day'] = df['DateTime'].dt.day
    df['Hour'] = df['DateTime'].dt.hour
    df['Min'] = df['DateTime'].dt.minute
    df['Month'] = df['DateTime'].dt.month_name()
    df['Year'] = df['DateTime'].dt.year

    # reordering all the columns
    neworder = ['Day', 'Month', 'Year', 'Hour', 'Min', 'DateTime', 'User', 'Messages']
    df = df.reindex(columns=neworder)

    return df