##
## Runs a few commands to initialize a python virtual environment and download the required packages for nickjgrahamcom.
##

$requiredPythonVersion = "3.10"

# Test to make sure Python is installed before we bother doing anything else.

try {
    $pyVersion = python --version
}
catch {
    Throw "Unable to find python. Make sure python $requiredPythonVersion is installed and included in your PATH."
}

# Split out the actual version number from the command output

$pyVersion = $pyVersion.Split(" ")
$pyVersion = $pyVersion[1]

# Split out the major/minor/patch numbers

$pyVersion = $pyVersion.Split(".")
$requiredPythonVersion = $requiredPythonVersion.Split(".")

# Make sure Python is at a high enough version

# Major version
if ($pyVersion[0] -lt $requiredPythonVersion[0]) {
    Throw "Python major version is lower than " + $requiredPythonVersion[0] + " (is " + $pyVersion[0] + "). Please upgrade and try again."
}
# Minor version
if ($pyVersion[1] -lt $requiredPythonVersion[1]) {
    Throw "Python minor version is lower than " + $requiredPythonVersion[1] + " (is " + $pyVersion[1] + "). Please upgrade and try again."
}

# Prompt user to make sure they actually want to create the virtual environment

Write-Host "This script creates a python virtual environment called 'venv' and packs it full of everything you need to run the nickjgrahamcom application."
Write-Warning "Are you sure you want to do this?"

if (Test-Path -Path "venv") {
    Write-Warning "'venv' already exists. Make sure you're okay with overwriting it."
}

$continue = Read-Host "Continue? (y/N)"

if ($continue -eq "y") {
    # Delete the old 'venv' directory if it already exists
    if ( Test-Path -Path "venv" ) {
        Write-Host "Deleting old environment..."
        Remove-Item -Path "venv" -Recurse
    }
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Activating virtual environment..."
    venv\Scripts\Activate.ps1
    Write-Host "Upgrading pip..."
    python -m pip install --upgrade pip wheel
    Write-Host "Installing packages..."
    pip install -r src\requirements.txt
    Write-Host "Ansible environment is now configured and activated. To activate it in the future, run 'Scripts\Activate.ps1' inside the same directory as this script."
    Write-Host "To deactivate the python environment, run 'deactivate'."
}
else {
    Write-Host "Quitting."
}