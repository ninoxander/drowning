from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class SentimentAnalyzer:
    def __init__(self, model_name="finiteautomata/beto-sentiment-analysis"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = ["NEG", "NEU", "POS"]  

    def analyze(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return {self.labels[i]: float(scores[0][i]) for i in range(len(self.labels))}

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    texto = "Jamás debimos estar juntos"
    resultados = analyzer.analyze(texto)

    