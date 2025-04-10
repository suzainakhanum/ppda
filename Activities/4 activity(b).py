import pandas as pd

# Read the CSV file
df = pd.read_csv("2experience.csv")

# 1. Display the last 3 rows only
print("Last 3 rows of the dataframe:")
print(df.tail(3))

# 2. Display description and info of the dataframe
print("\nDataFrame Description:")
print(df.describe())

print("\nDataFrame Information:")
print(df.info())

# 3. Display column names
print("\nColumn Names:")
print(df.columns.tolist())
