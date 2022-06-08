FROM python:3.9

# gettext for translations
RUN apt update
RUN apt install gettext -y



WORKDIR /usr/src/app

COPY requirements.txt ./
# installing requirements for python to run web site
RUN pip install -r requirements.txt
COPY . .

# translations for web site
RUN python manage.py compilemessages

# db migrations
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb

# running server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

