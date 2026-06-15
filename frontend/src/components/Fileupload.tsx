import "../styles/FileUpload.css";
import { useState } from "react";
import { uploadFile } from "../services/api";
import SectionCard from "./SectionCard";
import ReactMarkdown from "react-markdown";
import MetricCard from "./MetricCard";
import AnomalyTable from "./AnomalyTable";
import DatasetProfile from "./DatasetProfile";
import ChatBox from "./Chatbox";
import type {
    AnalyticsResponse,
} from "../types/types";
import CorrelationHeatmap from "./CorrelationHeatmap";

function FileUpload() {
    const [file, setFile] = useState<File | null>(null);

    const [loading, setLoading] = useState<boolean>(false);

    const [response, setResponse] = useState<AnalyticsResponse | null>(null);

    const [query, setQuery] = useState<string>("");

    const [error, setError] = useState<string | null>(null);

    // Derived data
    const strongCorrelations =
        response?.analytics.correlations.filter(
            (correlation) => Math.abs(correlation.value) > 0.9,
        ) || [];

    const topAnomalies = response?.analytics.anomalies.slice(0, 5) || [];

    return (
        <div className="page-container">



            <h2>Upload CSV</h2>
            <div className="upload-card">
                <input
                    disabled={loading}
                    type="file"
                    onChange={(event) => {
                        const selectedFile = event.target.files?.[0];

                        setFile(selectedFile);
                    }}
                />

                <br />
                <br />

            </div>



            <br />
            <br />

            <button
                type="submit"
                className="submit-button"
                disabled={!file || loading}
                onClick={async () => {
                    if (!file) return;
                    setError(null);
                    setLoading(true);

                    try {
                        const data = await uploadFile(file, query);

                        console.log(data);

                        setResponse(data);
                    }
                    catch (error) {
                        console.error(error);

                        setError(
                            "Failed to analyze dataset. Please try again."
                        );

                    } finally {
                        setLoading(false);
                    }
                }}
            >
                {loading ? "Analyzing..." : "Analyze Dataset"}
            </button>

            {error && (
                <div className="error-message">
                    {error}
                </div>
            )}
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

                    <div className="metrics-row">
                        <MetricCard
                            label="Insights"
                            value={response.analytics.insights.length}
                        />
                        <MetricCard
                            label="Anomalies"
                            value={response.analytics.anomalies.length}
                        />

                        <MetricCard
                            label="Mode"
                            value={response.mode}
                        />
                    </div>
                    <SectionCard title="Dataset Profile">
                        <DatasetProfile schema={response.schema} />
                    </SectionCard>
                    <CorrelationHeatmap
                        matrix={response.analytics.correlation_matrix}
                    />

                    <div className="section-card">
                        <SectionCard title="AI Report">
                            <div className="markdown-report">
                                <ReactMarkdown >
                                    {response.report}
                                </ReactMarkdown>
                            </div>
                        </SectionCard>

                        <SectionCard title="Key Insights">
                            <ul>
                                {response.analytics.insights.length === 0 ? (<p>No insights found</p>) : (response.analytics.insights.map((insight, index) => (
                                    <li key={index}>{insight}</li>
                                )))}
                            </ul>
                        </SectionCard>

                        <SectionCard title="Strong Corellations">
                            <ul>
                                {strongCorrelations.length === 0 ? (
                                    <p>No strong correlations found.</p>
                                ) : (
                                    strongCorrelations.map((correlation, index) => (
                                        <li key={index}>
                                            {correlation.col1} ↔ {correlation.col2}:{" "}
                                            {correlation.value}
                                        </li>
                                    )))}
                            </ul>
                        </SectionCard>
                        {/*<div className="anomaly-table">*/}
                        <SectionCard title="Anomalies" >
                            {topAnomalies.length === 0 ? (<p>No Anomalies found</p>) : (
                                <AnomalyTable anomalies={topAnomalies} />)}

                        </SectionCard>
                        <SectionCard title="Chat with your Data">

                            <ChatBox />

                        </SectionCard>
                        {/*</div>*/}
                    </div>
                </div>
            )}
        </div>
    );
}

export default FileUpload;
