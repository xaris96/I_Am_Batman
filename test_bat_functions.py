"""Test suite for Batman-related utility functions."""

import pytest
from bat_functions import (
    calculate_bat_power,
    signal_strength,
    get_bat_vehicle,
)

# --------------------------
# Exercise 1: Tests & Parametrization
# --------------------------

@pytest.mark.parametrize(
    "level, expected",
    [
        (0, 0),
        (2, 84),
        (-3, -126),
    ],
)
def test_calculate_bat_power(level, expected):
    """Tests calculate_bat_power with various levels."""
    assert calculate_bat_power(level) == expected

@pytest.mark.parametrize(
    "distance, expected",
    [
        (0, 100),
        (5, 50),
        (12, 0),
        (-5, 50),
    ],
)
def test_signal_strength(distance, expected):
    """Tests signal_strength with various distances."""
    assert signal_strength(distance) == expected

# --------------------------
# Exercise 2: Fixtures
# --------------------------

@pytest.fixture
def expected_vehicles():
    """Fixture providing expected vehicle specifications."""
    return {
        "Batmobile": {"speed": 200, "armor": 80},
        "Batwing": {"speed": 300, "armor": 60},
        "Batcycle": {"speed": 150, "armor": 50},
    }

def test_get_bat_vehicle_known(expected_vehicles): # pylint: disable=redefined-outer-name
    """Tests get_bat_vehicle with known vehicles."""
    for name, specs in expected_vehicles.items():
        assert get_bat_vehicle(name) == specs

def test_get_bat_vehicle_unknown():
    """Tests get_bat_vehicle with unknown vehicle."""
    with pytest.raises(ValueError):
        get_bat_vehicle("BatSubmarine")

# --------------------------
# Exercise 3: Mocking
# --------------------------

def test_fetch_joker_info_mocked(mocker):
    """Tests fetch_joker_info with mocking."""
    # Mocking the fetch_joker_info function
    mock_data = {'mischief_level': 0, 'location': 'captured'}
    mocker.patch("bat_functions.fetch_joker_info", return_value=mock_data)
    mocker.patch("bat_functions.time.sleep")
    # Import the module after patching to ensure the mock is used
    import bat_functions # pylint: disable=import-outside-toplevel
    result = bat_functions.fetch_joker_info()
    assert result == mock_data

def test_fetch_joker_info_real(mocker):
    """Tests actual fetch_joker_info code (covers time.sleep)."""
    # Mock ONLY the time.sleep function
    mock_sleep = mocker.patch("bat_functions.time.sleep")
    import bat_functions # pylint: disable=import-outside-toplevel
    result = bat_functions.fetch_joker_info()
    assert result == {'mischief_level': 100, 'location': 'unknown'}
    mock_sleep.assert_called_once_with(1)
