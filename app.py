import streamlit as st
import base64

# Set the background color: blue
st.set_page_config(
    page_title="The Official Webpage of Kazi",
    page_icon=":crescent_moon:",
    layout="wide",
    initial_sidebar_state="auto",
)

# st.markdown("""
#     <style>
#         .stApp {
#         background: url("https://static.vecteezy.com/system/resources/thumbnails/007/243/548/small/boxing-ring-background-concept-free-vector.jpg");
#         background-size: cover;
#         }
#     </style>""", unsafe_allow_html=True)

# Page Title and Introduction
st.title('Software Engineer | Data Engineer | Instructor | Student')
st.write("Welcome to my official webpage. This is where I share my experiences and skills with the world. I hope to learn "
         "from you as well so please feel free to reach out to me at the contact section below.")

# Video Section
st.header('Behind the Screen :movie_camera:')
st.video('https://www.youtube.com/watch?v=-kjk34xfZVU')


# Projects Section (you can add your projects with descriptions and links)
st.header('Snapshot :camera_with_flash:')
st.write("My name is Kazi and I was born and raised in NYC. I'm a software engineer with experience in the Electronics "
         "and Financial industries. I specialize in backend development including automation, data pipelines, "
         "data-as-a-service, API service and backend web applications. I am an expert in Python and SQL having production "
         "experience with Django, PySpark, Airflow, DBT, and PL-SQL. I have deployed AWS services to production including "
         "CloudFormation, Lambda, EC2, SQS, SNS, Redis Clusters, DynamoDB, and S3.")
st.write("Outside of my professional and personal tech pursuits, I enjoy tutoring. I have over 7 years of experience in "
         "tutoring students elementary writing to graduate data science courses. I am a passionate learner and love to "
         "teach others what I've learned. In my spare time, I enjoy training/exercising and watching UFC, "
         "English Premier League and NBA.")

# Resume Section
st.header('Resume')
resume_path = 'C:/Users/Anabil/Downloads/Kazi_Islam_Resume (2).pdf'
with open(resume_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)

# Connect with Me Section
st.header("Connect with Me")
st.write(f"- [:link: LinkedIn](https://www.linkedin.com/in/kaziislam2/)")
st.write(f"- [:link: GitHub](https://github.com/kzunayed)")
