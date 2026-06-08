# Cours Complet d'Administration Linux

## De zéro à l'autonomie — Guide pour débutant absolu

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais ouvert un terminal de sa vie.
> Tout ce dont tu as besoin, c'est un ordinateur et la possibilité d'installer une machine Linux (on t'explique comment juste après).
>
> **Orientation :** ce cours t'apprend à **utiliser, comprendre et administrer** un système Linux depuis le terminal. La progression est utile pour l'administration système classique, mais aussi pour monter en compétence en **cybersécurité défensive (SOC), pentest débutant et eJPT**. Les concepts d'admin et de sécurité sont enseignés ensemble, au moment où ils ont du sens. On apprend à **comprendre et défendre** un système, jamais à attaquer celui des autres.

---

## Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas croiser tout au long du cours. Reviens ici dès qu'un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Terminal** | La fenêtre où tu tapes des commandes texte pour parler à ton ordinateur |
| **Shell** | Le programme qui lit et exécute tes commandes (Bash est le shell le plus courant) |
| **Commande** | Une instruction que le shell sait exécuter (`ls`, `cd`, `cat`…) |
| **Prompt** | L'invite de commande : le petit texte affiché avant ton curseur, qui attend que tu tapes |
| **Kernel (noyau)** | Le cœur du système : il fait le lien entre le matériel et les programmes |
| **Distribution (distro)** | Une version « prête à l'emploi » de Linux (Ubuntu, Debian, Kali…) |
| **Root** | Le super-administrateur : il a tous les droits sur la machine |
| **Utilisateur (user)** | Un compte qui utilise la machine, avec des droits limités |
| **Fichier** | Une unité de stockage : du texte, une image, un programme… |
| **Répertoire (dossier)** | Un conteneur qui range des fichiers et d'autres dossiers |
| **Chemin (path)** | L'adresse d'un fichier ou d'un dossier dans le système |
| **Arborescence** | L'organisation des dossiers en arbre, à partir d'une racine unique |
| **Paquet** | Un logiciel prêt à installer, avec tout ce dont il a besoin |
| **Démon (daemon)** | Un programme qui tourne en permanence en arrière-plan (ex. le serveur SSH) |
| **Processus** | Un programme en train de s'exécuter |
| **Permission (droit)** | Ce qu'un utilisateur a le droit de faire sur un fichier (lire, écrire, exécuter) |
| **Log (journal)** | Un fichier qui enregistre les événements du système (connexions, erreurs…) |
| **SSH** | Le protocole pour se connecter à distance à une machine, en sécurité |
| **Option (flag)** | Un réglage ajouté à une commande, souvent précédé d'un `-` (ex. `ls -l`) |
| **Argument** | L'information sur laquelle une commande agit (ex. le fichier dans `cat fichier.txt`) |
| **SOC** | *Security Operations Center* : l'équipe qui surveille et défend un système d'information |

---

## Comment penser Linux

Avant de taper la moindre commande, il faut comprendre **l'état d'esprit** de Linux. Si tu intègres ces trois idées, tout le reste deviendra logique.

### 1. Tout est fichier

En Linux, presque tout est représenté comme un fichier : un document texte évidemment, mais aussi un disque dur, une imprimante, une connexion réseau, ou même un processus. Cette idée paraît étrange au début, mais elle est **libératrice** : si tout est fichier, alors les mêmes outils (lire, copier, chercher) marchent partout. Tu apprends à manipuler des fichiers une fois, et tu sais manipuler presque tout le système.

### 2. De petits outils qu'on combine

La philosophie Linux, c'est : **un outil = une tâche, faite bien.** Plutôt qu'un énorme programme qui fait tout, Linux te donne plein de petites commandes simples. La puissance vient de leur **combinaison**. Par exemple : une commande lit un fichier de logs, une autre filtre les lignes intéressantes, une troisième les compte. Mises bout à bout, elles répondent à une vraie question. On verra ce mécanisme (les « tuyaux ») dès la Partie 1.

### 3. Le système te fait confiance

Linux part du principe que **tu sais ce que tu fais**. Si tu lui demandes de supprimer tous tes fichiers, il le fait, sans demander « êtes-vous sûr ? » et **sans corbeille**. C'est un outil professionnel, pas une interface grand public. Cette confiance est une force (tu contrôles tout) mais elle impose une **discipline** (voir l'encadré ci-dessous). C'est tout l'enjeu de ce cours : te donner le contrôle **et** les bons réflexes.

---

## ⚠️ Les commandes à manipuler avec prudence

> **Lis ce passage avant tout le reste, et reviens-y souvent.** Certaines commandes peuvent endommager le système ou détruire des données **sans confirmation et sans retour possible**. Tu ne les utiliseras pas tout de suite, mais tu dois savoir dès maintenant qu'elles existent et qu'elles demandent de l'attention.

Les commandes à connaître comme « sensibles » (on les verra en détail au fil du cours) :

| Commande | Pourquoi elle est dangereuse |
|----------|------------------------------|
| `rm -rf` | Supprime fichiers et dossiers en masse, définitivement, sans confirmation |
| `chmod -R` | Change les permissions en cascade : peut casser tout un dossier système |
| `chown -R` | Change le propriétaire en cascade : mêmes risques |
| `dd` | Écrit directement sur un disque : une erreur peut effacer un disque entier |
| `mkfs` | Formate (= efface) un système de fichiers |
| `mount` / `umount` | Peut perturber l'accès à un disque ou un partage |
| `>` sur un fichier important | Écrase tout le contenu du fichier sans prévenir |
| `sudo` sur un chemin système | Multiplie la portée d'une erreur par les droits administrateur |

### Les 3 règles d'or

1. **Toujours vérifier `pwd` et `ls` avant une commande destructive.** Sais-tu vraiment où tu es et sur quoi tu agis ? Vérifie avant d'appuyer sur Entrée.
2. **Toujours tester dans un dossier de lab.** Avant d'utiliser une commande puissante « pour de vrai », essaie-la dans un dossier de test sans importance.
3. **Toujours faire une copie `.bak` avant de modifier une configuration.** Une seule ligne (`cp config config.bak`) peut te sauver des heures. On en fera un réflexe au chapitre 6.

> Ces règles reviendront au bon moment dans le cours (surtout au chapitre 5, sur la suppression). Pour l'instant, garde-les simplement en tête : **la prudence n'est pas de la peur, c'est du professionnalisme.**

---

## Mettre en place ton environnement

Pour suivre ce cours, il te faut un Linux où **tu ne risques rien** : un endroit où tu peux tout casser et tout recommencer. Voici tes options, de la plus simple à la plus complète.

**Option 1 — Une machine virtuelle (recommandé).** Une machine virtuelle (VM) est un « ordinateur dans ton ordinateur ». Tu installes un logiciel comme **VirtualBox** (gratuit), puis tu y installes **Ubuntu** ou **Debian**. Avantage : c'est isolé, tu peux faire une sauvegarde de l'état (snapshot) et revenir en arrière si tu casses tout. C'est le bac à sable idéal.

**Option 2 — WSL (si tu es sur Windows).** Le *Windows Subsystem for Linux* te donne un vrai terminal Linux directement dans Windows, sans VM. Rapide à installer (`wsl --install` dans un terminal Windows administrateur). Parfait pour débuter sur les commandes, avec quelques limites sur la partie matériel/réseau qu'on verra plus tard.

**Option 3 — Un serveur cloud.** Beaucoup d'hébergeurs proposent de petites machines Linux pour quelques euros par mois. Utile plus tard pour t'entraîner au SSH et à l'administration distante (Partie 5). Pas indispensable pour commencer.

### Quelle distribution choisir ?

> **Ubuntu ou Debian sont la base de ce cours.** Ce sont les distributions les plus répandues, les mieux documentées, et celles que tu rencontreras le plus souvent en entreprise. **Tous les exemples du cours sont écrits pour elles.**
>
> Tu entendras peut-être parler de **Kali Linux**, très populaire en cybersécurité. Kali est excellente comme boîte à outils offensive, mais **ce n'est pas une distribution d'administration quotidienne** : on la mentionnera ponctuellement pour le contexte cyber, sans en faire la base du cours. Apprends d'abord à administrer un système classique ; les outils spécialisés viendront ensuite.

### Installer un outil quand tu en as besoin

Linux n'installe pas tous les programmes par défaut. Quand le cours te demandera un outil qui n'est pas présent (par exemple `tree` ou `htop`), tu utiliseras **deux commandes** :

```bash
sudo apt update              # met à jour la liste des logiciels disponibles
sudo apt install tree        # installe le paquet "tree"
```

> **Pour l'instant, retiens juste ce réflexe :** `sudo apt update` puis `sudo apt install <nom-du-paquet>`. Tu n'as **rien à installer maintenant** : on le fera au cas par cas, au moment où chaque outil devient utile. La gestion complète des paquets (mises à jour, suppression, recherche…) est expliquée en détail au **chapitre 20**.

---

## Table des matières

### Partie 0 — Avant de commencer
*(glossaire, état d'esprit, prudence, installation — ci-dessus)*

### Partie 1 — Survivre dans le terminal
1. [Le terminal, le shell et l'aide](#chapitre-1--le-terminal-le-shell-et-laide)
2. [Se repérer dans l'arborescence](#chapitre-2--se-repérer-dans-larborescence)
3. [Lire le contenu des fichiers](#chapitre-3--lire-le-contenu-des-fichiers)
4. [Chercher, filtrer et transformer du texte](#chapitre-4--chercher-filtrer-et-transformer-du-texte)

### Partie 2 — Manipuler le système de fichiers
5. [Créer, copier, déplacer, supprimer](#chapitre-5--créer-copier-déplacer-supprimer)
6. [Éditer des fichiers dans le terminal](#chapitre-6--éditer-des-fichiers-dans-le-terminal)
7. [Liens, redirections et tuyaux](#chapitre-7--liens-redirections-et-tuyaux)
8. [Variables d'environnement et configuration du shell](#chapitre-8--variables-denvironnement-et-configuration-du-shell)

### Partie 3 — Qui a le droit de quoi
9. [Comprendre les permissions](#chapitre-9--comprendre-les-permissions)
10. [Propriété, utilisateurs et groupes](#chapitre-10--propriété-utilisateurs-et-groupes)
11. [sudo et l'élévation de privilèges](#chapitre-11--sudo-et-lélévation-de-privilèges)
12. [Permissions avancées (panorama)](#chapitre-12--permissions-avancées-panorama)

### Partie 4 — La machine vivante
13. [Les processus](#chapitre-13--les-processus)
14. [Les services avec systemd](#chapitre-14--les-services-avec-systemd)
15. [Les logs et journaux](#chapitre-15--les-logs-et-journaux)
16. [Tâches planifiées](#chapitre-16--tâches-planifiées)

### Partie 5 — Linux en réseau
17. [Les bases du réseau Linux](#chapitre-17--les-bases-du-réseau-linux)
18. [SSH : se connecter à distance](#chapitre-18--ssh--se-connecter-à-distance)
19. [Transférer des fichiers](#chapitre-19--transférer-des-fichiers)

### Partie 6 — Entretenir le système
20. [Gérer les paquets et logiciels](#chapitre-20--gérer-les-paquets-et-logiciels)
21. [Stockage et espace disque](#chapitre-21--stockage-et-espace-disque)
22. [Archives et compression](#chapitre-22--archives-et-compression)
23. [Sauvegardes](#chapitre-23--sauvegardes)

### Partie 7 — Diagnostiquer, sécuriser, automatiser
24. [Diagnostic système (méthode)](#chapitre-24--diagnostic-système-méthode)
25. [Sécurité de base (durcissement)](#chapitre-25--sécurité-de-base-durcissement)
26. [Automatiser avec Bash (admin)](#chapitre-26--automatiser-avec-bash-admin)
27. [Mini-projets pratiques](#chapitre-27--mini-projets-pratiques)

### Synthèse finale
- Cheat-sheets, erreurs classiques, arbre de décision, pour continuer

### Annexes
- Regex, sed/awk avancés, stockage avancé, pare-feu avancé, conteneurs, familles de distributions

---
---

# PARTIE 1 — Survivre dans le terminal

Avant de pouvoir administrer quoi que ce soit, il faut savoir **exister** dans le terminal : comprendre ce qu'on voit, se déplacer, lire des fichiers et y chercher de l'information — le tout **sans rien casser**. Cette première partie est volontairement « en lecture seule » : on observe, on explore, on s'oriente. On apprendra à modifier les choses dans la Partie 2, une fois qu'on sera à l'aise.

---

# Chapitre 1 — Le terminal, le shell et l'aide

## Le minimum à savoir

### Terminal, shell : quelle différence ?

Quand tu ouvres une « fenêtre noire » pour taper des commandes, deux choses travaillent ensemble :

- Le **terminal**, c'est la fenêtre elle-même : l'endroit où s'affiche le texte et où tu tapes.
- Le **shell**, c'est le programme qui tourne *dans* cette fenêtre, qui **lit** ce que tu tapes et **exécute** tes commandes. Le shell le plus courant s'appelle **Bash**.

Une image simple : le terminal est le **téléphone** (l'appareil), le shell est la **personne** à l'autre bout qui comprend ce que tu dis et agit. Pour débuter, tu peux utiliser les deux mots de façon assez interchangeable ; retiens juste que c'est le shell qui « comprend » tes commandes.

### Lire le prompt (l'invite de commande)

Quand le terminal est prêt, il affiche une **invite de commande** (ou *prompt*). Elle ressemble souvent à ceci :

```
alice@serveur:~$
```

Décortiquons-la, car elle est pleine d'informations utiles :

- `alice` → ton nom d'utilisateur (qui tu es)
- `serveur` → le nom de la machine (où tu es connecté)
- `~` → le dossier où tu te trouves actuellement (`~` signifie « ton dossier personnel »)
- `$` → indique que tu es un utilisateur normal *(un `#` à la place signifierait que tu es root, le super-administrateur)*

> **Le `$` final est un repère essentiel.** Dans ce cours, quand tu vois `$` au début d'une ligne d'exemple, ça représente le prompt : tu ne tapes pas le `$`, seulement ce qui suit.

### L'anatomie d'une commande

Presque toutes les commandes suivent la même structure :

```
commande   -options   arguments
```

Exemple concret :

```bash
ls -l /home
```

- `ls` → la **commande** (ici : « lister le contenu d'un dossier »)
- `-l` → une **option** (ici : « format long », avec plus de détails). Les options modifient le comportement de la commande et commencent presque toujours par `-`.
- `/home` → l'**argument** (ici : *quel* dossier lister)

Cette structure est universelle. Dès que tu vois une commande inconnue, essaie de la découper ainsi : quelle est l'action ? quels réglages ? sur quoi ?

### Tes premières commandes

Voici quatre commandes inoffensives pour te faire la main. Elles ne modifient rien.

```bash
whoami       # affiche ton nom d'utilisateur
hostname     # affiche le nom de la machine
date         # affiche la date et l'heure
echo Bonjour # affiche le texte que tu lui donnes
```

`echo` mérite une mention : elle se contente d'**afficher** ce que tu lui passes. Ça semble inutile, mais c'est l'une des commandes les plus utilisées en pratique (pour afficher des messages, vérifier une valeur, écrire dans des fichiers plus tard…).

```bash
echo "Le terminal n'est pas si effrayant"
```

## Très utile en pratique

### Trouver de l'aide tout seul

Personne ne connaît toutes les commandes par cœur. Le vrai réflexe d'un bon administrateur, ce n'est pas de tout savoir, c'est de **savoir où chercher**. Linux embarque sa propre documentation.

**Le manuel : `man`**

```bash
man ls
```

Cela ouvre le **manuel** de la commande `ls` : description, liste des options, exemples. Tu navigues avec les flèches, et tu **quittes en appuyant sur la touche `q`** (pour *quit*). Retiens bien ce `q`, c'est la sortie de secours de beaucoup d'outils.

**L'aide rapide : `--help`**

Plus court que le manuel, souvent suffisant :

```bash
ls --help
```

Cela affiche un résumé des options directement dans le terminal, sans ouvrir de manuel.

**Chercher une commande par mot-clé : `apropos`**

Tu ne connais pas le nom de la commande, mais tu sais ce que tu veux faire ?

```bash
apropos copy     # liste les commandes liées à "copy"
```

**Savoir ce qu'est une commande : `type`**

```bash
type ls          # te dit si c'est un programme, un alias, etc.
```

### L'historique : ne retape jamais deux fois

Le shell **se souvient** de ce que tu as tapé. Deux outils t'évitent de retaper :

- La **flèche du haut (↑)** rappelle les commandes précédentes, une par une.
- La commande `history` affiche toute la liste de ce que tu as tapé.

```bash
history          # affiche l'historique numéroté de tes commandes
```

Et pour repartir d'un écran propre :

```bash
clear            # efface l'écran (l'historique, lui, reste intact)
```

> **Astuce :** la combinaison de touches `Ctrl + L` fait la même chose que `clear`, sans rien taper.

## ❌ Erreur classique

```bash
# Taper la commande pour quitter "man" au lieu d'appuyer sur q
man ls
quit             # ❌ ne fait rien d'utile, tu es toujours dans le manuel
# ✅ Appuie simplement sur la touche q

# Confondre option et argument
ls /home -l      # fonctionne souvent, mais l'ordre logique est :
ls -l /home      # ✅ options d'abord, arguments ensuite

# Oublier que Linux est sensible à la casse
Date             # ❌ commande introuvable
date             # ✅ tout en minuscules

# Croire qu'il faut taper le $ du prompt
$ whoami         # ❌ le $ représente le prompt, ne le tape pas
whoami           # ✅
```

> **La sensibilité à la casse** est une source d'erreurs constante chez les débutants. Sous Linux, `Date`, `DATE` et `date` sont trois choses différentes. La quasi-totalité des commandes sont en **minuscules**.

## Exercices

**Guidé :** Ouvre le manuel de la commande `date` avec `man date`. Cherche dans le manuel comment afficher uniquement l'année (indice : il existe un format avec `+%Y`). Quitte le manuel avec `q`, puis teste la commande que tu as trouvée.

**Autonome :** Sans utiliser Internet, trouve à quoi sert la commande `uptime` (utilise `man` ou `--help`), puis exécute-la. Que t'apprend-elle sur la machine ?

**Défi :** Utilise `apropos` pour trouver une commande qui affiche le calendrier du mois. Une fois trouvée, exécute-la, puis consulte son manuel pour afficher le calendrier de l'année entière.

## ✅ Tu sais maintenant…

- La différence entre le **terminal** (la fenêtre) et le **shell** (le programme qui exécute)
- Lire un **prompt** : qui tu es, où tu es, et si tu es root (`$` vs `#`)
- Décortiquer une commande en **commande + options + arguments**
- Afficher des informations de base : `whoami`, `hostname`, `date`, `echo`
- Te débloquer seul avec `man`, `--help`, `apropos` et `type` (et **quitter `man` avec `q`**)
- Réutiliser tes commandes avec la **flèche du haut** et `history`
- Que Linux est **sensible à la casse** : `date` ≠ `Date`

---

# Chapitre 2 — Se repérer dans l'arborescence

## Le minimum à savoir

### Le système de fichiers est un arbre

Sous Windows, tu as plusieurs « disques » (`C:`, `D:`…). Sous Linux, c'est différent : **tout part d'un point unique**, appelé la **racine**, notée `/` (une simple barre oblique). À partir de cette racine, les dossiers se ramifient comme les branches d'un arbre.

```
/                        ← la racine : le sommet de tout
├── home/                ← les dossiers personnels des utilisateurs
│   └── alice/           ← le dossier personnel d'alice
├── etc/                 ← les fichiers de configuration du système
├── var/                 ← les données variables (logs, etc.)
│   └── log/             ← les journaux du système
├── bin/                 ← les programmes (commandes) de base
└── tmp/                 ← les fichiers temporaires
```

Tout fichier, où qu'il soit, descend de cette racine `/`. Il n'y a pas de second arbre : un seul, qui contient tout.

### Où suis-je ? `pwd`

La toute première question quand on est perdu : **dans quel dossier suis-je ?** La commande `pwd` (*print working directory*, « affiche le dossier de travail ») répond :

```bash
pwd
# affiche par exemple : /home/alice
```

> **Réflexe à prendre dès maintenant :** quand tu ne sais plus où tu es, tape `pwd`. C'est gratuit et ça évite les catastrophes (souviens-toi de la première règle d'or : vérifier où on est avant d'agir).

### Que contient ce dossier ? `ls`

`ls` (*list*) liste le contenu du dossier courant :

```bash
ls
```

Cette commande devient bien plus puissante avec ses options :

```bash
ls -l      # format "long" : permissions, propriétaire, taille, date
ls -a      # affiche TOUT, y compris les fichiers cachés (qui commencent par .)
ls -h      # tailles "lisibles" (Ko, Mo, Go) — à combiner avec -l
ls -t      # trie par date de modification (plus récent en premier)
```

On peut **combiner les options** :

```bash
ls -lah    # format long + fichiers cachés + tailles lisibles
```

> **Les fichiers cachés** ne sont pas « secrets » : ce sont simplement des fichiers dont le nom commence par un point (`.bashrc`, `.ssh`…). Linux les masque par défaut pour ne pas encombrer l'affichage. On en croisera beaucoup ; `ls -a` est le moyen de les voir.

### Se déplacer : `cd`

`cd` (*change directory*) te déplace d'un dossier à un autre :

```bash
cd /var/log      # va dans le dossier /var/log
cd /             # va à la racine
cd ~             # va dans ton dossier personnel
cd               # (sans rien) va aussi dans ton dossier personnel
```

## Très utile en pratique

### Chemins absolus et chemins relatifs

C'est **le** concept à maîtriser dans ce chapitre. Il y a deux façons d'indiquer où se trouve un fichier.

**Le chemin absolu** part toujours de la racine `/`. C'est une adresse complète, qui marche **depuis n'importe où** :

```bash
cd /home/alice/documents     # adresse complète, sans ambiguïté
```

**Le chemin relatif** part de là où tu te trouves *en ce moment*. Plus court, mais il dépend de ta position actuelle :

```bash
cd documents     # va dans le dossier "documents" situé ICI
```

Pour t'y retrouver, deux raccourcis essentiels :

- `.` → le dossier **courant** (là où tu es)
- `..` → le dossier **parent** (juste au-dessus)

```bash
cd ..            # remonte d'un niveau
cd ../..         # remonte de deux niveaux
cd ./scripts     # va dans "scripts", ici (le ./ est souvent optionnel)
```

Et deux raccourcis bien pratiques :

- `~` → ton dossier personnel (`/home/alice`)
- `cd -` → revient au **dossier précédent** (comme un bouton « retour »)

```bash
cd /var/log
cd -             # retourne là où tu étais juste avant
```

> **Image mentale :** un chemin absolu, c'est donner ton adresse postale complète (pays, ville, rue, numéro). Un chemin relatif, c'est dire « la deuxième porte à gauche » — ça ne marche que si on sait d'où tu pars.

### Visualiser l'arbre : `tree`

La commande `tree` affiche les dossiers sous forme d'arbre, ce qui est très parlant :

```bash
tree
```

Elle n'est pas toujours installée. Si tu obtiens « command not found », installe-la (tu te souviens du réflexe de la Partie 0) :

```bash
sudo apt update
sudo apt install tree
```

Pour ne pas être noyé, limite la profondeur affichée :

```bash
tree -L 2        # n'affiche que 2 niveaux de profondeur
```

### Les grands dossiers de Linux (le FHS)

Linux range ses fichiers selon une norme appelée **FHS** (*Filesystem Hierarchy Standard*). Tu n'as pas à tout retenir, mais reconnaître ces dossiers t'aidera énormément :

| Dossier | Ce qu'il contient |
|---------|-------------------|
| `/` | La racine : le point de départ de tout |
| `/home` | Les dossiers personnels des utilisateurs (`/home/alice`…) |
| `/root` | Le dossier personnel de l'administrateur root (attention, différent de `/`) |
| `/etc` | Les fichiers de **configuration** du système (« et cetera ») |
| `/var` | Les données qui **varient** : surtout les **logs** dans `/var/log` |
| `/bin`, `/usr/bin` | Les **programmes** (les commandes que tu tapes y vivent) |
| `/tmp` | Les fichiers **temporaires** (effacés au redémarrage) |
| `/dev` | Les **périphériques** (disques, etc.) — souviens-toi : « tout est fichier » |

> **Très utile en sécurité :** `/etc` (configurations) et `/var/log` (journaux) sont les deux dossiers que tu visiteras le plus souvent en administration et en analyse de sécurité. Note-les dès maintenant.

## ❌ Erreur classique

```bash
# Oublier où on est et lancer une commande au mauvais endroit
ls               # ❓ et si tu n'es pas dans le bon dossier ?
pwd              # ✅ vérifie TOUJOURS d'abord

# Confondre / au début (racine) et / au milieu (séparateur)
cd /home/alice   # le premier / = racine, les autres = séparateurs

# Croire que "cd .." peut dépasser la racine
cd /
cd ..            # reste à la racine : on ne peut pas remonter plus haut

# Taper le chemin avec une mauvaise casse
cd /Home/Alice   # ❌ introuvable
cd /home/alice   # ✅

# Mettre un espace dans un nom sans le protéger
cd Mes Documents     # ❌ Linux croit à deux arguments
cd "Mes Documents"   # ✅ entre guillemets
cd Mes\ Documents    # ✅ ou en échappant l'espace
```

## Exercices

**Guidé :** Depuis ton dossier personnel (`cd ~`), rends-toi dans `/var/log` en utilisant un **chemin absolu**. Vérifie avec `pwd` que tu y es bien. Liste son contenu avec `ls -l`. Puis reviens à ton point de départ avec `cd -`.

**Autonome :** Place-toi à la racine (`cd /`). Sans jamais utiliser de chemin absolu (uniquement `cd nom`, `cd ..`, etc.), navigue jusqu'à `/usr/bin`, vérifie ta position avec `pwd`, puis remonte jusqu'à la racine uniquement avec `..`.

**Défi :** Affiche l'arborescence de `/etc` sur 2 niveaux de profondeur seulement, et compare la quantité d'informations avec un `ls` simple du même dossier. Lequel est plus lisible pour avoir une vue d'ensemble ?

## ✅ Tu sais maintenant…

- Que le système Linux est un **arbre unique** partant de la racine `/`
- Répondre à « où suis-je ? » avec `pwd` (le réflexe anti-catastrophe)
- Lister un dossier avec `ls` et ses options clés : `-l`, `-a`, `-h`, `-t`
- Te déplacer avec `cd`, et utiliser `~`, `..`, `.` et `cd -`
- La différence **fondamentale** entre chemin **absolu** (part de `/`) et **relatif** (part d'où tu es)
- Reconnaître les grands dossiers du **FHS**, en particulier `/etc` et `/var/log`
- Protéger les noms contenant des **espaces** avec des guillemets

---

# Chapitre 3 — Lire le contenu des fichiers

## Le minimum à savoir

### Pourquoi lire avant d'agir

En administration, **on regarde avant de toucher**. Avant de modifier une configuration, on la lit. Avant de supprimer un fichier, on vérifie son contenu. Avant de comprendre un problème, on lit les logs. Ce chapitre te donne les outils pour **consulter** un fichier sans aucun risque de le modifier — c'est la suite logique de notre approche « lecture seule ».

### Texte ou binaire ? `file`

Tous les fichiers ne se lisent pas de la même façon. Un fichier **texte** (configuration, log, script) se lit directement. Un fichier **binaire** (image, programme) afficherait du charabia illisible si tu tentais de le lire comme du texte. Avant de lire un fichier inconnu, demande à Linux de quoi il s'agit :

```bash
file /etc/hostname       # → texte
file /bin/ls             # → exécutable (binaire)
```

> **Réflexe utile :** si une commande de lecture remplit ton écran de symboles incompréhensibles et fait « biper » le terminal, c'est probablement un fichier binaire. Ferme avec `q` ou `Ctrl + C`, et vérifie avec `file`.

### Afficher un fichier entier : `cat`

`cat` affiche tout le contenu d'un fichier d'un coup :

```bash
cat /etc/hostname        # affiche le nom de la machine
```

`cat` est parfait pour les **petits** fichiers. Mais sur un gros fichier (un log de plusieurs milliers de lignes), tout défile d'un coup et tu ne vois que la fin : peu pratique. D'où les outils suivants.

### Lire confortablement : `less`

`less` affiche un fichier **page par page**, sans tout déverser à l'écran :

```bash
less /var/log/syslog
```

Pendant que `less` est ouvert :

- **Flèches** ou **Espace** → naviguer (Espace = page suivante)
- **`/motcherché`** → rechercher un mot dans le fichier
- **`q`** → quitter (le même `q` que pour `man` — et pour cause, `man` utilise `less` !)

> **Le minimum à savoir :** pour les **petits** fichiers, `cat`. Pour les **gros** fichiers, `less`. Cette distinction simple t'évite bien des écrans qui défilent dans le vide.

### Voir le début ou la fin : `head` et `tail`

Souvent, tu ne veux que le **début** ou la **fin** d'un fichier :

```bash
head fichier.log         # les 10 premières lignes
tail fichier.log         # les 10 dernières lignes
head -n 5 fichier.log    # les 5 premières lignes
tail -n 20 fichier.log   # les 20 dernières lignes
```

`tail` est particulièrement précieux pour les logs : les événements les plus récents sont **à la fin** du fichier. Quand un problème vient de se produire, `tail` te montre tout de suite ce qui s'est passé en dernier.

## Très utile en pratique

### Suivre un log en direct : `tail -f`

Voici l'une des commandes les plus utiles de tout le cours. L'option `-f` (*follow*, « suivre ») garde le fichier ouvert et affiche **les nouvelles lignes en temps réel**, au fur et à mesure qu'elles s'ajoutent :

```bash
tail -f /var/log/syslog
```

L'écran ne se ferme pas : il attend et affiche chaque nouvel événement dès qu'il arrive. C'est exactement ce qu'on utilise pour **observer un système en train de fonctionner** : surveiller les connexions, voir un service démarrer, repérer une erreur dès qu'elle survient. Pour arrêter le suivi, appuie sur **`Ctrl + C`**.

> **Très utile en sécurité (SOC) :** `tail -f` sur un journal d'authentification permet de voir **en direct** les tentatives de connexion à une machine. C'est un réflexe d'analyste : ouvrir le log, le suivre, et regarder ce qui frappe à la porte.

### Compter : `wc`

`wc` (*word count*) compte les lignes, les mots et les caractères d'un fichier :

```bash
wc fichier.txt           # lignes, mots, caractères
wc -l fichier.txt        # uniquement le nombre de LIGNES
```

L'option `-l` est la plus utilisée : « combien de lignes ? » est une question fréquente (combien d'événements dans ce log ? combien d'utilisateurs dans ce fichier ?). On l'exploitera beaucoup au chapitre 4.

### Numéroter les lignes : `nl`

Pratique pour discuter d'un fichier ligne par ligne, ou repérer une ligne précise :

```bash
nl fichier.conf          # affiche le fichier avec un numéro devant chaque ligne
```

## ❌ Erreur classique

```bash
# Faire un "cat" sur un fichier énorme
cat /var/log/syslog      # ❌ des milliers de lignes défilent, illisible
less /var/log/syslog     # ✅ page par page

# Faire un "cat" sur un binaire
cat /bin/ls              # ❌ charabia + bips, le terminal devient bizarre
file /bin/ls             # ✅ vérifie d'abord ce que c'est

# Rester coincé dans less sans savoir en sortir
# ✅ La sortie est TOUJOURS la touche q

# Oublier le -n et passer un nombre directement
head -5 fichier          # fonctionne sur beaucoup de systèmes, mais
head -n 5 fichier        # ✅ la forme correcte et portable

# Lancer tail -f et croire que le terminal est figé
tail -f log              # il n'est pas figé, il ATTEND de nouvelles lignes
# ✅ Ctrl + C pour reprendre la main
```

> **Si ton terminal devient illisible** après avoir affiché un binaire (caractères bizarres même quand tu tapes), la commande `reset` le remet d'aplomb.

## Exercices

**Guidé :** Affiche les 3 premières lignes du fichier `/etc/passwd` avec `head`, puis ses 3 dernières lignes avec `tail`. Ensuite, compte combien de lignes contient ce fichier avec `wc -l`. Chaque ligne correspond à un compte utilisateur du système : combien y en a-t-il ?

**Autonome :** Utilise `file` sur trois éléments différents : `/etc/hostname`, `/bin/ls` et le dossier `/etc` lui-même. Note ce que `file` répond pour chacun. Lequel peux-tu lire avec `cat` sans danger ?

**Défi :** Lance `tail -f /var/log/syslog` dans ton terminal pour suivre le journal système en direct. Pendant que ça tourne, observe si de nouvelles lignes apparaissent. Au bout d'un moment, arrête proprement le suivi. *(Si `/var/log/syslog` n'existe pas sur ton système, on verra au chapitre 4 et 15 où trouver les bons journaux selon ta distribution.)*

## ✅ Tu sais maintenant…

- Que l'on **lit avant d'agir** : consulter un fichier ne le modifie jamais
- Distinguer un fichier **texte** d'un **binaire** avec `file`
- Afficher un fichier : `cat` pour les petits, `less` pour les gros (sortie : `q`)
- Voir le **début** (`head`) et la **fin** (`tail`) d'un fichier, avec `-n`
- Suivre un log **en temps réel** avec `tail -f` (et reprendre la main avec `Ctrl + C`)
- **Compter** les lignes d'un fichier avec `wc -l`
- Numéroter les lignes avec `nl`, et réparer un terminal abîmé avec `reset`

---

# Chapitre 4 — Chercher, filtrer et transformer du texte

## Le minimum à savoir

### L'idée : filtrer un flux

Au chapitre précédent, on **affichait** des fichiers. Maintenant, on va **chercher** dedans et n'en garder que l'utile. C'est une compétence centrale : un fichier de logs peut contenir des dizaines de milliers de lignes, et tu n'en cherches souvent qu'une poignée. L'art de l'administrateur, c'est de **réduire le bruit pour ne voir que le signal**.

### Chercher un texte : `grep`

`grep` est sans doute la commande la plus utilisée de tout l'univers Linux. Elle cherche un motif dans un fichier et n'affiche **que les lignes qui le contiennent** :

```bash
grep "erreur" fichier.log        # affiche les lignes contenant "erreur"
```

Ses options indispensables :

```bash
grep -i "erreur" fichier.log     # -i : ignore la casse (Erreur, ERREUR, erreur)
grep -n "erreur" fichier.log     # -n : affiche le numéro de chaque ligne trouvée
grep -v "erreur" fichier.log     # -v : INVERSE — lignes qui NE contiennent PAS le mot
grep -c "erreur" fichier.log     # -c : COMPTE le nombre de lignes correspondantes
grep -r "erreur" /etc/           # -r : cherche RÉCURSIVEMENT dans tout un dossier
```

> **Le minimum à savoir :** `grep "ce que je cherche" dans-quel-fichier`. Avec juste ça et les options `-i`, `-n`, `-v`, `-c`, tu réponds déjà à l'immense majorité des besoins de recherche.

### Trouver des fichiers : `find`

`grep` cherche **dans** les fichiers. `find` cherche **les fichiers eux-mêmes**, par leur nom, leur date, leur taille… Elle parcourt l'arborescence à partir d'un dossier de départ :

```bash
find /etc -name "*.conf"         # tous les fichiers .conf sous /etc
find /home -name "rapport.txt"   # le fichier nommé rapport.txt sous /home
find . -name "*.log"             # tous les .log à partir d'ici (.)
```

La structure de `find` est : `find <où chercher> <critère>`. Le critère le plus courant est `-name` (par nom). L'astérisque `*` signifie « n'importe quelle suite de caractères » : `*.conf` veut dire « tout ce qui se termine par `.conf` ».

### Une alternative rapide : `locate`

`locate` cherche dans une base de données préconstruite, donc c'est **très rapide**, mais la base n'est pas toujours à jour ni installée par défaut :

```bash
locate hostname              # trouve très vite les chemins contenant "hostname"
```

> `find` est toujours fiable (il regarde le système réel, en direct) mais plus lent. `locate` est instantané mais peut rater un fichier récent. Pour débuter, **privilégie `find`** : il ne ment jamais.

## Très utile en pratique

### Le tuyau (pipe) `|` : enchaîner les commandes

Voici l'idée la plus puissante de la Partie 1. Le caractère `|` (appelé *pipe*, ou « tuyau ») prend la **sortie** d'une commande et l'envoie comme **entrée** à la commande suivante. On enchaîne ainsi de petits outils pour répondre à une question précise :

```bash
cat fichier.log | grep "erreur"      # affiche le fichier, PUIS n'en garde que les erreurs
```

C'est exactement la philosophie « petits outils combinés » vue en Partie 0, rendue concrète. On peut chaîner plusieurs pipes :

```bash
cat fichier.log | grep "erreur" | wc -l    # COMBIEN de lignes contiennent "erreur" ?
```

Ici : on lit le fichier → on garde les erreurs → on les compte. Trois outils simples, une réponse précise.

> **Note importante :** ici, on utilise les pipes de façon **pratique**, comme un tuyau qui relie des commandes — c'est suffisant pour ce chapitre. Le fonctionnement complet des flux (entrée, sortie, sortie d'erreur, redirections vers des fichiers) sera expliqué proprement au **chapitre 7**. Pour l'instant, retiens juste : `|` envoie le résultat de gauche vers la commande de droite.

### Trier et dédoublonner : `sort` et `uniq`

```bash
sort fichier.txt             # trie les lignes par ordre alphabétique
sort -n fichier.txt          # -n : trie numériquement (1, 2, 10) et non (1, 10, 2)
uniq fichier.txt             # supprime les doublons CONSÉCUTIFS
```

> **Le duo classique :** `uniq` ne supprime que les doublons **qui se suivent**. Il faut donc presque toujours trier **avant** : `sort | uniq`. Encore mieux, `sort | uniq -c` trie, dédoublonne **et compte** combien de fois chaque ligne apparaît — extrêmement utile pour répondre à « quelle valeur revient le plus souvent ? ».

### Extraire une colonne : `cut`

Beaucoup de fichiers système sont organisés en colonnes séparées par un caractère. `cut` extrait la colonne qui t'intéresse :

```bash
cut -d: -f1 /etc/passwd      # -d: séparateur ":"   -f1 : 1re colonne
```

Le fichier `/etc/passwd` sépare ses champs par des `:`. La première colonne est le **nom d'utilisateur**. Cette commande liste donc tous les comptes du système. (`-d` = *delimiter*, le séparateur ; `-f` = *field*, le numéro de colonne.)

### Transformer du texte : `tr`, `sed`, `awk` (initiation)

Ces trois outils **transforment** le texte. On les introduit ici pour des cas **simples** : ils te seront indispensables pour traiter des logs. *(Leurs usages avancés dépassent le cadre d'un cours débutant et sont laissés en annexe.)*

**`tr`** — remplace ou supprime des caractères :

```bash
echo "BONJOUR" | tr 'A-Z' 'a-z'      # → bonjour (met tout en minuscules)
```

**`sed`** — remplace un motif par un autre (substitution) :

```bash
sed 's/ancien/nouveau/g' fichier.txt    # remplace "ancien" par "nouveau" partout
```

La syntaxe `s/.../.../g` se lit : *substitute* (remplacer) `s/ce-qu-on-cherche/ce-qu-on-met/g`, le `g` final signifiant « partout sur la ligne » (*global*).

**`awk`** — extrait une colonne, façon `cut` mais plus souple :

```bash
awk '{print $1}' fichier.txt             # affiche la 1re colonne (séparée par espaces)
awk -F: '{print $1}' /etc/passwd         # -F: change le séparateur en ":"
```

`$1` désigne la première colonne, `$2` la deuxième, etc. C'est parfait pour isoler une information précise dans une ligne de log.

> **Pour débuter, retiens juste ces quatre formes :** `tr 'A-Z' 'a-z'` (changer la casse), `sed 's/x/y/g'` (remplacer), `awk '{print $1}'` (extraire une colonne par espaces), `awk -F: '{print $1}'` (extraire une colonne par un autre séparateur). C'est largement suffisant pour traiter des logs au niveau débutant.

## Où sont les logs d'authentification ?

Plusieurs exercices de ce chapitre utilisent un journal d'authentification (les tentatives de connexion). **Son emplacement dépend de ta distribution :**

- Sur **Debian / Ubuntu** : `/var/log/auth.log`
- Sur **RHEL / CentOS / Fedora** : `/var/log/secure`
- Sur **tout système moderne avec systemd** : la méthode la plus fiable est `journalctl` (on l'étudiera en détail au **chapitre 15**)

> Si un fichier d'exemple n'existe pas chez toi, ce n'est pas une erreur de ta part : c'est juste que ta distribution range ses logs ailleurs. Adapte le chemin, ou note que `journalctl` sera la solution universelle vue plus tard.

## ❌ Erreur classique

```bash
# Oublier les guillemets quand le motif contient un espace
grep Failed password auth.log    # ❌ cherche "Failed" dans les fichiers "password" et "auth.log"
grep "Failed password" auth.log  # ✅ le motif entier entre guillemets

# Utiliser uniq sans trier avant
uniq fichier.txt                 # ❌ rate les doublons non consécutifs
sort fichier.txt | uniq          # ✅ trier d'abord

# Trier des nombres sans -n
sort fichier.txt                 # ❌ ordre alphabétique : 1, 10, 2, 20, 3
sort -n fichier.txt              # ✅ ordre numérique : 1, 2, 3, 10, 20

# Se tromper de sens avec grep -v
grep -v "ok" log                 # garde les lignes SANS "ok" (inversion) — voulu ?

# Confondre find et grep
find /etc -name "erreur"         # cherche un FICHIER nommé "erreur"
grep -r "erreur" /etc            # cherche le TEXTE "erreur" DANS les fichiers
```

> **La confusion `find` vs `grep`** est l'une des plus fréquentes. Mémo : `find` cherche **des fichiers** (par leur nom), `grep` cherche **du texte** (dans les fichiers).

## Exercices

**Guidé :** Dans `/etc/passwd`, affiche uniquement la liste des noms d'utilisateurs (1re colonne), triée par ordre alphabétique. Indice : combine `cut` (avec le séparateur `:`) et `sort` à l'aide d'un pipe.

**Autonome :** Toujours dans `/etc/passwd`, compte combien de comptes existent sur le système de deux façons différentes : avec `wc -l`, puis avec `grep -c ""`. Obtiens-tu le même nombre ? *(C'est normal, les deux comptent les lignes.)*

**Défi (orientation sécurité) :** Sur ton journal d'authentification (`/var/log/auth.log`, ou `/var/log/secure`, selon ta distribution), construis une chaîne de commandes qui :
1. extrait les lignes contenant « Failed password » (avec `grep`),
2. isole l'adresse IP source de chaque tentative (avec `awk`, en repérant la bonne colonne),
3. trie ces IP, les dédoublonne et **compte** combien de fois chacune apparaît (avec `sort` et `uniq -c`).

Tu obtiendras la liste des adresses ayant tenté le plus de connexions échouées — exactement le réflexe d'un analyste SOC face à une attaque par force brute. *(Si le fichier n'existe pas, garde la logique de la chaîne en tête : on la réutilisera avec `journalctl` au chapitre 15.)*

## 🧩 Mini-projet (Partie 1) — Ta première enquête

Mets bout à bout tout ce que tu viens d'apprendre dans une petite investigation. Sur ta machine :

1. **Repère-toi** : place-toi dans `/var/log` et liste son contenu trié par date de modification (`ls -lt`). Quels sont les journaux modifiés le plus récemment ?
2. **Lis** : choisis un fichier de log lisible, affiche ses 20 dernières lignes (`tail`), puis suis-le un instant en direct (`tail -f`, puis `Ctrl + C`).
3. **Cherche** : dans ce log, compte combien de lignes contiennent le mot « error » ou « failed » (insensible à la casse, avec `grep -ic`).
4. **Transforme** : si le log contient des lignes structurées, extrais une colonne intéressante (heure, service…) avec `awk` ou `cut`, et identifie la valeur la plus fréquente avec `sort | uniq -c | sort -n`.
5. **Conclus** : en deux phrases, qu'as-tu appris sur l'activité récente de ta machine ?

Ce mini-projet n'utilise **que** des commandes de lecture et de filtrage : tu mènes une vraie enquête sans rien modifier. C'est l'essence du travail défensif.

## ✅ Tu sais maintenant…

- **Filtrer un flux** pour ne garder que l'information utile
- Chercher du texte avec `grep` et ses options clés : `-i`, `-n`, `-v`, `-c`, `-r`
- Trouver des fichiers avec `find` (par nom), et la différence avec `grep`
- Enchaîner des commandes avec le **pipe** `|` (vu ici en pratique ; détaillé au ch. 7)
- Trier et dédoublonner avec `sort` et le duo `sort | uniq -c`
- Extraire une colonne avec `cut`, et transformer du texte avec `tr`, `sed`, `awk` (cas simples)
- Que l'emplacement des **logs d'auth** dépend de la distribution (`auth.log` / `secure` / `journalctl`)
- Mener une **enquête de lecture seule** sur les journaux de ta machine

---

> **🏁 CHECKPOINT 1 — Fin de la Partie 1**
>
> Tu sais désormais **survivre et te repérer** dans un système Linux sans aucun risque : te déplacer, lire, chercher et filtrer de l'information. C'est la fondation de tout le reste.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - expliquer la différence entre un chemin absolu et un chemin relatif ?
> - retrouver un fichier dont tu connais le nom, n'importe où sous `/etc` ?
> - suivre un log en temps réel, puis reprendre la main ?
> - compter combien de fois un mot apparaît dans un fichier ?
> - extraire la première colonne de `/etc/passwd` et la trier ?
>
> Si tu réponds oui à tout, tu es prêt pour la **Partie 2 — Manipuler le système de fichiers**, où l'on passera enfin de la lecture à l'action : créer, copier, déplacer, éditer — avec les bons réflexes de prudence.

---

---
---

# PARTIE 2 — Manipuler le système de fichiers

En Partie 1, on observait sans rien toucher. Maintenant, on passe à l'**action** : créer, copier, déplacer, supprimer, éditer des fichiers, et comprendre comment Linux relie les fichiers entre eux et fait circuler l'information. On garde en permanence les réflexes de prudence vus en Partie 0 : sous Linux, **il n'y a pas de corbeille**, et une commande mal placée agit immédiatement.

---

# Chapitre 5 — Créer, copier, déplacer, supprimer

## Le minimum à savoir

### Créer un fichier vide : `touch`

`touch` crée un fichier vide s'il n'existe pas (et met à jour sa date s'il existe déjà) :

```bash
touch rapport.txt        # crée un fichier vide nommé rapport.txt
touch fichier1 fichier2  # on peut en créer plusieurs d'un coup
```

C'est la façon la plus rapide de « poser » un fichier avant de le remplir.

### Créer un dossier : `mkdir`

`mkdir` (*make directory*) crée un dossier :

```bash
mkdir projet             # crée un dossier "projet"
```

Et si tu veux créer toute une arborescence d'un coup, l'option `-p` crée les dossiers parents manquants :

```bash
mkdir -p projet/logs/2025    # crée projet, puis logs, puis 2025
```

Sans `-p`, la commande échouerait si `projet` ou `logs` n'existaient pas encore. **Le `-p` est le réflexe pour créer un chemin complet.**

### Copier : `cp`

`cp` (*copy*) copie un fichier vers une destination. L'original reste en place :

```bash
cp rapport.txt sauvegarde.txt      # copie le fichier sous un nouveau nom
cp rapport.txt /tmp/               # copie le fichier dans le dossier /tmp
```

Pour copier un **dossier** (avec tout son contenu), il faut l'option `-r` (*recursive*) :

```bash
cp -r projet/ projet-copie/        # copie le dossier et tout ce qu'il contient
```

> **Réflexe à retenir :** sans `-r`, on ne peut pas copier un dossier. C'est aussi le `-r` qu'on retrouvera pour la suppression et les permissions : **`-r` = « et tout ce qu'il y a dedans »**.

### Déplacer et renommer : `mv`

`mv` (*move*) sert à **deux** choses qui sont en réalité la même : déplacer, et renommer.

```bash
mv rapport.txt /tmp/               # DÉPLACE le fichier dans /tmp
mv rapport.txt bilan.txt           # RENOMME le fichier (le "déplace" vers un nouveau nom)
```

Renommer, pour Linux, c'est juste déplacer un fichier vers un nouveau nom au même endroit. Pas besoin de commande séparée.

### Supprimer : `rm` (la commande à respecter)

`rm` (*remove*) supprime un fichier. **Définitivement. Sans corbeille. Sans confirmation.**

```bash
rm rapport.txt           # supprime le fichier (aucun retour possible)
```

Pour supprimer un **dossier** et son contenu, il faut `-r` :

```bash
rm -r projet/            # supprime le dossier et TOUT ce qu'il contient
```

Pour supprimer un dossier **vide** uniquement (plus sûr), il existe `rmdir` :

```bash
rmdir dossier-vide/      # échoue si le dossier n'est PAS vide (c'est une sécurité)
```

## Très utile en pratique

### Le filet de sécurité : `rm -i`

L'option `-i` (*interactive*) demande **confirmation** avant chaque suppression :

```bash
rm -i rapport.txt
# rm: supprimer fichier 'rapport.txt' ? (o/n)
```

C'est un excellent réflexe quand tu débutes, ou avant une suppression importante. Tu reprends la main sur une opération irréversible.

### Appliquer les règles d'or

Souviens-toi de la Partie 0. Avant toute suppression, le bon réflexe est :

```bash
pwd                      # 1. où suis-je vraiment ?
ls                       # 2. qu'est-ce qu'il y a ici, exactement ?
rm -i fichier-a-virer    # 3. je supprime, avec confirmation
```

Ces trois secondes de vérification t'éviteront un jour une vraie catastrophe.

### ⚠️ `rm -rf` : la commande qui ne pardonne pas

Tu croiseras partout la combinaison `rm -rf` :

- `-r` → récursif (dossiers et contenu)
- `-f` → *force* : ne demande rien, ignore les erreurs, supprime tout

```bash
rm -rf vieux-projet/     # supprime tout, sans aucune question
```

Cette commande est puissante et **utilisée tous les jours** par les administrateurs. Mais une faute de frappe peut être dévastatrice :

```bash
rm -rf / chemin          # ❌❌❌ CATASTROPHE : l'espace après / détruit la racine
rm -rf /chemin           # ce qui était voulu (un seul argument)
```

> **La règle absolue avec `rm -rf` :** relis la ligne **avant** d'appuyer sur Entrée. Cherche les espaces parasites. Vérifie que le chemin commence bien là où tu crois. En cas de doute, remplace temporairement `rm` par `ls` pour voir *ce qui serait supprimé* — si `ls` affiche les bons fichiers, alors `rm` visera les bons fichiers.

## ❌ Erreur classique

```bash
# Copier un dossier sans -r
cp projet/ copie/        # ❌ "omitting directory" — refusé
cp -r projet/ copie/     # ✅

# Écraser un fichier sans s'en rendre compte
cp a.txt b.txt           # ❌ si b.txt existait, son contenu est PERDU
cp -i a.txt b.txt        # ✅ -i demande confirmation avant d'écraser

# Croire que rm met à la corbeille
rm important.txt         # ❌ DÉFINITIF, pas de récupération simple

# Oublier que mv écrase la destination silencieusement
mv a.txt b.txt           # si b.txt existait, il est remplacé sans prévenir
mv -i a.txt b.txt        # ✅ -i pour être prévenu

# Mauvais espace dans rm -rf
rm -rf ./ *              # ❌ le "./ *" sépare en deux : danger
rm -rf ./vieux-dossier   # ✅ un seul chemin, sans espace parasite
```

## Exercices

**Guidé :** Crée d'un seul `mkdir -p` l'arborescence `atelier/scripts/sauvegardes`. Place-toi dedans, crée trois fichiers vides avec `touch` (`a.sh`, `b.sh`, `c.sh`), puis vérifie le tout avec `ls -R atelier` (le `-R` liste récursivement).

**Autonome :** Dans le dossier `atelier`, copie `scripts/a.sh` vers `scripts/a.sh.bak` (une sauvegarde). Renomme ensuite `b.sh` en `principal.sh`. Vérifie le résultat avec `ls`. Combien de fichiers y a-t-il maintenant dans `scripts` ?

**Défi :** Crée un dossier `lab-test` avec quelques fichiers à l'intérieur. Avant de le supprimer, entraîne-toi au réflexe de sécurité : fais `ls lab-test/` pour voir ce qu'il contient, puis supprime-le entièrement avec `rm -r`. Recommence en utilisant `rm -ri` pour voir la différence (confirmation à chaque élément). Lequel te semble plus prudent quand l'enjeu est important ?

## ✅ Tu sais maintenant…

- Créer des fichiers (`touch`) et des dossiers (`mkdir`, et `mkdir -p` pour une arborescence)
- Copier avec `cp` (et `-r` pour les dossiers, `-i` pour éviter d'écraser)
- Déplacer **et** renommer avec `mv` (c'est la même opération)
- Supprimer avec `rm` — **définitivement** — et la sécurité `rmdir` pour les dossiers vides
- Te protéger avec `rm -i`, et appliquer le réflexe `pwd` → `ls` → suppression
- Pourquoi `rm -rf` est puissant **et** dangereux, et comment le manipuler sans accident

---

# Chapitre 6 — Éditer des fichiers dans le terminal

## Le minimum à savoir

### Pourquoi éditer sans interface graphique ?

Quand tu administres un serveur, tu n'as **pas de souris ni de fenêtres** : tu es connecté en ligne de commande (on verra le SSH en Partie 5). Pour modifier un fichier de configuration, il te faut donc un éditeur qui fonctionne **dans le terminal**. C'est une compétence incontournable : la quasi-totalité du réglage d'un système Linux passe par l'édition de fichiers texte dans `/etc`.

### `nano` : l'éditeur pour débuter

`nano` est simple, lisible, et c'est celui qu'on recommande pour commencer :

```bash
nano notes.txt           # ouvre (ou crée) le fichier dans l'éditeur
```

Une fois dans `nano`, tu tapes ton texte normalement. En bas de l'écran, une **barre d'aide** rappelle les raccourcis. Le symbole `^` y signifie la touche **`Ctrl`**. Les deux à connaître absolument :

- **`Ctrl + O`** → *enregistrer* (puis Entrée pour confirmer le nom)
- **`Ctrl + X`** → *quitter*

> **Le minimum vital dans nano :** écrire, puis `Ctrl + O` pour sauvegarder, puis `Ctrl + X` pour sortir. Avec juste ça, tu peux déjà modifier n'importe quelle configuration.

### `vim` : survivre, au minimum

`vim` (et son ancêtre `vi`) est extrêmement puissant, mais **déroutant** au premier contact. Tu finiras peut-être par l'adorer, mais pour l'instant l'objectif est simple : **savoir en sortir sans paniquer**, car tu tomberas dessus par surprise un jour (certains systèmes l'ouvrent par défaut).

La clé : `vim` a des **modes**. Au démarrage, tu es en mode « commande » (taper du texte ne marche pas comme prévu). Le strict minimum :

- Appuie sur **`i`** → passe en mode *insertion* (là, tu peux taper du texte)
- Appuie sur **`Échap`** → reviens en mode commande
- Tape **`:wq`** puis Entrée → *write & quit* (enregistrer et quitter)
- Tape **`:q!`** puis Entrée → quitter **sans** enregistrer (la sortie de secours)

> **Si tu es coincé dans vim** et que tu veux juste partir sans rien casser : appuie sur `Échap`, puis tape `:q!` et Entrée. Retiens ce `:q!` — c'est ta porte de sortie garantie.

### Écrire sans éditeur : `echo` et les redirections

Pour des modifications très rapides, on peut écrire dans un fichier directement depuis la ligne de commande :

```bash
echo "première ligne" > notes.txt     # > ÉCRASE le fichier avec ce texte
echo "ligne ajoutée" >> notes.txt     # >> AJOUTE à la fin sans rien effacer
```

> **Distinction capitale** (qu'on approfondira au chapitre 7) : `>` **écrase** tout le contenu existant, `>>` **ajoute** à la fin. Confondre les deux sur un fichier important est une erreur classique aux conséquences sérieuses.

## Très utile en pratique

### Le réflexe sauvegarde-avant-modification

C'est la **troisième règle d'or** de la Partie 0, et c'est ici qu'elle prend tout son sens. **Avant de modifier un fichier de configuration, on en fait toujours une copie de sauvegarde.** Si la modification casse quelque chose, on restaure la copie et tout repart.

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. copie de sécurité (.bak)
sudo nano /etc/ssh/sshd_config                           # 2. on modifie
```

L'extension `.bak` est une convention (pour « backup ») : elle n'a rien de magique, mais elle signale clairement « ceci est une sauvegarde ». Si la modification tourne mal :

```bash
sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config    # on restaure, et on est sauvé
```

### `sudoedit` : la bonne façon d'éditer un fichier système

Pour modifier un fichier qui appartient au système (dans `/etc`, par exemple), il faut des droits d'administrateur. On pourrait écrire `sudo nano fichier`, mais il existe **mieux** : `sudoedit`.

```bash
sudoedit /etc/ssh/sshd_config       # (équivalent : sudo -e ...)
```

`sudoedit` t'ouvre le fichier dans une **copie temporaire** avec **ton** éditeur habituel et **tes** réglages, puis réécrit le fichier original à ta place une fois que tu as fini. C'est plus propre et plus sûr que `sudo nano` : ton éditeur ne tourne pas avec les pleins pouvoirs, ce qui limite les dégâts en cas de mauvaise manipulation.

> **Bonne pratique professionnelle :** pour éditer un fichier système, préfère `sudoedit fichier` plutôt que `sudo nano fichier`. *(Pour choisir quel éditeur `sudoedit` lance, on règle la variable d'environnement `EDITOR` — un sujet du chapitre 8.)*

### Comparer deux versions : `diff`

Après une modification, comment savoir **exactement** ce qui a changé ? `diff` compare deux fichiers et n'affiche que les **différences** :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

Le workflow complet, propre et professionnel, devient donc :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérification du changement
```

> **Très utile en sécurité :** garder un `.bak` et un `diff` permet de **prouver** ce qui a été modifié dans une configuration, et de revenir à l'état initial en cas de problème. C'est une trace précieuse lors d'un incident.

## ❌ Erreur classique

```bash
# Confondre > et >> et écraser un fichier
echo "nouvelle conf" > /etc/important.conf    # ❌ tout l'ancien contenu est PERDU
echo "ligne en plus" >> /etc/important.conf   # ✅ ajoute sans détruire

# Modifier une config système SANS sauvegarde
sudo nano /etc/ssh/sshd_config                # ❌ et si ça casse ?
sudo cp .../sshd_config .../sshd_config.bak   # ✅ toujours un .bak d'abord

# Rester bloqué dans vim et fermer brutalement le terminal
# ✅ Échap puis :q! suffit pour sortir proprement

# Croire que sudo nano = sudoedit
sudo nano /etc/fichier        # fonctionne, mais l'éditeur tourne en root
sudoedit /etc/fichier         # ✅ plus sûr : édition dans une copie temporaire

# Éditer un fichier système sans les droits
nano /etc/hosts               # ❌ "Permission denied" ou impossible d'enregistrer
sudoedit /etc/hosts           # ✅
```

## Exercices

**Guidé :** Avec `nano`, crée un fichier `~/notes-cours.txt`, écris-y trois lignes décrivant ce que tu as appris jusqu'ici, enregistre avec `Ctrl + O` et quitte avec `Ctrl + X`. Vérifie le contenu avec `cat ~/notes-cours.txt`.

**Autonome :** Crée un fichier `config-test.txt` avec quelques lignes. Fais-en une copie `.bak`. Modifie ensuite l'original (change une ligne, ajoutes-en une) avec l'éditeur de ton choix. Enfin, lance `diff config-test.txt.bak config-test.txt` et lis attentivement ce que `diff` te montre : reconnais-tu tes modifications ?

**Défi :** Ouvre volontairement un fichier avec `vim` (`vim test-vim.txt`). Passe en mode insertion avec `i`, écris une phrase, reviens en mode commande avec `Échap`, puis quitte **sans enregistrer** avec `:q!`. Recommence, mais cette fois enregistre avec `:wq`. Vérifie avec `cat` quel essai a bien été sauvegardé.

## ✅ Tu sais maintenant…

- Pourquoi l'édition en terminal est indispensable en administration
- Éditer simplement avec `nano` (sauver `Ctrl + O`, quitter `Ctrl + X`)
- **Survivre dans `vim`** : `i` pour écrire, `Échap`, puis `:wq` (enregistrer) ou `:q!` (sortie de secours)
- Écrire vite avec `echo >` (écrase) et `echo >>` (ajoute)
- Le **réflexe `.bak`** avant toute modification de configuration
- Éditer proprement un fichier système avec `sudoedit` (mieux que `sudo nano`)
- Vérifier précisément un changement avec `diff`

---

# Chapitre 7 — Liens, redirections et tuyaux

## Le minimum à savoir

### Les trois flux : entrée, sortie, erreur

Au chapitre 4, on a utilisé le pipe `|` « pour de vrai » sans tout expliquer. Le moment est venu de comprendre **comment l'information circule** sous Linux. Chaque commande dispose de trois canaux :

- **L'entrée standard (stdin)** : ce que la commande reçoit (par défaut, ton clavier).
- **La sortie standard (stdout)** : ce que la commande produit normalement (par défaut, l'écran).
- **La sortie d'erreur (stderr)** : là où la commande envoie ses messages d'erreur (par défaut, l'écran aussi).

```
                  ┌─────────────┐
   stdin   ─────► │   COMMANDE  │ ─────►  stdout (résultat normal)
  (clavier)       │             │ ─────►  stderr (messages d'erreur)
                  └─────────────┘
```

Le point essentiel : **sortie normale et sortie d'erreur sont deux canaux séparés**, même s'ils s'affichent tous les deux à l'écran par défaut. Pouvoir les rediriger indépendamment est ce qui rend Linux si puissant pour l'automatisation.

### Rediriger la sortie vers un fichier : `>` et `>>`

On l'a effleuré au chapitre 6, voici l'explication propre :

```bash
ls > liste.txt           # > : envoie la sortie dans le fichier (ÉCRASE l'ancien contenu)
ls >> liste.txt          # >> : AJOUTE la sortie à la fin du fichier
```

`>` redirige **stdout** vers un fichier au lieu de l'écran. C'est ainsi qu'on **enregistre** le résultat d'une commande.

> **Le piège classique, redit une fois de plus parce qu'il fait des dégâts :** `>` **écrase** sans prévenir. `commande > fichier-important` détruit le contenu du fichier. En cas de doute, utilise `>>` (ajout) ou redirige d'abord vers un fichier de test.

### Rediriger les erreurs : `2>` et `&>`

Les erreurs voyagent sur le canal `stderr`, identifié par le numéro **`2`** :

```bash
commande 2> erreurs.txt      # envoie UNIQUEMENT les erreurs dans erreurs.txt
commande > sortie.txt 2>&1   # envoie sortie ET erreurs dans le même fichier
commande &> tout.txt         # raccourci moderne : sortie + erreurs dans tout.txt
```

Un usage très courant : **se débarrasser des erreurs** qu'on ne veut pas voir, en les envoyant vers `/dev/null` (une sorte de « trou noir » du système qui jette tout ce qu'on lui donne) :

```bash
find / -name "*.conf" 2>/dev/null    # ne montre que les résultats, pas les "Permission denied"
```

> Tu reconnais ce `2>/dev/null` ? C'est exactement ce qu'on utilisera en Partie 3 pour les recherches de fichiers SUID : on cache les nombreux messages d'erreur pour ne garder que les vrais résultats.

## Très utile en pratique

### Le pipe `|` : maintenant tu comprends pourquoi ça marche

Le pipe relie la **sortie standard** d'une commande à l'**entrée standard** de la suivante. Ce que tu utilisais au chapitre 4 comme un simple « tuyau » est en fait une redirection de stdout vers stdin :

```bash
cat auth.log | grep "Failed" | wc -l
#   stdout ──► stdin   stdout ──► stdin
```

Chaque `|` branche la sortie de gauche sur l'entrée de droite. C'est le mécanisme qui incarne la philosophie « petits outils combinés ».

### Voir ET enregistrer en même temps : `tee`

Parfois tu veux à la fois **voir** un résultat à l'écran **et** le **garder** dans un fichier. La commande `tee` fait les deux (comme un « T » de plomberie qui sépare un flux en deux) :

```bash
ls -l /etc | tee inventaire.txt          # affiche le résultat ET l'écrit dans inventaire.txt
ls -l /etc | tee -a inventaire.txt       # -a : ajoute au fichier au lieu de l'écraser
```

> **Très utile en pratique :** lors d'une analyse, `commande | tee rapport.txt` te permet de suivre le résultat en direct tout en conservant une trace écrite pour plus tard. Indispensable pour documenter une investigation.

### Appliquer une commande à chaque résultat : `xargs`

`xargs` prend une liste arrivant par un pipe et la transforme en **arguments** pour une autre commande. C'est le pont entre « une liste de noms » et « une action sur chacun » :

```bash
find . -name "*.tmp" | xargs rm          # supprime tous les .tmp trouvés
```

Ici : `find` produit une liste de fichiers → `xargs` la passe à `rm` qui les supprime. C'est puissant… donc à manier avec la prudence habituelle (teste d'abord en remplaçant `rm` par `echo` pour voir ce qui serait fait).

### Les liens symboliques : `ln -s`

Un **lien symbolique** est un « raccourci » : un petit fichier qui pointe vers un autre fichier ou dossier, parfois situé ailleurs. On le crée avec `ln -s` (*link, symbolic*) :

```bash
ln -s /var/log/syslog ~/mon-log         # crée un raccourci "mon-log" vers le vrai fichier
```

Désormais, `~/mon-log` mène au vrai `/var/log/syslog`. Si tu supprimes le lien, le fichier d'origine reste intact (tu n'effaces que le raccourci). Tu reconnaîtras un lien dans un `ls -l` à la flèche `->` qui indique sa cible.

> Il existe aussi des liens « durs » (sans `-s`), plus techniques. Pour débuter, retiens surtout le **lien symbolique** : c'est de loin le plus courant et le plus utile.

## ❌ Erreur classique

```bash
# Écraser un fichier important avec >
cat resultats.txt > resultats.txt    # ❌ peut vider le fichier ! ne redirige pas vers la source
sort resultats.txt > tries.txt       # ✅ vers un AUTRE fichier

# Oublier que les erreurs ne passent pas par le pipe normalement
commande_qui_echoue | grep "ok"      # les erreurs s'affichent quand même (elles sont sur stderr)
commande_qui_echoue 2>&1 | grep "ok" # ✅ pour filtrer aussi les erreurs

# Confondre tee et >
ls | > fichier.txt               # ❌ syntaxe cassée
ls | tee fichier.txt             # ✅ voir + enregistrer
ls > fichier.txt                 # ✅ enregistrer seulement

# Utiliser xargs avec rm sans vérifier
find . -name "*" | xargs rm      # ❌ DANGER : teste d'abord avec echo
find . -name "*.tmp" | xargs echo  # ✅ visualise ce qui serait supprimé

# Supprimer la cible en croyant supprimer le lien
rm ~/mon-log/                    # attention à ce qu'on supprime exactement
```

## Exercices

**Guidé :** Liste le contenu de `/etc` et enregistre-le dans un fichier `etc-liste.txt` avec `>`. Vérifie avec `cat etc-liste.txt`. Relance la même commande mais avec `>>` et observe que le fichier double de taille (l'ajout). Puis recommence avec `>` : le fichier est réécrit de zéro.

**Autonome :** Lance `find /etc -name "*.conf"` deux fois : une fois sans rien, une fois avec `2>/dev/null`. Compare la quantité de messages d'erreur. Ensuite, utilise `tee` pour à la fois afficher la liste des `.conf` et l'enregistrer dans `confs.txt`.

**Défi :** Crée un lien symbolique vers ton journal système quelque part dans ton dossier personnel (`ln -s`). Vérifie avec `ls -l` que la flèche `->` pointe vers la bonne cible. Lis le log à travers ton lien (`tail mon-lien`). Puis supprime **le lien** et confirme avec `ls` que le fichier d'origine, lui, existe toujours.

## ✅ Tu sais maintenant…

- Les **trois flux** : entrée (stdin), sortie (stdout), erreur (stderr) — et que sortie et erreur sont **séparées**
- Rediriger la sortie avec `>` (écrase) et `>>` (ajoute)
- Rediriger les erreurs avec `2>`, les fusionner avec `2>&1` ou `&>`, et les jeter avec `2>/dev/null`
- **Pourquoi** le pipe `|` fonctionne : il relie stdout à stdin
- Voir **et** enregistrer en même temps avec `tee`
- Appliquer une action à chaque résultat avec `xargs` (en testant d'abord avec `echo`)
- Créer un raccourci avec un **lien symbolique** (`ln -s`) et le reconnaître au `->`

---

# Chapitre 8 — Variables d'environnement et configuration du shell

## Le minimum à savoir

### Pourquoi certaines commandes marchent « partout »

Tu as remarqué que tu peux taper `ls` depuis **n'importe quel** dossier et que ça fonctionne ? Pourtant, `ls` est un programme rangé quelque part (dans `/bin` ou `/usr/bin`). Comment le shell le retrouve-t-il sans que tu donnes son chemin complet ? La réponse tient en un mot : **les variables d'environnement**. Comprendre ce mécanisme, c'est lever l'un des derniers mystères du terminal.

### Qu'est-ce qu'une variable d'environnement ?

Une **variable** est un nom qui stocke une valeur. Une variable d'**environnement** est une variable que le shell (et les programmes qu'il lance) peuvent consulter pour savoir « comment se comporter ». Pour lire la valeur d'une variable, on met un `$` devant son nom :

```bash
echo $HOME       # → /home/alice (ton dossier personnel)
echo $USER       # → alice       (ton nom d'utilisateur)
echo $SHELL      # → /bin/bash    (ton shell)
echo $PWD        # → le dossier courant (mis à jour à chaque cd)
```

Pour voir **toutes** les variables d'environnement d'un coup :

```bash
env              # liste toutes les variables d'environnement
printenv         # équivalent (printenv USER affiche juste celle-là)
```

| Variable | Ce qu'elle contient |
|----------|---------------------|
| `HOME` | Le chemin de ton dossier personnel |
| `USER` | Ton nom d'utilisateur |
| `SHELL` | Le shell que tu utilises |
| `PWD` | Le dossier de travail actuel |
| `PATH` | La liste des dossiers où le shell cherche les programmes *(voir ci-dessous)* |

### Le `PATH` : la clé du mystère

`PATH` est **la** variable à comprendre. Elle contient une liste de dossiers, séparés par des `:`, dans lesquels le shell va **chercher** les programmes que tu tapes :

```bash
echo $PATH
# → /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin
```

Quand tu tapes `ls`, le shell parcourt ces dossiers **dans l'ordre** jusqu'à trouver un programme nommé `ls`. C'est pour ça que `ls` marche partout : son dossier (`/bin`) est dans le `PATH`. Et c'est aussi pourquoi une commande que tu viens d'écrire toi-même ne marche **pas** directement : son dossier n'est pas dans le `PATH`.

### Où est ce programme ? `which` et `command -v`

Pour savoir **quel** fichier sera exécuté quand tu tapes une commande :

```bash
which ls             # → /usr/bin/ls (le chemin du programme trouvé via le PATH)
command -v ls        # → même résultat, forme plus moderne et portable
```

`command -v` fonctionne aussi avec les commandes internes au shell et les alias, là où `which` peut être limité. **Pour débuter, `which` suffit** ; garde `command -v` en tête comme la version « propre ».

## Très utile en pratique

### Créer une variable : `export`

Tu peux définir tes propres variables. Sans `export`, la variable n'existe que dans le shell courant ; **avec `export`**, elle devient une variable d'environnement, transmise aux programmes que tu lances :

```bash
MAVAR="bonjour"          # variable locale au shell
export MAVAR="bonjour"   # variable d'environnement (héritée par les programmes lancés)
echo $MAVAR              # → bonjour
```

Un exemple concret et utile : choisir l'éditeur que `sudoedit` (chapitre 6) va lancer :

```bash
export EDITOR=nano       # désormais sudoedit ouvrira nano
```

### Ajouter un dossier au `PATH`

Imaginons que tu ranges tes propres scripts dans un dossier `~/bin`. Pour pouvoir les lancer **par leur nom** depuis partout, il faut ajouter ce dossier au `PATH` :

```bash
mkdir -p ~/bin                       # crée le dossier pour tes scripts
export PATH="$HOME/bin:$PATH"        # ajoute ~/bin EN TÊTE du PATH
```

Décortiquons `"$HOME/bin:$PATH"` : on met ton nouveau dossier, un `:`, puis **l'ancien `PATH` en entier**. C'est crucial : on **ajoute** à la liste existante, on ne la remplace pas. Oublier `:$PATH` à la fin ferait disparaître l'accès à toutes les commandes habituelles le temps de la session.

### Les alias : des raccourcis personnels

Un **alias** est un surnom que tu donnes à une commande, souvent pour ajouter des options par défaut ou raccourcir une commande longue :

```bash
alias ll='ls -lah'           # désormais "ll" = "ls -lah"
alias ..='cd ..'             # remonter d'un dossier en tapant juste ..
alias                        # (seul) affiche tous tes alias actuels
```

> **Très utile en pratique :** les administrateurs créent souvent un alias `alias rm='rm -i'` pour que `rm` demande **toujours** confirmation. Un petit filet de sécurité permanent, dans l'esprit des règles d'or de la Partie 0.

### Rendre tout cela permanent : `.bashrc` et `source`

Voici le point essentiel : **tout ce qu'on vient de faire (variables, PATH, alias) disparaît quand tu fermes le terminal.** Chaque nouveau terminal repart à zéro. Pour rendre tes réglages **permanents**, on les écrit dans un fichier que le shell lit **automatiquement à chaque démarrage** : `~/.bashrc`.

C'est un fichier caché (il commence par un `.`, souviens-toi de `ls -a`) dans ton dossier personnel. On l'édite comme n'importe quel fichier — avec le réflexe `.bak` du chapitre 6 :

```bash
cp ~/.bashrc ~/.bashrc.bak           # 1. sauvegarde, toujours
nano ~/.bashrc                       # 2. on ajoute nos lignes à la fin :
                                     #    export PATH="$HOME/bin:$PATH"
                                     #    alias ll='ls -lah'
                                     #    alias rm='rm -i'
```

Mais attention : modifier `.bashrc` ne change **rien** dans le terminal déjà ouvert, puisqu'il n'est lu qu'au démarrage. Pour appliquer tes changements **immédiatement**, sans rouvrir de terminal, on utilise `source` :

```bash
source ~/.bashrc         # relit le fichier et applique les changements ici et maintenant
```

> **Le concept à retenir :** `.bashrc` est lu **automatiquement** au lancement de chaque shell. `source ~/.bashrc` le relit **manuellement** dans le terminal courant. On écrit ses réglages une fois dans `.bashrc`, puis on `source` pour les tester sans redémarrer.

### Le mystère du `./script.sh` enfin résolu

Tu te demandais peut-être pourquoi, pour lancer un script à toi, on écrit `./script.sh` et pas juste `script.sh` ? Maintenant tu as la réponse : le dossier courant (`.`) **n'est pas dans le `PATH`** (pour des raisons de sécurité). Le shell ne cherche donc pas tes programmes ici. En écrivant `./script.sh`, tu donnes explicitement le chemin (« le script `script.sh`, **ici** ») au lieu de compter sur le `PATH`. Et si tu ranges tes scripts dans `~/bin` ajouté au `PATH`, tu pourras les lancer par leur nom, de partout — comme une vraie commande.

## ❌ Erreur classique

```bash
# Oublier le $ pour LIRE une variable
echo PATH         # ❌ affiche littéralement le mot "PATH"
echo $PATH        # ✅ affiche le contenu de la variable

# Mettre un $ pour DÉFINIR une variable
$MAVAR="x"        # ❌ erreur de syntaxe
MAVAR="x"         # ✅ pas de $ à la définition, seulement à la lecture

# Mettre des espaces autour du =
MAVAR = "x"       # ❌ le shell croit à une commande "MAVAR"
MAVAR="x"         # ✅ pas d'espaces autour du =

# ÉCRASER le PATH au lieu d'y ajouter
export PATH="$HOME/bin"          # ❌❌ catastrophe : plus aucune commande ne marche
export PATH="$HOME/bin:$PATH"    # ✅ on ajoute, on garde l'ancien

# Modifier .bashrc et s'étonner que rien ne change
nano ~/.bashrc                   # modification faite...
# ❌ ...mais pas appliquée dans ce terminal
source ~/.bashrc                 # ✅ relit et applique maintenant
```

> **Si tu casses ton `PATH`** pendant une session (plus aucune commande ne répond), pas de panique : ferme et rouvre le terminal. Comme `.bashrc` n'avait pas été modifié, tu repars sur un `PATH` sain. C'est exactement pour ça qu'on garde un `.bashrc.bak`.

## Exercices

**Guidé :** Affiche le contenu de tes variables `HOME`, `USER` et `PATH` avec `echo`. Puis utilise `which` pour trouver où se trouvent les programmes `ls`, `cat` et `grep`. Sont-ils tous dans des dossiers présents dans ton `PATH` ?

**Autonome :** Crée un dossier `~/bin`. Ajoute-le à ton `PATH` avec `export` (en n'oubliant pas `:$PATH`). Vérifie avec `echo $PATH` qu'il apparaît bien. Crée ensuite un alias temporaire `alias jrnl='tail -f /var/log/syslog'` et teste-le. *(Cet alias disparaîtra à la fermeture du terminal — c'est voulu.)*

**Défi :** Rends tes réglages permanents proprement. Fais d'abord une copie `.bak` de ton `~/.bashrc`. Ajoute-y l'export de `~/bin` dans le `PATH` et un alias `ll='ls -lah'`. Applique avec `source ~/.bashrc`, puis teste `ll`. Ouvre enfin un **nouveau** terminal et vérifie que `ll` fonctionne toujours, prouvant que le réglage est bien devenu permanent.

## 🧩 Mini-projet (Partie 2) — Atelier de configuration

Mets en œuvre toute la Partie 2 dans un atelier réaliste, **sur des fichiers de test uniquement** (pas de vrai fichier système) :

1. **Construis** une arborescence de travail avec `mkdir -p` : `atelier/{scripts,configs,sauvegardes}`.
2. **Crée** dans `configs/` un fichier `app.conf` avec quelques lignes de réglages (via `nano` ou `echo >>`).
3. **Sauvegarde** : avant toute modification, copie `app.conf` en `app.conf.bak` (le réflexe).
4. **Modifie** `app.conf` (change une valeur), puis prouve le changement avec `diff app.conf.bak app.conf`.
5. **Journalise** : avec un pipe et `tee`, enregistre la liste de tes fichiers dans `atelier/inventaire.txt` tout en l'affichant.
6. **Personnalise** : ajoute dans ton `.bashrc` (après un `.bak` !) un alias `atelier='cd ~/atelier && ls -lah'`, applique avec `source`, et teste-le.
7. **Range** : déplace tes scripts dans le dossier prévu avec `mv`, et fais le ménage des fichiers de test inutiles avec `rm -i`.

À la fin, tu auras mobilisé création, copie, déplacement, suppression prudente, édition sécurisée, redirections et configuration du shell — tout le cœur de la Partie 2.

## ✅ Tu sais maintenant…

- Ce qu'est une **variable d'environnement** et comment la lire (`$NOM`, `env`, `printenv`)
- Le rôle des variables clés : `HOME`, `USER`, `SHELL`, `PWD`
- **Pourquoi** les commandes marchent partout grâce au `PATH`, et comment l'inspecter
- Localiser un programme avec `which` et `command -v`
- Créer des variables avec `export`, et **ajouter** un dossier au `PATH` sans l'écraser
- Créer des raccourcis avec `alias` (dont le filet de sécurité `rm -i`)
- Rendre tes réglages **permanents** dans `.bashrc` et les appliquer avec `source`
- **Pourquoi** on tape `./script.sh` (le `.` n'est pas dans le `PATH`)

---

> **🏁 CHECKPOINT 2 — Fin de la Partie 2**
>
> Tu es passé de l'observation à l'**action** : tu sais créer, organiser, éditer et supprimer des fichiers en toute prudence, faire circuler l'information entre les commandes, et façonner ton propre environnement de travail.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - créer une arborescence complète en une commande, puis la supprimer prudemment ?
> - modifier un fichier de configuration en gardant une sauvegarde et en vérifiant le changement avec `diff` ?
> - sortir de `vim` sans paniquer ?
> - expliquer la différence entre `>`, `>>` et `|` ?
> - dire pourquoi `ls` marche partout, et ajouter ton propre dossier au `PATH` de façon permanente ?
>
> Si oui, tu maîtrises les fondations pratiques de Linux. Place à la **Partie 3 — Qui a le droit de quoi**, le cœur conceptuel de l'administration et de la sécurité : permissions, utilisateurs, groupes et `sudo`.

---

---
---

# PARTIE 3 — Qui a le droit de quoi

Voici le cœur de l'administration Linux et de la sécurité. Jusqu'ici, tu manipulais des fichiers ; maintenant, tu vas comprendre **qui** a le droit de faire **quoi**, et **pourquoi**. C'est le modèle qui protège un système : il décide qui peut lire un mot de passe, modifier une configuration, ou lancer un programme privilégié. Maîtriser cette partie, c'est comprendre à la fois comment administrer proprement **et** comment un système se fait attaquer. C'est la partie la plus importante du cours pour l'orientation cybersécurité.

---

# Chapitre 9 — Comprendre les permissions

## Le minimum à savoir

### L'idée : trois questions, trois réponses

Sous Linux, chaque fichier répond à trois questions :

1. **Qui possède ce fichier ?** → son **propriétaire** (*user*)
2. **Quel groupe y a accès ?** → son **groupe** (*group*)
3. **Et tous les autres ?** → les **autres** (*others*)

Pour chacune de ces trois catégories, le système définit ce qui est permis : **lire**, **écrire**, **exécuter**. C'est tout. Ce modèle simple (trois catégories × trois droits) gouverne l'accès à l'ensemble du système.

### Lire un `ls -l` : décrypter la première colonne

Tu as déjà vu `ls -l` au chapitre 2. Reprends-le maintenant avec un œil neuf :

```bash
ls -l rapport.txt
# -rw-r--r-- 1 alice equipe 1240 Jan 10 14:30 rapport.txt
```

Concentrons-nous sur le premier bloc, `-rw-r--r--`. Il se découpe ainsi :

```
  -        rw-       r--       r--
  │         │         │         │
type    propriétaire groupe   autres
```

- **1er caractère** : le **type**. `-` = fichier ordinaire, `d` = dossier (*directory*), `l` = lien symbolique.
- **Caractères 2 à 4** (`rw-`) : les droits du **propriétaire**.
- **Caractères 5 à 7** (`r--`) : les droits du **groupe**.
- **Caractères 8 à 10** (`r--`) : les droits des **autres**.

### Les trois droits : r, w, x

Chaque triplet se lit toujours dans le même ordre : `r`, `w`, `x`. Un tiret `-` signifie « ce droit est absent ».

| Lettre | Sur un fichier | Sur un dossier |
|--------|----------------|----------------|
| `r` (read) | lire le contenu | lister les fichiers qu'il contient |
| `w` (write) | modifier le contenu | créer/supprimer des fichiers dedans |
| `x` (execute) | exécuter le fichier (programme/script) | **entrer** dans le dossier (`cd`) |

> **Le piège des dossiers :** sur un **dossier**, `x` ne veut pas dire « exécuter » mais « traverser » (pouvoir faire `cd` dedans et accéder à son contenu). Un dossier sans `x` est inaccessible même si tu as `r`. Retiens : pour entrer dans un dossier, il faut le `x`.

Reprenons `-rw-r--r--` : c'est un fichier ordinaire, le propriétaire peut lire et écrire (`rw-`), le groupe peut seulement lire (`r--`), les autres aussi (`r--`). Personne ne peut l'exécuter. C'est typique d'un fichier de données.

## Très utile en pratique

### Modifier les permissions : `chmod` en notation symbolique

`chmod` (*change mode*) modifie les droits. La façon la plus lisible utilise des lettres :

- **Qui** : `u` (user/propriétaire), `g` (group), `o` (others), `a` (all/tous)
- **Action** : `+` (ajouter), `-` (retirer), `=` (fixer exactement)
- **Droit** : `r`, `w`, `x`

```bash
chmod u+x script.sh      # ajoute le droit d'exécution AU PROPRIÉTAIRE
chmod go-w fichier       # retire l'écriture au groupe ET aux autres
chmod a+r fichier        # donne la lecture à tout le monde
```

Le cas le plus fréquent de tout le cours : **rendre un script exécutable**.

```bash
chmod u+x mon-script.sh      # maintenant on peut le lancer avec ./mon-script.sh
```

> Ça boucle avec le chapitre 8 : un script fraîchement écrit n'est qu'un fichier texte. Pour que le système accepte de l'**exécuter**, il lui faut le droit `x`. Sans lui : « Permission denied ».

### La notation octale : les chiffres

Tu verras très souvent les permissions exprimées en **chiffres**, comme `chmod 755`. C'est la même chose, écrite autrement. Chaque droit vaut un nombre :

- `r` = **4**
- `w` = **2**
- `x` = **1**

On **additionne** pour chaque catégorie, ce qui donne un chiffre de 0 à 7 :

| Chiffre | Droits | Calcul |
|---------|--------|--------|
| 7 | `rwx` | 4+2+1 |
| 6 | `rw-` | 4+2 |
| 5 | `r-x` | 4+1 |
| 4 | `r--` | 4 |
| 0 | `---` | rien |

On écrit alors **trois** chiffres : propriétaire, groupe, autres.

```bash
chmod 755 script.sh      # rwx pour le proprio, r-x pour groupe et autres
chmod 644 fichier.txt    # rw- pour le proprio, r-- pour groupe et autres
chmod 600 secret.txt     # rw- pour le proprio, RIEN pour les autres
```

> **Les deux valeurs à mémoriser :** `644` pour un fichier de données normal (le propriétaire écrit, les autres lisent), `755` pour un programme ou un dossier (tout le monde peut exécuter/traverser, seul le propriétaire modifie). `600` pour un fichier privé (clé, secret) que toi seul peux lire. Ces trois valeurs couvrent l'immense majorité des cas.

### `umask` : les permissions par défaut

Quand tu crées un fichier, il reçoit des permissions par défaut. Celles-ci sont déterminées par le `umask`, un « filtre » qui **retire** des droits par défaut (typiquement, il enlève l'écriture aux autres) :

```bash
umask            # affiche le masque actuel (souvent 022)
```

Pour débuter, retiens simplement que `umask` **existe** et explique pourquoi tes nouveaux fichiers ne sont pas en écriture pour tout le monde. Tu n'as pas besoin de le modifier maintenant.

## ❌ Erreur classique

```bash
# Oublier de rendre un script exécutable
./mon-script.sh          # ❌ "Permission denied"
chmod u+x mon-script.sh  # ✅ puis ./mon-script.sh fonctionne

# Donner trop de droits "pour que ça marche"
chmod 777 fichier        # ❌ rwx pour TOUT LE MONDE : faille de sécurité béante
chmod 755 fichier        # ✅ juste ce qu'il faut

# Confondre l'ordre des chiffres
chmod 457 fichier        # rarement ce qu'on veut : réfléchis proprio/groupe/autres
chmod 644 fichier        # ✅ l'ordre est TOUJOURS proprio, groupe, autres

# Croire que r suffit pour entrer dans un dossier
chmod 600 dossier/       # ❌ sans x, impossible d'y faire cd
chmod 700 dossier/       # ✅ le x permet de traverser le dossier
```

> **Le réflexe `777` est un grand classique du débutant** : « ça ne marche pas, je mets tous les droits à tout le monde ». C'est exactement ce qu'un attaquant rêve de trouver. Donne **le minimum nécessaire**, jamais `777`.

## Exercices

**Guidé :** Crée un fichier `script.sh` contenant `echo "Bonjour"` (avec `echo "echo \"Bonjour\"" > script.sh`). Regarde ses permissions avec `ls -l`. Essaie de le lancer avec `./script.sh` — ça échoue. Rends-le exécutable avec `chmod u+x script.sh`, vérifie le changement avec `ls -l`, puis relance-le.

**Autonome :** Crée trois fichiers et donne-leur respectivement les permissions `644`, `600` et `755` en notation octale. Vérifie chacune avec `ls -l` et **traduis à voix haute** ce que chaque triplet signifie (qui peut faire quoi).

**Défi :** Pour un fichier donné, atteins exactement les permissions `rw-r-----` (le proprio lit/écrit, le groupe lit, les autres rien). Fais-le d'abord en notation symbolique (`chmod`), puis recommence sur un autre fichier en notation octale. Quel est le chiffre octal correspondant ? Vérifie avec `ls -l` que les deux méthodes donnent le même résultat.

## ✅ Tu sais maintenant…

- Le modèle **propriétaire / groupe / autres** (u/g/o) et les trois droits **r/w/x**
- **Lire** la ligne de permissions d'un `ls -l`, caractère par caractère
- Que `x` signifie « exécuter » sur un fichier mais « traverser » sur un dossier
- Modifier les droits avec `chmod` en **symbolique** (`u+x`, `go-w`…)
- La notation **octale** (r=4, w=2, x=1) et les valeurs clés `644`, `755`, `600`
- Pourquoi `chmod 777` est une mauvaise idée de sécurité
- Que `umask` détermine les permissions par défaut

---

# Chapitre 10 — Propriété, utilisateurs et groupes

## Le minimum à savoir

### L'identité sur un système Linux

Les permissions du chapitre 9 reposent sur une question : **qui es-tu ?** Sous Linux, chaque utilisateur a une identité numérique (un **UID**, *user ID*) et appartient à un ou plusieurs **groupes** (chacun avec un **GID**, *group ID*). Le système ne raisonne pas vraiment avec les noms (`alice`), mais avec ces numéros ; les noms sont là pour nous, humains.

```bash
id               # affiche TON identité : uid, gid, et tous tes groupes
whoami           # affiche juste ton nom d'utilisateur
groups           # affiche les groupes auxquels tu appartiens
```

Un exemple de sortie de `id` :

```
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo),100(users)
```

On y lit : alice a l'UID 1000, son groupe principal est `alice`, et elle appartient aussi aux groupes `sudo` (important : il donne le droit d'administrer !) et `users`.

### root : le super-utilisateur

Un compte est à part : **root**, l'administrateur. Son UID est **0**, et il **ignore les permissions** : root peut tout lire, tout modifier, tout supprimer. C'est à la fois indispensable (pour administrer) et dangereux (une erreur en root peut détruire le système). On verra au chapitre 11 comment utiliser ce pouvoir proprement, sans rester connecté en root en permanence.

### Où sont stockés les comptes ? Trois fichiers clés

Toute l'information sur les utilisateurs vit dans trois fichiers texte. **Savoir les lire est un réflexe d'audit fondamental.**

```bash
cat /etc/passwd          # la liste des comptes (lisible par tous)
cat /etc/group           # la liste des groupes
sudo cat /etc/shadow     # les mots de passe (chiffrés) — accès root uniquement
```

- **`/etc/passwd`** : une ligne par compte. Malgré son nom, il ne contient **pas** les mots de passe (historiquement oui, plus aujourd'hui). Chaque ligne, séparée par des `:`, donne le nom, l'UID, le GID, le dossier personnel, le shell…

  ```
  alice:x:1000:1000:Alice Martin:/home/alice:/bin/bash
  ```

- **`/etc/group`** : les groupes et leurs membres.
- **`/etc/shadow`** : les **empreintes chiffrées** des mots de passe. Lisible uniquement par root — c'est une protection essentielle.

> **Très utile en sécurité :** lire `/etc/passwd` est l'un des premiers gestes d'un audit. On y repère les comptes existants, ceux qui ont un vrai shell de connexion (`/bin/bash`) versus ceux qui n'en ont pas (`/usr/sbin/nologin`, typiques des comptes de service), et tout compte suspect ajouté par un intrus. La première colonne (`cut -d: -f1 /etc/passwd`, vu au chapitre 4) liste tous les comptes.

## Très utile en pratique

### Changer le propriétaire : `chown` et `chgrp`

Quand un fichier doit appartenir à quelqu'un d'autre (ou à un autre groupe), on utilise `chown` (*change owner*) :

```bash
sudo chown alice fichier.txt          # alice devient propriétaire
sudo chown alice:equipe fichier.txt   # propriétaire alice, groupe equipe
sudo chgrp equipe fichier.txt         # change seulement le groupe
```

Ces commandes nécessitent en général `sudo` : changer la propriété d'un fichier est une opération privilégiée.

> **Souviens-toi de la Partie 0 :** `chown -R` et `chmod -R` (récursifs) figurent dans les commandes dangereuses. Appliqués au mauvais dossier, ils peuvent rendre tout un pan du système inaccessible. Vérifie **toujours** le chemin avant un `-R`.

### Créer un utilisateur

Sur Debian/Ubuntu, le plus simple est `adduser`, un assistant interactif qui crée le compte, son dossier personnel et demande le mot de passe :

```bash
sudo adduser bob         # assistant guidé (recommandé sur Debian/Ubuntu)
```

Il existe aussi `useradd`, plus bas niveau et plus universel, mais moins convivial (il ne crée pas le dossier personnel sans options) :

```bash
sudo useradd -m -s /bin/bash bob     # -m crée le /home, -s définit le shell
sudo passwd bob                      # définit ensuite son mot de passe
```

### Gérer les mots de passe et les groupes

```bash
passwd                   # change TON propre mot de passe
sudo passwd bob          # change le mot de passe de bob (en admin)
sudo usermod -aG sudo bob   # ajoute bob au groupe "sudo" (-aG = append to Group)
```

> **L'option `-aG` est cruciale et piégeuse :** le `-a` (*append*, ajouter) est **obligatoire**. Sans lui, `usermod -G` **remplace** tous les groupes de l'utilisateur par celui indiqué, le retirant de tous les autres. Oublier le `-a` est une erreur classique qui peut, par exemple, retirer quelqu'un du groupe `sudo` sans le vouloir.

### Changer d'identité : `su`

`su` (*substitute user*) permet de devenir un autre utilisateur le temps d'une session :

```bash
su - bob         # devient bob (le tiret recharge SON environnement complet)
```

Le tiret `-` est important : il charge l'environnement de la cible (son `PATH`, son `HOME`, son `.bashrc` — tout ce qu'on a vu au chapitre 8) comme une vraie connexion. Sans le tiret, tu gardes en partie ton ancien environnement, ce qui prête à confusion. On reparlera de `su -` face à `sudo` au chapitre suivant.

## ❌ Erreur classique

```bash
# Oublier le -a dans usermod et écraser les groupes
sudo usermod -G sudo bob     # ❌ retire bob de TOUS ses autres groupes
sudo usermod -aG sudo bob    # ✅ AJOUTE bob au groupe sudo

# Croire que /etc/passwd contient les mots de passe
cat /etc/passwd              # le "x" en 2e champ renvoie à /etc/shadow
sudo cat /etc/shadow         # les empreintes chiffrées sont ICI

# Utiliser useradd en pensant que tout est prêt
sudo useradd bob             # ❌ pas de /home, pas de shell utilisable par défaut
sudo adduser bob             # ✅ assistant complet sur Debian/Ubuntu

# Faire su sans le tiret et s'étonner de l'environnement
su bob                       # garde une partie de TON environnement
su - bob                     # ✅ charge proprement l'environnement de bob

# chown récursif sur le mauvais dossier
sudo chown -R bob /           # ❌❌ catastrophe système
sudo chown -R bob /home/bob   # ✅ cible précise
```

## Exercices

**Guidé :** Lance `id` et `groups` sur ton propre compte. Repère ton UID, ton groupe principal, et la liste de tes groupes. Es-tu membre du groupe `sudo` ? Ensuite, affiche les cinq premières lignes de `/etc/passwd` avec `head -5 /etc/passwd` et identifie, pour ton compte, son dossier personnel et son shell.

**Autonome (en lab) :** Crée un nouvel utilisateur `testuser` avec `sudo adduser testuser`. Vérifie qu'il apparaît bien dans `/etc/passwd` (avec `grep testuser /etc/passwd`). Ajoute-le à un groupe existant avec `sudo usermod -aG users testuser`, puis confirme avec `groups testuser`. Quand tu as terminé, tu peux le supprimer avec `sudo deluser testuser`.

**Défi (orientation sécurité) :** Réalise un mini-audit des comptes. Avec `cut -d: -f1,7 /etc/passwd`, liste chaque compte avec son shell. Distingue les comptes qui ont un shell de connexion réel (`/bin/bash`, `/bin/sh`) de ceux qui ont `nologin` ou `false` (comptes de service, non destinés à se connecter). Combien de comptes peuvent réellement ouvrir une session ? C'est exactement la question que se pose un analyste face à une machine inconnue.

## ✅ Tu sais maintenant…

- Que l'identité repose sur des **UID** et des **GID**, derrière les noms lisibles
- Inspecter ton identité avec `id`, `whoami`, `groups`
- Le rôle de **root** (UID 0), qui ignore les permissions
- Lire les trois fichiers de comptes : `/etc/passwd`, `/etc/group`, `/etc/shadow`
- Changer la propriété avec `chown` / `chgrp` (et la prudence du `-R`)
- Créer un utilisateur (`adduser` sur Debian/Ubuntu, `useradd` ailleurs) et gérer son mot de passe
- Ajouter un utilisateur à un groupe avec `usermod -aG` (le `-a` **obligatoire**)
- Changer d'identité avec `su -` (le tiret recharge l'environnement)
- **Auditer les comptes** d'une machine en lisant `/etc/passwd`

---

# Chapitre 11 — sudo et l'élévation de privilèges

## Le minimum à savoir

### Le principe de moindre privilège

Le concept le plus important de la sécurité tient en une phrase : **on n'utilise que les droits dont on a besoin, au moment où on en a besoin, et pas plus.** C'est le **principe de moindre privilège**. Rester connecté en root « pour être tranquille » est exactement le contraire : la moindre erreur, ou le moindre programme malveillant lancé par mégarde, dispose alors de tous les pouvoirs. La bonne pratique est de travailler en utilisateur normal et de **n'élever ses privilèges que ponctuellement**, commande par commande.

### `sudo` : emprunter les pouvoirs de root, une commande à la fois

`sudo` (*substitute user do*, « faire en tant qu'un autre ») exécute **une seule commande** avec les droits de root, puis te rend immédiatement ton identité normale :

```bash
sudo apt update                  # exécute CETTE commande en root
sudo cat /etc/shadow             # lit un fichier réservé à root, puis on redevient normal
```

La première fois, `sudo` te demande **ton propre** mot de passe (pas celui de root), puis le mémorise quelques minutes pour ne pas te le redemander à chaque commande. Seuls les utilisateurs autorisés (membres du groupe `sudo` sur Debian/Ubuntu — souviens-toi de `id` au chapitre 10) peuvent l'utiliser.

> **Le minimum à savoir :** quand une commande échoue avec « Permission denied » et qu'il s'agit d'une vraie tâche d'administration (installer un logiciel, modifier `/etc`, gérer un service), préfixe-la par `sudo`. Mais demande-toi toujours : ai-je **vraiment** besoin des droits root pour ça ?

### Distinguer les façons d'élever ses privilèges

Plusieurs commandes se ressemblent mais font des choses différentes. Cette distinction est essentielle :

| Commande | Ce qu'elle fait |
|----------|-----------------|
| `sudo commande` | Exécute **une seule** commande en root, puis revient à toi. **C'est la méthode recommandée.** |
| `sudo -i` | Ouvre un **shell root interactif** (tu *deviens* root jusqu'à ce que tu tapes `exit`). À éviter sauf nécessité. |
| `su -` | Bascule vers le compte root en demandant **le mot de passe de root** (pas le tien). Souvent désactivé sur Ubuntu. |
| `sudoedit fichier` | Édite un fichier système en sécurité (vu au chapitre 6). Préférable à `sudo nano`. |

> **La différence clé entre `sudo -i` et `su -` :** `sudo -i` utilise **ton** mot de passe et passe par `sudo` (donc c'est journalisé, voir plus bas) ; `su -` réclame le mot de passe **de root** directement. Sur Ubuntu, le compte root n'a pas de mot de passe défini par défaut, donc `su -` échoue et l'on passe par `sudo`. Pour une commande ponctuelle, `sudo commande` reste **toujours** préférable à ouvrir un shell root entier.

## Très utile en pratique

### sudo est journalisé : chaque usage laisse une trace

Contrairement à une connexion root directe, **chaque commande lancée avec `sudo` est enregistrée** : qui, quand, depuis où, quelle commande. C'est un atout majeur pour la sécurité et la traçabilité. On retrouve ces traces dans le journal d'authentification (souviens-toi du chapitre 4 : `/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` ailleurs, ou `journalctl`) :

```bash
sudo grep sudo /var/log/auth.log     # retrouve les usages de sudo (Debian/Ubuntu)
```

> **Très utile en sécurité (SOC) :** lors d'une investigation, ces lignes permettent de répondre à « qui a fait quoi en tant qu'administrateur, et quand ? ». Une élévation de privilège inattendue dans ces logs est un signal d'alerte classique. On approfondira l'analyse des journaux au chapitre 15.

### Configurer sudo proprement : `visudo`

Les droits sudo sont définis dans un fichier spécial, `/etc/sudoers`. **On ne l'édite jamais directement** : on passe par `visudo`, qui **vérifie la syntaxe avant d'enregistrer**. Une erreur dans ce fichier pourrait sinon bloquer tout accès administrateur à la machine.

```bash
sudo visudo              # édite /etc/sudoers en toute sécurité (contrôle de syntaxe)
```

Pour débuter, tu n'as pas besoin de modifier ce fichier ; retiens surtout **pourquoi** `visudo` existe : c'est le garde-fou qui t'empêche de te verrouiller dehors. C'est le même esprit que le `.bak` du chapitre 6, appliqué au fichier le plus sensible du système.

### sudo, vecteur d'attaque classique

Du point de vue d'un attaquant, `sudo` est une cible de choix : s'il parvient à exécuter une commande via un `sudo` mal configuré, il obtient les pleins pouvoirs. C'est pourquoi, en sécurité, on vérifie systématiquement **ce qu'un utilisateur a le droit de faire avec sudo** :

```bash
sudo -l          # liste ce que TU es autorisé à exécuter via sudo
```

> **Orientation cyber / eJPT :** `sudo -l` est l'une des toutes premières commandes lancées lors d'une recherche d'élévation de privilèges. Une règle sudo trop permissive (par exemple, le droit de lancer un éditeur ou un interpréteur en root) est une voie d'escalade très répandue. Côté défense, on garde les règles sudo **minimales et précises**. On reverra ce réflexe au chapitre sécurité (25).

## ❌ Erreur classique

```bash
# Tout faire en root "pour être tranquille"
sudo -i                  # ❌ shell root permanent : une erreur = dégâts maximaux
sudo commande            # ✅ une commande à la fois, on reste normal le reste du temps

# Éditer /etc/sudoers directement
sudo nano /etc/sudoers   # ❌ une faute de syntaxe peut bloquer tout sudo
sudo visudo              # ✅ vérifie la syntaxe avant d'enregistrer

# Mettre sudo devant TOUT, par réflexe
sudo ls ~                # ❌ inutile : tu peux déjà lire ton propre dossier
ls ~                     # ✅ sudo seulement quand c'est nécessaire

# Confondre son mot de passe et celui de root
sudo commande            # demande TON mot de passe
su -                     # demande celui de ROOT (souvent absent sur Ubuntu)

# Oublier que sudo expire
sudo apt update          # mot de passe demandé...
# (quelques minutes plus tard)
sudo apt upgrade         # peut le redemander : c'est normal, c'est une sécurité
```

## Exercices

**Guidé :** Lance `sudo -l` pour voir ce que tu es autorisé à faire via sudo sur ta machine. Ensuite, tente `cat /etc/shadow` sans sudo (ça échoue : Permission denied), puis `sudo cat /etc/shadow` (ça fonctionne, mais ne te montre que des empreintes chiffrées). Observe la différence d'accès qu'apporte l'élévation.

**Autonome :** Utilise `sudo` pour une vraie tâche d'administration inoffensive, par exemple `sudo apt update`. Puis cherche la trace de ton action dans le journal d'authentification avec `sudo grep sudo /var/log/auth.log | tail` (adapte le chemin à ta distribution). Retrouves-tu la commande que tu viens de lancer, avec l'heure ?

**Défi :** Compare concrètement `sudo whoami` et `whoami`. Le premier doit afficher `root`, le second ton nom. Explique en une phrase pourquoi : `sudo` a exécuté `whoami` **en tant que root**, le temps de cette seule commande, avant de te rendre ton identité.

## ✅ Tu sais maintenant…

- Le **principe de moindre privilège** : n'élever ses droits que ponctuellement
- Utiliser `sudo commande` pour exécuter **une** action en root (avec **ton** mot de passe)
- Distinguer `sudo commande`, `sudo -i`, `su -` et `sudoedit`
- Que **chaque usage de sudo est journalisé** (traçabilité, valeur en sécurité)
- Configurer sudo en sécurité avec `visudo` (et pourquoi on n'édite jamais `/etc/sudoers` à la main)
- Vérifier tes droits avec `sudo -l` — réflexe clé en recherche d'escalade de privilèges

---

# Chapitre 12 — Permissions avancées (panorama)

## Le minimum à savoir

### Au-delà des r/w/x : un panorama

Le modèle r/w/x du chapitre 9 couvre 95 % des situations. Mais il existe des permissions **spéciales** qui résolvent des problèmes particuliers — et qui sont, justement pour cette raison, des **cibles privilégiées en sécurité**. L'objectif de ce chapitre n'est pas de te rendre expert, mais de te faire **reconnaître** ces mécanismes : tu dois savoir qu'ils existent, ce qu'ils font, et comment les repérer. C'est exactement ce qu'on regarde lors d'un audit ou d'une recherche d'élévation de privilèges.

### Le bit SUID : exécuter avec les droits du propriétaire

Normalement, quand tu lances un programme, il s'exécute avec **tes** droits. Le bit **SUID** (*Set User ID*) change cela : un programme avec SUID s'exécute avec les droits de **son propriétaire**, pas les tiens. Si le propriétaire est root, le programme tourne donc avec les pouvoirs de root, même lancé par un utilisateur normal.

Un exemple légitime et universel : `passwd`. Pour changer ton mot de passe, le système doit écrire dans `/etc/shadow` (réservé à root). `passwd` est donc SUID root : il te laisse modifier **ta** ligne, en toute sécurité, sans te donner root pour autant.

On repère le SUID dans un `ls -l` par un **`s`** à la place du `x` du propriétaire :

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#    ↑ ce "s" = bit SUID
```

### Pourquoi le SUID est central en sécurité

Le SUID est puissant, donc dangereux. **Un programme SUID root mal conçu ou inattendu est une porte vers les privilèges root.** Si un attaquant trouve sur le système un binaire SUID qui lui permet, d'une manière ou d'une autre, d'exécuter ses propres commandes, il devient root. C'est l'une des voies d'escalade les plus connues.

D'où un réflexe fondamental, aussi bien pour l'auditeur défensif que pour le testeur d'intrusion : **lister tous les fichiers SUID du système**.

```bash
find / -type f -perm -4000 2>/dev/null
```

Décortiquons cette commande, qui réunit tout ce que tu as appris :

- `find /` → cherche à partir de la racine (chapitre 4)
- `-type f` → uniquement des **fichiers** (pas des dossiers ni autres objets)
- `-perm -4000` → qui ont le bit SUID activé (le `4000` octal)
- `2>/dev/null` → on jette les innombrables « Permission denied » (chapitre 7) pour ne garder que les résultats utiles

> **Orientation cyber / eJPT :** cette commande figure dans toute checklist d'énumération d'un système Linux. Côté défense, on compare la liste obtenue aux binaires SUID **attendus** (ceux livrés par la distribution) ; tout SUID inhabituel mérite une enquête immédiate.

## Très utile en pratique

### SGID et sticky bit, en bref

Deux autres bits spéciaux, à connaître de nom :

- **SGID** (*Set Group ID*) : comme le SUID mais pour le **groupe**. Sur un dossier, il fait hériter tous les nouveaux fichiers du groupe du dossier — pratique pour le travail collaboratif. Repérable par un `s` dans le triplet du groupe.
- **Sticky bit** : posé sur un dossier partagé (comme `/tmp`), il empêche chacun de supprimer les fichiers des autres — tu ne peux effacer que **tes** fichiers. Repérable par un `t` à la fin :

  ```bash
  ls -ld /tmp
  # drwxrwxrwt ... /tmp     ← le "t" final = sticky bit
  ```

### Les capabilities : des privilèges root « en pièces détachées »

Sur les systèmes modernes, une alternative plus fine au tout-puissant SUID existe : les **capabilities**. Plutôt que de donner *tous* les pouvoirs de root à un programme, on lui accorde **un privilège précis et limité**. Par exemple, la capability `cap_net_raw` autorise un programme (comme `ping`) à manipuler le réseau à bas niveau, sans pour autant lui donner le reste des pouvoirs root.

On **observe** les capabilities présentes sur le système avec `getcap` :

```bash
getcap -r / 2>/dev/null      # liste récursivement tous les binaires porteurs de capabilities
```

> **Si `getcap` n'est pas disponible** (installations minimales), installe le paquet qui le fournit : `sudo apt install libcap2-bin`.

C'est le pendant moderne de la recherche de SUID : un binaire doté d'une capability trop puissante (ou inattendue) peut, lui aussi, ouvrir une voie d'escalade.

> **Important — observation, pas manipulation :** à ton niveau, `getcap` s'utilise en **observation** (lister, auditer). La commande inverse, `setcap`, qui *attribue* une capability à un binaire, ne doit être expérimentée qu'en **lab contrôlé**, sur une **copie** de binaire ou un exemple jetable — **jamais** sur un binaire système réel sans comprendre précisément ce que l'on fait. Modifier les capabilities d'un binaire système peut affaiblir gravement la sécurité de la machine.

### Les ACL, en un mot

Le modèle u/g/o ne permet qu'**un** propriétaire et **un** groupe. Quand on a besoin de droits plus granulaires (« alice peut écrire, bob peut seulement lire, et ce groupe précis a un autre accès »), on utilise les **ACL** (*Access Control Lists*). On les consulte avec `getfacl` et on les modifie avec `setfacl`. Pour débuter, retiens simplement qu'elles **existent** et permettent des permissions plus fines que le modèle de base — tu n'as pas à les manipuler maintenant.

## ❌ Erreur classique

```bash
# Oublier 2>/dev/null et se noyer sous les erreurs
find / -type f -perm -4000           # ❌ noyé sous les "Permission denied"
find / -type f -perm -4000 2>/dev/null  # ✅ seulement les résultats utiles

# Oublier -type f et lister autre chose que des fichiers
find / -perm -4000 2>/dev/null       # mélange fichiers et autres objets
find / -type f -perm -4000 2>/dev/null  # ✅ uniquement des fichiers

# Confondre le "s" du SUID et le "s" du SGID
# -rwsr-xr-x → SUID (s dans le triplet PROPRIÉTAIRE)
# -rwxr-sr-x → SGID (s dans le triplet GROUPE)

# Utiliser setcap sur un binaire système "pour tester"
sudo setcap cap_setuid+ep /usr/bin/python3   # ❌❌ faille de sécurité majeure
# ✅ getcap pour OBSERVER ; setcap seulement en lab sur une copie jetable

# Ajouter du SUID par curiosité
sudo chmod u+s /un/binaire           # ❌ ne jamais "essayer" ça sur un système réel
```

## Exercices

**Guidé :** Liste les fichiers SUID de ton système avec `find / -type f -perm -4000 2>/dev/null`. Tu devrais y voir des classiques comme `/usr/bin/passwd` ou `/usr/bin/sudo`. Choisis-en un et confirme son bit SUID avec `ls -l` : repères-tu bien le `s` à la place du `x` du propriétaire ?

**Autonome :** Observe le sticky bit de `/tmp` avec `ls -ld /tmp` et identifie le `t` final. Explique en une phrase pourquoi ce bit est important sur un dossier où **tout le monde** peut écrire. Ensuite, liste les capabilities présentes sur ta machine avec `getcap -r / 2>/dev/null` : combien de binaires en portent ?

**Défi (orientation sécurité) :** Tu fais l'inventaire de sécurité d'une machine. Produis deux listes : (1) tous les fichiers SUID, (2) tous les binaires avec capabilities. Enregistre chacune dans un fichier (avec `>` ou `tee`, chapitre 7) pour garder une trace. Ces deux listes constituent une **base de référence** : sur un vrai système, on les comparerait régulièrement pour détecter tout ajout suspect. Quel intérêt défensif vois-tu à conserver une telle référence dans le temps ?

## ✅ Tu sais maintenant…

- Que des permissions **spéciales** existent au-delà des r/w/x
- Ce qu'est le **SUID** (exécuter avec les droits du propriétaire) et comment le repérer (`s`)
- Pourquoi le SUID est une **voie d'escalade** majeure, et comment lister les SUID : `find / -type f -perm -4000 2>/dev/null`
- Reconnaître le **SGID** (`s` du groupe) et le **sticky bit** (`t`, sur `/tmp`)
- Que les **capabilities** découpent les pouvoirs de root, et les observer avec `getcap -r /` (jamais `setcap` hors lab)
- Que les **ACL** existent pour des droits plus fins (`getfacl`/`setfacl`)
- À constituer une **base de référence** SUID/capabilities, réflexe défensif

---

> **🏁 CHECKPOINT 3 — Fin de la Partie 3 (le plus important pour la sécurité)**
>
> Tu comprends maintenant **le modèle de sécurité de Linux** : qui possède quoi, qui peut faire quoi, comment on élève ses privilèges proprement, et où se cachent les voies d'escalade. C'est le socle de toute administration sérieuse et de toute analyse défensive.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - lire une ligne de `ls -l` et dire exactement qui peut lire, écrire, exécuter ?
> - traduire `chmod 640` en `rw-r-----` et inversement ?
> - expliquer le principe de moindre privilège et pourquoi `sudo commande` vaut mieux que `sudo -i` ?
> - retrouver dans les logs qui a utilisé `sudo` et quand ?
> - lister les binaires SUID d'un système et expliquer pourquoi c'est un enjeu de sécurité ?
>
> Si oui, tu as franchi l'étape conceptuelle la plus exigeante du cours. La suite va te faire passer de « gérer des fichiers et des droits » à « piloter une machine vivante » : place à la **Partie 4 — Processus, services et logs**.

---

---
---

# PARTIE 4 — La machine vivante

Jusqu'ici, tu manipulais des fichiers « au repos ». Maintenant, on regarde le système **en train de fonctionner** : les programmes qui tournent (processus), ceux qui tournent en permanence (services), ce que la machine raconte sur elle-même (logs), et comment lui faire faire des choses automatiquement dans le temps (tâches planifiées). C'est le passage de « gérer des fichiers » à « administrer une machine vivante ».

---

# Chapitre 13 — Les processus

## Le minimum à savoir

### Programme vs processus

Un **programme** est un fichier sur le disque (le binaire `/usr/bin/firefox`, par exemple) : inerte, il ne fait rien. Quand tu le lances, le système en crée une copie active en mémoire : c'est un **processus**. Un même programme peut donner naissance à plusieurs processus en même temps (plusieurs fenêtres d'un éditeur, par exemple). Retiens la formule : **un processus est un programme en cours d'exécution**.

### Chaque processus a un numéro : le PID

Le système identifie chaque processus par un numéro unique, le **PID** (*Process ID*). C'est par ce numéro qu'on agit sur un processus (pour l'observer, le mettre en pause, l'arrêter). Chaque processus connaît aussi son « parent » (le processus qui l'a lancé), identifié par le **PPID** (*Parent PID*). Tous les processus descendent ainsi d'un ancêtre commun lancé au démarrage de la machine.

### Voir les processus : `ps`

`ps` (*process status*) liste les processus. La combinaison la plus utile est `ps aux`, qui montre **tous** les processus de **tous** les utilisateurs :

```bash
ps aux                   # tous les processus, avec utilisateur, PID, CPU, mémoire…
ps aux | grep firefox    # ne garder que les lignes liées à firefox (pipe du chapitre 7)
```

Les colonnes importantes : `USER` (qui l'a lancé), `PID` (son numéro), `%CPU` et `%MEM` (ce qu'il consomme), et la commande elle-même. Le `ps aux | grep ...` est un réflexe quotidien : « ce programme tourne-t-il, et sous quel PID ? ».

### Voir en temps réel : `top` et `htop`

`ps` donne une photo à un instant donné. Pour observer l'activité **en continu**, on utilise `top` (toujours présent) :

```bash
top                      # tableau de bord temps réel ; on quitte avec q
```

`top` affiche, rafraîchies en direct, la charge du système et les processus les plus gourmands. On le quitte avec `q` (comme `man` et `less`).

`htop` est une version plus colorée et plus lisible, qu'on installe au besoin (réflexe de la Partie 0) :

```bash
sudo apt install htop
htop                     # version améliorée et navigable de top
```

> **Très utile en pratique :** quand une machine devient lente, le premier geste est `top` ou `htop` pour voir **quel processus dévore le CPU ou la mémoire**. C'est le point de départ de presque tout diagnostic de performance (on y reviendra au chapitre 24).

## Très utile en pratique

### Arrêter un processus : les signaux et `kill`

Pour demander à un processus de s'arrêter, on lui envoie un **signal** avec `kill`, en lui donnant son PID :

```bash
kill 4821                # envoie le signal par défaut (TERM) : demande polie d'arrêt
kill -9 4821             # envoie KILL : arrêt FORCÉ, sans condition
```

Deux signaux à connaître :

- **TERM** (le défaut) : « termine-toi proprement ». Le processus peut sauvegarder et fermer correctement. **C'est celui qu'on essaie en premier.**
- **KILL** (`-9`) : « arrête-toi immédiatement », sans possibilité de se préparer. Brutal, à réserver aux processus qui ne répondent plus.

> **Le bon ordre :** toujours essayer `kill PID` (poli) d'abord. Ne passer à `kill -9 PID` que si le processus refuse de s'arrêter. Le `-9` est un dernier recours, pas la solution par défaut : il peut laisser des fichiers à moitié écrits ou des données perdues.

Pour arrêter tous les processus d'un même nom :

```bash
killall firefox          # arrête tous les processus nommés "firefox"
```

### Premier plan, arrière-plan : `&`, `jobs`, `fg`, `bg`

Quand tu lances une commande longue, elle occupe ton terminal jusqu'à la fin. Tu peux la lancer **en arrière-plan** avec `&` pour récupérer la main :

```bash
une-longue-commande &    # lance en arrière-plan, le terminal reste libre
jobs                     # liste les tâches lancées depuis ce terminal
fg                       # ramène une tâche au premier plan (foreground)
```

Tu peux aussi suspendre une commande en cours avec `Ctrl + Z`, puis la relancer en arrière-plan avec `bg` ou au premier plan avec `fg`. Pour débuter, l'essentiel est `&` (lancer en fond) et `Ctrl + C` (interrompre la commande au premier plan).

### La priorité : `nice` (notion)

Chaque processus a une priorité qui influence sa part de temps processeur. On peut lancer un programme avec une priorité réduite (pour qu'il ne ralentisse pas le reste) avec `nice`. À ton niveau, retiens simplement que ça **existe** : on peut rendre un processus « plus poli » envers les autres.

## ❌ Erreur classique

```bash
# Dégainer kill -9 d'emblée
kill -9 4821             # ❌ brutal, risque de perte de données
kill 4821                # ✅ d'abord la demande propre (TERM)

# Se tromper de PID et arrêter le mauvais processus
kill 1                   # ❌❌ PID 1 = le processus maître du système, NE JAMAIS toucher
ps aux | grep le-bon-nom # ✅ vérifie le PID AVANT d'agir

# Confondre le nom et le PID
kill firefox             # ❌ kill attend un numéro, pas un nom
killall firefox          # ✅ killall travaille par nom
kill 4821                # ✅ kill travaille par PID

# Croire que fermer le terminal arrête un processus en arrière-plan
commande &               # selon les cas, peut continuer après fermeture du terminal
```

> **Ne touche jamais au PID 1.** C'est le tout premier processus, l'ancêtre de tous les autres (souvent `systemd`, voir chapitre suivant). L'arrêter reviendrait à éteindre brutalement le système.

## Exercices

**Guidé :** Lance `top`, observe quelques secondes quel processus consomme le plus de CPU et de mémoire, puis quitte avec `q`. Ensuite, avec `ps aux | grep bash`, retrouve le PID de ton propre shell. Compare-le à ce qu'affiche la variable spéciale `echo $$` (qui donne le PID du shell courant) : est-ce le même ?

**Autonome :** Lance une commande qui tourne longtemps en arrière-plan, par exemple `sleep 300 &` (attend 300 secondes sans rien faire). Liste-la avec `jobs`, retrouve son PID avec `ps aux | grep sleep`, puis arrête-la proprement avec `kill <PID>`. Vérifie avec `jobs` ou `ps` qu'elle a bien disparu.

**Défi (orientation sécurité) :** Lance `ps aux` et parcours la liste des processus. Pour chacun, demande-toi : est-ce que je reconnais ce programme et l'utilisateur qui le lance ? Sur une vraie machine, un analyste cherche ici un processus au **nom inhabituel**, lancé depuis un **emplacement suspect** (comme `/tmp`), ou consommant des ressources anormales. Repère le processus avec le plus gros `%CPU` et identifie de quel programme il s'agit : est-il légitime ?

## ✅ Tu sais maintenant…

- La différence entre **programme** (fichier inerte) et **processus** (programme en exécution)
- Que chaque processus a un **PID** (et un **PPID**, son parent)
- Lister les processus avec `ps aux` (souvent suivi de `| grep`)
- Observer l'activité **en temps réel** avec `top` et `htop` (sortie : `q`)
- Arrêter un processus avec `kill PID` (poli) puis `kill -9 PID` (forcé, en dernier recours), et `killall nom`
- Gérer l'arrière-plan avec `&`, `jobs`, `fg`, et interrompre avec `Ctrl + C`
- Qu'on ne touche **jamais** au PID 1, et qu'un processus suspect se repère par son nom, son origine et sa consommation

---

# Chapitre 14 — Les services avec systemd

## Le minimum à savoir

### Qu'est-ce qu'un service (ou démon) ?

Certains programmes ne sont pas faits pour être lancés à la main puis fermés : ils doivent tourner **en permanence**, en arrière-plan, prêts à répondre à tout moment. C'est le cas d'un serveur web, d'une base de données, ou du **serveur SSH** qui attend les connexions distantes. Ces programmes de fond s'appellent des **services**, ou **démons** (*daemons*). Leur nom se termine souvent par un `d` : `sshd` (SSH daemon), `cron`, etc.

### systemd : le chef d'orchestre

Au démarrage de la machine, quelque chose doit lancer tous ces services dans le bon ordre, les surveiller, les redémarrer s'ils tombent. Sur la quasi-totalité des distributions modernes, ce rôle est tenu par **systemd**. C'est lui le fameux **PID 1** du chapitre précédent : le tout premier processus, ancêtre de tous les autres. systemd gère des unités appelées **units**, dont les plus courantes sont les services (`.service`).

### Piloter un service : `systemctl`

L'outil unique pour gérer les services est `systemctl`. Sa logique est simple et régulière :

```bash
systemctl status ssh         # quel est l'état du service SSH ? (actif ? en erreur ?)
sudo systemctl start ssh     # démarre le service
sudo systemctl stop ssh      # arrête le service
sudo systemctl restart ssh   # redémarre (stop puis start)
sudo systemctl reload ssh    # recharge la config sans interrompre le service
```

La commande la plus utile au quotidien est `status` : elle te dit si le service tourne, depuis quand, et affiche ses dernières lignes de journal — précieux pour comprendre un problème.

> **Le minimum à savoir :** `systemctl status nom-du-service` pour diagnostiquer, `start`/`stop`/`restart` pour agir. Les actions qui modifient l'état (start, stop, restart) demandent `sudo` ; consulter le `status` est souvent possible sans.

### Démarrage automatique : `enable` et `disable`

Démarrer un service avec `start` ne le relance **pas** au prochain redémarrage de la machine. Pour qu'un service se lance **automatiquement au boot**, il faut l'**activer** :

```bash
sudo systemctl enable ssh    # SSH démarrera automatiquement à chaque démarrage
sudo systemctl disable ssh   # SSH ne démarrera plus automatiquement
sudo systemctl enable --now ssh   # active ET démarre tout de suite
```

> **Distinction essentielle :** `start` agit **maintenant** (jusqu'au prochain reboot), `enable` agit **au démarrage** (de façon permanente). On les confond souvent. Un service qu'on veut voir tourner durablement doit être à la fois **démarré** et **activé** — d'où le pratique `enable --now`.

## Très utile en pratique

### Lister et explorer les services

```bash
systemctl list-units --type=service          # tous les services actuellement chargés
systemctl list-units --type=service --state=running   # uniquement ceux qui tournent
systemctl list-unit-files --type=service     # tous les services installés et leur statut
```

> **Très utile en sécurité :** lister les services actifs revient à dresser l'inventaire de ce qui **tourne** — donc de ce qui pourrait être attaqué. Un service inattendu, ou activé sans raison, mérite qu'on s'y intéresse. C'est aussi la base du durcissement (chapitre 25) : **désactiver les services inutiles réduit la surface d'attaque**.

### Lire le journal d'un service

Quand un service refuse de démarrer, son journal explique pourquoi. `systemctl status` en donne un aperçu, mais on accède au journal complet avec `journalctl` (le chapitre 15 lui est consacré) :

```bash
systemctl status nginx       # aperçu de l'état + dernières lignes de log
journalctl -u nginx          # le journal complet du service nginx
```

Ce duo `status` + `journalctl -u` est la base du diagnostic d'un service défaillant : on regarde l'état, puis on lit ce que le service a écrit avant de tomber.

## ❌ Erreur classique

```bash
# Confondre start et enable
sudo systemctl start ssh     # démarre maintenant... mais pas après reboot
sudo systemctl enable ssh    # ✅ pour qu'il revienne au démarrage
sudo systemctl enable --now ssh  # ✅ les deux d'un coup

# Oublier sudo pour les actions
systemctl restart ssh        # ❌ "Permission denied" / demande d'authentification
sudo systemctl restart ssh   # ✅

# Se tromper de nom de service
systemctl status sshd        # selon la distro, le service s'appelle "ssh" ou "sshd"
systemctl status ssh         # ✅ sur Debian/Ubuntu c'est souvent "ssh"

# Modifier une config de service et oublier de recharger
sudoedit /etc/ssh/sshd_config   # modification faite...
# ❌ ...mais le service tourne encore avec l'ancienne config
sudo systemctl restart ssh      # ✅ recharge la nouvelle config
```

## Exercices

**Guidé :** Affiche l'état du service SSH avec `systemctl status ssh` (ou `sshd` selon ta distribution). Est-il `active (running)` ? Est-il `enabled` (démarrage auto) ? Lis attentivement les dernières lignes affichées : que t'apprennent-elles sur le service ?

**Autonome :** Liste tous les services en cours d'exécution avec `systemctl list-units --type=service --state=running`. Combien y en a-t-il ? Parcours la liste : reconnais-tu le rôle de quelques-uns (réseau, journalisation, planification…) ?

**Défi (en lab) :** Sur une machine de test, choisis un service non critique, note son état avec `systemctl status`, arrête-le avec `sudo systemctl stop`, vérifie qu'il est bien `inactive`, puis redémarre-le et confirme qu'il est de nouveau `active`. **Ne fais jamais cela sur le service SSH d'une machine à laquelle tu es connecté à distance** — tu couperais ta propre connexion (on en reparlera au chapitre 17).

## ✅ Tu sais maintenant…

- Ce qu'est un **service / démon** : un programme qui tourne en permanence en arrière-plan
- Que **systemd** orchestre les services et qu'il est le **PID 1**
- Piloter un service avec `systemctl` : `status`, `start`, `stop`, `restart`, `reload`
- La différence cruciale entre `start` (maintenant) et `enable` (au démarrage), et le raccourci `enable --now`
- Lister les services actifs (`list-units`) et pourquoi c'est un enjeu de surface d'attaque
- Diagnostiquer un service défaillant avec `status` puis `journalctl -u`

---

# Chapitre 15 — Les logs et journaux

## Le minimum à savoir

### Pourquoi les logs sont la matière première de la sécurité

Un système Linux **raconte en permanence ce qu'il fait** : connexions, erreurs, démarrages de services, tentatives d'accès refusées… Ces enregistrements sont les **logs** (journaux). Pour un administrateur, ils répondent à « pourquoi ça ne marche pas ? ». Pour un analyste sécurité, ils répondent à « que s'est-il passé, qui, quand ? ». **Sans logs, pas d'investigation possible.** Savoir où ils sont et comment les lire est une compétence centrale, en admin comme en SOC.

### Deux mondes : fichiers texte et journal systemd

Il existe historiquement **deux façons** de stocker les logs, et tu rencontreras les deux :

1. **Les fichiers texte dans `/var/log`** : la méthode classique. Chaque service y écrit son journal, et on les lit avec les outils du chapitre 3-4 (`cat`, `less`, `tail`, `grep`).
2. **Le journal systemd** : centralisé, structuré, interrogeable avec une seule commande, `journalctl`. C'est la méthode moderne, présente sur tous les systèmes systemd.

### Explorer `/var/log`

```bash
ls -lt /var/log              # liste les journaux, les plus récents en premier
sudo less /var/log/syslog    # journal général du système (Debian/Ubuntu)
sudo tail -f /var/log/syslog # suivre le journal système en direct (chapitre 3)
```

Quelques fichiers courants : `syslog` (journal général), les logs d'authentification, et des dossiers propres à certains services.

### Où sont les logs d'authentification ? (rappel essentiel)

Comme annoncé au chapitre 4, l'emplacement du journal d'authentification **dépend de la distribution** :

- **Debian / Ubuntu** : `/var/log/auth.log`
- **RHEL / CentOS / Fedora** : `/var/log/secure`
- **Tout système systemd** : `journalctl` est la méthode **la plus fiable et universelle** (voir ci-dessous)

> Ne sois pas surpris si `/var/log/auth.log` n'existe pas chez toi : c'est que ta distribution range ses logs ailleurs, ou s'appuie entièrement sur le journal systemd. Dans le doute, `journalctl` fonctionne partout où systemd est présent.

## Très utile en pratique

### `journalctl` : le journal unifié

`journalctl` interroge le journal systemd. C'est l'outil le plus puissant de ce chapitre :

```bash
journalctl                       # tout le journal (long ; navigue comme less, quitte avec q)
journalctl -e                    # saute directement à la fin (événements récents)
journalctl -u ssh                # uniquement les messages du service ssh
journalctl -f                    # suit le journal EN DIRECT (comme tail -f)
journalctl --since "today"       # depuis aujourd'hui
journalctl --since "1 hour ago"  # depuis une heure
journalctl -p err                # uniquement les messages de niveau "erreur" et plus grave
```

Les options à retenir en priorité : **`-u`** (filtrer par service), **`-f`** (suivre en direct), **`--since`** (filtrer par date). Combinées, elles répondent à des questions précises :

```bash
journalctl -u ssh --since "today"     # toutes les activités SSH d'aujourd'hui
```

> **Très utile en sécurité (SOC) :** `journalctl -u ssh -f` permet de **suivre en direct les tentatives de connexion SSH**. Couplé au `grep` du chapitre 4, c'est la base de la détection d'une attaque par force brute : on isole les échecs d'authentification, on compte les IP sources, on identifie celles qui frappent le plus.

### `dmesg` : les messages du noyau

À côté des logs de services, il existe un journal particulier : celui du **noyau** (le kernel), accessible avec `dmesg`. Il enregistre tout ce qui touche au **matériel et au bas niveau** :

```bash
sudo dmesg               # messages du noyau
sudo dmesg | tail        # les plus récents
sudo dmesg -T            # avec des dates lisibles (-T = timestamps humains)
```

`dmesg` est l'outil de référence pour les problèmes **matériels** :

- erreurs de **disque** (secteurs défectueux, déconnexions)
- branchement/débranchement de **périphériques USB**
- problèmes de **pilotes (drivers)**
- messages d'erreur du **noyau** lui-même

> **Réflexe :** quand un disque se comporte mal, qu'une clé USB n'est pas reconnue, ou qu'un matériel pose problème, `dmesg -T | tail` est souvent le moyen le plus rapide de voir ce que le noyau a constaté. On le réutilisera dans la démarche de diagnostic du chapitre 24.

### La rotation des logs : `logrotate` (notion)

Les logs grandissent sans cesse. Pour qu'ils ne remplissent pas le disque, un mécanisme appelé **rotation** archive et compresse régulièrement les anciens journaux, et supprime les plus vieux. C'est géré automatiquement par **`logrotate`**. Pour débuter, retiens simplement que ça **existe** : c'est pourquoi tu verras des fichiers comme `auth.log.1`, `auth.log.2.gz` — ce sont d'anciens journaux archivés. Tu n'as rien à configurer maintenant.

## ❌ Erreur classique

```bash
# Lire un gros log avec cat
cat /var/log/syslog          # ❌ des milliers de lignes défilent
sudo less /var/log/syslog    # ✅ page par page
journalctl -u ssh -e         # ✅ ou cibler directement le service

# Oublier sudo pour les logs sensibles
cat /var/log/auth.log        # ❌ souvent "Permission denied"
sudo cat /var/log/auth.log   # ✅ les logs d'auth sont protégés

# Chercher auth.log là où il n'existe pas
cat /var/log/auth.log        # ❌ absent sur RHEL/Fedora
sudo cat /var/log/secure     # ✅ sur RHEL/CentOS/Fedora
journalctl -u sshd           # ✅ méthode universelle (systemd)

# Croire que dmesg ne sert qu'au démarrage
dmesg                        # ❌ besoin de sudo sur beaucoup de systèmes
sudo dmesg -T | tail         # ✅ utile à tout moment pour le matériel
```

## Exercices

**Guidé :** Affiche les événements système d'aujourd'hui avec `journalctl --since "today"` (navigue, puis quitte avec `q`). Ensuite, cible un service précis avec `journalctl -u ssh` (ou un autre service actif chez toi vu au chapitre 14). Que t'apprend son journal ?

**Autonome :** Utilise `sudo dmesg -T | tail -20` pour voir les 20 derniers messages du noyau. Repères-tu des mentions de matériel (disque, USB, réseau) ? Si tu peux brancher/débrancher une clé USB, relance la commande juste après : vois-tu apparaître l'événement ?

**Défi (orientation SOC) :** Reprends la logique de détection de force brute du chapitre 4, mais avec le journal moderne. Avec `journalctl`, isole les tentatives d'authentification SSH échouées (cherche « Failed » dans le journal de SSH), puis, à l'aide des pipes et de `awk`/`grep`/`sort`/`uniq -c` (chapitre 4), identifie les adresses IP qui reviennent le plus souvent. Tu obtiens la même analyse qu'avec `auth.log`, mais d'une façon qui fonctionne sur **n'importe quel** système systemd.

## ✅ Tu sais maintenant…

- Pourquoi les logs sont **la matière première** de l'administration et de la sécurité
- Les deux mondes : **fichiers texte dans `/var/log`** et **journal systemd**
- Explorer `/var/log` avec `ls -lt`, `less`, `tail -f`
- Que les logs d'auth sont dans `auth.log` (Debian/Ubuntu), `secure` (RHEL/Fedora) ou via `journalctl` (universel)
- Interroger le journal avec `journalctl` et ses options clés `-u`, `-f`, `--since`, `-p`
- Lire les messages **matériels et noyau** avec `dmesg` (et `dmesg -T`)
- Que la **rotation** (`logrotate`) archive automatiquement les vieux journaux

---

# Chapitre 16 — Tâches planifiées

## Le minimum à savoir

### Pourquoi automatiser dans le temps

Beaucoup de tâches d'administration doivent se répéter : sauvegarder chaque nuit, nettoyer des fichiers temporaires chaque semaine, vérifier l'espace disque tous les matins. Plutôt que de les lancer à la main, on les **planifie** : le système les exécute tout seul, à l'heure dite, que tu sois là ou non. C'est l'un des grands intérêts d'un serveur, qui tourne en continu.

### cron : le planificateur classique

L'outil historique et universel est **cron**. Chaque utilisateur dispose de sa propre table de tâches planifiées, la **crontab**, qu'on édite ainsi :

```bash
crontab -e               # éditer SA table de tâches planifiées
crontab -l               # afficher SA table actuelle
```

La première fois, `crontab -e` te demande quel éditeur utiliser (choisis `nano` si tu hésites).

### Lire la syntaxe cron : cinq champs

Chaque ligne de la crontab décrit **quand** lancer **quoi**, avec cinq champs de temps suivis de la commande :

```
┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, dimanche = 0 ou 7)
│ │ │ │ │
* * * * *  commande-à-exécuter
```

Une `*` signifie « toutes les valeurs ». Quelques exemples parlants :

```bash
0 8 * * *    /chemin/script.sh      # tous les jours à 8h00
30 2 * * 0   /chemin/backup.sh      # chaque dimanche à 2h30
*/15 * * * * /chemin/check.sh       # toutes les 15 minutes
0 0 1 * *    /chemin/mensuel.sh     # le 1er de chaque mois à minuit
```

> **Le minimum à savoir :** les deux premiers champs (minute, heure) suffisent pour l'immense majorité des besoins : « tous les jours à telle heure ». Pour le reste, on met des `*`. En cas de doute sur une expression, des aides en ligne existent pour traduire une ligne cron en langage clair.

## Très utile en pratique

### Les dossiers cron du système

À côté de la crontab personnelle, le système propose des dossiers où **déposer un script** pour qu'il s'exécute à une fréquence donnée, sans même écrire de ligne cron :

```bash
ls /etc/cron.daily/      # scripts exécutés chaque jour
ls /etc/cron.weekly/     # chaque semaine
ls /etc/cron.hourly/     # chaque heure
```

Déposer un script exécutable (chapitre 9 : `chmod +x`) dans `/etc/cron.daily/` suffit à le faire tourner quotidiennement. Pratique et lisible.

### Une exécution unique : `at`

Là où cron **répète**, `at` exécute une commande **une seule fois**, à un moment futur :

```bash
echo "commande" | at 22:00       # lance la commande à 22h, une seule fois
at now + 1 hour                  # planifie pour dans une heure (mode interactif)
```

`at` n'est pas toujours installé ; au besoin, `sudo apt install at`.

### Les timers systemd (notion)

systemd propose une alternative moderne à cron : les **timers** (`.timer`). Ils sont plus puissants (meilleure journalisation via `journalctl`, gestion des tâches manquées…) mais plus verbeux à écrire. Pour débuter, retiens qu'ils **existent** et qu'on les rencontre de plus en plus ; cron reste parfaitement valable et plus simple pour commencer.

> **Orientation cyber / sécurité :** les tâches planifiées sont à double tranchant. Côté défense, elles automatisent la surveillance et les sauvegardes. Côté attaque, elles sont un **mécanisme de persistance** classique : un intrus ajoute une tâche cron pour relancer son code régulièrement. Lors d'un audit, **inspecter les crontabs** (`crontab -l`, les fichiers dans `/etc/cron.*` et `/var/spool/cron/`) fait partie des réflexes pour repérer une persistance suspecte.

## ❌ Erreur classique

```bash
# Éditer la crontab à la main au mauvais endroit
nano /var/spool/cron/...      # ❌ ne pas éditer directement les fichiers internes
crontab -e                    # ✅ toujours passer par crontab -e

# Utiliser un chemin relatif dans une tâche cron
0 8 * * * script.sh           # ❌ cron ne sait pas où il est ; PATH minimal
0 8 * * * /home/alice/script.sh   # ✅ TOUJOURS un chemin absolu

# Oublier de rendre le script exécutable
0 8 * * * /home/alice/backup.sh   # ❌ échoue si pas de droit x
chmod +x /home/alice/backup.sh    # ✅ (chapitre 9)

# Croire que la tâche tourne alors que la machine est éteinte
# cron a besoin que la machine soit ALLUMÉE à l'heure prévue
```

> **Le piège du chemin et de l'environnement :** une tâche cron s'exécute dans un environnement **minimal** (un `PATH` réduit, pas tes alias du chapitre 8). Une commande qui marche dans ton terminal peut échouer en cron si elle dépend de ton environnement. La parade : **utiliser des chemins absolus** partout dans tes scripts planifiés.

## Exercices

**Guidé :** Ouvre ta crontab avec `crontab -e` (choisis `nano` si on te le demande). Ajoute une ligne qui écrit la date dans un fichier toutes les minutes, à des fins de test : `* * * * * date >> /home/alice/cron-test.log` (**remplace `alice` par ton vrai nom d'utilisateur** — on met un chemin absolu, conformément à la règle ci-dessus). Enregistre, attends deux-trois minutes, puis lis `cron-test.log` : vois-tu plusieurs horodatages s'accumuler ? Retire ensuite la ligne avec `crontab -e` pour ne pas polluer.

**Autonome :** Écris en langage clair ce que feraient ces lignes cron, puis vérifie ton interprétation : `0 6 * * 1`, `*/10 * * * *`, `0 0 * * 0`. À quelle fréquence chacune s'exécute-t-elle ?

**Défi (orientation sécurité) :** Fais l'inventaire des tâches planifiées de ta machine. Affiche ta crontab (`crontab -l`), liste le contenu des dossiers `/etc/cron.daily/`, `/etc/cron.hourly/`, et regarde s'il existe des crontabs système (`cat /etc/crontab`). Sur une vraie investigation, pourquoi serait-il important de connaître **toutes** les tâches planifiées d'une machine ? Que chercherait un analyste là-dedans ?

## ✅ Tu sais maintenant…

- Pourquoi on **planifie** des tâches répétitives (sauvegardes, nettoyages, vérifications)
- Éditer et lire ta planification avec `crontab -e` et `crontab -l`
- Lire la **syntaxe cron** à cinq champs (minute, heure, jour, mois, jour de semaine)
- Déposer un script dans `/etc/cron.daily/` (et `.weekly`, `.hourly`)
- Planifier une exécution **unique** avec `at`, et que les **timers systemd** existent
- Le piège des **chemins relatifs** en cron (toujours des chemins absolus)
- Que les tâches planifiées sont un **mécanisme de persistance** à auditer en sécurité

---

> **🏁 CHECKPOINT 4 — Fin de la Partie 4**
>
> Tu sais désormais **piloter une machine en fonctionnement** : observer et contrôler les processus, gérer les services qui tournent en permanence, lire ce que le système raconte dans ses journaux, et automatiser des tâches dans le temps.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - retrouver le PID d'un programme et l'arrêter proprement (puis de force si besoin) ?
> - vérifier si un service tourne, le redémarrer, et le faire démarrer automatiquement au boot ?
> - expliquer la différence entre `systemctl start` et `systemctl enable` ?
> - suivre en direct les tentatives de connexion SSH avec `journalctl` ?
> - utiliser `dmesg` pour diagnostiquer un souci matériel ?
> - planifier un script pour qu'il tourne tous les jours à heure fixe ?
>
> Si oui, tu administres une machine vivante. Il est temps de l'**ouvrir sur le monde** : place à la **Partie 5 — Linux en réseau**.

---

---
---

# PARTIE 5 — Linux en réseau

Une machine isolée est rare. La plupart du temps, un système Linux communique : il sert des pages web, héberge des fichiers, ou s'administre à distance. Maintenant que tu comprends son fonctionnement interne, on l'ouvre sur le réseau. Tu vas apprendre à voir comment la machine communique, à t'y connecter à distance en sécurité, et à transférer des fichiers entre machines.

---

# Chapitre 17 — Les bases du réseau Linux

## Le minimum à savoir

### Le strict nécessaire de TCP/IP

Pas besoin d'être expert réseau pour administrer Linux, mais quelques notions sont indispensables :

- **Adresse IP** : l'adresse numérique d'une machine sur un réseau (ex. `192.168.1.10`). C'est son « numéro de téléphone ».
- **Masque de sous-réseau** : il définit quelles machines sont sur le **même** réseau local que toi.
- **Passerelle (gateway)** : la « porte de sortie » du réseau local vers le reste du monde (souvent ta box ou ton routeur).
- **Port** : sur une même machine, chaque service écoute sur un **port** numéroté (ex. 22 pour SSH, 80 pour le web, 443 pour le web sécurisé). Si l'IP est l'adresse de l'immeuble, le port est le numéro de l'appartement.
- **DNS** : le système qui traduit les noms (`exemple.com`) en adresses IP. C'est l'annuaire d'Internet.

### Voir sa configuration réseau : `ip`

La commande moderne pour tout ce qui touche au réseau est `ip` :

```bash
ip a             # affiche les interfaces et leurs adresses IP (a = address)
ip r             # affiche la table de routage, dont la passerelle (r = route)
```

`ip a` te montre tes **interfaces réseau** (carte filaire, Wi-Fi, interface locale `lo`…) et l'adresse IP de chacune. `ip r` te montre par où sortent tes paquets (notamment la ligne `default via ...` qui désigne ta passerelle).

### Tester la connectivité : `ping`

`ping` envoie de petits paquets à une machine pour vérifier qu'elle répond et mesurer le temps d'aller-retour :

```bash
ping 8.8.8.8             # teste la connectivité vers une IP (Ctrl + C pour arrêter)
ping exemple.com         # teste aussi la résolution DNS (nom → IP)
```

> **Réflexe de diagnostic :** si `ping 8.8.8.8` (une IP) fonctionne mais que `ping exemple.com` (un nom) échoue, ton problème vient probablement du **DNS**, pas de la connexion elle-même. Ce simple test isole déjà la cause.

## Très utile en pratique

### Voir les ports ouverts : `ss` (et le vieux `netstat`)

Quels services écoutent sur ta machine, et donc quelles « portes » sont ouvertes ? La réponse vient de `ss` :

```bash
ss -tulpn        # tous les ports en écoute, avec le programme associé
```

Décortiquons ces options très utilisées : `-t` (TCP), `-u` (UDP), `-l` (uniquement ce qui **écoute**, *listening*), `-p` (le **programme** qui écoute — nécessite souvent `sudo`), `-n` (afficher les **numéros** de port plutôt que les noms).

> **`ss` vs `netstat` :** tu croiseras souvent `netstat` dans d'anciens cours, scripts ou tutoriels. **`ss` est l'outil moderne recommandé** ; `netstat` est ancien et considéré comme déprécié, mais encore présent partout, donc utile à savoir lire. Sur les systèmes récents, `netstat` n'est même plus installé par défaut (il fait partie du paquet `net-tools`). Apprends `ss`, reconnais `netstat`.

> **Très utile en sécurité :** `ss -tulpn` révèle la **surface d'attaque locale** de la machine — chaque port en écoute est une porte potentielle. Côté défense, on vérifie que **seuls les services attendus** écoutent, et on ferme ou désactive le reste (lien avec le durcissement, chapitre 25). Un port inattendu en écoute est un signal à investiguer.

### Interroger le DNS : `dig` et `nslookup`

Pour traduire un nom en adresse IP (ou enquêter sur la configuration DNS d'un domaine) :

```bash
dig exemple.com          # interrogation DNS détaillée (paquet dnsutils)
nslookup exemple.com     # alternative plus simple à lire
```

`dig` n'est pas toujours installé : `sudo apt install dnsutils` (réflexe de la Partie 0).

### Télécharger et tester des services web : `curl` et `wget`

Deux outils pour parler à des serveurs web depuis le terminal :

```bash
curl https://exemple.com           # récupère et affiche le contenu d'une URL
curl -I https://exemple.com        # -I : seulement les en-têtes (code de réponse, serveur…)
wget https://exemple.com/fichier   # télécharge un fichier et l'enregistre sur le disque
```

> **À retenir :** `curl` sert surtout à **interroger/tester** un service (et afficher la réponse) ; `wget` sert surtout à **télécharger** un fichier. `curl -I` est un réflexe pratique pour vérifier rapidement qu'un site répond et avec quel code (200 = OK, 404 = absent, 500 = erreur serveur…).

### Suivre le chemin réseau : `traceroute` (notion)

`traceroute exemple.com` montre les étapes (les routeurs) par lesquelles passent tes paquets pour atteindre une destination. Utile pour localiser **où** une connexion se bloque. Outil à installer au besoin (`sudo apt install traceroute`), bon à connaître de nom.

## ❌ Erreur classique

```bash
# Utiliser ifconfig/netstat par habitude alors qu'ils ne sont plus là
ifconfig                 # ❌ souvent absent sur les systèmes récents
ip a                     # ✅ l'équivalent moderne
netstat -tulpn           # ❌ déprécié / absent par défaut
ss -tulpn                # ✅ l'équivalent moderne

# Oublier sudo pour voir le programme derrière un port
ss -tulpn                # le champ "programme" peut rester vide
sudo ss -tulpn           # ✅ pour voir quel processus écoute

# Conclure trop vite à une panne réseau
ping exemple.com         # échoue...
ping 8.8.8.8             # ✅ teste d'abord par IP : si ça marche, c'est le DNS

# Confondre curl et wget
wget https://api...      # télécharge un fichier au lieu d'afficher la réponse
curl https://api...      # ✅ affiche la réponse dans le terminal
```

## Exercices

**Guidé :** Affiche tes interfaces réseau avec `ip a` et repère ton adresse IP locale (souvent en `192.168.x.x` ou `10.x.x.x`). Affiche ensuite ta passerelle avec `ip r` (la ligne `default via ...`). Enfin, vérifie ta connectivité avec `ping -c 4 8.8.8.8` (le `-c 4` limite à 4 paquets).

**Autonome :** Liste les ports en écoute sur ta machine avec `sudo ss -tulpn`. Pour chaque ligne, identifie le port et, si possible, le programme. Le port 22 (SSH) est-il ouvert ? Reconnais-tu tous les services qui écoutent, ou certains te surprennent-ils ?

**Défi (orientation sécurité) :** Dresse l'inventaire réseau de ta machine comme le ferait un analyste. Enregistre dans un fichier (avec `tee`, chapitre 7) la sortie de `sudo ss -tulpn`. Pour chaque port en écoute, demande-toi : ce service doit-il **vraiment** tourner ? Doit-il être accessible depuis l'extérieur, ou seulement en local ? Cette réflexion est exactement celle du durcissement : **fermer ce qui n'a pas besoin d'être ouvert**.

## ✅ Tu sais maintenant…

- Les notions clés : **IP, masque, passerelle, port, DNS**
- Voir ta config réseau avec `ip a` (adresses) et `ip r` (routage/passerelle)
- Tester la connectivité avec `ping`, et isoler un problème **DNS** vs **réseau**
- Lister les ports en écoute avec **`ss -tulpn`** (la surface d'attaque locale)
- Que `ss` est l'outil **moderne** et `netstat` l'ancien **déprécié** (mais à savoir lire)
- Interroger le DNS (`dig`, `nslookup`) et tester un service web (`curl`, `curl -I`, `wget`)
- Que `traceroute` montre le chemin réseau vers une destination

---

# Chapitre 18 — SSH : se connecter à distance

## Le minimum à savoir

### Le principe : un terminal sur une machine distante

**SSH** (*Secure Shell*) est le protocole qui permet d'ouvrir un terminal sur une machine **distante**, à travers le réseau, de façon **chiffrée** (personne ne peut espionner la session). C'est l'outil fondamental de l'administration : la quasi-totalité des serveurs dans le monde se gèrent en SSH. Tout ce que tu as appris depuis le chapitre 1 s'applique à l'identique sur la machine distante — c'est juste le terminal qui est « ailleurs ».

Il y a deux côtés :

- Le **client SSH** (`ssh`) : sur ta machine, tu t'en sers pour te connecter.
- Le **serveur SSH** (`sshd`, le démon du chapitre 14) : sur la machine distante, il attend et accepte les connexions, sur le **port 22** par défaut.

### Se connecter : `ssh`

```bash
ssh alice@192.168.1.50       # se connecte en tant qu'alice sur la machine 192.168.1.50
ssh alice@serveur.exemple.com  # avec un nom de domaine
ssh -p 2222 alice@serveur    # -p pour préciser un port différent du 22
```

À la **première** connexion, SSH affiche l'**empreinte** (*fingerprint*) de la machine distante et te demande de confirmer. C'est une sécurité : tu vérifies que tu te connectes à la bonne machine, et non à un imposteur. Une fois acceptée, l'empreinte est mémorisée ; un changement futur déclenchera un avertissement.

Pour terminer une session distante, on tape simplement `exit` (ou `Ctrl + D`).

## Très utile en pratique

### L'authentification par clé : plus sûre que le mot de passe

Se connecter par mot de passe fonctionne, mais reste vulnérable (on peut le deviner, le forcer). La méthode professionnelle est l'**authentification par clé**, fondée sur une paire :

- une **clé privée**, qui reste **secrète** sur ta machine (à ne **jamais** partager) ;
- une **clé publique**, qu'on dépose sur les serveurs où l'on veut se connecter.

Le serveur vérifie que tu possèdes la clé privée correspondant à la clé publique qu'il connaît, sans qu'aucun secret ne circule. On génère sa paire de clés une fois :

```bash
ssh-keygen -t ed25519        # crée une paire de clés (algorithme moderne et sûr)
```

Cela crée deux fichiers dans `~/.ssh/` : `id_ed25519` (privée, à protéger) et `id_ed25519.pub` (publique, à diffuser). On copie ensuite la clé **publique** sur le serveur :

```bash
ssh-copy-id alice@serveur    # installe ta clé publique sur le serveur distant
```

Désormais, `ssh alice@serveur` te connecte **sans mot de passe**, de façon plus sûre.

> **Règle d'or des clés :** la clé **privée** ne quitte **jamais** ta machine et ne se partage **jamais**. Si quelqu'un l'obtient, il peut se faire passer pour toi. La clé **publique**, elle, peut être diffusée sans risque. Protège ta clé privée comme le mot de passe le plus important.

### Simplifier avec `~/.ssh/config`

Si tu te connectes souvent aux mêmes machines, tu peux leur donner des surnoms dans un fichier de configuration personnel :

```bash
# Dans ~/.ssh/config
Host monserveur
    HostName 192.168.1.50
    User alice
    Port 22
```

Tu n'as plus qu'à taper `ssh monserveur`. C'est plus court, moins source d'erreurs, et ça centralise tes accès.

### Durcir le serveur SSH (côté défense)

Le serveur SSH étant la porte d'entrée d'une machine, c'est une **cible privilégiée** des attaques (notamment les attaques par force brute du chapitre 4). Quelques réglages, dans `/etc/ssh/sshd_config`, réduisent fortement le risque. On les modifie **avec le réflexe du chapitre 6** (`.bak`, `sudoedit`, `diff`) :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
```

Les durcissements les plus courants :

- **`PermitRootLogin no`** : interdire la connexion directe en root (on se connecte en utilisateur normal, puis `sudo`). C'est l'un des réglages les plus importants.
- **`PasswordAuthentication no`** : n'autoriser que les clés, une fois celles-ci en place (supprime tout risque de force brute sur mot de passe).
- Éventuellement, changer le port par défaut pour réduire le bruit automatisé.

Après modification, on **recharge** le service (chapitre 14) pour appliquer :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérifier le changement
sudo systemctl restart ssh                               # 4. appliquer
```

> **⚠️ Prudence vitale en SSH distant :** ne désactive **jamais** ta seule méthode d'accès sans en avoir une autre qui fonctionne. Avant de couper l'authentification par mot de passe, **vérifie que ta clé fonctionne**. Avant de redémarrer `sshd` à distance, garde une session ouverte de secours. Une mauvaise manipulation peut te verrouiller dehors de ta propre machine.

> **Orientation cyber / SOC :** le durcissement SSH (pas de root, clés uniquement) est l'un des gestes défensifs les plus rentables. Et côté surveillance, suivre les tentatives de connexion (`journalctl -u ssh -f`, chapitre 15) permet de détecter une attaque en cours.

## ❌ Erreur classique

```bash
# Partager ou copier la mauvaise clé
cat ~/.ssh/id_ed25519        # ❌ JAMAIS : c'est la clé PRIVÉE, elle reste secrète
cat ~/.ssh/id_ed25519.pub    # ✅ la clé PUBLIQUE, celle qu'on diffuse

# Mauvaises permissions sur ~/.ssh (SSH refuse de fonctionner)
chmod 777 ~/.ssh             # ❌ SSH refusera d'utiliser des clés trop ouvertes
chmod 700 ~/.ssh             # ✅ dossier privé
chmod 600 ~/.ssh/id_ed25519  # ✅ clé privée lisible par toi seul

# Désactiver le mot de passe AVANT de tester la clé
# ❌ risque de se verrouiller dehors
# ✅ teste d'abord ssh par clé, PUIS désactive le mot de passe

# Redémarrer sshd à distance sans filet
sudo systemctl restart ssh   # ⚠️ garde une 2e session ouverte au cas où

# Ignorer un changement d'empreinte
# Un avertissement de changement de fingerprint peut signaler un vrai problème : ne pas l'ignorer aveuglément
```

## Exercices

**Guidé :** Génère ta paire de clés SSH avec `ssh-keygen -t ed25519` (accepte l'emplacement par défaut, choisis ou non une passphrase). Vérifie que deux fichiers ont été créés dans `~/.ssh/` avec `ls -l ~/.ssh/`. Identifie lequel est la clé privée et lequel est la publique. Quelles sont leurs permissions ?

**Autonome (si tu disposes d'une seconde machine ou d'une VM) :** Connecte-toi en SSH d'une machine à l'autre par mot de passe. Observe la demande de confirmation d'empreinte à la première connexion. Une fois connecté, lance `hostname` et `whoami` pour confirmer que tu es bien sur la machine distante. Termine avec `exit`.

**Défi (orientation sécurité, en lab) :** Sur une machine de test où tu as déjà un accès de secours, mets en place l'authentification par clé (`ssh-copy-id`), vérifie qu'elle fonctionne, puis prépare (sans forcément appliquer) les durcissements de `sshd_config` : `PermitRootLogin no` et `PasswordAuthentication no`. Avant tout `restart`, relis la règle d'or : as-tu un accès garanti si quelque chose tourne mal ? Décris la procédure prudente que tu suivrais.

## ✅ Tu sais maintenant…

- Que **SSH** ouvre un terminal **chiffré** sur une machine distante (port 22, démon `sshd`)
- Te connecter avec `ssh user@machine` (et `-p` pour un autre port), et l'importance de l'**empreinte**
- Mettre en place l'**authentification par clé** (`ssh-keygen`, `ssh-copy-id`), plus sûre que le mot de passe
- Que la clé **privée** ne se partage **jamais**, contrairement à la publique
- Simplifier tes accès avec `~/.ssh/config`
- **Durcir** le serveur SSH (`PermitRootLogin no`, `PasswordAuthentication no`) avec le réflexe `.bak`/`sudoedit`/`diff`
- La prudence vitale pour ne pas se verrouiller dehors lors d'un changement à distance

---

# Chapitre 19 — Transférer des fichiers

## Le minimum à savoir

### Déplacer des fichiers entre machines, en sécurité

Une fois connecté à distance, tu auras souvent besoin de **transférer des fichiers** : envoyer une configuration vers un serveur, récupérer des logs pour les analyser, déployer un script. Bonne nouvelle : ces transferts s'appuient sur SSH, donc ils sont **chiffrés** par défaut, et réutilisent les accès (clés, config) que tu viens de mettre en place.

### Copier un fichier : `scp`

`scp` (*secure copy*) copie un fichier vers ou depuis une machine distante, avec une syntaxe proche de `cp` :

```bash
scp fichier.txt alice@serveur:/home/alice/      # ENVOIE le fichier vers le serveur
scp alice@serveur:/var/log/app.log .            # RÉCUPÈRE un fichier distant ICI (.)
scp -r dossier/ alice@serveur:/home/alice/      # -r pour un dossier entier (comme cp)
```

La logique : `scp <source> <destination>`, où une machine distante s'écrit `user@machine:/chemin`. Le `:` sépare la machine du chemin. C'est l'outil le plus simple pour un transfert ponctuel.

> **Note de culture :** sur les versions récentes d'OpenSSH, `scp` s'appuie en interne sur SFTP — pour toi, la syntaxe ne change pas. Retiens simplement le partage des rôles : **`scp` pour une copie ponctuelle**, **`rsync` pour les sauvegardes et synchronisations** (vu juste après).

## Très utile en pratique

### Synchroniser intelligemment : `rsync`

Pour des transferts plus sérieux (gros dossiers, sauvegardes, synchronisations répétées), `rsync` est bien plus efficace que `scp` : il ne transfère que ce qui a **changé**, peut reprendre un transfert interrompu, et préserve les attributs des fichiers.

```bash
rsync -av dossier/ alice@serveur:/sauvegarde/    # synchronise dossier/ vers le serveur
rsync -av alice@serveur:/data/ ./data/           # synchronise depuis le serveur vers ici
```

Les options de base : `-a` (*archive* : préserve permissions, dates, liens…) et `-v` (*verbose* : affiche ce qui se passe). Une option de sécurité précieuse pour s'entraîner :

```bash
rsync -av --dry-run dossier/ alice@serveur:/sauvegarde/   # SIMULE sans rien transférer
```

> **Très utile en pratique :** `--dry-run` te montre **exactement ce qui serait transféré** sans rien faire. C'est le pendant réseau de la prudence des chapitres précédents : on vérifie avant d'agir. À utiliser systématiquement avant un gros `rsync`.

> **Attention au slash final dans `rsync` :** `rsync dossier/` (avec `/`) copie le **contenu** du dossier ; `rsync dossier` (sans `/`) copie le **dossier lui-même** dans la destination. Cette subtilité change le résultat — d'où l'intérêt du `--dry-run` pour vérifier.

### Une session interactive : `sftp`

`sftp` ouvre une session interactive de transfert (à la manière d'un FTP, mais sécurisé), où l'on navigue et transfère avec des commandes dédiées (`put` pour envoyer, `get` pour récupérer) :

```bash
sftp alice@serveur       # ouvre une session ; puis: put fichier, get fichier, ls, cd, bye
```

Pratique quand on veut explorer l'arborescence distante avant de choisir quoi transférer. Pour débuter, `scp` (ponctuel) et `rsync` (synchronisation) couvrent l'essentiel des besoins.

## ❌ Erreur classique

```bash
# Oublier le : qui sépare machine et chemin
scp fichier.txt alice@serveur/home/alice    # ❌ sans :, scp ne comprend pas
scp fichier.txt alice@serveur:/home/alice   # ✅ le : est obligatoire

# Oublier -r pour un dossier
scp dossier/ alice@serveur:/tmp/            # ❌ refusé (c'est un dossier)
scp -r dossier/ alice@serveur:/tmp/         # ✅

# Lancer un gros rsync sans simulation
rsync -av gros-dossier/ serveur:/dest/      # ❌ et si la cible/le slash est faux ?
rsync -av --dry-run gros-dossier/ serveur:/dest/   # ✅ simule d'abord

# Se tromper de sens (source/destination inversées)
scp serveur:/data/important .               # récupère DEPUIS le serveur
scp important serveur:/data/                # envoie VERS le serveur — vérifie le sens !
```

## Exercices

**Guidé :** Crée un fichier de test localement. Si tu disposes d'un accès SSH à une autre machine, envoie-le avec `scp fichier.txt user@machine:/tmp/`, puis connecte-toi en SSH et vérifie qu'il est bien arrivé dans `/tmp/`. Sinon, entraîne-toi à la **syntaxe** : écris (sans l'exécuter) la commande qui récupérerait `/var/log/syslog` d'un serveur vers ton dossier courant.

**Autonome :** Crée un dossier avec quelques fichiers. Utilise `rsync -av --dry-run` vers une destination (locale ou distante) et lis attentivement ce que la simulation annonce. Puis, si tu veux, lance le vrai transfert sans `--dry-run` et compare.

**Défi (orientation SOC) :** Imagine que tu doives **récupérer les logs** d'un serveur compromis pour les analyser sur ta machine, sans rien modifier sur le serveur. Quelle commande utiliserais-tu, et pourquoi privilégier `rsync` (préservation des dates et attributs, qui sont des preuves) plutôt qu'une simple copie manuelle ? Écris la commande complète.

## ✅ Tu sais maintenant…

- Que les transferts de fichiers s'appuient sur SSH et sont donc **chiffrés**
- Copier ponctuellement avec `scp` (et `-r` pour les dossiers), syntaxe `user@machine:/chemin`
- **Synchroniser** efficacement avec `rsync -av` (ne transfère que les changements)
- Utiliser `rsync --dry-run` pour **simuler** avant d'agir, et l'importance du slash final
- Explorer et transférer en interactif avec `sftp` (`put`, `get`)
- Faire attention au **sens** source → destination

---

> **🏁 CHECKPOINT 5 — Fin de la Partie 5**
>
> Ta machine n'est plus isolée : tu sais inspecter sa configuration réseau, voir ce qui écoute, t'y connecter à distance en sécurité et y transférer des fichiers. Tu peux désormais administrer une machine **que tu n'as pas physiquement devant toi** — la réalité de la quasi-totalité des serveurs.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - afficher ton adresse IP, ta passerelle, et tester ta connectivité ?
> - lister les ports en écoute et expliquer pourquoi c'est un enjeu de sécurité ?
> - te connecter en SSH et mettre en place une authentification par clé ?
> - citer deux durcissements importants du serveur SSH ?
> - transférer un dossier avec `rsync` en simulant d'abord ?
>
> Si oui, tu maîtrises Linux en réseau. Passons à l'**entretien du système sur la durée** : place à la **Partie 6 — Entretenir le système**.

---

---
---

# PARTIE 6 — Entretenir le système

Un système qu'on administre se maintient dans le temps : installer et mettre à jour des logiciels, surveiller l'espace disque, archiver des données, et sauvegarder pour ne rien perdre. Ce sont les gestes du quotidien d'un administrateur. Tu vas réutiliser beaucoup de ce que tu sais déjà (permissions, redirections, planification) au service de la maintenance.

---

# Chapitre 20 — Gérer les paquets et logiciels

## Le minimum à savoir

### Qu'est-ce qu'un gestionnaire de paquets ?

Sous Linux, on n'installe presque jamais un logiciel en téléchargeant un fichier sur un site web. À la place, un **gestionnaire de paquets** récupère les logiciels depuis des **dépôts** (des serveurs officiels et vérifiés), gère automatiquement leurs **dépendances** (les autres logiciels nécessaires), et permet de tout mettre à jour d'un coup. C'est plus simple, plus sûr (les paquets sont signés et vérifiés), et plus facile à maintenir.

Chaque famille de distributions a son gestionnaire :

- **Debian / Ubuntu** : `apt` (c'est celui de ce cours)
- **RHEL / CentOS / Fedora** : `dnf` (ou son ancêtre `yum`)
- **Arch** : `pacman`

### Les commandes apt essentielles

Sur Debian/Ubuntu, tout passe par `apt`, avec une poignée de sous-commandes très régulières (toutes celles qui modifient le système demandent `sudo`) :

```bash
sudo apt update              # met à jour la LISTE des paquets disponibles
sudo apt upgrade             # installe les mises à jour des paquets déjà présents
sudo apt install nom         # installe un paquet
sudo apt remove nom          # désinstalle un paquet (garde sa configuration)
sudo apt purge nom           # désinstalle ET supprime sa configuration
apt search motclé            # cherche un paquet par mot-clé (sans sudo)
apt show nom                 # affiche les détails d'un paquet
```

> **La distinction `update` / `upgrade` est essentielle et souvent confondue :** `update` rafraîchit seulement le **catalogue** (la liste de ce qui existe et des versions), il n'installe rien. `upgrade` applique réellement les mises à jour. **On fait toujours `update` avant `upgrade`** (ou avant un `install`), pour travailler sur un catalogue à jour. C'est exactement le réflexe `sudo apt update` qu'on a introduit dès la Partie 0.

### Mettre à jour son système

L'enchaînement de maintenance le plus courant, à faire régulièrement :

```bash
sudo apt update && sudo apt upgrade      # rafraîchit le catalogue PUIS met à jour
```

Le `&&` enchaîne les deux commandes : la seconde ne s'exécute que si la première a réussi.

> **À connaître — `apt full-upgrade` :** il existe aussi `sudo apt full-upgrade`, qui peut **installer ou supprimer** des paquets pour résoudre des mises à jour plus complexes (changements de dépendances). Pour débuter, retiens surtout `apt upgrade`. Utilise `full-upgrade` avec prudence, en **lisant bien ce qu'APT propose de supprimer** avant de confirmer.

> **Très utile en sécurité :** maintenir un système à jour fait partie des mesures défensives les plus **rentables** : beaucoup d'attaques exploitent des vulnérabilités **déjà connues et corrigées**. Un système non mis à jour laisse ces portes ouvertes. C'est le premier point de toute checklist de durcissement (chapitre 25).

## Très utile en pratique

### Sous le capot : `dpkg`

`apt` s'appuie sur un outil de plus bas niveau, `dpkg`, qui gère les paquets individuellement. Utile surtout pour interroger ce qui est installé :

```bash
dpkg -l                      # liste TOUS les paquets installés
dpkg -l | grep nginx         # cherche si nginx est installé (pipe du chapitre 7)
dpkg -L nom                  # liste les fichiers installés par un paquet
```

### Installer les outils de ce cours

Le moment est venu d'installer, **maintenant que tu en comprends le sens**, les outils mentionnés au fil des chapitres et regroupés dès la Partie 0. On les sépare en deux lots, ce qui clarifie leur rôle :

```bash
sudo apt update
# Lot 1 — outils d'apprentissage et d'administration
sudo apt install tree htop curl wget dnsutils traceroute net-tools rsync
# Lot 2 — outils de durcissement (on les configurera au chapitre 25)
sudo apt install ufw fail2ban
```

> **Lab vs production :** sur une machine de **lab**, tu peux installer ce lot d'un coup pour suivre le cours confortablement. Sur un **serveur réel**, installe uniquement les paquets nécessaires au besoin immédiat — chaque logiciel ajouté agrandit la surface d'attaque et la charge de maintenance. Les outils de sécurité `ufw` et `fail2ban` (lot 2) ne servent vraiment qu'une fois **configurés** : on s'en occupera au chapitre 25.

Petit rappel de ce que chacun apporte, et où on l'a croisé :

| Paquet | Outil(s) | Vu au chapitre |
|--------|----------|----------------|
| `tree` | affichage en arbre | 2 |
| `htop` | moniteur de processus | 13 |
| `curl`, `wget` | requêtes et téléchargements web | 17 |
| `dnsutils` | `dig`, `nslookup` | 17 |
| `traceroute` | chemin réseau | 17 |
| `net-tools` | `netstat`, `ifconfig` (anciens) | 17 |
| `rsync` | synchronisation/transfert | 19, 23 |
| `ufw` | pare-feu simple | 25 |
| `fail2ban` | protection contre la force brute | 25 |

> **Principe à garder :** on n'installe pas tout « au cas où » sur un vrai serveur. Sur une machine d'apprentissage, ces deux lots sont pratiques ; sur un serveur de production, on installe **uniquement le nécessaire**.

### Faire le ménage

Avec le temps, des paquets deviennent inutiles. Pour récupérer de l'espace proprement :

```bash
sudo apt autoremove          # supprime les dépendances devenues inutiles
sudo apt clean               # vide le cache des paquets téléchargés
```

## ❌ Erreur classique

```bash
# Faire upgrade sans update d'abord
sudo apt upgrade             # ❌ travaille sur un catalogue peut-être périmé
sudo apt update && sudo apt upgrade   # ✅ catalogue à jour, puis mise à jour

# Oublier sudo
apt install htop             # ❌ "Permission denied" / "are you root?"
sudo apt install htop        # ✅

# Confondre remove et purge
sudo apt remove apache2      # garde les fichiers de config
sudo apt purge apache2       # ✅ si tu veux TOUT supprimer, config comprise

# Installer des logiciels hors des dépôts sans réfléchir
# ❌ télécharger un .deb au hasard sur Internet contourne les vérifications
# ✅ privilégier les dépôts officiels ; vérifier la source si exception

# Ignorer les mises à jour de sécurité pendant des mois
# ❌ c'est la cause n°1 d'intrusions évitables
```

## Exercices

**Guidé :** Rafraîchis le catalogue avec `sudo apt update` et lis le résumé (combien de paquets peuvent être mis à jour ?). Cherche ensuite un outil avec `apt search`, par exemple `apt search htop`, puis affiche ses détails avec `apt show htop`. Enfin, installe-le avec `sudo apt install htop` et lance-le.

**Autonome :** Liste les paquets installés avec `dpkg -l` et compte-les (`dpkg -l | wc -l`, en gardant en tête que les premières lignes sont un en-tête). Cherche si quelques outils précis sont présents : `dpkg -l | grep -E "ssh|curl|rsync"`. Lesquels sont installés ?

**Défi (orientation sécurité) :** Vérifie l'état des mises à jour de sécurité de ta machine. Lance `sudo apt update`, puis `apt list --upgradable` pour voir ce qui peut être mis à jour. Combien de paquets sont concernés ? Sur un vrai système, pourquoi appliquer ces mises à jour est-il considéré comme la mesure de sécurité prioritaire ? Applique-les avec `sudo apt upgrade`.

## ✅ Tu sais maintenant…

- Ce qu'est un **gestionnaire de paquets**, des **dépôts** et des **dépendances**
- Les familles : `apt` (Debian/Ubuntu), `dnf`/`yum` (RHEL/Fedora), `pacman` (Arch)
- Les commandes `apt` clés : `update`, `upgrade`, `install`, `remove`, `purge`, `search`, `show`
- La distinction **`update`** (catalogue) vs **`upgrade`** (vraies mises à jour), et l'enchaînement `update && upgrade`
- Que **maintenir à jour** est la mesure de sécurité la plus efficace
- Interroger les paquets installés avec `dpkg -l`
- Faire le ménage avec `autoremove` et `clean`

---

# Chapitre 21 — Stockage et espace disque

## Le minimum à savoir

### Comprendre les niveaux : disque, partition, système de fichiers, point de montage

Le stockage sous Linux se comprend par couches, qu'il faut distinguer pour ne pas se perdre :

- Un **disque** physique (ou virtuel) : le matériel, par exemple `/dev/sda`.
- Une **partition** : une division du disque, par exemple `/dev/sda1`. Un disque peut être découpé en plusieurs partitions.
- Un **système de fichiers** : la façon dont les données sont organisées **dans** une partition (ext4, xfs…). C'est ce qui transforme un espace brut en quelque chose qui contient des fichiers.
- Un **point de montage** : l'**endroit dans l'arborescence** (chapitre 2) où ce système de fichiers devient accessible. C'est le concept clé : sous Linux, un disque n'apparaît pas comme « lecteur D: », il est **« monté »** à un endroit de l'arbre unique, par exemple `/` ou `/home` ou `/mnt/usb`.

> **L'idée à retenir :** sous Linux, on ne « voit » pas les disques séparément ; on les **rattache** (monte) à des dossiers de l'arborescence unique. Ouvrir un dossier peut donc, en réalité, accéder à un autre disque — de façon totalement transparente.

### Voir l'espace disque : `df`

`df` (*disk free*) montre l'espace **utilisé et disponible** sur chaque système de fichiers monté :

```bash
df -h            # -h = tailles lisibles (Go, Mo) ; vue d'ensemble de l'espace
```

Chaque ligne montre un système de fichiers, sa taille, l'espace utilisé, l'espace libre, et son **point de montage**. C'est le premier réflexe quand on se demande « est-ce que mon disque est plein ? ».

### Voir ce qui prend de la place : `du`

Là où `df` regarde les disques globalement, `du` (*disk usage*) mesure la taille **des fichiers et dossiers** :

```bash
du -sh dossier/          # -s = total (summary), -h = lisible : taille totale du dossier
du -h --max-depth=1 /var # taille de chaque sous-dossier de /var, un niveau
```

> **La confusion classique `df` vs `du` :** `df` répond « combien d'espace reste-t-il **sur le disque** ? » (vue globale, par système de fichiers). `du` répond « combien pèse **ce dossier** ? » (vue détaillée, par fichier). Quand un disque se remplit, on utilise `df` pour le **constater**, puis `du` pour **trouver le coupable**.

## Très utile en pratique

### Trouver ce qui remplit le disque

Le combo gagnant quand `df -h` annonce un disque presque plein : descendre avec `du` pour localiser les gros dossiers, en triant (chapitre 4) :

```bash
sudo du -h --max-depth=1 / | sort -rh | head    # les plus gros dossiers à la racine
```

Ici : `du` mesure chaque dossier de premier niveau, `sort -rh` trie par taille décroissante (`-r` inverse, `-h` comprend les tailles lisibles), `head` garde le haut du classement. On répète ensuite dans le dossier coupable pour affiner. C'est l'enquête type « où est passé mon espace ? ».

### Voir les disques et partitions : `lsblk`

`lsblk` (*list block devices*) affiche les disques et leurs partitions sous forme d'arbre — la vue « matériel » du stockage :

```bash
lsblk            # disques, partitions, tailles et points de montage
```

C'est l'outil idéal pour **observer** la structure de stockage sans rien risquer : quels disques existent, comment ils sont découpés, et où chaque partition est montée.

### Voir précisément ce qui est monté : `findmnt`

`findmnt` affiche la liste des systèmes de fichiers montés, joliment présentée en arbre, avec leur source et leurs options :

```bash
findmnt          # arbre clair de tous les points de montage
findmnt /home    # info sur un point de montage précis
```

> **Très utile en pratique :** `lsblk` (les disques) et `findmnt` (les montages) sont tes deux outils d'**observation** du stockage. Ils ne modifient rien, et te donnent une vue complète et sûre de la situation. Prends le réflexe de les consulter **avant** toute action.

### `/etc/fstab` : les montages permanents

Comment le système sait-il quels disques monter, et où, à chaque démarrage ? Grâce au fichier **`/etc/fstab`** (*file systems table*). Chaque ligne y décrit un système de fichiers et son point de montage permanent.

```bash
cat /etc/fstab           # lire la table des montages permanents (lecture sans risque)
```

> **À ton niveau : lire, comprendre — pas modifier.** Apprends d'abord à **lire** `/etc/fstab` pour comprendre comment ta machine est organisée. Le **modifier** est une opération sensible : une erreur peut empêcher la machine de démarrer correctement. Si tu dois un jour y toucher, applique le réflexe du chapitre 6 (copie `.bak` d'abord) et procède avec une grande prudence.

### Monter et démonter : `mount` / `umount` (avec prudence)

Pour rattacher temporairement un système de fichiers (une clé USB, un partage réseau) à un dossier, on utilise `mount` ; pour le détacher, `umount`. Ce sont des opérations **privilégiées** et **sensibles**.

```bash
sudo mount /dev/sdb1 /mnt/usb        # monte une partition sur /mnt/usb (montage temporaire)
sudo umount /mnt/usb                 # démonte proprement
```

> **⚠️ Prudence (rappel de la Partie 0) :** `mount` et `umount` figurent parmi les commandes sensibles. Démonter un disque en cours d'utilisation, ou se tromper de périphérique, peut perturber l'accès aux données ou provoquer des pertes. **Pour un débutant, on commence par observer** avec `lsblk`, `df` et `findmnt` ; on ne monte/démonte qu'en sachant exactement quel périphérique on manipule, idéalement en lab. Distinction utile : un montage par `mount` est **temporaire** (perdu au redémarrage) ; un montage **permanent** passe par `/etc/fstab`.

### La mémoire vive : `free`

Au passage, pour la mémoire (RAM), qui n'est pas du stockage disque mais qu'on surveille de la même façon :

```bash
free -h          # mémoire totale, utilisée, libre, et swap (en tailles lisibles)
```

## ❌ Erreur classique

```bash
# Confondre df et du
df -h dossier/           # ❌ df raisonne par système de fichiers, pas par dossier
du -sh dossier/          # ✅ du pour la taille d'un dossier
df -h                    # ✅ df pour l'espace global

# Oublier -h et lire des nombres bruts illisibles
df                       # tailles en blocs, peu parlant
df -h                    # ✅ Go/Mo lisibles

# Modifier /etc/fstab sans sauvegarde ni précaution
sudoedit /etc/fstab      # ⚠️ une erreur ici peut empêcher le boot
sudo cp /etc/fstab /etc/fstab.bak   # ✅ toujours un .bak d'abord (chapitre 6)

# Démonter un disque occupé
sudo umount /mnt/usb     # ❌ "target is busy" si un fichier y est ouvert
# ✅ ferme ce qui l'utilise, puis démonte ; observe d'abord avec findmnt

# Se tromper de périphérique avec mount
sudo mount /dev/sda /mnt # ❌ vérifie TOUJOURS avec lsblk avant de monter
```

## Exercices

**Guidé :** Affiche l'espace disque global avec `df -h`. Repère le système de fichiers monté sur `/` : quelle proportion est utilisée ? Ensuite, mesure la taille de ton dossier personnel avec `du -sh ~`. Compare : ton dossier représente-t-il une grande part de l'espace utilisé ?

**Autonome :** Observe la structure de stockage de ta machine avec `lsblk`, puis avec `findmnt`. Combien de disques/partitions vois-tu ? Où est monté chacun ? Enfin, lis `/etc/fstab` avec `cat` et essaie de faire le lien entre ce fichier et ce que `findmnt` t'a montré.

**Défi :** Mène l'enquête « où est passé mon espace ? ». Pars de `df -h` pour repérer le système de fichiers le plus rempli. Puis, avec `sudo du -h --max-depth=1 / | sort -rh | head`, identifie les plus gros dossiers à la racine. Descends d'un niveau dans le coupable et répète, jusqu'à localiser précisément ce qui occupe le plus d'espace. Quel dossier as-tu trouvé ?

## ✅ Tu sais maintenant…

- Distinguer **disque**, **partition**, **système de fichiers** et **point de montage**
- Que Linux **monte** les disques dans son arborescence unique (pas de « lecteur D: »)
- Voir l'espace global avec `df -h` et la taille des dossiers avec `du -sh`
- La distinction **`df`** (espace du disque) vs **`du`** (taille d'un dossier), et l'enquête `du | sort -rh | head`
- **Observer** le stockage sans risque avec `lsblk` (disques) et `findmnt` (montages)
- Lire `/etc/fstab` pour comprendre les montages permanents (sans le modifier à la légère)
- Que `mount`/`umount` sont **sensibles** : on observe d'abord, on agit en connaissant le périphérique
- Surveiller la mémoire avec `free -h`

---

# Chapitre 22 — Archives et compression

## Le minimum à savoir

### Archiver ≠ compresser

Deux opérations distinctes, qu'on combine souvent :

- **Archiver**, c'est **regrouper** plusieurs fichiers et dossiers en un seul fichier (sans forcément réduire la taille). L'outil historique est `tar`, qui produit un fichier `.tar` (une « archive »).
- **Compresser**, c'est **réduire la taille** des données. Les outils courants sont `gzip` (`.gz`), et d'autres comme `xz` ou `bzip2`.

Le plus souvent, on fait les deux d'un coup : on regroupe avec `tar`, et on compresse au passage, ce qui donne un `.tar.gz` (parfois écrit `.tgz`). C'est le format d'archive le plus répandu sous Linux.

### Créer et extraire une archive : `tar`

`tar` a une réputation de syntaxe intimidante, mais deux combinaisons couvrent presque tout :

```bash
tar -czvf archive.tar.gz dossier/    # CRÉER une archive compressée d'un dossier
tar -xzvf archive.tar.gz             # EXTRAIRE une archive compressée
```

Décortiquons les options (les mêmes lettres dans les deux cas, sauf la première) :

- `c` = *create* (créer) / `x` = *extract* (extraire)
- `z` = compresser/décompresser avec gzip
- `v` = *verbose* (affiche les fichiers traités)
- `f` = *file* (le nom du fichier d'archive suit) — **toujours en dernier**, juste avant le nom

> **Moyen mnémotechnique :** pour **créer**, pense « **c**reate **z**ip **v**erbose **f**ile » → `czvf`. Pour **extraire**, remplace le `c` par `x` → `xzvf`. Avec ces deux-là, tu gères l'immense majorité des archives. Le `f` est toujours collé au nom de l'archive.

Pour juste **regarder** le contenu d'une archive sans l'extraire :

```bash
tar -tzvf archive.tar.gz             # t = list (lister le contenu)
```

## Très utile en pratique

### Compresser un fichier seul : `gzip`

Pour compresser un fichier unique (sans archive) :

```bash
gzip gros-fichier.log        # crée gros-fichier.log.gz et SUPPRIME l'original
gunzip gros-fichier.log.gz   # décompresse (récupère l'original)
zcat fichier.log.gz          # lire un fichier compressé SANS le décompresser
```

> **Très utile en pratique :** tu te souviens des logs archivés du chapitre 15 (`auth.log.2.gz`) ? C'est exactement du gzip. `zcat`, `zless` et `zgrep` permettent de **lire et chercher dans les logs compressés sans les décompresser** — précieux pour fouiller d'anciens journaux lors d'une investigation.

### Le format zip : `zip` / `unzip`

Pour échanger avec des systèmes Windows, le format `.zip` est plus universel :

```bash
zip -r archive.zip dossier/  # créer un zip d'un dossier (-r pour le contenu)
unzip archive.zip            # extraire un zip
```

`zip`/`unzip` ne sont pas toujours installés (`sudo apt install zip unzip`).

## ❌ Erreur classique

```bash
# Mettre le nom de l'archive au mauvais endroit (f doit précéder le nom)
tar -cfzv dossier/ archive.tar.gz    # ❌ ordre des options cassé
tar -czvf archive.tar.gz dossier/    # ✅ f juste avant le nom de l'archive

# Extraire sans savoir où ça va se déverser
tar -xzvf archive.tar.gz             # extrait dans le dossier COURANT
pwd                                  # ✅ vérifie où tu es avant d'extraire

# Oublier que gzip supprime l'original
gzip rapport.log                     # rapport.log disparaît, devient rapport.log.gz
gzip -k rapport.log                  # ✅ -k garde l'original (keep)

# Décompresser un gros log juste pour le lire
gunzip auth.log.1.gz                 # ❌ inutile et encombrant
zcat auth.log.1.gz | grep "Failed"   # ✅ lire/chercher sans décompresser
```

## Exercices

**Guidé :** Crée un dossier avec quelques fichiers. Archive-le et compresse-le en une commande : `tar -czvf sauvegarde.tar.gz mondossier/`. Observe la liste défiler (grâce au `v`). Vérifie le contenu sans extraire avec `tar -tzvf sauvegarde.tar.gz`, puis extrais-le dans un autre dossier de test.

**Autonome :** Prends un fichier texte assez gros (par exemple une copie d'un log). Compresse-le avec `gzip -k` (en gardant l'original), puis compare les tailles avec `ls -lh` : quel gain de place obtiens-tu ? Lis ensuite le fichier compressé avec `zcat` sans le décompresser.

**Défi (orientation admin/SOC) :** Prépare une « collecte » de logs comme pour une investigation. Archive et compresse en une fois le contenu de `/var/log` (ce qui est lisible) dans un fichier horodaté : `sudo tar -czvf logs-$(date +%F).tar.gz /var/log/ 2>/dev/null`. Le `$(date +%F)` insère la date du jour dans le nom (tu reverras cette technique en Bash, chapitre 26). Vérifie l'archive créée et sa taille. Pourquoi horodater le nom d'une archive de logs est-il une bonne pratique ?

## ✅ Tu sais maintenant…

- La différence entre **archiver** (regrouper, `tar`) et **compresser** (réduire, `gzip`)
- Créer une archive compressée avec `tar -czvf` et l'extraire avec `tar -xzvf` (le `f` avant le nom)
- Lister le contenu d'une archive sans extraire (`tar -tzvf`)
- Compresser un fichier seul (`gzip`, `-k` pour garder l'original)
- **Lire/chercher dans un fichier compressé** sans le décompresser (`zcat`, `zgrep`)
- Utiliser le format `.zip` (`zip -r`, `unzip`) pour l'échange avec Windows

---

# Chapitre 23 — Sauvegardes

## Le minimum à savoir

### Pourquoi sauvegarder : la question n'est pas « si » mais « quand »

Un disque tombe en panne, un fichier est supprimé par erreur (`rm`, chapitre 5 !), une attaque chiffre les données… Tôt ou tard, **on perd des données**. La seule protection est la **sauvegarde** : une copie, ailleurs, qu'on peut restaurer. Ce n'est pas optionnel en administration ; c'est une responsabilité fondamentale.

### La règle 3-2-1

La référence en matière de sauvegarde tient en trois chiffres :

- **3** copies des données (l'originale + 2 sauvegardes)
- **2** supports différents (par exemple disque interne + disque externe)
- **1** copie hors site (ailleurs physiquement, pour survivre à un incendie, un vol, une attaque)

Pour débuter, retiens l'esprit : **une sauvegarde sur le même disque que l'original ne protège de presque rien.** Une vraie sauvegarde est ailleurs.

### Sauvegarde complète vs incrémentale

- Une sauvegarde **complète** copie tout, à chaque fois : simple, mais lourde et lente.
- Une sauvegarde **incrémentale** ne copie que ce qui a **changé** depuis la dernière fois : rapide et économe. C'est exactement ce que fait `rsync` (chapitre 19), ce qui en fait un excellent outil de sauvegarde.

## Très utile en pratique

### Sauvegarder avec `rsync`

`rsync` (vu au chapitre 19) est idéal : il ne copie que les changements, préserve les attributs, et fonctionne aussi bien en local que vers une machine distante.

```bash
# Sauvegarde locale vers un disque externe monté
rsync -av --delete ~/documents/ /mnt/backup/documents/

# Sauvegarde vers un serveur distant (à travers SSH, chapitre 18)
rsync -av ~/documents/ alice@serveur:/sauvegardes/documents/
```

L'option `--delete` rend la sauvegarde **identique** à la source (elle supprime côté sauvegarde ce qui a disparu côté source). Puissante, donc à manier avec soin :

> **⚠️ Prudence avec `--delete` :** combinée à une erreur de chemin, elle peut supprimer des fichiers de ta sauvegarde. **Teste toujours avec `--dry-run` d'abord** (chapitre 19) : `rsync -av --delete --dry-run ...`. C'est le même réflexe de prudence qui traverse tout le cours.

### Sauvegarder avec `tar` (archive datée)

Pour une sauvegarde ponctuelle sous forme d'archive unique (facile à stocker et à dater) :

```bash
tar -czvf backup-$(date +%F).tar.gz ~/documents/    # archive horodatée du jour
```

Le `$(date +%F)` insère la date (format `2025-01-10`) dans le nom : tu obtiens un historique clair de tes sauvegardes.

### Planifier les sauvegardes

Une sauvegarde n'a de valeur que si elle est **régulière**. On combine donc ce chapitre avec la planification du chapitre 16. Un petit script de sauvegarde, déposé en cron, et la machine se sauvegarde toute seule chaque nuit :

```bash
# Exemple de ligne crontab : sauvegarde chaque jour à 2h30
30 2 * * * /home/alice/scripts/sauvegarde.sh
```

> Souviens-toi du piège du chapitre 16 : dans un script planifié, utilise des **chemins absolus**, car cron s'exécute dans un environnement minimal.

### Le point le plus oublié : tester la restauration

**Une sauvegarde qu'on n'a jamais testée n'est pas une sauvegarde.** Beaucoup découvrent, le jour fatidique, que leurs sauvegardes étaient vides, corrompues ou incomplètes. Le réflexe professionnel : **restaurer régulièrement** un fichier au hasard pour vérifier que ça fonctionne.

```bash
# Vérifier qu'on peut bien extraire une archive de sauvegarde
tar -tzvf backup-2025-01-10.tar.gz | head     # le contenu est-il bien là ?
# Puis tester une vraie extraction dans un dossier temporaire
mkdir /tmp/test-restore && tar -xzvf backup-2025-01-10.tar.gz -C /tmp/test-restore
```

> **Très utile en sécurité :** face à une attaque par rançongiciel (qui chiffre les données), des sauvegardes **hors ligne, testées et régulières** sont souvent la seule façon de tout récupérer sans céder. C'est une pièce maîtresse de la résilience défensive.

## ❌ Erreur classique

```bash
# Sauvegarder sur le même disque que l'original
rsync -av ~/data/ /autre-dossier-du-meme-disque/   # ❌ le disque meurt = tout est perdu
rsync -av ~/data/ /mnt/disque-externe/             # ✅ support différent

# Utiliser --delete sans simuler
rsync -av --delete ~/data/ /mnt/backup/            # ❌ une erreur de chemin = perte
rsync -av --delete --dry-run ~/data/ /mnt/backup/  # ✅ simuler d'abord

# Ne jamais tester la restauration
# ❌ découvrir le jour J que la sauvegarde était inutilisable
tar -tzvf backup.tar.gz                            # ✅ vérifier régulièrement

# Croire qu'une copie unique suffit
# ❌ une seule copie n'est pas une stratégie : pense 3-2-1
```

## Exercices

**Guidé :** Crée un dossier `~/precieux/` avec quelques fichiers. Réalise une première sauvegarde complète vers un autre dossier avec `rsync -av ~/precieux/ ~/sauvegarde-precieux/`. Modifie ensuite un fichier de `~/precieux/`, relance le même `rsync`, et observe : seul le fichier modifié est transféré (c'est l'aspect incrémental).

**Autonome :** Crée une archive de sauvegarde horodatée de ton dossier `~/precieux/` avec `tar -czvf backup-$(date +%F).tar.gz ~/precieux/`. Vérifie son contenu sans l'extraire. Puis **teste la restauration** : extrais l'archive dans `/tmp/restore-test/` et confirme que tes fichiers sont bien là, intacts.

**Défi :** Conçois (sur le papier ou en vrai script) une stratégie de sauvegarde complète appliquant la règle 3-2-1 pour un dossier important. Décris : quoi sauvegarder, vers où (deux supports, une copie distante), à quelle fréquence (et comment la planifier avec cron), et comment tu vérifierais régulièrement que les sauvegardes sont restaurables. Tu mobilises ici rsync, tar, SSH et cron — toute la Partie 6.

## ✅ Tu sais maintenant…

- Pourquoi sauvegarder est une **responsabilité fondamentale**, pas une option
- La règle **3-2-1** (3 copies, 2 supports, 1 hors site)
- La différence entre sauvegarde **complète** et **incrémentale**
- Sauvegarder avec `rsync` (incrémental, local ou distant) et la prudence du `--delete` + `--dry-run`
- Créer des archives **horodatées** avec `tar` et `$(date +%F)`
- **Planifier** les sauvegardes avec cron (chemins absolus)
- Que **tester la restauration** est indispensable, et le rôle des sauvegardes contre les rançongiciels

---

> **🏁 CHECKPOINT 6 — Fin de la Partie 6**
>
> Tu sais maintenant **entretenir un système sur la durée** : installer et tenir les logiciels à jour, surveiller l'espace disque et la mémoire, archiver des données, et mettre en place des sauvegardes fiables et testées. Ce sont les gestes qui maintiennent une machine en bonne santé année après année.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - mettre à jour ton système proprement, et expliquer `update` vs `upgrade` ?
> - constater un disque plein avec `df`, puis trouver le coupable avec `du` ?
> - observer la structure de stockage avec `lsblk` et `findmnt` sans rien risquer ?
> - créer et extraire une archive `.tar.gz` ?
> - mettre en place une sauvegarde `rsync` incrémentale et tester sa restauration ?
>
> Si oui, tu sais faire vivre un système dans le temps. Il ne reste qu'à tout réunir : diagnostiquer, sécuriser et automatiser. Place à la **Partie 7 — Diagnostiquer, sécuriser, automatiser**, la synthèse appliquée du cours.

---

---
---

# PARTIE 7 — Diagnostiquer, sécuriser, automatiser

Voici la synthèse appliquée du cours. On ne découvre plus beaucoup de commandes nouvelles : on **mobilise tout ce qu'on a appris** pour résoudre des problèmes réels, sécuriser une machine et automatiser le travail. C'est ici que les six parties précédentes prennent tout leur sens et se rejoignent.

---

# Chapitre 24 — Diagnostic système (méthode)

## Le minimum à savoir

### Une méthode, pas une liste de commandes

Face à un problème (« le serveur est lent », « un service ne démarre pas », « le disque est plein »), le débutant tape des commandes au hasard. L'administrateur suit une **méthode** : du symptôme vers la cause, en éliminant les pistes une à une. Ce chapitre ne t'apprend presque aucune commande nouvelle — tu les connais toutes. Il t'apprend à les **enchaîner intelligemment**.

La démarche générale :

1. **Observer le symptôme précisément.** « Lent » ne veut rien dire ; lent à quoi ? depuis quand ? pour qui ?
2. **Formuler des hypothèses.** CPU saturé ? Mémoire pleine ? Disque plein ? Réseau coupé ? Service planté ?
3. **Vérifier chaque hypothèse** avec l'outil adapté, en commençant par le plus probable.
4. **Lire les logs**, qui racontent souvent directement ce qui s'est passé.
5. **Corriger**, puis **vérifier** que le problème a disparu.

### La trousse de diagnostic (tout ce que tu connais déjà)

| Question | Commande | Vu au chapitre |
|----------|----------|----------------|
| Depuis quand la machine tourne ? charge ? | `uptime` | (ici) |
| Quels processus consomment ? | `top`, `htop` | 13 |
| La mémoire est-elle saturée ? | `free -h` | 21 |
| Le disque est-il plein ? | `df -h` puis `du` | 21 |
| Un service est-il tombé ? | `systemctl status` | 14 |
| Que disent les journaux ? | `journalctl`, `/var/log` | 15 |
| Un souci matériel/noyau ? | `dmesg -T` | 15 |
| Le réseau répond-il ? | `ping`, `ip a`, `ss` | 17 |

`uptime` est le seul vrai nouveau venu, et il est simple :

```bash
uptime           # depuis quand la machine tourne + la "charge" (load average)
```

La **charge** (*load average*) donne trois chiffres (moyenne sur 1, 5 et 15 minutes). En première approche, comparée au nombre de cœurs du processeur : une charge durablement supérieure au nombre de cœurs indique un système surchargé.

## Très utile en pratique

### Scénario 1 : « la machine est lente »

```bash
uptime           # la charge est-elle anormalement haute ?
top              # quel processus dévore le CPU ? (trie par %CPU)
free -h          # la mémoire est-elle pleine ? (le système "swappe"-t-il ?)
df -h            # le disque est-il plein ? (un disque plein ralentit tout)
```

On part du plus global (`uptime`, `top`) vers le plus précis. Le coupable est presque toujours l'un de ces quatre : un processus emballé, la mémoire saturée, le disque plein, ou un disque défaillant (`dmesg -T`).

### Scénario 2 : « un service ne démarre pas »

```bash
sudo systemctl status nginx      # quel est l'état ? que dit le résumé ?
journalctl -u nginx -e           # le journal complet du service (fin)
journalctl -u nginx --since "10 min ago"   # juste avant l'échec
```

Le couple `status` + `journalctl -u` (chapitres 14-15) résout l'immense majorité des cas : le service écrit **pourquoi** il a échoué (port déjà utilisé, fichier de config invalide, permission manquante…). On lit, on comprend, on corrige.

### Scénario 3 : « pas d'accès réseau »

```bash
ip a                     # ai-je une adresse IP ?
ip r                     # ai-je une passerelle (route par défaut) ?
ping 8.8.8.8             # le réseau répond-il par IP ?
ping exemple.com         # le DNS résout-il les noms ?
```

On remonte la chaîne : interface → adresse → passerelle → connectivité IP → DNS. Le premier maillon qui casse désigne la cause (souvenir du chapitre 17 : IP OK mais nom KO = problème DNS).

> **Le réflexe maître :** quel que soit le problème, **les logs parlent**. Avant de spéculer longuement, lis `journalctl -e` et le `status` du service concerné. La réponse y est souvent écrite noir sur blanc.

## ❌ Erreur classique

```bash
# Taper des commandes au hasard sans hypothèse
# ❌ on s'agite sans avancer
# ✅ formuler une hypothèse, la tester, passer à la suivante

# Ignorer les logs et deviner
# ❌ spéculer sur la cause
journalctl -u service -e         # ✅ le service dit souvent POURQUOI il a échoué

# Confondre charge élevée et CPU élevé
uptime                           # charge haute peut aussi venir d'attente disque/IO
top                              # ✅ regarder CPU, mémoire ET état des processus

# Redémarrer sans comprendre
sudo reboot                      # ❌ "ça remarche" sans savoir pourquoi = ça reviendra
# ✅ comprendre la cause AVANT de redémarrer
```

## Exercices

**Guidé :** Fais un bilan de santé complet de ta machine en enchaînant : `uptime`, `free -h`, `df -h`, et `top` (quelques secondes, puis `q`). Pour chacun, note une conclusion : la charge est-elle normale ? reste-t-il de la mémoire ? de l'espace disque ? un processus consomme-t-il anormalement ?

**Autonome :** Choisis un service actif sur ta machine (vu au chapitre 14). Affiche son `systemctl status`, puis son journal récent avec `journalctl -u <service> --since "today"`. Entraîne-toi à lire ces sorties comme un diagnostic : le service est-il sain ? Y a-t-il des avertissements ou erreurs ?

**Défi :** Rédige ta propre **checklist de diagnostic** « machine lente », sous forme d'une liste ordonnée de commandes à lancer, avec pour chacune la question à laquelle elle répond et ce qui constituerait un résultat anormal. Tu construis là un véritable outil de travail réutilisable — exactement ce qu'un administrateur garde sous la main.

## ✅ Tu sais maintenant…

- Suivre une **méthode** : symptôme → hypothèses → vérification → logs → correction → vérification
- Mobiliser ta **trousse de diagnostic** (`uptime`, `top`, `free`, `df`/`du`, `systemctl`, `journalctl`, `dmesg`, `ping`/`ip`/`ss`)
- Lire la **charge** avec `uptime` et la relativiser au nombre de cœurs
- Dérouler les scénarios types : machine lente, service en panne, réseau coupé
- Que **les logs contiennent souvent la réponse** : les lire avant de spéculer
- Comprendre la cause **avant** de redémarrer

---

# Chapitre 25 — Sécurité de base (durcissement)

## Le minimum à savoir

### Durcir, c'est réduire la surface d'attaque

**Durcir** (*hardening*) une machine, c'est diminuer le nombre de façons dont elle peut être attaquée. Le principe directeur, déjà rencontré au chapitre 11, est le **moindre privilège** appliqué à tout : moins de services qui tournent, moins de ports ouverts, moins de comptes, moins de droits, moins de logiciels. **Tout ce qui n'est pas nécessaire est une porte potentielle qu'on ferme.** Ce chapitre rassemble, sous l'angle défensif, beaucoup de réflexes vus tout au long du cours.

### Les fondamentaux, dans l'ordre d'importance

1. **Maintenir à jour** (chapitre 20). La mesure la plus rentable, et de loin : beaucoup d'attaques exploitent des failles déjà connues et corrigées.

   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. **Réduire les services et ports** (chapitres 14, 17). Désactiver ce qui ne sert pas.

   ```bash
   sudo ss -tulpn                       # qu'est-ce qui écoute ?
   sudo systemctl disable --now service-inutile   # arrêter et désactiver
   ```

3. **Durcir SSH** (chapitre 18). Pas de connexion root, clés plutôt que mots de passe.

4. **Gérer les comptes et privilèges** (chapitres 10, 11, 12). Comptes au minimum, sudo précis, audit des SUID/capabilities.

5. **Mettre un pare-feu** (ci-dessous).

## Très utile en pratique

### Le pare-feu simple : `ufw`

Un **pare-feu** contrôle quelles connexions réseau sont autorisées. Sous Debian/Ubuntu, `ufw` (*Uncomplicated Firewall*) le rend accessible. La logique de durcissement : **tout bloquer par défaut, puis n'ouvrir que le nécessaire.**

```bash
sudo ufw default deny incoming       # bloquer toutes les connexions entrantes par défaut
sudo ufw default allow outgoing      # autoriser les connexions sortantes
sudo ufw allow 22/tcp                # autoriser SSH (sinon on se coupe l'accès !)
sudo ufw enable                      # activer le pare-feu
sudo ufw status verbose              # vérifier les règles actives
```

> **⚠️ Prudence (lien chapitre 18) :** avant d'activer le pare-feu sur une machine distante, **autorise SSH d'abord** (`ufw allow 22/tcp`). Sinon, `ufw enable` te couperait immédiatement ta propre connexion. Le même réflexe « ne te verrouille pas dehors » que pour SSH.

### Se protéger de la force brute : `fail2ban` (notion)

`fail2ban` surveille les logs (chapitre 15) et **bannit automatiquement** les adresses IP qui multiplient les échecs de connexion (typiquement, les attaques par force brute SSH du chapitre 4). C'est la réponse automatisée à la menace qu'on a appris à **détecter** manuellement.

```bash
sudo systemctl status fail2ban       # vérifier qu'il tourne
sudo fail2ban-client status sshd     # voir les IP bannies pour SSH
```

Pour débuter, retiens son principe : il transforme la détection (compter les échecs dans les logs) en **protection active** (bloquer l'attaquant). Sa configuration fine dépasse ce cours.

> **`fail2ban` n'est pas magique :** l'installer ne suffit pas toujours. Il faut **vérifier que la jail SSH est activée**, que les logs qu'il surveille correspondent bien à ta distribution (`auth.log` / `secure` / `journalctl`, chapitre 15), et **tester** que les bannissements fonctionnent réellement (`sudo fail2ban-client status sshd`). On l'utilise donc comme un mécanisme **à configurer et à tester**, pas comme une protection automatique garantie.

### La checklist de durcissement

Voici une checklist de base pour un serveur fraîchement installé, qui réunit le cours :

```
□ Système à jour (apt update && apt upgrade)
□ Comptes : pas de compte inutile, mots de passe robustes (audit /etc/passwd)
□ sudo : règles précises, pas de connexion root directe
□ SSH : PermitRootLogin no, authentification par clé, PasswordAuthentication no
□ Services : seuls les nécessaires tournent (ss -tulpn, systemctl disable les autres)
□ Pare-feu : ufw activé, deny par défaut, seuls les ports utiles ouverts
□ fail2ban : installé et actif pour SSH
□ SUID/capabilities : liste de référence établie (find -perm -4000, getcap -r /)
□ Logs : journalisation active et surveillée (journalctl)
□ Sauvegardes : en place, testées, hors site (chapitre 23)
```

> **Orientation cyber / SOC / eJPT :** cette checklist est le **versant défensif** de l'énumération qu'un attaquant réalise. Là où l'attaquant cherche un service mal configuré, un SUID exploitable, un sudo trop permissif ou un système non patché, le défenseur ferme ces mêmes portes en amont. Tu connais maintenant les deux faces : tu sais où regarder, donc tu sais quoi protéger.

## ❌ Erreur classique

```bash
# Activer ufw sans autoriser SSH (sur une machine distante)
sudo ufw enable                  # ❌ connexion SSH coupée immédiatement
sudo ufw allow 22/tcp            # ✅ AVANT d'activer, sur une machine distante
sudo ufw enable

# Ouvrir tout "pour que ça marche"
sudo ufw allow from any to any   # ❌ revient à ne pas avoir de pare-feu
sudo ufw allow 22/tcp            # ✅ ouvrir port par port, le strict nécessaire

# Croire qu'un pare-feu seul suffit
# ❌ le pare-feu est UNE couche ; mises à jour, SSH durci, comptes comptent autant

# Laisser des services par défaut tourner sans réfléchir
sudo ss -tulpn                   # ✅ inventorier, puis désactiver l'inutile
```

## Exercices

**Guidé :** Fais un mini-audit de durcissement de ta machine, **sans rien modifier**. Vérifie : le système est-il à jour (`apt list --upgradable`) ? Quels ports écoutent (`sudo ss -tulpn`) ? Le pare-feu est-il actif (`sudo ufw status`) ? Y a-t-il une connexion root SSH autorisée (`grep PermitRootLogin /etc/ssh/sshd_config`) ? Note ce qui pourrait être amélioré.

**Autonome (en lab) :** Sur une machine de test (pas un accès distant unique !), configure `ufw` proprement : politique deny par défaut en entrée, autorise SSH, active-le, et vérifie avec `ufw status verbose`. Confirme que tu as toujours accès. Désactive-le ensuite si c'était juste un exercice (`sudo ufw disable`).

**Défi (orientation sécurité) :** Reprends la checklist de durcissement ci-dessus et applique-la, point par point, à ta machine d'apprentissage. Pour chaque ligne, note l'état actuel (conforme / à corriger) et la commande qui vérifie ou corrige. Tu produis ainsi un **rapport de durcissement** — exactement le livrable d'un travail de sécurisation réel.

## ✅ Tu sais maintenant…

- Que **durcir** = réduire la surface d'attaque (moindre privilège appliqué à tout)
- L'ordre des priorités : **mises à jour** d'abord, puis services/ports, SSH, comptes, pare-feu
- Configurer un pare-feu avec `ufw` (deny par défaut, ouvrir le strict nécessaire, autoriser SSH avant `enable`)
- Que `fail2ban` transforme la **détection** de force brute en **protection** automatique
- Dérouler une **checklist de durcissement** complète, qui réunit tout le cours
- Que le durcissement défensif est le miroir de l'énumération offensive

---

# Chapitre 26 — Automatiser avec Bash (admin)

## Le minimum à savoir

### Du one-liner au script

Tout au long du cours, tu as enchaîné des commandes avec des pipes (chapitre 7). Un **script** Bash, c'est simplement plusieurs de ces commandes enregistrées dans un fichier, qu'on exécute d'un coup. C'est l'aboutissement naturel de l'administration : ce qu'on fait deux fois à la main, on l'automatise. Ce chapitre fait le **pont avec le scripting Bash** ; il en montre l'application à l'administration, sans réexpliquer ce que tu as déjà appris au chapitre 8 sur l'environnement (variables, `PATH`, alias, `.bashrc`).

### Un script minimal

Un script Bash est un fichier texte qui commence par une ligne spéciale, le *shebang*, indiquant quel interpréteur l'exécute :

```bash
#!/bin/bash
# Mon premier script d'administration
echo "Rapport du $(date)"
echo "Connecté en tant que : $(whoami)"
```

On le rend exécutable (chapitre 9 !) et on le lance :

```bash
chmod +x rapport.sh          # droit d'exécution
./rapport.sh                 # exécution (le ./ : le . n'est pas dans le PATH, chapitre 8)
```

> Tu retrouves ici trois notions du cours réunies : le droit `x` (chapitre 9), la raison du `./` (chapitre 8), et la substitution `$(commande)` qui insère le résultat d'une commande dans le texte (entrevue avec `$(date +%F)` au chapitre 22).

### Réutiliser tes acquis dans des scripts

Un script d'administration n'est rien d'autre que les commandes du cours, mises bout à bout. Par exemple, un script qui résume l'état du système :

```bash
#!/bin/bash
echo "=== État du système au $(date) ==="
echo ""
echo "--- Disque ---"
df -h /                                  # chapitre 21
echo ""
echo "--- Mémoire ---"
free -h                                  # chapitre 21
echo ""
echo "--- Charge ---"
uptime                                   # chapitre 24
echo ""
echo "--- Services clés ---"
systemctl is-active ssh                  # chapitre 14
```

Rien de neuf : juste l'assemblage de ce que tu sais déjà.

## Très utile en pratique

### Variables, environnement et alias (rappel d'application)

Le chapitre 8 t'a tout donné : variables, `export`, `PATH`, alias, `.bashrc`, `source`. En administration, on les **applique** :

- Ranger ses scripts dans `~/bin` (ajouté au `PATH`) pour les lancer **par leur nom**, de partout, comme de vraies commandes.
- Créer des **alias** pour les commandes d'admin fréquentes, dans `.bashrc` :

```bash
# Dans ~/.bashrc (après un .bak, chapitre 6)
alias maj='sudo apt update && sudo apt upgrade'
alias ports='sudo ss -tulpn'
alias monlog='sudo journalctl -u ssh -f'
```

Après `source ~/.bashrc`, taper `maj` met tout à jour, `ports` liste les ports, `monlog` suit SSH en direct. Tu façonnes ton environnement de travail autour de tes tâches réelles.

### Rediriger la sortie d'un script vers un rapport

Grâce aux redirections (chapitre 7), un script peut écrire son résultat dans un fichier horodaté :

```bash
./etat-systeme.sh > rapport-$(date +%F).txt        # enregistre le rapport du jour
./etat-systeme.sh | tee rapport-$(date +%F).txt     # affiche ET enregistre (tee)
```

### Planifier un script (le pont avec le chapitre 16)

Un script + cron = automatisation complète. On dépose le script dans `~/bin` ou un chemin absolu, et on l'inscrit en crontab :

```bash
# crontab -e : rapport d'état chaque matin à 7h, enregistré daté
0 7 * * * /home/alice/bin/etat-systeme.sh > /home/alice/rapports/etat-$(date +\%F).txt
```

> **Rappels du chapitre 16, qui prennent tout leur sens ici :** en cron, utilise des **chemins absolus** (l'environnement est minimal, tes alias et ton `PATH` personnels n'y sont pas), et note que le `%` doit être échappé (`\%`) dans une crontab.

> **Pour aller plus loin en scripting :** ce chapitre fait volontairement le lien sans tout réenseigner. Conditions, boucles, fonctions, gestion d'arguments, tests robustes — tout cela relève d'un cours de **scripting Bash** dédié, qui prolonge naturellement cette formation. Ici, l'essentiel est que tu saches **assembler tes commandes d'admin en scripts réutilisables et planifiés**.

## ❌ Erreur classique

```bash
# Oublier le shebang ou le droit d'exécution
./script.sh                  # ❌ "Permission denied" si pas de chmod +x
chmod +x script.sh           # ✅ (chapitre 9)

# Chemins relatifs dans un script planifié
df -h                        # ❌ ok à la main, mais en cron le contexte diffère
/bin/df -h /home/alice       # ✅ chemins absolus pour le planifié (chapitre 16)

# Oublier d'échapper le % en crontab
... > rapport-$(date +%F).txt    # ❌ le % a un sens spécial en crontab
... > rapport-$(date +\%F).txt   # ✅ échapper avec \

# Lancer un script non testé directement en production
# ✅ tester d'abord à la main, vérifier la sortie, PUIS planifier
```

## Exercices

**Guidé :** Crée un script `etat.sh` reprenant l'exemple « état du système » ci-dessus. Rends-le exécutable avec `chmod +x`, lance-le avec `./etat.sh`, et vérifie que toutes les sections s'affichent. Puis redirige sa sortie vers un fichier daté avec `./etat.sh > etat-$(date +%F).txt` et lis le rapport produit.

**Autonome :** Ajoute à ton `.bashrc` (après un `.bak` !) trois alias d'administration qui te seraient utiles au quotidien (par exemple mise à jour, ports en écoute, espace disque). Applique avec `source ~/.bashrc` et teste-les. Ouvre un nouveau terminal pour confirmer qu'ils sont permanents.

**Défi :** Planifie ton script `etat.sh` pour qu'il s'exécute chaque jour et enregistre un rapport horodaté dans un dossier dédié. Vérifie la syntaxe de ta ligne crontab (chemins absolus, `%` échappé). Le lendemain (ou en réglant l'heure proche), confirme qu'un rapport a bien été généré automatiquement. Tu viens de créer ta première surveillance automatisée.

## ✅ Tu sais maintenant…

- Qu'un **script** Bash assemble des commandes d'admin dans un fichier exécutable
- Écrire un script minimal (shebang `#!/bin/bash`, `chmod +x`, `./script`)
- Réutiliser tout le cours dans des scripts (disque, mémoire, services, logs…)
- **Appliquer** l'environnement du chapitre 8 : `~/bin` dans le `PATH`, alias d'admin dans `.bashrc`
- Produire des **rapports horodatés** avec redirections, `tee` et `$(date +%F)`
- **Planifier** un script avec cron (chemins absolus, `%` échappé)
- Que conditions/boucles/fonctions relèvent d'un cours de **scripting Bash** dédié, prolongement naturel

---

# Chapitre 27 — Mini-projets pratiques

Voici trois projets fil rouge qui mobilisent **l'ensemble du cours**. Ils sont conçus pour être réalisés sur ta machine d'apprentissage ou une VM dédiée. Prends ton temps : la valeur est dans la réalisation, pas dans la lecture.

---

## Projet 1 — Mettre en service un serveur (orientation admin)

**Objectif :** partir d'une machine fraîchement installée et la rendre opérationnelle, propre et sécurisée. C'est la synthèse de l'administration classique.

> **⚠️ À faire en lab :** réalise ce projet dans une **VM locale ou un serveur de lab**. N'expose **pas** un service sur Internet tant que tu n'as pas solidement compris le pare-feu, les mises à jour, les logs et les sauvegardes. Un serveur mal préparé exposé au Web est attaqué en quelques minutes.

**Étapes proposées :**

1. **Première prise en main** (parties 1-2) : connecte-toi, repère-toi (`pwd`, `ls`, arborescence), mets à jour le système (`sudo apt update && sudo apt upgrade`).
2. **Comptes** (partie 3) : crée un utilisateur d'administration dédié (`adduser`), ajoute-le au groupe `sudo` (`usermod -aG sudo`), vérifie ses droits (`id`, `sudo -l`).
3. **Accès distant sécurisé** (partie 5) : mets en place l'authentification SSH par clé (`ssh-keygen`, `ssh-copy-id`), puis durcis `sshd_config` (`PermitRootLogin no`, clés uniquement) avec le réflexe `.bak`/`sudoedit`/`diff`. **Garde une session de secours.**
4. **Pare-feu** (partie 7) : configure `ufw` (deny par défaut, autorise SSH **avant** d'activer).
5. **Un service** (partie 4) : installe un service simple (par exemple un serveur web), vérifie son `systemctl status`, active-le au démarrage (`enable --now`), confirme qu'il écoute (`ss -tulpn`).
6. **Sauvegardes** (partie 6) : écris un petit script de sauvegarde (`rsync` ou `tar` horodaté), teste-le, puis planifie-le en cron.
7. **Vérification finale** : déroule la checklist de durcissement du chapitre 25.

**Livrable :** une machine opérationnelle + un court document décrivant ce que tu as configuré et pourquoi.

---

## Projet 2 — Script de surveillance défensive (orientation SOC)

**Objectif :** créer un tableau de bord texte qui donne, en un coup d'œil, l'état de santé et de sécurité de la machine. C'est l'outil quotidien d'un analyste.

**Ce que le script doit produire** (un rapport horodaté) :

1. **Santé système** (parties 4, 6) : charge (`uptime`), mémoire (`free -h`), espace disque (`df -h`).
2. **Services clés** (partie 4) : état des services importants (SSH, pare-feu…) via `systemctl is-active`.
3. **Réseau** (partie 5) : ports actuellement en écoute (`ss -tulpn`).
4. **Sécurité — connexions** (parties 1, 3, 4) : dernières connexions réussies, et surtout les **tentatives d'authentification échouées** récentes, en isolant les IP sources les plus fréquentes (le pipeline `grep`/`awk`/`sort`/`uniq -c` du chapitre 4, appliqué à `auth.log`/`secure` ou via `journalctl`).
5. **Mise en forme** : un rapport clair, horodaté (`$(date)`), enregistré dans un fichier daté et/ou affiché avec `tee`.

**Étapes :**

- Construis le script section par section (chapitre 26), en testant chaque bloc à la main d'abord.
- Rends-le exécutable, range-le dans `~/bin`.
- Planifie-le (cron) pour un rapport quotidien automatique.

**Livrable :** un script `surveillance.sh` fonctionnel + un exemple de rapport généré. C'est une véritable première brique de supervision défensive.

---

## Projet 3 — Investigation d'incident (orientation cyber / eJPT)

**Objectif :** à partir d'un jeu de logs (réels de ta machine, ou un jeu de logs d'entraînement que tu te constitues), **reconstituer le déroulé d'une activité suspecte**. C'est l'exercice central de l'analyse défensive.

**Trame d'investigation :**

1. **Collecte** (parties 1, 6) : rassemble les logs pertinents sans les altérer (`rsync`/`tar` qui préservent les dates, chapitre 19/22). Travaille sur des **copies**.
2. **Connexions** (parties 1, 4) : dans le journal d'authentification, distingue les connexions réussies des échecs. Y a-t-il une rafale d'échecs (signe de force brute) ? Suivie d'une réussite (compromission possible) ? Depuis quelles IP ? (pipeline du chapitre 4 / `journalctl` du chapitre 15.)
3. **Privilèges** (partie 3) : recherche les usages de `sudo` dans les logs. Une élévation de privilèges inattendue ? Par quel compte ?
4. **Persistance** (partie 4) : inspecte les tâches planifiées (`crontab -l`, `/etc/cron.*`) et les services (`systemctl list-units`). Quelque chose d'anormal aurait-il été ajouté ?
5. **Traces sur le système** (parties 2, 3) : cherche des fichiers récents ou suspects (`find` par date), des binaires SUID ou capabilities inattendus (`find -perm -4000`, `getcap -r /`, chapitre 12), des fichiers dans des emplacements inhabituels (`/tmp`).
6. **Synthèse** : rédige une **chronologie** de ce que tu as reconstitué — quoi, quand, depuis où, par quel compte — comme un mini-rapport d'incident.

**Livrable :** un rapport d'investigation : la chronologie reconstituée, les indices retenus, et les recommandations (que faudrait-il durcir pour empêcher la récidive ? → chapitre 25).

> **Note éthique :** cet exercice est **défensif**. On apprend à **comprendre et reconstituer** une activité pour mieux protéger, jamais à attaquer un système qui ne nous appartient pas. Entraîne-toi uniquement sur tes propres machines ou des environnements prévus pour l'apprentissage.

---

> **🏁 CHECKPOINT FINAL — Fin du cours**
>
> Tu es allé du tout début — ouvrir un terminal sans savoir quoi en faire — jusqu'à savoir **administrer, diagnostiquer, sécuriser et automatiser** un système Linux, avec les réflexes défensifs d'un analyste. C'est un parcours considérable.
>
> **Tu sais maintenant :**
> - survivre et te repérer dans le terminal (parties 1-2) ;
> - comprendre le modèle de sécurité de Linux : permissions, utilisateurs, privilèges (partie 3) ;
> - piloter une machine vivante : processus, services, logs, planification (partie 4) ;
> - administrer une machine à distance et en réseau (partie 5) ;
> - entretenir un système : paquets, disque, archives, sauvegardes (partie 6) ;
> - diagnostiquer, durcir et automatiser (partie 7).
>
> La suite t'appartient : pratique sur tes propres machines, approfondis le **scripting Bash**, et explore les pistes **SOC / pentest / eJPT** qui prolongent naturellement ces fondations.

---

---
---

# SYNTHÈSE FINALE

Cette section te sert de **référence rapide** une fois le cours terminé. Garde-la sous la main : ce sont les commandes et réflexes que tu utiliseras au quotidien.

## Cheat-sheets thématiques

### Navigation et repérage

| Besoin | Commande |
|--------|----------|
| Où suis-je ? | `pwd` |
| Lister (détaillé, cachés, lisible) | `ls -lah` |
| Se déplacer / revenir | `cd chemin` / `cd -` / `cd ~` |
| Voir l'arbre | `tree -L 2` |
| Remonter d'un niveau | `cd ..` |

### Fichiers et lecture

| Besoin | Commande |
|--------|----------|
| Type d'un fichier | `file fichier` |
| Lire (petit / gros) | `cat fichier` / `less fichier` |
| Début / fin | `head fichier` / `tail fichier` |
| Suivre en direct | `tail -f fichier` (sortie : `Ctrl+C`) |
| Compter les lignes | `wc -l fichier` |
| Créer / copier / déplacer | `touch` / `cp -r` / `mv` |
| Supprimer (prudence !) | `rm -i` / `rm -r` |
| Créer une arborescence | `mkdir -p a/b/c` |

### Recherche et texte

| Besoin | Commande |
|--------|----------|
| Chercher du texte | `grep -i "motif" fichier` |
| Compter / inverser / numéroter | `grep -c` / `grep -v` / `grep -n` |
| Trouver un fichier | `find /chemin -name "*.ext"` |
| Extraire une colonne | `cut -d: -f1` / `awk '{print $1}'` |
| Remplacer du texte | `sed 's/ancien/nouveau/g'` |
| Trier / dédoublonner + compter | `sort` / `sort \| uniq -c` |
| Casse | `tr 'A-Z' 'a-z'` |

### Flux et environnement

| Besoin | Commande |
|--------|----------|
| Enregistrer / ajouter | `cmd > fichier` / `cmd >> fichier` |
| Jeter les erreurs | `cmd 2>/dev/null` |
| Enchaîner | `cmd1 \| cmd2` |
| Voir ET enregistrer | `cmd \| tee fichier` |
| Voir une variable | `echo $PATH` |
| Toutes les variables | `env` |
| Localiser un programme | `which cmd` / `command -v cmd` |
| Variable / alias permanents | éditer `~/.bashrc` puis `source ~/.bashrc` |

### Permissions et identité

| Besoin | Commande |
|--------|----------|
| Voir les droits | `ls -l` |
| Modifier (symbolique / octal) | `chmod u+x` / `chmod 755` |
| Rendre un script exécutable | `chmod +x script.sh` |
| Changer propriétaire / groupe | `chown user:grp` / `chgrp grp` |
| Mon identité | `id` / `whoami` / `groups` |
| Créer un user / l'ajouter à un groupe | `adduser bob` / `usermod -aG sudo bob` |
| Admin ponctuel | `sudo cmd` |
| Mes droits sudo | `sudo -l` |
| Lister les SUID / capabilities | `find / -type f -perm -4000 2>/dev/null` / `getcap -r / 2>/dev/null` |

### Processus et services

| Besoin | Commande |
|--------|----------|
| Lister les processus | `ps aux` / `ps aux \| grep nom` |
| Temps réel | `top` / `htop` (sortie : `q`) |
| Arrêter (poli / forcé) | `kill PID` / `kill -9 PID` |
| Par nom | `killall nom` |
| État d'un service | `systemctl status nom` |
| Démarrer / arrêter / redémarrer | `sudo systemctl start\|stop\|restart nom` |
| Auto au démarrage | `sudo systemctl enable --now nom` |
| Lister les services | `systemctl list-units --type=service` |

### Logs et diagnostic

| Besoin | Commande |
|--------|----------|
| Journal d'un service | `journalctl -u nom` |
| Suivre en direct | `journalctl -f` |
| Depuis quand / filtré | `journalctl --since "today"` |
| Messages noyau/matériel | `sudo dmesg -T \| tail` |
| Charge / uptime | `uptime` |
| Mémoire | `free -h` |
| Logs d'auth (selon distro) | `/var/log/auth.log` · `/var/log/secure` · `journalctl` |

### Réseau et SSH

| Besoin | Commande |
|--------|----------|
| Mes adresses / routes | `ip a` / `ip r` |
| Tester la connectivité | `ping -c 4 cible` |
| Ports en écoute | `sudo ss -tulpn` |
| Résolution DNS | `dig nom` / `nslookup nom` |
| Tester un site | `curl -I url` |
| Connexion distante | `ssh user@machine` |
| Générer / copier une clé | `ssh-keygen -t ed25519` / `ssh-copy-id user@machine` |
| Copier / synchroniser | `scp` / `rsync -av --dry-run` |

### Paquets, disque, archives

| Besoin | Commande |
|--------|----------|
| Mettre à jour | `sudo apt update && sudo apt upgrade` |
| Installer / supprimer | `sudo apt install nom` / `sudo apt purge nom` |
| Chercher un paquet | `apt search motclé` |
| Espace disque global | `df -h` |
| Taille d'un dossier | `du -sh dossier` |
| Plus gros dossiers | `du -h --max-depth=1 / \| sort -rh \| head` |
| Disques / montages (observer) | `lsblk` / `findmnt` |
| Archiver / extraire | `tar -czvf a.tar.gz dossier/` / `tar -xzvf a.tar.gz` |
| Lire un log compressé | `zcat fichier.gz` / `zgrep "motif" fichier.gz` |

## Récapitulatif des erreurs classiques

| Domaine | Le piège | Le bon réflexe |
|---------|----------|----------------|
| Suppression | `rm` est définitif, pas de corbeille | `pwd` → `ls` → `rm -i` ; relire `rm -rf` |
| Espace parasite | `rm -rf / chemin` détruit la racine | relire la ligne avant Entrée |
| Permissions | `chmod 777` = faille ouverte | donner le minimum (`644`, `755`, `600`) |
| Dossiers | `r` ne suffit pas pour entrer | il faut le `x` pour traverser |
| Groupes | `usermod -G` écrase les groupes | toujours `usermod -aG` |
| sudo | shell root permanent (`sudo -i`) | `sudo cmd` ponctuel |
| Services | `start` ≠ persistant | `enable --now` pour le démarrage auto |
| Redirection | `>` écrase sans prévenir | `>>` pour ajouter ; vérifier la cible |
| Recherche | confondre `find` (fichiers) et `grep` (texte) | `find` = noms, `grep` = contenu |
| Réseau | `netstat`/`ifconfig` absents | `ss` / `ip` (modernes) |
| Paquets | `upgrade` sans `update` | `update && upgrade` |
| Disque | confondre `df` (disque) et `du` (dossier) | `df` constate, `du` trouve le coupable |
| Montage | `mount`/`umount`/`fstab` sensibles | observer d'abord (`lsblk`, `findmnt`) |
| Archives | `f` mal placé dans `tar` | `f` toujours juste avant le nom |
| SSH | se verrouiller dehors | garder une session de secours, tester la clé d'abord |
| Pare-feu | `ufw enable` coupe SSH | `ufw allow 22/tcp` avant d'activer |
| cron | chemins relatifs, `%` non échappé | chemins absolus, `\%` |
| Variables | `echo PATH` au lieu de `$PATH` | `$` pour lire ; écraser le `PATH` casse tout |

## Arbre de décision — « Quelle commande pour quel besoin ? »

```
Je veux...
├─ me repérer / naviguer ........... pwd, ls, cd, tree
├─ lire un fichier
│   ├─ petit ....................... cat
│   ├─ gros ........................ less
│   └─ suivre en direct ........... tail -f / journalctl -f
├─ chercher
│   ├─ du texte DANS des fichiers .. grep
│   └─ des fichiers (par nom) ...... find
├─ modifier des fichiers .......... touch, cp, mv, rm, nano/sudoedit
├─ comprendre les droits .......... ls -l, chmod, chown, id
├─ faire une action admin ......... sudo
├─ voir ce qui tourne ............. ps aux, top/htop, systemctl
├─ comprendre un problème ......... journalctl, systemctl status, dmesg
├─ regarder le réseau ............. ip a, ss -tulpn, ping
├─ me connecter à distance ........ ssh
├─ transférer des fichiers ........ scp, rsync
├─ installer un logiciel .......... sudo apt install
├─ gérer l'espace disque .......... df -h, du -sh, lsblk, findmnt
├─ archiver / sauvegarder ......... tar, gzip, rsync
└─ automatiser .................... script Bash + cron
```

## Pour continuer

Tu as les fondations solides de l'administration Linux. Voici les prolongements naturels :

- **Scripting Bash approfondi** : conditions, boucles, fonctions, gestion d'arguments et de cas d'erreur. C'est le complément direct du chapitre 26, pour transformer tes commandes en véritables outils. *(Un cours de scripting Bash dédié prolonge idéalement cette formation.)*
- **Python pour l'automatisation défensive** : quand Bash atteint ses limites (parsing complexe, API, structures de données), Python prend le relais — particulièrement en analyse de logs, OSINT et traitement d'IOC.
- **Cybersécurité défensive / SOC** : approfondis l'analyse de logs, la détection d'intrusion, les SIEM. Les chapitres 4, 11, 12, 15 et le projet 3 en sont la porte d'entrée.
- **Pentest débutant / eJPT** : l'énumération système (chapitres 10-12), le réseau (chapitre 17) et SSH (chapitre 18) constituent exactement les bases attendues. Tu connais déjà le versant défensif de ce que cette certification aborde côté offensif.
- **La pratique, surtout** : monte un petit lab (quelques VM), casse-le, répare-le, automatise-le. C'est en administrant de vraies machines qu'on devient administrateur.

Bon parcours sous Linux.

---
---

# ANNEXES

Ces sujets dépassent le cœur du cours débutant, mais valent d'être connus quand tu progresseras. Ils sont volontairement traités en survol : chacun mériterait un cours à part entière.

## Annexe A — Expressions régulières (regex)

Les **regex** sont des motifs de recherche puissants, utilisés par `grep`, `sed`, `awk` et bien d'autres. Le cours en a montré l'usage le plus simple (chercher un mot littéral). Les regex permettent bien plus : `^` (début de ligne), `$` (fin de ligne), `.` (n'importe quel caractère), `*` (répétition), `[0-9]` (un chiffre), etc. Par exemple, `grep -E "^[0-9]+" fichier` trouve les lignes commençant par un nombre. C'est un domaine entier à explorer une fois les bases acquises ; il décuple la puissance de la recherche et du filtrage de logs.

## Annexe B — `sed` et `awk` avancés

Le chapitre 4 en a montré l'usage minimal (substitution simple, extraction de colonne). En réalité, `sed` est un éditeur de flux complet (suppression de lignes, insertion, plages d'adresses) et `awk` est un véritable **langage de traitement de texte** (variables, conditions, calculs, agrégations par champ). Pour l'analyse de logs poussée, ils sont irremplaçables — mais leur apprentissage approfondi relève d'un module dédié.

## Annexe C — Stockage avancé : partitions, LVM, RAID

Le chapitre 21 s'est concentré sur l'**observation** du stockage. La gestion avancée comprend : le **partitionnement** (`fdisk`, `parted`), le **LVM** (*Logical Volume Manager*, qui permet de redimensionner et combiner des volumes à chaud), et le **RAID** (combiner plusieurs disques pour la performance ou la redondance). Ces opérations sont puissantes mais risquées pour les données : à aborder en lab, avec méthode, une fois les fondamentaux maîtrisés.

## Annexe D — Pare-feu avancé : `iptables` / `nftables`

Le chapitre 25 a utilisé `ufw`, qui est une surcouche simplifiée. En dessous se trouvent `iptables` (historique) et `nftables` (moderne), qui offrent un contrôle très fin du trafic réseau (règles par protocole, par interface, NAT, etc.). C'est le niveau qu'on atteint pour des configurations réseau complexes ou des passerelles.

## Annexe E — Conteneurs et virtualisation

Au-delà des VM utilisées pour ce cours, l'écosystème moderne s'appuie massivement sur les **conteneurs** (Docker, Podman) : une façon légère d'empaqueter et d'isoler des applications. C'est une compétence majeure aujourd'hui, qui s'appuie directement sur les notions Linux de ce cours (processus, systèmes de fichiers, réseau, permissions). Un excellent sujet pour la suite.

## Annexe F — Familles de distributions

Le cours s'est concentré sur **Debian/Ubuntu** (gestionnaire `apt`). Les autres grandes familles : **RHEL/CentOS/Fedora/Rocky** (gestionnaire `dnf`/`yum`, logs dans `/var/log/secure`), et **Arch** (`pacman`, philosophie « rolling release »). Les **concepts** (permissions, processus, systemd, réseau) sont identiques partout ; seules changent quelques commandes de gestion de paquets et l'emplacement de certains fichiers. Savoir cela te permet de t'adapter à n'importe quelle distribution.

---
