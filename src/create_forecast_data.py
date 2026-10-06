import pandas as pd

# Load the datasets
sp500 = pd.read_csv("data/sp500.csv")
wti = pd.read_csv("data/wti_crude_oil.csv")

# Convert dates
sp500["observation_date"] = pd.to_datetime(sp500["observation_date"])
wti["observation_date"] = pd.to_datetime(wti["observation_date"])

# Remove missing values
sp500 = sp500.dropna()
wti = wti.dropna()

# Use data through December 2023 as historical data
sp500_history = sp500[sp500["observation_date"] <= "2023-12-31"]
wti_history = wti[wti["observation_date"] <= "2023-12-31"]

# Use 2024 as the period we will use to evaluate the forecasts
sp500_evaluation = sp500[
    (sp500["observation_date"] >= "2024-01-01")
    & (sp500["observation_date"] <= "2024-12-31")
]

wti_evaluation = wti[
    (wti["observation_date"] >= "2024-01-01")
    & (wti["observation_date"] <= "2024-12-31")
]

print("S&P 500 Historical Data")
print("Rows:", len(sp500_history))
print("Last date:", sp500_history["observation_date"].max())
print("Last value:", sp500_history["SP500"].iloc[-1])

print("\nS&P 500 Evaluation Data")
print("Rows:", len(sp500_evaluation))
print("First date:", sp500_evaluation["observation_date"].min())
print("Last date:", sp500_evaluation["observation_date"].max())

print("\nWTI Historical Data")
print("Rows:", len(wti_history))
print("Last date:", wti_history["observation_date"].max())
print("Last value:", wti_history["DCOILWTICO"].iloc[-1])

print("\nWTI Evaluation Data")
print("Rows:", len(wti_evaluation))
print("First date:", wti_evaluation["observation_date"].min())
print("Last date:", wti_evaluation["observation_date"].max())