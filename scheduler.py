import time

import schedule

from driver import run_driver


def start_scheduler():
    schedule.every().day.at("09:00", "America/New_York").do(run_driver)

    while True:
        schedule.run_pending()
        time.sleep(3600)
