import numpy.typing as npt

import numpy as np
import matplotlib.axes as mplax
import matplotlib.pyplot as plt
from matplotlib.typing import ColourType



def remove_tick_labels(axes: npt.ArrayLike | mplax.Axes | None = None):
    """Remove tick labels from a Matplotlib axis.

    Args:
        axes (npt.ArrayLike | mplax.Axes): The axes, or a list of axes from which to remove ticks.

    Raises:
        ValueError: Errors if the types are wrong.
    """
    if axes is None:
        axes = plt.gca()
    axes = np.array(axes)
    for ax in axes.flatten():
        if not isinstance(ax, mplax.Axes):
            raise ValueError("All items in list must be matplotlib axes.")
        ax.yaxis.set_tick_params(labelleft=False)
        ax.xaxis.set_tick_params(labelbottom=False)

def setup_matplotlib(dpi: int = 300):
    """Setup Matplotlib with my preferred values.

    Args:
        dpi (int, optional): Set the default dpi for your figures. 300 may be too high for Jupyter, but is good for publication. Defaults to 300.
    """
    import matplotlib.pyplot as plt

    plt.rcParams["figure.dpi"] = dpi
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 8
    plt.rcParams["axes.linewidth"] = 1
    plt.rcParams["figure.figsize"] = (4, 3)
    plt.rcParams["legend.frameon"] = False
    plt.rcParams["lines.linewidth"] = 1
    plt.rcParams["savefig.bbox"] = None
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1
    plt.rcParams["xtick.minor.width"] = 1
    plt.rcParams["xtick.major.size"] = 3
    plt.rcParams["xtick.minor.size"] = 1.5
    plt.rcParams["xtick.minor.visible"] = True
    plt.rcParams["xtick.top"] = True
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["ytick.major.width"] = 1
    plt.rcParams["ytick.minor.width"] = 1
    plt.rcParams["ytick.major.size"] = 3
    plt.rcParams["ytick.minor.size"] = 1.5
    plt.rcParams["ytick.minor.visible"] = True
    plt.rcParams["ytick.right"] = True
    plt.rcParams["lines.markersize"] = np.sqrt(5)
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.titlesize"] = "medium"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["figure.labelsize"] = "medium"
    plt.rcParams["figure.labelweight"] = "bold"
    plt.rcParams["figure.titlesize"] = "medium"
    plt.rcParams["figure.titleweight"] = "bold"
    plt.rcParams["figure.constrained_layout.use"] = True
    plt.rcParams["mathtext.fontset"] = "stixsans"
    plt.rcParams["svg.fonttype"] = "none"


def add_scalebar(
    length: float,
    ax: mplax.Axes | None = None,
    color: ColourType | None = None,
    units: str = "m",
    plot_scale=None,
    hide_label=False,
    fontproperties=None,
):
    """Add a scalebar to the desired axes with a given length.

    Args:
        distance (float): The length of the desired scalebar.
        ax (mplax.Axes, optional): The matplotlib axes to which you want to add the scalebar. Defaults to plt.gca().
        color (ColourType, optional): The colour of the scalebar. Defaults to white.
        units (str, optional): The units of the measurement. Must be supported by the Python pint library. Defaults to m (metres).
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
    import pint

    if plot_scale is None:
        plot_scale = 1

    if ax is None:
        ax = plt.gca()
    if color is None:
        color = "w"

    ureg = pint.UnitRegistry()

    q = length * ureg(units)
    bar = AnchoredSizeBar(
        ax.transData,
        length * plot_scale,
        f"{q:.0f~#P}" if not hide_label else None,
        "lower right",
        frameon=False,
        color=color,  # type: ignore
        pad=0.1,
        borderpad=0.5,
        sep=5,
        fontproperties=fontproperties,
    )
    ax.add_artist(bar)
