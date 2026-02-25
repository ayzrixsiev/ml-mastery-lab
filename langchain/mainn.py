import sqlite3
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.tools import tool


@tool
def get_expenses(month: str):
    """Fetches expenses from the database for a specific month."""
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT category, amount FROM transactions WHERE month = ?",
        (month.capitalize(),),
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No records found for {month}."

    return str(rows)


llm = ChatOllama(model="llama3.1:8b", temperature=0)
ai_soul = "You are a finance expert. Provide insights based on tools."

app = create_agent(model=llm, tools=[get_expenses], system_prompt=ai_soul)

user_input = "How much did I spend in January?"

result = app.invoke({"messages": [("human", user_input)]})

print("\nAI answer:", result["messages"][-1].content)
