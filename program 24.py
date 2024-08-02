import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define dialog acts
dialog_acts = [
    "statement", "question", "request", "command", "greeting", "closing", "backchannel", "apology", "thank", "other"
]

def recognize_dialog_acts(dialog):
    inputs = tokenizer(dialog, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    return [dialog_acts[prediction] for prediction in predictions]

# Example dialog
dialog = [
    "Hello, how are you?",
    "I'm good, thank you! How about you?",
    "I'm doing well, thanks for asking.",
    "Can you help me with my project?",
    "Sure, what do you need help with?",
    "I need help with coding a Python program."
]

# Recognize dialog acts
recognized_acts = recognize_dialog_acts(dialog)

for sentence, act in zip(dialog, recognized_acts):
    print(f"Sentence: {sentence} - Dialog Act: {act}")
