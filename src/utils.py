import base64
import io

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.use('agg')

plt.style.use("bmh")


def log_base_n(x, base=np.e):
    return np.log(x) / np.log(base)


def plot_log(base=np.e, xmin=0.001, xmax=10.001):

    fig, ax = plt.subplots(figsize=(5, 3))
    plt.style.use("bmh")
    n = round((xmax - xmin) * 10)
    x = np.linspace(xmin, xmax, n)
    plt.plot(x, log_base_n(x, base), label=f"log_{round(base, ndigits=2)}(x)")
    plt.legend()
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    url = base64.b64encode(img.getvalue()).decode()
    fig.clear()
    return f"data:image/png;base64,{url}"
