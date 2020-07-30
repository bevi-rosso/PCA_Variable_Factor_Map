import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="variable-factor-map-Huy-Bui", # Replace with your own username
    version="0.0.3",
    author="Huy Bui",
    author_email="williamhuybui@gmail.com",
    description="Variable Factor Map",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/williamhuybui/PCA_Variable_Factor_Map",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)