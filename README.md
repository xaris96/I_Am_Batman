🦇🦇🦇

## 📖 Overview
This repository contains **pytest-based tests** for critical components of Batman's tech systems, including:
- Batmobile power calculations (`calculate_bat_power`)
- Bat-Signal strength analysis (`signal_strength`)
- Vehicle specifications (`get_bat_vehicle`)
- Joker's mischief monitoring (`fetch_joker_info`)

## 🛠️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/xaris96/I_Am_Batman
    cd I_Am_Batman
    pip install -r requirements.txt
## 🧪 Running Tests
    # Run all tests with verbose output
        pytest test_bat_functions.py -v
    # Generate coverage report (optional)
        pytest --cov=bat_functions --cov-report=html

## 🐛 Testing Strategy
    Parametrized Tests: Multiple input combinations for calculate_bat_power and signal_strength.

    Fixtures: Reusable setup for vehicle specifications.

    Mocking: Simulated API calls for fetch_joker_info.

    Real Execution Test: Verify actual API latency.

## 📜 License
    Educational use only. Gotham City Confidential.

🦇🦇🦇
