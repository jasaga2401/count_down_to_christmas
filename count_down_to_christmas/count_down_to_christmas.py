

# count down until Christmas
from datetime import datetime

def countdown_to_christmas():
    # Get the current date and time
    now = datetime.now()

    # Set the date for Christmas
    current_year = now.year
    christmas_date = datetime(current_year, 12, 25)

    # Check if Christmas has already passed for this year
    if now > christmas_date:
        christmas_date = datetime(current_year + 1, 12, 25)

    # Calculate the time difference manually
    total_seconds = int((christmas_date - now).total_seconds())
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds until Christmas!"

# Run the countdown
print(countdown_to_christmas())
