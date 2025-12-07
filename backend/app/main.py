from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.predict import router as predict_router
from app.api.healthy import router as health_router

app = FastAPI(title="Traffic Sign API")

# fix CORS để FE gọi được
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # FE localhost
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}

# gắn router API
app.include_router(predict_router, prefix="/api")
app.include_router(health_router, prefix="/api")