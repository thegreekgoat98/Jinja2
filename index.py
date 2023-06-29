from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates=Jinja2Templates(directory="templates")

BATSMAN = [{"name":"Sachin Tendulkar", "side":"Right"},{"name":"Brian Lara", "side":"Left"}, {"name":"Virat Kohli","side":"Right"}]

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request, "name":"Hello World"})


@app.get("/batsman")
def show(request:Request):
    return templates.TemplateResponse("batsman.html",{"request":request,"batsman":BATSMAN})


    