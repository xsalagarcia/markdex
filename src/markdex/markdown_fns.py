"""
TOC manipulation functionalities.
"""

import re
from pathlib import Path


def get_index(path: Path) -> list[str]:
    """
    Open the Markdown file and return the index in a list[str] format.
    :param path:
    :return:
    """
    index = list[str]()

    with open(path, encoding="utf-8") as file:

        in_code = False
        """Flag the line is inside a code block"""

        for line in file:
            line = line.strip()

            split_line = line.split(sep=" ", maxsplit=1)

            if line.lstrip(">").startswith("```"):
                in_code = not in_code

            if in_code:
                continue

            if re.fullmatch(r"#{1,6}", split_line[0]):  # This line is a title.
                link = split_line[1].lower().replace(" ", "-")  # Whitespaces are '-'
                link = re.sub(r"[^a-z0-9-àáèéìíòóùúüöï]", "", link)  # Remove all that is not this set of chars.
                link = f'#{link}'
                index.append(" " * ((len(split_line[0]) - 1) *2)
                             + f"* [{split_line[1].removesuffix(chr(10))}]"
                             + f"({link})")
        return index


def replace_or_create_toc(old_content: str, toc_content: str) -> str:
    """
    Take old content (all content) and replace TOC or create it.
    :param old_content:
    :param toc_content: if a list, use ``toc_content="\n".join(list_of_strings)``
    :return: The new content with a new TOC.
    """

    existence_pattern = r"<!-- TOC -->.*<!-- TOC -->"
    replacing_pattern = r"(<!-- TOC -->\s*).*?(\s*<!-- TOC -->)"

    if bool(re.search(existence_pattern, old_content, re.DOTALL)):
        toc_replacement = rf"\1{toc_content.rstrip()}\2"
        return re.sub(replacing_pattern, toc_replacement, old_content, flags=re.DOTALL)

    else:
        return f"<!-- TOC -->\n{toc_content}\n<!-- TOC -->\n{old_content}"