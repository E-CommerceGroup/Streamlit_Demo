import random

DISEASES = ["Rare Disease A", "Rare Disease B", "Normal"]

class MockPredictionEngine:
    def predict(self, image):
        probs = [random.uniform(0.05, 0.9) for _ in DISEASES]
        total = sum(probs)
        probs = [p / total for p in probs]
        return dict(zip(DISEASES, probs))
