from fastapi import FastAPI
from routers import wallet_router
from uvicorn import run

app = FastAPI()
app.include_router(wallet_router, prefix='/api/v1')

if __name__ == '__main__':
    run(
        app, 
        host='0.0.0.0', 
        port=8000)