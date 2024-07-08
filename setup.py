from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filename: str)->List[str]:
    """
    Read the requirements file and return list of requirements
    """
    requirements=[]
    with open(filename, 'r') as file_object:
        requirements = file_object.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements ]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='ML_Project',
    version='0.0.1',
    author='Sourabh Patil',
    author_email='sasuke410206@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)