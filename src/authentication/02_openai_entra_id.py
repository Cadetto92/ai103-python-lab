"""Authenticate with the OpenAI SDK using Microsoft Entra ID."""

import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI


def main() -> None:
    # Load the Azure OpenAI resource name and deployment name for script 02.
    load_dotenv()

    # Authentication: DefaultAzureCredential looks for an available Entra ID
    # login, such as Azure CLI, Visual Studio Code, or a managed identity.
    credential = DefaultAzureCredential()
    # The token provider requests and refreshes a token for Azure AI services.
    token_provider = get_bearer_token_provider(
        credential,
        "https://cognitiveservices.azure.com/.default",
    )
    # Build the Azure OpenAI endpoint from the resource name.
    client = OpenAI(
        api_key=token_provider,
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME_02']}.openai.azure.com/openai/v1/"
        ),
    )

    # Inference: use the authenticated OpenAI-compatible client to call Azure OpenAI.
    response = client.responses.create(
        model=os.environ["DEPLOYMENT_NAME_02"],  # Important: use the deployed model name.
        input="In one or two sentences, explain how an Entra ID bearer token authenticates a request to Azure OpenAI.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()