import typing
from abc import ABCMeta

import pytest


def check_read_only(fields: typing.List[str], obj: ABCMeta):
    for field in fields:
        with pytest.raises(AttributeError):
            setattr(obj, field, "123")
