FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install gettext -y

WORKDIR /server

RUN python -m pip install --upgrade pip && pip install poetry
COPY ./pyproject.toml /server

RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-root --only main
RUN rm /server/pyproject.toml

COPY ./src /server

EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py seed_db && \
    python manage.py runserver 0.0.0.0:8000
