# pylint:disable=missing-module-docstring,missing-function-docstring

import smoketest.hello as hello


def test_say_hello_says_hello_to_provided_name():
    assert hello.say_hello("friend") == "hi, friend"
