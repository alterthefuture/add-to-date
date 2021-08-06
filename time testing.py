from datetime import datetime
from datetime import timedelta 

today_date = datetime.now()
current_date = today_date.strftime("%B %d, %Y %I:%M %p")

time = input(f"Format: 1d\nHow much days = D, seconds = S, or minutes = M, would you like to add to your current date? ")

if "d" in time or "D" in time:
    if "1" in time:
        new_date = datetime.now() + timedelta(days=1)
        layout = new_date.strftime("%B %d, %Y %I:%M %p")

        input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
    else:
        if "d" in time:
            times = time.replace('d','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(days=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
        elif "D" in time:
            times = time.replace('D','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(days=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
elif "s" in time or "S" in time:
    if "1" in time:
        new_date = datetime.now() + timedelta(seconds=1)
        layout = new_date.strftime("%B %d, %Y %I:%M %p")

        input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
    else:
        if "s" in time:
            times = time.replace('s','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(seconds=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
        elif "S" in time:
            times = time.replace('S','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(seconds=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
elif "m" in time or "M" in time:
    if "1" in time:
        new_date = datetime.now() + timedelta(minutes=1)
        layout = new_date.strftime("%B %d, %Y %I:%M %p")

        input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
    else:
        if "m" in time:
            times = time.replace('m','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(minutes=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
        elif "M" in time:
            times = time.replace('M','')
            int_date = int(times)

            new_date = datetime.now() + timedelta(minutes=int_date)
            layout = new_date.strftime("%B %d, %Y %I:%M %p")

            input(f"\nCurrent Date: {current_date}\nNew Date: {layout}\n\nPress any key to close.")
        