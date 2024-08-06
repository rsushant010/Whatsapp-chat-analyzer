import homepage,preprocessor,helper,word_level_analysis,hpage2
import streamlit as st


# Set page configuration
st.set_page_config(page_title="Whatsapp Chat Analyzer", page_icon=":bar_chart:", layout="wide")

# Check if the page state is set to "NextPage"
if st.session_state.get("page") == "NextPage":
    # Call the backend function
    hpage2.backend()
else:
    # Header section
    st.title("Welcome to the Whatsapp Chat Analysis Homepage")
    st.markdown(
        """
        **Get started with analyzing your WhatsApp chat data!**

        This app lets you:
        - **Upload** a text file of your chat.
        - Perform **upto word-level analysis** to gain insights by entering word in search box.

        To proceed, click the **"Proceed"** button below.

        **How it works:**
        1. Upload your chat file.
        2. Click **"Proceed"** to start the analysis.
        3. **"If you do not want to upload a file then you can get analysis on a demo data(study group) uploaded already"**.

        """
    )


    # Add a button to proceed
    if st.button("Proceed Further"):
        st.session_state.page = "NextPage"  # Set the page to the next one
        st.rerun()  # Rerun the app to reflect the changes



    
    

