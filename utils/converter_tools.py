from datetime import timedelta, time


def time_to_delta_time(time):
    return timedelta(hours=time.hour, minutes=time.minute, seconds=0)
