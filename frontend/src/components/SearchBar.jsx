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
    <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
      <input
        type="text"
        value={q}
        placeholder="Search keyword..."
        onChange={(e) => setQ(e.target.value)}
        style={{ marginRight: "0.5rem" }}
      />
      <select value={style} onChange={(e) => setStyle(e.target.value)} style={{ marginRight: "0.5rem" }}>
        <option value="">All Styles</option>
        <option value="concise">Concise</option>
        <option value="detailed">Detailed</option>
        <option value="bullets">Bullets</option>
      </select>
      <button type="submit">Search</button>
      <button type="button" onClick={handleReset} style={{ marginLeft: "0.5rem" }}>
        Reset
      </button>
    </form>
  );
}
