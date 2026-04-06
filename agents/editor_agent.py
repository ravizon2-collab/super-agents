"""
Editor Agent — modifies existing code based on user chat instructions.
"""
import openai

client = openai.OpenAI(
    base_url="https://api.puter.com/puterai/openai/v1/",
    api_key="YOUR_PUTER_AUTH_TOKEN"
)

def edit_code(existing_code: str, instruction: str, language: str = "javascript") -> str:
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are an expert {language} developer. "
                    "You will receive existing code and an instruction to modify it. "
                    "Return ONLY the updated code, no extra explanation."
                )
            },
            {
                "role": "user",
                "content": f"Existing code:\n```\n{existing_code}\n```\n\nInstruction: {instruction}"
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    code = "function hello() { console.log(\"Hello\"); }"
    updated = edit_code(code, "Add dark mode support and a goodbye function")
    print(updated)

