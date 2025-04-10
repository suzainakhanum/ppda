import pandas as pd

data = pd.read_csv('4laptops.csv')

q1 = data['Screen_size_inches'].quantile(0.25)
q3 = data['Screen_size_inches'].quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = data[(data['Screen_size_inches'] < lower_bound) | (data['Screen_size_inches'] > upper_bound)]

print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
print(f"IQR Value: {iqr}")
print(f"Number of Outliers: {outliers.shape[0]}")
print("\nOutlier Rows:")
print(outliers)
