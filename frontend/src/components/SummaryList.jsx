import { saveAs } from "file-saver";
import jsPDF from "jspdf";

export default function SummaryList({ summaries }) {
  if (!summaries.length) {
    return <p style={{ fontStyle: "italic", color: "#6b7280" }}>No summaries found.</p>;
  }

  const exportMarkdown = (s) => {
    const content = `# Summary (Style: ${s.style})\n\n${s.summary}`;
    const blob = new Blob([content], { type: "text/markdown;charset=utf-8" });
    saveAs(blob, `summary-${s.id}.md`);
  };

  const exportPDF = (s) => {
    const doc = new jsPDF();
    doc.setFont("helvetica", "normal");
    doc.setFontSize(12);
    doc.text(`Summary (Style: ${s.style})`, 10, 10);
    doc.setFontSize(11);
    doc.text(s.summary, 10, 20, { maxWidth: 180 });
    doc.save(`summary-${s.id}.pdf`);
  };

  return (
    <div>
      {summaries.map((s) => (
        <div key={s.id} className="summary-card">
          <div className="summary-header">
            <span style={{ fontSize: "0.9rem", color: "#6b7280" }}>
              {new Date(s.created_at).toLocaleString()}
            </span>
            <span className="summary-style">{s.style}</span>
          </div>

          <pre>{s.summary}</pre>

          <div style={{ display: "flex", gap: "0.5rem" }}>
            <button onClick={() => exportMarkdown(s)}>Export MD</button>
            <button onClick={() => exportPDF(s)}>Export PDF</button>
          </div>
        </div>
      ))}
    </div>
  );
}
