import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easychart",
    version="0.1.3",
    author="david.schenck@outlook.com",
    author_email="david.schenck@outlook.com",
    description="Highcharts meets python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://easychart.readthedocs.io/en/latest/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas","numpy","easytree"],
    include_package_data=True
)
