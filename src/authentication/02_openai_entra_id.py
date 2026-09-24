"""Authenticate with the OpenAI SDK using Microsoft Entra ID."""

import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI


def main() -> None:
    # Load the Azure OpenAI endpoint and deployment name from the local .env file.
    load_dotenv()

    # Authentication: DefaultAzureCredential looks for an available Entra ID
    # login, such as Azure CLI, Visual Studio Code, or a managed identity.
    credential = DefaultAzureCredential()
    # The token provider requests and refreshes a token for Azure AI services.
    token_provider = get_bearer_token_provider(
        credential,
        "https://cognitiveservices.azure.com/.default",
    )
    client = OpenAI(
        api_key=token_provider,
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    )

    # Inference: use the authenticated OpenAI-compatible client to call Azure OpenAI.
    response = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="Explain Microsoft Entra ID in one sentence.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()