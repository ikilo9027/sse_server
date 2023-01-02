from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from components.api import sse_api


def create_application() -> FastAPI:
    application = FastAPI(title='SSE_test', version="2.0")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(sse_api.router)

    return application


app = create_application()
