🔍 Ollama Web Scraper
=================

An intelligent web scraping tool that combines Selenium-based web scraping with AI-powered content extraction using Ollama. This tool can scrape websites, bypass common anti-bot measures, and extract specific information using natural language queries.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Chainlit](https://img.shields.io/badge/chainlit-enabled-orange.svg) ![Ollama](https://img.shields.io/badge/ollama-llama3.2-red.svg)

🎬 Video Demo
-------------
https://github.com/user-attachments/assets/217aa0f8-b070-4002-b9fb-de1634082a62

✨ Features
----------

-   **🤖 AI-Powered Extraction**: Use natural language to describe what you want to extract
-   **🔒 Anti-Detection**: Advanced techniques to bypass common bot protection
-   **🌐 Multi-Method Scraping**: Combines requests and Selenium for maximum success rate
-   **📱 Interactive Chat Interface**: User-friendly Chainlit web interface
-   **🔄 Content Quality Detection**: Automatically detects if scraping was successful
-   **📊 Chunk Processing**: Handles large content by splitting into manageable chunks
-   **🎯 Site-Specific Optimizations**: Special handling for popular sites like GitHub

🚀 Quick Start
--------------

### Prerequisites

-   Python 3.10 or higher
-   Chrome browser installed
-   Ollama installed and running

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/bassemalyyy/Ollama-Web-Scraper.git
    cd Ollama-Web-Scraper
    ```

2.  **Create virtual environment**

    ```bash
    python -m venv myenv

    # Windows
    myenv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install and setup Ollama**

    ```bash
    # Install Ollama (visit https://ollama.ai for your OS)
    # Then pull the required model
    ollama pull llama3.2
    ```

5.  **Run the application**

    ```bash
    chainlit run main.py
    ```

📋 Requirements
---------------

Create a `requirements.txt` file with:

```
chainlit
selenium
webdriver-manager
beautifulsoup4
langchain-ollama
langchain
requests
```

🎯 Usage
--------

### Basic Commands

1.  **Start the application**

    ```bash
    chainlit run main.py
    ```

2.  **Scrape a website**

    ```bash
    scrape https://example.com
    ```

3.  **Extract specific information**

    ```bash
    parse all email addresses
    parse product names and prices
    parse contact information
    ```

### Example Workflow

```bash
User: scrape https://github.com/username
Bot: ✅ Successfully scraped! Content size: 15,915 characters...

User: parse repository names and descriptions
Bot: 🎯 Extraction Results
     - Repository: awesome-project - A cool Python project
     - Repository: web-scraper - AI-powered web scraping tool
     ...
```

🏗️ Project Structure
---------------------

```bash
ollama_web_scrape/
├── main.py                          # Main Chainlit application
└── utils/
│       ├── __init__.py
│       ├── web_scrape.py            # Web scraping utilities
│       └── parse.py                 # AI parsing with Ollama
├── requirements.txt                 # Python dependencies
├── chromedriver.exe                # Chrome Web driver
├── README.md                       # This file
└── .gitignore                      # Git ignore file

```

🔧 Configuration
----------------

### Ollama Models

The default model is `llama3.2`. To use a different model, modify `parse.py`:

```bash
model = OllamaLLM(model="model-name")
```

### Chrome Options

Web scraping behavior can be customized in `web_scrape.py`:

```bash
def get_enhanced_chrome_options():
    options = Options()
    # Add your custom options here
    options.add_argument("--headless")  # Remove for visible browser
    return options
```

🛡️ Anti-Detection Features
---------------------------

-   **Rotating User Agents**: Multiple realistic browser user agents
-   **Stealth Mode**: Removes automation detection markers
-   **Random Delays**: Human-like timing patterns
-   **JavaScript Handling**: Dynamic enable/disable based on site requirements
-   **Content Quality Detection**: Identifies blocked or authentication pages

📖 API Reference
----------------

### Web Scraping Functions
#### `scrape_website(website)`
Main scraping function with fallback methods.

**Parameters:**
-   `website` (str): URL to scrape

**Returns:**
-   `str`: Raw HTML content

#### `extract_body_content(html_content)`
Extracts body content from HTML.
#### `clean_body_content(body_content)`
Cleans and formats scraped content.
#### `split_dom_content(dom_content, max_length=6000)`
Splits content into chunks for AI processing.
### AI Parsing Functions
#### `parse_with_ollama(dom_chunks, parse_description, progress_callback=None)`
Extracts specific information using AI.

**Parameters:**

-   `dom_chunks` (list): Content chunks to process
-   `parse_description` (str): Natural language description of what to extract
-   `progress_callback` (function): Optional progress reporting function

🎨 Usage Examples
-----------------

### Scraping E-commerce Sites

```bash
scrape https://example-shop.com
parse product names, prices, and availability
```

### Extracting Contact Information

```bash
scrape https://company-website.com
parse email addresses and phone numbers
```

### Analyzing GitHub Profiles

```bash
scrape https://github.com/username
parse repository names, stars, and descriptions
```

### News Article Extraction

```bash
scrape https://news-website.com
parse article titles, authors, and publication dates
```

🐛 Troubleshooting
------------------

### Common Issues

1.  **Ollama not running**

    ```bash
    ollama serve
    ```
2.  **ChromeDriver issues**
    -   The app uses webdriver-manager for automatic ChromeDriver management
    -   Ensure Chrome browser is installed
3.  **Authentication pages detected**
    -   The tool automatically detects and attempts to bypass auth pages
    -   Some sites may require manual intervention
4.  **Content quality low**
    -   Try different scraping methods
    -   Check if the site blocks automated access

### Error Messages

-   **"No running event loop"**: Fixed in the latest version
-   **"ChromeDriver not found"**: Install Chrome browser
-   **"Ollama service not running"**: Start Ollama with `ollama serve`


🙏 Acknowledgments
------------------

-   [Chainlit](https://chainlit.io/) for the amazing chat interface.
-   [Ollama](https://ollama.ai/) for local LLM capabilities.
-   [Selenium](https://selenium.dev/) for web automation.
-   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.


* * * * *

Made with ❤️ by [Bassem M. Aly]
