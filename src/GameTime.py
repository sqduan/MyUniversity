from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime

dayDelta   = -1

def CalculateDate(total_days):
    # Define the start date
    start_date = datetime.date(2000, 1, 1)
    
    # Calculate the date offset
    date_offset = datetime.timedelta(days=total_days)
    
    # Calculate the target date
    target_date = start_date + date_offset
    
    # Extract day, month, and year
    day = target_date.day
    month = target_date.month
    year = target_date.year
    
    return day, month, year

# Function to be executed as Task 1
def DayIncrease():
    global dayDelta
    dayDelta = dayDelta + 1
    [day, month, year] = CalculateDate(dayDelta)
    print(f"Day: {day}, Month: {month}, Year: {year}")

# Create a scheduler
scheduler = BackgroundScheduler()

# Schedule Task 2 to run every 5 seconds
scheduler.add_job(DayIncrease, 'interval', seconds=0.001)

# Start the scheduler
scheduler.start()

try:
    # Keep the main thread alive
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    # Shutdown the scheduler on Ctrl+C
    scheduler.shutdown()
