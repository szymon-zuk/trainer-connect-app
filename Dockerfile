FROM python:latest

RUN apt-get update && apt-get -y install python3-pip --fix-missing
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD cd trainerconnect && python manage.py runserver