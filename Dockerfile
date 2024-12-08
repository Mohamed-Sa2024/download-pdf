# Start with an official Python image
FROM python:3.10-slim

# Install dependencies for pdfkit (wkhtmltopdf)
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    libx11-dev \
    libxrender1 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . /app

# Expose the FastAPI app on port 8000
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
