from datetime import datetime


def get_datetime():
    current = datetime.today()
    day = current.day
    month = current.month
    year = current.year
    hour = current.hour
    minute = current.minute
    return "{day}.{month}.{year}\n{hour}:{minute}".format(day=day, month=month,
                                                         year=year, hour=hour, minute=minute)


def time_before_signal():
    current = datetime.today()
    return 60 - current.second, 1_000_000 - current.microsecond


def set_current_datetime(label):
    label.setText(get_datetime())


TIMER_DELAY = 5


def set_current_time(label, decrease):
    label.setText(str(TIMER_DELAY - decrease))

# time_delay = time_before_signal()
# print(int(time_delay[0] * 1000 + time_delay[1] / 1000))