import os
from tqdm import tqdm
from time import sleep
from datetime import datetime


def get_datetime():
    d = datetime.now()
    t = (str(d.year) + "_" + str(d.month) + "_" + str(d.day) + "_" + str(d.hour) + "_" + str(d.minute))
    return t


def restart_celery():
    t = get_datetime()

    print("RESTART celery")
    os.system(
        f'pipenv run celery multi restart celery -A tasks --loglevel=INFO -P gevent -E -O fair --autoscale=10,'
        f'1 -n "NMP" -f ./logs/{t}.log'
    )


def run_server():
    t = get_datetime()

    print("RUN celery")
    os.system(
        f'pipenv run celery -A tasks worker --loglevel=INFO -P gevent -E -O fair --autoscale=10,1 -n "NMP"'
        f' -f ./logs/{t}.log')


def run_celery():
    for _ in range(1000):
        restart_celery()
        print("Restart At 4 Hours")
        s = 60 * 60 * 4
        for _ in tqdm(range(s)):
            sleep(1)


if __name__ == "__main__":
    # run_server()
    run_celery()
