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

Copy `.env.example` to `.env` and add credentials only when an exercise needs them.
The `.env` file is ignored by Git and must never be committed.

Add your Python code under `src` and run it with the activated environment.

## Suggested layout

- `src/`: Python code for AI-103 exercises
- `.env.example`: names of configuration values, without secrets

## GitHub

After creating a GitHub repository named `ai103-python-lab`, connect and publish it:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/ai103-python-lab.git
git add .
git commit -m "Initial AI-103 Python lab setup"
git branch -M main
git push -u origin main
```