import os.path

from sqlalchemy import select
from fastapi import APIRouter

from sqlalchemy.ext.asyncio import create_async_engine
from fastapi.responses import FileResponse
from fastapi import UploadFile, File, HTTPException
from app.utils.convert_txt import ConvertTXT


class Converter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/api/v1",
            tags=["convertor"],
        )

    def get_router(self) -> APIRouter:
        self.router.post("/pdf")(self.convert)
        self.router.get("/health")(self.check_connection)
        return self.router

    async def convert(self, file: UploadFile = File()) -> FileResponse:
        # ,check: Check.check_ip_browser = Depends()
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

    async def check_connection(self) -> dict:
        try:
            async with create_async_engine(
                url="postgresql+asyncpg://postgres:qwrqer325345@localhost:5432",
            ).connect() as connection:
                await connection.execute(select(1))
            return {"status": "ok"}
        except Exception:
            raise HTTPException(status_code=500, detail="Database connection error")
