import { useState } from "react";
import { uploadFile } from "../services/api";
import SectionCard from "./SectionCard";

interface Anomaly {
    column: string;
    index: number;
    value: number;
    z_score: number;
    severity: string;
}

interface TrendMetric {
    direction: string;
    pct_change: number;
}

interface AnalyticsResponse {
    dataset: string;
    mode: string;
    report: string;
    analytics: {
        insights: string[];
        correlations: Correlation[];
        anomalies: Anomaly[];
    };
}

function FileUpload() {
    const [file, setFile] = useState<File | null>(null);

    const [loading, setLoading] = useState<boolean>(false);

    const [response, setResponse] = useState<AnalyticsResponse | null>(null);

    const [query, setQuery] = useState<string>("");

    // Derived data
    const strongCorrelations =
        response?.analytics.correlations.filter(
            (correlation) => Math.abs(correlation.value) > 0.9,
        ) || [];

    const topAnomalies = response?.analytics.anomalies.slice(0, 5) || [];

    return (
        <div>
            <h2>Upload CSV</h2>

            <input
                type="file"
                onChange={(event) => {
                    const selectedFile = event.target.files?.[0];

                    setFile(selectedFile);
                }}
            />

            <br />
            <br />

            <textarea
                placeholder="Ask a question about your dataset..."
                value={query}
                onChange={(event) => {
                    setQuery(event.target.value);
                }}
            />

            <br />
            <br />

            <button
                type="submit"
                disabled={!file || loading}
                onClick={async () => {
                    if (!file) return;

                    setLoading(true);

                    try {
                        const data = await uploadFile(file, query);

                        console.log(data);

                        setResponse(data);
                    } catch (error) {
                        console.error(error);
                    } finally {
                        setLoading(false);
                    }
                }}
            >
                {loading ? "Uploading..." : "Submit"}
            </button>

            {file && <p>Selected file: {file.name}</p>}

            {response && (
                <div>
                    <h2>Analysis Result</h2>

                    <p>
                        <strong>Dataset:</strong> {response.dataset}
                    </p>

                    <p>
                        <strong>Mode:</strong> {response.mode}
                    </p>
                    <SectionCard title="AI Report">
                        <pre>{response.report}</pre>
                    </SectionCard>

                    <SectionCard title="Key Insights">
                        <ul>
                            {response.analytics.insights.map((insight, index) => (
                                <li key={index}>{insight}</li>
                            ))}
                        </ul>
                    </SectionCard>

                    <SectionCard title="Strong Corellations">
                        <ul>
                            {strongCorrelations.map((correlation, index) => (
                                <li key={index}>
                                    {correlation.col1} ↔ {correlation.col2}:{" "}
                                    {correlation.value}
                                </li>
                            ))}
                        </ul>
                    </SectionCard>
                    <SectionCard title="Anomalies">
                        <ul>
                            {topAnomalies.map((anomaly, index) => (
                                <li key={index}>
                                    {anomaly.column} had unusual value {anomaly.value} (
                                    z-score: {anomaly.z_score})
                                </li>
                            ))}
                        </ul>
                    </SectionCard>
                </div>
            )}
        </div>
    );
}

export default FileUpload;
