from setuptools import find_packages,setup
from typing import List 


HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines from the file
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove '-e .' if it's in the requirements
    return requirements
      

setup(
name='Machine-Learning-Project',
version='0.0.1',
author='Mahesh',
author_email='maheshgmarar1993@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)