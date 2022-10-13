#!/bin/bash
##
## Runs a few commands to initialize a python virtual environment and download the required packages for nickjgrahamcom.
##

requiredPythonVersion="3.10"

# Test to make sure Python is installed before we bother doing anything else.

pyVersion=$(python --version) || (echo "Unable to find python. Make sure python $requiredPythonVersion is installed and included in your PATH." && exit 1)

# Split out the actual version number from the command output

pyVersion=($pyVersion)
pyVersion=${pyVersion[1]}

# Split out the major/minor/patch numbers

pyVersion=(`echo $pyVersion | tr '.' ' '`)
requiredPythonVersion=(`echo $requiredPythonVersion | tr '.' ' '`)

# Make sure Python is at a high enough version

# Major version

if test ${pyVersion[0]} -lt ${requiredPythonVersion[0]}
then
    echo "Python major version is lower than " + ${requiredPythonVersion[0]} + " (is " + ${pyVersion[0]} + "). Please upgrade and try again." && exit 1
fi
# Minor version
if test ${pyVersion[1]} -lt ${requiredPythonVersion[1]}
then
    echo "Python minor version is lower than " + ${requiredPythonVersion[1]} + " (is " + ${pyVersion[1]} + "). Please upgrade and try again." && exit 1
fi

# Prompt user to make sure they actually want to create the virtual environment

echo "This script creates a python virtual environment called 'venv' and packs it full of everything you need to run the nickjgrahamcom application."
echo "Are you sure you want to do this?"

if [ -d "venv" ]
then
    echo "'venv' already exists. Make sure you're okay with overwriting it."
fi

echo "Continue? (y/N)"
read continue

if [ "$continue" = "y" ]
then
    # Delete the old 'venv' directory if it already exists
    if [ -d "venv" ]
    then
        echo "Deleting old environment..."
        rm -rf venv
    fi
    echo "Creating virtual environment..."
    python -m venv venv
    echo "Creating symlink..."
    ln -sf venv/bin/activate activate
    ln -sf venv/bin/activate.fish activate.fish
    echo "Activating virtual environment..."
    source activate
    echo "Upgrading pip..."
    pip install --upgrade pip wheel
    echo "Installing packages..."
    pip install -r src/requirements.txt
    echo "Ansible environment is now configured and activated. To activate it in the future, run 'source activate' inside the same directory as this script."
    echo "To deactivate the python environment, run 'deactivate'."
else 
    echo "Quitting."
fi
