# Latest Echarts Version: 5.4 , July 2023
from .echarts_script import echarts54_js_template
from utils import RegularExpress as RE

_template = \
r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>$title$</title>
    $echarts_js_template$
    <!--ANCHOR_CSS_ON-->
    <style>
    .chartbox {
        margin: 10px auto;
        border-radius: 10px;
        background-color: white
    }
    </style>
    <!--ANCHOR_CSS_EXTEND-->
    <!--ANCHOR_CSS_OFF-->
    
</head>
<body style="background-color: $background_color$">
    <!--ANCHOR_BODY_ON-->
    $container$
    <!--ANCHOR_BODY_EXTEND-->
    <!--ANCHOR_BODY_OFF-->

</body>
</html>
"""

_supported_background_color = ['white', 'black', 'lightgray', 'gray']


class HTMLTemplate():


    def __init__(self, title="title", background_color="lightgray", chart_height='500px'):
        # 原始的 template
        self.org_template = _template
        # 正在工作中处理的 template
        self.wf_template = _template
        self.title = title
        self.chart_count = 0
        self.chart_options = []
        self.chart_height = chart_height

        assert background_color in _supported_background_color, f"Not supported background color, expect {_supported_background_color}"
        self.background_color = background_color

        self.init_template()

    def init_template(self):
        self.wf_template = self.org_template\
            .replace('$title$', self.title)\
            .replace('$background_color$', self.background_color)\

    def append_chart(self, chart_option):
        self.chart_count += 1
        self.chart_options.append(chart_option.export())
        self.build()

    def build(self):
        self.init_template()
        self.wf_template = self.wf_template.replace('$divHeight$', self.chart_height).replace('$divWidth$', '90%')
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        for i, chart_option in enumerate(self.chart_options):
            self.wf_template = self.wf_template.replace('$container$', f"{chart_option.export()}\n$container$")

    def export(self, path="res.html"):
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        keywords = ['$title$', '$background_color$', '$container$', '$container$', '$chart1$', '$chart2$']
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)

    def extend(self, extend_html_template):
        extend_css = RE.Find(extend_html_template.wf_template, r"<!--ANCHOR_CSS_ON-->(.+)<!--ANCHOR_CSS_OFF-->")[0]\
            .replace('<!--ANCHOR_CSS_EXTEND-->', '')
        extend_body = RE.Find(extend_html_template.wf_template, r"<!--ANCHOR_BODY_ON-->(.+)<!--ANCHOR_BODY_OFF-->")[0]\
            .replace('<!--ANCHOR_BODY_EXTEND-->', '')
        self.wf_template = self.wf_template.replace('$container$', '')

        self.wf_template = self.wf_template.replace('<!--ANCHOR_CSS_EXTEND-->', extend_css + '\n<!--ANCHOR_CSS_EXTEND-->')
        self.wf_template = self.wf_template.replace('<!--ANCHOR_BODY_EXTEND-->', extend_body + '\n<!--ANCHOR_BODY_EXTEND-->')
        return self

if __name__ == "__main__":

    with open("echarts43.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
