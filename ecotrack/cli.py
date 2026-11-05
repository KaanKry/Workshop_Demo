"""Print a summary of the lap times stored in a CSV file.

Run it from the repository folder:

    python3 -m ecotrack data/sample_laps.csv
"""

import csv
import sys

from ecotrack import laps


def read_lap_times(path):
    """Read the `time_s` column of a CSV file into a list of numbers."""
    with open(path, newline="") as f:
        return [float(row["time_s"]) for row in csv.DictReader(f)]


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python3 -m ecotrack <laps.csv>")
        return 1

    lap_times = read_lap_times(args[0])

    print(f"Total time:   {laps.format_lap_time(laps.total_time(lap_times))}")
    print(f"Best lap:     {laps.format_lap_time(laps.best_lap(lap_times))}")
    print(f"Average lap:  {laps.format_lap_time(laps.average_lap(lap_times))}")
    return 0
