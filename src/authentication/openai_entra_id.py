"""Authenticate with the OpenAI SDK using Microsoft Entra ID."""

import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
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
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    )
    response = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="Explain Microsoft Entra ID in one sentence.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()