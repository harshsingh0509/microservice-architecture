FROM python:3.8-slim

WORKDIR /app

COPY user_service.py /app

RUN pip install flask

CMD ["python", "user_service.py"]
