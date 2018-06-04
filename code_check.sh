#!/bin/bash

pep8 ./typedclass --ignore=E401,E122,E126,E127,E128,E124,E501,E241

pyflakes ./typedclass

find ./typedclass/ -name '*.py' | grep -v 'test_' | grep -v 'contracts_typedclass' | xargs pcregrep --multiline --line-number '(?<!@contract)\n[ \t]*def (?!test.*\((\n[ \t]*)?self)(?!setup_ota\(self\))(?!setUp\(self\))(?!handle\(self\))'
