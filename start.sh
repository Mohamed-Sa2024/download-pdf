#!/bin/bash

# Install wkhtmltopdf
apt-get update
apt-get install -y wkhtmltopdf

# Start the FastAPI app
exec "$@"
