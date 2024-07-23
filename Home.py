import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("EMMANUEL PATRICK")
    content = """Hi..I am Emmanuel,a passionate Python developer with a year of hands-on experience in building robust and scalable applications. With a background in computer science and a keen interest in problem-solving, John has honed his skills in Python development through various projects and continuous learning.

Over the past year, Emmanuel has worked on diverse projects ranging from web development to data analysis. He has a solid understanding of Python libraries such as Django, Flask, Pandas, and NumPy, which he has utilized to create efficient web applications and perform complex data manipulations.

    """

    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to contact me"""
st.write(content2)

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image('images/'+ row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
