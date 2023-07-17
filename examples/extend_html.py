import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import HTMLTemplate, TightHTMLTemplate, SuperTightHTMLTemplate
from ecpyecharts.charts import *

# create 2 html template, here `html_1` is standard template and `html_2` is tight template
html_1 = HTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html_2 = TightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html_3 = SuperTightHTMLTemplate(title="hello", background_color='gray', chart_height='300px')


# append bar chart into `html_1`
chart = BarTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html_1.append_chart(chart)


# append 2 pie charts into `html_2`
data_group_name = ['BJ']
data_group = [{'A': 12, 'B': 33, 'C': 24, 'D': 53}]

chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html_2.append_chart(chart)

chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html_2.append_chart(chart)


# now we put the charts of `html_2` into `html_1`
# after extension, the template cannot append charts any more
# please use it before export
html_2.extend(html_1)
html_2.export("../tmp/extend_html.html")

