#!/bin/bash

python3  regex_generator.py
uglifyjs main.js > main.min.js
uglifyjs regex_rules.js > regex_rules.min.js
python3 -m http.server
