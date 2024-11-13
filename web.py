import streamlit as st
import pandas
from pandas import wide_to_long

st.set_page_config(layout='wide')

col1, empty  = st.columns(2)

with col1:
    st.title("The Best Company")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    st. write(content)
    st.header("Our Team")

col2, col3, col4 = st.columns(3)

#data frame column1
df = pandas.read_csv('data.csv', sep=',')
with col2:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/"+ row['image'])

with col3:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("images/"+ row['image'])


with col4:
    for index, row in df[8:12].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])
