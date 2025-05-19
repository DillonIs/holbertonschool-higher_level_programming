#!/usr/bin/python3
"""Function that prints a text with 2 new lines after characters
Characters:
. ? and :
text_indentation prints a text with conditions
"""


def text_indentation(text):
    """Variable:
    text (str): string being examined

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for sep in ".:?":
        text = (sep + "\n\n").join(
            [line.strip(" ") for line in text.split(sep)])

    print(text, end="")
