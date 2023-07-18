# Latest Echarts Version: 5.4 , July 2023
from .echarts_script import echarts54_js_template
from .css_script import css_template
from utils import RegularExpress as RE

_template = \
r"""
<!DOCTYPE html>
<html>
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


class TightHTMLTemplate():


    def __init__(self, title="title", background_color="lightgray", chart_height='300px'):
        self.org_template = _template
        self.wf_template = _template
        self.title = title
        self.chart_count = 0
        self.chart_options = []
        self.chart_height = chart_height

        assert background_color in _supported_background_color, f"Not supported background color, expect {_supported_background_color}"
        self.background_color = background_color

        self.init_template()

    def init_template(self):

        self.wf_template = self.org_template \
            .replace('$css_template$', css_template)\
            .replace('$title$', self.title)\
            .replace('$background_color$', self.background_color)\
            .replace('divHeight', self.chart_height)

    def append_chart(self, chart_option):
        self.chart_count += 1
        self.chart_options.append(chart_option.export())
        self.build()

    def new_row(self):
        self.chart_options.append("$NL$")
        self.build()

    def build(self):
        self.init_template()
        container_template = \
            r"""
            <div class="container" style="margin: 0 auto">
                $chart1$
                $chart2$
            </div>
            $container$
            """
        rowix = 0
        for chart_option in self.chart_options:
            if chart_option == "$NL$":
                if rowix == 0:
                    continue
                else:
                    self.wf_template = self.wf_template.replace('$container$', container_template)
                    rowix = 0
            else:
                chart_option = chart_option.replace('$divWidth$', '100%').replace('$divHeight$', self.chart_height)
                if rowix == 0:  # chart1
                    rowix = 1
                    container_template = \
                        r"""
                        <div class="container" style="margin: 0 auto;">
                            $chart1$
                            $chart2$
                        </div>
                        $container$
                        """
                    container_template = container_template.replace('$chart1$',
                                                                    '<div class="box-tight">\n' + chart_option + '\n</div>')

                else:
                    rowix = 0
                    container_template = container_template.replace('$chart2$',
                                                                    '<div class="box-tight">\n' + chart_option + '\n</div>')
                    self.wf_template = self.wf_template.replace('$container$', container_template)

        if rowix != 0:
            self.wf_template = self.wf_template.replace('$container$', container_template)


    def export(self, path="res.html"):
        keywords = ['$title$', '$background_color$', '$charts$', '$container$', '$chart1$', '$chart2$', '$chart3$', '$chart4$']
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)

    def export_notebook(self):
        self.wf_template = self.wf_template.replace('$echarts_js_template$', echarts54_js_template)
        keywords = ['$title$', '$background_color$', '$container$', '$container$', '$chart1$', '$chart2$', '$chart3$', '$chart4$']
        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')

        from IPython.display import display, HTML
        display(HTML(export_template))

    def extend(self, extend_html_template):
        extend_body = RE.Find(extend_html_template.wf_template, r"<!--ANCHOR_BODY_ON-->(.+)<!--ANCHOR_BODY_OFF-->")[0] \
            .replace('<!--ANCHOR_BODY_EXTEND-->', '')
        self.wf_template = self.wf_template.replace('$container$', '')
        self.wf_template = self.wf_template.replace('<!--ANCHOR_BODY_EXTEND-->', extend_body + '\n<!--ANCHOR_BODY_EXTEND-->')
        return self




if __name__ == "__main__":

    with open("echarts43.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
