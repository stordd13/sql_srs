import io
import os 
import logging

import duckdb
import pandas as pd
import streamlit as st


if "data" not in os.listdir():
  
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")
if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=True)


with st.sidebar:
    theme = st.selectbox(
        "What would you like to revise ?",
        ["cross_joins", "Groupby", "window_functions"],
        index=None,
        placeholder="Select a theme ...",
    )  
    st.write("You selected :", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'").df().sort_values("last_reviewed").reset_index()
    st.write(exercice)

    exercice_name = exercice.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}.sql", 'r') as f:
        answer = f.read()
    solution_df = con.execute(answer).df()


st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query: 
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))

    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:

    exercice_tables = exercice.loc[0, "tables"]
    for table in exercice_tables: 
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
   
        st.dataframe(df_table)

#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solution_df)

with tab3:

    st.write(answer)
