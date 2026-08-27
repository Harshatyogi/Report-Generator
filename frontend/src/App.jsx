
import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import SummaryCards from "./components/SummaryCards";
import ReportTable from "./components/ReportTable";
import DownloadButton from "./components/DownloadButton";

import { generatePMC } from "./services/api";

import "./App.css";


function App() {

    const [file, setFile] = useState(null);

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");


    const handleGenerate = async () => {

        if (!file) {

            setError(
                "Please select an Excel file first."
            );

            return;
        }

        setLoading(true);
        setError("");
        setResult(null);

        try {

            const response =
                await generatePMC(file);

            setResult(response);

        } catch (err) {

            setError(
                err.message
            );

        } finally {

            setLoading(false);
        }
    };


    return (

        <div className="app">

            {/* Header */}

            <header className="header">

                <div>

                    <h1>
                        PMC Report Generator
                    </h1>

                    <p>
                        Employee effort automation system
                    </p>

                </div>

            </header>


            <main className="container">

                {/* Upload Section */}

                <section className="panel">

                    <FileUpload
                        file={file}
                        setFile={setFile}
                    />


                    <button
                        className="generate-button"
                        onClick={handleGenerate}
                        disabled={loading}
                    >

                        {loading
                            ? "Processing Report..."
                            : "Generate PMC Report"
                        }

                    </button>


                    {error && (

                        <div className="error-message">

                            ❌ {error}

                        </div>

                    )}

                </section>


                {/* Results */}

                {result && (

                    <>

                        <section className="panel">

                            <div className="section-header">

                                <div>

                                    <h2>
                                        PMC Report Summary
                                    </h2>

                                    <p>
                                        Report processed successfully
                                    </p>

                                </div>

                                <span className="success-badge">
                                    ✓ Generated
                                </span>

                            </div>


                            <SummaryCards
                                summary={result.summary}
                            />

                        </section>


                        <section className="panel">

                            <div className="section-header">

                                <div>

                                    <h2>
                                        Generated PMC Report
                                    </h2>

                                    <p>
                                        {result.data.length} records generated
                                    </p>

                                </div>


                                <DownloadButton
                                    fileId={
                                        result.file_id
                                    }
                                />

                            </div>


                            <ReportTable
                                data={result.data}
                            />

                        </section>

                    </>

                )}

            </main>


            <footer>

                PMC Report Generator

            </footer>

        </div>
    );
}


export default App;