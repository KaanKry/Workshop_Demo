import pytest

from ecotrack import laps

LAP_TIMES = [251.84, 245.30, 243.07]


def test_total_time():
    assert laps.total_time(LAP_TIMES) == pytest.approx(740.21)


def test_best_lap():
    assert laps.best_lap(LAP_TIMES) == 243.07


def test_average_lap():
    assert laps.average_lap(LAP_TIMES) == pytest.approx(246.7366, abs=1e-3)


def test_average_lap_rejects_empty_list():
    with pytest.raises(ValueError):
        laps.average_lap([])


def test_format_lap_time():
    assert laps.format_lap_time(75.25) == "1:15.25"
