import pandas as pd

column = ["Louis", "John", "Jeremy"]
titled_column= {"name": column,
                "height": [1.67, 1.9, 0.25],
                "weight": [54, 100, 1]}
data = pd.DataFrame(titled_column)
select_column = data["weight"][1]
select_row = data.iloc[1]["weight"]

bmi = []
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi
print(data)

#save to file
data.to_csv("bmi.csv", index=False, sep="\t")