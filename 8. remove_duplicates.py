import pandas as pd
import sqlite3

connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection)
duplicates = gta_data[gta_data.duplicated(subset=["city"], keep=False)]
print("*******Full Data*******")
print(gta_data)
print("*******Duplicates*******")
print(duplicates)
print(f"There are {len(duplicates)} repeated items")
