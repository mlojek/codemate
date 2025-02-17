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

## Functionalities
Codemate allows for a few useful actions to be done:  
🔧 `refactor` - Refactor the source code.  
🧑‍🏫 `explain` - Add explainatory comments.  
📖 `document` - Add docstrings and typehints.  
🪄 `insert` - Create new piece of code according to comments.  

## How to use codemate
After installation, codemate can be called by it's CLI interface:
```
usage: python -m codemate [-h] [--from_line FROM_LINE] [--to_line TO_LINE] [--api {gemini,openai}] [--model MODEL] [--inplace] {refactor,explain,document,insert} source_file

Codemate: LLM-powered software developer assistant.

positional arguments:
  {refactor,explain,document,insert}
                        Action that the assistant should take.
  source_file           Path to the source file to work on.

options:
  -h, --help            show this help message and exit
  --from_line FROM_LINE
                        The line number (starting from 0) in the source file to start from.
  --to_line TO_LINE     The line number (starting from 0) in the source file to end before (this line is not included).
  --api {gemini,openai}
                        Which LLM API to use.
  --model MODEL         Name of LLM to use.
  --inplace             If used the result will be pasted into the source file instead of the console.
```

## Examples
You will find `test.py` file in this repository to try out codemate.  
To add `divide` function according to comments, run:
```
python -m codemate insert test.py --from_line 11 --to_line 14 --inplace
```
Then to refactor the whole script:
```
python -m codemate refactor test.py --inplace
```
Add docstrings and typehints:
```
python -m codemate document test.py --inplace
```
Finally, if you don't understand what the script does, add explainatory comments:
```
python -m codemate explain test.py --inplace
```
