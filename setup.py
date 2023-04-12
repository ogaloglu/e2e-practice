from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements.

    Args:
        file_path (str): Path of the requirements.

    Returns:
        List[str]: List of requirements.
    """
    requirements = list()
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="e2e_practice_project",
    version="0.0.1",
    author="Onur Galoglu",
    author_email="onur.galoglu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    # install_requires=["pandas", "numpy", "seaborn"]
)
