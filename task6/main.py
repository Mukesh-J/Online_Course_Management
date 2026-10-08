from fastapi import FastAPI
from database.connection import engine, Base
from database import models
from routes import auth, course, user, enrollment, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Course Management API", version="1.0.0")

app.include_router(auth.router)
app.include_router(course.router)
app.include_router(user.router)
app.include_router(enrollment.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Online Course Management API is running"}
