"""Main module for filed_chatgpt."""

import argparse

from dialog_turns import DialogTurns
from message import Message
from openai import OpenAI, OpenAIError
from openai.types.chat import ChatCompletion


def main():
    """Process command-line arguments, and run the program."""
    args = get_args()
    dialog_turns = DialogTurns(args['model'])
    __chat_loop(dialog_turns)
    dialog_turns.serialize(args['output_file'])


def __chat_loop(dialog_turns: DialogTurns):
    while True:
        user_prompt = input('?: ')
        if user_prompt.lower() in ['exit', 'quit']:
            break  # Exit the loop
        dialog_turns.add_message(Message.from_prompt(user_prompt))
        completion: str = complete(dialog_turns)

        print(completion)
        print()


def complete(dialog_turns: DialogTurns) -> str:
    try:
        client = OpenAI()
        chat_completion: ChatCompletion = client.chat.completions.create(
            model=dialog_turns.model,
            messages=dialog_turns.messages()
        )
        dialog_turns.add_message(Message.from_completion(chat_completion))
        reply = chat_completion.choices[0].message.content
    except OpenAIError as e:
        reply = str(e)

    return reply


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
