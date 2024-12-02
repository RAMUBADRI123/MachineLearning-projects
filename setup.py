from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)-> List[str]:
    '''
    tHis will return requirments
    '''
    reqirments = []
    with open(file_path) as file_obj:
        reqirments = file_obj.readlines()
        reqirments=[req.replace("\n"," ")for req in reqirments]
        if Hypen_E_Dot in reqirments:
            reqirments.remove(Hypen_E_Dot)
    return reqirments
        
    
    

setup(
    name='mlproject'
    version='0.0.1'
    author='RamuBadri'
    author_email='ramubadri9@gmail.com'
    packages=find_packages()
    install_requires = get_requirements('requirements.txt')
    
    
)