FROM mcr.microsoft.com/playwright/python:latest

ARG TEST_PROFILE=api
ARG BACKEND_URL=http://host.docker.internal:4111/api
ARG DATABASE_URL=postgresql+psycopg2://symfony:password@host.docker.internal:5432/symfony_db

ENV TEST_PROFILE=${TEST_PROFILE}
ENV BACKEND_URL=${BACKEND_URL}
ENV DATABASE_URL=${DATABASE_URL}
ENV PYTHONPATH=/app

WORKDIR /app

COPY Module_5/requirements.txt .

RUN pip install -r requirements.txt

COPY Module_5 ./Module_5

CMD ["pytest", "Module_5", "-m", "api", "--alluredir=/app/reports/allure"]