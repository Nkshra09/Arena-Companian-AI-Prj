import json

def clean_text_for_json(text):
    """
    Clean and format text to be JSON-safe
    """
    # Replace special characters
    text = text.replace('\\', '\\\\')  # Escape backslashes first
    text = text.replace('"', '\\"')     # Escape double quotes
    text = text.replace('\n', '\\n')    # Escape newlines
    text = text.replace('\r', '\\r')    # Escape carriage returns
    text = text.replace('\t', '\\t')    # Escape tabs
    
    return text

def format_ai_response(response_text):
    """
    Takes raw AI response and returns JSON-safe version
    """
    cleaned = clean_text_for_json(response_text)
    return cleaned

# Example usage
if __name__ == "__main__":
    # Test with your AI response
    raw_response = """AI, or Artificial Intelligence, is technology that enables machines to perform tasks that typically require human intelligence.

There are different types of AI:
- Narrow AI (what we have today)
- General AI (still theoretical)"""
    
    formatted = format_ai_response(raw_response)
    print("Original:")
    print(raw_response)
    print("\nFormatted for JSON:")
    print(formatted)
    print("\nAs JSON:")
    print(json.dumps({"response": formatted}, indent=2))