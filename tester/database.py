import psycopg2
from internet_speed import Result
from enum import Enum
from datetime import datetime


class LogLevel(Enum):
    INFO = "INFO",
    WARN = "WARN",
    ERROR = "ERROR"


class Database:
    def __init__(self, host="localhost"):
        self.host = host

    def save_result(self, result: Result):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            """
             INSERT INTO t_speed_test_result (exec_timestamp, successful, ping_ms, download_mb, upload_mb, ip, isp, country, lat, lon)
             VALUES ( 
             %(exec_timestamp)s, %(successful)s,  %(ping_ms)s, %(download_mb)s, %(upload_mb)s, 
             %(ip)s, %(isp)s, %(country)s, %(lat)s, %(lon)s 
             )
             RETURNING id;
             """,
            {
                'exec_timestamp': result.timestamp,
                'successful': True,
                'ping_ms': result.ping_ms,
                'download_mb': result.download_mb,
                'upload_mb': result.upload_mb,
                'ip': result.ip,
                'isp': result.isp,
                'country': result.country,
                'lat': result.lat,
                'lon': result.lon
            }
        )
        row_id = cur.fetchone()[0]

        cur.execute(
            """INSERT INTO t_log (log_timestamp, level, msg, fk_test)
            VALUES (%(log_timestamp)s, %(level)s, %(msg)s, %(fk_test)s)""",
            {
                'log_timestamp': result.timestamp,
                'level': LogLevel.INFO.value,
                'msg': "Test Successful",
                'fk_test': row_id
            }
        )

        conn.commit()
        cur.close()
        conn.close()

    def save_unsuccessful(self, date_time: datetime, msg: str, error: bool):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            """
             INSERT INTO t_speed_test_result (exec_timestamp, successful)
             VALUES ( %(exec_timestamp)s, %(successful)s )
             RETURNING id;
             """,
            {
                'exec_timestamp': date_time,
                'successful': False
            }
        )
        row_id = cur.fetchone()[0]

        cur.execute(
            """INSERT INTO t_log (log_timestamp, level, msg, fk_test)
            VALUES (%(log_timestamp)s, %(level)s, %(msg)s, %(fk_test)s)""",
            {
                'log_timestamp': date_time,
                'level': LogLevel.ERROR.value if error else LogLevel.WARN.value,
                'msg': msg,
                'fk_test': row_id
            }
        )

        conn.commit()
        cur.close()
        conn.close()

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            port=5432,
            database="postgres",
            user="user",
            password="password"
        )
