from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from . import students
from . import auth

app = FastAPI(
    title="College Management API",
    version="1.0.0",
    description="A college management system with OAuth2 authentication"
)

# Add CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {
    "message": "Welcome to College Management API",
    "docs": "/docs",
    "test_ui": "/test",
    "endpoints": {
      "login": "POST /login",
      "students": "GET /students (requires auth)",
      "docs": "GET /docs",
      "test_ui": "GET /test"
    }
  }

@app.get("/test")
def serve_test_ui():
    """Serve the test HTML interface"""
    return FileResponse('/app/index.html')

app.include_router(auth.router)
app.include_router(students.router)
