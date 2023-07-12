FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

CMD ["python3", "src/app.py"]
