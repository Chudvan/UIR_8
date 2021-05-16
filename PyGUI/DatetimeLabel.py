from datetime import datetime


def get_datetime(format):
    current = datetime.today()

    d = {
        'YYYY-MM-DDTHH:MM': current.strftime('%Y-%m-%dT%H:%M'),
        'DD.MM.YYYY\nHH:MM': current.strftime('%d.%m.%Y\n%H:%M')
    }
    return d[format]


def time_before_signal():
    current = datetime.today()
    return 60 - current.second, 1_000_000 - current.microsecond


def set_current_datetime(label):
    label.setText(get_datetime('DD.MM.YYYY\nHH:MM'))


TIMER_DELAY = 15


def set_current_time(label, decrease):
    label.setText(str(TIMER_DELAY - decrease))

# time_delay = time_before_signal()
# print(int(time_delay[0] * 1000 + time_delay[1] / 1000))