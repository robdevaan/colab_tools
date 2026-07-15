import IPython.display as ipd


def md(c, *ac, mode="auto"):
    """Display content as Markdown in IPython, more specifically suited for Google Colab notebooks.

    Args:
    ---
        c (str): Content to be displayed as Markdown.
        *ac: Additional content to be displayed as Markdown. Optional.
        mode (str, optional): Display mode.
        Mode 'auto', or 'a', displays a single item as one line of Markdown and multiple items as multiline Markdown where each line ends with two spaces followed by a linebreak.
        Mode 'paragraphs', or 'p', displays each item on a line ending with two spaces and double linebreaks, effectively generating a new paragraph for each item.
        Mode 'list', or 'l', displays one or more items as list, preceding each line with "- " and ending each line with two spaces followed by a linebreak. Does not support nested lists.
        Defaults to 'auto'.

    Description:
    ---
        Function allows providing a single item of content as one string, or multiple string representing additional content.
        String can be f-string containing variables.
        Uses IPython.display and IPython.display's Markdown under the hood.
        Tip: when passing a sequence or array it must be unpacked into individual items.
    """
    match mode:
        case "auto" | "a":
            if len(ac) == 0:
                ipd.display(ipd.Markdown(c + "  \n"))
            else:
                ipd.display(ipd.Markdown(c + "  \n" + "  \n".join(ac) + "  \n"))
        case "paragraphs" | "p":
            if len(ac) == 0:
                ipd.display(ipd.Markdown(c + "  \n\n"))
            else:
                ipd.display(ipd.Markdown(c + "  \n\n" + "  \n\n".join(ac) + "  \n"))
        case "list" | "l":
            if len(ac) == 0:
                ipd.display(ipd.Markdown("- " + c + "  \n"))
            else:
                ipd.display(
                    ipd.Markdown("- " + c + "  \n- " + "  \n- ".join(ac) + "  \n")
                )
        case _:
            raise ValueError(
                f"value {mode} is not recognized as a valid value for the 'mode' keyword argument"
            )
