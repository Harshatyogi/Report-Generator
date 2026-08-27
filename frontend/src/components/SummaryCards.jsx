import React from "react";

function SummaryCards({ summary }) {

    if (!summary) {
        return null;
    }

    return (
        <div className="summary-grid">

            <div className="summary-card">
                <span>PMC Records</span>
                <strong>
                    {summary.pmc_records}
                </strong>
            </div>

            <div className="summary-card">
                <span>Resources</span>
                <strong>
                    {summary.resources}
                </strong>
            </div>

            <div className="summary-card">
                <span>Total Effort</span>
                <strong>
                    {summary.total_effort}
                </strong>
            </div>

            <div className="summary-card">
                <span>Unique Tasks</span>
                <strong>
                    {summary.unique_tasks}
                </strong>
            </div>

            <div className="summary-card">
                <span>Activities</span>
                <strong>
                    {summary.activities}
                </strong>
            </div>

        </div>
    );
}

export default SummaryCards;