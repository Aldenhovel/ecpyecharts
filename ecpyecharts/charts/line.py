import random
from typing import Dict, List

from ..colors import Color

_template = \
r"""
<div id="chart_$id$" style="width: 80%; height: 500px; border-radius: 20px; background-color: white; margin: 10px auto"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_$id$'));
    option_$id$ = {
    grid: { left: '10%', right: '10%', top: '15%', bottom: '10%'},
    tooltip: {trigger: 'axis', axisPointer: { type: 'cross', label: { backgroundColor: '#6a7985' } } },
    title: { left: 'left', text: '$title$', subtext: '$subtitle$' },
    //toolbox: { show: true, feature: { restore: { show: true }, saveAsImage: { show: true }}},
    xAxis: { type: 'category', data: $xdata$, boundaryGap: false, show: $$show_xaxis$$, name: '$xaxis$'},
    yAxis: { type: 'value', boundaryGap: [0, '50%'], name: '$yaxis$' },
    legend: {},
    $$datazoom$$
    series: [$series$],
    
};
    myChart.setOption(option_$id$);
</script>
"""

class LineTemplate():

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
            datazoom = r"dataZoom: [{ start: 0, end: 100 }],"

        assert min(y_lens) == len(xdata), f"x and y data should have the same length, but got {len(xdata)} and {min(y_lens)}"
        xdata_template = str(xdata)

        series_template = ""
        colorset = [*Color.C_3_M_Chinese_Style.items()]
        for ix, (name, array) in enumerate(ydata.items()):
            color0, color1 = colorset[ix % len(colorset)][1]

            series_item = \
            r"""
            { 
                name: '$name$', type: 'line', symbol: 'none', sampling: 'lttb', itemStyle: { color: 'rgb$color1$' },
                areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: 'rgb$color1$'}, { offset: 1, color: 'rgb$color0$'}])},
                data: $array$
            },
            """.replace('$name$', name)\
                .replace('$array$', str(array))\
                .replace('$color0$', str(color0))\
                .replace('$color1$', str(color1))
            series_template += series_item

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

