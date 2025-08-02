import chainlit as cl
import asyncio
from ollama_web_scrape.utils.web_scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content, detect_content_quality
from ollama_web_scrape.utils.parse import parse_with_ollama

# Store scraped content in user session
scraped_content = {}

@cl.on_chat_start
async def start():
    await cl.Message(
        content="# 🔍 AI Web Scraper\n\nWelcome! I can help you scrape websites and extract specific information using AI.\n\n**How to use:**\n1. Type `scrape <URL>` to scrape a website\n2. After scraping, type `parse <description>` to extract specific information\n\n**Examples:**\n- `scrape https://example.com`\n- `parse all email addresses`\n- `parse product prices and names`\n\nWhat would you like to scrape today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_message = message.content.strip().lower()
    
    # Check if user wants to scrape a website
    if user_message.startswith('scrape '):
        url = message.content[7:].strip()  # Remove 'scrape ' prefix
        await handle_scrape(url)
    
    # Check if user wants to parse content
    elif user_message.startswith('parse '):
        parse_description = message.content[6:].strip()  # Remove 'parse ' prefix
        await handle_parse(parse_description)
    
    # Handle help or general queries
    elif any(keyword in user_message for keyword in ['help', 'how', 'what can you do']):
        await cl.Message(
            content="## 📖 How to use the AI Web Scraper:\n\n"
                   "**Scraping a website:**\n"
                   "- Type: `scrape <URL>`\n"
                   "- Example: `scrape https://news.ycombinator.com`\n\n"
                   "**Parsing scraped content:**\n"
                   "- First scrape a website, then type: `parse <what you want to extract>`\n"
                   "- Examples:\n"
                   "  - `parse all email addresses`\n"
                   "  - `parse article titles and URLs`\n"
                   "  - `parse product names and prices`\n"
                   "  - `parse contact information`\n\n"
                   "**Tips:**\n"
                   "- Be specific about what you want to extract\n"
                   "- You can parse the same scraped content multiple times with different queries"
        ).send()
    
    else:
        await cl.Message(
            content="I didn't understand that command. Please use:\n"
                   "- `scrape <URL>` to scrape a website\n"
                   "- `parse <description>` to extract information from scraped content\n"
                   "- Type `help` for more information"
        ).send()

async def handle_scrape(url):
    """Handle website scraping"""
    if not url:
        await cl.Message(content="⚠️ Please provide a URL to scrape.").send()
        return
    
    # Show loading message
    loading_msg = cl.Message(content="🔄 Scraping the website... This may take a few moments.")
    await loading_msg.send()
    
    try:
        # Scrape the website
        html_content = await asyncio.get_event_loop().run_in_executor(
            None, scrape_website, url
        )
        
        # Extract and clean content
        body_content = extract_body_content(html_content)
        cleaned_content = clean_body_content(body_content)
        
        # Check content quality
        is_valid, quality_message = detect_content_quality(cleaned_content)
        
        # Store in user session
        user_id = cl.context.session.id
        scraped_content[user_id] = {
            'url': url,
            'content': cleaned_content,
            'content_length': len(cleaned_content),
            'is_valid': is_valid
        }
        
        # Format the preview more nicely
        preview_text = cleaned_content[:500] if len(cleaned_content) > 500 else cleaned_content
        # Clean up the preview text - remove extra whitespace and format better
        preview_lines = [line.strip() for line in preview_text.split('\n') if line.strip()]
        formatted_preview = '\n'.join(preview_lines[:15])  # Show first 15 non-empty lines
        
        # Send organized success message with quality indicator
        quality_indicator = "✅" if is_valid else "⚠️"
        status_message = "Successfully scraped!" if is_valid else f"Scraped with issues: {quality_message}"
        
        await cl.Message(
            content=f"# {quality_indicator} {status_message}\n\n"
                   f"**🌐 Website:** `{url}`\n"
                   f"**📊 Content Size:** `{len(cleaned_content):,}` characters\n"
                   f"**📄 Content Chunks:** `{len(split_dom_content(cleaned_content))}` chunks\n"
                   f"**🔍 Content Quality:** `{quality_message}`\n\n"
                   f"## 📖 Content Preview:\n"
                   f"```\n{formatted_preview}\n```\n"
                   f"{'*...content truncated*' if len(cleaned_content) > 500 else ''}\n\n"
                   f"## 🎯 Next Steps:\n"
                   f"{'You can now extract information using:' if is_valid else 'Content quality is low, but you can still try to extract information:'}\n"
                   f"`parse <what you want to find>`\n\n"
                   f"**Examples:**\n"
                   f"• `parse contact information`\n"
                   f"• `parse all links and URLs`\n"
                   f"• `parse email addresses`\n"
                   f"• `parse main headings and titles`\n"
                   f"• `parse repository information`" + (" (for GitHub profiles)" if "github.com" in url.lower() else "")
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ **Error scraping website:** {str(e)}\n\n"
                   "**Possible solutions:**\n"
                   "• Check if the URL is correct and accessible\n"
                   "• Ensure you have a stable internet connection\n"
                   "• The website might be blocking automated access\n"
                   "• Try adding `https://` if missing from the URL"
        ).send()

async def handle_parse(parse_description):
    """Handle content parsing"""
    user_id = cl.context.session.id
    
    if user_id not in scraped_content:
        await cl.Message(
            content="⚠️ **No scraped content found.**\n\nPlease scrape a website first using `scrape <URL>`"
        ).send()
        return
    
    if not parse_description:
        await cl.Message(
            content="⚠️ **Please describe what you want to extract.**\n\n"
                   "**Examples:**\n"
                   "• `parse all email addresses`\n"
                   "• `parse article titles and links`\n"
                   "• `parse product prices`\n"
                   "• `parse contact information`"
        ).send()
        return
    
    # Show loading message
    loading_msg = cl.Message(content="🔄 Analyzing content and extracting information...")
    await loading_msg.send()
    
    try:
        content = scraped_content[user_id]['content']
        url = scraped_content[user_id]['url']
        
        # Split content into chunks
        dom_chunks = split_dom_content(content)
        
        # Create a simple progress callback that doesn't use async
        progress_messages = []
        def progress_callback(message):
            progress_messages.append(message)
            print(f"Progress: {message}")
        
        # Parse content using Ollama (run in executor to avoid blocking)
        result = await asyncio.get_event_loop().run_in_executor(
            None, 
            parse_with_ollama,
            dom_chunks, 
            parse_description, 
            progress_callback
        )
        
        # Send results with better formatting
        await cl.Message(
            content=f"# 🎯 Extraction Results\n\n"
                   f"**🌐 Source:** `{url}`\n"
                   f"**📝 Query:** `{parse_description}`\n"
                   f"**🔍 Chunks Processed:** `{len(dom_chunks)}`\n\n"
                   f"## 📋 Results:\n"
                   f"```\n{result}\n```\n\n"
                   f"## 🔄 Want More?\n"
                   f"You can parse the same content again with a different query!\n"
                   f"Try: `parse <something else you want to find>`"
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ **Error during parsing:** {str(e)}\n\n"
                   "**This might be due to:**\n"
                   "• Ollama service not running - try `ollama serve` in terminal\n"
                   "• Model not available - try `ollama pull llama3.2`\n"
                   "• Network connectivity issues\n"
                   "• Content too large for processing"
        ).send()

if __name__ == "__main__":
    cl.run()