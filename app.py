import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

GOOGLE_API_KEY="AIzaSyBRbNiXR1ANu9zcUFt_2YwIRm2BXAFPpCE"

from dotenv import load_dotenv
load_dotenv() # load all the environemtn variables
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)
               
               
               
## Gemini Pro Response 

def get_gemini_response(input):
    model=genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        #page = reader.pages[page]
        text+=str(page.extract_text())
    return text

## Prompt Template
input_prompt = """Hey Act like a skilled or very experience ATS (Application Tracking System )
with a deep understanding of Process Automation field, RPA Tool Automation Anywhere 360 Developer.
Your task is to evaluate the resume based on the given Job 
Description.
You must consider the job market is very competitive and you should provide best 
assistance for improving the resumes. Assign the percentage Matching based on JD with resume and also with high accuracy
Resume : {text}
Description :{jd}

I want the response in one single string having the structure
{{"JD Match}:"%", "MissingKeywords :[]", "Profile Summary":""}
"""
##Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="please upload the pdf")
submit = st.button("Submit")


if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)
        
