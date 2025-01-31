# HTTP Client-Server Application

## Description

Ce projet combine un client et un serveur HTTP développés en Python. 

### Fonctionnalités principales

1. **Client HTTP** : 
   - Se connecte à un serveur HTTP via TCP.
   - Envoie une requête pour récupérer une page HTML (ex. `index.html`).
   - Affiche ou sauvegarde le fichier HTML reçu.

2. **Serveur HTTP** :
   - Attend les connexions sur le port 8080.
   - Répond aux requêtes HTTP en envoyant une page HTML minimale.

## Installation

1. Clonez ce projet ou téléchargez-le.
2. Assurez-vous d'avoir Python installé (version 3.7 ou supérieure).
3. Exécutez le serveur et le client dans deux terminaux distincts.

## Utilisation 

**Lancer le serveur HTTP**
Dans le terminal, placez vous à la racine du projet et exécutez la commande : 
```bash
python3 main.py server
```

**Lancer le client HTTP**
Dans un autre terminal, placez vous à la racine du projet et exécutez la commande : 
```bash
python3 main.py client
```


## Scénario

Un scénario d'utilisation est disponible [ici](Scenario.md).

## Présentation

Une vidéo est disponible [ici](https://youtu.be/GyKE8QV_5OY) pour montrer le fonctionnement du server et du client HTTP.