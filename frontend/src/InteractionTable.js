import { useEffect, useState } from "react";
import axios from "axios";

export default function InteractionTable() {
  const [data, setData] = useState([]);

  const loadData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/interactions");
      setData(res.data);
    } catch (err) {
      console.log("Error fetching interactions:", err);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>📊 Interaction History</h2>

      <button onClick={loadData} style={{ marginBottom: "10px" }}>
        Refresh
      </button>

      <table border="1" width="100%" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>HCP Name</th>
            <th>Summary</th>
            <th>Product</th>
            <th>Sentiment</th>
            <th>Follow Up</th>
          </tr>
        </thead>

        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.hcp_name}</td>
              <td>{item.summary}</td>
              <td>{item.product}</td>
              <td>{item.sentiment}</td>
              <td>{item.follow_up}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}