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
        self.fig = Figure(figsize=(7.5, 4.5))
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlabel('Year')

    def add_data(self, data):
        self.ax.set_title(data[1])
        self.ax.plot(AVAILABLE_YEARS.reverse(), data[2:])

    def get_fig(self):
        return self.fig_to_base64()

    def fig_to_base64(self):
        """Convert a matplotlib Figure into a base64 PNG string."""
        png_output = io.BytesIO()
        FigureCanvas(self.fig).print_png(png_output)
        return base64.b64encode(png_output.getvalue()).decode("utf-8")



    def to_number(self, value):
        """Convert a value to float for plotting."""
        if value is None:
            return 0.0
        if isinstance(value, (int, float)):
            return float(value)
        try:
            cleaned = str(value).replace(",", "")
            return float(cleaned)
        except (ValueError, TypeError):
            return 0.0

    def emissions_intensity_tons_per_mwh(self, data):
        """Compute CO2 intensity = tons CO2 per MWh generated."""
        co2_tons = self.to_number(data.get("co2Tons"))
        gen_kwh = self.to_number(data.get("generation"))
        gen_mwh = gen_kwh / 1000.0
        if gen_mwh <= 0:
            return 0.0
        return co2_tons / gen_mwh

    def price_plot_base64(self, state_data):
        """Bar chart: Average electricity price by sector (cents/kWh)."""
        categories = ["Residential", "Commercial", "Industrial", "Transportation", "Total"]
        values = [
            self.to_number(state_data.get("residentialPrice")),
            self.to_number(state_data.get("commercialPrice")),
            self.to_number(state_data.get("industrialPrice")),
            self.to_number(state_data.get("transportationPrice")),
            self.to_number(state_data.get("totalPrice")),
        ]

        fig = Figure(figsize=(7.5, 4.5))
        axis = fig.add_subplot(1, 1, 1)

        axis.bar(categories, values)
        axis.set_title("Average Electricity Price by Sector")
        axis.set_ylabel("cents / kWh")
        axis.set_ylim(bottom=0)
        axis.tick_params(axis="x", labelrotation=20)
        axis.grid(axis="y", linestyle="--", alpha=0.3)

        fig.tight_layout()
        return self.fig_to_base64(fig)

    def emissions_plot_base64(self, state_data, us_data):
        """Bar chart: CO2 intensity (tons/MWh) for State vs US average."""
        state_val = self.emissions_intensity_tons_per_mwh(state_data)
        us_val = self.emissions_intensity_tons_per_mwh(us_data)

        categories = ["State", "US avg"]
        values = [state_val, us_val]

        fig = Figure(figsize=(7.5, 4.5))
        axis = fig.add_subplot(1, 1, 1)

        axis.bar(categories, values)
        axis.set_title("CO₂ Emissions Intensity")
        axis.set_ylabel("tons CO₂ per MWh")
        axis.set_ylim(bottom=0)
        axis.grid(axis="y", linestyle="--", alpha=0.3)

        for i, v in enumerate(values):
            axis.text(i, v, f"{v:.3f}", ha="center", va="bottom")

        fig.tight_layout()
        return self.fig_to_base64(fig)
