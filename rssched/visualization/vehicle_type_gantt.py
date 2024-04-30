import plotly.figure_factory as ff

from rssched.model.response import Response
from rssched.visualization.colors import EVENT_TYPES


def plot_gantt_per_vehicle_type(response: Response, instance_name: str):
    figures = []

    for vehicle_type in response.schedule.fleet:
        vis_data = []
        for vehicle in vehicle_type.vehicles:
            for departure_segment in vehicle.departure_segments:
                vis_data.append(
                    {
                        "Task": vehicle.id,
                        "Start": departure_segment.departure,
                        "Finish": departure_segment.arrival,
                        "Type": "ServiceTrip",
                    }
                )
            for maintenance_slot in vehicle.maintenance_slots:
                vis_data.append(
                    {
                        "Task": vehicle.id,
                        "Start": maintenance_slot.start,
                        "Finish": maintenance_slot.end,
                        "Type": "MaintenanceSlot",
                    }
                )
            for dead_head_trip in vehicle.dead_head_trips:
                vis_data.append(
                    {
                        "Task": vehicle.id,
                        "Start": dead_head_trip.departure,
                        "Finish": dead_head_trip.arrival,
                        "Type": "DeadHeadTrip",
                    }
                )
        figures.append(
            ff.create_gantt(
                vis_data,
                title=f"Rolling stock schedule: {vehicle_type.vehicle_type} (instance: {instance_name})",
                colors=EVENT_TYPES,
                index_col="Type",
                show_colorbar=True,
                group_tasks=True,
                showgrid_x=True,
                height=1200,
            )
        )

    return figures
