from matplotlib.figure import Figure

from src.utils.config import (
    FSTMODEL_OUTPUT_PLOTS_PATH,
    SNDMODEL_OUTPUT_PLOTS_PATH,
)


# Plots
def export_3Dscatter_PCA(fig: Figure):
    fig.write_html(FSTMODEL_OUTPUT_PLOTS_PATH)


def export_3Dscatter_FAMD(fig: Figure):
    fig.write_html(SNDMODEL_OUTPUT_PLOTS_PATH)
