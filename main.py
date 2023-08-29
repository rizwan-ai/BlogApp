# Importing FastAPI packages
from fastapi import FastAPI

# Importing from project files
from routers import blog_routes


# Router Object to Create Routes
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    title="Blog APIs",
    description="BlogApp API Documentation",
    version="0.1a",
)

# ----------------------------------------------------------------------------#


@app.get("/")
def root():
    return {"message": "Hey, My BlogApp is Running"}


app.include_router(blog_routes.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
