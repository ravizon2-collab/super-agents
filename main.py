"""
Super Agents — Main Orchestrator
Connects all agents: Planner → Architect → Coder
"""
from agents.planner_agent import plan
from agents.architect_agent import design_architecture
from agents.coder_agent import generate_code
import json

def run(user_prompt: str):
    print(f"\n🧠 Planning: {user_prompt}")
    app_plan = plan(user_prompt)
    print(json.dumps(app_plan, indent=2))

    print("\n🏗️  Designing Architecture...")
    architecture = design_architecture(app_plan)
    print(json.dumps(architecture, indent=2))

    print("\n💻 Generating Code...")
    for route in architecture.get("api_routes", [])[:3]:
        task = f"Generate {route[\"method\"]} {route[\"path\"]} endpoint: {route[\"description\"]}"
        code = generate_code(task, "javascript")
        print(f"\n--- {route[\"path\"]} ---\n{code}")

    print("\n✅ Done!")

if __name__ == "__main__":
    user_input = input("What do you want to build? ")
    run(user_input)

