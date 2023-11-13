from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    new_docs = []
    for doc in docs:
        new_docs.append({
            'id': doc['_id'],
            'title': doc['title'],
            'desc': doc['desc'],
            'important': doc['important']
        })
    return templates.TemplateResponse("index.html", {"request": request, 'new_docs': new_docs})

@note.post('/')
async def create_item(request: Request):
    form = await request.form()
    print('formm:',form)
    form_dict = dict(form)
    form_dict['important'] = True if form_dict.get('important') == 'on' else False
    note = conn.notes.notes.insert_one(form_dict)
    return {'Success': True}