import requests
import json
import argparse

def chat_with_gpt_api(messages):
    url = "https://openai80.p.rapidapi.com/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ADDKEYHERE",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

def main():
    parser = argparse.ArgumentParser(description="Interact with GPT-3.5 Turbo API")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-p", "--prompt", type=str, help="Input prompt to send to GPT-3.5 Turbo API")
    input_group.add_argument("-f", "--file", type=str, help="Path to a text file containing the input prompt")
    parser.add_argument("-o", "--output", type=str, help="Path to a text file to save the output content")
    parser.add_argument("-c", "--continuous", action="store_true", help="Enable continuous conversation mode")

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            prompt = file.read()
    else:
        prompt = args.prompt

    messages = [{"role": "user", "content": prompt}]

    while True:
        response_text = chat_with_gpt_api(messages)
        response_json = json.loads(response_text)
        content = response_json['choices'][0]['message']['content']

        print(content)
        messages.append({"role": "assistant", "content": content})

        if args.output:
            with open(args.output, 'a') as output_file:
                output_file.write(content + '\n')

        if not args.continuous:
            break

        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

if __name__ == "__main__":
    main()
