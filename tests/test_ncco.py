#!/usr/bin/env python

import json
from os.path import join as join_path, dirname

from jsonschema import validate, ValidationError
import pytest
from pytest import raises

VALID_FILES = [
    "russell",
]

INVALID_FILES = [
    "invalid-action",
    "missing-action",
]

schema = json.load(open('ncco-schema.json'))

fixtures_dir = join_path(dirname(__file__), "fixtures")

def fixture(name):
    path = join_path(fixtures_dir, f"{name}.json")
    return json.load(open(path))

def validate_fixture(name):
    return validate(fixture(name), schema)

@pytest.mark.parametrize("fixture_name", VALID_FILES)
def test_valid(fixture_name):
    validate_fixture(fixture_name)

@pytest.mark.parametrize("fixture_name", INVALID_FILES)
def test_invalid(fixture_name):
    with raises(ValidationError):
        validate_fixture(fixture_name)
