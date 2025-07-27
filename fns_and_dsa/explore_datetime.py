import datetime
from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date)
display_current_datetime() 

def calculate_future_date():
    current_date = datetime.now()
    days_toadd = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=days_toadd)
    future_date = current_date + delta
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
calculate_future_date()

