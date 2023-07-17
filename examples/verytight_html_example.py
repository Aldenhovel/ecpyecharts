import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import VeryTightHTMLTemplate
from ecpyecharts.charts import *


def gen_random_curve(length=500, exp_bais=0):
    RANDOM_CURVE = [1]
    for i in range(length-1):
        RANDOM_CURVE.append(round(RANDOM_CURVE[-1] + random.randint(-100 + exp_bais, 100 + exp_bais) / 100, 4))
    return RANDOM_CURVE




html = VeryTightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')


chart = LineTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
chart.init_option(xdata=[str(i) for i in range(200)],
               ydata={'BJ Score': gen_random_curve(200, exp_bais=10),
                      'SH Score': gen_random_curve(200, exp_bais=5),
                      'HK Score': gen_random_curve(200, exp_bais=-10)
                      })
html.append_chart(chart)

chart = LineTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
chart.init_option(xdata=[str(i) for i in range(200)],
               ydata={'BJ Score': gen_random_curve(200, exp_bais=10),
                      'SH Score': gen_random_curve(200, exp_bais=5),
                      'HK Score': gen_random_curve(200, exp_bais=-10)
                      })
html.append_chart(chart)

data_group_name = ['BJ']
data_group = [
    {
        'A': 12,
        'B': 33,
        'C': 24,
        'D': 53,
    }
]
chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)

data_group_name = ['1990s']
data_group = [
    [
        [286, 77, 1709, 'Australia'],
        [311, 77, 2440, 'Canada'],
        [154, 68, 5773, 'China'],
    ],
]
chart = ScatterTemplate(title="Demo", subtitle="this is the subtitle of the demo")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)

chart = ScatterTemplate(title="Demo", subtitle="this is the subtitle of the demo")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)

chart = BarTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html.append_chart(chart)


date = ['2023-7-1', '2023-7-2', '2023-7-3', '2023-7-4', '2023-7-5']
price = [
    # [start, end, low, high]
    [20, 34, 10, 38],
    [40, 35, 30, 50],
    [31, 38, 33, 44],
    [38, 15, 5, 42],
    [34, 44, 12, 56],
]

chart = CandleStickTemplate(title="Stock Price", subtitle="this is the subtitle", xaxis='Date', yaxis='Price')
chart.init_option(xdata=date, ydata=price)
html.append_chart(chart)

chart = BarTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
chart.init_option(xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
               ydata={'BJ Score': [random.randint(0, 100) for _ in range(11)],
                      'SH Score': [random.randint(0, 100) for _ in range(11)],
                      'HK Score': [random.randint(0, 100) for _ in range(11)],
                      'CA Score': [random.randint(0, 100) for _ in range(11)],
                      })
html.append_chart(chart)

# export the html template to a file
html.export('../tmp/verytight_html_example.html')