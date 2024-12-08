from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pdfkit
from io import BytesIO
import os

app = FastAPI()

# Check if wkhtmltopdf is available in the path
if not pdfkit.configuration().get('wkhtmltopdf'):
    raise RuntimeError("wkhtmltopdf is not found, please ensure it's installed.")

@app.get("/download-pdf/")
async def download_pdf(url: str):
    try:
        # Generate PDF from the URL
        pdf_data = pdfkit.from_url(url, False)
        # Create a BytesIO buffer to hold the PDF
        pdf_file = BytesIO(pdf_data)
        pdf_file.seek(0)
        
        return StreamingResponse(pdf_file, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=webpage.pdf"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating PDF: {str(e)}")
