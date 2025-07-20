# Create virtual environment if it doesn't exist
if (-Not (Test-Path -Path ".\venv")) {
    python -m venv venv
}

# Activate the virtual environment
# Use the PowerShell activation script
. .\venv\Scripts\Activate.ps1

# Upgrade pip (optional)
# python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
Write-Output "Starting Flask app..."
python app.py
