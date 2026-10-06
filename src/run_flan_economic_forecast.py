from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "google/flan-t5-small"

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


# Load the economic forecasting prompt
with open("economic_llm_input.txt", "r", encoding="utf-8") as file:
    prompt = file.read()


# Convert the prompt into model input
inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True
)


# Generate the forecast
outputs = model.generate(
    **inputs,
    max_new_tokens=150,
    do_sample=False
)


# Convert the model output to text
response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


print("FLAN-T5-SMALL ECONOMIC FORECAST")
print("--------------------------------")
print(response)