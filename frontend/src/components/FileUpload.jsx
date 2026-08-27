
import React from "react";

function FileUpload({
    file,
    setFile
}) {

    const handleChange = (event) => {

        const selectedFile =
            event.target.files[0];

        if (selectedFile) {
            setFile(selectedFile);
        }
    };


    return (
        <div className="upload-box">

            <div className="upload-icon">
                📊
            </div>

            <h3>
                Upload Employee Report
            </h3>

            <p>
                Select an Excel file (.xlsx or .xls)
            </p>


            <label className="file-button">

                Choose Excel File

                <input
                    type="file"
                    accept=".xlsx,.xls"
                    onChange={handleChange}
                    hidden
                />

            </label>


            {file && (
                <div className="selected-file">

                    <span>
                        📄
                    </span>

                    <span>
                        {file.name}
                    </span>

                </div>
            )}

        </div>
    );
}


export default FileUpload;