from pydantic import BaseModel

class GetBucketResponse(BaseModel):
    name: str