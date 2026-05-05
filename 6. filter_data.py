import pandas as pd
import sqlite3

data = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection) #gta is the name of the TABLE not db

first_5_rows = gta_data.head(5)
last_2_rows = gta_data.tail(2) #tail does last x rows

filtered_data = gta_data[gta_data["city"] == "Liberty City"]
replaced_city = gta_data.replace("Liberty City", "New York")
print(filtered_data)
print("***********************************************************************")
print(replaced_city)