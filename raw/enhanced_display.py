import IPython.display as ipd
from IPython.core.magic import Magics, magics_class, line_magic


@magics_class
class EnhancedDisplayMagics(Magics):
    @line_magic
    def md(self, line):
        """Immediately display line content in IPython processed as Markdown."""
        ipd.display(ipd.Markdown(line))

    @line_magic
    def html(self, line):
        """Immediately display line content in IPython processed as HTML."""
        ipd.display(ipd.HTML(line))

    @line_magic
    def ltx(self, line):
        """Immediately display line content in IPython processed as Latex. Line should not include Latex delimiters (i.e. dollar sign characters)."""
        ipd.display(ipd.Latex(line))


def load_ipython_extension(ipython):
    """
    Register to IPython to allow loading through `%load_ext` or similar commands.
    """
    ipython.register_magics(EnhancedDisplayMagics)
