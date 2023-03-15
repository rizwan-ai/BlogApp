from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'name': 'rizwan'}

@app.get('/about')
async def about():
    return {'data': {'about': 'about for blog'}}