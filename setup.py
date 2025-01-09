from setuptools import setup, find_packages

setup(
    name="whatToEatAtUCLA",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.8.0",
        "beautifulsoup4==4.12.3",
        "bs4==0.0.2",
        "certifi==2024.12.14",
        "charset-normalizer==3.4.1",
        "colorama==0.4.6",
        "distro==1.9.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "jiter==0.8.2",
        "openai==1.59.5",
        "pydantic==2.10.4",
        "pydantic_core==2.27.2",
        "requests==2.32.3",
        "sniffio==1.3.1",
        "soupsieve==2.6",
        "tqdm==4.67.1",
        "typing_extensions==4.12.2",
        "urllib3==2.3.0",
    ],
    dependency_links=[
        'https://github.com/giyushino/whatToEatAtUCLA/tarball/8e2e774b0a9f76c422951f59c6d97e29ca8eb0e7#egg=whatToEatAtUCLA'
    ],
)
