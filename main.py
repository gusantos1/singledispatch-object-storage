import os
from despachante import Despachante, Gen2, Gcp, Ibm
from dotenv import load_dotenv, find_dotenv


# Variáveis de ambiente
load_dotenv(find_dotenv())
ENV_AZURE_CONTA = os.environ.get('AZURE_CONTA1')
ENV_AZURE_CHAVE = os.environ.get('AZURE_CHAVE')
ENV_AZURE_BUCKET = os.environ.get('AZURE_BUCKET')
ENV_GCP_BUCKET = os.environ.get('GCP_BUCKET')
ENV_IBM_BUCKET = os.environ.get('IBM_BUCKET')
ENV_IBM_ENDPOINT = os.environ.get('IBM_ENDPOINT')
ENV_IBM_API_KEY_ID = os.environ.get('IBM_API_KEY_ID')
ENV_IBM_INSTANCE_CRN = os.environ.get('IBM_INSTANCE_CRN')


despachante = Despachante()

with open('exemplo.json', 'rb') as dado:
    despachante.enviar_dados(
        Gen2(dado),
        nome_bucket=ENV_AZURE_BUCKET,
        nome_arquivo='exemplo.json',
        account_url=ENV_AZURE_CONTA,
        credential=ENV_AZURE_CHAVE,
    )  # Enviar para Azure Blob Storage.

with open('exemplo.json', 'rb') as dado:
    despachante.enviar_dados(
        Gcp(dado), 
        nome_bucket=ENV_GCP_BUCKET, 
        nome_arquivo='exemplo.json'
    )  # Enviar para Google Cloud Storage.
    
with open('exemplo.json', 'rb') as dado:
    despachante.enviar_dados(
        Ibm(dado),
        nome_bucket=ENV_IBM_BUCKET,
        nome_arquivo='exemplo.json',
        ibm_api_key_id=ENV_IBM_API_KEY_ID,
        ibm_service_instance_id=ENV_IBM_INSTANCE_CRN,
        endpoint_url=ENV_IBM_ENDPOINT,
    )  # Enviar para IBM Cloud Storage.