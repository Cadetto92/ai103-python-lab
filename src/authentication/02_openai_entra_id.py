"""Use the newer OpenAI v1 API with an Entra ID user bearer token."""

import os
from pathlib import Path

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI



def main() -> None:
    # Load the Azure OpenAI resource name and deployment name for script 02.
    load_dotenv(Path(__file__).resolve().parent / ".env")

    # Authentication: obtain a bearer token for the signed-in Entra ID user.
    # DefaultAzureCredential can use Azure CLI, Visual Studio Code, or a managed identity.
    credential = DefaultAzureCredential()
    # Pass a token provider so the OpenAI client receives and refreshes the bearer token.
    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
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
        input="In one or two sentences, explain how DefaultAzureCredential supplies an Entra ID token to the OpenAI client.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()