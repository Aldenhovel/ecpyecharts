import random
from typing import Dict, List, Any

_template = \
r"""
<div id="chart_$id$" class="chartbox" style="width: $divWidth$; height: $divHeight$"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_$id$'));
    option_$id$ = {
        title: { text: '$title$', subtext: '$subtitle$', left: 'left'},
        xAxis: { name: '$xaxis$', data: $xdata$, show: $$show_xaxis$$,},
        yAxis: { name: '$yaxis$', show: true, scale: true,},
        tooltip: { formatter: function (param) { var data = param.data; return 'Position: ' + data[0] + ', ' + data[1] + '<br>Value: ' +  data[2]; }},
        legend: {orient: 'vertical', left: 'left', top: '12%' },
        grid: { left: '120', right: '10%', top: '90', bottom: '50'},
        tooltip: {trigger: 'axis', axisPointer: { type: 'cross', label: { backgroundColor: '#6a7985' } } },
        legend: { orient: 'vertical', left: 'left', top: '90' },
        $$datazoom$$
        series: [$series$]
};
    myChart.setOption(option_$id$);
</script>
"""


class CandleStickTemplate():

    def __init__(self, id='', title='', subtitle='', xaxis='X', yaxis='Y'):
        self.org_template = _template
        self.wf_template = _template
        self.id = id if id != '' else f"{random.randint(0, 1000000)}"
        self.title = title
        self.subtitle = subtitle
        self.xaxis = xaxis
        self.yaxis = yaxis

    def init_option(self, xdata: List, ydata: List[List]):

        series_template = \
        r"""
         {
          type: 'candlestick',
          data: $data$,
        },
        """.replace('$data$', str(ydata))

        show_xaxis = 'true'
        datazoom = ''
        if len(xdata) > 10:
            # use data zoom mode
            show_xaxis = 'true'
            datazoom = r"dataZoom: [{ type: 'inside', start: 0, end: 100 }, { start: 0, end: 100 ,bottom: '2%',height: 20},],"

        self.wf_template = self.wf_template.replace('$id$', self.id) \
            .replace('$title$', self.title) \
            .replace('$subtitle$', self.subtitle) \
            .replace('$series$', series_template)\
            .replace('$xaxis$', self.xaxis)\
            .replace('$xdata$', str(xdata))\
            .replace('$yaxis$', self.yaxis)\
            .replace('$$datazoom$$', datazoom)\
            .replace('$$show_xaxis$$', show_xaxis)

    def export(self):
        keywords = []
        export_template = self.wf_template
        for kw in keywords:
            export_template.replace(kw, '')
        return export_template
