""" lambdata - a collection of Data Science helper functions
"""

import setuptools

REQUIRED=['numpy','python']

with open('README.md','r') as fh:
    LONG_DESCRIPTION=fh.read()

setuptools.setup(
    name="lambdatadanh",
    version="0.0.18",
    author="danh",
    description="A collection of Data Science Helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/danhorsley/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
