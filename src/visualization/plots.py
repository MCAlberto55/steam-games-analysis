from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import partial


def add_bar_value(plot, **kwargs):
    for i in plot.containers:
        plot.bar_label(i)
    return plot


def color_kde_plot(plot, color):
    if plot.collections:
        for collection in plot.collections:
            collection.set_facecolor(color)
            collection.set_edgecolor(color)
            collection.set_alpha(0.5)


PLOT_CONFIGS = {
    "bar": {"fun": sns.barplot, "fill": True},
    "line": {"fun": sns.lineplot, "marker": "o", "linewidth": 2},
    "kdeplot": {
        "fun": sns.kdeplot,
        "fill": True,
        "alpha": 0.4,
    },
    "box": {
        "fun": sns.boxplot,
        "linewidth": 1.5,
        "fliersize": 4,
        "notch": False,
    },
    "scatter": {
        "fun": sns.scatterplot,
        "s": 60,
        "alpha": 0.7,
        "marker": "o",
    },
}

POST_PROCESS = {
    "bar": add_bar_value,
    "line": None,
    "box": None,
    "kdeplot": color_kde_plot,
    "scatter": None,
}

"""
Set plot_type to pick the chart type.
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
    yticklabels_fontz=None,
    xticklabels_fontz=None,
    xscale="linear",
    yscale="linear",
    rotation=0,
    hue=None,
    legend=False,
    color=None,
):
    if plot_type not in PLOT_CONFIGS:
        raise ValueError(
            f"plot_type must be one of {list(PLOT_CONFIGS)}, received: {plot_type!r}"
        )

    plot_conf = PLOT_CONFIGS[plot_type].copy()
    plot_fn = plot_conf["fun"]
    plot_conf.pop("fun")

    # Use partial to inject variables for post process functions.
    ultimate_color = color
    post_fn_base = POST_PROCESS[plot_type]
    post_fn = partial(post_fn_base, color=ultimate_color) if post_fn_base else None

    kwargs = {
        "data": data,
        "x": x_col,
        "y": y_col,
        "ax": axes,
    }

    # Avoid seaborn's "palette without hue" warning (v0.14+) by always
    # providing a hue when a palette is used:
    # - explicit hue -> use it as given
    if hue is not None:
        kwargs.update(palette=palette, hue=hue, legend=legend)

    kwargs.update(plot_conf)
    plot = plot_fn(**kwargs)
    plot.set_title(title)
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)
    plot.set_xscale(xscale)
    plot.set_yscale(yscale)

    if xticklabels is not None:
        ticks = xticks if xticks is not None else range(len(xticklabels))
        plot.set_xticks(ticks)
        plot.set_xticklabels(xticklabels, rotation=rotation, fontsize=xticklabels_fontz)

    if yticklabels is not None:
        ticks = yticks if yticks is not None else range(len(yticklabels))
        plot.set_yticks(ticks)
        plot.set_yticklabels(yticklabels, rotation=rotation, fontsize=yticklabels_fontz)

    plt.tight_layout()
    if post_fn is not None:
        post_fn(plot)


def multiple_lineplot(data: list, title: str, xlabel: str, ylabel: str):
    for obs in data:
        plt.plot(obs["index"], obs["value"], label=obs["label"])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
