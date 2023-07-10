import random
from typing import Dict, List, Any

_template = \
    r"""
<div id="chart_$id$" style="width: 80%; height: 500px; border-radius: 10px; background-color: white; margin: 10px auto"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_$id$'));
    option_$id$ = { 
        title: { text: '$title$', subtext: '$subtitle$', left: 'left'},
        tooltip: { trigger: 'item' },
        legend: { orient: 'vertical', left: 'left', top: '12%' },
        series: [$series$]
    };
    myChart.setOption(option_$id$);
</script>
"""

_RADIUS = [0, 60, 50, 37.5, 33]


class PieTemplate():

    def __init__(self, id='', title='', subtitle=''):
        self.org_template = _template
        self.wf_template = _template
        self.id = id if id != '' else f"{random.randint(0, 1000000)}"
        self.title = title
        self.subtitle = subtitle

    def init_option(self, data_group_name: List[str], data_group: List[Dict[str, Any]]):
        groups_count = len(data_group)
        assert groups_count <= 4, "The pie chart only support maximun 4 pie in 1 chart."
        assert len(data_group_name) == groups_count, "len of data_group_name should == len of data_group."

        series_template = ""
        for i, group in enumerate(data_group):
            center_position = [(i + 1) * 100 // (groups_count + 1), 50]
            data_template = ''
            for name, value in group.items():
                data_template = data_template + "{" + f"name: '{name}', value: '{value}'" + "},"
            this_series_template = \
            r"""
            { name: '$group_name$', type: 'pie', radius: '$radius$%', center: ['$center_h$%', '$center_v$%'], data: [$data$], emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)'}}},
            """.replace('$data$', data_template).replace('$group_name$', data_group_name[i])\
                .replace('$radius$', str(_RADIUS[groups_count]))\
                .replace('$center_h$', str(center_position[0]))\
                .replace('$center_v$', str(center_position[1]))

            series_template += this_series_template

        self.wf_template = self.wf_template.replace('$id$', self.id)\
            .replace('$title$', self.title)\
            .replace('$subtitle$', self.subtitle)\
            .replace('$series$', series_template)

    def export(self):
        keywords = []
        export_template = self.wf_template
        for kw in keywords:
            export_template.replace(kw, '')
        return export_template
