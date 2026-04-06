# 🤖 Super Agents — AI-Powered Software Builder

An AI co-pilot system that builds software, web apps, and websites from a single prompt.

## 🧠 Agents

| Agent | Role |
|-------|------|
| `planner_agent.py` | Understands the idea, creates a dev plan |
| `architect_agent.py` | Designs folder structure, DB schema, API routes |
| `coder_agent.py` | Generates production-ready code |
| `editor_agent.py` | Modifies existing code via chat instructions |

## 🚀 Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## 💬 Example

```
What do you want to build? Food delivery app with admin dashboard

🧠 Planning...
🏗️  Designing Architecture...
💻 Generating Code...
✅ Done!
```

## 🔑 AI Provider

Uses [Puter AI](https://puter.com) — free access to GPT, Claude, Gemini and more.

## 📁 Structure

```
super-agents/
├── agents/
│   ├── planner_agent.py
│   ├── architect_agent.py
│   ├── coder_agent.py
│   └── editor_agent.py
├── main.py
├── requirements.txt
└── .env.example
```
