# AI-103 Python Lab

A personal workspace for experimenting with the Microsoft AI-103 learning path.

## Quick start

1. Create the local Python environment once:

```powershell
py -3.13 -m venv .venv
```

This workspace names the environment `.venv`. It is the same local Python
environment that the AI-103 materials refer to as `labenv`.

2. Activate the environment in each new PowerShell session:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Upgrade `pip` and install the project dependencies once after creating the
	environment:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Repeat step 3 only when `requirements.txt` changes or you want to update the
installed packages. You do not need to reinstall the dependencies before every
script.

4. Before running a Python script, copy `.env.example` to `.env` and fill in
	the required variables for that script. Keep `.env` private; it is ignored by
	Git.

```powershell
Copy-Item .env.example .env
```

5. Make sure the required Azure resources already exist: an Azure OpenAI
	resource with a model deployment, or a Microsoft Foundry resource with a
	project and model deployment.

6. Run any Python script while the environment is active. For example:

```powershell
python .\src\authentication\01_openai_azure_api_key.py
```

Replace the example path with the Python script you want to run.

7. When you are finished, leave the environment with:

```powershell
deactivate
```

## Layout

- `src/`: Python code for AI-103 exercises
- `src/authentication/`: authentication examples for Azure OpenAI and Microsoft Foundry
	- `01_openai_azure_api_key.py`: newer OpenAI v1 API with an Azure OpenAI API key
	- `02_openai_entra_id.py`: newer OpenAI v1 API with a Microsoft Entra ID token
	- `03_azure_openai_azure_api_key.py`: older AzureOpenAI API-version method with an Azure OpenAI API key
	- `04_azure_openai_entra_id.py`: older AzureOpenAI API-version method with a Microsoft Entra ID token
	- `05_foundry_entra_id.py`: Microsoft Foundry SDK with a Microsoft Entra ID credential

- `src/chat_completion_api/`: Chat Completions examples using Entra ID authentication, without and with conversation context
	- `01_chat_completion.py`: simple request without previous context
	- `02_chat_completion_with_context.py`: request with previous conversation messages
- `.env.example`: committed configuration template with empty values
- `.env`: local configuration values; this file is ignored by Git and must never be committed

## GitHub

After creating a GitHub repository named `ai103-python-lab`, connect and publish it:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/ai103-python-lab.git
git add .
git commit -m "Initial AI-103 Python lab setup"
git branch -M main
git push -u origin main
```

## Authentication

The examples are in `src/authentication/`. Scripts `01` and `02` use the newer
Azure OpenAI v1 API approach with the generic `OpenAI` client. Scripts `03` and
`04` show the older Azure-specific API-version approach with the `AzureOpenAI`
client. Script `05` uses the Microsoft Foundry project client with a credential
passed directly to that client.

All five scripts call a deployed model in Azure. The first four compare the
newer v1 API approach with the older API-version approach and show two
authentication choices; the fifth uses the Microsoft Foundry project client.

| Script | Client | Authentication | Endpoint style |
| --- | --- | --- | --- |
| `01_openai_azure_api_key.py` | `OpenAI` from the `openai` package | Azure OpenAI API key | Azure OpenAI `/openai/v1/` endpoint |
| `02_openai_entra_id.py` | `OpenAI` from the `openai` package | Entra ID user bearer token through a token provider | Azure OpenAI `/openai/v1/` endpoint |
| `03_azure_openai_azure_api_key.py` | `AzureOpenAI` from the `openai` package | Azure OpenAI API key | Azure endpoint plus API version |
| `04_azure_openai_entra_id.py` | `AzureOpenAI` from the `openai` package | Entra ID user bearer token through a token provider | Azure endpoint plus API version |
| `05_foundry_entra_id.py` | `AIProjectClient` from `azure-ai-projects` | Entra ID credential passed directly to the client | Microsoft Foundry project endpoint |

### Newer v1 API versus older API-version method

Both clients come from the same `openai` Python package. Azure OpenAI is the
Azure service being called; `AzureOpenAI` is not a separate Azure SDK.

The newer v1 approach in scripts `01` and `02` uses the generic `OpenAI` client
with a `base_url` ending in `/openai/v1/`. The `model` argument is the Azure
deployment name. This approach uses the OpenAI-compatible v1 endpoint and does
not require a dated Azure API version in the client constructor.

The older API-version method in scripts `03` and `04` uses the Azure-specific
`AzureOpenAI` client with `azure_endpoint` and a dated `api_version`. The client
uses the Azure OpenAI URL shape and API-version setting directly instead of the
`/openai/v1/` base URL. Script `03` uses an API key; script `04` uses an Entra
ID bearer-token provider. Both use the Chat Completions endpoint, which is
compatible with this older API-version method.

In short: scripts `01` and `02` demonstrate the newer v1 endpoint, while scripts
`03` and `04` demonstrate the older Azure-specific API-version configuration.
The authentication choice is independent of the endpoint method.

`AIProjectClient` is from the `azure-ai-projects` package. In script `05`, the
Entra ID credential is passed directly to `AIProjectClient`, which owns token
acquisition for the Microsoft Foundry project and returns an OpenAI-compatible
client for model inference. This differs from scripts `02` and `04`, where a
token provider supplies a user bearer token directly to the OpenAI client.

### Authentication choices

- **Azure OpenAI API key:** simple for local learning and quick experiments.
	The key grants access to the Azure OpenAI resource, so keep it in `.env`, do
	not commit it, and rotate it if it is exposed.
- **Microsoft Entra ID:** scripts `02` and `04` use a token provider to supply a
	bearer token to the OpenAI client; script `05` passes the credential directly
	to `AIProjectClient`. `DefaultAzureCredential` can find a signed-in user via
	Azure CLI or Visual Studio Code, or use a managed identity. The identity needs
	the appropriate Azure role on the Azure OpenAI resource or Foundry project.
	No long-lived API key is stored in these scripts.
