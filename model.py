from pydantic import BaseModel

# config
class config(BaseModel):
    x:float
    y:float

class target(BaseModel):
    target:float



