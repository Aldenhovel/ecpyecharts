import re
from typing import List


class RegularExpress():


    @staticmethod
    def Find(text: str, pattern: str) -> List[str]:
        return re.findall(pattern, text, re.DOTALL)



if __name__ == "__main__":
    txt = \
    r"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>hello</title>
    $echarts_js_template$
    <!--ANCHOR_CSS_ON-->
    <style>
    .chartbox {
        margin: 10px auto;
        border-radius: 10px;
        background-color: white
    }
    </style>
    <!--ANCHOR_CSS_OFF-->
    <!--ANCHOR_CSS_EXTEND-->
</head>
<body style="background-color: gray">
    <!--ANCHOR_BODY_ON-->
     
<div class="chartbox" id="chart_849540" style="width: $divWidth$; height: $divHeight$"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('chart_849540'));
    option_849540 = {
        grid: { left: '120', right: '15%', top: '90', bottom: '50'},
        title: {text: 'Chart B', subtext: 'this is the subtitle of B', left: 'left'},
        xAxis: { type: 'category', data: ['LiHua', 'XiaoMing', 'Ada', 'Happe', 'Aldenhovel', 'JOJO', 'MXY'], show: true, name: 'Name'},
        yAxis: { type: 'value', name: 'Age' },
        //toolbox: { show: true, feature: { magicType: { show: true, type: ['line', 'bar'] }, restore: { show: true }, saveAsImage: { show: true }}},
        tooltip: {trigger: 'axis', axisPointer: { type: 'cross', label: { backgroundColor: '#6a7985' } } },
        legend: {orient: 'vertical', left: 'left', top: '90'},
        
        series: [{name: 'Age', type: 'bar', data: [44, 53, 24, 65, 48, 41, 32], color: 'rgb(11, 50, 140)'},]
    };
    myChart.setOption(option_849540);
</script>

$charts$
    <!--ANCHOR_BODY_OFF-->
    <!--ANCHOR_BODY_EXTEND-->
</body> 
    """
    res = RegularExpress.Find(txt, r"<!--ANCHOR_CSS_ON-->(.+)<!--ANCHOR_CSS_OFF-->")
    print(res)