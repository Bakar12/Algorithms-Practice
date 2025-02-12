import datetime

# Get current date and time
now = datetime.datetime.now()

# Open (or create) a log file and append a new log entry
with open("update.log", "a") as log_file:
    log_file.write(f"Update run on: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

print("Update script ran successfully!")
