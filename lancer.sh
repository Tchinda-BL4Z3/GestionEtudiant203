#!/bin/bash
echo "======================================================"
echo "   DEMARRAGE DE L'APPLICATION (LINUX/ZORIN)"
echo "======================================================"

# 1. Verification Python
if ! command -v python3 &> /dev/null
then
    echo "[ERREUR] Python3 n'est pas installe."
    exit
fi

# 2. Installation
echo "[1/3] Installation de Django..."
pip3 install django --quiet

# 3. Migrations
echo "[2/3] Configuration de la base de donnees..."
python3 manage.py makemigrations scheduler
python3 manage.py migrate

# 4. Ouverture et serveur
echo "[3/3] Lancement..."
# On attend 2 secondes pour laisser le serveur démarrer avant d'ouvrir
(sleep 2 && xdg-open "http://127.0.0.1:8000") &
python3 manage.py runserver --noreload