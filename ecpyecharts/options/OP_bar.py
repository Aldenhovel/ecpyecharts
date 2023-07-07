
import random
import pandas as pd
from typing import List, Dict

_template = \
""" 
<div id="chart_$id$" style="width: 80%; height: 500px; border-radius: 20px; background-color: white; margin: 10px auto"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_$id$'));
    option_$id$ = {
        grid: { left: '15%', right: '15%', top: '10%', bottom: '10%'},
        title: {text: '$title$', subtext: '$subtitle$', left: 'center'},
        xAxis: { type: 'category', data: $xdata$, show: $$show_xaxis$$, name: '$xaxis$'},
        yAxis: { type: 'value', name: '$yaxis$' },
        toolbox: { show: true, feature: { magicType: { show: true, type: ['line', 'bar'] }, restore: { show: true }, saveAsImage: { show: true }}},
        tooltip: { trigger: 'axis', position: function (pt) { return [pt[0], '10%']; }},
        $$datazoom$$
        series: [$series$]
    };
    myChart.setOption(option_$id$);
</script>
"""

class BarOption():

    def __init__(self, id='', title='', subtitle='', xaxis='X', yaxis='Y'):
        self.org_template = _template
        self.wf_template = _template
        self.id = id if id != '' else f"{random.randint(0, 1000000)}"
        self.title = title
        self.subtitle = subtitle
        self.xaxis = xaxis
        self.yaxis = yaxis



    def init_option(self, xdata: List[str], ydata: Dict[str, List]):

        y_lens = [len(item[1]) for item in ydata.items()]
        assert min(y_lens) == max(y_lens), f"all y data should have the same length, but got {y_lens}"

        show_xaxis = 'true'
        datazoom = ''
        if len(xdata) > 10:
            # use data zoom mode
            show_xaxis = 'false'
            datazoom = r"dataZoom: [{ type: 'inside', start: 0, end: 100 }, { start: 0, end: 100 }, {show: true, yAxisIndex: 0, filterMode: 'empty', width: 30, height: '80%', showDataShadow: false, left: '86%' }],"



        assert min(y_lens) == len(xdata), f"x and y data should have the same length, but got {len(xdata)} and {min(y_lens)}"

        xdata_template = str(xdata)

        series_template = ""
        for name, array in ydata.items():
            series_template = series_template + '{' + f"name: '{name}', type: 'bar', data: {str(array)}" + '},'

        self.wf_template = self.wf_template.replace('$id$', self.id)\
            .replace('$title$', self.title)\
            .replace('$subtitle$', self.subtitle)\
            .replace('$xaxis$', self.xaxis)\
            .replace('$yaxis$', self.yaxis)\
            .replace('$xdata$', xdata_template)\
            .replace('$series$', series_template)\
            .replace('$$datazoom$$', datazoom)\
            .replace('$$show_xaxis$$', show_xaxis)

    def export(self):
        keywords = []
        export_template = self.wf_template
        for kw in keywords:
            export_template.replace(kw, '')
        return export_template


if __name__ == "__main__":

    op = BarOption()
    op.init_option(xdata=['Sun', 'Mon', 'TUE'], ydata={'BJ': [12,45,21], 'SH': [45,12,90]})


