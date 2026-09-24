"""Authenticate with the Microsoft Foundry SDK using Microsoft Entra ID."""

import os
from pathlib import Path

from dotenv import load_dotenv

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential



def main() -> None:
    # Load the Foundry resource, project, and deployment names for script 05.
    load_dotenv(Path(__file__).resolve().parent / ".env")

    # Authentication: DefaultAzureCredential obtains an Entra ID token without
    # storing a password or API key in the source code.
    # Build the Foundry project endpoint from the resource and project names.
    project_client = AIProjectClient(
        endpoint=(
            f"https://{os.environ['FOUNDRY_RESOURCE_NAME_05']}.services.ai.azure.com/"
            f"api/projects/{os.environ['FOUNDRY_PROJECT_NAME_05']}"
        ),
        credential=DefaultAzureCredential(),
    )

    # The Foundry client creates an OpenAI-compatible client for the project.
    openai_client = project_client.get_openai_client()

    # Inference: send a prompt through the authenticated Foundry connection.
    response = openai_client.responses.create(
        model=os.environ["DEPLOYMENT_NAME_05"],
        input="In one or two sentences, explain how Microsoft Foundry uses Entra ID to authenticate access to a project.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()