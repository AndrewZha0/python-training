from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()

line.add_xaxis(["China", "Japan", "America"])
line.add_yaxis("GDP", [100, 80, 90])

line.set_global_opts(
    title_opts=TitleOpts(title="GDP SHOW", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()
