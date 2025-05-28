import { useEffect, useState} from "react";
import axios from "axios";
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
} from "recharts";

type DataPoint = {
    timestamp: string;
    value: number;
}


export default function AssetCompare() {
  const [assetData, setAssetData] = useState<DataPoint[]>([]);
  const [benchmarkData, setBenchmarkData] = useState<DataPoint[]>([]);
  const [compare, setCompare] = useState<any>(null);

  useEffect(() => {
    axios.get("/api/v1/assets/history").then(res => setAssetData(res.data.records));
    axios.get("/api/v1/benchmark/market").then(res => setBenchmarkData(res.data.data));
    axios.get("/api/v1/assets/compare").then(res => setCompare(res.data));
  }, []);

  // 將兩筆資料合併對齊（根據 timestamp）
  const mergedData = assetData.map((d, i) => ({
    timestamp: d.timestamp.slice(0, 10), // 只顯示日期
    資產: d.value,
    大盤: benchmarkData[i]?.value || null,
  }));

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">資產 vs 大盤走勢圖</h1>

      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={mergedData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="資產" stroke="#8884d8" />
          <Line type="monotone" dataKey="大盤" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>

      {compare && (
        <div className="mt-6 bg-gray-100 p-4 rounded">
          <h2 className="text-lg font-semibold mb-2">報酬比較</h2>
          <p>使用者報酬率：{compare.user_return_pct}%</p>
          <p>大盤報酬率：{compare.benchmark_return_pct}%</p>
          <p>超額報酬率：{compare.excess_return_pct}%</p>
        </div>
      )}
    </div>
  );
}