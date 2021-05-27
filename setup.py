import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hamtrack",
    version="0.0.1",
    author="Dave Morris",
    author_email="scubadam@gmail.com",
    description="Hamster Wheel tracking to influxDb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scubadam/hamtrack",
    project_urls={
        "Readme": "https://github.com/scubadam/hamtrack#readme",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['gpiozero~=1.6.2']
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
