import requests
from datetime import datetime, timedelta
from config import Config

class NewsService:
    def __init__(self):
        self.api_key = Config.NEWS_API_KEY
        self.api_url = Config.NEWS_API_URL
        
    def get_ai_news(self, query="artificial intelligence", days=7, page_size=20):
        """
        Fetch AI-related news articles
        """
        if not self.api_key:
            return {
                "error": "News API key not configured",
                "articles": []
            }
        
        # Calculate date range
        from_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        to_date = datetime.now().strftime('%Y-%m-%d')
        
        params = {
            'q': query,
            'from': from_date,
            'to': to_date,
            'sortBy': 'publishedAt',
            'language': 'en',
            'pageSize': page_size,
            'apiKey': self.api_key
        }
        
        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Filter and format articles
                articles = []
                for article in data.get('articles', []):
                    if article.get('title') and article.get('description'):
                        formatted_article = {
                            'title': article['title'],
                            'description': article['description'],
                            'url': article['url'],
                            'source': article['source']['name'],
                            'published_at': article['publishedAt'],
                            'image_url': article.get('urlToImage'),
                            'author': article.get('author', 'Unknown')
                        }
                        articles.append(formatted_article)
                
                return {
                    'total_results': data.get('totalResults', 0),
                    'articles': articles,
                    'query': query,
                    'date_range': f"{from_date} to {to_date}"
                }
            else:
                return {
                    'error': f"API Error: {response.status_code}",
                    'articles': []
                }
                
        except Exception as e:
            return {
                'error': str(e),
                'articles': []
            }
    
    def get_trending_topics(self):
        """
        Get trending AI topics
        """
        topics = [
            "ChatGPT",
            "Claude AI",
            "Google Gemini",
            "Machine Learning",
            "Deep Learning",
            "Large Language Models",
            "AI Ethics",
            "AI Regulation"
        ]
        
        trending_news = {}
        for topic in topics[:4]:  # Limit to 4 topics to avoid rate limits
            news = self.get_ai_news(query=topic, days=3, page_size=5)
            if news.get('articles'):
                trending_news[topic] = news['articles'][:3]
        
        return trending_news