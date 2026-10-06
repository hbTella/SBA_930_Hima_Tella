# SBA 930 - Financial LLM Analysis

## Project Overview

This project explores how Large Language Models (LLMs) can be used to support financial forecasting and risk analysis.

The project compares two LLMs:

* OpenAI GPT
* Google's `google/flan-t5-small` from Hugging Face

The models were tested using historical financial and economic data. The goal was to compare their ability to forecast trends, identify financial risks, and provide useful explanations.

## Financial and Economic Data

The project uses historical data from the Federal Reserve Economic Data (FRED).

The datasets include:

* S&P 500 historical data
* WTI crude oil prices
* U.S. GDP data
* U.S. Consumer Price Index (CPI) data

The historical data through December 2023 was used for forecasting. The 2024 data was kept separate and used to compare the model forecasts with actual results.

## Project Requirements

### Requirement 1: LLM Evaluation for Financial Forecasting

The S&P 500 and WTI crude oil datasets were used to evaluate financial forecasting.

Both LLMs were asked to predict whether each asset would Increase, Decrease, or remain Stable during 2024.

The forecasts were then compared with the actual 2024 results.

### Requirement 2: Economic Trend Forecasting

U.S. GDP growth and inflation were used to test economic forecasting.

The models were asked to predict the direction of GDP growth and inflation during 2024. The forecasts were compared with the actual 2024 results.

### Requirement 3: Risk Identification and Mitigation

The models were tested on three types of financial risk:

* Market volatility
* Credit risk
* Liquidity risk

The models were asked to explain the risks and provide possible strategies for managing them.

### Requirement 4: Optimization and Enhancement

Prompt engineering was used to improve the quality of the LLM responses.

Longer prompts were simplified into smaller, task-specific prompts with clear instructions and expected answer formats.

The results showed that prompt optimization improved the completeness of some FLAN-T5-small responses, but it did not improve forecasting accuracy.

## Results

For the financial and economic forecasting tests, both models achieved 50% accuracy.

GPT generally provided more detailed explanations and more practical risk mitigation strategies.

FLAN-T5-small had more difficulty with longer and more complex prompts. However, simplifying the prompts and focusing on one task at a time produced more usable responses.

The project showed that LLMs can be useful for supporting financial analysis, but their forecasts should be checked against actual financial data before being used for financial decisions.

## Project Structure

```text
SBA_930/
│
├── data/
│   ├── sp500.csv
│   ├── wti_crude_oil.csv
│   ├── gdp.csv
│   ├── cpi.csv
│   ├── gdp_historical.csv
│   ├── gdp_2024.csv
│   ├── cpi_historical.csv
│   └── cpi_2024.csv
│
├── src/
│   ├── analyze_financial_data.py
│   ├── calculate_actual_2024.py
│   ├── calculate_actual_economic_2024.py
│   ├── classify_economic_trends.py
│   ├── create_economic_llm_input.py
│   ├── create_forecast_data.py
│   ├── create_llm_input.py
│   ├── create_risk_prompt.py
│   ├── create_simple_economic_prompt.py
│   ├── optimization_results.py
│   ├── prepare_economic_data.py
│   ├── run_flan_forecast.py
│   ├── run_flan_economic_forecast.py
│   ├── run_flan_gdp_forecast.py
│   ├── run_flan_inflation_forecast.py
│   ├── run_flan_market_volatility.py
│   ├── run_flan_credit_risk.py
│   ├── run_flan_liquidity_risk.py
│   └── run_flan_risk_analysis.py
│
├── financial_llm_input.txt
├── economic_llm_input.txt
├── economic_gdp_prompt.txt
├── economic_inflation_prompt.txt
├── risk_analysis_prompt.txt
├── market_volatility_prompt.txt
├── credit_risk_prompt.txt
├── liquidity_risk_prompt.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

## Technologies Used

* Python
* uv
* pandas
* PyTorch
* Hugging Face Transformers
* `google/flan-t5-small`
* OpenAI GPT
* FRED financial and economic data

## How to Run

Create and activate the project environment using `uv`.

For example:

```bash
uv sync
```

The FLAN-T5-small scripts can then be run using commands such as:

```bash
uv run python src/run_flan_forecast.py
uv run python src/run_flan_economic_forecast.py
uv run python src/run_flan_market_volatility.py
uv run python src/run_flan_liquidity_risk.py
uv run python src/run_flan_risk_analysis.py
```

## Conclusion

This project showed that LLMs can help analyze financial information, identify possible trends, and explain financial risks. However, the results also showed that LLM forecasts are not always accurate.

GPT generally provided more detailed financial analysis, while FLAN-T5-small benefited from shorter and more focused prompts.

LLM outputs should be treated as supporting information rather than a replacement for financial data analysis, validation, and human judgment.
