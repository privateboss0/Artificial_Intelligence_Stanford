import calendar
import datetime
import re

# Get the current year and month
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

# Create regular expression patterns
dday = r'\b{current_year}\b'.format(current_year=current_year)
ddayc = r"\033[31m\033[1m{current_year}\033[0m".format(current_year=current_year)
ddayd = r'\b{current_day}\b'.format(current_day=current_day)
ddaydc = r"\033[31m\033[1m{current_day}\033[0m".format(current_day=current_day)

# Replace the current year and date with colored text
calendar_text = calendar.month(current_year, current_month)
calendar_text = re.sub(dday, ddayc, calendar_text)
calendar_text = re.sub(ddayd, ddaydc, calendar_text)

print(calendar_text)