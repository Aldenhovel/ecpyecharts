css_template = \
r"""
<style>
.chartbox {
    margin: 10px auto;
    border-radius: 10px;
    background-color: white
}
.container {
    width: 90%;
    background-color: transparent;
    display: -webkit-box;
    justify-content: space-between;
}
body {
    margin: 0;
    padding: 0;
    background-color: $background_color$
}
.box {
    margin: 5px;
    flex: 0 0 calc(50% - 10px);
    display: flex;
    justify-content: center;
    align-items: center;
    height: $divHeight$;
    border-radius: 10px;
    background-color: white;
}
</style>
"""