import pandas as pd

from backend.modules.validator import validate_data


def test_valid_data():

    df = pd.DataFrame({
        "Emp Name": ["Arun"],
        "Booking Date": ["2026-08-26"],
        "Booking ID": ["B001"],
        "Hours Booked": [5],
        "Activity": ["Development"],
        "Task Code": ["TC001"],
        "Task Description": ["Payment"],
        "Analysis Code": ["A001"],
        "Work Item": ["Development"],
        "Booking Remarks": [""],
        "Authorisation Remarks": [""],
        "Billable": ["Yes"],
        "Site Details": [""],
        "Status": ["Approved"],
        "Reporting employee": ["Arun"]
    })

    valid, message = validate_data(df)

    assert valid is True
    assert message == ""


def test_missing_column():

    df = pd.DataFrame({
        "Task Code": ["TC001"]
    })

    valid, message = validate_data(df)

    assert valid is False