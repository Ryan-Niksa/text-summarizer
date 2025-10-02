import { useEffect, useState } from "react";
import SummaryForm from "./components/SummaryForm";
import SummaryList from "./components/SummaryList";
import SearchBar from "./components/SearchBar";
import { fetchSummaries } from "./api";

function App() {
  const [summaries, setSummaries] = useState([]);

  const loadSummaries = async (params = {}) => {
    const data = await fetchSummaries({ limit: 20, ...params });
    setSummaries(data.items);
  };

  useEffect(() => {
    loadSummaries();
  }, []);

  const handleNewSummary = (summary) => {
    setSummaries((prev) => [summary, ...prev]);
  };

  const handleSearch = (params) => {
    loadSummaries(params);
  };

  return (
    <div style={{ maxWidth: "800px", margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>AI Summarizer</h1>
      <SummaryForm onNewSummary={handleNewSummary} />
      <h2>Past Summaries</h2>
      <SearchBar onSearch={handleSearch} />
      <SummaryList summaries={summaries} />
    </div>
  );
}

export default App;
