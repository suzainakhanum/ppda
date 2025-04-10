import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler
data = pd.read_csv('3Salary_Data.csv')

salary_data = data[['Salary']]
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(salary_data)
data['Normalized_Salary'] = normalized_data

minmax_scaler = MinMaxScaler()
scaled_data = minmax_scaler.fit_transform(salary_data)
data['Scaled_Salary'] = scaled_data

data.to_csv('3Salary_Data_Scaled.csv', index=False)

print("Data has been normalized and scaled. Saved to '3Salary_Data_Scaled.csv'.")
