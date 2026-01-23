#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

echo "--- INSTALLATION AUTOMATIQUE (LINUX) ---"

# 1. Installation Backend (Prisma inclus)
echo "Étape 1: Installation du Backend..."
cd backend
npm install
# Génération du client Prisma (très important pour SQLite)
npx prisma generate
# Synchronisation de la base de données
npx prisma db push

# 2. Installation Frontend
echo "Étape 2: Installation du Frontend..."
cd ../frontend
npm install

echo "--- INSTALLATION TERMINÉE ---"
echo "Pour lancer le projet, tape : ./start.sh"
