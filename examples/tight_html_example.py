import random
from ecpyecharts.html import TightHTMLTemplate
from ecpyecharts.charts import BarTemplate, LineTemplate, PieTemplate, ScatterTemplate


def gen_random_curve(length=500, exp_bais=0):
    RANDOM_CURVE = [1]
    for i in range(length-1):
        RANDOM_CURVE.append(RANDOM_CURVE[-1] + random.randint(-100 + exp_bais, 100 + exp_bais)/ 100)
    return RANDOM_CURVE




html = TightHTMLTemplate(title="hello", background_color="gray", chart_height='400px')


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

# export the html template to a file
html.export('../tmp/tight_html_example.html')