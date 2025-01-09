# whatToEatAtUCLA

Welcome to What2Eat@UCLA! This repository is meant to help students choose what dining hall at UCLA to eat at. After all, there are so many great options!

This project currently relies heavily on Deepseek, so you will need an API key. However, there are plans to have this project run on lightweight, open-source LLMs, as well as using cosine similarity (explained more at the end).

To set up this project, clone the project and create a new Anaconda environment

```sh
conda create -n <my-env>
pip install -r .
pip install -e .
```

## Run this code
Navigate to whatToEatAtUCLA\scripts\main.py and enter in your API key 

```python
from scripts.webscraper import access_html, parse 
from scripts.model import deepseek_chat
import os 

#****************************
OPENAI_API_KEY = 'YOUR KEY HERE'
#*******************************
