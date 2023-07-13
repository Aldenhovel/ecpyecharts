# Latest Echarts Version: 5.4 , July 2023
from .echarts_script import echarts54_js_template

_template = \
r"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>$title$</title>
    $echarts_js_template$
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: $background_color$
        }

        .container {
            width: 90%;
            background-color: transparent;
            display: -webkit-box;
            justify-content: space-between;
        }

        .box {
            margin: 5px;
            flex: 0 0 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            height: $divHeight$;
            border-radius: 10px;
            background-color: white;
        }

    </style>
</head>
<body>
    <!--ANCHOR_ON-->
    $container$
    <!--ANCHOR_OFF-->
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

        self.wf_template = self.org_template\
            .replace('$title$', self.title)\
            .replace('$background_color$', self.background_color)\
            .replace('$echarts_js_template$', echarts54_js_template)\
            .replace('divHeight', self.chart_height)

    def append_chart(self, chart_option):
        self.chart_count += 1
        self.chart_options.append(chart_option.export())

    def export(self, path="res.html"):
        keywords = ['$title$', '$background_color$', '$container$', '$chart1$', '$chart2$']
        export_template = self.wf_template

        container_template = \
        r"""
        <div class="container" style="margin: 0 auto; padding: 0;">
            $chart1$
            $chart2$
        </div>
        $container$
        """
        for i, chart_option in enumerate(self.chart_options):
            chart_option = chart_option.replace('$divWidth$', '100%').replace('$divHeight$', self.chart_height).replace('$divWidth$', '100%')
            if i % 2 == 0: # chart1
                container_template = \
                    r"""
                    <div class="container" style="margin: 0 auto;">
                        $chart1$
                        $chart2$
                    </div>
                    $container$
                    """
                container_template = container_template.replace('$chart1$', '<div class="box">'+chart_option+'</div>')

            else:
                container_template = container_template.replace('$chart2$', '<div class="box">\n'+chart_option+'\n</div>')
                self.wf_template = self.wf_template.replace('$container$', container_template)

        if self.chart_count % 2 == 1:
            self.wf_template = self.wf_template.replace('$container$', container_template)

        export_template = self.wf_template
        for kw in keywords:
            export_template = export_template.replace(kw, '')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(export_template)




if __name__ == "__main__":

    with open("echarts43.js", 'r', encoding='utf-8') as f:
        echarts_js_template = f.read()
        print(echarts_js_template)
