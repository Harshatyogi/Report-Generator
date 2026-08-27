import React from "react";
import { getDownloadUrl } from "../services/api";

function DownloadButton({ fileId }) {

    if (!fileId) {
        return null;
    }

    const handleDownload = () => {

        const url = getDownloadUrl(fileId);

        window.open(url, "_blank");
    };

    return (
        <button
            className="download-button"
            onClick={handleDownload}
        >
            📥 Download PMC Report
        </button>
    );
}

export default DownloadButton;
