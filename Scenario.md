# **Scénario d'exécution**

Ce document illustre un exemple complet d'exécution pour chaque partie du projet : le serveur et le client.

Le serveur et le client interagissent entre eux.
---

## **1. Serveur**

### Étapes :
1. **Démarrage du serveur** :  
   Exécutez la commande suivante dans le terminal pour démarrer le serveur :
   ```bash
   python main.py server
   ```
2. **Résultat attendu** :
    Une fois le serveur démarré, il écoute les connexions sur l'adresse 127.0.0.1 et le port 8080. Le message suivant est affiché dans la console :
    ```bash
    Server listening on 127.0.0.1:8080...
    ```
3. **Réception d'une requête valide** :
    Si un client demande un fichier existant, par exemple /index.html, les logs du serveur affichent :
    ```bash
    Connection from ('127.0.0.1', 46726)
    Received request:
    GET /index.html HTTP/1.1
    Host: 127.0.0.1
    ```

## **2. Client**

### Étapes :
1. **Démarrer le client** :  
   Exécutez la commande suivante dans le terminal pour démarrer le client HTTP :
   ```bash
   python main.py client
   ```
2. **Résultat attendu** :
    Une fois le client démarré, il demandera de saisir la page web que l'on souhaite consulté :
    ```bash
    Enter the page you want to request:
    ```

3. **Saisie Page Web** :
    Le client peut renseigné la page qu'il souhaite, dans notre exemple on choisi "index.html":
    ```bash
    Enter the page you want to request:
    index.html
    ```

4. **Réponse** :
    Une fois la requête envoyée, le client reçoit la réponse du serveur :
    ```bash
    Requesting '/index.html' from the server...

    En-tête HTTP:
    HTTP/1.1 200 OK
    Date: Thu, 23 Jan 2025 23:09:59 GMT
    Content-Type: text/html
    Last-Modified: Wed, 22 Jan 2025 11:16:58 GMT
    Content-Length: 107


    Corps HTTP:
    <html>
    <head><title>Index Page</title></head>
    <body>
        <h1>Welcome to the Home Page</h1>
    </body>
    </html>
    ```

    La réponse se divise en deux parties : **L'en-tête HTTP** et **Le corps HTTP**

    Le client peut également consulter le fichier dans le dossier *client/output/response.html*

5. **Cas où le fichier n'existe pas** :
    Si le client renseigne une page web qui n'existe pas sur le serveur comme par exemple */nonexistant*, le serveur renvoie cette réponse : 
    ```bash
    Requesting '/nonexistant' from the server...

    En-tête HTTP:
    HTTP/1.1 404 NOT FOUND
    Date: Thu, 23 Jan 2025 23:18:31 GMT
    Content-Type: text/html
    Content-Length: 0


    Corps HTTP:
    <html><body><h1>404 Not Found</h1></body></html>
    ```