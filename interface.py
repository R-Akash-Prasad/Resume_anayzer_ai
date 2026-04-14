import streamlit  as st
from analysis import analyze_resume

st.set_page_config('Resume Analyzer',page_icon='🛠️')

st.title('RESUME ANALYZER USING AI 👨🏾‍💻')
st.header(f':blue[AI Powered Resume Analyzer with given job description using AI 🤖🧠🇦🇮👾]')
st.subheader('This page helps you to compare the resume and the given job description and provide ATS , Probality and SWOT Analysis')

st.sidebar.subheader('DROP YOUR RESUME HERE 📝')

pdf_doc = st.sidebar.file_uploader('Click here',type=['PDF'])

st.sidebar.markdown('DESIGNED BY AKASH PRASAD')
st.sidebar.markdown('GIT HUB : https://github.com/R-Akash-Prasad/Resume_anayzer_ai.git')

job_des = st.text_area('Copy And Paste the JD here ✍🏻 ' , max_chars=10000)

submit = st.button('GET RESULTS 🎯')

if submit:
    with st.spinner('Loading.....'):
        analyze_resume(pdf_doc , job_des)