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
    "scatter": sns.scatterplot,
}

POST_PROCESS = {
    "bar": add_bar_value,
    "line": None,
    "box": None,
    "scatter": None,
}

"""
Set plot_type to "bar", "line", or "box" to pick the chart type.
Pass xticklabels/yticklabels to rename tick labels; if the data's
positions don't match range(len(labels)) (e.g. months numbered 1-12),
pass matching xticks/yticks too. Pass hue with palette to color-group 
by a column.
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
    palette=None,
    xticklabels=None,
    yticklabels=None,
    xticks=None,
    yticks=None,
    xscale="linear",
    yscale="linear",
    rotation=0,
    hue=None,
    legend=False,
):
    if plot_type not in PLOT_FUNCTIONS:
        raise ValueError(
            f"plot_type must be one of {list(PLOT_FUNCTIONS)}, received: {plot_type!r}"
        )

    # Avoid seaborn's "palette without hue" warning (v0.14+) by always
    # providing a hue when a palette is used:
    # - explicit hue -> use it as given
    kwargs = {"data": data, "x": x_col, "y": y_col, "ax": axes}
    if hue is not None:
        kwargs.update(palette=palette, hue=hue, legend=legend)

    plot_fn = PLOT_FUNCTIONS[plot_type]
    plot = plot_fn(**kwargs)
    plot.set_title(title)
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)
    plot.set_xscale(xscale)
    plot.set_yscale(yscale)

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
