import datetime
from datetime import timedelta

import psycopg2


class Database:
    def __init__(self, host="localhost"):
        self.host = host

    def dump_speed_tests(self, start=datetime.date.min, end=datetime.date.today()):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            """
                SELECT * FROM t_speed_test_result
                WHERE exec_timestamp BETWEEN %(start)s AND %(end)s;
            """,
            {
                'start': start,
                'end': end + timedelta(days=1)
            })

        results = cur.fetchall()

        cur.close()
        conn.close()

        return results

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            port=5432,
            database="postgres",
            user="user",
            password="password"
        )
