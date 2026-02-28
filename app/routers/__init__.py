from app.routers.habits import router as habits_router
from app.routers.checkins import router as checkins_router
from app.routers.statistic import router as statistic_router

routers = [habits_router, checkins_router, statistic_router]
