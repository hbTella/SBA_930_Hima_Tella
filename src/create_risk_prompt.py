market_volatility_prompt = """
Market volatility means large or sudden changes in asset prices.

The S&P 500 increased 24.73% during 2023.

What is one practical strategy an investor can use to reduce the risk from market volatility?

Answer with one short sentence.
"""

credit_risk_prompt = """
Credit risk is the possibility that a borrower cannot repay a loan or financial obligation.

What is one practical strategy a financial institution can use to reduce credit risk?

Answer with one short sentence.
"""

liquidity_risk_prompt = """
Liquidity risk is the risk that an asset cannot be bought or sold quickly without a significant price change.

What is one practical strategy an investor or financial institution can use to reduce liquidity risk?

Answer with one short sentence.
"""

with open("market_volatility_prompt.txt", "w", encoding="utf-8") as file:
    file.write(market_volatility_prompt)

with open("credit_risk_prompt.txt", "w", encoding="utf-8") as file:
    file.write(credit_risk_prompt)

with open("liquidity_risk_prompt.txt", "w", encoding="utf-8") as file:
    file.write(liquidity_risk_prompt)

print("Simplified risk prompts created.")