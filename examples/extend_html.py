import sys
import pathlib
sys.path.append(str(pathlib.Path('.').absolute().parent))

import random
from ecpyecharts.html import HTMLTemplate, TightHTMLTemplate
from ecpyecharts.charts import *

# create a html template
html1 = HTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html2 = HTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html3 = TightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')
html4 = TightHTMLTemplate(title="hello", background_color="gray", chart_height='300px')



# create a bar chart template and init it, append it into the html template
chart = BarTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
chart.init_option(xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
               ydata={'BJ Score': [random.randint(0, 100) for _ in range(11)],
                      'SH Score': [random.randint(0, 100) for _ in range(11)],
                      'HK Score': [random.randint(0, 100) for _ in range(11)],
                      'CA Score': [random.randint(0, 100) for _ in range(11)],
                      })
html1.append_chart(chart)


# create the 2nd chart and append it into html template
chart = BarTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html2.append_chart(chart)



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
html3.append_chart(chart)
chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html3.append_chart(chart)

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
html4.append_chart(chart)


html3.extend(html1)

html3.export("../tmp/extend_html.html")