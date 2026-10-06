from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

with open("economic_inflation_prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True
)

outputs = model.generate(
    **inputs,
    max_new_tokens=10,
    do_sample=False
)

response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("FLAN-T5-SMALL INFLATION FORECAST")
print("--------------------------------")
print(response)