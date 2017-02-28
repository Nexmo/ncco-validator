#!/usr/bin/env python

import json
from os.path import join as join_path, dirname

from jsonschema import validate, ValidationError
import pytest
from pytest import raises

VALID_FILES = [
    "russell",
    "connect-full",
    "connect-sip-endpoint",
    "connect-websocket-endpoint",
    "conversation-full",
    "input-full",
    "record-full",
    "stream-full",
    "talk-full",
]

INVALID_FILES = [
    "connect-invalid-eventmethod",
    "connect-invalid-eventtype",
    "connect-invalid-eventurl",
    "connect-invalid-from",
    "connect-invalid-limit",
    "connect-invalid-machinedetection",
    "connect-invalid-timeout",
    "connect-sip-invalid-uri",
    "connect-websocket-invalid-uri",
    "conversation-invalid-endonexit",
    "conversation-invalid-eventmethod",
    "conversation-invalid-eventurl",
    "conversation-invalid-musiconholdurl",
    "conversation-invalid-record",
    "conversation-invalid-startonenter",
    "input-invalid-eventmethod",
    "input-invalid-eventurl",
    "input-invalid-maxdigits",
    "input-invalid-submitonhash",
    "input-invalid-timout",
    "invalid-action",
    "missing-action",
    "record-invalid-beepstart",
    "record-invalid-endonkey",
    "record-invalid-endonsilence",
    "record-invalid-eventmethod",
    "record-invalid-eventurl",
    "record-invalid-format",
    "record-invalid-timeout",
    "stream-invalid-bargein",
    "stream-invalid-level",
    "stream-invalid-loop",
    "stream-invalid-streamurl",
    "talk-invalid-bargein",
    "talk-invalid-loop",
    "talk-invalid-text",
    "talk-invalid-voice",
    "talk-missing-text",
    "unknown-property",
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
