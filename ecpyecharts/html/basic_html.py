# Latest Echarts Version: 5.4 , July 2023
from .echarts_script import echarts54_js_template
from .css_script import css_template
from utils import RegularExpress as RE

_template = \
r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>$title$</title>
    $echarts_js_template$
    $css_template$
    
</head>
<body>
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
            .replace('$title$', self.title) \
            .replace('$css_template$', css_template)\
            .replace('$background_color$', self.background_color)

    def append_chart(self, chart_option):
        self.chart_count += 1
        self.chart_options.append(chart_option.export())
        self.build()

    def build(self):
        self.init_template()
        self.wf_template = self.wf_template.replace('$divHeight$', self.chart_height).replace('$divWidth$', '90%')
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        for i, chart_option in enumerate(self.chart_options):
            container_template = \
                r"""
                <div class="container" style="margin: 0 auto; padding: 0;">
                    $chart$
                </div>
                $container$
                """
            chart_option = chart_option.replace('$divWidth$', '100%').replace('$divHeight$', self.chart_height)
            container_template = container_template.replace('$chart$', chart_option)
            self.wf_template = self.wf_template.replace('$container$', f"{container_template}\n$container$")


    def export(self, path="res.html"):
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        keywords = ['$title$', '$background_color$', '$container$', '$container$', '$chart1$', '$chart2$']
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)

    def extend(self, extend_html_template):
        extend_body = RE.Find(extend_html_template.wf_template, r"<!--ANCHOR_BODY_ON-->(.+)<!--ANCHOR_BODY_OFF-->")[0]\
            .replace('<!--ANCHOR_BODY_EXTEND-->', '')
        self.wf_template = self.wf_template.replace('$container$', '')
        self.wf_template = self.wf_template.replace('<!--ANCHOR_BODY_EXTEND-->', extend_body + '\n<!--ANCHOR_BODY_EXTEND-->')
        return self


if __name__ == "__main__":

    with open("echarts43.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
