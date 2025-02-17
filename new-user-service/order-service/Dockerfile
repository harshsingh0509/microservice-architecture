FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY order_service.py /app

CMD ["python", "order_service.py"]
