import re
from schemas import ScamResponse
from datetime import datetime

def detect_scam(message: str, history: list) -> ScamResponse:
    text = message.lower()

    scam_patterns = [
        r"(account\s+blocked)",
        r"(click\s+this\s+link)",
        r"(urgent)",
        r"(otp)",
        r"(lottery|prize|won)",
        r"(bank\s+details?)",
        r"(verify\s+your\s+account)",
        r"(processing\s+fee)",
        r"(refund)",
        r"(income\s+tax)",
        r"(kbc)"
    ]

    hits = [p for p in scam_patterns if re.search(p, text)]
    confidence = len(hits) / len(scam_patterns)

    if hits:
        return ScamResponse(
            is_scam=True,
            scam_type="Phishing",
            risk_level="High" if re.search(r"(otp|bank)", text) else "Medium",
            reason=f"Detected scam indicators: {', '.join(hits)}",
            confidence=round(confidence, 2),
            timestamp=datetime.utcnow(),
            suggested_action="Ignore and report"
        )

    return ScamResponse(
        is_scam=False,
        scam_type=None,
        risk_level="Low",
        reason="No scam indicators detected",
        confidence=0.0,
        timestamp=datetime.utcnow(),
        suggested_action="Safe message"
    )

