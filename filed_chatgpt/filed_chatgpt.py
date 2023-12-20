"""Main module for filed_chatgpt."""

import argparse


def main():
    """Process command-line arguments, and run the program."""
    parser = __setup_argparse()
    args = parser.parse_args()
    print(f'Using model: {args.model} and output file: {args.output_file}')


def __setup_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='ChatGPT model',
                        default='gpt-3.5-turbo',
                        required=False)
    parser.add_argument('-k', '--api-key',
                        help='ChatGPT API key',
                        required=True)
    parser.add_argument('-o', '--output-file',
                        help='Chat output file in YAML/ Markdown format',
                        required=True)
    return parser


if __name__ == '__main__':
    main()
