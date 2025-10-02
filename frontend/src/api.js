import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

// Create summary
export const createSummary = async (text, style) => {
  const res = await API.post("/summaries", { text, style });
  return res.data;
};

// Get summaries with optional filters
export const fetchSummaries = async (params = {}) => {
  const res = await API.get("/summaries", { params });
  return res.data;
};
