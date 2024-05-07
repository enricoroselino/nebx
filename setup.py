import pathlib
import setuptools

setuptools.setup(
    name="nebx",
    version="0.1.0",
    description='nebx is a python "Swiss Army knife" to orchestrate existing python packages, reducing boilerplate codes',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/enricoroselino/nebx",
    author="Enrico Roselino",
    author_email="roselino.dev@gmail.com",
    license="MIT",
    project_urls={
        "Source": "https://github.com/enricoroselino/nebx",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Intended Audience :: Science/Research",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.11,<3.13",
    install_requires=[
        "schedule>=1.2.1",
        "httpx>=0.27.0",
        "random_user_agent>=1.0.1"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True
)
