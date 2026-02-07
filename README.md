Arena Companion AI 📌 Project Overview Arena Companion AI is an MCA academic project designed as an AI model comparison platform. It enables users to evaluate, compare, and interact with multiple AI models through a unified interface. The system integrates a Python Flask backend with a React.js frontend, delivering a responsive and modular full-stack application. Features

Multi-Model Comparison Arena Compare outputs from different AI models side by side.
Intelligent Recommender System Suggests the most suitable AI model based on task requirements.
Comprehensive Analytics Dashboard Visualizes performance metrics and usage statistics.
Real-Time AI News Feed Integrated with NewsAPI to keep users updated on AI developments.
Dual Operational Modes
Demonstration Mode: Uses cached responses for offline demo.
Live Mode: Connects to APIs from OpenAI, Anthropic, Google, HuggingFace for real-time results.
Tech Stack

Backend: Python, Flask
Modular architecture
Environment-based configuration
JSON database
RESTful API endpoints
Frontend: React.js
React Router for navigation
Bootstrap components for styling
Responsive design
Setup Instructions

Clone the Repository git clone https://github.com/Nkshra09/Arena-CompanianAI.git cd Arena-CompanianAI
Backend Setup cd backend python -m venv arenaenv arenaenv\Scripts\activate # Windows pip install -r requirements.txt Create a .env file in backend/ Run the backend: py app.py
Frontend Setup cd frontend npm install npm start
