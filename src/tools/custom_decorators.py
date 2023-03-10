from . import __version__


def add_version(f):
    """
    Add the version of the tool to the help heading.
    :param f: function to decorate
    :return: decorated function
    """
    doc = f.__doc__
    f.__doc__ = "Version: v" + __version__ + "\n" + (doc or '')
    return f
