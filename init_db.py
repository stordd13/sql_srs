import io
import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# --------------------------------------------------------------
# EXERCICES LIST
# -------------------------------------------------------------- 

data = {
    "theme": ["cross_joins", "cross_joins"],
    "exercice_name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["1980-01-01", "1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state  AS SELECT * FROM memory_state_df")


# --------------------------------------------------------------
# CROSS JOIN EXERCICES 
# -------------------------------------------------------------- 

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""


CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

sizes = '''
size
XS
M
L
XL
'''

trademarks = '''
trademark
Nike
Asphalte
Abercrombie
Lewis
'''

beverages = pd.read_csv(io.StringIO(CSV))
food_items = pd.read_csv(io.StringIO(CSV2))
sizes = pd.read_csv(io.StringIO(sizes))
trademarks = pd.read_csv(io.StringIO(trademarks))

con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

con.close()
