from fastapi import APIRouter
from config.db import conn
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from schemas.note import noteEntity, notesEntity

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"],
                "important": doc["important"]
            })
    return templates.TemplateResponse("index.html", {"request": request,"newDocs": newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success": True}


