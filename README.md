# git-ready

## What is ```git ready```?
3 new custom git commands that help you format, document and get you ready to commit your staged file with good documentation and idiomatic language-specific rules

## How to Get Started?

1) Clone the repository and use the absolute path in the given input field below.
```
export PATH=$PATH:"${ABSOLUTE_CLONE_LOCATION}/git-formatting-documentation-command"
```

2) Run all the commands below to get the new git commands; make sure to change the fields below to the command you want to use. We currenlty support: ```format, doc & ready```
```
sudo mv git-<custom_command> /usr/local/bin/
sudo chmod a+x git-<custom_command>
```
3) You can edit the functionality of the LLM, by choosing your own in the ```doc.py``` file, if you would like to use other LLMs (not compatible with OpenAI). If not, make sure to define your API Keys for OpenAI compatible chat-completion objects in the ```.env``` file, in the following fields:
```
your_api = os.getenv("YOUR_API_KEY")
your_model = "YOUR_MODEL"
your_base_url = "https://YOUR_BASE_URL_PATH"
```

## Use cases:
This is how you can use each of the commands to execute specific tasks

### ```git format```:
Used to format code of all latest staged files by utilizing language-specifc formatters for all files. Currently supports: C/C++, Python, Typescript, Javascript, Rust, Go & Java

### ```git doc```:
Used to add documentation to all latest code files staged for a commit. Uses Groq to call DeepSeek API in dependency order to maximize code documentation properly. Creates a terminal side-by-side diff to approve/reject changes & comments when given the ```-c``` flag, else creates another an adjacent documented file. 

### ```git ready```:
Performs both ```git format``` and  ```git ready``` and then performs ```git commit``` to stage all files being tracked. Can utilize ```-m``` flag with a message to give a commit message and ```-c``` flag for ```git doc``` related functionality.
