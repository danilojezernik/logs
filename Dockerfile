FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=8080

ENV DB_PROCES="development"
ENV DB_CONNECTION_LOGGING="mongodb+srv://danijezernik:BNODyNiYlEJXbIwz@loggingevents.tx42xxh.mongodb.net/?retryWrites=true&w=majority"

ENV SECRET_KEY="33333344444443322243"
ENV ALGORITHM="HS256"

ENV DOMAIN="http://localhost:8080/"

CMD ["uvicorn", "src.__main__:app", "--port", "8080", "--host", "0.0.0.0"]
