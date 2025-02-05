# syntax=docker/dockerfile:1

FROM python:slim-bullseye

WORKDIR /app
ENV FLASK_APP=run.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]