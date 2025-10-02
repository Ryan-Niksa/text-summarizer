import { saveAs } from "file-saver";

export function exportAsMarkdown(summaries) {
  if (!summaries.length) {
    alert("No summaries to export.");
    return;
  }
  const content = summaries
    .map(
      (s) =>
        `### Summary #${s.id} (${s.style})\n\n${s.summary}\n\n*Created: ${new Date(
          s.created_at
        ).toLocaleString()}*\n`
    )
    .join("\n---\n\n");

  const blob = new Blob([content], { type: "text/markdown;charset=utf-8" });
  saveAs(blob, "summaries.md");
}

export function exportAsText(summaries) {
  if (!summaries.length) {
    alert("No summaries to export.");
    return;
  }
  const content = summaries
    .map(
      (s) =>
        `Summary #${s.id} [${s.style}]\n${s.summary}\nCreated: ${new Date(
          s.created_at
        ).toLocaleString()}\n`
    )
    .join("\n----------------------\n");

  const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "summaries.txt");
}
