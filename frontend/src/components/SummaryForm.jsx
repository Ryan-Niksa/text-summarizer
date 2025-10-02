import { useState } from "react";
import { createSummary } from "../api";

export default function SummaryForm({ onNewSummary }) {
  const [text, setText] = useState("");
  const [style, setStyle] = useState("concise");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    setLoading(true);
    try {
      const summary = await createSummary(text, style);
      onNewSummary(summary);
      setText("");
    } catch (err) {
      alert("Error: " + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste text here..."
        rows={6}
      />
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.75rem" }}>
        <label><strong>Style:</strong></label>
        <select value={style} onChange={(e) => setStyle(e.target.value)}>
          <option value="concise">Concise</option>
          <option value="detailed">Detailed</option>
          <option value="bullets">Bullets</option>
        </select>
      </div>
      <button type="submit" disabled={loading}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>
    </form>
  );
}
