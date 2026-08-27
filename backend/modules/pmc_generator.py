from config.settings import (
    OUTPUT_COLUMN_MAPPING,
    OUTPUT_COLUMNS,
    TEAM_NAME
)


def generate_pmc_data(df):

    result = df.copy()

    # Rename columns
    result = result.rename(
        columns=OUTPUT_COLUMN_MAPPING
    )

    # PMC ID must remain empty
    result.insert(
        0,
        "PMC ID",
        [""] * len(result)
    )

    # Team
    result["Team"] = TEAM_NAME

    # Empty fields
    result["Start Date"] = ""
    result["End Date"] = ""
    result["Status"] = ""
    result["Remarks"] = ""
    result["Estimation"] = ""
    result["PSR ID"] = ""

    # Correct column order
    result = result[OUTPUT_COLUMNS]

    return result