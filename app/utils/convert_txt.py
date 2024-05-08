from typing import Any

from fpdf import FPDF
from celery import Celery

celery_app = Celery("celery", broker="amqp://guest:guest@rabbitmq:5672")


class ConvertTXT:
    @staticmethod
    @celery_app.task
    def convert2pdf(content: bytes, name: str) -> Any | None:
        pdf = FPDF()
        content = content.decode("utf-8")
        pdf.add_page()
        pdf.set_font("Symbol", "", 16)
        pdf.multi_cell(0, 10, text=content)
        return pdf.output(f"{name}.pdf")
