# Kajotte Studio
# -----------------------------------------------------------------------------
# RESOURCE NAME: Download Center
# AUTHOR: Kajotte Studio (kajotte-studio.com)
# LICENSE: MIT License
# LEGAL & TECHNICAL DOCUMENTATION: https://kajotte-studio.com/docs
# -----------------------------------------------------------------------------
# TERMS OF USE:
# Permission is granted under the MIT License, provided that this header 
# remains intact. Removal of this metadata or the documentation link 
# constitutes a direct violation of the license terms.
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
