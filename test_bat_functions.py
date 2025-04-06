import pytest
from bat_functions import (
    calculate_bat_power,
    signal_strength,
    get_bat_vehicle,
    fetch_joker_info,
)
import bat_functions


# --------------------------
# Exercise 1: Basic Testing and Parameterization
# --------------------------

# Task 1: Test calculate_bat_power with parameterization
@pytest.mark.parametrize(
    "level, expected",
    [
        (0, 0),       # Level 0 → 0 * 42 = 0
        (2, 84),      # 2 * 42 = 84
        (-3, -126),   # Negative level → -3 * 42 = -126
        (10, 420),    # 10 * 42 = 420
        (100, 4200),  # 100 * 42 = 4200
    ],
)
def test_calculate_bat_power(level, expected):
    assert calculate_bat_power(level) == expected

# Task 2: Test signal_strength with parameterization
@pytest.mark.parametrize(
    "distance, expected",
    [
        (0, 100),     # 100 - (0*10) = 100
        (5, 50),      # 100 - (5*10) = 50
        (12, 0),      # 100 - (12*10) = -20 → max(0, -20) = 0
        (-5, 150),    # 100 - (-5*10) = 150
    ],
)
def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected


# --------------------------
# Exercise 2: Fixtures
# --------------------------

# Fixture with known vehicles
@pytest.fixture
def expected_vehicles():
    return {
        "Batmobile": {"speed": 200, "armor": 80},
        "Batwing": {"speed": 300, "armor": 60},
        "Batcycle": {"speed": 150, "armor": 50},
    }

# Test for known vehicles using the fixture
def test_get_bat_vehicle_known(expected_vehicles):
    for name, specs in expected_vehicles.items():
        assert get_bat_vehicle(name) == specs

# Test for unknown vehicle
def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError):
        get_bat_vehicle("BatSubmarine")


# --------------------------
# Exercise 3: Mocking
# --------------------------

# Mock the fetch_joker_info function
def test_fetch_joker_info_mocked(mocker):
    mock_data = {"mischief_level": 0, "location": "captured"}
    mocker.patch("bat_functions.fetch_joker_info", return_value=mock_data)
    result = bat_functions.fetch_joker_info()  # Κλήση μέσω του module
    assert result == mock_data
