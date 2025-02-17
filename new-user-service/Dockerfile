FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY new_user_service.py /app

CMD ["python", "new_user_service.py"]
