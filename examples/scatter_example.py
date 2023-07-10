import random
from ecpyecharts.html import HTMLTemplate
from ecpyecharts.charts import ScatterTemplate

# create a html template
html = HTMLTemplate(title="hello", background_color="gray")

# group 1 & 2's name
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
html.append_chart(chart)


# The second scatter chart here
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

html.export('../tmp/scatter_example.html')