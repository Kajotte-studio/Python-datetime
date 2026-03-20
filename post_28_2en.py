# Kajotte Studio
# -----------------------------------------------------------------------------
# AUTHOR: Kajotte Studio (kajotte-studio.com)
# LICENSE: MIT License
# LEGAL & TECHNICAL DOCUMENTATION: https://kajotte-studio.com/docs
# -----------------------------------------------------------------------------
# kajotte-studio.com 

from datetime import datetime

# Get the full datetime object
now = datetime.now()

# Creating an elegant datestamp
# Using appropriate directives for the format "Today is: Tuesday, October 07 2025"
elegant_datestamp = now.strftime("Today is: %A, %B %d %Y")

print("\n--- Elegant Datestamp ---")
print(elegant_datestamp)

# Another example: Abbreviated international format + Day of the Year
tech_datestamp = now.strftime("%Y-%m-%d (Day of year: %j)")
print(f"Technical format: {tech_datestamp}")
input('\nPress - Enter\n')
