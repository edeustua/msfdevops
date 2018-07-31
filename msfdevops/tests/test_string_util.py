from msfdevops import *
import pytest


def test_empty():
    assert string_util.title_string("") == "", 'Empty failed'

def test_str_type():
    with pytest.raises(TypeError):
        string_util.title_string([1, 2, 3])

    with pytest.raises(TypeError):
        string_util.title_string(3)


@pytest.mark.parametrize("in_str, out_str", [
    ("This DddSS lol", "This Dddss Lol"),
    ("my BROTHER likes CoFfEe", "My Brother Likes Coffee"),
    ("coupled-cluster theory with singles, doubles, and triples",
        "Coupled-cluster Theory With Singles, Doubles, And Triples")
    ])

def test_title(in_str, out_str):
    assert string_util.title_string(in_str) == out_str
