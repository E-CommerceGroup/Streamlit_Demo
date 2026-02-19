import torch
import torch.nn as nn
import json
import os
from torchvision import models, transforms
from PIL import Image

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(__file__)
VALIDATOR_PATH = os.path.join(BASE_DIR, "brain_validator.pth")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")

# ---------------- DEVICE ----------------
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------- LOAD LABELS ----------------
with open(LABELS_PATH, "r") as f:
    CLASS_NAMES = json.load(f)

# ---------------- MODEL ARCHITECTURE ----------------
def load_brain_validator():
    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = nn.Linear(model.last_channel, 1)
    model.load_state_dict(torch.load(VALIDATOR_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model

# ---------------- TRANSFORM ----------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# ---------------- PREDICTION ----------------
def validate_brain_image(image_pil):
    model = load_brain_validator()

    img = transform(image_pil).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        output = model(img)
        prob = torch.sigmoid(output).item()

    is_brain = prob < 0.5  # Based on training label

    return {
        "is_brain": is_brain,
        "confidence": 1 - prob if is_brain else prob
    }
