import pandas as pd

from backend.modules.pmc_generator import generate_pmc_data


def test_pmc_generation():

    df = pd.DataFrame({
        "Task Code": ["TC001"],
        "Task Description": ["Payment Enhancement"],
        "Activity": ["Development"],
        "Reporting employee": ["Arun"],
        "Hours Booked": [8]
    })

    result = generate_pmc_data(df)

    assert result.iloc[0]["PMC ID"] == "PMC-001"
    assert result.iloc[0]["Enhancement ID"] == "TC001"
    assert result.iloc[0]["Description"] == "Payment Enhancement"
    assert result.iloc[0]["Process Area"] == "Development"
    assert result.iloc[0]["Resource"] == "Arun"
    assert result.iloc[0]["Effort"] == 8
    assert result.iloc[0]["Team"] == "FIN_TECH"