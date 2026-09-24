"""Use the older AzureOpenAI API-version method with an Azure API key."""

import os
from pathlib import Path

from dotenv import load_dotenv

from openai import AzureOpenAI



def main() -> None:
    # Load the Azure OpenAI resource, API version, deployment, and key.
    load_dotenv(Path(__file__).resolve().parent / ".env")

    # Authentication: AzureOpenAI sends the Azure API key with each request.
    client = AzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY_03"],
        azure_endpoint=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME_03']}.openai.azure.com"
        ),
        api_version=os.environ["AZURE_OPENAI_API_VERSION_03"],
    )

    # Inference: model is the name of the deployment in Azure OpenAI.
    response = client.chat.completions.create(
        model=os.environ["DEPLOYMENT_NAME_03"],
        messages=[
            {
                "role": "user",
                "content": "In one or two sentences, explain how the AzureOpenAI client uses azure_endpoint and api_version to connect to Azure OpenAI.",
            }
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()