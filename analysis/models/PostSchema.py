from pydantic import BaseModel

class PostSchema(BaseModel):
    content: str
    color: str
    neg: float
    neu: float
    pos: float

    class Config:
        orm_mode = True
