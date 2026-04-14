import os 
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_text

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)
model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

def analyze_resume(pdf_doc,job_des):
    
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write(f'Text Extracted Successfully ✅️')
        
    else:
        st.warning('Error !! Drop the file in PDF format ⟳')
    
    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and provide ATS Score on scale of 0 to 100
                                       
                                       Generate the result in Bullet points (Maximum 5 Points)''')
    
    probability = model.generate_content(f'''Compre the given pdf {pdf_text} and given job description
                                         {job_des} and provied the probality to get short listed for the 
                                         given job description on scale 0 to 100 
                                         
                                         Generate the results in bullet points (maxium 5 points)''')
    
    resume_rating = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       Rate this resume as poor, moderate,
                                       good,very good
                                       Generate the results in bullet points (maxium 5 points)
                                       ''')
    skill_match = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des} and
                                       list all the skills that match and all the skills
                                       that does not match
                                       Generate the results in bullet points (maxium 5 points)
                                       ''')
    goodfit = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and check wheter the resume is suitable 
                                       for the JD if not then suggest any other 
                                       jobs
                                       Generate the results in bullet points (maxium 5 points)
                                       ''')
    swot = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and create a SWORT analysis of the candidate
                                       Generate the results in bullet points (maxium 5 points)
                                       ''')

    return (st.write(ats_score.text),
            st.write(probability.text),
            st.write(skill_match.text),
            st.write(resume_rating.text),
            st.write(goodfit.text),
            st.write(swot.text))
