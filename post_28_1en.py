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
import time 

def simple_clock(seconds=5):
    """Displays the current time in HH:MM:SS format and refreshes every second."""
    print(f"--- Clock running for {seconds} seconds ---")
    
    # Format codes: %H (Hour 24h), %M (Minute), %S (Second)
    time_format = "%H:%M:%S"
    
    for _ in range(seconds):
        now = datetime.now()
        formatted_time = now.strftime(time_format)
        
        # Using '\r' allows overwriting the previous line in the console
        print(f"Current time: {formatted_time}", end='\r')
        time.sleep(1)
        
    print("\n--- Clock finished ---")

# Calling the function
simple_clock(10)
