results = [
    {
        "Task": "Financial forecasting",
        "Original Prompt": "Combined S&P 500 and WTI prompt",
        "Original Result": "Incomplete: 1.",
        "Optimized Prompt": "One asset at a time with a short answer format",
        "Optimized Result": "Valid forecast: Stable"
    },
    {
        "Task": "Economic forecasting",
        "Original Prompt": "Combined GDP and inflation prompt",
        "Original Result": "Incomplete: 1.",
        "Optimized Prompt": "Separate GDP and inflation prompts",
        "Optimized Result": "Valid forecasts: Increase / Increase"
    },
    {
        "Task": "Risk analysis",
        "Original Prompt": "Three risks with detailed explanations",
        "Original Result": "Risk names only",
        "Optimized Prompt": "One risk at a time with a short strategy request",
        "Optimized Result": "Still incomplete or generic"
    }
]

print("LLM PROMPT OPTIMIZATION RESULTS")
print("--------------------------------")

for result in results:
    print(f"\nTask: {result['Task']}")
    print(f"Original prompt result: {result['Original Result']}")
    print(f"Optimized prompt result: {result['Optimized Result']}")