#All you need to do is run this to generate a DB file.

import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]    

cursor.execute("create table gta (release_year integer, release_name text, city text)")#creates a table
cursor.executemany("insert into gta values (?,?,?)", release_list) #inserts info into a table
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"}) #selects certain criteria- look in city column for anything mentioning liberty city
gta_search = cursor.fetchall()

for row in cursor.execute("select * from gta"):  #print whole table
    print(row)
print("********************************************************************")
print(gta_search) #print whole table
print("********************************************************************")

city_list = [("Los Santos", "Los Angeles"),
             ("Liberty City", "New York"),
             ("Vice City", "Miami"),
             ("San Andreas", "San Francisco")          
            ]
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.executemany("insert into cities values (?,?)", city_list)
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()

for row in cursor.execute("select * from cities"):
    print(row)
print("********************************************************************")
print(cities_search)
print("********************************************************************")

for i in gta_search:
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
print(adjusted)

connection.commit()
connection.close()