# responsibe in creating my ml application as package  and these packge anyone can use it by just installing it
from setuptools import find_packages,setup
from typing import List

FILE_PATH="requirements.txt"
HYPEN_E_DOT="-e ."   # auto matically trigger setup.py

def get_req()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(FILE_PATH) as f :
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

  



setup(
name='ml_project',
version="0.0.1" ,
author='Prikshit7766' ,
packages=find_packages(),  #  seach for how many folder you are having __init__.py file and if the file is there then it will consider that folder as package
install_requires= get_req()

)