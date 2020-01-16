import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="synbiopython",
    version="0.0.1",
    author="Global Biofundries Alliance",
    author_email="author@example.com",
    description="Python tools for Synthetic Biology.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Global-Biofoundries-Alliance/SynBioPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)