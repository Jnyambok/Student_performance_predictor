from setuptools import find_packages,setup
from typing import List

##constant for /e in requirements.txt
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this function return list of reqs
    '''
    requirements =[]
    with open(file_path) as file_obj:

        requirements = file_obj.readlines()
        requirements = [req.replace ("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



##metadata
setup(
name='mlproject',
version='0.0.1',
author='Jnyambok',
author_email='juliusnyambok14@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)