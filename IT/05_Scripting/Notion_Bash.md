### Introduction [Glossaire, penser un script]

- Glossaire
    
    
    | Terme | Définition simple |
    | --- | --- |
    | **Terminal** | La fenêtre noire où tu tapes des commandes texte |
    | **Shell** | Le programme qui lit et exécute tes commandes (Bash est un shell) |
    | **Script** | Un fichier texte contenant une liste de commandes à exécuter |
    | **Variable** | Un conteneur avec un nom qui stocke une valeur |
    | **Argument** | Une info que tu donnes à un script quand tu le lances |
    | **Commande** | Une instruction que le shell sait exécuter (`echo`, `ls`, `cd`...) |
    | **Sortie standard (stdout)** | Là où une commande affiche son résultat (l'écran par défaut) |
    | **Sortie d'erreur (stderr)** | Là où une commande affiche ses erreurs (l'écran aussi par défaut) |
    | **Code de retour** | Un nombre (0 = succès, autre = erreur) que chaque commande renvoie |
    | **Boucle** | Un mécanisme qui répète des commandes plusieurs fois |
    | **Fonction** | Un bloc de code réutilisable auquel on donne un nom |
    | **Pipe** | Un "tuyau" (`\|`) qui envoie la sortie d'une commande vers une autre |
- Comment penser un script : Recevoir > Stocker > Tester > Répéter > Afficher ou enregistrer
    - Tout script suit le même schéma
        
        ```powershell
          ENTRÉE           TRAITEMENT           SORTIE
          Ce que le    →   Ce que le script  →  Ce que le script
          script reçoit    fait avec            produit comme résultat
        ```
        
    - 5 briques de base dans un script :
        1. Recevoir des données (arguments, saisie utilisateur, fichier…)
        2. Stocker des informations dans des variables
        3. Tester si quelque chose est vrai ou faux (conditions)
        4. Répéter une action plusieurs fois (boucles)
        5. Afficher ou enregistrer un résultat (sortie)

### Découverte de Bash et premier script

- Terminal (fenêtre où tape commandes) & shell (programme à l’intérieur du terminal qui comprend et exécute commandes)
    - Pour ouvrir terminal :
        - **Linux** : `Ctrl + Alt + T` ou cherche "Terminal" dans tes applications
        - **Mac** : cherche "Terminal" dans Spotlight
        - **Windows** : installe WSL (Windows Subsystem for Linux)
    - Vérifier quel shell on utiliser
        
        ```powershell
        echo $SHELL
        ```
        
- Premier script : plusieurs commandes rangées dans un fichier.
    1. Crée un dossier de travail 
        
        ```powershell
        mkdir -p ~/mes_scripts
        cd ~/mes_scripts
        ```
        
    2. Crée fichier 
        
        ```powershell
        nano hello.sh
        ```
        
    3. Ecrire script 
        
        ```powershell
        #!/bin/bash
        # Mon tout premier script
        echo "Hello, World !"
        echo "Je suis un script Bash !"
        ```
        
    4. Rendre exédcutable fichier
        
        ```powershell
        chmod +x fichier.sh
        ```
        
    5. Lancer le script
        
        ```powershell
        ./hello.sh
        ```
        
- Shebang : #!/bin/bash
    - Première ligne #!/bin/bash s’appelle shebang. Dit au système “ce fichier doit être lu par Bash”
    - Sans shebang, système ne sait pas quel langage utiliser.
    - Toujours mettre shebang en première des scripts
- Pourquoi ./ devant script ?
    - Quand tape ls ou date, système sait trouver ces commandes grâce à variable PATH.
    - Dossier perso pas dans PATH, donc préciser “cherche dans dossier actuel”.
- Commande exit
    - exit permet de terminer un script avec code de sortie
    - Code essentiels :
        
        
        | Code | Signification |
        | --- | --- |
        | 0 | Succès (tout s’est bien passé) |
        | 1 | Erreur générale |
        | 127 | Commande introuvable |
    - A retenir : en Bash, `0` = succès, tout autre nombre = erreur. C'est l'inverse de ce qu'on pourrait penser !
    - Pour info, d'autres codes existent (`2` = mauvaise utilisation, `130` = Ctrl+C, `126` = pas le droit d'exécuter), mais tu n'as pas besoin de les mémoriser maintenant.
- Cheat sheet
    
    
    | **Commande / Syntaxe** | **Effet** |
    | --- | --- |
    | #!/bin/bash | Shebang — dit au système d'utiliser Bash. Toujours en 1ère ligne |
    | echo $SHELL | Vérifie quel shell est actif (doit afficher /bin/bash) |
    | nano script.sh | Crée ou ouvre un fichier script dans l'éditeur nano |
    | chmod +x script.sh | Rend le script exécutable (à faire une seule fois) |
    | ./script.sh | Lance le script depuis le dossier actuel |
    | bash script.sh | Lance le script sans avoir fait chmod +x |
    | exit 0 | Termine le script — succès |
    | exit 1 | Termine le script — erreur |
    | # commentaire | Ligne ignorée par Bash, sert à documenter le code |
- ❌ Erreur classique
    
    ```powershell
    # Oublier le shebang → le script peut ne pas fonctionner avec ./script.sh
    # Oublier chmod +x → "Permission denied" quand tu lances le script
    # Oublier le ./ → "command not found"
    ```
    
- Exercices
    
    **Guidé :** Crée un script `salut.sh` qui affiche deux lignes : "Bonjour !" puis "Bienvenue dans le monde du scripting."
    
    **Autonome :** Crée un script `info.sh` qui affiche ton nom d'utilisateur (`whoami`), la date (`date`), et le dossier actuel (`pwd`) sur des lignes séparées.
    
    ![image.png](attachment:8a8fc784-f60b-4af2-a4a9-3c92a090c4b5:image.png)
    

### Variables, affichage et saisie utilisateur [read, $(commande), var env, readonly]

- Variable : Conteneur avec étiquette, étiquette nom et à l’intérieur il y a valeur
    
    ```powershell
    │ prenom = Alice │ ← "prenom" est le nom, "Alice" est la valeur
    ```
    
- Créer et afficher variable
    
    ```powershell
    #!/bin/bash
    
    prenom="Alice"
    echo "Bonjour, $prenom !"
    ```
    
    - Règle critique : PAS d’espace autour du =
- Accèder au contenu d’une variable : Mettre $ devant son nom
    
    ```powershell
    echo "Bonjour, $prenom"     # → Bonjour, Alice
    echo "Bonjour, prenom"      # → Bonjour, prenom
    ```
    
    - Bonne pratique : Ecrire “$prenom” (avec guillemets plutôt que sans, évite problèmes si valeur contient espaces
- Forme avec accolades ${variable} : Eviter ambiguïtés
    
    ```powershell
    animal="chat"
    echo "J'ai 3 ${animal}s"    # → J'ai 3 chats
    echo "J'ai 3 $animals"      # → J'ai 3  (Bash cherche la variable "animals" qui n'existe pas)
    ```
    
- Modifier variable
    
    ```powershell
    #!/bin/bash
    humeur="content"
    echo "Je suis $humeur"
    
    humeur="fatigué"
    echo "Maintenant je suis $humeur"
    ```
    
- Guillemets simples (tout littéral) vs doubles (interprète variables)
    
    ```powershell
    prenom="Alice"
    
    echo "Bonjour, $prenom"    # Guillemets doubles → Bash remplace la variable
    # → Bonjour, Alice
    
    echo 'Bonjour, $prenom'    # Guillemets simples → tout est affiché tel quel
    # → Bonjour, $prenom
    ```
    
    > **À retenir :**
    > 
    > - **Guillemets doubles `" "`** → Bash interprète les variables
    > - **Guillemets simples `' '`** → tout est littéral, aucune interprétation
- Saisie utilisateur read (demande user de taper qque chose) : -s (invisible), -t (tiemout) | read -p “texte” variable
    - Commande read demande à l’user de taper quelque chose
        
        ```powershell
        #!/bin/bash
        
        read -p "Ton prénom : " prenom
        read -p "Ton âge : " age
        echo "Tu es $prenom et tu as $age ans."
        ```
        
        - -p permet de mettre message et saisie sur même ligne.
    - Saisie invisible : -s
        
        ```powershell
        read -p "Mot de passe : " -s motdepasse  # -s : saisie invisible
        ```
        
    - Timeout de 5 secondes : -t 5
        
        ```powershell
        read -p "Choix rapide : " -t 5 choix  # -t 5 : timeout de 5 secondes
        ```
        
    - Exemples
        - Faciliter scans nmap
            
            ```bash
            #!/bin/bash
            
            read -p "L'adresse à scanner : " ip_scan    # Va prendre ip saisie puis stocker dans variable ip_scan
            echo "Scan de $ip_scan en cours..."    
            nmap -F -sV "$ip_scan"
            ```
            
- ⚠️ Résutat / Substitut d’une commande dans variable : nom_var=$(commande)
    - Substitut de commande : directement dans sortie
    
    ```bash
    echo "Bienvenue sur cette machine : $(hostname) !"
    echo "La date du jour : $(date)"
    ```
    
    - Stocker résultat commande dans variable
    
    ```powershell
    #!/bin/bash
    
    aujourdhui=$(date)
    echo "Nous sommes le : $aujourdhui"
    
    utilisateur=$(whoami)
    echo "Connecté en tant que : $utilisateur"
    
    nb_fichiers=$(ls | wc -l)
    echo "Il y a $nb_fichiers éléments dans ce dossier"
    ```
    
    - A retenir : $(commande) exécuter la commande et renvoie son résultat. Fonctionnalités les plus puissantes de bash.
- Variables d’environnement : Variables déjà définies : env
    - Connaitre var env :
        
        ```powershell
        env
        ```
        
    - Système contient des variables déjà définies :
        
        ```powershell
        #!/bin/bash
        
        echo "Utilisateur : $USER"
        echo "Dossier perso : $HOME"
        echo "Shell actuel : $SHELL"
        echo "Dossier actuel : $PWD"
        ```
        
- Variables lecture seule : Jamais être modifiée : readonly
    - Pour qu’une variable ne puisse jamais être modifiée
        
        ```powershell
        readonly TEST="Texte qu'on ne pourra pas modifier"
        TEST="Essayer de modifier var" 
        ```
        
- “Types” en Bash : Var surtout texte même nombre manipulé comme texte, sauf quand calcul, pas types strict comme autre langages
- Cheat sheet
    
    
    | **Syntaxe** | **Effet** |
    | --- | --- |
    | nom="Alice" | Crée une variable (pas d'espace autour du =) |
    | echo "$nom" | Affiche la valeur de la variable (toujours mettre les guillemets) |
    | echo '${nom}s' | Accolades pour éviter l'ambiguïté (ex: ${animal}s → chats) |
    | "texte $var" | Guillemets doubles → la variable est interprétée |
    | 'texte $var' | Guillemets simples → tout est littéral, rien n'est interprété |
    | result=$(commande) | Substitution : stocke le résultat d'une commande dans une variable |
    | read -p "Texte : " var | Demande une saisie à l'utilisateur et la stocke dans var |
    | read -s -p "MDP : " var | Saisie invisible (pour mots de passe) |
    | read -t 5 -p "..." var | Saisie avec timeout de 5 secondes |
    | readonly MA_VAR="x" | Variable constante, ne peut pas être modifiée |
    | $USER · $HOME · $SHELL · $PWD | Variables d'environnement déjà définies par le système |
- ❌ Erreur classique
    
    ```bash
    prenom = "Alice"     # ❌ Espaces autour du = → Bash croit que "prenom" est une commande
    prenom="Alice"       # ✅ Correct
    
    echo $prenom         # ⚠️ Fonctionne, mais risqué si la valeur contient des espaces
    echo "$prenom"       # ✅ Toujours préférer cette forme
    ```
    
- Ex
    
    Crée un script `bienvenue.sh` qui :
    
    1. Affiche "Bienvenue sur cette machine !"
    2. Affiche la date du jour (avec substitution de commande)
    3. Demande le prénom de l'utilisateur
    4. Affiche "Bonjour [prénom], connecté en tant que [whoami]"
    
    ```bash
    # Code initial 
    
    #!/bin/bash
    
    machine=$(hostname)
    echo "Bienvenue sur cette machine : "$machine" !"
    
    aujourdhui=$(date)
    echo "La date du jour : "$aujourdhui""
    
    read -p "Comment vous appelez-vous ? " name
    echo "Bonjour "$name", connecté en tant que $(whoami)"
    
    # Corrigé 
    
    #!/bin/bash
    
    echo "Bienvenue sur cette machine : $(hostname) !"
    echo "La date du jour : $(date)"
    
    read -p "Comment vous appelez-vous ? " name
    echo "Bonjour $name, connecté en tant que $(whoami)"
    ```
    

### Arguments et variables spéciales [$0, $1, if [[ -z … ]]; then … exit 1 fi]

- Argument : donner info directement ./script Info (=argument)
    
    ```bash
    ./saluer.sh Alice
    #                 ↑ c'est un argument
    ```
    
- Paramêtres positionnels : Argument stocké dans var numérotée ./script (=$0) Info1 (=$1) Info2 (=$2) Info3 (=$3)
    - Chaque argument stocké dans variable numérotée :
        
        ```bash
        ./mon_script.sh  pomme   banane  cerise
               $0          $1      $2      $3
        ```
        
        - `$0` → le nom du script
        - `$1` → le premier argument
        - `$2` → le deuxième
        - `$3` → le troisième...
    - Exemple : saluer.sh
        
        ```bash
        #!/bin/bash 
        echo "Bonjour, $1 !"
        ```
        
        ```bash
        ./saluer.sh Alice   # -> Bonjour, Alice !
        ./saluer.sh Bob     # -> Bonjour, Bob !
        ```
        
- Variables spéciales : $0 (Nom script), $1/$2/… (arguments par position), $# (nombre d’arguments), $@ (tous arguments (séparément)), $? (code de sortie de dernière commande)
    - Special variables use the [Internal Field Separator](https://bash.cyberciti.biz/guide/$IFS) (`IFS`) to identify when an argument ends and the next begins.
    
    | Variable | Contenu | Description |
    | --- | --- | --- |
    | $0 | Le nom du script | Contient le nom du script exécuté. |
    | $1, $2... | Les arguments par position | Permet d’accéder aux arguments individuellement selon leur position (ex : $1 = premier argument). |
    | $# | Le nombre d'arguments | Contient le nombre total d’arguments passés au script. |
    | $@ | Tous les arguments (séparément) | Permet de récupérer tous les arguments en ligne de commande, chacun traité séparément. |
    | $? | Le code de sortie de la dernière commande | Contient le code de retour de la dernière commande (0 = succès, autre valeur = erreur). |
    | $$ | PID du processus | Contient l’identifiant (PID) du processus en cours d’exécution. |
    - Exemple :
        
        ```bash
        echo "Nom du script : $0"
        echo "Nombre d'arguments : $#"
        echo "Tous les arguments : $@"
        echo "Premier : $1"
        echo "Deuxième : $2"
        ```
        
        ```bash
        ./infos.sh pomme banane cerise
        ```
        
        ```bash
        Nom du script : ./infos.sh
        Nombre d'arguments : 3
        Tous les arguments : pomme banane cerise
        Premier : pomme
        Deuxième : banane
        ```
        
        ```bash
        if [ $# -eq 0 ]
        then
            echo -e "You need to specify the target domain.\n"
            echo -e "Usage:"
            echo -e "\t$0 <domain>"
            exit 1
        else
            domain=$1
        fi
        ```
        
- ⚠️ Vérifier que argument fourni : if [[ -z … ]]; then … exit 1 fi, if [[ ! -d … ]]; then…
    - Script qui attend argument devrait toujours vérifiés qu’il a été donné :
        - -z : Chaîne vide
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then  # [[ .. ] : test de condition / -z : vide
                echo "Erreur : donne un argument !"  # sortie texte
                echo "Utilisation : $0 <prenom>"  # sortie texte, intéressant pour dire quoi faire
                exit 1  # 1 : arrêter script avec erreur
        fi # fin du if
        
        echo "Bonjour $1 !"  # si argument donné, sortie
        
        ```
        
        - Explication : -z teste si chaîne est vide. Si $1 est vide (= pas d’argument), affiche un message d’erreur et quitte.
    - ! -d : Vérifier si dossier en argument
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument"
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide"
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        echo "$(date) "$1" "$nbr_fichiers"" > rapport.txt
        cat rapport.txt
        
        ```
        
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur, script attends <fichier1> et <fichier2>"
                exit 1
        fi
        
        echo "Comparaison de $1 et $2"
        echo "Taille de $1 :"
        wc -c < "$1"    # < "$1" = redirige le contenu du fichier $1 vers wc
        echo "Taille de $2 :"
        wc -c < "$2"
        
        ```
        
    - Bien indiquer comment faire
        
        ```bash
        #!/bin/bash
        
        if
                [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner votre prénom" >&2
                echo -e "Usage :\n\t$0 <prenom>"
                exit 1
        fi
        
        echo "Bonjour, $1 !"
        ```
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez indiquer le nom d'un fichier"
                echo -e  "Usage :\n\t$0 <fichier>"
                exit 1
        fi
        
        emplacement=$(find / -iname "$1" 2>/dev/null)
        
        if [[ -z "$emplacement" ]]; then
                echo "Aucun fichier trouvé"
                echo "Le fichier $1 ne semble pas présent sur le système"
                exit 1
        fi 
        
        echo "L'emplacement de $1 :"
        echo "$emplacement"
        ```
        
- Affichage sortie \n (retour à la ligne), \t (tabulation), echo -e
    - Bien indiquer echo -e pour que l’affichage soit correct
    - \n : Permet retour à la ligne
    - \t : Pemret tabulation
        
        ```bash
        if
                [[ -z "$1" ]]; then
                echo "Erreur : Veuillez indiquer le nom d'un fichier"
                echo -e  "Usage :\n\t$0 <fichier>"
                exit 1
        fi
        ```
        
        ![image.png](attachment:42d9bf9b-5228-4195-aee1-09781fba5821:image.png)
        
- Utiliser plusieurs arguments : comparaison fichiers
    - Comparaison entre fichiers
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur, script attends <fichier1> et <fichier2>"
                exit 1
        fi
        
        echo "Comparaison de $1 et $2"
        echo "Taille de $1 :"
        wc -c < "$1"    # < "$1" = redirige le contenu du fichier $1 vers wc
        echo "Taille de $2 :"
        wc -c < "$2"
        
        ```
        
- Variable $? : Renvoyer code de sortie dernière commande
    - Chaque commande renvoie un code de sortie : $? contient code de la dernière commande :
        
        ```bash
        ls /tmp
        echo $?    # → 0 (succès, le dossier existe)
        
        ls /dossier_inexistant
        echo $?    # → 2 (erreur, le dossier n'existe pas)
        ```
        
- Différence entre $@ (préserve chaque argument, 2 éléments) et $* (fusionne tout 1 seul bloc)
    
    ```bash
    ./test.sh "Jean Pierre" Marie
    ```
    
    - `"$@"` = 2 arguments : utiliser plus fréquemment
        - Jean Pierre
        - Marie
    - `"$*"` = 1 seul argument
        - Jean Pierre Marie
- Variable $$ : Contient numéro de processus (PID) du script, uttile script temp uniques : fichier_*temp*="/tmp/script_$$.tmp” : Moyen d'avoir numéro garanti unique à disposition dans  script.
    - Juste un moyen d'avoir un numéro garanti unique à disposition dans ton script.
    - Quand script lancé, système attribue numéro unique (PID). $$ contient ce numéro.
        
        ```bash
        echo "Mon PID est : $$"
        # → Mon PID est : 1234  (un nombre quelconque)
        
        Lancé deux fois de suite :
        ```
        → Mon PID : 1401
        → Mon PID : 1402
        
        # À chaque lancement num différent car nouveau programme qui démarre
        ```
        
    - Utile pour fichiers temporaires ? Parfois script besoin de créer fichier temp pour stocker données intermédiaires :
        
        ```bash
        fichier_temp="/tmp/mon_fichier.tmp"
        ```
        
        - Nom fixe, si quelqu’un lance script deux fois en même temps
            - Lancement 1 écrit dans `/tmp/mon_fichier.tmp`
            - Lancement 2 **écrase** `/tmp/mon_fichier.tmp` → le premier est corrompu
    - Avec $$ le nom devient unique automatiquement :
        
        ```bash
        fichier_temp="/tmp/mon_fichier_$$.tmp"
        # Lancement 1 → /tmp/mon_fichier_1401.tmp
        # Lancement 2 → /tmp/mon_fichier_1402.tmp  → pas de conflit
        ```
        
- shift : Décaler tous arguments d’une position : $2 devient $1…, traiter liste d’arguments un par un
    - Shift décale tous les arguments d’une position
    - Sert surtout à traiter liste d’arguments, un par un
        - Idée : lis premier argument > fais shift > passe au suivant > recommence
        
        ```bash
        #!/bin/bash
        
        echo "Avant shift :"
        echo "\$1 = $1"
        echo "\$2 = $2"
        echo "\$3 = $3"
        
        shift
        
        echo "Après shift :"
        echo "\$1 = $1"
        echo "\$2 = $2"
        echo "\$3 = $3"
        
        # lance ./script.sh alpha beta gamma
        
        Avant shift :
        $1 = alpha
        $2 = beta
        $3 = gamma
        
        Après shift :
        $1 = beta
        $2 = gamma
        $3 =
        ```
        
    - Exemple simple
        
        ```bash
        #!/bin/bash
        
        while [[ -n "$1" ]]; do # tant que le premier argument n’est pas vide, continue
            echo "Argument courant : $1"
            shift
        done
        
        # lance ./script.sh un deux trois
        
        Argument courant : un
        Argument courant : deux
        Argument courant : trois
        ```
        
        - `n` = la chaîne n’est pas vide
        - `$1` = premier argument courant
    - Au départ : `$1=Alice` `$2=Bob` `$3=Charlie/`Après un `shift` : `$1=Bob` `$2=Charlie` — Alice disparaît, tout glisse d'un cran.
        
        ```bash
        #!/bin/bash
        while [[ $# -gt 0 ]]; do  # tant qu’il reste au moins un argument, continue
            echo "Je traite : $1"
            shift          # on passe au suivant
        done
        ```
        ```
        ./script.sh Alice Bob Charlie
        → Je traite : Alice
        → Je traite : Bob
        → Je traite : Charlie
        ```
        
        - `$#` = nombre d’arguments restants
        - `gt 0` = strictement supérieur à 0
- Cheat sheet
    
    
    | **Variable** | **Contenu** |
    | --- | --- |
    | $0 | Nom du script (ex: ./mon_script.sh) |
    | $1, $2, $3… | Arguments passés au script dans l'ordre |
    | $# | Nombre d'arguments passés |
    | "$@" | Tous les arguments séparément (préserve les espaces) — à préférer |
    | "$*" | Tous les arguments fusionnés en un seul bloc |
    | $? | Code de sortie de la dernière commande (0 = succès) |
    | $$ | PID du script — utile pour créer des fichiers temporaires uniques |
    | shift | Décale les arguments : $2 → $1, $3 → $2… (consomme $1) |
    | [[ -z "$1" ]] | Teste si $1 est vide → à utiliser pour vérifier qu'un argument a été donné |
    
    ⚠️ Erreurs classiques : ne pas vérifier si l'argument existe → comportement silencieux · ne pas mettre de guillemets autour de `"$1"` → plante si le fichier a des espaces dans son nom
    
- ❌ Erreur classique
    
    ```bash
    # Oublier de vérifier si l'argument existe
    echo "Bonjour, $1"    # Si lancé sans argument → "Bonjour, " (chaîne vide, pas d'erreur)
    
    # Ne pas mettre de guillemets
    cat $1                 # ❌ Plante si le fichier s'appelle "mon document.txt"
    cat "$1"               # ✅ Correct
    ```
    

### Redirections, erreurs et pipes [>&2, 2>/dev/null, >, >>, tee]

- 3 flux de données : 0 stdin (entrée), 1 stdout (sortie normale), 2 stderr (erreurs) : chaque commande travaille avec ces flux
    - Chaque commande travaille avec trois flux :
        
        ```bash
                          ┌──────────────┐
          Entrée ───────▶ │   Commande   │ ──▶ 1 = Sortie normale (stdout)
          (clavier)       │              │ ──▶ 2 = Erreurs (stderr)
                          └──────────────┘
        ```
        
        | Numéro | Nom | Par défaut |
        | --- | --- | --- |
        | 0 | stdin (entrée) | Le clavier |
        | **1** | **stdout (sortie normale)** | **L'écran** |
        | **2** | **stderr (erreurs)** | **L'écran** |
    - Les redirections permettent de changer la destination de ces flux.
- Rediriger la sortie vers un fichier : Créer/écraser avec >, ajouter avec >> : echo “Text” > fichier.txt
    - Créer / Ecrasser avec > :
        
        ```bash
        echo "Bonjour" > message.txt    # Crée le fichier (ou l'écrase !)
        ls /etc > liste.txt             # La liste va dans le fichier
        ```
        
    - Ajouter avec >> :
        
        ```bash
        echo "Ligne 1" > journal.txt       # Crée le fichier
        echo "Ligne 2" >> journal.txt      # Ajoute à la suite
        echo "Ligne 3" >> journal.txt      # Ajoute encore
        ```
        
- Rediriger les erreurs : Envoyer erreurs dans fichiers 2> , Masquer erreur 2>/dev/null
    
    ```bash
    # Les erreurs vont dans un fichier, la sortie normale s'affiche à l'écran
    ls /dossier_inexistant 2> erreurs.txt
    
    # Masquer les erreurs en les envoyant dans le "trou noir"
    find / -name "mon_fichier" 2>/dev/null
    ```
    
    - /dev/null est une “poubelle”, tout ce qu’on y envoie disparaît.
- Rediriger tout (sortie + erreurs) : 2>&1 (tout → fichier, erreur et sortie), /dev/null 2>&1 (tout → poubelle)
    
    ```bash
    # Tout va dans le même fichier
    ./mon_script.sh > log.txt 2>&1  # > log.txt 2>&1 = "flux 1 va dans log.txt, et flux 2 suit flux 1" → tout finit dans log.txt.
    
    # Tout dans le vide (script silencieux)
    ./mon_script.sh > /dev/null 2>&1
    ```
    
    - Quand l’on fait > log.txt, rediges seulement flux 1
    - Explication de **`2>&1` :** "envoie le flux 2 (erreurs) au même endroit que le flux 1 (sortie normale)".
        - `> log.txt 2>&1` = "flux 1 va dans log.txt, et flux 2 suit flux 1" → **tout** finit dans `log.txt`.
    
    ```bash
    ./script.sh > log.txt          # stdout → fichier, erreurs → écran
    ./script.sh 2> log.txt         # erreurs → fichier, stdout → écran
    ./script.sh > log.txt 2>&1     # tout → fichier
    ./script.sh > /dev/null 2>&1   # tout → la poubelle (silence total)
    ```
    
- Ne pas polluer sortie dans fichier : echo “Erreur : …” >&2
    
    Imagine ce script :
    
    ```
    #!/bin/bash
    
    if [[-z"$1" ]];then
    echo"Erreur : argument manquant" >&2
    exit1
    fi
    
    echo"Dossier :$1"
    ```
    
    Si tu fais :
    
    ```
    ./script.sh > resultat.txt
    ```
    
    - Cas 1 : sans `>&2`
        - Le message d’erreur irait aussi dans `resultat.txt`.
            - Donc ton fichier pourrait contenir :
            
            ```
            Erreur : argument manquant
            ```
            
            - alors que ce n’est pas un “résultat”, c’est un problème.
    - Cas 2 : avec `>&2`
        - Le message d’erreur reste affiché à l’écran, et **ne va pas** dans `resultat.txt`.
        - Donc :
            - `resultat.txt` = sortie normale
            - écran = erreur
            - C’est plus propre.
- Pipes | : envoie sortie commande comme entrée d’une autre.
    - Chaque commande reçoit la sortie de la précédente. C’est une chaîne de traîtement.
    
    ```bash
    # Compter le nombre de fichiers
    ls | wc -l
    
    # Chercher un mot dans un résultat
    ps aux | grep firefox
    
    # Trier et garder les lignes uniques
    cat prenoms.txt | sort | uniq
    ```
    
- Tee : Afficher / sauvegarder en même temps : ls -la | tee log.txt
    
    ```bash
    # Affiche à l'écran ET écrit dans log.txt
    ls -la | tee log.txt
    
    # Ajouter au fichier (au lieu d'écraser)
    date | tee -a journal.log
    ```
    
- Rediriger l’entrée avec < : commande < fichier : wc -l < fichier
    
    ```bash
    # Compter les lignes d'un fichier
    wc -l < mon_fichier.txt
    
    # Trier le contenu d'un fichier
    sort < liste_noms.txt
    ```
    
- Enchaîner plusieurs pipes : ls /etc | grep “\.txt” | wc -l
    
    ```bash
    # Les 5 plus gros fichiers
    ls -lS | head -5
    
    # Compter les fichiers .txt dans /etc
    ls /etc | grep "\.txt" | wc -l
    ```
    
- Cheat sheet
    
    
    | Syntaxe | Effet |
    | --- | --- |
    | `commande > fichier` | Sortie dans fichier (écrase) |
    | `commande >> fichier` | Sortie dans fichier (ajoute) |
    | `commande 2> fichier` | Erreurs dans fichier |
    | `commande > fichier 2>&1` | Tout dans fichier |
    | `commande < fichier` | Entrée depuis un fichier |
    | `cmd1 \| cmd2` | Sortie de cmd1 → entrée de cmd2 |
    | `commande \| tee fichier` | Affiche ET sauvegarde |
    | `commande > /dev/null 2>&1` | Silence total |
- ❌ Erreur classique
    
    ```bash
    # Confondre > et >> : tu écrases un fichier important !
    echo "nouveau" > config.txt     # ❌ Tout l'ancien contenu est perdu
    echo "nouveau" >> config.txt    # ✅ Ajoute à la fin
    
    # Oublier 2> : les erreurs s'affichent en vrac et polluent la sortie
    find / -name "*.log"            # ❌ Des dizaines de "Permission denied"
    find / -name "*.log" 2>/dev/null  # ✅ Erreurs masquées
    ```
    

### Opérateurs, calculs et logique

- Calcul en bash avec nombres entiers : $(( expression )), $((var1 + var2))
    
    ```bash
    a=10
    b=3
    
    echo "Addition      : $((a + b))"      # 13
    echo "Soustraction  : $((a - b))"      # 7
    echo "Multiplication: $((a * b))"      # 30
    echo "Division      : $((a / b))"      # 3 (entière, pas de virgule !)
    echo "Modulo        : $((a % b))"      # 1 (reste de la division)
    ```
    
    - Attention : la division est entière. 10 / 3 donne 3, pas 3.33.
    - Ex :
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Opérateurrs arithmétiques : +, -, *, /, %, **
    
    
    | Opérateur | Signification | Exemple | Résultat |
    | --- | --- | --- | --- |
    | `+` | Addition | `$((5 + 3))` | `8` |
    | `-` | Soustraction | `$((5 - 3))` | `2` |
    | `*` | Multiplication | `$((5 * 3))` | `15` |
    | `/` | Division entière | `$((5 / 3))` | `1` |
    | `%` | Modulo (reste) | `$((5 % 3))` | `2` |
    | `**` | Puissance | `$((2 ** 3))` | `8` |
- Stocker résultat : nom_var=$(var1 opérateur var2), prix_final=$((prix - reduction))
    
    ```bash
    prix=50
    reduction=15
    prix_final=$((prix - reduction))
    echo "Le prix final est $prix_final euros"
    ```
    
    - Ex :
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Opérateurs logiques : && (ET, les conditions doivent être vraies), \|\| (OU, au moins une doit être vraie), ! (NON, inverse condition)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `&&` | ET — les deux conditions doivent être vraies |
    | `\|\|` | OU — au moins une doit être vraie |
    | `!` | NON — inverse la condition |
    
    ```bash
    age=25
    [[ $age -ge 18 && $age -le 65 ]]    # Vrai : entre 18 et 65
    
    [[ $age -lt 10 || $age -gt 60 ]]    # Faux : ni < 10, ni > 60
    
    [[ ! $age -lt 18 ]]                 # Vrai : 25 n'est PAS < 18
    [[ ! -d $1 ]]                       # $1 n'est pas un dossier
    ```
    
    - Ex :
        
        ```bash
        age=25
        
        if [[ $age -ge 18 && $age -le 65 ]]; then
            echo "Âge dans la tranche"
        fi
        ```
        
        ```bash
        age=70
        
        if [[ $age -lt 18 || $age -gt 65 ]]; then
            echo "Tarif spécial"
        fi
        ```
        
        ```bash
        if [[ ! -d "$1" ]]; then
            echo "Ce n'est pas un dossier"
        fi
        ```
        
        ```bash
        if [[ -f "$chemin" ]]; then
            echo "$chemin est un fichier"
        
            [[ -r "$chemin" ]] && echo "Le fichier est lisible" || echo "Le fichier n'est pas lisible"
            [[ -w "$chemin" ]] && echo "Le fichier est modifiable" || echo "Le fichier n'est pas modifiable"
            [[ -x "$chemin" ]] && echo "Le fichier est exécutable" || echo "Le fichier n'est pas exécutable"
        
        else
            echo "$chemin existe, mais ce n'est ni un fichier ni un dossier"
        fi
        ```
        
- Raccourcis avec && (mkdir dossier && echo “Dossier créé !” si commande réussit alors fait) et || (cd /inexistant || echo “Dossier existe pas” si commande échoue alors fait) entre commandes
    
    ```bash
    # Si la commande réussit, ALORS fait ceci
    mkdir mon_dossier && echo "Dossier créé !"
    
    # Si la commande échoue, ALORS fait cela
    cd /inexistant || echo "Le dossier n'existe pas"
    ```
    
- Incrémenter un compteur : ((var++)), ((var +=)), ((compteur++)) → 1, ((compteur += 5)) → 6
    
    ```bash
    compteur=0
    ((compteur++))       # → 1
    ((compteur++))       # → 2
    ((compteur += 5))    # → 7
    ```
    
    - Ex :
        
        ```bash
        fichiers=0
        
        ((fichiers++))
        ((fichiers++))
        
        echo "Nombre de fichiers traités : $fichiers"
        ```
        
- Calcul décimal pour nombres virgules avec bc
    
    ```bash
    echo "scale=2; 10 / 3" | bc
    # → 3.33
    
    resultat=$(echo "scale=2; 10 / 3" | bc)
    echo "Le résultat est $resultat"
    ```
    
- Comparer avec (( )) (syntaxe mathématique) : (( var > 5 )), (( var == 10 ))
    - Dans doubles parenthèses, utiliser symboles habituels
        
        ```bash
        a=10
        (( a > 5 ))     # Vrai
        (( a == 10 ))   # Vrai
        ```
        
        - Dans (( )), pas besoin de $ devant les variables.
    - Ex :
        
        ```bash
        a=10
        
        if (( a > 5 )); then
            echo "a est supérieur à 5"
        fi
        ```
        
        ```bash
        tentatives=4
        
        if (( tentatives >= 3 )); then
            echo "Compte bloqué"
        fi
        ```
        
        - Modulo
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Vérifier que des chiffres / nombres en arguments : [[ "$1" =~ ^-?[0-9]+$ ]]
    
    ```bash
    if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
        echo "Erreur : les deux arguments doivent être des nombres entiers"
        exit 1
    fi
    ```
    
    - Ce que ça veut dire :
        - `^` = début
        - `?` = signe  optionnel
        - `[0-9]+` = un ou plusieurs chiffres
        - `$` = fin
        
        Donc ça accepte :
        
        - `2`
        - `45`
        - `8`
        
        Mais pas :
        
        - `abc`
        - `4a`
        - `12.5`
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ $# -ne 2 ]]; then
            echo "Erreur : il faut deux arguments"
            echo -e "Usage :\n\t$0 <nombre1> <nombre2>"
            exit 1
        fi
        
        if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
            echo "Erreur : les deux arguments doivent être des nombres entiers"
            exit 1
        fi
        
        echo "La somme de vos deux nombres est : $(($1 + $2))"
        echo "La différence de vos deux nombres est : $(($1 - $2))"
        echo "Le produit de vos deux nombres est : $(($1 * $2))"
        ```
        
- Quand ça plante, lire code de retour : $?
    
    ```bash
    ma_commande
    echo "Code de retour : $?"
    # 0 = tout va bien, autre chose = problème
    ```
    
- Cheat sheet
    
    
    | Élément | Usage concret |
    | --- | --- |
    | `$((a + b))` | faire un calcul |
    | `prix_final=$((prix-reduction))` | stocker un résultat |
    | `-gt`, `-lt`, `-eq` | comparer des nombres |
    | `==`, `!=`, `-z`, `-n` | comparer du texte / tester vide |
    | `&&`, ` |  |
    | `-f`, `-d`, `-e` | tester fichier / dossier / existence |
    | `((compteur++))` | compter |
    | `bc` | faire des décimales |
    | `(( a > 5 ))` | comparer des nombres simplement |
    | `$?` | voir si une commande a réussi |
- ❌ Erreur classique
    
    ```bash
    # Confondre = (affectation) et -eq (comparaison)
    if [[ $age = 18 ]]; then     # ⚠️ Compare comme du TEXTE, pas un nombre
    if [[ $age -eq 18 ]]; then   # ✅ Compare comme un NOMBRE
    
    # Oublier $(( )) pour le calcul
    resultat=5+3                  # ❌ resultat vaut le TEXTE "5+3"
    resultat=$((5 + 3))           # ✅ resultat vaut le NOMBRE 8
    ```
    

### Conditions, comparaisons et tests [if, elif, else…]

- Structure if : if [[ condition ]]; then # … fi
    - Règles de syntaxe :
        - Espace après [[ et avant ]]
        - Espace autour de l’opérateur
        - then sur la même ligne (avec ;) ou sur la ligne suivante
    
    ```bash
    if [[ condition ]]; then
        # code si la condition est vraie
    fi
    ```
    
    - **Note :** `fi` c'est `if` à l'envers. C'est la fermeture du bloc.
    - Ex :
        
        ```bash
        nombre=15
        if [[ $nombre -gt 10 ]]; then
            echo "Le nombre est supérieur à 10"
        fi
        ```
        
- if … else
    
    ```bash
    nombre=5
    if [[ $nombre -gt 10 ]]; then
        echo "Supérieur à 10"
    else
        echo "Inférieur ou égal à 10"
    fi
    ```
    
- if … elif … else : Autant de elif que l’on veut, mais un seul else (à la fin), et un seul fi
    - Autant de elif que l’on veut, mais un seul else (à la fin), et un seul fi
    
    ```bash
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
    ```
    
    ```bash
    chemin="$1"
    
    if [[ -z "$chemin" ]]; then
        echo "Erreur : vous devez indiquer un chemin"
        exit 1
    elif [[ ! -e "$chemin" ]]; then
        echo "Erreur : $chemin n'existe pas"
        exit 1
    elif [[ -f "$chemin" ]]; then
        echo "$chemin est un fichier"
    
        [[ -r "$chemin" ]] && echo "Le fichier est lisible" || echo "Le fichier n'est pas lisible"
        [[ -w "$chemin" ]] && echo "Le fichier est modifiable" || echo "Le fichier n'est pas modifiable"
        [[ -x "$chemin" ]] && echo "Le fichier est exécutable" || echo "Le fichier n'est pas exécutable"
    
    elif [[ -d "$chemin" ]]; then
        echo "$chemin est un dossier"
        nbr_elements=$(ls "$chemin" | wc -l)
        echo "Il y a $nbr_elements éléments dans le dossier"
    
    else
        echo "$chemin existe, mais ce n'est ni un fichier ni un dossier"
    fi
    ```
    
- Comparer nombres : -eq (égal), -ne (différent), -lt (inférieur), -le (inférieur ou égal), -gt (supérieur), -ge (supérieur ou égal)
    
    
    | Opérateur | Signification | Moyen mnémotechnique |
    | --- | --- | --- |
    | -eq | Égal | **eq**ual |
    | -ne | Différent | **n**ot **e**qual |
    | -lt | Inférieur | **l**ess **t**han |
    | -le | Inférieur ou égal | **l**ess or **e**qual |
    | -gt | Supérieur | **g**reater **t**han |
    | -ge | Supérieur ou égal | **g**reater or **e**qual |
    
    ```bash
    age=25
    [[ $age -ge 18 ]]    # Est-ce que 25 ≥ 18 ? → Vrai
    [[ $age -eq 30 ]]    # Est-ce que 25 = 30 ? → Faux
    ```
    
    - Ex
        
        ```bash
        if [ $# -eq 0 ]
        then
            echo -e "You need to specify the target domain.\n"
            echo -e "Usage:"
            echo -e "\t$0 <domain>"
            exit 1
        else
            domain=$1
        fi
        ```
        
        ```bash
        age=25
        
        if [[ $age -ge 18 ]]; then
            echo "Majeur"
        fi
        ```
        
        ```bash
        tentatives=5
        
        if [[ $tentatives -gt 3 ]]; then
            echo "Trop de tentatives"
        fi
        ```
        
- Comparer chaînes de texte : = ou == (identiques), ≠ (! = différentes), -z (chaïne vide), -n (chaïne n’est pas vide)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `=` ou `==` | Les chaînes sont identiques |
    | `!=` | Les chaînes sont différentes |
    | `-z` | La chaîne est vide |
    | `-n` | La chaîne n'est pas vide |
    
    ```bash
    nom="Alice"
    [[ "$nom" == "Alice" ]]    # Vrai
    [[ "$nom" != "Bob" ]]      # Vrai
    [[ -z "$nom" ]]            # Faux (pas vide)
    ```
    
    - Ex :
        
        ```bash
        prenom="Camille"
        
        if [[ "$prenom" == "Camille" ]]; then
            echo "Bonjour Camille"
        fi
        ```
        
        ```bash
        nom=""
        
        [[ -z "$nom" ]] && echo "Le nom est vide"
        [[ -n "$nom" ]] && echo "Le nom n'est pas vide"
        ```
        
- Test sur fichiers & dossiers : -e (fichier existe), -f (fichier normal), -d (c’est dossier), -s (fichier pas vide), -r (fichier est lisible), -w (fichier est modifiable), -x (fichier est exec)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `-e fichier` | Le fichier existe |
    | `-f fichier` | C'est un fichier normal |
    | `-d fichier` | C'est un dossier |
    | `-s fichier` | Le fichier n'est pas vide |
    | `-r fichier` | Le fichier est lisible |
    | `-w fichier` | Le fichier est modifiable |
    | `-x fichier` | Le fichier est exécutable |
    
    ```bash
    [[ -f "/etc/passwd" ]]    # Vrai (le fichier existe)
    [[ -d "/home" ]]          # Vrai (c'est un dossier)
    [[ ! -d $1 ]]             # $1 n'est pas un dossier
    ```
    
    - Ex :
        - -e : existe
            
            ```bash
            if [[-e"notes.txt" ]];then
            echo"Le fichier existe"
            fi
            ```
            
        - -f : fichier normal
            
            ```bash
            if [[ -f "notes.txt" ]]; then
                echo "C'est un fichier"
            fi
            ```
            
        - -d : dossier
            
            ```bash
            if [[ -d "/home/kali" ]]; then
                echo "C'est un dossier"
            fi
            ```
            
        - -s : pas vide
            
            ```bash
            if [[ -s "rapport.txt" ]]; then
                echo "Le fichier contient quelque chose"
            fi
            ```
            
        - -r : lisible
            
            ```bash
            if [[ -r "/etc/passwd" ]]; then
                echo "Le fichier est lisible"
            fi
            ```
            
        - -w : modifiable
            
            ```bash
            if [[ -w "rapport.txt" ]]; then
                echo "Je peux écrire dedans"
            fi
            ```
            
        - -x : exécutable
            
            ```bash
            if [[ -x "script.sh" ]]; then
                echo "Le script est exécutable"
            fi
            ```
            
        - Combiner plusieurs
            
            ```bash
            chemin="$1"
            
            if [[ -z "$chemin" ]]; then
                echo "Erreur : vous devez indiquer un chemin"
                exit 1
            elif [[ ! -e "$chemin" ]]; then
                echo "Erreur : $chemin n'existe pas"
                exit 1
            elif [[ -f "$chemin" ]]; then
                echo "$chemin est un fichier"
            
                [[ -r "$chemin" ]] && echo "Le fichier est lisible" || echo "Le fichier n'est pas lisible"
                [[ -w "$chemin" ]] && echo "Le fichier est modifiable" || echo "Le fichier n'est pas modifiable"
                [[ -x "$chemin" ]] && echo "Le fichier est exécutable" || echo "Le fichier n'est pas exécutable"
            
            elif [[ -d "$chemin" ]]; then
                echo "$chemin est un dossier"
                nbr_elements=$(ls "$chemin" | wc -l)
                echo "Il y a $nbr_elements éléments dans le dossier"
            
            else
                echo "$chemin existe, mais ce n'est ni un fichier ni un dossier"
            fi
            ```
            
- Tests utiles : [[ -f “fichier.txt” ]], [[ -d "/home" ]], [[ -e "$1" ]], [[ -z "$nom" ]], [[ -n "$nom" ]], [[ $a -gt $b ]]
    
    
    | Test | Signification | Exemple |
    | --- | --- | --- |
    | -f | Le fichier existe | [[ -f “fichier.txt” ]] |
    | -d | Le dossier existe | [[ -d "/home" ]] |
    | -e | Le chemin existe (fichier ou dossier) | [[ -e "$1" ]] |
    | -z | La chaîne est vide | [[ -z "$nom" ]] |
    | -n | La chaîne n'est pas vide | [[ -n "$nom" ]] |
    | -gt | Le nombre est supérieur | [[ $a -gt $b ]] |
- Ex concret :
    - Vérifier un fichier
        
        ```bash
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
        ```
        
    - Combiner conditions
        
        ```bash
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
        ```
        
- Conditions imbriquées : mettre if dans un autre if
    
    ```bash
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
    ```
    
    - Si conditions imbriquées dépassent 2-3 niveaux, préférable de simplifier
- [ ] vs [[ ]] : Ancienne et syntaxe plus moderne
    - `[[ ]]` (la syntaxe moderne). Mais possible de voir `[ ]` dans scripts existants, c’est l’ancienne syntaxe. Elle fonctionne mais plis fragile (plante si une variable est vide et non protégée par des guillemets).
    
    ```bash
    # Avec [ ] — risqué si $nom est vide
    [ $nom = "Alice" ]     # ❌ Erreur si $nom est vide
    
    # Avec [[ ]] — pas de problème
    [[ $nom == "Alice" ]]  # ✅ Fonctionne même si $nom est vide
    ```
    
    **Règle simple :** utilise `[[ ]]` dans tes scripts. Si tu vois `[ ]` ailleurs, sache que c'est l'équivalent en plus ancien.
    
- ❌ Erreur classique
    
    ```bash
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
    ```
    

### Boucles : répètent des actions, deux façons de penser:

- for : répéter sur liste d’éléments : for var in X; do … done / for var in {1..10..2}; do … done
    - Forme générale
        
        ```bash
        for variable in liste; do
            commande
        done
        ```
        
    - Pour parcourir : liste de mots, suite de nombres, fichiers, arguments d’un script
    - Qu’est-ce qui change à chaque tour ? souvent la variable (fruit; fichier, i)
    - Qu’est-ce qui arrête la boucle ? la liste est terminée
    - Ex typiques
        - Parcourir tous les fichiers logs
            
            ```bash
            for fichier in *.log; do
                echo "$fichier"
            done
            ```
            
        - Parcourir une liste de mot
            
            ```bash
            for fruit in pomme banane cerise; do
                echo "J'aime la $fruit"
            done
            
            # Resultat 
            J'aime la pomme
            J'aime la banane
            J'aime la cerise
            ```
            
        - Parcourir une plage de nombres
            
            ```bash
            for i in {1..5}; do
                echo "Tour numéro $i"
            done
            ```
            
            - Parcourir avec un pas
                
                ```bash
                # Compter de 2 en 2
                for i in {0..10..2}; do
                    echo $i
                done
                # → 0, 2, 4, 6, 8, 10
                ```
                
        - Parcourir les arguments
            
            ```bash
            for arg in "$@"; do
                echo "Argument : $arg"
            done
            ```
            
        - Afficher table de multiplication d’un nombre donné
            
            ```bash
            for i in {1..10}; do
                echo "$1 x $i = $(($1 * $i))"
            done
            ```
            
    - ❌ Erreurs fréquentes
        - Oublier do ou done
            
            ```bash
            for i in {1..5}
                echo "$i"
            ```
            
        - Ne pas comprendre ce que contient la variable
            - fichier ne contient qu’un seul nom de fichier à la fois, pas toute la liste
            
            ```bash
            for fichier in *.txt; do
                echo "$fichier"
            done
            ```
            
- boucle while = répéter tant qu’une condition est vraie
    - Forme générale
        
        ```bash
        while condition; do
        	commande
        done
        ```
        
    - Pour : travailler avec compteur, lire fichier ligne par ligne, répéter action tant qu’une condition est vraie, traiter progressivement arguments
    - Qu’est-ce qui change à chaque tour ? souvent compteur, argument, ou ligne lue
    - Qu’est-ce qui arrête la boucle ? dans while : la condition devient fausse
    - Ex typiques :
        - Lire un fichier de cibles
        
        ```bash
        while read -r cible; do
            echo "Scan de $cible"
        done < cibles.txt
        ```
        
        - Lire fichier ligne par ligne
            - `-r` empêche `read` d'interpréter les caractères spéciaux comme `\`. C'est une bonne pratique.
        
        ```bash
        while read -r ligne; do
            echo "Lu : $ligne"
        done < mon_fichier.txt
        ```
        
        - Compteur
        
        ```bash
        compteur=1
        while [[ $compteur -le 5 ]]; do
            echo "$compteur"
            ((compteur++))
        done
        ```
        
        - Parcourir argument avec shift
        
        ```bash
        while [[ $# -gt 0 ]]; do
            echo "Argument courant : $1"
            shift
        done
        ```
        
    - ❌ Erreurs fréquentes
        - Boucle infinie
            - Ici, compteur change jamais, donc condition reste vraie pour toujours
            
            ```bash
            compteur=1
            while [[ $compteur -le 5 ]]; do
                echo "$compteur"
            done
            ```
            
            - Solution : évoluer condition avec `((compteur++))`
        - Oublier ce que lit read : Qu’une seule ligne à la fois
            
            ```bash
            while read -r ligne; do
                echo "$ligne"
            done < fichier.txt
            ```
            
- Boucle until : inverse de while : boucle tant que la condition est fause
    - En pratique, while est beaucoup plus courant, until est juste une autre façon d’écrire certaines boucles
    
    ```bash
    compteur=1
    until [[ $compteur -gt 5 ]]; do
        echo "Compteur : $compteur"
        ((compteur++))
    done
    ```
    
- break & continue : sortir de la boucle / sauteur au tour suivant
    - Break : sortir de la boucle
        
        ```bash
        for i in {1..10}; do
            if [[ $i -eq 6 ]]; then
                echo "Stop à $i"
                break
            fi
            echo "Numéro $i"
        done
        # Affiche 1, 2, 3, 4, 5 puis "Stop à 6"
        ```
        
    - Continue : sauter au tour suivant
        
        ```bash
        for i in {1..5}; do
            if [[ $i -eq 3 ]]; then
                continue
            fi
            echo "Numéro $i"
        done
        # Affiche 1, 2, 4, 5 (le 3 est sauté)
        ```
        
- Le for style C (pour les plages dynamiques)
    - Syntaxe {1005} ne fonctionne pas avec des variables, pour ça :
    
    ```bash
    limite=$1
    for (( i=1; i<=limite; i++ )); do
        echo "Tour $i"
    done
    ```
    
- Boucles imbriquées
    
    ```bash
    for i in {1..3}; do
        for j in {1..3}; do
            echo "i=$i, j=$j"
        done
    done
    ```
    
- Déboguer une boucle : Ajouter echo temporaires
    - Si pas de [DEBUG], c’est que la boucle ne s’exécute pas (peut-être qu’il n’y a aucun .txt dans le dossier).
    
    ```bash
    for fichier in *.txt; do
        echo "[DEBUG] fichier = '$fichier'"    # ← ajoute ça
        # ... le reste du code
    done
    ```
    

### Fonctions et case : bloc de code réutilisable

- Définir et appeler fonction : nom() { … }
    
    ```bash
    # 1. Définir la fonction
    saluer() {
        echo "Salut, bienvenue !"
    }
    
    # 2. L'appeler (juste son nom, sans parenthèses)
    saluer
    saluer
    ```
    
    - Règle : Définition doit apparaître avant l’appel dans le script
- Passer arguments à une fonction :
    - A l’intérieur de la fonction, $1, $2 … sont les arguments de la fonction (pas du script)
    
    ```bash
    saluer() {
        echo "Bonjour, $1 ! Tu as $2 ans." 
    }
    
    saluer "Alice" 25  # $1 = Alice / $2 = 25
    saluer "Bob" 30
    
    # Résultat 
    Bonjour, Alice ! Tu as 25 ans.
    Bonjour, Bob ! Tu as 30 ans.
    ```
    
    - Quand utiliser argument ? Ne pas créer fonction qui ne marche qu’avec valeur écrite en dur, faire fonction qui reçoit valeur en argument
        
        ```bash
        afficher_fichier() {
            cat "$1"
        }
        ```
        
        ```bash
        afficher_fichier notes.txt
        afficher_fichier rapport.txt
        ```
        
    - Ex
        - Script à ses propres arguments, la fonction à les sienne
            
            ```bash
            #!/bin/bash
            
            echo "Argument du script : $1"
            
            ma_fonction() {
                echo "Argument de la fonction : $1"
            }
            
            ma_fonction "test"
            
            # argument du script = bonjour
            # argument de la fonction = test
            ```
            
        - Même si utilise qu’une fois, le nom afficher_aide dit déjà ce que fait le bloc
            
            ```bash
            afficher_aide() {
                echo "Usage : $0 <option>"
            }
            ```
            
- Récupérer résultat d’une fonction : resultat=$(ma_fonction ...)
    - En bash, fonction “renvoie” souvent résultat en l’affichant avec **echo**, ensuite on récupère résultat avec :
        
        ```bash
        resultat=$(ma_fonction ...)
        ```
        
    - Ex :
        - Addition dans fonction
        
        ```bash
        addition() {
            echo $(( $1 + $2 ))
        }
        
        resultat=$(addition 15 27)
        echo "La somme est : $resultat"
        
        # - la fonction calcule `15 + 27`
        # - elle affiche `42`
        # - `$(...)` récupère cette sortie
        # - `resultat` reçoit `42`
        ```
        
    
    ```bash
    addition() {
        echo $(( $1 + $2 ))
    }
    
    resultat=$(addition "$1" "$2")
    echo "La somme est : $resultat"
    ```
    
- Variables dans fonctions : Globales v locales. local var
    - Par défaut : Var créée dans une fonction est souvent globale, ca veut donc dire qu’elle peut modifier le reste du script
        
        ```bash
        nom="Global"
        
        modifier() {
            nom="Local"
            echo "Dans la fonction : $nom"
        }
        
        echo "Avant : $nom"    # → Global
        modifier               # → Local
        echo "Après : $nom"    # → Local (affecté)
        ```
        
        - Résultat :
            - avant = Global
            - dans la fonction = Local
            - après = Local
        - La variable a été modifiée partout.
    - Garder var exclusive dans fonction
        - nom reste local à la fonction
        
        ```bash
        modifier() {
            local nom="Local"
            echo "Dans la fonction : $nom"
        }
        ```
        
        - Résultat :
            - avant = Global
            - dans la fonction = Local
            - après = Global
        
        ```bash
        #!/bin/bash
        
        nom="Global"
        
        modifier() {
            local nom="Local"
            echo "Dans la fonction : $nom"
        }
        
        echo "Avant : $nom"
        modifier
        echo "Après : $nom"
        
        remodifuer() {
            nom="Modif"
            echo "Dans le fonction test : $nom"
        }
        
        echo "Avant : $nom"
        remodifuer
        echo "Après : $nom"
        
        # résultat
        
        ┌──(kali㉿kali)-[~/Desktop/scripts]
        └─$ ./test.sh
        Avant : Global
        Dans la fonction : Local
        Après : Global
        Avant : Global
        Dans le fonction test : Modif
        Après : Modif
        ```
        
- Affecter valeur par défaut pour arguments : ${1:-"valeur"}
    - Si aucun argument n’est donné, prends cette valeur par défaut
        
        ```bash
        ${1:-"valeur"}
        
        # utilise $1 s’il existe, sinon mets "Inconnu"
        ```
        
    - Ex :
        
        ```bash
        saluer() {
            local nom=${1:-"Inconnu"}
            echo "Bonjour, $nom !"
        }
        
        saluer "Alice"
        saluer
        
        # résultat
        avec argument → Bonjour, Alice !
        sans argument → Bonjour, Inconnu !
        ```
        
- Code retour fonction return
    
    ```bash
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
    ```
    
- Faire un choix parmi possibilités : case
    - Forme générale de case
        - Si rien ne correspond, prend le *
        
        ```bash
        case variable in
            motif1)
                commandes ;;
            motif2)
                commandes ;;
            *)
                commandes ;;
        esac
        ```
        
    - **Notes :**
        - `esac` c'est `case` à l'envers (fermeture du bloc)
        - Chaque bloc se termine par `;;`
        - est le cas par défaut (si rien d'autre ne correspond)
        - `|` sépare plusieurs patterns pour le même bloc
    - Ex :
        
        ```bash
        case $1 in
            oui|o|yes|y)      
                echo "Tu as dit oui." ;;
            non|n|no)
                echo "Tu as dit non." ;;
            *)
                echo "Réponse non reconnue." ;;
        esac
        ```
        
        ```bash
        case $1 in
            start)
                echo "Démarrage" ;;
            stop)
                echo "Arrêt" ;;
            restart)
                echo "Redémarrage" ;;
            *)
                echo "Commande inconnue" ;;
        esac
        ```
        
        ```bash
        case $1 in
            jpg|jpeg)
                echo "Image JPEG" ;;
            png)
                echo "Image PNG" ;;
            gif)
                echo "Image GIF" ;;
            *)
                echo "Extension inconnue" ;;
        esac
        ```
        
- ❎ Fonction + case
    - Case choisit quoi faire + fonction contient bloc d’action
    
    ```bash
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
    
    # Résultat
    ./outil.sh -l      # Liste les fichiers
    ./outil.sh -d      # Affiche la date
    ./outil.sh -h      # Affiche l'aide
    ./outil.sh -z      # "Option '-z' inconnue."
    ```
    
    ```bash
    afficher_aide() {
        echo "Options disponibles :"
        echo "  -h  aide"
        echo "  -d  date"
        echo "  -u  utilisateur"
    }
    
    case $1 in
        -h) afficher_aide ;;
        -d) date ;;
        -u) whoami ;;
        *)
            echo "Option inconnue"
            afficher_aide ;;
    esac
    ```
    
- Menu interactif avec select
    - Syntaxe simple :
        
        ```bash
        echo "Que veux-tu faire ?"
        select choix in "Date" "Utilisateur" "Quitter"; do
            echo "Tu as choisi : $choix"
        done
        ```
        
    - Ex :
        
        ```bash
        echo "Que veux-tu faire ?"
        select choix in "Lister les fichiers" "Afficher la date" "Quitter"; do
            case $choix in
                "Lister les fichiers") ls ;;
                "Afficher la date") date ;;
                "Quitter") echo "Au revoir." ; break ;;
                *) echo "Choix invalide." ;;
            esac
        done
        ```
        
- Décaler les arguments shift : Traiter argument un par un
    - Sert à supprimer premier argument puis à décaler tous les autres
    - En gros : je regarde `$1` >je décide quoi en faire > je fais `shift` > je passe au suivant > Pour les scripts avec des flags comme `-n 42 -s "texte"`
    - Parcourir argument avec while + shift
        
        ```bash
        while [[ $# -gt 0 ]]; do
            echo "Argument courant : $1"
            shift
        done
        
        # ce qu'il se passe 
        $# = nombre d’arguments restants
        tant qu’il en reste, on continue
        shift enlève l’argument courant
        le suivant devient $1
        ```
        
    - Shift 2 : Parfois option prend 2 morceaux (flag et sa valeur)
        
        ```bash
        -n 42 
        # $1 = -n
        # $2 = 42
        ```
        
        - Si l’on veut consommer les deux d’un coup shift 2
        
        ```bash
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
        ```
        
        - Ce qu’il se passe concrétement
            
            ### Cas `n`
            
            Si l’utilisateur tape :
            
            ```
            ./script.sh-n42-s bonjour
            ```
            
            au début :
            
            - `$1 = -n`
            - `$2 = 42`
            
            Le script fait :
            
            - `nombre="$2"` → donc `nombre=42`
            - `shift 2` → on enlève `n` et `42`
            
            Ensuite il reste :
            
            - `$1 = -s`
            - `$2 = bonjour`
            
            Puis le script continue.
            
        - cas très simple : `./script.sh -u alice -p secret`
            
            Au départ :
            
            - `$1 = -u`
            - `$2 = alice`
            - `$3 = -p`
            - `$4 = secret`
            
            Si tu fais :
            
            - `shift 2`
            
            alors il reste :
            
            - `$1 = -p`
            - `$2 = secret`
            
            Tu as donc “consommé” :
            
            - `u`
            - `alice`
        
- Mini modèles à retenir
    - **Modèle 1 — fonction simple**
    
    ```bash
    saluer() {
        echo "Bonjour !"
    }
    
    saluer
    ```
    
    ---
    
    - **Modèle 2 — fonction avec arguments**
    
    ```bash
    saluer() {
        echo "Bonjour, $1 !"
    }
    
    saluer "Alice"
    ```
    
    ---
    
    - **Modèle 3 — fonction qui “renvoie” un résultat**
    
    ```bash
    addition() {
        echo $(( $1 + $2 ))
    }
    
    resultat=$(addition 3 4)
    echo "$resultat"
    ```
    
    ---
    
    - **Modèle 4 — fonction avec variable locale**
    
    ```bash
    saluer() {
        local nom=${1:-"Inconnu"}
        echo "Bonjour, $nom !"
    }
    ```
    
    ---
    
    - **Modèle 5 — `case` simple**
    
    ```bash
    case $1 in
        oui) echo "Oui" ;;
        non) echo "Non" ;;
        *) echo "Inconnu" ;;
    esac
    ```
    
    ---
    
    - **Modèle 6 — `case` + fonction**
    
    ```bash
    aide() {
        echo "Utilisation : $0 [option]"
    }
    
    case $1 in
        -h) aide ;;
        *) echo "Option inconnue" ;;
    esac
    ```
    

**Autonome :** Crée un script `outil.sh` avec les options `-l` (lister les fichiers), `-d` (afficher la date), `-u` (afficher l'utilisateur) en utilisant `case` et des fonctions.

Crée un script `gestion.sh` qui :

1. Propose un menu avec `case` : 1) Lister les fichiers .txt, 2) Compter les lignes d'un fichier, 3) Quitter
2. Chaque option appelle une fonction dédiée
3. La boucle `while true` permet de revenir au menu après chaque action
4. L'option "Quitter" utilise `break` pour sortir

### Workflow divers [ { echo … echo … } >]

- Retour à la ligne dans fichier de sortie : { echo … echo … } > fichier.txt
    - Commencer par accolade puis mettre echo + contenu et terminer par accolade et redirect
        
        ```bash
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        ```
        
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument" >&2
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide" >&2
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        
        ```
        
- Vérifier que des chiffres / nombres en arguments : [[ "$1" =~ ^-?[0-9]+$ ]]
    
    ```bash
    if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
        echo "Erreur : les deux arguments doivent être des nombres entiers"
        exit 1
    fi
    ```
    
    - Ce que ça veut dire :
        - `!` : inverse le test
        - `=~` : “est-ce que `$1` correspond à ce motif ?”
        - ^-?[0-9]+$ : REGEX
        - `^` = début
        - `?` = signe  optionnel
        - `[0-9]+` = un ou plusieurs chiffres
        - `$` = fin
        - `||` : ou
        
        Donc ça accepte :
        
        - `2`
        - `45`
        - `8`
        
        Mais pas :
        
        - `abc`
        - `4a`
        - `12.5`
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ $# -ne 2 ]]; then
            echo "Erreur : il faut deux arguments"
            echo -e "Usage :\n\t$0 <nombre1> <nombre2>"
            exit 1
        fi
        
        if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
            echo "Erreur : les deux arguments doivent être des nombres entiers"
            exit 1
        fi
        
        echo "La somme de vos deux nombres est : $(($1 + $2))"
        echo "La différence de vos deux nombres est : $(($1 - $2))"
        echo "Le produit de vos deux nombres est : $(($1 * $2))"
        ```
        

- Entrainement divers
    - Script laisse choix avec argument (fonction+case)
        
        ```bash
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
        ```
        
        ```bash
        afficher_aide() {
            echo "Options disponibles :"
            echo "  -h  aide"
            echo "  -d  date"
            echo "  -u  utilisateur"
        }
        
        case $1 in
            -h) afficher_aide ;;
            -d) date ;;
            -u) whoami ;;
            *)
                echo "Option inconnue"
                afficher_aide ;;
        esac
        ```
        
    - Faciliter scans nmap
        
        ```bash
        #!/bin/bash
        
        read -p "L'adresse à scanner : " ip_scan
        echo "Scan de $ip_scan en cours..."
        nmap -F -sV "$ip_scan"
        ```
        
        - Version optimisée avec sortie erreur
            
            ```bash
            #!/bin/bash
            
            read -p "Adresse IP ou hôte à scanner : " target
            
            if [[ -z "$target" ]]; then  # [[ .. ] : test de condition / -z : vide
                echo "Erreur : aucune cible saisie." >&2  # Affiche erreur
                exit 1  # 1 : arrêter script avec erreur
            fi  # fin du if
            
            echo "Scan de $target en cours..."
            nmap -F -sV "$target"
            ```
            
        - Evolution à faire
            - Vérifier que `$ip_scan` n'est pas vide avant de lancer le scan
            - Proposer plusieurs types de scans (rapide, complet, UDP...)
            - Sauvegarder le résultat dans un fichier
    - Comparaison fichier
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur, script attends <fichier1> et <fichier2>"
                exit 1
        fi
        
        echo "Comparaison de $1 et $2"
        echo "Taille de $1 :"
        wc -c < "$1"    # < "$1" = redirige le contenu du fichier $1 vers wc
        echo "Taille de $2 :"
        wc -c < "$2"
        
        ```
        
    - Traiter liste d’arguments un par un
        
        ```bash
        #!/bin/bash
        
        while [[ -n "$1" ]]; do
            echo "Argument courant : $1"
            shift
        done
        
        # lance ./script.sh un deux trois
        
        Argument courant : un
        Argument courant : deux
        Argument courant : trois
        ```
        
        ```bash
        #!/bin/bash
        while [[ $# -gt 0 ]]; do
            echo "Je traite : $1"
            shift          # on passe au suivant
        done
        ```
        ```
        ./script.sh Alice Bob Charlie
        → Je traite : Alice
        → Je traite : Bob
        → Je traite : Charlie
        ```
        
    - ❎ Prendre nom puis trouver emplacement fichier
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Veuillez renseigner le fichier que vous cherchez ./script <fichier>"
                exit 1
        fi
        
        echo "Le fichier "$1" est à l'emplacement suivant : "
        find / -iname "$1" 2>/dev/null
        ```
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez indiquer le nom d'un fichier"
                echo -e  "Usage :\n\t$0 <fichier>"
                exit 1
        fi
        
        emplacement=$(find / -iname "$1" 2>/dev/null)
        
        if [[ -z "$emplacement" ]]; then
                echo "Aucun fichier trouvé"
                echo "Le fichier $1 ne semble pas présent sur le système"
                exit 1
        fi 
        
        echo "L'emplacement de $1 :"
        echo "$emplacement"
        
        ```
        
    - Enregistrer nombre de ligne d’un fichier dans un nouveau fichier
        
        ```bash
        #!/bin/bash
        
        lignes_pass=$(cat /etc/passwd | wc -l)
        echo "Il y a "$lignes_pass" lignes dans le fichier passwd" | tee ex_pass.txt
        ```
        
    - Erreur argument expliquer comment utiliser script
        - Bien indiquer comment faire
            
            ```bash
            #!/bin/bash
            
            # Check for given argument
            if [ $# -eq 0 ]
            then
                echo -e "You need to specify the target domain.\n"
                echo -e "Usage:"
                echo -e "\t$0 <domain>"
                exit 1
            else
                domain=$1
            fi
            ```
            
            ```bash
            CamiiKazZ@htb[/htb]$ ./cidr.sh
            
            You need to specify the target domain.
            
            Usage:
                cidr.sh <domain>
            ```
            
    - Lancer commande générale pour fichier spécifique
        
        ```bash
        #!/bin/bash
        
        read -p "Quel fichier souhaitez vous analyser ?" fichier
        
        lignes=$(wc -l $fichier | tee nbr_lignes.txt)
        echo "Il y a $lignes dans $fichier"
        ```
        
    - Générer rapport concernant dossier et contenu
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument" >&2
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide" >&2
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        
        ```