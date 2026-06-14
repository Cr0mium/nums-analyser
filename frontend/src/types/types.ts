export interface Anomaly {
    column: string;
    index: number;
    value: number;
    z_score: number;
    severity: string;
}
export interface CorrelationMatrix {
    [key: string]: {
        [key: string]: number;
    };
}
export interface Correlation {
    col1: string;
    col2: string;
    value: number;
    type: string;
    strength: string;
}

export interface TrendMetric {
    direction: string;
    pct_change: number;
}

export interface AnalyticsResponse {
    dataset: string;
    schema: Schema;
    mode: string;
    analytics: {
        insights: string[];
        correlations: Correlation[];
        correlation_matrix: CorrelationMatrix;
        anomalies: Anomaly[];
    };
    report: string;
    response: string;
    error: string;
}

export interface Schema {
    rows: number;
    columns: number;
    time_col: string | null;
    numeric_cols: string[];
    categorical_cols: string[];
    mode: string;
    dataset_name: string | null;
}
