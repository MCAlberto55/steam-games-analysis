"""
Generate Seaborn charts consistently in notebooks.
All visual customization logic lives here; the notebook just calls
to make_plot() with the specified parameters.
"""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def post_bar_plot(plot: Axes, **kwargs) -> None:
    for container in plot.containers:
        plot.bar_label(container)
    return plot


# ---------------------------------------------------------------------------
# Chart Type Settings
# ---------------------------------------------------------------------------
PLOT_FN = {
    "bar": sns.barplot,
    "line": sns.lineplot,
    "kde": sns.kdeplot,
    "box": sns.boxplot,
    "scatter": sns.scatterplot,
}

PLOT_DEFAULTS: dict[str, dict] = {
    "bar": {"fill": True},
    "line": {"marker": "o", "linewidth": 2},
    "kde": {"fill": True, "alpha": 0.4, "cut": 0},
    "box": {"linewidth": 1.5, "fliersize": 4, "notch": False},
    "scatter": {"s": 60, "alpha": 0.7, "marker": "o"},
}

POST_PROCESS = {
    "bar": post_bar_plot,
    "line": None,
    "box": None,
    "kde": None,
    "scatter": None,
}

VALID_PLOT_TYPES = list(PLOT_FN)

"""
Set plot_type to pick the chart type.
Pass xticklabels/yticklabels to rename tick labels; if the data's
positions don't match range(len(labels)) (e.g. months numbered 1-12),
pass matching xticks/yticks too. Pass hue with palette to color-group 
by a column.
"""


def make_plot(
    plot_type: str,
    x_col: str | pd.Series,
    y_col: str | pd.Series,
    title: str,
    xlabel: str = None,
    ylabel: str = None,
    data: pd.DataFrame = None,
    axes: Axes = None,
    palette: str = None,
    xticklabels: np.ndarray = None,
    yticklabels: np.ndarray = None,
    xticks: np.ndarray = None,
    yticks: np.ndarray = None,
    yticklabels_fontz: int = None,
    xticklabels_fontz: int = None,
    xscale: str = "linear",
    yscale: str = "linear",
    rotation: int = 0,
    hue: pd.Series | str = None,
    legend: bool = False,
    legend_label: str = None,
    color: str = None,
) -> None:
    if plot_type not in VALID_PLOT_TYPES:
        raise ValueError(
            f"plot_type must be one of {VALID_PLOT_TYPES}, received: {plot_type!r}"
        )

    # Kwargs base para la función seaborn
    plot_kwargs: dict = {
        "data": data,
        "x": x_col,
        "y": y_col,
        "ax": axes,
        **PLOT_DEFAULTS[plot_type],
    }

    # Seaborn ≥0.14 issues a "palette without hue" warning; We only add palette when there is hue.
    if hue is not None:
        plot_kwargs.update(hue=hue, palette=palette, legend=legend, label=legend_label)
    elif legend is not False:
        plot_kwargs.update(legend=legend, label=legend_label)
    if color is not None:
        plot_kwargs.update(color=color)

    plot = PLOT_FN[plot_type](**plot_kwargs)

    if legend is not False:
        plot.legend()

    # axes attributes
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
    plt.grid(True, alpha=0.3)

    # Call post process function
    post_fn = POST_PROCESS[plot_type]
    if post_fn is not None:
        post_fn(plot, color=color)


def multiple_lineplot(data: list, title: str, xlabel: str, ylabel: str):
    for obs in data:
        plt.plot(obs["index"], obs["value"], label=obs["label"])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()


def multiple_scatterplot(
    data: pd.DataFrame,
    title: str,
    x_col: str,
    y_col: str,
    n: int,
    m: int,
    hue_values: pd.DataFrame,
    xsize: int,
    ysize: int,
):
    fig, axes = plt.subplots(n, m, figsize=(xsize, ysize))
    fig.suptitle(title, fontsize=16)

    axes = np.array(axes).reshape(-1)
    total_cols = hue_values.shape[1]

    for idx, ax in enumerate(axes):
        if idx >= total_cols:
            ax.axis("off")
            continue
        sns.scatterplot(
            data=data,
            x=x_col,
            y=y_col,
            ax=ax,
            hue=hue_values.iloc[:, idx],
        )
    plt.show()
