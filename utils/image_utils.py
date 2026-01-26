"""
Image processing and visualization utilities
"""
from PIL import Image, ImageDraw
import random


def generate_mock_gradcam(image):
    """
    Create a fake Grad-CAM style heatmap overlay
    (Placeholder until real Grad-CAM is implemented)
    
    Args:
        image (PIL.Image): Input medical image
        
    Returns:
        PIL.Image: Image with mock Grad-CAM heatmap overlay
    """
    heatmap = Image.new("RGBA", image.size, (255, 0, 0, 0))
    draw = ImageDraw.Draw(heatmap)

    for _ in range(30):
        x1 = random.randint(0, image.size[0] - 50)
        y1 = random.randint(0, image.size[1] - 50)
        x2 = x1 + random.randint(30, 80)
        y2 = y1 + random.randint(30, 80)
        # Red heatmap with transparency
        draw.ellipse([x1, y1, x2, y2], fill=(255, 0, 0, 80))

    return Image.alpha_composite(image.convert("RGBA"), heatmap)


def resize_for_inference(image, size=224):
    """
    Resize image for model inference
    
    Args:
        image (PIL.Image): Input image
        size (int): Target size
        
    Returns:
        PIL.Image: Resized image
    """
    return image.convert("RGB").resize((size, size))
