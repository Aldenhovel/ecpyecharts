from .echarts_script import echarts_js_template
_template = \
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>$title$</title>
    $echarts_js_template$
</head>
<body style="background-color: $background_color$">

    $options$
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

    def __init__(self, title="title", background_color="lightgray"):
        # 原始的 template
        self.org_template = _template
        # 正在工作中处理的 template
        self.wf_template = _template
        self.title = title

        assert background_color in _supported_background_color, f"Not supported background color, expect {_supported_background_color}"
        self.background_color = background_color

        self.init_template()

    def init_template(self):


        self.wf_template = self.org_template\
            .replace('$title$', self.title)\
            .replace('$background_color$', self.background_color)\
            .replace('$echarts_js_template$', echarts_js_template)

    def add_chart(self, chart_option):
        print(chart_option.export())
        self.wf_template = self.wf_template.replace('$options$', f"{chart_option.export()}\n$options$")

    def export(self, path="res.html"):
        keywords = ['$title$', '$background_color$', '$options$']
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)




if __name__ == "__main__":

    with open("echarts.min.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
