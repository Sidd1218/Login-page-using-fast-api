from urllib.request import Request
from fastapi import FastAPI,Request
from typing import Optional
from pydantic import BaseModel
import time

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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

@app.post("mypostendpoint")
async def mpep(emp:IPL):
    return {"emp":emp.name}

@app.get("/security")
async def sec(token:str):
    authToken = "VmVua2F0YXJhbWFu"
    if token !="" or token==authToken:
        authorisation = "success"
    else:
        authorisation = "failed"
    
    return{"server_pass":authorisation}


@app.get("/web", response_class=HTMLResponse)
async def web():
   code = """
        <html>
        <head>
        <title>Some HTML in here</title>
        </head>
        <body>
        <h1>Look ma! HTML!</h1>
        </body>
        </html>

    """
   return code

class user(BaseModel):
    name:str
    password:str
    email:str

@app.get("/html", response_class=HTMLResponse)
async def webpage(request:Request):
    return templates.TemplateResponse('index.html', context={'request':request})


@app.post("/create_user")
async def create_user(user:user):

    db = eval(open("userdb.json","r").read())

    user_profile = {"name":user.name,
                    "password":user.password,
                    "email":user.email}

    db["users"].append(user_profile)
    open("userdb.json","w+").write(str(db))
    return {"status":"success"}

class users(BaseModel):
    name:str
    password:str

@app.post("/login_user")
async def create_user(user:users):
 
    userdb = eval(open("userdb.json","r").read())  
    for each in  userdb["users"]:
        if each["name"]==user.name and each["password"]==user.password:
            return {"status":"Success"}
        else:
            pass
    return {"status":"Wrong password or Username"}