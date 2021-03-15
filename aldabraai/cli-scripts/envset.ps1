
# install virtualenv
Write-Output "installing virtualenv"

pip install virtualenv


# create virtual environment 'aldabra-env'
Write-Output "creating virtual environment 'aldabra-env'"

virtualenv ../aldabra-env

# activate environment
Write-Output "activating environment"

& ../aldabra-env/Scripts/Activate.ps1

# install requirements
Write-Output "installing requirements"

pip install -r ../requirements.txt
