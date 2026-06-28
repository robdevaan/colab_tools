import IPython.display as ipd
from IPython.core.magic import Magics, magics_class, line_magic


@magics_class
class EnhancedDisplay(Magics):
    @line_magic
    def markdown(self, line):
        """Immediately display line content in IPython Markdown form."""
        ipd.display(ipd.Markdown(line))


def load_ipython_extension(ipython):
    """
    Register to IPython to allow loading through `%load_ext` or similar commands.
    """
    ipython.register_magics(EnhancedDisplay)
