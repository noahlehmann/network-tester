# https://github.com/sivel/speedtest-cli
from datetime import datetime

import speedtest as st


class Result:
    def __init__(self, timestamp, ping_ms, download_mb, upload_mb, ip, isp, country, lat, lon):
        self.timestamp = timestamp
        self.ping_ms = ping_ms
        self.download_mb = download_mb
        self.upload_mb = upload_mb
        self.ip = ip
        self.isp = isp
        self.country = country
        self.lat = lat
        self.lon = lon


def test_network_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    ping_ms = speed_test.results.ping

    download = speed_test.download()
    upload = speed_test.upload()

    download_mbs = round(download / (10 ** 6), 2)
    upload_mbs = round(upload / (10 ** 6), 2)

    config = speed_test.get_config()

    return create_result(
        ping_ms, download_mbs, upload_mbs, config.get("client")
    )


def create_result(ping_ms, download_mb, upload_mb, config):
    return Result(
        datetime.now(),
        ping_ms, download_mb, upload_mb,
        config.get("ip"),
        config.get("isp"),
        config.get("country"),
        config.get("lat"),
        config.get("lon")
    )
