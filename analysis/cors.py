from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    """
    Agrega el middleware CORS a la aplicación FastAPI.
    """
    origins = [
        "http://localhost:3000",  
        "https://mi-dominio.com", 
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  
        allow_credentials=True, 
        allow_methods=["*"],  
        allow_headers=["*"],  
    )
