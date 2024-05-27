from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from main import extract_tickets, extract_emails, export_data

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/extract_tickets", response_class=HTMLResponse)
def get_tickets(request: Request):
    try:
        ticket_df = extract_tickets()
        tickets = ticket_df.to_dict(orient="records")
        return templates.TemplateResponse("result.html", {"request": request, "results": tickets, "type": "Tickets"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/extract_emails", response_class=HTMLResponse)
def get_emails(request: Request):
    try:
        email_df = extract_emails()
        emails = email_df.to_dict(orient="records")
        return templates.TemplateResponse("result.html", {"request": request, "results": emails, "type": "Emails"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/export_data", response_class=HTMLResponse)
def export(request: Request):
    try:
        result = export_data()
        return templates.TemplateResponse("result.html", {"request": request, "message": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
