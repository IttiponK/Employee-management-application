FROM python:3.10.14-alpine3.19

RUN apk add --no-cache mariadb-dev build-base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apk del mariadb-dev build-base

COPY handler /app/handler

COPY hexagonalmodel /app/hexagonalmodel

COPY infrastructure /app/infrastructure

CMD ["flask","--app","handler.run_flask:app","run","--host","0.0.0.0"]