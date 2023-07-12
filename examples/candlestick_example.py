import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import HTMLTemplate
from ecpyecharts.charts import CandleStickTemplate

# create a html template
html = HTMLTemplate(title="hello", background_color="gray")

# generate fake data for chart 1
date = ['2023-7-1', '2023-7-2', '2023-7-3', '2023-7-4', '2023-7-5']
price = [
    # [start, end, low, high]
    [20, 34, 10, 38],
    [40, 35, 30, 50],
    [31, 38, 33, 44],
    [38, 15, 5, 42],
    [34, 44, 12, 56],
]

# add the first CandleStick chart to html template
chart = CandleStickTemplate(title="Value", subtitle="this is the subtitle", xaxis='Date', yaxis='Value')
chart.init_option(xdata=date, ydata=price)
html.append_chart(chart)


# generate fake data for chart 2
def generate_dates(days=1000):
    from datetime import datetime, timedelta
    start_date = datetime(2000, 1, 1)
    dates = []
    for i in range(days):
        date_str = start_date.strftime("%Y-%m-%d")
        dates.append(date_str)
        start_date += timedelta(days=1)
    return dates


def generate_data(days=1000):
    import numpy as np
    def gen_random_curve(length=1000, exp_bais=0):
        RANDOM_CURVE = [1]
        for i in range(length - 1):
            RANDOM_CURVE.append(RANDOM_CURVE[-1] + random.randint(-100 + exp_bais, 100 + exp_bais) / 100)
        return RANDOM_CURVE

    open_ = np.asarray(gen_random_curve(days))
    high = open_ + np.random.rand(len(open_)) * 0.5 + 1
    low = open_ - np.random.rand(len(open_)) * 0.5 - 1
    close_ = open_ + np.random.randn(len(open_)) * np.random.randn()
    data = np.stack([open_, close_, high, low]).T.tolist()
    return data


date = generate_dates(100)
data = generate_data(100)

# add the second CandleStick chart to html template
chart = CandleStickTemplate(title="Value", subtitle="this is the subtitle", xaxis='Date', yaxis='Value')
chart.init_option(xdata=date, ydata=data)
html.append_chart(chart)

# export the html template to a file
html.export('../tmp/candlestick_example.html')