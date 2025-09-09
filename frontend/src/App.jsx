// import { useState } from "react";
// import axios from "axios";

// const LoadingSpinner = () => (
//   <div className="flex justify-center items-center mt-4">
//     <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-white"></div>
//   </div>
// );

// const App = () => {
//   const [url, setUrl] = useState("");
//   const [query, setQuery] = useState("");
//   const [scraped, setScraped] = useState(null);
//   const [parsed, setParsed] = useState(null);
//   const [loading, setLoading] = useState(false);

//   // Backend base URL (Fly.io)
//   const BACKEND_URL = "https://ollama-web-scraper.fly.dev";

//   const handleScrape = async () => {
//     if (!url) return;
//     setLoading(true);
//     setScraped(null);
//     setParsed(null);
//     try {
//       const res = await axios.get(
//         `${BACKEND_URL}/scrape?url=${encodeURIComponent(url)}`
//       );
//       setScraped(res.data.content);
//     } catch (err) {
//       console.error(err);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleParse = async () => {
//     if (!url || !query) return;
//     setLoading(true);
//     setParsed(null);
//     try {
//       const res = await axios.get(
//         `${BACKEND_URL}/parse?url=${encodeURIComponent(url)}&query=${encodeURIComponent(
//           query
//         )}`
//       );
//       setParsed(res.data.result);
//     } catch (err) {
//       console.error(err);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col items-center justify-center p-4 font-sans">
//       <div className="w-full max-w-4xl bg-gray-800 rounded-lg shadow-2xl p-8 transform transition-all duration-500 hover:shadow-gray-700">
//         <h1 className="text-4xl font-extrabold text-white text-center mb-6 flex items-center justify-center">
//           <svg
//             className="w-10 h-10 mr-4 text-purple-400"
//             fill="currentColor"
//             viewBox="0 0 24 24"
//           >
//             <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0017 10c0-3.03-2.47-5.5-5.5-5.5S6 6.97 6 10s2.47 5.5 5.5 5.5c1.45 0 2.78-.56 3.79-1.46l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-4 0C9.01 14 7 11.99 7 9.5S9.01 5 11.5 5 16 7.01 16 9.5 13.99 14 11.5 14z" />
//           </svg>
//           AI Web Scraper
//         </h1>

//         <div className="flex flex-col md:flex-row gap-4 mb-4">
//           <input
//             type="text"
//             className="flex-grow p-3 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
//             placeholder="Website URL"
//             value={url}
//             onChange={(e) => setUrl(e.target.value)}
//           />
//           <button
//             onClick={handleScrape}
//             className="w-full md:w-auto px-6 py-3 bg-purple-600 hover:bg-purple-700 transition-colors duration-200 rounded-lg font-bold text-white shadow-md active:bg-purple-800 disabled:opacity-50"
//             disabled={loading || !url}
//           >
//             Scrape
//           </button>
//         </div>

//         {loading && <LoadingSpinner />}

//         {scraped && (
//           <div className="bg-gray-700 rounded-lg p-4 mt-4 shadow-inner">
//             <h2 className="text-lg font-semibold text-white mb-2">
//               Scraped Content Preview
//             </h2>
//             <pre className="whitespace-pre-wrap text-sm text-gray-300 p-2 bg-gray-800 rounded-md max-h-64 overflow-y-auto">
//               {scraped.slice(0, 1000)}...
//             </pre>
//           </div>
//         )}

//         <div className="flex flex-col md:flex-row gap-4 mt-6">
//           <input
//             type="text"
//             className="flex-grow p-3 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
//             placeholder="What to extract (e.g., emails, phone numbers, a summary)"
//             value={query}
//             onChange={(e) => setQuery(e.target.value)}
//           />
//           <button
//             onClick={handleParse}
//             className="w-full md:w-auto px-6 py-3 bg-purple-600 hover:bg-purple-700 transition-colors duration-200 rounded-lg font-bold text-white shadow-md active:bg-purple-800 disabled:opacity-50"
//             disabled={loading || !url || !query}
//           >
//             Parse
//           </button>
//         </div>

//         {parsed && (
//           <div className="bg-gray-700 rounded-lg p-4 mt-4 shadow-inner">
//             <h2 className="text-lg font-semibold text-white mb-2">
//               Parsed Results
//             </h2>
//             <pre className="whitespace-pre-wrap text-sm text-gray-300 p-2 bg-gray-800 rounded-md max-h-64 overflow-y-auto">
//               {parsed}
//             </pre>
//           </div>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;

import { useState } from "react";
import axios from "axios";

// This is a single-file React application.
// All components and styling are within this file.

const LoadingSpinner = () => (
  <div className="flex justify-center items-center mt-4">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-white"></div>
  </div>
);

const App = () => {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");
  const [scraped, setScraped] = useState(null);
  const [parsed, setParsed] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  // ✅ Replace with your Fly.io backend
  const BACKEND_URL = "https://ollama-web-scraper.fly.dev";

  const handleScrape = async () => {
    if (!url) return;
    setLoading(true);
    setScraped(null);
    setParsed(null);
    setMessage("");
    try {
      const res = await axios.get(
        `${BACKEND_URL}/scrape?url=${encodeURIComponent(url)}`
      );
      if (res.data && res.data.content) {
        setScraped(res.data.content);
        setMessage("✅ Scraping successful!");
      } else {
        setMessage("⚠️ No content returned from backend.");
      }
    } catch (err) {
      console.error(err);
      setMessage("❌ Error scraping website.");
    } finally {
      setLoading(false);
    }
  };

  const handleParse = async () => {
    if (!url || !query) return;
    setLoading(true);
    setParsed(null);
    setMessage("");
    try {
      const res = await axios.get(
        `${BACKEND_URL}/parse?url=${encodeURIComponent(url)}&query=${encodeURIComponent(
          query
        )}`
      );
      if (res.data && res.data.result) {
        setParsed(res.data.result);
        setMessage("✅ Parsing successful!");
      } else {
        setMessage("⚠️ No parse results returned.");
      }
    } catch (err) {
      console.error(err);
      setMessage("❌ Error parsing website.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col items-center justify-center p-4 font-sans">
      <div className="w-full max-w-4xl bg-gray-800 rounded-lg shadow-2xl p-8 transform transition-all duration-500 hover:shadow-gray-700">
        <h1 className="text-4xl font-extrabold text-white text-center mb-6 flex items-center justify-center">
          <svg
            className="w-10 h-10 mr-4 text-purple-400"
            fill="currentColor"
            viewBox="0 0 24 24"
          >
            <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0017 10c0-3.03-2.47-5.5-5.5-5.5S6 6.97 6 10s2.47 5.5 5.5 5.5c1.45 0 2.78-.56 3.79-1.46l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-4 0C9.01 14 7 11.99 7 9.5S9.01 5 11.5 5 16 7.01 16 9.5 13.99 14 11.5 14z" />
          </svg>
          AI Web Scraper
        </h1>

        <div className="flex flex-col md:flex-row gap-4 mb-4">
          <input
            type="text"
            className="flex-grow p-3 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
            placeholder="Website URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button
            onClick={handleScrape}
            className="w-full md:w-auto px-6 py-3 bg-purple-600 hover:bg-purple-700 transition-colors duration-200 rounded-lg font-bold text-white shadow-md active:bg-purple-800 disabled:opacity-50"
            disabled={loading || !url}
          >
            Scrape
          </button>
        </div>

        {loading && <LoadingSpinner />}

        {message && (
          <div className="mt-4 text-center text-sm font-semibold">
            {message}
          </div>
        )}

        {scraped && (
          <div className="bg-gray-700 rounded-lg p-4 mt-4 shadow-inner">
            <h2 className="text-lg font-semibold text-white mb-2">
              Scraped Content Preview
            </h2>
            <pre className="whitespace-pre-wrap text-sm text-gray-300 p-2 bg-gray-800 rounded-md max-h-64 overflow-y-auto">
              {scraped.slice(0, 2000)}...
            </pre>
          </div>
        )}

        <div className="flex flex-col md:flex-row gap-4 mt-6">
          <input
            type="text"
            className="flex-grow p-3 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
            placeholder="What to extract (e.g., emails, phone numbers, a summary)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            onClick={handleParse}
            className="w-full md:w-auto px-6 py-3 bg-purple-600 hover:bg-purple-700 transition-colors duration-200 rounded-lg font-bold text-white shadow-md active:bg-purple-800 disabled:opacity-50"
            disabled={loading || !url || !query}
          >
            Parse
          </button>
        </div>

        {parsed && (
          <div className="bg-gray-700 rounded-lg p-4 mt-4 shadow-inner">
            <h2 className="text-lg font-semibold text-white mb-2">
              Parsed Results
            </h2>
            <pre className="whitespace-pre-wrap text-sm text-gray-300 p-2 bg-gray-800 rounded-md max-h-64 overflow-y-auto">
              {parsed}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;