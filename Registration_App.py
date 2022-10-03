import streamlit as st
from deta import Deta

st.image('./LOGO_091622.png')

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    telephone = st.text_input("Your phone number")
    one = st.text_input("What do you need notarized, what documents, a deed, etc.?")
    two = st.text_input("Are you working with a lawyer, please provide your lawyer's email?")
    three = st.text_input("What is the timeline to notarize, do you need to notarize immediately?")
    submitted = st.form_submit_button("Thank you for submitting your request. We will send you an email with further instructions shortly.")
    clear_on_submit=True
    
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("Notary_Registration_App")

# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "email": email, "telephone": telephone, 
            "qe": one, "qf": two, "qg": three})
    if submitted:
        st.write("Your request for notarization has been successfully received. For any questions or concerns please contact the office @ equin@assetmana.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items