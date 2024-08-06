import streamlit as st
import homepage,preprocessor,helper,word_level_analysis


def backend():
      
    
        # setting default path for text file
        DEFAULT_DATASET_PATH = 'WhatsApp Chat with PPC ( PCC Proper Cricket club).txt'

        st.sidebar.title("Whatsapp Chat Analyzer")

        # File uploader widget
        uploaded_file = st.sidebar.file_uploader("Choose a text file")

        # file uploading here

        if uploaded_file is None:
            # Use default dataset if no file is uploaded
            with open(DEFAULT_DATASET_PATH, 'r', encoding='utf-8') as file:
                data = file.read()

        # Check if a file is uploaded
        elif uploaded_file is not None:
            # Read file as bytes
            bytes_data = uploaded_file.getvalue()
            # Decode bytes to string
            data = bytes_data.decode('utf-8')


            # shows all the data in text format
            # st.text(data)
        df = preprocessor.preprocess(data)
            # st.dataframe(df)
            # there is no need to print the dataframe


        # calling function to make webpage interactive
        if df is not None:
            homepage.homepage(df)

