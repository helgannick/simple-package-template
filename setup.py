from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_vendas",
    version="0.0.1",
    author="Marcos Barbosa",
    author_email="Helgannnick@gmail.com",
    description="package vendas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/helgannick/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)