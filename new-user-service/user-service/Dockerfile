FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY user_service.py /app

CMD ["python", "user_service.py"]
