gdp_prompt = """
Use the historical information below to forecast U.S. GDP growth.

Historical information:
- Average GDP growth during 2023: 1.54%
- Ending GDP growth in 2023: 1.43%
- GDP growth was positive during 2023.

Choose exactly one:
Increase
Decrease
Stable

Answer with only one word.
"""

inflation_prompt = """
Use the historical information below to forecast U.S. inflation.

Historical information:
- January 2023 inflation: 6.33%
- December 2023 inflation: 3.32%
- Average inflation during 2023: 4.15%
- Inflation decreased during 2023.

Choose exactly one:
Increase
Decrease
Stable

Answer with only one word.
"""

with open("economic_gdp_prompt.txt", "w", encoding="utf-8") as file:
    file.write(gdp_prompt)

with open("economic_inflation_prompt.txt", "w", encoding="utf-8") as file:
    file.write(inflation_prompt)

print("GDP and inflation prompts created.")