# ----------------------------------------------------------------------------------
#
# Copyright Microsoft Corporation
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------------

param(
    [Parameter(Mandatory = $false, Position = 0, HelpMessage = "Name of the product to install. By default both AzPs and AzCli are installed.")]
    [ValidateSet("All", "AzPs", "AzCli")]
    [string]$Product = "All",
    [Parameter(Mandatory = $false, Position = 1, HelpMessage = "Upgrading the existing products, will overwrite the existing installation. By default it is false.")]
    [switch]$upgrade
)

<#################################################
#
#               Helper functions
#
#################################################>
function Test-ShellCopilotExist{
    param(
        [Parameter(Mandatory = $false)]
        [string]$AishPath = (Join-Path $env:userprofile ".azure" "bin" "shell-copilot")
    )
    return ([Environment]::GetEnvironmentVariable("PATH", "Process") -like "*$aishPath*") -or ([Environment]::GetEnvironmentVariable("PATH", "User") -like "*$aishPath*")
}

function Copy-ShellCopilotToLocalDir{
    param(
        [Parameter(Mandatory = $false, HelpMessage = "Whether to overwrite Shell-Copilot, default to false")]
        [switch]$Overwrite
    )
    [string]$SourcePath = (Join-Path $PSScriptRoot "shell-copilot")
    [string]$DestinationParentPath = (Join-Path $env:userprofile ".azure" "bin")
    [string]$DestinationPath = (Join-Path $DestinationParentPath "shell-copilot")
    [string]$AishPath = (Join-Path $DestinationPath "aish.exe")
    if ((Test-Path $DestinationPath) -and (Test-Path $AishPath -PathType Leaf))
    {
        if ($Overwrite)
        {
            Write-Host "[Shell Copilot was already copied to local path, upgrading by overwriting the original files]" -ForegroundColor Green
            Copy-Item -Path $SourcePath -Destination $DestinationParentPath -Recurse -Force
            Write-Host "[Shell Copilot copied to $DestinationPath]" -ForegroundColor Green
        }
        else
        {
            Write-Host "[Shell Copilot was already copied to local path, not upgrading]" -ForegroundColor Green
        }

    }
    else
    {
        Write-Host "[Copying Shell Copilot to local]" -ForegroundColor Green
        Copy-Item -Path $SourcePath -Destination $DestinationParentPath -Recurse
        Write-Host "[Shell Copilot copied to $DestinationPath]" -ForegroundColor Green
    }
}

function Add-ShellCopilotToPath{
    param(
        [Parameter(Mandatory = $false)]
        [string]$AishPath = (Join-Path $env:userprofile ".azure" "bin" "shell-copilot")
    )
    if (Test-ShellCopilotExist)
    {
        Write-Host "[Shell Copilot was already added in PATH]" -ForegroundColor Green
    }
    else {
        Write-Host "[Adding Shell Copilot to PATH]" -ForegroundColor Green
        $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
        $processPath = [Environment]::GetEnvironmentVariable("PATH", "Process")
        if ($userPath -notmatch ";$"){
            $userPath += ";"
        }
        if ($processPath -notmatch ";$"){
            $processPath += ";"
        }
        [Environment]::SetEnvironmentVariable("PATH", $userPath + $aishPath, "User")
        [Environment]::SetEnvironmentVariable("PATH", $processPath + $aishPath, "Process")
    }
}

function Install-AzPsCopilot {
    param(
        [string]
        [Parameter(Mandatory = $false, Position = 0, HelpMessage = "Name of the module to install. By default all modules are installed.")]
        $ModuleName = "Az.Tools.Copilot",
        [string]
        [Parameter(Mandatory = $false, Position = 1, HelpMessage = "Specifies the path for discovering and installing modules from.")]
        $SourceLocation = $PSScriptRoot,
        [string]
        [ValidateSet("CurrentUser", "AllUsers")]
        [Parameter(Mandatory = $false, Position = 2, HelpMessage = "The scope of the installed module")]
        $Scope = "CurrentUser"
    )

    $gallery = [guid]::NewGuid().ToString()
    Write-Debug "[Registering temporary repository $gallery with InstallationPolicy Trusted]"
    Register-PSRepository -Name $gallery -SourceLocation $SourceLocation -PackageManagementProvider NuGet -InstallationPolicy Trusted

    try {
      Write-Host "[Installing $ModuleName]" -ForegroundColor Green
      Install-Module -Name $ModuleName -Repository $gallery -Scope $Scope -AllowClobber -Force
    }
    finally {
      Write-Debug "[Unregistering gallery $gallery]"
      Unregister-PSRepository -Name $gallery
    }

    Write-Host "[Installation has completed]" -ForegroundColor Green
    Write-Host "Please make sure ``Connect-AzAccount`` is executed before running ``Start-Copilot``" -ForegroundColor Yellow
}

function Install-AzCliCopilot {
    param(
        [Parameter(Mandatory = $false, HelpMessage = "Whether or not to upgrade the azcli extension. By default it is false.")]
        [switch]$upgrade
    )
    [string]$cliwhlPath = Get-ChildItem -Path (Join-Path $PSScriptRoot "azcli") -Filter *.whl
    if ($upgrade)
    {
        Write-Host "[Upgrading az copilot extension]" -ForegroundColor Green
        az extension add --source $cliwhlPath --upgrade -y
        Write-Host "[Upgrade has completed]" -ForegroundColor Green
    }
    else
    {
        Write-Host "[Installing az copilot extension]" -ForegroundColor Green
        az extension add --source $cliwhlPath -y
        Write-Host "[Installation has completed]" -ForegroundColor Green
    }

    Write-Host "Please make sure to run ``az login --tenant <tenant-id>`` before running ``az copilot``" -ForegroundColor Yellow
}

<###################################
#
#           Setup/Execute
#
###################################>
Write-Host "----------------------------------------`n" -ForegroundColor Green

Copy-ShellCopilotToLocalDir -Overwrite:$upgrade

Write-Host "`n----------------------------------------`n" -ForegroundColor Green

Add-ShellCopilotToPath

Write-Host "`n----------------------------------------`n" -ForegroundColor Green

if(("All" -eq $Product) -or ("AzPs" -eq $Product)){
    Install-AzPsCopilot
    Write-Host "`n----------------------------------------`n" -ForegroundColor Green
}

if(("All" -eq $Product) -or ("AzCli" -eq $Product)){
    Install-AzCliCopilot -upgrade:$upgrade
    Write-Host "`n----------------------------------------" -ForegroundColor Green
}

Write-Host "[Please make sure Windows Terminal is installed before using ``Start-Copilot` and ``az copilot``]" -ForegroundColor Yellow