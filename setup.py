import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dehumanizer",
    version="0.0.2",
    author="Orlando Diaz",
    author_email="orlandodiaz.dev@gmail.com",
    description="Dehumanize number strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orlandodiaz/dehumanizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['']

)