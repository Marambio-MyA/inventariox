from fastapi import APIRouter
from routes.views import login_view
from routes.views import home_view

router = APIRouter()
router.include_router(home_view.router, prefix="", tags=["Home"])
router.include_router(login_view.router, prefix="", tags=["Dashboard"])
