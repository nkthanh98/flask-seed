FROM python:3.7-alpine

WORKDIR /app

EXPOSE 5000

RUN apk update --no-cache && apk add --no-cache mariadb-connector-c-dev gcc musl-dev

ADD ./requirements/requirements-prod.txt .

RUN pip install --no-cache-dir -r requirements-prod.txt

ADD . .

ENTRYPOINT gunicorn -c gunicorn.config.py wsgi:wsgi_app
