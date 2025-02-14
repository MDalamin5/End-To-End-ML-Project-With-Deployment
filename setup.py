from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT="-e ."
# def get_requirements(file_path:str)->List[str]:
#     """
#     This function will return the list of requirements
#     """
#     requirements=[]
#     with open(file_path, 'r') as file_obj:
#         requirements=file_obj.readline()
#         requirements=[req.replace("\n","") for req in requirements]
        
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()  # Read all lines, not just one!
        requirements = [req.strip() for req in requirements]  # Remove whitespace and newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='generic_ml_project',
    version="0.0.1",
    author='Al Amin',
    author_email="nsuer.alamin@gamil.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)