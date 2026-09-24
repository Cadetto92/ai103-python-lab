"""Run an Entra ID Responses API loop without conversation context."""

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

        # Responses API accepts a string input for an independent prompt, so no
        # previous response or conversation history is sent here.
        response = client.responses.create(
            model=os.environ["DEPLOYMENT_NAME"],
            input=user_input,
        )
        print(f"Assistant: {response.output_text}")


if __name__ == "__main__":
    main()
