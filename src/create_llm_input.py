import pandas as pd

# Load the financial datasets
sp500 = pd.read_csv("data/sp500.csv")
wti = pd.read_csv("data/wti_crude_oil.csv")

# Convert dates
sp500["observation_date"] = pd.to_datetime(sp500["observation_date"])
wti["observation_date"] = pd.to_datetime(wti["observation_date"])

# Remove missing values
sp500 = sp500.dropna()
wti = wti.dropna()

# Historical data available before the forecast period
sp500_history = sp500[sp500["observation_date"] <= "2023-12-31"].copy()
wti_history = wti[wti["observation_date"] <= "2023-12-31"].copy()

# 2023 data
sp500_2023 = sp500[
    (sp500["observation_date"] >= "2023-01-01")
    & (sp500["observation_date"] <= "2023-12-31")
].copy()

wti_2023 = wti[
    (wti["observation_date"] >= "2023-01-01")
    & (wti["observation_date"] <= "2023-12-31")
].copy()

# S&P 500 historical summary
sp500_start = sp500_history["SP500"].iloc[0]
sp500_end = sp500_history["SP500"].iloc[-1]
sp500_high = sp500_history["SP500"].max()
sp500_low = sp500_history["SP500"].min()
sp500_change = ((sp500_end - sp500_start) / sp500_start) * 100

# S&P 500 2023 summary
sp500_2023_start = sp500_2023["SP500"].iloc[0]
sp500_2023_end = sp500_2023["SP500"].iloc[-1]
sp500_2023_high = sp500_2023["SP500"].max()
sp500_2023_low = sp500_2023["SP500"].min()
sp500_2023_change = (
    (sp500_2023_end - sp500_2023_start) / sp500_2023_start
) * 100

# WTI historical summary
wti_start = wti_history["DCOILWTICO"].iloc[0]
wti_end = wti_history["DCOILWTICO"].iloc[-1]
wti_high = wti_history["DCOILWTICO"].max()
wti_low = wti_history["DCOILWTICO"].min()
wti_change = ((wti_end - wti_start) / wti_start) * 100

# WTI 2023 summary
wti_2023_start = wti_2023["DCOILWTICO"].iloc[0]
wti_2023_end = wti_2023["DCOILWTICO"].iloc[-1]
wti_2023_high = wti_2023["DCOILWTICO"].max()
wti_2023_low = wti_2023["DCOILWTICO"].min()
wti_2023_change = ((wti_2023_end - wti_2023_start) / wti_2023_start) * 100

# Create the summary for the LLMs
summary = f"""
FINANCIAL DATA SUMMARY

Historical data cutoff: December 31, 2023
Forecast period: January 1, 2024 to December 31, 2024

S&P 500 - Long-Term Historical Data:
Starting value: {sp500_start:.2f}
Ending value: {sp500_end:.2f}
Historical high: {sp500_high:.2f}
Historical low: {sp500_low:.2f}
Overall historical change: {sp500_change:.2f}%

S&P 500 - 2023 Data:
Starting value: {sp500_2023_start:.2f}
Ending value: {sp500_2023_end:.2f}
2023 high: {sp500_2023_high:.2f}
2023 low: {sp500_2023_low:.2f}
2023 change: {sp500_2023_change:.2f}%

WTI CRUDE OIL - Long-Term Historical Data:
Starting price: ${wti_start:.2f}
Ending price: ${wti_end:.2f}
Historical high: ${wti_high:.2f}
Historical low: ${wti_low:.2f}
Overall historical change: {wti_change:.2f}%

WTI CRUDE OIL - 2023 Data:
Starting price: ${wti_2023_start:.2f}
Ending price: ${wti_2023_end:.2f}
2023 high: ${wti_2023_high:.2f}
2023 low: ${wti_2023_low:.2f}
2023 change: {wti_2023_change:.2f}%

TASK:
Use only the historical information above to forecast the overall
direction of the S&P 500 and WTI crude oil during 2024.

Possible forecast directions:
- Increase
- Decrease
- Stable

For each asset, provide:
1. Forecast direction
2. Brief reason
3. Confidence level: Low, Medium, or High

Do not use information from 2024 when making the forecast.
"""

# Save the summary
with open("financial_llm_input.txt", "w") as file:
    file.write(summary)

print(summary)
print("LLM input saved to financial_llm_input.txt")