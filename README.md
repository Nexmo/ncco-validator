# NCCOCheck

This is a tool that uses json-schema to validate a series of NCCO objects. The aim is that it
can be used in libraries that assist with the webhook side of Nexmo integrations, or with
a web-based tool for writing NCCOs.

The tests are in python3, but the real content is the [ncco-schema.json](ncco-schema.json) file, which should work with any json-schema v4 compliant library.
