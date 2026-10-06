import pandas as pd


# Load historical economic data
gdp = pd.read_csv("data/gdp_historical.csv")
cpi = pd.read_csv("data/cpi_historical.csv")


# Convert dates
gdp["observation_date"] = pd.to_datetime(gdp["observation_date"])
cpi["observation_date"] = pd.to_datetime(cpi["observation_date"])


# Get the 2023 data
gdp_2023 = gdp[gdp["observation_date"].dt.year == 2023]
cpi_2023 = cpi[cpi["observation_date"].dt.year == 2023]


# Calculate historical GDP growth statistics
gdp_growth = gdp["GDP_Growth"].dropna()

gdp_start = gdp_growth.iloc[0]
gdp_end = gdp_growth.iloc[-1]
gdp_high = gdp_growth.max()
gdp_low = gdp_growth.min()
gdp_2023_avg = gdp_2023["GDP_Growth"].mean()


# Calculate historical inflation statistics
inflation = cpi["Inflation"].dropna()

inflation_start = inflation.iloc[0]
inflation_end = inflation.iloc[-1]
inflation_high = inflation.max()
inflation_low = inflation.min()
inflation_2023_avg = cpi_2023["Inflation"].mean()

inflation_jan_2023 = cpi_2023.iloc[0]["Inflation"]
inflation_dec_2023 = cpi_2023.iloc[-1]["Inflation"]


# Create the LLM input
llm_input = f"""
ECONOMIC DATA SUMMARY

Historical data cutoff: December 31, 2023
Forecast period: January 1, 2024 to December 31, 2024

U.S. GDP GROWTH:
Historical starting quarterly growth: {gdp_start:.2f}%
Historical ending quarterly growth: {gdp_end:.2f}%
Historical highest quarterly growth: {gdp_high:.2f}%
Historical lowest quarterly growth: {gdp_low:.2f}%
Average quarterly GDP growth during 2023: {gdp_2023_avg:.2f}%

U.S. INFLATION:
Historical starting inflation rate: {inflation_start:.2f}%
Historical ending inflation rate: {inflation_end:.2f}%
Historical highest inflation rate: {inflation_high:.2f}%
Historical lowest inflation rate: {inflation_low:.2f}%
January 2023 inflation: {inflation_jan_2023:.2f}%
December 2023 inflation: {inflation_dec_2023:.2f}%
Average inflation during 2023: {inflation_2023_avg:.2f}%

TASK:
Use only the historical information above to forecast the overall
direction of U.S. GDP growth and inflation during 2024.

Possible forecast directions:
- Increase
- Decrease
- Stable

For each economic indicator, provide:
1. Forecast direction
2. Brief reason
3. Confidence level: Low, Medium, or High

Do not use information from 2024 when making the forecast.
"""


with open("economic_llm_input.txt", "w", encoding="utf-8") as file:
    file.write(llm_input)


print("Economic LLM input created.")
print("\n" + llm_input)