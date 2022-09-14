FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY rook /app/rook

CMD ["uvicorn", "rook:Server", "--host", "0.0.0.0", "--port", "8080"]