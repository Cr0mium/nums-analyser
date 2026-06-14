import type { Anomaly } from "../types/types";

interface AnomalyTableProps {
    anomalies: Anomaly[];
}

function AnomalyTable({ anomalies }: AnomalyTableProps) {
    return (
        <table className="anomaly-table">
            <thead>
                <tr>
                    <th>Column</th>
                    <th>Value</th>
                    <th>Z-Score</th>
                    <th>Severity</th>
                </tr>
            </thead>

            <tbody>
                {anomalies.map((anomaly, index) => (
                    <tr key={index}>
                        <td>{anomaly.column}</td>
                        <td>{anomaly.value}</td>
                        <td>{anomaly.z_score.toFixed(2)}</td>
                        <td>{anomaly.severity}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default AnomalyTable;
