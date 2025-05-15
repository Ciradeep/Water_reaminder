import time
from plyer import notification

interval_minutes = 30
total_reminders = 8
log_file = "water_log.txt"

print("Water Reminder Started!")

for i in range(total_reminders):
    time.sleep(interval_minutes * 60)

    current_time = time.strftime("%I:%M %p")
    current_date = time.strftime("%Y-%m-%d")

    notification.notify(
        title="Water Reminder",
        message=f"Time to drink water! ({i + 1}/{total_reminders})\nTime: {current_time} on {current_date}",
        timeout=10
    )

    with open(log_file, "a") as file:
        file.write(f"Reminder {i + 1}/{total_reminders} at {current_time} on {current_date}\n")