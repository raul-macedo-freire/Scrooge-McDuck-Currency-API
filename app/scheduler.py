import sched
import time


def cron_scheduler(callback, minutes: int = 10, *args, **kwargs):
    scheduler = sched.scheduler(time.time, time.sleep)

    delay = minutes*60
    callback(*args, **kwargs)
    while True:
        scheduler.enter(delay, 1, callback, args, kwargs)

        scheduler.run()
