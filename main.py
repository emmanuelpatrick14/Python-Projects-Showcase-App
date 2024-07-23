import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("EMMANUEL PATRICK")
    content = """Hi..I am Emmanuel,a passionate Python developer with a year of hands-on experience in building robust and scalable applications. With a background in computer science and a keen interest in problem-solving, John has honed his skills in Python development through various projects and continuous learning.

Over the past year, Emmanuel has worked on diverse projects ranging from web development to data analysis. He has a solid understanding of Python libraries such as Django, Flask, Pandas, and NumPy, which he has utilized to create efficient web applications and perform complex data manipulations.

    """
    st.write(content)
