def get_confidence(max_prob):
    if max_prob >= 0.75:
        return "High"
    elif max_prob >= 0.50:
        return "Medium"
    else:
        return "Low"