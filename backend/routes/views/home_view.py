from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        return None
    return user

@router.get("/")
def home(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    
    return templates.TemplateResponse("home.html", {"request": request, "user": user})
