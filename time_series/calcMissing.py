#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
import pandas as pd
import re

def calcMissing(readings):
    # Write your code here
    # for s in readings:
    #     print(s)
    dates, vals = list(), list()
    missing = list()
    for i, string in enumerate(readings):
        date, _, val = string.split()
        dates.append(date)
        if re.findall('^missing_.*', val, re.I):
            vals.append(None)
            missing.append(date)
        else:
            vals.append(float(val))
    ts = pd.DataFrame({'date': dates, 'value': vals})
    ts.index = pd.to_datetime(ts.loc[:, 'date'])
    ts = ts.drop(columns = ['date'])
    # ts['day'] = ts.index.day_name()
    res = ts.resample('D').interpolate(method = 'linear')
    res = res.fillna(method = 'backfill')
    # print(res.head(20))
    for n in res.loc[pd.to_datetime(missing), 'value'].values:
        print(n)
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
