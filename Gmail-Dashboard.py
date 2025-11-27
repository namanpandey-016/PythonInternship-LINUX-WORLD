#This dashboard will help you to send email
import streamlit as st

import smtplib
import ssl
from email.message import EmailMessage
st.header("SEND EMAIL FROM HERE")
st.title("You can send email from this dashboard all what you need to have APP PASSWOR and senders and recievers email")
EMAIL = st.text_input("Enter Your Email")
APP_PASSWORD = st.text_input("Enter Your APP PASSWORD")
RECIEVER = st.text_input("Enter Recievers Email")
Sub = st.text_input("Enter the subject of your email")
content = st.text_area("Enter the Content of your email")
msg = EmailMessage()
msg["from"] = EMAIL
msg["To"] = RECIEVER
msg["subject"] = Sub
msg.set_content(f"{content}")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
