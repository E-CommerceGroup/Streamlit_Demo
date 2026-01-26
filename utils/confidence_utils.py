"""
Confidence level classification utilities
"""


def confidence_label(probability):
    """
    Convert probability to confidence level
    
    Args:
        probability (float): Confidence value (0-1)
        
    Returns:
        str: "High", "Moderate", or "Low"
    """
    if probability >= 0.80:
        return "High"
    elif probability >= 0.60:
        return "Moderate"
    else:
        return "Low"


def get_confidence_emoji(level):
    """Get emoji for confidence level"""
    emojis = {
        "High": "✅",
        "Moderate": "⚠️",
        "Low": "❌"
    }
    return emojis.get(level, "❓")


def get_confidence_message(level):
    """Get clinical interpretation message"""
    messages = {
        "High": "HIGH confidence – suitable for automated screening.",
        "Moderate": "MODERATE confidence – expert review required.",
        "Low": "LOW confidence – do not rely on AI alone."
    }
    return messages.get(level, "Unknown confidence level")
