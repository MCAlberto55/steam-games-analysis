from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def add_bar_value(plot):
    for i in plot.containers:
        plot.bar_label(i)
    return plot


PLOT_FUNCTIONS = {
    "bar": sns.barplot,
    "line": sns.lineplot,
    "box": sns.boxplot,
}

POST_PROCESS = {
    "bar": add_bar_value,
    "line": None,
    "box": None,
}

"""
Set plot_type to "bar", "line", or "box" to pick the chart type.
Use vertical=False to flip x_col/y_col (e.g. horizontal bar plots).
Pass xticklabels/yticklabels to rename tick labels; if the data's
positions don't match range(len(labels)) (e.g. months numbered 1-12),
pass matching xticks/yticks too. Pass hue to color-group by a column
other than x_col (e.g. a line plot split by year).
"""


def make_plot(
    plot_type,
    x_col,
    y_col,
    title,
    xlabel=None,
    ylabel=None,
    data=None,
    axes=None,
    palette="Dark2",
    vertical=True,
    xticklabels=None,
    yticklabels=None,
    xticks=None,
    yticks=None,
    rotation=0,
    hue=None,
    legend=False,
):
    if plot_type not in PLOT_FUNCTIONS:
        raise ValueError(
            f"plot_type must be one of {list(PLOT_FUNCTIONS)}, received: {plot_type!r}"
        )

    x, y = (x_col, y_col) if vertical else (y_col, x_col)

    # Avoid seaborn's "palette without hue" warning (v0.14+) by always
    # providing a hue when a palette is used:
    # - explicit hue -> use it as given
    # - no hue, but x exists -> use x as hue (per-category colors, no legend)
    # - no hue and no x (single series, e.g. one-variable boxplot) -> use a
    #   single fixed color from the palette instead
    kwargs = {"data": data, "x": x, "y": y, "ax": axes}
    if hue is not None:
        kwargs.update(palette=palette, hue=hue, legend=legend)
    elif x is not None:
        kwargs.update(palette=palette, hue=x, legend=False)
    else:
        kwargs.update(color=sns.color_palette(palette)[0])

    plot_fn = PLOT_FUNCTIONS[plot_type]
    plot = plot_fn(**kwargs)

    plot.set_title(title)
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)

    if xticklabels is not None:
        ticks = xticks if xticks is not None else range(len(xticklabels))
        plot.set_xticks(ticks)
        plot.set_xticklabels(xticklabels, rotation=rotation)

    if yticklabels is not None:
        ticks = yticks if yticks is not None else range(len(yticklabels))
        plot.set_yticks(ticks)
        plot.set_yticklabels(yticklabels, rotation=rotation)

    plt.tight_layout()
    post_fn = POST_PROCESS.get(plot_type)
    if post_fn is not None:
        post_fn(plot)
