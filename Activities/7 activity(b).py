import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\SHANTRVRVU\Programs\Minors\IDA\Activities\Datasets\6\Mcd_null_values.csv")

print("Original DataFrame:")
print(df)

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values in all columns with mean (only numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataFrame after filling missing values:")
print(df)

# Check for duplicates
print("\nNumber of duplicate rows before dropping:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

print("\nDataFrame after dropping duplicates:")
print(df)
