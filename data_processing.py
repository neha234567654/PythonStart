import pandas as pd

df = pd.read_csv("GOOGL_stock_data (1).csv")


print(df.head(5))        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.shape)         # (rows, columns)
print(df.columns)       # Column names
df.info()        # Data types + null counts
print(df.describe())    # Statistical summary
