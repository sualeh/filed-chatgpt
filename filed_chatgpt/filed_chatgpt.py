"""Main module for filed_chatgpt."""

import argparse

from openai import OpenAI, OpenAIError


def main():
    """Process command-line arguments, and run the program."""
    args = get_args()
    __chat_loop(args)


def __chat_loop(args):
    user_prompt = 'When was the first moon landing?'
    reply = ''
    try:
        client = OpenAI(api_key=args['api_key'])
        chat_completion = client.chat.completions.create(
            model=args['model'],
            messages=[{'role': 'user', 'content': user_prompt}],
        )
        reply = chat_completion.choices[0].message.content
    except OpenAIError as e:
        reply = str(e)

    print(user_prompt)
    print(reply)


def get_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='ChatGPT model',
                        default='gpt-3.5-turbo',
                        required=False)
    parser.add_argument('-o', '--output-file',
                        help='Chat output file in YAML/ Markdown format',
                        required=True)

    args = parser.parse_args()

    arg_dict = {
        'model': args.model,
        'output_file': args.output_file
    }

    return arg_dict


if __name__ == '__main__':
    main()
