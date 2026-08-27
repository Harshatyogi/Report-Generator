import React from "react";
function ReportTable({
    data
}) {

    if (!data || data.length === 0) {

        return (
            <p className="empty-message">
                No records found.
            </p>
        );
    }


    return (

        <div className="table-wrapper">

            <table>

                <thead>

                    <tr>

                        <th>PMC ID</th>

                        <th>
                            Enhancement ID
                        </th>

                        <th>
                            Description
                        </th>

                        <th>
                            Process Area
                        </th>

                        <th>
                            Resource
                        </th>

                        <th>
                            Effort
                        </th>

                        <th>
                            Team
                        </th>

                        <th>
                            Start Date
                        </th>

                        <th>
                            End Date
                        </th>

                        <th>
                            Status
                        </th>

                        <th>
                            Remarks
                        </th>

                        <th>
                            Estimation
                        </th>

                        <th>
                            PSR ID
                        </th>

                    </tr>

                </thead>


                <tbody>

                    {data.map(
                        (row, index) => (

                            <tr key={index}>

                                <td>
                                    {row["PMC ID"]}
                                </td>

                                <td>
                                    {row["Enhancement ID"]}
                                </td>

                                <td>
                                    {row["Description"]}
                                </td>

                                <td>
                                    {row["Process Area"]}
                                </td>

                                <td>
                                    {row["Resource"]}
                                </td>

                                <td className="effort">
                                    {row["Effort"]}
                                </td>

                                <td>
                                    {row["Team"]}
                                </td>

                                <td>
                                    {row["Start Date"]}
                                </td>

                                <td>
                                    {row["End Date"]}
                                </td>

                                <td>
                                    {row["Status"]}
                                </td>

                                <td>
                                    {row["Remarks"]}
                                </td>

                                <td>
                                    {row["Estimation"]}
                                </td>

                                <td>
                                    {row["PSR ID"]}
                                </td>

                            </tr>

                        )
                    )}

                </tbody>

            </table>

        </div>
    );
}


export default ReportTable;