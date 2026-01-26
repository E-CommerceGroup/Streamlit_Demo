import torch
import torch.nn.functional as F
import numpy as np
import cv2
from PIL import Image


class GradCAM:
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None

        self._register_hooks()

    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output

        def backward_hook(module, grad_in, grad_out):
            self.gradients = grad_out[0]

        self.target_layer.register_forward_hook(forward_hook)
        self.target_layer.register_backward_hook(backward_hook)

    def generate(self, input_tensor, class_idx):
        self.model.zero_grad()

        output = self.model(input_tensor)
        score = output[:, class_idx]
        score.backward()

        weights = self.gradients.mean(dim=(2, 3), keepdim=True)
        cam = (weights * self.activations).sum(dim=1)
        cam = F.relu(cam)

        cam = cam[0].detach().cpu().numpy()
        cam -= cam.min()
        cam /= (cam.max() + 1e-8)

        return cam


def generate_real_gradcam(model, image_pil, transform, device, class_idx):
    image_tensor = transform(image_pil).unsqueeze(0).to(device)

    gradcam = GradCAM(model, model.backbone.layer4)
    cam = gradcam.generate(image_tensor, class_idx)

    cam = cv2.resize(cam, image_pil.size)
    heatmap = np.uint8(255 * cam)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    original = np.array(image_pil)
    overlay = cv2.addWeighted(original, 0.6, heatmap, 0.4, 0)

    return Image.fromarray(overlay)
