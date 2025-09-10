# 🔍 Ollama Web Scraper


An intelligent **fullstack web scraping and parsing application** that combines **Selenium-based scraping**, **FastAPI + Chainlit backend**, and a **React + Tailwind frontend**.

The project integrates **Ollama** for AI-powered content extraction and supports **CI/CD deployment** with Fly.io and GitHub Pages.

* * * * *

# 🎥 Video Demo

https://github.com/user-attachments/assets/e5bb8b18-dd37-47d6-96d1-0b3fc158b9dc

* * * * *

# ✨ Features


### Backend (FastAPI + Chainlit + Ollama)

-   🤖 **AI-Powered Extraction**: Extract structured information using natural language queries.

-   🔒 **Anti-Detection Scraping**: Stealth Selenium options, rotating user agents, and human-like patterns.

-   🌐 **Multi-Method Scraping**: Requests + Selenium for maximum success rate.

-   📊 **Chunk Processing**: Splits large DOMs into manageable pieces for AI parsing.

-   🎯 **Special Handling** for GitHub and popular sites.

-   🔄 **CORS Enabled**: Frontend-backend integration supported.

### Frontend (React + Tailwind)

-   ⚡ **Interactive UI**: Enter a URL to scrape, then parse results with natural language.

-   🖼️ **Responsive Design**: Built with Tailwind (CDN mode).

-   🔔 **Success/Error Feedback**: Real-time status updates after scrape/parse.

-   🌍 **Deployed on GitHub Pages** with CI/CD.

### DevOps

-   🚀 **Backend Deployment**: Fly.io

-   🌐 **Frontend Deployment**: GitHub Pages

-   🔄 **GitHub Actions CI/CD**: Automated build & deploy on push to `main`.

* * * * *

# 🏗️ Project Structure
```bash
Ollama-Web-Scraper/

├── backend/                     # FastAPI + Chainlit backend

│   ├── main.py                  # Entry point with routes + CORS

│   ├── utils/

│   │   ├── web_scrape.py        # Scraping logic (Selenium + requests)

│   │   └── parse.py             # AI parsing with Ollama

│   ├── requirements.txt         # Backend dependencies

│   └── fly.toml                 # Fly.io config


├── frontend/                    # React + Vite frontend

│   ├── index.html

│   ├── src/

│   │   ├── App.jsx              # UI (Scrape + Parse forms + results)

│   │   └── main.jsx

│   ├── package.json

│   └── vite.config.js

│

├── .github/workflows/CICD.yml   # GitHub Actions CI/CD

├── README.md                    # This file

```
* * * * *

# ⚙️ Installation

### Backend
```bash
git clone https://github.com/bassemalyyy/Ollama-Web-Scraper.git

cd Ollama-Web-Scraper/backend
```

### Create virtual environment
```bash
python -m venv myenv

myenv\Scripts\activate   # Windows

source myenv/bin/activate # Linux/Mac
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Install Ollama + model
```bash
ollama pull llama3.2
```

### Run backend
```bash
chainlit run main.py
```

### Frontend
```bash
cd ../frontend
```

### Install dependenciess
```bash
npm install
```

### Run dev server
```bash
npm run dev
```
* * * * *

# 🚀 Deployment

-   **Backend** → Fly.io (`flyctl deploy`)

-   **Frontend** → GitHub Pages (`npm run deploy`)

Both are automated via **GitHub Actions** (`.github/workflows/CICD.yml`).

* * * * *

# 🎯 Usage


1\.  Open the **frontend** (React app).

2\.  Enter a website URL → press **Scrape**.

3\.  Enter a natural language query → press **Parse**.

4\.  Results are displayed on the page.

### Example Workflow

-   **User**: Scrape `https://github.com/username`

-   **Backend**: ✅ Successfully scraped content.

-   **User**: Parse `repository names and descriptions`

-   **Bot**:
```bash
     🎯 Results:

    - awesome-project → A cool Python project

    - web-scraper → AI-powered web scraping tool
```

* * * * *

# 📋 Requirements

**Backend**
```bash
chainlit

fastapi

selenium

webdriver-manager

beautifulsoup4

langchain

langchain-ollama

requests
```

**Frontend**
```bash
react

vite

gh-pages
```
* * * * *

# 🛡️ Anti-Detection Scraping

-   Rotating user agents

-   Stealth Selenium flags

-   Random delays for human-like browsing

-   JS execution control

-   Content quality detection (detects auth pages / bot blocks)

* * * * *

# 🐛 Troubleshooting


-   **White page on GitHub Pages** → Check `vite.config.js` → set correct `base` path.

-   **No results from Parse** → Enable debug mode in backend to see raw scraped content.

-   **Ollama errors** → Ensure `ollama serve` is running.

-   **ChromeDriver issues** → `webdriver-manager` auto-handles version, but ensure Chrome is installed.

* * * * *

# 🙏 Acknowledgments

-   **Chainlit** → For interactive backend UI

-   **Ollama** → Local LLMs

-   **Selenium + BeautifulSoup** → Reliable scraping stack

-   **React + Vite + Tailwind** → Frontend

-   **Fly.io & GitHub Actions** → Smooth deployment

* * * * *

🔥 Built with ❤️ by **Bassem M. Aly**
