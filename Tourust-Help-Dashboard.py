#The problem statement was taken from the SIH Website

#Mian Page
import streamlit as st

create_page = st.Page("home.py", title="Home")
email_page = st.Page("email.py", title="E-Mail")
whatsapp_page = st.Page("whatapp.py", title="Message Us")
about_page = st.Page("about.py", title="About Us")
pg = st.navigation([create_page, email_page, whatsapp_page, about_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()

#Code which i added in homepage.py...............................................................................................................

import streamlit as st
st.title("Smart Tourist Safety Management")
st.write("Welcome to the page of Smart Tourist Safety Management")
st.write("-- Move to the E-mail Menu to write down the complaint to our team")
st.write("-- Move to the WhatApp Menu to send you compalint over there")
st.write("-- Naviagate to the Feedback menu to suggest us about the development that we can do at ground level make other tourists feel better")

#Codes that i used in Email.py......................................................................................................................

import streamlit as st
import smtplib
import ssl
st.header("Instructions about what you need to send Email to our team")
st.write("-- You must have a gmail account")
st.write("--You should also have App password if you don't have go and create one")

from email.message import EmailMessage
st.write("Fill out the form to Mail to our team")
EMAIL = st.text_input("Enter Your Email")
APP_PASSWORD = st.text_input("Enter Your APP PASSWORD")
RECIEVER = "namankraj2@gmail.com"
Sub = st.text_input("Enter the subject of your email")
content = st.text_area("Enter the Content of your email and prestt ctrl+Enter to Mail Us")
if st.button("Send Mail"):
    msg = EmailMessage()
    msg["from"] = EMAIL
    msg["To"] = RECIEVER
    msg["subject"] = Sub
    msg.set_content(f"{content}")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        st.success("Mail sent!")


#Codes that is used in Whatapp.py...........................................................................................................................................

import streamlit as st
import pywhatkit
st.header("Instructions about what you need to Message Us")
st.write("-- You must have login to whatsapp web to directly send us message")
message = st.text_input("Enter the message you wants to send")

if st.button("Send Message"):
    pywhatkit.sendwhatmsg_instantly(f"+91" , f"{message}")
    

#Codes that i used in about.py..................................................................................................................................................
import streamlit as st
st.title("Ministry of Development of North Eastern Region (MoDoNER)")
st.write("We are the ministry of development of Northe Eastern States aka Seven Sisters and we welcome you all on our")
st.write("-- We provide you the way to complain about the problems that you face in your way to cahnge and develop to make sure that will never happens to others")
st.write("-- Visit Touriststs Places and donot try to spread trash over there if you are facing more problems like this you can complain to use")


