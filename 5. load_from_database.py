import pandas as pd
import sqlite3

data = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")
gta_data = pd.read_sql("select * from gta", connection) #gta is the name of the TABLE not db
print(gta_data.head(5)) #tail does last x rows