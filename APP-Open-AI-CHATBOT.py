#Dashboard for open ai chatbo
import streamlit as st
import google.generativeai as genai
key = "AIzaSyChmitMjN0DL9cOz197bpEw3tbsjnmYFmc"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")
st.header("AI Bot")
st.write("You can ask me whatever you wnats to ask")
user = st.chat_input("Heii, How are you Doin'")

if user:
    st.chat_message("user")
    st.markdown(user)
    
    st.chat_message("Assistant")
    response = model.generate_content(user)
    st.markdown(response.text)
    
    
