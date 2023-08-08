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
.box-single {
    margin: 5px;
    flex: 0 0 calc(100% - 10px);
    display: flex;
    justify-content: center;
    align-items: center;
    height: $divHeight$;
    border-radius: 10px;
    background-color: white;
}
.row-title {
    flex: 0 0 100%;
    padding-left: 10px;
    display: flex;
    justify-content: left;
    align-items: left;
    background-color: transparent;
    color: $txt_color$;
}
.box-tight {
    margin: 5px;
    flex: 0 0 calc(50% - 10px);
    display: flex;
    justify-content: center;
    align-items: center;
    height: $divHeight$;
    border-radius: 10px;
    background-color: white;
}
.box-verytight {
    margin: 5px;
    flex: 0 0 calc(33.34% - 10px);
    display: flex;
    justify-content: center;
    align-items: center;
    height: $divHeight$;
    border-radius: 10px;
    background-color: white;
}
.box-supertight {
    margin: 5px;
    flex: 0 0 calc(25% - 10px);
    display: flex;
    justify-content: center;
    align-items: center;
    height: $divHeight$;
    border-radius: 10px;
    background-color: white;
}
</style>
"""