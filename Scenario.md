# **Scénario d'exécution**

Ce document illustre un exemple complet d'exécution pour chaque partie du projet : le serveur et le client.

Le client peut fonctionner de manière indépendante. 
Si le client souhaite envoyer une requête au serveur local, celui-ci doit d'abord être démarré en suivant les étapes appropriées. 
Toutefois, le client peut également être exécuté indépendamment pour communiquer avec un serveur distant, comme www.google.ca ou www.amazon.ca.

---

## **1. Serveur**

### Étapes :
1. **Démarrage du serveur** :  
   Exécutez la commande suivante dans le terminal pour démarrer le serveur :
   ```bash
   python3 main.py server
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
   python3 main.py client
   ```
2. **Saisie serveur** :
    Une fois le client démarré, il vous demande à quel serveur vous souhaitez vous connecter :
    ```bash
    What server do you want to connect ?
    ```

3. **Saisie Page Web** :
    Le client demande ensuite la page que vous souhaitez joindre:
    ```bash
    Enter the page you want to request:
    ```

3. **Exemple de demande de saisie**:
    Comme exemple on peut obtenir ce résultat : 
    ```bash
    What server do you want to connect ? www.google.ca
    Enter the page you want to request : index.html
    ```

4. **Réponse** :
    Une fois la requête envoyée, le client reçoit la réponse du serveur. Pour des raisons de simplicité nous présentons ici un exemple avec le serveur local HTTP que nous avons développé : 
    ```bash
    What server do you want to connect ? localhost
    Enter the page you want to request : index.html
    Requesting the page from 127.0.0.1:8080/index.html ...

    En-tête HTTP:
    HTTP/1.1 200 OK
    Date: Wed, 29 Jan 2025 13:14:06 GMT
    Content-Type: text/html
    Last-Modified: Wed, 29 Jan 2025 12:39:44 GMT
    Content-Length: 110



    Corps HTTP:
    <html>
    <head><title>Index Page</title></head>
    <body>
        <h1>This is the index page html</h1>
    </body>
    </html>
    ```

    La réponse se divise en deux parties : **L'en-tête HTTP** et **Le corps HTTP**

    Le client peut également consulter le fichier dans le dossier *client/output/response.html*

5. **Cas où le fichier n'existe pas** :
    Si le client renseigne une page web qui n'existe pas sur le serveur comme par exemple */nonexistant*, le serveur renvoie cette réponse : 
    ```bash
    Requesting the page from 127.0.0.1:8080/nonexistant ...

    En-tête HTTP:
    HTTP/1.1 404 NOT FOUND
    Date: Thu, 23 Jan 2025 23:18:31 GMT
    Content-Type: text/html
    Content-Length: 0


    Corps HTTP:
    <html><body><h1>404 Not Found</h1></body></html>
    ```