import pandas as pd
import plotly.express as px

from rssched.model.response import Response
from rssched.visualization.colors import COLORS


def plot_vehicle_utilization(response: Response, instance_name: str):
    utilization_data = []
    for fleet in response.schedule.fleet:
        for vehicle in fleet.vehicles:
            for segment in vehicle.departure_segments:
                duration = segment.arrival - segment.departure
                utilization_data.append(
                    {
                        "Vehicle": vehicle.id,
                        "Vehicle Type": fleet.vehicle_type,
                        "Duration": duration.total_seconds() / 3600,
                    }
                )

    df_utilization = pd.DataFrame(utilization_data)
    df_summed = df_utilization.groupby(["Vehicle", "Vehicle Type"]).sum().reset_index()
    df_summed_sorted = df_summed.sort_values(by="Duration", ascending=False)

    fig = px.bar(
        df_summed_sorted,
        x="Vehicle",
        y="Duration",
        color="Vehicle Type",
        title=f"Vehicle Utilization (instance: {instance_name})",
        color_discrete_sequence=COLORS,
        labels={"Duration": "Total Hours"},
    )
    fig.update_layout(
        xaxis_title="Vehicle ID",
        yaxis_title="Service Trip Time [h]",
        xaxis={"categoryorder": "total descending"},
    )
    fig.update_layout(hovermode="x", hoverdistance=50)

    return fig
