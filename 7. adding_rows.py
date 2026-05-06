import pandas as pd
import sqlite3

data = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection) #gta is the name of the TABLE not db

#add rows
row = {"release_year": "2021",
       "release_name": "Natural Vision Evolved",
       "city": "Los Angeles"
       }
new_row_data = pd.concat([gta_data, pd.DataFrame([row])], ignore_index=True)
print(new_row_data)