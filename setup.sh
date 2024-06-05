#!/bin/bash

# Check if pyenv is installed
if ! command -v pyenv &> /dev/null
then
    echo "pyenv could not be found, please install pyenv first."
    exit
fi

# Set local Python version
pyenv install -s 3.8.19
pyenv local 3.8.19

# Create virtual environment
python -m venv venv

echo "Virtual environment created. Run 'source venv/bin/activate' to activate."
