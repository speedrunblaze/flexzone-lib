
from setuptools import setup, find_packages

setup(
    name="flexzone",
    version="0.1",
    author="Seu Nome",
    author_email="seunome@exemplo.com",
    description="A flexible library for file management tasks",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SeuUsuario/flexzone",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
    