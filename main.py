"""Main module for filed_chatgpt."""

from filed_chatgpt.dialog_turns import DialogTurns
from filed_chatgpt.filed_chatgpt import chat_loop, get_args


def main():
    """Process command-line arguments, and run the program."""
    args = get_args()
    dialog_turns = DialogTurns(args["model"])
    chat_loop(dialog_turns)
    dialog_turns.serialize(args["output_file"])


if __name__ == "__main__":
    main()
