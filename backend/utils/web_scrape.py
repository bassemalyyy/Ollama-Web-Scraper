# import selenium.webdriver as webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import os

# def scrape_website(website):
#     print("Launching Chrome browser...")
    
#     # Use webdriver-manager to automatically handle chromedriver
#     try:
#         chrome_driver_path = ChromeDriverManager().install()
#     except Exception as e:
#         # Fallback to manual path if webdriver-manager fails
#         chrome_driver_path = r"myenv/ollama_web_scrape/chromedriver.exe"
#         if not os.path.exists(chrome_driver_path):
#             raise FileNotFoundError(f"ChromeDriver not found. Please install it manually or use webdriver-manager.")
    
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")
#     options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
#     driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
#     try:
#         if not website.startswith(('http://', 'https://')):
#             website = 'https://' + website
            
#         driver.get(website)
#         print("Page loaded...")
        
#         # Wait for page to load completely
#         driver.implicitly_wait(10)
        
#         html = driver.page_source
#         return html
        
#     except Exception as e:
#         print(f"Error occurred while scraping: {str(e)}")
#         raise e
#     finally:
#         driver.quit()
        
# def extract_body_content(html_content):
#     """Extract body content from HTML"""
#     try:
#         soup = BeautifulSoup(html_content, "html.parser")
#         body_content = soup.body
#         if body_content:
#             return str(body_content)
#         else:
#             return ""
#     except Exception as e:
#         print(f"Error extracting body content: {str(e)}")
#         return ""
    
# def clean_body_content(body_content):
#     """Clean body content by removing scripts, styles, and formatting text"""
#     try:
#         soup = BeautifulSoup(body_content, "html.parser")
        
#         # Remove script and style elements
#         for script_or_style in soup(["script", "style"]):
#             script_or_style.extract()
            
#         # Remove other unwanted elements
#         for element in soup(["nav", "footer", "header", "aside"]):
#             element.extract()
            
#         cleaned_content = soup.get_text(separator="\n")
#         cleaned_content = "\n".join(
#             line.strip() for line in cleaned_content.splitlines() if line.strip()
#         )
        
#         return cleaned_content
        
#     except Exception as e:
#         print(f"Error cleaning body content: {str(e)}")
#         return body_content

# def split_dom_content(dom_content, max_length=6000):
#     """Split DOM content into chunks for LLM processing"""
#     if not dom_content:
#         return []
        
#     return [
#         dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
#     ]

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time
import random
import requests
from urllib.parse import urlparse

def get_enhanced_chrome_options():
    """Get Chrome options with enhanced stealth capabilities"""
    options = Options()
    
    # Stealth options to avoid detection
    options.add_argument("--headless=new")  # Remove this line if you want to see the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # More realistic user agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    options.add_argument(f"--user-agent={random.choice(user_agents)}")
    
    # Additional stealth options
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-images")  # Faster loading
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--ignore-certificate-errors-spki-list")
    
    return options

def try_requests_fallback(website):
    """Try to scrape using requests as a fallback"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        response = requests.get(website, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Requests fallback failed: {str(e)}")
        return None

def scrape_website(website):
    """Enhanced website scraping with multiple fallback methods"""
    print("Launching enhanced Chrome browser...")
    
    # Ensure proper URL format
    if not website.startswith(('http://', 'https://')):
        website = 'https://' + website
    
    # First, try requests method (faster and sometimes works better)
    print("Trying requests method first...")
    html_content = try_requests_fallback(website)
    if html_content and len(html_content) > 1000:  # Basic content check
        print("Requests method successful!")
        return html_content
    
    # If requests fails, use Selenium with enhanced options
    print("Requests method failed, using enhanced Selenium...")
    
    try:
        chrome_driver_path = ChromeDriverManager().install()
    except Exception as e:
        # Fallback to manual path if webdriver-manager fails
        chrome_driver_path = r"myenv/ollama_web_scrape/chromedriver.exe"
        if not os.path.exists(chrome_driver_path):
            raise FileNotFoundError(f"ChromeDriver not found. Please install it manually or use webdriver-manager.")
    
    options = get_enhanced_chrome_options()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        # Execute script to remove webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # Navigate to the website
        driver.get(website)
        print("Page loaded, waiting for content...")
        
        # Wait for page to load and add random delay
        time.sleep(random.uniform(2, 4))
        
        # For GitHub specifically, try to wait for main content
        domain = urlparse(website).netloc.lower()
        if 'github.com' in domain:
            try:
                # Wait for GitHub's main content to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "main"))
                )
                print("GitHub main content detected!")
            except:
                print("GitHub main content not found, proceeding anyway...")
        
        # Scroll down to load any dynamic content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        html = driver.page_source
        
        # Check if we got meaningful content
        if "sign in" in html.lower() and "signed out" in html.lower():
            print("⚠️ Detected authentication page, trying alternative approach...")
            
            # Try without JavaScript disabled
            driver.quit()
            options = get_enhanced_chrome_options()
            # Remove the JavaScript disable option
            args = [arg for arg in options.arguments if not arg.startswith('--disable-javascript')]
            options.arguments = args
            
            driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.get(website)
            time.sleep(random.uniform(3, 5))
            html = driver.page_source
        
        return html
        
    except Exception as e:
        print(f"Error occurred while scraping: {str(e)}")
        raise e
    finally:
        driver.quit()

def extract_body_content(html_content):
    """Extract body content from HTML with enhanced cleaning"""
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Remove unwanted elements that might indicate auth pages
        for element in soup.find_all(text=lambda text: text and any(phrase in text.lower() for phrase in [
            "signed in with another tab", "signed out in another tab", "reload to refresh your session"
        ])):
            if element.parent:
                element.parent.decompose()
        
        body_content = soup.body
        if body_content:
            return str(body_content)
        else:
            # If no body, return the whole content
            return str(soup)
    except Exception as e:
        print(f"Error extracting body content: {str(e)}")
        return html_content

# def clean_body_content(body_content):
#     """Enhanced cleaning of body content"""
#     try:
#         soup = BeautifulSoup(body_content, "html.parser")
        
#         # Remove script and style elements
#         for script_or_style in soup(["script", "style", "noscript"]):
#             script_or_style.extract()
            
#         # Remove other unwanted elements
#         for element in soup(["nav", "footer", "header", "aside"]):
#             element.extract()
            
#         # Remove GitHub-specific auth elements
#         for element in soup.find_all(attrs={"class": lambda x: x and any(cls in str(x).lower() for cls in ["auth", "signin", "login", "session"])}):
#             element.extract()
            
#         # Remove elements with auth-related text
#         for element in soup.find_all(text=lambda text: text and any(phrase in text.lower() for phrase in [
#             "skip to content", "signed in with another tab", "signed out in another tab", 
#             "reload to refresh your session", "dismiss alert"
#         ])):
#             if element.parent:
#                 element.parent.extract()
        
#         cleaned_content = soup.get_text(separator="\n")
#         cleaned_content = "\n".join(
#             line.strip() for line in cleaned_content.splitlines() 
#             if line.strip() and not any(phrase in line.lower() for phrase in [
#                 "signed in with another tab", "signed out in another tab",
#                 "reload to refresh your session", "dismiss alert", "skip to content"
#             ])
#         )
        
#         return cleaned_content
        
#     except Exception as e:
#         print(f"Error cleaning body content: {str(e)}")
#         return body_content

def clean_body_content(body_content):
    try:
        soup = BeautifulSoup(body_content, "html.parser")
        
        # Only remove scripts and styles
        for script_or_style in soup(["script", "style", "noscript"]):
            script_or_style.extract()

        cleaned_content = soup.get_text(separator="\n")
        cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
        
        return cleaned_content
    except Exception as e:
        print(f"Error cleaning body content: {str(e)}")
        return body_content

def split_dom_content(dom_content, max_length=6000):
    """Split DOM content into chunks for LLM processing"""
    if not dom_content:
        return []
        
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

def detect_content_quality(content):
    """Detect if the scraped content is meaningful or just auth pages"""
    if not content:
        return False, "No content found"
    
    # Check for auth-related indicators
    auth_indicators = [
        "signed in with another tab",
        "signed out in another tab", 
        "reload to refresh your session",
        "skip to content"
    ]
    
    auth_count = sum(1 for indicator in auth_indicators if indicator in content.lower())
    content_length = len(content.strip())
    
    if auth_count > 2 and content_length < 2000:
        return False, "Content appears to be authentication/session page"
    
    if content_length < 500:
        return False, "Content too short, might be blocked"
    
    return True, "Content appears valid"