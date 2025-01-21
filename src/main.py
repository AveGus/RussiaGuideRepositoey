from fastapi import FastAPI
from api.cities import router as cities_router
from api.routes import router as routes_router
from api.places import router as places_router
from api.categories import router as categories_router
from api.completed_routes import router as completed_routes_router

app = FastAPI(title="Russia Guide API")

app.include_router(cities_router)
app.include_router(routes_router)
app.include_router(places_router)
app.include_router(categories_router)
app.include_router(completed_routes_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
