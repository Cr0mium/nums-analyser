import type { Schema } from "../types/types";
import "../styles/FileUpload.css";

interface DatasetProfileProps {
    schema: Schema;
}

function DatasetProfile({ schema }: DatasetProfileProps) {
    return (
        <div className="dataset-profile">
            <div className="profile-item">
                <span>Total Rows</span>
                <strong>{schema.rows}</strong>
            </div>

            <div className="profile-item">
                <span>Total Columns</span>
                <strong>{schema.columns}</strong>
            </div>

            <div className="profile-item">
                <span>Numeric</span>
                <strong>{schema.numeric_cols.length}</strong>
            </div>

            <div className="profile-item">
                <span>Date/Time</span>
                <strong>{schema.time_col ? 1 : 0}</strong>
            </div>

            <div className="profile-item">
                <span>Categorical</span>
                <strong>{schema.categorical_cols.length}</strong>
            </div>
        </div>
    );
}

export default DatasetProfile;
