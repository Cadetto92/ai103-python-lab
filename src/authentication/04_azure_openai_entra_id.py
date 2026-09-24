"""Use the older AzureOpenAI API-version method with an Entra ID user bearer token."""

import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI



def main() -> None:
    # Load the Azure OpenAI resource, API version, and deployment.
    load_dotenv()

    # Authentication: obtain a bearer token for the signed-in Entra ID user.
    # DefaultAzureCredential can use Azure CLI, Visual Studio Code, or a managed identity.
    credential = DefaultAzureCredential()
    # Pass a token provider so AzureOpenAI receives and refreshes the bearer token.
    token_provider = get_bearer_token_provider(
        credential,
        "https://cognitiveservices.azure.com/.default",
    )
    client = AzureOpenAI(
        azure_ad_token_provider=token_provider,
        azure_endpoint=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME_04']}.openai.azure.com"
        ),
        api_version=os.environ["AZURE_OPENAI_API_VERSION_04"],
    )

    # Inference: model is the name of the deployment in Azure OpenAI.
    response = client.chat.completions.create(
        model=os.environ["DEPLOYMENT_NAME_04"],
        messages=[
            {
                "role": "user",
                "content": "In one or two sentences, explain how the AzureOpenAI client uses an Entra ID token provider to authenticate this request.",
            }
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()