// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App


import { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");
  const [scraped, setScraped] = useState(null);
  const [parsed, setParsed] = useState(null);

  const handleScrape = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/scrape?url=${encodeURIComponent(url)}`);
      setScraped(res.data.content);
    } catch (err) {
      console.error(err);
    }
  };

  const handleParse = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/parse?url=${encodeURIComponent(url)}&query=${encodeURIComponent(query)}`);
      setParsed(res.data.result);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🔍 AI Web Scraper</h1>
      <input placeholder="Website URL" value={url} onChange={e => setUrl(e.target.value)} />
      <button onClick={handleScrape}>Scrape</button>
      {scraped && (
        <div>
          <h2>Scraped Content Preview</h2>
          <pre>{scraped.slice(0, 500)}...</pre>
        </div>
      )}
      <input placeholder="What to extract (e.g. emails)" value={query} onChange={e => setQuery(e.target.value)} />
      <button onClick={handleParse}>Parse</button>
      {parsed && (
        <div>
          <h2>Parsed Results</h2>
          <pre>{parsed}</pre>
        </div>
      )}
    </div>
  );
}

export default App;