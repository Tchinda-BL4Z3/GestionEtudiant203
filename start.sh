#!/bin/bash
echo "Lancement de l'application Gestion EDT..."

# Lancement du backend en arrière-plan
cd backend
npm start &

# Lancement du frontend
cd ../frontend
npm run dev
