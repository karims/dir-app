import React, { useState } from 'react';

function App() {
  const [arxivId, setArxivId] = useState('');
  const [summary, setSummary] = useState('');
  const [researchDirections, setResearchDirections] = useState('');

  const handleProcess = async () => {
    const response = await fetch('/process/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ arxiv_id: arxivId })
    });
    const data = await response.json();
    setSummary(data.summary);
    setResearchDirections(data.research_directions);
  };

  return (
    <div>
      <h1>Research Paper Processor</h1>
      <input
        type="text"
        value={arxivId}
        onChange={(e) => setArxivId(e.target.value)}
        placeholder="Enter arXiv ID"
      />
      <button onClick={handleProcess}>Process</button>
      <h2>Summary</h2>
      <p>{summary}</p>
      <h2>Future Research Directions</h2>
      <p>{researchDirections}</p>
    </div>
  );
}

export default App;
