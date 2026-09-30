import unittest
from pathlib import Path

from markdex.markdown_fns import get_index, replace_or_create_toc


class TestMarkdownFns(unittest.TestCase):
    def test_get_index(self):
        path = Path(__file__).parent.joinpath("markdown_test.md")
        index = get_index(path)
        self.assertEqual(index[0], "* [Ai,xò és, un `<títol.>`.](#això-és-un-títol)")
        self.assertEqual(index[1], "  * [*un* (altre) [títol]](#un-altre-títol)")


    def test_replace_or_create_toc(self):
        path = Path(__file__).parent.joinpath("markdown_test.md")

        with path.open("r", encoding="utf-8") as f:
            content = f.read()

        # visual check.
        print(replace_or_create_toc(old_content=content, toc_content="a e i o u"))