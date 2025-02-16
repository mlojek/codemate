# codemate
Codemate is a LLM-powered CLI tool to help software developers with repetitive and boring tasks. Codemate allows you to refactor your code, add docstrings, insert code snippets and explain hard to understand fragments of code.

## Installation
Firstly, clone this repository. In a python environment run:
```
make install
```
This will install all necessary dependencies. Python 3.11 and above is required.

## Create configuration
Codemate can be configured by a `~/.codemate` config file. It holds user's LLM API keys. The user has to create it by hand. Then, paste the following config template and add your keys:
```.env
# gemini
GEMINI_API_KEY = 'your api key goes here'
GEMINI_FAV_MODEL = 'name of the default model'

# openai
OPENAI_API_KEY = 'your api key goes here'
OPENAI_FAV_MODEL = 'name of the default model'
```

## Using codemate
After installation, codemate can be called by it's CLI interface:
```
TODO
```
TODO examples