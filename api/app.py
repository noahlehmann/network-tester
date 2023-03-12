import datetime

from flask import Flask, request

from database import Database

app = Flask(__name__)

database = Database(host="raspberrypi")


@app.route("/dump")
def get_test_dump():
    start = request.args.get('start', type=to_date)
    end = request.args.get('end', type=to_date)
    return database.dump_speed_tests(start=start, end=end)


def to_date(data_str):
    return datetime.datetime.strptime(data_str, "%Y-%m-%d").date()

