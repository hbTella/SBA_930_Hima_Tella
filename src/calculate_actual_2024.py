import pandas as pd


# Load the original financial datasets
sp500 = pd.read_csv("data/sp500.csv")
wti = pd.read_csv("data/wti_crude_oil.csv")


# Convert the date column
sp500["observation_date"] = pd.to_datetime(sp500["observation_date"])
wti["observation_date"] = pd.to_datetime(wti["observation_date"])


# Keep only 2024 data
sp500_2024 = sp500[
    (sp500["observation_date"] >= "2024-01-01") &
    (sp500["observation_date"] <= "2024-12-31")
].copy()

wti_2024 = wti[
    (wti["observation_date"] >= "2024-01-01") &
    (wti["observation_date"] <= "2024-12-31")
].copy()

# Remove missing financial values
sp500_2024 = sp500_2024.dropna(subset=["SP500"])
wti_2024 = wti_2024.dropna(subset=["DCOILWTICO"])


def calculate_direction(data, value_column):
    """Calculate the overall 2024 change and direction."""
    start_value = data[value_column].iloc[0]
    end_value = data[value_column].iloc[-1]

    percent_change = ((end_value - start_value) / start_value) * 100

    if percent_change > 5:
        direction = "Increase"
    elif percent_change < -5:
        direction = "Decrease"
    else:
        direction = "Stable"

    return start_value, end_value, percent_change, direction


# Calculate S&P 500 results
sp500_start, sp500_end, sp500_change, sp500_direction = calculate_direction(
    sp500_2024, "SP500"
)


# Calculate WTI results
wti_start, wti_end, wti_change, wti_direction = calculate_direction(
    wti_2024, "DCOILWTICO"
)


# Display actual 2024 results
print("\nACTUAL 2024 RESULTS")
print("=" * 50)

print("\nS&P 500:")
print(f"Starting value: {sp500_start:.2f}")
print(f"Ending value: {sp500_end:.2f}")
print(f"2024 change: {sp500_change:.2f}%")
print(f"Actual direction: {sp500_direction}")

print("\nWTI CRUDE OIL:")
print(f"Starting price: ${wti_start:.2f}")
print(f"Ending price: ${wti_end:.2f}")
print(f"2024 change: {wti_change:.2f}%")
print(f"Actual direction: {wti_direction}")