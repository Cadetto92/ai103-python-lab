"""Run an Entra ID Chat Completions loop without conversation context."""

import os
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI


def main() -> None:
    load_dotenv(Path(__file__).resolve().parent / ".env")

    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
    )
    client = OpenAI(
        api_key=token_provider,
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME']}.openai.azure.com/openai/v1/"
        ),
    )

    while True:
        user_input = input("Enter a prompt, or type 'quit' to quit: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue

        # Chat Completions always receives a messages array. With no context,
        # the array contains only the current user message.
        response = client.chat.completions.create(
            model=os.environ["DEPLOYMENT_NAME"],
            messages=[{"role": "user", "content": user_input}],
        )
        print(f"Assistant: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()
