FROM python:3.12-slim

WORKDIR /test

COPY . .

EXPOSE 5000

CMD ["python", "test.py"]
