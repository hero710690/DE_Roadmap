import pandas as pd

# Sample data
data = {
    'Product': ['Shoes', 'Shirt', 'Socks', 'Jacket', 'Pants'],
    'TargetDemographic': ['Men', 'Women', 'Men', 'Women', 'Men'],
    'Price': [100, 85, 15, 120, 60]
}

df = pd.DataFrame(data, columns=['Product', 'TargetDemographic','Price'])
df.groupby('TargetDemographic')['Price'].mean()