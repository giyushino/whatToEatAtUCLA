# whatToEatAtUCLA

Welcome to What2Eat@UCLA! This repository is meant to help students choose what dining hall at UCLA to eat at. After all, there are so many great options! However, for those who are also more health conscious or worry about allergies, this project can help you stay safe, healthy, and fit! 
Here's a preview of this project in action:

https://github.com/user-attachments/assets/a5dbed0d-e89b-4b99-b16d-37ad5f31705b



This project currently relies heavily on Deepseek, so you will need an API key. However, there are plans to have this project run on lightweight, open-source LLMs and use cosine similarity to retain current capabilities without spending money. 

To set up this project, clone the project and create a new Anaconda environment

```sh
conda create -n <my-env>
pip install -e .
pip install -r requirements.txt
```

## Run this code
Navigate to /whatToEatAtUCLA/scripts/main.py and enter your API key, replacing the placeholder 'YOUR KEY HERE'

```python
from scripts.webscraper import access_html, parse 
from scripts.model import deepseek_chat
import os 

#*******************************
OPENAI_API_KEY = 'YOUR KEY HERE'
#*******************************
```

In your conda environment, cd to /whatToEatAtUCLA/scripts/ and run python main.py. 
Have fun!


