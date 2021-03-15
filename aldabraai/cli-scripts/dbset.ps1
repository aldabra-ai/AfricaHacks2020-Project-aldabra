

# download chocolatey package installer
Write-Output "downloading chocolatey package installer"

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# check for postgresql
Write-Output "checking for postgresql"

choco find postgresql

# install postgresql
Write-Output "installing postgrestql"

choco install postgresql13 --params '/Password:passcodetestdb'

# test installation
Write-Output "testing installation"

$Env:PGPASSWORD='passcodetestdb'; '\conninfo' | psql -Upostgres

# create database
Write-Output "Creating Database 'aldabratestdb'"

createdb aldabratestdb