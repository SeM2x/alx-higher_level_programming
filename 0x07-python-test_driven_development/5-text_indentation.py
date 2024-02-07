#!/usr/bin/python3
""" function that prints a text with 2 new
    lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """indentate a text

    Args:
        text: the text to indentate
    Raises:
        TypeError: if text is not a sting
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    lines = text.split('\n')
    new_lines = [line.strip() if line.startswith(' ') else line for line in lines]
    text = '\n'.join(new_lines)
    print(text, end="")
