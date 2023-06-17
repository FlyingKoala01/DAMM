from dateutil.relativedelta import relativedelta
from datetime import datetime

def one_month_ago(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    one_month_ago = date_obj - relativedelta(months=1)
    return one_month_ago

def one_year_ago(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    one_year_ago = date_obj - relativedelta(years=1)
    return one_year_ago
