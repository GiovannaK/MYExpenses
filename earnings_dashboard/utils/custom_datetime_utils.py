from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

current_year = datetime.now().year
current_month = datetime.now().month
current_month_date = datetime.now()
last_day = calendar.monthrange(current_year, current_month)[1]

five_years_ago = current_year - 5
last_three_months = current_month_date - relativedelta(months=3)
last_year = current_year - 1

month_start = datetime(year=current_year, month=current_month, day=1)
month_end = datetime(year=current_year, month=current_month, day=last_day)

start_date = datetime(year=current_year, month=1, day=1)
end_date = datetime(year=current_year, month=12, day=31)

initial_year = datetime(year=five_years_ago, month=1, day=1)
final_year = datetime(year=current_year, month=12, day=31)

initial_last_year = datetime(year=last_year, month=1, day=1)
final_last_year = datetime(year=last_year, month=12, day=31)