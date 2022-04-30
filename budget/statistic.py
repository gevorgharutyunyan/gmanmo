import datetime

from django.db.models import Sum
from budget.utils import monthly_spent_dict
from budget.models import Spent
from budget.config_params import stat_headers, fields, month_dict
from django.shortcuts import render


class Statistics:

    @staticmethod
    def render_statistic(request):
        stat_dict = {
            "daily": Statistics.daily_stat(),
            "monthly_sum": Statistics.monthly_stat()[0],
            "spent_amount": Statistics.monthly_stat()[1],
            "stat_headers": stat_headers
        }
        return render(request, 'budget/statistics.html', stat_dict)

    @staticmethod
    def daily_stat():
        last_spent = []
        for tb_fld in fields:
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            last_day = Spent.objects.all().filter(date=today).values_list(tb_fld)[0][0]
            last_spent.append(last_day)
        last_day_sum = sum(last_spent[1:])
        return last_day_sum

    @staticmethod
    def monthly_stat():
        month_spent = monthly_spent_dict()[0]
        month_ranges = monthly_spent_dict()[1]
        monthly_sum = dict()
        col_sum_list = []
        for month_name, mth_range in zip(month_spent, month_ranges):
            col_sum_list.clear()
            for col_name in fields[1:]:  # Date field can not be summed cause of that [1:]
                each_item_sum = month_spent[month_name].filter(date__range=mth_range).aggregate(Sum(col_name))
                if each_item_sum[(col_name + "__sum")] is None:
                    each_item_sum[(col_name + "__sum")] = 0
                else:
                    each_item_sum = month_spent[month_name].filter(date__range=mth_range).aggregate(Sum(col_name))
                    monthly_sum.setdefault(month_name, {}).update(each_item_sum)

        spent_amount = month_dict  # Don't change initial dictionary month_dict
        for month_name, sec_sum in monthly_sum.items():
            mt_amount = sum(sec_sum.values())
            month_dict[month_name] = mt_amount

        return monthly_sum, spent_amount

    def yearly_stat(self):
        pass
