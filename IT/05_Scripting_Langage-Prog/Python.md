# Cours Complet de Scripting Python pour la Cybersécurité Défensive

## De zéro à l'automatisation défensive — Guide pour débutant absolu

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c'est un ordinateur (Linux, Mac ou Windows) et l'envie d'apprendre.
>
> **Orientation :** ce cours enseigne Python en s'appuyant sur des exemples de **cybersécurité défensive** (SOC, analyse de logs, OSINT, CTI, forensic léger, manipulation d'IOC). On apprend à **automatiser l'analyse**, jamais à attaquer. Tous les exemples sont légitimes et défensifs.

-----

## Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou. On y mélange volontairement les termes Python et les termes cyber, car tu vas les croiser ensemble.

| Terme            | Définition simple                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **Terminal**     | La fenêtre où tu tapes des commandes texte pour parler à ton ordinateur                               |
| **Script**       | Un fichier texte contenant des instructions Python à exécuter                                         |
| **Variable**     | Un conteneur avec un nom qui stocke une valeur (un nombre, du texte…)                                 |
| **Type**         | La nature d'une valeur : texte (`str`), entier (`int`), décimal (`float`), vrai/faux (`bool`)         |
| **Argument**     | Une info que tu donnes à un script quand tu le lances dans le terminal                                |
| **Fonction**     | Un bloc de code réutilisable auquel on donne un nom                                                   |
| **Boucle**       | Un mécanisme qui répète des instructions plusieurs fois                                               |
| **Module**       | Un fichier Python contenant des fonctions prêtes à l'emploi que tu peux importer                      |
| **Indentation**  | Les espaces en début de ligne qui délimitent les blocs de code en Python                              |
| **Liste**        | Une collection ordonnée de valeurs, modifiable                                                        |
| **Dictionnaire** | Une collection de paires clé-valeur (comme un vrai dictionnaire : mot → définition)                   |
| **Exception**    | Une erreur qui se produit pendant l'exécution du script                                               |
| **Log**          | Un fichier journal : chaque ligne enregistre un événement (connexion, erreur, accès…)                 |
| **IOC**          | *Indicator of Compromise* : une trace observable d'une attaque (IP, domaine, hash, URL malveillante…) |
| **IP**           | L'adresse numérique d'une machine sur un réseau (ex. `192.168.1.10`)                                  |
| **Hash**         | Une empreinte numérique unique d'un fichier ou d'un texte (ex. MD5, SHA-256)                          |
| **SOC**          | *Security Operations Center* : l'équipe qui surveille et défend un système d'information              |
| **SIEM**         | Outil qui centralise et analyse les logs de sécurité de toute une organisation                        |
| **CTI**          | *Cyber Threat Intelligence* : le renseignement sur les menaces (qui attaque, comment, avec quoi)      |
| **OSINT**        | *Open Source Intelligence* : le renseignement à partir de sources publiques et ouvertes               |

-----

## Comment penser un script

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

En cyber défensive, ce schéma est partout :

```
  Un fichier   →   On extrait les    →  Une liste d'IP
  de logs          IP suspectes         à bloquer
```

Concrètement, il n'y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier de log…)
2. **Stocker** des informations dans des variables
3. **Tester** si quelque chose est vrai ou faux (conditions)
4. **Répéter** une action plusieurs fois (boucles)
5. **Afficher ou enregistrer** un résultat (rapport, alerte, fichier de sortie)

Tous les scripts, même un parser de logs ou un extracteur d'IOC, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

-----

## La grande différence avec Bash

Si tu viens du cours Bash de cette collection, un point fondamental va changer : **Python n'est pas un langage de commandes système, c'est un langage de programmation généraliste.**

En Bash, tu enchaînes des commandes du système (`ls`, `grep`, `cat`…) et tu les relies avec des pipes. En Python, tu écris des **instructions** que Python exécute lui-même.

Concrètement :

- En Bash, `grep "Failed password" auth.log` appelle la commande `grep` du système.
- En Python, tu écris toi-même la logique : ouvrir le fichier, parcourir les lignes, tester si chacune contient `"Failed password"`. C'est plus de code, mais infiniment plus puissant : tu peux ensuite compter, regrouper par IP, exporter en JSON, interroger une API…

Python a ses propres outils, souvent plus puissants et plus lisibles que les commandes système. Ce cours t'apprend ces outils à partir de zéro.

-----

## Table des matières

### Partie 1 — Fondamentaux Python (orientés cyber défensive)

1. [Découverte de Python et premier script](#chapitre-1--découverte-de-python-et-premier-script)
2. [Variables, types, affichage et saisie utilisateur](#chapitre-2--variables-types-affichage-et-saisie-utilisateur)
3. [Arguments, terminal et scripts paramétrés](#chapitre-3--arguments-terminal-et-scripts-paramétrés)
4. [Opérateurs, calculs et logique](#chapitre-4--opérateurs-calculs-et-logique)
5. Conditions
6. Chaînes de caractères
7. Listes et boucles
8. Fonctions
9. Dictionnaires
10. Fichiers, chemins, CSV, JSON
11. Erreurs, débogage et code propre
12. Cas pratiques et automatisation

### Partie 2 — Python pour la cybersécurité défensive

13. Regex avec `re` — extraire IP, emails, domaines, URLs, hash
14. Parsing de logs : SSH, web et événements structurés
15. Manipulation d'IOC : IP, domaines, URLs, hash
16. Requêtes HTTP et APIs CTI avec `requests`
17. JSON avancé pour APIs CTI/SIEM
18. Calcul de hash avec `hashlib`
19. Validation d'IP et réseaux avec `ipaddress`
20. Mini-projets cyber défensifs

-----

# Chapitre 1 — Découverte de Python et premier script

## Le minimum à savoir

### Pourquoi Python en cybersécurité ?

Python est l'un des langages les plus utilisés au monde, et **l'un des langages les plus utilisés en cybersécurité défensive**. Il est populaire pour une raison simple : **il se lit presque comme de l'anglais**. Là où d'autres langages utilisent des symboles cryptiques, Python utilise des mots clairs.

En SOC, en analyse de menaces ou en forensic, on passe son temps à manipuler du texte : des logs, des adresses IP, des domaines, des hash. Python excelle exactement là-dessus. Un analyste qui sait scripter en Python peut automatiser en quelques lignes ce qui prendrait des heures à la main : extraire toutes les IP d'un fichier de logs, calculer le hash d'un fichier suspect, interroger une base de menaces…

Dans ce cours, on se concentre sur le **scripting** : écrire des petits programmes pour automatiser des tâches concrètes d'analyse défensive.

### Installer Python

**Linux :** Python est déjà installé. Vérifie avec :

```bash
python3 --version
```

Tu devrais voir quelque chose comme `Python 3.12.x` ou `Python 3.13.x`. Si tu vois une version 3.8 ou plus récente, c'est bon.

**Mac :** Python 3 n'est pas toujours installé par défaut. La méthode la plus simple :

```bash
# Vérifie d'abord
python3 --version

# Si ça ne fonctionne pas, va sur https://www.python.org/downloads/
# et télécharge l'installeur Mac
```

**Windows :**

1. Va sur [python.org/downloads](https://python.org/downloads)
2. Télécharge la dernière version
3. **IMPORTANT : coche la case "Add Python to PATH"** pendant l'installation. Si tu oublies cette case, rien ne fonctionnera dans le terminal.
4. Ouvre un terminal (PowerShell) et tape `python --version`

> **Piège Windows :** sur Windows, la commande est souvent `python` (sans le `3`), alors que sur Linux et Mac c'est `python3`. Dans ce cours, on utilisera `python3`, mais adapte si tu es sur Windows.

### Environnement de travail conseillé

Avant de te lancer, prépare un environnement simple et sûr :

- **Un terminal** (celui de ton système suffit).
- **Un éditeur de code** : VS Code est recommandé (coloration, indentation automatique), mais nano ou n'importe quel éditeur fonctionne.
- **Un dossier dédié** `scripts_cyber` pour tous tes scripts.
- **Des fichiers de test que tu crées toi-même** (faux logs, faux CSV d'IOC). À partir du chapitre 10, garde sous la main quelques fichiers de test comme `auth.log`, `access.log`, `iocs.csv`, `rapport.txt` : c'est ce qui te fera progresser le plus vite.
- **Règle d'or :** ne lance jamais tes scripts sur des logs ou des systèmes que tu n'es pas autorisé à analyser.

> **Environnement virtuel (à garder pour le chapitre 16) :** dès que tu installeras une bibliothèque externe comme `requests`, il est propre de créer un environnement isolé. Tu n'en as pas besoin tout de suite, mais voici la commande pour plus tard :
```bash  
python3 -m venv venv  
source venv/bin/activate # sur Windows : venv\Scripts\activate  
pip install requests  
```
### Le mode interactif : ton terrain d'entraînement

Tape `python3` dans ton terminal :

```bash
python3
```

Tu vois apparaître les `>>>`, le **prompt interactif**. Tu peux taper des instructions et voir le résultat immédiatement :

```python
>>> print("Analyse démarrée")
Analyse démarrée
>>> 22 + 80
102
>>> "192.168.1.1" in "Connexion depuis 192.168.1.1"
True
```

C'est un bac à sable : tu tapes, Python répond. Parfait pour tester une idée rapidement, par exemple vérifier si une IP apparaît dans une ligne de log.

Pour quitter :

```python
>>> exit()
```

> **À retenir :** le mode interactif est idéal pour **tester** de petites choses. Pour écrire un vrai script réutilisable, tu utilises un fichier.

### Ton premier script en 3 étapes

**Étape 1 — Crée un dossier de travail :**

```bash
mkdir -p ~/scripts_cyber
cd ~/scripts_cyber
```

**Étape 2 — Crée le fichier et écris le script :**

Ouvre un éditeur de texte (nano, VS Code…) et crée un fichier `alerte.py` :

```python
# Mon tout premier script de sécurité
print("[+] Outil d'analyse démarré")
print("[+] Aucune menace détectée pour l'instant")
```

Sauvegarde le fichier.

**Étape 3 — Lance-le :**

```bash
python3 alerte.py
```

Résultat :

```
[+] Outil d'analyse démarré
[+] Aucune menace détectée pour l'instant
```

Félicitations, tu viens d'écrire et d'exécuter ton premier script Python ! Le préfixe `[+]` est une convention courante dans les outils de sécurité pour marquer une information ; on verra aussi `[-]` (problème) et `[!]` (alerte).

> **Remarque :** contrairement à Bash, pas besoin de `chmod +x` ni de shebang. Tu lances simplement `python3 nom_du_script.py`.

### Les commentaires

Le symbole `#` marque un commentaire. Python ignore tout ce qui suit un `#` sur la même ligne :

```python
# Ceci est un commentaire — Python l'ignore complètement
print("Ceci s'affiche")  # Un commentaire en fin de ligne
```

Les commentaires servent à expliquer ton code, pour toi et pour les autres analystes qui le reliront.

### Python est sensible à la casse

`print` et `Print` sont deux choses différentes pour Python :

```python
print("Bonjour")    # ✅ Fonctionne
Print("Bonjour")    # ❌ NameError: name 'Print' is not defined
```

Les commandes Python sont en **minuscules** : `print`, `input`, `if`, `for`.

## Très utile en pratique

### Le shebang (optionnel)

Si tu veux lancer ton outil directement avec `./scan.py`, ajoute un shebang en première ligne :

```python
#!/usr/bin/env python3
print("Outil prêt")
```

Puis :

```bash
chmod +x scan.py
./scan.py
```

Ce n'est pas obligatoire, mais c'est pratique pour transformer un script en commande réutilisable.

### Mode interactif vs fichier script

|Mode interactif (`python3`)        |Fichier script (`python3 script.py`)|
|-----------------------------------|------------------------------------|
|Pour tester une idée rapidement    |Pour un outil réutilisable          |
|Le code disparaît à la fermeture   |Le code est sauvegardé              |
|Résultat affiché automatiquement   |Il faut utiliser `print()`          |
|Pas pratique pour plus de 5 lignes |Adapté à n'importe quelle taille    |

## Application cyber

Un analyste teste souvent une idée dans le mode interactif avant d'écrire un script. Exemple : tu reçois une ligne de log et tu veux vérifier rapidement si elle contient un mot-clé suspect.

```python
>>> ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5"
>>> "Failed password" in ligne
True
>>> "root" in ligne
True
```

En deux secondes, tu as confirmé que cette ligne est une **tentative de connexion SSH échouée sur le compte root**, un signal classique de tentative d'intrusion. On apprendra à automatiser ça sur un fichier entier dans les chapitres suivants.

## ❌ Erreur classique

```python
# Oublier les parenthèses de print (syntaxe Python 2, plus valide)
print "Démarrage"        # ❌ SyntaxError
print("Démarrage")       # ✅ Correct

# Oublier les guillemets autour du texte
print(Demarrage)          # ❌ NameError: name 'Demarrage' is not defined
print("Demarrage")        # ✅ Correct

# Majuscule sur print
Print("Démarrage")        # ❌ NameError
print("Démarrage")        # ✅ Correct
```

## Exercices

**Guidé :** Crée un script `banniere.py` qui affiche trois lignes : `"=== Outil SOC ==="`, `"[+] Initialisation..."`, puis `"[+] Prêt à analyser."`.

**Autonome :** Crée un script `etat.py` qui affiche le résultat de `443 + 80` (total de deux ports), de `1024 * 64`, et le texte `"[+] Calculs réseau terminés"` — chacun sur une ligne séparée avec `print()`.

## ✅ Tu sais maintenant…

- Ce qu'est Python et pourquoi c'est central en cyber défensive
- Installer et vérifier ta version de Python
- Utiliser le mode interactif pour tester rapidement une idée (ex. chercher un mot-clé dans une ligne de log)
- Créer un fichier `.py` et le lancer avec `python3`
- Écrire des commentaires avec `#`

-----

# Chapitre 2 — Variables, types, affichage et saisie utilisateur

## Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable, c'est un **conteneur avec une étiquette**. L'étiquette c'est le nom, à l'intérieur il y a une valeur.

```
┌──────────────────────────┐
│  ip_source = "203.0.113.5" │   ← "ip_source" est le nom, "203.0.113.5" la valeur
└──────────────────────────┘
```

### Créer une variable

```python
ip_source = "203.0.113.5"
utilisateur = "root"
port = 22
score_risque = 8.5
est_bloquee = True
```

> **Différence avec Bash :** en Python, on met des **espaces autour du `=`** (`ip_source = "..."`). C'est l'inverse de Bash.

**Règles pour les noms de variables :**

- Que des lettres, chiffres et underscores (`_`)
- Ne peut pas commencer par un chiffre
- Pas d'espaces, pas de tirets, pas de caractères spéciaux
- Sensible à la casse (`ip` et `IP` sont deux variables différentes)

> **Convention Python :** les noms s'écrivent en `snake_case` : minuscules, mots séparés par des underscores. `ip_source` plutôt que `ipSource`.

### Les types de données

C'est ici que Python diffère fondamentalement de Bash. **En Bash, tout est du texte.** En Python, chaque valeur a un **type**, et ce type détermine ce qu'on peut faire avec.

Les 4 types de base, avec des exemples cyber :

|Type           |Nom Python|Exemple cyber                 |Ce que c'est            |
|---------------|----------|------------------------------|------------------------|
|Texte          |`str`     |`"203.0.113.5"`, `"evil.com"` |Une chaîne de caractères|
|Nombre entier  |`int`     |`22`, `443`, `404`            |Un nombre sans virgule  |
|Nombre décimal |`float`   |`8.5`, `0.95`                 |Un nombre avec virgule  |
|Booléen        |`bool`    |`True`, `False`               |Vrai ou Faux            |

```python
ip = "203.0.113.5"       # str — une IP est du texte, pas un nombre !
port = 22                # int
score = 8.5              # float
est_malveillante = True  # bool
```

Pour vérifier le type d'une variable :

```python
print(type(ip))                # <class 'str'>
print(type(port))              # <class 'int'>
print(type(est_malveillante))  # <class 'bool'>
```

> **Très important en cyber :** une adresse IP, un domaine, un hash sont du **texte** (`str`), même s'ils contiennent des chiffres. `"203.0.113.5"` n'est pas un nombre. À l'inverse, un port (`22`) ou un code HTTP (`404`) sont des nombres entiers.

### Python détecte les types automatiquement

Tu n'as pas besoin de déclarer le type. Python le devine :

```python
x = 22          # int
x = "evil.com"  # maintenant str — Python s'adapte
x = 0.95        # maintenant float
```

C'est pratique, mais une variable peut changer de type en cours de route, ce qui peut créer des bugs si tu n'y fais pas attention.

### Afficher avec `print()`

`print()` affiche du texte à l'écran. C'est l'équivalent du `echo` de Bash.

```python
ip = "203.0.113.5"
port = 22

# Méthode 1 : virgules (ajoute un espace automatiquement)
print("Connexion depuis", ip, "sur le port", port)
# → Connexion depuis 203.0.113.5 sur le port 22

# Méthode 2 : f-strings (la meilleure)
print(f"[!] Connexion depuis {ip} sur le port {port}")
# → [!] Connexion depuis 203.0.113.5 sur le port 22
```

> **À retenir :** les **f-strings** (avec le `f` devant les guillemets) sont la manière recommandée d'insérer des variables dans du texte. Entre les `{}`, tu mets le nom de la variable, Python remplace par sa valeur.

### Guillemets simples et doubles

En Python, `"texte"` et `'texte'` sont **strictement équivalents**. L'intérêt est de pouvoir imbriquer :

```python
log = "L'utilisateur 'admin' s'est connecté"
log = 'Domaine suspect : "evil.com"'
```

> **Différence avec Bash :** en Python, il n'y a **aucune différence** de comportement entre guillemets simples et doubles. Les deux interprètent les variables de la même façon dans une f-string : `f"..."` et `f'...'`.

### Lire une saisie utilisateur avec `input()`

`input()` affiche un message et attend que l'utilisateur tape quelque chose :

```python
ip = input("IP à analyser : ")
print(f"[+] Analyse de {ip} en cours...")
```

Exécution :

```
IP à analyser : 203.0.113.5
[+] Analyse de 203.0.113.5 en cours...
```

C'est l'équivalent du `read -p` de Bash.

### Le piège fondamental de `input()`

**`input()` renvoie TOUJOURS du texte** (`str`), même si l'utilisateur tape un nombre :

```python
port = input("Port : ")
print(type(port))        # <class 'str'> — c'est du TEXTE, pas un nombre !
```

Si tu veux faire des calculs ou des comparaisons numériques, tu dois **convertir** :

```python
port = int(input("Port : "))   # On convertit en entier
if port < 1024:
    print("[!] Port système (privilégié)")
```

Les fonctions de conversion :

| Fonction  | Convertit vers | Exemple                |
| --------- | -------------- | ---------------------- |
| `int()`   | Nombre entier  | `int("443")` → `443`   |
| `float()` | Nombre décimal | `float("8.5")` → `8.5` |
| `str()`   | Texte          | `str(404)` → `"404"`   |

```python
# ❌ Si tu oublies de convertir :
port = input("Port : ")          # l'utilisateur tape 22
suivant = port + 1                # ❌ TypeError : "22" + 1 impossible

# ✅ Correct :
port = int(input("Port : "))
suivant = port + 1                # ✅ 23
```

## Très utile en pratique

### Modifier une variable

```python
statut = "inconnu"
print(f"Statut : {statut}")

statut = "malveillant"
print(f"Statut mis à jour : {statut}")
```

### Affectation multiple

```python
ip, port, protocole = "203.0.113.5", 443, "https"
```

### Concaténation de texte

Pour coller deux chaînes :

```python
protocole = "https"
domaine = "exemple.com"
url = protocole + "://" + domaine
print(url)      # → https://exemple.com
```

Mais on ne peut pas coller du texte et un nombre directement :

```python
port = 443
print("Port : " + port)        # ❌ TypeError
print("Port : " + str(port))   # ✅ Fonctionne mais lourd
print(f"Port : {port}")        # ✅ Beaucoup mieux avec f-string
```

> **Bonne pratique :** utilise les f-strings plutôt que la concaténation `+`. Plus lisible, moins d'erreurs de type.

### Les f-strings en détail

Les f-strings peuvent contenir des expressions, pas seulement des variables :

```python
echecs = 47
fenetre_min = 5
print(f"{echecs} échecs en {fenetre_min} min")          # → 47 échecs en 5 min
print(f"Taux : {echecs / fenetre_min:.1f} par minute")  # → Taux : 9.4 par minute
```

## Application cyber

Modélisons une **alerte de sécurité** avec des variables typées correctement — c'est exactement ce qu'on manipulera plus tard sous forme de dictionnaire.

```python
# Une alerte SOC décrite avec des variables
ip_source = "203.0.113.5"       # str
ip_dest = "10.0.0.12"           # str
port_dest = 22                  # int
protocole = "SSH"               # str
nb_tentatives = 47              # int
score_risque = 8.5              # float
est_critique = True             # bool

print(f"[!] ALERTE — risque {score_risque}/10")
print(f"    Source      : {ip_source}")
print(f"    Destination : {ip_dest}:{port_dest} ({protocole})")
print(f"    Tentatives  : {nb_tentatives}")
print(f"    Critique    : {est_critique}")
```

Résultat :

```
[!] ALERTE — risque 8.5/10
    Source      : 203.0.113.5
    Destination : 10.0.0.12:22 (SSH)
    Tentatives  : 47
    Critique    : True
```

Note bien les **types** : les IP et le protocole sont du texte, le port et le nombre de tentatives sont des entiers, le score est un décimal, et le caractère critique est un booléen. Choisir le bon type dès le départ évite des bugs plus tard (par exemple, on ne pourra comparer `score_risque > 7` que si c'est bien un nombre).

## Bonus

### `None` — l'absence de valeur

`None` représente « rien », « pas encore de valeur » :

```python
pays_source = None     # On ne connaît pas encore le pays de l'IP
print(pays_source)     # → None
```

C'est utile pour déclarer une variable qu'on remplira plus tard (par exemple après une requête à une API de géolocalisation).

### Les chaînes multi-lignes

```python
rapport = """=== Rapport d'analyse ===
IP analysée : 203.0.113.5
Verdict     : malveillante"""

print(rapport)
```

## ❌ Erreur classique

```python
# Oublier de convertir la saisie utilisateur
port = input("Port : ")
suivant = port + 1          # ❌ TypeError — "22" + 1 ne fonctionne pas
port = int(input("Port : "))
suivant = port + 1          # ✅ 23

# Traiter une IP comme un nombre
ip = 192.168.1.1            # ❌ SyntaxError — une IP n'est PAS un nombre
ip = "192.168.1.1"          # ✅ Une IP est du texte

# Utiliser un mot réservé comme nom de variable
class = "malware"            # ❌ "class" est un mot réservé Python
categorie = "malware"        # ✅ Correct

# Oublier le f devant la f-string
ip = "203.0.113.5"
print("Source : {ip}")      # → Source : {ip}  (les accolades s'affichent telles quelles)
print(f"Source : {ip}")     # → Source : 203.0.113.5
```

## Exercices

**Guidé :** Crée un script `profil_ip.py` qui demande une IP, un port et un protocole avec `input()`, convertit le port en entier, et affiche un résumé sous la forme `"[+] {ip}:{port} via {protocole}"` avec une f-string.

**Autonome :** Crée un script `score.py` qui demande le nombre de tentatives de connexion échouées (à convertir en entier) et affiche un score de risque calculé comme `tentatives * 0.2` (avec 1 décimale), puis le texte `"[!] Surveillance recommandée"` si tu le souhaites.

## 🧩 Mini-projet (chapitres 1-2)

Crée un script `fiche_ioc.py` qui :

1. Affiche `"=== Fiche IOC ==="`.
2. Demande une adresse IP suspecte.
3. Demande un nombre de connexions observées (converti en entier).
4. Demande un niveau de confiance entre 0 et 1 (converti en `float`).
5. Affiche une fiche récapitulative claire avec des f-strings, par exemple :
   `"[!] IOC 203.0.113.5 — 47 connexions — confiance 0.9"`.

## ✅ Tu sais maintenant…

- Créer une variable et l'afficher avec `print()` et les f-strings
- Les 4 types de base : `str`, `int`, `float`, `bool`
- Qu'une IP, un domaine, un hash sont du **texte**, mais qu'un port ou un code HTTP sont des **entiers**
- Lire une saisie utilisateur avec `input()`
- Convertir entre types avec `int()`, `float()`, `str()`
- Pourquoi `input()` renvoie toujours du texte et comment gérer ça

-----

# Chapitre 3 — Arguments, terminal et scripts paramétrés

## Le minimum à savoir

### C'est quoi un argument ?

Au chapitre 2, tu demandais des infos pendant l'exécution (avec `input()`). Mais il y a une autre façon de fournir des infos : **les arguments**, donnés au moment du lancement.

```bash
python3 analyse_ip.py 203.0.113.5
#                      ↑ c'est un argument
```

Les arguments rendent le script utilisable **sans interaction** : tu lances la commande et c'est fait. C'est **essentiel pour l'automatisation** — un script paramétré peut être appelé en boucle, depuis un autre script, ou planifié avec `cron`.

### `sys.argv` — la liste des arguments

Pour accéder aux arguments, on utilise le module `sys` et sa variable `argv` :

```python
import sys

print(sys.argv)
```

```bash
python3 test.py 203.0.113.5 evil.com 80
```

```
['test.py', '203.0.113.5', 'evil.com', '80']
```

`sys.argv` est une **liste** (vue en détail au chapitre 7). Pour l'instant, retiens :

- `sys.argv[0]` → le nom du script
- `sys.argv[1]` → le premier argument
- `sys.argv[2]` → le deuxième argument
- `len(sys.argv)` → le nombre total d'éléments (script + arguments)

```python
import sys

print(f"Script   : {sys.argv[0]}")
print(f"Cible     : {sys.argv[1]}")
print(f"Arguments : {len(sys.argv) - 1}")
```

```bash
python3 scan.py 203.0.113.5
```

```
Script   : scan.py
Cible     : 203.0.113.5
Arguments : 1
```

> **Comparaison avec Bash :** `sys.argv[1]` ≈ `$1`, `sys.argv[2]` ≈ `$2`, `len(sys.argv) - 1` ≈ `$#`. La différence : en Python les arguments sont dans une liste indexée à partir de 0, et le nom du script est `sys.argv[0]` (comme `$0`).

### Le `import` — un mot nouveau

`import sys` est ta première rencontre avec `import`. C'est un concept fondamental : **importer un module**.

Un module est un fichier contenant des fonctions et variables prêtes à l'emploi. `sys` est fourni avec Python et donne accès à des infos sur le système (arguments, version…).

La ligne `import sys` dit à Python : « charge le module `sys` ». Ensuite tu accèdes à ses fonctionnalités avec `sys.quelque_chose`.

On utilisera beaucoup de modules en cyber : `re` (regex), `hashlib` (hash), `ipaddress` (réseaux), `json`, `csv`… Le principe sera toujours le même.

> **Bonne pratique :** les `import` se mettent **tout en haut** du script.

### Vérifier qu'un argument est fourni

Un script qui attend un argument doit **toujours vérifier** qu'il a été donné, sinon Python plante avec `IndexError` :

```python
import sys

if len(sys.argv) < 2:
    print(f"[-] Erreur : donne une IP en argument.")
    print(f"Utilisation : python3 {sys.argv[0]} <ip>")
    sys.exit(1)

ip = sys.argv[1]
print(f"[+] Analyse de {ip}")
```

> **Note :** `sys.exit(1)` arrête le script avec un code d'erreur (comme `exit 1` en Bash). `sys.exit(0)` = succès. On met `sys.exit(1)` quand quelque chose ne va pas.

> **Pas de panique :** on utilise ici un `if` qu'on verra en détail au chapitre 5. La logique est intuitive : « si le nombre d'arguments est inférieur à 2, affiche un message et quitte ».

### La différence `input()` vs arguments

|`input()`                              |Arguments (`sys.argv`)                            |
|---------------------------------------|--------------------------------------------------|
|L'utilisateur tape pendant l'exécution |L'info est fournie au lancement                   |
|Pratique pour un script interactif     |Pratique pour l'automatisation                    |
|Difficile à enchaîner                  |Facile à intégrer dans un cron, un pipeline, un SOAR|

En pratique, beaucoup d'outils défensifs utilisent les arguments pour les paramètres (IP, fichier de log…) et `input()` pour une confirmation (« bloquer cette IP ? o/n »).

### Les arguments sont toujours du texte

Comme `input()`, les arguments de `sys.argv` sont **toujours des chaînes** (`str`). Si tu attends un nombre, convertis :

```python
import sys

if len(sys.argv) < 3:
    print(f"Utilisation : python3 {sys.argv[0]} <ip> <port>")
    sys.exit(1)

ip = sys.argv[1]            # reste du texte (une IP est du texte)
port = int(sys.argv[2])     # converti en entier pour comparaison
print(f"[+] {ip} sur le port {port}")
if port < 1024:
    print("[!] Port système")
```

## Très utile en pratique

### Accéder à tous les arguments d'un coup

`sys.argv[1:]` donne **tous les arguments sauf le nom du script** — très pratique pour traiter une liste d'IOC passés en ligne de commande :

```python
import sys

iocs = sys.argv[1:]
print(f"[+] {len(iocs)} IOC à traiter : {iocs}")
```

```bash
python3 traite.py 203.0.113.5 evil.com bad-domain.net
# → [+] 3 IOC à traiter : ['203.0.113.5', 'evil.com', 'bad-domain.net']
```

> **Explication :** `sys.argv[1:]` utilise le **slicing** (détaillé aux chapitres 6 et 7). `[1:]` signifie « tout à partir de la position 1 » — donc tout sauf le nom du script.

### Script complet : un outil paramétré

Un petit outil qui qualifie une cible selon un type passé en argument :

```python
import sys

if len(sys.argv) < 2:
    print(f"Utilisation : python3 {sys.argv[0]} <indicateur> [type]")
    print("Types : ip (défaut), domaine, hash")
    sys.exit(1)

indicateur = sys.argv[1]

# Si un deuxième argument est fourni, on l'utilise ; sinon "ip" par défaut
if len(sys.argv) >= 3:
    type_ioc = sys.argv[2]
else:
    type_ioc = "ip"

if type_ioc == "ip":
    print(f"[+] IOC de type IP    : {indicateur}")
elif type_ioc == "domaine":
    print(f"[+] IOC de type domaine : {indicateur}")
elif type_ioc == "hash":
    print(f"[+] IOC de type hash    : {indicateur}")
else:
    print(f"[-] Type '{type_ioc}' non reconnu.")
```

```bash
python3 ioc.py 203.0.113.5            # → [+] IOC de type IP    : 203.0.113.5
python3 ioc.py evil.com domaine       # → [+] IOC de type domaine : evil.com
python3 ioc.py d41d8cd9... hash       # → [+] IOC de type hash    : d41d8cd9...
```

## Application cyber

Voici le squelette d'un outil défensif typique : il prend **un fichier de log en argument** et vérifie qu'il a bien été fourni. C'est la base de tous les parsers de logs qu'on écrira plus loin.

```python
import sys

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
    sys.exit(1)

fichier_log = sys.argv[1]
print(f"[+] Analyse du fichier de log : {fichier_log}")
# Au chapitre 10, on apprendra à ouvrir et lire ce fichier ligne par ligne.
```

Ce schéma — *vérifier l'argument, le stocker, puis traiter* — revient dans la quasi-totalité des outils en ligne de commande, qu'ils analysent un log, calculent un hash ou interrogent une API.

## Bonus

### `argparse` — pour les outils sérieux

Pour les scripts avec beaucoup d'options (`-v`, `--output rapport.json`), Python fournit `argparse`, l'équivalent professionnel. Un aperçu :

```python
import argparse

parser = argparse.ArgumentParser(description="Analyseur d'IOC")
parser.add_argument("ioc", help="L'indicateur à analyser")
parser.add_argument("-t", "--type", default="ip", help="Type d'IOC")
args = parser.parse_args()

print(f"[+] {args.ioc} (type : {args.type})")
```

```bash
python3 outil.py 203.0.113.5 --type ip
python3 outil.py --help        # affiche l'aide automatiquement
```

C'est puissant, mais `sys.argv` suffit largement pour débuter.

## ❌ Erreur classique

```python
# Oublier de vérifier le nombre d'arguments
import sys
ip = sys.argv[1]    # ❌ IndexError si lancé sans argument

# Il faut TOUJOURS vérifier :
if len(sys.argv) < 2:
    print("[-] Argument manquant")
    sys.exit(1)

# Oublier que les arguments sont du texte
import sys
port = sys.argv[1]
double = port * 2     # ❌ "22" * 2 = "2222" (texte répété, pas un calcul)
port = int(sys.argv[1])
double = port * 2     # ✅ 44

# Confondre sys.argv[0] et sys.argv[1]
# sys.argv[0] = nom du script, sys.argv[1] = PREMIER argument
```

## Exercices

**Guidé :** Crée un script `qualifie_ip.py` qui prend une IP en argument, vérifie qu'elle est fournie, et affiche `"[+] IP à analyser : {ip}"`. Sans argument, affiche un message d'utilisation et quitte avec `sys.exit(1)`.

**Autonome :** Crée un script `ports.py` qui prend deux numéros de port en arguments, les convertit en entiers, et affiche lequel est le plus petit, lequel est le plus grand, et si l'un des deux est inférieur à 1024 (port « système »). Vérifie que les deux arguments sont fournis.

## ✅ Tu sais maintenant…

- Passer des arguments à un script (`sys.argv`) — la base des outils en ligne de commande
- Accéder aux arguments par leur position (`sys.argv[1]`, `sys.argv[2]`…)
- Récupérer tous les arguments avec `sys.argv[1:]` (ex. une liste d'IOC)
- Vérifier le nombre d'arguments avec `len(sys.argv)`
- La différence entre `input()` (interactif) et `sys.argv` (automatisation)
- Importer un module avec `import` et quitter avec `sys.exit()`

-----

# Chapitre 4 — Opérateurs, calculs et logique

## Le minimum à savoir

### Le calcul en Python

Python est un excellent calculateur, et il gère nativement les nombres à virgule :

```python
echecs = 47
fenetre = 5      # minutes

print(f"Total          : {echecs}")
print(f"Par minute     : {echecs / fenetre}")    # 9.4 (décimale !)
print(f"Par minute (entier) : {echecs // fenetre}")  # 9 (partie entière)
print(f"Reste          : {echecs % fenetre}")    # 2
print(f"Puissance      : {2 ** 10}")             # 1024
```

> **Différence majeure avec Bash :** en Python, `/` donne un résultat **décimal** (`9.4`). Pour la division entière (comme en Bash), utilise `//`. Et pas besoin de `$(( ))` — tu écris les calculs directement.

### Les opérateurs arithmétiques

| Opérateur | Signification       | Exemple  | Résultat    |
| --------- | ------------------- | -------- | ----------- |
| `+`       | Addition            | `5 + 3`  | `8`         |
| `-`       | Soustraction        | `5 - 3`  | `2`         |
| `*`       | Multiplication      | `5 * 3`  | `15`        |
| `/`       | Division (décimale) | `5 / 3`  | `1.6666...` |
| `//`      | Division entière    | `5 // 3` | `1`         |
| `%`       | Modulo (reste)      | `5 % 3`  | `2`         |
| `**`      | Puissance           | `2 ** 3` | `8`         |

### Les raccourcis d'affectation

Au lieu de `x = x + 1`, écris `x += 1`. Indispensable pour les compteurs (compter des échecs de connexion, par exemple) :

```python
echecs = 0
echecs += 1       # 1
echecs += 1       # 2
echecs += 5       # 7
```

### Les opérateurs de comparaison

Pour tester si une valeur est plus grande, plus petite, égale à une autre :

| Opérateur | Signification     | Exemple      | Résultat |
| --------- | ----------------- | ------------ | -------- |
| `==`      | Égal              | `200 == 200` | `True`   |
| `!=`      | Différent         | `404 != 200` | `True`   |
| `<`       | Inférieur         | `80 < 443`   | `True`   |
| `>`       | Supérieur         | `443 > 80`   | `True`   |
| `<=`      | Inférieur ou égal | `5 <= 5`     | `True`   |
| `>=`      | Supérieur ou égal | `8 >= 7`     | `True`   |

> **Différence avec Bash :** on utilise les symboles mathématiques (`==`, `<`, `>`) au lieu de `-eq`, `-lt`, `-gt`. Bien plus intuitif.

```python
code_http = 404
print(code_http == 200)    # False
print(code_http >= 400)    # True — c'est une erreur côté client/serveur
```

Le résultat d'une comparaison est toujours un **booléen** (`True` / `False`).

> **Ne pas confondre :** `=` **affecte** une valeur (`score = 8`), `==` **compare** (`score == 8`). C'est l'erreur la plus fréquente.

### Les opérateurs logiques

Python utilise des **mots** : `and`, `or`, `not`.

| Opérateur | Signification                     | Équivalent Bash |
| --------- | --------------------------------- | --------------- |
| `and`     | ET — les deux doivent être vraies | `&&`            |
| `or`      | OU — au moins une doit être vraie | `\|\|`          |
| `not`     | NON — inverse la condition        | `!`             |

```python
nb_echecs = 47
ip_externe = True

# Alerte si beaucoup d'échecs ET depuis l'extérieur
print(nb_echecs > 10 and ip_externe)    # True

code = 503
print(code == 502 or code == 503)        # True — erreur serveur

print(not ip_externe)                     # False
```

> **Astuce Python :** pour tester un intervalle, écriture mathématique naturelle (impossible en Bash) :

```python
port = 8080
print(1024 <= port <= 49151)    # True — port "enregistré"
```

### L'opérateur `in`

`in` teste si quelque chose est **contenu** dans autre chose. Extrêmement utile en cyber pour chercher un mot-clé dans une ligne de log :

```python
ligne = "Failed password for root from 203.0.113.5"
print("Failed password" in ligne)    # True
print("root" in ligne)               # True
print("sudo" in ligne)               # False
```

C'est un outil très puissant que Bash n'a pas sous cette forme.

## Très utile en pratique

### Priorité des opérateurs

Comme en maths, `*` passe avant `+`. En cas de doute, mets des parenthèses :

```python
score = 2 + 3 * 4     # 14 (le * d'abord)
score = (2 + 3) * 4   # 20
```

### Le modulo `%` en pratique

Le modulo donne le **reste**. Utile pour traiter une ligne sur N dans un gros log, ou détecter un nombre pair :

```python
numero_ligne = 1000
if numero_ligne % 100 == 0:
    print(f"[+] {numero_ligne} lignes traitées")
```

### Arrondir un nombre

```python
taux = 47 / 5
print(round(taux, 1))      # 9.4
print(round(taux))          # 9
```

## Application cyber — calculer un score de risque

Combinons calculs et logique pour produire un **score de risque** simple à partir de plusieurs signaux. C'est exactement le genre de logique qu'un SIEM applique pour prioriser les alertes.

```python
# Signaux observés sur une IP source
nb_echecs = 47          # tentatives de connexion échouées
ip_externe = True       # l'IP vient d'Internet (pas du réseau interne)
cible_sensible = True   # la cible est un serveur critique (ex. contrôleur de domaine)

# On construit un score sur 10
score = 0
score += nb_echecs * 0.1        # plus d'échecs = plus de risque
if ip_externe:
    score += 2
if cible_sensible:
    score += 3

# On plafonne à 10
score = min(score, 10)

print(f"[!] Score de risque : {round(score, 1)}/10")

# Décision logique
if score >= 8:
    print("[!] CRITIQUE — investigation immédiate")
elif score >= 5:
    print("[*] Moyen — à surveiller")
else:
    print("[+] Faible")
```

Résultat :

```
[!] Score de risque : 9.7/10
[!] CRITIQUE — investigation immédiate
```

On a utilisé : des calculs (`*`, `+=`), une fonction (`min`), des comparaisons (`>=`) et des conditions. Tu remarques qu'on a tout combiné — c'est le cœur de l'automatisation défensive.

## Bonus

### Les grands nombres et la lisibilité

Python gère des entiers de taille illimitée. Pour la lisibilité, on peut utiliser des underscores comme séparateurs :

```python
limite_octets = 1_000_000_000    # 1 Go, plus lisible
print(limite_octets)              # → 1000000000
```

## ❌ Erreur classique

```python
# Confondre = et ==
if score = 8:        # ❌ SyntaxError — c'est une affectation
if score == 8:       # ✅ Correct — c'est un test

# Diviser par zéro
taux = echecs / 0    # ❌ ZeroDivisionError

# Mélanger texte et nombre venant d'un argument
port = "443"
double = port * 2     # ❌ "443443" (texte répété)
double = int(port) * 2  # ✅ 886

# Comparer une IP (texte) avec < comme un nombre — n'a pas le sens attendu
print("203.0.113.5" < "203.0.113.50")   # comparaison alphabétique, pas numérique !
# (Pour comparer vraiment des IP, on utilisera le module ipaddress au chapitre 19.)
```

## Exercices

**Guidé :** Crée un script `risque.py` qui prend un nombre d'échecs de connexion en argument, le convertit en entier, calcule un score `echecs * 0.2`, et affiche `"CRITIQUE"` si le score dépasse 8, sinon `"OK"`.

**Autonome :** Crée un script `verdict_http.py` qui prend un code HTTP en argument (entier) et affiche : `"Succès"` (200-299), `"Redirection"` (300-399), `"Erreur client"` (400-499), `"Erreur serveur"` (500-599). Utilise les comparaisons et `and`.

## ✅ Tu sais maintenant…

- Faire des calculs avec les opérateurs arithmétiques
- La différence entre `/` (décimale) et `//` (entière)
- Comparer des valeurs avec `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combiner des conditions avec `and`, `or`, `not`
- Utiliser `in` pour chercher un mot-clé dans une ligne de log
- Construire un score de risque simple en combinant calculs et logique
- La différence entre `=` (affectation) et `==` (comparaison)

-----

# Chapitre 5 — Conditions

## Le minimum à savoir

### La structure `if`

```python
score = 8

if score >= 7:
    print("[!] Alerte critique")
```

Deux choses cruciales :

1. **Les deux-points `:`** à la fin de la ligne `if`
2. **L'indentation** (les espaces en début de ligne) du bloc qui suit

### L'indentation : LE concept fondamental de Python

En Bash, les blocs sont délimités par des mots-clés (`then`/`fi`). **En Python, c'est l'indentation qui délimite les blocs.** Pas de `fi`, pas d'accolades : c'est l'alignement du texte qui dit « ce code fait partie de ce bloc ».

```python
if score >= 7:
    print("[!] Alerte critique")     # ← indenté = dans le if
    print("[!] Notification envoyée") # ← indenté = aussi dans le if
print("Fin de l'analyse")             # ← pas indenté = toujours exécuté
```

> **C'est le concept le plus important de Python pour un débutant.** Si tu comprends l'indentation, tu comprends Python.

**Les règles :**

- **4 espaces** par niveau d'indentation (standard Python)
- Tout le code d'un même bloc a **exactement** le même niveau
- Ne mélange **jamais** tabulations et espaces (configure ton éditeur pour convertir les tabs en 4 espaces)

```python
# ❌ Erreur — pas d'indentation
if score >= 7:
print("Alerte")        # IndentationError !
```

> **Conseil :** utilise un éditeur (VS Code) qui indente automatiquement après le `:`.

### `if...else`

```python
ip_externe = True

if ip_externe:
    print("[!] Connexion depuis Internet")
else:
    print("[+] Connexion interne")
```

> **Note :** `else` est au même niveau que `if`, avec ses propres deux-points `:`.

### `if...elif...else`

```python
code = 404

if code < 300:
    print("[+] Succès")
elif code < 400:
    print("[*] Redirection")
elif code < 500:
    print("[-] Erreur client")
else:
    print("[!] Erreur serveur")
```

`elif` = « else if ». Autant de `elif` que tu veux, mais un seul `else` (à la fin).

### Les tests les plus courants

```python
# Tester un nombre
if nb_echecs > 10:
    print("[!] Trop d'échecs")

# Tester l'égalité d'une chaîne
if statut == "malveillant":
    print("[!] À bloquer")

# Tester une chaîne vide
ligne = ""
if ligne == "":
    print("Ligne vide, ignorée")

# Plus pythonique :
if not ligne:
    print("Ligne vide, ignorée")

# Tester un mot-clé dans une ligne de log
if "Failed password" in ligne_log:
    print("[!] Tentative de connexion échouée")
```

### Combiner des conditions

```python
nb_echecs = 47
ip_externe = True

# ET
if nb_echecs > 10 and ip_externe:
    print("[!] Attaque par force brute probable")

# OU
if code == 502 or code == 503:
    print("[!] Service indisponible")

# NON
if not ip_externe:
    print("[+] Source interne")
```

## Très utile en pratique

### Les valeurs « falsy » et « truthy »

Certaines valeurs sont considérées comme « fausses » dans un test, sans comparaison explicite :

|Valeur            |Considérée comme|
|------------------|----------------|
|`False`           |Faux            |
|`0`               |Faux            |
|`""` (chaîne vide)|Faux            |
|`[]` (liste vide) |Faux            |
|`None`            |Faux            |
|Tout le reste     |Vrai            |

Ça rend les tests très lisibles :

```python
iocs_trouves = []

if iocs_trouves:        # équivalent de : if len(iocs_trouves) > 0
    print(f"[!] {len(iocs_trouves)} IOC trouvés")
else:
    print("[+] Aucun IOC, log propre")
```

### Conditions imbriquées

Un `if` dans un `if` — chaque niveau ajoute 4 espaces :

```python
if ip_externe:
    if nb_echecs > 50:
        print("[!] Force brute massive depuis l'extérieur")
    elif nb_echecs > 10:
        print("[*] Activité suspecte")
    else:
        print("[+] Activité normale")
else:
    print("[+] Trafic interne")
```

> **Conseil :** si tu dépasses 2-3 niveaux imbriqués, simplifie (souvent en combinant avec `and`/`or`).

### L'opérateur ternaire (condition en une ligne)

```python
score = 9
verdict = "CRITIQUE" if score >= 8 else "normal"
print(verdict)    # → CRITIQUE
```

Pratique pour une affectation courte ; pour une logique complexe, garde un `if`/`else` classique.

## Application cyber — trier une ligne de log

Voici un mini-trieur qui classe une ligne de log selon son contenu. C'est le cœur de tout détecteur : *observer un signal, décider d'une catégorie*.

```python
ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5"

if "Failed password" in ligne and "root" in ligne:
    niveau = "CRITIQUE"
    raison = "Échec de connexion sur le compte root"
elif "Failed password" in ligne:
    niveau = "ALERTE"
    raison = "Échec de connexion"
elif "Accepted password" in ligne:
    niveau = "INFO"
    raison = "Connexion réussie"
else:
    niveau = "IGNORÉ"
    raison = "Aucun signal connu"

print(f"[{niveau}] {raison}")
```

Résultat :

```
[CRITIQUE] Échec de connexion sur le compte root
```

On combine ici `in` (chercher un mot-clé), `and` (deux conditions), et `if/elif/else` (décider la catégorie). C'est *littéralement* ce que fait un règle de détection.

## Bonus

### Le `match/case` (Python 3.10+)

> **Attention :** nécessite **Python 3.10 minimum** (`python3 --version`). Sinon, ignore cette section : les `if/elif` font la même chose.

```python
commande = input("Action (analyser/bloquer/quitter) : ")

match commande:
    case "analyser":
        print("[+] Analyse en cours")
    case "bloquer":
        print("[!] IP ajoutée à la liste de blocage")
    case "quitter":
        print("Au revoir")
    case _:
        print(f"[-] Action '{commande}' inconnue")
```

Le `_` est le cas par défaut. Les `if/elif` restent la méthode universelle.

## ❌ Erreur classique

```python
# Oublier les deux-points
if score >= 8         # ❌ SyntaxError — il manque le ":"
    print("Alerte")

# Indentation manquante
if score >= 8:
print("Alerte")       # ❌ IndentationError

# Utiliser = au lieu de ==
if statut = "malveillant":   # ❌ SyntaxError — affectation au lieu de test
if statut == "malveillant":  # ✅ Correct

# Oublier que "in" est sensible à la casse
ligne = "FAILED PASSWORD"
if "Failed password" in ligne:   # ❌ Ne matche pas (casse différente)
    print("Détecté")
if "failed password" in ligne.lower():  # ✅ On normalise d'abord (chapitre 6)
    print("Détecté")
```

## Exercices

**Guidé :** Crée un script `triage.py` qui prend un code HTTP en argument et affiche un verdict : `"[+] OK"` (200-299), `"[*] Redirection"` (300-399), `"[-] Erreur client"` (400-499), `"[!] Erreur serveur"` (500+).

**Autonome :** Crée un script `verif_ligne.py` qui prend une ligne de log en argument (entre guillemets) et affiche `"[!] SUSPECT"` si elle contient `"Failed password"` **ou** `"Invalid user"`, sinon `"[+] RAS"`.

## 🧩 Mini-projet (chapitres 3-5)

Crée un script `port_scanner_verdict.py` (sans rien scanner — on raisonne juste sur une valeur) qui :

1. Prend un numéro de port en argument et le convertit en entier.
2. Affiche `"port système"` (< 1024), `"port enregistré"` (1024-49151) ou `"port dynamique"` (> 49151).
3. Affiche en plus `"[!] Service sensible"` si le port est 22, 23, 3389 ou 445 (utilise `in` avec une liste, qu'on verra au chapitre 7 — ici tu peux enchaîner des `or`).

## ✅ Tu sais maintenant…

- Écrire des conditions avec `if`, `elif`, `else`
- L'indentation comme structure de bloc (4 espaces par niveau)
- Les deux-points `:` après chaque `if`, `elif`, `else`
- Combiner des conditions avec `and`, `or`, `not`
- Les valeurs « falsy » (chaîne vide, 0, liste vide, None)
- Classer une ligne de log selon son contenu (base d'une règle de détection)

-----

# Chapitre 6 — Chaînes de caractères

## Le minimum à savoir

### Les chaînes sont des séquences

Une chaîne (`str`) n'est pas un bloc opaque : c'est une **séquence ordonnée de caractères**, chacun accessible par sa position (son **index**).

```
 Texte :   e    v    i    l
 Index :   0    1    2    3
 Négatif: -4   -3   -2   -1
```

```python
domaine = "evil.com"

print(domaine[0])      # e (premier)
print(domaine[-1])     # m (dernier)
print(domaine[-3])     # c
```

> **Rappel :** les index commencent à **0**.

### Longueur d'une chaîne

```python
hash_md5 = "d41d8cd98f00b204e9800998ecf8427e"
print(len(hash_md5))    # 32 — un MD5 fait toujours 32 caractères hexadécimaux
```

Mesurer la longueur d'un hash est une première vérification utile : 32 → MD5, 40 → SHA-1, 64 → SHA-256.

### Le slicing : extraire une partie

Syntaxe `[début:fin]` (de `début` **inclus** à `fin` **exclu**) :

```python
url = "https://evil.com/malware.exe"

print(url[0:5])     # "https"
print(url[8:16])    # "evil.com"
print(url[:5])      # "https"   (du début à 4)
print(url[8:])      # "evil.com/malware.exe"  (de 8 à la fin)
```

Slicing avec un **pas** :

```python
texte = "abcdef"
print(texte[::-1])     # "fedcba" — inverser la chaîne
```

### Les méthodes essentielles

Les chaînes ont des **méthodes** : des fonctions appelées avec un point.

```python
ligne = "  Failed Password For ROOT  "

print(ligne.upper())        # "  FAILED PASSWORD FOR ROOT  "
print(ligne.lower())        # "  failed password for root  "
print(ligne.strip())        # "Failed Password For ROOT" (espaces enlevés)
print(ligne.strip().lower()) # "failed password for root"
print(ligne.replace("ROOT", "[REDACTED]").strip())  # "Failed Password For [REDACTED]"
```

> **Différence avec Bash :** au lieu de `${var^^}` ou `${var/ancien/nouveau}`, on utilise des **méthodes** : `var.upper()`, `var.replace()`. Plus lisible.

> **Réflexe cyber :** avant de comparer du texte (un domaine, un mot-clé), on **normalise** souvent avec `.lower()` et `.strip()`, car `Evil.COM`, `evil.com` et `  evil.com ` désignent la même chose.

### Découper et joindre

```python
# split : découper en liste
ioc_brut = "203.0.113.5,evil.com,bad.net"
iocs = ioc_brut.split(",")
print(iocs)      # ['203.0.113.5', 'evil.com', 'bad.net']

# join : recoller une liste en chaîne
print(" | ".join(iocs))   # "203.0.113.5 | evil.com | bad.net"
```

`split()` sans argument découpe sur les espaces — parfait pour séparer les champs d'une ligne de log :

```python
ligne = "203.0.113.5 - - [10/Jan/2025] GET /admin"
champs = ligne.split()
print(champs[0])    # "203.0.113.5" — l'IP est le premier champ
```

### Chercher dans une chaîne

```python
ligne = "Failed password for root from 203.0.113.5"

print("root" in ligne)              # True
print(ligne.find("from"))           # 26 (position) ; -1 si absent
print(ligne.count("o"))             # nombre de 'o'

fichier = "facture.pdf.exe"
print(fichier.endswith(".exe"))     # True — extension exécutable, suspect !
print(fichier.startswith("facture")) # True
```

### Les chaînes sont immuables

On ne peut **pas** modifier une chaîne directement :

```python
mot = "evil"
mot[0] = "E"       # ❌ TypeError
```

Pour « modifier », on crée une **nouvelle** chaîne (`replace`, `upper`, etc. renvoient toujours une nouvelle chaîne).

## Très utile en pratique

### Les f-strings avancées (alignement, décimales)

Utile pour produire des rapports lisibles :

```python
ip = "203.0.113.5"
nb = 47
print(f"{ip:<18} {nb:>5} échecs")    # IP alignée à gauche, nombre à droite
# → 203.0.113.5            47 échecs

numero = 42
print(f"Alerte #{numero:04d}")        # "Alerte #0042"
```

### Tableau récapitulatif des méthodes

| Méthode           | Effet                        | Exemple cyber                       |
| ----------------- | ---------------------------- | ----------------------------------- |
| `len(s)`          | Longueur                     | `len(hash)` → 32 / 40 / 64          |
| `s.upper()`       | Majuscules                   | normaliser un hash                  |
| `s.lower()`       | Minuscules                   | normaliser un domaine               |
| `s.strip()`       | Enlever espaces début/fin    | nettoyer une ligne lue              |
| `s.replace(a, b)` | Remplacer                    | anonymiser une IP dans un rapport   |
| `s.split(sep)`    | Découper en liste            | séparer les champs d'un log         |
| `sep.join(liste)` | Recoller une liste           | produire une ligne CSV              |
| `s.find(x)`       | Position de x (-1 si absent) | localiser un mot-clé                |
| `s.count(x)`      | Nombre d'occurrences         | compter les `Failed` dans une ligne |
| `s.startswith(x)` | Commence par x ?             | `url.startswith("http")`            |
| `s.endswith(x)`   | Finit par x ?                | `fichier.endswith(".exe")`          |
| `s.isdigit()`     | Que des chiffres ?           | valider un port saisi               |

## Application cyber — normaliser et inspecter un IOC

Un même indicateur peut arriver sous plusieurs formes. Normalisons un domaine et extrayons des infos d'une URL.

```python
# Normaliser un domaine (sources hétérogènes)
domaine_brut = "  EVIL.com  "
domaine = domaine_brut.strip().lower()
print(domaine)                  # "evil.com"

# Inspecter une URL simplement (sans regex, pour l'instant)
url = "https://evil.com/login.php?id=1"

print(url.startswith("https"))  # True — connexion chiffrée
print(".exe" in url)            # False
print("evil.com" in url)        # True — domaine connu malveillant

# Extraire grossièrement le domaine d'une URL
sans_schema = url.replace("https://", "").replace("http://", "")
domaine_url = sans_schema.split("/")[0]
print(domaine_url)              # "evil.com"
```

Ici, on a transformé `"  EVIL.com  "` en `"evil.com"` (comparable de façon fiable) et extrait le domaine d'une URL avec `replace` + `split`. Au chapitre 13, les regex rendront ce genre d'extraction beaucoup plus robuste — mais ces méthodes de base suffisent déjà pour beaucoup de cas.

## Bonus

### Les caractères d'échappement

```python
print("Ligne1\nLigne2")          # \n = retour à la ligne
print("Champ1\tChamp2")          # \t = tabulation
print("Chemin : C:\\Windows")    # \\ = un seul backslash
```

### Les raw strings (chemins Windows)

```python
chemin = r"C:\Users\Public\malware.exe"   # le r empêche l'interprétation des \
print(chemin)   # C:\Users\Public\malware.exe
```

Indispensable quand tu manipules des chemins Windows dans un contexte forensic.

## ❌ Erreur classique

```python
# Essayer de modifier une chaîne
empreinte = "abc"
empreinte[0] = "A"     # ❌ TypeError — les chaînes sont immuables

# Comparer sans normaliser
if "evil.com" == "Evil.com":   # ❌ False (casse différente)
    pass
if "evil.com" == "Evil.com".lower():  # ✅ True

# Oublier que find() renvoie -1 (pas une erreur) si absent
pos = "log normal".find("Failed")
print(pos)             # -1 — pas trouvé, mais pas d'erreur

# Confondre fonction et méthode
len("abc")             # ✅ fonction
"abc".upper()          # ✅ méthode
"abc".len()            # ❌ len n'est pas une méthode
```

## Exercices

**Guidé :** Crée un script `reformat_ip.py` qui prend une IP avec des tirets (`203-0-113-5`) en argument et l'affiche reformatée avec des points (`203.0.113.5`). Utilise `.replace()`.

**Autonome :** Crée un script `inspect_url.py` qui prend une URL en argument et affiche : son schéma (`http`/`https` via `startswith`), si elle se termine par une extension exécutable (`.exe`, `.scr`), le domaine (via `replace` + `split`), et la longueur totale de l'URL.

## ✅ Tu sais maintenant…

- Accéder aux caractères par index (`mot[0]`, `mot[-1]`) et au slicing (`url[8:16]`, `[::-1]`)
- Les méthodes clés : `upper`, `lower`, `strip`, `replace`, `split`, `join`, `find`, `count`, `startswith`, `endswith`
- Normaliser un IOC (`.strip().lower()`) avant de le comparer
- Découper une ligne de log en champs avec `split()`
- Que les chaînes sont immuables (on crée une nouvelle chaîne)

-----

# Chapitre 7 — Listes et boucles

## Le minimum à savoir

### Qu'est-ce qu'une liste ?

Une liste est une **collection ordonnée de valeurs**, modifiable. C'est la structure la plus utilisée en Python — idéale pour stocker une série d'IOC, des lignes de log, des IP à bloquer.

```python
ips_suspectes = ["203.0.113.5", "198.51.100.9", "203.0.113.7"]
ports_sensibles = [22, 23, 445, 3389]
vide = []
```

### Accéder aux éléments

```python
ips = ["203.0.113.5", "198.51.100.9"]

print(ips[0])       # "203.0.113.5" (premier)
print(ips[-1])      # "198.51.100.9" (dernier)
print(len(ips))     # 2
```

### Modifier, ajouter, supprimer

```python
ips = ["203.0.113.5", "198.51.100.9"]

ips.append("203.0.113.7")    # ajouter à la fin
print(ips)   # ['203.0.113.5', '198.51.100.9', '203.0.113.7']

ips.remove("198.51.100.9")   # supprimer par valeur
print(ips)   # ['203.0.113.5', '203.0.113.7']

derniere = ips.pop()         # supprimer le dernier et le récupérer
print(derniere)              # "203.0.113.7"
```

### Tester l'appartenance

```python
liste_noire = ["203.0.113.5", "198.51.100.9"]

print("203.0.113.5" in liste_noire)    # True — IP connue malveillante
print("8.8.8.8" in liste_noire)        # False
```

C'est l'opérateur `in` du chapitre 4, qui marche aussi sur les listes. C'est exactement comme ça qu'on vérifie une IP contre une liste de blocage.

### Trier et dédoublonner

```python
ports = [443, 22, 80, 22, 8080]

ports.sort()              # trie la liste elle-même
print(ports)              # [22, 22, 80, 443, 8080]

uniques = sorted(set(ports))   # set() supprime les doublons, sorted() trie
print(uniques)            # [22, 80, 443, 8080]
```

> **Astuce cyber :** `set(liste)` enlève les doublons. Très pratique pour obtenir la liste des IP **uniques** vues dans un log.

### Le slicing sur les listes

Comme pour les chaînes :

```python
iocs = ["a", "b", "c", "d", "e"]
print(iocs[:3])     # ['a', 'b', 'c'] (les 3 premiers)
print(iocs[-2:])    # ['d', 'e'] (les 2 derniers)
```

-----

## Les boucles

### La boucle `for` : parcourir une liste

```python
ips = ["203.0.113.5", "198.51.100.9", "203.0.113.7"]

for ip in ips:
    print(f"[+] Analyse de {ip}")
```

```
[+] Analyse de 203.0.113.5
[+] Analyse de 198.51.100.9
[+] Analyse de 203.0.113.7
```

La variable `ip` prend successivement chaque valeur. L'indentation (4 espaces) délimite le bloc répété.

> **Comparaison avec Bash :** `for ip in "${ips[@]}"; do ... done` → en Python : `for ip in ips:` + bloc indenté. Plus court, pas de `do`/`done`.

### `range()` : générer une séquence de nombres

```python
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

for port in range(20, 23):
    print(port)        # 20, 21, 22
```

> **Attention :** `range(20, 23)` va de 20 à **22** (borne supérieure exclue).

### La boucle `while`

Répète tant qu'une condition est vraie :

```python
tentatives = 0

while tentatives < 3:
    print(f"Tentative {tentatives + 1}")
    tentatives += 1
```

> **Attention :** si tu oublies `tentatives += 1`, la boucle tourne **à l'infini**. `Ctrl+C` pour l'arrêter.

### `break` et `continue`

```python
# break — sortir de la boucle dès qu'on trouve
liste_noire = ["203.0.113.5", "198.51.100.9"]
for ip in liste_noire:
    if ip == "198.51.100.9":
        print("[!] IP recherchée trouvée, on arrête")
        break

# continue — sauter au tour suivant
for ligne in ["INFO ok", "", "ERROR fail", ""]:
    if not ligne:          # ligne vide
        continue           # on l'ignore
    print(f"Traitée : {ligne}")
```

### `enumerate()` : avoir l'index ET la valeur

Très pratique pour numéroter les lignes d'un log :

```python
lignes = ["connexion ok", "echec auth", "connexion ok"]

for numero, ligne in enumerate(lignes, start=1):
    print(f"Ligne {numero} : {ligne}")
```

```
Ligne 1 : connexion ok
Ligne 2 : echec auth
Ligne 3 : connexion ok
```

## Très utile en pratique

### Construire une liste dans une boucle (filtrer)

Le pattern le plus fréquent en analyse de logs : parcourir, tester, garder ce qui nous intéresse.

```python
lignes = [
    "Accepted password for alice",
    "Failed password for root",
    "Failed password for admin",
    "Accepted password for bob",
]

echecs = []                      # liste vide au départ
for ligne in lignes:
    if "Failed password" in ligne:
        echecs.append(ligne)     # on garde les échecs

print(f"[!] {len(echecs)} échec(s) détecté(s)")
for e in echecs:
    print(f"    {e}")
```

### La boucle infinie volontaire (menu d'outil)

```python
while True:
    action = input("Action (analyser/quitter) : ")
    if action == "quitter":
        print("Au revoir")
        break
    print(f"[+] Action : {action}")
```

### Compter avec un dictionnaire (aperçu)

On verra les dictionnaires au chapitre 9, mais voici un avant-goût : compter combien de fois chaque IP apparaît.

```python
ips = ["203.0.113.5", "198.51.100.9", "203.0.113.5", "203.0.113.5"]

compteur = {}
for ip in ips:
    compteur[ip] = compteur.get(ip, 0) + 1

print(compteur)   # {'203.0.113.5': 3, '198.51.100.9': 1}
```

## Application cyber — compter les échecs par IP

Combinons tout : parcourir des lignes de log, extraire l'IP, et compter les échecs par IP. C'est un mini-détecteur de force brute.

```python
lignes = [
    "Failed password for root from 203.0.113.5",
    "Failed password for admin from 203.0.113.5",
    "Accepted password for alice from 10.0.0.4",
    "Failed password for root from 203.0.113.5",
    "Failed password for root from 198.51.100.9",
]

echecs_par_ip = {}

for ligne in lignes:
    if "Failed password" in ligne:
        # L'IP est le dernier champ de la ligne
        ip = ligne.split()[-1]
        echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

print("[*] Échecs de connexion par IP :")
for ip, nb in echecs_par_ip.items():
    marqueur = "[!]" if nb >= 3 else "   "
    print(f"  {marqueur} {ip} : {nb} échec(s)")
```

Résultat :

```
[*] Échecs de connexion par IP :
   [!] 203.0.113.5 : 3 échec(s)
       198.51.100.9 : 1 échec(s)
```

On a utilisé : une boucle `for`, le test `in`, `split()` pour isoler l'IP, et un compteur. L'IP `203.0.113.5` avec 3 échecs est marquée `[!]` — c'est une candidate au blocage. Ce petit script est déjà un vrai outil défensif.

## Bonus

### Les compréhensions de liste

Syntaxe compacte pour filtrer/transformer une liste :

```python
lignes = ["Failed root", "Accepted alice", "Failed admin"]

# Au lieu d'une boucle + append :
echecs = [l for l in lignes if "Failed" in l]
print(echecs)    # ['Failed root', 'Failed admin']
```

Puissant et élégant, mais la boucle classique reste parfaitement correcte pour débuter.

### Les tuples — les listes immuables

Un **tuple** est comme une liste mais **non modifiable** (parenthèses au lieu de crochets). Utile pour un couple de valeurs fixes, comme une paire (IP, port) :

```python
cible = ("203.0.113.5", 22)
print(cible[0])    # "203.0.113.5"
cible[0] = "x"     # ❌ TypeError — un tuple ne se modifie pas
```

## ❌ Erreur classique

```python
# Oublier l'indentation dans la boucle
for ip in ips:
print(ip)              # ❌ IndentationError

# Modifier une liste qu'on parcourt (dangereux)
ips = ["a", "b", "c"]
for ip in ips:
    if ip == "b":
        ips.remove(ip)    # ❌ comportement imprévisible
# Solution : construire une nouvelle liste filtrée

# Boucle infinie par oubli d'incrément
n = 0
while n < 5:
    print(n)
    # ❌ oubli de n += 1 → boucle infinie

# Dépasser les bornes de la liste
ips = ["a", "b"]
print(ips[5])          # ❌ IndexError: list index out of range
```

## Exercices

**Guidé :** Crée un script `bloquer.py` qui contient une liste d'IP en liste noire, prend une IP en argument, et affiche `"[!] IP bloquée"` si elle est dans la liste, sinon `"[+] IP autorisée"`.

**Autonome :** Crée un script `iocs_uniques.py` qui prend plusieurs IOC en arguments (`sys.argv[1:]`), supprime les doublons (avec `set`), les trie, et les affiche numérotés avec `enumerate`.

**Défi :** Crée un script `top_ip.py` qui contient une liste de lignes de log (en dur), compte les échecs par IP (comme dans l'« Application cyber »), et affiche uniquement les IP ayant **3 échecs ou plus**.

## 🧩 Mini-projet (chapitres 5-7)

Crée un script `mini_soc.py` qui :

1. Contient une liste de lignes de log (en dur dans le script).
2. Parcourt les lignes et compte : le nombre total de lignes, le nombre d'échecs (`Failed password`), le nombre de connexions réussies (`Accepted password`).
3. Construit la liste des IP **uniques** ayant échoué.
4. Affiche un petit rapport résumé avec ces chiffres.

## ✅ Tu sais maintenant…

- Créer, modifier et parcourir une liste (`append`, `remove`, `pop`)
- Tester l'appartenance avec `in` (ex. IP contre une liste noire)
- Trier (`sort`, `sorted`) et dédoublonner (`set`)
- Parcourir avec `for ... in ...:` et générer des nombres avec `range()`
- Répéter avec `while`, contrôler avec `break` et `continue`
- Numéroter avec `enumerate()`
- Filtrer des lignes de log et compter par IP — un vrai mini-détecteur

-----

# Chapitre 8 — Fonctions

## Le minimum à savoir

### Qu'est-ce qu'une fonction ?

Une fonction est un **bloc de code réutilisable** auquel tu donnes un nom. En cyber, on encapsule souvent une vérification (« cette extension est-elle dangereuse ? », « cette IP est-elle privée ? ») dans une fonction qu'on réutilise partout.

### Définir et appeler une fonction

```python
def afficher_banniere():
    print("=" * 30)
    print("   Outil SOC v1.0")
    print("=" * 30)

afficher_banniere()
```

> **Note :** on utilise `def` (« define ») + nom + parenthèses + `:`. Le bloc est indenté. Pas d'accolades — c'est l'indentation qui délimite.

> **Règle :** la définition (`def ...`) doit apparaître **avant** l'appel. Python lit le fichier de haut en bas.

### Passer des arguments

```python
def analyser_ip(ip):
    print(f"[+] Analyse de {ip} en cours...")

analyser_ip("203.0.113.5")
analyser_ip("198.51.100.9")
```

> **Différence avec Bash :** en Bash, les arguments d'une fonction étaient `$1`, `$2`. En Python, chaque argument a un **nom clair** (`ip`). Bien plus lisible.

### Retourner un résultat avec `return`

`return` renvoie une valeur au code appelant. C'est ce qui rend une fonction réutilisable dans une condition.

```python
def is_suspicious_extension(nom_fichier):
    extensions_dangereuses = [".exe", ".scr", ".bat", ".js", ".vbs"]
    for ext in extensions_dangereuses:
        if nom_fichier.lower().endswith(ext):
            return True
    return False

print(is_suspicious_extension("facture.pdf.exe"))   # True
print(is_suspicious_extension("rapport.pdf"))        # False

# On l'utilise dans une condition :
if is_suspicious_extension("invoice.scr"):
    print("[!] Fichier potentiellement dangereux")
```

> **Différence majeure avec Bash :** en Bash, `return` ne sert qu'aux codes d'erreur (0-255). En Python, `return` renvoie **n'importe quelle valeur** (un booléen, du texte, une liste…).

Après un `return`, Python sort de la fonction immédiatement.

### Valeurs par défaut

```python
def normaliser_domaine(domaine, en_minuscules=True):
    domaine = domaine.strip()
    if en_minuscules:
        domaine = domaine.lower()
    return domaine

print(normaliser_domaine("  EVIL.com "))        # "evil.com"
print(normaliser_domaine("EVIL.com", False))    # "EVIL.com" (juste strip)
```

Les paramètres avec valeur par défaut viennent **après** les paramètres obligatoires.

### Portée des variables (locale par défaut)

Une variable créée **dans** une fonction n'existe que **dans** cette fonction :

```python
def verifier():
    verdict = "malveillant"     # variable locale
    print(verdict)

verifier()
print(verdict)     # ❌ NameError — "verdict" n'existe pas ici
```

> **Différence avec Bash :** en Bash, les variables d'une fonction sont globales par défaut. En Python, c'est l'inverse : **locales par défaut**. C'est plus sûr.

## Très utile en pratique

### Retourner plusieurs valeurs

```python
def analyser_ligne(ligne):
    champs = ligne.split()
    ip = champs[-1]
    est_echec = "Failed password" in ligne
    return ip, est_echec

ip, echec = analyser_ligne("Failed password for root from 203.0.113.5")
print(ip)      # "203.0.113.5"
print(echec)   # True
```

Python renvoie un **tuple** qu'on « décompacte » dans plusieurs variables.

### Une fonction utile : `is_private_ip()`

Une IP privée (réseau interne) commence par `10.`, `192.168.` ou `172.16.`–`172.31.`. Voici une version simple (on fera mieux avec `ipaddress` au chapitre 19) :

```python
def is_private_ip(ip):
    if ip.startswith("10.") or ip.startswith("192.168."):
        return True
    if ip.startswith("172."):
        # 172.16.x.x à 172.31.x.x
        deuxieme = int(ip.split(".")[1])
        if 16 <= deuxieme <= 31:
            return True
    return False

print(is_private_ip("10.0.0.4"))       # True (interne)
print(is_private_ip("203.0.113.5"))    # False (publique → vient d'Internet)
```

Savoir si une IP est privée ou publique est fondamental : une attaque venant d'une IP **publique** est généralement plus préoccupante.

### Documenter avec une docstring

```python
def calculer_score(nb_echecs, ip_externe):
    """Calcule un score de risque sur 10.

    Arguments :
        nb_echecs : nombre de connexions échouées (int)
        ip_externe : True si l'IP vient d'Internet (bool)
    Retourne : le score arrondi (float)
    """
    score = nb_echecs * 0.1
    if ip_externe:
        score += 2
    return min(round(score, 1), 10)
```

La docstring (entre `"""..."""`) documente la fonction. Accessible avec `help(calculer_score)`.

### Des fonctions qui s'appellent entre elles

```python
def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.")

def qualifier_ip(ip):
    if is_private_ip(ip):
        return f"{ip} → interne"
    return f"{ip} → EXTERNE (à surveiller)"

print(qualifier_ip("10.0.0.4"))        # 10.0.0.4 → interne
print(qualifier_ip("203.0.113.5"))     # 203.0.113.5 → EXTERNE (à surveiller)
```

## Application cyber — une petite boîte à fonctions défensives

Regroupons des vérifications réutilisables. C'est ainsi qu'on construit, brique par brique, une bibliothèque d'analyse.

```python
def normalize_domain(domaine):
    """Met un domaine en forme comparable."""
    return domaine.strip().lower().rstrip(".")

def is_suspicious_extension(nom):
    """True si le fichier a une extension exécutable courante."""
    dangereuses = (".exe", ".scr", ".bat", ".cmd", ".js", ".vbs")
    return nom.lower().endswith(dangereuses)

def is_private_ip(ip):
    """True si l'IP appartient à une plage privée (simplifié)."""
    return ip.startswith("10.") or ip.startswith("192.168.")

# Utilisation combinée
print(normalize_domain("  Evil.COM. "))          # "evil.com"
print(is_suspicious_extension("photo.jpg.exe"))  # True
print(is_private_ip("203.0.113.5"))              # False
```

Astuce : `nom.endswith(dangereuses)` accepte directement un **tuple** d'extensions — pas besoin de boucle. Ces trois fonctions sont la base d'outils plus gros qu'on assemblera aux chapitres 14-15.

## Bonus

### Les arguments nommés

```python
def creer_alerte(ip, niveau, raison):
    return f"[{niveau}] {ip} — {raison}"

# L'ordre n'importe plus si on nomme les arguments :
print(creer_alerte(raison="force brute", ip="203.0.113.5", niveau="CRITIQUE"))
```

### Le nombre variable d'arguments (`*args`)

```python
def compter_iocs(*iocs):
    return len(iocs)

print(compter_iocs("203.0.113.5", "evil.com"))    # 2
print(compter_iocs("a", "b", "c", "d"))           # 4
```

`*iocs` collecte tous les arguments dans un tuple (équivalent du `$@` de Bash).

## ❌ Erreur classique

```python
# Oublier les parenthèses à l'appel
afficher_banniere        # ❌ ne fait rien (référence, pas appel)
afficher_banniere()      # ✅ appelle la fonction

# Oublier return
def is_dangereux(nom):
    nom.endswith(".exe")    # ❌ calcule mais ne retourne rien
resultat = is_dangereux("x.exe")
print(resultat)              # None

def is_dangereux(nom):
    return nom.endswith(".exe")   # ✅

# Mettre du code après return (jamais exécuté)
def f():
    return True
    print("jamais affiché")    # ⚠️ code mort

# Croire qu'une variable locale modifie la globale
total = 0
def ajouter(n):
    total = total + n    # ❌ UnboundLocalError
```

## Exercices

**Guidé :** Crée une fonction `is_blacklisted(ip, liste_noire)` qui retourne `True` si l'IP est dans la liste noire. Teste-la avec une petite liste et deux IP.

**Autonome :** Crée une fonction `hash_type(h)` qui retourne `"MD5"`, `"SHA-1"`, `"SHA-256"` ou `"inconnu"` selon la **longueur** du hash (32, 40, 64). Teste-la sur trois hash de longueurs différentes.

## ✅ Tu sais maintenant…

- Définir une fonction avec `def` et l'appeler
- Passer des arguments (avec noms clairs) et des valeurs par défaut
- Retourner un résultat avec `return` (y compris plusieurs valeurs), utilisable dans une condition
- Écrire des fonctions défensives réutilisables (`is_suspicious_extension`, `normalize_domain`, `is_private_ip`)
- La portée locale des variables
- Documenter avec une docstring

-----

# Chapitre 9 — Dictionnaires

## Le minimum à savoir

### Qu'est-ce qu'un dictionnaire ?

Un dictionnaire stocke des **paires clé-valeur** : tu cherches une clé et tu trouves sa valeur. En cyber, c'est l'outil parfait pour représenter une **alerte**, un **événement SIEM** ou une **fiche IOC** : chaque info a un nom.

```python
alerte = {
    "ip_source": "203.0.113.5",
    "port": 22,
    "type": "ssh_bruteforce",
    "severite": "haute",
    "nb_echecs": 47
}
```

> **Comparaison avec Bash :** équivalent des tableaux associatifs (`declare -A`), mais natif et omniprésent en Python.

### Accéder à une valeur

```python
print(alerte["ip_source"])     # "203.0.113.5"
print(alerte["severite"])      # "haute"
```

Si la clé n'existe pas → erreur `KeyError`. Pour éviter ça, utilise `.get()` :

```python
print(alerte["pays"])               # ❌ KeyError
print(alerte.get("pays"))           # None (pas d'erreur)
print(alerte.get("pays", "inconnu")) # "inconnu" (valeur par défaut)
```

> **Réflexe cyber :** les données venant d'un log ou d'une API sont souvent incomplètes. Utilise `.get(clé, défaut)` plutôt que `[clé]` pour ne pas planter sur un champ manquant.

### Ajouter et modifier

```python
alerte["pays"] = "RU"            # ajouter une clé
alerte["severite"] = "critique"  # modifier une valeur existante
```

### Supprimer

```python
del alerte["port"]               # supprimer une paire
valeur = alerte.pop("nb_echecs") # supprimer et récupérer
```

### Vérifier si une clé existe

```python
print("ip_source" in alerte)     # True
print("hash" in alerte)          # False
```

> **Note :** `in` teste les **clés**, pas les valeurs.

### Parcourir un dictionnaire

```python
alerte = {"ip": "203.0.113.5", "port": 22, "type": "ssh"}

# Les paires clé-valeur (le plus utile)
for cle, valeur in alerte.items():
    print(f"{cle} : {valeur}")
```

```
ip : 203.0.113.5
port : 22
type : ssh
```

La méthode `.items()` donne clés et valeurs ensemble — idéale pour afficher une fiche complète.

## Très utile en pratique

### Le dictionnaire comme fiche IOC

```python
ioc = {
    "valeur": "203.0.113.5",
    "type": "ip",
    "source": "feed_interne",
    "confiance": 0.9,
    "actif": True
}

print(f"[{ioc['type'].upper()}] {ioc['valeur']} — confiance {ioc['confiance']}")
```

C'est l'usage le plus courant : regrouper des informations liées dans une seule structure nommée.

### Liste de dictionnaires (pattern central)

Un export SIEM, une liste d'événements, un feed d'IOC : presque toujours une **liste de dictionnaires**.

```python
evenements = [
    {"ip": "203.0.113.5", "action": "echec", "user": "root"},
    {"ip": "10.0.0.4", "action": "succes", "user": "alice"},
    {"ip": "203.0.113.5", "action": "echec", "user": "admin"},
]

for ev in evenements:
    if ev["action"] == "echec":
        print(f"[!] Échec : {ev['user']} depuis {ev['ip']}")
```

```
[!] Échec : root depuis 203.0.113.5
[!] Échec : admin depuis 203.0.113.5
```

### Récapitulatif

| Opération        | Syntaxe                          |
| ---------------- | -------------------------------- |
| Créer            | `d = {"cle": "valeur"}`          |
| Lire (sûr)       | `d.get("cle", défaut)`           |
| Ajouter/modifier | `d["cle"] = valeur`              |
| Supprimer        | `del d["cle"]` ou `d.pop("cle")` |
| Tester une clé   | `"cle" in d`                     |
| Parcourir        | `for k, v in d.items():`         |
| Nombre de clés   | `len(d)`                         |

## Application cyber — compter et regrouper

Le dictionnaire brille pour **agréger** : compter les échecs par IP, regrouper les événements par type. Reprenons le comptage du chapitre 7, version dictionnaire complète.

```python
evenements = [
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "10.0.0.4", "action": "succes"},
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "198.51.100.9", "action": "echec"},
]

# Compter les échecs par IP
echecs_par_ip = {}
for ev in evenements:
    if ev["action"] == "echec":
        ip = ev["ip"]
        echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

# Produire un résumé sous forme de dictionnaire d'alertes
resume = {
    "total_evenements": len(evenements),
    "ips_en_echec": len(echecs_par_ip),
    "detail": echecs_par_ip
}

print(f"[*] {resume['total_evenements']} événements analysés")
print(f"[*] {resume['ips_en_echec']} IP en échec")
for ip, nb in resume["detail"].items():
    if nb >= 3:
        print(f"  [!] {ip} : {nb} échecs — force brute probable")
```

Résultat :

```
[*] 5 événements analysés
[*] 2 IP en échec
  [!] 203.0.113.5 : 3 échecs — force brute probable
```

On a utilisé `.get(cle, 0) + 1` pour compter, et un dictionnaire pour structurer le résumé. C'est exactement la forme qu'aurait le résultat d'un mini-SIEM.

## Bonus

### Dictionnaires imbriqués (config d'outil)

```python
config = {
    "seuils": {"echecs_critique": 5, "score_alerte": 7},
    "sortie": {"format": "json", "fichier": "rapport.json"}
}

print(config["seuils"]["echecs_critique"])    # 5
```

C'est la forme typique d'un fichier de configuration JSON (chapitre 10).

### Compter les occurrences en une boucle

```python
texte = "Failed Failed Accepted Failed"
compteur = {}
for mot in texte.split():
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)    # {'Failed': 3, 'Accepted': 1}
```

## ❌ Erreur classique

```python
# Accéder à une clé inexistante sans get()
alerte = {"ip": "203.0.113.5"}
print(alerte["pays"])          # ❌ KeyError
print(alerte.get("pays", "?")) # ✅ "?"

# Confondre clé et valeur avec "in"
print("203.0.113.5" in alerte)            # False — c'est une valeur, pas une clé !
print("203.0.113.5" in alerte.values())   # True — là on cherche dans les valeurs

# Confondre liste et dictionnaire
ips = ["a", "b"]               # liste : indexée par des nombres
scores = {"a": 1, "b": 2}      # dict : indexé par des clés
```

## Exercices

**Guidé :** Crée un dictionnaire `alerte` avec les clés `ip`, `type`, `severite`, `nb_echecs`. Affiche chaque paire avec `.items()`, puis affiche `"[!] CRITIQUE"` si `severite` vaut `"haute"`.

**Autonome :** Crée un script qui prend une phrase de log en argument, découpe-la en mots avec `split()`, et compte les occurrences de chaque mot dans un dictionnaire. Affiche les résultats.

## 🧩 Mini-projet (chapitres 8-9)

Crée un script `fiches_ioc.py` qui :

1. Contient une **liste de dictionnaires** IOC (chaque IOC a `valeur`, `type`, `confiance`).
2. Définit une **fonction** `afficher_ioc(ioc)` qui affiche une fiche formatée.
3. Définit une **fonction** `iocs_fiables(liste, seuil)` qui retourne la liste des IOC dont la confiance dépasse le seuil.
4. Affiche toutes les fiches, puis seulement les IOC de confiance ≥ 0.8.

## ✅ Tu sais maintenant…

- Créer, lire, modifier, supprimer des éléments d'un dictionnaire
- Utiliser `.get(cle, défaut)` pour gérer les champs manquants (réflexe cyber)
- Parcourir avec `.items()`
- Modéliser une alerte / un événement / une fiche IOC avec un dictionnaire
- Le pattern « liste de dictionnaires » pour les exports SIEM et feeds d'IOC
- Agréger des données (compter les échecs par IP)

-----

# Chapitre 10 — Fichiers, chemins, CSV et JSON

> **Prépare tes fichiers de test avant de commencer ce chapitre.** À partir d'ici, tes scripts vont lire de vrais fichiers. Pour t'entraîner, crée-les toi-même (jamais sur des systèmes que tu n'es pas autorisé à analyser). Organise un dossier de travail comme ceci :
>
> ```
> scripts_cyber/
> ├── auth.log
> ├── access.log
> ├── iocs.csv
> ├── rapport.txt
> ├── scripts/      ← tes scripts .py
> └── sorties/      ← les rapports qu'ils produisent
> ```
>
> Crée par exemple un `auth.log` minimal avec quelques lignes factices (tu peux copier-coller ces lignes dans ton éditeur) :
>
> ```
> Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2
> Jan 10 03:22:14 srv sshd[2452]: Failed password for admin from 203.0.113.5 port 51240 ssh2
> Jan 10 03:25:02 srv sshd[2460]: Accepted password for alice from 10.0.0.4 port 51250 ssh2
> Jan 10 03:26:40 srv sshd[2471]: Failed password for root from 198.51.100.9 port 44102 ssh2
> ```
>
> Et un `iocs.csv` minimal :
>
> ```
> valeur,type,confiance
> 203.0.113.5,ip,90
> evil.example.com,domaine,70
> 5d41402abc4b2a76b9719d911017c592,hash,80
> ```
>
> Avec ces deux fichiers, tu pourras exécuter pour de vrai la quasi-totalité des exemples et exercices des chapitres 10 à 20.

## Le minimum à savoir

### Lire un fichier de log

```python
with open("auth.log", "r", encoding="utf-8") as f:
    contenu = f.read()

print(contenu)
```

> **Bonne pratique :** ajoute toujours `encoding="utf-8"` à l'ouverture d'un fichier texte. Sans ça, l'encodage varie selon l'OS et tu risques des erreurs sur les accents ou certains caractères. On ne le répétera pas à chaque exemple, mais prends le réflexe.

Le mot-clé `with` garantit que le fichier est **fermé proprement** à la fin, même en cas d'erreur. `open("fichier", "r")` ouvre en lecture (`"r"` = read), `as f` nomme le fichier ouvert `f`.

### Les modes d'ouverture

|Mode |Signification                  |Équivalent Bash|
|-----|-------------------------------|---------------|
|`"r"`|Lecture (par défaut)           |`cat fichier`  |
|`"w"`|Écriture (écrase le fichier !) |`>`            |
|`"a"`|Ajout (à la fin)               |`>>`           |

> **Attention :** `"w"` **écrase** tout le contenu. Pour un fichier de journal (rapport, log d'analyse), utilise `"a"` pour **ajouter** sans tout perdre.

### Lire ligne par ligne (le mode roi en analyse de logs)

```python
with open("auth.log", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()       # enlève le \n de fin de ligne
        if "Failed password" in ligne:
            print(f"[!] {ligne}")
```

> **Bonne pratique :** `.strip()` à chaque ligne pour retirer le `\n` final, sinon tes comparaisons échouent.

Lire ligne par ligne fonctionne même sur des fichiers énormes (plusieurs Go) sans saturer la mémoire — essentiel pour les vrais logs.

### Écrire un rapport

```python
with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport d'analyse ===\n")
    f.write("IP suspecte : 203.0.113.5\n")
    f.write("Verdict : force brute\n")
```

> **Note :** `f.write()` n'ajoute **pas** de `\n` automatiquement, contrairement à `print()`. Mets-le toi-même.

### Vérifier qu'un fichier existe

```python
import os

if os.path.isfile("auth.log"):
    print("[+] Fichier trouvé")
else:
    print("[-] Fichier introuvable")
```

> **Comparaison avec Bash :** `os.path.isfile()` ≈ `[[ -f ... ]]`, `os.path.isdir()` ≈ `[[ -d ... ]]`, `os.path.exists()` ≈ `[[ -e ... ]]`.

-----

## Les chemins avec `pathlib` (la méthode moderne)

`pathlib` est la manière moderne et lisible de manipuler les chemins (recommandée depuis Python 3.4).

```python
from pathlib import Path

chemin = Path("logs/auth.log")

print(chemin.exists())     # True / False
print(chemin.name)         # "auth.log"
print(chemin.suffix)       # ".log" (l'extension)
print(chemin.parent)       # "logs"
```

### Parcourir un dossier de logs

```python
from pathlib import Path

dossier = Path("/var/log")

# Tous les fichiers .log
for fichier in dossier.glob("*.log"):
    print(f"[+] Log trouvé : {fichier.name}")

# Recherche récursive (sous-dossiers inclus)
for fichier in dossier.rglob("*.log"):
    print(fichier)
```

C'est exactement ce qu'on fait pour analyser tous les logs d'une arborescence d'un coup.

## Très utile en pratique

### Travailler avec des fichiers CSV (exports SIEM)

Les exports SIEM, listes d'IOC et inventaires sont souvent en CSV. Python a un module intégré :

```python
import csv

# Lire un CSV avec en-têtes → chaque ligne devient un dictionnaire
with open("iocs.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['type']} : {ligne['valeur']} (confiance {ligne['confiance']})")

# Écrire un CSV (rapport d'IOC)
with open("rapport.csv", "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["ip", "echecs", "verdict"])      # en-tête
    ecrivain.writerow(["203.0.113.5", "47", "bloquer"])
    ecrivain.writerow(["10.0.0.4", "1", "ok"])
```

Avec `DictReader`, chaque ligne est un dictionnaire dont les clés sont les en-têtes — on retrouve exactement le pattern du chapitre 9.

### Travailler avec du JSON (APIs CTI, configs)

JSON est le format standard des APIs de menaces et des configurations :

```python
import json

# Lire du JSON
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
print(config["seuils"]["score_alerte"])

# Écrire du JSON
rapport = {
    "ip": "203.0.113.5",
    "echecs": 47,
    "verdict": "bloquer"
}
with open("rapport.json", "w", encoding="utf-8") as f:
    json.dump(rapport, f, indent=4)    # indent=4 = joli formatage
```

> **Lien clé :** `json.load()` transforme un fichier JSON en **dictionnaire/liste Python**, et `json.dump()` fait l'inverse. C'est le pont entre tes scripts et les APIs CTI/SIEM (chapitre 17).

### Date et heure avec `datetime`

```python
from datetime import datetime

maintenant = datetime.now()
horodatage = maintenant.strftime("%Y-%m-%d %H:%M:%S")
print(horodatage)        # 2025-01-10 14:30:00

# Nom de fichier de rapport daté
nom = f"rapport_{maintenant.strftime('%Y%m%d')}.txt"
print(nom)               # rapport_20250110.txt
```

Horodater ses rapports et entrées de journal est indispensable en forensic et en SOC.

## Application cyber — un parser de logs qui écrit un rapport

Combinons lecture de log, comptage, et écriture d'un rapport horodaté. C'est un outil défensif complet, simple mais réel.

```python
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
    sys.exit(1)

fichier = Path(sys.argv[1])
if not fichier.is_file():
    print(f"[-] Fichier introuvable : {fichier}")
    sys.exit(1)

# 1. Lire et compter les échecs par IP
echecs_par_ip = {}
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        if "Failed password" in ligne:
            ip = ligne.split()[-1]
            echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

# 2. Écrire un rapport horodaté
horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("rapport_echecs.txt", "w", encoding="utf-8") as r:
    r.write(f"=== Rapport d'analyse ({horodatage}) ===\n")
    r.write(f"Fichier analysé : {fichier}\n\n")
    for ip, nb in echecs_par_ip.items():
        marque = "[BLOQUER]" if nb >= 5 else "[INFO]"
        r.write(f"{marque} {ip} : {nb} échec(s)\n")

print(f"[+] Rapport écrit dans rapport_echecs.txt ({len(echecs_par_ip)} IP)")
```

Lancement : `python3 parser.py auth.log`. Le script lit le log ligne par ligne, compte les échecs par IP, et produit un rapport texte daté marquant les IP à bloquer. Tu as réuni : arguments, vérification de fichier, lecture ligne par ligne, dictionnaire, et écriture de rapport.

## Bonus

### Exécuter une commande système (le pont avec Bash)

Si tu dois vraiment appeler un outil système (rare en pratique) :

```python
import subprocess

resultat = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(resultat.stdout)
```

Préfère les outils Python natifs (`pathlib`, `os`) quand c'est possible.

## ❌ Erreur classique

```python
# Ouvrir en lecture puis vouloir écrire
with open("rapport.txt", "r") as f:
    f.write("texte")          # ❌ io.UnsupportedOperation (mode "r")
with open("rapport.txt", "w") as f:
    f.write("texte")          # ✅

# Confondre "w" et "a" — "w" EFFACE le contenu existant
with open("journal.log", "w") as f:   # ❌ écrase tout le journal !
    f.write("nouvelle entrée\n")
with open("journal.log", "a") as f:   # ✅ ajoute à la fin
    f.write("nouvelle entrée\n")

# Oublier .strip() en lisant ligne par ligne
for ligne in f:
    if ligne == "STOP":        # ❌ ne matche jamais (ligne = "STOP\n")
        break
    if ligne.strip() == "STOP": # ✅
        break

# Ouvrir un fichier inexistant en lecture
with open("absent.log", "r") as f:    # ❌ FileNotFoundError
    f.read()
```

## Exercices

**Guidé :** Crée un script `compter_lignes.py` qui prend un fichier en argument, vérifie qu'il existe, et affiche le nombre total de lignes et le nombre de lignes contenant `"Failed"`.

**Autonome :** Crée un script `csv_vers_json.py` qui lit un fichier CSV d'IOC (colonnes `valeur`, `type`) avec `DictReader`, met chaque ligne dans une liste de dictionnaires, et écrit le tout dans un fichier `iocs.json` avec `json.dump(..., indent=4)`.

## 🧩 Mini-projet (chapitres 8-10)

Crée un script `journal_soc.py` qui :

1. Prend un message d'alerte en argument (ou le demande avec `input()` si absent).
2. Ajoute la date et le message dans un fichier `soc.log` au format `[2025-01-10 14:30] Message`.
3. Avec l'argument `--lire`, affiche tout le contenu du journal.
4. Utilise des **fonctions** : une pour ajouter une entrée, une pour lire le journal.

## ✅ Tu sais maintenant…

- Ouvrir, lire et écrire des fichiers avec `open()` et `with`
- La différence entre les modes `"r"`, `"w"` (écrase) et `"a"` (ajoute)
- Lire un log ligne par ligne (même très gros) et nettoyer avec `.strip()`
- Manipuler les chemins avec `pathlib` (`glob`, `rglob`, `.suffix`…)
- Lire/écrire du CSV (`DictReader`, `writer`) et du JSON (`json.load`, `json.dump`)
- Horodater un rapport avec `datetime`
- Construire un parser de logs qui produit un rapport

-----

# Chapitre 11 — Erreurs, débogage et code propre

## Le minimum à savoir

### Lire un message d'erreur Python (le traceback)

Quand Python plante, il affiche un **traceback** :

```
Traceback (most recent call last):
  File "parser.py", line 8, in <module>
    ip = ligne.split()[-1]
IndexError: list index out of range
```

Comment le lire :

1. **Dernière ligne** = type d'erreur + message (`IndexError: list index out of range`)
2. **Au-dessus** = la ligne fautive (`ip = ligne.split()[-1]`)
3. **Encore au-dessus** = fichier et numéro de ligne (`parser.py, line 8`)

> **Réflexe :** lis le traceback **de bas en haut**. La dernière ligne est la plus importante.

### Les 5 erreurs de débutant les plus fréquentes

|Erreur            |Cause                                   |Exemple cyber                          |
|------------------|----------------------------------------|---------------------------------------|
|`SyntaxError`     |Syntaxe (`:` oublié…)                   |`if "Failed" in ligne` sans `:`        |
|`IndentationError`|Indentation incorrecte                  |mauvais nombre d'espaces               |
|`NameError`       |Variable/fonction non définie           |faute de frappe dans `ip_soruce`       |
|`TypeError`       |Mauvais type                            |`"443" + 1` (port texte + nombre)      |
|`IndexError`/`KeyError`|Élément/clé inexistant             |`ligne.split()[-1]` sur ligne vide     |

```python
# TypeError — port lu comme texte
port = "443"
suivant = port + 1     # ❌ "443" + 1 impossible
suivant = int(port) + 1  # ✅

# IndexError — ligne vide dans un log
ligne = ""
ip = ligne.split()[-1]   # ❌ liste vide, pas d'index -1
```

### Les `print()` de débogage

La méthode la plus simple et universelle pour comprendre ce qui se passe :

```python
ligne = "Failed password for root from 203.0.113.5"
print(f"[DEBUG] ligne = {ligne!r}")     # ← ajoute ça
ip = ligne.split()[-1]
print(f"[DEBUG] ip extraite = {ip!r}")  # ← et ça
```

> **Astuce :** le préfixe `[DEBUG]` permet de retrouver et supprimer facilement ces messages. Utiliser `print()` pour suivre l'exécution est une méthode **normale**, utilisée même par les analystes expérimentés. Le `!r` affiche la valeur avec ses guillemets, pratique pour voir les espaces et `\n` cachés.

### Gérer les erreurs avec `try/except`

Au lieu de laisser le script planter sur un fichier absent ou une ligne mal formée, **capture** l'erreur :

```python
try:
    with open("auth.log", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("[-] Fichier introuvable, analyse annulée")
```

> **Comparaison avec Bash :** équivalent de `commande || echo "Erreur"`, mais bien plus puissant : tu différencies les types d'erreurs.

### `try/except` avec plusieurs types

```python
import sys

try:
    fichier = sys.argv[1]
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
except IndexError:
    print("[-] Donne un fichier en argument.")
except FileNotFoundError:
    print(f"[-] Le fichier '{sys.argv[1]}' n'existe pas.")
except PermissionError:
    print(f"[-] Pas le droit de lire '{sys.argv[1]}'.")
```

### `finally`

Le bloc `finally` s'exécute **toujours**, erreur ou non :

```python
try:
    f = open("auth.log", "r", encoding="utf-8")
    données = f.read()
except FileNotFoundError:
    print("[-] Introuvable")
finally:
    print("[*] Analyse terminée")
```

## Très utile en pratique

### Rendre un parser robuste face aux lignes mal formées

Un vrai fichier de log contient des lignes vides, tronquées, ou inattendues. Un bon parser **ne plante pas** dessus, il les ignore proprement.

```python
lignes = [
    "Failed password for root from 203.0.113.5",
    "",                       # ligne vide
    "log corrompu sans ip",   # ligne sans IP exploitable
    "Failed password for admin from 198.51.100.9",
]

echecs = {}
for ligne in lignes:
    ligne = ligne.strip()
    if not ligne or "Failed password" not in ligne:
        continue              # on saute ce qui ne nous intéresse pas
    try:
        ip = ligne.split()[-1]
        echecs[ip] = echecs.get(ip, 0) + 1
    except IndexError:
        print(f"[DEBUG] ligne ignorée : {ligne!r}")

print(echecs)   # {'203.0.113.5': 1, '198.51.100.9': 1}
```

La combinaison `continue` (ignorer les lignes non pertinentes) + `try/except` (se protéger des surprises) est la clé d'un parser fiable.

### Noms de variables descriptifs

```python
# ❌ Incompréhensible
a = 5
b = []

# ✅ Clair
nb_echecs = 5
ips_suspectes = []
```

### Structurer avec des fonctions et `main()`

```python
import sys

def verifier_arguments():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>")
        sys.exit(1)
    return sys.argv[1]

def compter_echecs(chemin):
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" in ligne:
                ip = ligne.split()[-1]
                echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    chemin = verifier_arguments()
    echecs = compter_echecs(chemin)
    for ip, nb in echecs.items():
        print(f"{ip} : {nb}")

if __name__ == "__main__":
    main()
```

**Ce que fait `if __name__ == "__main__":`** : le code dedans ne s'exécute **que** si tu lances le script directement (`python3 script.py`). Si tu **importes** le fichier ailleurs pour réutiliser ses fonctions, ce bloc ne s'exécute pas. C'est une bonne habitude dès que tes scripts grandissent.

## Application cyber — un script défensif robuste

Réunissons tout : un outil qui ne plante jamais, quels que soient les arguments ou l'état du fichier.

```python
import sys
from pathlib import Path

def analyser(chemin):
    """Compte les échecs SSH par IP dans un fichier de log."""
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" not in ligne:
                continue
            try:
                ip = ligne.strip().split()[-1]
            except IndexError:
                continue          # ligne inattendue → on ignore
            echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
        sys.exit(1)

    chemin = Path(sys.argv[1])
    try:
        echecs = analyser(chemin)
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {chemin}")
        sys.exit(1)
    except PermissionError:
        print(f"[-] Lecture refusée : {chemin}")
        sys.exit(1)

    if not echecs:
        print("[+] Aucun échec détecté.")
        return
    for ip, nb in echecs.items():
        marque = "[!]" if nb >= 5 else "   "
        print(f"{marque} {ip} : {nb} échec(s)")

if __name__ == "__main__":
    main()
```

Ce script gère l'argument manquant, le fichier absent, l'accès refusé, les lignes mal formées et le cas « aucun résultat ». C'est la différence entre un script de TP et un outil sur lequel un analyste peut compter.

## Bonus

### Le module `logging`

Au lieu de `print("[DEBUG]...")`, les outils sérieux utilisent `logging`, qu'on peut activer/désactiver et rediriger vers un fichier :

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Analyse démarrée")
logger.warning("IP suspecte détectée")
logger.error("Fichier illisible")
```

## ❌ Erreur classique

```python
# Capturer toutes les erreurs sans les nommer (masque les vrais bugs)
try:
    analyser()
except:                         # ❌ trop large
    print("Erreur")

try:
    analyser()
except FileNotFoundError as e:  # ✅ erreur précise
    print(f"Fichier : {e}")

# Laisser des print de debug dans la version finale
print("[DEBUG] x =", x)        # ← pense à les retirer

# Ne pas tester les cas limites — teste toujours :
```

```bash
python3 parser.py                          # pas d'argument ?
python3 parser.py absent.log               # fichier inexistant ?
python3 parser.py vide.log                 # fichier vide ?
python3 parser.py "log avec espaces.txt"   # espaces dans le nom ?
```

## Exercices

**Guidé :** Reprends ton parser de logs et entoure l'ouverture du fichier d'un `try/except FileNotFoundError`. Teste-le avec un fichier inexistant pour vérifier qu'il affiche un message propre au lieu de planter.

**Autonome :** Écris une fonction `lire_port(texte)` qui tente `int(texte)` dans un `try/except ValueError` et retourne le port si valide, ou `None` sinon. Teste-la avec `"443"` et `"abc"`.

## ✅ Tu sais maintenant…

- Lire un traceback (de bas en haut) et reconnaître les 5 erreurs fréquentes
- Déboguer avec `print("[DEBUG]...")`
- Gérer les erreurs avec `try/except` (par type) et `finally`
- Rendre un parser robuste face aux fichiers absents et lignes mal formées
- Structurer proprement avec des fonctions et `if __name__ == "__main__":`

-----

# Chapitre 12 — Cas pratiques et automatisation

> Jusqu'ici, tu as appris les briques une par une. Maintenant on les **combine** dans de vrais petits outils défensifs.

## Penser comme un analyste qui automatise

Avant d'écrire un outil, pose-toi trois questions :

1. **Qu'est-ce que je fais à la main régulièrement ?** (chercher des IP dans des logs, calculer des hash…)
2. **Est-ce toujours les mêmes étapes ?**
3. **Est-ce que ça pourrait tourner tout seul ?** (planifié, ou lancé sur un dossier entier)

Trois « oui » → bon candidat pour un script.

## Cas pratique 1 — Extraire les IP uniques d'un log

```python
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <log>")
    sys.exit(1)

ips = set()    # un set : pas de doublons
with open(sys.argv[1], "r", encoding="utf-8") as f:
    for ligne in f:
        if "from " in ligne:
            ip = ligne.strip().split()[-1]
            ips.add(ip)

print(f"[+] {len(ips)} IP unique(s) :")
for ip in sorted(ips):
    print(f"    {ip}")
```

> **Illustre :** `set` pour dédoublonner, lecture ligne par ligne, `split`.

## Cas pratique 2 — Vérifier des chemins et repérer les fichiers sensibles

```python
import sys
from pathlib import Path

extensions_sensibles = (".exe", ".scr", ".bat", ".ps1")

for chemin_str in sys.argv[1:]:
    chemin = Path(chemin_str)
    if not chemin.exists():
        print(f"[-] {chemin} — introuvable")
    elif chemin.is_file():
        marque = "[!]" if chemin.suffix.lower() in extensions_sensibles else "[+]"
        taille = chemin.stat().st_size
        print(f"{marque} {chemin.name} — {taille} octets")
    elif chemin.is_dir():
        nb = len(list(chemin.iterdir()))
        print(f"[+] {chemin.name}/ — dossier ({nb} éléments)")
```

> **Illustre :** `pathlib`, `.suffix`, `.stat().st_size`, tuple d'extensions.

## Cas pratique 3 — Analyser un CSV d'événements

```python
import csv
import sys

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <evenements.csv>")
    sys.exit(1)

total = 0
echecs = 0
par_ip = {}

try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            total += 1
            if ligne.get("action") == "echec":
                echecs += 1
                ip = ligne.get("ip", "inconnue")
                par_ip[ip] = par_ip.get(ip, 0) + 1
    print(f"[*] {total} événements, {echecs} échec(s)")
    for ip, nb in par_ip.items():
        if nb >= 3:
            print(f"  [!] {ip} : {nb} échecs")
except FileNotFoundError:
    print(f"[-] Fichier '{sys.argv[1]}' introuvable")
```

> **Illustre :** `csv.DictReader`, `.get()`, comptage, `try/except`.

## Les modules essentiels pour l'automatisation défensive

Tous inclus avec Python — rien à installer (sauf `requests`, chapitre 16).

|Module      |Utilité                          |Vu au chapitre|
|------------|---------------------------------|--------------|
|`sys`       |Arguments, quitter               |3             |
|`pathlib`   |Chemins, parcours de dossiers    |10            |
|`datetime`  |Horodatage des rapports          |10            |
|`json`      |APIs CTI, configs                |10, 17        |
|`csv`       |Exports SIEM, listes d'IOC       |10            |
|`re`        |Extraction d'IOC (regex)         |13            |
|`hashlib`   |Calcul de hash                   |18            |
|`ipaddress` |Manipulation d'IP/réseaux        |19            |
|`requests`  |Requêtes HTTP/API (à installer)  |16            |

## Script modèle réutilisable

Un squelette propre pour tes outils défensifs :

```python
#!/usr/bin/env python3
"""
Nom         : mon_outil.py
Description : [Ce que fait l'outil]
Usage       : python3 mon_outil.py <argument>
"""

import sys
from datetime import datetime


def log(message):
    """Affiche un message horodaté."""
    h = datetime.now().strftime("%H:%M:%S")
    print(f"[{h}] {message}")


def traiter(cible):
    """Traitement principal."""
    log(f"Analyse de {cible}")
    # ... ton code ...
    log("Terminé.")


def main():
    if len(sys.argv) < 2:
        print(f"Usage : python3 {sys.argv[0]} <cible>")
        sys.exit(1)
    traiter(sys.argv[1])


if __name__ == "__main__":
    main()
```

## Application cyber — assembler une mini-chaîne d'analyse

On combine plusieurs fonctions des chapitres précédents en un seul outil cohérent.

```python
import sys

def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.")

def analyser_log(chemin):
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" not in ligne:
                continue
            ip = ligne.strip().split()[-1]
            echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>")
        sys.exit(1)
    echecs = analyser_log(sys.argv[1])
    print("=== Résumé d'analyse ===")
    for ip, nb in sorted(echecs.items(), key=lambda x: x[1], reverse=True):
        origine = "interne" if is_private_ip(ip) else "EXTERNE"
        verdict = "[!] bloquer" if nb >= 5 and not is_private_ip(ip) else "ok"
        print(f"{ip} ({origine}) : {nb} échecs → {verdict}")

if __name__ == "__main__":
    main()
```

Ici, `sorted(..., key=lambda x: x[1], reverse=True)` trie les IP de la plus active à la moins active (ne t'inquiète pas du `lambda`, c'est juste « trie selon le nombre d'échecs »). On combine fonction de classification, parcours de log, comptage et décision — la structure type d'un outil SOC.

## ❌ Erreur classique

```python
# Réécrire 5 fois le même bloc au lieu d'en faire une fonction
# → factorise dans une fonction réutilisable

# Tout mettre dans un seul gros bloc sans main()
# → structure avec des fonctions + if __name__ == "__main__"

# Oublier de gérer le fichier absent dans un outil "réel"
# → toujours un try/except autour de l'ouverture
```

## Exercices

**Guidé :** Crée un outil qui prend un dossier en argument et liste tous les fichiers `.log` qu'il contient (avec `pathlib.glob`), en affichant la taille de chacun.

**Autonome :** Crée un outil « boîte à outils » avec un menu (`while True` + `input()`) : 1) compter les échecs dans un log, 2) lister les IP uniques, 3) afficher la date/heure, 4) quitter. Chaque option appelle une **fonction** dédiée.

**Défi :** Crée un outil qui lit un CSV d'IOC, les filtre par confiance (≥ un seuil donné en argument) et exporte les IOC retenus dans un fichier JSON.

## ✅ Tu sais maintenant…

- Combiner toutes les briques dans de vrais outils défensifs
- Utiliser les modules essentiels (`sys`, `pathlib`, `datetime`, `json`, `csv`)
- Structurer un outil proprement avec le modèle réutilisable et `main()`
- Automatiser des tâches réelles : extraire des IP, analyser un CSV, produire un rapport

-----

# Partie 2 — Python pour la cybersécurité défensive

> Tu maîtrises maintenant les fondamentaux. Cette partie applique tout ça à des tâches concrètes d'analyse défensive : extraire des indicateurs, parser des logs, manipuler des IOC, interroger des APIs de menaces, calculer des hash, raisonner sur des réseaux. Le niveau reste progressif : chaque chapitre introduit **un** nouveau module et l'applique simplement.
>
> **Rappel d'éthique :** tout ici est **défensif**. On analyse, on détecte, on documente. On n'attaque rien, on ne contourne rien. Les domaines/IP des exemples utilisent les plages de documentation réservées (`example.com`, `203.0.113.x`, `198.51.100.x`).

-----

# Chapitre 13 — Regex avec `re` : extraire IP, emails, domaines, URLs et hash

## Le minimum à savoir

### C'est quoi une regex ?

Une **expression régulière** (regex) est un motif qui décrit une forme de texte. Au lieu de chercher un mot exact, tu décris *à quoi ressemble* ce que tu cherches : « quatre groupes de chiffres séparés par des points » (une IP), « du texte, un @, un domaine » (un email).

C'est l'outil n°1 pour **extraire des IOC** d'un texte brut (un log, un email, un rapport).

```python
import re

texte = "Connexion depuis 203.0.113.5 puis 198.51.100.9 détectée"
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", texte)
print(ips)    # ['203.0.113.5', '198.51.100.9']
```

`re.findall(motif, texte)` retourne **une liste** de toutes les correspondances. C'est la fonction que tu utiliseras le plus.

> **Extraction ≠ validation :** cette regex repère une *forme* qui ressemble à une IPv4, mais elle ne vérifie pas que chaque octet est bien compris entre 0 et 255. Elle matcherait aussi `999.999.999.999`, qui n'est pas une vraie IP. C'est parfait pour **extraire** des candidats d'un texte, mais pour **valider** réellement qu'une IP est correcte, on utilisera le module `ipaddress` au chapitre 19. Retiens cette distinction : on extrait largement, puis on valide proprement.

### Les briques de base d'un motif

|Symbole |Signifie                          |Exemple        |
|--------|----------------------------------|---------------|
|`\d`    |un chiffre (0-9)                  |`\d` → `7`     |
|`\w`    |une lettre, chiffre ou `_`        |`\w` → `a`, `3`|
|`.`     |n'importe quel caractère          |               |
|`\.`    |un vrai point (échappé)           |dans une IP    |
|`+`     |1 fois ou plus                    |`\d+` → `2025` |
|`*`     |0 fois ou plus                    |               |
|`{n}`   |exactement n fois                 |`\d{4}`        |
|`{a,b}` |entre a et b fois                 |`\d{1,3}`      |
|`[...]` |un caractère parmi l'ensemble     |`[a-f0-9]`     |

> **Le `r"..."` (raw string) :** on préfixe toujours les motifs regex par `r` pour que Python n'interprète pas les `\`. `r"\d"` est correct ; `"\d"` peut poser problème.

### Extraire les indicateurs les plus courants

```python
import re

texte = """
Source 203.0.113.5 a contacté evil.example.com
URL piégée : https://bad.example.net/payload
Contact : attaquant@example.com
Hash du fichier : 5d41402abc4b2a76b9719d911017c592
"""

# IP v4
ips = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", texte)
print("IP   :", ips)

# Emails
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte)
print("Mails:", emails)

# URLs http/https
urls = re.findall(r"https?://[^\s]+", texte)
print("URLs :", urls)

# Hash hexadécimaux (MD5=32, SHA-1=40, SHA-256=64)
hashes = re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte)
print("Hash :", hashes)
```

Résultat :

```
IP   : ['203.0.113.5']
Mails: ['attaquant@example.com']
URLs : ['https://bad.example.net/payload']
Hash : ['5d41402abc4b2a76b9719d911017c592']
```

> Ne cherche pas à mémoriser ces motifs par cœur dès maintenant. Comprends leur logique (« des chiffres et des points pour une IP ») et garde-les sous la main comme une boîte à outils.

> **Pourquoi `(?:...{32}|...{40}|...{64})` pour les hash ?** On cible exactement les trois longueurs réelles : MD5 = 32, SHA-1 = 40, SHA-256 = 64 caractères hexadécimaux. Un motif plus simple comme `{32,64}` matcherait aussi des longueurs intermédiaires (33, 50…) qui ne correspondent à aucun hash standard. Le `(?:...)` est un groupe « non capturant » : il sert juste à regrouper les trois possibilités séparées par `|` (OU), sans créer de groupe de capture.

### `re.search()` : juste tester / trouver le premier

```python
import re

ligne = "Failed password for root from 203.0.113.5"

resultat = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", ligne)
if resultat:
    print("IP trouvée :", resultat.group())   # 203.0.113.5
else:
    print("Aucune IP")
```

`re.search` renvoie le **premier** résultat (ou `None`). `.group()` donne le texte trouvé.

## Très utile en pratique

### Les groupes de capture : extraire des morceaux précis

Les parenthèses `(...)` capturent une partie du motif :

```python
import re

ligne = "10/Jan/2025:14:30:55 GET /admin 403"
m = re.search(r"(GET|POST) (\S+) (\d{3})", ligne)
if m:
    methode = m.group(1)    # "GET"
    chemin = m.group(2)     # "/admin"
    code = m.group(3)       # "403"
    print(f"{methode} {chemin} → {code}")
```

`\S` = un caractère qui n'est pas un espace ; `\S+` = un mot. Les groupes te permettent de découper une ligne de log en champs nommés.

### Compiler un motif réutilisé

Si tu utilises le même motif des milliers de fois (gros log), compile-le une fois :

```python
import re

motif_ip = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")

for ligne in lignes:
    for ip in motif_ip.findall(ligne):
        print(ip)
```

## Application cyber — un extracteur d'IOC

Voici un petit extracteur qui sort tous les IOC d'un texte et les range par type. C'est la base d'un outil de triage d'emails de phishing ou de rapports.

```python
import re

def extraire_iocs(texte):
    """Extrait IP, domaines, URLs, emails et hash d'un texte."""
    return {
        "ips": re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte),
        "urls": re.findall(r"https?://[^\s]+", texte),
        "emails": re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte),
        "hashes": re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte),
    }

texte = """De: attaquant@example.com
Cliquez sur https://bad.example.net/login
Serveur de commande : 203.0.113.5
Empreinte : 5d41402abc4b2a76b9719d911017c592
"""

iocs = extraire_iocs(texte)
for type_ioc, valeurs in iocs.items():
    if valeurs:
        print(f"[+] {type_ioc} ({len(valeurs)}) : {valeurs}")
```

Résultat :

```
[+] ips (1) : ['203.0.113.5']
[+] urls (1) : ['https://bad.example.net/login']
[+] emails (1) : ['attaquant@example.com']
[+] hashes (1) : ['5d41402abc4b2a76b9719d911017c592']
```

En quelques lignes, tu transformes un email brut en liste structurée d'indicateurs prêts à être vérifiés.

## Bonus

### `re.sub()` : remplacer / anonymiser

Utile pour **caviarder** des données sensibles dans un rapport (RGPD, partage externe) :

```python
import re

texte = "Utilisateur 203.0.113.5 a échoué 47 fois"
anonyme = re.sub(r"\d{1,3}(?:\.\d{1,3}){3}", "[IP_MASQUÉE]", texte)
print(anonyme)    # Utilisateur [IP_MASQUÉE] a échoué 47 fois
```

## ❌ Erreur classique

```python
import re

# Oublier le r devant le motif
re.findall("\d+", "abc 123")     # ⚠️ peut générer un avertissement
re.findall(r"\d+", "abc 123")    # ✅ correct

# Oublier d'échapper le point (. = n'importe quel caractère !)
re.findall(r"\d+.\d+", "1x2")    # matche "1x2" car . = n'importe quoi
re.findall(r"\d+\.\d+", "1.2")   # ✅ \. = un vrai point

# Croire que findall plante s'il ne trouve rien
re.findall(r"\d+", "aucun chiffre")   # → [] (liste vide, pas d'erreur)

# Oublier de tester si search a trouvé quelque chose
m = re.search(r"\d+", "rien")
print(m.group())    # ❌ AttributeError si m est None
if m:               # ✅ toujours tester
    print(m.group())
```

## Exercices

**Guidé :** Crée un script `extraire_ip.py` qui prend un fichier de log en argument, extrait toutes les IP avec `re.findall`, les dédoublonne (`set`) et les affiche triées.

**Autonome :** Crée un script `extraire_iocs.py` qui lit un fichier texte (un email sauvegardé, par exemple), utilise la fonction `extraire_iocs` ci-dessus, et écrit le résultat dans un fichier JSON.

## ✅ Tu sais maintenant…

- Ce qu'est une regex et pourquoi c'est central pour extraire des IOC
- Les briques de base (`\d`, `\w`, `+`, `{n}`, `[...]`, `\.`) et le `r"..."`
- `re.findall` (toutes les correspondances) et `re.search` (la première)
- Les groupes de capture `(...)` pour découper une ligne en champs
- `re.sub` pour anonymiser des données sensibles

-----

# Chapitre 14 — Parsing de logs : SSH, web et événements structurés

## Le minimum à savoir

### Qu'est-ce que parser un log ?

**Parser**, c'est transformer une ligne de texte brute en données exploitables (un dictionnaire de champs). Chaque type de log a son format, mais la démarche est toujours la même :

```
Ligne brute  →  découper / extraire  →  dictionnaire structuré  →  analyse
```

On réutilise tout ce qu'on a vu : `split()`, regex, dictionnaires, fichiers.

### Parser un log SSH (Linux — auth.log)

Les tentatives SSH échouées sont un classique. Format typique :

```
Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2
```

```python
import re

ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2"

m = re.search(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})", ligne)
if m:
    evenement = {
        "type": "ssh_echec",
        "utilisateur": m.group(1),
        "ip": m.group(2),
    }
    print(evenement)
```

```
{'type': 'ssh_echec', 'utilisateur': 'root', 'ip': '203.0.113.5'}
```

### Parser un log web (Apache/Nginx — access.log)

Format « combined » typique :

```
203.0.113.5 - - [10/Jan/2025:14:30:55 +0000] "GET /admin HTTP/1.1" 403 512
```

```python
import re

ligne = '203.0.113.5 - - [10/Jan/2025:14:30:55 +0000] "GET /admin HTTP/1.1" 403 512'

m = re.search(r'(\d{1,3}(?:\.\d{1,3}){3}).*"(\S+) (\S+) [^"]+" (\d{3})', ligne)
if m:
    requete = {
        "ip": m.group(1),
        "methode": m.group(2),
        "chemin": m.group(3),
        "code": int(m.group(4)),
    }
    print(requete)
```

```
{'ip': '203.0.113.5', 'methode': 'GET', 'chemin': '/admin', 'code': 403}
```

### Parser un log « clé=valeur » (fréquent côté Windows/EDR exporté)

Beaucoup de logs Windows/SIEM exportés sont au format `clé=valeur` :

```
EventID=4625 Account=admin SourceIP=203.0.113.5 Status=failure
```

```python
ligne = "EventID=4625 Account=admin SourceIP=203.0.113.5 Status=failure"

champs = {}
for paire in ligne.split():
    if "=" in paire:
        cle, valeur = paire.split("=", 1)
        champs[cle] = valeur

print(champs["SourceIP"])    # 203.0.113.5
print(champs["EventID"])     # 4625
```

> **Note Windows :** l'`EventID` 4625 = échec d'ouverture de session, 4624 = succès. Connaître quelques ID clés aide à repérer l'essentiel sans tout mémoriser.

## Très utile en pratique

### Parser un fichier entier ligne par ligne

```python
import re

motif = re.compile(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})")

evenements = []
with open("auth.log", "r", encoding="utf-8") as f:
    for ligne in f:
        m = motif.search(ligne)
        if m:
            evenements.append({"utilisateur": m.group(1), "ip": m.group(2)})

print(f"[+] {len(evenements)} échec(s) SSH")
```

On obtient une **liste de dictionnaires** — le format idéal pour analyser ensuite (compter par IP, par utilisateur…).

### Ignorer proprement les lignes qui ne matchent pas

Un log mélange beaucoup de types de lignes. Le motif ne matche que ce qui nous intéresse ; le reste est simplement ignoré (le `if m:` s'en charge). Pas besoin de `try/except` ici : si `search` ne trouve rien, il renvoie `None`.

## Application cyber — un parser SSH qui repère la force brute

```python
import re
import sys

def parser_ssh(chemin):
    """Retourne le nombre d'échecs SSH par IP."""
    motif = re.compile(r"Failed password for \S+ from (\d{1,3}(?:\.\d{1,3}){3})")
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            m = motif.search(ligne)
            if m:
                ip = m.group(1)
                echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <auth.log>")
        sys.exit(1)
    try:
        echecs = parser_ssh(sys.argv[1])
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {sys.argv[1]}")
        sys.exit(1)

    print("=== Tentatives SSH échouées ===")
    for ip, nb in sorted(echecs.items(), key=lambda x: x[1], reverse=True):
        if nb >= 5:
            print(f"[!] {ip} : {nb} échecs — force brute probable")
        else:
            print(f"    {ip} : {nb} échec(s)")

if __name__ == "__main__":
    main()
```

Cet outil lit un `auth.log` réel, extrait chaque IP en échec via regex, compte, trie, et signale les attaques par force brute. C'est un véritable script de triage SOC.

## Bonus

### Détecter une fenêtre temporelle (rafale d'échecs)

Pour aller plus loin, on peut extraire aussi l'horodatage et compter les échecs sur une courte fenêtre (ex. « 20 échecs en 1 minute » = signal fort). On s'appuierait sur `datetime` (chapitre 10) pour comparer les heures. C'est une bonne évolution de l'exercice une fois à l'aise.

## ❌ Erreur classique

```python
# Supposer un format unique alors que les logs varient
# → écris un motif tolérant et ignore ce qui ne matche pas

# split("=") sans limite sur une valeur contenant un "="
"url=http://x?a=b".split("=")          # ['url', 'http://x?a', 'b'] ❌
"url=http://x?a=b".split("=", 1)       # ['url', 'http://x?a=b'] ✅ (découpe 1 fois)

# Oublier que le code HTTP est extrait en texte
code = m.group(4)        # "403" (str)
if code >= 400:          # ❌ comparaison str/int
    pass
code = int(m.group(4))   # ✅
```

## Exercices

**Guidé :** Crée un script qui parse un `access.log` web et compte le nombre de réponses par code HTTP (200, 403, 404, 500…) dans un dictionnaire.

**Autonome :** Crée un script qui parse un log SSH et produit deux statistiques : les IP les plus actives en échec, **et** les noms d'utilisateurs les plus visés.

## ✅ Tu sais maintenant…

- Ce que signifie « parser » un log (texte brut → dictionnaire structuré)
- Parser des logs SSH (Linux), web (Apache/Nginx) et `clé=valeur` (Windows/SIEM)
- Transformer un fichier entier en liste de dictionnaires
- Construire un parser SSH qui repère la force brute

-----

# Chapitre 15 — Manipulation d'IOC : IP, domaines, URLs, hash

## Le minimum à savoir

### Qu'est-ce qu'un IOC, concrètement ?

Un **IOC** (*Indicator of Compromise*) est une donnée observable qui peut indiquer une compromission : une IP, un domaine, une URL, un hash de fichier. Manipuler des IOC, c'est les **extraire**, les **normaliser**, les **dédoublonner**, les **classer par type** et les **comparer à des listes connues**.

### Normaliser un IOC

Les IOC arrivent sous des formes variées. Avant toute comparaison, on les met en forme.

```python
def normaliser_ioc(valeur):
    return valeur.strip().lower()

print(normaliser_ioc("  EVIL.Example.COM "))   # "evil.example.com"
print(normaliser_ioc("ABCDEF123456"))           # "abcdef123456" (hash en minuscules)
```

### « Défanger » et « refanger »

Dans les rapports de menaces, les IOC sont souvent **défangés** pour éviter les clics accidentels : `hxxp://evil[.]com`. Il faut savoir les remettre en forme pour les traiter.

```python
def refang(ioc):
    """Remet un IOC défangé en forme normale."""
    return (ioc.replace("hxxp", "http")
               .replace("[.]", ".")
               .replace("(.)", "."))

print(refang("hxxps://evil[.]com/path"))    # https://evil.com/path
print(refang("203[.]0[.]113[.]5"))          # 203.0.113.5
```

> **Note défensive :** on défang justement pour **ne pas** activer un lien malveillant. Ces fonctions servent à analyser, jamais à visiter.

### Déterminer le type d'un IOC

```python
import re

def type_ioc(valeur):
    valeur = valeur.strip()
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur):
        return "ip"
    if re.fullmatch(r"[a-fA-F0-9]{32}", valeur):
        return "hash_md5"
    if re.fullmatch(r"[a-fA-F0-9]{64}", valeur):
        return "hash_sha256"
    if valeur.startswith("http://") or valeur.startswith("https://"):
        return "url"
    if "." in valeur:
        return "domaine"
    return "inconnu"

for v in ["203.0.113.5", "evil.example.com", "https://bad.net/x",
          "5d41402abc4b2a76b9719d911017c592"]:
    print(f"{v} → {type_ioc(v)}")
```

```
203.0.113.5 → ip
evil.example.com → domaine
https://bad.net/x → url
5d41402abc4b2a76b9719d911017c592 → hash_md5
```

`re.fullmatch` exige que **tout** le texte corresponde au motif (contrairement à `search` qui en trouve une partie).

> **Version améliorée (à connaître après le chapitre 19) :** ici, `re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur)` reconnaît la *forme* d'une IP, mais classerait aussi `999.999.999.999` comme `"ip"`. C'est la distinction extraction ≠ validation déjà vue. Une fois le module `ipaddress` connu, on peut valider réellement :
>
> ```python
> import ipaddress
>
> def est_ip(valeur):
>     try:
>         ipaddress.ip_address(valeur)
>         return True
>     except ValueError:
>         return False
> ```
>
> Le principe à retenir : **au début, on utilise une regex pour reconnaître une forme ; plus tard, on utilise `ipaddress` pour valider vraiment.** Dans `type_ioc`, tu pourrais remplacer le test regex de l'IP par `if est_ip(valeur): return "ip"`.

## Très utile en pratique

### Extraire le domaine d'une URL ou d'un email

```python
def domaine_de_url(url):
    sans_schema = url.replace("https://", "").replace("http://", "")
    return sans_schema.split("/")[0].lower()

def domaine_de_email(email):
    return email.split("@")[-1].lower()

print(domaine_de_url("https://bad.Example.com/login"))   # bad.example.com
print(domaine_de_email("attaquant@evil.example.net"))    # evil.example.net
```

### Comparer des IOC à une liste connue

```python
liste_noire = {"evil.example.com", "bad.example.net", "203.0.113.5"}

a_verifier = ["evil.example.com", "google.com", "203.0.113.5"]

for ioc in a_verifier:
    if ioc in liste_noire:
        print(f"[!] {ioc} — CONNU MALVEILLANT")
    else:
        print(f"[+] {ioc} — non listé")
```

Utiliser un `set` pour la liste noire rend la vérification très rapide, même avec des millions d'entrées.

## Application cyber — un mini-gestionnaire d'IOC

Réunissons extraction, normalisation, typage et déduplication dans un petit outil.

```python
import re

def extraire_et_classer(texte):
    """Extrait les IOC d'un texte et les range par type, sans doublons."""
    resultat = {"ip": set(), "url": set(), "email": set(), "hash": set()}

    for ip in re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte):
        resultat["ip"].add(ip)
    for url in re.findall(r"https?://[^\s]+", texte):
        resultat["url"].add(url.lower())
    for mail in re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte):
        resultat["email"].add(mail.lower())
    for h in re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte):
        resultat["hash"].add(h.lower())

    # On convertit les sets en listes triées pour l'affichage
    return {t: sorted(v) for t, v in resultat.items()}

rapport = """Source 203.0.113.5 et 203.0.113.5 (doublon)
URL : https://bad.example.net/x
Mail : Attaquant@Example.com
Hash : 5D41402ABC4B2A76B9719D911017C592
"""

iocs = extraire_et_classer(rapport)
for type_ioc, valeurs in iocs.items():
    if valeurs:
        print(f"[+] {type_ioc.upper()} : {valeurs}")
```

Résultat :

```
[+] IP : ['203.0.113.5']
[+] URL : ['https://bad.example.net/x']
[+] EMAIL : ['attaquant@example.com']
[+] HASH : ['5d41402abc4b2a76b9719d911017c592']
```

Le doublon d'IP a disparu (grâce au `set`), le mail et le hash sont normalisés en minuscules. C'est exactement ce qu'on veut avant d'envoyer une liste d'IOC à une plateforme CTI.

## Bonus

### Vers un format d'échange standard

Les IOC s'échangent souvent en JSON structuré (proche du standard STIX, simplifié) :

```python
ioc = {
    "type": "domain",
    "value": "evil.example.com",
    "confidence": 80,
    "source": "rapport_interne",
    "tags": ["phishing", "c2"]
}
```

On retrouve simplement un dictionnaire — exportable en JSON avec `json.dump` (chapitre 17).

## ❌ Erreur classique

```python
# Comparer des IOC sans les normaliser
"Evil.com" in {"evil.com"}        # False ❌
"Evil.com".lower() in {"evil.com"}  # True ✅

# Confondre search et fullmatch pour valider un format
import re
re.search(r"\d{1,3}(?:\.\d{1,3}){3}", "ip=203.0.113.5 !")    # matche (partie)
re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", "ip=203.0.113.5 !") # None (tout doit matcher)

# Garder les doublons (oublier set)
# → utilise set() pour dédoublonner automatiquement
```

## Exercices

**Guidé :** Crée une fonction `est_dans_liste_noire(ioc, liste)` qui normalise l'IOC puis vérifie son appartenance à une liste noire (un `set`). Teste avec des casses différentes.

**Autonome :** Crée un script qui lit un fichier texte, extrait tous les IOC (IP, URL, email, hash), les classe par type sans doublons, et écrit un rapport JSON structuré.

## ✅ Tu sais maintenant…

- Ce qu'est un IOC et les opérations clés (extraire, normaliser, typer, dédoublonner, comparer)
- Normaliser et « refanger » des IOC défangés (`hxxp`, `[.]`)
- Déterminer le type d'un IOC avec `re.fullmatch`
- Extraire le domaine d'une URL/email
- Comparer des IOC à une liste noire (avec un `set`)

-----

# Chapitre 16 — Requêtes HTTP et APIs CTI avec `requests`

## Le minimum à savoir

### Installer `requests`

`requests` est le seul module non inclus de ce cours. Installe-le :

```bash
pip install requests
# ou, selon ton système :
pip3 install requests
```

C'est la bibliothèque standard de fait pour faire des requêtes HTTP en Python. On l'utilise pour interroger des **APIs de threat intelligence** (réputation d'IP, infos sur un domaine, etc.).

> **Connexion Internet requise :** tous les exemples de ce chapitre utilisent `httpbin.org`, un service public de test, et nécessitent donc un accès Internet. Si tu es sur un réseau filtré, derrière un proxy, ou dans un environnement isolé, ces exemples peuvent échouer **même si ton code est correct**. Dans ce cas, ce n'est pas un bug : c'est le réseau. Le raisonnement et la structure du code restent valables.

### Une première requête GET

```python
import requests

reponse = requests.get("https://httpbin.org/get")

print(reponse.status_code)     # 200 (succès)
print(reponse.text[:80])        # le contenu (texte)
```

`requests.get(url)` renvoie un objet **réponse** avec :

- `.status_code` → le code HTTP (200 = OK, 404 = absent, 403 = interdit…)
- `.text` → le contenu brut en texte
- `.json()` → le contenu décodé si c'est du JSON (le plus utile pour les APIs)

### Lire une réponse JSON d'API

La plupart des APIs renvoient du JSON, que `requests` convertit directement en dictionnaire Python :

```python
import requests

reponse = requests.get("https://httpbin.org/json")
donnees = reponse.json()         # → dictionnaire Python

print(type(donnees))             # <class 'dict'>
print(donnees.keys())            # les clés disponibles
```

> **Lien clé :** `.json()` te rend un **dictionnaire** — tu retrouves tout ce que tu sais du chapitre 9 pour explorer la réponse.

### Vérifier le code de statut avant de traiter

```python
import requests

reponse = requests.get("https://httpbin.org/status/404")

if reponse.status_code == 200:
    print("[+] OK, traitement de la réponse")
    donnees = reponse.json()
else:
    print(f"[-] Erreur HTTP {reponse.status_code}")
```

## Très utile en pratique

### Passer des paramètres et un timeout

```python
import requests

params = {"ip": "203.0.113.5"}
reponse = requests.get(
    "https://httpbin.org/get",
    params=params,
    timeout=5            # toujours un timeout : ne pas bloquer indéfiniment
)
print(reponse.url)       # .../get?ip=203.0.113.5
```

> **Bonne pratique :** mets **toujours** un `timeout`. Sans lui, ton script peut rester bloqué si l'API ne répond pas.

### Envoyer une clé d'API dans les en-têtes

Les APIs CTI exigent souvent une clé d'authentification, transmise dans les en-têtes :

```python
import requests

headers = {"x-apikey": "TA_CLE_API"}      # ne JAMAIS écrire la clé en dur en vrai
reponse = requests.get("https://api.exemple-cti.test/ip/203.0.113.5",
                       headers=headers, timeout=5)
```

> **Sécurité :** ne mets jamais une vraie clé d'API directement dans le code. Lis-la depuis une variable d'environnement (`os.getenv("CTI_API_KEY")`) ou un fichier de config non versionné.

### Gérer les erreurs réseau

Le réseau peut échouer (pas de connexion, API en panne). On entoure d'un `try/except` :

```python
import requests

try:
    reponse = requests.get("https://httpbin.org/get", timeout=5)
    reponse.raise_for_status()       # lève une erreur si code 4xx/5xx
    donnees = reponse.json()
    print("[+] Réponse reçue")
except requests.exceptions.Timeout:
    print("[-] L'API n'a pas répondu à temps")
except requests.exceptions.RequestException as e:
    print(f"[-] Erreur réseau : {e}")
```

## Application cyber — un client de réputation d'IP (générique)

Voici un client simple qui interroge une API de réputation et interprète la réponse. On utilise une API publique de test (`httpbin`) pour que le code soit exécutable sans clé ; en réel, tu remplacerais l'URL par celle de ton fournisseur CTI.

```python
import requests

def verifier_ip(ip):
    """Interroge une API de réputation (ici simulée) et renvoie un verdict."""
    url = "https://httpbin.org/get"        # remplace par ton API CTI réelle
    try:
        rep = requests.get(url, params={"ip": ip}, timeout=5)
        rep.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"ip": ip, "statut": "erreur", "detail": str(e)}

    donnees = rep.json()
    # En réel, on lirait par ex. donnees["malicious_score"].
    # Ici on illustre juste l'accès aux champs renvoyés.
    return {
        "ip": ip,
        "statut": "ok",
        "echo_params": donnees.get("args", {}),
    }

for ip in ["203.0.113.5", "198.51.100.9"]:
    resultat = verifier_ip(ip)
    print(f"[+] {resultat['ip']} → {resultat['statut']} {resultat.get('echo_params')}")
```

La structure est celle de tous les clients CTI : construire l'URL, envoyer la requête avec un timeout, gérer les erreurs réseau, décoder le JSON, extraire les champs utiles et renvoyer un verdict structuré. Pour passer en réel, il suffit de changer l'URL, d'ajouter la clé d'API et de lire les bons champs de la réponse.

## Bonus

### Boucler sur une liste d'IOC (avec pause)

Quand tu interroges une API pour plusieurs IOC, respecte ses limites de débit :

```python
import time

for ip in ["203.0.113.5", "198.51.100.9"]:
    resultat = verifier_ip(ip)
    print(resultat)
    time.sleep(1)        # 1 seconde entre deux requêtes (politesse + quotas)
```

## ❌ Erreur classique

```python
import requests

# Oublier le timeout → script qui peut se bloquer
requests.get(url)                 # ❌
requests.get(url, timeout=5)      # ✅

# Appeler .json() sur une réponse qui n'est pas du JSON
reponse.json()                    # ❌ JSONDecodeError si c'est du HTML/texte
# → vérifie status_code et le type de contenu d'abord

# Écrire sa clé d'API en dur dans le script
headers = {"x-apikey": "abc123..."}   # ❌ ne jamais committer ça
import os
headers = {"x-apikey": os.getenv("CTI_API_KEY")}   # ✅

# Ne pas gérer les erreurs réseau → crash au moindre souci de connexion
```

## Exercices

**Guidé :** Crée un script `ping_api.py` qui fait un `requests.get` sur `https://httpbin.org/status/200`, vérifie le `status_code`, et affiche `"[+] API joignable"` ou `"[-] Problème"`.

**Autonome :** Crée une fonction `interroger(ioc)` qui interroge `https://httpbin.org/get` avec l'IOC en paramètre, gère les erreurs réseau avec `try/except`, et retourne un dictionnaire `{"ioc": ..., "statut": "ok"/"erreur"}`. Boucle sur une liste de 3 IOC avec une pause d'1 seconde.

## ✅ Tu sais maintenant…

- Installer et utiliser `requests` pour faire des requêtes HTTP
- Lire `.status_code`, `.text` et surtout `.json()` (→ dictionnaire)
- Passer des paramètres, des en-têtes (clé d'API) et un `timeout`
- Gérer les erreurs réseau avec `try/except`
- Construire un client de réputation d'IOC générique
- Protéger ses clés d'API (variables d'environnement)

-----

# Chapitre 17 — JSON avancé pour APIs CTI/SIEM

## Le minimum à savoir

### Rappel : JSON ⟷ Python

JSON est le langage commun des APIs de menaces et des SIEM. Python le traduit directement :

|JSON         |Python      |
|-------------|------------|
|objet `{}`   |dictionnaire|
|tableau `[]` |liste       |
|`"texte"`    |`str`       |
|`42`         |`int`       |
|`true`/`false`|`True`/`False`|
|`null`       |`None`      |

Deux paires de fonctions à connaître :

```python
import json

# Depuis/vers une CHAÎNE de texte (ex. réponse d'API)
donnees = json.loads('{"ip": "203.0.113.5", "score": 80}')   # texte → dict
texte = json.dumps(donnees)                                   # dict → texte

# Depuis/vers un FICHIER
with open("ioc.json") as f:
    donnees = json.load(f)        # fichier → dict
with open("sortie.json", "w") as f:
    json.dump(donnees, f, indent=4)   # dict → fichier
```

> **Moyen mnémotechnique :** `loads`/`dumps` (avec **s** comme *string*) travaillent sur du texte ; `load`/`dump` (sans s) travaillent sur des **fichiers**.

### Explorer une réponse d'API imbriquée

Les réponses CTI sont souvent imbriquées (dictionnaires dans des dictionnaires dans des listes). On y accède pas à pas :

```python
import json

reponse = json.loads("""
{
  "data": {
    "ip": "203.0.113.5",
    "reputation": {"score": 85, "verdict": "malicious"},
    "tags": ["c2", "scanner"]
  }
}
""")

print(reponse["data"]["ip"])                       # 203.0.113.5
print(reponse["data"]["reputation"]["score"])      # 85
print(reponse["data"]["tags"][0])                  # c2
```

Chaque `[...]` descend d'un niveau. C'est de la navigation dans des dictionnaires et listes — rien de nouveau, juste imbriqué.

### Accès sûr avec `.get()` (champs parfois absents)

Les réponses d'API varient. Ne suppose jamais qu'un champ existe :

```python
reputation = reponse["data"].get("reputation", {})
score = reputation.get("score", 0)        # 0 si absent
print(f"Score : {score}")
```

Enchaîner des `.get(..., {})` évite les `KeyError` quand un niveau manque.

## Très utile en pratique

### Parcourir une liste de résultats

```python
import json

reponse = json.loads("""
{"results": [
  {"ioc": "203.0.113.5", "type": "ip", "score": 90},
  {"ioc": "evil.example.com", "type": "domain", "score": 70},
  {"ioc": "8.8.8.8", "type": "ip", "score": 0}
]}
""")

for item in reponse["results"]:
    if item["score"] >= 80:
        print(f"[!] {item['ioc']} ({item['type']}) — score {item['score']}")
```

```
[!] 203.0.113.5 (ip) — score 90
```

### Construire un événement au format SIEM et l'exporter

```python
import json
from datetime import datetime

evenement = {
    "timestamp": datetime.now().isoformat(),
    "source": "parser_ssh",
    "alert": {
        "type": "ssh_bruteforce",
        "src_ip": "203.0.113.5",
        "count": 47,
        "severity": "high"
    },
    "iocs": ["203.0.113.5"]
}

with open("alerte_siem.json", "w", encoding="utf-8") as f:
    json.dump(evenement, f, indent=4, ensure_ascii=False)

print("[+] Alerte exportée au format JSON")
```

> **Astuce :** `ensure_ascii=False` garde les accents lisibles dans le fichier (`é` au lieu de `\u00e9`). `datetime.now().isoformat()` produit un horodatage standard exploitable par les SIEM.

### Transformer un CSV d'IOC en JSON (cas très courant)

```python
import csv
import json

iocs = []
with open("iocs.csv", "r", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        iocs.append({
            "value": ligne["valeur"],
            "type": ligne["type"],
            "confidence": int(ligne.get("confiance", 0))
        })

with open("iocs.json", "w", encoding="utf-8") as f:
    json.dump(iocs, f, indent=4, ensure_ascii=False)

print(f"[+] {len(iocs)} IOC convertis en JSON")
```

## Application cyber — analyser une réponse CTI et produire un verdict

On reçoit une réponse JSON (comme une vraie API de réputation) et on la résume en un verdict clair.

```python
import json

# Réponse simulée d'une API CTI
brut = """
{
  "ioc": "203.0.113.5",
  "type": "ip",
  "engines": {"total": 80, "malicious": 12, "suspicious": 5},
  "tags": ["scanner", "bruteforce"],
  "last_seen": "2025-01-09"
}
"""

def verdict_cti(reponse_json):
    data = json.loads(reponse_json)
    engines = data.get("engines", {})
    malicious = engines.get("malicious", 0)
    total = engines.get("total", 1)

    ratio = malicious / total
    if ratio >= 0.10:
        niveau = "MALVEILLANT"
    elif malicious > 0:
        niveau = "SUSPECT"
    else:
        niveau = "PROPRE"

    return {
        "ioc": data.get("ioc"),
        "type": data.get("type"),
        "niveau": niveau,
        "detections": f"{malicious}/{total}",
        "tags": data.get("tags", [])
    }

resultat = verdict_cti(brut)
print(f"[{resultat['niveau']}] {resultat['ioc']} "
      f"({resultat['detections']}) tags={resultat['tags']}")
```

Résultat :

```
[MALVEILLANT] 203.0.113.5 (12/80) tags=['scanner', 'bruteforce']
```

On a décodé le JSON, navigué dans les champs imbriqués avec `.get()` (sans risque de plantage), calculé un ratio de détection et produit un verdict structuré — exactement le travail d'un script d'enrichissement CTI.

## Bonus

### Joindre le résultat d'une API et un fichier local

On peut fusionner une réponse d'API (chapitre 16) avec ses notes internes :

```python
enrichi = {
    "ioc": "203.0.113.5",
    "cti": verdict_cti(brut),          # le verdict ci-dessus
    "note_interne": "Vu sur 3 serveurs le 09/01"
}
print(json.dumps(enrichi, indent=2, ensure_ascii=False))
```

## ❌ Erreur classique

```python
import json

# Confondre loads (texte) et load (fichier)
json.loads(open("f.json"))     # ❌ loads attend du texte, pas un fichier
json.load(open("f.json"))      # ✅ load lit un fichier
json.loads('{"a": 1}')         # ✅ loads lit une chaîne

# Supposer qu'un champ imbriqué existe
data["reputation"]["score"]                 # ❌ KeyError si "reputation" absent
data.get("reputation", {}).get("score", 0)  # ✅ sûr

# Oublier de convertir les nombres lus depuis un CSV (texte)
"confidence": ligne["confiance"]        # "80" (str)
"confidence": int(ligne["confiance"])   # 80 (int)
```

## Exercices

**Guidé :** Crée un script qui charge un fichier JSON contenant une liste d'IOC (`[{"value":..., "score":...}]`) et affiche uniquement ceux dont le score dépasse 70.

**Autonome :** Crée un script `csv2json_ioc.py` qui convertit un CSV d'IOC en JSON structuré (avec conversion du champ confiance en entier) et écrit le résultat avec `indent=4` et `ensure_ascii=False`.

## ✅ Tu sais maintenant…

- La correspondance JSON ⟷ Python et les fonctions `loads`/`dumps`/`load`/`dump`
- Naviguer dans une réponse CTI imbriquée avec des `[...]` et des `.get()` sûrs
- Construire et exporter un événement au format SIEM (avec horodatage `isoformat`)
- Convertir un CSV d'IOC en JSON
- Produire un verdict structuré à partir d'une réponse d'API

-----

# Chapitre 18 — Calcul de hash avec `hashlib`

## Le minimum à savoir

### À quoi sert un hash en défense ?

Un **hash** est une empreinte numérique unique d'un fichier ou d'un texte. Le moindre changement dans le contenu change complètement le hash. En défense, on s'en sert pour :

- **Identifier un fichier** sans le partager (on échange le hash, pas le malware).
- **Vérifier l'intégrité** d'un fichier (a-t-il été modifié ?).
- **Comparer un fichier** à des bases de hash malveillants connus (CTI).

`hashlib` est inclus avec Python — rien à installer.

### Hasher un texte

```python
import hashlib

texte = "données à empreinter"
donnees = texte.encode("utf-8")        # hashlib travaille sur des octets

print(hashlib.md5(donnees).hexdigest())
print(hashlib.sha1(donnees).hexdigest())
print(hashlib.sha256(donnees).hexdigest())
```

> **Note :** il faut d'abord convertir le texte en **octets** avec `.encode("utf-8")`. `.hexdigest()` donne le hash en hexadécimal (le format qu'on voit partout).

### Les longueurs de hash (rappel utile)

|Algorithme |Longueur (caractères hex)|
|-----------|-------------------------|
|MD5        |32                       |
|SHA-1      |40                       |
|SHA-256    |64                       |

> **Choix défensif :** privilégie **SHA-256** pour l'identification de fichiers. MD5 et SHA-1 restent très présents dans les bases d'IOC existantes, donc tu les croiseras, mais ils sont considérés comme faibles aujourd'hui.

### Hasher un fichier (la vraie tâche du quotidien)

On lit le fichier **par blocs** pour gérer même les gros fichiers sans saturer la mémoire :

```python
import hashlib

def hash_fichier(chemin, algo="sha256"):
    h = hashlib.new(algo)
    with open(chemin, "rb") as f:        # "rb" = lecture binaire
        for bloc in iter(lambda: f.read(8192), b""):
            h.update(bloc)
    return h.hexdigest()

print(hash_fichier("rapport.pdf"))
```

> **Important :** on ouvre le fichier en mode binaire `"rb"` (pas `"r"`), car un hash se calcule sur les octets bruts, pas sur du texte. La ligne `iter(lambda: f.read(8192), b"")` lit le fichier par morceaux de 8 Ko jusqu'à la fin.

## Très utile en pratique

### Vérifier l'intégrité d'un fichier

```python
import hashlib

def hash_fichier(chemin, algo="sha256"):
    h = hashlib.new(algo)
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            h.update(bloc)
    return h.hexdigest()

attendu = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
calcule = hash_fichier("telechargement.iso")

if calcule == attendu:
    print("[+] Intégrité vérifiée")
else:
    print("[!] FICHIER ALTÉRÉ — hash différent !")
```

C'est exactement comme ça qu'on vérifie qu'un téléchargement n'a pas été corrompu ou trafiqué.

### Comparer un fichier à une liste de hash malveillants

```python
hash_malveillants = {
    "5d41402abc4b2a76b9719d911017c592",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}

h = hash_fichier("suspect.bin", "md5")
if h in hash_malveillants:
    print(f"[!] {h} — fichier connu malveillant")
else:
    print(f"[+] {h} — non listé")
```

## Application cyber — calculer les 3 hash d'un fichier (fiche d'identité)

Quand on documente un fichier suspect en forensic, on note ses trois empreintes. Voici un outil qui les calcule en une seule lecture du fichier (efficace).

```python
import hashlib
import sys

def empreintes(chemin):
    """Calcule MD5, SHA-1 et SHA-256 en une seule passe."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            md5.update(bloc)
            sha1.update(bloc)
            sha256.update(bloc)
    return {
        "fichier": chemin,
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
    }

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier>")
        sys.exit(1)
    try:
        fiche = empreintes(sys.argv[1])
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {sys.argv[1]}")
        sys.exit(1)

    print(f"=== Empreintes de {fiche['fichier']} ===")
    print(f"MD5    : {fiche['md5']}")
    print(f"SHA-1  : {fiche['sha1']}")
    print(f"SHA-256: {fiche['sha256']}")

if __name__ == "__main__":
    main()
```

Lecture unique du fichier, mise à jour des trois algorithmes en parallèle, gestion du fichier absent : c'est l'outil que tout analyste garde sous la main pour produire la « carte d'identité » d'un fichier avant de le soumettre à une base CTI.

## Bonus

### Comparer en ignorant la casse

Les hash s'écrivent parfois en majuscules, parfois en minuscules. Normalise avant de comparer :

```python
a = "5D41402ABC4B2A76B9719D911017C592"
b = "5d41402abc4b2a76b9719d911017c592"
print(a.lower() == b.lower())     # True
```

## ❌ Erreur classique

```python
import hashlib

# Oublier d'encoder le texte en octets
hashlib.sha256("texte")              # ❌ TypeError
hashlib.sha256("texte".encode())     # ✅

# Ouvrir le fichier en mode texte au lieu de binaire
with open("f.bin", "r") as f:        # ❌ peut planter / hash faux
with open("f.bin", "rb") as f:       # ✅ binaire

# Comparer des hash de casses différentes
"ABC" == "abc"                       # ❌ False
"ABC".lower() == "abc".lower()       # ✅

# Croire qu'un hash MD5 identique = fichiers sûrs
# MD5 est faible : pour l'intégrité de sécurité, préfère SHA-256
```

## Exercices

**Guidé :** Crée un script `hash_texte.py` qui prend un texte en argument et affiche son MD5, SHA-1 et SHA-256.

**Autonome :** Crée un script `verif_hash.py` qui prend un fichier et un hash SHA-256 attendu en arguments, calcule le hash réel, et affiche si l'intégrité est vérifiée ou si le fichier a été altéré.

## ✅ Tu sais maintenant…

- À quoi servent les hash en défense (identification, intégrité, comparaison CTI)
- Hasher du texte (`.encode()` puis `.hexdigest()`)
- Hasher un fichier par blocs en mode binaire `"rb"`
- Vérifier l'intégrité et comparer à une liste de hash malveillants
- Privilégier SHA-256 et normaliser la casse avant comparaison

-----

# Chapitre 19 — Validation d'IP et réseaux avec `ipaddress`

## Le minimum à savoir

### Pourquoi un module dédié ?

Au chapitre 4, on a vu qu'une IP est du texte et que la comparer avec `<` ne donne pas le résultat attendu. Le module `ipaddress` (inclus avec Python) comprend **vraiment** les adresses et les réseaux : il sait si une IP est privée, à quel réseau elle appartient, etc. C'est l'outil propre pour tout raisonnement réseau.

> **Note pédagogique importante — les IP de documentation :** dans tout ce cours, les plages `203.0.113.0/24`, `198.51.100.0/24` et `192.0.2.0/24` sont utilisées dans les exemples de logs. Ce sont des plages **réservées à la documentation** (RFC 5737), choisies pour ne jamais afficher de vraie IP publique. Attention : avec le module `ipaddress`, ces adresses ne sont **pas** considérées comme globalement routables — `is_private` peut donc renvoyer `True` pour elles (la sémantique de `is_private` correspond à « non globalement joignable », pas seulement aux plages privées RFC 1918, et ce comportement a été affiné dans Python 3.13). Donc, pour les exemples de **classification interne/externe** de ce chapitre, on utilise de **vraies IP publiques** comme `8.8.8.8` ou `1.1.1.1` (les DNS publics de Google et Cloudflare), uniquement comme exemples de classification — on ne fait **aucune** requête vers elles. Retiens : on extrait avec les IP de doc, mais on illustre `is_private`/`is_global` avec de vraies publiques pour obtenir des résultats fiables quelle que soit ta version de Python.

### Créer et inspecter une adresse IP

```python
import ipaddress

ip = ipaddress.ip_address("8.8.8.8")     # DNS public de Google (exemple)

print(ip.version)        # 4 (IPv4)
print(ip.is_private)     # False — c'est une IP publique (vient d'Internet)
print(ip.is_global)      # True
```

```python
interne = ipaddress.ip_address("10.0.0.4")
print(interne.is_private)    # True — réseau interne
```

> **Fini la fonction artisanale du chapitre 8 !** `ip.is_private` gère correctement **toutes** les plages privées (`10.x`, `192.168.x`, `172.16-31.x`), sans risque d'erreur — et bien plus de cas encore.

### Valider une IP

Si le texte n'est pas une IP valide, `ip_address` lève une `ValueError` — pratique pour valider une saisie :

```python
import ipaddress

def est_ip_valide(texte):
    try:
        ipaddress.ip_address(texte)
        return True
    except ValueError:
        return False

print(est_ip_valide("203.0.113.5"))    # True
print(est_ip_valide("999.1.1.1"))      # False (999 impossible)
print(est_ip_valide("pas une ip"))     # False
```

### Travailler avec des réseaux (CIDR)

Un réseau s'écrit en notation **CIDR** : `192.168.1.0/24` (les 24 premiers bits fixes). On teste facilement si une IP appartient à un réseau :

```python
import ipaddress

reseau = ipaddress.ip_network("192.168.1.0/24")

ip = ipaddress.ip_address("192.168.1.50")
print(ip in reseau)       # True — l'IP est dans ce réseau

ip2 = ipaddress.ip_address("10.0.0.1")
print(ip2 in reseau)      # False
```

L'opérateur `in` fonctionne directement entre une IP et un réseau — exactement ce qu'il faut pour vérifier une appartenance.

## Très utile en pratique

### Lister les adresses d'un réseau

```python
import ipaddress

reseau = ipaddress.ip_network("192.168.1.0/29")    # petit réseau
for ip in reseau.hosts():
    print(ip)
# 192.168.1.1 ... 192.168.1.6 (les adresses utilisables)
```

### Classer une liste d'IP en interne / externe

```python
import ipaddress

# On mélange des IP internes et de vraies IP publiques (DNS publics, en exemple)
ips = ["10.0.0.4", "8.8.8.8", "192.168.1.10", "1.1.1.1"]

internes, externes = [], []
for texte in ips:
    ip = ipaddress.ip_address(texte)
    if ip.is_private:
        internes.append(texte)
    else:
        externes.append(texte)

print("Internes :", internes)   # ['10.0.0.4', '192.168.1.10']
print("Externes :", externes)   # ['8.8.8.8', '1.1.1.1']
```

Séparer le trafic interne du trafic externe est une étape de triage très courante : une attaque venant de l'extérieur est généralement prioritaire.

### Vérifier si une IP est dans une plage à surveiller

```python
import ipaddress

# Plages internes "sensibles" (ex. serveurs critiques)
plages_sensibles = [
    ipaddress.ip_network("10.0.0.0/24"),
    ipaddress.ip_network("192.168.100.0/24"),
]

def est_sensible(ip_texte):
    ip = ipaddress.ip_address(ip_texte)
    return any(ip in reseau for reseau in plages_sensibles)

print(est_sensible("10.0.0.50"))      # True
print(est_sensible("172.16.0.1"))     # False
```

`any(...)` renvoie `True` dès qu'une des plages contient l'IP.

## Application cyber — enrichir des IP extraites d'un log

On combine extraction (regex, chapitre 13), déduplication (`set`, chapitre 7) et classification réseau (`ipaddress`) pour enrichir les IP d'un log.

```python
import re
import ipaddress

# Log d'exemple : IP internes + de vraies IP publiques (ici des DNS publics,
# utilisés uniquement comme exemples de classification — aucune requête n'est faite).
texte_log = """
Failed password for root from 8.8.8.8
Accepted password for alice from 10.0.0.4
Failed password for admin from 1.1.1.1
Connexion interne depuis 192.168.1.20
"""

# 1. Extraire et dédoublonner les IP
ips = set(re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte_log))

# 2. Enrichir chaque IP
print("=== Enrichissement des IP ===")
for texte in sorted(ips):
    try:
        ip = ipaddress.ip_address(texte)
    except ValueError:
        print(f"[-] {texte} — IP invalide, ignorée")
        continue
    origine = "interne" if ip.is_private else "EXTERNE"
    priorite = "ok" if ip.is_private else "[!] à investiguer"
    print(f"{texte:<16} {origine:<8} {priorite}")
```

Résultat :

```
=== Enrichissement des IP ===
1.1.1.1          EXTERNE  [!] à investiguer
10.0.0.4         interne  ok
192.168.1.20     interne  ok
8.8.8.8          EXTERNE  [!] à investiguer
```

> Dans un vrai `auth.log`, les IP externes seraient des adresses publiques quelconques (souvent des IP d'attaquants). On a pris ici des DNS publics connus seulement pour que `is_private` renvoie un résultat fiable et vérifiable.

On a une chaîne complète : du texte brut d'un log à une liste d'IP enrichies et priorisées. Les IP externes sont automatiquement marquées pour investigation. C'est le cœur d'un enrichissement automatique en SOC.

## Bonus

### Gérer aussi l'IPv6

`ipaddress` gère l'IPv6 de la même façon :

```python
import ipaddress

ip = ipaddress.ip_address("2001:db8::1")
print(ip.version)        # 6
print(ip.is_private)     # dépend de la plage
```

Ton code n'a pas besoin de changer : `ip_address` détecte automatiquement v4 ou v6.

## ❌ Erreur classique

```python
import ipaddress

# Comparer des IP comme du texte (chapitre 4)
"203.0.113.9" < "203.0.113.10"     # ❌ False (comparaison alphabétique !)
ipaddress.ip_address("203.0.113.9") < ipaddress.ip_address("203.0.113.10")  # ✅ True

# Oublier que ip_address plante sur une valeur invalide
ipaddress.ip_address("999.1.1.1")  # ❌ ValueError
# → entoure d'un try/except pour valider

# Confondre ip_address (une adresse) et ip_network (un réseau)
ipaddress.ip_address("192.168.1.0/24")   # ❌ ValueError (c'est un réseau)
ipaddress.ip_network("192.168.1.0/24")   # ✅
```

## Exercices

**Guidé :** Crée un script `valide_ip.py` qui prend une IP en argument et affiche si elle est valide, et si oui, si elle est privée ou publique.

**Autonome :** Crée un script `tri_ip.py` qui prend plusieurs IP en arguments, ignore les invalides (avec `try/except`), et affiche deux listes : les internes et les externes.

**Défi :** Crée un script qui prend un fichier de log, extrait toutes les IP, et affiche uniquement les IP **publiques uniques** (celles venant d'Internet), triées.

## ✅ Tu sais maintenant…

- Pourquoi `ipaddress` est meilleur que la manipulation de texte pour les IP
- Inspecter une IP (`.is_private`, `.is_global`, `.version`)
- Valider une IP avec `try/except ValueError`
- Tester l'appartenance d'une IP à un réseau CIDR (`ip in reseau`)
- Classer des IP en interne/externe et les enrichir depuis un log

-----

# Chapitre 20 — Mini-projets cyber défensifs

> Voici huit mini-projets progressifs qui combinent tout le cours. Chacun est un vrai petit outil défensif. Commence par les premiers (plus simples) et garde les derniers comme défis. Pour chaque projet : un objectif, les notions mobilisées, et une trame de départ.

-----

## Projet 1 — Extracteur d'IOC depuis un texte

**Objectif :** lire un fichier texte (un email, un rapport) et extraire tous les IOC (IP, URLs, emails, hash), sans doublons, classés par type.

**Notions :** fichiers (ch. 10), regex (ch. 13), set/dictionnaires (ch. 7, 9), fonctions (ch. 8).

```python
import re
import sys

def extraire_iocs(texte):
    return {
        "ip": sorted(set(re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte))),
        "url": sorted(set(re.findall(r"https?://[^\s]+", texte))),
        "email": sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte))),
        "hash": sorted(set(re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte))),
    }

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier.txt>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        iocs = extraire_iocs(f.read())
    for type_ioc, valeurs in iocs.items():
        if valeurs:
            print(f"[+] {type_ioc.upper()} ({len(valeurs)}) : {valeurs}")

if __name__ == "__main__":
    main()
```

**Pour aller plus loin :** exporte le résultat en JSON ; ajoute la détection des hash défangés (`[.]`).

-----

## Projet 2 — Analyseur simple d'URL

**Objectif :** prendre une URL et produire une fiche : schéma, domaine, présence d'IP au lieu d'un domaine, extension suspecte, signaux d'alerte simples.

**Notions :** chaînes (ch. 6), regex (ch. 13), fonctions (ch. 8), conditions (ch. 5).

```python
import re
import sys

def analyser_url(url):
    fiche = {"url": url, "alertes": []}
    fiche["https"] = url.startswith("https://")
    sans_schema = re.sub(r"^https?://", "", url)
    fiche["domaine"] = sans_schema.split("/")[0].lower()

    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", fiche["domaine"]):
        fiche["alertes"].append("IP brute au lieu d'un domaine")
    if url.lower().endswith((".exe", ".scr", ".zip", ".js")):
        fiche["alertes"].append("extension potentiellement dangereuse")
    if not fiche["https"]:
        fiche["alertes"].append("connexion non chiffrée (http)")
    return fiche

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <url>")
        sys.exit(1)
    fiche = analyser_url(sys.argv[1])
    print(f"Domaine : {fiche['domaine']}")
    print(f"HTTPS   : {fiche['https']}")
    if fiche["alertes"]:
        for a in fiche["alertes"]:
            print(f"  [!] {a}")
    else:
        print("  [+] Aucun signal évident")

if __name__ == "__main__":
    main()
```

-----

## Projet 3 — Parser de logs SSH

**Objectif :** parser un `auth.log`, extraire les échecs par IP et par utilisateur, et afficher un résumé trié.

**Notions :** regex (ch. 13, 14), dictionnaires (ch. 9), fichiers (ch. 10), tri (ch. 7).

```python
import re
import sys

def parser(chemin):
    motif = re.compile(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})")
    par_ip, par_user = {}, {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            m = motif.search(ligne)
            if m:
                user, ip = m.group(1), m.group(2)
                par_ip[ip] = par_ip.get(ip, 0) + 1
                par_user[user] = par_user.get(user, 0) + 1
    return par_ip, par_user

# (ajoute un main() avec vérif d'argument et try/except FileNotFoundError)
```

**Défi :** ajoute l'horodatage et signale les IP avec « ≥ N échecs en peu de temps ».

-----

## Projet 4 — Compteur d'échecs de connexion (détecteur de force brute)

**Objectif :** à partir des échecs par IP (projet 3), appliquer un seuil et produire une liste d'IP à bloquer, exportée en fichier.

**Notions :** dictionnaires (ch. 9), conditions (ch. 5), fichiers (ch. 10), `ipaddress` (ch. 19).

```python
import ipaddress

def ips_a_bloquer(echecs_par_ip, seuil=5):
    """Retourne les IP publiques dépassant le seuil d'échecs."""
    a_bloquer = []
    for ip, nb in echecs_par_ip.items():
        if nb < seuil:
            continue
        try:
            if not ipaddress.ip_address(ip).is_private:   # on ne bloque pas l'interne à la légère
                a_bloquer.append((ip, nb))
        except ValueError:
            continue
    return sorted(a_bloquer, key=lambda x: x[1], reverse=True)
```

> **Rappel (voir chapitre 19) :** si tu testes cette fonction avec des IP de documentation (`203.0.113.x`, `198.51.100.x`), `is_private` peut les considérer comme non publiques et donc ne pas les retenir. Pour vérifier la logique « bloquer l'externe », teste avec de vraies IP publiques comme `8.8.8.8`.

-----

## Projet 5 — Calculateur de hash de fichiers

**Objectif :** calculer MD5/SHA-1/SHA-256 d'un ou plusieurs fichiers et écrire une fiche d'empreintes.

**Notions :** `hashlib` (ch. 18), `pathlib` (ch. 10), arguments (ch. 3), JSON (ch. 17).

```python
import hashlib, json, sys
from pathlib import Path

def empreintes(chemin):
    algos = {"md5": hashlib.md5(), "sha1": hashlib.sha1(), "sha256": hashlib.sha256()}
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            for h in algos.values():
                h.update(bloc)
    return {nom: h.hexdigest() for nom, h in algos.items()}

# main() : boucle sur sys.argv[1:], écrit les fiches dans empreintes.json
```

-----

## Projet 6 — Convertisseur CSV → JSON pour des IOC

**Objectif :** transformer un export CSV d'IOC en JSON structuré, en typant et normalisant chaque IOC.

**Notions :** CSV (ch. 10), JSON (ch. 17), regex/typage (ch. 15), fonctions (ch. 8).

```python
import csv, json, sys

def typer(valeur):
    import re
    valeur = valeur.strip().lower()
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur): return "ip"
    if re.fullmatch(r"[a-f0-9]{32}", valeur): return "md5"
    if re.fullmatch(r"[a-f0-9]{64}", valeur): return "sha256"
    if valeur.startswith("http"): return "url"
    return "domaine"

def convertir(csv_path, json_path):
    iocs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            valeur = ligne["valeur"].strip().lower()
            iocs.append({"value": valeur, "type": typer(valeur),
                         "confidence": int(ligne.get("confiance", 0))})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(iocs, f, indent=4, ensure_ascii=False)
    return len(iocs)
```

-----

## Projet 7 — Mini-outil SOC : log → résumé

**Objectif :** lire un fichier de log, produire un résumé complet (total de lignes, échecs, IP uniques, top des IP en échec, part interne/externe) et l'afficher proprement.

**Notions :** tout ! fichiers, regex, dictionnaires, `ipaddress`, fonctions, robustesse.

```python
import re, sys, ipaddress

def resumer(chemin):
    motif_ip = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
    total, echecs = 0, 0
    par_ip = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            total += 1
            if "Failed password" in ligne:
                echecs += 1
                m = motif_ip.search(ligne)
                if m:
                    ip = m.group()
                    par_ip[ip] = par_ip.get(ip, 0) + 1

    externes = 0
    for ip in par_ip:
        try:
            if not ipaddress.ip_address(ip).is_private:
                externes += 1
        except ValueError:
            pass

    return {"lignes": total, "echecs": echecs,
            "ips_uniques": len(par_ip), "ips_externes": externes,
            "top": sorted(par_ip.items(), key=lambda x: x[1], reverse=True)[:5]}

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>"); sys.exit(1)
    try:
        r = resumer(sys.argv[1])
    except FileNotFoundError:
        print("[-] Fichier introuvable"); sys.exit(1)
    print("=== Résumé SOC ===")
    print(f"Lignes      : {r['lignes']}")
    print(f"Échecs      : {r['echecs']}")
    print(f"IP uniques  : {r['ips_uniques']} (dont {r['ips_externes']} externes)")
    print("Top IP en échec :")
    for ip, nb in r["top"]:
        print(f"  {ip} : {nb}")

if __name__ == "__main__":
    main()
```

C'est l'aboutissement du cours : un vrai mini-SIEM en une cinquantaine de lignes.

-----

## Projet 8 — Client API très simple (source générique)

**Objectif :** interroger une API (de réputation, ici simulée par `httpbin`) pour une liste d'IOC, gérer les erreurs réseau, et produire un rapport JSON des verdicts.

**Notions :** `requests` (ch. 16), JSON (ch. 17), fonctions, robustesse, boucles.

```python
import requests, json, time

def interroger(ioc):
    """Interroge une API (à remplacer par ton fournisseur CTI réel)."""
    try:
        rep = requests.get("https://httpbin.org/get",
                           params={"ioc": ioc}, timeout=5)
        rep.raise_for_status()
        return {"ioc": ioc, "statut": "ok"}     # en réel : lire le verdict renvoyé
    except requests.exceptions.RequestException as e:
        return {"ioc": ioc, "statut": "erreur", "detail": str(e)}

def main():
    iocs = ["203.0.113.5", "198.51.100.9", "evil.example.com"]
    resultats = []
    for ioc in iocs:
        r = interroger(ioc)
        print(f"[+] {r['ioc']} → {r['statut']}")
        resultats.append(r)
        time.sleep(1)                            # respecter les quotas de l'API
    with open("verdicts.json", "w", encoding="utf-8") as f:
        json.dump(resultats, f, indent=4, ensure_ascii=False)
    print("[+] Rapport écrit dans verdicts.json")

if __name__ == "__main__":
    main()
```

**Rappel :** mets ta clé d'API dans une variable d'environnement, jamais dans le code.

-----

## ✅ Tu sais maintenant…

- Combiner toutes les notions du cours dans de vrais outils défensifs
- Construire un extracteur d'IOC, un analyseur d'URL, un parser de logs SSH
- Détecter la force brute et produire une liste d'IP à bloquer
- Calculer des empreintes de fichiers et convertir des IOC entre formats
- Assembler un mini-outil SOC complet (log → résumé)
- Écrire un client API défensif robuste

-----

# Conclusion

Tu es parti de zéro et tu disposes maintenant d'une vraie base : écrire des scripts Python clairs, structurés et **orientés défense**.

**Partie 1 — Les fondamentaux :**
- Script, variables, arguments (ch. 1-3)
- Calculs, logique, conditions (ch. 4-5)
- Chaînes, listes, boucles, fonctions, dictionnaires (ch. 6-9)
- Fichiers, CSV, JSON, erreurs, automatisation (ch. 10-12)

**Partie 2 — La cybersécurité défensive :**
- Regex et extraction d'IOC (ch. 13)
- Parsing de logs (ch. 14)
- Manipulation d'IOC (ch. 15)
- APIs et `requests` (ch. 16)
- JSON avancé CTI/SIEM (ch. 17)
- Hash avec `hashlib` (ch. 18)
- IP et réseaux avec `ipaddress` (ch. 19)
- Mini-projets défensifs (ch. 20)

**Pour continuer à progresser :**
- Écris des scripts pour tes propres besoins d'analyse — c'est la meilleure façon d'apprendre.
- `help(fonction)` dans le mode interactif reste ton meilleur ami.
- La documentation officielle [docs.python.org](https://docs.python.org) est excellente.
- Entraîne-toi sur des **logs et données de test** que tu génères toi-même, jamais sur des systèmes qui ne t'appartiennent pas.

**Prochaines étapes possibles (toujours côté défense) :**
- Approfondir les regex pour des formats de logs plus variés.
- Automatiser l'enrichissement d'IOC via plusieurs sources CTI.
- Stocker tes résultats dans une base `sqlite3` pour les requêter.
- Découvrir des bibliothèques d'analyse comme `pandas` pour de gros volumes de logs.
- Planifier tes scripts (cron) pour une surveillance continue.

**Rappel final d'éthique :** ces compétences servent à **protéger, détecter et comprendre**. N'analyse que des systèmes et des données que tu es autorisé à examiner. La cybersécurité défensive, c'est d'abord une question de responsabilité.

Bon scripting, et bonne défense !
