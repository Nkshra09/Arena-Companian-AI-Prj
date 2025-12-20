import time
import requests
from config import Config

class AIModelService:
    def __init__(self):
        self.config = Config.MODELS_CONFIG
        
    def call_openai(self, prompt, model_name="GPT-4"):
        """Call OpenAI API"""
        model_config = self.config.get(model_name)
        if not model_config or not model_config['enabled']:
            return None
            
        headers = {
            "Authorization": f"Bearer {model_config['api_key']}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model_config['model_id'],
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        
        start_time = time.time()
        try:
            response = requests.post(model_config['endpoint'], headers=headers, json=data, timeout=30)
            response_time = round(time.time() - start_time, 2)
            
            if response.status_code == 200:
                result = response.json()
                text = result['choices'][0]['message']['content']
                tokens = result['usage']['completion_tokens']
                return {
                    "response": text,
                    "response_time": response_time,
                    "token_count": tokens
                }
        except Exception as e:
            print(f"Error calling OpenAI: {str(e)}")
            return None
    
    def call_anthropic(self, prompt, model_name="Claude-3"):
        """Call Anthropic Claude API"""
        model_config = self.config.get(model_name)
        if not model_config or not model_config['enabled']:
            return None
            
        headers = {
            "x-api-key": model_config['api_key'],
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model_config['model_id'],
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        
        start_time = time.time()
        try:
            response = requests.post(model_config['endpoint'], headers=headers, json=data, timeout=30)
            response_time = round(time.time() - start_time, 2)
            
            if response.status_code == 200:
                result = response.json()
                text = result['content'][0]['text']
                tokens = result['usage']['output_tokens']
                return {
                    "response": text,
                    "response_time": response_time,
                    "token_count": tokens
                }
        except Exception as e:
            print(f"Error calling Anthropic: {str(e)}")
            return None
    
    def call_google(self, prompt, model_name="Gemini Pro"):
        """Call Google Gemini API"""
        model_config = self.config.get(model_name)
        if not model_config or not model_config['enabled']:
            return None
            
        url = f"{model_config['endpoint']}?key={model_config['api_key']}"
        
        data = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 500}
        }
        
        start_time = time.time()
        try:
            response = requests.post(url, json=data, timeout=30)
            response_time = round(time.time() - start_time, 2)
            
            if response.status_code == 200:
                result = response.json()
                text = result['candidates'][0]['content']['parts'][0]['text']
                # Gemini doesn't return token count directly, estimate it
                tokens = len(text.split()) * 1.3  # Rough estimate
                return {
                    "response": text,
                    "response_time": response_time,
                    "token_count": int(tokens)
                }
        except Exception as e:
            print(f"Error calling Google: {str(e)}")
            return None
    
    def call_huggingface(self, prompt, model_name):
        """Call HuggingFace models"""
        model_config = self.config.get(model_name)
        if not model_config or not model_config['enabled']:
            return None
            
        headers = {
            "Authorization": f"Bearer {model_config['api_key']}",
            "Content-Type": "application/json"
        }
        
        data = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 500}
        }
        
        start_time = time.time()
        try:
            response = requests.post(model_config['endpoint'], headers=headers, json=data, timeout=30)
            response_time = round(time.time() - start_time, 2)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    text = result[0].get('generated_text', '')
                    tokens = len(text.split()) * 1.3  # Rough estimate
                    return {
                        "response": text,
                        "response_time": response_time,
                        "token_count": int(tokens)
                    }
        except Exception as e:
            print(f"Error calling HuggingFace {model_name}: {str(e)}")
            return None
    
    def get_live_response(self, prompt, model_name):
        """Route to appropriate API based on model name"""
        if model_name == "GPT-4":
            return self.call_openai(prompt, model_name)
        elif model_name == "Claude-3":
            return self.call_anthropic(prompt, model_name)
        elif model_name == "Gemini Pro":
            return self.call_google(prompt, model_name)
        elif model_name in ["Llama-3-70B", "Mistral-7B", "Phi-3"]:
            return self.call_huggingface(prompt, model_name)
        return None