FROM python:3.11-slim
WORKDIR /django_start
COPY ./requirements.txt /django_start/requirements.txt
RUN pip install --no-cache-dir -r /django_start/requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]