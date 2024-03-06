## Copyright (c) Microsoft Corporation.
## Licensed under the MIT License.

#Requires -Version 7.2
#Requires -PSEdition Core

$aishPath = Join-Path $PWD "aish" "debug"
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
$processPath = [Environment]::GetEnvironmentVariable("PATH", "Process")
if ($processPath -notlike "*$aishPath*")
{
    Write-Host "[Adding Shell Copilot to PATH]" -ForegroundColor Green
    if ($userPath -notmatch ";$"){
        $userPath += ";"
    }
    if ($processPath -notmatch ";$"){
        $processPath += ";"
    }
    [Environment]::SetEnvironmentVariable("PATH", $userPath + $aishPath, "User")
    [Environment]::SetEnvironmentVariable("PATH", $processPath + $aishPath, "Process")
}
else {
    Write-Host "[Shell Copilot already in PATH]" -ForegroundColor Green
}
Write-Host "[Installing az copilot extension]" -ForegroundColor Green
az extension add --source ./copilot-1.0.0b4-py3-none-any.whl -y
Write-Host "[Installation has completed]`nPlease make sure to run [az login --tenant <tenant-id>]`nbefore running [az copilot]`nPlease make sure to not delete the azcopilot folder" -ForegroundColor Green