"""Lap time statistics. All lap times are in seconds."""


def total_time(lap_times):
    """Return the sum of all lap times."""
    return sum(lap_times)


def best_lap(lap_times):
    """Return the fastest (smallest) lap time."""
    if not lap_times:
        raise ValueError("lap_times is empty")
    return min(lap_times)


def average_lap(lap_times):
    """Return the mean lap time."""
    if not lap_times:
        raise ValueError("lap_times is empty")
    return sum(lap_times) / len(lap_times)


def format_lap_time(seconds):
    """Format a duration in seconds as M:SS.ss

    Examples:
        format_lap_time(75.25)  -> "1:15.25"
        format_lap_time(125.5)  -> "2:05.50"
    """
    minutes = int(seconds // 60)
    rest = seconds - minutes * 60
    return f"{minutes}:{rest:.2f}"

def function(funcInput):
    """This is a placeholder function for future implementation."""
    print("example, function called with input:", funcInput)
    pass