import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import TightHTMLTemplate
from ecpyecharts.charts import *


html = TightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')

data_group_name = ['BJ']
data_group = [{'A': 12, 'B': 33, 'C': 24, 'D': 53}]
chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)

# Here we start a new row of charts
html.new_row()

data_group_name = ['1990s']
data_group = [[[286, 77, 1709, 'Australia'], [311, 77, 2440, 'Canada'], [154, 68, 5773, 'China']]]
chart = ScatterTemplate(title="Demo", subtitle="this is the subtitle of the demo")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)


# export the html template to a file
html.export('../tmp/new_row_example.html')