import pandas as pd

column = ["Louis", "John", "Jeremy"]
titled_column= {"name": column,
                "height": [1.67, 1.9, 0.25],
                "weight": [54, 100, 1]}
data = pd.DataFrame(titled_column)
select_column = data["weight"][1]
select_row = data.iloc[1]["weight"]
print(data)
print(select_column)
print(select_row)