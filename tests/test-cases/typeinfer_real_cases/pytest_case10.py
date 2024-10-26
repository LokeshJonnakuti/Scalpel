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


def pytest_runtest_protocol(item: Item) -> Generator[None, None, None]:
    if isinstance(item, TestCaseFunction) and "twisted.trial.unittest" in sys.modules:
        ut: Any = sys.modules["twisted.python.failure"]
        Failure__init__ = ut.Failure.__init__
        check_testcase_implements_trial_reporter()

        def excstore(
            self, exc_value=None, exc_type=None, exc_tb=None, captureVars=None
        ):
            if exc_value is None:
                self._rawexcinfo = sys.exc_info()
            else:
                if exc_type is None:
                    exc_type = type(exc_value)
                self._rawexcinfo = (exc_type, exc_value, exc_tb)
            try:
                Failure__init__(
                    self, exc_value, exc_type, exc_tb, captureVars=captureVars
                )
            except TypeError:
                Failure__init__(self, exc_value, exc_type, exc_tb)

        ut.Failure.__init__ = excstore
        yield
        ut.Failure.__init__ = Failure__init__
    else:
        yield
