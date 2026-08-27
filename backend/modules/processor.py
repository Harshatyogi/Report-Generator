import pandas as pd

from config.settings import GROUP_COLUMNS


def clean_data(df):

    df = df.copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Convert Hours Booked to number
    df["Hours Booked"] = pd.to_numeric(
        df["Hours Booked"],
        errors="coerce"
    )

    # Remove invalid hours
    df = df.dropna(
        subset=["Hours Booked"]
    )

    # Clean grouping columns
    for column in GROUP_COLUMNS:

        df[column] = (
            df[column]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    return df


def calculate_total_hours(df):

    df = clean_data(df)

    result = (
        df.groupby(
            GROUP_COLUMNS,
            as_index=False,
            dropna=False
        )["Hours Booked"]
        .sum()
    )

    return result