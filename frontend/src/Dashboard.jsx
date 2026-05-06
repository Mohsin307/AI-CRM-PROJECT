import InteractionForm from "./InteractionForm";
import ChatBox from "./ChatBox";
import InteractionTable from "./InteractionTable";

export default function Dashboard() {
  return (
    <div style={{ padding: "20px", fontFamily: "Inter, sans-serif" }}>
      
      <h1>AI CRM HCP Dashboard</h1>

      {/* TOP SECTION: FORM + CHAT */}
      <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
        
        {/* LEFT: AI INTERACTION FORM */}
        <div style={{ flex: 1, border: "1px solid #ddd", padding: "10px" }}>
          <InteractionForm />
        </div>

        {/* RIGHT: CHAT ASSISTANT */}
        <div style={{ flex: 1, border: "1px solid #ddd", padding: "10px" }}>
          <ChatBox />
        </div>

      </div>

      {/* BOTTOM: INTERACTION HISTORY TABLE */}
      <div style={{ border: "1px solid #ddd", padding: "10px" }}>
        <InteractionTable />
      </div>

    </div>
  );
}