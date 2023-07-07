import random
from ecpyecharts.templates import HTMLTemplate
from ecpyecharts.options.OP_bar import BarOption

html = HTMLTemplate(title="hello", background_color="black")
op = BarOption(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
op.init_option(xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
               ydata={'BJ': [random.randint(0, 100) for _ in range(11)],
                      'SH': [random.randint(0, 100) for _ in range(11)],
                      'HK': [random.randint(0, 100) for _ in range(11)]
                      })
html.add_chart(op)
op = BarOption(title="Chart B", subtitle="this is the subtitle of B", xaxis='Name', yaxis='Age')
op.init_option(xdata=['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'],
               ydata={'Age': [random.randint(0, 100) for _ in range(7)],})
html.add_chart(op)
html.export('../tmp/bar_example.html')