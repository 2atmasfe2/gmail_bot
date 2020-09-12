FROM python:3.8-alpine3.12

WORKDIR /app


COPY requirements requirements
RUN pip install -U pip
RUN pip install -Ur requirements/development.txt


COPY docker-entrypoint.sh docker-entrypoint.sh
COPY run.py .

CMD ["./docker-entrypoint.sh"]
