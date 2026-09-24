"""Use the newer OpenAI v1 API with an Azure OpenAI API key."""

import os
from pathlib import Path

from dotenv import load_dotenv

from openai import OpenAI



def main() -> None:
    # Load the Azure resource, deployment, and API key for script 01.
    load_dotenv(Path(__file__).resolve().parent / ".env")

    # Authentication: the OpenAI SDK sends the Azure API key with each request.
    client = OpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY_01"],
        base_url=(
            f"https://{os.environ['AZURE_OPENAI_RESOURCE_NAME_01']}.openai.azure.com/openai/v1/"
        ),
    )

    # Inference: use the deployed model through the Azure OpenAI endpoint.
    response = client.responses.create(
        model=os.environ["DEPLOYMENT_NAME_01"],  # Important: use the deployed model name.
        input="In one or two sentences, explain how the Azure OpenAI API key authenticates this request.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()