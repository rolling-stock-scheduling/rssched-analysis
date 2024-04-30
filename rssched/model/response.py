from datetime import datetime
from typing import List

from pydantic import BaseModel


class Info(BaseModel):
    running_time: str
    number_of_threads: int
    timestamp_utc: datetime
    hostname: str


class ObjectiveValue(BaseModel):
    unserved_passengers: int
    maintenance_violation: int
    vehicle_count: int
    costs: int


class Load(BaseModel):
    vehicle_type: str
    spawn_count: int


class DepotLoad(BaseModel):
    depot: str
    load: List[Load]


class DepartureSegment(BaseModel):
    departure_segment: str
    origin: str
    destination: str
    departure: datetime
    arrival: datetime


class MaintenanceSlot(BaseModel):
    maintenance_slot: str
    location: str
    start: datetime
    end: datetime


class DeadHeadTrip(BaseModel):
    id: str
    origin: str
    destination: str
    departure: datetime
    arrival: datetime


class Vehicle(BaseModel):
    id: str
    start_depot: str
    end_depot: str
    departure_segments: List[DepartureSegment]
    maintenance_slots: List[MaintenanceSlot]
    dead_head_trips: List[DeadHeadTrip]


class Fleet(BaseModel):
    vehicle_type: str
    vehicles: List[Vehicle]
    vehicle_cycles: List[List[str]]


class Schedule(BaseModel):
    depot_loads: List[DepotLoad]
    fleet: List[Fleet]
    departure_segments: List[DepartureSegment]
    maintenance_slots: List[MaintenanceSlot]
    dead_head_trips: List[DeadHeadTrip]


class Response(BaseModel):
    info: Info
    objective_value: ObjectiveValue
    schedule: Schedule
