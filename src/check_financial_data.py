import pandas as pd

# Load the S&P 500 data
sp500 = pd.read_csv("data/sp500.csv")

# Load the WTI crude oil data
wti = pd.read_csv("data/wti_crude_oil.csv")

print("S&P 500 Data")
print(sp500.head())
print("\nS&P 500 Shape:", sp500.shape)

print("\nWTI Crude Oil Data")
print(wti.head())
print("\nWTI Shape:", wti.shape)