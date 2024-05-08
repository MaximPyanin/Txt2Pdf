import os.path

from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import FastAPI, Path, Query, UploadFile, File, HTTPException
from app.utils.convert_txt import ConvertTXT


class Converter:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1", tags=["convertor"])

    def get_router(self) -> APIRouter:
        self.router.post("/pdf")(self.convert)
        return self.router

    async def convert(self, file: UploadFile = File()) -> FileResponse:
        if file.content_type != "text/plain":
            raise HTTPException(
                status_code=415,
                detail="Invalid file format. Please upload a .txt file.",
            )
        name = file.filename[:-4]
        content = await file.read()
        ConvertTXT.convert2pdf.delay(content, name)
        while os.path.isfile(f"{name}.pdf") != True:
            pass
        return FileResponse(
            f"..utils.{name}.pdf", media_type="application/pdf", filename=f"{name}.pdf"
        )
