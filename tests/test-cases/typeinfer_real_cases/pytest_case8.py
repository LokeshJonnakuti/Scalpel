"""
From pytest_unittest.py
"""

import sys
import traceback
import types
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generator,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

import _pytest._code
import pytest
from _pytest.compat import getimfunc, is_async_function
from _pytest.config import hookimpl
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Collector, Item
from _pytest.outcomes import exit, fail, skip, xfail
from _pytest.python import Class, Function, PyCollector
from _pytest.runner import CallInfo
from _pytest.scope import Scope


def setup(self) -> None:
    # A bound method to be called during teardown() if set (see 'runtest()').
    self._explicit_tearDown: Optional[Callable[[], None]] = None
    assert self.parent is not None
    self._testcase = self.parent.obj(self.name)  # type: ignore[attr-defined]
    self._obj = getattr(self._testcase, self.name)
    if hasattr(self, "_request"):
        self._request._fillfixtures()
