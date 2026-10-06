import pandas as pd

# Load the datasets
sp500 = pd.read_csv("data/sp500.csv")
wti = pd.read_csv("data/wti_crude_oil.csv")

# Convert dates to datetime
sp500["observation_date"] = pd.to_datetime(sp500["observation_date"])
wti["observation_date"] = pd.to_datetime(wti["observation_date"])

# Remove missing values
sp500 = sp500.dropna()
wti = wti.dropna()

# Calculate S&P 500 statistics
sp500_start = sp500["SP500"].iloc[0]
sp500_end = sp500["SP500"].iloc[-1]
sp500_high = sp500["SP500"].max()
sp500_low = sp500["SP500"].min()
sp500_change = ((sp500_end - sp500_start) / sp500_start) * 100

# Calculate WTI statistics
wti_start = wti["DCOILWTICO"].iloc[0]
wti_end = wti["DCOILWTICO"].iloc[-1]
wti_high = wti["DCOILWTICO"].max()
wti_low = wti["DCOILWTICO"].min()
wti_change = ((wti_end - wti_start) / wti_start) * 100

# Display S&P 500 results
print("S&P 500 Analysis")
print("-----------------")
print(f"Start Price: {sp500_start:.2f}")
print(f"End Price: {sp500_end:.2f}")
print(f"Highest Price: {sp500_high:.2f}")
print(f"Lowest Price: {sp500_low:.2f}")
print(f"Overall Change: {sp500_change:.2f}%")

# Display WTI results
print("\nWTI Crude Oil Analysis")
print("----------------------")
print(f"Start Price: {wti_start:.2f}")
print(f"End Price: {wti_end:.2f}")
print(f"Highest Price: {wti_high:.2f}")
print(f"Lowest Price: {wti_low:.2f}")
print(f"Overall Change: {wti_change:.2f}%")