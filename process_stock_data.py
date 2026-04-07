import numpy as np
import pandas as pd

# Load CSV file
filename = 'GOOGL_stock_data (1).csv'
data = pd.read_csv(filename)

# Convert relevant columns to numpy arrays
close_prices = data['Close'].values
volume = data['Volume'].values

# Example: Calculate mean and std of Close prices
mean_close = np.mean(close_prices)
std_close = np.std(close_prices)

# Example: Calculate correlation between Close price and Volume
correlation = np.corrcoef(close_prices, volume)[0, 1]

print(f"Mean Close Price: {mean_close:.4f}")
print(f"Std Close Price: {std_close:.4f}")
print(f"Correlation (Close vs Volume): {correlation:.4f}")
