from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class IPL(BaseModel):
    team_code: int
    name = str
    signup: Optional[bool] = None
    list1: Optional[list] = []

@app.get("/")
def home():
    return {"Hey": "IPL is round the corner"}

@app.get("/IPL/{star}")
def performance(performance: str, rating: int, review: Optional[str] = "GOOD"):
    return {"Performance": performance, "rating": rating ,"review": review}

@app.put("IPL/endpoint")
def endpoint(IPL: IPL):
    return {"name": IPL.name ,"Team Code": IPL.team_code, "Team Code": IPL.signup , "list1": IPL.list1 }