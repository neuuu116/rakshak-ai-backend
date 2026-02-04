from schemas import ScamResponse


def detect_scam(message: str, history: list) -> ScamResponse:
    """
    Rule-based scam detection (AI-ready fallback).
    Works 100% without external APIs.
    """

    text = message.lower()

    scam_keywords = [
        "account blocked",
        "click this link",
        "urgent",
        "otp",
        "won",
        "lottery",
        "prize",
        "bank",
        "verify",
        "processing fee",
        "kbc",
        "income tax",
        "refund"
    ]

    hits = [kw for kw in scam_keywords if kw in text]

    if hits:
        return ScamResponse(
            is_scam=True,
            scam_type="Phishing",
            risk_level="High" if ("otp" in hits or "bank" in hits) else "Medium",
            reason=f"Detected scam indicators: {', '.join(hits)}"
        )

    return ScamResponse(
        is_scam=False,
        scam_type=None,
        risk_level="Low",
        reason="No scam indicators detected"
    )

