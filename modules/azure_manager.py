import os

from azure.storage.blob import (
    BlobServiceClient,
    BlobClient,
    ContainerClient,
    __version__)
from dotenv import load_dotenv
load_dotenv()


class AzureManager(object):
    """ Class to Manage Images for Azure """

    def upload_image(
            self,
            file_name=None,
            path=None,
            container_name=None):
        """ Upload an Image to Azure as blob """
        try:

            connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
            blob_service_client = BlobServiceClient.from_connection_string(
                connect_str)
            print(f'\nUploading to Azure Storage as blob:\n\t {file_name}')
            with open(f'{path}/{file_name}', 'rb') as data:
                blob_client = blob_service_client.get_blob_client(
                    container=container_name,
                    blob=file_name)
                blob_client.upload_blob(data, overwrite=True)
            return 1
        except Exception as e:
            print(str(e))
            return 0

    def upload_dir_image(
            self,
            dir_path=None,
            container_name=None):
        """ Uploads the contents of a dir to azure container. """
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        try:
            for root, dirs, files in os.walk(dir_path):
                for filename in files:
                    file_name = filename.replace(' ', '')
                    print(
                        f'\nUploading to Azure Storage as blob:\n\t {file_name}')
                    with open(f'{root}/{filename}', 'rb') as data:
                        blob_client = blob_service_client.get_blob_client(
                            container=container_name,
                            blob=file_name)
                        blob_client.upload_blob(data, overwrite=True)
            return 1
        except Exception as e:
            print(str(e))
            return 0

    def list_blobs_names(self, container_name=None):
        """ List all the blobs names in a container """
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        container_client = blob_service_client.get_container_client(
            container_name)
        list_blobs = []
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            list_blobs.append(blob.name)
        return list_blobs

    def get_blob_url(
            self,
            container_name=None,
            file_name=None):
        base_url = os.getenv('AZURE_STORAGE_URL')
        return f'{base_url}{container_name}/{file_name}'
