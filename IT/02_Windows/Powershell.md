# PowerShell pour l'administration Windows

## De zéro à l'automatisation, l'Active Directory et la cybersécurité — Guide pour débutant absolu

---

> **Prérequis :** Aucun en PowerShell ni en programmation. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une ligne de script.
> Il t'apprend PowerShell **en administrant Windows** : chaque notion du langage est introduite à travers un vrai cas d'administration.

---

## Ce que ce cours est — et ce qu'il n'est pas

Ce cours t'apprend à **piloter et automatiser un environnement Windows avec PowerShell**, du poste local jusqu'à l'Active Directory, les GPO, l'administration distante et les API.

L'idée directrice tient en une phrase :

> **On n'apprend pas PowerShell puis l'administration. On apprend PowerShell EN administrant.**

À la fin, tu ne diras pas seulement « je sais écrire quelques scripts ». Tu diras : « je comprends PowerShell et son pipeline objet ; je sais administrer un poste ou un serveur Windows — services, processus, fichiers, permissions, utilisateurs, tâches, registre, réseau ; automatiser Active Directory ; comprendre et manipuler des GPO ; administrer plusieurs machines à distance ; interroger une API REST et Microsoft Graph ; produire des scripts robustes ; et utiliser tout ça comme base pour le diagnostic et la cybersécurité Windows. »

Ce cours **n'est pas** :

- un cours complet d'Active Directory, de Windows Server, de réseau ou de GPO (ce sont des cours à part entière ; ici, **PowerShell reste le fil rouge** et on apprend à *piloter* ces technologies)
- un cours de développement .NET
- un cours de cybersécurité offensive (la partie sécurité est **défensive** : diagnostic, triage, durcissement)

Le niveau final visé est **junior solide / intermédiaire débutant** en administration Windows PowerShell — pas expert Microsoft. Le cours te donne les fondations pour approfondir ensuite séparément AD, Windows Server, Entra ID, la cybersécurité Windows, etc.

---

## Guide de lecture

Chaque chapitre est organisé en trois niveaux. Tu peux suivre le parcours principal (🟢 + 🟡) et revenir aux 🔴 plus tard.

| Section | Niveau | Objectif |
|---------|--------|----------|
| **🟢 Le minimum à savoir** | Essentiel | Ce qu'il faut absolument comprendre |
| **🟡 Très utile en pratique** | Opérationnel | Ce qui te rend efficace en administration réelle |
| **🔴 Bonus / avancé** | Approfondissement | À connaître, mais tu peux y revenir plus tard |

Deux **réflexes** sont martelés dans tout le cours — ce sont les meilleures habitudes qu'un débutant puisse prendre :

> **Réflexe n°1 — Explorer avec `Get-Member`.** Chaque fois que tu récupères un objet que tu ne connais pas, passe-le dans `Get-Member` pour voir ses propriétés et méthodes. Tu ne mémorises pas PowerShell : tu l'explores.

> **Réflexe n°2 — `Get`/`Test` avant `Set`/`New`/`Remove`.** On regarde toujours avant de modifier. On lit l'état actuel, on teste, *puis* on change — et plus tard, on utilise `-WhatIf`, `-Confirm` et des sauvegardes. C'est la discipline de base de l'administrateur.

### Parcours recommandés

| Parcours | Chapitres | Objectif |
|----------|-----------|----------|
| **🎯 Fondamentaux & poste local** | Parties I-II (Ch.1-14) | Être autonome sur un poste Windows, comprendre PowerShell |
| **🔧 Administrateur Windows** | Parties I-VI (Ch.1-31) | Administrer postes, serveurs, réseau, AD, GPO, à distance |
| **🚀 Complet** | Tout | + industrialisation et cybersécurité |

---

## Environnement de lab recommandé

PowerShell fonctionne partout, mais **toutes les cmdlets ne sont pas disponibles partout**. Voici ce dont tu as besoin selon la partie du cours.

| Parties | Ce que tu administres | Environnement suffisant |
|---------|----------------------|------------------------|
| **I → III** (Ch.1-18) | Poste local, réseau du poste | **Windows 10 ou 11** (ce que tu as déjà) |
| **IV → V** (Ch.19-28) | Active Directory, GPO, DNS/DHCP/SMB serveur | **Une VM Windows Server** (contrôleur de domaine) |
| **VI** (Ch.29-34) | Machines distantes, API | Idéalement 2 machines (un client + un serveur) |

**Le lab idéal (facultatif mais recommandé pour les parties IV+) :** trois machines virtuelles sur ton PC (avec VirtualBox, VMware Workstation, ou Hyper-V) :

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    DC01     │     │    SRV01    │     │  CLIENT01   │
│ Windows Srv │     │ Windows Srv │     │ Windows 10  │
│ Contrôleur  │     │ Serveur     │     │ Poste       │
│ de domaine  │     │ membre      │     │ client      │
│ AD/DNS/DHCP │     │ Fichiers    │     │ RSAT        │
└─────────────┘     └─────────────┘     └─────────────┘
        └──────── domaine lab.local ────────┘
```

> **Important :** ce cours n'est **pas** un tutoriel d'installation de lab (monter un domaine AD est un sujet à part entière). Mais garde en tête cette distinction : si tu tapes `Get-ADUser` sur ton Windows 11 personnel sans domaine ni RSAT, ça ne marchera pas — et c'est normal. Chaque chapitre te signale l'environnement et les droits nécessaires.

**Windows PowerShell 5.1 vs PowerShell 7 :** les deux coexistent (on détaille au Ch.1). Pour la majorité de ce cours, la version intégrée à Windows (5.1) suffit. Les rares points spécifiques à PowerShell 7 sont signalés par le marqueur `[⚡ PS7+]`. Les opérations nécessitant des droits administrateur sont signalées par `[🔑 Admin]`, et celles spécifiques à Windows Server par `[🖥️ Server]`.

---

## Comment lire une commande PowerShell

Pour chaque cmdlet importante, ce cours répond systématiquement à ces questions — c'est le canevas mental à adopter :

1. **Que fait-elle ?** (son rôle)
2. **Que retourne-t-elle ?** (rien à l'écran ≠ rien du tout — souvent un objet)
3. **Quel type d'objet ?** (pour savoir quoi en faire ensuite — d'où le réflexe `Get-Member`)
4. **Quelles propriétés sont utiles ?**
5. **Pourquoi un admin l'utilise ?**
6. **Quand l'éviter ?**
7. **Quels droits / quelle version / client ou serveur ?**

---

## Glossaire — Les mots à connaître

Reviens ici dès qu'un terme te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **PowerShell** | Le shell moderne de Microsoft : terminal + langage de scripting + outil d'administration Windows |
| **Cmdlet** | Une commande PowerShell native, nommée `Verbe-Nom` (`Get-Service`, `New-ADUser`) |
| **Objet** | Une donnée structurée avec des **propriétés** (informations) et des **méthodes** (actions) |
| **Propriété** | Une information portée par un objet (le nom d'un service, son statut…) |
| **Méthode** | Une action qu'un objet sait faire (`.Stop()` sur un service) |
| **Pipeline** | Le `\|` qui envoie la sortie d'une commande dans la suivante — en PowerShell, ce sont des **objets** qui circulent, pas du texte |
| **Module** | Un ensemble de cmdlets regroupées (module `ActiveDirectory`, `DnsServer`…) |
| **Cmdlet vs commande externe** | Une cmdlet est native PowerShell ; `ping.exe` ou `ipconfig.exe` sont des exécutables externes appelables depuis PowerShell |
| **Variable** | Un conteneur nommé, préfixé par `$` (`$Service`, `$env:COMPUTERNAME`) |
| **Hashtable** | Une collection de paires clé-valeur (`@{ Nom = "SRV01" }`) — comme un dictionnaire Python |
| **PSCustomObject** | Un objet sur mesure que tu fabriques pour structurer des données (idéal pour les rapports) |
| **Script** | Un fichier `.ps1` contenant des commandes PowerShell |
| **Fonction** | Un bloc de code nommé et réutilisable, souvent lui aussi en `Verbe-Nom` |
| **Registre** | La base de données de configuration de Windows |
| **Service** | Un programme qui tourne en arrière-plan (pare-feu, spouleur d'impression…) |
| **Remoting** | L'exécution de commandes PowerShell sur des machines distantes (via WinRM) |
| **WinRM** | Windows Remote Management — le service qui permet le remoting |
| **AD (Active Directory)** | L'annuaire central d'un réseau Windows d'entreprise (utilisateurs, ordinateurs, groupes…) |
| **GPO (Group Policy Object)** | Un objet de stratégie qui applique des réglages à des utilisateurs/ordinateurs |
| **RSAT** | Remote Server Administration Tools — les modules qui ajoutent `Get-ADUser`, `Get-GPO`… sur un poste client |
| **API REST** | Une interface web qui permet à des programmes de dialoguer via HTTP (GET, POST…) et JSON |
| **CIM/WMI** | La couche d'instrumentation de Windows qui expose des centaines de classes d'infos système (`Get-CimInstance`) |

---

## Table des matières

**PARTIE I — FONDAMENTAUX POWERSHELL POUR ADMINISTRER WINDOWS**

1. [PowerShell dans l'écosystème Windows](#chapitre-1--powershell-dans-lécosystème-windows)
2. [Variables, types et informations système](#chapitre-2--variables-types-et-informations-système)
3. [Paramètres et scripts administrables](#chapitre-3--paramètres-et-scripts-administrables)
4. [Le pipeline et les objets : le concept fondamental](#chapitre-4--le-pipeline-et-les-objets)
5. [Opérateurs et conditions](#chapitre-5--opérateurs-et-conditions)
6. [Collections, hashtables et boucles](#chapitre-6--collections-hashtables-et-boucles)
7. [Fonctions et scripts structurés](#chapitre-7--fonctions-et-scripts-structurés)
8. [Gestion des erreurs et débogage](#chapitre-8--gestion-des-erreurs-et-débogage)

**PARTIE II — ADMINISTRATION WINDOWS LOCALE**

9. [Fichiers, dossiers et permissions NTFS](#chapitre-9--fichiers-dossiers-et-permissions-ntfs)
10. [Utilisateurs et groupes locaux](#chapitre-10--utilisateurs-et-groupes-locaux)
11. [Processus et services](#chapitre-11--processus-et-services)
12. [Le registre Windows](#chapitre-12--le-registre-windows)
13. [Tâches planifiées](#chapitre-13--tâches-planifiées)
14. [Disques, volumes et stockage](#chapitre-14--disques-volumes-et-stockage) · [Rôles, fonctionnalités et logiciels](#rôles-fonctionnalités-et-logiciels)

**PARTIE III — ADMINISTRATION RÉSEAU WINDOWS**

15. [Interfaces et configuration IP](#chapitre-15--interfaces-et-configuration-ip)
16. [DNS client et résolution](#chapitre-16--dns-client-et-résolution)
17. [Routage et connexions](#chapitre-17--routage-et-connexions)
18. [Pare-feu Windows](#chapitre-18--pare-feu-windows)

**PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY**

19. [Comprendre Active Directory](#chapitre-19--comprendre-active-directory)
20. [Utilisateurs AD](#chapitre-20--utilisateurs-ad)
21. [Groupes AD](#chapitre-21--groupes-ad)
22. [Ordinateurs et unités d'organisation](#chapitre-22--ordinateurs-et-unités-dorganisation)
23. [Recherche et filtrage AD](#chapitre-23--recherche-et-filtrage-ad)
24. [Administration en masse avec CSV](#chapitre-24--administration-en-masse-avec-csv)

**PARTIE V — GPO ET SERVICES WINDOWS SERVER**

25. [Group Policy (GPO)](#chapitre-25--group-policy-gpo)
26. [DNS Server](#chapitre-26--dns-server)
27. [DHCP Server](#chapitre-27--dhcp-server)
28. [File Server et partages SMB](#chapitre-28--file-server-et-partages-smb)

**PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION**

29. [PowerShell Remoting](#chapitre-29--powershell-remoting)
30. [Authentification, autorisation et tokens](#chapitre-30--authentification-autorisation-et-tokens)
31. [API REST avec PowerShell](#chapitre-31--api-rest-avec-powershell)
32. [Microsoft Graph et Entra ID](#chapitre-32--microsoft-graph-et-entra-id)

**PARTIE VII — AUTOMATISATION ET INDUSTRIALISATION**

33. [Industrialiser ses scripts](#chapitre-33--industrialiser-ses-scripts)

**PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ**

34. [Diagnostic, logs et triage](#chapitre-34--diagnostic-logs-et-triage)
35. [Sécurité de l'exécution et durcissement](#chapitre-35--sécurité-de-lexécution-et-durcissement)

**ANNEXES**

---

# PARTIE I — FONDAMENTAUX POWERSHELL POUR ADMINISTRER WINDOWS

Cette partie pose les fondations du langage. Mais dès le premier chapitre, on manipule de vraies commandes d'administration Windows : l'idée n'est pas d'apprendre des concepts abstraits, c'est d'apprendre PowerShell **en regardant ce qui se passe sur une vraie machine**.

---

# Chapitre 1 — PowerShell dans l'écosystème Windows

## 🟢 Le minimum à savoir

### Qu'est-ce que PowerShell ?

PowerShell est **trois choses à la fois** :

1. **Un terminal (un shell)** — tu tapes des commandes, il les exécute
2. **Un langage de scripting** — tu écris des scripts pour automatiser
3. **Un outil d'administration Windows** — tu pilotes services, processus, utilisateurs, registre, réseau, Active Directory…

C'est ce troisième point qui nous intéresse le plus. Tout ce que tu peux faire dans les interfaces graphiques de Windows (le Gestionnaire des tâches, les Services, l'Observateur d'événements, la console AD…), tu peux le faire en PowerShell — plus vite, de façon reproductible, et surtout **automatisable** et applicable à **des centaines de machines à la fois**.

### Un aperçu de ce qu'on va pouvoir faire

Avant même d'apprendre la syntaxe, tape ces commandes pour voir la puissance de l'outil. Ne cherche pas encore à tout comprendre — c'est une bande-annonce :

```powershell
Get-Service                     # Tous les services Windows et leur état
Get-Process                     # Tous les programmes en cours d'exécution
Get-ComputerInfo                # Une fiche complète de la machine
Get-CimInstance Win32_OperatingSystem   # Infos sur le système d'exploitation
Get-NetIPAddress                # Les adresses IP de la machine
```

Chacune de ces commandes t'a renvoyé des informations structurées. C'est le cœur de PowerShell, et on va apprendre à l'exploiter méthodiquement.

### La convention Verbe-Nom

Toutes les commandes PowerShell (les **cmdlets**) suivent le même pattern : **`Verbe-Nom`**.

| Verbe | Signification | Exemples d'administration |
|-------|--------------|--------------------------|
| `Get` | Obtenir, lire | `Get-Service`, `Get-Process`, `Get-ADUser` |
| `Set` | Modifier, configurer | `Set-Service`, `Set-ADUser` |
| `New` | Créer | `New-LocalUser`, `New-ADUser`, `New-Item` |
| `Remove` | Supprimer | `Remove-Item`, `Remove-ADUser` |
| `Start` / `Stop` | Démarrer / arrêter | `Start-Service`, `Stop-Process` |
| `Restart` | Redémarrer | `Restart-Service`, `Restart-Computer` |
| `Test` | Vérifier | `Test-Path`, `Test-Connection`, `Test-NetConnection` |
| `Enable` / `Disable` | Activer / désactiver | `Enable-ADAccount`, `Disable-LocalUser` |

C'est la grande force de PowerShell : la convention est **prédictible**. Tu ne connais pas la commande pour lister les services ? Essaie `Get-Service`. Pour en arrêter un ? `Stop-Service`. Pour changer sa configuration ? `Set-Service`. Ça marche presque toujours.

> **Comparaison avec Bash :** en Bash, les noms sont courts et souvent cryptiques (`ls`, `ps`, `grep`, `awk`). En PowerShell, ils sont longs mais explicites. C'est plus verbeux à taper, mais tu **devines** la commande au lieu de la mémoriser — un énorme avantage quand tu débutes.

> **La discipline `Get` d'abord :** remarque que la moitié des verbes ci-dessus ne font que **lire** (`Get`, `Test`). C'est voulu. En administration, on regarde toujours avant de modifier. On y reviendra sans cesse.

### Les 3 commandes pour tout découvrir

Ces trois cmdlets sont ta porte d'entrée vers tout le reste de PowerShell. Retiens-les avant tout :

```powershell
# 1. TROUVER une commande
Get-Command *Service*        # Toutes les cmdlets contenant "Service"
Get-Command -Verb Get        # Toutes les cmdlets qui commencent par "Get"
Get-Command -Noun ADUser     # Toutes les cmdlets qui agissent sur "ADUser"

# 2. COMPRENDRE une commande
Get-Help Get-Service                 # L'aide
Get-Help Get-Service -Examples       # Des exemples concrets (le plus utile !)
Get-Help Get-Service -Online         # L'aide complète dans le navigateur

# 3. EXPLORER ce qu'une commande retourne
Get-Service | Get-Member     # Les propriétés et méthodes d'un objet "service"
```

> **📌 Réflexe transversal — `Get-Member` :** `Get-Service | Get-Member` te montre **tout** ce que contient un objet service : ses propriétés (`Name`, `Status`, `StartType`…) et ses méthodes (`.Start()`, `.Stop()`…). Chaque fois que ce cours introduira un nouvel objet (un utilisateur AD, une tâche planifiée, une réponse d'API…), le réflexe sera le même : le passer dans `Get-Member` pour l'explorer. On ne mémorise pas PowerShell, on l'explore.

> **Première utilisation de l'aide :** PowerShell peut te proposer de télécharger les fichiers d'aide détaillés. Lance une fois `Update-Help -ErrorAction SilentlyContinue` (nécessite Internet et, selon la version, des droits admin). Sans ça, `Get-Help` reste minimal.

### Windows PowerShell 5.1 vs PowerShell 7

Il existe **deux** versions qui coexistent, et c'est important de le comprendre :

| | Windows PowerShell **5.1** | PowerShell **7+** |
|---|---|---|
| Exécutable | `powershell.exe` | `pwsh.exe` |
| Installé par défaut sur Windows ? | ✅ Oui | ❌ Non (à installer) |
| Multi-plateforme (Linux/Mac) ? | ❌ Non | ✅ Oui |
| Basé sur | .NET Framework | .NET (Core) |
| Modules AD, GPO, DNS Server… | ✅ Oui (via RSAT) | ✅ Oui (compatibilité) |

**Pour ce cours :** Windows PowerShell 5.1, déjà présent sur ton Windows, suffit pour la quasi-totalité du contenu. C'est aussi souvent la seule version disponible sur les serveurs en production. Les points spécifiques à PowerShell 7 sont signalés `[⚡ PS7+]`.

> **Où télécharger PowerShell 7 :** sur le dépôt officiel [github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell). Utile surtout si tu veux les nouveautés du langage ou travailler aussi sous Linux/Mac.

### PowerShell vs CMD

Windows a un autre shell historique, **CMD** (l'Invite de commandes). Ce sont deux outils différents :

- **CMD** manipule du **texte brut** et a un jeu de commandes limité (`dir`, `copy`, `ipconfig`…)
- **PowerShell** manipule des **objets** et a des milliers de cmdlets structurées

Beaucoup de commandes CMD et d'exécutables classiques (`ipconfig`, `ping`, `whoami`) fonctionnent aussi depuis PowerShell — mais l'inverse est faux : les cmdlets PowerShell ne fonctionnent pas dans CMD.

### Ouvrir PowerShell (et en administrateur)

- Menu Démarrer → tape "PowerShell" → **Windows PowerShell**
- Pour les opérations d'administration : **clic droit → Exécuter en tant qu'administrateur**
- Recommandé : **Windows Terminal** (depuis le Microsoft Store), qui regroupe PowerShell, CMD et WSL dans une fenêtre à onglets

> **🔑 Quand faut-il être administrateur ?** Lire est souvent possible sans privilèges (`Get-Service`, `Get-Process`). **Modifier** le système (arrêter un service, écrire dans `HKLM:`, lire le journal Security) nécessite en général une console élevée. Chaque fois que c'est le cas, ce cours l'indique avec `[🔑 Admin]`. Pour vérifier rapidement si ta console est élevée, une astuce : `net session` renvoie une erreur "Accès refusé" si tu n'es **pas** administrateur.

### Ton premier script

Crée un dossier de travail et un fichier `poste.ps1` :

```powershell
# poste.ps1 — Premières infos sur la machine
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Date        : $(Get-Date)"
```

Pour le lancer :

```powershell
.\poste.ps1
```

Le `.\` devant le nom dit à PowerShell « exécute le script du dossier courant » (comme `./` en Bash). C'est une mesure de sécurité : PowerShell ne lance pas un script juste parce qu'on tape son nom.

Tu obtiens probablement une **erreur rouge** parlant de politique d'exécution. C'est le prochain point.

### La politique d'exécution (Execution Policy)

Par défaut, Windows bloque l'exécution des scripts `.ps1`. Pour l'autoriser :

```powershell
# Voir la politique actuelle
Get-ExecutionPolicy

# Autoriser les scripts locaux pour ton compte utilisateur
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

| Politique | Effet |
|-----------|-------|
| `Restricted` | Aucun script ne s'exécute (défaut sur les clients Windows) |
| `RemoteSigned` | Les scripts locaux fonctionnent ; ceux téléchargés doivent être signés |
| `Unrestricted` / `Bypass` | Tout passe (à éviter) |

> **⚠️ Point technique important — l'Execution Policy n'est PAS une barrière de sécurité.** C'est un **garde-fou anti-erreur**, pas une protection contre un attaquant. Elle empêche un double-clic accidentel de lancer un script, mais elle se contourne trivialement — par exemple `powershell -ExecutionPolicy Bypass -File script.ps1`, ou en copiant-collant le contenu du script dans la console. Ne compte jamais dessus pour te protéger d'un code malveillant. Les vraies protections d'exécution (contrôle applicatif App Control/WDAC ou AppLocker, qui déclenche le Constrained Language Mode, et signature de code) sont vues en Partie VIII. Retiens : `RemoteSigned` en `CurrentUser` est le bon réglage **de confort** pour apprendre. En entreprise, cette politique est généralement imposée par GPO.

### Les commentaires

```powershell
# Commentaire sur une ligne

<#
Commentaire
sur plusieurs lignes
#>

Write-Output "Ceci s'affiche"   # Commentaire en fin de ligne
```

## 🟡 Très utile en pratique

### Les alias : passerelle avec Bash et CMD

PowerShell fournit des raccourcis (**alias**) pour les commandes courantes :

| Tu tapes | PowerShell exécute | Équivalent Bash |
|----------|-------------------|-----------------|
| `ls` / `dir` | `Get-ChildItem` | `ls` |
| `cd` | `Set-Location` | `cd` |
| `cat` / `type` | `Get-Content` | `cat` |
| `cp` | `Copy-Item` | `cp` |
| `rm` / `del` | `Remove-Item` | `rm` |
| `cls` | `Clear-Host` | `clear` |

Pratiques pour taper vite dans la console. **Mais dans un script, utilise toujours les noms complets** (`Get-ChildItem` plutôt que `ls`) : c'est plus lisible et portable.

> **Attention :** ces alias appellent des cmdlets PowerShell, pas les vraies commandes Linux. `ls -la` ne fonctionne pas ; l'équivalent est `Get-ChildItem -Force`.

### Un éditeur : VS Code

Pour écrire des scripts confortablement, installe **Visual Studio Code** avec l'extension **PowerShell** (gratuit, multi-plateforme). Il offre coloration, autocomplétion et débogage. L'ancien **PowerShell ISE** (intégré à Windows) fonctionne aussi mais n'est plus développé.

### La tab-complétion

Tape le début d'une cmdlet et appuie sur `Tab` : PowerShell complète. Ça marche aussi sur les paramètres (`Get-Service -N` + Tab → `-Name`). Indispensable et anti-fautes de frappe.

## 🔴 Bonus

### Le profil PowerShell

Le profil est un script qui s'exécute à chaque ouverture de PowerShell (comme le `.bashrc` de Bash). Utile pour définir des raccourcis ou des fonctions perso :

```powershell
$PROFILE            # Le chemin de ton profil
notepad $PROFILE    # L'éditer
```

### PowerShell Gallery

Le dépôt public de modules ([powershellgallery.com](https://www.powershellgallery.com/)), équivalent de PyPI ou npm :

```powershell
Install-Module -Name <NomDuModule> -Scope CurrentUser
```

## ❌ Erreur classique

```powershell
# Croire que l'Execution Policy sécurise le système
# → NON : c'est un garde-fou anti-erreur, contournable trivialement

# Oublier le .\ devant un script
poste.ps1        # ❌ "terme non reconnu"
.\poste.ps1      # ✅

# Utiliser les options Linux avec les alias
ls -la           # ❌
Get-ChildItem -Force   # ✅

# Confondre PowerShell et CMD
# Les cmdlets (Get-Service…) ne fonctionnent PAS dans CMD
```

## 💡 Exercices

**Guidé :** Ouvre PowerShell, lance `Get-Command -Verb Get | Measure-Object` pour compter combien de cmdlets `Get-*` existent sur ta machine. Puis `Get-Command -Noun Service` pour voir toutes les commandes liées aux services.

**Autonome :** Utilise `Get-Help` pour trouver comment lister uniquement les services *arrêtés* avec `Get-Service`. (Indice : `Get-Help Get-Service -Examples`.)

## ✅ Tu sais maintenant...

- Ce qu'est PowerShell (shell + langage + outil d'administration)
- La convention `Verbe-Nom` et pourquoi elle rend PowerShell prédictible
- Le trio `Get-Command` / `Get-Help` / `Get-Member` pour tout découvrir
- Le réflexe `Get-Member` pour explorer n'importe quel objet
- La différence 5.1 vs 7, PowerShell vs CMD
- Exécuter un script et régler l'Execution Policy — **en sachant qu'elle n'est pas une sécurité**

## 💬 Questions d'entretien typiques

- **Qu'est-ce qu'une cmdlet ?** → Une commande native PowerShell nommée `Verbe-Nom`, qui retourne des objets (pas du texte).
- **Comment découvrir une commande inconnue ?** → `Get-Command` pour la trouver, `Get-Help -Examples` pour l'utiliser, `Get-Member` pour explorer ce qu'elle retourne.
- **L'Execution Policy protège-t-elle des malwares ?** → Non. C'est un garde-fou anti-exécution accidentelle, contournable trivialement (`-ExecutionPolicy Bypass`, copier-coller…). Les vraies protections sont le contrôle applicatif (App Control/WDAC ou AppLocker) qui déclenche le Constrained Language Mode, plus la signature.
- **Différence Windows PowerShell 5.1 / PowerShell 7 ?** → 5.1 est intégré à Windows, basé sur .NET Framework, Windows uniquement. 7 est à installer, basé sur .NET, multi-plateforme.

---

# Chapitre 2 — Variables, types et informations système

## 🟢 Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable est un **conteneur nommé**. En PowerShell, le nom commence **toujours** par `$` — à la création comme à l'utilisation :

```powershell
$Prenom = "Alice"
$Age = 25
$EstAdmin = $true
```

> **Comparaison :** en Bash, `$` seulement à l'utilisation (`prenom="Alice"` puis `echo $prenom`). En Python, jamais de `$`. En PowerShell, **toujours** `$`.

Les petits exemples abstraits comme ci-dessus servent à poser une première idée. Mais on va vite les relier à Windows — c'est là que PowerShell devient concret :

```powershell
$Utilisateur = $env:USERNAME
$Machine     = $env:COMPUTERNAME
$OS          = Get-CimInstance Win32_OperatingSystem

Write-Output "Connecté en tant que $Utilisateur sur $Machine"
Write-Output "Système : $($OS.Caption)"
```

Ici, `$OS` ne contient pas un simple texte : c'est un **objet** riche décrivant le système, dont on lira les propriétés (`.Caption`, `.Version`, `.LastBootUpTime`…). On explore comment au Ch.4.

### Les types de données

PowerShell détecte le type automatiquement, mais tu peux le forcer :

| Type | Notation | Exemple |
|------|----------|---------|
| Texte | `[string]` | `"SRV01"` |
| Entier | `[int]` | `25` |
| Décimal | `[double]` | `1.75` |
| Booléen | `[bool]` | `$true`, `$false` |
| Date | `[datetime]` | `Get-Date` |

```powershell
# Vérifier le type d'une variable
$Machine.GetType().Name          # String
(Get-Date).GetType().Name        # DateTime

# Forcer une conversion
[int]$Nombre = "42"              # le texte "42" devient l'entier 42
```

Forcer le type est utile en administration : quand tu attends un nombre de jours, un seuil d'espace disque, etc., tu veux un `[int]`, pas du texte.

### Afficher : `Write-Output` vs `Write-Host`

```powershell
Write-Output "Bonjour"    # Envoie dans le pipeline (capturable, redirigeable)
Write-Host   "Bonjour"    # Écrit directement à l'écran
```

La différence concrète :

```powershell
$r = Write-Output "Hello"
$r                         # → "Hello" (capturé)

$r = Write-Host "Hello"    # "Hello" s'affiche, mais...
$r                         # → (vide, rien n'a été capturé)
```

> **Règle :** dans un script, produis tes **données** avec `Write-Output` (ou simplement en laissant l'objet « tomber » dans le pipeline). Réserve `Write-Host` aux **messages destinés à l'humain** (état, couleurs) — jamais aux données que tu voudras réutiliser.

> **Note version :** longtemps, `Write-Host` a eu mauvaise réputation car son texte « disparaissait » (impossible à capturer/rediriger). Depuis PowerShell 5+, `Write-Host` écrit en réalité dans un flux dédié (*Information stream*) et peut être capturé via `6>`. En pratique la règle ne change pas : **données → `Write-Output`, messages → `Write-Host`**.

### L'interpolation de chaînes

Guillemets **doubles** → les variables sont interprétées. Guillemets **simples** → texte littéral.

```powershell
$Machine = "SRV01"
Write-Output "Serveur : $Machine"     # → Serveur : SRV01
Write-Output 'Serveur : $Machine'     # → Serveur : $Machine
```

Pour insérer une **propriété** ou une **expression**, encadre avec `$(...)` :

```powershell
Write-Output "OS : $($OS.Caption)"
Write-Output "Uptime calculé le $(Get-Date)"
```

> **Piège classique :** `"$OS.Caption"` affiche l'objet suivi du texte `.Caption` — pas ce que tu veux. Il faut `"$($OS.Caption)"`. Retiens : dès qu'il y a un point (une propriété) ou un calcul, encadre avec `$(...)`.

### Saisie utilisateur avec `Read-Host`

```powershell
$NomServeur = Read-Host "Nom du serveur à vérifier"
Write-Output "Vérification de $NomServeur..."
```

Par défaut, `Read-Host` renvoie **du texte** (une chaîne). Si tu attends un nombre, convertis :

```powershell
[int]$Seuil = Read-Host "Seuil d'espace disque libre (Go)"
```

> **Une exception au « texte » :** avec l'option `-AsSecureString`, `Read-Host` masque la saisie et renvoie un **`SecureString`**, pas une chaîne. C'est la façon correcte de demander un mot de passe — on la retrouvera aux Ch.10, 20 et 33.

> **Bonne pratique d'admin :** `Read-Host` rend un script **interactif**, donc **non automatisable**. Pour un vrai script d'administration, on préfère les **paramètres** (Ch.3), qui permettent de lancer le script sans intervention humaine. On garde `Read-Host` pour les confirmations ponctuelles.

### Les variables automatiques utiles

```powershell
$true / $false / $null       # Booléens et absence de valeur
$HOME                        # Dossier personnel
$PWD                         # Dossier courant
$PSVersionTable              # Version de PowerShell (.PSVersion)
$env:USERNAME                # Utilisateur courant
$env:COMPUTERNAME            # Nom de la machine
$env:USERPROFILE             # Profil utilisateur
$?                           # La dernière commande a-t-elle réussi ? (True/False)
$LASTEXITCODE                # Code de sortie du dernier programme externe
```

Les variables `$env:` exposent les **variables d'environnement** Windows — équivalent de `$USER`, `$HOME` en Bash. On y accède aussi via le PSDrive `Env:` (`Get-ChildItem Env:`), qu'on verra au Ch.12.

## 🟡 Très utile en pratique

### `Write-Host` en couleurs (pour les messages d'état)

```powershell
Write-Host "Service actif"   -ForegroundColor Green
Write-Host "Service arrêté"  -ForegroundColor Red
Write-Host "Attention"       -ForegroundColor Yellow
```

Idéal pour un rapport lisible à l'écran — mais rappelle-toi : ce sont des messages, pas des données.

### Interroger le système avec `Get-CimInstance`

`Get-CimInstance` est **la** porte d'entrée vers les informations système (via la couche CIM/WMI de Windows). Il renvoie des objets riches :

```powershell
# Système d'exploitation
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, LastBootUpTime

# Matériel
Get-CimInstance Win32_ComputerSystem |
    Select-Object Manufacturer, Model, TotalPhysicalMemory

# Calculer l'uptime (depuis le dernier démarrage)
$os = Get-CimInstance Win32_OperatingSystem
(Get-Date) - $os.LastBootUpTime
```

> **📌 Réflexe `Get-Member` :** tu ne sais pas quelles propriétés existent ? `Get-CimInstance Win32_OperatingSystem | Get-Member` te les liste toutes. C'est **toujours** la bonne première étape face à un objet inconnu.

> **Note version :** `Get-CimInstance` (moderne) remplace l'ancien `Get-WmiObject`. **`Get-WmiObject` n'existe plus du tout dans PowerShell 7** — utilise `Get-CimInstance` partout, il fonctionne en 5.1 comme en 7.

## 🔴 Bonus

### Les méthodes .NET

Chaque objet PowerShell est un objet .NET. Tu peux appeler des méthodes .NET directement :

```powershell
[math]::Round(3.14159, 2)               # 3.14
[math]::Round($os.FreePhysicalMemory/1MB, 2)
[System.Environment]::OSVersion         # Version de l'OS
```

Pas indispensable pour débuter, mais c'est ce qui donne à PowerShell sa profondeur.

## ❌ Erreur classique

```powershell
# Oublier le $
Machine = "SRV01"        # ❌
$Machine = "SRV01"       # ✅

# Interpoler une propriété sans $()
"OS : $OS.Caption"       # ❌ affiche l'objet puis ".Caption"
"OS : $($OS.Caption)"    # ✅

# Oublier de convertir une saisie numérique
$Seuil = Read-Host "Seuil"
$Seuil + 1               # ❌ concaténation de texte ("101" au lieu de 11)
[int]$Seuil = Read-Host "Seuil"   # ✅
```

## 💡 Exercices

**Guidé :** Crée `fiche.ps1` qui stocke `$env:COMPUTERNAME`, `$env:USERNAME` et `Get-Date` dans des variables, puis les affiche proprement.

**Autonome :** Récupère l'objet `Get-CimInstance Win32_OperatingSystem` dans une variable `$os` et affiche sa version (`.Version`) et sa date de dernier démarrage (`.LastBootUpTime`) via l'interpolation `$(...)`.

## 🧩 Mini-projet — Fiche d'identité du poste

Crée `Get-PosteInfo.ps1` qui affiche une fiche claire :

```
=== Fiche du poste ===
Machine     : <COMPUTERNAME>
Utilisateur : <USERNAME>
OS          : <Caption> <Version>
RAM totale  : <Go>
PowerShell  : <version>
Démarré le  : <LastBootUpTime>
```

Utilise `$env:`, `Get-CimInstance Win32_OperatingSystem` et `Win32_ComputerSystem`, `$PSVersionTable.PSVersion`, l'interpolation `$(...)` et `Write-Host` en couleurs pour le titre. (On étoffera cette fiche au fil du cours — disque au Ch.14, IP au Ch.15.)

## ✅ Tu sais maintenant...

- Créer une variable avec `$`, forcer un type
- La différence `Write-Output` (données) / `Write-Host` (messages)
- L'interpolation, et le piège `$($objet.Propriété)`
- Lire une saisie avec `Read-Host` — et pourquoi les paramètres sont préférables
- Les variables automatiques (`$env:`, `$?`, `$LASTEXITCODE`…)
- Interroger le système avec `Get-CimInstance` (et que `Get-WmiObject` est mort en PS7)

## 💬 Questions d'entretien typiques

- **`Write-Output` ou `Write-Host` pour un résultat réutilisable ?** → `Write-Output` : il va dans le pipeline et peut être capturé. `Write-Host` sert aux messages destinés à l'humain.
- **Comment récupérer la version de l'OS d'une machine ?** → `Get-CimInstance Win32_OperatingSystem` puis lire `.Caption` / `.Version`. `Get-WmiObject` est l'ancêtre, absent de PowerShell 7.
- **Pourquoi préférer des paramètres à `Read-Host` ?** → Pour rendre le script automatisable (planifiable, appelable en masse) au lieu d'exiger une saisie humaine.

---

# Chapitre 3 — Paramètres et scripts administrables

## 🟢 Le minimum à savoir

### Le problème : rendre un script réutilisable

Un script qui ne fait qu'une chose figée a peu de valeur. Un bon script d'administration prend des **paramètres** : le nom du serveur à vérifier, le service à redémarrer, le seuil d'alerte… C'est ce qui le rend réutilisable et **automatisable**.

### La méthode simple : `$args`

`$args` est un tableau contenant les arguments passés au script :

```powershell
# verifier.ps1
Write-Output "Service demandé : $($args[0])"
```

```powershell
.\verifier.ps1 Spooler       # → Service demandé : Spooler
```

C'est rudimentaire : pas de noms, pas de types, pas de valeurs par défaut. On s'en sert rarement dans un vrai script.

### La méthode recommandée : `param()`

`param()` déclare des paramètres **nommés, typés, validés**. C'est la façon professionnelle :

```powershell
# Get-ServiceStatus.ps1 — interroge le service SUR LA MACHINE LOCALE
param(
    [Parameter(Mandatory)]
    [string]$ServiceName,

    [switch]$IncludeStartType     # afficher aussi le type de démarrage
)

$svc = Get-Service -Name $ServiceName
if ($IncludeStartType) {
    Write-Output "$($svc.Name) : $($svc.Status) (démarrage : $($svc.StartType))"
} else {
    Write-Output "$($svc.Name) : $($svc.Status)"
}
```

```powershell
.\Get-ServiceStatus.ps1 -ServiceName Spooler
.\Get-ServiceStatus.ps1 -ServiceName wuauserv -IncludeStartType
```

> **[⚡ PS7+]** `$svc.StartType` est utilisé ici pour garder l'exemple simple. Sous **Windows PowerShell 5.1**, cette propriété peut être vide : utilise alors `Get-CimInstance Win32_Service` et sa propriété `StartMode`. Cette différence est expliquée au **Ch.4** puis appliquée au **Ch.11** — si tu travailles en 5.1, garde-la en tête dès maintenant.

> **Pourquoi pas de `-ComputerName` ici ?** Ce serait trompeur : `Get-Service` s'exécute **en local**. Ajouter un paramètre `-ComputerName` qui n'interroge pas vraiment la machine distante afficherait « le service de SRV01 est Running » alors qu'on a lu **ton poste**. Pour interroger réellement une machine distante, on utilise le **Remoting** (`Invoke-Command`, Ch.29) — et non un paramètre cosmétique. (Note : `Get-Service -ComputerName` existait en Windows PowerShell 5.1 mais **a été retiré de PowerShell 7** ; le remoting est désormais la voie recommandée.)

Les avantages de `param()`, décisifs en administration :

- Les paramètres ont des **noms** (`-ServiceName`) — pas besoin de retenir l'ordre
- On impose un **type** (`[string]`, `[int]`) — les erreurs sont attrapées tôt
- On définit des **valeurs par défaut**
- On rend un paramètre **obligatoire** (`[Parameter(Mandatory)]`)
- La **tab-complétion** fonctionne sur les noms

> **`param()` doit être la toute première instruction** du script (hors commentaires). Sinon, erreur.

> **Comparaison :** en Bash, tu gères `$1`, `$2` et des `shift` manuels ; en Python, `sys.argv` ou `argparse`. `param()` fait tout ça nativement, proprement.

### Des noms de paramètres qui parlent

En administration, on retrouve toujours les mêmes noms de paramètres. Adopte-les, c'est la convention :

```powershell
param(
    [string]$ComputerName,     # la machine cible
    [string]$ServiceName,      # un service
    [string]$UserName,         # un utilisateur
    [string]$Path,             # un chemin
    [string]$OutputPath,       # où écrire un rapport
    [int]$ThresholdGB,         # un seuil
    [switch]$Force             # forcer sans confirmation
)
```

### Paramètres obligatoires

```powershell
param(
    [Parameter(Mandatory)]
    [string]$ServiceName
)
```

Si l'utilisateur oublie `-ServiceName`, PowerShell le lui **demande** automatiquement au lancement — pas de plantage.

### Les paramètres `[switch]` (drapeaux)

Un `[switch]` est un interrupteur : présent = `$true`, absent = `$false`.

```powershell
param(
    [string]$ServiceName,
    [switch]$Restart
)

$svc = Get-Service -Name $ServiceName
Write-Output "$($svc.Name) : $($svc.Status)"

if ($Restart) {
    Restart-Service -Name $ServiceName
    Write-Output "Service redémarré."
}
```

```powershell
.\svc.ps1 -ServiceName Spooler            # affiche seulement
.\svc.ps1 -ServiceName Spooler -Restart   # affiche ET redémarre
```

## 🟡 Très utile en pratique

### La validation des paramètres

PowerShell peut valider automatiquement les valeurs **avant** que le script ne s'exécute :

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ServiceName,

    [ValidateRange(1, 100)]
    [int]$ThresholdGB = 10,

    [ValidateSet("Running", "Stopped", "All")]
    [string]$Filter = "All"
)
```

- `ValidateNotNullOrEmpty` : refuse une valeur vide
- `ValidateRange(1,100)` : impose un intervalle
- `ValidateSet(...)` : n'autorise qu'une liste de valeurs (et active la tab-complétion dessus !)

C'est un gain énorme : les mauvaises entrées sont rejetées avec un message clair, avant de casser quoi que ce soit.

### Le splatting : passer les paramètres via une hashtable

Quand une commande a beaucoup de paramètres, on peut les regrouper dans une hashtable et la « projeter » avec `@` :

```powershell
$params = @{
    Name        = "wuauserv"
    ErrorAction = "Stop"
}
Get-Service @params
```

Plus lisible qu'une longue ligne, et pratique pour construire des appels dynamiquement. On y reviendra en Partie VII (industrialisation).

> **Note :** on n'a volontairement pas mis de `ComputerName` dans ce splat — `Get-Service -ComputerName` n'existe plus en PowerShell 7 (voir plus haut). Pour cibler une machine distante, on splatterait plutôt un appel `Invoke-Command` (Ch.29).

## 🔴 Bonus

### `CmdletBinding` et paramètres communs

En ajoutant `[CmdletBinding()]` au-dessus du `param()`, ton script gagne gratuitement plusieurs **paramètres communs** : `-Verbose`, `-Debug`, `-ErrorAction`… En revanche, `-WhatIf` et `-Confirm` **ne sont pas** ajoutés par le seul `[CmdletBinding()]` : ils nécessitent `[CmdletBinding(SupportsShouldProcess)]` et un appel à `ShouldProcess` (détaillé au Ch.33). On approfondit `[CmdletBinding()]` au Ch.7 (fonctions).

## ❌ Erreur classique

```powershell
# param() pas en première position
Write-Output "Début"
param([string]$Nom)      # ❌ doit être la première instruction

# Oublier la virgule entre paramètres
param(
    [string]$Nom
    [int]$Age            # ❌ virgule manquante après $Nom
)

# Appeler avec la syntaxe C# (parenthèses + virgules)
Get-ServiceStatus("Spooler")           # ❌
.\Get-ServiceStatus.ps1 -ServiceName Spooler   # ✅
```

## 💡 Exercices

**Guidé :** Écris `Test-ServicePresent.ps1` avec un paramètre obligatoire `-ServiceName`. Le script affiche si le service existe (`Get-Service -Name $ServiceName -ErrorAction SilentlyContinue`) et son statut.

**Autonome :** Ajoute un paramètre `-Start` de type `[switch]`. Si présent et que le service est arrêté, le script le démarre. (On verra les conditions `if` au Ch.5 — ici, un simple `if ($Start) { ... }` suffit.)

## ✅ Tu sais maintenant...

- Passer des arguments (`$args`) et, mieux, déclarer des paramètres avec `param()`
- Rendre un paramètre obligatoire, typé, avec valeur par défaut
- Les `[switch]` et la validation (`ValidateSet`, `ValidateRange`…)
- Pourquoi les paramètres rendent un script **automatisable**
- Le splatting pour les appels à nombreux paramètres

## 💬 Questions d'entretien typiques

- **Pourquoi `param()` plutôt que `$args` ?** → Paramètres nommés, typés, validés, avec valeurs par défaut et tab-complétion. Plus robuste et automatisable.
- **Comment forcer un paramètre à faire partie d'une liste de valeurs ?** → `[ValidateSet("a","b","c")]`, qui rejette les autres valeurs et active l'autocomplétion.
- **Qu'est-ce que le splatting ?** → Passer les paramètres d'une cmdlet via une hashtable projetée avec `@`, pour la lisibilité et la construction dynamique d'appels.

---

# Chapitre 4 — Le pipeline et les objets

## 🟢 Le minimum à savoir

### Pourquoi ce chapitre est LE plus important

Si tu ne retiens qu'une chose de tout le cours, retiens ceci : **en PowerShell, le pipeline transporte des objets, pas du texte.** C'est ce qui le rend radicalement différent de Bash, et c'est ce qui rend l'administration Windows si efficace.

### Le pipeline : texte (Bash) vs objets (PowerShell)

**En Bash** : `ps aux | grep firefox | awk '{print $2}'`
- `ps` produit du **texte** ; `grep` filtre des lignes de texte ; `awk` découpe la 2ᵉ colonne de texte. Si le format d'affichage change, tout casse.

**En PowerShell** : `Get-Process firefox | Select-Object Id`
- `Get-Process` produit des **objets processus** ; chaque objet a des propriétés (`Name`, `Id`, `CPU`, `WorkingSet64`…) ; `Select-Object` lit directement la propriété `Id`. Aucun texte à découper, rien ne casse.

> **À garder en tête tout le cours :** les pipelines Unix manipulent des flux de texte ; le pipeline PowerShell manipule des **propriétés d'objets**. C'est la différence fondamentale.

### Voir les objets en action

```powershell
$svc = Get-Service -Name Spooler

$svc.Name            # Spooler
$svc.Status          # Running (ou Stopped)
$svc.StartType       # Automatic / Manual / Disabled
$svc.DisplayName     # "Spouleur d'impression"
```

`$svc` n'est pas du texte : c'est un objet service, dont on lit les propriétés avec un point `.`.

> **⚠️ Compatibilité 5.1 — propriété `StartType`.** La propriété `StartType` sur l'objet renvoyé par `Get-Service` a été **ajoutée à PowerShell 6+**. En **Windows PowerShell 5.1**, `(Get-Service Spooler).StartType` peut être vide. Les exemples de ce cours qui utilisent `$svc.StartType` supposent donc PowerShell 7 (le plus courant aujourd'hui). **Pour obtenir le type de démarrage de façon portable 5.1 ET 7**, passe par CIM (que le cours détaille au Ch.11) :
> ```powershell
> Get-CimInstance Win32_Service -Filter "Name='Spooler'" |
>     Select-Object Name, State, StartMode    # StartMode = Auto / Manual / Disabled
> ```
> Retiens cette équivalence : `Get-Service`.`StartType` (PS7) ↔ `Win32_Service`.`StartMode` (5.1 et 7). On la réutilisera.

### `Get-Member` : LA commande pour explorer

C'est le réflexe central de PowerShell. `Get-Member` révèle **tout** ce que contient un objet :

```powershell
Get-Service | Get-Member
```

La sortie liste :
- les **propriétés** (les informations : `Name`, `Status`, `StartType`…)
- les **méthodes** (les actions : `Start()`, `Stop()`, `Restart()`…)

> **📌 Réflexe transversal.** Tu récupères un objet inconnu ? Passe-le dans `Get-Member`. Ce cours te le rappellera à chaque nouvel objet : service, utilisateur AD, tâche planifiée, réponse d'API… La démarche est toujours la même. C'est le meilleur réflexe PowerShell qui soit.

### Les 5 cmdlets du pipeline

| Cmdlet | Rôle | Analogie Bash |
|--------|------|--------------|
| `Where-Object` | **Filtrer** les objets selon une condition | `grep` |
| `Select-Object` | **Choisir** des propriétés (ou les N premiers) | `cut` / `awk` |
| `Sort-Object` | **Trier** par une propriété | `sort` |
| `Measure-Object` | **Compter**, additionner, moyenner | `wc` |
| `ForEach-Object` | **Agir** sur chaque objet | boucle `for` |

### Filtrer avec `Where-Object`

```powershell
# Les services en cours d'exécution
Get-Service | Where-Object { $_.Status -eq "Running" }

# Les services démarrés automatiquement mais actuellement arrêtés (anomalie !)
Get-Service | Where-Object { $_.StartType -eq "Automatic" -and $_.Status -eq "Stopped" }

# Les processus consommant plus de 200 Mo
Get-Process | Where-Object { $_.WorkingSet64 -gt 200MB }
```

`$_` représente **l'objet courant** qui traverse le pipeline. On le retrouvera partout.

> **Syntaxe simplifiée (PowerShell 3+) :** pour un test simple, on peut écrire `Get-Service | Where-Object Status -eq "Running"` (sans accolades ni `$_`). Les deux formes coexistent ; les accolades restent nécessaires pour les conditions composées.

### Sélectionner avec `Select-Object`

```powershell
Get-Service | Select-Object Name, Status, StartType    # certaines propriétés
Get-Process | Select-Object -First 5                    # les 5 premiers
Get-Process | Select-Object Name, Id -Last 3            # les 3 derniers
```

### Trier avec `Sort-Object`

```powershell
# Les 10 processus les plus gourmands en mémoire
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id -First 10
```

### Compter et calculer avec `Measure-Object`

```powershell
(Get-Service).Count                              # nombre de services (rapide)
Get-Process | Measure-Object WorkingSet64 -Sum   # mémoire totale utilisée
```

### Agir avec `ForEach-Object`

```powershell
# Afficher un message pour chaque service arrêté
Get-Service | Where-Object Status -eq "Stopped" | ForEach-Object {
    Write-Output "Arrêté : $($_.Name)"
}
```

### Un pipeline complet, réaliste

Les 10 processus les plus gourmands, avec la RAM en Mo (propriété **calculée**) :

```powershell
Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{ Name = "RAM(Mo)"; Expression = { [math]::Round($_.WorkingSet64/1MB) } } |
    Select-Object -First 10
```

La syntaxe `@{ Name = "..."; Expression = { ... } }` crée une colonne calculée à la volée. On l'écrit souvent en abrégé `@{ N=...; E={...} }`.

## 🟡 Très utile en pratique

### Exporter les résultats (et le piège `Format-Table`)

Comme le pipeline transporte des objets, on peut les exporter directement — proprement :

```powershell
Get-Service | Select-Object Name, Status, StartType |
    Export-Csv -Path "services.csv" -NoTypeInformation -Encoding UTF8

Get-Process | Select-Object Name, Id, CPU |
    ConvertTo-Json | Set-Content "process.json" -Encoding UTF8
```

> **⚠️ Règle importante — `Format-*` en toute fin de pipeline uniquement.** Les cmdlets `Format-Table`, `Format-List`, `Format-Wide` transforment tes objets en **instructions d'affichage** : après elles, ce ne sont plus des données exploitables. Ne mets **jamais** un `Format-Table` avant un `Export-Csv`, un `Where-Object` ou un traitement — tu obtiendrais un CSV illisible rempli d'objets de formatage. `Format-*` sert **seulement** à présenter à l'écran, en tout dernier.
>
> ```powershell
> Get-Service | Format-Table | Export-Csv out.csv   # ❌ CSV corrompu
> Get-Service | Export-Csv out.csv -NoTypeInformation  # ✅ export propre
> Get-Service | Format-Table -AutoSize                  # ✅ affichage écran, en dernier
> ```

### `Out-GridView` : une fenêtre interactive `[🪟 Windows]`

```powershell
Get-Service | Out-GridView    # tableau graphique triable/filtrable
```

## 🔴 Bonus

### Les propriétés calculées, plus loin

On peut enchaîner plusieurs propriétés calculées pour bâtir un rapport sur mesure — on s'en servira beaucoup pour les inventaires (Ch.14) et les rapports AD (Ch.24).

## ❌ Erreur classique

```powershell
# Oublier $_ dans Where-Object (forme avec accolades)
Get-Service | Where-Object { Status -eq "Running" }     # ❌
Get-Service | Where-Object { $_.Status -eq "Running" }  # ✅

# Mettre Format-Table avant un traitement
Get-Process | Format-Table | Where-Object CPU -gt 10    # ❌ ne filtre plus rien d'utile
Get-Process | Where-Object CPU -gt 10 | Format-Table    # ✅

# Croire que "rien à l'écran" = "rien retourné"
$x = Get-Service    # rien ne s'affiche, mais $x contient tous les services
```

## 💡 Exercices

**Guidé :** Liste les services arrêtés dont le démarrage est `Automatic` (une anomalie fréquente), triés par nom, et affiche `Name` + `DisplayName`.

**Autonome :** Affiche les 5 processus les plus gourmands en mémoire avec une colonne calculée « RAM(Mo) », puis exporte le résultat complet (tous les processus, pas seulement 5) en CSV.

## 🧩 Mini-projet — Top consommateurs

Crée `Get-TopProcess.ps1` avec un paramètre `-Count` (défaut 10) qui affiche les N processus les plus gourmands en mémoire (nom, PID, RAM en Mo via propriété calculée) **et** affiche en vert le total de RAM consommée par ces N processus. Réutilise `param()` (Ch.3), le pipeline, la propriété calculée et `Measure-Object`.

## ✅ Tu sais maintenant...

- Le pipeline transporte des **objets**, pas du texte
- `$_` = l'objet courant ; `Get-Member` = le réflexe d'exploration
- `Where-Object` / `Select-Object` / `Sort-Object` / `Measure-Object` / `ForEach-Object`
- Les propriétés calculées `@{N=...;E={...}}`
- Exporter en CSV/JSON, et **ne jamais** mettre `Format-*` avant un traitement

## 💬 Questions d'entretien typiques

- **Quelle est LA différence entre le pipeline Bash et PowerShell ?** → Bash transporte du texte à parser ; PowerShell transporte des objets dont on lit les propriétés directement.
- **Que fait `Get-Member` ?** → Il révèle les propriétés et méthodes d'un objet. C'est l'outil pour explorer tout objet inconnu.
- **Pourquoi ne pas mettre `Format-Table` au milieu d'un pipeline ?** → Il convertit les objets en instructions d'affichage : plus rien n'est exploitable ensuite (filtrage, export). `Format-*` va en tout dernier, pour l'écran uniquement.

---

# Chapitre 5 — Opérateurs et conditions

## 🟢 Le minimum à savoir

### Les opérateurs de comparaison

PowerShell utilise des opérateurs avec tiret (comme Bash), **pas** les symboles `<` `>` `==` (réservés à d'autres usages) :

| Opérateur | Signification | Exemple |
|-----------|--------------|---------|
| `-eq` | Égal | `$_.Status -eq "Running"` |
| `-ne` | Différent | `$_.Status -ne "Stopped"` |
| `-gt` / `-ge` | Supérieur / ou égal | `$_.WorkingSet64 -gt 200MB` |
| `-lt` / `-le` | Inférieur / ou égal | `$FreeGB -lt 10` |
| `-like` | Correspond à un motif (`*`, `?`) | `$_.Name -like "Win*"` |
| `-match` | Correspond à une regex | `$_.Name -match "^svc"` |
| `-contains` / `-in` | Appartenance à une collection | `$Critiques -contains $_.Name` |

> **Comparaison :** PowerShell `-eq` / `-lt` / `-gt` ≈ Bash `-eq` / `-lt` / `-gt`. Python utilise `==` / `<` / `>`. En PowerShell, `<` et `>` servent à la **redirection** — d'où les opérateurs à tiret.

> **Insensible à la casse par défaut :** `"SPOOLER" -eq "spooler"` renvoie `$true`. Pour forcer la casse, préfixe par `c` : `-ceq`, `-clike`, `-cmatch`.

### Les opérateurs logiques

```powershell
$FreeGB -lt 10 -and $svc.Status -eq "Running"     # les deux vraies
$Role -eq "admin" -or $Role -eq "operator"        # au moins une
-not ($svc.Status -eq "Running")                   # négation
```

`-and`, `-or`, `-not` (Bash : `&&`, `||`, `!` ; Python : `and`, `or`, `not`).

### Manipuler le texte : opérateurs de chaînes

En administration, on manipule sans cesse du texte : noms de machines, chemins, DN Active Directory, noms DNS, URIs, valeurs de registre. Ces opérateurs sont indispensables :

```powershell
# -like : motifs simples avec * et ?
"SRV-DC01" -like "SRV-*"                 # True

# -match : expressions régulières
"user@lab.local" -match "@(.+)$"         # True ; $Matches[1] = "lab.local"

# -replace : remplacer (avec regex)
"lab\alice" -replace "^lab\\", ""        # "alice"

# -split / -join : découper / recoller
"DC01,SRV01,CLIENT01" -split ","         # tableau de 3 éléments
@("a","b","c") -join " | "               # "a | b | c"
```

Et les **méthodes** de chaîne (rappel : ce sont des objets `[string]`) :

```powershell
$dn = "CN=Alice Martin,OU=IT,DC=lab,DC=local"
$dn.Length                                # longueur
$dn.ToUpper() / $dn.ToLower()             # casse
$dn.Trim()                                # enlève les espaces aux extrémités
$dn.Replace("lab", "corp")                # remplacement simple (sans regex)
$dn.Split(",")                            # découpe → tableau
$dn.StartsWith("CN=")                     # True
$dn.Substring(0, 8)                       # "CN=Alice"
```

> **Pourquoi c'est crucial :** au Ch.20, un DN (Distinguished Name) AD ressemble à `CN=Alice,OU=IT,DC=lab,DC=local`. Savoir le découper avec `.Split(",")` ou `-match` te permettra d'en extraire l'OU, le nom, le domaine. Ces opérations de chaînes reviennent partout : parser un chemin, isoler un nom d'utilisateur, construire une URI d'API.

### Vérifier une existence : `Test-Path` et compagnie

Les cmdlets `Test-*` renvoient un booléen (`$true`/`$false`) — parfaites pour les conditions :

```powershell
Test-Path "C:\Scripts"                    # le dossier existe ?
Test-Path "HKLM:\SOFTWARE\MonApp"          # la clé de registre existe ?
Test-Connection SRV01 -Count 1 -Quiet      # la machine répond au ping ?
```

> **📌 Réflexe `Get`/`Test` avant d'agir :** ces cmdlets incarnent la discipline d'administration. Avant de créer un dossier, `Test-Path`. Avant de configurer une machine, `Test-Connection`. On vérifie l'état **avant** de modifier.

### Les conditions : `if` / `elseif` / `else`

```powershell
$svc = Get-Service -Name Spooler

if ($svc.Status -eq "Running") {
    Write-Host "Le spouleur tourne." -ForegroundColor Green
}
elseif ($svc.Status -eq "Stopped") {
    Write-Host "Le spouleur est arrêté." -ForegroundColor Red
}
else {
    Write-Host "État : $($svc.Status)" -ForegroundColor Yellow
}
```

Syntaxe : condition entre **parenthèses** `()`, bloc entre **accolades** `{}`. Pas de `then`, pas de `fi`. C'est `elseif` en un seul mot.

### Un cas d'administration complet

```powershell
# Vérifier l'espace disque et réagir
$free = (Get-PSDrive C).Free / 1GB

if ($free -lt 10) {
    Write-Host "ALERTE : seulement $([math]::Round($free,1)) Go libres sur C:" -ForegroundColor Red
}
else {
    Write-Host "Espace OK : $([math]::Round($free,1)) Go libres" -ForegroundColor Green
}
```

### Le `switch` : choix multiples

Quand on teste une même valeur contre plusieurs cas, `switch` est plus lisible qu'une cascade de `if` :

```powershell
$svc = Get-Service -Name Spooler

switch ($svc.Status) {
    "Running" { Write-Host "Actif" -ForegroundColor Green }
    "Stopped" { Write-Host "Arrêté" -ForegroundColor Red }
    default   { Write-Host "État : $($svc.Status)" -ForegroundColor Yellow }
}
```

Le `switch` PowerShell gère aussi les motifs :

```powershell
switch -Wildcard ($fichier) {
    "*.log" { "Journal" }
    "*.csv" { "Données" }
    default { "Autre" }
}
```

## 🟡 Très utile en pratique

### Comparaisons et pipeline : la même logique

`Where-Object { $_.Status -eq "Running" }` (Ch.4) utilise exactement ces opérateurs. Un `if` teste **une** valeur ; `Where-Object` applique le même test à **chaque objet** du pipeline. Même grammaire, deux usages.

### L'opérateur ternaire `[⚡ PS7+]`

```powershell
$etat = $svc.Status -eq "Running" ? "OK" : "PROBLEME"
```

En 5.1, utilise un `if`/`else` classique.

## 🔴 Bonus

### `-match` et la variable `$Matches`

Après un `-match` réussi, `$Matches` contient les groupes capturés :

```powershell
if ("user@lab.local" -match "^(.+)@(.+)$") {
    $Matches[1]   # user
    $Matches[2]   # lab.local
}
```

Très utile pour extraire des morceaux d'un log, d'un DN, d'une adresse.

## ❌ Erreur classique

```powershell
# Utiliser == ou > au lieu des opérateurs à tiret
if ($age == 18) { }      # ❌ == n'existe pas
if ($a > $b) { }         # ❌ > redirige vers un fichier !
if ($age -eq 18) { }     # ✅
if ($a -gt $b) { }       # ✅

# Confondre = (affectation) et -eq (comparaison)
if ($status = "Running") { }    # ❌ affectation, toujours vrai
if ($status -eq "Running") { }  # ✅

# Oublier les parenthèses ou accolades
if $svc.Status -eq "Running" { }   # ❌ parenthèses obligatoires
```

## 💡 Exercices

**Guidé :** Écris un script qui prend un `-ServiceName` et affiche en couleur : vert si Running, rouge si Stopped, jaune sinon. Utilise `switch`.

**Autonome :** Écris un script qui vérifie l'espace libre de `C:` et affiche une alerte si moins de 15 Go. Ajoute un test : si en plus le service `wuauserv` (Windows Update) tourne, suggère de le mettre en pause (message seulement).

## ✅ Tu sais maintenant...

- Les opérateurs de comparaison (`-eq`, `-lt`, `-like`, `-match`…) et logiques (`-and`, `-or`, `-not`)
- Les opérateurs et méthodes de chaîne (`-split`, `-replace`, `.Trim()`, `.Split()`…) — cruciaux pour DN, chemins, URIs
- `Test-Path` / `Test-Connection` et la discipline `Test` avant d'agir
- `if` / `elseif` / `else` et `switch` (avec motifs)

## 💬 Questions d'entretien typiques

- **Comment teste-t-on l'égalité en PowerShell ?** → `-eq` (insensible à la casse ; `-ceq` pour la casse). `==` n'existe pas ; `=` est une affectation.
- **Comment extraire le domaine de `user@lab.local` ?** → `-match "@(.+)$"` puis `$Matches[1]`, ou `.Split("@")[1]`.
- **`Where-Object` et `if`, quel rapport ?** → Même grammaire de comparaison ; `if` teste une valeur, `Where-Object` applique le test à chaque objet du pipeline.

---

# Chapitre 6 — Collections, hashtables et boucles

## 🟢 Le minimum à savoir

### Les tableaux (arrays)

Un tableau regroupe plusieurs valeurs. En administration, c'est typiquement **une liste de machines** :

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

$Serveurs[0]           # DC01 (premier)
$Serveurs[-1]          # SRV-WEB01 (dernier)
$Serveurs.Count        # 3
$Serveurs += "SRV02"   # ajoute (crée un nouveau tableau — lent en boucle serrée)
$Serveurs -contains "DC01"    # True
```

### Les hashtables (dictionnaires clé-valeur)

Une hashtable associe des **clés** à des **valeurs** :

```powershell
$Seuils = @{
    DisqueGB = 10
    RAMPourcent = 90
    Uptime = 30
}

$Seuils["DisqueGB"]        # 10
$Seuils.RAMPourcent        # 90 (syntaxe avec point)
$Seuils["Uptime"] = 45     # modifier
$Seuils.ContainsKey("DisqueGB")   # True
```

On les retrouve partout : configuration, `-FilterHashtable` pour les logs (Ch.34), splatting (Ch.3), corps JSON d'API (Ch.31).

> **Comparaison :** `@{ Clé = "Valeur" }` en PowerShell ≈ dictionnaire Python `{ "clé": "valeur" }` ≈ tableau associatif Bash `declare -A`.

### Le PSCustomObject : construire des objets pour tes rapports

C'est **l'outil clé** pour produire des rapports d'administration propres. Tu fabriques un objet avec les propriétés que tu veux :

```powershell
$rapport = [PSCustomObject]@{
    Serveur   = "SRV01"
    Statut    = "OK"
    EspaceGB  = 42
    Verifie   = Get-Date
}

$rapport.Serveur          # SRV01
```

L'intérêt : un tableau de PSCustomObject s'exporte directement en CSV/JSON, s'affiche en table, se filtre… C'est ainsi qu'on produit des inventaires (Ch.14), des rapports AD (Ch.24), des états de parc.

```powershell
$parc = @(
    [PSCustomObject]@{ Serveur = "DC01";  Role = "AD";     RAM_GB = 16 }
    [PSCustomObject]@{ Serveur = "SRV01"; Role = "Files";  RAM_GB = 8 }
)
$parc | Format-Table -AutoSize        # affichage
$parc | Export-Csv parc.csv -NoTypeInformation -Encoding UTF8   # export
```

### Les boucles

**`foreach`** — parcourir une collection (le cas le plus courant en admin) :

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

foreach ($s in $Serveurs) {
    if (Test-Connection $s -Count 1 -Quiet) {
        Write-Host "$s répond" -ForegroundColor Green
    } else {
        Write-Host "$s NE répond PAS" -ForegroundColor Red
    }
}
```

**`for`** — quand tu as besoin d'un compteur :

```powershell
for ($i = 1; $i -le 5; $i++) {
    Write-Output "Tentative $i"
}
```

**`while`** / **`do...while`** / **`do...until`** — tant qu'une condition tient :

```powershell
# Attendre qu'un service démarre (avec sécurité anti-boucle infinie)
$essais = 0
do {
    Start-Sleep -Seconds 2
    $svc = Get-Service -Name Spooler
    $essais++
} while ($svc.Status -ne "Running" -and $essais -lt 10)
```

**`break`** sort de la boucle, **`continue`** passe à l'itération suivante.

### `foreach` (mot-clé) vs `ForEach-Object` (pipeline)

```powershell
# foreach : la collection est déjà en mémoire
$services = Get-Service
foreach ($s in $services) { $s.Name }

# ForEach-Object : traite les objets au fil du pipeline (économe en mémoire)
Get-Service | ForEach-Object { $_.Name }
```

Les deux existent, choisis selon le contexte. En pipeline, c'est `ForEach-Object` (avec `$_`).

## 🟡 Très utile en pratique

### Construire un rapport de parc

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

$resultats = foreach ($s in $Serveurs) {
    $enLigne = Test-Connection $s -Count 1 -Quiet
    [PSCustomObject]@{
        Serveur = $s
        EnLigne = $enLigne
        Teste   = Get-Date -Format "HH:mm:ss"
    }
}

$resultats | Format-Table -AutoSize
```

Remarque : la boucle `foreach` **produit** des objets qu'on capture dans `$resultats`. C'est un pattern fondamental pour les inventaires.

### Performance : `+=` sur un gros tableau

`$tab += $x` recrée tout le tableau à chaque ajout — lent sur des milliers d'éléments. Alternative :

```powershell
$liste = [System.Collections.Generic.List[object]]::new()
$liste.Add($x)
```

Pour débuter, `+=` suffit sur de petits volumes ; retiens juste que ça ne passe pas à l'échelle.

## 🔴 Bonus

### Parcours parallèle `[⚡ PS7+]`

PowerShell 7 permet `ForEach-Object -Parallel` pour traiter plusieurs machines en même temps :

```powershell
$Serveurs | ForEach-Object -Parallel { Test-Connection $_ -Count 1 -Quiet } -ThrottleLimit 5
```

Puissant pour l'inventaire d'un grand parc — on en reparle en Partie VI.

## ❌ Erreur classique

```powershell
# Confondre foreach (mot-clé) et ForEach-Object (pipeline)
Get-Service | foreach ($s in ...) { }      # ❌
Get-Service | ForEach-Object { $_.Name }   # ✅

# Boucle potentiellement infinie sans garde-fou
do { ... } while ($svc.Status -ne "Running")   # ❌ si le service ne démarre jamais
# ✅ ajoute un compteur d'essais maximum

# Indexer une hashtable comme un tableau
$Seuils[0]              # ❌ 0 n'est pas une clé
$Seuils["DisqueGB"]     # ✅
```

## 💡 Exercices

**Guidé :** Crée un tableau de 3 noms de services critiques (`"Spooler"`, `"wuauserv"`, `"EventLog"`). Parcours-le avec `foreach` et affiche l'état de chacun en couleur.

**Autonome :** Transforme le résultat précédent en tableau de PSCustomObject (`Service`, `Statut`, `DemarrageAuto`) et exporte-le en CSV.

## 🧩 Mini-projet — Supervision de services critiques

Crée `Test-CriticalServices.ps1` qui : prend un paramètre `-Services` (tableau, avec une valeur par défaut de 3-4 services), parcourt la liste, construit un PSCustomObject par service (Nom, Statut, TypeDémarrage, Conforme), affiche le tout en table, et exporte en CSV. Réutilise `param()` (Ch.3), le pipeline (Ch.4), les conditions (Ch.5) et les collections (Ch.6). *(Pour le type de démarrage portable en 5.1 comme en 7, tu utiliseras `Get-CimInstance Win32_Service` et sa propriété `StartMode` — détaillé au Ch.11.)*

## ✅ Tu sais maintenant...

- Créer et manipuler tableaux (`@()`) et hashtables (`@{}`)
- Fabriquer des **PSCustomObject** pour des rapports propres
- Les boucles `foreach` / `for` / `while` / `do` et `break`/`continue`
- La différence `foreach` (mot-clé) vs `ForEach-Object` (pipeline)
- Produire un tableau d'objets depuis une boucle (pattern d'inventaire)

## 💬 Questions d'entretien typiques

- **Comment produire un rapport structuré exportable en CSV ?** → Construire des `[PSCustomObject]` (une propriété par colonne), les collecter dans un tableau, puis `Export-Csv`.
- **`foreach` ou `ForEach-Object` ?** → `foreach` quand la collection est en mémoire ; `ForEach-Object` dans un pipeline (plus économe, utilise `$_`).
- **Pourquoi `$tab += $x` est déconseillé en masse ?** → Il recrée le tableau à chaque ajout ; sur de gros volumes, on utilise une `List[object]`.

---

# Chapitre 7 — Fonctions et scripts structurés

## 🟢 Le minimum à savoir

### Pourquoi des fonctions ?

Jusqu'ici, tes scripts étaient linéaires. Dès qu'une logique se répète (vérifier un service, tester une machine, produire une ligne de rapport), on la range dans une **fonction** : un bloc nommé, réutilisable, testable. C'est le premier pas vers des outils d'administration propres.

### Définir et appeler une fonction

```powershell
function Get-Uptime {
    $os = Get-CimInstance Win32_OperatingSystem
    (Get-Date) - $os.LastBootUpTime
}

Get-Uptime        # appel : on écrit juste son nom
```

> **Convention :** nomme tes fonctions en `Verbe-Nom`, comme les cmdlets (`Get-Uptime`, `Test-ServerHealth`). Utilise des verbes approuvés (liste : `Get-Verb`). Ça rend tes fonctions cohérentes avec l'écosystème PowerShell.

### Paramètres de fonction

C'est le **même `param()`** que pour les scripts (Ch.3) — une fonction est un mini-script :

```powershell
function Test-ServiceRunning {
    param(
        [Parameter(Mandatory)]
        [string]$ServiceName
    )

    $svc = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
    $svc -and $svc.Status -eq "Running"
}

Test-ServiceRunning -ServiceName Spooler    # → True ou False
```

### Le return implicite : LE piège à comprendre

**En PowerShell, tout ce qui n'est pas capturé ou redirigé est automatiquement renvoyé.** Pas besoin de `return` pour renvoyer une valeur — mais attention aux sorties parasites.

```powershell
function Get-Somme {
    param([int]$A, [int]$B)
    $A + $B          # renvoyé automatiquement, sans return
}

$r = Get-Somme -A 10 -B 25     # → 35
```

Le piège : si la fonction produit **d'autres** sorties, elles sont aussi renvoyées :

```powershell
function Get-SommeBuggee {
    param([int]$A, [int]$B)
    Write-Output "Calcul en cours..."   # ← renvoyé AUSSI !
    $A + $B
}

$r = Get-SommeBuggee -A 10 -B 25
$r    # → un TABLEAU @("Calcul en cours...", 35), pas 35 !
```

**La solution :** pour les messages de diagnostic, utilise `Write-Verbose` (affiché seulement si l'appelant passe `-Verbose`), qui nécessite `[CmdletBinding()]` :

```powershell
function Get-SommeCorrecte {
    [CmdletBinding()]
    param([int]$A, [int]$B)
    Write-Verbose "Calcul en cours..."   # n'entre PAS dans la sortie
    $A + $B                               # seule vraie valeur renvoyée
}

$r = Get-SommeCorrecte -A 10 -B 25            # → 35
$r = Get-SommeCorrecte -A 10 -B 25 -Verbose   # affiche le message, renvoie 35
```

> **Comparaison :** en Python, seul `return` renvoie. En PowerShell, **tout** ce qui « tombe » dans le pipeline est renvoyé. C'est puissant (une fonction peut émettre un flux d'objets) mais il faut garder ses fonctions « propres » : une fonction renvoie des **données**, ses messages passent par `Write-Verbose`/`Write-Host`.

### `return` existe (mais ne fait pas ce que tu crois)

`return` renvoie une valeur **et** quitte la fonction. Il sert surtout à sortir tôt :

```powershell
function Get-AccountState {
    param([int]$FailedLogons)
    if ($FailedLogons -ge 5) { return "À verrouiller" }
    if ($FailedLogons -ge 1) { return "À surveiller" }
    "OK"
}
```

`return "x"` équivaut à « émettre `x` puis stopper ». Il ne « fabrique » pas la sortie à lui seul — la ligne `"OK"` sans `return` renvoie tout autant.

### La portée des variables (scope)

Les variables créées dans une fonction sont **locales** — elles n'affectent pas l'extérieur :

```powershell
$Cible = "Global"

function Set-Cible {
    $Cible = "Local"        # crée une variable LOCALE
    Write-Output "Dans la fonction : $Cible"    # Local
}

Set-Cible
Write-Output "Après : $Cible"                   # Global (inchangé)
```

Pour lire une variable du script parent, PowerShell « remonte » les portées automatiquement en **lecture**. Mais pour **modifier** une variable parente, il faudrait `$script:Cible` ou `$global:Cible` — à **éviter**. La bonne pratique : une fonction reçoit ce dont elle a besoin par **paramètres** et **renvoie** un résultat. Pas d'effets de bord cachés.

## 🟡 Très utile en pratique

### `[CmdletBinding()]` : transformer une fonction en outil pro

Ajouter `[CmdletBinding()]` au-dessus du `param()` donne gratuitement à ta fonction les **paramètres communs** : `-Verbose`, `-Debug`, `-ErrorAction`, et (avec un peu plus de code) `-WhatIf`/`-Confirm` (voir Ch.33).

```powershell
function Test-ServerHealth {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$ComputerName,
        [int]$MinFreeGB = 10
    )

    Write-Verbose "Vérification de $ComputerName..."

    $online = Test-Connection $ComputerName -Count 1 -Quiet

    [PSCustomObject]@{
        Serveur = $ComputerName
        EnLigne = $online
        Verifie = Get-Date -Format "yyyy-MM-dd HH:mm"
    }
}

Test-ServerHealth -ComputerName SRV01 -Verbose
```

Remarque le pattern clé : la fonction **renvoie un PSCustomObject**. Elle ne l'affiche pas, elle le produit — l'appelant décide ensuite d'afficher, filtrer, exporter.

### Placer ses fonctions dans un script

Un script d'administration typique définit ses fonctions en haut, puis les orchestre en bas :

```powershell
# ServerHealth.ps1
param(
    [string[]]$Servers = @("DC01", "SRV01")
)

function Test-ServerHealth {
    [CmdletBinding()]
    param([string]$ComputerName)
    [PSCustomObject]@{
        Serveur = $ComputerName
        EnLigne = Test-Connection $ComputerName -Count 1 -Quiet
    }
}

# Orchestration
$Servers | ForEach-Object { Test-ServerHealth -ComputerName $_ } |
    Format-Table -AutoSize
```

## 🔴 Bonus

### `begin` / `process` / `end` : accepter le pipeline

Une fonction avancée peut traiter des objets reçus **par le pipeline** grâce à un paramètre marqué `ValueFromPipeline` et un bloc `process` :

```powershell
function Get-ServiceReport {
    [CmdletBinding()]
    param(
        [Parameter(ValueFromPipeline)]
        [System.ServiceProcess.ServiceController]$Service
    )
    process {
        [PSCustomObject]@{
            Nom    = $Service.Name
            Statut = $Service.Status
        }
    }
}

Get-Service | Get-ServiceReport    # la fonction reçoit chaque service via le pipeline
```

C'est ce qui rend une fonction « native » au pipeline PowerShell. À creuser plus tard.

## ❌ Erreur classique

```powershell
# Return implicite pollué par .Add()
function Build-List {
    $l = @()
    $l.Add("x")          # ❌ .Add() sur un tableau renvoie... et échoue souvent
}
# → utiliser une vraie liste et absorber les sorties parasites
$l = [System.Collections.Generic.List[object]]::new()
$l.Add("x")              # ok, ne pollue pas

# Appeler une fonction à la C#
Test-ServiceRunning("Spooler")          # ❌ un seul argument (un tableau)
Test-ServiceRunning -ServiceName Spooler   # ✅

# Modifier une variable globale depuis une fonction
function Set-Flag { $global:Flag = $true }   # ❌ effet de bord caché
# → renvoyer une valeur et la capturer à l'extérieur
```

## 💡 Exercices

**Guidé :** Écris une fonction `Test-DiskSpace` qui prend `-Drive` (ex : `"C"`) et `-MinFreeGB` (défaut 10), et renvoie un PSCustomObject `{ Lecteur; LibreGB; Conforme }`.

**Autonome :** Écris `Get-ServiceStatus` qui accepte plusieurs noms de services et renvoie un PSCustomObject par service. Appelle-la puis exporte le résultat en CSV.

## ✅ Tu sais maintenant...

- Définir des fonctions `Verbe-Nom` avec `param()`
- Le **return implicite** et comment garder une fonction propre (`Write-Verbose`)
- La portée locale des variables et pourquoi éviter les variables globales
- `[CmdletBinding()]` pour des fonctions avec paramètres communs
- Le pattern « une fonction renvoie des objets, elle ne les affiche pas »

## 💬 Questions d'entretien typiques

- **Comment une fonction PowerShell renvoie-t-elle une valeur ?** → Tout ce qui n'est pas capturé/redirigé est renvoyé ; `return` sert surtout à sortir tôt.
- **Pourquoi `Write-Verbose` plutôt que `Write-Output` pour un message ?** → `Write-Output` polluerait la valeur de retour ; `Write-Verbose` ne s'affiche qu'avec `-Verbose` et n'entre pas dans la sortie.
- **À quoi sert `[CmdletBinding()]` ?** → À obtenir les paramètres communs (`-Verbose`, `-ErrorAction`, support de `-WhatIf`…) et faire de la fonction un outil « avancé ».

---

# Chapitre 8 — Gestion des erreurs et débogage

## 🟢 Le minimum à savoir

### Pourquoi c'est vital en administration

Un script d'administration touche à de vraies machines. S'il plante silencieusement au milieu d'une boucle sur 200 serveurs, ou s'il continue comme si de rien n'était après un échec, les dégâts peuvent être réels. Savoir **détecter, intercepter et journaliser** les erreurs est une compétence non négociable.

### Erreurs terminantes vs non-terminantes : la distinction clé

PowerShell a **deux** sortes d'erreurs, et c'est LE point à comprendre :

- **Non-terminante** : la cmdlet signale un problème mais **continue** (et le script continue). C'est le cas par défaut de la plupart des cmdlets. Exemple : `Get-Service "Absent1","Spooler"` affiche une erreur pour `Absent1` mais renvoie quand même `Spooler`.
- **Terminante** : l'exécution **s'arrête** (erreur de syntaxe, exception .NET, ou erreur non-terminante que tu as *promue* en terminante).

Le problème : un `try/catch` (voir plus bas) n'attrape **que les erreurs terminantes**. Une erreur non-terminante passe à travers le `catch` sans le déclencher. D'où la nécessité de `-ErrorAction Stop`.

### `-ErrorAction` : contrôler le comportement

Chaque cmdlet accepte `-ErrorAction`, qui décide quoi faire en cas d'erreur :

| Valeur | Effet |
|--------|-------|
| `Continue` | (défaut) Affiche l'erreur et continue |
| `Stop` | **Transforme l'erreur en terminante** (indispensable pour `try/catch`) |
| `SilentlyContinue` | Ignore l'erreur silencieusement et continue |
| `Ignore` | Ignore sans même enregistrer l'erreur dans `$Error` |

```powershell
Get-Service "Absent" -ErrorAction SilentlyContinue   # pas de rouge à l'écran
Get-Service "Absent" -ErrorAction Stop               # lève une erreur terminante
```

### `try` / `catch` / `finally`

C'est le mécanisme d'interception. **Rappel : il faut `-ErrorAction Stop` pour que `catch` attrape une erreur de cmdlet.**

```powershell
try {
    $svc = Get-Service -Name "ServiceInexistant" -ErrorAction Stop
    Restart-Service -Name $svc.Name -ErrorAction Stop
    Write-Host "Service redémarré." -ForegroundColor Green
}
catch {
    Write-Host "Échec : $($_.Exception.Message)" -ForegroundColor Red
}
finally {
    Write-Host "Vérification terminée."   # s'exécute TOUJOURS
}
```

- `try` : le code qui peut échouer
- `catch` : ce qu'on fait en cas d'erreur (`$_` contient l'objet erreur ; `$_.Exception.Message` le message)
- `finally` : s'exécute dans tous les cas (nettoyage, fermeture de session…) — optionnel

> **Comparaison :** `try/catch/finally` existe quasi à l'identique en Python et dans beaucoup de langages. La spécificité PowerShell, c'est le `-ErrorAction Stop` à ne pas oublier.

### Un exemple d'administration réel

```powershell
$Serveurs = @("DC01", "SRV-ABSENT", "SRV01")

foreach ($s in $Serveurs) {
    try {
        $os = Get-CimInstance Win32_OperatingSystem -ComputerName $s -ErrorAction Stop
        Write-Host "$s OK — démarré le $($os.LastBootUpTime)" -ForegroundColor Green
    }
    catch {
        Write-Host "$s injoignable : $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

Grâce au `try/catch` **dans** la boucle, un serveur injoignable n'interrompt pas le traitement des autres. C'est le pattern d'or de l'administration de parc.

### `$?` et `$LASTEXITCODE` : deux indicateurs à ne pas confondre

```powershell
Get-Service Spooler
$?               # $true si la DERNIÈRE commande PowerShell a réussi, $false sinon

ping SRV01
$LASTEXITCODE    # code de sortie du dernier PROGRAMME EXTERNE (ping.exe) : 0 = succès
```

- `$?` : booléen, indique le **succès de la dernière opération** — cmdlet **ou** commande native. Pour un exécutable externe, `$?` passe à `$true` si le code de sortie est `0`, `$false` sinon. Il ne dit **pas** *quel* code : juste réussi/échoué. Il se remet à jour à **chaque** commande — capture-le tout de suite.
- `$LASTEXITCODE` : entier, donne le **code de sortie exact** du dernier **programme externe** (`ping`, `robocopy`, `git`…). Convention Unix : `0` = succès, autre = erreur (et la valeur précise peut renseigner sur la cause).

> **En pratique :** `$?` = « ça a réussi, oui ou non ? » (booléen, marche pour tout) ; `$LASTEXITCODE` = « quel code exact a renvoyé l'exécutable ? » (entier, exécutables natifs seulement). Pour tester finement le résultat d'un `.exe`, préfère `$LASTEXITCODE -eq 0` plutôt que `$?`, car tu récupères la valeur exacte. Et `$?` est fugace : `Get-Service; Write-Host "x"; $?` te donne le succès du `Write-Host`, pas du `Get-Service`.

## 🟡 Très utile en pratique

### La variable `$Error`

PowerShell garde l'historique des erreurs dans `$Error` (un tableau, la plus récente en `[0]`) :

```powershell
$Error[0]                      # la dernière erreur
$Error[0].Exception.Message    # son message
$Error.Clear()                 # vider l'historique
```

Pratique pour le débogage : après un souci, `$Error[0] | Format-List *` donne tous les détails.

### Les messages de diagnostic

PowerShell a plusieurs « flux » de sortie dédiés — utilise le bon selon l'intention :

```powershell
Write-Verbose "Détail affiché avec -Verbose"      # diagnostic (nécessite CmdletBinding)
Write-Warning "Avertissement (jaune)"             # avertissement visible
Write-Error   "Erreur non-terminante"             # erreur (rouge), sans stopper
Write-Debug   "Message de débogage (-Debug)"      # débogage
```

> **Bonne pratique :** ne mélange pas tes **données** (via `Write-Output`/objets) et tes **messages** (via ces flux). C'est ce qui rend un script à la fois exploitable en pipeline *et* lisible par un humain.

### `Set-StrictMode` : le filet anti-bugs

`Set-StrictMode` force PowerShell à signaler les erreurs silencieuses classiques (variable non définie, propriété inexistante) :

```powershell
Set-StrictMode -Version Latest

$Total = $Compteur + 1    # ❌ erreur claire si $Compteur n'a jamais été défini
```

Sans lui, `$Compteur` non défini vaudrait `$null` (donc `0`) et le bug passerait inaperçu. Mets-le en tête de tes scripts sérieux.

### L'aide basée sur les commentaires

Documente tes fonctions/scripts avec un bloc spécial — `Get-Help` le lira :

```powershell
function Test-ServerHealth {
<#
.SYNOPSIS
    Vérifie l'état de santé d'un serveur.
.PARAMETER ComputerName
    Le nom du serveur à vérifier.
.EXAMPLE
    Test-ServerHealth -ComputerName SRV01
#>
    [CmdletBinding()]
    param([string]$ComputerName)
    # ...
}

Get-Help Test-ServerHealth -Examples    # affiche ta doc
```

## 🔴 Bonus

### Attraper des erreurs spécifiques

`catch` peut cibler un type d'exception précis, pour réagir différemment selon la cause :

```powershell
try {
    Get-Content "C:\introuvable.txt" -ErrorAction Stop
}
catch [System.IO.FileNotFoundException] {
    Write-Warning "Fichier absent."
}
catch {
    Write-Warning "Autre erreur : $($_.Exception.Message)"
}
```

### Le point d'arrêt et le débogage pas-à-pas

Dans VS Code, tu peux poser des points d'arrêt (clic dans la marge, ou `Set-PSBreakpoint`) et exécuter le script pas-à-pas pour inspecter les variables. Indispensable quand un script se comporte de façon inattendue.

## ❌ Erreur classique

```powershell
# try/catch SANS -ErrorAction Stop → le catch ne se déclenche pas
try { Get-Service "Absent" }               # ❌ erreur non-terminante, catch ignoré
catch { "attrapé" }
try { Get-Service "Absent" -ErrorAction Stop }   # ✅ catch fonctionne
catch { "attrapé" }

# Choisir le bon indicateur après un .exe
ping SRV01; if (-not $?) { }               # ⚠️ marche, mais moins informatif (pas le code exact)
ping SRV01; if ($LASTEXITCODE -ne 0) { }   # ✅ code exact du programme externe

# Vérifier $? trop tard
Get-Service Spooler
Write-Host "ok"
$?                                          # ❌ reflète Write-Host, pas Get-Service
```

## 💡 Exercices

**Guidé :** Écris un script qui tente `Restart-Service -Name $ServiceName -ErrorAction Stop` dans un `try/catch` et affiche un message vert en cas de succès, rouge (avec `$_.Exception.Message`) en cas d'échec.

**Autonome :** Reprends ton script de supervision de services (Ch.6) et entoure chaque vérification d'un `try/catch` pour qu'un service inexistant n'interrompe pas la boucle. Ajoute `Set-StrictMode -Version Latest` en tête.

## 🧩 Capstone Partie I — `Get-ServerHealth.ps1`

Assemble tout ce que tu as appris dans un outil complet :

- **Paramètres** (`-ComputerName` avec tableau possible, `-MinFreeGB`) — Ch.3
- Une **fonction** `Test-ServerHealth` documentée (aide par commentaires) — Ch.7
- Un **pipeline** qui produit un PSCustomObject par serveur (nom, en ligne, espace disque, uptime, statut global) — Ch.4, Ch.6
- Des **conditions** pour déterminer le statut (OK / Alerte) — Ch.5
- Un **try/catch** par serveur pour la robustesse + `Set-StrictMode` — Ch.8
- Un **export CSV** du rapport final

C'est le premier vrai outil d'administration du cours. On le fera évoluer : disque (Ch.14), réseau (Ch.18), exécution à distance (Ch.29).

## ✅ Tu sais maintenant...

- La différence **erreur terminante / non-terminante** et pourquoi `-ErrorAction Stop` est indispensable
- `try` / `catch` / `finally` pour intercepter et nettoyer
- `$?` = succès **booléen** de la dernière opération (cmdlet **ou** natif) ; `$LASTEXITCODE` = **code numérique exact** du dernier programme natif
- `$Error`, les flux `Write-Verbose`/`Warning`/`Error`/`Debug`
- `Set-StrictMode` et l'aide par commentaires

## 💬 Questions d'entretien typiques

- **Pourquoi un `try/catch` ne capture-t-il parfois rien ?** → Parce que l'erreur est non-terminante ; il faut `-ErrorAction Stop` pour la rendre terminante.
- **Différence entre `$?` et `$LASTEXITCODE` ?** → `$?` = succès booléen de la dernière opération, cmdlet **ou** exécutable (`$true` si code 0 pour un natif) ; `$LASTEXITCODE` = code de sortie **numérique exact** du dernier exécutable externe. Pour tester finement un `.exe`, on utilise `$LASTEXITCODE`.
- **Comment éviter qu'un serveur injoignable casse une boucle sur tout un parc ?** → Mettre le traitement de chaque serveur dans un `try/catch` avec `-ErrorAction Stop`, pour isoler les échecs.
- **À quoi sert `Set-StrictMode` ?** → À transformer en erreurs les pièges silencieux (variables/propriétés inexistantes), ce qui fiabilise les scripts.

---

# PARTIE II — ADMINISTRATION WINDOWS LOCALE

À partir d'ici, PowerShell devient réellement un outil d'administration. On applique tout ce qu'on a appris (pipeline, objets, conditions, boucles, fonctions, gestion d'erreurs) à la gestion concrète d'un poste Windows : fichiers et permissions, comptes locaux, processus et services, registre, tâches planifiées, disques et logiciels.

Le fil conducteur de cette partie : **`Get`/`Test` d'abord, puis `Set`/`New`/`Remove`**. On regarde toujours avant de modifier.

---

# Chapitre 9 — Fichiers, dossiers et permissions NTFS

## 🟢 Le minimum à savoir

### Lister et explorer

```powershell
Get-ChildItem C:\Scripts                 # contenu d'un dossier (alias : ls, dir)
Get-ChildItem C:\Scripts -Recurse        # récursif (sous-dossiers inclus)
Get-ChildItem C:\Scripts -File           # seulement les fichiers
Get-ChildItem C:\Scripts -Directory      # seulement les dossiers
Get-ChildItem C:\Logs -Filter *.log      # filtrés par motif
Get-Item C:\Scripts\run.ps1              # UN élément précis
```

`Get-ChildItem` renvoie des objets `FileInfo`/`DirectoryInfo`. Réflexe :

```powershell
Get-ChildItem C:\Scripts | Get-Member    # propriétés : Name, FullName, Length, LastWriteTime...
```

> **📌 Réflexe `Get-Member` :** un fichier n'est pas un nom, c'est un objet riche. `Length` (taille en octets), `CreationTime`, `LastWriteTime`, `Extension`, `FullName`, `Attributes`… autant de propriétés exploitables dans un tri, un filtre, un rapport.

### Lire et écrire du contenu

```powershell
# Lire
Get-Content C:\Logs\app.log                       # tout le fichier (comme cat)
Get-Content C:\Logs\app.log -TotalCount 10        # 10 premières lignes (head)
Get-Content C:\Logs\app.log -Tail 20              # 20 dernières lignes (tail)
Get-Content C:\Logs\app.log -Tail 20 -Wait        # suit les ajouts en direct (tail -f)

# Écrire
Set-Content C:\out.txt -Value "ligne" -Encoding UTF8    # écrase (comme >)
Add-Content C:\out.txt -Value "ajout" -Encoding UTF8    # ajoute (comme >>)
```

> **⚠️ Encodage — un piège selon la version.** En **Windows PowerShell 5.1**, l'encodage par défaut de `Set-Content`/`Out-File` n'est pas UTF-8 (c'est souvent de l'ANSI ou de l'UTF-16), ce qui casse les accents dans d'autres outils. En **PowerShell 7**, le défaut est l'UTF-8 (sans BOM). Pour être tranquille et **portable entre versions**, précise **toujours** `-Encoding UTF8`.

### Manipuler les chemins

```powershell
Join-Path C:\Scripts "logs\run.log"       # construit "C:\Scripts\logs\run.log"
Split-Path C:\Scripts\run.ps1 -Leaf        # "run.ps1"
Split-Path C:\Scripts\run.ps1 -Parent      # "C:\Scripts"
Test-Path C:\Scripts                        # le chemin existe ? (True/False)
Test-Path C:\Scripts -PathType Container    # est-ce un dossier ?
```

> **Bonne pratique :** construis toujours tes chemins avec `Join-Path` plutôt qu'en collant des chaînes avec `\`. Ça évite les doubles `\\` ou les séparateurs manquants, et reste correct quel que soit le contexte.

### Créer, copier, déplacer, supprimer

```powershell
New-Item -ItemType Directory -Path C:\Scripts\archive -Force    # créer un dossier
New-Item -ItemType File -Path C:\Scripts\notes.txt             # créer un fichier
Copy-Item C:\a.txt C:\backup\a.txt                             # copier
Copy-Item C:\src\* C:\dst\ -Recurse                            # copier récursif
Move-Item C:\a.txt C:\archive\a.txt                            # déplacer / renommer
Remove-Item C:\vieux.txt                                       # supprimer
Remove-Item C:\vieuxdossier -Recurse -Force                    # supprimer un dossier
```

> **📌 `Test` avant d'agir :** `if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst }` — on vérifie l'existence avant de créer. Et `Remove-Item -Recurse -Force` est **irréversible** : pas de corbeille. Vérifie toujours ton chemin avant.

## 🟡 Très utile en pratique

### CSV et JSON natifs (rappel et approfondissement)

On l'a vu au Ch.4 : PowerShell lit le CSV comme des **objets** et le JSON aussi. C'est un atout majeur pour l'administration.

```powershell
# CSV → objets (chaque ligne devient un objet avec des propriétés nommées)
$users = Import-Csv C:\users.csv -Encoding UTF8
$users | Where-Object { $_.Ville -eq "Paris" }

# objets → CSV
Get-Service | Select-Object Name, Status |
    Export-Csv C:\services.csv -NoTypeInformation -Encoding UTF8

# JSON
$config = Get-Content C:\config.json -Encoding UTF8 | ConvertFrom-Json
$config.ServerName
@{ Server = "SRV01"; Port = 8080 } | ConvertTo-Json | Set-Content C:\config.json -Encoding UTF8
```

On réutilisera intensivement `Import-Csv` pour créer des utilisateurs AD en masse (Ch.24).

### Les permissions NTFS : `Get-Acl` / `Set-Acl`

Sur un volume NTFS, chaque fichier et dossier porte une **ACL** (Access Control List) — la liste de qui a le droit de faire quoi. Comprendre les ACL est fondamental en administration Windows.

Le vocabulaire minimal :

- **ACL** : la liste complète des permissions d'un objet
- **ACE** (Access Control Entry) : une entrée de cette liste — « tel utilisateur/groupe a tel droit, en Allow ou en Deny »
- **Allow / Deny** : autoriser ou refuser (un `Deny` l'emporte sur un `Allow`)
- **Héritage** : par défaut, un fichier hérite des permissions de son dossier parent
- **Propriétaire (Owner)** : le compte propriétaire de l'objet, qui peut toujours modifier ses permissions

```powershell
# LIRE les permissions d'un dossier
$acl = Get-Acl C:\Partages\Compta
$acl.Owner                       # le propriétaire
$acl.Access                      # la liste des ACE

# Afficher proprement qui a quoi
(Get-Acl C:\Partages\Compta).Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType, IsInherited
```

> **📌 Réflexe `Get-Member` :** `(Get-Acl C:\Partages\Compta).Access | Get-Member` te montre les propriétés d'une ACE (`IdentityReference` = qui, `FileSystemRights` = quel droit, `AccessControlType` = Allow/Deny, `IsInherited` = hérité ou explicite).

Modifier une ACL est plus délicat (on manipule des objets .NET). Le schéma général — **toujours en lisant l'ACL d'abord, en la modifiant, puis en la réappliquant** :

```powershell
$acl = Get-Acl C:\Partages\Compta                              # 1. lire
$regle = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "lab\Comptables", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.AddAccessRule($regle)                                     # 2. modifier en mémoire
Set-Acl -Path C:\Partages\Compta -AclObject $acl              # 3. réappliquer   [🔑 Admin]
```

> **⚠️ Prudence extrême avec `Set-Acl`.** Une mauvaise manipulation d'ACL peut verrouiller un dossier pour tout le monde (y compris toi) ou, à l'inverse, l'ouvrir trop largement. Règles de survie : **lis et sauvegarde l'ACL existante avant** (`Get-Acl ... | Export-Clixml sauvegarde.xml`), teste sur un dossier bac à sable, et privilégie la gestion des droits via des **groupes** plutôt que des utilisateurs individuels. On reverra la distinction **permissions NTFS vs permissions de partage SMB** au Ch.28 — ce sont deux couches différentes qui se combinent.

## 🔴 Bonus

### Rechercher dans des fichiers : `Select-String`

L'équivalent de `grep` :

```powershell
Select-String -Path C:\Logs\*.log -Pattern "ERROR"          # lignes contenant ERROR
Select-String -Path C:\Logs\*.log -Pattern "fail" -Context 2  # avec 2 lignes de contexte
```

Renvoie des objets `MatchInfo` (fichier, numéro de ligne, ligne) — donc filtrables et exploitables.

### Prendre possession d'un dossier

Si tu n'as plus accès à un dossier, `takeown` (exécutable) puis `Set-Acl` permettent de reprendre la main — opération sensible, réservée aux cas de récupération, en `[🔑 Admin]`.

## ❌ Erreur classique

```powershell
# Oublier -Encoding UTF8 (accents cassés, surtout en 5.1)
Set-Content out.txt -Value "éàü"                   # ⚠️ selon la version
Set-Content out.txt -Value "éàü" -Encoding UTF8    # ✅

# Coller des chemins à la main
$p = "C:\Scripts" + "\" + $nom                     # ⚠️ fragile
$p = Join-Path C:\Scripts $nom                     # ✅

# Supprimer sans vérifier (pas de corbeille !)
Remove-Item C:\Data -Recurse -Force                # ❌ irréversible si mauvais chemin
if (Test-Path C:\Data) { Remove-Item C:\Data -Recurse -Force -WhatIf }   # ✅ teste d'abord

# Modifier une ACL sans l'avoir sauvegardée
Set-Acl ...                                        # ❌ sans filet
Get-Acl C:\D | Export-Clixml backup.xml; Set-Acl ...   # ✅
```

## 💡 Exercices

**Guidé :** Écris un script qui liste les fichiers d'un dossier (paramètre `-Path`) de plus de 100 Mo, triés par taille décroissante, avec nom et taille en Mo (propriété calculée).

**Autonome :** Écris un script qui affiche les ACE d'un dossier (`-Path`) sous forme de tableau lisible : qui (`IdentityReference`), quel droit (`FileSystemRights`), Allow/Deny, hérité ou non.

## 🧩 Mini-projet — Inventaire de dossier

Crée `Get-FolderReport.ps1` (paramètre `-Path`, `-OutputPath`) qui parcourt un dossier, produit un PSCustomObject par fichier (Nom, Extension, TailleMo, ModifieLe), exporte en CSV, et affiche un résumé (nombre de fichiers, taille totale, plus gros fichier). Réutilise pipeline, propriétés calculées, `Measure-Object` et `Export-Csv`.

## ✅ Tu sais maintenant...

- Explorer et manipuler fichiers/dossiers (`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`)
- Construire des chemins proprement (`Join-Path`, `Split-Path`, `Test-Path`)
- **Toujours** préciser `-Encoding UTF8` (piège 5.1 vs 7)
- Lire et exporter CSV/JSON nativement
- Lire les permissions NTFS avec `Get-Acl` (ACL, ACE, Allow/Deny, héritage, propriétaire) et la prudence requise pour `Set-Acl`

## 💬 Questions d'entretien typiques

- **Pourquoi toujours mettre `-Encoding UTF8` ?** → Parce que le défaut varie (5.1 ≠ 7) et casse les accents ; UTF-8 explicite rend le résultat portable.
- **Qu'est-ce qu'une ACE ?** → Une entrée d'ACL : un couple (identité, droit) en Allow ou Deny, hérité ou explicite.
- **Comment modifier des permissions sans risque ?** → Sauvegarder l'ACL (`Get-Acl | Export-Clixml`), travailler par groupes, tester sur un bac à sable, puis `Set-Acl`.

---

# Chapitre 10 — Utilisateurs et groupes locaux

## 🟢 Le minimum à savoir

### Comptes locaux vs comptes de domaine

Une machine Windows a des **comptes locaux** (définis sur la machine elle-même). Dans un domaine, il existe aussi des **comptes AD** (centralisés, vus en Partie IV). Ce chapitre traite les **comptes locaux** — gérés par le module `Microsoft.PowerShell.LocalAccounts`.

> **Note :** ces cmdlets `*-LocalUser` / `*-LocalGroup` fonctionnent sur Windows 10/11 et Windows Server. Elles agissent sur la base SAM locale, pas sur l'annuaire du domaine.

### Lister les utilisateurs et groupes locaux

```powershell
Get-LocalUser                        # tous les comptes locaux
Get-LocalUser -Name Administrateur   # un compte précis
Get-LocalGroup                       # tous les groupes locaux
Get-LocalGroupMember -Group "Administrateurs"   # membres du groupe Administrateurs
```

> **📌 Réflexe `Get-Member` :** `Get-LocalUser | Get-Member` révèle `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, `SID`… Autant de propriétés pour auditer les comptes.

### Le cas d'usage n°1 : auditer les administrateurs locaux

Qui est administrateur local d'une machine ? C'est une **question de sécurité fondamentale** — trop d'admins locaux = surface d'attaque.

```powershell
Get-LocalGroupMember -Group "Administrateurs" |
    Select-Object Name, PrincipalSource, ObjectClass
```

`PrincipalSource` indique si le membre est local ou vient du domaine ; `ObjectClass` s'il s'agit d'un utilisateur ou d'un groupe.

> **Note langue :** le groupe s'appelle `Administrateurs` sur un Windows en français, `Administrators` en anglais. Pour un script portable, on peut cibler par SID : le groupe Administrateurs a toujours le SID `S-1-5-32-544`. `Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"`.

### Créer, modifier, désactiver un compte local `[🔑 Admin]`

**Discipline `Get`/`Test` avant d'agir** : on vérifie qu'un compte n'existe pas avant de le créer.

```powershell
# 1. Vérifier
if (-not (Get-LocalUser -Name "svc_backup" -ErrorAction SilentlyContinue)) {

    # 2. Créer un compte technique (mot de passe en SecureString — voir Ch.33)
    $pwd = Read-Host "Mot de passe" -AsSecureString
    New-LocalUser -Name "svc_backup" -Password $pwd `
        -FullName "Compte de sauvegarde" -Description "Service backup" `
        -PasswordNeverExpires
}

# Modifier
Set-LocalUser -Name "svc_backup" -Description "Compte technique sauvegarde"

# Désactiver / réactiver (préférable à la suppression pour garder une trace)
Disable-LocalUser -Name "svc_backup"
Enable-LocalUser  -Name "svc_backup"
```

> **Bonne pratique :** on **désactive** plutôt qu'on supprime un compte quand on n'en est pas sûr — la suppression est définitive et fait perdre le SID (donc l'historique des permissions). C'est la même logique que le « soft delete » en base de données.

### Gérer l'appartenance aux groupes `[🔑 Admin]`

```powershell
Add-LocalGroupMember    -Group "Administrateurs" -Member "svc_backup"
Remove-LocalGroupMember -Group "Administrateurs" -Member "svc_backup"
```

## 🟡 Très utile en pratique

### Auditer tous les comptes actifs

```powershell
Get-LocalUser | Where-Object Enabled |
    Select-Object Name, LastLogon, PasswordExpires |
    Sort-Object LastLogon
```

Repérer un compte activé jamais connecté, ou un mot de passe qui n'expire jamais, est un réflexe d'hygiène de sécurité.

### Produire un rapport de tous les groupes et leurs membres

```powershell
Get-LocalGroup | ForEach-Object {
    $grp = $_.Name
    Get-LocalGroupMember -Group $grp -ErrorAction SilentlyContinue | ForEach-Object {
        [PSCustomObject]@{
            Groupe = $grp
            Membre = $_.Name
            Type   = $_.ObjectClass
            Source = $_.PrincipalSource
        }
    }
} | Export-Csv C:\audit_groupes.csv -NoTypeInformation -Encoding UTF8
```

Ce pattern (boucler sur des groupes, produire des objets, exporter) est directement transposable à l'audit AD (Ch.21).

## 🔴 Bonus

### Le compte administrateur intégré

Le compte `Administrateur` (SID se terminant par `-500`) est souvent désactivé par défaut sur les postes modernes. On peut le repérer :

```powershell
Get-LocalUser | Where-Object { $_.SID -like "*-500" }
```

Un compte `-500` **activé** et renommé est un point d'attention en sécurité.

## ❌ Erreur classique

```powershell
# Cibler "Administrators" en dur sur un Windows en français
Get-LocalGroupMember -Group "Administrators"    # ❌ échoue en FR
Get-LocalGroupMember -Group "Administrateurs"   # ✅ (ou cibler par SID S-1-5-32-544)

# Supprimer un compte au lieu de le désactiver
Remove-LocalUser -Name "ancien"    # ⚠️ définitif, perte du SID
Disable-LocalUser -Name "ancien"   # ✅ réversible, garde la trace

# Créer un compte sans vérifier son existence
New-LocalUser -Name "svc"          # ❌ erreur si déjà présent
if (-not (Get-LocalUser svc -ErrorAction SilentlyContinue)) { New-LocalUser ... }   # ✅
```

## 💡 Exercices

**Guidé :** Affiche les membres du groupe Administrateurs locaux avec leur type et leur source. Cible le groupe par son SID pour être portable.

**Autonome :** Écris un script qui liste tous les comptes locaux activés dont le mot de passe n'expire jamais (`PasswordExpires -eq $null`) — un point d'audit de sécurité classique.

## 🧩 Mini-projet — Audit des comptes locaux

Crée `Get-LocalAccountAudit.ps1` qui produit un rapport CSV : tous les comptes locaux avec `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, et une colonne `EstAdmin` (True si le compte est membre du groupe Administrateurs). Réutilise `Get-LocalUser`, `Get-LocalGroupMember`, PSCustomObject et `Export-Csv`.

## ✅ Tu sais maintenant...

- La différence comptes locaux / comptes de domaine
- Lister, créer, modifier, désactiver des comptes locaux (`*-LocalUser`)
- Gérer les groupes locaux et leurs membres (`*-LocalGroup*`)
- Auditer les administrateurs locaux (par nom ou par SID, pour la portabilité)
- Préférer **désactiver** à **supprimer**

## 💬 Questions d'entretien typiques

- **Pourquoi désactiver plutôt que supprimer un compte ?** → Réversible, conserve le SID et l'historique des permissions.
- **Comment auditer les admins locaux de façon portable (FR/EN) ?** → Cibler le groupe par SID `S-1-5-32-544` plutôt que par son nom.
- **Différence compte local / compte de domaine ?** → Le compte local vit dans la base SAM de la machine ; le compte de domaine est centralisé dans Active Directory.

---

# Chapitre 11 — Processus et services

## 🟢 Le minimum à savoir

### Processus vs services : la distinction

- Un **processus** est un programme en cours d'exécution (une instance de `chrome.exe`, `notepad.exe`…). Il a un **PID** (identifiant numérique).
- Un **service** est un programme qui tourne en **arrière-plan**, souvent sans interface, géré par Windows (démarrage automatique, redémarrage en cas d'échec…). Le pare-feu, Windows Update, le spouleur d'impression sont des services.

Un service, quand il tourne, s'exécute *via* un ou plusieurs processus — mais on les gère avec des cmdlets différentes.

### Gérer les processus

```powershell
Get-Process                          # tous les processus
Get-Process -Name chrome             # par nom
Get-Process -Id 1234                 # par PID

# Les 5 plus gros consommateurs de mémoire
Get-Process | Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{N="RAM(Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 5

# Lancer / arrêter
Start-Process notepad
Start-Process "C:\outil.exe" -ArgumentList "/silent"
Stop-Process -Name notepad
Stop-Process -Id 1234 -Force
```

> **📌 Réflexe `Get-Member` :** `Get-Process | Get-Member` révèle `Id`, `Name`, `CPU`, `WorkingSet64` (mémoire), `Path`, `StartTime`, et des méthodes comme `.Kill()`. Un processus est un objet riche — on peut trier, filtrer, corréler.

> **⚠️ `Stop-Process` est brutal :** il tue le processus sans sauvegarde (comme `kill -9`). Vérifie le PID/nom avant. Certains processus système protégés nécessitent `[🔑 Admin]`.

### Gérer les services

```powershell
Get-Service                           # tous les services
Get-Service -Name wuauserv            # un service précis (Windows Update)
Get-Service | Where-Object Status -eq "Running"    # ceux qui tournent

# Contrôler un service                                   [🔑 Admin]
Start-Service   -Name wuauserv
Stop-Service    -Name wuauserv
Restart-Service -Name wuauserv

# Changer le type de démarrage                           [🔑 Admin]
Set-Service -Name wuauserv -StartupType Automatic   # Automatic / Manual / Disabled
```

Les propriétés clés d'un service : `Name`, `DisplayName`, `Status` (Running/Stopped), `StartType` (Automatic/Manual/Disabled), `DependentServices`, `ServicesDependedOn`.

### Le point à investiguer : Automatic + Stopped

Un service configuré en démarrage **automatique** mais actuellement **arrêté** est un **point à investiguer** — pas nécessairement une panne :

```powershell
# Version portable 5.1 et 7 via CIM (StartMode = "Auto" pour les services automatiques)
Get-CimInstance Win32_Service |
    Where-Object { $_.StartMode -eq "Auto" -and $_.State -eq "Stopped" } |
    Select-Object Name, DisplayName, StartMode, State
```

> **⚠️ Nuance importante — « Automatic + Stopped » n'est pas toujours une anomalie.** Windows gère des services **déclenchés par événement** (*trigger-start*) : un service peut être configuré en automatique (ou automatique-différé), démarrer quand un événement survient, puis **s'arrêter légitimement** quand il n'a plus de travail. Le voir `Stopped` à un instant donné peut être parfaitement normal. Microsoft recommande même ce modèle *trigger-start* dans certains scénarios.
>
> La bonne façon de raisonner la **conformité** n'est donc pas « tout service Automatic doit être Running », mais : **comparer l'état observé à une baseline attendue** (la liste des services qui, chez toi, *doivent* tourner en permanence). Un service critique attendu en fonctionnement continu et trouvé arrêté = à investiguer ; un service *trigger-start* arrêté = souvent normal.

C'est un contrôle de santé que tout administrateur fait régulièrement — en gardant cette nuance à l'esprit.

### Les dépendances de services

Certains services en requièrent d'autres. Le savoir évite les mauvaises surprises quand on en arrête un :

```powershell
(Get-Service -Name wuauserv).ServicesDependedOn    # ce dont dépend Windows Update
(Get-Service -Name rpcss).DependentServices         # ce qui dépend de RPCSS
```

> **Piège :** arrêter un service dont dépendent d'autres services les arrête aussi (avec `-Force`) ou échoue (sans). Toujours vérifier `DependentServices` avant un `Stop-Service`.

## 🟡 Très utile en pratique

### `Get-Service` vs `Get-CimInstance Win32_Service`

`Get-Service` est simple mais limité. Pour obtenir le **compte de service**, le **chemin de l'exécutable** ou le **PID**, on passe par CIM :

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName, PathName |
    Where-Object { $_.StartName -notlike "*LocalSystem*" }
```

`StartName` (le compte sous lequel tourne le service) et `PathName` (le binaire) sont essentiels en administration **et** en sécurité — un service tournant depuis un chemin inhabituel est suspect (on approfondit au Ch.34).

### Un contrôle de santé de services critiques

```powershell
function Test-CriticalServices {
    [CmdletBinding()]
    param([string[]]$Services = @("wuauserv","WinDefend","EventLog","Spooler"))

    foreach ($nom in $Services) {
        $svc = Get-Service -Name $nom -ErrorAction SilentlyContinue
        # StartMode via CIM = portable 5.1 et 7 (contrairement à $svc.StartType, PS7 seulement)
        $cim = Get-CimInstance Win32_Service -Filter "Name='$nom'" -ErrorAction SilentlyContinue
        [PSCustomObject]@{
            Service   = $nom
            Present   = [bool]$svc
            Statut    = if ($svc) { $svc.Status } else { "ABSENT" }
            Demarrage = if ($cim) { $cim.StartMode } else { "-" }   # Auto / Manual / Disabled
        }
    }
}

Test-CriticalServices | Format-Table -AutoSize
```

Ce petit outil réunit fonctions (Ch.7), gestion d'absence (Ch.8), collections (Ch.6) et PSCustomObject. Il utilise `Win32_Service`.`StartMode` pour rester portable entre Windows PowerShell 5.1 et PowerShell 7.

## 🔴 Bonus

### Processus et leur ligne de commande complète

La ligne de commande exacte d'un processus (arguments inclus) est précieuse pour le diagnostic :

```powershell
Get-CimInstance Win32_Process -Filter "Name = 'powershell.exe'" |
    Select-Object ProcessId, CommandLine
```

Un `powershell.exe` lancé avec des arguments encodés en base64 est un signal d'alerte (Ch.34).

## ❌ Erreur classique

```powershell
# Arrêter un service sans vérifier ses dépendances
Stop-Service RPCSS            # ❌ échoue ou casse une cascade de services
(Get-Service RPCSS).DependentServices   # ✅ vérifier d'abord

# Utiliser Get-Service quand on a besoin du chemin/compte du service
Get-Service wuauserv | Select-Object Path    # ❌ pas de propriété Path
Get-CimInstance Win32_Service -Filter "Name='wuauserv'" | Select PathName, StartName  # ✅

# Tuer un processus par nom alors que plusieurs instances tournent
Stop-Process -Name chrome     # ⚠️ tue TOUTES les instances de Chrome
```

## 💡 Exercices

**Guidé :** Affiche les services en démarrage automatique actuellement arrêtés, triés par nom.

**Autonome :** Écris un script qui prend un `-ServiceName`, vérifie ses dépendances (`ServicesDependedOn`), et n'affiche un message de redémarrage possible que si toutes ses dépendances sont `Running`.

## 🧩 Mini-projet — Rapport de services critiques

Étends `Test-CriticalServices` : la conformité se juge **par rapport à une baseline** que tu définis (les services qui, chez toi, doivent tourner en permanence). Ajoute une colonne `Conforme` (True si un service **attendu en fonctionnement** est bien `Running`), affiche en couleur les non-conformes, et exporte le rapport complet en CSV horodaté (`services_$(Get-Date -Format yyyyMMdd).csv`). Note que « Automatic + Stopped » seul ne suffit pas à conclure : compare à ta liste attendue.

## ✅ Tu sais maintenant...

- La différence processus / service
- Gérer les processus (`Get/Start/Stop-Process`) et les services (`Get/Start/Stop/Restart/Set-Service`)
- Repérer le point à investiguer « Automatic + Stopped » — en le comparant à une baseline (pas une anomalie automatique, à cause des services *trigger-start*)
- Vérifier les dépendances avant d'arrêter un service
- Passer par `Win32_Service` pour le compte et le chemin d'un service

## 💬 Questions d'entretien typiques

- **Différence entre un processus et un service ?** → Un processus est un programme en cours ; un service tourne en arrière-plan sous le contrôle du gestionnaire de services (démarrage auto, resilience).
- **Comment obtenir le chemin du binaire d'un service ?** → `Get-CimInstance Win32_Service` (propriété `PathName`), car `Get-Service` ne l'expose pas.
- **Quel contrôle de santé faire sur les services ?** → Comparer l'état à une baseline : les services *attendus en fonctionnement continu* doivent être `Running`. « Automatic + Stopped » est un point à investiguer, mais pas une anomalie en soi (services *trigger-start*).

---

# Chapitre 12 — Le registre Windows

## 🟢 Le minimum à savoir

### Qu'est-ce que le registre ?

Le registre est la **base de données de configuration** de Windows. On y trouve les réglages du système, des logiciels, des associations de fichiers, des politiques de sécurité, et — ce qui intéressera la Partie VIII — des mécanismes de démarrage automatique.

PowerShell traite le registre **comme un système de fichiers** : mêmes cmdlets que pour les dossiers.

### Les ruches principales

```powershell
Get-PSDrive -PSProvider Registry    # les "lecteurs" du registre
```

| Ruche | Abréviation | Contenu |
|-------|-------------|---------|
| `HKEY_CURRENT_USER` | `HKCU:` | Configuration de l'utilisateur **courant** |
| `HKEY_LOCAL_MACHINE` | `HKLM:` | Configuration de la **machine** (nécessite `[🔑 Admin]` pour écrire) |

### Lire le registre

```powershell
# Parcourir comme un dossier
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion"

# Lire TOUTES les valeurs d'une clé
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"

# Lire UNE valeur précise
Get-ItemPropertyValue "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName
```

> **📌 Réflexe `Test-Path` :** avant de lire ou d'écrire, `Test-Path "HKLM:\SOFTWARE\MonApp"` évite les erreurs sur une clé absente.

### Le concept de PSDrive : une abstraction unifiée

Le registre est un exemple de **PSDrive** — PowerShell présente plusieurs systèmes comme des « lecteurs » navigables avec les **mêmes** cmdlets (`Get-ChildItem`, `Get-ItemProperty`…) :

| PSDrive | Contenu |
|---------|---------|
| `C:`, `D:` | Système de fichiers |
| `HKCU:`, `HKLM:` | Registre |
| `Env:` | Variables d'environnement |
| `Cert:` | Certificats |
| `Variable:` | Variables PowerShell |

```powershell
Get-ChildItem Env:                       # toutes les variables d'environnement
Get-ChildItem Cert:\CurrentUser\My       # tes certificats personnels
```

C'est une idée puissante : apprendre `Get-ChildItem` une fois, l'utiliser partout.

### Modifier le registre `[🔑 Admin pour HKLM]`

**Discipline `Test`/`Get` avant `Set`/`New`** — et prudence maximale :

```powershell
# Créer une clé (si absente)
if (-not (Test-Path "HKCU:\Software\MonApp")) {
    New-Item -Path "HKCU:\Software\MonApp" -Force
}

# Créer une valeur avec son type explicite
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "dark" -PropertyType String
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Version" -Value 2 -PropertyType DWord

# Modifier une valeur existante
Set-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "light"

# Supprimer
Remove-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme"
Remove-Item -Path "HKCU:\Software\MonApp" -Recurse
```

Les types de valeurs courants : `String`, `DWord` (entier 32 bits), `QWord` (64 bits), `Binary`, `ExpandString`, `MultiString`.

> **⚠️ Le registre est critique — prudence maximale.** Une mauvaise modification de `HKLM:` peut empêcher Windows de démarrer. Règles de survie : travaille d'abord dans `HKCU:` (moins dangereux), **sauvegarde** la clé avant modification (`reg export`), et ne touche à `HKLM:` que si tu sais exactement ce que tu fais. `New-ItemProperty` pour créer (avec `-PropertyType`), `Set-ItemProperty` pour modifier.

## 🟡 Très utile en pratique

### Sauvegarder avant de modifier

```powershell
# Exporter une clé avant de la toucher (via l'outil reg.exe)
reg export "HKLM\SOFTWARE\MonApp" "C:\backup\MonApp.reg" /y
```

C'est le `Get`/backup avant `Set` appliqué au registre. Indispensable en production.

### Lire une information de configuration système

```powershell
# Version précise de Windows depuis le registre
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild
```

## 🔴 Bonus

### Les clés de démarrage automatique

Certaines clés lancent des programmes au démarrage — utile à connaître pour l'admin, essentiel pour la sécurité (persistance de malware, Ch.34) :

```powershell
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
```

> **Renvoi croisé :** on réutilise exactement ces clés `Run`/`RunOnce` au **Ch.34** pour le triage de persistance. Ici on les lit comme configuration ; là-bas on les analyse comme indicateur de compromission.

## ❌ Erreur classique

```powershell
# Écrire dans HKLM sans droits admin
Set-ItemProperty "HKLM:\..." -Name X -Value 1     # ❌ Accès refusé
# → console en administrateur

# Confondre New-ItemProperty (créer) et Set-ItemProperty (modifier)
Set-ItemProperty "HKCU:\Software\MonApp" -Name Nouveau -Value 1   # crée quand même,
# mais sans contrôle du type → préférer New-ItemProperty -PropertyType pour créer

# Modifier le registre sans sauvegarde
Set-ItemProperty "HKLM:\..."                       # ❌ sans filet
reg export "HKLM\..." backup.reg /y ; Set-ItemProperty ...   # ✅
```

## 💡 Exercices

**Guidé :** Lis et affiche `ProductName`, `DisplayVersion` et `CurrentBuild` depuis `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion`.

**Autonome :** Écris un script qui crée une clé `HKCU:\Software\MonLab`, y ajoute une valeur `String` et une valeur `DWord`, les relit pour vérifier, puis supprime la clé entière. Encadre chaque étape d'un `Test-Path`.

## ✅ Tu sais maintenant...

- Ce qu'est le registre et ses ruches (`HKCU:`, `HKLM:`)
- Le lire (`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`)
- Le modifier (`New-ItemProperty` pour créer avec type, `Set-ItemProperty` pour modifier)
- Le concept unificateur de **PSDrive** (fichiers, registre, Env:, Cert:…)
- La prudence : `HKCU:` d'abord, sauvegarde avant `HKLM:`

## 💬 Questions d'entretien typiques

- **Comment PowerShell voit-il le registre ?** → Comme un système de fichiers (un PSDrive), navigable avec `Get-ChildItem`, `Get-ItemProperty`…
- **Différence `HKCU:` / `HKLM:` ?** → `HKCU:` = config de l'utilisateur courant ; `HKLM:` = config machine, écriture réservée aux administrateurs.
- **`New-ItemProperty` ou `Set-ItemProperty` ?** → `New-ItemProperty` pour créer une valeur (avec `-PropertyType`), `Set-ItemProperty` pour en modifier une existante.

---

# Chapitre 13 — Tâches planifiées

## 🟢 Le minimum à savoir

### À quoi ça sert

Une **tâche planifiée** exécute un programme ou un script automatiquement : à heure fixe, au démarrage, à la connexion d'un utilisateur, ou sur événement. C'est l'équivalent Windows de `cron` sous Linux — et c'est ainsi qu'on **automatise** l'exécution de ses scripts PowerShell (sauvegardes, rapports, nettoyages).

### Lister et inspecter les tâches

```powershell
Get-ScheduledTask                                   # toutes les tâches
Get-ScheduledTask -TaskName "MaTache"               # une tâche
Get-ScheduledTask | Where-Object State -eq "Ready"  # les tâches actives

# Infos d'exécution (dernier/prochain lancement, dernier résultat)
Get-ScheduledTask -TaskName "MaTache" | Get-ScheduledTaskInfo
```

> **📌 Réflexe `Get-Member` :** `Get-ScheduledTask | Get-Member` montre `TaskName`, `TaskPath`, `State`, `Actions`, `Triggers`, `Principal`. Une tâche est un objet composé : elle contient des **actions** (quoi exécuter) et des **déclencheurs** (quand).

### Les 4 briques d'une tâche

Créer une tâche, c'est assembler quatre éléments :

1. **Action** — quoi exécuter (`New-ScheduledTaskAction`)
2. **Déclencheur (trigger)** — quand (`New-ScheduledTaskTrigger`)
3. **Principal** — sous quel compte et avec quels privilèges (`New-ScheduledTaskPrincipal`)
4. **Enregistrement** — assembler et créer (`Register-ScheduledTask`)

### Créer une tâche planifiée `[🔑 Admin]`

```powershell
# 1. Action : lancer un script PowerShell
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -File C:\Scripts\backup.ps1"

# 2. Déclencheur : tous les jours à 2h du matin
$trigger = New-ScheduledTaskTrigger -Daily -At "02:00"

# 3. Principal : exécuter en tant que SYSTEM, avec privilèges élevés
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

# 4. Enregistrer
Register-ScheduledTask -TaskName "BackupQuotidien" `
    -Action $action -Trigger $trigger -Principal $principal `
    -Description "Sauvegarde quotidienne à 2h"
```

> **Note sur l'argument :** pour lancer un script `.ps1`, on exécute `powershell.exe` (ou `pwsh.exe` en PS7) avec `-File`. `-NoProfile` (ignore le profil, pour un environnement prévisible) est une bonne habitude.
>
> **⚠️ À propos de `-ExecutionPolicy Bypass` :** on voit souvent `-ExecutionPolicy Bypass` ajouté ici par réflexe. **Ne l'utilise pas systématiquement.** Rappel du Ch.1 : l'Execution Policy n'est pas une frontière de sécurité, mais l'ajouter aveuglément dans chaque tâche est une mauvaise habitude qui banalise le contournement. La bonne approche : le script tourne sous une **policy correctement configurée** (souvent `RemoteSigned` imposée par GPO) ou, mieux, il est **signé** (Ch.35). Réserve `Bypass` à un choix **volontaire et justifié** dans un contexte contrôlé — pas à une recette copiée-collée partout.

### Supprimer une tâche

```powershell
Unregister-ScheduledTask -TaskName "BackupQuotidien" -Confirm:$false
```

## 🟡 Très utile en pratique

### Comprendre le contexte d'exécution

Une tâche s'exécute sous un **compte** avec un **niveau de privilège** — deux points cruciaux :

- **Le compte** (`-UserId`) : `SYSTEM` (tout-puissant local), un compte de service dédié, ou un utilisateur. Détermine les droits **et** l'accès réseau.
- **Le niveau** (`-RunLevel`) : `Limited` (normal) ou `Highest` (élevé). Un script qui touche à `HKLM:` ou aux services a besoin de `Highest`.
- **« Exécuter même si l'utilisateur n'est pas connecté »** : implique de stocker des identifiants — sujet sécurité (Ch.33).

> **Réflexe sécurité :** une tâche planifiée tournant en `SYSTEM` qui lance un script modifiable par tous est une porte d'entrée classique pour l'élévation de privilèges. On y revient au Ch.34 (triage de persistance) : les tâches planifiées sont un mécanisme de persistance très utilisé.

### Différents types de déclencheurs

```powershell
New-ScheduledTaskTrigger -Daily -At "02:00"                  # quotidien
New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At "8am"  # hebdomadaire
New-ScheduledTaskTrigger -AtStartup                          # au démarrage machine
New-ScheduledTaskTrigger -AtLogOn                            # à la connexion
```

## 🔴 Bonus

### Auditer les tâches non standard

```powershell
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, TaskPath, State,
        @{N="Action";E={$_.Actions.Execute}}
```

Filtrer les tâches hors `\Microsoft\*` fait ressortir celles ajoutées par des logiciels ou des humains — un bon point de départ pour un audit (et pour du triage de sécurité, Ch.34).

## ❌ Erreur classique

```powershell
# Ajouter -ExecutionPolicy Bypass par réflexe dans CHAQUE tâche
-Argument "-NoProfile -ExecutionPolicy Bypass -File C:\s.ps1"   # ⚠️ mauvaise habitude
# ✅ compter sur une policy correcte (GPO) ou un script signé ; Bypass = choix justifié seulement

# Créer une tâche SYSTEM lançant un script world-writable
# ❌ risque d'élévation de privilèges — protéger les ACL du script (Ch.9)

# Chemins relatifs dans une tâche
-Argument "-File .\backup.ps1"     # ❌ le dossier courant n'est pas garanti
-Argument "-File C:\Scripts\backup.ps1"   # ✅ chemin absolu
```

## 💡 Exercices

**Guidé :** Liste les tâches planifiées actives (`State -eq "Ready"`) qui ne sont pas dans `\Microsoft\`, avec leur nom et l'exécutable lancé.

**Autonome :** Crée une tâche `RapportHebdo` qui lance un script PowerShell tous les lundis à 8h, puis vérifie sa création avec `Get-ScheduledTaskInfo`, puis supprime-la.

## ✅ Tu sais maintenant...

- Le rôle des tâches planifiées (automatiser ses scripts, équivalent `cron`)
- Lister et inspecter (`Get-ScheduledTask`, `Get-ScheduledTaskInfo`)
- Les 4 briques : action, déclencheur, principal, enregistrement
- L'importance du **contexte d'exécution** (compte + niveau de privilège)
- Le lien avec la sécurité (persistance, à revoir Ch.34)

## 💬 Questions d'entretien typiques

- **Comment automatiser l'exécution quotidienne d'un script PowerShell ?** → Une tâche planifiée avec une action `powershell.exe -File ...` et un déclencheur `-Daily`.
- **Pourquoi le compte d'exécution d'une tâche est-il sensible ?** → Il détermine les privilèges ; une tâche `SYSTEM` lançant un script modifiable par tous permet une élévation de privilèges.
- **Équivalent de `cron` sous Windows ?** → Le Planificateur de tâches, piloté par les cmdlets `*-ScheduledTask*`.

---

# Chapitre 14 — Disques, volumes et stockage

## 🟢 Le minimum à savoir

### Les trois niveaux : disque, partition, volume

Le stockage Windows s'empile en trois couches, et les cmdlets suivent cette logique :

- **Disque** (`Get-Disk`) : le matériel physique (ou virtuel)
- **Partition** (`Get-Partition`) : une division d'un disque
- **Volume** (`Get-Volume`) : un système de fichiers monté, souvent avec une lettre (`C:`, `D:`)

```powershell
Get-Disk                     # les disques physiques
Get-Partition                # les partitions
Get-Volume                   # les volumes (avec espace libre !)
```

> **📌 Réflexe `Get-Member` :** `Get-Volume | Get-Member` révèle `DriveLetter`, `FileSystemLabel`, `Size`, `SizeRemaining`, `HealthStatus`. C'est `Get-Volume` qu'on utilise le plus, car il donne directement l'espace libre.

### Le cas d'usage n°1 : surveiller l'espace disque

C'est l'une des vérifications les plus fréquentes en administration. Un disque plein = services qui tombent, logs qui ne s'écrivent plus, serveur en panne.

```powershell
Get-Volume | Where-Object DriveLetter |
    Select-Object DriveLetter, FileSystemLabel,
        @{N="TailleGB";E={[math]::Round($_.Size/1GB,1)}},
        @{N="LibreGB";E={[math]::Round($_.SizeRemaining/1GB,1)}},
        @{N="Libre%";E={[math]::Round($_.SizeRemaining/$_.Size*100,1)}}
```

### Alerter sous un seuil

```powershell
$SeuilGB = 20

Get-Volume | Where-Object { $_.DriveLetter -and ($_.SizeRemaining/1GB) -lt $SeuilGB } |
    ForEach-Object {
        Write-Host "ALERTE $($_.DriveLetter): $([math]::Round($_.SizeRemaining/1GB,1)) Go libres" -ForegroundColor Red
    }
```

### `Get-PSDrive` : la vue rapide

`Get-PSDrive` donne une vue synthétique (et couvre aussi les lecteurs réseau) :

```powershell
Get-PSDrive -PSProvider FileSystem |
    Select-Object Name,
        @{N="LibreGB";E={[math]::Round($_.Free/1GB,1)}},
        @{N="UtiliséGB";E={[math]::Round($_.Used/1GB,1)}}
```

## 🟡 Très utile en pratique

### Santé des disques

```powershell
Get-Disk | Select-Object Number, FriendlyName, HealthStatus, OperationalStatus,
    @{N="TailleGB";E={[math]::Round($_.Size/1GB)}}
```

`HealthStatus` (`Healthy`/`Warning`/`Unhealthy`) est un indicateur de défaillance matérielle à surveiller.

### Intégrer l'espace disque à la fiche du poste

Souviens-toi de `Get-PosteInfo.ps1` (Ch.2). On peut maintenant y ajouter le disque :

```powershell
$c = Get-Volume -DriveLetter C
"Disque C: : $([math]::Round($c.SizeRemaining/1GB,1)) Go libres sur $([math]::Round($c.Size/1GB,1)) Go"
```

## 🔴 Bonus `[🖥️ Server]`

### Création de partitions et formatage

Sur un serveur, on peut initialiser et partitionner un nouveau disque — opérations **destructives**, à manier avec une extrême prudence :

```powershell
# Exemple (DESTRUCTIF) : initialiser le disque 1, créer une partition, formater
# Initialize-Disk -Number 1 -PartitionStyle GPT
# New-Partition -DiskNumber 1 -UseMaximumSize -AssignDriveLetter |
#     Format-Volume -FileSystem NTFS -NewFileSystemLabel "Data"
```

> **⚠️ `Format-Volume` et `Initialize-Disk` effacent les données.** Vérifie **trois fois** le numéro de disque (`Get-Disk`) avant. Une erreur de numéro formate le mauvais disque.

## ❌ Erreur classique

```powershell
# Confondre Size (octets) et affichage en Go (oubli de la division)
$v.Size            # ❌ un énorme nombre en octets
$v.Size / 1GB      # ✅ en gigaoctets

# Filtrer les volumes sans lettre (partitions système)
Get-Volume | Select DriveLetter, SizeRemaining    # ⚠️ inclut des volumes sans lettre
Get-Volume | Where-Object DriveLetter | ...        # ✅ seulement les volumes montés

# Se tromper de numéro de disque avant un formatage
Format-Volume ...    # ❌❌ vérifier Get-Disk avant, TOUJOURS
```

## 💡 Exercices

**Guidé :** Affiche tous les volumes avec lettre, leur taille, leur espace libre en Go et le pourcentage libre.

**Autonome :** Écris un script `-SeuilGB` (défaut 20) qui liste les volumes sous le seuil et renvoie un PSCustomObject par volume concerné (Lecteur, LibreGB, Pourcent). Exporte en CSV si au moins un volume est en alerte.

---

## Rôles, fonctionnalités et logiciels

Cette section clôt la Partie II en abordant l'inventaire du logiciel installé — côté client comme côté serveur.

### Rôles et fonctionnalités Windows Server `[🖥️ Server]`

Sur **Windows Server**, les capacités s'ajoutent sous forme de **rôles** (AD DS, DNS, DHCP, File Server…) et **fonctionnalités**. On les gère avec le module `ServerManager` :

```powershell
Get-WindowsFeature                                   # tout, avec l'état Installed/Available
Get-WindowsFeature | Where-Object Installed          # ce qui est installé
Install-WindowsFeature -Name DNS -IncludeManagementTools    # installer le rôle DNS  [🔑 Admin]
```

> **Important :** `Get-WindowsFeature` / `Install-WindowsFeature` n'existent **que sur Windows Server**, pas sur Windows 10/11. C'est ainsi qu'on installe les rôles qu'on administrera en Parties IV et V (AD, DNS, DHCP…).

### Fonctionnalités sur Windows 10/11

Côté **client**, l'équivalent passe par d'autres cmdlets :

```powershell
Get-WindowsOptionalFeature -Online                          # fonctionnalités optionnelles
Get-WindowsOptionalFeature -Online -FeatureName *Hyper-V*   # rechercher
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All   # activer  [🔑 Admin]
```

C'est ainsi qu'on active, par exemple, Hyper-V ou le client OpenSSH sur un poste.

### Inventorier les logiciels installés — SANS `Win32_Product`

Question fréquente : « quels logiciels sont installés ? ». La tentation est d'utiliser `Get-CimInstance Win32_Product`. **À éviter absolument.**

> **⚠️ Ne JAMAIS utiliser `Win32_Product` pour un inventaire.** Interroger cette classe déclenche, pour **chaque** logiciel MSI, une vérification de cohérence (une réparation à blanc) — c'est **lent** et surtout ça peut générer des milliers d'événements et **relancer des installations**. C'est un piège classique qui a causé de vrais incidents en production.

La bonne méthode : lire les clés de désinstallation du registre.

```powershell
$chemins = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

Get-ItemProperty $chemins -ErrorAction SilentlyContinue |
    Where-Object DisplayName |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Sort-Object DisplayName
```

Cette approche est **rapide et sûre** pour inventorier les applications **desktop enregistrées au niveau machine**, en 32 comme en 64 bits (grâce à `WOW6432Node`). C'est celle qu'utilisent les vrais outils d'inventaire.

> **Ce qu'elle ne couvre pas.** Deux angles morts à connaître : les logiciels installés **par utilisateur** (clé `HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*`, à ajouter si besoin), et les applications **AppX/MSIX** (applications du Microsoft Store et applications modernes), qui ont leur propre mécanisme d'inventaire :
> ```powershell
> Get-AppxPackage | Select-Object Name, Version, PackageFullName
> ```
> Un inventaire réellement exhaustif combine donc les clés `Uninstall` (machine + utilisateur) et `Get-AppxPackage`.

## ✅ Tu sais maintenant...

- Les trois couches disque / partition / volume et leurs cmdlets
- Surveiller l'espace disque et alerter sous un seuil (le cas d'usage n°1)
- Vérifier la santé des disques (`HealthStatus`)
- Installer des rôles/fonctionnalités (`Install-WindowsFeature` sur **Server** uniquement)
- Inventorier les logiciels **via le registre**, jamais avec `Win32_Product`

## 💬 Questions d'entretien typiques

- **Comment vérifier l'espace disque libre ?** → `Get-Volume` (propriété `SizeRemaining`) ou `Get-PSDrive`, avec un calcul en Go.
- **Pourquoi éviter `Win32_Product` ?** → Son interrogation déclenche une vérification/réparation de chaque MSI : lent et potentiellement perturbant. On lit plutôt les clés `Uninstall` du registre.
- **Où installe-t-on un rôle comme DNS ou AD DS ?** → Sur Windows Server, avec `Install-WindowsFeature` (indisponible sur les clients).

## 🧩 Capstone Partie II — Boîte à outils du poste local

Assemble un script `Get-LocalHealthReport.ps1` qui produit un rapport complet du poste, en réutilisant toute la Partie II :

- Infos système (Ch.2) et espace disque (Ch.14)
- Services critiques et leur conformité (Ch.11)
- Comptes administrateurs locaux (Ch.10)
- Tâches planifiées non-Microsoft (Ch.13)
- Le tout structuré en PSCustomObject, exporté en CSV, avec un résumé coloré à l'écran, et robuste aux erreurs (`try/catch`, Ch.8)

C'est la version « poste local » de l'outil que tu enrichiras avec le réseau (Partie III) puis l'exécution distante (Partie VI).

---

# PARTIE III — ADMINISTRATION RÉSEAU WINDOWS

Le réseau est le système nerveux de toute infrastructure. Cette partie t'apprend à inspecter et configurer le réseau d'un poste Windows avec PowerShell : interfaces, adresses IP, DNS, routes, connexions et pare-feu. On y remplace avantageusement les vieux outils (`ipconfig`, `ping`, `netstat`, `nslookup`) par des cmdlets qui renvoient des **objets** exploitables.

> **Comparaison Linux :** là où Linux utilise `ip`, `ping`, `ss`, `dig`, PowerShell offre `Get-NetIPConfiguration`, `Test-Connection`, `Get-NetTCPConnection`, `Resolve-DnsName`. Même logique, mais avec des objets au lieu de texte à parser.

---

# Chapitre 15 — Interfaces et configuration IP

## 🟢 Le minimum à savoir

### Voir la configuration réseau

La cmdlet à connaître en premier, qui remplace `ipconfig` :

```powershell
Get-NetIPConfiguration          # vue synthétique : interface, IP, passerelle, DNS
```

Pour aller dans le détail, trois cmdlets par couche :

```powershell
Get-NetAdapter                  # les cartes réseau (physiques/virtuelles) et leur état
Get-NetIPAddress                # les adresses IP configurées
Get-NetIPInterface              # les propriétés d'interface (DHCP on/off, métrique...)
```

> **📌 Réflexe `Get-Member` :** `Get-NetAdapter | Get-Member` révèle `Name`, `Status` (`Up`/`Disconnected`), `MacAddress`, `LinkSpeed`, `InterfaceIndex`. L'`InterfaceIndex` est la clé qui relie les cartes, adresses et routes entre elles.

### Lire l'adresse IPv4 d'une interface

```powershell
Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -ne "127.0.0.1" } |
    Select-Object InterfaceAlias, IPAddress, PrefixLength
```

Le `PrefixLength` est le masque en notation CIDR : `/24` = `255.255.255.0`.

### Les cartes réseau et leur état

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed, MacAddress

# Activer / désactiver une carte                          [🔑 Admin]
Disable-NetAdapter -Name "Ethernet" -Confirm:$false
Enable-NetAdapter  -Name "Ethernet"
```

### Configurer une IP statique `[🔑 Admin]`

**Discipline `Get` avant `Set`/`New`** : on lit la config actuelle avant de la changer.

```powershell
# 1. Regarder l'existant
Get-NetIPConfiguration -InterfaceAlias "Ethernet"

# 2. Supprimer l'ancienne IP si besoin, puis en créer une nouvelle
New-NetIPAddress -InterfaceAlias "Ethernet" `
    -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1

# (pour repasser en DHCP)
Set-NetIPInterface -InterfaceAlias "Ethernet" -Dhcp Enabled
```

> **⚠️ Attention en session distante :** changer l'IP d'une interface par laquelle tu es **connecté à distance** peut te couper l'accès à la machine. C'est un piège classique. Sur un serveur distant, on planifie ce genre de changement avec précaution (console physique/hors-bande disponible).

### DHCP vs statique

- **DHCP** : l'adresse est attribuée automatiquement par un serveur DHCP (Ch.27). C'est le cas des postes clients.
- **Statique** : l'adresse est fixée manuellement. C'est le cas des serveurs, imprimantes, équipements réseau.

```powershell
# L'interface est-elle en DHCP ?
Get-NetIPInterface -InterfaceAlias "Ethernet" -AddressFamily IPv4 |
    Select-Object InterfaceAlias, Dhcp
```

## 🟡 Très utile en pratique

### Une fiche réseau complète

```powershell
Get-NetIPConfiguration | ForEach-Object {
    [PSCustomObject]@{
        Interface = $_.InterfaceAlias
        Statut    = $_.NetAdapter.Status
        IPv4      = $_.IPv4Address.IPAddress
        Passerelle = $_.IPv4DefaultGateway.NextHop
        DNS       = ($_.DNSServer | Where-Object AddressFamily -eq 2).ServerAddresses -join ", "
    }
}
```

Ce PSCustomObject réunit interface, IP, passerelle et DNS — exactement ce qu'un admin veut voir d'un coup d'œil. On l'intègre au diagnostic réseau (mini-projet Ch.18).

## 🔴 Bonus

### Renommer une interface

```powershell
Rename-NetAdapter -Name "Ethernet 2" -NewName "LAN-Serveur"    # [🔑 Admin]
```

Nommer clairement ses interfaces (`LAN`, `DMZ`, `Backup`) facilite l'administration sur les serveurs multi-cartes.

## ❌ Erreur classique

```powershell
# Changer l'IP de l'interface qui te connecte à distance
New-NetIPAddress ...    # ❌ risque de te déconnecter du serveur

# Oublier -AddressFamily et mélanger IPv4/IPv6
Get-NetIPAddress | Select IPAddress    # ⚠️ mélange v4 et v6
Get-NetIPAddress -AddressFamily IPv4   # ✅

# Créer une IP sans supprimer l'ancienne → conflit / double IP
# Vérifier avec Get-NetIPAddress avant, retirer avec Remove-NetIPAddress si besoin
```

## 💡 Exercices

**Guidé :** Affiche, pour chaque interface active (`Status -eq "Up"`), son nom, son IPv4 et son débit (`LinkSpeed`).

**Autonome :** Écris un script qui produit la « fiche réseau » (PSCustomObject : Interface, IPv4, Passerelle, DNS) pour toutes les interfaces connectées, et l'exporte en CSV.

## ✅ Tu sais maintenant...

- `Get-NetIPConfiguration` (remplace `ipconfig`) et les cmdlets par couche (`Get-NetAdapter`, `Get-NetIPAddress`, `Get-NetIPInterface`)
- Lire IP, masque (PrefixLength), passerelle
- Configurer une IP statique ou repasser en DHCP — avec la prudence en session distante
- Construire une fiche réseau exploitable

## 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `ipconfig` ?** → `Get-NetIPConfiguration` (vue synthétique) ; `Get-NetIPAddress` pour le détail des adresses.
- **DHCP ou statique pour un serveur ?** → Statique en général, pour une adresse stable et prévisible.
- **Quel risque à reconfigurer l'IP à distance ?** → Se couper soi-même l'accès à la machine si on modifie l'interface de connexion.

---

# Chapitre 16 — DNS client et résolution

## 🟢 Le minimum à savoir

### Le DNS, en une phrase

Le **DNS** (Domain Name System) traduit les noms (`serveur.lab.local`, `google.com`) en adresses IP. Côté client, deux choses nous intéressent : **quels serveurs DNS** la machine utilise, et **comment résoudre** un nom.

### Voir et définir les serveurs DNS

```powershell
# Quels serveurs DNS utilise chaque interface ?
Get-DnsClientServerAddress -AddressFamily IPv4 |
    Select-Object InterfaceAlias, ServerAddresses

# Définir les serveurs DNS d'une interface                 [🔑 Admin]
# Machine jointe au domaine : UNIQUEMENT des DNS INTERNES (les DC/DNS du domaine)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" `
    -ServerAddresses "192.168.1.10"                 # un seul DC/DNS
# Avec deux contrôleurs/serveurs DNS internes :
# Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.1.10","192.168.1.11"

# Revenir au DNS automatique (via DHCP)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ResetServerAddresses
```

> **⚠️ Ne mets JAMAIS un DNS public (8.8.8.8…) sur un poste joint au domaine.** Une machine du domaine doit interroger **exclusivement les DNS internes**, seuls capables de résoudre les enregistrements AD (localisation des contrôleurs de domaine, services…). Mettre `8.8.8.8` en secondaire casse la résolution AD de façon intermittente (le client peut interroger le mauvais serveur). La résolution des **noms Internet** se fait ensuite via des **forwarders configurés côté serveur DNS** (Ch.26) — pas en ajoutant un DNS public sur le client. C'est un pré-requis pour tout le lab AD des parties IV-V.

### Résoudre un nom : `Resolve-DnsName`

L'équivalent moderne et puissant de `nslookup` :

```powershell
Resolve-DnsName google.com                       # résolution simple (A/AAAA)
Resolve-DnsName lab.local -Type A                # enregistrements A (IPv4)
Resolve-DnsName lab.local -Type MX               # serveurs mail
Resolve-DnsName 192.168.1.10 -Type PTR           # résolution inverse (IP → nom)
Resolve-DnsName dc01.lab.local -Server 192.168.1.10   # interroger un serveur précis
```

> **📌 Réflexe `Get-Member` :** `Resolve-DnsName google.com | Get-Member` montre que le résultat est un objet avec `Name`, `Type`, `IPAddress`, `TTL`. On peut donc filtrer et exploiter la réponse, contrairement au texte brut de `nslookup`.

> **Comparaison :** `Resolve-DnsName` ≈ `dig`/`nslookup` sous Linux, mais renvoie des objets. `-Type` sélectionne le type d'enregistrement (A, AAAA, MX, CNAME, PTR, TXT, NS…).

### Le cache DNS du client

Windows garde en cache les résolutions récentes :

```powershell
Get-DnsClientCache               # voir le cache
Clear-DnsClientCache             # vider le cache (équivaut à ipconfig /flushdns)
```

> **Cas pratique :** après un changement DNS côté serveur, un client peut continuer à résoudre l'ancienne IP tant que son cache n'est pas expiré. `Clear-DnsClientCache` règle ce genre de « pourquoi ça pointe encore vers l'ancienne adresse ? ».

## 🟡 Très utile en pratique

### Diagnostiquer une résolution qui échoue

```powershell
# 1. La machine a-t-elle des serveurs DNS configurés ?
Get-DnsClientServerAddress -AddressFamily IPv4 | Select InterfaceAlias, ServerAddresses

# 2. Le serveur DNS répond-il pour ce nom ?
Resolve-DnsName dc01.lab.local -Server 192.168.1.10 -ErrorAction SilentlyContinue

# 3. Le cache contient-il une vieille entrée ?
Get-DnsClientCache -Name "*lab.local*"
```

Cette séquence est un mini-arbre de décision de dépannage DNS très courant.

## 🔴 Bonus

### Comparer résolution interne et externe

Interroger explicitement deux serveurs DNS différents permet de repérer une incohérence (split-horizon, cache empoisonné, mauvaise configuration) :

```powershell
Resolve-DnsName intranet.lab.local -Server 192.168.1.10    # DNS interne
Resolve-DnsName intranet.lab.local -Server 8.8.8.8 -ErrorAction SilentlyContinue   # DNS public
```

## ❌ Erreur classique

```powershell
# Oublier de vider le cache après un changement DNS
# → le client résout encore l'ancienne IP
Clear-DnsClientCache    # ✅

# Confondre "pas de réponse DNS" et "hôte injoignable"
# Resolve-DnsName teste la RÉSOLUTION (nom→IP), pas la connectivité
# Pour la connectivité → Test-Connection / Test-NetConnection (Ch.17)

# Interroger le DNS système alors qu'on veut tester un serveur précis
Resolve-DnsName x.lab.local -Server 192.168.1.10   # ✅ cible explicite
```

## 💡 Exercices

**Guidé :** Affiche les serveurs DNS configurés sur chaque interface, puis résous `google.com` et affiche uniquement les adresses IPv4 (`Type -eq "A"`).

**Autonome :** Écris un script `-Name` qui résout un nom, et si la résolution échoue, affiche les serveurs DNS configurés et suggère de vider le cache. Utilise `try/catch`.

## ✅ Tu sais maintenant...

- Le rôle du DNS et comment voir/définir les serveurs DNS d'une interface
- Résoudre des noms avec `Resolve-DnsName` (types A, MX, PTR…) — objets exploitables
- Gérer le cache DNS (`Get`/`Clear-DnsClientCache`)
- Une séquence de diagnostic de résolution

## 💬 Questions d'entretien typiques

- **Quelle cmdlet remplace `nslookup` ?** → `Resolve-DnsName`, qui renvoie des objets (avec `-Type`, `-Server`).
- **Pourquoi vider le cache DNS ?** → Pour forcer une nouvelle résolution après un changement côté serveur (l'ancienne entrée peut persister).
- **`Resolve-DnsName` teste-t-il la connectivité ?** → Non, seulement la résolution nom→IP. La connectivité se teste avec `Test-Connection`/`Test-NetConnection`.

---

# Chapitre 17 — Routage et connexions

## 🟢 Le minimum à savoir

### Tester la connectivité : `Test-Connection` et `Test-NetConnection`

```powershell
# Ping simple (renvoie des objets, pas du texte) — forme positionnelle, valable 5.1 et 7
Test-Connection dc01.lab.local -Count 2

# Ping "booléen" pour un if
if (Test-Connection dc01.lab.local -Count 1 -Quiet) { "En ligne" }

# LE couteau suisse : Test-NetConnection (ping + test de PORT + route)
Test-NetConnection -ComputerName dc01.lab.local -Port 445    # le port SMB est-il ouvert ?
Test-NetConnection -ComputerName google.com -Port 443        # HTTPS accessible ?
```

> **Note version :** le nom du premier paramètre de `Test-Connection` diffère selon la version — `-ComputerName` en Windows PowerShell 5.1, `-TargetName` en PowerShell 7. Pour rester compatible avec les deux, utilise la **forme positionnelle** (`Test-Connection dc01.lab.local`), comme ci-dessus.

> **`Test-NetConnection` est essentiel :** il ne fait pas que pinguer — il teste si un **port TCP** est joignable. « Le serveur répond au ping mais l'application ne marche pas » se diagnostique avec `-Port`. C'est l'outil de dépannage réseau n°1.

> **📌 Réflexe `Get-Member` :** `Test-NetConnection google.com -Port 443 | Get-Member` montre `TcpTestSucceeded`, `PingSucceeded`, `RemoteAddress`, `SourceAddress`. On peut donc scripter des tests de connectivité qui renvoient `True`/`False` par port.

### La table de routage

La table de routage décide par où sortent les paquets :

```powershell
Get-NetRoute -AddressFamily IPv4 |
    Select-Object DestinationPrefix, NextHop, RouteMetric, InterfaceAlias

# La route par défaut (0.0.0.0/0) = la passerelle
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

`DestinationPrefix 0.0.0.0/0` est la **route par défaut** : tout ce qui n'a pas de route spécifique passe par là (la passerelle).

### Les connexions TCP actives : `Get-NetTCPConnection`

L'équivalent objet de `netstat` :

```powershell
Get-NetTCPConnection -State Established |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess

# Quel PROCESSUS écoute sur un port donné ?
Get-NetTCPConnection -LocalPort 445 -State Listen |
    Select-Object LocalPort, OwningProcess
```

> **Astuce puissante :** `OwningProcess` est le PID du processus. En le croisant avec `Get-Process`, on répond à « quel programme écoute sur ce port ? » — utile en admin comme en sécurité :
> ```powershell
> Get-NetTCPConnection -LocalPort 3389 -State Listen |
>     ForEach-Object { Get-Process -Id $_.OwningProcess }
> ```

## 🟡 Très utile en pratique

### Un test de connectivité multi-ports

```powershell
$cible = "dc01.lab.local"
$ports = @{ "DNS/TCP"=53; "Kerberos"=88; "LDAP"=389; "SMB"=445; "RDP"=3389 }

foreach ($nom in $ports.Keys) {
    $ok = (Test-NetConnection $cible -Port $ports[$nom] -WarningAction SilentlyContinue).TcpTestSucceeded
    [PSCustomObject]@{ Service = $nom; Port = $ports[$nom]; OuvertTCP = $ok }
}
```

Ce genre de test « quels ports d'un contrôleur de domaine sont joignables ? » est un diagnostic classique.

> **⚠️ `Test-NetConnection -Port` teste uniquement le TCP.** Le résultat `TcpTestSucceeded` signifie « **TCP/53 joignable** », pas « le service DNS fonctionne ». Or le DNS utilise **UDP et TCP** selon les opérations (les requêtes courantes passent en UDP/53, TCP/53 servant surtout aux transferts de zone et grandes réponses). Un `Test-NetConnection -Port 53` peut donc échouer alors que la résolution marche très bien. **Pour tester réellement le service DNS**, interroge-le avec `Resolve-DnsName` (Ch.16) :
> ```powershell
> Resolve-DnsName lab.local -Server 192.168.1.10   # le serveur répond-il VRAIMENT à une requête DNS ?
> ```
> Règle générale : `Test-NetConnection -Port` répond à « le port TCP est-il joignable ? » ; pour « le service applicatif répond-il ? », utilise l'outil du protocole (ici `Resolve-DnsName`).

## 🔴 Bonus

### Tracer la route (`traceroute`)

```powershell
Test-NetConnection google.com -TraceRoute        # chemin réseau saut par saut
```

### Ajouter une route statique `[🔑 Admin]`

```powershell
New-NetRoute -DestinationPrefix "10.10.0.0/16" -InterfaceAlias "Ethernet" -NextHop "192.168.1.254"
```

Rare sur un poste, plus courant sur des serveurs à réseaux multiples.

## ❌ Erreur classique

```powershell
# Croire que "ping OK" = "service OK"
Test-Connection SRV01 -Count 1    # ⚠️ teste seulement ICMP, pas l'application
Test-NetConnection SRV01 -Port 445   # ✅ teste le vrai port applicatif

# Lire du texte de netstat au lieu d'objets
netstat -ano | findstr 445    # ⚠️ texte à parser
Get-NetTCPConnection -LocalPort 445   # ✅ objets exploitables

# Oublier -Quiet quand on veut juste un booléen dans un if
if (Test-Connection SRV01 -Count 1) { }          # ⚠️ renvoie des objets
if (Test-Connection SRV01 -Count 1 -Quiet) { }   # ✅ True/False
```

## 💡 Exercices

**Guidé :** Teste si le port 443 de `google.com` est joignable et affiche `TcpTestSucceeded`. Puis trouve quel processus écoute sur le port 135 en local.

**Autonome :** Écris un script `-ComputerName` qui teste une liste de ports (par exemple 53, 389, 445) et renvoie un PSCustomObject par port (Port, Ouvert). Exporte en CSV.

## ✅ Tu sais maintenant...

- Tester connectivité et ports avec `Test-Connection` et surtout `Test-NetConnection -Port`
- Lire la table de routage (`Get-NetRoute`) et repérer la route par défaut
- Lister les connexions TCP (`Get-NetTCPConnection`) et relier un port à son processus (`OwningProcess`)
- Diagnostiquer « ping OK mais service KO » via les ports

## 💬 Questions d'entretien typiques

- **Comment vérifier qu'un port applicatif est joignable ?** → `Test-NetConnection -ComputerName X -Port N` (propriété `TcpTestSucceeded`).
- **Quelle cmdlet remplace `netstat` ?** → `Get-NetTCPConnection`, avec `OwningProcess` pour retrouver le programme via `Get-Process`.
- **Qu'est-ce que la route `0.0.0.0/0` ?** → La route par défaut : tout le trafic sans route spécifique passe par sa passerelle.

---

# Chapitre 18 — Pare-feu Windows

## 🟢 Le minimum à savoir

### Les profils de pare-feu

Le Pare-feu Windows Defender applique des règles selon un **profil** correspondant au type de réseau :

- **Domain** : la machine est connectée à son domaine AD
- **Private** : réseau privé de confiance (maison, bureau)
- **Public** : réseau non fiable (café, aéroport) — le plus restrictif

```powershell
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

> **Important :** un même poste applique le profil correspondant au réseau où il se trouve. Une règle peut être active sur `Private` mais pas sur `Public`.

### Lister les règles

```powershell
Get-NetFirewallRule | Where-Object Enabled -eq "True" |
    Select-Object DisplayName, Direction, Action, Profile -First 20

# Les règles entrantes qui autorisent quelque chose
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Select-Object DisplayName, Profile
```

> **📌 Réflexe `Get-Member` :** une règle de pare-feu a beaucoup de propriétés (`DisplayName`, `Direction`, `Action`, `Profile`, `Enabled`). Le détail des ports/protocoles se lit via des cmdlets associées (`Get-NetFirewallPortFilter`), car une règle est liée à des filtres.

### Direction et action

- **Direction** : `Inbound` (trafic entrant) ou `Outbound` (sortant)
- **Action** : `Allow` (autoriser) ou `Block` (bloquer)

La logique par défaut d'un poste : **entrant bloqué** sauf exceptions, **sortant autorisé**.

### Créer une règle `[🔑 Admin]`

```powershell
# Autoriser le port TCP 8080 en entrée, sur les profils Domain et Private
New-NetFirewallRule -DisplayName "App interne 8080" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 8080 `
    -Profile Domain,Private
```

### Modifier et supprimer `[🔑 Admin]`

```powershell
Set-NetFirewallRule -DisplayName "App interne 8080" -Enabled False   # désactiver
Remove-NetFirewallRule -DisplayName "App interne 8080"               # supprimer
```

> **⚠️ Prudence :** créer une règle trop permissive (par ex. autoriser 3389/RDP depuis n'importe où sur le profil `Public`) ouvre une porte d'entrée. Restreins toujours au **profil** et, idéalement, à la **plage d'adresses** (`-RemoteAddress`) nécessaires. Et comme pour le réseau : ne te bloque pas toi-même en désactivant une règle qui autorise ta propre session distante.

## 🟡 Très utile en pratique

### Vérifier qu'un port est autorisé

```powershell
# Existe-t-il une règle Allow entrante pour le port 445 ?
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    Where-Object { ($_ | Get-NetFirewallPortFilter).LocalPort -eq 445 } |
    Select-Object DisplayName, Profile
```

Utile pour diagnostiquer « pourquoi le partage de fichiers ne répond pas ? » — souvent une règle de pare-feu.

### Auditer les règles entrantes autorisées

```powershell
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True |
    ForEach-Object {
        $port = ($_ | Get-NetFirewallPortFilter).LocalPort
        [PSCustomObject]@{
            Regle   = $_.DisplayName
            Profil  = $_.Profile
            Port    = $port
        }
    } | Sort-Object Port
```

Cet audit — « qu'est-ce qui est ouvert en entrée ? » — est un contrôle de sécurité de base.

## 🔴 Bonus

### État global du pare-feu

```powershell
# S'assurer que le pare-feu est actif sur tous les profils
Get-NetFirewallProfile | Where-Object Enabled -eq $false
# → si cette commande renvoie quelque chose, un profil est désactivé (à corriger)
```

Un pare-feu désactivé sur un profil est un écart de sécurité classique à détecter.

## ❌ Erreur classique

```powershell
# Créer une règle sans restreindre le profil
New-NetFirewallRule -DisplayName "X" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3389
# ❌ ouvre le port sur TOUS les profils (dont Public !)
# ✅ ajouter -Profile Domain,Private et/ou -RemoteAddress

# Désactiver une règle dont dépend ta session RDP/WinRM
Set-NetFirewallRule ... -Enabled False    # ❌ risque de te couper l'accès

# Confondre "règle existe" et "règle activée"
Get-NetFirewallRule -DisplayName "X"      # peut exister mais être Enabled False
```

## 💡 Exercices

**Guidé :** Affiche l'état (`Enabled`, actions par défaut) des trois profils de pare-feu. Signale en rouge tout profil désactivé.

**Autonome :** Écris un script qui liste les règles entrantes autorisées avec leur port et leur profil, et exporte le résultat en CSV (un audit d'ouverture réseau).

## 🧩 Mini-projet — Diagnostic réseau du poste

Crée `Get-NetworkDiagnostic.ps1` qui réunit toute la Partie III et produit un rapport :

- La fiche réseau : interface, IPv4, passerelle, DNS (Ch.15-16)
- Un test de connectivité vers la passerelle et vers un hôte externe (Ch.17)
- Un test de résolution DNS d'un nom connu (Ch.16)
- L'état des profils de pare-feu (Ch.18)
- Le tout en PSCustomObject, avec résumé coloré et export CSV, robuste aux erreurs (`try/catch`)

C'est le pendant « réseau » de ta boîte à outils. Combiné au Capstone de la Partie II, tu obtiens un véritable outil de diagnostic de poste.

## ✅ Tu sais maintenant...

- Les profils de pare-feu (Domain/Private/Public) et pourquoi ils comptent
- Lister, créer, modifier, supprimer des règles (`*-NetFirewallRule`)
- Direction (Inbound/Outbound) et action (Allow/Block)
- Restreindre par profil et adresse pour ne pas trop ouvrir
- Auditer ce qui est ouvert en entrée

## 💬 Questions d'entretien typiques

- **À quoi servent les profils de pare-feu ?** → Appliquer des règles différentes selon le type de réseau (Domain/Private/Public), Public étant le plus restrictif.
- **Comment ouvrir un port sans trop exposer la machine ?** → `New-NetFirewallRule` en restreignant `-Profile` et `-RemoteAddress` au strict nécessaire.
- **Comment savoir quel port est ouvert en entrée ?** → Croiser `Get-NetFirewallRule` (Inbound/Allow/Enabled) avec `Get-NetFirewallPortFilter`.

---

# PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY

> **🏗️ À ce stade, on entre dans l'administration d'infrastructure Windows.** Les parties précédentes s'appliquaient à un poste isolé. Active Directory est l'annuaire central d'un **réseau d'entreprise**. Pour pratiquer cette partie, il te faut l'environnement de lab décrit en début de cours : une **VM Windows Server** promue contrôleur de domaine, ou un poste avec **RSAT** connecté à un domaine.
>
> **⚠️ Pratique sur un lab, JAMAIS en production.** À partir d'ici, les exemples **créent, modifient, désactivent et suppriment** de vrais objets d'annuaire (comptes, groupes, OU). Une erreur sur un domaine de production peut désactiver des utilisateurs réels ou casser des accès. Tous les exercices et mini-projets de cette partie sont à réaliser exclusivement sur **ton domaine de lab** (`lab.local`), sur des objets de test. Applique systématiquement la discipline du cours : `Get`/`Test` avant d'agir, `-WhatIf` avant toute opération de masse.
>
> **Ce cours reste un cours PowerShell.** On apprend ici à *piloter* AD avec PowerShell — pas à concevoir une forêt, gérer la réplication, les niveaux fonctionnels ou les approbations. Pour ça, réfère-toi à un cours Active Directory dédié. Ici, AD est le **terrain** sur lequel on applique tout ce qu'on a appris : objets, pipeline, filtrage, boucles, CSV.

---

# Chapitre 19 — Comprendre Active Directory

## 🟢 Le minimum à savoir

### Qu'est-ce qu'Active Directory ?

**Active Directory (AD)** est l'annuaire centralisé d'un réseau Windows d'entreprise. Au lieu de gérer des comptes locaux sur chaque machine (Ch.10), on centralise **utilisateurs, ordinateurs, groupes** dans une base unique, administrée depuis les **contrôleurs de domaine**.

Concrètement, AD répond à : « qui es-tu (authentification), qu'as-tu le droit de faire (autorisation), et où es-tu rangé dans l'organisation ? ».

### Le vocabulaire indispensable

Avant toute cmdlet, il faut ces mots — sinon les commandes n'ont pas de sens :

| Terme | Ce que c'est |
|-------|-------------|
| **Domaine** | L'unité d'administration AD (ex : `lab.local`). Regroupe des objets partageant une base de sécurité commune |
| **Contrôleur de domaine (DC)** | Un serveur qui héberge la base AD et authentifie les utilisateurs |
| **Forêt** | L'ensemble de tous les domaines liés (le conteneur le plus haut) |
| **Objet** | Toute entité d'AD : un utilisateur, un ordinateur, un groupe… |
| **Utilisateur** | Un compte de connexion (`alice.martin`) |
| **Ordinateur** | Un compte machine (chaque PC/serveur membre du domaine en a un) |
| **Groupe** | Un ensemble d'utilisateurs/ordinateurs, pour attribuer des droits en bloc |
| **OU (Unité d'organisation)** | Un « dossier » qui range les objets (ex : `OU=IT`, `OU=Compta`). Sert à organiser **et** à cibler les GPO |
| **Attribut** | Une propriété d'un objet (nom, email, service, date de dernière connexion…) |

### Le Distinguished Name (DN) : l'adresse d'un objet

Chaque objet AD a une **adresse unique**, son **DN** (Distinguished Name), qui décrit son emplacement dans l'arborescence, de l'objet jusqu'au domaine :

```
CN=Alice Martin,OU=IT,OU=Utilisateurs,DC=lab,DC=local
│                │     │              │
│                │     │              └─ le domaine lab.local (DC = Domain Component)
│                │     └─ rangé dans l'OU Utilisateurs
│                └─ puis dans l'OU IT
└─ l'objet lui-même (CN = Common Name)
```

On **lit** un DN de gauche (l'objet) à droite (le domaine). Tu n'as pas à le mémoriser ou le taper à la main : les cmdlets te le renvoient, et tu peux le **découper** avec les techniques de chaînes du Ch.5 (`-split ","`, `-match`) pour en extraire l'OU ou le domaine.

> **Rappel Ch.5 :** `"CN=Alice,OU=IT,DC=lab,DC=local" -split "," ` te donne un tableau `["CN=Alice", "OU=IT", "DC=lab", "DC=local"]`. C'est exactement là que les opérations de chaînes deviennent concrètes.

### Le module ActiveDirectory et RSAT

Les cmdlets AD (`Get-ADUser`, `New-ADUser`…) viennent du module **ActiveDirectory**, qui n'est **pas** présent partout :

- Sur un **contrôleur de domaine** : présent d'office.
- Sur un **Windows Server membre** : via le rôle/outils AD.
- Sur un **Windows 10/11** : via **RSAT** (Remote Server Administration Tools), à installer.

```powershell
# Installer RSAT AD sur Windows 10/11                      [🔑 Admin]
Add-WindowsCapability -Online -Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"

# Charger le module
Import-Module ActiveDirectory

# Vérifier qu'il est disponible
Get-Module -ListAvailable ActiveDirectory
```

> **⚠️ Si `Get-ADUser` renvoie « terme non reconnu » :** le module n'est pas installé. Sur un poste client, installe RSAT (ci-dessus). C'est LE piège du débutant qui tape `Get-ADUser` sur son Windows 11 personnel sans domaine — comme prévenu en début de cours.

### Vérifier son environnement AD

```powershell
Get-ADDomain                     # infos sur le domaine courant
Get-ADForest                     # infos sur la forêt
Get-ADDomainController -Discover # trouver un contrôleur de domaine
```

`Get-ADDomain` renvoie notamment le `DistinguishedName` du domaine (`DC=lab,DC=local`) et le `DNSRoot` (`lab.local`) — pratiques pour construire des recherches (Ch.23).

## 🟡 Très utile en pratique

### AD vs comptes locaux : ne pas confondre

| | Comptes **locaux** (Ch.10) | **Active Directory** |
|---|---|---|
| Cmdlets | `*-LocalUser`, `*-LocalGroup` | `*-ADUser`, `*-ADGroup` |
| Portée | Une seule machine | Tout le domaine |
| Base | SAM locale | Base AD (sur les DC) |
| Quand ? | Poste isolé, compte technique local | Réseau d'entreprise |

C'est la même logique d'administration (lister, créer, modifier, désactiver), mais à l'échelle du domaine. Tes réflexes du Ch.10 se transposent directement.

### L'objet renvoyé par `Get-ADUser`

```powershell
Get-ADUser -Identity alice.martin | Get-Member
```

> **📌 Réflexe `Get-Member` :** un objet utilisateur AD a énormément d'attributs. Mais **par défaut, `Get-ADUser` n'en renvoie qu'une poignée** (nom, SamAccountName, DN, statut). Pour obtenir les autres (email, service, dernière connexion…), il faut le paramètre `-Properties` — un point crucial qu'on détaille au Ch.23.

## 🔴 Bonus

### La structure logique vs physique

AD a une structure **logique** (domaines, OU, objets — ce qu'on manipule ici) et une structure **physique** (sites, sous-réseaux, réplication entre DC). Ce cours ne traite que la partie logique via PowerShell ; la topologie physique relève d'un cours AD dédié.

## ❌ Erreur classique

```powershell
# Taper une cmdlet AD sans le module / sans domaine
Get-ADUser alice        # ❌ "terme non reconnu" si RSAT absent
Import-Module ActiveDirectory   # (après avoir installé RSAT)

# Croire qu'un compte local et un compte AD sont la même chose
Get-LocalUser alice     # compte LOCAL de la machine
Get-ADUser alice        # compte du DOMAINE — objets différents !

# Vouloir taper un DN à la main sans erreur
# → laisse les cmdlets te le fournir, découpe-le avec -split (Ch.5)
```

## 💡 Exercices

**Guidé :** Sur ton lab, exécute `Get-ADDomain` et affiche le `DNSRoot` et le `DistinguishedName` du domaine. Puis `Get-ADDomainController -Discover` pour identifier ton DC.

**Autonome :** Prends le DN d'un utilisateur (`(Get-ADUser alice.martin).DistinguishedName`) et, avec `-split ","`, extrais uniquement la première OU dans laquelle il se trouve.

## ✅ Tu sais maintenant...

- Ce qu'est AD (annuaire central) et son vocabulaire (domaine, DC, forêt, OU, objet, attribut)
- Lire et comprendre un **Distinguished Name**
- Le module **ActiveDirectory** et **RSAT** (et le piège du module absent)
- La différence comptes locaux / comptes AD
- Que `Get-ADUser` ne renvoie que quelques attributs par défaut (d'où `-Properties`)

## 💬 Questions d'entretien typiques

- **Qu'est-ce qu'un contrôleur de domaine ?** → Un serveur qui héberge la base AD et authentifie les utilisateurs du domaine.
- **Qu'est-ce qu'un DN ?** → Le Distinguished Name, l'adresse unique d'un objet dans l'arborescence AD (`CN=...,OU=...,DC=...`).
- **Pourquoi `Get-ADUser` ne montre-t-il pas l'email ?** → Par défaut il ne renvoie qu'un jeu réduit d'attributs ; il faut `-Properties mail` (ou `-Properties *`) pour les autres.
- **Où trouve-t-on les cmdlets AD sur un poste client ?** → Il faut installer RSAT, puis `Import-Module ActiveDirectory`.

---

# Chapitre 20 — Utilisateurs AD

## 🟢 Le minimum à savoir

### Chercher un utilisateur : `Get-ADUser`

```powershell
# Par identité (SamAccountName, DN, SID, GUID)
Get-ADUser -Identity alice.martin

# Avec des attributs supplémentaires (rappel Ch.19 : sinon jeu réduit)
Get-ADUser -Identity alice.martin -Properties mail, Department, LastLogonDate

# Tous les utilisateurs (filtre obligatoire — voir Ch.23)
Get-ADUser -Filter *
```

Les attributs par défaut : `Name`, `SamAccountName`, `DistinguishedName`, `Enabled`, `UserPrincipalName`, `SID`, `GivenName`, `Surname`. Tout le reste (`mail`, `Department`, `Title`, `LastLogonDate`, `Manager`…) nécessite `-Properties`.

> **📌 Réflexe `Get-Member` :** `Get-ADUser alice.martin -Properties * | Get-Member` liste **tous** les attributs disponibles pour un utilisateur. Fais-le une fois pour découvrir ce que tu peux exploiter (souvent 100+ attributs).

### Créer un utilisateur : `New-ADUser` `[🔑 Admin]`

**Discipline `Get` avant `New`** : on vérifie que le compte n'existe pas.

```powershell
if (-not (Get-ADUser -Filter "SamAccountName -eq 'jdupont'" -ErrorAction SilentlyContinue)) {

    $motDePasse = Read-Host "Mot de passe initial" -AsSecureString

    New-ADUser `
        -Name "Jean Dupont" `
        -GivenName "Jean" -Surname "Dupont" `
        -SamAccountName "jdupont" `
        -UserPrincipalName "jdupont@lab.local" `
        -Path "OU=IT,DC=lab,DC=local" `
        -AccountPassword $motDePasse `
        -Enabled $true `
        -ChangePasswordAtLogon $true
}
```

Points clés :
- `-SamAccountName` : l'identifiant de connexion (format court, `jdupont`)
- `-UserPrincipalName` : l'identifiant moderne (format email, `jdupont@lab.local`)
- `-Path` : le DN de l'OU où créer le compte
- `-AccountPassword` : un **SecureString** (jamais en clair — voir Ch.33)
- `-Enabled $true` : sinon le compte est créé désactivé
- `-ChangePasswordAtLogon $true` : bonne pratique pour un mot de passe initial

### Modifier un utilisateur : `Set-ADUser` `[🔑 Admin]`

```powershell
Set-ADUser -Identity jdupont -EmailAddress "jean.dupont@lab.local" -Department "Informatique"
Set-ADUser -Identity jdupont -Title "Technicien" -Office "Bâtiment A"
```

### Activer, désactiver, déverrouiller `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity jdupont      # désactiver (départ, suspension)
Enable-ADAccount  -Identity jdupont      # réactiver
Unlock-ADAccount  -Identity jdupont      # déverrouiller (après trop d'essais de mot de passe)
```

> **Verrouillé ≠ désactivé :** un compte **verrouillé** l'a été automatiquement (trop de mauvais mots de passe) — on le **déverrouille**. Un compte **désactivé** l'a été manuellement (départ…) — on le **réactive**. Deux situations différentes.

### Réinitialiser un mot de passe `[🔑 Admin]`

```powershell
$nouveau = Read-Host "Nouveau mot de passe" -AsSecureString
Set-ADAccountPassword -Identity jdupont -NewPassword $nouveau -Reset
Set-ADUser -Identity jdupont -ChangePasswordAtLogon $true    # forcer le changement
```

### Supprimer un utilisateur `[🔑 Admin]`

```powershell
Remove-ADUser -Identity jdupont -Confirm:$false
```

> **Bonne pratique (rappel Ch.10) :** on préfère souvent **désactiver et déplacer** un compte (départ d'un employé) plutôt que le supprimer d'emblée — pour conserver l'historique et pouvoir restaurer. La suppression vient après une période de rétention.

## 🟡 Très utile en pratique

### Identifier les comptes à problème

```powershell
# Comptes désactivés
Get-ADUser -Filter "Enabled -eq '$false'" | Select-Object Name, SamAccountName

# Comptes verrouillés
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName

# Comptes dont le mot de passe n'expire jamais (point d'audit)
Get-ADUser -Filter "PasswordNeverExpires -eq '$true'" -Properties PasswordNeverExpires |
    Select-Object Name, SamAccountName
```

`Search-ADAccount` est un raccourci pratique pour les cas courants (`-LockedOut`, `-AccountDisabled`, `-AccountInactive`, `-PasswordExpired`).

### La discipline Get → Set en action

```powershell
# 1. Regarder l'état actuel
Get-ADUser jdupont -Properties Department, Title | Select Department, Title

# 2. Modifier en connaissance de cause
Set-ADUser jdupont -Department "Support" -Title "Technicien N2"

# 3. Vérifier
Get-ADUser jdupont -Properties Department, Title | Select Department, Title
```

Ce triptyque lire → modifier → vérifier est la marque d'un administrateur rigoureux.

## 🔴 Bonus

### Comptes inactifs depuis X jours

```powershell
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly |
    Select-Object Name, SamAccountName, LastLogonDate
```

> **⚠️ Nuance importante sur `LastLogonDate` :** cet attribut dérive de `lastLogonTimestamp`, qui n'est répliqué entre contrôleurs de domaine que périodiquement (par défaut avec une marge d'environ 9-14 jours). Il est donc **approximatif** : parfait pour repérer des comptes « globalement inactifs depuis des mois », mais **pas** pour savoir la dernière connexion exacte à la minute. Pour une précision fine, il faudrait interroger l'attribut `lastLogon` (non répliqué) sur **chaque** DC — beaucoup plus lourd. Pour l'audit courant, `LastLogonDate` suffit, en gardant sa marge d'erreur en tête.

## ❌ Erreur classique

```powershell
# Créer un compte sans -Enabled → compte inutilisable (désactivé)
New-ADUser -Name "X" -SamAccountName x -AccountPassword $p   # ⚠️ créé désactivé
New-ADUser ... -Enabled $true                                 # ✅

# Passer le mot de passe en clair
-AccountPassword "P@ssw0rd"          # ❌ refusé (attend un SecureString)
-AccountPassword (Read-Host -AsSecureString)   # ✅

# Confondre verrouillé et désactivé
Enable-ADAccount jdupont    # ❌ ne déverrouille pas un compte verrouillé
Unlock-ADAccount jdupont    # ✅ pour un compte verrouillé

# Se fier à LastLogonDate à la minute près
# → attribut approximatif (réplication différée)
```

## 💡 Exercices

**Guidé :** Affiche le nom, l'email et le service (`Department`) de `alice.martin` (pense à `-Properties`). Puis modifie son `Title` et vérifie le changement.

**Autonome :** Écris une fonction `New-LabUser` qui prend `-GivenName`, `-Surname` et `-OU`, construit le `SamAccountName` (première lettre du prénom + nom, en minuscules, via les méthodes de chaîne du Ch.5), vérifie l'absence du compte, puis le crée activé avec changement de mot de passe à la première connexion.

## ✅ Tu sais maintenant...

- Chercher (`Get-ADUser`, avec `-Properties`), créer (`New-ADUser`), modifier (`Set-ADUser`)
- Activer/désactiver (`Enable`/`Disable-ADAccount`), déverrouiller (`Unlock-ADAccount`)
- Réinitialiser un mot de passe (`Set-ADAccountPassword -Reset`)
- Repérer les comptes à problème (`Search-ADAccount`)
- La nuance sur `LastLogonDate` (approximatif, réplication différée)

## 💬 Questions d'entretien typiques

- **Différence entre un compte verrouillé et désactivé ?** → Verrouillé = automatique (trop de mauvais mots de passe), on déverrouille ; désactivé = manuel, on réactive.
- **Pourquoi un `New-ADUser` donne-t-il un compte inutilisable ?** → Souvent l'oubli de `-Enabled $true` (créé désactivé par défaut).
- **Peut-on se fier à `LastLogonDate` à la minute ?** → Non : dérivé de `lastLogonTimestamp`, répliqué avec une marge de plusieurs jours ; bon pour l'inactivité globale, pas pour l'exactitude.
- **Comment passer un mot de passe à `New-ADUser` ?** → Via un `SecureString` (`-AsSecureString`), jamais en clair.

---

# Chapitre 21 — Groupes AD

## 🟢 Le minimum à savoir

### Pourquoi les groupes sont centraux

En administration, **on n'attribue jamais un droit à un utilisateur directement** — on l'attribue à un **groupe**, et on met l'utilisateur dans le groupe. Ainsi, gérer 500 personnes revient à gérer quelques dizaines de groupes. C'est le principe **AGDLP** (on met les comptes dans des groupes, les groupes dans des ressources), fondamental en sécurité Windows.

### Chercher et lister des groupes

```powershell
Get-ADGroup -Identity "Comptables"
Get-ADGroup -Filter * | Select-Object Name, GroupScope, GroupCategory
Get-ADGroup -Filter "Name -like 'GG_*'"    # tous les groupes commençant par GG_
```

### Voir les membres d'un groupe

```powershell
Get-ADGroupMember -Identity "Comptables" |
    Select-Object Name, SamAccountName, objectClass

# Membres récursifs (y compris via des groupes imbriqués)
Get-ADGroupMember -Identity "Comptables" -Recursive
```

> **📌 Réflexe `Get-Member` :** `Get-ADGroup Comptables -Properties * | Get-Member` montre les attributs d'un groupe (`GroupScope`, `GroupCategory`, `member`, `Description`, `ManagedBy`…).

### Créer un groupe : `New-ADGroup` `[🔑 Admin]`

```powershell
New-ADGroup -Name "GG_Compta" `
    -SamAccountName "GG_Compta" `
    -GroupScope Global `
    -GroupCategory Security `
    -Path "OU=Groupes,DC=lab,DC=local" `
    -Description "Groupe global du service Comptabilité"
```

### Ajouter et retirer des membres `[🔑 Admin]`

```powershell
Add-ADGroupMember    -Identity "GG_Compta" -Members jdupont, alice.martin
Remove-ADGroupMember -Identity "GG_Compta" -Members jdupont -Confirm:$false
```

### Voir les groupes d'un utilisateur

```powershell
Get-ADPrincipalGroupMembership -Identity jdupont |
    Select-Object Name, GroupScope
```

C'est la question inverse : « de quels groupes cet utilisateur est-il membre ? » — essentielle pour comprendre ses droits.

## 🟡 Très utile en pratique

### Catégorie : Sécurité vs Distribution

- **Security** (Sécurité) : sert à attribuer des **droits** (accès à un partage, à une ressource). C'est le cas courant en administration.
- **Distribution** : sert uniquement aux **listes de diffusion mail** (Exchange), pas aux droits.

En cas de doute pour donner des permissions : c'est un groupe **Security**.

### Portée (Scope) : Domain Local, Global, Universal

La **portée** détermine qui peut être membre et où le groupe peut être utilisé. Pour un débutant, retiens la logique courante en domaine unique :

| Scope | Contient typiquement | Utilisé pour |
|-------|---------------------|--------------|
| **Global** | Des comptes du **même domaine** | Regrouper des utilisateurs par rôle/service (ex : `GG_Compta`) |
| **Domain Local** | Des groupes globaux | Attribuer un droit sur **une ressource** (ex : `DL_Partage_Compta_Modif`) |
| **Universal** | Des comptes/groupes de **toute la forêt** | Environnements multi-domaines |

> **Le modèle classique (AGDLP) :** on met les **A**ccounts dans un **G**lobal group (par rôle), ce groupe global dans un **D**omain **L**ocal group (par ressource), et c'est au Domain Local qu'on donne la **P**ermission. Ça paraît abstrait au début, mais c'est ce qui rend les droits maintenables à grande échelle. Pour un lab simple en domaine unique, on peut rester pragmatique, mais connaître ce modèle est attendu d'un administrateur.

### Auditer l'appartenance à un groupe sensible

```powershell
# Qui est Admin du domaine ? (groupe le plus sensible qui soit)
Get-ADGroupMember -Identity "Admins du domaine" -Recursive |
    Select-Object Name, SamAccountName, objectClass
```

> **Sécurité :** l'appartenance aux groupes privilégiés (`Admins du domaine` / `Domain Admins`, `Administrateurs de l'entreprise` / `Enterprise Admins`) doit être **minimale et auditée**. Chaque membre est une cible de choix pour un attaquant. Ce contrôle est un incontournable de la sécurité AD.

> **Note langue (même principe qu'au Ch.10).** Ces noms **dépendent de la langue du domaine** : `Admins du domaine` en français, `Domain Admins` en anglais. Un script qui cible ces groupes par leur nom cassera sur un annuaire dans une autre langue. Pour être portable, on cible par **SID**, dont le suffixe (le *RID*) est fixe : `-512` pour les administrateurs du domaine, `-519` pour les administrateurs de l'entreprise.
> ```powershell
> $domainSID = (Get-ADDomain).DomainSID.Value
> $admins = Get-ADGroup -Identity "$domainSID-512"    # "Admins du domaine" / "Domain Admins"
> Get-ADGroupMember -Identity $admins -Recursive | Select-Object Name, SamAccountName
> ```

## 🔴 Bonus

### Groupes imbriqués et appartenance récursive

Un groupe peut contenir d'autres groupes. `Get-ADGroupMember -Recursive` « aplatit » cette imbrication pour révéler tous les utilisateurs effectifs — indispensable pour comprendre les droits réels (un utilisateur peut être admin sans être membre *direct* du groupe admin).

## ❌ Erreur classique

```powershell
# Donner un droit à un utilisateur au lieu d'un groupe
# ❌ ingérable à l'échelle → toujours passer par un groupe

# Créer un groupe Distribution pour gérer des droits
New-ADGroup ... -GroupCategory Distribution   # ❌ ne porte pas de droits
New-ADGroup ... -GroupCategory Security        # ✅

# Oublier -Recursive et rater des membres indirects
Get-ADGroupMember "Admins du domaine"             # ⚠️ membres directs seulement
Get-ADGroupMember "Admins du domaine" -Recursive  # ✅ tous les membres effectifs
```

## 💡 Exercices

**Guidé :** Crée un groupe global de sécurité `GG_Test`, ajoute-lui deux utilisateurs, liste ses membres, puis retire-en un.

**Autonome :** Écris un script qui prend un `-GroupName` et exporte en CSV tous ses membres récursifs (Name, SamAccountName, Type). Ajoute une colonne indiquant s'il s'agit d'un membre direct ou indirect.

## ✅ Tu sais maintenant...

- Pourquoi on attribue les droits via des **groupes**, jamais aux utilisateurs directement
- Chercher, créer des groupes, gérer leurs membres (`*-ADGroup`, `*-ADGroupMember`)
- Voir les groupes d'un utilisateur (`Get-ADPrincipalGroupMembership`)
- La différence **Security** / **Distribution** et les **portées** (Global/Domain Local/Universal)
- Auditer les groupes privilégiés (avec `-Recursive`)

## 💬 Questions d'entretien typiques

- **Pourquoi attribuer les droits à des groupes plutôt qu'à des utilisateurs ?** → Maintenabilité à l'échelle : on gère quelques groupes au lieu de milliers d'attributions individuelles.
- **Security ou Distribution pour donner un accès ?** → Security ; Distribution ne sert qu'aux listes de diffusion mail.
- **Pourquoi `-Recursive` sur un groupe admin ?** → Pour révéler les membres indirects (via groupes imbriqués), donc les droits réels.

---

# Chapitre 22 — Ordinateurs et unités d'organisation

## 🟢 Le minimum à savoir

### Les comptes ordinateurs

Chaque machine jointe au domaine possède un **compte ordinateur** dans AD — comme les utilisateurs, mais pour les machines. On les gère avec `*-ADComputer`.

```powershell
Get-ADComputer -Identity "CLIENT01"
Get-ADComputer -Filter * | Select-Object Name, Enabled, OperatingSystem

# Avec des attributs utiles
Get-ADComputer -Filter * -Properties OperatingSystem, LastLogonDate |
    Select-Object Name, OperatingSystem, LastLogonDate
```

> **📌 Réflexe `Get-Member` :** `Get-ADComputer CLIENT01 -Properties * | Get-Member` révèle `OperatingSystem`, `OperatingSystemVersion`, `LastLogonDate`, `IPv4Address`, `Enabled`, `DistinguishedName`.

### Le cas d'usage : inventaire du parc machines

```powershell
# Inventaire des OS présents dans le domaine
Get-ADComputer -Filter * -Properties OperatingSystem |
    Group-Object OperatingSystem |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```

`Group-Object` regroupe les machines par OS et les compte — un inventaire instantané, très parlant pour repérer des OS obsolètes (ex : Windows 7 encore présent).

### Repérer les machines obsolètes ou inactives

```powershell
# Ordinateurs inactifs depuis 90 jours (rappel : LastLogonDate approximatif, Ch.20)
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -ComputersOnly |
    Select-Object Name, LastLogonDate
```

### Désactiver / supprimer un compte ordinateur `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity "CLIENT01$"          # noter le $ pour un compte machine
Remove-ADComputer -Identity "CLIENT01" -Confirm:$false
```

> **Note :** le nom de compte machine se termine par `$` (ex : `CLIENT01$`). `Get-ADComputer` accepte le nom sans `$`, mais certaines opérations bas niveau l'exigent.

## 🟡 Les unités d'organisation (OU)

### À quoi servent les OU

Une **OU** (Organizational Unit) est un conteneur qui **range** les objets AD. Elle a deux rôles majeurs :

1. **Organiser** : ranger les objets par service, site, type (`OU=IT`, `OU=Compta`, `OU=Serveurs`)
2. **Cibler les GPO** : on lie une stratégie de groupe à une OU pour l'appliquer à tous ses objets (Ch.25)

Ce deuxième rôle est fondamental : la structure d'OU **conditionne** l'application des GPO.

### Lister et créer des OU `[🔑 Admin]`

```powershell
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName

New-ADOrganizationalUnit -Name "Comptabilité" -Path "OU=Services,DC=lab,DC=local"
```

> **Bonne pratique :** par défaut, une OU créée avec PowerShell est **protégée contre la suppression accidentelle** (`ProtectedFromAccidentalDeletion = $true`). C'est voulu : ça évite d'effacer d'un coup une OU pleine d'objets. Pour supprimer une OU, il faut d'abord retirer cette protection.

### Déplacer un objet : `Move-ADObject` `[🔑 Admin]`

Déplacer un objet le range dans une autre OU — et donc change les GPO qui s'y appliquent :

```powershell
# Déplacer un utilisateur vers l'OU Comptabilité
$dn = (Get-ADUser jdupont).DistinguishedName
Move-ADObject -Identity $dn -TargetPath "OU=Comptabilité,OU=Services,DC=lab,DC=local"
```

> **Cas concret (départ d'un employé) :** on désactive le compte, puis on le **déplace** vers une OU « Départs » (souvent liée à une GPO restrictive). Déplacer + désactiver plutôt que supprimer, c'est la procédure propre.

## 🔴 Bonus

### Retirer la protection avant suppression d'une OU

```powershell
Set-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" `
    -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" -Confirm:$false
```

## ❌ Erreur classique

```powershell
# Essayer de supprimer une OU protégée directement
Remove-ADOrganizationalUnit "OU=X,..."    # ❌ échoue si protégée
# → retirer d'abord ProtectedFromAccidentalDeletion (voir bonus)

# Oublier que déplacer un objet change les GPO appliquées
Move-ADObject ...    # ⚠️ conséquence : nouvelles stratégies, nouveaux droits

# Confondre le conteneur "Computers" (par défaut) et une vraie OU
# Les objets du conteneur CN=Computers ne reçoivent pas les GPO liées aux OU
```

## 💡 Exercices

**Guidé :** Fais l'inventaire des systèmes d'exploitation des ordinateurs du domaine avec `Group-Object`. Identifie le plus répandu.

**Autonome :** Crée une OU `OU=Test`, crée un utilisateur dedans, déplace-le vers une autre OU avec `Move-ADObject`, vérifie son nouveau DN, puis nettoie (retire la protection et supprime l'OU).

## ✅ Tu sais maintenant...

- Gérer les comptes ordinateurs (`*-ADComputer`) et inventorier le parc (`Group-Object` par OS)
- Repérer machines obsolètes/inactives
- Le rôle double des **OU** (organiser + cibler les GPO)
- Créer des OU, déplacer des objets (`Move-ADObject`) et l'impact sur les GPO
- La protection contre la suppression accidentelle

## 💬 Questions d'entretien typiques

- **À quoi sert une OU ?** → Ranger les objets AD et servir de cible aux GPO (la structure d'OU conditionne les stratégies appliquées).
- **Que se passe-t-il quand on déplace un objet d'OU ?** → Il reçoit les GPO liées à sa nouvelle OU — ses stratégies et droits peuvent changer.
- **Comment inventorier les OS du parc ?** → `Get-ADComputer -Properties OperatingSystem | Group-Object OperatingSystem`.
- **Pourquoi une OU ne se supprime-t-elle pas directement ?** → Protection contre la suppression accidentelle activée par défaut ; il faut la retirer d'abord.

---

# Chapitre 23 — Recherche et filtrage AD

## 🟢 Le minimum à savoir

### Pourquoi ce chapitre est important

Un annuaire d'entreprise contient des milliers d'objets. Savoir **filtrer efficacement** est ce qui sépare un script qui met 10 minutes (et surcharge le DC) d'un script instantané. La clé : filtrer **côté serveur** avec `-Filter`, pas côté client avec `Where-Object`.

### `-Filter` : le filtrage côté serveur

`-Filter` envoie la condition au contrôleur de domaine, qui ne renvoie **que** les objets correspondants. C'est rapide et économe.

```powershell
# Utilisateurs activés
Get-ADUser -Filter "Enabled -eq '$true'"

# Utilisateurs d'un service
Get-ADUser -Filter "Department -eq 'Comptabilité'" -Properties Department

# Recherche par motif
Get-ADUser -Filter "Surname -like 'Dup*'"

# Combiner des conditions
Get-ADUser -Filter "Enabled -eq '$true' -and Department -eq 'IT'" -Properties Department
```

> **Syntaxe du `-Filter` :** elle ressemble aux opérateurs PowerShell (`-eq`, `-like`, `-and`) mais s'écrit **entre guillemets** et suit des règles propres à AD. Les attributs utilisés dans le filtre doivent exister dans AD (ex : `Surname`, pas `Nom`).

### `-Filter` vs `Where-Object` : la différence cruciale

```powershell
# ❌ LENT : récupère TOUS les utilisateurs, puis filtre côté client
Get-ADUser -Filter * -Properties Department | Where-Object { $_.Department -eq "IT" }

# ✅ RAPIDE : le DC ne renvoie que les utilisateurs IT
Get-ADUser -Filter "Department -eq 'IT'" -Properties Department
```

> **Règle d'or :** filtre **toujours** au plus près de la source. `-Filter` (côté serveur) d'abord ; `Where-Object` (côté client) seulement pour ce que `-Filter` ne sait pas faire (calculs complexes, propriétés dérivées). Sur un annuaire de 50 000 objets, la différence est spectaculaire.

### `-SearchBase` : limiter la recherche à une OU

```powershell
# Ne chercher que dans l'OU IT
Get-ADUser -Filter * -SearchBase "OU=IT,DC=lab,DC=local"

# Combiner filtre et périmètre
Get-ADUser -Filter "Enabled -eq '$true'" -SearchBase "OU=Comptabilité,DC=lab,DC=local"
```

`-SearchBase` restreint la recherche à une branche de l'arbre — plus rapide et plus ciblé. `-SearchScope` affine (`Base`, `OneLevel`, `Subtree`).

### `-Properties` : récupérer les bons attributs

Rappel (Ch.19-20) : par défaut, seul un jeu réduit d'attributs revient. `-Properties` charge ceux dont tu as besoin :

```powershell
Get-ADUser -Filter * -Properties mail, Department, LastLogonDate |
    Select-Object Name, mail, Department, LastLogonDate
```

> **Performance :** ne demande que les attributs nécessaires. `-Properties *` charge **tout** (100+ attributs par objet) — pratique pour explorer un seul objet, mais coûteux sur une recherche de masse. En production, liste explicitement les attributs voulus.

## 🟡 Très utile en pratique

### Un rapport ciblé et performant

```powershell
# Comptes IT activés, avec leurs infos clés — filtré et projeté proprement
Get-ADUser -Filter "Enabled -eq '$true'" `
           -SearchBase "OU=IT,DC=lab,DC=local" `
           -Properties mail, Title, LastLogonDate |
    Select-Object Name, SamAccountName, mail, Title, LastLogonDate |
    Sort-Object Name |
    Export-Csv "C:\rapports\users_IT.csv" -NoTypeInformation -Encoding UTF8
```

Ce pipeline combine `-Filter` (serveur), `-SearchBase` (périmètre), `-Properties` (attributs), `Select-Object` (projection) et `Export-Csv` — le schéma type d'un rapport AD.

### Compter par catégorie

```powershell
# Répartition des utilisateurs par service
Get-ADUser -Filter * -Properties Department |
    Group-Object Department |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```

## 🔴 Bonus

### `Get-ADObject` : chercher tous types d'objets

Quand on ne sait pas si l'objet est un utilisateur, un groupe ou un ordinateur, `Get-ADObject` cherche par-delà les types :

```powershell
Get-ADObject -Filter "Name -like 'SRV*'" |
    Select-Object Name, ObjectClass, DistinguishedName
```

### Filtres LDAP

Pour des recherches très pointues, `-LDAPFilter` accepte la syntaxe LDAP native :

```powershell
Get-ADUser -LDAPFilter "(&(objectCategory=user)(!(mail=*)))"    # utilisateurs sans email
```

Puissant mais plus aride — à réserver aux cas que `-Filter` ne couvre pas.

## ❌ Erreur classique

```powershell
# Tout ramener puis filtrer côté client (lent, surcharge le DC)
Get-ADUser -Filter * | Where-Object { $_.Department -eq "IT" }   # ❌
Get-ADUser -Filter "Department -eq 'IT'"                          # ✅

# Filtrer sur un attribut non chargé
Get-ADUser -Filter * | Where-Object { $_.mail -like "*@lab*" }    # ❌ mail non chargé → vide
Get-ADUser -Filter "mail -like '*@lab*'" -Properties mail         # ✅

# Utiliser -Properties * en masse
Get-ADUser -Filter * -Properties *    # ⚠️ très lourd sur un gros annuaire
Get-ADUser -Filter * -Properties mail, Department   # ✅ juste le nécessaire
```

## 💡 Exercices

**Guidé :** Liste les utilisateurs activés de l'OU IT avec leur email et leur `Title`, triés par nom, en utilisant `-Filter`, `-SearchBase` et `-Properties`.

**Autonome :** Produis un rapport CSV de la répartition des utilisateurs par service (`Department`), avec le compte par service, trié du plus grand au plus petit.

## ✅ Tu sais maintenant...

- Filtrer **côté serveur** avec `-Filter` (et pourquoi c'est bien plus rapide que `Where-Object`)
- Restreindre le périmètre avec `-SearchBase` / `-SearchScope`
- Charger les bons attributs avec `-Properties` (sans abuser de `*`)
- Construire des rapports AD performants (filtre → périmètre → attributs → projection → export)

## 💬 Questions d'entretien typiques

- **`-Filter` ou `Where-Object` en AD ?** → `-Filter` (côté serveur) chaque fois que possible : le DC ne renvoie que le nécessaire. `Where-Object` seulement pour ce que `-Filter` ne peut pas exprimer.
- **Pourquoi un attribut apparaît-il vide alors qu'il existe ?** → Il n'a pas été chargé ; il faut `-Properties <attribut>`.
- **À quoi sert `-SearchBase` ?** → Limiter la recherche à une OU précise, pour la rapidité et le ciblage.

---

# Chapitre 24 — Administration en masse avec CSV

## 🟢 Le minimum à savoir

### L'objectif : l'onboarding automatisé

C'est le projet phare de la Partie IV, et un classique du métier : **créer des dizaines de comptes AD depuis un fichier CSV** (arrivée d'une promotion, d'un service entier…). Ce chapitre assemble presque tout le cours : `Import-Csv` (Ch.9), boucles (Ch.6), fonctions (Ch.7), gestion d'erreurs (Ch.8), création AD (Ch.20), groupes (Ch.21), OU (Ch.22).

### Le flux complet

```
CSV utilisateurs
      ↓  Import-Csv
validation des données
      ↓  foreach
vérification d'existence (Get-ADUser)
      ↓
New-ADUser (-WhatIf d'abord !)
      ↓
Add-ADGroupMember (groupes)
      ↓
rapport CSV (succès / échecs)
```

### Le fichier CSV de départ

```
GivenName,Surname,SamAccountName,Department,OU,Group
Jean,Dupont,jdupont,Comptabilité,"OU=Compta,DC=lab,DC=local",GG_Compta
Alice,Martin,amartin,IT,"OU=IT,DC=lab,DC=local",GG_IT
Sophie,Bernard,sbernard,IT,"OU=IT,DC=lab,DC=local",GG_IT
```

### Lire et valider

```powershell
$utilisateurs = Import-Csv "C:\onboarding\nouveaux.csv" -Encoding UTF8

# Validation minimale : colonnes attendues présentes et non vides
foreach ($u in $utilisateurs) {
    if (-not $u.SamAccountName -or -not $u.OU) {
        Write-Warning "Ligne invalide ignorée : $($u.GivenName) $($u.Surname)"
        continue
    }
    # ... traitement ...
}
```

### `-WhatIf` : simuler avant d'agir

> **📌 La discipline `Get`/`Test` culmine ici.** Avant de créer 50 comptes pour de vrai, on **simule** avec `-WhatIf`. La plupart des cmdlets de modification (`New-ADUser`, `Set-ADUser`, `Remove-*`, `Add-ADGroupMember`…) acceptent `-WhatIf`, qui affiche ce qui *serait* fait **sans rien faire**.

```powershell
New-ADUser -Name "Test" -SamAccountName test -Path "OU=IT,DC=lab,DC=local" -WhatIf
# → "What if: Performing the operation "New-ADUser" on target "CN=Test,OU=IT,...""
```

C'est le filet de sécurité indispensable pour toute opération de masse. On lance d'abord tout le script en `-WhatIf`, on vérifie la sortie, **puis** on retire le `-WhatIf`.

## 🟡 Le script d'onboarding complet

```powershell
# Invoke-Onboarding.ps1 — Création de comptes AD en masse depuis un CSV
# SÛR PAR DÉFAUT : le script SIMULE. Il faut le lancer avec -Execute pour créer réellement.
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string]$CsvPath,
    [string]$ReportPath = "C:\onboarding\rapport_$(Get-Date -Format yyyyMMdd_HHmmss).csv",
    [switch]$Execute      # SANS ce switch, le script simule (ne crée rien)
)

Import-Module ActiveDirectory
Set-StrictMode -Version Latest

# Sûr par défaut : tant que -Execute n'est pas fourni, on force le mode simulation.
# -WhatIf:$true fait que tous les ShouldProcess n'affichent que ce qui SERAIT fait.
if (-not $Execute) {
    $WhatIfPreference = $true
    Write-Host "MODE SIMULATION (ajoute -Execute pour créer réellement les comptes)" -ForegroundColor Yellow
}

# --- Contrôles PRÉALABLES (Test avant d'agir) -------------------------------
# On vérifie l'environnement AVANT de créer le moindre compte : il serait absurde
# de créer 50 utilisateurs puis de planter au moment d'écrire le rapport.
if (-not (Test-Path $CsvPath -PathType Leaf)) {
    throw "CSV introuvable : $CsvPath"
}
$reportDir = Split-Path -Parent $ReportPath
if (-not (Test-Path $reportDir)) {
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
}

$utilisateurs = Import-Csv $CsvPath -Encoding UTF8
$resultats = [System.Collections.Generic.List[object]]::new()

# Fichier SÉPARÉ pour la remise des mots de passe initiaux (jamais dans le rapport principal).
# À protéger par ACL et à supprimer après distribution (voir note plus bas).
# On dérive son nom de celui du rapport : rapport_xxx.csv → rapport_xxx_secrets.csv
$secretsPath = Join-Path $reportDir `
    ("{0}_secrets.csv" -f [System.IO.Path]::GetFileNameWithoutExtension($ReportPath))
$secrets = [System.Collections.Generic.List[object]]::new()

# Générateur de mot de passe initial, AUTONOME pour ce chapitre.
# (Le Ch.33 montrera une version industrialisée : RNG cryptographique + garantie de complexité.)
function New-InitialPassword {
    param(
        # Validation du paramètre (rappel Ch.3) : en dessous de 8 caractères, un mot de
        # passe initial n'a pas de sens face à une politique de domaine.
        [ValidateRange(8, 128)]
        [int]$Length = 16
    )
    # Pour le lab : simple et lisible. Voir Ch.33 pour la version robuste (cryptographique).
    $maj = "ABCDEFGHJKLMNPQRSTUVWXYZ"; $min = "abcdefghijkmnpqrstuvwxyz"
    $chi = "23456789"; $sym = "!@#%*-_"

    # Garantit au moins un caractère de chaque catégorie (conformité AD, cf. Ch.33).
    # ATTENTION : on travaille avec un TABLEAU de caractères, pas des additions de chars.
    # En PowerShell, [char] + [char] fait une addition NUMÉRIQUE ('A' + 'b' donne 195),
    # pas une concaténation : on assemble donc un tableau et on le -join à la fin.
    $obligatoires = @(
        $maj[(Get-Random -Maximum $maj.Length)]
        $min[(Get-Random -Maximum $min.Length)]
        $chi[(Get-Random -Maximum $chi.Length)]
        $sym[(Get-Random -Maximum $sym.Length)]
    )
    $tout  = ($maj + $min + $chi + $sym).ToCharArray()

    # Garde explicite : NE PAS écrire directement 1..($Length - 4). Si la différence
    # vaut 0, PowerShell évalue 1..0 comme la plage DESCENDANTE @(1, 0) — soit deux
    # caractères de trop. La validation du paramètre seule ne protège pas de ça.
    $reste = @()
    if ($Length -gt $obligatoires.Count) {
        $reste = 1..($Length - $obligatoires.Count) | ForEach-Object { $tout | Get-Random }
    }

    # Mélange final (sinon les 4 premiers seraient toujours Maj/Min/Chiffre/Symbole)
    -join (($obligatoires + $reste) | Sort-Object { Get-Random })
}

foreach ($u in $utilisateurs) {

    $statut = "OK"; $detail = ""

    try {
        # 1. Validation des données du CSV
        if (-not $u.SamAccountName -or -not $u.OU) {
            throw "Données manquantes (SamAccountName ou OU)"
        }

        # 2. Vérifier l'existence du compte (Get avant New)
        $existe = Get-ADUser -Filter "SamAccountName -eq '$($u.SamAccountName)'" -ErrorAction SilentlyContinue
        if ($existe) { throw "Le compte existe déjà" }

        # 3. Vérifier les DÉPENDANCES AVANT de créer quoi que ce soit :
        #    une OU ou un groupe inexistant doit faire échouer AVANT la création,
        #    pas après (sinon on laisse un compte à moitié configuré).
        if (-not (Test-Path "AD:\$($u.OU)")) { throw "OU introuvable : $($u.OU)" }
        if ($u.Group -and -not (Get-ADGroup -Filter "Name -eq '$($u.Group)'" -ErrorAction SilentlyContinue)) {
            throw "Groupe introuvable : $($u.Group)"
        }

        # 4. Créer le compte. ShouldProcess respecte $WhatIfPreference :
        #    en simulation il n'exécute rien, il décrit seulement l'action.
        if ($PSCmdlet.ShouldProcess($u.SamAccountName, "Créer le compte AD")) {
            # Mot de passe initial aléatoire, généré en clair le temps de le poser sur le compte
            $pwdClair = New-InitialPassword
            $motDePasse = ConvertTo-SecureString $pwdClair -AsPlainText -Force
            New-ADUser `
                -Name "$($u.GivenName) $($u.Surname)" `
                -GivenName $u.GivenName -Surname $u.Surname `
                -SamAccountName $u.SamAccountName `
                -UserPrincipalName "$($u.SamAccountName)@lab.local" `
                -Department $u.Department `
                -Path $u.OU `
                -AccountPassword $motDePasse `
                -Enabled $true `
                -ChangePasswordAtLogon $true `
                -ErrorAction Stop

            # 5. Le compte EXISTE désormais → on enregistre IMMÉDIATEMENT son mot de passe.
            #    Si on attendait la fin, un échec à l'étape suivante ferait perdre
            #    la seule information permettant la première connexion.
            $secrets.Add([PSCustomObject]@{
                Utilisateur       = $u.SamAccountName
                MotDePasseInitial = $pwdClair
            })
            $statut = "CRÉÉ"

            # 6. Ajouter au groupe — traité À PART : un échec ici ne doit pas faire
            #    croire que le compte n'a pas été créé (il l'a été, et il est activé).
            if ($u.Group) {
                try {
                    Add-ADGroupMember -Identity $u.Group -Members $u.SamAccountName -ErrorAction Stop
                }
                catch {
                    $statut = "CRÉÉ_PARTIEL"
                    $detail = "Compte créé, mais ajout au groupe '$($u.Group)' échoué : $($_.Exception.Message)"
                }
            }
        }
        else {
            $statut = "SIMULÉ"     # ShouldProcess a refusé l'action (mode simulation)
        }
    }
    catch {
        # On n'arrive ici que si RIEN n'a été créé (validation ou New-ADUser en échec)
        $statut = "ÉCHEC"
        $detail = $_.Exception.Message
    }

    # 5. Journaliser le résultat (SANS le mot de passe)
    $resultats.Add([PSCustomObject]@{
        Utilisateur    = $u.SamAccountName
        Nom            = "$($u.GivenName) $($u.Surname)"
        OU             = $u.OU
        Groupe         = $u.Group
        Statut         = $statut
        Detail         = $detail
    })
}

# 6. Rapport principal (aucun secret dedans)
$resultats | Export-Csv $ReportPath -NoTypeInformation -Encoding UTF8
$resultats | Format-Table -AutoSize

# 6bis. Remise TEMPORAIRE des mots de passe initiaux (fichier séparé, accès restreint, à détruire)
if ($secrets.Count -gt 0) {
    $secrets | Export-Csv $secretsPath -NoTypeInformation -Encoding UTF8
    # Restreindre l'accès au SEUL créateur du fichier.
    #   /inheritance:r  → supprime les autorisations héritées du dossier parent
    #   *<SID>:(F)      → contrôle total pour ce compte, désigné par son SID
    # On cible par SID (préfixe *) et non par nom : cela lève toute ambiguïté entre
    # un compte de domaine DOMAINE\alice et un compte local alice.
    # Et (F) plutôt que (R) : le fichier doit pouvoir être SUPPRIMÉ après distribution.
    $identite = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    icacls $secretsPath /inheritance:r /grant:r "*$($identite.User.Value):(F)" | Out-Null
    Write-Host "Mots de passe initiaux : $secretsPath (À DISTRIBUER PUIS SUPPRIMER)" -ForegroundColor Yellow
}

$crees    = ($resultats | Where-Object Statut -eq "CRÉÉ").Count
$partiels = ($resultats | Where-Object Statut -eq "CRÉÉ_PARTIEL").Count
$simules  = ($resultats | Where-Object Statut -eq "SIMULÉ").Count
$ko       = ($resultats | Where-Object Statut -eq "ÉCHEC").Count
Write-Host "`nTerminé : $crees créé(s), $partiels partiel(s), $simules simulé(s), $ko échec(s). Rapport : $ReportPath" -ForegroundColor Cyan
if ($partiels -gt 0) {
    Write-Host "⚠️  $partiels compte(s) créé(s) mais incomplet(s) — voir la colonne Detail du rapport." -ForegroundColor Yellow
}
```

**Utilisation :**

```powershell
# 1. D'ABORD simuler — c'est le comportement PAR DÉFAUT (rien n'est créé)
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv

# 2. Vérifier la sortie (colonne Statut = SIMULÉ), PUIS exécuter réellement
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv -Execute
```

> **⚠️ Sûr par défaut — le point le plus important de ce script.** Sans `-Execute`, le script **simule** (grâce à `$WhatIfPreference = $true` qui force tous les `ShouldProcess` en mode simulation) : la colonne `Statut` affiche `SIMULÉ` et **aucun compte n'est créé**. Il faut explicitement ajouter `-Execute` pour créer réellement. C'est exactement la philosophie du cours : on observe et on simule avant d'agir. (Tu peux aussi toujours ajouter `-WhatIf` manuellement, qui a le même effet.)

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré.

> **Note sur le mot de passe initial.** Le script est **autonome** : il définit sa propre fonction `New-InitialPassword` (pas de dépendance à un chapitre ultérieur), qui garantit au moins un caractère de chaque catégorie (majuscule, minuscule, chiffre, symbole) pour respecter la politique de complexité AD. Chaque compte reçoit un mot de passe **unique**. Ces mots de passe sont écrits dans un **fichier séparé** (`…secrets.csv`), **jamais dans le rapport principal**, avec un accès **restreint** (`icacls`) : c'est une **remise temporaire à accès restreint** — à distribuer aux utilisateurs, **puis à détruire**. Sans ça, on créerait des comptes… dont personne ne connaît le mot de passe pour la première connexion. (Le terme **stockage sécurisé** est réservé au coffre du Ch.33 : un CSV protégé par ACL n'en est pas un.)

> **🎯 Le vrai sujet d'administration : l'état « partiellement créé ».** Une opération en masse enchaîne plusieurs actions par utilisateur (créer le compte, l'ajouter à un groupe, …). Que se passe-t-il si la **deuxième** échoue ? Le compte existe déjà, activé, mais incomplet. Deux erreurs classiques :
> - Marquer l'utilisateur `ÉCHEC` : faux, et trompeur — au prochain lancement le script dira « le compte existe déjà », et personne ne saura qu'il faut finir le travail.
> - Perdre le mot de passe initial parce qu'on ne l'enregistrait qu'à la toute fin.
>
> Le script traite les deux : il **valide les dépendances (OU, groupe) AVANT** de créer quoi que ce soit — c'est le plus efficace, la plupart des échecs disparaissent —, il **enregistre le mot de passe dès que le compte existe**, et il isole l'ajout au groupe dans son propre `try/catch` pour produire un statut `CRÉÉ_PARTIEL` explicite. On préfère ici un **état honnête et rattrapable** à un rollback automatique (supprimer le compte qu'on vient de créer), plus risqué et plus complexe.
>
> **➡️ Renvoi Ch.33 :** cette gestion reste rudimentaire (fichier à accès restreint). Le Ch.33 l'industrialise : générateur **cryptographique** (`RandomNumberGenerator` plutôt que `Get-Random`) et surtout stockage des secrets dans un **coffre** (SecretManagement/SecretStore) plutôt qu'un fichier plat.

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré, et remise sécurisée des secrets.

## 🔴 Bonus

### Générer un SamAccountName automatiquement

Si le CSV ne fournit pas le `SamAccountName`, on le construit (rappel des méthodes de chaîne, Ch.5) :

```powershell
$sam = ($u.GivenName.Substring(0,1) + $u.Surname).ToLower() -replace '[^a-z]', ''
# Jean Dupont → "jdupont"
```

### Gérer les doublons de SamAccountName

Deux « Jean Dupont » donneraient le même `jdupont`. On teste et on incrémente :

```powershell
$base = $sam; $i = 1
while (Get-ADUser -Filter "SamAccountName -eq '$sam'" -ErrorAction SilentlyContinue) {
    $sam = "$base$i"; $i++
}
```

## ❌ Erreur classique

```powershell
# Bien comprendre le mode par défaut : SANS -Execute, le script SIMULE
.\Invoke-Onboarding.ps1 -CsvPath x.csv             # ✅ SIMULATION (rien n'est créé)
# Le point réellement sensible, c'est l'exécution :
.\Invoke-Onboarding.ps1 -CsvPath x.csv -Execute    # ⚠️ crée réellement les comptes
# → toujours avoir relu la sortie de la simulation AVANT d'ajouter -Execute

# Pas de try/catch → une ligne en erreur arrête tout le lot
foreach ($u in $users) { New-ADUser ... }   # ❌ un échec = tout s'arrête
# ✅ try/catch par utilisateur : on isole les échecs, on continue

# Pas de rapport → impossible de savoir ce qui a réussi/échoué
# ✅ toujours produire un rapport CSV succès/échecs

# Encodage CSV oublié → prénoms accentués cassés
Import-Csv x.csv                    # ⚠️
Import-Csv x.csv -Encoding UTF8     # ✅
```

## 💡 Exercices

**Guidé :** Crée un petit CSV de 3 utilisateurs et lance le script d'onboarding **sans `-Execute`** (mode simulation par défaut). Vérifie que la colonne `Statut` affiche `SIMULÉ` et qu'aucun compte n'est créé. Relance ensuite avec `-Execute` (sur ton lab uniquement).

**Autonome :** Ajoute au script une colonne CSV `Title` et fais en sorte qu'elle soit appliquée (`-Title`). Ajoute aussi la génération automatique du `SamAccountName` avec gestion des doublons (bonus ci-dessus).

## 🧩 Capstone Partie IV — Suite d'onboarding/offboarding

Construis deux scripts complémentaires :

1. **`Invoke-Onboarding.ps1`** (ci-dessus) : création en masse depuis CSV, avec `-WhatIf`, gestion d'erreurs par ligne, et rapport.
2. **`Invoke-Offboarding.ps1`** : pour une liste de `SamAccountName`, **désactive** le compte, le **déplace** vers `OU=Départs`, retire ses groupes, et produit un rapport. Applique la discipline `Get` avant modification et `-WhatIf`.

Ensemble, ils forment un vrai outil de gestion du cycle de vie des comptes — le genre de livrable attendu d'un administrateur junior.

## ✅ Tu sais maintenant...

- Automatiser la création de comptes AD depuis un CSV (`Import-Csv` + boucle + `New-ADUser`)
- **Simuler avec `-WhatIf`** avant toute opération de masse (la discipline poussée à son maximum)
- Isoler les erreurs par ligne (`try/catch`) pour ne pas casser tout le lot
- Produire un rapport de succès/échecs
- Assembler tout le cours dans un livrable professionnel

## 💬 Questions d'entretien typiques

- **Comment créer 100 comptes AD depuis un fichier ?** → `Import-Csv`, une boucle `foreach`, `New-ADUser` par ligne, avec validation, `try/catch` et rapport.
- **Pourquoi `-WhatIf` est-il crucial en masse ?** → Il simule l'opération sans l'exécuter : on vérifie ce qui *serait* fait avant de le faire réellement.
- **Comment éviter qu'une ligne en erreur arrête tout ?** → Encadrer chaque itération d'un `try/catch` pour isoler l'échec et poursuivre le lot.

---

# PARTIE V — GPO ET SERVICES WINDOWS SERVER

> **🏗️ On reste dans l'administration d'infrastructure.** Cette partie couvre les stratégies de groupe (GPO) et trois rôles serveur essentiels : DNS, DHCP et le partage de fichiers (SMB). Environnement requis : le lab Windows Server de la Partie IV.
>
> **PowerShell reste le fil rouge.** On n'apprend pas ici à concevoir une architecture DNS ou un plan d'adressage — on apprend à *piloter* ces rôles avec PowerShell. Pour la conception, réfère-toi aux cours dédiés à chaque technologie.
>
> **⚠️ Lab uniquement.** Comme en Partie IV, ces chapitres modifient des éléments d'infrastructure (GPO liées à des OU, enregistrements DNS, étendues DHCP, partages). Une GPO mal réglée ou un enregistrement DNS erroné affecte **tout un domaine**. Pratique exclusivement sur ton lab, et sauvegarde avant de modifier (`Backup-GPO`, export de zone…).

---

# Chapitre 25 — Group Policy (GPO)

## 🟢 Le minimum à savoir

### Comprendre le modèle AVANT les cmdlets

> **⚠️ Point pédagogique clé.** Administrer les GPO, ce n'est **pas** mémoriser `New-GPO`. C'est comprendre un **modèle** : comment une stratégie s'applique, à qui, dans quel ordre. Sans ce modèle, les cmdlets ne servent à rien. On pose donc d'abord les concepts.

Une **GPO** (Group Policy Object) est un ensemble de réglages appliqués automatiquement à des utilisateurs et/ou des ordinateurs : politique de mot de passe, fonds d'écran, restrictions, scripts de démarrage, déploiement de logiciels, réglages de sécurité (dont le Script Block Logging du Ch.35)…

### Les deux moitiés d'une GPO

Une GPO a deux sections :

- **Computer Configuration** : s'applique aux **ordinateurs** (au démarrage et périodiquement)
- **User Configuration** : s'applique aux **utilisateurs** (à la connexion et périodiquement)

Selon ce que tu veux régler, tu utilises l'une ou l'autre.

### Le mécanisme d'application : lien + héritage

Une GPO ne fait rien tant qu'elle n'est pas **liée** à un conteneur. On lie une GPO à :

- un **site**, un **domaine**, ou (le plus courant) une **OU**

Et elle s'applique à **tous les objets de ce conteneur et des OU en dessous** (héritage). D'où l'importance de la structure d'OU vue au Ch.22 : **c'est elle qui détermine qui reçoit quelles GPO**.

L'ordre d'application (le dernier gagne en cas de conflit) suit l'acronyme **LSDOU** : **L**ocal → **S**ite → **D**omaine → **OU** (de la plus haute à la plus basse). Une GPO liée à une OU proche de l'objet l'emporte donc sur une GPO de domaine.

### Les modificateurs d'héritage

Trois mécanismes altèrent cet ordre — à connaître pour comprendre ce qui s'applique vraiment :

| Mécanisme | Effet |
|-----------|-------|
| **Enforced** (Appliqué) | Force la GPO à gagner, même sur les OU enfants qui bloquent l'héritage |
| **Block Inheritance** (Bloquer l'héritage) | Une OU refuse les GPO héritées des niveaux supérieurs (sauf Enforced) |
| **Security Filtering** | Restreint l'application de la GPO à certains utilisateurs/groupes seulement |
| **WMI Filtering** | Applique la GPO seulement si une condition WMI est vraie (ex : « seulement les portables ») |

### Les cmdlets GPO `[🖥️ Server]` `[🔑 Admin]`

Elles viennent du module **GroupPolicy** (présent sur un DC ou via RSAT) :

```powershell
Import-Module GroupPolicy

Get-GPO -All                          # lister toutes les GPO
Get-GPO -Name "Politique Mot de Passe"

New-GPO -Name "Restrictions USB" -Comment "Bloque les clés USB"    # créer (vide)

# Lier une GPO à une OU (c'est le lien qui la rend active)
New-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local"

# Modifier un lien (ordre, activation, enforced)
Set-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local" -Enforced Yes

Remove-GPO -Name "Restrictions USB"   # supprimer
```

> **📌 Le piège du débutant :** `New-GPO` crée une GPO **vide et non liée** — elle ne fait rien. Il faut ensuite (1) **configurer** ses réglages (souvent via la console graphique GPMC, car PowerShell ne couvre pas tous les réglages nativement) et (2) la **lier** à une OU avec `New-GPLink`. Créer ≠ appliquer.

## 🟡 Très utile en pratique

### Documenter et sauvegarder les GPO

```powershell
# Générer un rapport HTML lisible d'une GPO (ce qu'elle contient)
Get-GPOReport -Name "Politique Mot de Passe" -ReportType Html -Path "C:\rapports\GPO_MDP.html"

# Rapport de TOUTES les GPO
Get-GPOReport -All -ReportType Html -Path "C:\rapports\Toutes_GPO.html"

# Sauvegarder / restaurer (indispensable avant toute modification)
Backup-GPO -All -Path "C:\backup\gpo"
Restore-GPO -Name "Politique Mot de Passe" -Path "C:\backup\gpo"
```

> **📌 Discipline `Get`/backup avant modification :** avant de toucher à une GPO, on la **sauvegarde** (`Backup-GPO`) et on **documente** l'existant (`Get-GPOReport`). Une GPO mal réglée peut affecter des milliers de postes d'un coup.

### Diagnostiquer ce qui s'applique réellement : RSOP

La question fréquente « pourquoi ce réglage ne s'applique-t-il pas ? » se résout avec le **Resultant Set of Policy** — l'ensemble des stratégies effectivement appliquées à un utilisateur/ordinateur :

```powershell
# Rapport RSOP pour un utilisateur sur une machine
Get-GPResultantSetOfPolicy -User lab\jdupont -Computer CLIENT01 -ReportType Html -Path "C:\rapports\rsop.html"

# En ligne de commande rapide (sur la machine cible)
gpresult /r                    # résumé des GPO appliquées
gpresult /h rsop.html          # rapport HTML complet

# Forcer la réapplication immédiate des GPO
gpupdate /force
```

## 🔴 Bonus

### Les limites de PowerShell pour les GPO

PowerShell gère très bien le **cycle de vie** des GPO (créer, lier, sauvegarder, rapporter, déléguer). Mais **modifier le contenu** d'une GPO (les milliers de réglages individuels) est partiellement couvert : `Set-GPRegistryValue` permet de piloter les réglages basés sur le registre, mais beaucoup de réglages passent encore par la console graphique (GPMC) ou des modèles ADMX. C'est une limite à connaître : PowerShell orchestre, la GPMC affine.

```powershell
# Exemple de réglage basé sur le registre via PowerShell
Set-GPRegistryValue -Name "Restrictions USB" `
    -Key "HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR" `
    -ValueName "Start" -Type DWord -Value 4
```

## ❌ Erreur classique

```powershell
# Croire que New-GPO applique quelque chose
New-GPO -Name "X"           # ❌ crée une GPO VIDE et NON LIÉE (sans effet)
# → il faut la configurer PUIS New-GPLink vers une OU

# Modifier une GPO sans sauvegarde
Set-GPRegistryValue ...     # ❌ sans filet
Backup-GPO -Name "X" -Path C:\backup ; Set-GPRegistryValue ...   # ✅

# Ne pas comprendre pourquoi une GPO ne s'applique pas
# → vérifier : lien actif ? Block Inheritance ? Security Filtering ? → RSOP / gpresult
```

## 💡 Exercices

**Guidé :** Liste toutes les GPO du domaine, puis génère un rapport HTML de l'une d'elles avec `Get-GPOReport`.

**Autonome :** Crée une GPO de test, lie-la à une OU, sauvegarde-la avec `Backup-GPO`, génère son rapport, puis nettoie (supprime le lien et la GPO).

## ✅ Tu sais maintenant...

- Le **modèle** GPO (Computer/User Config, lien, héritage LSDOU, Enforced, Block Inheritance, filtres)
- Piloter le cycle de vie des GPO (`Get`/`New`/`Remove-GPO`, `New`/`Set-GPLink`)
- Documenter (`Get-GPOReport`) et sauvegarder (`Backup`/`Restore-GPO`)
- Diagnostiquer l'application réelle (RSOP, `gpresult`, `gpupdate`)
- Que `New-GPO` ne suffit pas (créer ≠ configurer ≠ lier) et les limites de PowerShell

## 💬 Questions d'entretien typiques

- **Que fait `New-GPO` exactement ?** → Crée une GPO vide et non liée ; il faut la configurer puis la lier à une OU pour qu'elle s'applique.
- **Dans quel ordre les GPO s'appliquent-elles ?** → LSDOU : Local, Site, Domaine, OU — la dernière (OU la plus proche) l'emporte, sauf Enforced.
- **Comment savoir quelles GPO s'appliquent à un poste ?** → RSOP (`Get-GPResultantSetOfPolicy`) ou `gpresult /r` sur la machine.
- **Que faire avant de modifier une GPO ?** → La sauvegarder (`Backup-GPO`) et documenter l'existant (`Get-GPOReport`).

---

# Chapitre 26 — DNS Server

## 🟢 Le minimum à savoir

### Client vs serveur DNS

Au Ch.16, on configurait le DNS **côté client** (quels serveurs interroger, résoudre un nom). Ici, on administre le **serveur DNS** lui-même — celui qui héberge les enregistrements. Dans un domaine AD, le DNS est presque toujours installé sur les contrôleurs de domaine (AD en dépend fortement).

Le module : **DnsServer** (`[🖥️ Server]`, sur un serveur DNS ou via RSAT).

### Les zones

Une **zone** est une portion de l'espace de noms DNS que le serveur gère (ex : la zone `lab.local`). Deux grandes familles :

- **Zone de recherche directe** : nom → IP (le cas normal)
- **Zone de recherche inversée** : IP → nom (pour les requêtes PTR)

```powershell
Get-DnsServerZone                          # lister les zones
Get-DnsServerZone -Name "lab.local"        # une zone précise
```

### Les enregistrements

Une zone contient des **enregistrements** (records). Les types courants :

| Type | Rôle |
|------|------|
| **A** | Nom → adresse IPv4 |
| **AAAA** | Nom → adresse IPv6 |
| **CNAME** | Alias (un nom pointe vers un autre nom) |
| **PTR** | IP → nom (résolution inverse) |
| **MX** | Serveur de messagerie du domaine |
| **NS** | Serveur de noms de la zone |

```powershell
# Lister les enregistrements d'une zone
Get-DnsServerResourceRecord -ZoneName "lab.local"

# Filtrer par type
Get-DnsServerResourceRecord -ZoneName "lab.local" -RRType A
```

> **📌 Réflexe `Get-Member` :** `Get-DnsServerResourceRecord -ZoneName lab.local | Get-Member` révèle `HostName`, `RecordType`, `RecordData`, `TimeToLive`. La structure `RecordData` contient l'IP (pour un A) ou la cible (pour un CNAME).

### Créer et supprimer des enregistrements `[🔑 Admin]`

```powershell
# Ajouter un enregistrement A
Add-DnsServerResourceRecordA -ZoneName "lab.local" `
    -Name "srv-app" -IPv4Address "192.168.1.60"

# Ajouter un CNAME (alias)
Add-DnsServerResourceRecordCName -ZoneName "lab.local" `
    -Name "intranet" -HostNameAlias "srv-app.lab.local"

# Supprimer un enregistrement
Remove-DnsServerResourceRecord -ZoneName "lab.local" -Name "srv-app" -RRType A -Force
```

> **📌 `Get` avant d'agir :** avant d'ajouter un enregistrement `srv-app`, vérifie qu'il n'existe pas déjà (`Get-DnsServerResourceRecord -ZoneName lab.local -Name srv-app`). Un doublon d'enregistrement A crée des résolutions imprévisibles.

## 🟡 Très utile en pratique

### Vérifier la cohérence client/serveur

Le Ch.16 (client) et ce chapitre (serveur) se combinent pour diagnostiquer :

```powershell
# Côté serveur : l'enregistrement existe-t-il ?
Get-DnsServerResourceRecord -ZoneName "lab.local" -Name "srv-app"

# Côté client : la résolution fonctionne-t-elle ? (rappel Ch.16)
Resolve-DnsName "srv-app.lab.local" -Server 192.168.1.10
```

Si l'enregistrement existe côté serveur mais que le client ne résout pas : problème de cache client (`Clear-DnsClientCache`) ou de serveur DNS interrogé.

### Auditer les enregistrements d'une zone

```powershell
Get-DnsServerResourceRecord -ZoneName "lab.local" -RRType A |
    Select-Object HostName, @{N="IP";E={$_.RecordData.IPv4Address}} |
    Sort-Object HostName |
    Export-Csv "C:\rapports\dns_A_records.csv" -NoTypeInformation -Encoding UTF8
```

## 🔴 Bonus

### Zones intégrées à AD

Dans un domaine, les zones DNS sont souvent **intégrées à Active Directory** : elles sont répliquées automatiquement entre tous les DC (via la réplication AD) et sécurisées. C'est la configuration recommandée, mais sa mise en place relève d'un cours DNS/AD dédié.

## ❌ Erreur classique

```powershell
# Créer un doublon d'enregistrement A
Add-DnsServerResourceRecordA ...    # ❌ sans vérifier l'existant → résolution aléatoire
Get-DnsServerResourceRecord -ZoneName lab.local -Name srv-app   # ✅ vérifier d'abord

# Oublier de vider le cache client après un changement serveur (Ch.16)
Clear-DnsClientCache

# Confondre zone directe et inversée
# Un enregistrement PTR va dans la zone INVERSÉE, pas la directe
```

## 💡 Exercices

**Guidé :** Liste les zones du serveur DNS, puis affiche tous les enregistrements A de `lab.local` avec leur IP.

**Autonome :** Ajoute un enregistrement A `test-srv` pointant vers une IP, vérifie sa création côté serveur (`Get-DnsServerResourceRecord`) et côté client (`Resolve-DnsName`), puis supprime-le.

## ✅ Tu sais maintenant...

- La différence DNS client (Ch.16) / serveur (ici)
- Les zones (directe/inversée) et les types d'enregistrements (A, AAAA, CNAME, PTR, MX, NS)
- Lister, créer, supprimer des enregistrements (`*-DnsServerResourceRecord*`)
- Diagnostiquer en croisant serveur et client

## 💬 Questions d'entretien typiques

- **Différence entre un enregistrement A et un CNAME ?** → A pointe un nom vers une IP ; CNAME pointe un nom vers un autre nom (alias).
- **Où va un enregistrement PTR ?** → Dans une zone de recherche **inversée** (résolution IP → nom).
- **Pourquoi le DNS est-il critique en AD ?** → Active Directory repose sur le DNS pour localiser les contrôleurs de domaine et les services ; un DNS cassé casse l'authentification.

---

# Chapitre 27 — DHCP Server

## 🟢 Le minimum à savoir

### À quoi sert le DHCP

Le **DHCP** (Dynamic Host Configuration Protocol) attribue automatiquement une configuration IP (adresse, masque, passerelle, DNS) aux machines qui se connectent au réseau. Sans lui, il faudrait configurer chaque poste à la main. Au Ch.15, on voyait le côté client (« l'interface est en DHCP ») ; ici, on administre le **serveur** qui distribue les adresses.

Le module : **DhcpServer** (`[🖥️ Server]`).

### Les concepts clés

| Terme | Ce que c'est |
|-------|-------------|
| **Scope (étendue)** | Une plage d'adresses distribuables (ex : `192.168.1.100` → `192.168.1.200`) |
| **Lease (bail)** | Une adresse attribuée à une machine pour une durée limitée |
| **Reservation** | Une adresse toujours attribuée à la même machine (via son adresse MAC) |
| **Option** | Un paramètre distribué avec l'adresse (passerelle = option 3, DNS = option 6…) |

### Lister les scopes et les baux

```powershell
Get-DhcpServerv4Scope                          # les étendues configurées

# Les baux actifs d'une étendue (qui a quelle IP ?)
Get-DhcpServerv4Lease -ScopeId 192.168.1.0
```

> **📌 Réflexe `Get-Member` :** `Get-DhcpServerv4Lease -ScopeId 192.168.1.0 | Get-Member` révèle `IPAddress`, `ClientId` (la MAC), `HostName`, `AddressState`, `LeaseExpiryTime`. C'est ainsi qu'on répond à « quelle machine a l'adresse .150 ? ».

### Les réservations `[🔑 Admin]`

Une **réservation** garantit qu'une machine (identifiée par sa MAC) reçoit toujours la même IP — indispensable pour les imprimantes, serveurs, équipements :

```powershell
# Réserver 192.168.1.150 pour une imprimante (via sa MAC)
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
    -IPAddress 192.168.1.150 `
    -ClientId "00-11-22-33-44-55" `
    -Description "Imprimante Compta"

# Lister les réservations
Get-DhcpServerv4Reservation -ScopeId 192.168.1.0
```

## 🟡 Très utile en pratique

### Diagnostiquer l'épuisement d'un scope

Un problème classique : « plus personne ne reçoit d'adresse ». Souvent, le scope est **épuisé** (toutes les adresses distribuées) :

```powershell
# Statistiques d'une étendue (taux d'utilisation)
Get-DhcpServerv4ScopeStatistics -ScopeId 192.168.1.0 |
    Select-Object ScopeId, Free, InUse, PercentageInUse
```

Un `PercentageInUse` proche de 100 % explique pourquoi les nouvelles machines n'obtiennent pas d'adresse.

### Auditer les baux actifs

```powershell
Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object AddressState -eq "Active" |
    Select-Object IPAddress, HostName, ClientId, LeaseExpiryTime |
    Sort-Object IPAddress
```

Utile pour repérer une machine inconnue sur le réseau (un `HostName` ou une MAC non identifiés = point d'attention sécurité).

## 🔴 Bonus

### Convertir un bail en réservation

Quand une machine a déjà un bail et qu'on veut fixer son adresse, on peut créer la réservation depuis son bail existant — pratique pour « figer » l'IP d'un serveur récemment déployé :

```powershell
$bail = Get-DhcpServerv4Lease -ScopeId 192.168.1.0 |
    Where-Object HostName -like "SRV-APP*"
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
    -IPAddress $bail.IPAddress -ClientId $bail.ClientId -Description "SRV-APP fixé"
```

## ❌ Erreur classique

```powershell
# Créer une réservation sans vérifier l'état de l'adresse
# → s'assurer qu'elle n'est pas déjà utilisée ou réservée à un AUTRE client
# ✅ regarder les baux actifs et les réservations existantes avant de réserver
#
# ⚠️ Idée fausse fréquente : une réservation DHCP n'a PAS besoin d'être exclue du scope.
#    La réservation lie l'adresse au client désigné : le serveur ne la distribuera pas
#    à quelqu'un d'autre. Les EXCLUSIONS servent surtout aux adresses configurées
#    STATIQUEMENT sur les machines (serveurs, imprimantes, équipements réseau),
#    que le DHCP ne doit jamais proposer.

# Confondre ClientId (MAC) et IPAddress dans une réservation
Add-DhcpServerv4Reservation -ClientId "192.168.1.150"   # ❌ le ClientId est la MAC
Add-DhcpServerv4Reservation -ClientId "00-11-22-33-44-55" -IPAddress "192.168.1.150"  # ✅

# Ignorer les statistiques quand "personne n'a d'IP"
# → vérifier PercentageInUse (scope peut-être épuisé)
```

## 💡 Exercices

**Guidé :** Affiche les statistiques d'utilisation de ton étendue DHCP et ses baux actifs (IP, nom d'hôte, expiration).

**Autonome :** Crée une réservation pour une machine fictive, vérifie-la, puis supprime-la (`Remove-DhcpServerv4Reservation`). Exporte la liste des baux actifs en CSV.

## ✅ Tu sais maintenant...

- Le rôle du DHCP (attribution IP automatique) — côté serveur
- Les concepts : scope, lease, reservation, option
- Lister scopes et baux, créer des réservations (`*-DhcpServerv4*`)
- Diagnostiquer un scope épuisé (`Get-DhcpServerv4ScopeStatistics`)

## 💬 Questions d'entretien typiques

- **Différence entre un bail et une réservation ?** → Un bail est temporaire et dynamique ; une réservation attribue toujours la même IP à une machine (via sa MAC).
- **Pourquoi une machine n'obtient-elle plus d'adresse ?** → Souvent un scope épuisé (`PercentageInUse` ~100 %), à vérifier via les statistiques.
- **Comment garantir une IP fixe à une imprimante sans la configurer en statique ?** → Une réservation DHCP basée sur sa MAC.

---

# Chapitre 28 — File Server et partages SMB

## 🟢 Le minimum à savoir

### Le partage de fichiers en réseau

**SMB** (Server Message Block) est le protocole de partage de fichiers de Windows. Un **partage** (share) expose un dossier du serveur sur le réseau, accessible via `\\serveur\partage`. On gère tout ça avec le module **SmbShare**.

```powershell
Get-SmbShare                          # les partages du serveur
Get-SmbShare -Name "Compta"           # un partage précis
```

> **📌 Réflexe `Get-Member` :** `Get-SmbShare | Get-Member` révèle `Name`, `Path`, `Description`, `EncryptData`. Un partage relie un **nom réseau** à un **chemin local**.

### Créer un partage `[🔑 Admin]`

```powershell
New-SmbShare -Name "Compta" -Path "C:\Partages\Compta" `
    -Description "Dossier du service Comptabilité" `
    -FullAccess "lab\Administrateurs" `
    -ChangeAccess "lab\GG_Compta" `
    -ReadAccess "lab\GG_Consultants"
```

### LE point crucial : permissions de partage vs permissions NTFS

> **⚠️ La confusion n°1 en administration de fichiers.** Il existe **deux couches de permissions** distinctes qui se cumulent, et c'est **la plus restrictive des deux qui gagne** :
>
> 1. **Permissions de partage (SMB)** : s'appliquent quand on accède via le réseau (`\\serveur\partage`). Gérées par `Grant-SmbShareAccess`. Grossières (FullAccess / ChangeAccess / ReadAccess).
> 2. **Permissions NTFS** (Ch.9, `Get-Acl`/`Set-Acl`) : s'appliquent **toujours** (réseau ET local). Fines (par fichier/dossier, nombreux droits).
>
> **L'accès effectif = l'intersection des deux.** Si le partage autorise `Change` mais que NTFS n'autorise que `Read`, l'utilisateur n'aura que `Read`. Et inversement.

```powershell
# Permissions de PARTAGE (couche SMB)
Get-SmbShareAccess -Name "Compta"
Grant-SmbShareAccess -Name "Compta" -AccountName "lab\GG_Compta" -AccessRight Change -Force

# Permissions NTFS (couche fichiers — rappel Ch.9)
Get-Acl "C:\Partages\Compta" | Select-Object -ExpandProperty Access
```

> **Une approche courante (à comprendre, pas à appliquer aveuglément) :** beaucoup d'administrateurs mettent les permissions de partage **assez larges** et gèrent la **finesse au niveau NTFS** uniquement, pour éviter de raisonner sur deux couches en parallèle. Attention toutefois : « large » ne veut pas dire `Full Control` pour tout le monde. Donner `Full Control` en partage inclut le droit de **modifier les permissions**, ce qui est excessif ; on se limite en général à `Change` pour les groupes qui écrivent, et l'on s'appuie sur NTFS pour le détail. Le point à retenir : il faut **comprendre les deux couches** pour diagnostiquer un « je ne peux pas écrire alors que j'ai les droits » — le choix de simplifier côté partage est un compromis d'exploitation, pas une règle absolue.

### Voir qui est connecté

```powershell
Get-SmbSession                        # sessions SMB ouvertes (qui est connecté ?)
Get-SmbOpenFile                       # fichiers actuellement ouverts via le réseau
```

Utile avant une maintenance (« qui utilise ce partage là maintenant ? ») ou pour diagnostiquer un fichier verrouillé.

## 🟡 Très utile en pratique

### Diagnostiquer « je n'ai pas accès »

La séquence de dépannage type, qui combine les deux couches :

```powershell
# 1. Le partage existe et quelles permissions SMB ?
Get-SmbShare -Name "Compta"
Get-SmbShareAccess -Name "Compta"

# 2. Quelles permissions NTFS sur le dossier ? (Ch.9)
(Get-Acl "C:\Partages\Compta").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

# 3. L'utilisateur est-il dans le bon groupe ? (Ch.21)
Get-ADGroupMember "GG_Compta" | Where-Object SamAccountName -eq "jdupont"
```

Ce diagnostic croise SMB (ce chapitre), NTFS (Ch.9) et les groupes AD (Ch.21) — une vraie synthèse d'administration.

### Fermer une session ou un fichier bloqué

```powershell
# Fermer un fichier ouvert (avant maintenance) — force la fermeture côté serveur
Close-SmbOpenFile -FileId <id> -Force

# Fermer une session
Close-SmbSession -SessionId <id> -Force
```

## 🔴 Bonus

### Partages administratifs cachés

Windows crée des partages cachés (suffixés `$` : `C$`, `ADMIN$`) réservés aux administrateurs. Ils n'apparaissent pas en navigation réseau mais sont accessibles via `\\serveur\C$` :

```powershell
Get-SmbShare | Where-Object Name -like "*$"    # les partages administratifs
```

> **Sécurité :** ces partages administratifs sont utiles pour l'administration distante, mais aussi exploités par les attaquants pour se déplacer latéralement. Leur usage est surveillé en sécurité (Ch.34).

## ❌ Erreur classique

```powershell
# Ne raisonner que sur une seule couche de permissions
# ❌ "j'ai mis Full en partage mais l'utilisateur ne peut pas écrire"
# → vérifier AUSSI les permissions NTFS (l'intersection gagne)

# Créer un partage sans restreindre l'accès
New-SmbShare -Name "X" -Path "C:\X" -FullAccess "Tout le monde"   # ❌ trop ouvert
New-SmbShare -Name "X" -Path "C:\X" -ChangeAccess "lab\GG_X"       # ✅ par groupe

# Supprimer un partage occupé sans prévenir
Remove-SmbShare -Name "Compta"    # ⚠️ vérifier Get-SmbSession avant
```

## 💡 Exercices

**Guidé :** Liste les partages du serveur (hors partages administratifs `$`), avec leur chemin et leur description. Affiche les permissions SMB de l'un d'eux.

**Autonome :** Écris un script qui, pour un partage donné, affiche côte à côte ses permissions SMB (`Get-SmbShareAccess`) et NTFS (`Get-Acl`), pour visualiser les deux couches d'un coup.

## 🧩 Capstone Partie V — Rapport d'infrastructure

Construis `Get-InfraReport.ps1` (à exécuter sur le serveur) qui produit un état des lieux :

- Les GPO du domaine et leurs liens (Ch.25)
- Les zones DNS et le nombre d'enregistrements A (Ch.26)
- Les scopes DHCP et leur taux d'utilisation (Ch.27)
- Les partages SMB et leurs permissions (Ch.28)
- Le tout en sections claires, exporté en CSV (un fichier par domaine) ou en rapport HTML

C'est le type de livrable qu'un administrateur produit pour documenter une infrastructure.

## ✅ Tu sais maintenant...

- Créer et gérer des partages SMB (`*-SmbShare`)
- **La distinction cruciale permissions de partage (SMB) vs NTFS**, et que la plus restrictive gagne
- Voir les sessions et fichiers ouverts (`Get-SmbSession`, `Get-SmbOpenFile`)
- Diagnostiquer un problème d'accès en croisant SMB, NTFS et groupes AD
- Les partages administratifs cachés (`C$`, `ADMIN$`)

## 💬 Questions d'entretien typiques

- **Quelle est la différence entre permissions de partage et NTFS ?** → Le partage (SMB) ne s'applique qu'en accès réseau et reste grossier ; NTFS s'applique toujours et est fin. L'accès effectif est l'intersection (la plus restrictive gagne).
- **Un utilisateur a Full en partage mais ne peut pas écrire, pourquoi ?** → Les permissions NTFS sont probablement plus restrictives ; c'est l'intersection qui compte.
- **Comment savoir qui utilise un partage avant une maintenance ?** → `Get-SmbSession` et `Get-SmbOpenFile`.

---

# PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION

Jusqu'ici, on administrait des machines une par une, souvent en local. Cette partie change d'échelle : exécuter des commandes sur **des dizaines de machines à distance** (Remoting), puis dialoguer avec des services web via des **API REST** — en comprenant d'abord comment fonctionne l'**authentification** moderne, avant d'aborder **Microsoft Graph**.

---

# Chapitre 29 — PowerShell Remoting

## 🟢 Le minimum à savoir

### Le principe

**PowerShell Remoting** exécute des commandes sur des machines distantes — c'est l'équivalent Windows de SSH. Il repose sur **WinRM** (Windows Remote Management), le service qui écoute les connexions distantes.

Deux usages :
- **Session interactive** (`Enter-PSSession`) : tu « entres » sur la machine distante, comme SSH
- **Commande distante** (`Invoke-Command`) : tu envoies un bloc de code à exécuter, éventuellement sur plusieurs machines à la fois

### Activer le remoting `[🔑 Admin]`

```powershell
# Sur la machine CIBLE (celle qu'on veut administrer), une seule fois
Enable-PSRemoting -Force
```

En environnement AD, le remoting est souvent déjà activé (par GPO) sur les serveurs.

### Session interactive

```powershell
Enter-PSSession -ComputerName SRV01
# [SRV01]: PS C:\>   ← tu es maintenant SUR SRV01
Get-Service           # s'exécute sur SRV01
Exit-PSSession        # revenir sur ta machine
```

### Commande distante (le cas le plus puissant)

```powershell
# Sur une machine
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service -Name wuauserv }

# Sur PLUSIEURS machines à la fois
Invoke-Command -ComputerName SRV01, SRV02, DC01 -ScriptBlock {
    Get-CimInstance Win32_OperatingSystem | Select-Object LastBootUpTime
}
```

> **La propriété `PSComputerName` :** quand `Invoke-Command` cible plusieurs machines, chaque objet renvoyé porte automatiquement une propriété `PSComputerName` indiquant sa provenance. Indispensable pour savoir quel résultat vient de quelle machine :
> ```powershell
> Invoke-Command -ComputerName SRV01,SRV02 -ScriptBlock { Get-Service Spooler } |
>     Select-Object PSComputerName, Name, Status
> ```

### Le modèle d'exécution : local vs distant

> **Point important :** le `-ScriptBlock` s'exécute **sur la machine distante**, avec ses variables et son contexte. Tes variables locales n'y sont **pas** disponibles automatiquement — il faut les passer explicitement :
> ```powershell
> $nomService = "wuauserv"
> Invoke-Command -ComputerName SRV01 -ScriptBlock {
>     Get-Service -Name $using:nomService     # $using: injecte la variable locale
> }
> ```
> Le préfixe `$using:` transporte une variable locale dans le bloc distant. Sans lui, `$nomService` serait vide côté serveur.

## 🟡 WinRM, authentification et sécurité : les vraies nuances

> **⚠️ Correction d'une simplification répandue.** On lit souvent « WinRM est chiffré » ou « le remoting utilise HTTPS ». La réalité est plus nuancée, et un administrateur doit la connaître.

### Le transport : HTTP (5985) vs HTTPS (5986)

Par défaut, WinRM écoute sur le port **5985 (HTTP)**. Cela ne veut **pas** dire que tout circule en clair : dans un domaine, l'**authentification et le chiffrement** du contenu sont assurés au niveau du protocole d'authentification (voir ci-dessous), même sur le port HTTP. Le port **5986 (HTTPS)** ajoute une couche TLS au niveau **transport** (avec un certificat), utile hors domaine ou pour une exigence de conformité.

### Les mécanismes d'authentification

| Contexte | Mécanisme | Chiffrement du contenu |
|----------|-----------|----------------------|
| **Dans un domaine AD** | **Kerberos** (automatique) | Oui, assuré par Kerberos même sur HTTP/5985 |
| **Hors domaine** (workgroup) | **NTLM** ou HTTPS | NTLM chiffre le contenu ; sinon HTTPS requis |
| **Hors domaine, par IP** | Nécessite **TrustedHosts** ou HTTPS | Selon configuration |

**En résumé nuancé :**
- **En domaine :** Kerberos gère l'authentification **et** chiffre le contenu, de façon transparente, même sur le port HTTP 5985. C'est le cas le plus courant et il est sûr.
- **Hors domaine :** l'authentification par nom/IP hors domaine oblige à configurer **TrustedHosts** (liste des machines de confiance) côté client, ce qui **contourne certaines protections** — ou, mieux, à utiliser **HTTPS** avec un certificat.

```powershell
# Hors domaine : déclarer une machine de confiance (à manier avec prudence)  [🔑 Admin]
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.60" -Force

# Se connecter avec des identifiants explicites (hors domaine)
$cred = Get-Credential
Invoke-Command -ComputerName 192.168.1.60 -Credential $cred -ScriptBlock { hostname }
```

> **À retenir, sans simplifier abusivement :** ne dis pas « WinRM est toujours chiffré ». Dis plutôt : « en domaine, Kerberos authentifie et chiffre le contenu, même sur HTTP ; hors domaine, il faut NTLM correctement configuré, ou TrustedHosts (moins sûr), ou HTTPS (recommandé) ». Cette précision est ce qui distingue un administrateur qui comprend de celui qui récite.

### Les sessions persistantes

Ouvrir une connexion à chaque `Invoke-Command` est coûteux. Une **session persistante** (`PSSession`) maintient la connexion pour plusieurs commandes :

```powershell
$session = New-PSSession -ComputerName SRV01
Invoke-Command -Session $session -ScriptBlock { $svc = Get-Service }   # la variable persiste
Invoke-Command -Session $session -ScriptBlock { $svc.Count }           # réutilisable
Remove-PSSession $session                                              # fermer proprement
```

## 🔴 Bonus

### Exécution en parallèle sur un grand parc

Pour interroger beaucoup de machines, `Invoke-Command` parallélise déjà nativement (jusqu'à 32 par défaut, réglable via `-ThrottleLimit`) :

```powershell
$serveurs = Get-ADComputer -Filter "OperatingSystem -like '*Server*'" |
    Select-Object -ExpandProperty Name

Invoke-Command -ComputerName $serveurs -ThrottleLimit 20 -ScriptBlock {
    [PSCustomObject]@{
        Uptime = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
    }
} | Select-Object PSComputerName, Uptime
```

Voilà comment on obtient l'uptime de tout un parc en une commande. On croise ici le remoting (Ch.29) et l'inventaire AD (Ch.22).

## ❌ Erreur classique

```powershell
# Croire que ses variables locales sont dispo dans le ScriptBlock distant
$nom = "wuauserv"
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service $nom }   # ❌ $nom vide
Invoke-Command -ComputerName SRV01 -ScriptBlock { Get-Service $using:nom }  # ✅

# Affirmer "WinRM est toujours chiffré" sans nuance
# → vrai en domaine (Kerberos), à qualifier hors domaine (NTLM/TrustedHosts/HTTPS)

# Ajouter tout le monde dans TrustedHosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*"   # ❌ dangereux
# → lister seulement les machines nécessaires, ou utiliser HTTPS

# Oublier de fermer les sessions persistantes
New-PSSession ...    # ⚠️ sessions qui s'accumulent
Remove-PSSession ...  # ✅
```

## 💡 Exercices

**Guidé :** Avec `Invoke-Command`, récupère l'heure de dernier démarrage de deux machines de ton lab et affiche le résultat avec `PSComputerName`.

**Autonome :** Écris un script qui prend une liste de `-ComputerName`, exécute à distance une collecte (OS, uptime, espace disque C:), et renvoie un PSCustomObject par machine (avec `PSComputerName`). Gère les machines injoignables avec `try/catch`.

## ✅ Tu sais maintenant...

- Le remoting via WinRM : session interactive (`Enter-PSSession`) et commande distante (`Invoke-Command`)
- Cibler plusieurs machines et exploiter `PSComputerName`
- Passer des variables locales avec `$using:`
- **Les vraies nuances WinRM** : HTTP/5985 vs HTTPS/5986, Kerberos (domaine) vs NTLM/TrustedHosts/HTTPS (hors domaine)
- Les sessions persistantes (`New`/`Remove-PSSession`)

## 💬 Questions d'entretien typiques

- **Le remoting WinRM est-il chiffré ?** → En domaine, oui : Kerberos authentifie et chiffre le contenu même sur le port HTTP 5985. Hors domaine, il faut NTLM correctement configuré, TrustedHosts (moins sûr) ou HTTPS.
- **Comment utiliser une variable locale dans un `Invoke-Command` distant ?** → Avec le préfixe `$using:`.
- **Comment savoir de quelle machine vient un résultat ?** → La propriété `PSComputerName`, ajoutée automatiquement par `Invoke-Command`.
- **Pourquoi `TrustedHosts = *` est-il déconseillé ?** → Il fait confiance à toutes les machines, contournant des protections ; on limite à la liste nécessaire ou on utilise HTTPS.

---

# Chapitre 30 — Authentification, autorisation et tokens

## 🟢 Le minimum à savoir

> **Pourquoi ce chapitre avant les API ?** Sans lui, on arrive à `-Headers @{ Authorization = "Bearer $token" }` sans comprendre d'où vient `$token` ni ce qu'il autorise. Ce chapitre donne le **modèle mental** nécessaire — pas un cours complet d'OAuth, juste ce qu'il faut pour utiliser une API et Microsoft Graph en connaissance de cause.

### Authentification vs autorisation : deux choses différentes

C'est la distinction fondamentale, souvent confondue :

- **Authentification** (AuthN) : **qui es-tu ?** Prouver son identité (mot de passe, certificat, token…).
- **Autorisation** (AuthZ) : **qu'as-tu le droit de faire ?** Une fois identifié, quelles actions te sont permises.

On peut être authentifié (identifié) sans être autorisé (avoir le droit) pour une action donnée. Les deux étapes sont séparées.

### Les grandes méthodes d'authentification aux API

| Méthode | Principe | Sécurité |
|---------|----------|----------|
| **API Key** | Une clé secrète envoyée à chaque requête (souvent dans un header) | Simple, mais la clé = accès total si elle fuite |
| **Basic Auth** | Nom + mot de passe encodés en base64 dans le header | Historique, à éviter (le mot de passe circule à chaque appel) |
| **Bearer Token** | Un jeton temporaire obtenu après authentification | Moderne, recommandé (jeton à durée limitée) |

> **⚠️ Base64 n'est PAS du chiffrement.** Le « base64 » de Basic Auth est un simple **encodage**, décodable instantanément. Il ne protège rien par lui-même — c'est **HTTPS** (le transport chiffré) qui protège les identifiants en circulation. Ne confonds jamais encodage (base64) et chiffrement.

### Le Bearer Token : le modèle moderne

Le schéma dominant aujourd'hui :

1. Tu t'authentifies auprès d'un **serveur d'autorisation** (avec des identifiants, un certificat, etc.)
2. Il te délivre un **access token** (un jeton) à durée de vie limitée (souvent ~1h)
3. Tu joins ce token à chaque requête API dans un header : `Authorization: Bearer <token>`
4. L'API vérifie le token et t'autorise (ou non) selon ce qu'il contient

```powershell
# Le token une fois obtenu (on verra comment au Ch.31-32)
$headers = @{ Authorization = "Bearer $token" }
Invoke-RestMethod -Uri "https://api.exemple.com/v1/users" -Headers $headers
```

L'intérêt du token : il **expire** (limite les dégâts en cas de fuite), et il peut porter des **permissions précises** (les scopes).

### OAuth 2.0, à très haut niveau

**OAuth 2.0** est le standard qui orchestre cette délivrance de tokens. Sans entrer dans les détails, retiens les acteurs :

- **Resource Owner** : l'utilisateur (toi) ou l'organisation propriétaire des données
- **Client** : l'application qui veut accéder aux données (ton script)
- **Authorization Server** : celui qui authentifie et délivre les tokens (ex : Entra ID pour Microsoft)
- **Resource Server** : l'API qui héberge les données (ex : Microsoft Graph)

Le flux, très simplifié : *le client demande un token à l'Authorization Server, en prouvant son identité et en précisant les permissions voulues (scopes) ; s'il est autorisé, il reçoit un access token qu'il présente au Resource Server.*

### Les scopes : des permissions précises

Un **scope** est une permission granulaire attachée au token : `User.Read`, `User.ReadWrite.All`, `Group.Read.All`… Le token ne donne accès qu'à ce que ses scopes permettent. C'est le principe de **moindre privilège** appliqué aux API : on ne demande que les scopes strictement nécessaires.

## 🟡 Très utile en pratique

### Permissions déléguées vs permissions d'application

Distinction **cruciale** pour Microsoft Graph (Ch.32), et souvent mal comprise :

| Type | Qui agit ? | Exemple d'usage |
|------|-----------|-----------------|
| **Déléguée** | L'application agit **au nom d'un utilisateur connecté** | Un script interactif : « lis MES emails » — limité aux droits de l'utilisateur |
| **Application** | L'application agit **en son propre nom**, sans utilisateur | Un service automatisé/planifié : « lis les emails de toute l'organisation » — droits larges, sans humain |

> **Conséquence pratique :** un script d'administration **interactif** utilise généralement des permissions **déléguées** (tu te connectes, le script agit avec tes droits). Un script **automatisé** (tâche planifiée, sans humain) utilise des permissions **d'application** (l'app a ses propres droits, via un secret ou un certificat). Les permissions d'application sont plus puissantes et donc plus sensibles — elles doivent être minimales et surveillées.

### Où stocker un token ou un secret ?

> **Jamais en clair dans le script.** Un token, une API key, un secret client ne doivent pas être écrits en dur. On les stocke dans un **SecureString**, un coffre (SecretManagement), une variable d'environnement protégée, ou on utilise un certificat. Le Ch.33 détaille ces mécanismes. Retiens dès maintenant : un secret dans un `.ps1` versionné dans Git est une fuite garantie.

## 🔴 Bonus

### Anatomie d'un token JWT

Les access tokens sont souvent des **JWT** (JSON Web Tokens) : trois parties séparées par des points (`header.payload.signature`), encodées en base64url. Le *payload* contient des *claims* (qui, quels scopes, quelle expiration). On peut le décoder (sans la clé) pour l'inspecter — utile pour déboguer « pourquoi mon appel est refusé ? » (souvent un scope manquant ou un token expiré). Décoder ≠ falsifier : la **signature** garantit l'intégrité.

## ❌ Erreur classique

```powershell
# Confondre authentification et autorisation
# → être connecté ne signifie pas avoir le droit pour CETTE action

# Croire que base64 protège quelque chose
# ❌ base64 = encodage réversible, PAS du chiffrement → HTTPS est ce qui protège

# Demander des scopes trop larges "pour être tranquille"
# ❌ viole le moindre privilège → ne demander que le nécessaire

# Écrire un token/secret en dur dans le script
$token = "eyJ0eXAi..."   # ❌ fuite si versionné → coffre/SecureString (Ch.33)
```

## 💡 Exercices

**Guidé (conceptuel) :** Pour chacun de ces cas, dis s'il faut des permissions **déléguées** ou **d'application** : (a) un script interactif où l'admin lit ses propres groupes ; (b) une tâche planifiée nocturne qui désactive les comptes inactifs de toute l'organisation.

**Autonome (conceptuel) :** Explique en 3-4 phrases, à un collègue débutant, pourquoi `Authorization: Bearer <token>` est plus sûr que d'envoyer un mot de passe à chaque requête. Mentionne l'expiration et les scopes.

## ✅ Tu sais maintenant...

- La différence **authentification** (qui es-tu) / **autorisation** (qu'as-tu le droit de faire)
- Les méthodes : API Key, Basic (à éviter), **Bearer Token** (moderne)
- Que **base64 ≠ chiffrement** (c'est HTTPS qui protège le transport)
- **OAuth 2.0** à haut niveau : client, authorization server, resource server, access token
- Les **scopes** (permissions granulaires, moindre privilège)
- **Déléguées vs application** — distinction clé pour Graph
- Qu'un secret ne s'écrit **jamais** en clair (Ch.33)

## 💬 Questions d'entretien typiques

- **Différence entre authentification et autorisation ?** → AuthN prouve l'identité (qui es-tu) ; AuthZ décide des droits (qu'as-tu le droit de faire).
- **Pourquoi un Bearer token est-il préférable à Basic Auth ?** → Il expire (limite les dégâts d'une fuite), porte des scopes précis, et évite d'envoyer le mot de passe à chaque requête.
- **Permissions déléguées ou d'application pour une tâche planifiée sans utilisateur ?** → D'application (l'app agit en son propre nom) — puissantes, donc à restreindre au minimum.
- **base64 protège-t-il un mot de passe ?** → Non, c'est un encodage réversible ; seule la couche HTTPS protège les identifiants en transit.

---

# Chapitre 31 — API REST avec PowerShell

## 🟢 Le minimum à savoir

### Ce qu'est une API REST, en clair

Une **API REST** est une interface qui permet à des programmes de dialoguer via le web. Concrètement : tu envoies une requête HTTP à une **URL** (endpoint), et tu reçois une réponse, presque toujours en **JSON**. C'est ainsi qu'un script PowerShell peut interroger un service en ligne, un outil de ticketing, un système de supervision, ou Microsoft Graph (Ch.32).

### Le vocabulaire HTTP minimal

| Terme | Ce que c'est |
|-------|-------------|
| **URI / endpoint** | L'adresse de la ressource (`https://api.exemple.com/v1/users`) |
| **Méthode** | L'action : `GET` (lire), `POST` (créer), `PUT`/`PATCH` (modifier), `DELETE` (supprimer) |
| **Headers** | Métadonnées de la requête (authentification, type de contenu…) |
| **Body** | Les données envoyées (pour POST/PUT/PATCH), en général du JSON |
| **Status code** | Le résultat : `200` OK, `201` créé, `401` non authentifié, `403` interdit, `404` introuvable, `429` trop de requêtes, `500` erreur serveur |

### `Invoke-RestMethod` : la cmdlet clé

`Invoke-RestMethod` envoie une requête HTTP **et convertit automatiquement le JSON de réponse en objets PowerShell**. C'est ce qui rend PowerShell si agréable pour les API :

```powershell
# GET simple — la réponse JSON devient un objet directement exploitable
$reponse = Invoke-RestMethod -Uri "https://api.github.com/users/powershell"
$reponse.name           # "PowerShell"
$reponse.public_repos   # un nombre
```

> **📌 Réflexe `Get-Member` :** `Invoke-RestMethod -Uri "..." | Get-Member` te montre la structure de la réponse — les propriétés que l'API renvoie. C'est ainsi qu'on découvre ce qu'une API expose, sans deviner.

### `Invoke-RestMethod` vs `Invoke-WebRequest`

- **`Invoke-RestMethod`** : parse automatiquement le JSON en objets. **À privilégier pour les API REST.**
- **`Invoke-WebRequest`** : renvoie la réponse HTTP brute (status, headers, contenu texte). Utile quand on a besoin des détails HTTP (code de statut exact, headers de réponse) ou pour du web non-API.

### Envoyer des headers (dont l'authentification)

Rappel du Ch.30 : l'authentification passe souvent par un header `Authorization` :

```powershell
$headers = @{
    Authorization = "Bearer $token"
    Accept        = "application/json"
}
Invoke-RestMethod -Uri "https://api.exemple.com/v1/me" -Headers $headers
```

### Envoyer des données : POST avec un body JSON

```powershell
# Construire le corps comme une hashtable, puis le convertir en JSON
$corps = @{
    name  = "Nouveau projet"
    owner = "equipe-infra"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://api.exemple.com/v1/projects" `
    -Method Post `
    -Headers $headers `
    -Body $corps `
    -ContentType "application/json"
```

> **Le duo `ConvertTo-Json` / `ConvertFrom-Json` :** on construit le body avec une hashtable qu'on convertit en JSON (`ConvertTo-Json`) ; et si on reçoit du JSON brut (via `Invoke-WebRequest`), on le reconvertit en objets avec `ConvertFrom-Json`. Avec `Invoke-RestMethod`, la conversion de la réponse est automatique.

## 🟡 Très utile en pratique

### Gérer les erreurs HTTP

Une requête peut échouer (401, 404, 500…). On l'encadre d'un `try/catch` (rappel Ch.8) :

```powershell
try {
    $r = Invoke-RestMethod -Uri "https://api.exemple.com/v1/users/999" `
        -Headers $headers -ErrorAction Stop
}
catch {
    $code = $_.Exception.Response.StatusCode.value__
    switch ($code) {
        401 { Write-Warning "Non authentifié — token invalide ou expiré (Ch.30)" }
        403 { Write-Warning "Interdit — scope insuffisant (Ch.30)" }
        404 { Write-Warning "Ressource introuvable" }
        429 { Write-Warning "Trop de requêtes — ralentir (throttling)" }
        default { Write-Warning "Erreur HTTP $code : $($_.Exception.Message)" }
    }
}
```

> **Diagnostic croisé Ch.30 :** un `401` renvoie souvent à un token expiré, un `403` à un **scope manquant**. Comprendre l'auth (Ch.30) rend le débogage des API bien plus rapide.

### La pagination

Les API limitent le nombre de résultats par réponse et fournissent un lien vers la « page suivante ». Il faut boucler tant qu'il y en a une :

```powershell
$url = "https://api.exemple.com/v1/users?limit=100"
$tous = [System.Collections.Generic.List[object]]::new()

while ($url) {
    $page = Invoke-RestMethod -Uri $url -Headers $headers
    $page.data | ForEach-Object { $tous.Add($_) }
    $url = $page.next_page_url    # null quand il n'y a plus de page → sort de la boucle
}

"Total récupéré : $($tous.Count)"
```

Le nom du champ de pagination varie selon l'API (`next`, `next_page_url`, `@odata.nextLink` pour Graph…) — c'est là que lire la doc de l'API est indispensable.

### Query parameters

Les paramètres de requête affinent une requête GET (`?cle=valeur&autre=valeur`) :

```powershell
$params = @{ q = "powershell"; sort = "stars"; per_page = 5 }
Invoke-RestMethod -Uri "https://api.github.com/search/repositories" -Body $params
# En GET, -Body est encodé comme query string : ?q=powershell&sort=stars&per_page=5
```

## 🔴 Bonus

### Un mini-connecteur réutilisable

En pratique, on encapsule les appels dans une fonction, avec l'auth et la gestion d'erreurs centralisées :

```powershell
function Invoke-MonApi {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Endpoint,
        [string]$Method = "Get",
        [object]$Body
    )
    $headers = @{ Authorization = "Bearer $script:Token"; Accept = "application/json" }
    $params = @{
        Uri = "https://api.exemple.com/v1/$Endpoint"
        Method = $Method; Headers = $headers; ErrorAction = "Stop"
    }
    if ($Body) { $params.Body = ($Body | ConvertTo-Json); $params.ContentType = "application/json" }
    Invoke-RestMethod @params    # splatting (Ch.3)
}

Invoke-MonApi -Endpoint "users" | Select-Object id, name
```

Ce pattern (splatting + fonction + gestion d'erreurs) est directement réutilisable pour n'importe quelle API. Le `$script:Token` est ici une variable de portée script : en pratique, on la remplit depuis un coffre (`Get-Secret`, Ch.33), jamais avec un token écrit en dur.

## ❌ Erreur classique

```powershell
# Utiliser Invoke-WebRequest et parser le JSON à la main
$r = Invoke-WebRequest -Uri "..."; $data = $r.Content | ConvertFrom-Json   # ⚠️ verbeux
$data = Invoke-RestMethod -Uri "..."   # ✅ conversion automatique

# Oublier -ContentType sur un POST JSON
Invoke-RestMethod -Uri "..." -Method Post -Body $json   # ⚠️ l'API peut mal interpréter
Invoke-RestMethod -Uri "..." -Method Post -Body $json -ContentType "application/json"  # ✅

# Ne pas gérer la pagination → ne récupérer que la 1re page
# ✅ boucler tant qu'il y a une "page suivante"

# Ignorer le status code en cas d'échec
# ✅ try/catch + lire $_.Exception.Response.StatusCode
```

## 💡 Exercices

**Guidé :** Avec `Invoke-RestMethod`, interroge `https://api.github.com/users/microsoft` et affiche le nom, le nombre de dépôts publics et la date de création. Explore la réponse avec `Get-Member`.

**Autonome :** Écris une fonction `Get-GitHubRepos -User <nom>` qui récupère les dépôts publics d'un utilisateur GitHub (gère la pagination via le header `Link` ou le paramètre `page`), et exporte nom + langage + nombre d'étoiles en CSV.

## ✅ Tu sais maintenant...

- Ce qu'est une API REST (endpoint, méthode, headers, body, status code)
- `Invoke-RestMethod` (JSON → objets automatiquement) vs `Invoke-WebRequest`
- Envoyer des headers d'authentification (Bearer, rappel Ch.30) et un body JSON (`ConvertTo-Json`)
- Gérer les erreurs HTTP (401/403/404/429) et la **pagination**
- Encapsuler les appels dans une fonction réutilisable

## 💬 Questions d'entretien typiques

- **`Invoke-RestMethod` ou `Invoke-WebRequest` ?** → `Invoke-RestMethod` pour les API REST (conversion JSON→objets automatique) ; `Invoke-WebRequest` quand on a besoin des détails HTTP bruts.
- **Que signifie un 401 vs un 403 ?** → 401 = non authentifié (token absent/expiré) ; 403 = authentifié mais non autorisé (scope insuffisant).
- **Comment récupérer tous les résultats d'une API paginée ?** → Boucler en suivant le lien de page suivante jusqu'à ce qu'il soit nul.

---

# Chapitre 32 — Microsoft Graph et Entra ID

## 🟢 Le minimum à savoir

### Ce qu'est Microsoft Graph

**Microsoft Graph** est l'API REST unifiée de Microsoft 365 et **Entra ID** (l'ancien Azure Active Directory — l'annuaire *cloud*, à distinguer de l'AD *on-premise* des Parties IV-V). Via Graph, on administre les utilisateurs, groupes, licences, appareils, e-mails, équipes Teams… du cloud Microsoft. C'est l'équivalent moderne, côté cloud, de ce qu'on faisait avec le module `ActiveDirectory` en local.

> **AD on-premise vs Entra ID :** l'Active Directory des Parties IV-V vit sur **tes serveurs** (contrôleurs de domaine). **Entra ID** est l'annuaire **dans le cloud** Microsoft. Beaucoup d'organisations utilisent les deux, synchronisés. Les cmdlets diffèrent : `Get-ADUser` (on-premise) vs `Get-MgUser` (cloud). Ne les confonds pas.

### Deux façons d'appeler Graph

1. **Le module Microsoft Graph PowerShell** (`Microsoft.Graph`) : des cmdlets prêtes à l'emploi (`Get-MgUser`…) qui gèrent l'authentification et la pagination pour toi. **Recommandé pour débuter.**
2. **Les appels REST directs** (`Invoke-RestMethod` vers `https://graph.microsoft.com`) : plus de contrôle, mais tu gères toi-même le token et la pagination (Ch.31). Utile quand une fonctionnalité n'est pas couverte par le module.

### Installer et se connecter (module)

```powershell
# Installer le module (une fois) — en CurrentUser, PAS besoin de console admin
Install-Module Microsoft.Graph -Scope CurrentUser

# Se connecter en demandant les SCOPES nécessaires (rappel Ch.30 : moindre privilège)
Connect-MgGraph -Scopes "User.Read.All", "Group.Read.All"
```

> **Note :** l'installation en `-Scope CurrentUser` ne nécessite **pas** de console administrateur (elle s'installe dans ton profil). Microsoft **recommande PowerShell 7** pour le SDK Graph ; il peut fonctionner sur d'autres versions selon les prérequis, mais 7 est la cible conseillée.

> **Le lien direct avec le Ch.30 :** `Connect-MgGraph -Scopes ...` matérialise tout ce qu'on a vu sur l'autorisation. Tu demandes des **scopes** précis ; une fenêtre de connexion t'authentifie (permissions **déléguées** : le script agira avec **tes** droits) ; un **token** est obtenu et géré par le module. Tu ne vois pas le token, mais c'est bien le mécanisme du Ch.30 qui opère.

### Interroger Graph (module)

```powershell
# L'utilisateur actuellement connecté
Get-MgContext                                   # contexte : compte, scopes accordés

# Rechercher un utilisateur
Get-MgUser -Filter "startsWith(displayName,'Jean')" |
    Select-Object DisplayName, UserPrincipalName, Id

# Lister des groupes
Get-MgGroup -Top 10 | Select-Object DisplayName, Id

# Les membres d'un groupe
Get-MgGroupMember -GroupId "<id-du-groupe>"
```

> **📌 Réflexe `Get-Member` :** `Get-MgUser -Top 1 | Get-Member` révèle les propriétés d'un utilisateur Entra ID (`DisplayName`, `UserPrincipalName`, `Mail`, `AccountEnabled`, `Id`…). Comme pour l'AD on-premise, certains attributs nécessitent d'être demandés explicitement (`-Property`).

### Se déconnecter

```powershell
Disconnect-MgGraph
```

## 🟡 Très utile en pratique

### Les scopes et le consentement

La première connexion avec de nouveaux scopes déclenche un **consentement** : Microsoft demande d'approuver les permissions. C'est le principe d'autorisation du Ch.30 rendu visible.

- Un scope en **lecture** (`User.Read.All`) suffit pour un rapport — ne demande pas d'écriture « au cas où ».
- Un scope en **écriture** (`User.ReadWrite.All`) est nécessaire pour modifier — et bien plus sensible.

```powershell
# Pour un rapport : lecture seule (moindre privilège)
Connect-MgGraph -Scopes "User.Read.All"

# Pour modifier des comptes : écriture (plus sensible, à justifier)
Connect-MgGraph -Scopes "User.ReadWrite.All"
```

### Un rapport d'utilisateurs Entra ID

```powershell
Connect-MgGraph -Scopes "User.Read.All"

Get-MgUser -All -Property DisplayName, UserPrincipalName, AccountEnabled, Department |
    Select-Object DisplayName, UserPrincipalName, AccountEnabled, Department |
    Export-Csv "C:\rapports\entra_users.csv" -NoTypeInformation -Encoding UTF8

Disconnect-MgGraph
```

On retrouve exactement le schéma des rapports AD (Ch.23), transposé au cloud : requête filtrée → projection → export.

### Appel REST direct (quand le module ne couvre pas un endpoint)

Le SDK fournit `Invoke-MgGraphRequest`, qui appelle **n'importe quel endpoint Graph en réutilisant le contexte d'authentification** de `Connect-MgGraph` — sans que tu aies à manipuler le token toi-même :

```powershell
# Après Connect-MgGraph : appeler un endpoint brut avec le contexte déjà authentifié
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"

# Un endpoint moins courant, non couvert par une cmdlet dédiée
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$top=5"
```

> **Attention à une confusion courante :** `Get-MgContext` renvoie le **contexte** (compte, scopes accordés, tenant) — **pas** un access token prêt à coller dans un header `Authorization`. Pour un appel REST authentifié, utilise `Invoke-MgGraphRequest` (qui gère le token pour toi), plutôt que d'essayer d'extraire un bearer token du contexte.

> **Renvoi Ch.31 — attention à la pagination.** `Invoke-MgGraphRequest` gère l'**authentification** (il réutilise la session `Connect-MgGraph`, tu n'as pas à manipuler le token). Mais il **ne suit pas automatiquement la pagination** : si la réponse contient un `@odata.nextLink`, c'est à **toi** de rappeler cette URL pour récupérer les pages suivantes (comme au Ch.31). En résumé : les **cmdlets** Graph avec `-All` (ex. `Get-MgUser -All`) parcourent les pages pour toi ; `Invoke-MgGraphRequest` gère l'auth mais te laisse suivre `@odata.nextLink` toi-même. L'appel `Invoke-RestMethod` totalement manuel (avec ton propre token) reste possible quand tu gères l'authentification hors du SDK.

## 🔴 Bonus

### Permissions d'application pour l'automatisation

Les exemples ci-dessus utilisent des permissions **déléguées** (tu te connectes interactivement). Pour une **tâche planifiée sans humain** (rappel Ch.30), on utilise des permissions **d'application** : on enregistre une *app* dans Entra ID, on lui attribue des permissions d'application, et on s'authentifie avec un **certificat** (préférable) ou un **secret client**. C'est plus puissant (agit sur toute l'organisation, sans utilisateur) donc plus sensible — à réserver aux automatisations, avec des permissions minimales.

```powershell
# Authentification applicative (schéma), pour un script non interactif
Connect-MgGraph -ClientId "<app-id>" -TenantId "<tenant-id>" -CertificateThumbprint "<empreinte>"
```

## ❌ Erreur classique

```powershell
# Confondre AD on-premise et Entra ID
Get-ADUser alice        # ❌ AD local — ne marche pas pour le cloud
Get-MgUser -Filter "..."   # ✅ pour Entra ID (cloud)

# Demander des scopes en écriture pour un simple rapport
Connect-MgGraph -Scopes "User.ReadWrite.All"   # ❌ trop pour lire
Connect-MgGraph -Scopes "User.Read.All"         # ✅ moindre privilège

# Oublier de se déconnecter / laisser des scopes larges accordés
Disconnect-MgGraph   # ✅ bonne hygiène

# Croire que Get-MgUser renvoie tous les attributs
Get-MgUser -Top 1                              # ⚠️ jeu réduit
Get-MgUser -Top 1 -Property Department, Mail   # ✅ demander explicitement
```

## 💡 Exercices

**Guidé (nécessite un tenant de test/dev) :** Connecte-toi à Graph en lecture (`User.Read.All`), affiche ton propre compte avec `Get-MgContext`, puis liste 5 utilisateurs avec leur UPN.

**Autonome :** Écris un script qui produit un rapport CSV des utilisateurs Entra ID désactivés (`AccountEnabled -eq $false`), avec leur nom, UPN et service. Utilise le bon scope minimal et déconnecte-toi à la fin.

## ✅ Tu sais maintenant...

- Ce qu'est Microsoft Graph (API unifiée M365/Entra ID) et la différence **AD on-premise / Entra ID cloud**
- Les deux approches : **module `Microsoft.Graph`** (recommandé) vs **REST direct** (Ch.31)
- `Connect-MgGraph -Scopes` comme application concrète de l'autorisation (Ch.30)
- Interroger utilisateurs/groupes (`Get-MgUser`, `Get-MgGroup`) et produire des rapports
- Déléguées (interactif) vs application (automatisation) pour Graph

## 💬 Questions d'entretien typiques

- **Différence entre AD on-premise et Entra ID ?** → L'AD on-premise vit sur tes contrôleurs de domaine ; Entra ID est l'annuaire cloud de Microsoft. Cmdlets différentes (`Get-ADUser` vs `Get-MgUser`).
- **Module Graph ou REST direct ?** → Le module pour la simplicité (auth et pagination gérées) ; le REST direct pour le contrôle fin ou ce que le module ne couvre pas.
- **Que fait `Connect-MgGraph -Scopes` ?** → Il demande des permissions précises, authentifie l'utilisateur et obtient un token — l'autorisation OAuth du Ch.30 en pratique.
- **Déléguées ou application pour un script planifié Graph ?** → Application (pas d'utilisateur interactif), avec certificat de préférence, permissions minimales.

---

# PARTIE VII — AUTOMATISATION ET INDUSTRIALISATION

Tu sais maintenant administrer une machine, un domaine, un parc, des API. Cette partie répond à une question de maturité : **comment transformer des scripts « qui marchent » en outils fiables, réutilisables et sûrs ?** C'est ce qui distingue un script bricolé d'un outil de production.

---

# Chapitre 33 — Industrialiser ses scripts

## 🟢 Le minimum à savoir

### Des scripts aux modules

Un **module** regroupe des fonctions réutilisables dans un fichier `.psm1`, qu'on importe comme les modules natifs. C'est ainsi qu'on capitalise : au lieu de copier-coller `Test-ServerHealth` dans dix scripts, on la range dans un module.

```powershell
# MonModule.psm1 — plusieurs fonctions réutilisables
function Test-ServerHealth { <# ... #> }
function Get-DiskAlert     { <# ... #> }
Export-ModuleMember -Function Test-ServerHealth, Get-DiskAlert
```

```powershell
# Utilisation
Import-Module .\MonModule.psm1
Test-ServerHealth -ComputerName SRV01
```

Un module bien rangé (dans un dossier du `$env:PSModulePath`) devient disponible partout, comme les cmdlets natives.

### Le splatting pour des appels lisibles

Rappel du Ch.3, désormais systématique dès qu'un appel a plus de 3-4 paramètres :

```powershell
$params = @{
    Name          = "svc_backup"
    Path          = "OU=Services,DC=lab,DC=local"
    AccountPassword = $pwd
    Enabled       = $true
    ChangePasswordAtLogon = $true
}
New-ADUser @params      # bien plus lisible qu'une ligne à rallonge avec des backticks
```

### Externaliser la configuration

Un bon script ne code pas ses valeurs en dur : serveurs, seuils, chemins vont dans un fichier de config (JSON, souvent) qu'on lit au démarrage :

```powershell
# config.json
# { "Serveurs": ["DC01","SRV01"], "SeuilDisqueGB": 20, "Rapport": "C:\\rapports" }

$config = Get-Content ".\config.json" -Encoding UTF8 | ConvertFrom-Json
$config.Serveurs | ForEach-Object { Test-ServerHealth -ComputerName $_ }
```

Changer un seuil ou ajouter un serveur ne demande alors plus de toucher au code — juste la config.

### Journaliser (logs)

Un script de production doit laisser une trace exploitable :

```powershell
function Write-Log {
    param([string]$Message, [ValidateSet("INFO","WARN","ERROR")][string]$Level = "INFO")
    $ligne = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') [$Level] $Message"
    $ligne | Add-Content -Path "C:\logs\script.log" -Encoding UTF8
    if ($Level -eq "ERROR") { Write-Host $ligne -ForegroundColor Red }
}

Write-Log "Début du traitement" -Level INFO
Write-Log "Serveur injoignable" -Level ERROR
```

## 🟡 Très utile en pratique

### Gérer les secrets proprement

> **⚠️ Rappel des Ch.10, 20, 30 : un secret ne s'écrit JAMAIS en clair dans un script.** Voici les mécanismes propres, du plus simple au plus robuste.

**SecureString** — pour ne pas manipuler un mot de passe en clair en mémoire :

```powershell
$pwd = Read-Host "Mot de passe" -AsSecureString      # saisie masquée
# ou, à partir d'un texte (ex : mot de passe généré), sans jamais l'écrire en dur
```

**Le module SecretManagement** — un coffre-fort pour les secrets, la vraie bonne pratique :

```powershell
Install-Module Microsoft.PowerShell.SecretManagement, Microsoft.PowerShell.SecretStore -Scope CurrentUser
Register-SecretVault -Name Coffre -ModuleName Microsoft.PowerShell.SecretStore -DefaultVault

# Stocker SANS écrire le secret sur la ligne de commande (sinon il finit dans l'historique !)
$secret = Read-Host "Valeur du secret" -AsSecureString
Set-Secret -Name "ApiToken" -SecureStringSecret $secret     # stocker (chiffré)

$token = Get-Secret -Name "ApiToken" -AsPlainText            # récupérer au moment de l'usage
```

> **⚠️ Ne mets jamais le secret en clair sur la ligne `Set-Secret`.** Écrire `Set-Secret -Secret "valeur-du-token"` place la valeur dans l'**historique** de ta console (`Get-History`, fichier `PSReadLine`) — une fuite. Saisis-le via `Read-Host -AsSecureString` (masqué, non historisé), comme ci-dessus.

Ainsi, le secret n'apparaît **jamais** dans le code source ni dans l'historique. C'est ce qu'on utilise pour les tokens d'API (Ch.30-31), les identifiants Graph applicatifs (Ch.32), les mots de passe de comptes de service.

**Générer un mot de passe initial aléatoire** (pour l'onboarding, Ch.24). Deux exigences : un **générateur cryptographique** (`RandomNumberGenerator`, pas `Get-Random`), **et** une **composition garantie** (AD peut exiger au moins 3 catégories parmi majuscule/minuscule/chiffre/symbole). On tire donc au moins un caractère de chaque catégorie, puis on complète, puis on mélange :

```powershell
function New-RandomPassword {
    param(
        # Validation (Ch.3) : en dessous de 8, la garantie « une majuscule + une minuscule
        # + un chiffre + un symbole » deviendrait plus longue que le mot de passe demandé.
        [ValidateRange(8, 128)]
        [int]$Length = 16
    )

    # RNG cryptographique : renvoie un entier dans [0, max)
    function Get-CryptoIndex([int]$max) {
        $bytes = [byte[]]::new(4)
        $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
        try { $rng.GetBytes($bytes) } finally { $rng.Dispose() }
        # ToUInt32 (non signé) plutôt que ToInt32 + [math]::Abs() : Abs() lèverait une
        # exception sur Int32.MinValue, dont la valeur absolue n'est pas représentable.
        [int]([BitConverter]::ToUInt32($bytes, 0) % $max)
    }

    $cat = @{
        Maj = "ABCDEFGHJKLMNPQRSTUVWXYZ"
        Min = "abcdefghijkmnpqrstuvwxyz"
        Chi = "23456789"
        Sym = "!@#%*-_"
    }

    # 1. Garantir AU MOINS un caractère de chaque catégorie (conformité AD)
    $chars = foreach ($set in $cat.Values) { $set[(Get-CryptoIndex $set.Length)] }

    # 2. Compléter jusqu'à la longueur voulue depuis l'ensemble complet
    $tous = -join $cat.Values
    while ($chars.Count -lt $Length) { $chars += $tous[(Get-CryptoIndex $tous.Length)] }

    # 3. Mélanger l'ordre (sinon les 4 premiers seraient toujours Maj/Min/Chi/Sym)
    $melange = $chars | Sort-Object { Get-CryptoIndex 100000 }
    -join $melange
}
```

> **Pourquoi ces deux exigences ?** D'abord, `Get-Random` s'appuie sur un générateur pseudo-aléatoire **non cryptographique** : suffisant pour choisir un élément au hasard, mais **inadapté** aux secrets (prévisibilité théorique) — d'où `RandomNumberGenerator`. Ensuite, un simple tirage dans un pool mixte **ne garantit pas** la présence de chaque catégorie : un mot de passe pourrait, par malchance, ne contenir aucun chiffre et être **rejeté** par la politique AD. En imposant un caractère de chaque catégorie avant de compléter, on est toujours conforme.

### L'idempotence

Un script **idempotent** produit le même état final qu'on le lance une ou dix fois. C'est essentiel en automatisation : on vérifie **avant** d'agir (la discipline `Get`/`Test` de tout le cours).

```powershell
# ❌ NON idempotent : échoue au 2e passage (le compte existe déjà)
New-ADUser -Name "X" ...

# ✅ Idempotent : ne crée que si absent
if (-not (Get-ADUser -Filter "SamAccountName -eq 'x'" -ErrorAction SilentlyContinue)) {
    New-ADUser -Name "X" ...
}
```

### `-WhatIf`, `-Confirm` et `ShouldProcess`

Rappel du Ch.24, généralisé. Pour qu'une **fonction maison** supporte `-WhatIf`/`-Confirm`, on ajoute `SupportsShouldProcess` et on encadre les actions modifiantes :

```powershell
function Remove-OldUser {
    [CmdletBinding(SupportsShouldProcess)]
    param([Parameter(Mandatory)][string]$SamAccountName)

    $user = Get-ADUser -Identity $SamAccountName -ErrorAction Stop
    if ($PSCmdlet.ShouldProcess($SamAccountName, "Désactiver et déplacer")) {
        Disable-ADAccount -Identity $user
        Move-ADObject -Identity $user.DistinguishedName -TargetPath "OU=Départs,DC=lab,DC=local"
    }
}

Remove-OldUser -SamAccountName jdupont -WhatIf     # simule
Remove-OldUser -SamAccountName jdupont -Confirm    # demande confirmation
```

Tes propres outils gagnent ainsi le même filet de sécurité que les cmdlets natives — la marque d'un script professionnel.

### Robustesse : retries

Une opération réseau peut échouer temporairement. Un **retry** (nouvelle tentative) évite d'abandonner à la première erreur passagère :

```powershell
function Invoke-WithRetry {
    param([scriptblock]$Action, [int]$MaxRetries = 3, [int]$DelaySeconds = 5)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try { return & $Action }
        catch {
            if ($i -eq $MaxRetries) { throw }
            Write-Warning "Tentative $i échouée, nouvel essai dans $DelaySeconds s..."
            Start-Sleep -Seconds $DelaySeconds
        }
    }
}

Invoke-WithRetry -Action { Invoke-RestMethod -Uri "https://api.exemple.com/data" }
```

## 🔴 Bonus

### Tester ses scripts avec Pester

**Pester** est le framework de test de PowerShell. Pourquoi tester un script d'administration ? Parce qu'un script qui crée des comptes ou supprime des données **doit** se comporter comme prévu — un test attrape une régression avant qu'elle ne casse la production.

```powershell
# MonModule.Tests.ps1
Describe "New-RandomPassword" {
    It "génère un mot de passe de la longueur demandée" {
        (New-RandomPassword -Length 20).Length | Should -Be 20
    }
    It "génère des mots de passe différents à chaque appel" {
        (New-RandomPassword) | Should -Not -Be (New-RandomPassword)
    }
}
```

```powershell
Invoke-Pester .\MonModule.Tests.ps1
```

Pas besoin d'en faire un cours de CI/CD : retiens qu'on **peut** et qu'on **devrait** tester les fonctions critiques. C'est un réflexe de maturité, pas un luxe.

### Vers la CI/CD

À un niveau plus avancé, ces tests s'exécutent automatiquement à chaque modification (GitHub Actions, Azure DevOps…) et la publication des modules se fait sur un dépôt interne. C'est la suite naturelle, hors périmètre de ce cours d'introduction.

## ❌ Erreur classique

```powershell
# Secrets en clair dans le script
$token = "abc123..."     # ❌ fuite garantie si versionné → SecretManagement

# Valeurs codées en dur
$seuil = 20              # ⚠️ à externaliser en config si réutilisé
$config.SeuilDisqueGB    # ✅

# Script non idempotent lancé deux fois
New-ADUser ...           # ❌ échoue au 2e passage
if (-not (Get-ADUser ...)) { New-ADUser ... }   # ✅

# Fonction destructive sans ShouldProcess
function Remove-Stuff { Remove-ADUser ... }      # ❌ pas de -WhatIf possible
[CmdletBinding(SupportsShouldProcess)] + ShouldProcess   # ✅
```

## 💡 Exercices

**Guidé :** Transforme ta fonction `Test-CriticalServices` (Ch.11) en module `.psm1` avec `Export-ModuleMember`, importe-le et utilise-le. Ajoute une fonction `Write-Log`.

**Autonome :** Reprends `Invoke-Offboarding` (Ch.24) et rends-le pleinement professionnel : `SupportsShouldProcess` (`-WhatIf`/`-Confirm`), configuration externe (OU de départ, chemin de log en JSON), journalisation via `Write-Log`, et idempotence (ne rien faire si le compte est déjà désactivé et déplacé).

## 🧩 Capstone Partie VII — Boîte à outils d'administration

Rassemble tes meilleures fonctions dans un module `AdminToolkit.psm1` :

- `Get-ServerHealth` (Ch.8), `Test-CriticalServices` (Ch.11), `Get-DiskAlert` (Ch.14), `Get-NetworkDiagnostic` (Ch.18)
- Avec configuration externe (JSON), journalisation, gestion des secrets (SecretManagement), et `SupportsShouldProcess` sur les fonctions modifiantes
- Documente chaque fonction (aide par commentaires, Ch.8) et ajoute quelques tests Pester

C'est le livrable qui fait passer de « je sais écrire des scripts » à « je livre des outils fiables ».

## ✅ Tu sais maintenant...

- Regrouper des fonctions dans des **modules** (`.psm1`, `Export-ModuleMember`)
- Le **splatting** et la **configuration externe** (JSON) pour des scripts propres
- **Journaliser** (`Write-Log`) et gérer les **secrets** (SecureString, SecretManagement) — jamais en clair
- L'**idempotence** (`Get`/`Test` avant d'agir) et `SupportsShouldProcess` (`-WhatIf`/`-Confirm`)
- Les **retries** pour la robustesse, et l'introduction à **Pester**

## 💬 Questions d'entretien typiques

- **Comment rendre un script rejouable sans effet indésirable ?** → Le rendre idempotent : vérifier l'état avec `Get`/`Test` avant chaque action modifiante.
- **Où stocker un token ou un mot de passe de service ?** → Dans un coffre (SecretManagement) ou un SecureString — jamais en clair dans le code.
- **Comment donner `-WhatIf` à sa propre fonction ?** → `[CmdletBinding(SupportsShouldProcess)]` et encadrer les actions par `$PSCmdlet.ShouldProcess(...)`.
- **Pourquoi tester un script d'administration ?** → Parce qu'il touche à des données réelles (comptes, fichiers) ; un test (Pester) attrape une régression avant la production.

---

# PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ

> **Pourquoi la cybersécurité arrive en dernier.** On ne peut repérer une **anomalie** que si on connaît la **normale**. Grâce aux parties précédentes, tu sais désormais à quoi ressemble un système sain : quels services tournent, quels comptes existent, quelles tâches sont planifiées, quelles connexions sont attendues. Cette partie applique ces compétences au **diagnostic**, à la **détection** et au **durcissement** — dans une optique défensive (blue team), jamais offensive.
>
> On distingue clairement quatre postures : **administration** (gérer), **diagnostic** (comprendre un problème), **défense** (durcir, surveiller) et **investigation** (trier après un incident). PowerShell sert les quatre.

---

# Chapitre 34 — Diagnostic, logs et triage

## 🟢 Le minimum à savoir

### Les journaux d'événements Windows

Les **Event Logs** sont la mémoire de Windows : chaque événement notable (connexion, erreur, démarrage de service, création de compte…) y est enregistré. C'est **la** source d'information pour le diagnostic et la sécurité. La cmdlet moderne est `Get-WinEvent`.

```powershell
# Lister les journaux disponibles et leur volume
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 |
    Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending

# Lire les derniers événements d'un journal
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20     # [🔑 Admin]
```

> **📌 Réflexe `Get-Member` :** `Get-WinEvent -LogName System -MaxEvents 1 | Get-Member` révèle `TimeCreated`, `Id`, `LevelDisplayName`, `Message`, `ProviderName`. Ces propriétés permettent de filtrer et corréler les événements.

### Filtrer efficacement avec `-FilterHashtable`

> **⚠️ Point de performance majeur.** Sur un journal de millions d'événements, filtrer **côté serveur** avec `-FilterHashtable` est incomparablement plus rapide que tout ramener puis filtrer avec `Where-Object` (même logique qu'`-Filter` en AD, Ch.23).

```powershell
# ✅ RAPIDE : le filtre est appliqué à la source
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625              # échecs de connexion
    StartTime = (Get-Date).AddHours(-24)
}

# ❌ LENT : ramène tout, puis filtre
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
```

### Les Event IDs à connaître

| Event ID | Journal | Signification |
|----------|---------|--------------|
| **4624** | Security | Connexion réussie |
| **4625** | Security | **Échec** de connexion (brute-force si répété) |
| **4634 / 4647** | Security | Déconnexion |
| **4720** | Security | **Création** d'un compte utilisateur |
| **4726** | Security | Suppression d'un compte |
| **4732 / 4728** | Security | Ajout à un groupe (local / global) — surveiller les groupes admin |
| **4688** | Security | Création d'un processus (traçabilité des exécutions) |
| **7045** | System | **Installation d'un nouveau service** (persistance possible) |
| **1102** | Security | **Effacement du journal de sécurité** (signal fort) |

> **⚠️ Les Event IDs dépendent de la stratégie d'audit — l'absence d'un événement ne prouve pas l'absence d'activité.** Windows ne génère la plupart de ces événements que si l'**audit correspondant est activé** (par GPO, Ch.25). Exemple concret : l'événement **4688** (création de processus) n'apparaît que si *Audit Process Creation* est activé ; et pour que la **ligne de commande** du processus soit renseignée dans l'événement, il faut **en plus** activer *Include command line in process creation events* — sinon le champ reste vide.
>
> C'est un piège conceptuel majeur en défense : conclure « aucun 4688 → aucun processus suspect créé » est un **faux négatif**. Le bon réflexe est celui du Ch.35 sur le 4104 : avant d'interpréter une absence, **vérifier que la journalisation est configurée**. Un journal muet peut signifier « rien ne s'est passé »… ou « on n'écoutait pas ».

### Détecter une attaque par brute-force

Un cas d'école, qui réunit filtrage, regroupement et seuil :

```powershell
# Compter les échecs de connexion (4625) par compte sur 24h
Get-WinEvent -FilterHashtable @{ LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24) } |
    ForEach-Object {
        # On convertit l'événement en XML pour lire le champ PAR SON NOM (TargetUserName),
        # plutôt que par une position d'index fragile.
        $xml = [xml]$_.ToXml()
        ($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'
    } |
    Group-Object |
    Where-Object Count -gt 10 |
    Select-Object @{N="Compte";E={$_.Name}}, Count |
    Sort-Object Count -Descending
```

> **⚠️ Ne lis pas les champs d'un event par index (`$_.Properties[5]`).** L'ordre et le nombre des propriétés d'un événement **varient** selon la version de Windows et le type d'événement : un index en dur casse silencieusement (tu lis le mauvais champ). La méthode robuste : convertir l'événement en XML (`$_.ToXml()`) et lire le champ **par son nom** (`TargetUserName` pour le compte ciblé, `IpAddress` pour la source…). C'est un peu plus verbeux, mais fiable dans le temps.

Un compte avec des dizaines d'échecs en peu de temps = tentative de brute-force à investiguer. C'est exactement le genre de détection qu'un analyste blue team automatise.

## 🟡 Le triage : appliquer ses connaissances d'admin

Le **triage** consiste à examiner rapidement un système suspect. Tout ce qu'on a appris devient un point de contrôle. La logique : **comparer à la normale**.

### Vérifier l'intégrité d'un fichier : `Get-FileHash`

```powershell
Get-FileHash "C:\Windows\System32\cmd.exe" -Algorithm SHA256
```

Comparer le hash d'un fichier à une référence connue détecte une altération. On vérifie aussi un téléchargement contre le hash publié par l'éditeur.

### Vérifier la signature : `Get-AuthenticodeSignature`

```powershell
Get-AuthenticodeSignature "C:\Windows\System32\cmd.exe" |
    Select-Object Status, SignerCertificate
```

Un binaire système **non signé** ou à signature **invalide** dans un emplacement système est très suspect. `Status = Valid` et un signataire Microsoft sont attendus pour les fichiers système.

### Détecter la persistance : les points de démarrage automatique

Un attaquant cherche à **survivre au redémarrage**. Les mécanismes de persistance sont exactement les objets qu'on sait déjà administrer :

```powershell
# 1. Clés Run/RunOnce du registre (rappel Ch.12)
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# 2. Tâches planifiées non-Microsoft (rappel Ch.13)
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, @{N="Action";E={$_.Actions.Execute}}

# 3. Services dont le binaire est dans un emplacement inhabituel (rappel Ch.11)
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notlike "*\Windows\*" -and $_.PathName -notlike "*Program Files*" } |
    Select-Object Name, PathName, StartName

# 4. Nouveaux services récemment installés (Event ID 7045)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-7) } -ErrorAction SilentlyContinue
```

> **La bascule admin → sécurité :** remarque que ce sont **exactement** les mêmes cmdlets qu'en administration (Ch.11, 12, 13). La différence est l'**intention** : là où l'admin configure, l'analyste **compare à la normale** pour repérer l'anomalie. C'est pour ça qu'on a appris l'administration d'abord.

### Détecter les comptes et connexions suspects

```powershell
# Membres du groupe Administrateurs locaux — ciblé par SID pour être portable FR/EN (rappel Ch.10)
$grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"
Get-LocalGroupMember -Group $grpAdmins.Name

# Connexions établies HORS du réseau 192.168.x.x du lab (rappel Ch.17)
Get-NetTCPConnection -State Established |
    Where-Object { $_.RemoteAddress -notlike "192.168.*" -and $_.RemoteAddress -ne "127.0.0.1" } |
    ForEach-Object {
        [PSCustomObject]@{
            Distant = "$($_.RemoteAddress):$($_.RemotePort)"
            Process = (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name
        }
    }
```

> **⚠️ Heuristique volontairement simplifiée.** Ce filtre ne dit pas « connexion externe » mais « connexion hors du réseau `192.168.x.x` du lab ». D'autres plages **privées** (`10.0.0.0/8`, `172.16.0.0/12`) et l'IPv6 seraient classées à tort comme extérieures. En entreprise, compare aux **plages internes réellement utilisées** chez toi. C'est le principe général du triage : un filtre grossier sert à **réduire le bruit**, pas à produire un verdict — le tri fin reste humain.

### Les Alternate Data Streams (ADS)

NTFS permet de cacher des données dans des **flux alternatifs** attachés à un fichier — une technique de dissimulation classique :

```powershell
# Lister les flux alternatifs d'un fichier
Get-Item "C:\suspect.txt" -Stream * | Select-Object Stream, Length

# Lire un flux caché
Get-Content "C:\suspect.txt" -Stream "cache"
```

Un fichier anodin portant un flux `:` volumineux ou exécutable mérite attention.

## 🔴 Bonus

### Un script de triage synthétique

En pratique, on regroupe ces contrôles dans un script de triage qui produit un rapport horodaté — réutilisant fonctions (Ch.7), objets (Ch.6) et gestion d'erreurs (Ch.8) :

```powershell
function Invoke-QuickTriage {
    [CmdletBinding()]
    param([string]$OutputPath = "C:\triage")

    # Test avant d'agir : le dossier de sortie doit exister
    if (-not (Test-Path $OutputPath)) { New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null }

    # Groupe Administrateurs ciblé par SID → portable FR/EN (rappel Ch.10)
    $grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"

    $rapport = [ordered]@{
        Date            = Get-Date
        AdminsLocaux    = (Get-LocalGroupMember -Group $grpAdmins.Name -ErrorAction SilentlyContinue).Name
        TachesNonMs     = (Get-ScheduledTask | Where-Object TaskPath -notlike "\Microsoft\*").TaskName
        RunKeys         = (Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue)
        # Nom honnête : c'est "hors 192.168.x.x", pas "externe" au sens strict
        ConnexionsHorsLAN = (Get-NetTCPConnection -State Established |
            Where-Object RemoteAddress -notlike "192.168.*").RemoteAddress
    }
    $rapport | ConvertTo-Json -Depth 4 |
        Set-Content "$OutputPath\triage_$(Get-Date -Format yyyyMMdd_HHmmss).json" -Encoding UTF8
}
```

C'est un point de départ de triage, pas un outil forensic complet — mais il montre comment tes compétences d'admin se convertissent directement en capacité défensive.

## ❌ Erreur classique

```powershell
# Filtrer les logs côté client (très lent)
Get-WinEvent -LogName Security | Where-Object Id -eq 4625   # ❌
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625}  # ✅

# Conclure trop vite ("un service hors Windows = malware")
# → un binaire hors chemin standard est un SIGNAL à investiguer, pas une preuve
# → toujours corréler (hash, signature, date, contexte) avant de conclure

# Lire le journal Security sans droits admin
Get-WinEvent -LogName Security    # ❌ sans admin → accès refusé
```

## 💡 Exercices

**Guidé :** Compte les échecs de connexion (Event ID 4625) des dernières 24 h et affiche les comptes ayant plus de 5 échecs.

**Autonome :** Écris `Get-PersistenceReport.ps1` qui collecte les clés Run (HKLM + HKCU), les tâches planifiées non-Microsoft et les services hors chemins standard, puis exporte le tout en JSON horodaté. Réutilise ce que tu sais des Ch.11-13.

## ✅ Tu sais maintenant...

- Lire et **filtrer efficacement** les Event Logs (`Get-WinEvent -FilterHashtable`)
- Les Event IDs clés (4624/4625/4720/7045/1102…)
- Détecter une attaque par brute-force
- Vérifier intégrité (`Get-FileHash`) et signature (`Get-AuthenticodeSignature`)
- Trier la persistance (Run, tâches, services) — les **mêmes cmdlets qu'en admin, avec l'intention de détecter**
- Repérer connexions suspectes et flux alternatifs (ADS)

## 💬 Questions d'entretien typiques

- **Comment détecter une attaque par brute-force en PowerShell ?** → Filtrer les Event ID 4625 sur une période, regrouper par compte, alerter au-dessus d'un seuil.
- **Pourquoi `-FilterHashtable` plutôt que `Where-Object` sur les logs ?** → Le filtrage est appliqué à la source : indispensable sur des journaux volumineux.
- **Où un malware cherche-t-il à persister ?** → Clés Run/RunOnce, tâches planifiées, services, dossiers de démarrage — tout ce qu'on sait déjà administrer.
- **Comment vérifier qu'un binaire système est légitime ?** → Sa signature (`Get-AuthenticodeSignature`, statut Valid + signataire attendu) et son hash (`Get-FileHash`) comparé à une référence.

---

# Chapitre 35 — Sécurité de l'exécution et durcissement

## 🟢 Le minimum à savoir

### Journaliser ce que fait PowerShell lui-même

PowerShell est un outil puissant — donc utilisé aussi par les attaquants. La défense commence par **tracer son propre usage**. Trois mécanismes clés, à activer (idéalement par GPO, Ch.25) :

**Script Block Logging** — enregistre le **contenu des blocs de script traités** par PowerShell dans le journal `Microsoft-Windows-PowerShell/Operational` (Event ID **4104**). Comme il journalise le code tel qu'il est traité par le moteur, il offre souvent une **excellente visibilité sur du code décodé/désobfusqué au moment de l'exécution** — un atout majeur pour la détection. (Ne le présente pas comme une garantie absolue que *tout* script obfusqué sera toujours journalisé entièrement déminé : c'est très utile, sans être infaillible.)

```powershell
# Lire les blocs de script journalisés
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[EventID=4104]]" -MaxEvents 20

# Vérifier si le Script Block Logging est CONFIGURÉ (via registre / GPO)
# EnableScriptBlockLogging = 1 → activé. L'ABSENCE d'événements 4104 ne prouve PAS qu'il est désactivé.
$k = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
if (Test-Path $k) {
    (Get-ItemProperty $k).EnableScriptBlockLogging    # 1 = activé
} else {
    "Non configuré par GPO/registre"
}
```

**Module Logging** — journalise les commandes des modules ciblés.

**Transcription** — enregistre des **transcriptions complètes** des sessions (entrées/sorties) dans des fichiers texte :

```powershell
Start-Transcript -Path "C:\logs\session.txt"    # démarrer manuellement (ou via GPO)
# ... activité ...
Stop-Transcript
```

> **Activation par GPO :** en entreprise, ces trois mécanismes s'activent par stratégie de groupe (Ch.25) sous *Computer Configuration → Administrative Templates → Windows Components → Windows PowerShell*. C'est la boucle bouclée : on utilise les GPO (Partie V) pour durcir PowerShell.

### AMSI : l'inspection à l'exécution

**AMSI** (Antimalware Scan Interface) permet à l'antivirus d'inspecter le code (scripts, commandes) **au moment où il s'exécute**, même s'il a été téléchargé et exécuté en mémoire sans toucher le disque. C'est une défense importante contre les scripts malveillants « fileless ». AMSI est actif par défaut sur les Windows modernes avec Defender ; les attaquants cherchent à le contourner, ce que la journalisation (4104) aide à repérer.

### Le Constrained Language Mode

PowerShell peut fonctionner en **Constrained Language Mode (CLM)**, un mode restreint qui **réduit les capacités de PowerShell** (appels .NET arbitraires, COM, types complexes) tout en autorisant l'administration courante. Mais il faut bien distinguer les rôles :

- **Le mécanisme qui applique la politique**, c'est le **contrôle applicatif** : **App Control for Business** (le nom actuel de la technologie WDAC) ou, plus ancien, **AppLocker**. C'est lui qui décide quel code est approuvé.
- **CLM est la conséquence** : quand le contrôle applicatif est en place, PowerShell bascule **automatiquement** le code **non approuvé** en Constrained Language Mode, ce qui le prive des fonctions dangereuses.

> **Recommandation actuelle :** pour les nouveaux déploiements, Microsoft recommande **App Control for Business (WDAC)** plutôt qu'AppLocker (considéré comme la solution héritée). AppLocker reste répandu dans l'existant.

```powershell
# Voir le mode de langage courant
$ExecutionContext.SessionState.LanguageMode
# FullLanguage (normal) ou ConstrainedLanguage (restreint)
```

> **Rappel Ch.1 :** *ceci* — contrôle applicatif (App Control/WDAC, ou AppLocker) qui déclenche CLM sur le code non approuvé, plus la signature de code — constitue la **vraie** sécurité d'exécution, par opposition à l'Execution Policy qui n'est qu'un garde-fou anti-erreur. On boucle ici la nuance posée au tout début du cours.

## 🟡 Très utile en pratique

### La signature de scripts

Signer ses scripts avec un certificat garantit leur **intégrité** (non modifiés) et leur **origine**. Combinée à une Execution Policy `AllSigned` imposée par GPO, la signature **impose la vérification de signature dans les usages PowerShell normaux et renforce la gouvernance** (on sait d'où viennent les scripts, on détecte les modifications). En revanche — cohérence avec le Ch.1 — l'Execution Policy `AllSigned` **n'est pas** un rempart opposable à un attaquant déterminé (contournable). Pour un **contrôle de sécurité réellement opposable**, on s'appuie sur le **contrôle applicatif (App Control/WDAC ou AppLocker)** vu juste avant. La signature reste néanmoins une excellente pratique d'intégrité et de traçabilité :

```powershell
# Signer un script (avec un certificat de signature de code)
$cert = Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert
Set-AuthenticodeSignature -FilePath ".\MonScript.ps1" -Certificate $cert

# Vérifier la signature (rappel Ch.34)
Get-AuthenticodeSignature ".\MonScript.ps1" | Select-Object Status
```

### Le principe de moindre privilège, appliqué

Toute la discipline du cours converge ici :

- Des **comptes de service** dédiés, avec le minimum de droits (Ch.10, 20)
- Des **scopes** d'API minimaux (Ch.30, 32)
- Des **secrets** dans un coffre, jamais en clair (Ch.33)
- Une appartenance **minimale** aux groupes privilégiés (Ch.21)
- Le remoting **restreint** (pas de `TrustedHosts = *`, Ch.29)

La sécurité n'est pas un chapitre isolé : c'est une **manière de faire** présente dans toutes les parties.

### Détecter les usages suspects de PowerShell

```powershell
# Rechercher des lignes de commande PowerShell suspectes (base64, téléchargement)
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[EventID=4104]]" -MaxEvents 100 -ErrorAction SilentlyContinue |
    Where-Object { $_.Message -match "-enc|FromBase64|DownloadString|IEX|Invoke-Expression" } |
    Select-Object TimeCreated, @{N="Extrait";E={$_.Message.Substring(0, [Math]::Min(120,$_.Message.Length))}}
```

Ces motifs (`-enc`, `FromBase64String`, `DownloadString`, `IEX`) sont des signaux classiques d'exécution malveillante — à corréler, jamais à interpréter isolément.

## 🔴 Bonus

### JEA — Just Enough Administration

**JEA** permet d'accorder à un opérateur **juste les commandes nécessaires** (ex : redémarrer un service précis) via des *endpoints* de remoting contraints, **sans** lui donner de droits d'administrateur complets. C'est le moindre privilège appliqué au remoting — un sujet avancé, mais la direction à connaître pour déléguer sans sur-privilégier.

## ❌ Erreur classique

```powershell
# Se reposer sur l'Execution Policy comme sécurité
# ❌ rappel : ce n'est PAS une barrière → contrôle applicatif (App Control/WDAC) + CLM + signature

# Ne pas activer la journalisation PowerShell
# ❌ sans Script Block Logging (4104), les usages malveillants passent inaperçus
# ✅ activer par GPO : Script Block Logging + Module Logging + Transcription

# Interpréter un seul signal comme une preuve
# → base64 ou IEX peut être légitime ; corréler avant de conclure
```

## 💡 Exercices

**Guidé :** Affiche ton mode de langage courant (`$ExecutionContext.SessionState.LanguageMode`) et lis les 10 derniers événements 4104 du journal PowerShell Operational.

**Autonome :** Écris un script qui recherche dans les événements 4104 les motifs suspects (`-enc`, `DownloadString`, `IEX`) sur les dernières 24 h et produit un rapport horodaté. Rappelle en commentaire que ces motifs sont des signaux à corréler, pas des preuves.

## 🧩 Capstone Partie VIII — Script de posture défensive

Construis `Get-SecurityPosture.ps1` qui audite la posture de sécurité d'un poste :

- Script Block Logging **configuré** ? (lire la **configuration** — GPO/registre — et **non** conclure sur la simple absence d'événements 4104 récents : une absence peut juste signifier qu'aucun script n'a tourné. Optionnellement, provoquer un événement de test bénin puis vérifier son 4104)
- Mode de langage (FullLanguage vs ConstrainedLanguage)
- Pare-feu actif sur tous les profils (Ch.18)
- Admins locaux (Ch.10) et comparaison à une liste attendue
- Persistance suspecte (Ch.34 : Run, tâches, services)
- Rapport structuré (PSCustomObject → JSON/CSV), avec une note rappelant que les signaux doivent être corrélés

C'est la synthèse défensive de tout le cours : tes compétences d'administration, retournées en capacité d'audit de sécurité.

## ✅ Tu sais maintenant...

- Journaliser PowerShell : **Script Block Logging (4104)**, Module Logging, Transcription (via GPO)
- Le rôle d'**AMSI** (inspection à l'exécution, anti-fileless)
- Le contrôle applicatif (**App Control/WDAC** ou AppLocker) qui déclenche le **Constrained Language Mode** = la vraie sécurité d'exécution (vs Execution Policy)
- **Signer** ses scripts et appliquer le **moindre privilège** partout
- Détecter les usages suspects de PowerShell (motifs à corréler)

## 💬 Questions d'entretien typiques

- **Qu'est-ce qui sécurise vraiment l'exécution de scripts (pas l'Execution Policy) ?** → Le contrôle applicatif (App Control/WDAC, recommandé ; ou AppLocker) qui bascule le code non approuvé en Constrained Language Mode, plus la signature de code — imposés par GPO.
- **À quoi sert le Script Block Logging ?** → Journaliser le code PowerShell réellement exécuté (Event 4104), même obfusqué — clé pour détecter les usages malveillants.
- **Qu'est-ce qu'AMSI ?** → Une interface qui laisse l'antivirus inspecter le code à l'exécution, y compris en mémoire (contre les attaques fileless).
- **Comment déléguer une action précise sans donner les pleins droits ?** → JEA (Just Enough Administration), qui expose juste les commandes nécessaires via un endpoint contraint.

---

# ANNEXES

---

## Annexe A — Correspondance PowerShell / Bash / Python

Pour ceux qui viennent de Linux ou de Python. **Rappel fondamental :** Bash et la plupart des pipelines Unix manipulent du **texte** ; PowerShell manipule des **objets**. L'analogie aide à démarrer mais ne doit pas faire oublier cette différence.

| Tâche | PowerShell | Bash | Python |
|-------|-----------|------|--------|
| Lister un dossier | `Get-ChildItem` | `ls` | `os.listdir` / `pathlib` |
| Chemin existe ? | `Test-Path` | `[[ -e ]]` | `Path.exists()` |
| Lire un fichier | `Get-Content` | `cat` | `open().read()` |
| Filtrer | `Where-Object` | `grep` / `awk` | `filter` / compréhension |
| Transformer | `ForEach-Object` | boucle / `sed` | `map` / compréhension |
| Trier | `Sort-Object` | `sort` | `sorted()` |
| Compter | `Measure-Object` / `.Count` | `wc` | `len()` |
| Longueur d'une chaîne | `$s.Length` | `${#s}` | `len(s)` |
| Découper une chaîne | `-split` / `.Split()` | `cut` / IFS | `str.split()` |
| Recoller | `-join` | `paste` | `str.join()` |
| Remplacer | `-replace` / `.Replace()` | `sed` | `str.replace()` / `re.sub` |
| Variable | `$x = 1` | `x=1` | `x = 1` |
| Dictionnaire | `@{ k = v }` | `declare -A` | `{ "k": v }` |
| Condition | `if () {}` | `if [[ ]]; then` | `if:` |
| Boucle | `foreach () {}` | `for … do` | `for … in` |
| Fonction | `function f {}` | `f() {}` | `def f():` |
| Ping | `Test-Connection` | `ping` | `subprocess` |
| Requête HTTP | `Invoke-RestMethod` | `curl` | `requests` |
| Exécution distante | `Invoke-Command` | `ssh` | `paramiko` |
| JSON → objet | `ConvertFrom-Json` | `jq` | `json.loads` |

---

## Annexe B — Cmdlets essentielles par domaine

### Découverte
`Get-Command`, `Get-Help`, `Get-Member`, `Get-Module`, `Get-Verb`

### Système & infos
`Get-CimInstance`, `Get-ComputerInfo`, `Get-Date`, `$env:`, `$PSVersionTable`

### Fichiers
`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`, `New-Item`, `Test-Path`, `Join-Path`, `Get-Acl`, `Set-Acl`, `Select-String`

### Comptes locaux
`Get/New/Set/Disable/Enable-LocalUser`, `Get-LocalGroup`, `Get-LocalGroupMember`, `Add/Remove-LocalGroupMember`

### Processus & services
`Get/Start/Stop-Process`, `Get/Start/Stop/Restart/Set-Service`, `Get-CimInstance Win32_Service`

### Registre
`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`, `New/Set/Remove-ItemProperty`, `Test-Path`

### Tâches planifiées
`Get-ScheduledTask`, `Get-ScheduledTaskInfo`, `New-ScheduledTaskAction/Trigger/Principal`, `Register/Unregister-ScheduledTask`

### Stockage
`Get-Disk`, `Get-Partition`, `Get-Volume`, `Get-PSDrive`, `Get-WindowsFeature` (Server)

### Réseau
`Get-NetIPConfiguration`, `Get-NetAdapter`, `Get-NetIPAddress`, `New-NetIPAddress`, `Get/Set-DnsClientServerAddress`, `Resolve-DnsName`, `Get-NetRoute`, `Get-NetTCPConnection`, `Test-Connection`, `Test-NetConnection`, `Get/New/Set/Remove-NetFirewallRule`

### Active Directory
`Get/New/Set/Remove-ADUser`, `Enable/Disable/Unlock-ADAccount`, `Set-ADAccountPassword`, `Get/New-ADGroup`, `Get/Add/Remove-ADGroupMember`, `Get-ADPrincipalGroupMembership`, `Get/New/Set/Remove-ADComputer`, `Get/New-ADOrganizationalUnit`, `Move-ADObject`, `Search-ADAccount`, `Get-ADDomain`

### GPO & Server
`Get/New/Remove-GPO`, `New/Set-GPLink`, `Get-GPOReport`, `Backup/Restore-GPO`, `Get-GPResultantSetOfPolicy`, `Get-DnsServerZone`, `*-DnsServerResourceRecord*`, `Get-DhcpServerv4Scope/Lease`, `Add-DhcpServerv4Reservation`, `Get/New-SmbShare`, `Get-SmbSession`, `Get-SmbShareAccess`

### Distant & API
`Enter-PSSession`, `Invoke-Command`, `New/Remove-PSSession`, `Enable-PSRemoting`, `Invoke-RestMethod`, `Invoke-WebRequest`, `ConvertTo/From-Json`, `Connect-MgGraph`, `Get-MgUser`, `Get-MgGroup`

### Industrialisation
`Export-ModuleMember`, `Import-Module`, `Get/Set-Secret`, `Start/Stop-Transcript`, `Invoke-Pester`

### Sécurité & triage
`Get-WinEvent`, `Get-FileHash`, `Get-AuthenticodeSignature`, `Set-AuthenticodeSignature`, `Get-Item -Stream`

---

## Annexe C — Event IDs de référence

| Event ID | Journal | Signification |
|----------|---------|--------------|
| 4624 | Security | Connexion réussie |
| 4625 | Security | Échec de connexion (brute-force si répété) |
| 4634 / 4647 | Security | Déconnexion |
| 4648 | Security | Connexion avec identifiants explicites |
| 4672 | Security | Privilèges spéciaux attribués (compte à privilèges) |
| 4688 | Security | Création d'un processus |
| 4720 | Security | Création d'un compte |
| 4722 / 4725 | Security | Compte activé / désactivé |
| 4726 | Security | Suppression d'un compte |
| 4728 / 4732 | Security | Ajout à un groupe (global / local) |
| 4740 | Security | Compte verrouillé |
| 1102 | Security | Journal de sécurité effacé (signal fort) |
| 7045 | System | Nouveau service installé |
| 7040 | System | Type de démarrage d'un service modifié |
| 4104 | PowerShell/Operational | Bloc de script exécuté (Script Block Logging) |

---

## Annexe D — Droits, versions et modules requis

| Opération | Droits | Version / Environnement | Module |
|-----------|--------|------------------------|--------|
| Lire services/processus | Standard | 5.1 / 7 | intégré |
| Modifier services, écrire `HKLM:` | **Admin** | 5.1 / 7 | intégré |
| Lire journal Security | **Admin** | 5.1 / 7 | intégré |
| `Get-WmiObject` | — | **5.1 seulement** (absent en 7) | intégré |
| `Get-CimInstance` | selon classe | 5.1 / 7 | intégré |
| Cmdlets `*-LocalUser` | Admin (modif) | Win 10/11 & Server | LocalAccounts |
| Cmdlets `*-AD*` | délégué/Admin | 5.1 / 7 + **RSAT** ou DC | ActiveDirectory |
| Cmdlets `*-GPO`, `*-GPLink` | Admin | **RSAT** ou DC | GroupPolicy |
| `Install-WindowsFeature` | Admin | **Windows Server uniquement** | ServerManager |
| Cmdlets `*-DnsServer*` | Admin | Serveur DNS ou RSAT | DnsServer |
| Cmdlets `*-DhcpServer*` | Admin | Serveur DHCP ou RSAT | DhcpServer |
| `Enable-PSRemoting` | **Admin** | 5.1 / 7 | intégré |
| `Connect-MgGraph`, `Get-Mg*` | selon scopes | 5.1 / 7 | Microsoft.Graph |
| `Invoke-Pester` | Standard | 5.1 / 7 | Pester |
| `ForEach-Object -Parallel` | Standard | **7 uniquement** | intégré |
| Opérateur ternaire `? :` | Standard | **7 uniquement** | intégré |

> **Note sur la compatibilité des modules Windows en PowerShell 7.** Les modules d'administration Windows n'ont pas tous le même statut en PS7. Certains sont **nativement compatibles** ; d'autres (historiquement liés à Windows PowerShell) sont chargés via la **couche de compatibilité Windows PowerShell** : PS7 les exécute en réalité dans une session Windows PowerShell 5.1 en arrière-plan et **sérialise** les objets échangés — ce qui fonctionne dans la grande majorité des cas, mais peut entraîner des **limitations** (objets « désérialisés » sans leurs méthodes, quelques différences de comportement). En pratique, pour ce cours : `ActiveDirectory`, `DnsServer`, `DhcpServer`, `GroupPolicy`, `ServerManager` fonctionnent en 7, parfois via cette couche de compatibilité. En cas de comportement inattendu sur un objet renvoyé par un de ces modules, vérifie s'il n'est pas désérialisé (un `Get-Member` montrera des types préfixés `Deserialized.`) et, au besoin, exécute la commande depuis une console Windows PowerShell 5.1. La liste exacte évolue : consulte la matrice de compatibilité Microsoft si un module précis pose problème.

---

## Annexe E — Pièges classiques et corrections

| Piège | ❌ Incorrect | ✅ Correct |
|-------|-------------|-----------|
| Comparaison | `if ($a == $b)` | `if ($a -eq $b)` |
| Interpolation de propriété | `"$obj.Prop"` | `"$($obj.Prop)"` |
| Concaténer deux caractères | `$s[0] + $s[1]` (→ addition **numérique** : 195) | `-join @($s[0], $s[1])` ou `"$($s[0])$($s[1])"` |
| Plage calculée pouvant valoir 0 | `1..($n - 4)` (si `$n=4` → `1..0` = **@(1,0)**, 2 éléments !) | tester `if ($n -gt 4) { 1..($n - 4) }` |
| Format avant traitement | `... \| Format-Table \| Export-Csv` | `... \| Export-Csv` (Format en dernier) |
| Filtrer côté client | `Get-ADUser -Filter * \| Where …` | `Get-ADUser -Filter "…"` |
| Encodage fichier | `Set-Content x` | `Set-Content x -Encoding UTF8` |
| `Get-WmiObject` en PS7 | `Get-WmiObject …` | `Get-CimInstance …` |
| Inventaire logiciels | `Win32_Product` | clés `Uninstall` du registre |
| Variable distante | `{ Get-Service $nom }` | `{ Get-Service $using:nom }` |
| try/catch sans Stop | `try { Get-… }` | `try { Get-… -ErrorAction Stop }` |
| `$?` après un .exe | `ping…; if (-not $?)` | `ping…; if ($LASTEXITCODE -ne 0)` |
| Créer sans vérifier | `New-ADUser …` | `if (-not (Get-ADUser …)) { New-ADUser … }` |
| Masse sans simuler | `New-ADUser …` (en boucle) | `… -WhatIf` d'abord |
| Secret en clair | `$token = "abc"` | SecretManagement / SecureString |
| Execution Policy = sécurité | s'y fier | contrôle applicatif (App Control/WDAC) → CLM + signature |
| WinRM « toujours chiffré » | affirmation brute | nuancer (Kerberos domaine / NTLM-HTTPS hors domaine) |
| `LastLogonDate` exact | s'y fier à la minute | approximatif (réplication différée) |
| Permissions fichiers | ne voir que SMB ou que NTFS | l'intersection des deux gagne |

---

## Annexe F — Les deux réflexes transversaux

Tout le cours repose sur deux habitudes. Si tu ne retiens que ça :

### Réflexe 1 — Explorer avec `Get-Member`

Face à **tout** objet inconnu (service, utilisateur AD, tâche, réponse d'API, événement…) :

```powershell
<commande> | Get-Member
```

Tu découvres ses propriétés (informations) et méthodes (actions). Tu n'as pas à mémoriser PowerShell — tu l'explores. On l'a appliqué à chaque nouveau type d'objet du cours.

### Réflexe 2 — `Get`/`Test` avant `Set`/`New`/`Remove`

On regarde **toujours** avant de modifier :

```powershell
Get-…    /  Test-…        # 1. observer l'état actuel
# … décision …
Set-… / New-… / Remove-…  # 2. agir en connaissance de cause
-WhatIf                    # 3. et pour les opérations sensibles/en masse, simuler d'abord
```

Cette discipline — vérifier, simuler, sauvegarder avant d'agir — traverse toute l'administration, de la création d'un dossier (Ch.9) à l'onboarding de masse (Ch.24) en passant par les GPO (Ch.25) et le registre (Ch.12).

---

## Annexe G — Parcours de certification et ressources

### Certifications utiles (à jour 2025-2026)

| Certification | Éditeur | Portée |
|--------------|---------|--------|
| **AZ-104** (Azure Administrator) | Microsoft | Administration cloud, inclut PowerShell/Graph |
| **MD-102** (Endpoint Administrator) | Microsoft | Postes de travail, Intune |
| **AZ-802** (Windows Server Administrator Associate) | Microsoft | Windows Server, AD, hybride — successeur 2026, remplace AZ-800/AZ-801 (retirés le 30/09/2026) |
| **SC-300** (Identity and Access) | Microsoft | Entra ID, identité |
| **Sec+** (Security+) | CompTIA | Fondamentaux sécurité (utile Partie VIII) |

> Les certifications Microsoft évoluent régulièrement (noms, codes, contenus). Vérifie les intitulés actuels sur le site officiel Microsoft Learn avant de t'engager.

### Ressources d'apprentissage

- **Microsoft Learn** — documentation officielle et parcours gratuits
- **`Get-Help` et `Get-Command`** — ta première documentation, toujours à portée
- **PowerShell Gallery** ([powershellgallery.com](https://www.powershellgallery.com/)) — modules communautaires
- **Le dépôt GitHub PowerShell** — source, discussions, nouveautés
- **Communautés** : r/PowerShell, PowerShell.org, les forums Microsoft Q&A

### Pour approfondir séparément

Ce cours t'a donné les fondations PowerShell pour piloter Windows. Pour aller plus loin sur chaque technologie **en tant que telle**, oriente-toi vers des cours dédiés :

- **Active Directory** (conception, réplication, FSMO, approbations, sécurité AD)
- **Windows Server** (rôles avancés, clustering, stockage)
- **Réseau Windows** (routage, VLAN, VPN)
- **Entra ID / Microsoft 365 / Intune** (identité et gestion cloud)
- **Cybersécurité Windows / Digital Forensics** (investigation approfondie)
- **PowerShell avancé** (classes, DSC, modules binaires, CI/CD)

---

## Conclusion

Tu es parti de zéro et tu sais maintenant :

- **Comprendre PowerShell** : cmdlets `Verbe-Nom`, pipeline **objet**, variables, conditions, boucles, fonctions, gestion d'erreurs
- **Administrer un poste Windows** : fichiers et permissions NTFS, comptes locaux, processus, services, registre, tâches, disques, logiciels
- **Gérer le réseau** : IP, DNS, routage, connexions, pare-feu
- **Automatiser Active Directory** : utilisateurs, groupes, ordinateurs, OU, recherche filtrée, onboarding de masse
- **Piloter GPO et services serveur** : stratégies de groupe, DNS, DHCP, partages SMB
- **Administrer à distance et via API** : Remoting nuancé, authentification/tokens, REST, Microsoft Graph
- **Industrialiser** : modules, secrets, idempotence, `-WhatIf`, tests
- **Défendre** : diagnostic, triage, journalisation, durcissement

Et surtout, tu as acquis les **deux réflexes** qui te rendront autonome bien au-delà de ce cours : **explorer avec `Get-Member`** tout objet inconnu, et **observer avant d'agir** (`Get`/`Test` → `Set`/`New`/`Remove`, puis `-WhatIf`).

Le niveau atteint est celui d'un **administrateur Windows PowerShell junior solide** : capable d'administrer, d'automatiser, de diagnostiquer, et de s'appuyer sur ces bases pour se spécialiser. PowerShell n'est pas une fin en soi — c'est le **fil conducteur** qui relie toute l'administration Windows. Tu tiens maintenant ce fil. À toi de tirer.

**Bon scripting, et bonne administration !**
