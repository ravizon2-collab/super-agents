"""
Architect Agent — designs folder structure, database schema, and API routes.
"""
import openai
import json

client = openai.OpenAI(
    base_url="https://api.puter.com/puterai/openai/v1/",
    api_key="YOUR_PUTER_AUTH_TOKEN"
)

def design_architecture(plan: dict) -> dict:
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a software architect. Given an app plan, return a JSON with: "
                    "folder_structure, api_routes (list of {method, path, description}), "
                    "database_tables (list of {name, fields})."
                )
            },
            {"role": "user", "content": f"Design architecture for: {json.dumps(plan)}"}
        ]
    )
    content = response.choices[0].message.content
    try:
        return json.loads(content)
    except Exception:
        return {"raw_architecture": content}

if __name__ == "__main__":
    plan = {"app_name": "TodoApp", "features": ["create task", "delete task", "mark done"]}
    result = design_architecture(plan)
    print(json.dumps(result, indent=2))

