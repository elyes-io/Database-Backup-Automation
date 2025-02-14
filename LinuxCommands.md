# Create and Edit a Cron Job to Schedule the Script

# Open the crontab for the current user
crontab -e

# Set up the configuration file by specifying the schedule (minute - hour - day of the month - month - day of the week)
# This runs the backup script every day at 3:00 AM
0 3 * * * /usr/bin/python3 /path/backup.py

# Save and exit the crontab editor

# 3. Manually Run the Backup Script (For testing or one-time run)
python3 /path/backup.py

# 4. Verify Cron Jobs
crontab -l