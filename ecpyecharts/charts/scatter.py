import random
from typing import Dict, List, Any

_template = \
r"""
<div id="chart_$id$" style="width: 80%; height: 500px; border-radius: 10px; background-color: white; margin: 10px auto"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_$id$'));
    option_$id$ = {
        title: { text: '$title$', subtext: '$subtitle$', left: 'left'},
        xAxis: { name: '$xaxis$', show: true},
        yAxis: { name: '$yaxis$', show: true, scale: true, boundaryGap: ['10%', '10%'],},
        tooltip: { formatter: function (param) { var data = param.data; return 'Position: ' + data[0] + ', ' + data[1] + '<br>Value: ' +  data[2];
    }},
        legend: {orient: 'vertical', left: 'left', top: '12%' },
        grid: { left: '15%', right: '15%', top: '20%', bottom: '10%' },
        series: [$series$]
};
    myChart.setOption(option_$id$);
</script>
"""

class ScatterTemplate():

    def __init__(self, id='', title='', subtitle='', xaxis='X', yaxis='Y'):
        self.org_template = _template
        self.wf_template = _template
        self.id = id if id != '' else f"{random.randint(0, 1000000)}"
        self.title = title
        self.subtitle = subtitle
        self.xaxis = xaxis
        self.yaxis = yaxis

    def init_option(self, data_group_name: List[str], data_group: List[List[List]]):
        groups_count = len(data_group)
        assert len(data_group_name) == groups_count, "len of data_group_name should == len of data_group."

        vals = []
        for group in data_group:
            for point in group:
                vals.append(point[2])
        symbol_size_factor = max(vals)

        series_template = ""
        for i, group in enumerate(data_group):
            points = group
            this_series_template = \
            r"""
            {
            name: '$name$',
            data: $points$,
            type: 'scatter',
            symbolSize: function (data) { return (Math.sqrt(data[2]) - Math.sqrt($minval$)) / (Math.sqrt($maxval$) - Math.sqrt($minval$)) * 80 +20; },
            emphasis: { focus: 'self' },
            labelLayout: { y: 20, align: 'center', hideOverlap: true},
            labelLine: { show: true, length2: 5, lineStyle: { color: '#bbb' }},
            label: { show: true, formatter: function (param) { return param.data[3]; }, minMargin: 20, position: 'top'}
            },
            """.replace('$name$', data_group_name[i])\
                .replace('$points$', str(points))\
                .replace('$minval$', str(min(vals)))\
                .replace('$maxval$', str(max(vals)))
            series_template += this_series_template

        self.wf_template = self.wf_template.replace('$id$', self.id)\
            .replace('$title$', self.title)\
            .replace('$subtitle$', self.subtitle)\
            .replace('$xaxis$', self.xaxis)\
            .replace('$yaxis$', self.yaxis)\
            .replace('$series$', series_template)


    def export(self):
        keywords = []
        export_template = self.wf_template
        for kw in keywords:
            export_template.replace(kw, '')
        return export_template