import torch.nn as nn
from torchvision import models

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.backbone = models.resnet18(pretrained=False)
        self.backbone.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        return self.backbone(x)
