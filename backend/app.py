from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
from config import Config
from models.ai_service import AIModelService
from services.news_service import NewsService

app = Flask(__name__)
CORS(app)

# Initialize AI Service
ai_service = AIModelService()
news_service = NewsService()

# Load data from JSON files
def load_json_file(filename):
    try:
        with open(f'data/{filename}', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Get model information with strengths
def get_model_info(model_name):
    """Get model information from models_info.json"""
    models_data = load_json_file('models_info.json')
    if models_data:
        for model in models_data['models']:
            if model['model_name'] == model_name:
                return {
                    'model_type': model['model_type'],
                    'provider': model['provider'],
                    'strengths': model.get('best_for', [])
                }
    return {'model_type': 'LLM', 'provider': 'Unknown', 'strengths': []}

@app.route('/')
def home():
    return jsonify({
        "message": "Arena Companion AI Backend is running!",
        "mode": Config.APP_MODE,
        "available_modes": ["demo", "live"]
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "mode": Config.APP_MODE
    })

@app.route('/api/mode', methods=['GET'])
def get_mode():
    """Get current application mode"""
    enabled_models = [name for name, config in Config.MODELS_CONFIG.items() if config['enabled']]
    return jsonify({
        "current_mode": Config.APP_MODE,
        "enabled_models": enabled_models,
        "total_enabled": len(enabled_models)
    })

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    """Get all available demo prompts"""
    data = load_json_file('responses.json')
    if data:
        prompts = [{"id": p["id"], "prompt": p["prompt"]} for p in data["prompts"]]
        return jsonify({"prompts": prompts})
    return jsonify({"error": "Data not found"}), 404

@app.route('/api/compare', methods=['POST'])
def compare_models():
    """Compare AI models - works in both demo and live mode"""
    request_data = request.get_json()
    user_prompt = request_data.get('prompt', '').strip()
    mode = request_data.get('mode', Config.APP_MODE)  # Allow override from frontend
    
    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    # DEMO MODE - Use pre-generated responses
    if mode == 'demo':
        data = load_json_file('responses.json')
        if not data:
            return jsonify({"error": "Database not found"}), 500
        
        # Find matching prompt
        matching_prompt = None
        for p in data["prompts"]:
            if p["prompt"].lower() == user_prompt.lower():
                matching_prompt = p
                break
        
        if not matching_prompt:
            return jsonify({
                "error": "Prompt not found in demo database",
                "message": "Please try one of the available demo prompts or switch to live mode",
                "available_prompts": [p["prompt"] for p in data["prompts"]],
                "mode": "demo"
            }), 404
        
        time.sleep(0.5)  # Simulate processing
        
        return jsonify({
            "prompt": matching_prompt["prompt"],
            "responses": matching_prompt["responses"],
            "total_models": len(matching_prompt["responses"]),
            "mode": "demo"
        })
    
    # LIVE MODE - Call actual APIs
    elif mode == 'live':
        models_to_query = ["GPT-4", "Claude-3", "Gemini Pro", "Llama-3-70B", "Mistral-7B", "Phi-3"]
        responses = []
        
        for model_name in models_to_query:
            # Check if model is enabled (has API key)
            if not Config.MODELS_CONFIG.get(model_name, {}).get('enabled'):
                continue
            
            # Get live response from API
            result = ai_service.get_live_response(user_prompt, model_name)
            
            if result:
                # Get model additional info
                model_info = get_model_info(model_name)
                
                responses.append({
                    "model_name": model_name,
                    "model_type": model_info['model_type'],
                    "provider": model_info['provider'],
                    "response": result['response'],
                    "response_time": result['response_time'],
                    "token_count": result['token_count'],
                    "strengths": model_info['strengths']
                })
        
        if not responses:
            return jsonify({
                "error": "No models available",
                "message": "Please add API keys to enable live mode",
                "mode": "live"
            }), 503
        
        return jsonify({
            "prompt": user_prompt,
            "responses": responses,
            "total_models": len(responses),
            "mode": "live"
        })
    
    return jsonify({"error": "Invalid mode"}), 400

@app.route('/api/models', methods=['GET'])
def get_models_info():
    """Get all models information"""
    data = load_json_file('models_info.json')
    if data:
        # Add API key status to each model
        for model in data['models']:
            model_name = model['model_name']
            model['api_enabled'] = Config.MODELS_CONFIG.get(model_name, {}).get('enabled', False)
        return jsonify(data)
    return jsonify({"error": "Models information not found"}), 404

@app.route('/api/recommend', methods=['POST'])
def recommend_model():
    """Smart Recommender - Recommend models based on task"""
    request_data = request.get_json()
    task = request_data.get('task', '').strip().lower()
    
    if not task:
        return jsonify({"error": "Task is required"}), 400
    
    data = load_json_file('models_info.json')
    if not data:
        return jsonify({"error": "Models information not found"}), 500
    
    recommendations = data["task_recommendations"].get(task, [])
    
    if not recommendations:
        return jsonify({
            "error": "Task not found",
            "available_tasks": list(data["task_recommendations"].keys())
        }), 404
    
    recommended_models = []
    for model_name in recommendations:
        for model in data["models"]:
            if model["model_name"] == model_name:
                # Add API status
                model_copy = model.copy()
                model_copy['api_enabled'] = Config.MODELS_CONFIG.get(model_name, {}).get('enabled', False)
                recommended_models.append(model_copy)
                break
    
    return jsonify({
        "task": task,
        "recommended_models": recommended_models,
        "total_recommendations": len(recommended_models)
    })

@app.route('/api/analytics', methods=['POST'])
def get_analytics():
    """Get comparison analytics"""
    request_data = request.get_json()
    responses = request_data.get('responses', [])
    
    if not responses:
        return jsonify({"error": "No responses provided"}), 400
    
    fastest_model = min(responses, key=lambda x: x['response_time'])
    slowest_model = max(responses, key=lambda x: x['response_time'])
    most_detailed = max(responses, key=lambda x: x['token_count'])
    most_concise = min(responses, key=lambda x: x['token_count'])
    
    avg_response_time = sum(r['response_time'] for r in responses) / len(responses)
    avg_token_count = sum(r['token_count'] for r in responses) / len(responses)
    
    return jsonify({
        "fastest_model": fastest_model['model_name'],
        "fastest_time": fastest_model['response_time'],
        "slowest_model": slowest_model['model_name'],
        "slowest_time": slowest_model['response_time'],
        "most_detailed_model": most_detailed['model_name'],
        "most_detailed_tokens": most_detailed['token_count'],
        "most_concise_model": most_concise['model_name'],
        "most_concise_tokens": most_concise['token_count'],
        "average_response_time": round(avg_response_time, 2),
        "average_token_count": round(avg_token_count, 2)
    })
@app.route('/api/news', methods=['GET'])
def get_ai_news():
    """Get AI-related news articles"""
    query = request.args.get('query', 'artificial intelligence')
    days = int(request.args.get('days', 7))
    page_size = int(request.args.get('pageSize', 20))
    
    news_data = news_service.get_ai_news(query, days, page_size)
    
    return jsonify(news_data)

@app.route('/api/news/trending', methods=['GET'])
def get_trending_news():
    """Get trending AI topics and news"""
    trending = news_service.get_trending_topics()
    
    return jsonify({
        'trending_topics': trending,
        'total_topics': len(trending)
    })
@app.route('/api/news/search', methods=['POST'])
def search_news():
    """Search news with custom parameters"""
    request_data = request.get_json()
    
    query = request_data.get('query', 'AI')
    days = request_data.get('days', 7)
    page_size = request_data.get('pageSize', 20)
    
    news_data = news_service.get_ai_news(query, days, page_size)
    
    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)