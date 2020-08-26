import pandas
filename = "FB-NASDAQ-data.csv"
df= pandas.read_csv(filename)
print(df)

highs = df.High
print(highs)

value_august25 = highs[0]
print("Value on August 25, 2020:")
print(value_august25)
