import streamlit as st 
import pandas as pd 
import duckdb

st.write("Hello world")

data = {"a":[1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    query = st.text_area(label="entrez votre input")
    st.write(f"Vous avez entré la query suivante : {query}")

    result = duckdb.sql(query).df()
    st.write(result)
    
