# backend/inference.py
from PIL import Image
import numpy as np

from backend.config import CLASS_NAMES, MODEL_PATH

# Lazy imports - only load when needed
torch = None
transforms = None
SimpleCNN = None

def _init_torch():
    global torch, transforms, SimpleCNN
    if torch is None:
        import torch as torch_lib
        from torchvision import transforms as transforms_lib
        from backend.models.model_architecture import SimpleCNN as SimpleCNN_lib

        torch_lib.set_grad_enabled(False)
        torch_lib.backends.cudnn.deterministic = True
        torch_lib.backends.cudnn.benchmark = False

        torch = torch_lib
        transforms = transforms_lib
        SimpleCNN = SimpleCNN_lib

def _get_device():
    _init_torch()
    return "cpu"   # Streamlit → CPU

# ===============================
# MODEL CACHING
# ===============================
_model = None

def _load_model():
    global _model
    if _model is None:
        _init_torch()
        device = _get_device()
        model = SimpleCNN(num_classes=len(CLASS_NAMES)).to(device)
        model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
        model.eval()
        _model = model
        print(f"✅ Model loaded successfully on {device}")
    return _model

def _get_transform():
    _init_torch()
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])

# ===============================
# PREDICTION FUNCTION (SAME AS COLAB)
# ===============================
def predict_image(pil_image: Image.Image):
    """
    Run inference exactly like Colab single-image prediction
    """
    _init_torch()
    
    model = _load_model()
    device = _get_device()
    transform = _get_transform()

    # Preprocess
    image = pil_image.convert("RGB")
    tensor = transform(image).unsqueeze(0).to(device)  # [1, 3, 224, 224]

    # Inference
    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.softmax(outputs, dim=1)
        conf, pred = torch.max(probs, dim=1)

    pred_idx = pred.item()
    confidence = conf.item()
    probs_np = probs[0].cpu().numpy()

    return {
        "prediction": CLASS_NAMES[pred_idx],
        "confidence": confidence,  # 0–1 (multiply by 100 in UI if needed)
        "probabilities": {
            CLASS_NAMES[i]: float(probs_np[i])
            for i in range(len(CLASS_NAMES))
        },
    }
