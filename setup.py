from setuptools import find_packages,setup
from typing import List

HYPE_DOT="-e ."

def get_requirements(filename:str)->List[str]:
    requirements=[]

    with open(filename) as f:
        requirements=f.readlines()

        requirements=[req.replace("\n","")for req in requirements]

        if HYPE_DOT in requirements:
            requirements.remove(HYPE_DOT)


setup(
    name="iris",
    version="0.0.1",
    author="anbu",
    author_mail="anbarasanpm9@gmail.com",
    package=find_packages(),
    install_requires=get_requirements("requirements.txt")

)