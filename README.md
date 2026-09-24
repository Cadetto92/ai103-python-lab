# AI-103 Python Lab

A personal workspace for experimenting with the Microsoft AI-103 learning path.

## Quick start

Create and activate the local environment:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This workspace names the environment `.venv`. It is the same local Python
environment that the AI-103 materials refer to as `labenv`.

Add credentials to `.env` only when an exercise needs them. The `.env` file is
ignored by Git and must never be committed.

Add your Python code under `src` and run it with the activated environment.

Authentication examples are in `src\authentication`:

- `01_openai_api_key.py`: OpenAI SDK with an API key
- `02_openai_entra_id.py`: OpenAI SDK with a Microsoft Entra ID token
- `03_foundry_entra_id.py`: Microsoft Foundry SDK with a Microsoft Entra ID credential

## Suggested layout

- `src/`: Python code for AI-103 exercises
- `.env`: local configuration values, never committed to GitHub

## GitHub

After creating a GitHub repository named `ai103-python-lab`, connect and publish it:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/ai103-python-lab.git
git add .
git commit -m "Initial AI-103 Python lab setup"
git branch -M main
git push -u origin main
```