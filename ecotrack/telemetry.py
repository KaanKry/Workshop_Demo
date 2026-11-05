"""Simple physics helpers for telemetry data."""


def average_speed_kmh(distance_m, time_s):
    """Return the average speed in km/h.

    Example: average_speed_kmh(1000, 100) -> 36.0
    """
    if time_s <= 0:
        raise ValueError("time_s must be positive")
    return (distance_m / time_s) * 3.6


def efficiency_km_per_kwh(distance_km, energy_kwh):
    """Return how many kilometres the car travels per kWh of energy used.

    Example: efficiency_km_per_kwh(10, 2) -> 5.0
    """
    return distance_km / energy_kwh
