"""
Produces base64-encoded PNG images for embedding in HTML templates.
"""

import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from ProductionCode.config import AVAILABLE_YEARS

class PlotBuilder:
    """Builds matplotlib figures and returns them as base64 PNG strings."""

    def __init__(self):
        """Construct PlotBuilder object"""
        self.fig = Figure(figsize=(7.5, 4.5))
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlabel('Year')

    def add_data(self, data):
        """
        Add a set of data to the plot
        param data: list:
            [0] state
            [1] graph title
            [2..] data
        """

        self.ax.set_title(data[1])
        reformated_years = [int(i) for i in AVAILABLE_YEARS]
        reformated_years.reverse()
        self.ax.plot(reformated_years, data[2:], label=data[0])
        self.ax.legend()

    def get_fig(self):
        '''
        Get the figure as a base 64 string
        return: base 64 figure string
        '''
        return self.fig_to_base64()

    def fig_to_base64(self):
        """
        Convert a matplotlib Figure into a base64 PNG string.
        return: base 64 figure string
        """
        png_output = io.BytesIO()
        FigureCanvas(self.fig).print_png(png_output)
        png_B64_String = "data:image/png;base64,"
        png_B64_String += base64.b64encode(png_output.getvalue()).decode("utf-8")
        return png_B64_String
