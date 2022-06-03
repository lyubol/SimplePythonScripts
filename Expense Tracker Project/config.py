from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url="https://lirkov-keyvault.vault.azure.net/",
    credential=credential
)

secret = client.get_secret("lirkov-azure-sqldb-key")

