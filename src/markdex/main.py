from markdex.args_parser import parse_args
from markdex.markdown_fns import get_index, replace_or_create_toc


def main():
    """
    Entry point.
    :return:
    """
    script_args = parse_args()
    index = get_index(script_args.file)

    if script_args.output is not None:
        with open(script_args.output, "f") as file:
            old_content = file.read()
        with script_args.output.open("w", encoding="utf-8" ) as f:
            f.write(replace_or_create_toc(old_content=old_content, toc_content="\n".join(index)))
    elif script_args.edit_file:
        with open(script_args.file, "r") as file:
            old_content = file.read()
        with script_args.file.open("w", encoding="utf-8" ) as f:
            f.write(replace_or_create_toc(old_content=old_content, toc_content="\n".join(index)))
    else:
        for entry in index:
            print(entry)



if __name__ == "__main__":
    main()