from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class WebAPI():
    def __init__():
        pass
    
    @staticmethod
    def create_app():
        app = FastAPI()
        app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],  
        allow_headers=["*"],  
        )
        return app

