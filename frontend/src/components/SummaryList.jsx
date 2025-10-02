export default function SummaryList({ summaries }) {
    if (!summaries.length) {
      return <p>No summaries yet.</p>;
    }
  
    return (
      <ul style={{ listStyle: "none", padding: 0 }}>
        {summaries.map((s) => (
          <li key={s.id} style={{ marginBottom: "1rem" }}>
            <div><b>Style:</b> {s.style}</div>
            <div><b>Summary:</b></div>
            <pre style={{ whiteSpace: "pre-wrap" }}>{s.summary}</pre>
            <small>{new Date(s.created_at).toLocaleString()}</small>
            <hr />
          </li>
        ))}
      </ul>
    );
  }
  