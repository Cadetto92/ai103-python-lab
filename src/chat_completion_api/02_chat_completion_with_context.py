"""Run an Entra ID Chat Completions conversation with context."""

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

    # Chat Completions keeps context in an ordered messages array. Each item
    # identifies who produced the content: system, user, or assistant.
    messages = [
        {
            "role": "system",
            "content": "Answer in one short sentence.",
        }
    ]

    while True:
        user_input = input("Enter a prompt, or type 'quit' to quit: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue

        # Add the new user turn before sending the complete conversation.
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model=os.environ["DEPLOYMENT_NAME"],
            messages=messages,
        )
        assistant_message = response.choices[0].message.content or ""
        # Add the model reply so the next request can use this turn as context.
        messages.append({"role": "assistant", "content": assistant_message})
        print(f"Assistant: {assistant_message}")


if __name__ == "__main__":
    main()
