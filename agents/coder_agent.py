"""
Coder Agent — generates code based on the plan from the planner agent.
"""
import openai

client = openai.OpenAI(
    base_url="https://api.puter.com/puterai/openai/v1/",
    api_key="YOUR_PUTER_AUTH_TOKEN"
)

def generate_code(task: str, language: str = "javascript") -> str:
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are an expert {language} developer. "
                    "Generate clean, production-ready, well-commented code. "
                    "Return ONLY the code, no extra explanation."
                )
            },
            {"role": "user", "content": task}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    code = generate_code("Create a REST API with Express.js for a todo app", "javascript")
    print(code)

