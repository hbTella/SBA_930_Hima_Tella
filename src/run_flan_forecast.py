from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def forecast(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=False
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


sp500_prompt = """
Historical S&P 500 data through December 31, 2023:
Long-term change: +120.70%.
2023 change: +24.73%.
2023 ending value: 4769.83.

Question:
What will be the overall direction of the S&P 500 during 2024?

Answer with exactly one word:
Increase, Decrease, or Stable.
"""

wti_prompt = """
Historical WTI crude oil data through December 31, 2023:
Long-term change: +181.26%.
2023 change: -6.48%.
2023 ending price: $71.89.

Question:
What will be the overall direction of WTI crude oil during 2024?

Answer with exactly one word:
Increase, Decrease, or Stable.
"""


print("\nFLAN-T5-SMALL S&P 500 FORECAST")
print("=" * 50)
print(forecast(sp500_prompt))

print("\nFLAN-T5-SMALL WTI FORECAST")
print("=" * 50)
print(forecast(wti_prompt))