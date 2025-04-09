import pandas as pd

# List of dictionaries
products = [
    {'Product Name': 'Laptop', 'Category': 'Electronics', 'Price': 60000},
    {'Product Name': 'Chair', 'Category': 'Furniture', 'Price': 3000},
    {'Product Name': 'Watch', 'Category': 'Accessories', 'Price': 2500},
    {'Product Name': 'Smartphone', 'Category': 'Electronics', 'Price': 20000}
]

# Creating DataFrame
df = pd.DataFrame(products)

# Adding discounted price (90% of original)
df['Discounted Price'] = df['Price'] * 0.9

# Displaying the DataFrame
print("Final DataFrame with Discounted Price:")
print(df)
