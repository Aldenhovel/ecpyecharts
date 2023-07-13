# Latest Echarts Version: 5.4 , July 2023
from .echarts_script import echarts54_js_template

_template = \
r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>$title$</title>
    $echarts_js_template$
    <style>
    .chartbox {
        margin: 10px auto;
        border-radius: 10px;
        background-color: white
    }
    </style>
</head>
<body style="background-color: $background_color$">
    <!--ANCHOR_ON-->
    $charts$
    <!--ANCHOR_OFF-->
</body>
</html>
"""

_supported_background_color = ['white', 'black', 'lightgray', 'gray']


class HTMLTemplate():
    """
    加载静态模板 _template 为 self.org_template
    使用 init_template 生成一个工作流模板 self.template, add_charts 等都在上面做
    做完之后用 export 清除掉 template 的锚点并输出

    """

    def __init__(self, title="title", background_color="lightgray", chart_height='500px'):
        # 原始的 template
        self.org_template = _template
        # 正在工作中处理的 template
        self.wf_template = _template
        self.title = title
        self.chart_height = chart_height

        assert background_color in _supported_background_color, f"Not supported background color, expect {_supported_background_color}"
        self.background_color = background_color

        self.init_template()

    def init_template(self):


        self.wf_template = self.org_template\
            .replace('$title$', self.title)\
            .replace('$background_color$', self.background_color)\
            .replace('$echarts_js_template$', echarts54_js_template)

    def append_chart(self, chart_option):
        print(chart_option.export())
        self.wf_template = self.wf_template.replace('$charts$', f"{chart_option.export()}\n$charts$")

    def export(self, path="res.html"):
        keywords = ['$title$', '$background_color$', '$charts$']
        self.wf_template = self.wf_template.replace('$divHeight$', self.chart_height).replace('$divWidth$', '80%')
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)




if __name__ == "__main__":

    with open("echarts43.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
