from rssched.model.response import Response
from rssched.visualization.active_events import plot_active_events_over_time
from rssched.visualization.fleet_efficiency import plot_fleet_efficiency
from rssched.visualization.vehicle_type_gantt import plot_gantt_per_vehicle_type
from rssched.visualization.vehicle_utilization import plot_vehicle_utilization


def generate_plots(response: Response, instance_name: str):
    figures = plot_gantt_per_vehicle_type(response, instance_name)
    figures.append(plot_active_events_over_time(response, instance_name))
    figures.append(plot_vehicle_utilization(response, instance_name))
    figures.extend(plot_fleet_efficiency(response, instance_name))
    return figures
