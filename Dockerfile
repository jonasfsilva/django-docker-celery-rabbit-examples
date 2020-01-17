FROM python:3.6-alpine
LABEL maintainer="Jonas Ferreira"

RUN apk update \
  # psycopg2 dependencies
  && apk add --no-cache postgresql-libs \
  && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev\
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  && apk add make \
  && apk add libxml2-dev libxslt-dev

# Upgrade pip
RUN pip install --upgrade pip --no-cache-dir

ENV PYTHONUNBUFFERED 1

RUN pip install psycopg2-binary
RUN pip install pipenv

RUN mkdir /code
WORKDIR /code

ADD Pipfile* /code/
RUN pipenv install --system

ADD . /code/