import os

# Lazy torch import (only when needed)
_torch = None

def _get_device():
    global _torch
    if _torch is None:
        import torch
        _torch = torch
    return "cuda" if _torch.cuda.is_available() else "cpu"

DEVICE = None  # Will be set on first use

CLASS_NAMES = [
    "Moyamoya Disease with Intraventricular Hemorrhage",
    "Neurofibromatosis Type 1 (NF1)",
    "Optic Glioma",
    "Tuberous Sclerosis",
    "normal"
]

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "best_model.pth"
)
