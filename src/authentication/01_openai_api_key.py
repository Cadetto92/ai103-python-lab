"""Authenticate with the OpenAI SDK using an API key."""

import os
from dotenv import load_dotenv

from openai import OpenAI


def main() -> None:
    # Load OPENAI_API_KEY and MODEL from the local .env file.
    load_dotenv()

    # Authentication: the OpenAI SDK reads the API key supplied here.
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    # Inference: send a prompt after the client has been authenticated.
    response = client.responses.create(
        # For the public OpenAI API, MODEL is an OpenAI model ID, not an Azure deployment name.
        model=os.environ["MODEL"],
        input="Explain Microsoft Entra ID in one sentence.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()