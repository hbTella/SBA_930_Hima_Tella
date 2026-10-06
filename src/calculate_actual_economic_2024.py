import pandas as pd

# Load the actual 2024 economic data
gdp = pd.read_csv("data/gdp_2024.csv")
cpi = pd.read_csv("data/cpi_2024.csv")

# GDP statistics
gdp_start = gdp["GDP_Growth"].iloc[0]
gdp_end = gdp["GDP_Growth"].iloc[-1]
gdp_average = gdp["GDP_Growth"].mean()

# Inflation statistics
inflation_start = cpi["Inflation"].iloc[0]
inflation_end = cpi["Inflation"].iloc[-1]
inflation_average = cpi["Inflation"].mean()

print("2024 ACTUAL ECONOMIC RESULTS")
print("----------------------------")

print("\nGDP Growth:")
print(f"Starting 2024 growth: {gdp_start:.2f}%")
print(f"Ending 2024 growth: {gdp_end:.2f}%")
print(f"Average 2024 growth: {gdp_average:.2f}%")

print("\nInflation:")
print(f"Starting 2024 inflation: {inflation_start:.2f}%")
print(f"Ending 2024 inflation: {inflation_end:.2f}%")
print(f"Average 2024 inflation: {inflation_average:.2f}%")

print("\nGDP 2024 data:")
print(gdp[["observation_date", "GDP_Growth"]].to_string(index=False))

print("\nInflation 2024 data:")
print(cpi[["observation_date", "Inflation"]].to_string(index=False))