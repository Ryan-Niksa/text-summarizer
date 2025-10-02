import "./App.css";
import { useEffect, useState } from "react";
import SummaryForm from "./components/SummaryForm";
import SummaryList from "./components/SummaryList";
import SearchBar from "./components/SearchBar";
import { fetchSummaries } from "./api";

function App() {
  const [summaries, setSummaries] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const loadSummaries = async (params = {}) => {
    setLoading(true);
    setError("");
    try {
      const data = await fetchSummaries({ limit: 20, ...params });
      setSummaries(data.items);
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
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
    <div className="container">
      <h1>AI Summarizer</h1>

      <SummaryForm onNewSummary={handleNewSummary} />

      <h2>Past Summaries</h2>
      <SearchBar onSearch={handleSearch} />

      {loading && <p>Loading summaries...</p>}
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
      {!loading && !error && <SummaryList summaries={summaries} />}
    </div>
  );
}

export default App;
