import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from streamlit.components.v1 import html
import os

load_dotenv()

def generate_email(business_details, email_prompt):
    model = ChatOpenAI(model="gpt-3.5-turbo")



    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert email writer. Your job is to manage user's email account. These are the details of the user: {user_details} You have to write a short personalized and human written email based on the prompt provided by the user keeping in mind all the user details provided to you."),
    ("human", "email to ask employee what are the revenue figures of the last month."),
    ("ai", "Subject: Request for Last Month's Revenue Figures\n\nDear [Employee's Name],\nI hope this message finds you well.\nAs we prepare for the upcoming financial review, could you please provide me with the revenue figures for the last month? Having a detailed and accurate understanding of our financial performance is crucial for our strategic planning and reporting.\nCould you please send me the figures by [specific date or deadline]? If you need any further details or assistance in gathering this information, please let me know.\nThank you for your attention to this matter and your continued dedication.\n\nBest regards,\nAmsal Uzair"),
    ("human", "{user_input}"),
])




    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    email_body = (chain.invoke({"user_details":business_details,
                    "user_input":email_prompt}))

    return email_body

st.title('📧 Email Generator App')

# User inputs

business_details = st.sidebar.text_area("Enter your business details:", height=150)
email_prompt = st.text_input("Enter the subject or prompt for your email:")

if st.button('Generate Email'):
    if business_details and email_prompt:
        email = generate_email( business_details, email_prompt)
        st.text_area("Generated Email:", value=email, height=300)

        url = 'https://mail.google.com/mail/u/0/#inbox?compose=new'

# Create a hyperlink button using Markdown
        st.markdown(f'<a href="{url}" target="_blank"><button style="color: white; background-color: #78BBFF; border: none;  border-radius: 10px; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font: Source Sans Pro; font-size: 16px; margin: 4px 2px; cursor: pointer;">MAIL IT!</button></a>', unsafe_allow_html=True)

    else:
        st.error("Please fill all the fields to generate an email.")

