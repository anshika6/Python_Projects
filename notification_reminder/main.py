import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title =" Please Drink Water now!!",
            message = " About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 "
                      "liters) of fluids a day for women.",
            timeout=10,
            app_icon = r"C:\Users\anshi\Python_Projects\notification_reminder\icon.ico"
        )
        time.sleep(60*60)