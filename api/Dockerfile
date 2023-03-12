FROM python:3.9-alpine3.16

WORKDIR /app

COPY . .

RUN apk add build-base postgresql-dev
RUN pip install -r requirements.txt

ENV FLASK_APP=app

CMD ["python", "/app/app.py", "--docker"]