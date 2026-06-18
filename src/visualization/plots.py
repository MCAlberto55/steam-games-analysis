import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def simple_bar_plot(data, x_col, y_col, title, xlabel, ylabel, vertical=True):
    plt.figure(figsize=(10, 6))
    plot = None
    if vertical:
        plot = sns.barplot(x=x_col, y=y_col, data=data)
    else:
        plot = sns.barplot(x=y_col, y=x_col, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    add_bar_value(plot)
    plt.show()


def add_bar_value(plot):
    for i in plot.containers:
        plot.bar_label(i)
    return plot
