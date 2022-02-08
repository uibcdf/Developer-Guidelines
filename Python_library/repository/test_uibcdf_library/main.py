import pkg_resources
import yaml

def print_hello():
    print("hello")
    pass

def get_versions():
    from ._version import get_versions as _get_versions
    return _get_versions()

def get_requirements():
    file_path=pkg_resources.resource_filename('test_uibcdf_library','data/requirements.yml')
    with open(file_path) as file:
        requirements = yaml.load(file, Loader=yaml.FullLoader)
    return requirements

def list_files_in_data():
    return pkg_resources.resource_listdir('test_uibcdf_library', 'data')

