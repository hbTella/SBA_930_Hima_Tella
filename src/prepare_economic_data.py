import pandas as pd


# Load GDP and CPI data
gdp = pd.read_csv("data/gdp.csv")
cpi = pd.read_csv("data/cpi.csv")


# Convert dates to datetime
gdp["observation_date"] = pd.to_datetime(gdp["observation_date"])
cpi["observation_date"] = pd.to_datetime(cpi["observation_date"])


# Calculate quarterly GDP growth
gdp["GDP_Growth"] = gdp["GDP"].pct_change() * 100


# Calculate year-over-year inflation using CPI
cpi["Inflation"] = cpi["CPIAUCSL"].pct_change(periods=12) * 100


# Historical data through December 31, 2023
gdp_historical = gdp[gdp["observation_date"] <= "2023-12-31"].copy()
cpi_historical = cpi[cpi["observation_date"] <= "2023-12-31"].copy()


# 2024 data kept separate for evaluation
gdp_2024 = gdp[
    (gdp["observation_date"] >= "2024-01-01")
    & (gdp["observation_date"] <= "2024-12-31")
].copy()

cpi_2024 = cpi[
    (cpi["observation_date"] >= "2024-01-01")
    & (cpi["observation_date"] <= "2024-12-31")
].copy()


# Save the prepared datasets
gdp_historical.to_csv("data/gdp_historical.csv", index=False)
cpi_historical.to_csv("data/cpi_historical.csv", index=False)

gdp_2024.to_csv("data/gdp_2024.csv", index=False)
cpi_2024.to_csv("data/cpi_2024.csv", index=False)


print("Economic data preparation complete.")
print("GDP historical rows:", len(gdp_historical))
print("GDP 2024 rows:", len(gdp_2024))
print("CPI historical rows:", len(cpi_historical))
print("CPI 2024 rows:", len(cpi_2024))