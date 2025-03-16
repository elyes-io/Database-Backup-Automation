FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY backup.py .

EXPOSE 5000

CMD ["python", "backup.py"]