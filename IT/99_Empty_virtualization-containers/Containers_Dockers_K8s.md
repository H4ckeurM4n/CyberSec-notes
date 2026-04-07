J’ai deux cours le scripting (bash et python) orienté très très débutant pour quelqu’un qui n’a jamais fait de programmation / développement ni ne connaît l’algorithmique, je veux que tu me fasses un équivalent de ce cours mais pour du powershell, si le powershell n’est pas vraiment utile pour du scripting ce n’est rien je veux surtout un cours aussi introductif que ceux de bash et python mais pour powershell et son usage tu comprends l’idée ? Voici mes cours bash que tu aies une idée : # Cours Complet de Scripting Bash
De zéro à l’automatisation — Guide pour débutant absolu

Prérequis : Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais écrit une seule ligne de code.
Tout ce dont tu as besoin, c’est un ordinateur avec Linux (ou un terminal Bash sur Mac/Windows via WSL).

Glossaire — Les mots à connaître
Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.



|Terme                       |Définition simple                                                  |
|----------------------------|-------------------------------------------------------------------|
|**Terminal**                |La fenêtre noire où tu tapes des commandes texte                   |
|**Shell**                   |Le programme qui lit et exécute tes commandes (Bash est un shell)  |
|**Script**                  |Un fichier texte contenant une liste de commandes à exécuter       |
|**Variable**                |Un conteneur avec un nom qui stocke une valeur                     |
|**Argument**                |Une info que tu donnes à un script quand tu le lances              |
|**Commande**                |Une instruction que le shell sait exécuter (`echo`, `ls`, `cd`…)   |
|**Sortie standard (stdout)**|Là où une commande affiche son résultat (l’écran par défaut)       |
|**Sortie d’erreur (stderr)**|Là où une commande affiche ses erreurs (l’écran aussi par défaut)  |
|**Code de retour**          |Un nombre (0 = succès, autre = erreur) que chaque commande renvoie |
|**Boucle**                  |Un mécanisme qui répète des commandes plusieurs fois               |
|**Fonction**                |Un bloc de code réutilisable auquel on donne un nom                |
|**Pipe**                    |Un “tuyau” (`|`) qui envoie la sortie d’une commande vers une autre|

Comment penser un script
Avant d’écrire la moindre ligne de code, il faut comprendre la logique de base. Tout script suit le même schéma :

  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat


Concrètement, il n’y a que 5 briques de base dans un script :
	1.	Recevoir des données (arguments, saisie utilisateur, fichier…)
	2.	Stocker des informations dans des variables
	3.	Tester si quelque chose est vrai ou faux (conditions)
	4.	Répéter une action plusieurs fois (boucles)
	5.	Afficher ou enregistrer un résultat (sortie)
Tous les scripts, même les plus complexes, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

Table des matières
	1.	Découverte de Bash et premier script
	2.	Variables, affichage et saisie utilisateur
	3.	Arguments et variables spéciales
	4.	Redirections, erreurs et pipes
	5.	Opérateurs, calculs et logique
	6.	Conditions, comparaisons et tests
	7.	Boucles
	8.	Fonctions et case
	9.	Chaînes de caractères
	10.	Tableaux
	11.	Déboguer et écrire des scripts propres
	12.	Cas pratiques et automatisation

Chapitre 1 — Découverte de Bash et premier script
Le minimum à savoir
Le terminal et le shell
Le terminal, c’est une fenêtre où tu tapes des commandes en texte au lieu de cliquer sur des icônes. Le shell, c’est le programme à l’intérieur du terminal qui comprend et exécute ces commandes. Le shell le plus répandu s’appelle Bash.
Pour ouvrir un terminal :
	∙	Linux : Ctrl + Alt + T ou cherche “Terminal” dans tes applications
	∙	Mac : cherche “Terminal” dans Spotlight
	∙	Windows : installe WSL (Windows Subsystem for Linux)
Vérifie que tu utilises bien Bash :

echo $SHELL


Tu devrais voir /bin/bash.
Quelques commandes pour se familiariser
Tape ces commandes dans ton terminal pour te familiariser :

echo "Bonjour !"       # Afficher du texte
pwd                     # Où suis-je ? (quel dossier)
ls                      # Qu'est-ce qu'il y a ici ? (liste des fichiers)
date                    # Quelle date et heure ?
whoami                  # Qui suis-je ? (nom d'utilisateur)


À retenir : le symbole # marque un commentaire. Bash ignore tout ce qui suit un #. Les commentaires servent à expliquer ton code.
Ton premier script en 5 étapes
Un script, c’est simplement plusieurs commandes rangées dans un fichier. Au lieu de les taper une par une, tu les écris une fois et tu les lances quand tu veux.
Étape 1 — Crée un dossier de travail :

mkdir -p ~/mes_scripts
cd ~/mes_scripts


Étape 2 — Crée le fichier :

nano hello.sh


Bonne pratique : l’extension .sh indique que c’est un script Bash. Ce n’est pas obligatoire, mais c’est une convention utile.
Étape 3 — Écris le script :

#!/bin/bash
# Mon tout premier script
echo "Hello, World !"
echo "Je suis un script Bash !"


Sauvegarde (Ctrl + O puis Entrée dans nano) et quitte (Ctrl + X).
Étape 4 — Rends-le exécutable :

chmod +x hello.sh


Étape 5 — Lance-le :

./hello.sh


Résultat :

Hello, World !
Je suis un script Bash !


Félicitations, tu viens d’écrire et d’exécuter ton premier script !
Le shebang : #!/bin/bash
La première ligne #!/bin/bash s’appelle le shebang. Elle dit au système : “ce fichier doit être lu par Bash”.
Sans shebang, le système ne sait pas quel langage utiliser. Avec le shebang, tu peux lancer ton script avec ./script.sh directement.
À retenir : mets TOUJOURS #!/bin/bash en première ligne de tes scripts.
Pourquoi ./ devant le script ?
Quand tu tapes ls ou date, le système sait où trouver ces commandes grâce à une variable appelée PATH. Ton dossier personnel n’est pas dans le PATH, donc il faut préciser “cherche dans le dossier actuel” avec ./.
La commande exit
exit permet de terminer un script avec un code de sortie :

#!/bin/bash
echo "Ce message s'affiche"
exit 0
echo "Ceci ne s'affichera JAMAIS"


Les codes essentiels :



|Code     |Signification                     |
|---------|----------------------------------|
|**`0`**  |**Succès** (tout s’est bien passé)|
|**`1`**  |**Erreur générale**               |
|**`127`**|**Commande introuvable**          |

À retenir : en Bash, 0 = succès, tout autre nombre = erreur. C’est l’inverse de ce qu’on pourrait penser !
Pour info, d’autres codes existent (2 = mauvaise utilisation, 130 = Ctrl+C, 126 = pas le droit d’exécuter), mais tu n’as pas besoin de les mémoriser maintenant.
❌ Erreur classique

# Oublier le shebang → le script peut ne pas fonctionner avec ./script.sh
# Oublier chmod +x → "Permission denied" quand tu lances le script
# Oublier le ./ → "command not found"


Exercices
Guidé : Crée un script salut.sh qui affiche deux lignes : “Bonjour !” puis “Bienvenue dans le monde du scripting.”
Autonome : Crée un script info.sh qui affiche ton nom d’utilisateur (whoami), la date (date), et le dossier actuel (pwd) sur des lignes séparées.
✅ Tu sais maintenant…
	∙	Ce qu’est un terminal, un shell et un script
	∙	Créer un fichier script avec le shebang #!/bin/bash
	∙	Rendre un script exécutable avec chmod +x
	∙	Lancer un script avec ./mon_script.sh
	∙	Ce que signifie un code de sortie

Chapitre 2 — Variables, affichage et saisie utilisateur
Le minimum à savoir
Qu’est-ce qu’une variable ?
Une variable, c’est un conteneur avec une étiquette. L’étiquette c’est le nom, et à l’intérieur il y a une valeur.

┌─────────────────┐
│  prenom = Alice  │   ← "prenom" est le nom, "Alice" est la valeur
└─────────────────┘


Créer et afficher une variable

#!/bin/bash

prenom="Alice"
echo "Bonjour, $prenom !"


Résultat : Bonjour, Alice !
Règle critique : PAS d’espace autour du =

# ✅ CORRECT
prenom="Alice"

# ❌ FAUX — Bash croit que "prenom" est une commande
prenom = "Alice"


Pour accéder au contenu d’une variable, on met $ devant son nom. Sans le $, Bash affiche le texte brut :

echo "Bonjour, $prenom"     # → Bonjour, Alice
echo "Bonjour, prenom"      # → Bonjour, prenom


Bonne pratique : écris "$prenom" (avec guillemets) plutôt que $prenom nu. Ça évite des problèmes si la valeur contient des espaces. Prends ce réflexe dès maintenant.
La forme avec accolades ${variable}
Les accolades servent à éviter les ambiguïtés :

animal="chat"
echo "J'ai 3 ${animal}s"    # → J'ai 3 chats
echo "J'ai 3 $animals"      # → J'ai 3  (Bash cherche la variable "animals" qui n'existe pas)


Modifier une variable
Tu peux changer la valeur à tout moment :

#!/bin/bash
humeur="content"
echo "Je suis $humeur"

humeur="fatigué"
echo "Maintenant je suis $humeur"


Guillemets simples vs doubles

prenom="Alice"

echo "Bonjour, $prenom"    # Guillemets doubles → Bash remplace la variable
# → Bonjour, Alice

echo 'Bonjour, $prenom'    # Guillemets simples → tout est affiché tel quel
# → Bonjour, $prenom


À retenir :
	∙	Guillemets doubles " " → Bash interprète les variables
	∙	Guillemets simples ' ' → tout est littéral, aucune interprétation
Lire une saisie utilisateur avec read
La commande read demande à l’utilisateur de taper quelque chose :

#!/bin/bash

read -p "Ton prénom : " prenom
read -p "Ton âge : " age
echo "Tu es $prenom et tu as $age ans."


Exécution :

Ton prénom : Alice
Ton âge : 25
Tu es Alice et tu as 25 ans.


-p permet de mettre le message et la saisie sur la même ligne. C’est la forme la plus pratique.
Très utile en pratique
La substitution de commande
Tu peux stocker le résultat d’une commande dans une variable avec $(commande) :

#!/bin/bash

aujourdhui=$(date)
echo "Nous sommes le : $aujourdhui"

utilisateur=$(whoami)
echo "Connecté en tant que : $utilisateur"

nb_fichiers=$(ls | wc -l)
echo "Il y a $nb_fichiers éléments dans ce dossier"


À retenir : $(commande) exécute la commande et renvoie son résultat. C’est l’une des fonctionnalités les plus puissantes de Bash.
Les variables d’environnement
Ton système contient des variables déjà définies :

echo "Utilisateur : $USER"
echo "Dossier personnel : $HOME"
echo "Shell actuel : $SHELL"
echo "Dossier actuel : $PWD"


Variables en lecture seule
Pour qu’une variable ne puisse jamais être modifiée :

readonly PI=3.14159
PI=3.0    # → Erreur ! bash: PI: readonly variable


Bonus
Note sur les “types” en Bash
En Bash, une variable contient surtout du texte. Même les nombres sont manipulés comme du texte, sauf quand tu fais du calcul (chapitre 5). Il n’y a pas de système de types strict comme dans d’autres langages. Ne te préoccupe pas de ça pour l’instant.
Autres options de read

read -p "Mot de passe : " -s motdepasse    # -s : saisie invisible
read -p "Choix rapide : " -t 5 choix        # -t 5 : timeout de 5 secondes


❌ Erreur classique

prenom = "Alice"     # ❌ Espaces autour du = → Bash croit que "prenom" est une commande
prenom="Alice"       # ✅ Correct

echo $prenom         # ⚠️ Fonctionne, mais risqué si la valeur contient des espaces
echo "$prenom"       # ✅ Toujours préférer cette forme


Exercices
Guidé : Crée un script presentation.sh qui demande le prénom et l’âge avec read -p, puis affiche “Tu es [prénom] et tu as [âge] ans.”
Autonome : Crée un script machine.sh qui affiche le nom de l’utilisateur, la date et le nom de la machine (hostname) en utilisant la substitution de commande $(...).
🧩 Mini-projet (chapitres 1-2)
Crée un script bienvenue.sh qui :
	1.	Affiche “Bienvenue sur cette machine !”
	2.	Affiche la date du jour (avec substitution de commande)
	3.	Demande le prénom de l’utilisateur
	4.	Affiche “Bonjour [prénom], connecté en tant que [whoami]”
✅ Tu sais maintenant…
	∙	Créer une variable et l’afficher avec $
	∙	La différence entre guillemets simples et doubles
	∙	Lire une saisie utilisateur avec read -p
	∙	Stocker le résultat d’une commande avec $(commande)

Chapitre 3 — Arguments et variables spéciales
Le minimum à savoir
C’est quoi un argument ?
Au lieu que le script pose des questions (avec read), tu peux lui donner des infos directement quand tu le lances :

./saluer.sh Alice
#                 ↑ c'est un argument


Les paramètres positionnels
Chaque argument est stocké dans une variable numérotée :

./mon_script.sh  pomme   banane  cerise
       $0          $1      $2      $3


	∙	$0 → le nom du script
	∙	$1 → le premier argument
	∙	$2 → le deuxième
	∙	$3 → le troisième…
Exemple :

#!/bin/bash
echo "Bonjour, $1 !"


./saluer.sh Alice     # → Bonjour, Alice !
./saluer.sh Bob       # → Bonjour, Bob !


Les variables spéciales essentielles



|Variable   |Contenu                                      |
|-----------|---------------------------------------------|
|`$0`       |Le nom du script                             |
|`$1`, `$2`…|Les arguments par position                   |
|`$#`       |Le **nombre** d’arguments                    |
|`$@`       |**Tous** les arguments (séparément)          |
|`$?`       |Le **code de sortie** de la dernière commande|

Exemple :

#!/bin/bash

echo "Nom du script : $0"
echo "Nombre d'arguments : $#"
echo "Tous les arguments : $@"
echo "Premier : $1"
echo "Deuxième : $2"


./infos.sh pomme banane cerise


Nom du script : ./infos.sh
Nombre d'arguments : 3
Tous les arguments : pomme banane cerise
Premier : pomme
Deuxième : banane


Vérifier qu’un argument est fourni
Un script qui attend un argument devrait toujours vérifier qu’il a été donné :

#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Erreur : donne un prénom en argument !"
    echo "Utilisation : $0 <prénom>"
    exit 1
fi

echo "Bonjour, $1 !"


Explication : -z teste si la chaîne est vide. Si $1 est vide (= pas d’argument), on affiche un message d’erreur et on quitte. On verra les conditions en détail au chapitre 6.
La variable $?
Chaque commande renvoie un code de sortie. $? contient le code de la dernière commande :

ls /tmp
echo $?           # → 0 (succès, le dossier existe)

ls /dossier_inexistant
echo $?           # → 2 (erreur, le dossier n'existe pas)


Très utile en pratique
Utiliser plusieurs arguments

#!/bin/bash
echo "Comparaison de $1 et $2"
echo "Taille de $1 :"
wc -c < "$1"
echo "Taille de $2 :"
wc -c < "$2"


Bonne pratique : mets toujours "$1" entre guillemets (pas $1 nu). Ça évite les problèmes si le nom de fichier contient des espaces.
Différence entre $@ et $*

./test.sh "Jean Pierre" Marie


	∙	"$@" → préserve chaque argument : "Jean Pierre" et "Marie" (2 éléments)
	∙	"$*" → fusionne tout : "Jean Pierre Marie" (1 seul bloc)
Utilise "$@" dans la grande majorité des cas.
Bonus
La variable $$
$$ contient le numéro de processus (PID) du script. Utile pour créer des fichiers temporaires uniques :

fichier_temp="/tmp/script_$$.tmp"


La commande shift
shift décale tous les arguments d’une position : $2 devient $1, $3 devient $2, etc. On l’utilisera au chapitre 8 pour parser des options avancées.
❌ Erreur classique

# Oublier de vérifier si l'argument existe
echo "Bonjour, $1"    # Si lancé sans argument → "Bonjour, " (chaîne vide, pas d'erreur)

# Ne pas mettre de guillemets
cat $1                 # ❌ Plante si le fichier s'appelle "mon document.txt"
cat "$1"               # ✅ Correct


Exercices
Guidé : Crée un script bonjour_arg.sh qui prend un prénom en argument, vérifie qu’il est fourni, et affiche “Bonjour, [prénom] !”
Autonome : Crée un script chercher.sh qui prend un nom de fichier en argument et le cherche sur le système : find / -iname "$1" 2>/dev/null
✅ Tu sais maintenant…
	∙	Passer des arguments à un script ($1, $2…)
	∙	Connaître le nombre d’arguments avec $#
	∙	Récupérer tous les arguments avec $@
	∙	Vérifier le code de retour avec $?
	∙	Vérifier qu’un argument existe avant de l’utiliser

Chapitre 4 — Redirections, erreurs et pipes
Le minimum à savoir
Les 3 flux de données
Chaque commande travaille avec trois flux :

                  ┌──────────────┐
  Entrée ───────▶ │   Commande   │ ──▶ 1 = Sortie normale (stdout)
  (clavier)       │              │ ──▶ 2 = Erreurs (stderr)
                  └──────────────┘




|Numéro|Nom                        |Par défaut |
|------|---------------------------|-----------|
|0     |stdin (entrée)             |Le clavier |
|**1** |**stdout (sortie normale)**|**L’écran**|
|**2** |**stderr (erreurs)**       |**L’écran**|

Les redirections permettent de changer la destination de ces flux.
Rediriger la sortie vers un fichier
Écraser avec > :

echo "Bonjour" > message.txt   # Crée le fichier (ou l'écrase !)
ls /etc > liste.txt            # La liste va dans le fichier


Ajouter avec >> :

echo "Ligne 1" > journal.txt       # Crée le fichier
echo "Ligne 2" >> journal.txt      # Ajoute à la suite
echo "Ligne 3" >> journal.txt      # Ajoute encore


À retenir : > écrase, >> ajoute. Confondre les deux = perdre des données.
Rediriger les erreurs

# Les erreurs vont dans un fichier, la sortie normale s'affiche à l'écran
ls /dossier_inexistant 2> erreurs.txt

# Masquer les erreurs en les envoyant dans le "trou noir"
find / -name "mon_fichier" 2>/dev/null


/dev/null est une “poubelle” : tout ce qu’on y envoie disparaît.
Rediriger tout (sortie + erreurs)

# Tout va dans le même fichier
./mon_script.sh > log.txt 2>&1 # > log.txt 2>&1 = "flux 1 va dans log.txt, et flux 2 suit flux 1" → tout finit dans log.txt.

# Tout dans le vide (script silencieux)
./mon_script.sh > /dev/null 2>&1


Explication de 2>&1 : “envoie le flux 2 (erreurs) au même endroit que le flux 1 (sortie normale)”.
Les pipes |
Le pipe envoie la sortie d’une commande comme entrée d’une autre. C’est l’outil le plus puissant de Bash.

# Compter le nombre de fichiers
ls | wc -l

# Chercher un mot dans un résultat
ps aux | grep firefox

# Trier et garder les lignes uniques
cat prenoms.txt | sort | uniq


Chaque commande reçoit la sortie de la précédente. C’est une chaîne de traitement.
Note : ces exemples sont volontairement simples pour comprendre le principe d’un pipe. Tu verras plus tard qu’en Bash, certaines alternatives sont plus robustes selon le contexte.
La commande tee
tee permet d’afficher ET sauvegarder en même temps :

# Affiche à l'écran ET écrit dans log.txt
ls -la | tee log.txt

# Ajouter au fichier (au lieu d'écraser)
date | tee -a journal.log


Très utile en pratique
Rediriger l’entrée avec <

# Compter les lignes d'un fichier
wc -l < mon_fichier.txt

# Trier le contenu d'un fichier
sort < liste_noms.txt


Enchaîner plusieurs pipes

# Les 5 plus gros fichiers
ls -lS | head -5

# Compter les fichiers .txt dans /etc
ls /etc | grep "\.txt" | wc -l


Récapitulatif



|Syntaxe                    |Effet                          |
|---------------------------|-------------------------------|
|`commande > fichier`       |Sortie dans fichier (écrase)   |
|`commande >> fichier`      |Sortie dans fichier (ajoute)   |
|`commande 2> fichier`      |Erreurs dans fichier           |
|`commande > fichier 2>&1`  |Tout dans fichier              |
|`commande < fichier`       |Entrée depuis un fichier       |
|`cmd1 | cmd2`              |Sortie de cmd1 → entrée de cmd2|
|`commande | tee fichier`   |Affiche ET sauvegarde          |
|`commande > /dev/null 2>&1`|Silence total                  |

❌ Erreur classique

# Confondre > et >> : tu écrases un fichier important !
echo "nouveau" > config.txt     # ❌ Tout l'ancien contenu est perdu
echo "nouveau" >> config.txt    # ✅ Ajoute à la fin

# Oublier 2> : les erreurs s'affichent en vrac et polluent la sortie
find / -name "*.log"            # ❌ Des dizaines de "Permission denied"
find / -name "*.log" 2>/dev/null  # ✅ Erreurs masquées


Exercices
Guidé : Écris le résultat de date dans un fichier log.txt avec >, puis ajoute une deuxième date avec >>. Affiche le contenu avec cat log.txt.
Autonome : Crée un script qui compte le nombre de lignes de /etc/passwd en utilisant un pipe (wc -l), et qui utilise tee pour afficher le résultat ET l’écrire dans un fichier.
🧩 Mini-projet (chapitres 3-4)
Crée un script rapport.sh qui :
	1.	Prend un dossier en argument (vérifie qu’il est fourni)
	2.	Compte le nombre de fichiers dans ce dossier (ls "$1" | wc -l)
	3.	Écrit un mini-rapport dans rapport.txt avec la date, le dossier, et le nombre de fichiers
	4.	Affiche le rapport à l’écran avec cat
✅ Tu sais maintenant…
	∙	Rediriger la sortie vers un fichier (>, >>)
	∙	Rediriger les erreurs (2>, 2>&1)
	∙	Masquer les erreurs avec /dev/null
	∙	Enchaîner des commandes avec le pipe |
	∙	Afficher et sauvegarder en même temps avec tee

Chapitre 5 — Opérateurs, calculs et logique
Le minimum à savoir
Le calcul en Bash
Bash peut faire des calculs avec des nombres entiers. La syntaxe est $(( expression )) :

#!/bin/bash

a=10
b=3

echo "Addition      : $((a + b))"      # 13
echo "Soustraction  : $((a - b))"      # 7
echo "Multiplication: $((a * b))"      # 30
echo "Division      : $((a / b))"      # 3 (entière, pas de virgule !)
echo "Modulo        : $((a % b))"      # 1 (reste de la division)


Attention : la division est entière. 10 / 3 donne 3, pas 3.33.
Stocker un résultat

prix=50
reduction=15
prix_final=$((prix - reduction))
echo "Le prix final est $prix_final euros"


Les opérateurs arithmétiques



|Opérateur|Signification   |Exemple      |Résultat|
|---------|----------------|-------------|--------|
|`+`      |Addition        |`$((5 + 3))` |`8`     |
|`-`      |Soustraction    |`$((5 - 3))` |`2`     |
|`*`      |Multiplication  |`$((5 * 3))` |`15`    |
|`/`      |Division entière|`$((5 / 3))` |`1`     |
|`%`      |Modulo (reste)  |`$((5 % 3))` |`2`     |
|`**`     |Puissance       |`$((2 ** 3))`|`8`     |

Comparer des nombres
Pour tester si un nombre est plus grand, plus petit, égal à un autre :



|Opérateur|Signification    |Moyen mnémotechnique    |
|---------|-----------------|------------------------|
|`-eq`    |Égal             |**eq**ual               |
|`-ne`    |Différent        |**n**ot **e**qual       |
|`-lt`    |Inférieur        |**l**ess **t**han       |
|`-le`    |Inférieur ou égal|**l**ess or **e**qual   |
|`-gt`    |Supérieur        |**g**reater **t**han    |
|`-ge`    |Supérieur ou égal|**g**reater or **e**qual|

age=25
[[ $age -ge 18 ]]    # Est-ce que 25 ≥ 18 ? → Vrai
[[ $age -eq 30 ]]    # Est-ce que 25 = 30 ? → Faux


Ne pas confondre : = sert à affecter une valeur à une variable (age=25). -eq sert à comparer deux nombres dans un test.
Comparer des chaînes de texte



|Opérateur  |Signification               |
|-----------|----------------------------|
|`=` ou `==`|Les chaînes sont identiques |
|`!=`       |Les chaînes sont différentes|
|`-z`       |La chaîne est vide          |
|`-n`       |La chaîne n’est pas vide    |

nom="Alice"
[[ "$nom" == "Alice" ]]    # Vrai
[[ "$nom" != "Bob" ]]      # Vrai
[[ -z "$nom" ]]            # Faux (pas vide)


Les opérateurs logiques



|Opérateur|Signification                               |
|---------|--------------------------------------------|
|`&&`     |ET — les deux conditions doivent être vraies|
|`||`     |OU — au moins une doit être vraie           |
|`!`      |NON — inverse la condition                  |

age=25
[[ $age -ge 18 && $age -le 65 ]]    # Vrai : entre 18 et 65

[[ $age -lt 10 || $age -gt 60 ]]     # Faux : ni < 10, ni > 60

[[ ! $age -lt 18 ]]                   # Vrai : 25 n'est PAS < 18


Raccourcis avec && et || entre commandes

# Si la commande réussit, ALORS fait ceci
mkdir mon_dossier && echo "Dossier créé !"

# Si la commande échoue, ALORS fait cela
cd /inexistant || echo "Le dossier n'existe pas"


Très utile en pratique
Les tests sur les fichiers



|Opérateur   |Signification            |
|------------|-------------------------|
|`-e fichier`|Le fichier existe        |
|`-f fichier`|C’est un fichier normal  |
|`-d fichier`|C’est un dossier         |
|`-s fichier`|Le fichier n’est pas vide|
|`-r fichier`|Le fichier est lisible   |
|`-w fichier`|Le fichier est modifiable|
|`-x fichier`|Le fichier est exécutable|

[[ -f "/etc/passwd" ]]    # Vrai (le fichier existe)
[[ -d "/home" ]]          # Vrai (c'est un dossier)


Incrémenter un compteur

compteur=0
((compteur++))       # → 1
((compteur++))       # → 2
((compteur += 5))    # → 7


Bonus
Le calcul décimal avec bc
Pour les nombres à virgule, utilise bc :

echo "scale=2; 10 / 3" | bc
# → 3.33

resultat=$(echo "scale=2; 10 / 3" | bc)
echo "Le résultat est $resultat"


Comparer avec (( )) (syntaxe mathématique)
Dans les doubles parenthèses, tu peux utiliser les symboles habituels :

a=10
(( a > 5 ))     # Vrai
(( a == 10 ))   # Vrai


Note : dans (( )), pas besoin de $ devant les variables.
🔧 Quand ça plante : lire un code de retour
Quand quelque chose ne marche pas, vérifie $? :

ma_commande
echo "Code de retour : $?"
# 0 = tout va bien, autre chose = problème


❌ Erreur classique

# Confondre = (affectation) et -eq (comparaison)
if [[ $age = 18 ]]; then     # ⚠️ Compare comme du TEXTE, pas un nombre
if [[ $age -eq 18 ]]; then   # ✅ Compare comme un NOMBRE

# Oublier $(( )) pour le calcul
resultat=5+3                  # ❌ resultat vaut le TEXTE "5+3"
resultat=$((5 + 3))           # ✅ resultat vaut le NOMBRE 8


Exercices
Guidé : Crée un script calculatrice.sh qui prend deux nombres en arguments et affiche leur somme, différence et produit.
Autonome : Crée un script est_pair.sh qui prend un nombre en argument et dit s’il est pair ou impair (indice : un nombre est pair si nombre % 2 vaut 0).
✅ Tu sais maintenant…
	∙	Faire des calculs avec $(( ))
	∙	Comparer des nombres (-eq, -lt, -gt…)
	∙	Comparer des chaînes (==, !=, -z, -n)
	∙	Combiner des conditions avec &&, ||, !
	∙	Tester des propriétés de fichiers (-f, -d, -e)

Chapitre 6 — Conditions, comparaisons et tests
Le minimum à savoir
La structure if

if [[ condition ]]; then
    # code si la condition est vraie
fi


Note : fi c’est if à l’envers. C’est la fermeture du bloc.
Exemple simple :

#!/bin/bash

nombre=15
if [[ $nombre -gt 10 ]]; then
    echo "Le nombre est supérieur à 10"
fi


Règles de syntaxe :
	∙	Espace après [[ et avant ]]
	∙	Espace autour de l’opérateur
	∙	then sur la même ligne (avec ;) ou sur la ligne suivante
if...else

#!/bin/bash

nombre=5
if [[ $nombre -gt 10 ]]; then
    echo "Supérieur à 10"
else
    echo "Inférieur ou égal à 10"
fi


if...elif...else

#!/bin/bash

age=$1

if [[ $age -lt 13 ]]; then
    echo "Tu es un enfant."
elif [[ $age -lt 18 ]]; then
    echo "Tu es un adolescent."
elif [[ $age -lt 65 ]]; then
    echo "Tu es un adulte."
else
    echo "Tu es un senior."
fi


À retenir : autant de elif que tu veux, mais un seul else (à la fin), et un seul fi.
Les 6 tests les plus utiles
Pour débuter, ces 6 tests couvrent 90% des besoins :



|Test |Signification                        |Exemple                |
|-----|-------------------------------------|-----------------------|
|`-f` |Le fichier existe                    |`[[ -f "config.txt" ]]`|
|`-d` |Le dossier existe                    |`[[ -d "/home" ]]`     |
|`-e` |Le chemin existe (fichier ou dossier)|`[[ -e "$1" ]]`        |
|`-z` |La chaîne est vide                   |`[[ -z "$nom" ]]`      |
|`-n` |La chaîne n’est pas vide             |`[[ -n "$nom" ]]`      |
|`-gt`|Le nombre est supérieur              |`[[ $a -gt $b ]]`      |

Exemple concret : vérifier un fichier

#!/bin/bash

fichier=$1

if [[ -z "$fichier" ]]; then
    echo "Erreur : donne un chemin en argument."
    exit 1
fi

if [[ -f "$fichier" ]]; then
    echo "$fichier est un fichier."
elif [[ -d "$fichier" ]]; then
    echo "$fichier est un dossier."
else
    echo "$fichier n'existe pas."
fi


Combiner des conditions

#!/bin/bash

age=$1
nom=$2

# ET : les deux doivent être vraies
if [[ $age -ge 18 && "$nom" == "Alice" ]]; then
    echo "Alice est majeure."
fi

# OU : au moins une doit être vraie
if [[ $age -lt 10 || $age -gt 80 ]]; then
    echo "Âge extrême."
fi


Très utile en pratique
Les conditions imbriquées
Tu peux mettre un if dans un autre if :

#!/bin/bash

temperature=$1

if [[ $temperature -gt 0 ]]; then
    if [[ $temperature -lt 15 ]]; then
        echo "Il fait frais."
    elif [[ $temperature -lt 25 ]]; then
        echo "Il fait bon."
    else
        echo "Il fait chaud."
    fi
else
    echo "Il gèle !"
fi


Conseil : si tes conditions imbriquées dépassent 2-3 niveaux, c’est signe qu’il faut simplifier.
[ ] vs [[ ]] — ce qu’il faut savoir
Dans ce cours, on utilise [[ ]] (la syntaxe moderne). Mais tu verras souvent [ ] dans des scripts existants sur internet. C’est l’ancienne syntaxe. Elle fonctionne, mais elle est plus fragile (elle plante si une variable est vide et non protégée par des guillemets).

# Avec [ ] — risqué si $nom est vide
[ $nom = "Alice" ]     # ❌ Erreur si $nom est vide

# Avec [[ ]] — pas de problème
[[ $nom == "Alice" ]]  # ✅ Fonctionne même si $nom est vide


Règle simple : utilise [[ ]] dans tes scripts. Si tu vois [ ] ailleurs, sache que c’est l’équivalent en plus ancien.
❌ Erreur classique

# Oublier then
if [[ $a -gt 5 ]]      # ❌ Erreur : "then" manquant
    echo "Grand"
fi

# Oublier les espaces
if [[$a -gt 5]]; then   # ❌ Erreur : pas d'espace
if [[ $a -gt 5 ]]; then # ✅ Correct

# Utiliser > pour comparer des nombres
if [[ $a > $b ]]; then      # ⚠️ Compare comme du TEXTE, pas des nombres
if [[ $a -gt $b ]]; then    # ✅ Compare comme des NOMBRES

# Oublier fi
if [[ $a -gt 5 ]]; then
    echo "Grand"
                             # ❌ Erreur : fi manquant


Exercices
Guidé : Crée un script meteo.sh qui prend une température en argument et affiche “Il gèle” (< 0), “Froid” (0-15), “Bon” (15-25), ou “Chaud” (> 25).
Autonome : Crée un script verifier.sh qui prend un chemin en argument et dit si c’est un fichier, un dossier, ou si ça n’existe pas. Pense à vérifier que l’argument est fourni.
🧩 Mini-projet (chapitres 5-6)
Crée un script acces.sh qui :
	1.	Prend un chemin de fichier en argument
	2.	Vérifie qu’il existe (-e)
	3.	Si c’est un fichier (-f), affiche s’il est lisible (-r), modifiable (-w) et exécutable (-x)
	4.	Si c’est un dossier (-d), compte le nombre d’éléments qu’il contient (ls "$1" | wc -l)
✅ Tu sais maintenant…
	∙	Écrire des conditions avec if / elif / else / fi
	∙	Utiliser [[ ]] pour les tests
	∙	Tester des fichiers (-f, -d, -e)
	∙	Combiner des conditions avec && et ||
	∙	La différence entre [[ ]] (moderne) et [ ] (ancien)

Chapitre 7 — Boucles
Le minimum à savoir
À quoi servent les boucles ?
Les boucles répètent des actions. Tu dois renommer 200 fichiers ? Vérifier 50 serveurs ? Tu n’écris pas 200 commandes : tu écris une boucle.
Il y a deux façons de penser :
	∙	for = répéter sur une liste d’éléments
	∙	while = répéter tant qu’une condition est vraie
La boucle for
Parcourir une liste de mots :

#!/bin/bash

for fruit in pomme banane cerise; do
    echo "J'aime la $fruit"
done


J'aime la pomme
J'aime la banane
J'aime la cerise


Parcourir une plage de nombres :

for i in {1..5}; do
    echo "Tour numéro $i"
done


Parcourir des fichiers (le cas le plus courant) :

#!/bin/bash

for fichier in *.txt; do
    echo "Traitement de $fichier"
done


À retenir : for fichier in *.txt parcourt tous les fichiers .txt du dossier actuel. C’est la façon propre et sûre de parcourir des fichiers.
Parcourir avec un pas :

# Compter de 2 en 2
for i in {0..10..2}; do
    echo $i
done
# → 0, 2, 4, 6, 8, 10


La boucle while

#!/bin/bash

compteur=1
while [[ $compteur -le 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done


Compteur : 1
Compteur : 2
Compteur : 3
Compteur : 4
Compteur : 5


Attention : si tu oublies ((compteur++)), la boucle tourne à l’infini ! Appuie sur Ctrl+C pour l’arrêter.
Lire un fichier ligne par ligne :

#!/bin/bash

while read -r ligne; do
    echo "Lu : $ligne"
done < mon_fichier.txt


Note : -r empêche read d’interpréter les caractères spéciaux comme \. C’est une bonne pratique.
break et continue
break — sortir de la boucle :

for i in {1..10}; do
    if [[ $i -eq 6 ]]; then
        echo "Stop à $i"
        break
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 3, 4, 5 puis "Stop à 6"


continue — sauter au tour suivant :

for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 4, 5 (le 3 est sauté)


Très utile en pratique
Le for style C (pour les plages dynamiques)
La syntaxe {1..5} ne fonctionne pas avec des variables. Pour ça :

#!/bin/bash

limite=$1
for (( i=1; i<=limite; i++ )); do
    echo "Tour $i"
done


Les boucles imbriquées

#!/bin/bash

for i in {1..3}; do
    for j in {1..3}; do
        echo "i=$i, j=$j"
    done
done


Attention aux boucles infinies

# ❌ BOUCLE INFINIE — le compteur ne change jamais
compteur=1
while [[ $compteur -le 5 ]]; do
    echo $compteur
    # Oubli de ((compteur++)) !
done


Si ça t’arrive : Ctrl+C pour arrêter.
Boucle infinie volontaire (parfois utile) :

while true; do
    echo "En attente..."
    sleep 5
done


Bonus
La boucle until
until est l’inverse de while : elle boucle tant que la condition est fausse :

compteur=1
until [[ $compteur -gt 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done


En pratique, while est beaucoup plus courant. until est juste une autre façon d’écrire certaines boucles.
🔧 Quand ça plante : déboguer une boucle
Ajoute des echo temporaires pour voir ce qui se passe :

for fichier in *.txt; do
    echo "[DEBUG] fichier = '$fichier'"    # ← ajoute ça
    # ... le reste du code
done


Si tu ne vois aucun [DEBUG], c’est que la boucle ne s’exécute pas (peut-être qu’il n’y a aucun .txt dans le dossier).
❌ Erreur classique

# Oublier do
for i in {1..5};        # ❌ "do" manquant
    echo $i
done

# Oublier done
for i in {1..5}; do
    echo $i
                        # ❌ "done" manquant

# Boucle infinie par oubli d'incrément
while [[ $n -le 10 ]]; do
    echo $n
    # ← Il faut ((n++)) ici !
done


Exercices
Guidé : Crée un script qui affiche les nombres de 1 à 10, un par ligne. Utilise une boucle for avec {1..10}.
Autonome : Crée un script qui lit un fichier texte ligne par ligne et affiche chaque ligne précédée de son numéro (indice : utilise un compteur avec ((numero++))).
Défi : Crée un script qui affiche la table de multiplication d’un nombre donné en argument (de 1 à 10).
✅ Tu sais maintenant…
	∙	Parcourir une liste ou des fichiers avec for
	∙	Répéter tant qu’une condition est vraie avec while
	∙	Lire un fichier ligne par ligne
	∙	Contrôler une boucle avec break et continue
	∙	Éviter et arrêter les boucles infinies

Chapitre 8 — Fonctions et case
Le minimum à savoir
Qu’est-ce qu’une fonction ?
Une fonction, c’est un bloc de code réutilisable auquel tu donnes un nom. Au lieu de copier-coller les mêmes lignes, tu les mets dans une fonction et tu l’appelles par son nom.
Définir et appeler une fonction

#!/bin/bash

# 1. Définir la fonction
saluer() {
    echo "Salut, bienvenue !"
}

# 2. L'appeler (juste son nom, sans parenthèses)
saluer
saluer


Salut, bienvenue !
Salut, bienvenue !


Règle : la définition doit apparaître AVANT l’appel dans le script.
Passer des arguments à une fonction
À l’intérieur de la fonction, $1, $2… sont les arguments de la fonction (pas du script) :

#!/bin/bash

saluer() {
    echo "Bonjour, $1 ! Tu as $2 ans."
}

saluer "Alice" 25
saluer "Bob" 30


Bonjour, Alice ! Tu as 25 ans.
Bonjour, Bob ! Tu as 30 ans.


Récupérer le résultat d’une fonction
En Bash, une fonction renvoie un résultat en l’affichant avec echo. On le récupère avec $(...) :

#!/bin/bash

addition() {
    echo $(( $1 + $2 ))
}

resultat=$(addition 15 27)
echo "La somme est : $resultat"


À retenir : return ne sert PAS à renvoyer une chaîne ou un nombre. Il sert uniquement à donner un code de succès (0) ou d’erreur (1). Pour renvoyer un résultat, utilise echo + $(...).
Le case : choix multiples propres
Le case teste une variable contre plusieurs valeurs possibles. C’est plus lisible que des enchaînements de elif :

#!/bin/bash

case $1 in
    oui|o|yes|y)
        echo "Tu as dit oui." ;;
    non|n|no)
        echo "Tu as dit non." ;;
    *)
        echo "Réponse non reconnue." ;;
esac


Notes :
	∙	esac c’est case à l’envers (fermeture du bloc)
	∙	Chaque bloc se termine par ;;
	∙	* est le cas par défaut (si rien d’autre ne correspond)
	∙	| sépare plusieurs patterns pour le même bloc
Très utile en pratique
Fonctions + case = script avec des options

#!/bin/bash

afficher_aide() {
    echo "Utilisation : $0 [option]"
    echo "  -l    Lister les fichiers"
    echo "  -d    Afficher la date"
    echo "  -h    Afficher cette aide"
}

case $1 in
    -l) ls -la ;;
    -d) date ;;
    -h) afficher_aide ;;
    "")
        echo "Erreur : aucune option fournie."
        afficher_aide
        exit 1 ;;
    *)
        echo "Option '$1' inconnue."
        afficher_aide
        exit 1 ;;
esac


./outil.sh -l      # Liste les fichiers
./outil.sh -d      # Affiche la date
./outil.sh -h      # Affiche l'aide
./outil.sh -z      # "Option '-z' inconnue."


Variables locales
Par défaut, les variables dans une fonction sont globales. Pour les limiter à la fonction, utilise local :

#!/bin/bash

nom="Global"

modifier() {
    local nom="Local"
    echo "Dans la fonction : $nom"
}

echo "Avant : $nom"    # → Global
modifier               # → Local
echo "Après : $nom"    # → Global (pas affecté)


Bonne pratique : utilise toujours local pour les variables internes d’une fonction.
Valeurs par défaut pour les arguments
${1:-"valeur"} signifie : utilise $1 s’il existe, sinon prends "valeur".

saluer() {
    local nom=${1:-"Inconnu"}
    echo "Bonjour, $nom !"
}

saluer "Alice"    # → Bonjour, Alice !
saluer            # → Bonjour, Inconnu !


Le code de retour d’une fonction (return)

fichier_existe() {
    if [[ -f "$1" ]]; then
        return 0    # Succès
    else
        return 1    # Échec
    fi
}

if fichier_existe "/etc/passwd"; then
    echo "Le fichier existe."
else
    echo "Le fichier n'existe pas."
fi


Bonus
Menu interactif avec select
select crée automatiquement un menu numéroté :

#!/bin/bash

echo "Que veux-tu faire ?"
select choix in "Lister les fichiers" "Afficher la date" "Quitter"; do
    case $choix in
        "Lister les fichiers") ls ;;
        "Afficher la date") date ;;
        "Quitter") echo "Au revoir." ; break ;;
        *) echo "Choix invalide." ;;
    esac
done


Parser des arguments nommés avec shift
Pour les scripts avec des flags comme -n 42 -s "texte" :

#!/bin/bash

while [[ $# -gt 0 ]]; do
    case $1 in
        -n) nombre="$2" ; shift 2 ;;
        -s) texte="$2" ; shift 2 ;;
        -h) echo "Aide : $0 -n <nombre> -s <texte>" ; exit 0 ;;
        *) echo "Option inconnue : $1" ; exit 1 ;;
    esac
done

echo "Nombre : $nombre"
echo "Texte : $texte"


Note : shift décale les arguments : l’ancien $2 devient $1. shift 2 décale de 2 positions. C’est comme ça qu’on “consomme” les flags un par un.
❌ Erreur classique

# Croire que return renvoie une chaîne
ma_fonction() {
    return "Hello"     # ❌ return ne prend qu'un nombre (0-255)
}

# Il faut utiliser echo :
ma_fonction() {
    echo "Hello"       # ✅ On capture avec $(ma_fonction)
}

# Appeler une fonction avec des parenthèses
saluer()               # ❌ Les parenthèses sont pour la DÉFINITION
saluer                 # ✅ Pour appeler, juste le nom


Exercices
Guidé : Crée une fonction maximum qui prend deux nombres et affiche le plus grand. Teste-la avec echo "Le max est $(maximum 10 25)".
Autonome : Crée un script outil.sh avec les options -l (lister les fichiers), -d (afficher la date), -u (afficher l’utilisateur) en utilisant case et des fonctions.
🧩 Mini-projet (chapitres 7-8)
Crée un script gestion.sh qui :
	1.	Propose un menu avec case : 1) Lister les fichiers .txt, 2) Compter les lignes d’un fichier, 3) Quitter
	2.	Chaque option appelle une fonction dédiée
	3.	La boucle while true permet de revenir au menu après chaque action
	4.	L’option “Quitter” utilise break pour sortir
✅ Tu sais maintenant…
	∙	Définir, appeler et passer des arguments à une fonction
	∙	Récupérer un résultat avec echo + $(...) (et non avec return)
	∙	Utiliser case pour des choix multiples propres
	∙	Protéger les variables internes avec local

Chapitre 9 — Chaînes de caractères
Le minimum à savoir
Longueur d’une chaîne

mot="Bonjour"
echo ${#mot}       # → 7


Concaténation (coller des chaînes)

debut="Bon"
fin="jour"
mot=$debut$fin
echo "$mot"        # → Bonjour


Extraire une sous-chaîne

phrase="Bash est génial"

echo "${phrase:0:4}"     # → Bash     (4 caractères depuis la position 0)
echo "${phrase:5:3}"     # → est      (3 caractères depuis la position 5)
echo "${phrase:9}"       # → génial   (tout depuis la position 9)


Rappel : les positions commencent à 0.
Remplacer dans une chaîne

phrase="J'adore les pommes"

# Remplacer la première occurrence
echo "${phrase/pommes/bananes}"
# → J'adore les bananes

# Remplacer TOUTES les occurrences (double slash)
tel="01-23-45-67-89"
echo "${tel//-/.}"
# → 01.23.45.67.89


Supprimer dans une chaîne
Supprimer, c’est remplacer par rien :

tel="01-23-45-67-89"

# Supprimer tous les tirets
echo "${tel//-/}"
# → 0123456789


Majuscules et minuscules

nom="alice dupont"
NOM="ALICE DUPONT"

echo "${nom^^}"          # → ALICE DUPONT  (tout en majuscules)
echo "${NOM,,}"          # → alice dupont  (tout en minuscules)
echo "${nom^}"           # → Alice dupont  (première lettre en majuscule)


Très utile en pratique
Tester si une chaîne est vide

nom=""
[[ -z "$nom" ]] && echo "Nom est vide"       # → Nom est vide

autre="Alice"
[[ -n "$autre" ]] && echo "Autre n'est pas vide"  # → Autre n'est pas vide


Récapitulatif



|Syntaxe                 |Effet                           |
|------------------------|--------------------------------|
|`${#var}`               |Longueur                        |
|`${var:pos:len}`        |Extraire une sous-chaîne        |
|`${var/ancien/nouveau}` |Remplacer la 1ère occurrence    |
|`${var//ancien/nouveau}`|Remplacer toutes les occurrences|
|`${var//ancien/}`       |Supprimer toutes les occurrences|
|`${var^^}`              |Tout en majuscules              |
|`${var,,}`              |Tout en minuscules              |
|`${var^}`               |1ère lettre en majuscule        |

Bonus
Extraire l’extension d’un fichier

fichier="rapport.tar.gz"
echo "${fichier##*.}"    # → gz (tout après le dernier .)
echo "${fichier%.*}"     # → rapport.tar (tout avant le dernier .)


Pattern matching avancé

# Supprimer un préfixe
chemin="/home/user/documents/fichier.txt"
echo "${chemin##*/}"     # → fichier.txt (garde juste le nom)

# Supprimer un suffixe
echo "${chemin%/*}"      # → /home/user/documents (garde juste le dossier)


❌ Erreur classique

# Oublier les accolades
echo "$phrase:0:4"       # ❌ Affiche le contenu de $phrase suivi de ":0:4"
echo "${phrase:0:4}"     # ✅ Extrait correctement

# Confondre / et //
echo "${tel/-/}"         # Supprime seulement le PREMIER tiret
echo "${tel//-/}"        # Supprime TOUS les tirets


Exercices
Guidé : Crée un script qui prend un numéro de téléphone avec des tirets (01-23-45-67-89) et l’affiche reformaté avec des points (01.23.45.67.89).
Autonome : Crée un script qui prend une phrase en argument et affiche sa longueur, la phrase en majuscules, et la phrase en minuscules.
✅ Tu sais maintenant…
	∙	Mesurer la longueur d’une chaîne
	∙	Extraire, remplacer et supprimer des parties de chaîne
	∙	Convertir entre majuscules et minuscules
	∙	Les syntaxes ${var/...} et ${var^^}/${var,,}

Chapitre 10 — Tableaux
Note : les tableaux sont utiles, mais pas indispensables pour commencer à automatiser. Tu peux écrire beaucoup de scripts sans en avoir besoin. Ce chapitre t’équipe pour le jour où tu en auras besoin. Si ce chapitre te semble flou au premier passage, passe au suivant et reviens-y quand tu en auras besoin dans un vrai script.
Le minimum à savoir
Créer un tableau
Un tableau stocke plusieurs valeurs dans une seule variable. Chaque valeur a un index qui commence à 0.

fruits=("pomme" "banane" "cerise")


Index :     0         1         2
         ┌─────┐  ┌──────┐  ┌──────┐
         │pomme│  │banane│  │cerise│
         └─────┘  └──────┘  └──────┘


Accéder aux éléments

fruits=("pomme" "banane" "cerise")

echo "${fruits[0]}"      # → pomme
echo "${fruits[1]}"      # → banane
echo "${fruits[@]}"      # → pomme banane cerise (tout)
echo "${#fruits[@]}"     # → 3 (le nombre d'éléments)


Ajouter un élément

fruits+=("kiwi")
echo "${fruits[@]}"      # → pomme banane cerise kiwi


Modifier un élément

fruits[1]="fraise"
echo "${fruits[@]}"      # → pomme fraise cerise kiwi


Supprimer un élément

unset fruits[1]
echo "${fruits[@]}"      # → pomme cerise kiwi


Parcourir un tableau

#!/bin/bash

fruits=("pomme" "banane" "cerise" "kiwi")

for fruit in "${fruits[@]}"; do
    echo "Fruit : $fruit"
done


Très utile en pratique
Parcourir avec les index

for i in "${!fruits[@]}"; do
    echo "Index $i : ${fruits[$i]}"
done


Tableaux multi-types
Un tableau Bash peut contenir des valeurs de types différents :

infos=("Alice" 25 "Paris" "admin")

echo "Nom  : ${infos[0]}"
echo "Âge  : ${infos[1]}"
echo "Ville: ${infos[2]}"
echo "Rôle : ${infos[3]}"


Récapitulatif



|Syntaxe            |Effet                |
|-------------------|---------------------|
|`tab=("a" "b" "c")`|Créer un tableau     |
|`${tab[0]}`        |Accéder à l’élément 0|
|`${tab[@]}`        |Tous les éléments    |
|`${#tab[@]}`       |Nombre d’éléments    |
|`${!tab[@]}`       |Tous les index       |
|`tab+=("d")`       |Ajouter un élément   |
|`tab[1]="x"`       |Modifier un élément  |
|`unset tab[1]`     |Supprimer un élément |

Bonus
Les tableaux associatifs (dictionnaires)
Les tableaux associatifs utilisent des clés nommées au lieu d’index numériques. C’est comme un dictionnaire : chaque mot (clé) a une définition (valeur).

# OBLIGATOIRE : declare -A
declare -A capitales

capitales[France]="Paris"
capitales[Allemagne]="Berlin"
capitales[Espagne]="Madrid"

echo "${capitales[France]}"       # → Paris
echo "${!capitales[@]}"           # → France Allemagne Espagne (les clés)

# Parcourir
for pays in "${!capitales[@]}"; do
    echo "La capitale de $pays est ${capitales[$pays]}"
done


Prérequis : Bash 4.0+ (bash --version pour vérifier). Le declare -A est obligatoire, sinon Bash crée un tableau indexé normal.
❌ Erreur classique

# Oublier les accolades et l'[@]
echo $fruits         # ❌ N'affiche que le premier élément
echo "${fruits[@]}"  # ✅ Affiche tout

# Oublier les guillemets dans une boucle
for f in ${fruits[@]}; do     # ❌ Problème si un élément contient des espaces
for f in "${fruits[@]}"; do   # ✅ Correct


Exercices
Guidé : Crée un tableau avec 5 prénoms, puis affiche-les numérotés avec une boucle for et un compteur.
Autonome : Crée un script qui prend des noms en arguments ($@), les stocke dans un tableau, et les affiche triés (indice : tu peux utiliser un pipe avec sort).
🧩 Mini-projet (chapitres 9-10)
Crée un script contacts.sh qui :
	1.	Contient un tableau de noms : noms=("Alice" "Bob" "Charlie")
	2.	Contient un tableau d’emails correspondants : emails=("alice@mail.com" "bob@mail.com" "charlie@mail.com")
	3.	Affiche chaque contact sous la forme “Nom : Alice — Email : alice@mail.com”
	4.	Demande à l’utilisateur un numéro et affiche le contact correspondant
✅ Tu sais maintenant…
	∙	Créer, modifier et parcourir un tableau indexé
	∙	Accéder aux éléments par leur index
	∙	Ajouter et supprimer des éléments
	∙	(Bonus) Utiliser des tableaux associatifs

Chapitre 11 — Déboguer et écrire des scripts propres
Le minimum à savoir
Les echo de débogage
La méthode la plus simple : ajouter des echo pour voir les valeurs en cours de route :

#!/bin/bash

fichier=$1
echo "[DEBUG] fichier = '$fichier'"

if [[ -f "$fichier" ]]; then
    echo "[DEBUG] Le fichier existe"
    nb_lignes=$(wc -l < "$fichier")
    echo "[DEBUG] nb_lignes = '$nb_lignes'"
fi


Astuce : utilise le préfixe [DEBUG] pour retrouver facilement tes messages et les supprimer une fois le bug corrigé.
Utiliser echo pour voir ce que contient une variable ou pour suivre l’exécution d’un script, c’est une méthode normale, simple, et utilisée par tout le monde — même les développeurs expérimentés. Ce n’est pas du bricolage, c’est du débogage.
Lire un message d’erreur
Les messages d’erreur de Bash suivent ce format :

./mon_script.sh: line 12: commande: command not found


	∙	./mon_script.sh → quel fichier
	∙	line 12 → quelle ligne
	∙	command not found → quel problème
Le mode trace avec bash -x
-x affiche chaque commande avant de l’exécuter, avec les variables remplacées par leurs valeurs :

bash -x mon_script.sh


Tu peux aussi l’activer/désactiver dans le script :

#!/bin/bash
set -x          # Active la trace
echo "Ceci sera tracé"
nombre=$((5 + 3))
set +x          # Désactive la trace
echo "Ceci ne sera plus tracé"


Sortie :

+ echo 'Ceci sera tracé'
Ceci sera tracé
+ nombre=8
+ set +x
Ceci ne sera plus tracé


Les 5 erreurs de débutant les plus fréquentes



|Erreur                  |Message                  |Solution                                      |
|------------------------|-------------------------|----------------------------------------------|
|Espaces autour de `=`   |`command not found`      |`var="valeur"` (pas d’espace)                 |
|`then` ou `fi` oublié   |`syntax error`           |Vérifie chaque `if` a son `then` et son `fi`  |
|`do` ou `done` oublié   |`syntax error`           |Vérifie chaque boucle a son `do` et son `done`|
|Guillemets oubliés      |`unary operator expected`|Mets `"$var"` au lieu de `$var`               |
|`-eq` confondu avec `==`|Résultat inattendu       |`-eq` pour nombres, `==` pour texte           |

Très utile en pratique
Vérifier les arguments en début de script

#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Erreur : argument manquant" >&2
    echo "Utilisation : $0 <fichier>" >&2
    exit 1
fi


Note : >&2 envoie le message vers stderr (la sortie d’erreur). C’est la bonne pratique pour les messages d’erreur.
Noms de variables descriptifs

# ❌ Incompréhensible
a=5
b="txt"

# ✅ Clair
nombre_fichiers=5
extension="txt"


Structurer avec des fonctions

# ❌ Script monolithique de 200 lignes

# ✅ Script structuré
verifier_arguments() { ... }
traiter_fichier() { ... }
generer_rapport() { ... }

verifier_arguments "$@"
traiter_fichier "$1"
generer_rapport


Commenter ton code

#!/bin/bash
# Ce script sauvegarde les fichiers de configuration
# Usage : ./backup.sh <dossier_destination>


Toujours mettre les variables entre guillemets

cat $fichier       # ❌ Dangereux si $fichier contient des espaces
cat "$fichier"     # ✅ Sûr


Bonus
set -e : arrêt sur erreur
Par défaut, Bash continue même quand une commande échoue. set -e change ça :

#!/bin/bash
set -e

echo "Étape 1"
cd /dossier_inexistant     # ← Erreur ! Le script s'arrête ici
echo "Étape 2"             # ← Jamais exécuté


C’est utile pour les scripts importants, mais attention : ça peut aussi arrêter le script sur des erreurs “attendues”. Utilise-le quand tu maîtrises bien ton script.
set -u : erreur si variable non définie

#!/bin/bash
set -u

echo "Mon nom est $nom"    # ← Erreur ! $nom n'est pas défini


La combinaison set -euo pipefail
Beaucoup de développeurs expérimentés utilisent :

#!/bin/bash
set -euo pipefail


	∙	-e : arrêt sur erreur
	∙	-u : erreur si variable non définie
	∙	-o pipefail : un pipe échoue si n’importe quelle commande du pipe échoue
C’est un filet de sécurité puissant, mais à utiliser quand tu es à l’aise avec les bases. Ne te force pas à le mettre dans tes premiers scripts.
❌ Erreur classique

# Laisser des echo [DEBUG] dans le script final
echo "[DEBUG] valeur = $x"    # ← Pense à les supprimer !

# Ne pas tester le script avec des cas limites
./script.sh ""                # Que se passe-t-il avec un argument vide ?
./script.sh "fichier avec espaces.txt"   # Et avec des espaces ?


Exercices
Guidé : Prends un de tes scripts précédents et lance-le avec bash -x. Observe les lignes précédées de +.
Autonome : Crée un script volontairement bugué (variable mal nommée, fi manquant, variable vide…) et corrige les erreurs en lisant les messages d’erreur.
✅ Tu sais maintenant…
	∙	Déboguer avec echo [DEBUG] et bash -x
	∙	Lire et comprendre les messages d’erreur
	∙	Les 5 erreurs les plus fréquentes
	∙	Les bonnes pratiques : guillemets, noms clairs, commentaires, fonctions
	∙	(Bonus) set -e, set -u, set -euo pipefail

Chapitre 12 — Cas pratiques et automatisation
Jusqu’ici, tu as appris les briques du scripting Bash une par une. Maintenant, on les combine dans de vrais petits scripts, proches de situations réelles. C’est ici que tout prend son sens.
Penser comme un automaticien
Avant d’écrire un script d’automatisation, pose-toi trois questions :
	1.	Qu’est-ce que je fais à la main régulièrement ?
	2.	Est-ce que c’est toujours les mêmes étapes ?
	3.	Est-ce que ça pourrait tourner tout seul ?
Si oui aux trois → c’est un bon candidat pour un script.
Cas pratique 1 — Journaliser et accueillir
Un script simple qui journalise les connexions :

#!/bin/bash

LOG="$HOME/connexions.log"

utilisateur=$(whoami)
date_heure=$(date '+%Y-%m-%d %H:%M:%S')

echo "Bienvenue, $utilisateur !"
echo "[$date_heure] Connexion de $utilisateur" >> "$LOG"
echo "Connexion enregistrée dans $LOG"


Ce script illustre : variables, substitution de commande, redirection >>.
Cas pratique 2 — Tester des fichiers/dossiers
Un script qui vérifie l’état d’une liste de chemins :

#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Utilisation : $0 <chemin1> [chemin2] ..." >&2
    exit 1
fi

for chemin in "$@"; do
    if [[ -f "$chemin" ]]; then
        taille=$(wc -c < "$chemin")
        echo "✓ $chemin — fichier ($taille octets)"
    elif [[ -d "$chemin" ]]; then
        nb=$(ls "$chemin" | wc -l)
        echo "✓ $chemin — dossier ($nb éléments)"
    else
        echo "✗ $chemin — n'existe pas"
    fi
done


Ce script illustre : arguments, boucle for, conditions, tests de fichiers, pipes.
Cas pratique 3 — Sauvegarder des dossiers

#!/bin/bash

# --- Configuration ---
dossiers=("/etc" "/home")
destination="/tmp/backups"
date_du_jour=$(date +%Y-%m-%d)

# --- Préparation ---
mkdir -p "$destination"

echo "=== Sauvegarde du $date_du_jour ==="

for dossier in "${dossiers[@]}"; do
    nom_archive=$(echo "$dossier" | tr '/' '_')
    fichier="${destination}/${nom_archive}-${date_du_jour}.tar.gz"

    echo -n "Sauvegarde de $dossier ... "

    if tar -czf "$fichier" "$dossier" 2>/dev/null; then
        taille=$(du -h "$fichier" | cut -f1)
        echo "OK ($taille)"
    else
        echo "ERREUR" >&2
    fi
done

echo "=== Terminé ==="


Ce script illustre : tableaux, boucle for, conditions, redirections, substitution de commande.
Cas pratique 4 — Renommer des fichiers en masse
Renommer tous les .jpeg en .jpg :

#!/bin/bash

dossier=${1:-.}
compteur=0

for fichier in "$dossier"/*.jpeg; do
    [[ -f "$fichier" ]] || continue

    nouveau="${fichier%.jpeg}.jpg"
    mv "$fichier" "$nouveau"
    echo "Renommé : $fichier → $nouveau"
    ((compteur++))
done

echo "Total : $compteur fichier(s) renommé(s)."


Explication : ${fichier%.jpeg} supprime .jpeg à la fin de la chaîne (vu au chapitre 9).
Planifier avec cron
cron exécute des scripts automatiquement à des heures précises.
Éditer la crontab

crontab -e     # Ouvrir l'éditeur
crontab -l     # Lister les tâches


La syntaxe cron

┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, 0 et 7 = dimanche)
│ │ │ │ │
* * * * * commande


Exemples

# Tous les jours à minuit
0 0 * * * /home/user/scripts/backup.sh

# Toutes les 6 heures
0 */6 * * * /home/user/scripts/check_disk.sh

# Tous les lundis à 8h
0 8 * * 1 /home/user/scripts/rapport.sh


Astuce : redirige la sortie vers un log :

0 0 * * * /home/user/scripts/backup.sh >> /home/user/logs/backup.log 2>&1


Script modèle
Voici un squelette “propre” que tu peux réutiliser comme base :

#!/bin/bash
# =============================================================================
# Nom        : mon_script.sh
# Description : [Ce que fait le script]
# Utilisation : ./mon_script.sh [options] <arguments>
# =============================================================================

# --- Fonctions ---
afficher_aide() {
    echo "Utilisation : $0 [options] <argument>"
    echo "  -h    Afficher cette aide"
}

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# --- Vérification des arguments ---
if [[ $# -lt 1 ]]; then
    afficher_aide
    exit 1
fi

case $1 in
    -h|--help) afficher_aide ; exit 0 ;;
esac

# --- Programme principal ---
log "Début du script"

# ... ton code ici ...

log "Fin du script"


Exercices
Guidé : Crée un script de sauvegarde qui compresse un dossier donné en argument, le nomme avec la date, et le place dans /tmp/backups/.
Autonome : Crée un script “boîte à outils” avec un menu (case + boucle) : 1) Lister les fichiers, 2) Espace disque (df -h), 3) Info système (uname -a), 4) Quitter.
Défi : Planifie un de tes scripts pour qu’il s’exécute tous les jours à 8h avec crontab -e.
✅ Tu sais maintenant…
	∙	Écrire des scripts d’automatisation complets
	∙	Combiner toutes les notions apprises dans des cas concrets
	∙	Planifier des scripts avec cron
	∙	Structurer un script proprement avec un modèle réutilisable

Conclusion
Tu as toutes les bases pour écrire des scripts Bash utiles et bien structurés :
	∙	Chapitres 1-3 : Les fondamentaux — script, variables, arguments
	∙	Chapitre 4 : Les flux — redirections et pipes
	∙	Chapitres 5-6 : La logique — calculs, conditions, tests
	∙	Chapitre 7 : La répétition — boucles
	∙	Chapitre 8 : La structure — fonctions et case
	∙	Chapitres 9-10 : Les données — chaînes et tableaux
	∙	Chapitre 11 : La qualité — débogage et bonnes pratiques
	∙	Chapitre 12 : La mise en pratique — automatisation et cron
Pour continuer à progresser :
	∙	Écris des scripts pour tes propres besoins quotidiens
	∙	Quand tu es bloqué, man commande est ton meilleur ami
	∙	Lis les scripts des autres pour découvrir de nouvelles techniques
	∙	La meilleure façon d’apprendre, c’est de pratiquer sur des problèmes réels
Bon scripting !


# Cours Complet de Scripting Python

## De zéro à l’automatisation — Guide pour débutant absolu

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c’est un ordinateur (Linux, Mac ou Windows) et l’envie d’apprendre.

-----

## Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

|Terme           |Définition simple                                                                                            |
|----------------|-------------------------------------------------------------------------------------------------------------|
|**Terminal**    |La fenêtre où tu tapes des commandes texte pour parler à ton ordinateur                                      |
|**Script**      |Un fichier texte contenant des instructions Python à exécuter                                                |
|**Variable**    |Un conteneur avec un nom qui stocke une valeur (un nombre, du texte…)                                        |
|**Type**        |La nature d’une valeur : texte (`str`), nombre entier (`int`), nombre à virgule (`float`), vrai/faux (`bool`)|
|**Argument**    |Une info que tu donnes à un script quand tu le lances dans le terminal                                       |
|**Fonction**    |Un bloc de code réutilisable auquel on donne un nom                                                          |
|**Boucle**      |Un mécanisme qui répète des instructions plusieurs fois                                                      |
|**Module**      |Un fichier Python contenant des fonctions prêtes à l’emploi que tu peux importer                             |
|**Indentation** |Les espaces en début de ligne qui délimitent les blocs de code en Python                                     |
|**Liste**       |Une collection ordonnée de valeurs, modifiable                                                               |
|**Dictionnaire**|Une collection de paires clé-valeur (comme un vrai dictionnaire : mot → définition)                          |
|**Exception**   |Une erreur qui se produit pendant l’exécution du script                                                      |

-----

## Comment penser un script

Avant d’écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

Concrètement, il n’y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier…)
1. **Stocker** des informations dans des variables
1. **Tester** si quelque chose est vrai ou faux (conditions)
1. **Répéter** une action plusieurs fois (boucles)
1. **Afficher ou enregistrer** un résultat (sortie)

Tous les scripts, même les plus complexes, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

-----

## La grande différence avec Bash

Si tu viens du cours Bash de cette collection, un point fondamental va changer : **Python n’est pas un langage de commandes système, c’est un langage de programmation généraliste.**

En Bash, tu enchaînes des commandes du système (`ls`, `grep`, `cat`…) et tu les relies avec des pipes. En Python, tu écris des **instructions** que Python exécute lui-même, sans passer par le système. C’est un changement de logique important.

Concrètement :

- En Bash, `echo "Bonjour"` appelle la commande `echo` du système.
- En Python, `print("Bonjour")` appelle la fonction `print` **de Python**.

Python ne connaît pas `ls`, `grep` ou `cat`. Il a ses propres outils, souvent plus puissants et plus lisibles, mais différents. Ce cours t’apprend ces outils à partir de zéro.

-----

## Table des matières

1. [Découverte de Python et premier script](#chapitre-1--découverte-de-python-et-premier-script)
1. [Variables, types, affichage et saisie utilisateur](#chapitre-2--variables-types-affichage-et-saisie-utilisateur)
1. [Arguments, terminal et scripts paramétrés](#chapitre-3--arguments-terminal-et-scripts-paramétrés)
1. [Opérateurs, calculs et logique](#chapitre-4--opérateurs-calculs-et-logique)
1. [Conditions](#chapitre-5--conditions)
1. [Chaînes de caractères](#chapitre-6--chaînes-de-caractères)
1. [Listes et boucles](#chapitre-7--listes-et-boucles)
1. [Fonctions](#chapitre-8--fonctions)
1. [Dictionnaires](#chapitre-9--dictionnaires)
1. [Fichiers, chemins et automatisation simple](#chapitre-10--fichiers-chemins-et-automatisation-simple)
1. [Erreurs, débogage et code propre](#chapitre-11--erreurs-débogage-et-code-propre)
1. [Cas pratiques et automatisation](#chapitre-12--cas-pratiques-et-automatisation)

-----

# Chapitre 1 — Découverte de Python et premier script

## Le minimum à savoir

### Pourquoi Python ?

Python est l’un des langages de programmation les plus utilisés au monde. Il est populaire pour une raison simple : **il se lit presque comme de l’anglais**. Là où d’autres langages utilisent des symboles cryptiques, Python utilise des mots clairs. C’est le langage le plus recommandé pour apprendre à programmer.

Python sert à tout : automatiser des tâches, manipuler des fichiers, analyser des données, créer des sites web, faire de l’intelligence artificielle, écrire des outils de cybersécurité. Dans ce cours, on se concentre sur le **scripting** : écrire des petits programmes pour automatiser des tâches concrètes.

### Installer Python

**Linux :** Python est déjà installé. Vérifie avec :

```bash
python3 --version
```

Tu devrais voir quelque chose comme `Python 3.12.x` ou `Python 3.13.x`. Si tu vois une version 3.8 ou plus récente, c’est bon.

**Mac :** Python 3 n’est pas toujours installé par défaut. La méthode la plus simple :

```bash
# Vérifie d'abord
python3 --version

# Si ça ne fonctionne pas, installe via le site officiel
# Va sur https://www.python.org/downloads/ et télécharge l'installeur Mac
```

**Windows :**

1. Va sur [python.org/downloads](https://python.org/downloads)
1. Télécharge la dernière version
1. **IMPORTANT : coche la case “Add Python to PATH”** pendant l’installation. Si tu oublies cette case, rien ne fonctionnera dans le terminal.
1. Ouvre un terminal (PowerShell ou Invite de commandes) et tape `python --version`

> **Piège Windows :** sur Windows, la commande est souvent `python` (sans le `3`), alors que sur Linux et Mac c’est `python3`. Dans ce cours, on utilisera `python3`, mais adapte si tu es sur Windows.

### Le mode interactif : ton terrain d’entraînement

Tape `python3` dans ton terminal :

```bash
python3
```

Tu vois apparaître :

```
Python 3.12.x (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Les `>>>` sont le **prompt interactif**. Tu peux taper des instructions Python et voir le résultat immédiatement :

```python
>>> print("Bonjour !")
Bonjour !
>>> 2 + 3
5
>>> "Alice" * 3
'AliceAliceAlice'
```

C’est un bac à sable : tu tapes, Python répond. C’est parfait pour tester une idée rapidement.

Pour quitter le mode interactif :

```python
>>> exit()
```

> **À retenir :** le mode interactif est idéal pour **tester** des petites choses. Pour écrire un vrai script, tu utilises un fichier.

### Ton premier script en 3 étapes

**Étape 1 — Crée un dossier de travail :**

```bash
mkdir -p ~/mes_scripts_python
cd ~/mes_scripts_python
```

**Étape 2 — Crée le fichier et écris le script :**

Ouvre un éditeur de texte (nano, VS Code, ou n’importe quel éditeur) et crée un fichier `hello.py` :

```python
# Mon tout premier script Python
print("Hello, World !")
print("Je suis un script Python !")
```

Sauvegarde le fichier.

**Étape 3 — Lance-le :**

```bash
python3 hello.py
```

Résultat :

```
Hello, World !
Je suis un script Python !
```

Félicitations, tu viens d’écrire et d’exécuter ton premier script Python !

> **Remarque importante :** contrairement à Bash, tu n’as pas besoin de `chmod +x` ni de shebang. Tu lances simplement `python3 nom_du_script.py`. C’est plus simple.

### Les commentaires

Le symbole `#` marque un commentaire. Python ignore tout ce qui suit un `#` sur la même ligne :

```python
# Ceci est un commentaire — Python l'ignore complètement
print("Ceci s'affiche")  # Un commentaire en fin de ligne
```

Les commentaires servent à expliquer ton code. Ils sont pour toi (et pour les autres humains qui liront ton code), pas pour Python.

### L’extension `.py`

L’extension `.py` indique que c’est un fichier Python. Ce n’est pas strictement obligatoire, mais c’est une convention universelle. Ton éditeur de texte reconnaîtra le fichier comme du Python et te proposera la coloration syntaxique (les mots-clés en couleur).

### Python est sensible à la casse

`print` et `Print` sont deux choses différentes pour Python :

```python
print("Bonjour")    # ✅ Fonctionne
Print("Bonjour")    # ❌ NameError: name 'Print' is not defined
PRINT("Bonjour")    # ❌ Même erreur
```

Les commandes Python sont en **minuscules**. `print`, `input`, `if`, `for` — toujours en minuscules.

## Très utile en pratique

### Le shebang (optionnel)

Si tu veux pouvoir lancer ton script directement avec `./mon_script.py` (sans taper `python3` devant), tu peux ajouter un shebang en première ligne :

```python
#!/usr/bin/env python3
# Le reste du script
print("Hello !")
```

Puis :

```bash
chmod +x mon_script.py
./mon_script.py
```

Ce n’est pas obligatoire — `python3 mon_script.py` fonctionne toujours. Mais c’est utile si tu crées des outils que tu veux lancer comme des commandes.

### Mode interactif vs fichier script

|Mode interactif (`python3`)       |Fichier script (`python3 script.py`)|
|----------------------------------|------------------------------------|
|Pour tester rapidement            |Pour un programme réutilisable      |
|Le code disparaît à la fermeture  |Le code est sauvegardé              |
|Résultat affiché automatiquement  |Il faut utiliser `print()`          |
|Pas pratique pour plus de 5 lignes|Adapté à n’importe quelle taille    |


> **Note subtile :** dans le mode interactif, taper `2 + 3` affiche `5` directement. Dans un fichier script, `2 + 3` tout seul ne produit rien à l’écran — il faut écrire `print(2 + 3)`.

## ❌ Erreur classique

```python
# Oublier les parenthèses de print
print "Bonjour"        # ❌ SyntaxError (c'était la syntaxe Python 2, plus valide)
print("Bonjour")       # ✅ Correct en Python 3

# Oublier les guillemets autour du texte
print(Bonjour)          # ❌ NameError: name 'Bonjour' is not defined
print("Bonjour")        # ✅ Correct

# Majuscule sur print
Print("Bonjour")        # ❌ NameError
print("Bonjour")        # ✅ Correct
```

## Exercices

**Guidé :** Crée un script `salut.py` qui affiche deux lignes : “Bonjour !” puis “Bienvenue dans le monde de Python.”

**Autonome :** Crée un script `exploration.py` qui affiche le résultat de `2 + 2`, de `10 * 5`, et le texte “Python sait compter !” — chacun sur une ligne séparée avec `print()`.

## ✅ Tu sais maintenant…

- Ce qu’est Python et pourquoi l’utiliser
- Installer et vérifier ta version de Python
- Utiliser le mode interactif pour tester des idées
- Créer un fichier `.py` et le lancer avec `python3`
- Écrire des commentaires avec `#`

-----

# Chapitre 2 — Variables, types, affichage et saisie utilisateur

## Le minimum à savoir

### Qu’est-ce qu’une variable ?

Une variable, c’est un **conteneur avec une étiquette**. L’étiquette c’est le nom, et à l’intérieur il y a une valeur.

```
┌─────────────────┐
│  prenom = "Alice" │   ← "prenom" est le nom, "Alice" est la valeur
└─────────────────┘
```

### Créer une variable

```python
prenom = "Alice"
age = 25
taille = 1.75
est_admin = True
```

> **Différence avec Bash :** en Python, on met des **espaces autour du `=`**. C’est l’inverse de Bash où les espaces étaient interdits. En Python, `prenom = "Alice"` est le style recommandé.

**Règles pour les noms de variables :**

- Que des lettres, chiffres et underscores (`_`)
- Ne peut pas commencer par un chiffre
- Pas d’espaces, pas de tirets, pas de caractères spéciaux
- Sensible à la casse (`age` et `Age` sont deux variables différentes)

```python
mon_nom = "Alice"       # ✅ Correct
age2 = 30               # ✅ Correct
_secret = "caché"       # ✅ Correct
2eme_essai = "non"      # ❌ Ne peut pas commencer par un chiffre
mon-nom = "non"         # ❌ Le tiret n'est pas autorisé
```

> **Convention Python :** les noms de variables s’écrivent en `snake_case` : tout en minuscules, les mots séparés par des underscores. Pas de camelCase. `nombre_fichiers` plutôt que `nombreFichiers`.

### Les types de données

C’est ici que Python diffère fondamentalement de Bash. **En Bash, tout est du texte.** En Python, chaque valeur a un **type**, et ce type détermine ce qu’on peut faire avec.

Les 4 types de base :

|Type          |Nom Python|Exemple               |Ce que c’est            |
|--------------|----------|----------------------|------------------------|
|Texte         |`str`     |`"Alice"`, `'Bonjour'`|Une chaîne de caractères|
|Nombre entier |`int`     |`25`, `-3`, `0`       |Un nombre sans virgule  |
|Nombre décimal|`float`   |`1.75`, `3.14`, `-0.5`|Un nombre avec virgule  |
|Booléen       |`bool`    |`True`, `False`       |Vrai ou Faux            |

```python
prenom = "Alice"       # str
age = 25               # int
taille = 1.75          # float
est_admin = True       # bool
```

Pour vérifier le type d’une variable :

```python
print(type(prenom))    # <class 'str'>
print(type(age))       # <class 'int'>
print(type(taille))    # <class 'float'>
print(type(est_admin)) # <class 'bool'>
```

> **Pourquoi c’est important ?** Parce que Python ne te laissera pas mélanger n’importe quoi. `"5" + 3` provoquera une erreur, car `"5"` est du texte et `3` est un nombre. On verra comment gérer ça juste après.

### Python détecte les types automatiquement

Tu n’as pas besoin de déclarer le type d’une variable. Python le devine tout seul :

```python
x = 42          # Python sait que c'est un int
x = "hello"     # Maintenant c'est un str — Python s'adapte
x = 3.14        # Maintenant c'est un float
```

C’est pratique, mais ça veut dire qu’une variable peut changer de type en cours de route. Si tu n’y fais pas attention, ça peut créer des bugs.

### Afficher avec `print()`

`print()` est la fonction qui affiche du texte à l’écran. C’est l’équivalent du `echo` de Bash.

```python
nom = "Alice"
age = 25

# Méthode 1 : virgules (ajoute un espace automatiquement)
print("Bonjour,", nom, "! Tu as", age, "ans.")
# → Bonjour, Alice ! Tu as 25 ans.

# Méthode 2 : f-strings (la meilleure — claire et puissante)
print(f"Bonjour, {nom} ! Tu as {age} ans.")
# → Bonjour, {nom} ! Tu as 25 ans.
```

> **À retenir :** les **f-strings** (avec le `f` devant les guillemets) sont la manière recommandée d’afficher des variables dans du texte. Le `f` signifie “formatted”. Entre les `{}`, tu mets le nom de la variable, et Python remplace par sa valeur. C’est l’équivalent du `echo "Bonjour $nom"` de Bash, en plus lisible.

### Guillemets simples et doubles

En Python, `"texte"` et `'texte'` sont **strictement équivalents** :

```python
message1 = "Bonjour"
message2 = 'Bonjour'
# Les deux font exactement la même chose
```

L’intérêt, c’est de pouvoir imbriquer l’un dans l’autre :

```python
phrase = "Il a dit 'bonjour' en partant."
phrase = 'Il a dit "bonjour" en partant.'
```

> **Différence avec Bash :** en Bash, guillemets simples et doubles ont un comportement différent (les simples empêchent l’interprétation des variables). **En Python, il n’y a aucune différence.** Les deux interprètent les variables de la même façon — et les f-strings fonctionnent avec les deux : `f"..."` et `f'...'`.

### Lire une saisie utilisateur avec `input()`

`input()` affiche un message et attend que l’utilisateur tape quelque chose :

```python
prenom = input("Ton prénom : ")
print(f"Bonjour, {prenom} !")
```

Exécution :

```
Ton prénom : Alice
Bonjour, Alice !
```

C’est l’équivalent du `read -p` de Bash.

### Le piège fondamental de `input()`

**`input()` renvoie TOUJOURS du texte** (`str`), même si l’utilisateur tape un nombre :

```python
age = input("Ton âge : ")
print(type(age))        # <class 'str'> — c'est du TEXTE, pas un nombre !
```

Si tu veux faire des calculs avec, tu dois **convertir** :

```python
age_texte = input("Ton âge : ")    # "25" (texte)
age = int(age_texte)                # 25 (nombre entier)

# Ou en une seule ligne :
age = int(input("Ton âge : "))
```

Les fonctions de conversion :

|Fonction |Convertit vers|Exemple                 |
|---------|--------------|------------------------|
|`int()`  |Nombre entier |`int("25")` → `25`      |
|`float()`|Nombre décimal|`float("3.14")` → `3.14`|
|`str()`  |Texte         |`str(25)` → `"25"`      |

```python
# ❌ Ce qui se passe si tu oublies de convertir :
age = input("Ton âge : ")        # L'utilisateur tape 25
annee_prochaine = age + 1         # ❌ TypeError: can only concatenate str to str

# ✅ Correct :
age = int(input("Ton âge : "))   # On convertit en entier
annee_prochaine = age + 1         # ✅ 26
```

## Très utile en pratique

### Modifier une variable

Tu peux changer la valeur d’une variable à tout moment :

```python
humeur = "content"
print(f"Je suis {humeur}")       # → Je suis content

humeur = "fatigué"
print(f"Maintenant je suis {humeur}")   # → Maintenant je suis fatigué
```

### Affectation multiple

Python permet d’affecter plusieurs variables en une ligne :

```python
x, y, z = 1, 2, 3
prenom, age = "Alice", 25
```

Et d’échanger deux valeurs sans variable temporaire :

```python
a, b = 1, 2
a, b = b, a     # a vaut maintenant 2, b vaut 1
```

### Concaténation de texte

Pour coller deux chaînes de texte ensemble :

```python
debut = "Bon"
fin = "jour"
mot = debut + fin
print(mot)      # → Bonjour
```

Mais attention, on ne peut pas coller du texte et un nombre directement :

```python
age = 25
print("J'ai " + age + " ans")      # ❌ TypeError
print("J'ai " + str(age) + " ans") # ✅ Fonctionne, mais lourd
print(f"J'ai {age} ans")            # ✅ Beaucoup mieux avec f-string
```

> **Bonne pratique :** utilise les f-strings plutôt que la concaténation `+`. C’est plus lisible et ça évite les erreurs de type.

### Les f-strings en détail

Les f-strings peuvent contenir des expressions, pas seulement des variables :

```python
prix = 49.99
quantite = 3
print(f"Total : {prix * quantite} euros")     # → Total : 149.97 euros
print(f"Prix arrondi : {prix:.0f} euros")      # → Prix arrondi : 50 euros
```

## Bonus

### Les chaînes multi-lignes

Pour du texte sur plusieurs lignes, utilise les triples guillemets :

```python
message = """Bonjour,
Ceci est un message
sur plusieurs lignes."""

print(message)
```

### `None` — l’absence de valeur

`None` représente “rien”, “pas de valeur” :

```python
resultat = None
print(resultat)       # → None
print(type(resultat)) # → <class 'NoneType'>
```

C’est utile quand tu veux déclarer une variable sans lui donner de valeur tout de suite.

## ❌ Erreur classique

```python
# Oublier de convertir la saisie utilisateur
age = input("Âge : ")
resultat = age + 1          # ❌ TypeError — "25" + 1 ne fonctionne pas
age = int(input("Âge : "))
resultat = age + 1          # ✅ 26

# Confondre un nombre et un texte qui ressemble à un nombre
x = "42"
y = 42
print(x + y)                # ❌ TypeError
print(int(x) + y)           # ✅ 84

# Utiliser un nom de variable interdit
class = "terminale"          # ❌ "class" est un mot réservé Python
niveau = "terminale"         # ✅ Correct

# Oublier le f devant la f-string
nom = "Alice"
print("Bonjour, {nom} !")   # → Bonjour, {nom} !  (les accolades s'affichent telles quelles)
print(f"Bonjour, {nom} !")  # → Bonjour, Alice !
```

## Exercices

**Guidé :** Crée un script `presentation.py` qui demande le prénom et l’âge avec `input()`, convertit l’âge en entier, et affiche “Tu es [prénom] et tu as [âge] ans. L’année prochaine tu auras [âge+1] ans.” en utilisant une f-string.

**Autonome :** Crée un script `conversion.py` qui demande une température en degrés Celsius, la convertit en Fahrenheit (formule : `F = C * 9/5 + 32`), et affiche le résultat.

## 🧩 Mini-projet (chapitres 1-2)

Crée un script `bienvenue.py` qui :

1. Affiche “Bienvenue dans le calculateur d’âge !”
1. Demande le prénom de l’utilisateur
1. Demande son année de naissance
1. Calcule son âge approximatif (année actuelle - année de naissance — pour obtenir l’année actuelle, utilise `from datetime import datetime` puis `datetime.now().year`)
1. Affiche “Bonjour [prénom], tu as environ [âge] ans.”

## ✅ Tu sais maintenant…

- Créer une variable et l’afficher avec `print()` et les f-strings
- Les 4 types de base : `str`, `int`, `float`, `bool`
- Lire une saisie utilisateur avec `input()`
- Convertir entre types avec `int()`, `float()`, `str()`
- Pourquoi `input()` renvoie toujours du texte et comment gérer ça

-----

# Chapitre 3 — Arguments, terminal et scripts paramétrés

## Le minimum à savoir

### C’est quoi un argument ?

Au chapitre 2, tu as appris à demander des informations à l’utilisateur pendant l’exécution du script (avec `input()`). Mais il y a une autre façon de donner des infos à un script : **les arguments**, fournis au moment du lancement.

```bash
python3 saluer.py Alice
#                  ↑ c'est un argument
```

Les arguments sont pratiques parce qu’ils rendent le script utilisable **sans interaction** : tu lances la commande et c’est fait. C’est essentiel pour l’automatisation.

### `sys.argv` — la liste des arguments

Pour accéder aux arguments en Python, on utilise le module `sys` et sa variable `argv` :

```python
import sys

print(sys.argv)
```

```bash
python3 test.py pomme banane cerise
```

```
['test.py', 'pomme', 'banane', 'cerise']
```

`sys.argv` est une **liste** (on verra les listes en détail au chapitre 7). Pour l’instant, retiens juste que :

- `sys.argv[0]` → le nom du script
- `sys.argv[1]` → le premier argument
- `sys.argv[2]` → le deuxième argument
- `len(sys.argv)` → le nombre total d’éléments (script + arguments)

```python
import sys

print(f"Nom du script : {sys.argv[0]}")
print(f"Nombre d'arguments : {len(sys.argv) - 1}")
print(f"Premier argument : {sys.argv[1]}")
```

```bash
python3 infos.py Alice 25
```

```
Nom du script : infos.py
Nombre d'arguments : 2
Premier argument : Alice
```

> **Comparaison avec Bash :** `sys.argv[1]` est l’équivalent de `$1`, `sys.argv[2]` de `$2`, et `len(sys.argv) - 1` de `$#`. La différence : en Python, les arguments sont dans une liste (indexée à partir de 0), et le nom du script est `sys.argv[0]` (comme `$0` en Bash).

### Le `import` — un mot nouveau

`import sys` est la première fois que tu vois `import` dans ce cours. C’est un concept fondamental en Python : **importer un module**.

Un module, c’est un fichier contenant des fonctions et des variables prêtes à l’emploi. `sys` est un module fourni avec Python qui donne accès à des informations sur le système (arguments, version de Python, etc.).

La ligne `import sys` dit à Python : “charge le module `sys` pour que je puisse utiliser ce qu’il contient”. Après ça, tu accèdes à ses fonctionnalités avec `sys.quelque_chose`.

On utilisera d’autres modules au fil du cours (`os`, `pathlib`, `datetime`…). Le principe sera toujours le même.

> **Bonne pratique :** les `import` se mettent **tout en haut** du script, avant le reste du code.

### Vérifier qu’un argument est fourni

Un script qui attend un argument doit **toujours vérifier** qu’il a été donné. Sinon, Python plantera avec une erreur `IndexError` si l’utilisateur oublie l’argument :

```python
import sys

if len(sys.argv) < 2:
    print(f"Erreur : donne un prénom en argument.")
    print(f"Utilisation : python3 {sys.argv[0]} <prénom>")
    sys.exit(1)

prenom = sys.argv[1]
print(f"Bonjour, {prenom} !")
```

> **Note :** `sys.exit(1)` arrête le script avec un code d’erreur (comme `exit 1` en Bash). `sys.exit(0)` ou `sys.exit()` = succès. On met `sys.exit(1)` quand quelque chose ne va pas.

> **Pas de panique :** on utilise ici un `if` qu’on n’a pas encore vu en détail (c’est le chapitre 5). La syntaxe est intuitive : “si le nombre d’arguments est inférieur à 2, affiche un message et quitte”. Tu comprendras chaque détail au chapitre 5.

### La différence `input()` vs arguments

|`input()`                             |Arguments (`sys.argv`)                         |
|--------------------------------------|-----------------------------------------------|
|L’utilisateur tape pendant l’exécution|L’info est fournie au lancement                |
|Le script attend une réponse          |Le script démarre directement                  |
|Pratique pour les scripts interactifs |Pratique pour l’automatisation                 |
|Impossible à enchaîner facilement     |Facile à intégrer dans des scripts Bash ou cron|

En pratique, beaucoup de scripts utilisent les deux : les arguments pour les paramètres obligatoires, et `input()` pour demander une confirmation ou un choix.

### Les arguments sont toujours du texte

Comme `input()`, les arguments de `sys.argv` sont **toujours des chaînes de caractères** (`str`). Si tu attends un nombre, il faut convertir :

```python
import sys

if len(sys.argv) < 3:
    print(f"Utilisation : python3 {sys.argv[0]} <nombre1> <nombre2>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])
print(f"La somme de {a} et {b} est {a + b}")
```

```bash
python3 somme.py 10 25
# → La somme de 10 et 25 est 35
```

## Très utile en pratique

### Un script avec plusieurs arguments

```python
import sys

if len(sys.argv) < 3:
    print(f"Utilisation : python3 {sys.argv[0]} <prénom> <âge>")
    sys.exit(1)

prenom = sys.argv[1]
age = int(sys.argv[2])
print(f"{prenom} a {age} ans. Dans 10 ans, il aura {age + 10} ans.")
```

### Accéder à tous les arguments d’un coup

`sys.argv[1:]` donne **tous les arguments sauf le nom du script** :

```python
import sys

arguments = sys.argv[1:]
print(f"Tu as donné {len(arguments)} argument(s) : {arguments}")
```

```bash
python3 test.py rouge vert bleu
# → Tu as donné 3 argument(s) : ['rouge', 'vert', 'bleu']
```

> **Explication :** `sys.argv[1:]` utilise le **slicing** (on verra ça en détail aux chapitres 6 et 7). Pour l’instant, retiens que `[1:]` signifie “tout à partir de la position 1” — donc tout sauf le premier élément (le nom du script).

### Script complet : un outil paramétré

Voici un exemple de script paramétré qui fait quelque chose d’utile — un message de bienvenue paramétrable :

```python
import sys

if len(sys.argv) < 2:
    print("Utilisation : python3 bienvenue.py <prénom> [langue]")
    print("Langues disponibles : fr (défaut), en, es")
    sys.exit(1)

prenom = sys.argv[1]

# Si un deuxième argument est fourni, on l'utilise ; sinon, "fr" par défaut
if len(sys.argv) >= 3:
    langue = sys.argv[2]
else:
    langue = "fr"

if langue == "fr":
    print(f"Bonjour, {prenom} !")
elif langue == "en":
    print(f"Hello, {prenom}!")
elif langue == "es":
    print(f"¡Hola, {prenom}!")
else:
    print(f"Langue '{langue}' non reconnue.")
```

```bash
python3 bienvenue.py Alice         # → Bonjour, Alice !
python3 bienvenue.py Alice en      # → Hello, Alice!
python3 bienvenue.py Alice es      # → ¡Hola, Alice!
```

## Bonus

### `argparse` — pour les scripts sérieux

Pour les scripts avec beaucoup d’options (type `-v`, `--output fichier.txt`), Python fournit le module `argparse`. C’est l’équivalent professionnel de la gestion d’arguments. On ne le détaille pas ici car c’est avancé, mais sache qu’il existe. Un petit aperçu :

```python
import argparse

parser = argparse.ArgumentParser(description="Mon outil")
parser.add_argument("nom", help="Le nom de l'utilisateur")
parser.add_argument("-a", "--age", type=int, help="L'âge")
args = parser.parse_args()

print(f"Bonjour {args.nom}, tu as {args.age} ans.")
```

```bash
python3 outil.py Alice --age 25
# → Bonjour Alice, tu as 25 ans.
python3 outil.py --help
# → Affiche l'aide automatiquement
```

C’est puissant, mais tu n’en as pas besoin pour commencer. `sys.argv` suffit largement pour tes premiers scripts.

## ❌ Erreur classique

```python
# Oublier de vérifier le nombre d'arguments
import sys
prenom = sys.argv[1]    # ❌ IndexError si lancé sans argument

# Il faut TOUJOURS vérifier :
if len(sys.argv) < 2:
    print("Erreur : argument manquant")
    sys.exit(1)

# Oublier que les arguments sont du texte
import sys
nombre = sys.argv[1]
resultat = nombre * 2     # ❌ "55" au lieu de 10 — "5" * 2 = "55" (texte répété)
nombre = int(sys.argv[1])
resultat = nombre * 2     # ✅ 10

# Confondre sys.argv[0] et sys.argv[1]
# sys.argv[0] = le nom du script, sys.argv[1] = le PREMIER argument
```

## Exercices

**Guidé :** Crée un script `bonjour_arg.py` qui prend un prénom en argument, vérifie qu’il est fourni, et affiche “Bonjour, [prénom] !”. Si pas d’argument, affiche un message d’utilisation.

**Autonome :** Crée un script `calculer.py` qui prend deux nombres en arguments et affiche leur somme, leur différence et leur produit. Pense à convertir avec `int()` et à vérifier que les arguments sont fournis.

## ✅ Tu sais maintenant…

- Passer des arguments à un script Python (`sys.argv`)
- Accéder aux arguments par leur position (`sys.argv[1]`, `sys.argv[2]`…)
- Vérifier le nombre d’arguments avec `len(sys.argv)`
- La différence entre `input()` (interactif) et `sys.argv` (paramétré)
- Importer un module avec `import`
- Quitter un script avec `sys.exit()`

-----

# Chapitre 4 — Opérateurs, calculs et logique

## Le minimum à savoir

### Le calcul en Python

Python est un excellent calculateur. Contrairement à Bash, il gère nativement les nombres à virgule et la syntaxe est intuitive :

```python
a = 10
b = 3

print(f"Addition      : {a + b}")       # 13
print(f"Soustraction  : {a - b}")       # 7
print(f"Multiplication: {a * b}")       # 30
print(f"Division      : {a / b}")       # 3.3333... (décimale !)
print(f"Division entière : {a // b}")   # 3 (partie entière)
print(f"Modulo        : {a % b}")       # 1 (reste de la division)
print(f"Puissance     : {a ** b}")      # 1000
```

> **Différence majeure avec Bash :** en Python, la division `/` donne un résultat décimal (`3.3333...`). Si tu veux la division entière (comme en Bash), utilise `//`. Et pas besoin de `$(( ))` — tu écris directement les calculs.

### Les opérateurs arithmétiques

|Opérateur|Signification      |Exemple |Résultat   |
|---------|-------------------|--------|-----------|
|`+`      |Addition           |`5 + 3` |`8`        |
|`-`      |Soustraction       |`5 - 3` |`2`        |
|`*`      |Multiplication     |`5 * 3` |`15`       |
|`/`      |Division (décimale)|`5 / 3` |`1.6666...`|
|`//`     |Division entière   |`5 // 3`|`1`        |
|`%`      |Modulo (reste)     |`5 % 3` |`2`        |
|`**`     |Puissance          |`2 ** 3`|`8`        |

### Stocker un résultat

```python
prix = 50
reduction = 15
prix_final = prix - reduction
print(f"Le prix final est {prix_final} euros")   # → 35
```

### Les raccourcis d’affectation

Au lieu de `x = x + 5`, tu peux écrire `x += 5` :

```python
compteur = 0
compteur += 1       # compteur vaut 1
compteur += 1       # compteur vaut 2
compteur += 5       # compteur vaut 7
compteur -= 3       # compteur vaut 4
compteur *= 2       # compteur vaut 8
```

### Les opérateurs de comparaison

Pour tester si un nombre est plus grand, plus petit, égal à un autre :

|Opérateur|Signification    |Exemple |Résultat|
|---------|-----------------|--------|--------|
|`==`     |Égal             |`5 == 5`|`True`  |
|`!=`     |Différent        |`5 != 3`|`True`  |
|`<`      |Inférieur        |`3 < 5` |`True`  |
|`>`      |Supérieur        |`5 > 3` |`True`  |
|`<=`     |Inférieur ou égal|`5 <= 5`|`True`  |
|`>=`     |Supérieur ou égal|`5 >= 6`|`False` |


> **Différence avec Bash :** en Python, on utilise les symboles mathématiques standards (`==`, `<`, `>`) au lieu de `-eq`, `-lt`, `-gt`. C’est beaucoup plus intuitif.

```python
age = 25
print(age >= 18)       # True
print(age == 30)       # False
print(age != 25)       # False
```

Le résultat d’une comparaison est toujours un **booléen** : `True` ou `False`.

> **Ne pas confondre :** `=` sert à **affecter** une valeur (`age = 25`), `==` sert à **comparer** (`age == 25`). C’est l’erreur la plus fréquente chez les débutants.

### Les opérateurs logiques

Python utilise des **mots** pour la logique, pas des symboles :

|Opérateur|Signification                    |Équivalent Bash|
|---------|---------------------------------|---------------|
|`and`    |ET — les deux doivent être vraies|`&&`           |
|`or`     |OU — au moins une doit être vraie|`||`           |
|`not`    |NON — inverse la condition       |`!`            |

```python
age = 25
print(age >= 18 and age <= 65)    # True — entre 18 et 65
print(age < 10 or age > 60)       # False — ni < 10 ni > 60
print(not age < 18)               # True — 25 n'est PAS < 18
```

> **Astuce Python :** pour tester si une valeur est dans un intervalle, Python permet une écriture mathématique naturelle :

```python
age = 25
print(18 <= age <= 65)    # True — Python permet ça ! (pas possible en Bash)
```

### L’opérateur `in`

`in` teste si quelque chose est **contenu** dans autre chose :

```python
print("a" in "chat")        # True
print("z" in "chat")        # False
print(3 in [1, 2, 3, 4])    # True (on verra les listes au chapitre 7)
```

C’est un outil très puissant que Bash n’a pas sous cette forme.

## Très utile en pratique

### Priorité des opérateurs

Comme en maths : la multiplication passe avant l’addition. En cas de doute, utilise des parenthèses :

```python
resultat = 2 + 3 * 4     # 14 (pas 20 — le * passe avant le +)
resultat = (2 + 3) * 4   # 20 (les parenthèses forcent l'ordre)
```

### La division : `/` vs `//`

```python
print(10 / 3)     # 3.3333... (division décimale)
print(10 // 3)    # 3 (division entière — tronque la partie décimale)
print(-10 // 3)   # -4 (arrondi vers le bas, pas vers zéro !)
```

### Le modulo `%` en pratique

Le modulo donne le **reste** de la division. C’est très utile pour savoir si un nombre est pair :

```python
nombre = 42
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")
```

### Arrondir un nombre

```python
prix = 49.987
print(round(prix, 2))      # 49.99 (arrondi à 2 décimales)
print(round(prix))          # 50 (arrondi à l'entier)
```

## Bonus

### Les nombres complexes

Python gère les nombres complexes nativement (utile en mathématiques et en ingénierie) :

```python
z = 3 + 4j
print(z.real)       # 3.0
print(z.imag)       # 4.0
```

### Les grands nombres

Python gère des entiers de taille arbitraire — pas de limite :

```python
grand = 2 ** 1000    # Un nombre avec 302 chiffres — aucun problème
print(len(str(grand)))  # 302
```

Pour la lisibilité, tu peux utiliser des underscores comme séparateurs :

```python
population = 8_000_000_000    # Plus lisible que 8000000000
print(population)              # → 8000000000
```

## ❌ Erreur classique

```python
# Confondre = et ==
age = 18         # Affectation — donne la valeur 18 à age
age == 18        # Comparaison — teste si age vaut 18 (True ou False)

# Diviser par zéro
resultat = 10 / 0    # ❌ ZeroDivisionError

# Mélanger texte et nombres
prix = "50"
total = prix * 2     # ❌ "5050" (texte répété, pas un calcul)
total = int(prix) * 2  # ✅ 100
```

## Exercices

**Guidé :** Crée un script `calculatrice.py` qui prend deux nombres en arguments et affiche leur somme, leur différence, leur produit, et leur division (avec 2 décimales).

**Autonome :** Crée un script `est_pair.py` qui prend un nombre en argument et dit s’il est pair ou impair. (Indice : un nombre est pair si `nombre % 2 == 0`.)

## ✅ Tu sais maintenant…

- Faire des calculs avec les opérateurs arithmétiques
- La différence entre `/` (décimale) et `//` (entière)
- Comparer des valeurs avec `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combiner des conditions avec `and`, `or`, `not`
- Utiliser `in` pour tester l’appartenance
- La différence entre `=` (affectation) et `==` (comparaison)

-----

# Chapitre 5 — Conditions

## Le minimum à savoir

### La structure `if`

```python
age = 20

if age >= 18:
    print("Tu es majeur.")
```

Deux choses cruciales dans cette syntaxe :

1. **Les deux-points `:`** à la fin de la ligne `if`
1. **L’indentation** (les espaces en début de ligne) du bloc de code qui suit

### L’indentation : LE concept fondamental de Python

En Bash, les blocs de code sont délimités par des mots-clés (`then`/`fi`, `do`/`done`). **En Python, c’est l’indentation qui délimite les blocs.** Il n’y a pas de `fi`, pas de `done`, pas d’accolades. C’est l’alignement du texte qui dit à Python “ce code fait partie de ce bloc”.

```python
if age >= 18:
    print("Tu es majeur.")       # ← indenté = fait partie du if
    print("Tu peux voter.")      # ← indenté = fait aussi partie du if
print("Fin du programme.")       # ← pas indenté = en dehors du if, toujours exécuté
```

> **C’est le concept le plus important de Python pour un débutant.** Si tu comprends l’indentation, tu comprends Python. Si tu ne la comprends pas, rien ne fonctionnera.

**Les règles :**

- Utilise **4 espaces** pour chaque niveau d’indentation (c’est le standard Python)
- Tout le code d’un même bloc doit avoir **exactement** le même niveau d’indentation
- Ne mélange **jamais** des tabulations et des espaces (configure ton éditeur pour convertir les tabs en 4 espaces)

```python
# ✅ Correct — 4 espaces
if True:
    print("OK")
    print("OK aussi")

# ❌ Erreur — indentation incohérente
if True:
    print("OK")
      print("Trop indenté")    # IndentationError !

# ❌ Erreur — pas d'indentation
if True:
print("Pas indenté")           # IndentationError !
```

> **Conseil :** utilise un éditeur de code (VS Code, par exemple) qui gère automatiquement l’indentation. Quand tu tapes `:` et que tu appuies sur Entrée, l’éditeur indente automatiquement la ligne suivante.

### `if...else`

```python
age = 15

if age >= 18:
    print("Tu es majeur.")
else:
    print("Tu es mineur.")
```

> **Note :** `else` est au même niveau d’indentation que `if`, et il a aussi ses deux-points `:`.

### `if...elif...else`

```python
age = 25

if age < 13:
    print("Tu es un enfant.")
elif age < 18:
    print("Tu es un adolescent.")
elif age < 65:
    print("Tu es un adulte.")
else:
    print("Tu es un senior.")
```

`elif` est la contraction de “else if”. C’est l’équivalent exact du `elif` de Bash.

> **À retenir :** autant de `elif` que tu veux, mais un seul `else` (à la fin). Et pas de `fi` — c’est l’indentation qui ferme le bloc.

### Les tests les plus courants

```python
# Tester un nombre
if age >= 18:
    print("Majeur")

# Tester l'égalité d'une chaîne
if reponse == "oui":
    print("D'accord !")

# Tester si une chaîne est vide
nom = ""
if nom == "":
    print("Le nom est vide")

# Ou plus pythonique :
if not nom:
    print("Le nom est vide")

# Tester si un élément est dans une chaîne
if "chat" in "J'ai un chat noir":
    print("Il y a un chat !")
```

### Combiner des conditions

```python
age = 25
nom = "Alice"

# ET : les deux doivent être vraies
if age >= 18 and nom == "Alice":
    print("Alice est majeure.")

# OU : au moins une doit être vraie
if age < 10 or age > 80:
    print("Âge extrême.")

# NON : inverse
if not nom == "Bob":
    print("Ce n'est pas Bob.")
```

## Très utile en pratique

### Les valeurs “falsy” et “truthy”

En Python, certaines valeurs sont considérées comme “fausses” (`False`) dans un test, même sans comparaison explicite :

|Valeur            |Considérée comme|
|------------------|----------------|
|`False`           |Faux            |
|`0`               |Faux            |
|`0.0`             |Faux            |
|`""` (chaîne vide)|Faux            |
|`[]` (liste vide) |Faux            |
|`None`            |Faux            |
|Tout le reste     |Vrai            |

Ça permet d’écrire des tests très lisibles :

```python
nom = input("Ton nom : ")

if nom:        # Equivalent de : if nom != ""
    print(f"Bonjour {nom}")
else:
    print("Tu n'as rien tapé !")
```

### Conditions imbriquées

Tu peux mettre un `if` dans un autre `if`. Chaque niveau ajoute 4 espaces d’indentation :

```python
temperature = 22

if temperature > 0:
    if temperature < 15:
        print("Il fait frais.")
    elif temperature < 25:
        print("Il fait bon.")
    else:
        print("Il fait chaud.")
else:
    print("Il gèle !")
```

> **Conseil :** si tes conditions imbriquées dépassent 2-3 niveaux, c’est signe qu’il faut simplifier (souvent en combinant les conditions avec `and`/`or`).

### L’opérateur ternaire (condition en une ligne)

Pour les cas simples :

```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)    # → majeur
```

C’est pratique pour des affectations conditionnelles courtes, mais n’en abuse pas — si la condition est complexe, utilise un `if`/`else` classique.

## Bonus

### Le `match/case` (Python 3.10+)

> **Attention :** cette partie bonus nécessite **Python 3.10 minimum**. Vérifie ta version avec `python3 --version`. Si tu as une version antérieure, ignore cette section — les `if`/`elif` font exactement la même chose.

Depuis Python 3.10, il existe un équivalent du `case` de Bash :

```python
commande = input("Commande (aide/version/quitter) : ")

match commande:
    case "aide":
        print("Affiche l'aide.")
    case "version":
        print("Version 1.0")
    case "quitter":
        print("Au revoir.")
    case _:
        print(f"Commande '{commande}' inconnue.")
```

Le `_` est le cas par défaut (équivalent du `*` dans le `case` Bash). C’est propre et lisible, mais comme ça nécessite Python 3.10 minimum, les `if`/`elif` restent la méthode universelle.

## ❌ Erreur classique

```python
# Oublier les deux-points
if age >= 18         # ❌ SyntaxError — il manque le ":"
    print("Majeur")

if age >= 18:        # ✅ Correct
    print("Majeur")

# Indentation manquante
if age >= 18:
print("Majeur")      # ❌ IndentationError

# Indentation incohérente
if age >= 18:
    print("Majeur")
      print("Oui")   # ❌ IndentationError — trop d'espaces

# Utiliser = au lieu de ==
if age = 18:          # ❌ SyntaxError — c'est une affectation, pas un test
if age == 18:         # ✅ Correct — c'est un test

# Oublier le else (pas une erreur, mais un piège logique)
# Si tu ne mets pas de else, rien ne se passe quand la condition est fausse
```

## Exercices

**Guidé :** Crée un script `meteo.py` qui prend une température en argument et affiche “Il gèle” (< 0), “Froid” (0-15), “Bon” (15-25), ou “Chaud” (> 25).

**Autonome :** Crée un script `verifier.py` qui prend un mot en argument et affiche “Court” (moins de 5 caractères), “Moyen” (5-10), ou “Long” (plus de 10). Utilise `len()` pour mesurer la longueur.

## 🧩 Mini-projet (chapitres 3-5)

Crée un script `devinette.py` qui :

1. Choisit un nombre secret (écris-le en dur pour l’instant, par exemple `secret = 42`)
1. Demande à l’utilisateur de deviner avec `input()`
1. Affiche “Trop petit”, “Trop grand” ou “Bravo, c’est le bon nombre !”
1. Affiche aussi la différence : “Tu étais à [écart] près.”

## ✅ Tu sais maintenant…

- Écrire des conditions avec `if`, `elif`, `else`
- L’indentation comme structure de bloc (4 espaces par niveau)
- Les deux-points `:` après chaque `if`, `elif`, `else`
- Combiner des conditions avec `and`, `or`, `not`
- Les valeurs “falsy” (chaîne vide, 0, None, False)
- (Bonus) Le `match/case` pour les choix multiples

-----

# Chapitre 6 — Chaînes de caractères

## Le minimum à savoir

### Les chaînes sont des séquences

En Python, une chaîne de caractères (`str`) n’est pas un bloc opaque — c’est une **séquence ordonnée de caractères**, chacun accessible par sa position (son **index**).

```
 Mot :     P    y    t    h    o    n
 Index :   0    1    2    3    4    5
 Négatif: -6   -5   -4   -3   -2   -1
```

```python
mot = "Python"

print(mot[0])      # P (premier caractère)
print(mot[5])      # n (dernier caractère)
print(mot[-1])     # n (dernier, avec un index négatif)
print(mot[-2])     # o (avant-dernier)
```

> **Rappel :** les index commencent à **0**, pas à 1. Le premier caractère est `mot[0]`.

### Longueur d’une chaîne

```python
mot = "Bonjour"
print(len(mot))    # 7
```

### Le slicing : extraire une partie

Le slicing permet d’extraire une sous-chaîne avec la syntaxe `[début:fin]` :

```python
phrase = "Bonjour le monde"

print(phrase[0:7])     # "Bonjour"    (de la position 0 à 6 incluse)
print(phrase[8:10])    # "le"         (positions 8 et 9)
print(phrase[11:])     # "monde"      (de 11 jusqu'à la fin)
print(phrase[:7])      # "Bonjour"    (du début jusqu'à 6)
```

> **Règle :** `[début:fin]` va de `début` **inclus** à `fin` **exclu**. C’est déroutant au début, mais c’est la convention Python.

Le slicing avec un **pas** :

```python
texte = "abcdefghij"

print(texte[::2])      # "acegi"     (un caractère sur deux)
print(texte[::-1])     # "jihgfedcba" (inverser la chaîne !)
```

### Les méthodes essentielles

Les chaînes ont des **méthodes** — des fonctions intégrées qu’on appelle avec un point. Voici les plus utiles :

```python
texte = "  Bonjour le monde  "

# Majuscules et minuscules
print(texte.upper())          # "  BONJOUR LE MONDE  "
print(texte.lower())          # "  bonjour le monde  "
print(texte.capitalize())     # "  bonjour le monde  " (1ère lettre maj)
print(texte.title())          # "  Bonjour Le Monde  " (chaque mot)

# Supprimer les espaces en début/fin
print(texte.strip())          # "Bonjour le monde"

# Remplacer
print(texte.strip().replace("monde", "Python"))   # "Bonjour le Python"
```

> **Différence avec Bash :** en Bash, on utilisait `${var^^}`, `${var,,}`, `${var/ancien/nouveau}`. En Python, on utilise des **méthodes** appelées avec un point : `var.upper()`, `var.replace()`. C’est plus lisible.

### Découper et joindre

```python
# Découper une chaîne en morceaux (split)
phrase = "pomme,banane,cerise"
fruits = phrase.split(",")
print(fruits)      # ['pomme', 'banane', 'cerise']

# Joindre une liste en chaîne (join)
mots = ["Bonjour", "le", "monde"]
phrase = " ".join(mots)
print(phrase)      # "Bonjour le monde"
```

`split()` sans argument découpe sur les espaces :

```python
texte = "Bonjour   le    monde"
mots = texte.split()
print(mots)        # ['Bonjour', 'le', 'monde'] (les espaces multiples sont gérés)
```

### Chercher dans une chaîne

```python
phrase = "Bonjour le monde"

# Tester si un mot est dedans
print("monde" in phrase)          # True
print("Python" in phrase)         # False

# Trouver la position
print(phrase.find("monde"))       # 11 (position du début)
print(phrase.find("Python"))      # -1 (pas trouvé)

# Compter les occurrences
texte = "abracadabra"
print(texte.count("a"))           # 5

# Tester le début ou la fin
fichier = "rapport.pdf"
print(fichier.endswith(".pdf"))    # True
print(fichier.startswith("rap"))   # True
```

### Les chaînes sont immuables

En Python, une chaîne ne peut **pas** être modifiée directement :

```python
mot = "Python"
mot[0] = "J"       # ❌ TypeError: 'str' object does not support item assignment
```

Pour “modifier” une chaîne, tu crées une **nouvelle** chaîne :

```python
mot = "Python"
nouveau_mot = "J" + mot[1:]
print(nouveau_mot)   # "Jython"
```

Ce n’est pas un problème en pratique — `replace()`, `upper()`, `lower()` etc. créent toutes une nouvelle chaîne.

## Très utile en pratique

### Les f-strings avancées

```python
nom = "Alice"
solde = 1234.5678

print(f"{'Nom':<10} : {nom}")          # Aligné à gauche, 10 caractères
print(f"{'Solde':<10} : {solde:.2f}")   # 2 décimales
print(f"{'Solde':<10} : {solde:>10.2f}")  # Aligné à droite, 10 caractères

# Remplir avec des zéros
numero = 42
print(f"N° {numero:05d}")              # "N° 00042"
```

### Tableau récapitulatif des méthodes

|Méthode          |Effet                       |Exemple                            |
|-----------------|----------------------------|-----------------------------------|
|`len(s)`         |Longueur                    |`len("abc")` → `3`                 |
|`s.upper()`      |Tout en majuscules          |`"abc".upper()` → `"ABC"`          |
|`s.lower()`      |Tout en minuscules          |`"ABC".lower()` → `"abc"`          |
|`s.strip()`      |Supprimer espaces début/fin |`" ab ".strip()` → `"ab"`          |
|`s.replace(a, b)`|Remplacer a par b           |`"abc".replace("b", "X")` → `"aXc"`|
|`s.split(sep)`   |Découper en liste           |`"a,b".split(",")` → `["a", "b"]`  |
|`sep.join(liste)`|Joindre une liste           |`",".join(["a","b"])` → `"a,b"`    |
|`s.find(x)`      |Position de x (-1 si absent)|`"abc".find("b")` → `1`            |
|`s.count(x)`     |Nombre d’occurrences        |`"aba".count("a")` → `2`           |
|`s.startswith(x)`|Commence par x ?            |`"abc".startswith("ab")` → `True`  |
|`s.endswith(x)`  |Finit par x ?               |`"abc".endswith("bc")` → `True`    |
|`s.isdigit()`    |Contient que des chiffres ? |`"123".isdigit()` → `True`         |

## Bonus

### Les chaînes multi-lignes

```python
message = """Ceci est un texte
sur plusieurs lignes.
Les retours à la ligne sont préservés."""

print(message)
```

### Les caractères d’échappement

```python
print("Ligne 1\nLigne 2")       # \n = retour à la ligne
print("Col1\tCol2")              # \t = tabulation
print("Il a dit \"bonjour\"")    # \" = guillemet dans un texte entre guillemets
print("Chemin : C:\\Users")      # \\ = un seul backslash
```

### Les raw strings (pour les chemins Windows)

```python
chemin = r"C:\Users\Alice\Documents"   # Le r empêche l'interprétation des \
print(chemin)   # C:\Users\Alice\Documents
```

## ❌ Erreur classique

```python
# Essayer de modifier une chaîne
mot = "Python"
mot[0] = "J"          # ❌ TypeError — les chaînes sont immuables

# Oublier que find() renvoie -1 (pas une erreur) si rien n'est trouvé
position = "abc".find("z")
print(position)        # -1 — pas d'erreur, juste -1

# Confondre len() (fonction) et .upper() (méthode)
len("abc")             # ✅ Fonction : len(chaîne)
"abc".upper()          # ✅ Méthode : chaîne.upper()
"abc".len()            # ❌ len n'est pas une méthode
len.("abc")            # ❌ Syntaxe invalide
```

## Exercices

**Guidé :** Crée un script qui prend un numéro de téléphone avec des tirets (`01-23-45-67-89`) en argument et l’affiche reformaté avec des points (`01.23.45.67.89`). Utilise `.replace()`.

**Autonome :** Crée un script qui prend une phrase en argument et affiche : sa longueur, le nombre de mots (indice : `split()` puis `len()`), la phrase en majuscules, et la phrase inversée (indice : slicing `[::-1]`).

## ✅ Tu sais maintenant…

- Accéder aux caractères par leur index (`mot[0]`, `mot[-1]`)
- Extraire des sous-chaînes avec le slicing (`mot[2:5]`, `mot[::-1]`)
- Les méthodes essentielles : `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `find()`, `count()`
- Que les chaînes sont immuables (on crée une nouvelle chaîne au lieu de modifier)
- Les f-strings pour l’affichage formaté

-----

# Chapitre 7 — Listes et boucles

## Le minimum à savoir

### Qu’est-ce qu’une liste ?

Une liste est une **collection ordonnée de valeurs**, modifiable. C’est la structure de données la plus utilisée en Python — l’équivalent des tableaux en Bash, mais beaucoup plus puissant.

```python
fruits = ["pomme", "banane", "cerise"]
nombres = [1, 2, 3, 4, 5]
mixte = ["Alice", 25, True, 3.14]     # Possible, mais déconseillé
vide = []                              # Liste vide
```

```
Index :     0         1         2
         ┌─────┐  ┌──────┐  ┌──────┐
         │pomme│  │banane│  │cerise│
         └─────┘  └──────┘  └──────┘
```

### Accéder aux éléments

```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])       # pomme (premier)
print(fruits[-1])      # cerise (dernier)
print(len(fruits))     # 3 (nombre d'éléments)
```

### Modifier, ajouter, supprimer

```python
fruits = ["pomme", "banane", "cerise"]

# Modifier
fruits[1] = "fraise"
print(fruits)          # ['pomme', 'fraise', 'cerise']

# Ajouter à la fin
fruits.append("kiwi")
print(fruits)          # ['pomme', 'fraise', 'cerise', 'kiwi']

# Insérer à une position
fruits.insert(1, "mangue")    # Insère à la position 1
print(fruits)          # ['pomme', 'mangue', 'fraise', 'cerise', 'kiwi']

# Supprimer par valeur
fruits.remove("fraise")
print(fruits)          # ['pomme', 'mangue', 'cerise', 'kiwi']

# Supprimer par position et récupérer la valeur
dernier = fruits.pop()         # Supprime le dernier
print(dernier)         # kiwi
print(fruits)          # ['pomme', 'mangue', 'cerise']
```

### Tester l’appartenance

```python
fruits = ["pomme", "banane", "cerise"]

print("banane" in fruits)     # True
print("kiwi" in fruits)       # False
```

C’est l’opérateur `in` qu’on a vu au chapitre 4 — il fonctionne aussi bien avec les chaînes qu’avec les listes.

### Trier

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Trier la liste elle-même (modifie la liste)
nombres.sort()
print(nombres)         # [1, 1, 2, 3, 4, 5, 6, 9]

# Trier dans l'ordre inverse
nombres.sort(reverse=True)
print(nombres)         # [9, 6, 5, 4, 3, 2, 1, 1]

# Créer une nouvelle liste triée (sans modifier l'originale)
mots = ["cerise", "banane", "pomme"]
mots_tries = sorted(mots)
print(mots)            # ['cerise', 'banane', 'pomme'] (inchangée)
print(mots_tries)      # ['banane', 'cerise', 'pomme'] (nouvelle liste triée)
```

### Le slicing sur les listes

Le slicing fonctionne exactement comme pour les chaînes :

```python
nombres = [10, 20, 30, 40, 50]

print(nombres[1:3])    # [20, 30]
print(nombres[:2])     # [10, 20]
print(nombres[3:])     # [40, 50]
print(nombres[::-1])   # [50, 40, 30, 20, 10] (inverser)
```

-----

## Les boucles

### La boucle `for` : parcourir une liste

```python
fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(f"J'aime la {fruit}")
```

```
J'aime la pomme
J'aime la banane
J'aime la cerise
```

La variable `fruit` prend successivement chaque valeur de la liste. L’indentation (4 espaces) délimite le bloc répété.

> **Comparaison avec Bash :** `for fruit in "${fruits[@]}"; do ... done` → en Python : `for fruit in fruits:` suivi du bloc indenté. Plus court, plus lisible, pas de `do`/`done`.

### `range()` : générer une séquence de nombres

`range()` est l’outil essentiel pour les boucles sur des nombres :

```python
# De 0 à 4 (5 exclu)
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

# De 1 à 10
for i in range(1, 11):
    print(i)           # 1, 2, 3, ..., 10

# De 0 à 10 de 2 en 2
for i in range(0, 11, 2):
    print(i)           # 0, 2, 4, 6, 8, 10
```

> **Attention :** `range(1, 10)` va de 1 à **9** (la borne supérieure est exclue). C’est la même logique que le slicing.

### La boucle `while`

```python
compteur = 1

while compteur <= 5:
    print(f"Compteur : {compteur}")
    compteur += 1
```

```
Compteur : 1
Compteur : 2
Compteur : 3
Compteur : 4
Compteur : 5
```

> **Attention :** si tu oublies `compteur += 1`, la boucle tourne **à l’infini**. Appuie sur `Ctrl+C` pour l’arrêter.

### `break` et `continue`

```python
# break — sortir de la boucle
for i in range(1, 11):
    if i == 6:
        print("Stop !")
        break
    print(i)
# Affiche 1, 2, 3, 4, 5, Stop !

# continue — sauter au tour suivant
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Affiche 1, 2, 4, 5 (le 3 est sauté)
```

### `enumerate()` : avoir l’index ET la valeur

C’est l’un des outils les plus pratiques de Python :

```python
fruits = ["pomme", "banane", "cerise"]

for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
```

```
0 : pomme
1 : banane
2 : cerise
```

Si tu veux commencer à 1 :

```python
for numero, fruit in enumerate(fruits, start=1):
    print(f"{numero}. {fruit}")
```

```
1. pomme
2. banane
3. cerise
```

### Parcourir une chaîne caractère par caractère

```python
mot = "Python"
for lettre in mot:
    print(lettre)
# P, y, t, h, o, n (un par ligne)
```

## Très utile en pratique

### La boucle infinie volontaire

```python
while True:
    reponse = input("Commande (quitter pour sortir) : ")
    if reponse == "quitter":
        print("Au revoir !")
        break
    print(f"Tu as tapé : {reponse}")
```

### Construire une liste dans une boucle

```python
carres = []
for i in range(1, 6):
    carres.append(i ** 2)
print(carres)      # [1, 4, 9, 16, 25]
```

### Boucles imbriquées

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}", end="   ")
    print()    # Retour à la ligne après chaque ligne
```

```
1 × 1 = 1   1 × 2 = 2   1 × 3 = 3   
2 × 1 = 2   2 × 2 = 4   2 × 3 = 6   
3 × 1 = 3   3 × 2 = 6   3 × 3 = 9   
```

## Bonus

### Les compréhensions de liste

Python a une syntaxe compacte pour créer des listes :

```python
# Au lieu de :
carres = []
for i in range(1, 6):
    carres.append(i ** 2)

# Tu peux écrire :
carres = [i ** 2 for i in range(1, 6)]
print(carres)      # [1, 4, 9, 16, 25]

# Avec un filtre :
pairs = [i for i in range(1, 11) if i % 2 == 0]
print(pairs)       # [2, 4, 6, 8, 10]
```

C’est puissant et élégant, mais ne te force pas à l’utiliser au début. La boucle classique est parfaitement correcte.

### `zip()` : parcourir deux listes en parallèle

```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for nom, age in zip(noms, ages):
    print(f"{nom} a {age} ans")
```

### Les tuples — les listes immuables

Un **tuple** est comme une liste, mais **immuable** (on ne peut pas le modifier après création) :

```python
coordonnees = (48.8566, 2.3522)    # Parenthèses au lieu de crochets
print(coordonnees[0])               # 48.8566

coordonnees[0] = 0     # ❌ TypeError — un tuple ne peut pas être modifié
```

Quand utiliser un tuple plutôt qu’une liste ? Quand les données ne doivent pas changer (coordonnées GPS, date de naissance, dimensions). En pratique, pour un débutant, utilise des listes par défaut.

## ❌ Erreur classique

```python
# Oublier l'indentation dans la boucle
for i in range(5):
print(i)              # ❌ IndentationError

# Modifier une liste qu'on parcourt (dangereux !)
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    if fruit == "banane":
        fruits.remove(fruit)    # ❌ Comportement imprévisible
# Solution : créer une nouvelle liste ou parcourir une copie

# Boucle infinie par oubli d'incrément
n = 1
while n <= 10:
    print(n)
    # ❌ Oubli de n += 1 → boucle infinie (Ctrl+C pour arrêter)

# Dépasser les bornes de la liste
fruits = ["pomme", "banane"]
print(fruits[5])       # ❌ IndexError: list index out of range
```

## Exercices

**Guidé :** Crée un script qui affiche la table de multiplication d’un nombre donné en argument (de 1 à 10). Utilise une boucle `for` avec `range()`.

**Autonome :** Crée un script qui prend plusieurs mots en arguments (`sys.argv[1:]`), les stocke dans une liste, les trie par ordre alphabétique, et les affiche numérotés.

**Défi :** Crée un script `devinette_v2.py` qui choisit un nombre entre 1 et 100, et laisse l’utilisateur deviner dans une boucle `while` avec les indices “trop petit” / “trop grand”, jusqu’à ce qu’il trouve. Affiche le nombre de tentatives à la fin.

## 🧩 Mini-projet (chapitres 5-7)

Crée un script `notes.py` qui :

1. Demande à l’utilisateur de saisir des notes une par une (avec `input()` dans une boucle `while`)
1. L’utilisateur tape “fin” pour arrêter la saisie
1. Le script affiche : le nombre de notes, la moyenne, la note la plus haute (`max()`), la note la plus basse (`min()`)
1. Il affiche aussi combien de notes sont au-dessus de la moyenne

## ✅ Tu sais maintenant…

- Créer, modifier et parcourir une liste
- Ajouter (`append`), supprimer (`remove`, `pop`), trier (`sort`, `sorted`)
- Tester l’appartenance avec `in`
- Parcourir avec `for ... in ...:`
- Générer des séquences avec `range()`
- Répéter avec `while`
- Contrôler les boucles avec `break` et `continue`
- Obtenir l’index avec `enumerate()`

-----

# Chapitre 8 — Fonctions

## Le minimum à savoir

### Qu’est-ce qu’une fonction ?

Une fonction, c’est un **bloc de code réutilisable** auquel tu donnes un nom. Au lieu de copier-coller les mêmes lignes, tu les mets dans une fonction et tu l’appelles par son nom.

### Définir et appeler une fonction

```python
# 1. Définir la fonction
def saluer():
    print("Salut, bienvenue !")

# 2. L'appeler
saluer()
saluer()
```

```
Salut, bienvenue !
Salut, bienvenue !
```

> **Note :** en Python, on utilise `def` (pour “define”) suivi du nom de la fonction et de parenthèses. Le bloc de code est indenté. Pas de `{` ni de `}` — c’est l’indentation qui délimite.

> **Règle :** la définition (`def ...`) doit apparaître **avant** l’appel dans le script. Python lit le fichier de haut en bas.

### Passer des arguments (paramètres)

```python
def saluer(prenom, age):
    print(f"Bonjour {prenom} ! Tu as {age} ans.")

saluer("Alice", 25)
saluer("Bob", 30)
```

```
Bonjour Alice ! Tu as 25 ans.
Bonjour Bob ! Tu as 30 ans.
```

> **Différence avec Bash :** en Bash, les arguments d’une fonction étaient `$1`, `$2` — sans nom explicite. En Python, chaque argument a un nom clair. C’est beaucoup plus lisible.

### Retourner un résultat avec `return`

`return` renvoie une valeur au code qui a appelé la fonction :

```python
def addition(a, b):
    return a + b

resultat = addition(15, 27)
print(f"La somme est : {resultat}")     # La somme est : 42
```

> **Différence majeure avec Bash :** en Bash, une fonction renvoie un résultat via `echo` et on le capture avec `$(...)`. Le `return` de Bash ne sert qu’aux codes d’erreur (0-255). En Python, `return` renvoie **n’importe quelle valeur** — c’est beaucoup plus naturel.

Après un `return`, Python sort de la fonction immédiatement :

```python
def verifier_age(age):
    if age < 0:
        return "Âge invalide"       # Sort ici si l'âge est négatif
    if age >= 18:
        return "Majeur"
    return "Mineur"

print(verifier_age(25))      # Majeur
print(verifier_age(-5))      # Âge invalide
```

### Valeurs par défaut

Tu peux donner des **valeurs par défaut** aux paramètres :

```python
def saluer(prenom, langue="fr"):
    if langue == "fr":
        print(f"Bonjour, {prenom} !")
    elif langue == "en":
        print(f"Hello, {prenom}!")
    else:
        print(f"Hi, {prenom}!")

saluer("Alice")              # Bonjour, Alice !  (langue="fr" par défaut)
saluer("Alice", "en")        # Hello, Alice!
```

Les paramètres avec valeur par défaut doivent être **après** les paramètres obligatoires.

### Portée des variables (locale vs globale)

Une variable créée **dans** une fonction n’existe que **dans** cette fonction :

```python
def ma_fonction():
    message = "Je suis locale"
    print(message)

ma_fonction()          # ✅ "Je suis locale"
print(message)         # ❌ NameError — "message" n'existe pas ici
```

> **Différence avec Bash :** en Bash, les variables d’une fonction sont globales par défaut (il faut `local` pour les rendre locales). En Python, c’est l’inverse : les variables d’une fonction sont **locales par défaut**. C’est plus sûr.

Une fonction peut **lire** une variable globale, mais ne peut pas la **modifier** sans le mot-clé `global` (qu’on évite en général) :

```python
nom = "Global"

def afficher():
    print(nom)         # ✅ Peut lire la variable globale

def modifier():
    nom = "Local"      # Crée une variable LOCALE, ne modifie pas la globale
    print(nom)

afficher()             # → Global
modifier()             # → Local
print(nom)             # → Global (pas changé)
```

## Très utile en pratique

### Retourner plusieurs valeurs

```python
def analyser(texte):
    nb_mots = len(texte.split())
    nb_chars = len(texte)
    return nb_mots, nb_chars

mots, caracteres = analyser("Bonjour le monde")
print(f"{mots} mots, {caracteres} caractères")   # 3 mots, 16 caractères
```

Python retourne en fait un **tuple**, qu’on “décompacte” dans plusieurs variables.

### Fonction qui ne retourne rien

Si une fonction n’a pas de `return` (ou fait `return` sans valeur), elle retourne `None` :

```python
def afficher_banniere(texte):
    print("=" * 40)
    print(texte.center(40))
    print("=" * 40)

resultat = afficher_banniere("MON PROGRAMME")
print(resultat)      # None
```

C’est normal — certaines fonctions font des actions (afficher, écrire dans un fichier) sans avoir besoin de retourner une valeur.

### Documenter une fonction avec une docstring

```python
def calculer_imc(poids, taille):
    """Calcule l'Indice de Masse Corporelle.
    
    Arguments :
        poids : le poids en kg
        taille : la taille en mètres
    
    Retourne : l'IMC arrondi à 1 décimale
    """
    imc = poids / (taille ** 2)
    return round(imc, 1)
```

La docstring (entre `"""..."""`) est une bonne pratique. Elle documente ce que fait la fonction, ses paramètres et sa valeur de retour. Tu peux y accéder avec `help(calculer_imc)`.

### Fonctions qui appellent d’autres fonctions

```python
def est_majeur(age):
    return age >= 18

def categoriser(prenom, age):
    if est_majeur(age):
        return f"{prenom} est majeur(e)."
    return f"{prenom} est mineur(e)."

print(categoriser("Alice", 25))    # Alice est majeur(e).
print(categoriser("Bob", 15))      # Bob est mineur(e).
```

## Bonus

### Les arguments nommés

Tu peux appeler une fonction en nommant les arguments — l’ordre n’a plus d’importance :

```python
def creer_profil(nom, age, ville):
    return f"{nom}, {age} ans, {ville}"

# Appel classique (par position)
print(creer_profil("Alice", 25, "Paris"))

# Appel avec noms (l'ordre n'importe plus)
print(creer_profil(ville="Lyon", nom="Bob", age=30))
```

### Le nombre variable d’arguments (`*args`)

```python
def somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

print(somme(1, 2, 3))          # 6
print(somme(10, 20, 30, 40))   # 100
```

`*nombres` collecte tous les arguments dans un tuple. C’est l’équivalent du `$@` de Bash.

## ❌ Erreur classique

```python
# Oublier les parenthèses à l'appel
saluer        # ❌ Ne fait rien — c'est une référence à la fonction, pas un appel
saluer()      # ✅ Appelle la fonction

# Oublier return
def doubler(n):
    n * 2           # ❌ Calcule mais ne retourne rien
    
resultat = doubler(5)
print(resultat)     # None

def doubler(n):
    return n * 2    # ✅ Retourne le résultat

# Mettre du code après return
def test():
    return 42
    print("Jamais exécuté")    # ⚠️ Ce code ne s'exécutera jamais

# Modifier une variable globale sans le vouloir
total = 0
def ajouter(n):
    total = total + n    # ❌ UnboundLocalError — Python croit que total est locale
```

## Exercices

**Guidé :** Crée une fonction `maximum(a, b)` qui retourne le plus grand des deux nombres. Teste-la avec `print(f"Le max est {maximum(10, 25)}")`.

**Autonome :** Crée un script avec une fonction `est_palindrome(mot)` qui retourne `True` si le mot est un palindrome (se lit pareil à l’endroit et à l’envers). Indice : `mot == mot[::-1]`.

## ✅ Tu sais maintenant…

- Définir une fonction avec `def`
- Passer des arguments et utiliser des valeurs par défaut
- Retourner un résultat avec `return` (y compris plusieurs valeurs)
- La portée des variables (locale par défaut en Python)
- Documenter avec les docstrings

-----

# Chapitre 9 — Dictionnaires

## Le minimum à savoir

### Qu’est-ce qu’un dictionnaire ?

Un dictionnaire stocke des **paires clé-valeur**. C’est comme un vrai dictionnaire : tu cherches un mot (la **clé**) et tu trouves sa définition (la **valeur**).

```python
capitales = {
    "France": "Paris",
    "Allemagne": "Berlin",
    "Espagne": "Madrid"
}
```

> **Comparaison avec Bash :** c’est l’équivalent des tableaux associatifs (`declare -A` en Bash 4+), mais natif, puissant, et omniprésent en Python.

### Accéder à une valeur

```python
print(capitales["France"])       # Paris
print(capitales["Allemagne"])    # Berlin
```

Si la clé n’existe pas, Python lève une erreur `KeyError`. Pour éviter ça, utilise `.get()` :

```python
print(capitales["Japon"])            # ❌ KeyError
print(capitales.get("Japon"))        # None (pas d'erreur)
print(capitales.get("Japon", "?"))   # "?" (valeur par défaut si absent)
```

### Ajouter et modifier

```python
# Ajouter une nouvelle paire
capitales["Italie"] = "Rome"

# Modifier une valeur existante
capitales["France"] = "Marseille"   # (oui, on peut faire cette erreur)
capitales["France"] = "Paris"       # On corrige

print(capitales)
# {'France': 'Paris', 'Allemagne': 'Berlin', 'Espagne': 'Madrid', 'Italie': 'Rome'}
```

### Supprimer

```python
del capitales["Espagne"]                    # Supprime la paire
valeur = capitales.pop("Italie")            # Supprime et retourne la valeur
print(valeur)                                # Rome
```

### Vérifier si une clé existe

```python
print("France" in capitales)       # True
print("Japon" in capitales)        # False
```

> **Note :** `in` teste les **clés**, pas les valeurs. `"Paris" in capitales` renvoie `False` car `"Paris"` est une valeur, pas une clé.

### Parcourir un dictionnaire

```python
capitales = {"France": "Paris", "Allemagne": "Berlin", "Espagne": "Madrid"}

# Les clés
for pays in capitales:
    print(pays)                   # France, Allemagne, Espagne

# Les valeurs
for ville in capitales.values():
    print(ville)                  # Paris, Berlin, Madrid

# Les paires clé-valeur
for pays, ville in capitales.items():
    print(f"La capitale de {pays} est {ville}")
```

La méthode `.items()` est la plus utile — elle donne les clés et les valeurs en même temps.

### Nombre d’éléments

```python
print(len(capitales))    # 3
```

## Très utile en pratique

### Dictionnaire comme fiche de données

```python
utilisateur = {
    "nom": "Alice Dupont",
    "age": 25,
    "email": "alice@example.com",
    "admin": False
}

print(f"Nom : {utilisateur['nom']}")
print(f"Admin : {utilisateur['admin']}")

# Modifier
utilisateur["age"] = 26
```

C’est l’usage le plus courant : regrouper des informations liées dans une seule structure.

### Liste de dictionnaires

```python
equipe = [
    {"nom": "Alice", "role": "dev", "experience": 5},
    {"nom": "Bob", "role": "ops", "experience": 3},
    {"nom": "Charlie", "role": "sec", "experience": 7}
]

for membre in equipe:
    print(f"{membre['nom']} — {membre['role']} ({membre['experience']} ans)")
```

```
Alice — dev (5 ans)
Bob — ops (3 ans)
Charlie — sec (7 ans)
```

C’est un pattern extrêmement courant en Python — des données structurées dans des listes de dictionnaires.

### Récapitulatif

|Opération         |Syntaxe                             |
|------------------|------------------------------------|
|Créer             |`d = {"clé": "valeur"}`             |
|Lire              |`d["clé"]` ou `d.get("clé", défaut)`|
|Ajouter/modifier  |`d["clé"] = valeur`                 |
|Supprimer         |`del d["clé"]` ou `d.pop("clé")`    |
|Tester            |`"clé" in d`                        |
|Parcourir         |`for k, v in d.items():`            |
|Nombre d’éléments |`len(d)`                            |
|Toutes les clés   |`d.keys()`                          |
|Toutes les valeurs|`d.values()`                        |

## Bonus

### Dictionnaires imbriqués

```python
config = {
    "serveur": {
        "host": "192.168.1.100",
        "port": 8080
    },
    "base_de_donnees": {
        "nom": "ma_base",
        "utilisateur": "admin"
    }
}

print(config["serveur"]["host"])    # 192.168.1.100
```

### Compréhension de dictionnaire

```python
carres = {n: n ** 2 for n in range(1, 6)}
print(carres)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Compter des occurrences

```python
texte = "abracadabra"
compteur = {}
for lettre in texte:
    compteur[lettre] = compteur.get(lettre, 0) + 1
print(compteur)    # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

## ❌ Erreur classique

```python
# Accéder à une clé inexistante sans get()
d = {"a": 1}
print(d["b"])          # ❌ KeyError
print(d.get("b", 0))  # ✅ 0

# Confondre listes et dictionnaires
fruits = ["pomme", "banane"]       # Liste : indexée par des nombres
prix = {"pomme": 1.5, "banane": 0.8}   # Dict : indexé par des clés

# Tester une valeur au lieu d'une clé avec "in"
print("Paris" in capitales)        # False — "Paris" est une valeur, pas une clé
print("Paris" in capitales.values())  # True — là on cherche dans les valeurs
```

## Exercices

**Guidé :** Crée un dictionnaire `contacts` avec 3 personnes (nom → téléphone). Affiche tous les contacts avec une boucle, puis demande un nom à l’utilisateur et affiche son numéro (avec `.get()` pour gérer le cas où le nom n’existe pas).

**Autonome :** Crée un script qui prend une phrase en argument et compte le nombre d’occurrences de chaque mot (en utilisant un dictionnaire). Affiche les résultats triés par fréquence décroissante.

## 🧩 Mini-projet (chapitres 8-9)

Crée un script `repertoire.py` qui :

1. Contient un dictionnaire de contacts (nom → numéro)
1. Propose un menu en boucle : 1) Afficher les contacts, 2) Ajouter un contact, 3) Chercher un contact, 4) Supprimer un contact, 5) Quitter
1. Chaque option est implémentée dans une **fonction** dédiée
1. Le menu tourne dans une boucle `while True` et se termine avec `break` sur l’option “Quitter”

## ✅ Tu sais maintenant…

- Créer, lire, modifier et supprimer des éléments dans un dictionnaire
- Parcourir les clés, les valeurs, ou les deux avec `.items()`
- Utiliser `.get()` pour éviter les `KeyError`
- Les patterns courants : dictionnaire comme fiche de données, liste de dictionnaires

-----

# Chapitre 10 — Fichiers, chemins et automatisation simple

## Le minimum à savoir

### Lire un fichier

```python
# Ouvrir, lire, fermer — la méthode propre avec "with"
with open("mon_fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

print(contenu)
```

> **Bonne pratique :** ajoute toujours `encoding="utf-8"` quand tu ouvres un fichier texte. Sans ça, Python utilise l’encodage par défaut du système, qui varie selon l’OS (UTF-8 sur Linux/Mac, souvent CP-1252 sur Windows). Avec `encoding="utf-8"`, ton script se comporte de la même façon partout et gère correctement les accents. On ne le répétera pas à chaque exemple pour alléger la lecture, mais prends le réflexe.

Le mot-clé `with` garantit que le fichier est fermé proprement à la fin du bloc, même si une erreur se produit. C’est la manière recommandée de travailler avec les fichiers en Python.

> **Explication de la syntaxe :** `open("fichier", "r")` ouvre le fichier en mode lecture (`"r"` = read). `as f` donne le nom `f` au fichier ouvert. Tout le code indenté après le `:` peut utiliser `f`. Quand le bloc se termine, Python ferme le fichier automatiquement.

### Les modes d’ouverture

|Mode |Signification                 |Équivalent Bash|
|-----|------------------------------|---------------|
|`"r"`|Lecture (par défaut)          |`cat fichier`  |
|`"w"`|Écriture (écrase le fichier !)|`>`            |
|`"a"`|Ajout (ajoute à la fin)       |`>>`           |


> **Attention :** le mode `"w"` **écrase** le contenu existant, exactement comme `>` en Bash. Le mode `"a"` **ajoute** à la fin, comme `>>`.

### Écrire dans un fichier

```python
# Écraser (créer ou remplacer)
with open("resultat.txt", "w", encoding="utf-8") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")

# Ajouter à la fin
with open("journal.txt", "a", encoding="utf-8") as f:
    f.write("Nouvelle entrée\n")
```

> **Note :** `f.write()` n’ajoute **pas** de retour à la ligne automatiquement. Il faut mettre `\n` toi-même. C’est différent de `print()` qui ajoute un retour à la ligne.

### Lire ligne par ligne

C’est le mode le plus courant pour traiter des fichiers :

```python
with open("donnees.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()    # Supprime le \n en fin de ligne
        print(f"Lu : {ligne}")
```

> **Bonne pratique :** utilise toujours `.strip()` quand tu lis ligne par ligne, pour supprimer le retour à la ligne `\n` qui est inclus dans chaque ligne lue.

### Lire toutes les lignes dans une liste

```python
with open("donnees.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()

print(lignes)    # ['Ligne 1\n', 'Ligne 2\n', 'Ligne 3\n']

# Plus propre :
with open("donnees.txt", "r", encoding="utf-8") as f:
    lignes = [ligne.strip() for ligne in f]

print(lignes)    # ['Ligne 1', 'Ligne 2', 'Ligne 3']
```

### Vérifier qu’un fichier existe

Avant d’ouvrir un fichier, il est prudent de vérifier qu’il existe :

```python
import os

if os.path.exists("mon_fichier.txt"):
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")

# Plus précis :
if os.path.isfile("mon_fichier.txt"):
    print("C'est un fichier")
elif os.path.isdir("mon_fichier.txt"):
    print("C'est un dossier")
```

> **Comparaison avec Bash :** `os.path.isfile()` = `[[ -f ... ]]`, `os.path.isdir()` = `[[ -d ... ]]`, `os.path.exists()` = `[[ -e ... ]]`.

-----

## Les chemins avec `pathlib` (la méthode moderne)

Tu as vu que `os.path` permet de vérifier l’existence de fichiers. Ça fonctionne, mais en Python moderne, on préfère le module `pathlib`, qui est plus lisible, plus agréable à utiliser, et qui regroupe toutes les opérations sur les chemins dans un seul outil cohérent.

Le module `pathlib` est la manière moderne (et recommandée depuis Python 3.4) de manipuler les chemins de fichiers. Il est plus lisible que `os.path`.

```python
from pathlib import Path

# Créer un objet chemin
chemin = Path("mon_dossier/mon_fichier.txt")

# Vérifier l'existence
print(chemin.exists())         # True ou False
print(chemin.is_file())        # Est-ce un fichier ?
print(chemin.is_dir())         # Est-ce un dossier ?

# Extraire des parties du chemin
print(chemin.name)             # "mon_fichier.txt"
print(chemin.stem)             # "mon_fichier" (sans l'extension)
print(chemin.suffix)           # ".txt" (l'extension)
print(chemin.parent)           # "mon_dossier" (le dossier parent)
```

### Lire et écrire avec `pathlib`

```python
from pathlib import Path

chemin = Path("resultat.txt")

# Écrire
chemin.write_text("Bonjour le monde\n")

# Lire
contenu = chemin.read_text()
print(contenu)
```

### Parcourir un dossier

```python
from pathlib import Path

dossier = Path("/etc")

# Lister le contenu
for element in dossier.iterdir():
    print(element)

# Filtrer par extension
for fichier in dossier.glob("*.conf"):
    print(f"Fichier de config : {fichier.name}")

# Recherche récursive (sous-dossiers inclus)
for fichier in dossier.rglob("*.log"):
    print(f"Log trouvé : {fichier}")
```

### Manipuler les chemins

```python
from pathlib import Path

# Construire un chemin
base = Path.home()                    # /home/utilisateur
chemin = base / "Documents" / "rapport.txt"    # L'opérateur / joint les parties
print(chemin)    # /home/utilisateur/Documents/rapport.txt

# Créer un dossier
dossier = Path("mon_dossier/sous_dossier")
dossier.mkdir(parents=True, exist_ok=True)    # Crée tous les dossiers intermédiaires

# Renommer
ancien = Path("ancien_nom.txt")
nouveau = Path("nouveau_nom.txt")
if ancien.exists():
    ancien.rename(nouveau)
```

## Très utile en pratique

### Travailler avec des fichiers CSV

Les fichiers CSV (Comma-Separated Values) sont partout — exports de tableurs, logs, données. Python a un module intégré :

```python
import csv

# Lire un CSV
with open("donnees.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)      # Chaque ligne est une liste de valeurs

# Lire un CSV avec en-têtes (en dictionnaire)
with open("donnees.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['nom']} — {ligne['email']}")

# Écrire un CSV
with open("sortie.csv", "w", newline="") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["nom", "age", "ville"])      # En-tête
    ecrivain.writerow(["Alice", "25", "Paris"])
    ecrivain.writerow(["Bob", "30", "Lyon"])
```

### Travailler avec du JSON

JSON est le format standard pour les données structurées (APIs, configurations) :

```python
import json

# Lire du JSON
with open("config.json", "r", encoding="utf-8") as f:
    donnees = json.load(f)

print(donnees["serveur"])

# Écrire du JSON
config = {
    "serveur": "192.168.1.1",
    "port": 8080,
    "debug": True
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)    # indent=4 pour un joli formatage
```

### Date et heure avec `datetime`

```python
from datetime import datetime

maintenant = datetime.now()
print(maintenant)                              # 2025-04-07 14:30:00.123456
print(maintenant.strftime("%Y-%m-%d %H:%M"))   # 2025-04-07 14:30

# Pour un nom de fichier avec la date
nom_fichier = f"rapport_{maintenant.strftime('%Y%m%d')}.txt"
print(nom_fichier)    # rapport_20250407.txt
```

## Bonus

### Exécuter des commandes système (le pont avec Bash)

Si tu as vraiment besoin d’exécuter une commande système depuis Python :

```python
import subprocess

# Exécuter une commande et récupérer le résultat
resultat = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(resultat.stdout)

# Vérifier le code de retour
if resultat.returncode == 0:
    print("Commande réussie")
else:
    print(f"Erreur : {resultat.stderr}")
```

En général, préfère les outils Python natifs (`pathlib`, `os`, `shutil`) aux commandes système. Mais `subprocess` est utile pour les cas où tu dois interagir avec des outils qui n’ont pas d’équivalent Python.

## ❌ Erreur classique

```python
# Oublier le mode à l'ouverture
with open("fichier.txt") as f:       # ✅ Mode "r" par défaut (lecture)
    contenu = f.read()

with open("fichier.txt") as f:
    f.write("texte")                  # ❌ io.UnsupportedOperation — le mode est "r" !

with open("fichier.txt", "w") as f:
    f.write("texte")                  # ✅ Mode "w" pour écrire

# Confondre "w" et "a"
with open("journal.txt", "w") as f:   # ❌ EFFACE tout le contenu existant !
    f.write("Nouvelle ligne\n")

with open("journal.txt", "a") as f:   # ✅ AJOUTE à la fin
    f.write("Nouvelle ligne\n")

# Oublier .strip() en lisant ligne par ligne
with open("fichier.txt") as f:
    for ligne in f:
        if ligne == "stop":           # ❌ Ne matche jamais car ligne = "stop\n"
            break

# Correct :
        if ligne.strip() == "stop":   # ✅ strip() enlève le \n
            break

# Ouvrir un fichier qui n'existe pas en lecture
with open("inexistant.txt", "r") as f:    # ❌ FileNotFoundError
    contenu = f.read()
```

## Exercices

**Guidé :** Crée un script qui lit un fichier texte (donné en argument), compte le nombre de lignes et de mots, et affiche les résultats.

**Autonome :** Crée un script qui parcourt un dossier (donné en argument) et affiche pour chaque fichier : son nom, son extension, et sa taille en octets (indice : `Path(fichier).stat().st_size`).

## 🧩 Mini-projet (chapitres 8-10)

Crée un script `journal.py` qui :

1. Prend un message en argument (ou le demande avec `input()` si pas d’argument)
1. Ajoute la date et le message dans un fichier `journal.txt` au format `[2025-04-07 14:30] Message ici`
1. Si on lance le script avec l’argument `--lire`, il affiche le contenu du journal
1. Utilise des **fonctions** pour structurer le code (une fonction pour ajouter, une pour lire)

## ✅ Tu sais maintenant…

- Ouvrir, lire et écrire des fichiers avec `open()` et `with`
- La différence entre les modes `"r"`, `"w"` et `"a"`
- Manipuler les chemins avec `pathlib` (Path, glob, mkdir, rename…)
- Vérifier l’existence de fichiers et dossiers
- Travailler avec des fichiers CSV et JSON
- Obtenir la date et l’heure avec `datetime`

-----

# Chapitre 11 — Erreurs, débogage et code propre

## Le minimum à savoir

### Lire un message d’erreur Python (le traceback)

Quand Python rencontre une erreur, il affiche un **traceback**. C’est le message le plus important à apprendre à lire :

```
Traceback (most recent call last):
  File "mon_script.py", line 5, in <module>
    resultat = 10 / 0
ZeroDivisionError: division by zero
```

Comment le lire :

1. **Dernière ligne** = le type d’erreur et le message (`ZeroDivisionError: division by zero`)
1. **Ligne au-dessus** = la ligne de code fautive (`resultat = 10 / 0`)
1. **Encore au-dessus** = le fichier et le numéro de ligne (`File "mon_script.py", line 5`)

> **Réflexe :** lis le traceback **de bas en haut**. La dernière ligne est la plus importante.

### Les 5 erreurs de débutant les plus fréquentes

|Erreur            |Cause                                               |Exemple                                |
|------------------|----------------------------------------------------|---------------------------------------|
|`SyntaxError`     |Erreur de syntaxe (`:` oublié, parenthèse manquante)|`if x == 5` (manque `:`)               |
|`IndentationError`|Indentation incorrecte                              |Mauvais nombre d’espaces               |
|`NameError`       |Variable ou fonction non définie                    |Faute de frappe dans un nom            |
|`TypeError`       |Opération sur un mauvais type                       |`"5" + 3` (texte + nombre)             |
|`IndexError`      |Index hors limites                                  |`liste[10]` sur une liste de 3 éléments|

```python
# SyntaxError — Python ne comprend pas la syntaxe
if age >= 18         # ❌ Il manque le ":"

# IndentationError — l'indentation est incorrecte
if True:
print("oups")        # ❌ Il manque l'indentation

# NameError — la variable n'existe pas
print(prenom)        # ❌ Si "prenom" n'a jamais été défini

# TypeError — on mélange les types
resultat = "5" + 3   # ❌ On ne peut pas additionner du texte et un nombre

# IndexError — on dépasse la taille
fruits = ["pomme", "banane"]
print(fruits[5])     # ❌ Il n'y a que 2 éléments (index 0 et 1)
```

### Les `print()` de débogage

La méthode la plus simple et la plus universelle pour comprendre ce qui se passe dans ton script :

```python
fichier = sys.argv[1] if len(sys.argv) > 1 else None
print(f"[DEBUG] fichier = '{fichier}'")     # ← ajoute ça

if fichier:
    with open(fichier) as f:
        lignes = f.readlines()
    print(f"[DEBUG] nombre de lignes = {len(lignes)}")     # ← et ça
```

> **Astuce :** utilise le préfixe `[DEBUG]` pour retrouver facilement tes messages et les supprimer une fois le bug corrigé.

> Utiliser `print()` pour voir ce que contient une variable ou pour suivre l’exécution d’un script, c’est une méthode **normale**, simple, et utilisée par tout le monde — même les développeurs expérimentés. Ce n’est pas du bricolage, c’est du débogage.

### Gérer les erreurs avec `try/except`

Au lieu de laisser le script planter, tu peux **capturer** les erreurs :

```python
try:
    age = int(input("Ton âge : "))
    print(f"Tu as {age} ans.")
except ValueError:
    print("Ce n'est pas un nombre valide !")
```

Si l’utilisateur tape “abc”, au lieu de planter avec un `ValueError`, le script affiche gentiment un message d’erreur.

> **Comparaison avec Bash :** c’est l’équivalent de `commande || echo "Erreur"`, mais beaucoup plus puissant car tu peux différencier les types d’erreurs.

### `try/except` avec plusieurs types d’erreurs

```python
import sys

try:
    fichier = sys.argv[1]
    with open(fichier) as f:
        contenu = f.read()
    print(contenu)
except IndexError:
    print("Erreur : donne un fichier en argument.")
except FileNotFoundError:
    print(f"Erreur : le fichier '{sys.argv[1]}' n'existe pas.")
except PermissionError:
    print(f"Erreur : pas le droit de lire '{sys.argv[1]}'.")
```

### `try/except/finally`

Le bloc `finally` s’exécute **toujours**, qu’il y ait une erreur ou non :

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro !")
finally:
    print("Ce message s'affiche toujours.")
```

### `try/except/else`

Le bloc `else` s’exécute **seulement s’il n’y a pas eu d’erreur** :

```python
try:
    nombre = int(input("Un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre.")
else:
    print(f"Le carré de {nombre} est {nombre ** 2}")
```

## Très utile en pratique

### Noms de variables descriptifs

```python
# ❌ Incompréhensible
a = 5
b = "txt"
c = []

# ✅ Clair
nombre_fichiers = 5
extension = "txt"
fichiers_trouves = []
```

### Structurer avec des fonctions

```python
# ❌ Script monolithique
import sys
# ... 100 lignes de code mélangé ...

# ✅ Script structuré
import sys

def verifier_arguments():
    if len(sys.argv) < 2:
        print(f"Utilisation : python3 {sys.argv[0]} <fichier>")
        sys.exit(1)
    return sys.argv[1]

def traiter_fichier(chemin):
    with open(chemin) as f:
        return f.readlines()

def afficher_resultats(lignes):
    print(f"Nombre de lignes : {len(lignes)}")

# Programme principal
fichier = verifier_arguments()
lignes = traiter_fichier(fichier)
afficher_resultats(lignes)
```

### Le `if __name__ == "__main__":`

Tu verras souvent cette ligne dans les scripts Python :

```python
def main():
    print("Programme principal")

if __name__ == "__main__":
    main()
```

**Ce que ça fait :** le code dans le bloc `if __name__ == "__main__":` ne s’exécute **que** si tu lances le script directement avec `python3 script.py`. Si tu **importes** le fichier depuis un autre script (pour réutiliser ses fonctions), ce bloc ne s’exécute pas.

Pour tes premiers scripts, ce n’est pas obligatoire. Mais c’est une bonne habitude à prendre quand tes scripts grandissent.

### Commenter ton code

```python
# Ce script analyse un fichier de logs et compte les erreurs
# Usage : python3 analyse_logs.py <fichier_log>
```

Des commentaires utiles expliquent le **pourquoi**, pas le **quoi**. Le code devrait être assez clair pour qu’on comprenne ce qu’il fait ; le commentaire explique pourquoi on le fait.

```python
# ❌ Commentaire inutile (dit ce qu'on voit déjà)
compteur = compteur + 1    # Incrémente le compteur

# ✅ Commentaire utile (explique pourquoi)
compteur += 1    # On ignore les fichiers cachés (commençant par .)
```

## Bonus

### Le module `logging` (pour les scripts sérieux)

Au lieu de `print("[DEBUG] ...")`, les scripts professionnels utilisent le module `logging` :

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Message de débogage")
logger.info("Information")
logger.warning("Attention")
logger.error("Erreur")
```

L’avantage : tu peux activer/désactiver les messages de débogage sans les supprimer du code, et les rediriger vers un fichier.

### Les assertions

`assert` est un outil de débogage qui vérifie qu’une condition est vraie :

```python
def diviser(a, b):
    assert b != 0, "Le diviseur ne peut pas être zéro"
    return a / b
```

Si la condition est fausse, Python lève une `AssertionError`. C’est utile pendant le développement pour attraper les bugs tôt.

## ❌ Erreur classique

```python
# Capturer toutes les erreurs sans les identifier (mauvaise pratique)
try:
    resultat = faire_quelque_chose()
except:                                # ❌ Trop large — masque les vrais bugs
    print("Une erreur est survenue")

# Mieux : capturer les erreurs spécifiques
try:
    resultat = faire_quelque_chose()
except ValueError as e:
    print(f"Erreur de valeur : {e}")
except FileNotFoundError as e:
    print(f"Fichier introuvable : {e}")

# Laisser des print() de debug dans le script final
print("[DEBUG] x =", x)    # ← Pense à les supprimer !

# Ne pas tester les cas limites
# Teste ton script depuis le terminal avec ces cas limites :
```

```bash
python3 script.py ""                           # Argument vide ?
python3 script.py "fichier avec espaces.txt"   # Espaces dans le nom ?
python3 script.py                              # Pas d'argument ?
```

## Exercices

**Guidé :** Prends un de tes scripts précédents et ajoute un `try/except` autour du code qui pourrait échouer (ouverture de fichier, conversion de nombre). Teste avec des entrées invalides.

**Autonome :** Crée un script volontairement bugué (variable mal nommée, indentation incorrecte, type incorrect…) et corrige les erreurs en lisant les tracebacks.

## ✅ Tu sais maintenant…

- Lire et comprendre un traceback Python (de bas en haut)
- Les 5 erreurs les plus fréquentes
- Déboguer avec `print("[DEBUG] ...")`
- Gérer les erreurs avec `try/except`
- Les bonnes pratiques : noms clairs, fonctions, commentaires utiles
- Le `if __name__ == "__main__":` pour structurer un script

-----

# Chapitre 12 — Cas pratiques et automatisation

> Jusqu’ici, tu as appris les briques du scripting Python une par une. Maintenant, on les **combine** dans de vrais petits scripts, proches de situations réelles. C’est ici que tout prend son sens.

## Penser comme un automaticien

Avant d’écrire un script d’automatisation, pose-toi trois questions :

1. **Qu’est-ce que je fais à la main régulièrement ?**
1. **Est-ce que c’est toujours les mêmes étapes ?**
1. **Est-ce que ça pourrait tourner tout seul ?**

Si oui aux trois → c’est un bon candidat pour un script.

## Cas pratique 1 — Journaliser et accueillir

Un script simple qui enregistre les connexions :

```python
import getpass
from datetime import datetime
from pathlib import Path

log_path = Path.home() / "connexions.log"

utilisateur = getpass.getuser()
date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Bienvenue, {utilisateur} !")

with open(log_path, "a") as f:
    f.write(f"[{date_heure}] Connexion de {utilisateur}\n")

print(f"Connexion enregistrée dans {log_path}")
```

> **Ce script illustre :** `pathlib`, `datetime`, `getpass`, écriture en mode `"a"`, f-strings.

## Cas pratique 2 — Vérifier des fichiers et dossiers

Un script qui analyse une liste de chemins donnés en arguments :

```python
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print(f"Utilisation : python3 {sys.argv[0]} <chemin1> [chemin2] ...")
    sys.exit(1)

for chemin_str in sys.argv[1:]:
    chemin = Path(chemin_str)
    
    if chemin.is_file():
        taille = chemin.stat().st_size
        print(f"✓ {chemin} — fichier ({taille} octets)")
    elif chemin.is_dir():
        nb = len(list(chemin.iterdir()))
        print(f"✓ {chemin} — dossier ({nb} éléments)")
    else:
        print(f"✗ {chemin} — n'existe pas")
```

> **Ce script illustre :** `sys.argv`, `pathlib`, boucle `for`, conditions, `Path.stat()`.

## Cas pratique 3 — Renommer des fichiers en masse

Renommer tous les `.jpeg` en `.jpg` dans un dossier :

```python
import sys
from pathlib import Path

dossier = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
compteur = 0

for fichier in dossier.glob("*.jpeg"):
    nouveau = fichier.with_suffix(".jpg")
    fichier.rename(nouveau)
    print(f"Renommé : {fichier.name} → {nouveau.name}")
    compteur += 1

print(f"Total : {compteur} fichier(s) renommé(s).")
```

> **Ce script illustre :** `pathlib.glob()`, `.with_suffix()`, `.rename()`, compteur.

## Cas pratique 4 — Lire et analyser un CSV

```python
import csv
import sys

if len(sys.argv) < 2:
    print(f"Utilisation : python3 {sys.argv[0]} <fichier.csv>")
    sys.exit(1)

fichier = sys.argv[1]
total = 0
compteur = 0

try:
    with open(fichier, "r") as f:
        lecteur = csv.DictReader(f)
        
        for ligne in lecteur:
            nom = ligne.get("nom", "?")
            montant = float(ligne.get("montant", 0))
            total += montant
            compteur += 1
            print(f"{nom} : {montant:.2f} €")
    
    print(f"\n--- Résumé ---")
    print(f"Nombre d'entrées : {compteur}")
    print(f"Total : {total:.2f} €")
    print(f"Moyenne : {total/compteur:.2f} €" if compteur > 0 else "Pas de données")

except FileNotFoundError:
    print(f"Erreur : fichier '{fichier}' introuvable.")
except ValueError as e:
    print(f"Erreur de données : {e}")
```

> **Ce script illustre :** `csv.DictReader`, gestion d’erreurs `try/except`, calculs, formatage des nombres.

## Les modules essentiels pour l’automatisation

Voici les modules que tu utiliseras le plus souvent. Ils sont tous **inclus avec Python** — pas besoin d’installer quoi que ce soit.

|Module      |Utilité                       |Exemple                           |
|------------|------------------------------|----------------------------------|
|`sys`       |Arguments, quitter le script  |`sys.argv`, `sys.exit()`          |
|`os`        |Système d’exploitation        |`os.getenv()`, `os.getcwd()`      |
|`pathlib`   |Manipulation de chemins       |`Path("fichier.txt").exists()`    |
|`datetime`  |Dates et heures               |`datetime.now()`                  |
|`json`      |Lire/écrire du JSON           |`json.load()`, `json.dump()`      |
|`csv`       |Lire/écrire du CSV            |`csv.reader()`, `csv.DictReader()`|
|`shutil`    |Copier/déplacer des fichiers  |`shutil.copy()`, `shutil.move()`  |
|`subprocess`|Exécuter des commandes système|`subprocess.run(["ls"])`          |
|`re`        |Expressions régulières        |`re.search()`, `re.findall()`     |

Pour en utiliser un, il suffit de l’importer en haut du script :

```python
import json
from pathlib import Path
from datetime import datetime
```

## Script modèle

Voici un squelette “propre” que tu peux réutiliser comme base pour tes scripts :

```python
#!/usr/bin/env python3
"""
Nom        : mon_script.py
Description : [Ce que fait le script]
Utilisation : python3 mon_script.py [options] <arguments>
"""

import sys
from datetime import datetime
from pathlib import Path


def log(message):
    """Affiche un message horodaté."""
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{horodatage}] {message}")


def afficher_aide():
    """Affiche l'aide du script."""
    print(f"Utilisation : python3 {sys.argv[0]} <argument>")
    print(f"  -h, --help    Afficher cette aide")


def traiter(argument):
    """Fonction principale de traitement."""
    log(f"Traitement de : {argument}")
    # ... ton code ici ...
    log("Traitement terminé.")


def main():
    """Point d'entrée du script."""
    if len(sys.argv) < 2:
        afficher_aide()
        sys.exit(1)
    
    if sys.argv[1] in ("-h", "--help"):
        afficher_aide()
        sys.exit(0)
    
    traiter(sys.argv[1])


if __name__ == "__main__":
    main()
```

## Exercices

**Guidé :** Crée un script de sauvegarde qui prend un dossier en argument, crée une copie compressée dans `/tmp/backups/` avec la date dans le nom. (Indice : utilise `shutil.make_archive()`.)

**Autonome :** Crée un script “boîte à outils” avec un menu (`while True` + `input()`) : 1) Lister les fichiers du dossier courant, 2) Espace disque (`shutil.disk_usage()`), 3) Date et heure, 4) Quitter. Chaque option appelle une fonction dédiée.

**Défi :** Crée un script qui lit un fichier CSV de contacts (nom, email, téléphone), permet de chercher un contact par nom, et d’ajouter un nouveau contact. Les modifications sont sauvegardées dans le fichier.

## ✅ Tu sais maintenant…

- Combiner toutes les notions dans des scripts concrets
- Utiliser les modules essentiels (`sys`, `os`, `pathlib`, `datetime`, `json`, `csv`)
- Structurer un script proprement avec le modèle réutilisable
- Automatiser des tâches réelles (fichiers, données, journalisation)

-----

# Conclusion

Tu as toutes les bases pour écrire des scripts Python utiles et bien structurés :

- **Chapitres 1-3 :** Les fondamentaux — script, variables, arguments
- **Chapitres 4-5 :** La logique — calculs, comparaisons, conditions
- **Chapitre 6 :** Le texte — chaînes de caractères
- **Chapitre 7 :** Les données et la répétition — listes et boucles
- **Chapitre 8 :** La structure — fonctions
- **Chapitre 9 :** Les données structurées — dictionnaires
- **Chapitre 10 :** Le monde extérieur — fichiers, chemins, CSV, JSON
- **Chapitre 11 :** La qualité — erreurs, débogage, bonnes pratiques
- **Chapitre 12 :** La mise en pratique — automatisation

**Pour continuer à progresser :**

- Écris des scripts pour tes propres besoins quotidiens — c’est la meilleure façon d’apprendre
- Quand tu es bloqué, `help(fonction)` dans le mode interactif est ton meilleur ami
- La documentation officielle [docs.python.org](https://docs.python.org) est excellente et complète
- Lis le code des autres pour découvrir de nouvelles techniques
- Explore les modules de la bibliothèque standard — il y en a pour presque tout

**Prochaines étapes possibles :**

- Les expressions régulières (`re`) pour le traitement de texte avancé
- Les requêtes HTTP (`requests`) pour interagir avec des APIs
- Les bases de données (`sqlite3`) pour stocker des données structurées
- La programmation orientée objet (classes) pour les projets