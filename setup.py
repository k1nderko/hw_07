from setuptools import setup, find_namespace_packages

setup(
    name='Sorting Folders',
    version='0.0.1',
    description='Clean trash folders',
    url='https://github.com/k1nderko/hw_06_modul',
    entry_points={'console_scripts': [
        'file-sorting=file_sorting.sorting:main']}

)
