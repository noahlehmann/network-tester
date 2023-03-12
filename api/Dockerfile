FROM python:3.9-alpine3.16

WORKDIR /app

COPY . .

RUN apk add build-base postgresql-dev
RUN pip install -r requirements.txt

RUN echo "*/10 * * * * python /app/main.py --docker >> log.txt" > crontab.txt
RUN crontab crontab.txt

CMD ["crond", "-f"]

# flask run --host=0.0.0.0