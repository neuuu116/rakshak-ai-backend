from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ScamRequest(BaseModel):
    user_id: int
    message: str
    history: Optional[List[str]] = None

class ScamResponse(BaseModel):
    is_scam: bool
    scam_type: Optional[str]
    risk_level: str
    reason: str
    confidence: float
    timestamp: datetime
    suggested_action: str

