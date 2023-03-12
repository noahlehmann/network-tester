from speedtest import ConfigRetrievalError
from internet_speed import test_network_speeds
from database import Database
from datetime import datetime
import sys, getopt


def main(in_docker: bool):
    db: Database
    if in_docker:
        db = Database("pg")
    else:
        db = Database()
    result = None
    try:
        result = test_network_speeds()
    except ConfigRetrievalError as config_retrieval_error:
        err_msg = str(config_retrieval_error)
        db.save_unsuccessful(datetime.now(), err_msg, False)
        return 1
    except Exception as exception:
        err_msg = str(exception)
        db.save_unsuccessful(datetime.now(), err_msg, True)
        return 2
    finally:
        if result is not None:
            db.save_result(result)


def check_docker_flag(argv):
    flag_set: bool = False

    try:
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
    return flag_set


if __name__ == "__main__":
    docker_flag_set = check_docker_flag(sys.argv[1:])
    log_str = "%s [%s]:[%s] %s"
    host = "DOCKER" if docker_flag_set else " HOST "
    try:
        main(docker_flag_set)
        print(log_str % (datetime.now(), "INFO", host, "Network Speed Test Successfully executed"))
    except Exception as e:
        print(log_str % (datetime.now(), "ERROR", host, str(e).replace("\n", "")))
