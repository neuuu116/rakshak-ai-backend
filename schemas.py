from pydantic import BaseModel

class ScamRequest(BaseModel):
    user_id: int
    message: str


class ScamResponse(BaseModel):
    is_scam: bool
    scam_type: str | None
    risk_level: str
    reason: str

