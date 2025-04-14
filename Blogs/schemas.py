from typing import Optional
from pydantic import BaseModel

# Blog Model
class blog_model(BaseModel):
    title: str
    body: str
    # id: Optional[int]
