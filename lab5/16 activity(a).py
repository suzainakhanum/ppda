#Activitiy_16(a)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("6Mcd.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Confirm column names
print("Columns in dataset:", df.columns.tolist())

# Sort by Year just in case
df = df.sort_values(by='Year')

# Check for missing values
print("\nMissing values:")
print(df[['Year', 'McDonalds_Revenue_$Billion']].isnull().sum())

# Matplotlib Line Chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['McDonalds_Revenue_$Billion'], marker='o', label='Revenue over Years')
plt.xlabel('Year')
plt.ylabel('Revenue ($ Billion)')
plt.title('McDonald\'s Revenue Over the Years (Matplotlib)')
plt.legend()
plt.grid(True)
plt.show()

# Seaborn Line Plot
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.lineplot(x='Year', y='McDonalds_Revenue_$Billion', data=df, marker='o')
plt.title('McDonald\'s Revenue Over the Years (Seaborn)')
plt.xlabel('Year')
plt.ylabel('Revenue ($ Billion)')
plt.grid(True)
plt.show()
