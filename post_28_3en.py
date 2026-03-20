# Kajotte Studio
# -----------------------------------------------------------------------------
# AUTHOR: Kajotte Studio (kajotte-studio.com)
# LICENSE: MIT License
# LEGAL & TECHNICAL DOCUMENTATION: https://kajotte-studio.com/docs
# -----------------------------------------------------------------------------
# kajotte-studio.com

from datetime import datetime, timedelta

today = datetime.now()
# Calculate the date 10 days and 12 hours from now
in_10_days = today + timedelta(days=10, hours=12)
# Calculate the date 3 weeks ago
three_weeks_ago = today - timedelta(weeks=3)

print("\n--- Time Operations (timedelta) ---")
print(f"Today:              {today.strftime('%Y-%m-%d %H:%M')}")
print(f"In 10 days and 12h: {in_10_days.strftime('%Y-%m-%d %H:%M')}")
print(f"3 weeks ago:        {three_weeks_ago.strftime('%Y-%m-%d %H:%M')}")

# Calculate the difference (timedelta) between two dates
created_date = datetime(year=2023, month=1, day=14, hour=21)
difference = today - created_date

print(f"\nDifference since 01/15/2023 (21:00): {difference.days} days and {difference.seconds // 3600} hours.")

input('\nPress - Enter\n')
