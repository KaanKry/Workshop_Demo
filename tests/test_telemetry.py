import pytest

from ecotrack.telemetry import average_speed_kmh, efficiency_km_per_kwh


def test_average_speed_kmh():
    assert average_speed_kmh(1000, 100) == pytest.approx(36.0)


def test_average_speed_rejects_zero_time():
    with pytest.raises(ValueError):
        average_speed_kmh(1000, 0)


def test_efficiency_km_per_kwh():
    assert efficiency_km_per_kwh(10, 2) == pytest.approx(5.0)
