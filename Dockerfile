FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD ["uvicorn", "src.__main__:app", "--port", "8080", "--host", "0.0.0.0"]
