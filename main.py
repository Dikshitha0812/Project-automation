  
import datetime
import time
import requests
from plyer import notification

title='Reminder'
message='Drink Water'
notification.notify(
    title=title,
    message=message,
    app_icon=None,
    timeout=3,
    toast=False
)
time.sleep(1800)
