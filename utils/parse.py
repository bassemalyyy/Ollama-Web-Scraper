from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_ollama(dom_chunks, parse_description, progress_callback=None):
    """Parse DOM content using Ollama LLM with optional progress callback"""
    try:
        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(template) 
        chain = prompt | model
        
        parsed_results = []
        
        for i, chunk in enumerate(dom_chunks, start=1):
            try:
                if progress_callback:
                    # Call progress callback synchronously - no async/await
                    progress_callback(f"Processing chunk {i} of {len(dom_chunks)}...")
                
                response = chain.invoke({
                    "dom_content": chunk, 
                    "parse_description": parse_description
                })
                print(f"Parsed batch {i} of {len(dom_chunks)}")
                
                # Only add non-empty responses
                if response and response.strip():
                    parsed_results.append(response.strip())
                    
            except Exception as e:
                print(f"Error processing chunk {i}: {str(e)}")
                if progress_callback:
                    progress_callback(f"Error processing chunk {i}: {str(e)}")
                continue
        
        # Join results with proper formatting
        if parsed_results:
            return "\n\n".join(parsed_results)
        else:
            return "No matching information found in the content."
            
    except Exception as e:
        print(f"Error in parse_with_ollama: {str(e)}")
        return f"Error occurred during parsing: {str(e)}"