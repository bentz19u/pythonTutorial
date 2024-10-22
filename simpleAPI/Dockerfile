FROM python:3.13-slim

WORKDIR /neural-api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "./src/main.py"]