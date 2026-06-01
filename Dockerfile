
# slim smaller version of python
FROM python:3.12-slim

WORKDIR /base

COPY requirements.txt .

RUN pip install -r requirements.txt

# to stop .pyc files inside container 
ENV PYTHONDONTWRITEBYTECODE=1

# print logs instead of buffering
ENV PYTHONUNBUFFERED=1
# copy all the projects file
COPY . .

RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
