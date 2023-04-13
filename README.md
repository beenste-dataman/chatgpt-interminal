# chatgpt-interminal

usage: gpt-gosh.py [-h] (-p PROMPT | -f FILE) [-o OUTPUT] [-c]

Interact with GPT-3.5 Turbo API

optional arguments:
 * -h, --help            show this help message and exit
 * -p PROMPT, --prompt PROMPT
                        Input prompt to send to GPT-3.5 Turbo API
 * -f FILE, --file FILE  Path to a text file containing the input prompt
 * -o OUTPUT, --output OUTPUT
                        Path to a text file to save the output content
 * -c, --continuous      Enable continuous conversation mode
  
  
---

examples:

python gpt_api_tool.py -f input.txt -o output.txt --continuous


python gpt_api_tool.py -f input.txt -o output.txt --continuous
