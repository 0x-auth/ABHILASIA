FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY api_requirements.txt .
RUN pip install --no-cache-dir -r api_requirements.txt

# Install abhilasia
COPY . .
RUN pip install -e .

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "abhilasia.api:app", "--host", "0.0.0.0", "--port", "8000"]
