import datetime
import time
from playsound import playsound

def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM:SS AM/PM): ").strip()
    try:
        alarm_hour = int(alarm_time.split(":")[0])
        alarm_minute = int(alarm_time.split(":")[1])
        alarm_second = int(alarm_time.split(":")[2].split()[0])
        alarm_period = alarm_time.split(":")[2].split()[1].upper()

        if alarm_period == "PM" and alarm_hour != 12:
            alarm_hour += 12
        if alarm_period == "AM" and alarm_hour == 12:
            alarm_hour = 0
    except Exception as e:
        print("Invalid format. Please enter time as HH:MM:SS AM/PM")
        return

    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.datetime.now()
        if (now.hour == alarm_hour and
            now.minute == alarm_minute and
            now.second == alarm_second):
            print("Wake up!")
            playsound("alarm.mp3")
            break
        time.sleep(1)

set_alarm()
