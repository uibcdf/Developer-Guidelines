import yaml

def print_hello():
    print("hello")
    pass

def get_versions():
    from ._version import get_versions as _get_versions
    return _get_versions()

def get_requirements():
    with open('./data/requirements.yaml') as file:
        requirements = yaml.load(file, Loader=yaml.FullLoader)
    return requirements

def list_files_in_data():
    import pkg_resources
    return pkg_resources.resource_listdir('test_uibcdf_library', 'data')

