from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description =f.read()

setup(
    name="src",
    version="0.0.1",
    author="srinivasaragavan",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Srinivasaragavan/myrepodvc.git",
    author_email="srinimuniappan@yahoo.co.in",
    #packages=setuptools.find_packages()
    packages=["src"],
    python_requires ='>=3.7',
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]

)