"""
IPython/Jupyter Notebook progressbar decorator for iterators.
Includes a default (x)range iterator printing to stderr.
Usage:
  >>> from tqdm_notebook import tnrange[, tqdm_notebook]
  >>> for i in tnrange(10): #same as: for i in tqdm_notebook(xrange(10))
  ...     ...
"""
# future division is important to divide integers and get as
# a result precise floating numbers (instead of truncated int)
from __future__ import absolute_import, division

# import compatibility functions and utilities
import sys

# to inherit from the tqdm class
from ._tqdm import tqdm
from ._utils import _range

if True:  # pragma: no cover
    # import IPython/Jupyter base widget and display utilities
    try:  # IPython 4.x
        import ipywidgets

        IPY = 4
    except ImportError:  # IPython 3.x / 2.x
        IPY = 32
        import warnings

        with warnings.catch_warnings():
            ipy_deprecation_msg = "The `IPython.html` package has been deprecated"
            warnings.filterwarnings("error", message=".*" + ipy_deprecation_msg + ".*")
            try:
                import IPython.html.widgets as ipywidgets
            except Warning as e:
                if ipy_deprecation_msg not in str(e):
                    raise
                warnings.simplefilter("ignore")
                try:
                    import IPython.html.widgets as ipywidgets  # NOQA
                except ImportError:
                    pass
            except ImportError:
                pass

    try:  # IPython 4.x / 3.x
        if IPY == 32:
            from IPython.html.widgets import HTML, HBox, IntProgress

            IPY = 3
        else:
            from ipywidgets import HTML, HBox, IntProgress
    except ImportError:
        try:  # IPython 2.x
            from IPython.html.widgets import HTML
            from IPython.html.widgets import ContainerWidget as HBox
            from IPython.html.widgets import IntProgressWidget as IntProgress

            IPY = 2
        except ImportError:
            IPY = 0
