#!/bin/bash

# no console, esteja na pasta raiz (basic_tornado) e execute o seguinte comando:
# venv/create_venv.sh

# Obs.: o arquivo create_venv.sh precisa ter permissão de execução, utilize o seguinte comando:
# chmod +x create_venv.sh

# caso uma excecao ocorra antes do "echo", a excecao eh lancada para cima e retorna um erro para o console
set -e  # If occur any error, exit
function to_console {
    echo -e "\n $1 \n"
}

# build a new virtualenv, installing the dependencies
virtualenv venv/
to_console "--> Created the Virtualenv."

source venv/bin/activate
to_console "--> Activated the Virtualenv."

pip install -r venv/requirements.txt
to_console "--> Installed the requirements."