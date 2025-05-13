# Agentic_AI
This project is an agentic AI assistant powered by OpenAI and Tavily APIs. It can autonomously plan and execute tasks, perform live web searches, and generate or execute Python code—all through a conversational interface built with Streamlit.

✨ Features

🤖 LLM-driven step-by-step task planning

🔎 Real-time web search using Tavily API

🐍 Code generation and execution using Python's exec()

💬 Streamlit-based chat UI with memory support

🌐 Fully local and easy to customize

🚀 Getting Started
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/agentic-ai-assistant.git
cd agentic-ai-assistant
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
Run the app

bash
Copy
Edit
streamlit run task_agent.py
🛠️ Tech Stack
OpenAI GPT-3.5/GPT-4 via API

Tavily Web Search API

Python + Streamlit

dotenv for API key management

🧩 Use Cases
Research automation

Python coding assistant

Intelligent task breakdown

Custom AI agent experimentation
