# Cours Complet de PowerShell

## De zéro à l'automatisation et l'administration Windows — Guide pour débutant absolu

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c'est un ordinateur sous Windows (ou Linux/Mac avec PowerShell 7 installé).

---

## Guide de lecture — Comment utiliser ce cours

Ce cours couvre à la fois le scripting PowerShell et l'administration Windows. Tu n'as **pas besoin de tout maîtriser d'un coup**.

**Chaque chapitre est organisé en 3 niveaux :**

| Section | Niveau | Objectif |
|---------|--------|----------|
| **Le minimum à savoir** | 🟢 Essentiel | Ce qu'il faut comprendre pour ne pas être perdu |
| **Très utile en pratique** | 🟡 Bon à connaître | Ce qui te rend opérationnel au quotidien |
| **Bonus** | 🔴 Avancé | Ce qui fait la différence en poste — tu peux y revenir plus tard |

### Parcours recommandés

| Parcours | Chapitres | Objectif |
|----------|-----------|----------|
| **🎯 Entretien / Junior** | Ch.1-6, 8-9, 10 (fichiers), 11 (processus/services) | Comprendre PowerShell, être crédible en entretien |
| **🔧 Scripting opérationnel** | Tous les chapitres | Écrire des scripts d'automatisation solides |
| **🛡️ Profil cyber / blue team** | Tout + focus Ch.11 (logs, forensic léger) + Ch.12 (cas pratiques sécu) | Triage, investigation, hardening |

---

## Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **PowerShell** | Le shell moderne de Microsoft — à la fois un terminal, un langage de scripting et un outil d'administration |
| **Cmdlet** | Une commande PowerShell native, toujours nommée `Verbe-Nom` (ex : `Get-Process`, `Set-Location`) |
| **Pipeline** | Le mécanisme qui envoie la sortie d'une commande comme entrée d'une autre — en PowerShell, ce sont des **objets** qui circulent, pas du texte |
| **Objet** | Une structure de données avec des **propriétés** (des informations) et des **méthodes** (des actions) |
| **Propriété** | Une information attachée à un objet (ex : le nom d'un fichier, la taille, la date de modification) |
| **Variable** | Un conteneur avec un nom qui stocke une valeur — en PowerShell, le nom commence toujours par `$` |
| **Script** | Un fichier texte `.ps1` contenant des commandes PowerShell à exécuter |
| **Module** | Un ensemble de commandes PowerShell regroupées (ex : le module ActiveDirectory) |
| **Registre** | La base de données de configuration de Windows — PowerShell peut le parcourir comme un disque |
| **Service** | Un programme qui tourne en arrière-plan sous Windows (ex : le pare-feu, le spooler d'impression) |
| **Remoting** | La capacité d'exécuter des commandes PowerShell sur des machines distantes |
| **Hashtable** | Une collection de paires clé-valeur — l'équivalent des dictionnaires Python |
| **PSDrive** | Un "lecteur" PowerShell — le filesystem, le registre, les certificats, les variables d'environnement sont tous accessibles comme des disques |

---

## Comment penser un script

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

Concrètement, il n'y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier, système...)
2. **Stocker** des informations dans des variables
3. **Tester** si quelque chose est vrai ou faux (conditions)
4. **Répéter** une action plusieurs fois (boucles)
5. **Afficher ou enregistrer** un résultat (sortie)

Tous les scripts, même les plus complexes, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

---

## La grande différence avec Bash et Python

PowerShell a une particularité fondamentale : **le pipeline transporte des objets, pas du texte**.

En **Bash**, quand tu fais `ls | grep ".txt"`, la commande `ls` produit du **texte brut** (une liste de noms de fichiers) et `grep` cherche un motif dans ce texte. Si tu veux la taille d'un fichier, tu dois parser du texte avec `awk`, `cut` ou `sed`.

En **Python**, tu utilises des fonctions et des structures de données (`pathlib`, `os`) pour manipuler les fichiers. Il n'y a pas vraiment de pipeline.

En **PowerShell**, quand tu fais `Get-ChildItem -File | Where-Object { $_.Length -gt 1MB }`, la commande `Get-ChildItem` produit des **objets fichier** — chaque objet a des propriétés (`Name`, `Length`, `LastWriteTime`, `Extension`...) que tu peux lire directement, sans parser du texte. C'est un changement de paradigme qui rend PowerShell très puissant pour l'administration système.

> **Note :** le flag `-File` dans `Get-ChildItem -File` limite les résultats aux fichiers (excluant les dossiers). C'est important quand tu travailles avec des tailles (`Length`) car les dossiers n'ont pas de propriété `Length` exploitable, ce qui peut fausser les résultats.

Et l'autre grande particularité : PowerShell n'est pas seulement un langage de scripting. C'est aussi un **outil d'administration Windows natif**. Gérer les processus, les services, le registre, les logs, les tâches planifiées, les machines distantes — tout ça se fait en PowerShell, souvent en une seule ligne.

---

## Table des matières

1. [Découverte de PowerShell et premières commandes](#chapitre-1--découverte-de-powershell-et-premières-commandes)
2. [Variables, types, affichage et saisie utilisateur](#chapitre-2--variables-types-affichage-et-saisie-utilisateur)
3. [Arguments, paramètres et scripts paramétrés](#chapitre-3--arguments-paramètres-et-scripts-paramétrés)
4. [Le pipeline et les objets : le concept fondamental](#chapitre-4--le-pipeline-et-les-objets)
5. [Opérateurs, calculs et logique](#chapitre-5--opérateurs-calculs-et-logique)
6. [Conditions](#chapitre-6--conditions)
7. [Chaînes de caractères](#chapitre-7--chaînes-de-caractères)
8. [Tableaux, hashtables et boucles](#chapitre-8--tableaux-hashtables-et-boucles)
9. [Fonctions](#chapitre-9--fonctions)
10. [Fichiers, registre et administration système](#chapitre-10--fichiers-registre-et-administration-système)
11. [Processus, services, logs, remoting et triage forensic léger](#chapitre-11--processus-services-logs-et-remoting)
12. [Débogage, bonnes pratiques et cas pratiques](#chapitre-12--débogage-bonnes-pratiques-et-cas-pratiques)

---

# Chapitre 1 — Découverte de PowerShell et premières commandes

## Le minimum à savoir

### Qu'est-ce que PowerShell ?

PowerShell est trois choses à la fois :

1. **Un terminal** (un shell) — tu tapes des commandes, il les exécute
2. **Un langage de scripting** — tu écris des scripts pour automatiser des tâches
3. **Un outil d'administration Windows** — tu gères des processus, services, utilisateurs, registre, Active Directory...

C'est le couteau suisse de l'administration Windows. Tout ce que tu peux faire dans l'interface graphique de Windows, tu peux le faire en PowerShell — et souvent plus vite, et surtout de manière reproductible et automatisable.

### Windows PowerShell vs PowerShell 7

Il existe deux versions qui coexistent :

| Version | Nom | Exécutable | Inclus dans Windows ? | Cross-platform ? |
|---------|-----|-----------|----------------------|-----------------|
| 5.1 | **Windows PowerShell** | `powershell.exe` | Oui (intégré) | Non (Windows uniquement) |
| 7+ | **PowerShell** (tout court) | `pwsh.exe` | Non (à installer) | Oui (Windows, Linux, Mac) |

**Windows PowerShell 5.1** est déjà installé sur ton Windows. C'est celui que tu ouvres quand tu cherches "PowerShell" dans le menu Démarrer. Il suffit pour 95% de ce cours.

**PowerShell 7+** est la version moderne, open source, cross-platform. Il ajoute quelques fonctionnalités (opérateur ternaire, pipeline parallèle). Tu peux l'installer depuis [github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell).

> **Pour ce cours :** Windows PowerShell 5.1 suffit. Les rares cas où PowerShell 7 est nécessaire sont signalés.

### Ouvrir PowerShell

**Windows :**
- Cherche "PowerShell" dans le menu Démarrer → **Windows PowerShell**
- Pour les opérations d'administration : clic droit → **Exécuter en tant qu'administrateur**
- Windows Terminal (recommandé) : cherche "Terminal" → ouvre un onglet PowerShell

**Linux / Mac :**
```bash
# Installer PowerShell 7
# Ubuntu/Debian :
sudo apt-get install -y powershell
# Mac :
brew install powershell

# Lancer
pwsh
```

### Les premières commandes

Tape ces commandes dans ton terminal PowerShell pour te familiariser :

```powershell
Get-Date                    # Quelle date et heure ?
Get-Location                # Où suis-je ? (quel dossier)
Get-ChildItem               # Qu'est-ce qu'il y a ici ? (liste des fichiers)
Write-Output "Bonjour !"    # Afficher du texte
$env:USERNAME               # Qui suis-je ? (nom d'utilisateur)
```

### La convention Verbe-Nom

Tu remarques quelque chose ? Toutes les commandes PowerShell suivent le même pattern : **`Verbe-Nom`**.

| Verbe | Signification | Exemples |
|-------|--------------|---------|
| `Get` | Obtenir, lire | `Get-Process`, `Get-Service`, `Get-Date` |
| `Set` | Modifier, configurer | `Set-Location`, `Set-Content` |
| `New` | Créer | `New-Item`, `New-Object` |
| `Remove` | Supprimer | `Remove-Item`, `Remove-Variable` |
| `Start` | Démarrer | `Start-Process`, `Start-Service` |
| `Stop` | Arrêter | `Stop-Process`, `Stop-Service` |
| `Test` | Vérifier | `Test-Path`, `Test-Connection` |
| `Write` | Écrire, afficher | `Write-Output`, `Write-Host` |

C'est la force de PowerShell : la convention est **prédictible**. Tu ne connais pas la commande pour lister les services ? Essaie `Get-Service`. Pour les arrêter ? `Stop-Service`. Pour en démarrer un ? `Start-Service`. Ça fonctionne presque toujours.

> **Comparaison avec Bash :** en Bash, les noms de commandes sont courts et souvent cryptiques (`ls`, `ps`, `grep`, `awk`, `sed`). En PowerShell, les noms sont longs mais explicites. C'est plus verbeux, mais tu devines la commande au lieu de la mémoriser.

### Les 3 commandes pour apprendre

Ces 3 commandes sont tes meilleures alliées pour explorer PowerShell :

```powershell
# 1. Trouver une commande
Get-Command *Process*       # Quelles commandes contiennent "Process" ?
Get-Command -Verb Get       # Toutes les commandes qui commencent par "Get"

# 2. Obtenir l'aide
Get-Help Get-Process        # Comment utiliser Get-Process ?
Get-Help Get-Process -Examples    # Des exemples concrets

# 3. Découvrir les propriétés d'un objet (on verra ça en détail au Ch.4)
Get-Process | Get-Member    # Quelles propriétés a un objet "processus" ?
```

> **À retenir :** `Get-Command` pour trouver, `Get-Help` pour comprendre, `Get-Member` pour explorer. Ces 3 commandes sont la porte d'entrée de tout dans PowerShell.

### Les alias : la passerelle avec Bash et CMD

PowerShell fournit des alias pour les commandes que tu connais peut-être déjà :

| Tu tapes | PowerShell exécute | Équivalent Bash |
|----------|-------------------|-----------------|
| `ls` | `Get-ChildItem` | `ls` |
| `cd` | `Set-Location` | `cd` |
| `pwd` | `Get-Location` | `pwd` |
| `cat` | `Get-Content` | `cat` |
| `cp` | `Copy-Item` | `cp` |
| `mv` | `Move-Item` | `mv` |
| `rm` | `Remove-Item` | `rm` |
| `echo` | `Write-Output` | `echo` |
| `cls` | `Clear-Host` | `clear` |
| `mkdir` | `New-Item -ItemType Directory` | `mkdir` |

Tu peux utiliser `ls` au lieu de `Get-ChildItem` — ça fonctionne. Mais dans un script, utilise les noms complets pour la lisibilité.

> **Attention :** les alias PowerShell ne sont PAS les commandes Linux. `ls` dans PowerShell exécute `Get-ChildItem` (qui renvoie des objets), pas le `ls` de Linux (qui renvoie du texte). Les options sont différentes : `ls -la` ne fonctionne pas, il faut `Get-ChildItem -Force`.

### Ton premier script

**Étape 1 — Crée un dossier de travail :**

```powershell
New-Item -ItemType Directory -Path "$HOME\mes_scripts" -Force
Set-Location "$HOME\mes_scripts"
```

**Étape 2 — Crée le fichier et écris le script :**

Ouvre un éditeur de texte (Notepad, VS Code, ou PowerShell ISE) et crée un fichier `hello.ps1` :

```powershell
# Mon tout premier script PowerShell
Write-Output "Hello, World !"
Write-Output "Je suis un script PowerShell !"
```

Sauvegarde le fichier.

**Étape 3 — Lance-le :**

```powershell
.\hello.ps1
```

**Problème probable :** tu vois un message d'erreur rouge qui dit quelque chose comme "l'exécution de scripts est désactivée sur ce système".

### La politique d'exécution

Par défaut, Windows **interdit** l'exécution de scripts PowerShell. C'est une mesure de sécurité. Pour la modifier :

```powershell
# Voir la politique actuelle
Get-ExecutionPolicy

# Autoriser les scripts locaux (recommandé pour l'apprentissage)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

| Politique | Effet |
|-----------|-------|
| `Restricted` | Aucun script ne peut s'exécuter (défaut) |
| `RemoteSigned` | Les scripts locaux fonctionnent, les scripts téléchargés doivent être signés |
| `Unrestricted` | Tout fonctionne (déconseillé en production) |
| `Bypass` | Aucune vérification (déconseillé) |

> **Note sécurité :** `RemoteSigned` au scope `CurrentUser` est le bon compromis pour apprendre. En entreprise, la politique est souvent gérée par GPO (Group Policy).

Relance ton script :

```powershell
.\hello.ps1
```

```
Hello, World !
Je suis un script PowerShell !
```

Félicitations, tu viens d'écrire et d'exécuter ton premier script PowerShell !

### Les commentaires

```powershell
# Ceci est un commentaire sur une ligne

<#
Ceci est un commentaire
sur plusieurs lignes
(bloc de commentaire)
#>

Write-Output "Ceci s'affiche"  # Commentaire en fin de ligne
```

### Pourquoi `.\` devant le script ?

Comme en Bash avec `./`, PowerShell ne cherche pas les scripts dans le dossier courant par défaut (mesure de sécurité). Le `.\` dit "cherche dans le dossier actuel".

## Très utile en pratique

### PowerShell ISE vs VS Code

**PowerShell ISE** (Integrated Scripting Environment) est l'éditeur intégré à Windows pour PowerShell. Cherche "ISE" dans le menu Démarrer. Il a un éditeur avec coloration syntaxique et un terminal intégré. C'est pratique pour débuter.

**VS Code** avec l'extension PowerShell est le choix moderne et recommandé. Plus puissant, cross-platform, et mieux maintenu.

### La tab-completion

PowerShell complète automatiquement les commandes et les paramètres quand tu appuies sur `Tab` :

```powershell
Get-Pro[Tab]     # → Get-Process
Get-Process -N[Tab]   # → Get-Process -Name
```

C'est extrêmement pratique et ça te fait gagner du temps.

### Exécuter une commande rapide sans script

Tu n'as pas toujours besoin d'un script. PowerShell est un **shell** — tu tapes des commandes directement :

```powershell
# Combien de processus tournent ?
(Get-Process).Count

# Quel est l'espace disque disponible ?
Get-PSDrive C

# Depuis combien de temps la machine tourne ?
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
```

## Bonus

### PowerShell Gallery

Le [PowerShell Gallery](https://www.powershellgallery.com/) est le dépôt public de modules PowerShell (comme PyPI pour Python ou npm pour JavaScript). Tu peux installer des modules avec :

```powershell
Install-Module -Name PSReadLine -Scope CurrentUser
```

### Le profil PowerShell

Le profil est un script qui s'exécute automatiquement à chaque ouverture de PowerShell (l'équivalent du `.bashrc` en Bash) :

```powershell
# Voir le chemin du profil
$PROFILE

# Créer/éditer le profil
notepad $PROFILE
```

## ❌ Erreur classique

```powershell
# La politique d'exécution bloque le script
.\mon_script.ps1    # ❌ "l'exécution de scripts est désactivée"
# → Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Oublier le .\ devant le script
mon_script.ps1      # ❌ "terme non reconnu"
.\mon_script.ps1    # ✅ Correct

# Utiliser les options Linux avec les alias
ls -la              # ❌ Les options Linux ne fonctionnent pas
Get-ChildItem -Force   # ✅ L'équivalent PowerShell

# Confondre PowerShell et CMD (Invite de commandes)
# PowerShell ≠ CMD. Ce sont deux shells différents.
# Les commandes CMD (dir, type, copy) fonctionnent parfois en PowerShell,
# mais les commandes PowerShell ne fonctionnent PAS dans CMD.
```

## Exercices

**Guidé :** Crée un script `salut.ps1` qui affiche "Bonjour !" puis "Bienvenue dans le monde de PowerShell."

**Autonome :** Crée un script `info.ps1` qui affiche le nom de l'utilisateur (`$env:USERNAME`), la date (`Get-Date`), et le dossier actuel (`Get-Location`) sur des lignes séparées.

## ✅ Tu sais maintenant...

- Ce qu'est PowerShell (shell + langage + outil d'administration)
- La convention Verbe-Nom (`Get-Process`, `Set-Location`...)
- Les 3 commandes pour apprendre (`Get-Command`, `Get-Help`, `Get-Member`)
- Créer et exécuter un script `.ps1`
- Modifier la politique d'exécution
- Les alias (`ls`, `cd`, `cat`...) et pourquoi ils ne sont pas identiques aux commandes Linux

## 💬 Questions d'entretien typiques

- **Qu'est-ce que PowerShell ?** → C'est à la fois un shell (terminal de commandes), un langage de scripting, et un outil d'administration Windows natif. Il manipule des objets dans le pipeline, pas du texte brut.
- **Quelle est la convention de nommage des commandes PowerShell ?** → Toutes les commandes (cmdlets) suivent le pattern Verbe-Nom : `Get-Process`, `Stop-Service`, `Set-Content`. C'est prédictible et découvrable.
- **Comment trouver une commande qu'on ne connaît pas ?** → `Get-Command *motclé*` pour chercher, `Get-Help commande` pour comprendre, `Get-Member` pour explorer les propriétés d'un objet.

---

# Chapitre 2 — Variables, types, affichage et saisie utilisateur

## Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable, c'est un **conteneur avec une étiquette**. En PowerShell, le nom commence toujours par `$` :

```powershell
$prenom = "Alice"
$age = 25
$taille = 1.75
$est_admin = $true
```

> **Comparaison :** en Bash, les variables n'ont pas de `$` à la création (`prenom="Alice"`) mais en ont un à l'utilisation (`echo $prenom`). En Python, jamais de `$`. En PowerShell, **toujours** un `$`, à la création ET à l'utilisation.

### Les types de données

PowerShell gère les types automatiquement, mais il est plus riche que Bash :

| Type | Notation | Exemple | Ce que c'est |
|------|----------|---------|-------------|
| Texte | `[string]` | `"Alice"` | Une chaîne de caractères |
| Nombre entier | `[int]` | `25` | Un nombre sans virgule |
| Nombre décimal | `[double]` | `1.75` | Un nombre avec virgule |
| Booléen | `[bool]` | `$true`, `$false` | Vrai ou Faux |
| Date | `[datetime]` | `Get-Date` | Une date avec heure |

```powershell
$prenom = "Alice"
$age = 25
$taille = 1.75
$est_admin = $true
$maintenant = Get-Date

# Vérifier le type
$prenom.GetType().Name    # String
$age.GetType().Name       # Int32
```

Tu peux forcer un type :

```powershell
[int]$nombre = "42"       # Convertit le texte "42" en nombre 42
[string]$texte = 123      # Convertit le nombre 123 en texte "123"
```

### Afficher : `Write-Output` vs `Write-Host`

C'est une distinction importante en PowerShell :

```powershell
Write-Output "Bonjour"    # Envoie dans le pipeline (peut être capturé, redirigé)
Write-Host "Bonjour"      # Affiche directement à l'écran (ne va PAS dans le pipeline)
```

**Quelle différence ?**

```powershell
# Write-Output → peut être capturé
$resultat = Write-Output "Hello"
$resultat    # → "Hello"

# Write-Host → ne peut PAS être capturé
$resultat = Write-Host "Hello"    # "Hello" s'affiche, mais...
$resultat    # → (vide — rien n'a été capturé)
```

> **Règle simple :** utilise `Write-Output` dans tes scripts (ou ne mets rien — PowerShell envoie automatiquement dans le pipeline). Utilise `Write-Host` uniquement pour les messages de présentation destinés à l'utilisateur (couleurs, messages d'état).

### L'interpolation de chaînes

Comme en Bash, les **guillemets doubles** interprètent les variables, les **guillemets simples** non :

```powershell
$prenom = "Alice"

Write-Output "Bonjour, $prenom !"    # → Bonjour, Alice !
Write-Output 'Bonjour, $prenom !'    # → Bonjour, $prenom !
```

Pour des expressions plus complexes, utilise `$()` (la sous-expression) :

```powershell
Write-Output "Il y a $((Get-ChildItem).Count) fichiers ici."
Write-Output "2 + 3 = $(2 + 3)"
```

> **Comparaison :** c'est la même logique que `$(commande)` en Bash et les f-strings `f"{expression}"` en Python.

### Saisie utilisateur avec `Read-Host`

```powershell
$prenom = Read-Host "Ton prénom"
$age = Read-Host "Ton âge"
Write-Output "Tu es $prenom et tu as $age ans."
```

```
Ton prénom: Alice
Ton âge: 25
Tu es Alice et tu as 25 ans.
```

### Le piège de `Read-Host`

Comme `input()` en Python, `Read-Host` renvoie **toujours du texte** :

```powershell
$age = Read-Host "Ton âge"
$annee_prochaine = $age + 1    # ⚠️ "251" au lieu de 26 !
# PowerShell concatène le texte "25" avec le nombre 1 → "251"

# Correct :
[int]$age = Read-Host "Ton âge"
$annee_prochaine = $age + 1    # → 26
```

> **Bonne pratique :** force le type avec `[int]` quand tu attends un nombre.

### Les variables automatiques

PowerShell a des variables pré-définies utiles :

```powershell
$true                  # Vrai (booléen)
$false                 # Faux (booléen)
$null                  # Absence de valeur
$HOME                  # Dossier personnel de l'utilisateur
$PWD                   # Dossier courant
$PSVersionTable        # Version de PowerShell
$env:USERNAME          # Nom de l'utilisateur (variable d'environnement)
$env:COMPUTERNAME      # Nom de la machine
$env:USERPROFILE       # Chemin du profil utilisateur
$LASTEXITCODE          # Code de sortie de la dernière commande externe
```

> **Note :** les variables d'environnement sont accessibles via `$env:NOM`. C'est l'équivalent de `$USER`, `$HOME` en Bash et `os.getenv()` en Python.

## Très utile en pratique

### Write-Host avec des couleurs

```powershell
Write-Host "Succès !" -ForegroundColor Green
Write-Host "Attention !" -ForegroundColor Yellow
Write-Host "Erreur !" -ForegroundColor Red -BackgroundColor White
```

C'est l'un des avantages de `Write-Host` — le contrôle de la couleur. Utile pour les menus et les messages de statut.

### Les constantes

Pour qu'une variable ne puisse pas être modifiée :

```powershell
Set-Variable -Name "PI" -Value 3.14159 -Option ReadOnly
$PI = 3.0    # ❌ Erreur !
```

### Créer et supprimer des variables

```powershell
# Créer
$message = "Hello"

# Supprimer
Remove-Variable -Name "message"
# ou
Clear-Variable -Name "message"    # Met à $null sans supprimer
```

## Bonus

### Les types .NET

PowerShell est construit sur .NET, ce qui signifie que chaque objet PowerShell est un objet .NET. Tu peux utiliser les méthodes .NET sur les types :

```powershell
[math]::PI                    # 3.14159265358979
[math]::Round(3.14159, 2)     # 3.14
[math]::Max(10, 25)           # 25
[System.Environment]::MachineName    # Nom de la machine
```

Tu n'as pas besoin de ça pour commencer, mais c'est ce qui rend PowerShell très puissant pour les usages avancés.

## ❌ Erreur classique

```powershell
# Oublier le $ devant le nom de variable
prenom = "Alice"       # ❌ Erreur
$prenom = "Alice"      # ✅ Correct

# Confondre guillemets doubles et simples
$nom = "Alice"
Write-Output 'Bonjour $nom'    # → Bonjour $nom (PAS interprété)
Write-Output "Bonjour $nom"    # → Bonjour Alice

# Oublier de convertir la saisie utilisateur
$age = Read-Host "Âge"
$resultat = $age + 1           # ❌ "251" (concaténation texte)
[int]$age = Read-Host "Âge"
$resultat = $age + 1           # ✅ 26
```

## Exercices

**Guidé :** Crée un script `presentation.ps1` qui demande le prénom et l'âge avec `Read-Host`, convertit l'âge en entier, et affiche "Tu es [prénom] et tu as [âge] ans. L'année prochaine tu auras [âge+1] ans."

**Autonome :** Crée un script `machine.ps1` qui affiche le nom de l'utilisateur, le nom de la machine, la version de PowerShell (`$PSVersionTable.PSVersion`), et la date.

## 🧩 Mini-projet (chapitres 1-2)

Crée un script `bienvenue.ps1` qui :
1. Affiche "Bienvenue sur cette machine !" en vert
2. Affiche la date du jour
3. Demande le prénom de l'utilisateur
4. Affiche "Bonjour [prénom], connecté en tant que [USERNAME] sur [COMPUTERNAME]"

## ✅ Tu sais maintenant...

- Créer une variable avec `$` et l'afficher
- Les types de base : `[string]`, `[int]`, `[double]`, `[bool]`
- La différence entre `Write-Output` (pipeline) et `Write-Host` (écran)
- L'interpolation de chaînes (guillemets doubles vs simples)
- Lire une saisie utilisateur avec `Read-Host`
- Les variables automatiques (`$true`, `$false`, `$null`, `$HOME`, `$env:USERNAME`)

---

# Chapitre 3 — Arguments, paramètres et scripts paramétrés

## Le minimum à savoir

### C'est quoi un argument ?

Au lieu de poser des questions avec `Read-Host`, tu peux donner des infos directement quand tu lances le script :

```powershell
.\saluer.ps1 Alice
#                 ↑ c'est un argument
```

### La méthode simple : `$args`

`$args` est un tableau qui contient tous les arguments passés au script :

```powershell
# saluer.ps1
Write-Output "Bonjour, $($args[0]) !"
```

```powershell
.\saluer.ps1 Alice       # → Bonjour, Alice !
.\saluer.ps1 Bob         # → Bonjour, Bob !
```

> **Comparaison :** `$args[0]` en PowerShell = `$1` en Bash = `sys.argv[1]` en Python. Attention : en PowerShell, `$args[0]` est le premier argument (pas le nom du script). Le nom du script est dans `$MyInvocation.MyCommand.Name`.

### La méthode recommandée : `param()`

`param()` est la manière propre de déclarer des paramètres en PowerShell. C'est beaucoup plus puissant que `$args` :

```powershell
# saluer.ps1
param(
    [string]$Prenom,
    [int]$Age = 0
)

Write-Output "Bonjour, $Prenom !"
if ($Age -gt 0) {
    Write-Output "Tu as $Age ans."
}
```

```powershell
.\saluer.ps1 -Prenom Alice -Age 25
# → Bonjour, Alice !
# → Tu as 25 ans.

.\saluer.ps1 -Prenom Bob
# → Bonjour, Bob !
# (pas de message sur l'âge — valeur par défaut = 0)
```

**Pourquoi `param()` est mieux que `$args` :**
- Les paramètres ont des **noms** (`-Prenom`, `-Age`) — pas besoin de retenir l'ordre
- Tu peux spécifier le **type** (`[string]`, `[int]`) — les erreurs sont détectées automatiquement
- Tu peux définir des **valeurs par défaut** (`$Age = 0`)
- Tu peux rendre un paramètre **obligatoire**
- La **tab-completion** fonctionne sur les noms de paramètres

> **C'est un avantage majeur de PowerShell sur Bash et Python.** En Bash, tu gères les arguments avec `$1`, `$2` et des `shift` manuels. En Python, tu utilises `sys.argv` ou `argparse`. En PowerShell, `param()` fait tout ça nativement.

### Paramètres obligatoires

```powershell
param(
    [Parameter(Mandatory)]
    [string]$Nom,
    
    [string]$Ville = "Paris"
)

Write-Output "$Nom habite à $Ville."
```

Si tu oublies `-Nom`, PowerShell te le demande automatiquement :

```
cmdlet script.ps1 at command pipeline position 1
Supply values for the following parameters:
Nom: Alice
Alice habite à Paris.
```

### Vérifier les arguments (avec `$args`)

Si tu utilises `$args` au lieu de `param()` :

```powershell
if ($args.Count -lt 1) {
    Write-Output "Erreur : donne un prénom en argument."
    Write-Output "Utilisation : .\saluer.ps1 <prénom>"
    exit 1
}

Write-Output "Bonjour, $($args[0]) !"
```

> **Note :** `exit 1` termine le script avec un code d'erreur, comme en Bash et Python.

### La différence `Read-Host` vs `param()`

| `Read-Host` | `param()` |
|-------------|-----------|
| L'utilisateur tape pendant l'exécution | L'info est fournie au lancement |
| Script interactif | Script automatisable |
| Pas utilisable dans un pipeline | Intégrable dans un pipeline |

> **Bonne pratique :** utilise `param()` pour les paramètres principaux (automatisable, scriptable), et `Read-Host` uniquement pour les confirmations interactives ("Êtes-vous sûr ?").

## Très utile en pratique

### Les paramètres switch (booléens)

```powershell
param(
    [string]$Chemin,
    [switch]$Verbose,
    [switch]$Force
)

if ($Verbose) {
    Write-Output "Mode verbeux activé"
}
```

```powershell
.\script.ps1 -Chemin "C:\temp" -Verbose    # $Verbose = $true
.\script.ps1 -Chemin "C:\temp"             # $Verbose = $false
```

Un paramètre `[switch]` est activé par sa présence (pas besoin de valeur).

### La validation de paramètres

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Nom,
    
    [ValidateRange(1, 120)]
    [int]$Age,
    
    [ValidateSet("fr", "en", "es")]
    [string]$Langue = "fr"
)
```

PowerShell vérifie automatiquement les contraintes. Si tu passes `-Age 200`, tu obtiens une erreur avant même que le script ne commence.

## Bonus

### Le splatting : passer un hashtable comme paramètres

```powershell
$params = @{
    Path      = "C:\temp"
    Filter    = "*.log"
    Recurse   = $true
}

Get-ChildItem @params    # Équivalent de : Get-ChildItem -Path "C:\temp" -Filter "*.log" -Recurse
```

C'est utile quand tu as beaucoup de paramètres — le code est plus lisible.

## ❌ Erreur classique

```powershell
# Mettre param() APRÈS du code
Write-Output "Hello"
param([string]$Nom)    # ❌ param() doit être la PREMIÈRE instruction du script

param([string]$Nom)    # ✅ Toujours en premier
Write-Output "Hello"

# Oublier la virgule entre les paramètres dans param()
param(
    [string]$Nom
    [int]$Age          # ❌ Il manque la virgule après $Nom
)

param(
    [string]$Nom,      # ✅ Virgule
    [int]$Age
)

# Confondre $args et param() — ne mélange pas les deux
```

## Exercices

**Guidé :** Crée un script `bonjour.ps1` avec `param()` qui prend un prénom (obligatoire) et une langue (optionnel, défaut "fr"), et affiche un message d'accueil dans la bonne langue.

**Autonome :** Crée un script `calculer.ps1` avec `param()` qui prend deux nombres et affiche leur somme, différence et produit.

## ✅ Tu sais maintenant...

- Passer des arguments avec `$args` (méthode simple)
- Déclarer des paramètres avec `param()` (méthode recommandée)
- Les paramètres obligatoires (`[Parameter(Mandatory)]`)
- Les valeurs par défaut, les types, la validation
- Les paramètres switch (`[switch]`)
- La différence entre `Read-Host` et `param()`

---

# Chapitre 4 — Le pipeline et les objets : le concept fondamental

## Le minimum à savoir

### Pourquoi ce chapitre est LE plus important

Si tu ne retiens qu'une seule chose de ce cours, retiens ça : **en PowerShell, le pipeline transporte des objets, pas du texte**. C'est ce qui rend PowerShell fondamentalement différent de Bash et c'est ce qui le rend puissant pour l'administration.

### Le pipeline en Bash vs PowerShell

**En Bash :** `ps aux | grep firefox | awk '{print $2}'`
- `ps aux` produit du **texte** (des lignes de caractères)
- `grep` filtre des **lignes de texte** qui contiennent "firefox"
- `awk` extrait la **2ème colonne de texte** (le PID)
- Si le format de sortie de `ps` change, tout le pipeline casse

**En PowerShell :** `Get-Process firefox | Select-Object Id`
- `Get-Process` produit des **objets** processus
- Chaque objet a des propriétés (`Name`, `Id`, `CPU`, `WorkingSet`...)
- `Select-Object` sélectionne la **propriété** `Id` directement
- Pas de parsing de texte, pas de risque de casse

### Voir les objets en action

```powershell
# Obtenir un processus
$proc = Get-Process -Name explorer
$proc

# Voir ses propriétés
$proc.Name               # explorer
$proc.Id                 # 1234
$proc.CPU                # 15.23 (secondes CPU)
$proc.WorkingSet64       # 85000192 (mémoire en octets)
$proc.StartTime          # 07/04/2025 08:30:00
```

L'objet `$proc` n'est pas du texte — c'est une structure de données riche avec des dizaines de propriétés et de méthodes. Tu y accèdes avec un point `.`.

### `Get-Member` : explorer les propriétés d'un objet

C'est ta commande de découverte. Elle te dit **ce que contient un objet** :

```powershell
Get-Process | Get-Member
```

La sortie montre toutes les propriétés (informations) et méthodes (actions) disponibles sur les objets processus. C'est comme ça que tu apprends ce que tu peux faire avec un objet.

### Les 5 cmdlets du pipeline

| Cmdlet | Rôle | Analogie |
|--------|------|---------|
| `Where-Object` | **Filtrer** les objets selon une condition | Le `grep` de PowerShell |
| `Select-Object` | **Choisir** les propriétés à afficher | Le `cut`/`awk` de PowerShell |
| `Sort-Object` | **Trier** les objets par une propriété | Le `sort` de PowerShell |
| `Measure-Object` | **Compter**, additionner, moyenner | Le `wc` de PowerShell |
| `ForEach-Object` | **Appliquer** une action à chaque objet | La boucle `for` dans le pipeline |

### Filtrer avec `Where-Object`

```powershell
# Processus qui utilisent plus de 100 Mo de mémoire
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB }

# Fichiers .txt dans le dossier courant
Get-ChildItem | Where-Object { $_.Extension -eq ".txt" }

# Services en cours d'exécution
Get-Service | Where-Object { $_.Status -eq "Running" }
```

> **Note :** `$_` représente l'objet courant dans le pipeline. C'est l'équivalent du "chaque élément" dans une boucle. Tu verras `$_` partout en PowerShell.

> **Raccourci (PowerShell 3+) :** `Get-Process | Where-Object CPU -gt 10` (syntaxe simplifiée sans les accolades pour les cas simples).

### Sélectionner avec `Select-Object`

```powershell
# Afficher seulement le nom et l'ID des processus
Get-Process | Select-Object Name, Id

# Les 5 premiers
Get-Process | Select-Object -First 5

# Les 3 derniers
Get-Process | Select-Object -Last 3
```

### Trier avec `Sort-Object`

```powershell
# Trier les processus par mémoire (du plus gourmand au moins gourmand)
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 10

# Trier les fichiers par taille
Get-ChildItem -File | Sort-Object Length -Descending
```

### Compter avec `Measure-Object`

```powershell
# Combien de processus tournent ?
Get-Process | Measure-Object

# Taille totale des fichiers
Get-ChildItem -File | Measure-Object -Property Length -Sum -Average -Maximum
```

### Appliquer une action avec `ForEach-Object`

```powershell
# Afficher un message pour chaque service arrêté
Get-Service | Where-Object { $_.Status -eq "Stopped" } | ForEach-Object {
    Write-Output "Le service $($_.Name) est arrêté."
}
```

### Un pipeline complet

Voici un pipeline réaliste — les 10 processus qui consomment le plus de mémoire :

```powershell
Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{Name="RAM (Mo)"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}} |
    Select-Object -First 10
```

Ce pipeline fait en une commande ce qui nécessiterait 4-5 commandes Bash avec du parsing de texte.

## Très utile en pratique

### L'opérateur de pipeline `|` enchaîné

Tu peux écrire un pipeline sur plusieurs lignes pour la lisibilité :

```powershell
Get-ChildItem -Path "C:\" -Recurse -File |
    Where-Object { $_.Length -gt 100MB } |
    Sort-Object Length -Descending |
    Select-Object FullName, @{Name="Taille (Mo)"; Expression={[math]::Round($_.Length / 1MB)}} |
    Format-Table -AutoSize
```

### Les propriétés calculées

La syntaxe `@{Name="..."; Expression={...}}` crée une propriété calculée à la volée :

```powershell
Get-Process | Select-Object Name, @{Name="RAM (Mo)"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}}
```

### Exporter les résultats

```powershell
# En CSV
Get-Process | Select-Object Name, Id, CPU | Export-Csv -Path "processus.csv" -NoTypeInformation

# En JSON
Get-Process | Select-Object Name, Id, CPU | ConvertTo-Json | Set-Content "processus.json"

# En tableau HTML
Get-Process | Select-Object Name, Id, CPU | ConvertTo-Html | Set-Content "processus.html"

# En GridView (fenêtre graphique interactive — Windows uniquement)
Get-Process | Out-GridView
```

## ❌ Erreur classique

```powershell
# Oublier $_ dans Where-Object
Get-Process | Where-Object { Name -eq "explorer" }      # ❌ Name n'est pas reconnu
Get-Process | Where-Object { $_.Name -eq "explorer" }   # ✅ $_ = l'objet courant

# Confondre Write-Output et Write-Host dans le pipeline
Get-Process | ForEach-Object { Write-Host $_.Name }     # ⚠️ Affiche mais ne passe PAS dans le pipeline
Get-Process | ForEach-Object { Write-Output $_.Name }   # ✅ Continue dans le pipeline
```

## Exercices

**Guidé :** Liste les 5 fichiers les plus gros de ton dossier personnel avec un pipeline (`Get-ChildItem | Sort-Object | Select-Object`).

**Autonome :** Liste tous les services Windows en cours d'exécution, triés par nom, et exporte le résultat en CSV.

## 🧩 Mini-projet (chapitres 3-4)

Crée un script `top_process.ps1` qui :
1. Prend un paramètre `-Nombre` (défaut 10) pour le nombre de résultats
2. Affiche les N processus les plus gourmands en mémoire
3. Affiche le nom, le PID, et la RAM en Mo (propriété calculée)
4. Affiche aussi le total de RAM utilisée par ces processus

## ✅ Tu sais maintenant...

- Le pipeline transporte des **objets**, pas du texte
- `$_` représente l'objet courant dans le pipeline
- `Where-Object` pour filtrer, `Select-Object` pour choisir, `Sort-Object` pour trier
- `Measure-Object` pour compter et calculer
- `ForEach-Object` pour appliquer une action à chaque objet
- `Get-Member` pour explorer les propriétés d'un objet
- Exporter en CSV, JSON, HTML

## 💬 Questions d'entretien typiques

- **Quelle est la différence entre le pipeline Bash et le pipeline PowerShell ?** → En Bash, le pipeline transporte du texte brut qu'il faut parser avec `grep`, `awk`, `cut`. En PowerShell, le pipeline transporte des objets structurés avec des propriétés qu'on manipule directement (`Where-Object`, `Select-Object`, `Sort-Object`).
- **Que signifie `$_` dans PowerShell ?** → C'est l'objet courant dans le pipeline. Dans `Get-Process | Where-Object { $_.CPU -gt 10 }`, `$_` représente chaque processus tour à tour.
- **Comment découvrir les propriétés d'un objet ?** → En le passant dans `Get-Member` : `Get-Process | Get-Member` montre toutes les propriétés et méthodes disponibles.

---

# Chapitre 5 — Opérateurs, calculs et logique

## Le minimum à savoir

### Le calcul en PowerShell

PowerShell gère les calculs comme Python — directement, avec les nombres décimaux :

```powershell
$a = 10
$b = 3

Write-Output "Addition      : $($a + $b)"       # 13
Write-Output "Soustraction  : $($a - $b)"       # 7
Write-Output "Multiplication: $($a * $b)"       # 30
Write-Output "Division      : $($a / $b)"       # 3.33333... (décimale)
Write-Output "Modulo        : $($a % $b)"       # 1
```

> **Note :** pas besoin de `$(( ))` comme en Bash ni d'opérateur spécial comme `//` en Python. La division est décimale par défaut. Pour la division entière : `[math]::Floor($a / $b)`.

### Les opérateurs de comparaison

PowerShell utilise des opérateurs avec tiret, comme Bash :

| Opérateur | Signification | Exemple |
|-----------|--------------|---------|
| `-eq` | Égal | `5 -eq 5` → `True` |
| `-ne` | Différent | `5 -ne 3` → `True` |
| `-lt` | Inférieur | `3 -lt 5` → `True` |
| `-gt` | Supérieur | `5 -gt 3` → `True` |
| `-le` | Inférieur ou égal | `5 -le 5` → `True` |
| `-ge` | Supérieur ou égal | `5 -ge 6` → `False` |

> **Comparaison :** PowerShell utilise `-eq`, `-lt`, `-gt` comme Bash. Python utilise `==`, `<`, `>`. C'est la convention PowerShell — les symboles `<` et `>` sont réservés pour les redirections.

### Les opérateurs de chaînes

| Opérateur | Signification | Exemple |
|-----------|--------------|---------|
| `-like` | Correspond au pattern (wildcards) | `"fichier.txt" -like "*.txt"` → `True` |
| `-notlike` | Ne correspond pas | `"fichier.txt" -notlike "*.log"` → `True` |
| `-match` | Correspond à la regex | `"abc123" -match "\d+"` → `True` |
| `-replace` | Remplacer | `"Hello World" -replace "World", "PowerShell"` |
| `-contains` | La collection contient | `@(1,2,3) -contains 2` → `True` |
| `-in` | L'élément est dans la collection | `2 -in @(1,2,3)` → `True` |

> **Particularité importante :** les comparaisons de chaînes sont **insensibles à la casse** par défaut. `"Alice" -eq "alice"` renvoie `True`. Pour un test sensible à la casse, préfixe avec `c` : `-ceq`, `-clike`, `-cmatch`.

### Les opérateurs logiques

```powershell
$age = 25

$age -ge 18 -and $age -le 65    # True — entre 18 et 65
$age -lt 10 -or $age -gt 60     # False — ni < 10 ni > 60
-not ($age -lt 18)               # True — 25 n'est PAS < 18
```

> **Comparaison :** `-and`, `-or`, `-not` en PowerShell. `&&`, `||`, `!` en Bash. `and`, `or`, `not` en Python.

### Les raccourcis d'affectation

```powershell
$compteur = 0
$compteur += 1       # 1
$compteur += 5       # 6
$compteur -= 2       # 4
$compteur *= 3       # 12
$compteur++          # 13
$compteur--          # 12
```

### Les tailles de fichiers

PowerShell comprend les suffixes de taille :

```powershell
1KB    # 1024
1MB    # 1048576
1GB    # 1073741824

# Très pratique pour les comparaisons
Get-ChildItem -File | Where-Object { $_.Length -gt 10MB }
```

## Très utile en pratique

### L'opérateur de plage `..`

```powershell
1..10           # Génère 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
"A".."Z"        # Génère les lettres de A à Z (PowerShell 7+)
```

C'est l'équivalent de `{1..10}` en Bash et `range(1, 11)` en Python.

### Test de fichiers avec `Test-Path`

```powershell
Test-Path "C:\Windows"           # True (le dossier existe)
Test-Path "C:\inexistant.txt"    # False
Test-Path "C:\Windows" -PathType Container    # True (c'est un dossier)
Test-Path "C:\Windows\notepad.exe" -PathType Leaf    # True (c'est un fichier)
```

> **Comparaison :** `Test-Path` = `[[ -e ... ]]` en Bash = `os.path.exists()` en Python.

## ❌ Erreur classique

```powershell
# Utiliser == au lieu de -eq
if ($age == 18) { }     # ❌ == n'existe pas en PowerShell
if ($age -eq 18) { }    # ✅ Correct

# Oublier que les comparaisons de chaînes sont insensibles à la casse
"Alice" -eq "alice"     # True ! (par défaut)
"Alice" -ceq "alice"    # False (comparaison sensible à la casse)

# Utiliser > pour comparer (c'est une redirection !)
if ($a > $b) { }        # ❌ Crée un fichier au lieu de comparer
if ($a -gt $b) { }      # ✅ Correct
```

## ✅ Tu sais maintenant...

- Les opérateurs arithmétiques (`+`, `-`, `*`, `/`, `%`)
- Les opérateurs de comparaison (`-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`)
- Les opérateurs de chaînes (`-like`, `-match`, `-replace`, `-contains`, `-in`)
- Les opérateurs logiques (`-and`, `-or`, `-not`)
- Les suffixes de taille (`KB`, `MB`, `GB`)
- `Test-Path` pour vérifier l'existence de fichiers/dossiers

---

# Chapitre 6 — Conditions

## Le minimum à savoir

### La structure `if`

```powershell
$age = 20

if ($age -ge 18) {
    Write-Output "Tu es majeur."
}
```

> **Syntaxe :** la condition est entre **parenthèses** `()`, le code est entre **accolades** `{}`. Pas de `then`, pas de `fi` (comme en Bash). Pas d'indentation structurelle (comme en Python). Les accolades délimitent le bloc.

### `if...else`

```powershell
$age = 15

if ($age -ge 18) {
    Write-Output "Tu es majeur."
} else {
    Write-Output "Tu es mineur."
}
```

### `if...elseif...else`

```powershell
$age = 25

if ($age -lt 13) {
    Write-Output "Tu es un enfant."
} elseif ($age -lt 18) {
    Write-Output "Tu es un adolescent."
} elseif ($age -lt 65) {
    Write-Output "Tu es un adulte."
} else {
    Write-Output "Tu es un senior."
}
```

> **Note :** c'est `elseif` en un seul mot (pas `elsif` comme en Perl, pas `elif` comme en Bash/Python).

### Combiner des conditions

```powershell
if ($age -ge 18 -and $nom -eq "Alice") {
    Write-Output "Alice est majeure."
}

if ($age -lt 10 -or $age -gt 80) {
    Write-Output "Âge extrême."
}
```

### Le `switch` : choix multiples

```powershell
$jour = (Get-Date).DayOfWeek

switch ($jour) {
    "Monday"    { Write-Output "Lundi — courage !" }
    "Friday"    { Write-Output "Vendredi — bientôt le weekend !" }
    "Saturday"  { Write-Output "Samedi — repos !" }
    "Sunday"    { Write-Output "Dimanche — repos !" }
    default     { Write-Output "Milieu de semaine." }
}
```

Le `switch` PowerShell est plus puissant que le `case` Bash :

```powershell
# Switch avec wildcards
switch -Wildcard ($fichier) {
    "*.txt"  { Write-Output "Fichier texte" }
    "*.log"  { Write-Output "Fichier log" }
    "*.csv"  { Write-Output "Fichier CSV" }
    default  { Write-Output "Type inconnu" }
}

# Switch avec regex
switch -Regex ($email) {
    "^[a-z]+@gmail"    { Write-Output "Adresse Gmail" }
    "^[a-z]+@outlook"  { Write-Output "Adresse Outlook" }
    default            { Write-Output "Autre fournisseur" }
}
```

## Très utile en pratique

### L'opérateur ternaire `[⚡ PowerShell 7+]`

```powershell
$statut = $age -ge 18 ? "Majeur" : "Mineur"
```

> **Attention :** cet opérateur nécessite **PowerShell 7+**. En Windows PowerShell 5.1, utilise un `if/else` classique.

### Conditions dans le pipeline

`Where-Object` est essentiellement un `if` appliqué à chaque objet du pipeline :

```powershell
# Tous les services arrêtés
Get-Service | Where-Object { $_.Status -eq "Stopped" }

# Tous les fichiers modifiés aujourd'hui
Get-ChildItem | Where-Object { $_.LastWriteTime.Date -eq (Get-Date).Date }
```

## ❌ Erreur classique

```powershell
# Oublier les parenthèses autour de la condition
if $age -ge 18 { }     # ❌ Parenthèses obligatoires
if ($age -ge 18) { }   # ✅ Correct

# Oublier les accolades
if ($age -ge 18)
    Write-Output "Majeur"   # ❌ Accolades obligatoires

if ($age -ge 18) {
    Write-Output "Majeur"   # ✅ Correct
}

# Confondre = (affectation) et -eq (comparaison)
if ($age = 18) { }     # ❌ C'est une AFFECTATION, pas un test !
if ($age -eq 18) { }   # ✅ Correct
```

## Exercices

**Guidé :** Crée un script `meteo.ps1` avec `param()` qui prend une température et affiche "Il gèle" (< 0), "Froid" (0-15), "Bon" (15-25), ou "Chaud" (> 25).

**Autonome :** Crée un script `verifier.ps1` qui prend un chemin en paramètre et dit si c'est un fichier, un dossier, ou si ça n'existe pas. Utilise `Test-Path`.

## 🧩 Mini-projet (chapitres 5-6)

Crée un script `etat_service.ps1` qui :
1. Prend un nom de service en paramètre (obligatoire)
2. Vérifie si le service existe (`Get-Service -Name $Nom -ErrorAction SilentlyContinue`)
3. Affiche son état (Running, Stopped, etc.)
4. Si le service est arrêté, demande si l'utilisateur veut le démarrer (Read-Host pour confirmer)

## ✅ Tu sais maintenant...

- Écrire des conditions avec `if / elseif / else`
- La syntaxe : parenthèses pour la condition, accolades pour le bloc
- Le `switch` pour les choix multiples (avec wildcards et regex)
- Les conditions dans le pipeline (`Where-Object`)

---

# Chapitre 7 — Chaînes de caractères

## Le minimum à savoir

### Guillemets doubles vs simples

Même logique qu'en Bash :

```powershell
$prenom = "Alice"

"Bonjour, $prenom !"    # → Bonjour, Alice ! (interprète la variable)
'Bonjour, $prenom !'    # → Bonjour, $prenom ! (littéral)
```

### Les here-strings (multi-lignes)

```powershell
# Here-string avec interpolation
$nom = "Alice"
$message = @"
Bonjour $nom,
Ceci est un message
sur plusieurs lignes.
"@

# Here-string littéral (pas d'interpolation)
$code = @'
$ceci = "n'est pas interprété"
Write-Output $ceci
'@
```

> **Attention :** le `"@` de fermeture doit être **tout seul en début de ligne**, sans espace avant.

### Longueur et accès par index

```powershell
$mot = "PowerShell"
$mot.Length              # 10
$mot[0]                  # P (premier caractère)
$mot[-1]                 # l (dernier caractère)
$mot[0..4] -join ""      # Power (5 premiers caractères)
```

### Les méthodes essentielles

Chaque chaîne est un objet .NET avec des méthodes :

```powershell
$texte = "  Bonjour le monde  "

$texte.ToUpper()              # "  BONJOUR LE MONDE  "
$texte.ToLower()              # "  bonjour le monde  "
$texte.Trim()                 # "Bonjour le monde"
$texte.Replace("monde", "PowerShell")    # "  Bonjour le PowerShell  "
$texte.Split(" ")             # Tableau de mots
$texte.Contains("monde")     # True
$texte.StartsWith("  Bon")   # True
$texte.EndsWith("  ")        # True
$texte.IndexOf("monde")      # 14 (position)
$texte.Substring(2, 7)       # "Bonjour" (position 2, longueur 7)
```

### Les opérateurs de chaînes

```powershell
# Remplacer (avec regex !)
"Hello World" -replace "World", "PowerShell"    # Hello PowerShell

# Découper
"pomme,banane,cerise" -split ","    # Tableau : pomme, banane, cerise

# Joindre
@("Bonjour", "le", "monde") -join " "    # "Bonjour le monde"

# Pattern matching
"fichier.txt" -like "*.txt"     # True (wildcard)
"abc123" -match "\d+"            # True (regex)
```

### Le formatage

```powershell
# L'opérateur -f (format)
"Bonjour {0}, tu as {1} ans." -f "Alice", 25    # Bonjour Alice, tu as 25 ans.

# Formatage de nombres
"Prix : {0:N2} €" -f 49.987     # Prix : 49,99 €
"N° {0:D5}" -f 42               # N° 00042
```

> **Comparaison :** l'opérateur `-f` en PowerShell = les f-strings en Python = `printf` en Bash. Les trois font la même chose avec une syntaxe différente.

## Très utile en pratique

### Tableau récapitulatif

| PowerShell | Bash | Python | Effet |
|-----------|------|--------|-------|
| `$s.Length` | `${#s}` | `len(s)` | Longueur |
| `$s.ToUpper()` | `${s^^}` | `s.upper()` | Majuscules |
| `$s.ToLower()` | `${s,,}` | `s.lower()` | Minuscules |
| `$s.Trim()` | — | `s.strip()` | Supprimer espaces |
| `$s.Replace(a,b)` | `${s//a/b}` | `s.replace(a,b)` | Remplacer |
| `$s -split ","` | — | `s.split(",")` | Découper |
| `$a -join " "` | — | `" ".join(a)` | Joindre |
| `$s -match "regex"` | `[[ $s =~ regex ]]` | `re.match()` | Regex |

## ✅ Tu sais maintenant...

- L'interpolation de chaînes (guillemets doubles vs simples)
- Les here-strings pour le multi-lignes
- Les méthodes `.ToUpper()`, `.ToLower()`, `.Trim()`, `.Replace()`, `.Split()`, `.Contains()`
- Les opérateurs `-replace`, `-split`, `-join`, `-match`, `-like`
- Le formatage avec `-f`

---

# Chapitre 8 — Tableaux, hashtables et boucles

## Le minimum à savoir

### Les tableaux (arrays)

```powershell
# Créer un tableau
$fruits = @("pomme", "banane", "cerise")

# Accéder aux éléments
$fruits[0]           # pomme
$fruits[-1]          # cerise
$fruits.Count        # 3

# Ajouter un élément
$fruits += "kiwi"    # ⚠️ Crée un NOUVEAU tableau (lent pour les gros tableaux)

# Parcourir
foreach ($fruit in $fruits) {
    Write-Output "Fruit : $fruit"
}

# Tester l'appartenance
$fruits -contains "banane"    # True
"banane" -in $fruits          # True (PowerShell 3+)
```

> **Comparaison :** `@("a", "b", "c")` en PowerShell = `("a" "b" "c")` en Bash = `["a", "b", "c"]` en Python.

### Les hashtables (dictionnaires)

```powershell
# Créer un hashtable
$capitales = @{
    France    = "Paris"
    Allemagne = "Berlin"
    Espagne   = "Madrid"
}

# Accéder
$capitales["France"]       # Paris
$capitales.France          # Paris (syntaxe alternative avec point)

# Ajouter
$capitales["Italie"] = "Rome"

# Modifier
$capitales["France"] = "Lyon"    # (oups)
$capitales["France"] = "Paris"   # (corrigé)

# Supprimer
$capitales.Remove("Espagne")

# Vérifier l'existence
$capitales.ContainsKey("France")       # True
$capitales.ContainsValue("Paris")      # True

# Parcourir
foreach ($pays in $capitales.Keys) {
    Write-Output "La capitale de $pays est $($capitales[$pays])"
}

# Ou avec GetEnumerator()
$capitales.GetEnumerator() | ForEach-Object {
    Write-Output "$($_.Key) → $($_.Value)"
}
```

> **Comparaison :** `@{ Clé = "Valeur" }` en PowerShell = `declare -A` en Bash = `{ "clé": "valeur" }` en Python.

### Les boucles

**`foreach` — parcourir une collection :**

```powershell
$noms = @("Alice", "Bob", "Charlie")

foreach ($nom in $noms) {
    Write-Output "Bonjour $nom"
}
```

**`for` — boucle classique avec compteur :**

```powershell
for ($i = 1; $i -le 10; $i++) {
    Write-Output "Tour $i"
}
```

**`while` — tant qu'une condition est vraie :**

```powershell
$compteur = 1
while ($compteur -le 5) {
    Write-Output "Compteur : $compteur"
    $compteur++
}
```

**`do...while` et `do...until` :**

```powershell
# do...while : exécute AU MOINS une fois, puis vérifie
do {
    $reponse = Read-Host "Tape 'oui' pour continuer"
} while ($reponse -ne "oui")

# do...until : exécute AU MOINS une fois, puis vérifie l'inverse
do {
    $reponse = Read-Host "Tape 'quitter' pour sortir"
} until ($reponse -eq "quitter")
```

**L'opérateur de plage `..` :**

```powershell
1..10 | ForEach-Object { Write-Output "Numéro $_" }

# Équivalent de range(1, 11) en Python et {1..10} en Bash
```

**`break` et `continue` :**

```powershell
foreach ($i in 1..10) {
    if ($i -eq 6) { break }        # Sort de la boucle
    if ($i -eq 3) { continue }    # Passe au tour suivant
    Write-Output $i
}
# Affiche : 1, 2, 4, 5
```

### `foreach` (statement) vs `ForEach-Object` (pipeline)

```powershell
# foreach (statement) — utilise quand tu as déjà la collection en mémoire
$services = Get-Service
foreach ($s in $services) {
    Write-Output $s.Name
}

# ForEach-Object (pipeline) — traite les objets au fur et à mesure
Get-Service | ForEach-Object { Write-Output $_.Name }
```

La différence : `foreach` charge tout en mémoire d'abord, `ForEach-Object` traite objet par objet (plus économe en mémoire pour les gros volumes).

## Très utile en pratique

### Les PSCustomObject

Pour créer des objets structurés avec des propriétés nommées :

```powershell
$utilisateur = [PSCustomObject]@{
    Nom    = "Alice"
    Age    = 25
    Ville  = "Paris"
    Admin  = $false
}

$utilisateur.Nom      # Alice
$utilisateur.Age      # 25

# Très utile pour créer des tableaux structurés
$equipe = @(
    [PSCustomObject]@{ Nom = "Alice"; Role = "Dev"; Exp = 5 }
    [PSCustomObject]@{ Nom = "Bob";   Role = "Ops"; Exp = 3 }
    [PSCustomObject]@{ Nom = "Charlie"; Role = "Sec"; Exp = 7 }
)

$equipe | Format-Table -AutoSize
```

### Mini script complet : menu de gestion de services

Un exemple de script fonctionnel de 25 lignes combinant hashtable, boucle et switch :

```powershell
# gestion_services.ps1 — Mini outil de supervision de services
$services_critiques = @("wuauserv", "W32Time", "WinDefend", "EventLog")

do {
    Write-Host "`n=== Supervision des services ===" -ForegroundColor Cyan
    Write-Host "1) État des services critiques"
    Write-Host "2) Services arrêtés (tous)"
    Write-Host "3) Quitter"
    $choix = Read-Host "Choix"

    switch ($choix) {
        "1" {
            foreach ($nom in $services_critiques) {
                $s = Get-Service -Name $nom -ErrorAction SilentlyContinue
                if ($s) {
                    $couleur = if ($s.Status -eq "Running") { "Green" } else { "Red" }
                    Write-Host "  $($s.DisplayName) : $($s.Status)" -ForegroundColor $couleur
                }
            }
        }
        "2" {
            Get-Service | Where-Object { $_.Status -eq "Stopped" } |
                Select-Object Name, DisplayName -First 15 | Format-Table -AutoSize
        }
        "3" { Write-Host "Au revoir." -ForegroundColor Yellow }
        default { Write-Host "Choix invalide." -ForegroundColor Red }
    }
} until ($choix -eq "3")
```

## ❌ Erreur classique

```powershell
# $fruits += "kiwi" est LENT pour les gros tableaux
# PowerShell crée un nouveau tableau à chaque += (copie tout)
# Pour les gros volumes, utilise une ArrayList :
$liste = [System.Collections.ArrayList]@()
$liste.Add("element") | Out-Null

# Confondre foreach et ForEach-Object
# foreach ne s'utilise PAS dans un pipeline
Get-Process | foreach ($p in ???) { }    # ❌ Syntaxe incorrecte
Get-Process | ForEach-Object { $_.Name } # ✅ Dans le pipeline
```

## 🧩 Mini-projet (chapitres 7-8)

Crée un script `contacts.ps1` qui :
1. Contient un tableau de hashtables (contacts avec nom et email)
2. Propose un menu en boucle : 1) Afficher, 2) Ajouter, 3) Chercher, 4) Quitter
3. Utilise `switch` pour le menu
4. L'option "Quitter" sort avec `break`

## ✅ Tu sais maintenant...

- Créer et manipuler des tableaux (`@()`)
- Créer et manipuler des hashtables (`@{}`)
- Les boucles : `foreach`, `for`, `while`, `do...while`, `do...until`
- L'opérateur de plage `..`
- La différence entre `foreach` (statement) et `ForEach-Object` (pipeline)
- Les PSCustomObject pour les données structurées

---

# Chapitre 9 — Fonctions

## Le minimum à savoir

### Définir et appeler une fonction

```powershell
function Dire-Bonjour {
    Write-Output "Salut, bienvenue !"
}

Dire-Bonjour
Dire-Bonjour
```

> **Convention :** les fonctions PowerShell suivent aussi le pattern `Verbe-Nom`. Pas obligatoire pour tes fonctions, mais c'est la bonne pratique.

### Paramètres de fonction avec `param()`

```powershell
function Dire-Bonjour {
    param(
        [Parameter(Mandatory)]
        [string]$Prenom,
        
        [int]$Age = 0
    )
    
    Write-Output "Bonjour $Prenom !"
    if ($Age -gt 0) {
        Write-Output "Tu as $Age ans."
    }
}

Dire-Bonjour -Prenom "Alice" -Age 25
Dire-Bonjour -Prenom "Bob"
```

C'est le même mécanisme `param()` que pour les scripts — les fonctions PowerShell sont de mini-scripts.

### Retourner un résultat : le piège fondamental

**En PowerShell, tout ce qui n'est pas capturé dans une variable est automatiquement renvoyé dans le pipeline.** C'est le concept le plus déroutant pour les débutants.

```powershell
function Calculer-Somme {
    param([int]$A, [int]$B)
    $A + $B    # ← Pas de "return" nécessaire — le résultat est renvoyé automatiquement
}

$resultat = Calculer-Somme -A 10 -B 25
Write-Output "La somme est : $resultat"    # → La somme est : 35
```

**Le piège :** si ta fonction fait d'autres opérations qui produisent une sortie, elles AUSSI sont renvoyées :

```powershell
function Mauvaise-Fonction {
    param([int]$A, [int]$B)
    Write-Output "Calcul en cours..."    # ← Ceci est AUSSI renvoyé !
    $A + $B
}

$resultat = Mauvaise-Fonction -A 10 -B 25
$resultat    # → @("Calcul en cours...", 35) — un TABLEAU, pas un nombre !
```

**La solution :** utilise `Write-Verbose` pour les messages de diagnostic. `Write-Verbose` n'est renvoyé que si l'appelant passe `-Verbose` — mais pour que `-Verbose` fonctionne, ta fonction doit avoir l'attribut `[CmdletBinding()]` (voir plus bas dans ce chapitre) :

```powershell
function Bonne-Fonction {
    [CmdletBinding()]
    param([int]$A, [int]$B)
    Write-Verbose "Calcul en cours..."    # ← Affiché uniquement avec -Verbose
    $A + $B                                # ← Seul ceci est renvoyé
}

$resultat = Bonne-Fonction -A 10 -B 25           # → 35 (pas de message verbose)
$resultat = Bonne-Fonction -A 10 -B 25 -Verbose  # → affiche "Calcul en cours...", puis 35
```

> **Comparaison :** en Python, seul `return` renvoie une valeur. En Bash, `echo` + `$(...)`. En PowerShell, **tout** est renvoyé sauf ce qui est explicitement capturé ou envoyé ailleurs.

### `return` existe, mais...

`return` existe en PowerShell, mais il fait deux choses : il renvoie la valeur ET il quitte la fonction. Il n'est pas obligatoire pour renvoyer un résultat.

```powershell
function Verifier-Age {
    param([int]$Age)
    if ($Age -lt 0) {
        return "Âge invalide"    # Quitte la fonction ici
    }
    if ($Age -ge 18) {
        return "Majeur"
    }
    return "Mineur"
}
```

### Portée des variables

Les variables dans une fonction sont **locales** par défaut :

```powershell
$nom = "Global"

function Modifier {
    $nom = "Local"
    Write-Output "Dans la fonction : $nom"    # → Local
}

Modifier
Write-Output "Après la fonction : $nom"       # → Global (pas changé)
```

Pour accéder à la portée parente : `$script:nom`, `$global:nom`. Mais en général, évite de modifier les variables globales — passe des paramètres et renvoie des résultats.

## Très utile en pratique

### Fonctions avancées avec `[CmdletBinding()]`

L'attribut `[CmdletBinding()]` transforme ta fonction en cmdlet "avancé" avec le support automatique de `-Verbose`, `-Debug`, `-ErrorAction`, `-WhatIf` :

```powershell
function Renommer-Fichiers {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Dossier,
        
        [string]$Extension = ".bak"
    )
    
    Write-Verbose "Traitement du dossier $Dossier"
    
    Get-ChildItem -Path $Dossier -File | ForEach-Object {
        $nouveau = $_.BaseName + $Extension
        Write-Verbose "Renommage : $($_.Name) → $nouveau"
    }
}

# Appel normal
Renommer-Fichiers -Dossier "C:\temp"

# Appel avec messages de diagnostic
Renommer-Fichiers -Dossier "C:\temp" -Verbose
```

## ❌ Erreur classique

```powershell
# Le piège du return implicite
function Test {
    $liste = @()
    $liste.Add("item")    # ← .Add() renvoie l'index (0) → pollue la sortie !
    return $liste
}
# Solution : capturer ou rediriger
$liste.Add("item") | Out-Null    # ← Out-Null absorbe la sortie non désirée

# Appeler une fonction avec des parenthèses et des virgules (syntaxe C#)
Dire-Bonjour("Alice", 25)        # ❌ PowerShell interprète comme un seul argument (un tableau)
Dire-Bonjour -Prenom "Alice" -Age 25   # ✅ Syntaxe PowerShell correcte
Dire-Bonjour "Alice" 25          # ✅ Paramètres positionnels (sans noms)
```

## ✅ Tu sais maintenant...

- Définir une fonction avec `function Nom { param(...) ... }`
- Le piège du return implicite (tout ce qui n'est pas capturé est renvoyé)
- Utiliser `Write-Verbose` au lieu de `Write-Output` pour les messages de diagnostic
- Les paramètres de fonction (même `param()` que pour les scripts)
- `[CmdletBinding()]` pour les fonctions avancées

---

# Chapitre 10 — Fichiers, registre et administration système

## Le minimum à savoir

### Lire un fichier

```powershell
# Lire tout le contenu
$contenu = Get-Content -Path "mon_fichier.txt" -Encoding UTF8
Write-Output $contenu

# Lire ligne par ligne (chaque ligne est un élément du tableau)
$lignes = Get-Content -Path "donnees.txt" -Encoding UTF8
foreach ($ligne in $lignes) {
    Write-Output "Lu : $ligne"
}

# Lire les N premières/dernières lignes
Get-Content "log.txt" -First 10     # Les 10 premières lignes (comme head)
Get-Content "log.txt" -Last 5       # Les 5 dernières lignes (comme tail)
Get-Content "log.txt" -Tail 5 -Wait # Comme tail -f (suit les ajouts en temps réel)
```

> **Comparaison :** `Get-Content` = `cat` en Bash = `open().read()` en Python.

> **Bonne pratique :** ajoute toujours `-Encoding UTF8` pour gérer correctement les accents et les caractères spéciaux.

### Écrire dans un fichier

```powershell
# Écraser (créer ou remplacer)
Set-Content -Path "resultat.txt" -Value "Ligne 1" -Encoding UTF8

# Ajouter à la fin
Add-Content -Path "journal.txt" -Value "Nouvelle entrée" -Encoding UTF8

# Écrire plusieurs lignes
@("Ligne 1", "Ligne 2", "Ligne 3") | Set-Content "fichier.txt" -Encoding UTF8

# Rediriger la sortie d'une commande vers un fichier
Get-Process | Out-File -Path "processus.txt" -Encoding UTF8
```

> **Comparaison :** `Set-Content` = `>` en Bash = `open("f", "w")` en Python. `Add-Content` = `>>` = `open("f", "a")`.

### Manipuler les chemins

```powershell
# Joindre des chemins
Join-Path -Path $HOME -ChildPath "Documents\rapport.txt"
# → C:\Users\Alice\Documents\rapport.txt

# Extraire des parties d'un chemin
Split-Path "C:\Users\Alice\rapport.txt" -Leaf       # rapport.txt (le nom)
Split-Path "C:\Users\Alice\rapport.txt" -Parent      # C:\Users\Alice
[System.IO.Path]::GetExtension("rapport.txt")        # .txt

# Vérifier l'existence
Test-Path "C:\Users\Alice\Documents"                  # True ou False
Test-Path "C:\Users\Alice\Documents" -PathType Container   # C'est un dossier ?
Test-Path "C:\Users\Alice\rapport.txt" -PathType Leaf      # C'est un fichier ?
```

### Créer, copier, déplacer, supprimer

```powershell
# Créer un dossier
New-Item -ItemType Directory -Path "C:\temp\mon_dossier" -Force

# Créer un fichier
New-Item -ItemType File -Path "C:\temp\mon_fichier.txt"

# Copier
Copy-Item -Path "source.txt" -Destination "copie.txt"
Copy-Item -Path "C:\source\*" -Destination "C:\destination\" -Recurse

# Déplacer / renommer
Move-Item -Path "ancien.txt" -Destination "nouveau.txt"

# Supprimer
Remove-Item -Path "fichier.txt"
Remove-Item -Path "dossier" -Recurse -Force    # Supprimer un dossier et son contenu
```

### CSV natif (sans module !)

PowerShell gère le CSV nativement — pas besoin d'importer un module :

```powershell
# Lire un CSV → chaque ligne devient un objet avec des propriétés !
$donnees = Import-Csv -Path "contacts.csv" -Encoding UTF8

foreach ($ligne in $donnees) {
    Write-Output "$($ligne.Nom) — $($ligne.Email)"
}

# Filtrer et manipuler
$parisiens = $donnees | Where-Object { $_.Ville -eq "Paris" }

# Exporter en CSV
Get-Process | Select-Object Name, Id, CPU | Export-Csv -Path "processus.csv" -NoTypeInformation -Encoding UTF8
```

> **C'est un avantage majeur de PowerShell :** le CSV est lu comme des **objets** avec des propriétés nommées. Pas besoin de parser du texte ou de compter les colonnes.

### JSON natif

```powershell
# Lire du JSON
$config = Get-Content "config.json" -Encoding UTF8 | ConvertFrom-Json
$config.serveur
$config.port

# Écrire du JSON
$data = @{
    serveur = "192.168.1.1"
    port    = 8080
    debug   = $true
}
$data | ConvertTo-Json | Set-Content "config.json" -Encoding UTF8
```

---

## Le registre Windows : une spécificité PowerShell `[🪟 Windows]`

### Qu'est-ce que le registre ?

Le registre Windows est la **base de données de configuration** du système. Tout y est : les paramètres du système, les logiciels installés, les associations de fichiers, les politiques de sécurité, les configurations réseau. En administration Windows, le registre est incontournable.

PowerShell traite le registre **comme un système de fichiers**. Tu le parcours avec les mêmes commandes (`Get-ChildItem`, `Get-ItemProperty`, `Set-ItemProperty`) :

```powershell
# Les "lecteurs" du registre
Get-PSDrive -PSProvider Registry
# HKCU (HKEY_CURRENT_USER) — configuration de l'utilisateur courant
# HKLM (HKEY_LOCAL_MACHINE) — configuration de la machine

# Parcourir le registre comme un dossier
Get-ChildItem -Path "HKCU:\Software"

# Lire une valeur
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer" -Name "Max Cached Icons"

# Lire toutes les valeurs d'une clé
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
```

### Modifier le registre

```powershell
# Créer une clé
New-Item -Path "HKCU:\Software\MonApp" -Force

# Créer une nouvelle valeur (avec le type explicite)
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "dark" -PropertyType String
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Version" -Value 2 -PropertyType DWord

# Modifier une valeur existante
Set-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "light"

# Supprimer une valeur
Remove-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme"

# Supprimer une clé
Remove-Item -Path "HKCU:\Software\MonApp" -Recurse
```

> **Bonne pratique :** utilise `New-ItemProperty` pour créer une valeur (en spécifiant le type avec `-PropertyType`), et `Set-ItemProperty` pour modifier une valeur existante. Les types courants sont `String`, `DWord` (entier 32 bits), `QWord` (entier 64 bits), `Binary`, `ExpandString`, `MultiString`.

> **⚠️ Attention :** modifier le registre peut casser le système si tu te trompes. Travaille d'abord dans `HKCU:` (utilisateur) avant de toucher `HKLM:` (machine — nécessite les droits admin).

### Le concept de PSDrive

Le registre n'est qu'un exemple de **PSDrive**. PowerShell abstrait plusieurs systèmes comme des "lecteurs" que tu parcours avec les mêmes commandes :

| PSDrive | Contenu |
|---------|---------|
| `C:`, `D:` | Le système de fichiers |
| `HKCU:`, `HKLM:` | Le registre Windows |
| `Env:` | Les variables d'environnement |
| `Cert:` | Les certificats |
| `Variable:` | Les variables PowerShell |

```powershell
# Lister les variables d'environnement
Get-ChildItem Env:

# Voir un certificat
Get-ChildItem Cert:\CurrentUser\My
```

### Mini script complet : rapport de dossier en CSV

Un script fonctionnel qui analyse un dossier et produit un rapport — la combinaison fichiers + pipeline + CSV :

```powershell
# rapport_dossier.ps1 — Inventaire rapide d'un dossier
param(
    [string]$Dossier = ".",
    [string]$Sortie = "rapport.csv"
)

if (-not (Test-Path $Dossier -PathType Container)) {
    Write-Error "Le dossier '$Dossier' n'existe pas."
    exit 1
}

$fichiers = Get-ChildItem -Path $Dossier -File | ForEach-Object {
    [PSCustomObject]@{
        Nom       = $_.Name
        Extension = $_.Extension
        Taille_Ko = [math]::Round($_.Length / 1KB, 1)
        Modifie   = $_.LastWriteTime.ToString("yyyy-MM-dd HH:mm")
    }
}

$fichiers | Export-Csv -Path $Sortie -NoTypeInformation -Encoding UTF8

$stats = $fichiers | Measure-Object -Property Taille_Ko -Sum -Maximum
Write-Host "`nRapport exporté dans $Sortie" -ForegroundColor Green
Write-Output "$($fichiers.Count) fichier(s), $([math]::Round($stats.Sum)) Ko total, plus gros : $([math]::Round($stats.Maximum)) Ko"
```

## ❌ Erreur classique

```powershell
# Confondre Set-Content et Out-File
# Set-Content écrit du texte brut, Out-File écrit la sortie formatée de PowerShell
# Pour des fichiers texte/CSV/JSON → Set-Content
# Pour enregistrer la sortie d'un cmdlet → Out-File

# Oublier -Encoding UTF8
Get-Content "fichier.txt"    # ⚠️ L'encodage par défaut varie selon la version de PowerShell
Get-Content "fichier.txt" -Encoding UTF8   # ✅ Toujours spécifier

# Oublier -NoTypeInformation sur Export-Csv
Export-Csv -Path "data.csv"     # ❌ Ajoute une ligne #TYPE en en-tête
Export-Csv -Path "data.csv" -NoTypeInformation   # ✅ CSV propre

# Modifier le registre machine sans droits admin
Set-ItemProperty -Path "HKLM:\..." -Name "Valeur" -Value 1   # ❌ Accès refusé
# → Lance PowerShell en tant qu'administrateur
```

## 🧩 Mini-projet (chapitres 9-10)

Crée un script `inventaire.ps1` qui :
1. Prend un dossier en paramètre
2. Liste tous les fichiers avec leur nom, extension, taille en Ko, et date de modification
3. Crée des PSCustomObject pour chaque fichier
4. Exporte le tout en CSV
5. Affiche un résumé : nombre de fichiers, taille totale, fichier le plus gros

## ✅ Tu sais maintenant...

- Lire et écrire des fichiers (`Get-Content`, `Set-Content`, `Add-Content`)
- Manipuler les chemins (`Join-Path`, `Split-Path`, `Test-Path`)
- Importer et exporter du CSV et du JSON nativement
- Parcourir et modifier le registre Windows
- Le concept de PSDrive (fichiers, registre, certificats, env — même interface)

---

# Chapitre 11 — Processus, services, logs, remoting et triage forensic léger

## Le minimum à savoir

Ce chapitre est celui où PowerShell montre sa vraie valeur : **l'administration Windows en ligne de commande**.

### Gérer les processus

```powershell
# Lister tous les processus
Get-Process

# Chercher un processus par nom
Get-Process -Name chrome

# Les 5 processus les plus gourmands en mémoire
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id, @{N="RAM (Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 5

# Arrêter un processus
Stop-Process -Name notepad
Stop-Process -Id 1234

# Lancer un processus
Start-Process notepad
Start-Process "C:\Program Files\app.exe" -ArgumentList "/silent"
```

### Gérer les services Windows

```powershell
# Lister tous les services
Get-Service

# Services en cours d'exécution
Get-Service | Where-Object { $_.Status -eq "Running" }

# Vérifier un service spécifique
Get-Service -Name "wuauserv"    # Windows Update

# Démarrer / arrêter / redémarrer un service                    [🔑 Admin]
Start-Service -Name "wuauserv"
Stop-Service -Name "wuauserv"
Restart-Service -Name "wuauserv"

# Changer le type de démarrage                                   [🔑 Admin]
Set-Service -Name "wuauserv" -StartupType Automatic
Set-Service -Name "wuauserv" -StartupType Disabled
```

> **Pourquoi c'est important :** en administration Windows et en cybersécurité, savoir vérifier quels services tournent, les arrêter, les démarrer, et changer leur configuration est une compétence fondamentale. Un service non autorisé qui tourne peut être un indicateur de compromission.

### Lire les journaux d'événements Windows (Event Logs) `[🪟 Windows]`

Les Event Logs sont les **logs du système Windows** — la source d'information principale pour le diagnostic et la sécurité.

```powershell
# Lister les journaux disponibles
Get-WinEvent -ListLog * | Select-Object LogName, RecordCount -First 20

# Lire les derniers événements du journal System
Get-WinEvent -LogName System -MaxEvents 20

# Lire les derniers événements du journal Security (nécessite admin)
Get-WinEvent -LogName Security -MaxEvents 20

# Filtrer par ID d'événement (ex : 4624 = connexion réussie)
Get-WinEvent -LogName Security -FilterHashtable @{Id=4624} -MaxEvents 10

# Filtrer par période
Get-WinEvent -LogName System -FilterHashtable @{
    StartTime = (Get-Date).AddDays(-1)    # Depuis hier
    Level     = 2                          # Erreurs uniquement (2 = Error)
}
```

Les Event IDs importants pour la sécurité :

| Event ID | Journal | Signification |
|----------|---------|--------------|
| 4624 | Security | Connexion réussie |
| 4625 | Security | Échec de connexion |
| 4648 | Security | Connexion avec des identifiants explicites |
| 4720 | Security | Création d'un compte utilisateur |
| 7045 | System | Installation d'un service |
| 1102 | Security | Journal d'audit effacé (suspect !) |

> **Pourquoi c'est important :** la lecture des Event Logs est une compétence clé en blue team. Un script PowerShell qui surveille les Event ID 4625 (échecs de connexion) peut détecter une attaque par brute-force.

### Informations système

```powershell
# Informations sur le système
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber, LastBootUpTime

# Informations sur le matériel
Get-CimInstance Win32_ComputerSystem | Select-Object Name, Manufacturer, Model, TotalPhysicalMemory

# Espace disque
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, @{N="Taille (Go)";E={[math]::Round($_.Size/1GB)}}, @{N="Libre (Go)";E={[math]::Round($_.FreeSpace/1GB)}}

# Adresses réseau
Get-NetIPAddress | Where-Object { $_.AddressFamily -eq "IPv4" -and $_.IPAddress -ne "127.0.0.1" }
```

> **Note :** `Get-CimInstance` remplace l'ancien `Get-WmiObject`. C'est l'interface vers WMI/CIM — la couche d'instrumentation de Windows qui donne accès à des centaines de classes d'information système.

### Les tâches planifiées

L'équivalent de `cron` sous Linux :

```powershell
# Lister les tâches planifiées
Get-ScheduledTask

# Détails d'une tâche
Get-ScheduledTask -TaskName "MaTache" | Get-ScheduledTaskInfo

# Créer une tâche planifiée
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\scripts\backup.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "02:00"
Register-ScheduledTask -TaskName "BackupQuotidien" -Action $action -Trigger $trigger -Description "Sauvegarde quotidienne"

# Supprimer une tâche
Unregister-ScheduledTask -TaskName "BackupQuotidien" -Confirm:$false
```

## Très utile en pratique

### Le remoting : exécuter des commandes à distance

PowerShell Remoting permet d'exécuter des commandes sur des machines distantes — c'est l'équivalent de SSH pour Windows. `[🪟 Windows]` `[🔑 Admin]`

```powershell
# Activer le remoting sur la machine cible (une seule fois, en admin)   [🔑 Admin]
Enable-PSRemoting -Force

# Ouvrir une session interactive sur une machine distante
Enter-PSSession -ComputerName "SERVEUR01"
# Tu es maintenant "sur" SERVEUR01 — toutes les commandes s'exécutent là-bas
Exit-PSSession

# Exécuter une commande sur une machine distante (sans session interactive)
Invoke-Command -ComputerName "SERVEUR01" -ScriptBlock {
    Get-Service | Where-Object { $_.Status -eq "Running" }
}

# Exécuter sur PLUSIEURS machines en même temps
Invoke-Command -ComputerName "SERVEUR01", "SERVEUR02", "SERVEUR03" -ScriptBlock {
    Get-CimInstance Win32_OperatingSystem | Select-Object PSComputerName, Caption, LastBootUpTime
}
```

> **Pourquoi c'est puissant :** une seule commande pour vérifier l'état de 50 serveurs, installer un patch, redémarrer un service. C'est l'outil fondamental de l'administration Windows à grande échelle.

> **Note sécurité :** le remoting utilise WinRM (Windows Remote Management), qui est chiffré (HTTPS ou Kerberos). En environnement Active Directory, l'authentification est automatique (Kerberos). Hors domaine, il faut configurer TrustedHosts ou utiliser HTTPS avec des certificats.

### Ouverture sur Active Directory

Si le module Active Directory est installé (il l'est sur les contrôleurs de domaine et les postes avec RSAT) :

```powershell
# Importer le module
Import-Module ActiveDirectory

# Lister les utilisateurs
Get-ADUser -Filter * -Properties DisplayName, LastLogonDate | Select-Object DisplayName, LastLogonDate

# Chercher un utilisateur
Get-ADUser -Identity "alice.dupont"

# Lister les groupes
Get-ADGroup -Filter *

# Les utilisateurs inactifs depuis 90 jours
$seuil = (Get-Date).AddDays(-90)
Get-ADUser -Filter {LastLogonDate -lt $seuil} -Properties LastLogonDate
```

> **Note :** ce cours n'est pas un cours AD (voir le cours Active Directory de la bibliothèque). Mais savoir que PowerShell est l'outil principal d'administration AD est important pour le contexte.

## Bonus — PowerShell pour le triage et le forensic léger

PowerShell permet un premier niveau de **triage forensic** sur un poste Windows : vérifier une signature, calculer un hash, inspecter des traces, repérer des indices de compromission. Ce n'est pas un outil de forensic complet, mais c'est un excellent outil d'**observation rapide et d'automatisation**.

### Vérifier la signature d'un fichier

```powershell
Get-AuthenticodeSignature "C:\Temp\outil.exe"

# Résultat exploitable
Get-AuthenticodeSignature "C:\Temp\outil.exe" | Select-Object Status, StatusMessage, Path
```

Le champ `Status` te dit si le fichier est signé (`Valid`), non signé (`NotSigned`), ou si la signature est invalide (`HashMismatch`). Un fichier signé n'est pas forcément sain, mais un fichier non signé dans `C:\Windows\System32` est suspect.

### Calculer le hash d'un fichier

```powershell
Get-FileHash "C:\Temp\outil.exe" -Algorithm SHA256
```

Le hash SHA256 est l'empreinte unique du fichier. Tu peux le comparer avec des bases d'IOC (VirusTotal, MISP) pour vérifier si le fichier est connu comme malveillant. Utilise SHA256 par défaut — MD5 et SHA1 sont considérés comme faibles.

### Récupérer les métadonnées d'un fichier

```powershell
Get-Item "C:\Temp\outil.exe" | Select-Object Name, FullName, Length, CreationTime, LastWriteTime, LastAccessTime
```

Les dates sont importantes en forensic : un fichier dont la date de création est postérieure à la date de dernière écriture est suspect (possiblement copié ou modifié avec des outils de timestomping).

### Vérifier les Alternate Data Streams (ADS)

Les ADS sont des flux de données cachés attachés à un fichier — une spécificité NTFS. Le flux `Zone.Identifier` indique qu'un fichier a été téléchargé depuis Internet :

```powershell
# Lister les ADS d'un fichier
Get-Item "C:\Temp\outil.exe" -Stream *

# Lire le Zone.Identifier (provenance du fichier)
Get-Content "C:\Temp\outil.exe" -Stream Zone.Identifier
# ZoneId=3 → téléchargé depuis Internet
```

Un exécutable avec un `Zone.Identifier` supprimé alors qu'il devrait en avoir un peut indiquer une tentative de contournement de la protection SmartScreen.

### Lire l'historique des commandes PowerShell

```powershell
# Chemin de l'historique PSReadLine
$histPath = "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"

# Lire les dernières commandes
Get-Content $histPath -Tail 50
```

> **Note :** cet historique ne capture que les commandes tapées dans une console interactive avec PSReadLine. Les scripts exécutés automatiquement, les sessions distantes, et les sessions sans PSReadLine n'y apparaissent pas. C'est un indice, pas un journal exhaustif.

### Consulter les logs PowerShell

```powershell
# Activité PowerShell récente
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -MaxEvents 20 |
    Select-Object TimeCreated, Id, Message

# Chercher des exécutions de scripts (Event ID 4104 = Script Block Logging)
Get-WinEvent -FilterHashtable @{
    LogName = "Microsoft-Windows-PowerShell/Operational"
    Id      = 4104
} -MaxEvents 10 -ErrorAction SilentlyContinue
```

Les Event IDs PowerShell importants :

| Event ID | Journal | Signification |
|----------|---------|--------------|
| 4103 | PowerShell/Operational | Exécution de module |
| 4104 | PowerShell/Operational | Script Block Logging (contenu du script exécuté) |
| 400 | Windows PowerShell | Démarrage du moteur PowerShell |
| 403 | Windows PowerShell | Arrêt du moteur PowerShell |

> **Pour la blue team :** le Script Block Logging (Event ID 4104) est l'une des sources les plus précieuses pour détecter l'utilisation malveillante de PowerShell. Si cette journalisation est activée (GPO), chaque bloc de script exécuté est enregistré — y compris les scripts obfusqués après désobfuscation.

### Repérer des indices de persistance

Un rapide triage des mécanismes de persistance classiques :

```powershell
# Programmes au démarrage (registre utilisateur)
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# Programmes au démarrage (registre machine — nécessite admin)
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# Tâches planifiées inhabituelles
Get-ScheduledTask | Where-Object { $_.State -eq "Ready" } |
    Select-Object TaskName, TaskPath, @{N="Action";E={$_.Actions.Execute}} |
    Format-Table -AutoSize

# Services avec un chemin d'exécution inhabituel
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -and $_.PathName -notlike "*System32*" -and $_.PathName -notlike "*SysWOW64*" } |
    Select-Object Name, State, PathName
```

### Cas pratique : analyser rapidement un fichier suspect

```powershell
param(
    [Parameter(Mandatory)]
    [string]$Chemin
)

if (-not (Test-Path $Chemin)) {
    Write-Error "Fichier introuvable : $Chemin"
    exit 1
}

Write-Host "`n=== Analyse rapide de $Chemin ===" -ForegroundColor Cyan

# 1. Métadonnées
$item = Get-Item $Chemin
Write-Host "`n[Métadonnées]" -ForegroundColor Yellow
Write-Output "Taille     : $([math]::Round($item.Length / 1KB, 1)) Ko"
Write-Output "Créé       : $($item.CreationTime)"
Write-Output "Modifié    : $($item.LastWriteTime)"

# 2. Hash
Write-Host "`n[Hash SHA256]" -ForegroundColor Yellow
(Get-FileHash $Chemin -Algorithm SHA256).Hash

# 3. Signature
Write-Host "`n[Signature]" -ForegroundColor Yellow
$sig = Get-AuthenticodeSignature $Chemin
Write-Output "Statut : $($sig.Status)"
if ($sig.SignerCertificate) {
    Write-Output "Signataire : $($sig.SignerCertificate.Subject)"
}

# 4. ADS
Write-Host "`n[Alternate Data Streams]" -ForegroundColor Yellow
$streams = Get-Item $Chemin -Stream * -ErrorAction SilentlyContinue
$streams | Select-Object Stream, Length | Format-Table -AutoSize

Write-Host "`n=== Fin de l'analyse ===" -ForegroundColor Cyan
```

> **Positionnement :** cette mini-section donne les réflexes de triage. Pour une investigation forensic complète, voir le cours Digital Forensics de la bibliothèque.

## Bonus — Sécurité de l'exécution PowerShell

Pour un profil cyber, comprendre comment PowerShell se protège (et peut être contourné) est important.

### Constrained Language Mode

PowerShell peut être verrouillé en mode **langage contraint** — seuls les cmdlets de base fonctionnent, pas les appels .NET, les classes, ni le chargement de modules non signés :

```powershell
# Vérifier le mode actuel              [🪟 Windows]
$ExecutionContext.SessionState.LanguageMode
# FullLanguage     → tout est autorisé (défaut)
# ConstrainedLanguage → restreint (typiquement forcé par AppLocker/WDAC)
```

Le Constrained Language Mode est une protection contre l'utilisation offensive de PowerShell. Il est généralement activé via **AppLocker** ou **WDAC** (Windows Defender Application Control), pas manuellement.

### AMSI (Antimalware Scan Interface)

AMSI est l'interface qui permet à l'antivirus d'inspecter le contenu des scripts **avant leur exécution** — y compris après désobfuscation. Concrètement, quand tu exécutes un script PowerShell, AMSI envoie le contenu à l'antivirus qui peut bloquer l'exécution.

```powershell
# Tester si AMSI est actif (ce script inoffensif déclenche AMSI par convention)
# La chaîne "AmsiUtils" est surveillée comme marqueur de test
```

> **Pour la blue team :** AMSI est une couche de défense critique. Sa désactivation (via `amsiInitFailed` ou patch mémoire) est un indicateur de compromission — les attaquants tentent souvent de contourner AMSI en premier.

### Script Block Logging et transcription

Deux mécanismes de journalisation essentiels, activables par GPO :

**Script Block Logging** (Event ID 4104) : enregistre le contenu de chaque bloc de script exécuté dans le journal PowerShell/Operational — y compris les scripts obfusqués après désobfuscation par le moteur PowerShell.

**Transcription PowerShell** : enregistre tout ce qui est tapé et affiché dans une session PowerShell dans un fichier texte.

```powershell
# Activer la transcription manuellement (pour tester)        [🪟 Windows]
Start-Transcript -Path "$HOME\powershell_transcript.txt"
# ... toutes les commandes sont enregistrées ...
Stop-Transcript

# En production, ces deux mécanismes sont activés par GPO :
# Configuration ordinateur → Stratégies → Modèles d'administration →
#   Composants Windows → Windows PowerShell →
#   - "Activer la journalisation de blocs de script PowerShell"
#   - "Activer la transcription PowerShell"
```

> **Recommandation blue team :** activer le Script Block Logging et la transcription sur tous les postes et serveurs de l'entreprise. C'est l'une des sources les plus précieuses pour détecter l'utilisation malveillante de PowerShell (encodage base64, téléchargement de payloads, Invoke-Expression, etc.).

## ❌ Erreur classique

```powershell
# Oublier les droits admin pour les opérations système
Stop-Service -Name "wuauserv"     # ❌ Accès refusé si pas admin
# → Lancer PowerShell "en tant qu'administrateur"

# Confondre Get-WmiObject (ancien) et Get-CimInstance (moderne)
Get-WmiObject Win32_OperatingSystem    # ⚠️ Fonctionne mais déprécié
Get-CimInstance Win32_OperatingSystem  # ✅ La méthode moderne

# Oublier -MaxEvents sur Get-WinEvent (le journal est ÉNORME)
Get-WinEvent -LogName Security    # ❌ Tente de charger TOUT le journal → très lent
Get-WinEvent -LogName Security -MaxEvents 50   # ✅ Les 50 derniers
```

## ✅ Tu sais maintenant...

- Gérer les processus (`Get-Process`, `Stop-Process`, `Start-Process`)
- Gérer les services (`Get-Service`, `Start-Service`, `Stop-Service`)
- Lire les journaux d'événements Windows (`Get-WinEvent`)
- Récupérer des informations système (`Get-CimInstance`)
- Créer des tâches planifiées (`Register-ScheduledTask`)
- Exécuter des commandes à distance (`Enter-PSSession`, `Invoke-Command`)
- L'ouverture vers l'administration AD
- (Bonus) Le triage forensic léger : signature, hash, ADS, historique PowerShell, logs, persistance

## 💬 Questions d'entretien typiques

- **Qu'est-ce que le pipeline d'objets en PowerShell ?** → Contrairement à Bash où le pipeline transporte du texte brut, PowerShell transporte des objets structurés avec des propriétés. On peut filtrer, trier et sélectionner des propriétés directement, sans parser du texte.
- **Quelle est la différence entre `Write-Output` et `Write-Host` ?** → `Write-Output` envoie dans le pipeline (peut être capturé, redirigé). `Write-Host` affiche directement à l'écran et ne passe PAS dans le pipeline.
- **Comment exécuter une commande sur une machine distante ?** → `Invoke-Command -ComputerName SERVEUR -ScriptBlock { commande }` pour une commande ponctuelle, ou `Enter-PSSession` pour une session interactive.
- **Comment vérifier rapidement si un fichier est suspect ?** → Calculer son hash (`Get-FileHash`), vérifier sa signature (`Get-AuthenticodeSignature`), inspecter ses métadonnées et ses Alternate Data Streams, puis croiser le hash avec des bases d'IOC.
- **Pourquoi `param()` est préférable à `$args` ?** → Les paramètres sont nommés, typés, validables, auto-complétés par Tab. C'est plus lisible, plus robuste, et plus professionnel.

---

# Chapitre 12 — Débogage, bonnes pratiques et cas pratiques

## Le minimum à savoir

### Lire les messages d'erreur PowerShell

PowerShell utilise des **couleurs** pour les messages :
- **Rouge** = erreur (terminante ou non)
- **Jaune** = avertissement (warning)
- **Cyan** = message d'information (verbose)

```
Get-Content : Cannot find path 'C:\inexistant.txt' because it does not exist.
At C:\scripts\test.ps1:3 char:1
+ Get-Content "C:\inexistant.txt"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\inexistant.txt:String) [Get-Content], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand
```

Comment le lire :
1. **Première ligne** = le message d'erreur clair
2. **Ligne suivante** = le fichier et le numéro de ligne
3. **La ligne avec `+`** = la commande fautive
4. **CategoryInfo** = le type d'erreur

### La gestion d'erreurs avec `try/catch`

```powershell
try {
    $contenu = Get-Content "inexistant.txt" -ErrorAction Stop
    Write-Output "Fichier lu avec succès"
}
catch {
    Write-Output "Erreur : $($_.Exception.Message)"
}
finally {
    Write-Output "Ce bloc s'exécute toujours"
}
```

> **Point crucial :** `-ErrorAction Stop` est **obligatoire** pour que `catch` fonctionne avec les cmdlets PowerShell. Sans ça, l'erreur s'affiche en rouge mais le script continue — le `catch` n'est jamais déclenché.

### Les niveaux d'ErrorAction

| Valeur | Effet |
|--------|-------|
| `Continue` | Affiche l'erreur et continue (défaut) |
| `Stop` | Transforme l'erreur en exception (pour try/catch) |
| `SilentlyContinue` | Ignore l'erreur silencieusement |
| `Inquire` | Demande à l'utilisateur quoi faire |

```powershell
# Ignorer une erreur attendue
$service = Get-Service -Name "ServiceInexistant" -ErrorAction SilentlyContinue
if ($null -eq $service) {
    Write-Output "Le service n'existe pas"
}
```

### La variable `$Error`

PowerShell stocke toutes les erreurs récentes dans `$Error` :

```powershell
$Error[0]           # La dernière erreur
$Error.Count        # Nombre d'erreurs stockées
$Error.Clear()      # Vider la liste
```

### Les messages de diagnostic

```powershell
# Write-Verbose — pour les messages de diagnostic (activés avec -Verbose)
Write-Verbose "Traitement du fichier $fichier"

# Write-Warning — pour les avertissements
Write-Warning "Le dossier de destination n'existe pas, création..."

# Write-Debug — pour le débogage approfondi (activé avec -Debug)
Write-Debug "Variable x = $x"

# Write-Error — pour signaler une erreur non fatale
Write-Error "Le paramètre est invalide"
```

> **Bonne pratique :** utilise `Write-Verbose` pour les messages de suivi (activés à la demande avec `-Verbose`). N'utilise pas `Write-Host` pour le débogage — ça ne peut pas être désactivé.

### `Set-StrictMode` : le filet de sécurité

```powershell
Set-StrictMode -Version Latest

$resultat = $variableQuiNexistePas    # ❌ Erreur ! (sans StrictMode, ça renvoie $null silencieusement)
```

C'est l'équivalent de `set -euo pipefail` en Bash et `Set-StrictMode` attrape les variables non définies, les propriétés inexistantes, et d'autres erreurs sournoises.

### Les bonnes pratiques

```powershell
# 1. Utiliser les noms de paramètres complets
Get-ChildItem -Path "C:\" -Recurse -File    # ✅ Clair
gci C:\ -r -fi                              # ❌ Cryptique

# 2. Nommer les variables en PascalCase ou camelCase
$NombreFichiers = 5     # ✅ Lisible
$nf = 5                 # ❌ Cryptique

# 3. Commenter pourquoi, pas quoi
# ❌ Inutile :
$compteur++    # Incrémente le compteur

# ✅ Utile :
$compteur++    # On ignore les fichiers système cachés

# 4. Structurer avec des fonctions
# 5. Toujours gérer les erreurs dans les scripts de production
# 6. Utiliser param() au lieu de $args
```

### L'aide basée sur les commentaires

```powershell
function Get-RapportSysteme {
    <#
    .SYNOPSIS
        Génère un rapport système.
    
    .DESCRIPTION
        Ce script collecte les informations système (OS, CPU, RAM, disque)
        et les exporte en CSV.
    
    .PARAMETER Chemin
        Le chemin de sortie du rapport CSV.
    
    .EXAMPLE
        Get-RapportSysteme -Chemin "C:\rapports\systeme.csv"
    
    .NOTES
        Auteur : Sami
        Date   : 2025-04-07
    #>
    param(
        [Parameter(Mandatory)]
        [string]$Chemin
    )
    # ...
}

# Ensuite, Get-Help fonctionne automatiquement :
Get-Help Get-RapportSysteme -Full
```

---

## Cas pratiques

### Cas pratique 1 — Journaliser et accueillir

```powershell
$logPath = Join-Path $HOME "connexions.log"
$utilisateur = $env:USERNAME
$machine = $env:COMPUTERNAME
$dateHeure = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Write-Host "Bienvenue, $utilisateur !" -ForegroundColor Green
Add-Content -Path $logPath -Value "[$dateHeure] Connexion de $utilisateur sur $machine" -Encoding UTF8
Write-Output "Connexion enregistrée dans $logPath"
```

### Cas pratique 2 — Inventaire système

```powershell
param(
    [string]$Sortie = "inventaire.csv"
)

$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$disques = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"

$rapport = [PSCustomObject]@{
    Machine       = $cs.Name
    OS            = $os.Caption
    Version       = $os.Version
    RAM_Go        = [math]::Round($cs.TotalPhysicalMemory / 1GB, 1)
    Uptime_Jours  = [math]::Round(((Get-Date) - $os.LastBootUpTime).TotalDays, 1)
    Disque_C_Go   = [math]::Round(($disques | Where-Object DeviceID -eq "C:").Size / 1GB)
    Libre_C_Go    = [math]::Round(($disques | Where-Object DeviceID -eq "C:").FreeSpace / 1GB)
}

$rapport | Export-Csv -Path $Sortie -NoTypeInformation -Encoding UTF8
$rapport | Format-List
Write-Output "Rapport exporté dans $Sortie"
```

### Cas pratique 3 — Surveillance des connexions échouées

```powershell
param(
    [int]$Heures = 24,
    [int]$Seuil = 5
)

$debut = (Get-Date).AddHours(-$Heures)

try {
    $echecs = Get-WinEvent -FilterHashtable @{
        LogName   = "Security"
        Id        = 4625
        StartTime = $debut
    } -ErrorAction Stop
    
    Write-Output "Tentatives de connexion échouées (dernières $Heures heures) : $($echecs.Count)"
    
    if ($echecs.Count -ge $Seuil) {
        Write-Warning "ALERTE : $($echecs.Count) échecs de connexion détectés (seuil : $Seuil)"
    }
    
    $echecs | Select-Object TimeCreated, @{N="Compte";E={$_.Properties[5].Value}}, @{N="Source";E={$_.Properties[19].Value}} -First 10 | Format-Table

    # ⚠️ Note : les indices Properties[5] et Properties[19] correspondent aux champs
    # TargetUserName et IpAddress pour l'Event ID 4625 spécifiquement.
    # Les indices varient selon le type d'événement — vérifie toujours avec
    # $echecs[0].Properties pour voir les champs disponibles et leur position.
}
catch {
    Write-Warning "Impossible de lire les logs Security (droits admin nécessaires ?)"
}
```

### Cas pratique 4 — Renommer des fichiers en masse

```powershell
param(
    [Parameter(Mandatory)]
    [string]$Dossier,
    
    [string]$Ancien = ".jpeg",
    [string]$Nouveau = ".jpg"
)

$fichiers = Get-ChildItem -Path $Dossier -Filter "*$Ancien"
$compteur = 0

foreach ($f in $fichiers) {
    $nouveauNom = $f.Name.Replace($Ancien, $Nouveau)
    Rename-Item -Path $f.FullName -NewName $nouveauNom
    Write-Output "Renommé : $($f.Name) → $nouveauNom"
    $compteur++
}

Write-Output "Total : $compteur fichier(s) renommé(s)."
```

### Script modèle réutilisable

```powershell
<#
.SYNOPSIS
    [Description courte du script]
.DESCRIPTION
    [Description détaillée]
.PARAMETER Param1
    [Description du paramètre]
.EXAMPLE
    .\mon_script.ps1 -Param1 "valeur"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$Param1,
    
    [string]$Param2 = "defaut",
    
    [switch]$Force
)

# --- Fonctions ---
function Write-Log {
    param([string]$Message)
    $horodatage = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Verbose "[$horodatage] $Message"
}

# --- Programme principal ---
Write-Log "Début du script"

try {
    # ... ton code ici ...
    Write-Log "Traitement de $Param1"
}
catch {
    Write-Error "Erreur : $($_.Exception.Message)"
    exit 1
}

Write-Log "Fin du script"
```

## Exercices

**Guidé :** Crée un script qui liste tous les services arrêtés, les exporte en CSV, et affiche un résumé.

**Autonome :** Crée un script "boîte à outils" avec un menu (`switch` + boucle `do...while`) : 1) Info système, 2) Services en cours, 3) Derniers événements Security, 4) Espace disque, 5) Quitter.

**Défi :** Crée un script qui surveille les Event ID 4625 (échecs de connexion) toutes les 5 minutes en boucle et affiche une alerte si le nombre dépasse un seuil.

## ✅ Tu sais maintenant...

- Lire et comprendre les messages d'erreur PowerShell
- Gérer les erreurs avec `try/catch` (et `-ErrorAction Stop`)
- Les niveaux d'erreur (`Continue`, `Stop`, `SilentlyContinue`)
- Les messages de diagnostic (`Write-Verbose`, `Write-Warning`)
- `Set-StrictMode` pour attraper les erreurs sournoises
- L'aide basée sur les commentaires (`<# .SYNOPSIS ... #>`)
- Combiner toutes les notions dans des scripts concrets d'administration

---

# Conclusion

**Ce qui fait la force de PowerShell :**
- Le **pipeline d'objets** — manipuler des données structurées sans parser du texte
- La **convention Verb-Noun** — prédictible, découvrable
- L'**administration native** — processus, services, registre, logs, AD, remoting
- Le `param()` — les paramètres nommés, typés, validés, auto-complétés

**Pour continuer à progresser :**

- Écris des scripts pour tes tâches d'administration quotidiennes
- Explore les modules : `ActiveDirectory`, `NetSecurity` (pare-feu), `Defender`
- `Get-Command`, `Get-Help`, `Get-Member` — les 3 commandes pour tout découvrir
- La documentation officielle : [learn.microsoft.com/powershell](https://learn.microsoft.com/powershell)
- Explore PowerShell Gallery pour les modules communautaires

**Le trio complet :**
Avec Bash (Linux), Python (multiplateforme) et PowerShell (Windows), tu couvres l'intégralité des environnements d'un profil cyber/infra moderne.

Bon scripting !
