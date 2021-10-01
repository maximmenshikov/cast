#!/bin/bash
# Apply formatting rules to all project files

export TOP_DIR="$(cd "$(dirname "$(which "$0")")"/.. ; pwd -P)"


pushd "${TOP_DIR}/cast" > /dev/null
autopep8 -i *.py
popd > /dev/null