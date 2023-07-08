import random
from ecpyecharts.html import HTMLTemplate
from ecpyecharts.charts import LineTemplate

def gen_random_curve(length=500, exp_bais=0):
    RANDOM_CURVE = [1]
    for i in range(length-1):
        RANDOM_CURVE.append(RANDOM_CURVE[-1] + random.randint(-100 + exp_bais, 100 + exp_bais)/ 100)
    return RANDOM_CURVE

# create a html template
html = HTMLTemplate(title="hello", background_color="gray")

# create a bar chart template and init it, append it into the html template
chart = LineTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
chart.init_option(xdata=[str(i) for i in range(200)],
               ydata={'BJ Score': gen_random_curve(200, exp_bais=10),
                      'SH Score': gen_random_curve(200, exp_bais=5),
                      'HK Score': gen_random_curve(200, exp_bais=-10)
                      })
html.append_chart(chart)

# create the 2nd chart and append it into html template
chart = LineTemplate(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
chart.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(20, 65) for _ in range(7)],})
html.append_chart(chart)

# export the html template to a file
html.export('../tmp/line_example.html')