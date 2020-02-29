# -*- coding: utf-8 -*-#
import datetime


def opt_date(number):
    new_time = datetime.datetime.now()
    if isinstance(number, int):
        cut_date = new_time + datetime.timedelta(days=number)
        old_date_str = datetime.datetime.strftime(cut_date, "%Y-%m-%d")
        print(old_date_str)
        return old_date_str

if __name__ == '__main__':
    opt_date(2)
