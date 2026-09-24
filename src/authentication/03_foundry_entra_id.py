"""Authenticate with the Microsoft Foundry SDK using Microsoft Entra ID."""

import os
from dotenv import load_dotenv

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


def main() -> None:
    # Load the Foundry project endpoint and model deployment name from .env.
    load_dotenv()

    # Authentication: DefaultAzureCredential obtains an Entra ID token without
    # storing a password or API key in the source code.
    project_client = AIProjectClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )

    # The Foundry client creates an OpenAI-compatible client for the project.
    openai_client = project_client.get_openai_client()

    # Inference: send a prompt through the authenticated Foundry connection.
    response = openai_client.responses.create(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        input="Explain Microsoft Entra ID in one sentence.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()