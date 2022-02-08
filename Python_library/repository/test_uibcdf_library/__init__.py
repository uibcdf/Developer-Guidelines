"""
Test_UIBCDF_Library
This must be a short description of the project
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# Add imports here
from .main import print_hello
from .main import get_versions
from .main import get_requirements
from .main import list_files_in_data

