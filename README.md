# whatToEatAtUCLA

Welcome to What2Eat@UCLA! This repository is meant to help students choose what dining hall at UCLA to eat at. After all, there are so many great options! However, for those who are also more health conscious or worry about allergies, this project can help you stay safe, healthy, and fit! 

Here's a preview of this project in action:

https://github.com/user-attachments/assets/7787bc2f-342b-4f43-ad96-e004a192ab2c

This project currently relies heavily on Deepseek, so you will need an API key. I will provide one if necessary, However, there are plans to have this project run on lightweight, open-source LLMs and use cosine similarity to retain current capabilities without spending money. 

## Setting up with Anaconda  
To set up this project, clone the project and create a new Anaconda environment

```sh
conda create -n <my-env>
pip install -e .
```

## Setting up with venv 
```sh
python -m venv .venv
.venv\Scripts\activate 
pip install -e .
```

### Run this code
Users can manually cd to /whatToEatAtUCLA/scripts/main.py and enter their API key, replacing the placeholder 'YOUR KEY HERE'. It is recommended that users create a .env file and enter their API key there. 

```python
from openai import OpenAI
import os
from scripts.reformat import create_menus, split
from dotenv import load_dotenv
load_dotenv()

# You can set OPENAI_API_KEY to the actual API if you don't want to set up a .env file 
#*******************************
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
********************************


In your conda environment, cd to /whatToEatAtUCLA/scripts/ and run python main.py. 
Have fun!


