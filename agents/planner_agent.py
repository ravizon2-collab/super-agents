"""
Planner Agent — analyzes user prompt and creates a development plan.
"""
import openai
import json

client = openai.OpenAI(
    base_url="https://api.puter.com/puterai/openai/v1/",
    api_key="YOUR_PUTER_AUTH_TOKEN"
)

def plan(prompt: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior software architect. Given a user idea, "
                    "return a JSON plan with: app_name, description, tech_stack, "
                    "features (list), folder_structure (dict), and database_schema (dict)."
                )
            },
            {"role": "user", "content": f"Plan this app: {prompt}"}
        ]
    )
    content = response.choices[0].message.content
    try:
        return json.loads(content)
    except Exception:
        return {"raw_plan": content}

if __name__ == "__main__":
    result = plan("Build a task manager web app")
    print(json.dumps(result, indent=2))

