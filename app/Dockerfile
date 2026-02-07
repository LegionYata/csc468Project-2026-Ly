FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pymongo flask

COPY main.py .

EXPOSE 5000

CMD ["python","main.py"]
