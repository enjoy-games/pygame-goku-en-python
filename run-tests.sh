#!/bin/bash
set -x # show executed commands
set -u # exit when unset variable is used
set -e # exit when expression fails
set -E # forward <ERR> signal properly to trap
set -o pipefail # exit when any command in a pipe fails

# Get directory containing the script
readonly DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# Get path to python3 command and execute it
readonly PYTHON3='/usr/bin/env python3' # path depends on installation method

# Check that code style follows pep8
find $DIR -name "*.py" -exec $PYTHON3 -m pycodestyle --verbose --show-source \
  --show-pep8 --max-line-length=79 --max-doc-length=72 {} +

# Run unit tests with test discovery
cd $DIR # The script could have been executed from another directory
$PYTHON3 -m unittest --verbose
