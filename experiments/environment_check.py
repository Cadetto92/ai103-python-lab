"""Confirm that the AI-103 lab environment is ready."""

import sys


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")

    try:
        import azure.identity  # noqa: F401
        import dotenv  # noqa: F401
        import rich  # noqa: F401
    except ImportError as error:
        print(f"Missing package: {error.name}")
        print("Install dependencies with: python -m pip install -r requirements.txt")
        raise SystemExit(1) from error

    print("AI-103 lab packages are available.")