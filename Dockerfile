FROM python:3.9

WORKDIR /app

COPY requirements.txt manage.py /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=trainerconnect.settings
ENV DEBUG=False

RUN python manage.py migrate && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", ":8000"]