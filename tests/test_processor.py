import pandas as pd

from backend.modules.processor import calculate_total_hours


def test_calculate_total_hours():

    data = {
        "Task Code": [
            "TC001",
            "TC001",
            "TC001",
            "TC002"
        ],

        "Task Description": [
            "Payment",
            "Payment",
            "Payment",
            "Login"
        ],

        "Activity": [
            "Development",
            "Development",
            "Testing",
            "Development"
        ],

        "Reporting employee": [
            "Arun",
            "Arun",
            "Arun",
            "Priya"
        ],

        "Hours Booked": [
            2,
            3,
            4,
            5
        ]
    }

    df = pd.DataFrame(data)

    result = calculate_total_hours(df)

    development = result[
        (result["Task Code"] == "TC001") &
        (result["Activity"] == "Development") &
        (result["Reporting employee"] == "Arun")
    ]

    assert development.iloc[0]["Hours Booked"] == 5