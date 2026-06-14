import type { CorrelationMatrix } from "../types/types";
import { ResponsiveHeatMap } from "@nivo/heatmap";

interface CorrelationHeatmapProps {
    matrix: CorrelationMatrix;
}

function CorrelationHeatmap({ matrix }: CorrelationHeatmapProps) {

    const heatmapData = Object.entries(matrix).map(
        ([row, values]) => ({
            id: row,
            data: Object.entries(values).map(
                ([column, value]) => ({
                    x: column,
                    y: value,
                })
            ),
        })
    );
    console.log(heatmapData)
    return (
        <div style={{ height: "500px" }}>
            <ResponsiveHeatMap
                data={heatmapData}
                margin={{ top: 60, right: 90, bottom: 60, left: 90 }}
                valueFormat=".2f"
                colors={{
                    type: "diverging",
                    scheme: "red_yellow_blue",
                    divergeAt: 0.5,
                    minValue: -1,
                    maxValue: 1,
                }}
                axisTop={{
                    tickRotation: -45,
                }}
                axisLeft={{
                    tickSize: 5,
                }}
                emptyColor="#555555"
                borderWidth={1}
                borderColor="#ffffff"
                enableLabels={true}
                labelTextColor="#000000"
            />
        </div>
    );
}

export default CorrelationHeatmap;
