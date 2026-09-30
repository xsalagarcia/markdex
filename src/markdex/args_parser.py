"""
Parsing CLI arguments functionality.
"""

import argparse
from pathlib import Path
from typing import NamedTuple, Optional


class ScriptArgs(NamedTuple):
    file: Path
    edit_file: bool
    output: Path | None

def check_and_get_path(file: str) -> Path:
    """
    Return Path object (absolute).
    :param file:
    :return:
    """
    file_path = Path(file).resolve()
    if not file_path.is_file():
        raise argparse.ArgumentTypeError(f"Path {file_path} is not a file")
    return file_path


def parse_args() -> ScriptArgs:
    parser = argparse.ArgumentParser(
        prog="markdex",
        description="Markdown TOC creator.")
    parser.add_argument("file", help="Markdown file name",
                        type=check_and_get_path)

    parser.add_argument("-e", "--edit",
                        help="If present, the file will be edited. If not, the TOC will be printed.",
                        dest="edit_file",
                        action="store_true")

    parser.add_argument("-o", "--output",
                        dest="output",
                        type=Path)

    args = parser.parse_args()
    return ScriptArgs(**vars(args))