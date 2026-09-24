"""Run an Entra ID Chat Completions conversation with context."""

import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI


def main() -> None:
    load_dotenv()

    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential,
        "https://cognitiveservices.azure.com/.default",
    )
    client = OpenAI(
        api_key=token_provider,
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME_02']}.openai.azure.com/openai/v1/"
        ),
    )

    messages = [
        {
            "role": "system",
            "content": "Answer in one short sentence.",
        }
    ]

    while True:
        user_input = input("Enter a prompt, or type 'exit' to quit: ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model=os.environ["DEPLOYMENT_NAME_02"],
            messages=messages,
        )
        assistant_message = response.choices[0].message.content or ""
        messages.append({"role": "assistant", "content": assistant_message})
        print(f"Assistant: {assistant_message}")


if __name__ == "__main__":
    main()
