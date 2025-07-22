param (
    [string]$action
)

if (-not $action) {
    Write-Host "Usage: .\init_db.ps1 [create|drop|truncate]"
    exit 1
}

switch ($action.toLower()) {
    "create"    { python init_db.py --create }
    "drop"      { python init_db.py --drop }
    "truncate"  { python init_db.py --truncate }
    default     { Write-Host "Invalid argument. Use: create, drop, or truncate" }
}