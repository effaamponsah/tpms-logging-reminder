import pytest
from mail_sender import addnumbers


def test_answer():
    assert addnumbers(1,2) == 3