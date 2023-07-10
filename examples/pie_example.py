import random
from ecpyecharts.html import HTMLTemplate
from ecpyecharts.charts import PieTemplate

# create a html template
html = HTMLTemplate(title="hello", background_color="gray")

data_group_name = ['BJ', 'SH', 'CA', 'HK']
data_group = [
    {
        'A': 12,
        'B': 33,
        'C': 24,
        'D': 53,
    },
    {
        'A': 12,
        'B': 13,
        'C': 44,
        'D': 53,
    },
    {
        'A': 4,
        'C': 74,
        'D': 53,
    },
    {
        'A': 12,
        'B': 33,
        'C': 24,
        'F': 5,
    },
]
chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)


# The 2nd pie chart
data_group_name = ['BJ']
data_group = [
    {
        'A': 12,
        'B': 33,
        'C': 24,
        'D': 53,
    },
]
chart = PieTemplate(title="Citys", subtitle="this is the subtitle of A")
chart.init_option(data_group_name=data_group_name, data_group=data_group)
html.append_chart(chart)


html.export('../tmp/pie_example.html')