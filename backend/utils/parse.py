# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# template = (
#     "You are tasked with extracting specific information from the following text content: {dom_content}. "
#     "Please follow these instructions carefully: \n\n"
#     "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
#     "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
#     "3. **Empty Response:** If no information matches the description, return an empty string ('')."
#     "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
# )

# def parse_with_ollama(dom_chunks, parse_description, progress_callback=None):
#     """Parse DOM content using Ollama LLM with optional progress callback"""
#     try:
#         model = OllamaLLM(model="llama3.2")
#         prompt = ChatPromptTemplate.from_template(template) 
#         chain = prompt | model
        
#         parsed_results = []
        
#         for i, chunk in enumerate(dom_chunks, start=1):
#             try:
#                 if progress_callback:
#                     # Call progress callback synchronously - no async/await
#                     progress_callback(f"Processing chunk {i} of {len(dom_chunks)}...")
                
#                 response = chain.invoke({
#                     "dom_content": chunk, 
#                     "parse_description": parse_description
#                 })
#                 print(f"Parsed batch {i} of {len(dom_chunks)}")
                
#                 # Only add non-empty responses
#                 if response and response.strip():
#                     parsed_results.append(response.strip())
                    
#             except Exception as e:
#                 print(f"Error processing chunk {i}: {str(e)}")
#                 if progress_callback:
#                     progress_callback(f"Error processing chunk {i}: {str(e)}")
#                 continue
        
#         # Join results with proper formatting
#         if parsed_results:
#             return "\n\n".join(parsed_results)
#         else:
#             return "No matching information found in the content."
            
#     except Exception as e:
#         print(f"Error in parse_with_ollama: {str(e)}")
#         return f"Error occurred during parsing: {str(e)}"

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

def parse_with_groq(dom_chunks, parse_description, progress_callback=None):
    """Parse DOM content using Groq LLM with repo secrets (env vars)"""
    try:
        # ✅ Load API key from environment (repo secret will be available here)
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Make sure it's set in your repo secrets.")

        # ✅ Initialize Groq model
        model = ChatGroq(
            model="llama-3.1-8b-instant",  # you can swap to mixtral or gemma
            api_key=api_key
        )

        template = (
            "You are a world-class content analyzer. Your task is to analyze the following text "
            "and provide a helpful, relevant, and concise response to the user's query.\n\n"
            "Text to analyze: {dom_content}\n\n"
            "User's Query: {parse_description}\n\n"
            "Instructions:\n"
            "1. Respond based ONLY on the provided text.\n"
            "2. If answer not present, reply with: "
            "'The provided text does not contain information on that topic.'\n"
            "3. Do not invent information.\n"
            "4. Return a single, unified response."
        )

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model

        parsed_results = []

        for i, chunk in enumerate(dom_chunks, start=1):
            if progress_callback:
                progress_callback(f"Processing chunk {i} of {len(dom_chunks)}...")

            response = chain.invoke({
                "dom_content": chunk[:6000],
                "parse_description": parse_description
            })

            if hasattr(response, "content") and response.content.strip():
                parsed_results.append(response.content.strip())
            elif isinstance(response, str) and response.strip():
                parsed_results.append(response.strip())

        return "\n\n".join(parsed_results) if parsed_results else \
            "The provided text does not contain information on that topic."

    except Exception as e:
        print(f"Error in parse_with_groq: {str(e)}")
        return f"Error occurred during parsing: {str(e)}"