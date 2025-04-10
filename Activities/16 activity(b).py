
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("6Mcd.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Scatter plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(df['Growth_rate_percent'], df['McDonalds_Revenue_$Billion'], color='blue')
plt.xlabel('Growth Rate (%)')
plt.ylabel('Revenue ($ Billion)')
plt.title('Scatter Plot of Growth Rate vs Revenue (Matplotlib)')
plt.grid(True)
plt.show()

# Scatter plot using Seaborn
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")
sns.scatterplot(x='Growth_rate_percent', y='McDonalds_Revenue_$Billion', data=df, color='green')
plt.title('Scatter Plot of Growth Rate vs Revenue (Seaborn)')
plt.xlabel('Growth Rate (%)')
plt.ylabel('Revenue ($ Billion)')
plt.grid(True)
plt.show()
