from matplotlib.pyplot import plot


def add_bar_value(plot):
    for i in plot.containers:
        plot.bar_label(i)
    return plot
