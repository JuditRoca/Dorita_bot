FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .
RUN pip install openai
RUN pip install --no-cache-dir -r requirements.txt

COPY src .
COPY .env .
COPY .gitignore .

CMD ["python", "app.py"]
EXPOSE 5000

