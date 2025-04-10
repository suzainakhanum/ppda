import pandas as pd

# Read the CSV file
df = pd.read_csv("1experience.csv")

# 1. Display the content of the file
print("1. Content of the file:")
print(df)

# 2. Find the total number of rows and columns
print("\n2. Total number of rows and columns:")
print(df.shape)

# 3. Calculate the length of the dataframe
print("\n3. Length of the dataframe:")
print(len(df))

# 4. Display the first 2 rows only
print("\n4. First 2 rows of the dataframe:")
print(df.head(2))
