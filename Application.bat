@echo off
title Gestion Etudiant ICT 203
echo ======================================================
echo   DEMARRAGE DE L'APPLICATION (WINDOWS)
echo ======================================================

:: Verification Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe.
    pause
    exit
)

echo [1/3] Verification des dependances...
pip install django --quiet

echo [2/3] Mise a jour de la Base de Donnees...
python manage.py makemigrations scheduler
python manage.py migrate

echo [3/3] Lancement du navigateur et du serveur...
:: On ouvre l'accueil directement
start "" "http://127.0.0.1:8000"
python manage.py runserver --noreload
pause