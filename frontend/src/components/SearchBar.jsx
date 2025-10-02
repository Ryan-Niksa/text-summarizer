import { useState } from "react";

export default function SearchBar({ onSearch }) {
  const [q, setQ] = useState("");
  const [style, setStyle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ q, style: style || undefined });
  };

  const handleReset = () => {
    setQ("");
    setStyle("");
    onSearch({});
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", gap: "0.5rem", marginBottom: "1rem" }}>
      <input
        type="text"
        value={q}
        placeholder="Search keyword..."
        onChange={(e) => setQ(e.target.value)}
      />
      <select value={style} onChange={(e) => setStyle(e.target.value)}>
        <option value="">All Styles</option>
        <option value="concise">Concise</option>
        <option value="detailed">Detailed</option>
        <option value="bullets">Bullets</option>
      </select>
      <button type="submit">Search</button>
      <button type="button" className="secondary" onClick={handleReset}>
        Reset
      </button>
    </form>
  );
}
