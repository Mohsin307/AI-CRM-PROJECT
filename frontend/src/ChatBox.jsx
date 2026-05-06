import { useState } from "react";
import axios from "axios";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const send = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat", {
      input,
    });

    setResponse(res.data.response);
  };

  return (
    <div>
      <h2>Chat Assistant</h2>

      <input
        style={{ width: "100%" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={send} style={{ marginTop: "10px" }}>
        Send
      </button>

      {response && (
        <p style={{ marginTop: "10px" }}>
          🤖 {response}
        </p>
      )}
    </div>
  );
}