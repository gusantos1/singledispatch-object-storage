import ibm_boto3
from dataclasses import dataclass
from functools import singledispatchmethod
from typing import BinaryIO
from azure.storage.blob import BlobServiceClient
from google.cloud import storage
from ibm_botocore.client import Config


@dataclass
class Gen2:
    binario: BinaryIO


@dataclass
class Gcp:
    binario: BinaryIO


@dataclass
class Ibm:
    binario: BinaryIO


class Despachante:
    @singledispatchmethod
    def enviar_dados(self):
        raise NotImplementedError('Não deve ser implementado')

    @enviar_dados.register(Gen2)
    def _(self, objeto, nome_bucket: str, nome_arquivo: str, **credenciais):
        dado = objeto.binario
        servico = BlobServiceClient(**credenciais)
        cliente = servico.get_blob_client(
            container=nome_bucket, blob=nome_arquivo
        )
        return cliente.upload_blob(dado)

    @enviar_dados.register(Gcp)
    def _(self, objeto, nome_bucket: str, nome_arquivo: str):
        dado = objeto.binario
        servico = storage.Client()
        cliente = servico.get_bucket(nome_bucket).blob(nome_arquivo)
        return cliente.upload_from_file(dado, rewind=True)

    @enviar_dados.register(Ibm)
    def _(self, objeto, nome_bucket: str, nome_arquivo: str, **credenciais):
        dado = objeto.binario
        cliente = ibm_boto3.client(
            's3',
            **credenciais,
            config=Config(signature_version='oauth'),
        )
        return cliente.upload_fileobj(dado, nome_bucket, nome_arquivo)
