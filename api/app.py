import datetime
import getopt
import sys

from flask import Flask, request

from database import Database

app = Flask(__name__)

flag_set: bool = False

try:
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "hd:", ["docker"])
    for opt, arg in opts:
        if opt in ("--docker", "-d"):
            flag_set = True
except getopt.GetoptError:
    print(
        "Invalid Arguments passed. "
        "Valid Options are -d or --docker for running inside docker. "
        "Defaulting to localhost mode"
    )

database = Database(host="pg" if flag_set else "localhost")


@app.route("/dump")
def get_test_dump():
    return database.dump_speed_tests()


def to_date(data_str):
    return datetime.datetime.strptime(data_str, "%Y-%m-%d").date()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
