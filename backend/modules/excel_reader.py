import pandas as pd


def read_excel(file):

    try:
        df = pd.read_excel(file)

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Remove spaces from column names
        df.columns = (
            df.columns
            .astype(str)
            .str.strip()
        )

        return df

    except Exception as e:
        raise ValueError(
            f"Unable to read Excel file: {str(e)}"
        )