import calendar
import datetime
from budget.models import Spent


def monthly_spent_dict():
    month_name_list = list(calendar.month_name)
    month_name_list.pop(0)
    month_spent = {}
    month_ranges = []
    for m_name, m_num in zip(month_name_list, range(1, 13)):
        year_num = datetime.datetime.now().year
        _, num_days = calendar.monthrange(year_num, m_num)
        start = datetime.date(year_num, m_num, 1).strftime('%Y-%m-%d')
        end = datetime.date(year_num, m_num, num_days).strftime('%Y-%m-%d')
        month_spent[m_name] = Spent.objects.filter(date__range=[start, end])
        month_ranges.append([start, end])

    return month_spent, month_ranges
