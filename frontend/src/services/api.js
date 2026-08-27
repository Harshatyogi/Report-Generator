const API_URL = "http://127.0.0.1:8000";


export async function generatePMC(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        `${API_URL}/api/generate-pmc`,
        {
            method: "POST",
            body: formData
        }
    );


    const data = await response.json();


    if (!response.ok) {

        throw new Error(
            data.detail ||
            "Failed to generate PMC report."
        );

    }


    return data;
}


export function getDownloadUrl(fileId) {

    return `${API_URL}/api/download/${fileId}`;

}