"""Run an Entra ID Responses API conversation with context."""

import os
from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv(Path(__file__).resolve().parent / ".env")

    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential,
        "https://cognitiveservices.azure.com/.default",
    )
    client = OpenAI(
        api_key=token_provider,
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME']}.openai.azure.com/openai/v1/"
        ),
    )

    previous_response_id = None

    while True:
        user_input = input("Enter a prompt, or type 'quit' to quit: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue

        response_parameters = {
            "model": os.environ["DEPLOYMENT_NAME"],
            "instructions": "Answer in one short sentence.",
            "input": user_input,
        }
        if previous_response_id:
            response_parameters["previous_response_id"] = previous_response_id

        response = client.responses.create(**response_parameters)
        assistant_message = response.output_text
        previous_response_id = response.id
        print(f"Assistant: {assistant_message}")


if __name__ == "__main__":
    main()
