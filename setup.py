from setuptools import find_packages, setup

setup(
    name="network_security",          # the package name you want
    version="0.0.1",
    author="Samyadeep",
    author_email="sahasamyadeep@gmail.com",
    description="End-to-end MLOps project for network security",
    packages=find_packages(),         # this will include network_security and subpackages
    install_requires=[
        # put your dependencies here, or read from requirements.txt
        # "pandas",
        # "scikit-learn",
        # "fastapi",
    ],
)
