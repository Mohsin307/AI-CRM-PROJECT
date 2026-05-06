import { useState } from "react";
import axios from "axios";

export default function InteractionForm() {
  const [notes, setNotes] = useState("");
  const [result, setResult] = useState(null);

  const submit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/log-ai", {
      notes,
    });

    setResult(res.data.data);
  };

  return (
    <div>
      <h2>Log Interaction (AI)</h2>

      <textarea
        rows="5"
        style={{ width: "100%" }}
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        placeholder="Enter HCP interaction notes..."
      />

      <br />
      <button onClick={submit} style={{ marginTop: "10px" }}>
        Submit
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>AI Extracted Data</h3>

          <p><b>HCP:</b> {result.hcp_name}</p>
          <p><b>Summary:</b> {result.summary}</p>
          <p><b>Product:</b> {result.product}</p>
          <p><b>Sentiment:</b> {result.sentiment}</p>
          <p><b>Follow-up:</b> {result.follow_up}</p>
        </div>
      )}
    </div>
  );
}