FIT_TARGET_DIFF = {
    "oversized": {"top": 4.0, "bottom": 3.0},
    "regular": {"top": 1.5, "bottom": 1.0},
    "slim": {"top": 0.0, "bottom": 0.0},
}

def recommend_size(user_measurement: float, size_chart: list, fit_preference: str, category_type: str = "top"):
    """
    user_measurement: user's chest or waist in inches
    size_chart: list of dicts, each like {"size": "M", "chest": 43, ...}
    fit_preference: "oversized" | "regular" | "slim"
    category_type: "top" (uses chest) or "bottom" (uses waist)
    """
    if not size_chart:
        return {"recommended_size": None, "confidence": 0.0, "fit": {}, "fit_score": 0}

    target_diff = FIT_TARGET_DIFF.get(fit_preference, FIT_TARGET_DIFF["regular"])[category_type]
    measurement_key = "chest" if category_type == "top" else "waist"

    best_size = None
    best_score = -1
    best_actual_diff = None

    for entry in size_chart:
        garment_measurement = entry.get(measurement_key)
        if garment_measurement is None:
            continue

        actual_diff = garment_measurement - user_measurement
        # Score = how close actual_diff is to target_diff (closer = higher score)
        distance = abs(actual_diff - target_diff)
        score = max(0, 100 - (distance * 15))  # 15 pts off per inch of mismatch

        if score > best_score:
            best_score = score
            best_size = entry["size"]
            best_actual_diff = actual_diff

    if best_size is None:
        return {"recommended_size": None, "confidence": 0.0, "fit": {}, "fit_score": 0}

    # Translate actual_diff into a human-readable fit description
    if best_actual_diff <= 0.5:
        fit_desc = "snug"
    elif best_actual_diff <= 2.5:
        fit_desc = "good"
    elif best_actual_diff <= 4.5:
        fit_desc = "relaxed"
    else:
        fit_desc = "very loose"

    return {
        "recommended_size": best_size,
        "confidence": round(best_score / 100, 2),
        "fit": {measurement_key: fit_desc},
        "fit_score": round(best_score),
    }