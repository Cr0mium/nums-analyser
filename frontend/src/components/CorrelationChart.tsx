import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

import type { Correlation } from "../types/types";
interface CorrelationChartProps {
    correlations: Correlation[];
}

function CorrelationChart({ correlations }: CorrelationChartProps) {
    const chartData = [...correlations]
        .sort(
            (a, b) => Math.abs(b.value) - Math.abs(a.value)
        )
        .slice(0, 10)
        .map((correlation) => ({
            name: `${correlation.col1} ↔ ${correlation.col2}`,
            value: correlation.value,
        }));
    return (
        <ResponsiveContainer width="100%" height={300}>
            <BarChart
                layout="vertical"
                data={chartData}
            >
                <XAxis type="number" />
                <YAxis
                    type="category"
                    dataKey="name"
                    width={200}
                />
                <Tooltip />
                <Bar dataKey="value" fill="#8884d8" />
            </BarChart>
        </ResponsiveContainer>
    );
}

export default CorrelationChart
