FROM python:3.9-slim

WORKDIR /app

# Copy backend files
COPY ./app /app/app
COPY requirements.txt /app
COPY .env /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
