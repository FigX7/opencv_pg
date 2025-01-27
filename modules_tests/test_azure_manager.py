import pytest
import os
from modules.azure_manager import AzureManager
from PIL import Image

@pytest.fixture
def azure_manager(request):
    """Create tester object"""
    return AzureManager()


def test_list_blobs(azure_manager):
    list_blobs = azure_manager.list_blobs('tests')
    assert 1 <= len(list_blobs)


def test_upload_blobs(azure_manager):
    result = azure_manager.upload_dir_image(
        './modules_tests/assets/test_upload_dir',
        'tests')
    assert 1 == result


def test_get_blob_url(azure_manager):
    base_url = os.getenv('AZURE_STORAGE_URL')
    container_name = 'tests'
    file_name = 'armas(2).jpg'
    test_url = azure_manager.get_blob_url(container_name, file_name)
    expected_url = f'{base_url}{container_name}/{file_name}'
    assert expected_url == test_url


def test_upload_image(azure_manager):
    image = Image.open('./modules_tests/assets/test_upload_dir/armas.jpg')
    container_name = 'tests'
    result = azure_manager.upload_image(image, container_name)
    assert 1 == result
