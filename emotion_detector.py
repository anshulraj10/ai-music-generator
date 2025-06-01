from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import numpy as np

# Load trained DistilBERT model
model_path = "models/distilbert_emotion"
tokenizer = DistilBertTokenizer.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)
model.eval()

# Emotion labels
EMOTIONS = {0: 'sadness', 1: 'joy', 2: 'love', 3: 'anger', 4: 'fear', 5: 'surprise'}

def detect_emotion(text):
    """Predicts emotion using DistilBERT."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=50)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1).numpy()[0]

    predicted_class = np.argmax(probabilities)

    # Debugging: Print class probabilities
    # print(f"Probabilities: {probabilities}")
    # print(f"Predicted Class: {predicted_class} - {EMOTIONS[predicted_class]}")

    return EMOTIONS[predicted_class]