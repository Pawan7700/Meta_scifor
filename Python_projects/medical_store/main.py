from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

medicines = [
    {"name": "Paracetamol", "description": "Pain and fever reducer", "price": "Rs.5", "quantity": "100"},
    {"name": "Aspirin", "description": "Used reduce inflammation", "price": "Rs.7", "quantity": "100"},
    {"name": "Monticope", "description": "Use for cold and headache", "price": "Rs.10", "quantity": "100"}
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "medicines": medicines})
