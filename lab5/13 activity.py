import pandas as pd

# Employee Data
details = pd.DataFrame({'EmployeeID': [101,102,103,104,105],
                        'Name': ['Alice','Bob','Charlie','David','Eva'],
                        'Department': ['HR','Engineering','Engineering','HR','Marketing']})
salaries = pd.DataFrame({'EmployeeID': [101,102,103,104,105],
                         'Salary': [50000,70000,80000,55000,60000]})

# Median Salary per Department
print("\n Median Salary per Department:")
print(pd.merge(details, salaries).groupby('Department')['Salary'].median())

# Outer Merge
print("\n Outer Merged Data:")
print(pd.merge(details, salaries, how='outer'))

# Stock & Market Data joined by Date
dates = pd.date_range('2024-01-01', periods=5)
stocks = pd.DataFrame({'Date': dates, 'Price': [150,155,152,158,160]}).set_index('Date')
volume = pd.DataFrame({'Date': dates, 'Volume': [1000,1100,1050,1150,1200]}).set_index('Date')
print("\n Joined Stock & Volume:")
print(stocks.join(volume))

# Horizontal Sales Concatenation
north = pd.DataFrame({'Date': dates, 'Region': 'North', 'Sales': [250,300,200,400,350]})
south = pd.DataFrame({'Sales': [300,320,280,360,310]})
print("\n Horizontally Concatenated Sales:")
print(pd.concat([north.reset_index(drop=True), south.rename(columns={'Sales': 'South_Sales'})], axis=1))
