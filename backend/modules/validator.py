import pandas as pd

from config.settings import INPUT_COLUMNS


def validate_columns(df):

    missing_columns = [
        column
        for column in INPUT_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return False, (
            "Missing columns: "
            + ", ".join(missing_columns)
        )

    return True, ""


def validate_hours(df):

    if "Hours Booked" not in df.columns:
        return False, "Hours Booked column is missing."

    hours = pd.to_numeric(
        df["Hours Booked"],
        errors="coerce"
    )

    invalid_values = hours.isna()

    if invalid_values.any():
        return False, (
            "Hours Booked contains invalid or empty values."
        )

    if (hours < 0).any():
        return False, (
            "Hours Booked cannot contain negative values."
        )

    return True, ""


def validate_data(df):

    valid, message = validate_columns(df)

    if not valid:
        return False, message

    valid, message = validate_hours(df)

    if not valid:
        return False, message

    return True, ""