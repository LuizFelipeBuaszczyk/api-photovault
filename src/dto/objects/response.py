from pydantic import BaseModel
from typing import Optional

class CreateObjectResponse(BaseModel):
    name: str
    bucket_name: str
    version_id: Optional[str]    