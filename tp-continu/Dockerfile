FROM python:3.14-slim

WORKDIR /app

RUN useradd -ms /bin/bash pythonuser

RUN chown -R pythonuser:pythonuser /app

COPY requirement.txt .

RUN pip install -r requirement.txt

EXPOSE 5000

COPY app/ .

USER pythonuser

ENTRYPOINT flask run --host 0.0.0.0

