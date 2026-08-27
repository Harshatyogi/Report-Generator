import io
import os
import uuid
import tempfile

import pandas as pd

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse


from modules.excel_reader import read_excel
from modules.validator import validate_data
from modules.processor import calculate_total_hours
from modules.pmc_generator import generate_pmc_data
from modules.excel_exporter import export_to_excel


app = FastAPI(
    title="PMC Report Generator API",
    version="1.0.0"
)


# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# =====================================================
# Temporary generated files
# =====================================================

generated_files = {}


# =====================================================
# Home
# =====================================================

@app.get("/")
def root():

    return {
        "message": "PMC Report Generator API is running"
    }


# =====================================================
# Generate PMC Report
# =====================================================

@app.post("/api/generate-pmc")
async def generate_pmc(
    file: UploadFile = File(...)
):

    # Validate extension
    if not file.filename.lower().endswith(
        (".xlsx", ".xls")
    ):

        raise HTTPException(
            status_code=400,
            detail="Please upload an Excel file."
        )

    try:

        # Read uploaded file
        contents = await file.read()

        file_stream = io.BytesIO(
            contents
        )

        # Read Excel
        df = read_excel(
            file_stream
        )

        # Validate
        valid, message = validate_data(df)

        if not valid:

            raise HTTPException(
                status_code=400,
                detail=message
            )

        # Calculate total hours
        processed_df = calculate_total_hours(
            df
        )

        # Generate PMC data
        pmc_df = generate_pmc_data(
            processed_df
        )

        # Create temporary Excel
        file_id = str(uuid.uuid4())

        output_path = os.path.join(
            tempfile.gettempdir(),
            f"PMC_Report_{file_id}.xlsx"
        )

        # Export
        export_to_excel(
            pmc_df,
            output_path
        )

        # Store file path
        generated_files[file_id] = output_path

        # Summary
        summary = {
            "pmc_records": int(
                len(pmc_df)
            ),

            "resources": int(
                pmc_df["Resource"]
                .nunique()
            ),

            "total_effort": float(
                pmc_df["Effort"]
                .sum()
            ),

            "unique_tasks": int(
                pmc_df["Enhancement ID"]
                .nunique()
            ),

            "activities": int(
                pmc_df["Process Area"]
                .nunique()
            )
        }

        # Convert DataFrame to JSON
        records = pmc_df.to_dict(
            orient="records"
        )

        return {
            "success": True,
            "message": (
                "PMC report generated successfully."
            ),
            "summary": summary,
            "data": records,
            "file_id": file_id
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# Download PMC Report
# =====================================================

@app.get("/api/download/{file_id}")
def download_report(file_id: str):

    file_path = generated_files.get(
        file_id
    )

    if not file_path:

        raise HTTPException(
            status_code=404,
            detail="Report not found."
        )

    if not os.path.exists(file_path):

        raise HTTPException(
            status_code=404,
            detail="Report file no longer exists."
        )

    return FileResponse(
        path=file_path,
        filename="PMC_Report.xlsx",
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )