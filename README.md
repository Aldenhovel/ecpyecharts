<h1 align="center">ecpyecharts: <br/>Easy, Python & Echarts</h1>
<h4 align="center">
    <p>
        <a href="https://github.com/Aldenhovel/ecpyecharts/blob/main/README_ZH.md">简体中文</a> |
        <b>English</b> 
    <p>
</h4>

## Introduction

Choosing [Apache Echarts](https://github.com/apache/echarts) for data visualization is a wise decision. However, since echarts is primarily a JavaScript library designed for frontend data visualization in web browsers, it may not be very convenient for backend developers who prioritize efficiency. As a result, a Python version of echarts called [pyecharts](https://github.com/pyecharts/pyecharts) has been developed to address this issue.

With pyecharts, you can directly generate echarts charts within Python scripts. It offers powerful functionality, allowing you to achieve almost all the features available in native echarts. Moreover, pyecharts provides extensive documentation and enjoys support from a vibrant community of developers.

**So why do we need ecpyecharts?**

We have discovered that data visualization is actually a discipline that combines both technology and art. The powerful and versatile tools like echarts and pyecharts provide a solid technical foundation, but when developers use these technologies to build their own visual reports, the results can be disappointing. This is because inappropriate visualization combinations may go against visual preferences.

Our development goal for ecpyecharts is to simplify the design burden for developers by subtracting from echarts and pyecharts, providing more concise, higher integration, and visually appealing customized visualization report templates.


![#1](examples/imgs/demo.gif)

- Supports generating HTML templates with different styles.
- Support a variety of well-designed chart templates.
- Wrote very simple code.
- Support for use in `jupyter notebook/lab`.
- Supports the use of GUI to build visual reports. *(in the future)*


## How to use ecpyecharts

1. Download or clone this repository.
    ```bash
    git clone git@github.com:Aldenhovel/ecpyecharts.git && cd ecpyecharts
    ```

2. Find the desired template in `examples/`.



3. Please refer to this code snippet, which briefly introduces the most direct way to use ecpyecharts.

    ```python
    import random
    from ecpyecharts.html import HTMLTemplate
    from ecpyecharts.charts import BarTemplate
    
    # create a html template
    html = HTMLTemplate(title="hello", background_color="gray")
    
    # create a bar chart template 
    # init it with data
    chart = BarTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
    chart.init_option(xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                   ydata={'BJ Score': [random.randint(0, 100) for _ in range(11)],
                          'SH Score': [random.randint(0, 100) for _ in range(11)],
                          'HK Score': [random.randint(0, 100) for _ in range(11)]
                          })
    
    # Once the chart is initialized, 
    # we can append it into the html template
    html.append_chart(chart)
    
    # export the html template to a file
    html.export('../tmp/bar_example.html')
    ```

4. Templates will be placed in `examples/`. If you want to view the running results, please view the corresponding HTML files in `tmp/`.

## notebook tutorials
We made some jupyter notebook tutorials to show interesting functions and related features of `ecpyecharts`, please check them under `notebooks/`.