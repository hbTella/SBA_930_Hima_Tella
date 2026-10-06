import pandas as pd


def classify_direction(start, end):
    percent_change = ((end - start) / start) * 100

    if percent_change > 5:
        direction = "Increase"
    elif percent_change < -5:
        direction = "Decrease"
    else:
        direction = "Stable"

    return percent_change, direction


# Load 2024 data
gdp = pd.read_csv("data/gdp_2024.csv")
cpi = pd.read_csv("data/cpi_2024.csv")

# GDP direction
gdp_start = gdp["GDP_Growth"].iloc[0]
gdp_end = gdp["GDP_Growth"].iloc[-1]

gdp_change, gdp_direction = classify_direction(gdp_start, gdp_end)

# Inflation direction
inflation_start = cpi["Inflation"].iloc[0]
inflation_end = cpi["Inflation"].iloc[-1]

inflation_change, inflation_direction = classify_direction(
    inflation_start,
    inflation_end
)

print("2024 ECONOMIC TREND CLASSIFICATION")
print("----------------------------------")

print("\nGDP Growth:")
print(f"Start: {gdp_start:.2f}%")
print(f"End: {gdp_end:.2f}%")
print(f"Percentage change: {gdp_change:.2f}%")
print(f"Direction: {gdp_direction}")

print("\nInflation:")
print(f"Start: {inflation_start:.2f}%")
print(f"End: {inflation_end:.2f}%")
print(f"Percentage change: {inflation_change:.2f}%")
print(f"Direction: {inflation_direction}")