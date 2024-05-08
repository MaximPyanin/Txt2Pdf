from app.api.conventer import Converter
from fastapi import FastAPI


class ConverterHandler:

    def __init__(self):
        self.router = Converter()
        self.app = FastAPI(title="txt2pdf")
        self.app.include_router(self.router.get_router())
