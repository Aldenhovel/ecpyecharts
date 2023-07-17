import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import HTMLTemplate, TightHTMLTemplate, VeryTightHTMLTemplate
from ecpyecharts.charts import *

# create 2 html template, here `html_1` is standard template and `html_2` is tight template
html_1 = HTMLTemplate(title="hello", background_color="gray", chart_height='400px')
html_2 = TightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html_3 = VeryTightHTMLTemplate(title="hello", background_color='gray', chart_height='300px')
html_4 = VeryTightHTMLTemplate(title="hello", background_color='gray', chart_height='300px')

# append bar chart into `html_1`
chart = BarTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY', 'YUNAN', 'DAXIN', 'XUEE'],
               ydata={'Age': [random.randint(20, 65) for _ in range(10)],})
html_1.append_chart(chart)


# append 2 pie charts into `html_2`
data_group_nameA = ['BJ']
data_group_nameB = ['BJ', 'SH']
data_groupA = [{'A': 12, 'B': 33, 'C': 24, 'D': 53}]
data_groupB = [{'A': 132, 'B': 343, 'C': 234, 'D': 153}, {'A': 123, 'B': 143, 'C': 334, 'D': 103}]

chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_nameA, data_group=data_groupA)
html_2.append_chart(chart)

chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_nameB, data_group=data_groupB)
html_2.append_chart(chart)

# html_3
data_group_name = ['1990s', '2000s', '2010s']
data_group = [
    # group 1
    [
        [286, 77, 1709, 'Australia'],
        [311, 77, 2440, 'Canada'],
        [154, 68, 5773, 'China'],
        [130, 74, 1082, 'Cuba'],
        [599, 75, 4705, 'Finland'],
        [476, 77, 3299, 'France'],
        [316, 75, 8237, 'Germany'],
        [286, 78, 2830, 'Iceland']
    ],
    # group 2
    [
        [446, 81, 8973, 'Australia'],
        [294, 21, 3527, 'Canada'],
        [334, 36, 1943, 'China'],
        [291, 48, 9562, 'Cuba'],
        [323, 80, 5457, 'Finland'],
    ],
    # group 3
    [
        [326, 23, 8943, 'Australia'],
        [222, 45, 1245, 'Canada'],
        [124, 63, 5672, 'China'],
        [512, 73, 3244, 'France'],
    ],
]
chart = ScatterTemplate(title="Demo", subtitle="this is the subtitle of the demo")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html_3.append_chart(chart)


# create the 2nd chart and append it into html template
chart = LineTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html_3.append_chart(chart)

chart = BarTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html_3.append_chart(chart)

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
html_4.append_chart(chart)


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
html_4.append_chart(chart)

# now we put the charts of `html_2` into `html_1`
# after extension, the template cannot append charts any more
# please use it before export
html_2.extend(html_1).extend(html_3).extend(html_4)
html_2.export("../tmp/demo.html")

