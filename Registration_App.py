import streamlit as st
from deta import Deta

st.image('./LOGO_091622.png')
st.header('Eduardo Quin, Florida Notary Public')
st.subheader('Please answer the following questions and submit your request below')

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    email = st.text_input("Your email")
    telephone = st.number_input("Your phone number")
    one = st.text_input("What document(s) do you need notarized, deed, etc?")
    two = st.text_input("What is the timeframe you need the document(s) notarized, 1 day, 1 week?")
    three = st.text_input("Are you working with a lawyer, please provide lawyer's email?")
    
    submitted = st.form_submit_button("Submit your notarization request")
    clear_on_submit=True
    
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("Notary_Registration_App")

# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age, "email": email, "telephone": telephone, 
            "qe": one, "qf": two, "qg": three})
    if submitted:
        st.write("Your answers have been successfully received. For any questions or concerns please contact the office @ equin@assetmana.com. Please close your browser when you are finished.")
