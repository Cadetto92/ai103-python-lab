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
        "https://ai.azure.com/.default",
    )
    client = OpenAI(
        api_key=token_provider,
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME']}.openai.azure.com/openai/v1/"
        ),
    )

    # The Responses API keeps context by linking each response to the previous
    # one, rather than by resending a messages array.
    previous_response_id = None

    while True:
        user_input = input("Enter a prompt, or type 'quit' to quit: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue

        # The first request has no previous ID. Later requests use the prior
        # response ID so the service can continue the same conversation.
        response_parameters = {
            "model": os.environ["DEPLOYMENT_NAME"],
            "instructions": "Answer in one short sentence.",
            "input": user_input,
        }
        if previous_response_id:
            response_parameters["previous_response_id"] = previous_response_id

        response = client.responses.create(**response_parameters)
        assistant_message = response.output_text
        # Save this response ID for the next turn in the conversation.
        previous_response_id = response.id
        print(f"Assistant: {assistant_message}")


if __name__ == "__main__":
    main()
