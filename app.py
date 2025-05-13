import os
import streamlit as st
from openai import OpenAI
from tavily import TavilyClient
from dotenv import load_dotenv

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize clients
client = OpenAI(api_key=OPENAI_API_KEY)
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# Initialize session state for memory
if "memory" not in st.session_state:
    st.session_state.memory = []

# LLM interaction
def chat_with_llm(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

# Web search with Tavily
def web_search(query):
    try:
        results = tavily.search(query=query, search_depth="basic")
        return str(results)
    except Exception as e:
        return f"Search failed: {e}"

# Execute Python code
def execute_python(code):
    try:
        exec(code, globals())
        return "Code executed successfully."
    except Exception as e:
        return f"Execution error: {e}"

# Plan and execute task
def plan_and_execute(task):
    st.chat_message("assistant").write("📋 Planning steps...")
    plan_prompt = f"""
    Break this task into steps: {task}
    Return as a numbered list. Example:
    1. Search for X
    2. Write a Python script to process Y
    """
    plan = chat_with_llm(plan_prompt)
    st.chat_message("assistant").write(f"🧠 Plan:\n{plan}")

    for step in plan.split("\n"):
        if not step.strip():
            continue
        st.chat_message("user").write(step.strip())
        if "search" in step.lower():
            query = step.split("Search for ")[-1]
            result = web_search(query)
            st.chat_message("assistant").write(f"🔍 Search Result:\n{result}")
            st.session_state.memory.append(f"Search: {query}\nResult: {result}")
        elif "python" in step.lower():
            code_prompt = f"Write Python code to: {step}"
            code = chat_with_llm(code_prompt)
            result = execute_python(code)
            st.chat_message("assistant").write(f"```python\n{code}\n```\n💡Result: {result}")
            st.session_state.memory.append(f"Code: {code}\nResult: {result}")
        else:
            response = chat_with_llm(step)
            st.chat_message("assistant").write(f"{response}")
            st.session_state.memory.append(f"Step: {step}\nResponse: {response}")

# Streamlit app layout
st.set_page_config(page_title="LLM Task Agent", layout="centered")
st.title("🧠 LLM Task Agent with Web + Code")

task = st.chat_input("Enter a high-level task...")
if task:
    st.chat_message("user").write(task)
    plan_and_execute(task)

# Display memory/history
if st.session_state.memory:
    with st.expander("🗂 Task Memory"):
        for item in st.session_state.memory:
            st.markdown(f"```\n{item}\n```")
