# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG SECRETKEY
ARG DJANGOSETTINGSMODULE

ENV DJANGO_SECRET_KEY=$SECRETKEY
ENV DJANGO_SETTINGS_MODULE=$DJANGOSETTINGSMODULE

ENV DJANGO_DEBUG False

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]