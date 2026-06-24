# Containers, Docker et Kubernetes

## De zéro à la maîtrise — Comprendre, déployer et sécuriser

-----

> **Prérequis :** Aucune expérience avec les containers n’est nécessaire. Le cours part de zéro.
> Une familiarité basique avec le terminal Linux (naviguer dans les dossiers, éditer un fichier, lancer des commandes) est un plus, mais les commandes essentielles sont rappelées au fil du cours.

-----

## Guide de lecture — Comment utiliser ce cours

Ce cours couvre un domaine vaste. Tu n’as **pas besoin de tout maîtriser d’un coup**. Voici comment naviguer selon ton objectif.

**Chaque chapitre est organisé en 3 niveaux :**

|Section                   |Niveau               |Objectif                                                                                 |
|--------------------------|---------------------|-----------------------------------------------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel          |Ce qu’il faut comprendre pour ne pas être perdu. Si tu ne retiens qu’une chose, c’est ça.|
|**Très utile en pratique**|🟡 Bon à connaître    |Ce qui te rend opérationnel. Indispensable si tu vas travailler avec le sujet.           |
|**Bonus**                 |🔴 Avancé / Production|Ce qui fait la différence en poste. Tu peux y revenir plus tard.                         |

**Si tu prépares un entretien ou vises un poste junior :**
Concentre-toi sur les sections “Le minimum à savoir” de chaque chapitre. Avec ça, tu pourras expliquer clairement ce qu’est un container, pourquoi on utilise Docker et Kubernetes, comment ça fonctionne, et quels sont les risques de sécurité. C’est ce qu’on attend d’un profil junior.

**Si tu veux devenir opérationnel (poste DevOps, SRE, SecOps) :**
Lis tout, y compris les sections “Très utile en pratique”. Les “Bonus” viendront naturellement avec l’expérience.

**Les chapitres indispensables pour un entretien :**
Ch.1-5 (comprendre Docker), Ch.6-8 (construire et composer), Ch.11-14 (comprendre Kubernetes), Ch.21 (sécurité — risques), Ch.23 et Ch.25 (sécurité runtime et K8s). Avec ces chapitres, tu as 80% de ce qu’on attend d’un junior.

### Parcours recommandés

|Parcours                 |Chapitres                |Objectif                                         |
|-------------------------|-------------------------|-------------------------------------------------|
|**🎯 Entretien / Junior** |Ch.1-8, 11-15, 21, 23, 25|Comprendre, expliquer, être crédible en entretien|
|**🔧 Opérationnel**       |Tout jusqu’au Ch.26      |Être autonome sur un poste qui utilise Docker/K8s|
|**🚀 Avancé / Production**|Ch.27-30 + annexes       |Architectures avancées, scaling, gouvernance     |

Tu n’as pas besoin de tout lire linéairement. Commence par le parcours qui correspond à ton objectif actuel, et reviens aux chapitres suivants quand tu en as besoin.

-----

## Glossaire — Les mots à connaître

Reviens ici chaque fois qu’un terme te semble flou. Tous ces termes seront expliqués en détail dans le cours.

|Terme                |Définition simple                                                                               |
|---------------------|------------------------------------------------------------------------------------------------|
|**Container**        |Un environnement isolé et léger qui fait tourner une application avec toutes ses dépendances    |
|**Image**            |Le modèle (template) à partir duquel on crée un container — comme un plan de construction       |
|**Docker**           |L’outil le plus populaire pour créer et gérer des containers                                    |
|**Dockerfile**       |Le fichier texte qui décrit comment construire une image Docker, étape par étape                |
|**Registry**         |Un entrepôt d’images Docker (comme Docker Hub — le “GitHub des images”)                         |
|**Volume**           |Un espace de stockage persistant qui survit à la destruction du container                       |
|**Docker Compose**   |Un outil pour lancer plusieurs containers ensemble (ex : application + base de données)         |
|**Kubernetes (K8s)** |Un système qui gère automatiquement des containers sur plusieurs serveurs                       |
|**Pod**              |La plus petite unité dans Kubernetes — contient un ou plusieurs containers                      |
|**Deployment**       |Un objet K8s qui gère le déploiement et le scaling d’une application                            |
|**Service**          |Un objet K8s qui donne une adresse réseau stable à un groupe de Pods                            |
|**Namespace**        |Un espace de noms qui sépare logiquement les ressources dans un cluster K8s                     |
|**YAML**             |Le format de fichier utilisé pour décrire les configurations Docker Compose et Kubernetes       |
|**Cluster**          |L’ensemble des serveurs (nœuds) gérés par Kubernetes                                            |
|**Orchestration**    |La gestion automatique de containers sur plusieurs serveurs (scaling, self-healing, déploiement)|
|**Kernel**           |Le cœur du système d’exploitation — les containers partagent le kernel de la machine hôte       |
|**Namespace (Linux)**|Un mécanisme du kernel Linux qui isole les processus, le réseau, les fichiers d’un container    |
|**RBAC**             |Role-Based Access Control — le système de permissions dans Kubernetes                           |
|**Network Policy**   |Une règle de pare-feu entre les Pods dans Kubernetes                                            |

-----

## Le schéma mental

Avant de plonger, voici le fil conducteur. **Tout ce cours suit une progression logique :**

```
  POURQUOI ?         COMMENT ?           EN SÉCURITÉ ?
  Pourquoi les   →   Comment les      →  Comment les
  containers ?       utiliser ?           sécuriser ?
```

**Partie I-II** : Comprendre et utiliser Docker (construire, lancer, composer)
**Partie III** : Comprendre et utiliser Kubernetes (orchestrer, déployer)
**Partie IV** : Opérer au quotidien (CI/CD, monitoring, troubleshooting)
**Partie V** : Sécuriser (images, runtime, réseau, Kubernetes)
**Partie VI-VII** : Aller plus loin (architectures, synthèse)

-----

## Table des matières

**PARTIE I — FONDATIONS (Ch.1-5)**

1. [Pourquoi les containers : du serveur physique au container](#chapitre-1--pourquoi-les-containers)
1. [L’architecture container : comment ça marche sous le capot](#chapitre-2--larchitecture-container)
1. [Installer Docker et premiers containers](#chapitre-3--installer-docker-et-premiers-containers)
1. [Images Docker : comprendre, chercher, utiliser](#chapitre-4--images-docker)
1. [Réseau, volumes et persistance](#chapitre-5--réseau-volumes-et-persistance)

**PARTIE II — CONSTRUIRE ET COMPOSER (Ch.6-10)**
6. [Écrire un Dockerfile : de zéro à l’image](#chapitre-6--écrire-un-dockerfile)
7. [Optimiser et durcir ses images](#chapitre-7--optimiser-et-durcir-ses-images)
8. [Docker Compose : orchestrer plusieurs containers](#chapitre-8--docker-compose)
9. [Registries et gestion des images](#chapitre-9--registries-et-gestion-des-images)
10. [Capstone : containeriser une application complète](#chapitre-10--capstone-partie-ii)

**PARTIE III — KUBERNETES : LES FONDAMENTAUX (Ch.11-16)**
11. [Pourquoi Kubernetes : quand Docker ne suffit plus](#chapitre-11--pourquoi-kubernetes)
12. [Architecture Kubernetes : les composants du cluster](#chapitre-12--architecture-kubernetes)
13. [Les objets Kubernetes essentiels](#chapitre-13--les-objets-kubernetes-essentiels)
14. [Déployer sur Kubernetes : kubectl et les manifests](#chapitre-14--déployer-sur-kubernetes)
15. [Stockage, Ingress et configuration avancée](#chapitre-15--stockage-ingress-et-configuration)
16. [Capstone : déployer une application sur Kubernetes](#chapitre-16--capstone-partie-iii)

**PARTIE IV — OPÉRATIONS ET CYCLE DE VIE (Ch.17-20)**
17. [CI/CD et containers : du code au déploiement](#chapitre-17--cicd-et-containers)
18. [Monitoring, logs et observabilité](#chapitre-18--monitoring-logs-et-observabilité)
19. [Troubleshooting containers et Kubernetes](#chapitre-19--troubleshooting)
20. [Capstone : pipeline CI/CD et monitoring](#chapitre-20--capstone-partie-iv)

**PARTIE V — SÉCURITÉ DES CONTAINERS (Ch.21-26)**
21. [Surface d’attaque des containers : comprendre les risques](#chapitre-21--surface-dattaque)
22. [Sécuriser les images : de la construction au déploiement](#chapitre-22--sécuriser-les-images)
23. [Sécuriser le runtime : isolation et contrôle d’exécution](#chapitre-23--sécuriser-le-runtime)
24. [Sécuriser le réseau : segmentation et chiffrement](#chapitre-24--sécuriser-le-réseau)
25. [Sécuriser Kubernetes : RBAC, Secrets et API Server](#chapitre-25--sécuriser-kubernetes)
26. [Détection et réponse aux incidents dans les containers](#chapitre-26--détection-et-réponse)

**PARTIE VI — ARCHITECTURES ET PATTERNS AVANCÉS (Ch.27-28)**
27. [Microservices, patterns et anti-patterns](#chapitre-27--microservices)
28. [Multi-tenancy, scaling et production](#chapitre-28--production)

**PARTIE VII — SYNTHÈSE (Ch.29-30)**
29. [Cas de synthèse : audit de sécurité d’un environnement containerisé](#chapitre-29--cas-de-synthèse)
30. [Le métier et les perspectives](#chapitre-30--le-métier)

**ANNEXES**

-----

## Fil rouge : Opération CONTAINER

> **Contexte narratif**
> 
> **Sami Khelil**, 29 ans, ingénieur sécurité infrastructure dans une ESN (800 personnes), est intégré à l’équipe projet de **MedFlow**, une startup healthtech (60 personnes) qui migre son application monolithique vers une architecture containerisée.
> 
> L’application MedFlow est une plateforme de gestion de dossiers patients. La stack technique : Python/Django (backend), PostgreSQL (base de données), Redis (cache), Celery (tâches asynchrones). L’application tourne actuellement sur 3 machines virtuelles classiques, configurées manuellement.
> 
> La cible : Docker en développement, Kubernetes managé (type EKS/AKS/GKE) en production.
> 
> Sami intervient en **double casquette** : accompagner la containerisation (ops) ET garantir la sécurité de l’architecture résultante. Il découvre en cours de projet que l’image Docker de base contient 147 CVE, que les secrets de l’application sont en clair dans les fichiers de configuration Kubernetes, et qu’un développeur a monté le Docker socket dans un container de CI — une faille qui donne le contrôle total de la machine hôte.
> 
> **Progression :** pourquoi containeriser → premiers containers Docker → construction d’images → Docker Compose → introduction Kubernetes → déploiement K8s → sécurisation progressive → incident et remédiation.

-----

# PARTIE I — FONDATIONS

-----

# Chapitre 1 — Pourquoi les containers : du serveur physique au container

## Le minimum à savoir

### Le problème de départ

Imagine que tu développes une application web. Elle a besoin de Python 3.12, de PostgreSQL 15, de Redis, et de quelques bibliothèques spécifiques. Ça fonctionne sur ton ordinateur. Mais quand tu la déploies sur le serveur de production, rien ne marche : le serveur a Python 3.9, une version différente de PostgreSQL, et il manque des bibliothèques.

C’est le problème classique du **“ça marche sur ma machine”**. Les containers le résolvent.

### L’évolution en 3 étapes

Pour comprendre les containers, il faut comprendre ce qui existait avant et pourquoi chaque étape a été inventée.

**Étape 1 — Le serveur physique (bare metal)**

Au début, chaque application tournait sur un serveur physique dédié. Un serveur = une application. Le problème : si l’application n’utilise que 10% du CPU, les 90% restants sont gaspillés. Et si tu as 20 applications, tu as besoin de 20 serveurs physiques — coûteux, lents à déployer, difficiles à maintenir.

**Étape 2 — La virtualisation (machines virtuelles)**

La virtualisation permet de faire tourner **plusieurs systèmes d’exploitation** sur un seul serveur physique. Chaque machine virtuelle (VM) a son propre OS complet, son propre kernel, ses propres ressources. Un hyperviseur (VMware, Hyper-V, KVM) gère le partage du matériel.

C’est un progrès énorme : un serveur physique peut héberger 10-20 VMs. Mais chaque VM embarque un OS complet (plusieurs Go), consomme de la RAM juste pour son kernel, et met 30 secondes à 2 minutes pour démarrer.

**Étape 3 — Les containers**

Les containers sont une forme d’isolation **sans OS complet**. Au lieu d’embarquer un kernel entier, le container **partage le kernel de la machine hôte** et n’embarque que l’application et ses dépendances.

Résultat :

- Une image container fait typiquement **50-200 Mo** au lieu de **5-20 Go** pour une VM
- Un container démarre en **quelques secondes** au lieu de minutes
- Tu peux faire tourner **des dizaines de containers** là où tu mettrais 5-10 VMs
- L’application se comporte **exactement de la même façon** partout (sur ton laptop, sur le serveur de test, en production)

### Container vs VM : la comparaison visuelle

```
  MACHINE VIRTUELLE                    CONTAINER
┌───────────────────────┐       ┌───────────────────────┐
│  App A  │  App B      │       │  App A  │  App B      │
│─────────│─────────────│       │─────────│─────────────│
│  Libs A │  Libs B     │       │  Libs A │  Libs B     │
│─────────│─────────────│       │─────────│─────────────│
│  OS     │  OS         │       │    Container Engine   │
│ complet │ complet     │       │     (Docker)          │
│─────────│─────────────│       │───────────────────────│
│      Hyperviseur      │       │    OS hôte (1 seul)   │
│───────────────────────│       │───────────────────────│
│     Matériel (CPU,    │       │     Matériel (CPU,    │
│     RAM, disque)      │       │     RAM, disque)      │
└───────────────────────┘       └───────────────────────┘
```

La différence fondamentale : **la VM virtualise le matériel** (chaque VM croit avoir son propre ordinateur), **le container virtualise l’OS** (chaque container croit avoir son propre système, mais ils partagent le même kernel).

> **À retenir pour un entretien :** “Un container partage le kernel de la machine hôte et n’embarque que l’application et ses dépendances. C’est plus léger et plus rapide qu’une VM, mais l’isolation est moins forte car le kernel est partagé.”

### Les 4 avantages concrets des containers

1. **Portabilité** : le container fonctionne partout de la même façon — sur ton laptop, sur le serveur de test, en production, chez un collègue. Plus jamais “ça marche sur ma machine”.
1. **Reproductibilité** : l’image container décrit exactement ce qui est installé. Pas de configuration manuelle, pas de “j’ai oublié d’installer cette bibliothèque”. Si l’image est la même, le résultat est le même.
1. **Isolation** : chaque container a son propre filesystem, ses propres processus, son propre réseau. L’application A dans son container ne peut pas interférer avec l’application B dans un autre container.
1. **Densité** : un serveur qui fait tourner 5 VMs peut faire tourner 50 containers. Les containers consomment beaucoup moins de ressources.

### Ce que les containers ne sont PAS

C’est important de le dire dès le départ :

- **Les containers ne sont PAS des VMs.** L’isolation est moins forte (kernel partagé). Une vulnérabilité dans le kernel affecte tous les containers de la machine.
- **Les containers ne sont PAS magiquement sécurisés.** Un container mal configuré (exécuté en root, avec trop de permissions, avec des secrets dans l’image) est une vulnérabilité.
- **Les containers ne remplacent PAS la virtualisation dans tous les cas.** Pour une isolation forte (multi-tenant, environnements hostiles), une VM reste plus sûre.
- **Les containers ne simplifient PAS tout.** Ils ajoutent une couche de complexité (réseau, stockage, orchestration). Le bénéfice vient quand cette complexité est maîtrisée.

> **📋 CONTAINER — Épisode 1**
> 
> Sami rejoint l’équipe MedFlow. L’application tourne sur 3 VMs : une pour Django (le serveur web), une pour PostgreSQL (la base de données), une pour Redis + Celery (le cache et les tâches en arrière-plan). Chaque VM est configurée manuellement par un administrateur système. Le dernier déploiement a cassé la production : la version de Python sur la VM de staging (3.11) n’était pas la même qu’en production (3.9). Le CTO demande à Sami d’accompagner la migration vers des containers. Objectif : “que l’application se comporte exactement pareil partout.”

## Très utile en pratique

### Les cas d’usage concrets

**Développement local reproductible :** au lieu d’installer PostgreSQL, Redis, Elasticsearch sur ton laptop (et de gérer les versions, les conflits, le nettoyage), tu lances des containers. Un `docker compose up` et tout ton environnement de développement est prêt. Un `docker compose down` et tout disparaît proprement.

**CI/CD (intégration et déploiement continus) :** les pipelines de test et de déploiement utilisent des containers pour garantir un environnement identique à chaque exécution. Les tests passent dans un container → on construit l’image de production → on la déploie.

**Microservices :** au lieu d’une grosse application monolithique, on découpe en services indépendants, chacun dans son container. Chaque service peut être développé, déployé et mis à l’échelle indépendamment.

**Labs de sécurité et pentest :** les containers sont parfaits pour lancer rapidement des environnements d’entraînement (DVWA, Juice Shop, Metasploitable) sans polluer ta machine.

### Container vs VM : le tableau comparatif

|Critère    |Machine Virtuelle                       |Container                 |
|-----------|----------------------------------------|--------------------------|
|Isolation  |Forte (kernel séparé)                   |Moyenne (kernel partagé)  |
|Taille     |5-20 Go                                 |50-500 Mo                 |
|Démarrage  |30s - 2 min                             |1-5 secondes              |
|Densité    |5-20 par serveur                        |50-200 par serveur        |
|OS embarqué|OS complet                              |Juste les libs nécessaires|
|Portabilité|Moyenne (format VMware, Hyper-V…)       |Excellente (standard OCI) |
|Performance|Légère perte (virtualisation matérielle)|Quasi native              |
|Sécurité   |Plus forte par défaut                   |Nécessite du hardening    |

## Bonus

### Un peu d’histoire

Les containers ne sont pas une invention récente. Les premières formes d’isolation de processus datent de `chroot` (1979) sous Unix. Puis sont venus les FreeBSD Jails (2000), Solaris Zones (2004), et LXC (Linux Containers, 2008). **Docker** (2013) a démocratisé le concept en le rendant simple d’utilisation avec un format d’image standardisé et un écosystème d’outils. Docker n’a pas inventé les containers — il les a rendus accessibles.

Aujourd’hui, le standard est **OCI** (Open Container Initiative) — un format ouvert pour les images et les runtimes de containers, indépendant de Docker. Kubernetes utilise `containerd` (un runtime OCI) plutôt que Docker directement.

### Le standard OCI en bref

L’OCI définit deux choses : un format d’image (comment une image est construite et distribuée) et un runtime (comment un container est exécuté). Docker, Podman, containerd — tous respectent le standard OCI. Une image construite avec Docker fonctionne avec Podman et vice versa.

## ❌ Erreur classique

```
# Croire que container = VM légère
→ Non. Le modèle d'isolation est fondamentalement différent (kernel partagé vs séparé).

# Croire que les containers sont sécurisés par défaut
→ Non. Un container en root avec le Docker socket monté est MOINS sécurisé qu'une VM.

# Vouloir mettre "tout en containers" sans réflexion
→ Une base de données de production avec de fortes contraintes de performance et de
  persistance n'est pas toujours le meilleur candidat pour la containerisation.
```

## ✅ Tu sais maintenant…

- La différence entre serveur physique, VM et container
- Pourquoi les containers existent (portabilité, reproductibilité, isolation, densité)
- Que les containers partagent le kernel de la machine hôte (conséquence en sécurité)
- Ce que les containers ne sont PAS (pas des VMs, pas magiquement sécurisés)

## 💬 Questions d’entretien typiques

- **Quelle est la différence entre un container et une machine virtuelle ?** → Le container partage le kernel de l’hôte et isole au niveau de l’OS (namespaces), la VM virtualise le matériel avec un kernel séparé. Le container est plus léger et rapide, la VM offre une isolation plus forte.
- **Quels sont les avantages des containers ?** → Portabilité, reproductibilité, isolation des dépendances, densité (plus de containers que de VMs par serveur), démarrage rapide.
- **Les containers sont-ils sécurisés ?** → Pas par défaut. L’isolation repose sur des mécanismes logiciels (namespaces, cgroups), pas sur une séparation matérielle. Un container mal configuré (root, Docker socket monté) peut être moins sécurisé qu’une VM.

-----

# Chapitre 2 — L’architecture container : comment ça marche sous le capot

## Le minimum à savoir

### Pourquoi comprendre “le dessous”

Tu n’as pas besoin de maîtriser les mécanismes internes du kernel Linux pour utiliser Docker. Mais comprendre les grandes lignes te permet de :

- répondre aux questions techniques en entretien (“comment fonctionne l’isolation d’un container ?”)
- comprendre pourquoi certaines configurations sont dangereuses
- diagnostiquer les problèmes quand ça ne fonctionne pas

### L’isolation par les namespaces

Les **namespaces** sont le mécanisme du kernel Linux qui donne à chaque container l’illusion d’avoir son propre système. Chaque namespace isole un aspect :

|Namespace|Ce qu’il isole                  |Effet concret                                                                            |
|---------|--------------------------------|-----------------------------------------------------------------------------------------|
|**PID**  |Les processus                   |Le container ne voit que ses propres processus (pas ceux de l’hôte)                      |
|**NET**  |Le réseau                       |Le container a sa propre interface réseau, sa propre IP                                  |
|**MNT**  |Le filesystem                   |Le container a son propre système de fichiers                                            |
|**UTS**  |Le hostname                     |Le container a son propre nom de machine                                                 |
|**IPC**  |La communication inter-processus|Les processus du container ne peuvent pas communiquer avec ceux d’un autre               |
|**USER** |Les utilisateurs                |L’utilisateur “root” dans le container peut être un utilisateur non privilégié sur l’hôte|

Concrètement, quand tu lances un container et que tu fais `ps aux` dedans, tu ne vois que les processus du container. L’hôte, lui, voit tous les processus de tous les containers. C’est une illusion, pas une séparation matérielle — et c’est la raison pour laquelle l’isolation est plus faible qu’une VM.

> **À retenir pour un entretien :** “L’isolation des containers repose sur les namespaces Linux, qui donnent à chaque container l’illusion d’avoir son propre système. Mais contrairement à une VM, il n’y a pas de séparation matérielle — c’est une isolation logicielle au niveau du kernel.”

### Le contrôle des ressources par les cgroups

Les **cgroups** (control groups) limitent les ressources qu’un container peut consommer :

- **CPU** : “ce container ne peut pas utiliser plus de 50% du CPU”
- **Mémoire** : “ce container ne peut pas utiliser plus de 512 Mo de RAM”
- **I/O disque** : “ce container ne peut pas saturer le disque”

Sans cgroups, un container pourrait monopoliser toutes les ressources de la machine et faire tomber les autres containers. Les cgroups sont le mécanisme de “fair play” entre containers.

> **Conséquence pratique :** quand un container dépasse sa limite mémoire, le kernel le tue brutalement (OOMKilled — Out Of Memory Killed). C’est un comportement normal, pas un bug — c’est la protection qui fonctionne. On verra comment diagnostiquer ça au chapitre 19.

### Le filesystem par couches (layers)

Les images Docker sont construites en **couches** superposées (layers). Chaque instruction dans le Dockerfile (on verra ça au chapitre 6) crée une couche :

```
┌─────────────────────────────────┐
│ Couche 4 : COPY app.py          │  ← Ton code (petite couche)
│─────────────────────────────────│
│ Couche 3 : RUN pip install      │  ← Tes dépendances
│─────────────────────────────────│
│ Couche 2 : RUN apt-get update   │  ← Les mises à jour système
│─────────────────────────────────│
│ Couche 1 : FROM python:3.12     │  ← L'image de base (la plus grosse)
└─────────────────────────────────┘
```

Chaque couche est **en lecture seule**. Quand le container tourne, une couche supplémentaire **en écriture** est ajoutée au-dessus. Quand le container est détruit, cette couche d’écriture disparaît — c’est pourquoi les données non persistées sont perdues.

**L’avantage :** si deux images utilisent la même couche de base (`python:3.12`), cette couche n’est stockée qu’une seule fois sur le disque. C’est un gain de place considérable.

> **À retenir :** les couches sont en lecture seule et partagées entre images. Le container ajoute une couche d’écriture temporaire qui disparaît quand le container est supprimé. C’est pour ça qu’on utilise des **volumes** pour les données qu’on veut garder (chapitre 5).

### Le kernel partagé : la conséquence en sécurité

C’est **le** point à comprendre en profondeur :

```
Container A    Container B    Container C
    │              │              │
    └──────────────┼──────────────┘
                   │
           Kernel Linux (partagé)
                   │
             Matériel (CPU, RAM)
```

Tous les containers utilisent le **même kernel** que la machine hôte. Conséquences :

1. **Performance :** c’est pour ça que les containers sont rapides — pas de virtualisation du matériel.
1. **Compatibilité :** tu ne peux pas faire tourner un container Windows sur un hôte Linux (sauf via une VM intermédiaire, comme Docker Desktop sur Mac/Windows).
1. **Sécurité :** une vulnérabilité dans le kernel affecte **tous les containers** de la machine. C’est la raison principale pour laquelle l’isolation est plus faible qu’une VM.

### Les composants de l’écosystème Docker

Quand tu utilises Docker, plusieurs composants collaborent :

```
  Toi
   │
   ▼
Docker CLI  ────►  Docker Daemon  ────►  containerd  ────►  runc  ────►  Container
(docker run)       (dockerd)              (gestion)         (exécution)
```

- **Docker CLI** : la commande `docker` que tu tapes dans le terminal
- **Docker Daemon** (`dockerd`) : le service qui tourne en arrière-plan et gère tout
- **containerd** : le runtime de haut niveau qui gère le cycle de vie des containers
- **runc** : le runtime de bas niveau qui crée effectivement le container (namespaces, cgroups)

Tu n’as pas besoin de connaître ces détails pour utiliser Docker au quotidien. Mais savoir que le Docker daemon tourne en **root** et que le socket Docker (`/var/run/docker.sock`) donne un accès total au daemon est crucial pour la sécurité (on y reviendra au chapitre 21).

## Très utile en pratique

### OverlayFS : le filesystem en couches concrètement

Le filesystem utilisé par Docker (sur la plupart des distributions Linux) s’appelle **OverlayFS**. Il superpose les couches de l’image et rend le tout transparent pour l’application dans le container.

```bash
# Voir les couches d'une image
docker inspect --format='{{.RootFS.Layers}}' python:3.12-slim
```

Chaque couche est identifiée par un hash SHA256. Si tu modifies une seule ligne de ton Dockerfile, seules les couches à partir de cette ligne sont reconstruites — c’est le **cache de build**, et c’est un gain de temps considérable.

### Les capabilities Linux

En plus des namespaces et des cgroups, Linux a un système de **capabilities** — des permissions granulaires qui décomposent les pouvoirs du root. Au lieu de donner “tous les droits” (root classique), on peut donner des droits spécifiques :

|Capability        |Droit accordé                                |
|------------------|---------------------------------------------|
|`NET_BIND_SERVICE`|Écouter sur les ports < 1024                 |
|`NET_RAW`         |Utiliser des sockets raw (ping, tcpdump)     |
|`SYS_ADMIN`       |Presque tout — la “super capability” à éviter|
|`SYS_PTRACE`      |Tracer les processus (débogage)              |
|`DAC_OVERRIDE`    |Ignorer les permissions de fichiers          |

Docker donne un ensemble de capabilities par défaut à chaque container. En sécurité, le principe est de **supprimer toutes les capabilities** (`--cap-drop ALL`) puis d’ajouter uniquement celles dont l’application a besoin (`--cap-add NET_BIND_SERVICE`). On verra ça en détail au chapitre 23.

## Bonus

### Alternatives à Docker : Podman

**Podman** est une alternative à Docker qui fonctionne **sans daemon** (pas de processus root en arrière-plan) et peut exécuter des containers **sans privilèges root** (rootless). Les commandes sont les mêmes (`podman run` au lieu de `docker run`). C’est un choix de plus en plus courant dans les environnements où la sécurité est une priorité (RHEL, Fedora).

### Les runtimes alternatifs

- **gVisor** (Google) : un kernel “sandbox” qui intercepte les appels système du container — isolation plus forte que les namespaces classiques, avec un coût en performance
- **Kata Containers** : des containers qui tournent dans des micro-VMs — l’isolation d’une VM avec l’expérience utilisateur d’un container
- **Firecracker** (AWS) : des micro-VMs ultra-légères (démarrage en 125ms) utilisées par AWS Lambda et Fargate

Ces alternatives existent pour les cas où l’isolation standard des containers n’est pas suffisante (environnements multi-tenant, clouds publics).

## ❌ Erreur classique

```
# Croire que "isolation par namespaces" = "aussi sécurisé qu'une VM"
→ Les namespaces sont une isolation logicielle, pas matérielle.
  Une vulnérabilité kernel peut permettre un "container escape".

# Ignorer les cgroups (ne pas mettre de limites de ressources)
→ Un container sans limite mémoire peut consommer toute la RAM de l'hôte
  et faire tomber les autres containers.

# Confondre "root dans le container" et "root sur l'hôte"
→ Par défaut, root dans le container correspond à l'UID 0 sur l'hôte (si le
  remapping n'est pas activé). L'isolation par namespaces et capabilities le
  limite, mais en cas de faille d'isolation ou de mauvaise configuration,
  l'impact peut devenir critique.
```

## ✅ Tu sais maintenant…

- Les namespaces isolent les processus, le réseau et le filesystem de chaque container
- Les cgroups limitent les ressources (CPU, mémoire)
- Le filesystem fonctionne par couches en lecture seule + une couche d’écriture temporaire
- Le kernel est partagé entre tous les containers et la machine hôte
- Pourquoi cette architecture a des implications en sécurité

-----

# Chapitre 3 — Installer Docker et premiers containers

## Le minimum à savoir

### Installer Docker

**Linux (Ubuntu/Debian) :**

```bash
# 1. Supprimer les anciennes versions éventuelles
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2. Installer les prérequis
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

# 3. Ajouter le dépôt officiel Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Installer Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# 5. Ajouter ton utilisateur au groupe docker (pour ne pas taper sudo à chaque fois)
sudo usermod -aG docker $USER
# ⚠️ Déconnecte-toi et reconnecte-toi pour que ça prenne effet
```

> **Important :** utilise le dépôt **officiel Docker**, pas le paquet `docker.io` de ta distribution. Le paquet de la distribution est souvent une version ancienne.

> **Note sécurité :** ajouter ton utilisateur au groupe `docker` lui donne **l’équivalent des droits root** sur la machine (car le Docker daemon tourne en root). C’est pratique pour le développement, mais en production, l’accès au groupe docker doit être restreint. Si la sécurité est une priorité, sache que deux alternatives existent : **Docker en mode rootless** (le daemon tourne sans root — configuration spécifique) et **Podman** (un outil compatible Docker qui fonctionne nativement sans daemon root). Pour ce cours, on utilise Docker classique — c’est le plus répandu et le plus simple pour apprendre.

**Mac / Windows :** installe [Docker Desktop](https://www.docker.com/products/docker-desktop/) — c’est une application graphique qui installe tout. Sur Mac et Windows, Docker tourne en réalité dans une VM Linux cachée (car les containers Linux ont besoin d’un kernel Linux).

### Vérifier l’installation

```bash
docker version
```

Tu devrais voir deux sections : **Client** et **Server**. Si le Server ne répond pas, le daemon Docker n’est pas démarré (`sudo systemctl start docker`).

```bash
docker info
```

Affiche des informations sur l’installation : nombre de containers, nombre d’images, version du kernel, driver de stockage, etc.

### Ton premier container

```bash
docker run hello-world
```

Que se passe-t-il ? Décortiquons :

1. Docker cherche l’image `hello-world` en local → elle n’existe pas
1. Docker la **télécharge** (pull) depuis Docker Hub
1. Docker **crée** un container à partir de cette image
1. Docker **exécute** le programme dans le container (qui affiche un message)
1. Le programme se termine → le container **s’arrête**

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Félicitations, tu as lancé ton premier container !

### Les commandes essentielles

```bash
# Lancer un container
docker run nginx                  # Lance un serveur web Nginx

# Lancer en arrière-plan (mode détaché)
docker run -d nginx               # Le -d "détache" : le container tourne en fond

# Voir les containers en cours d'exécution
docker ps

# Voir TOUS les containers (y compris les arrêtés)
docker ps -a

# Arrêter un container
docker stop <id_ou_nom>

# Supprimer un container arrêté
docker rm <id_ou_nom>

# Voir les logs d'un container
docker logs <id_ou_nom>

# Exécuter une commande dans un container en cours d'exécution
docker exec -it <id_ou_nom> bash
```

> **Le flag `-it` :** `-i` = interactif (garde l’entrée standard ouverte), `-t` = terminal (alloue un pseudo-terminal). Combinés, ils te permettent d’entrer “dans” le container et de taper des commandes comme si tu étais sur une machine.

### Explorer un container interactif

```bash
docker run -it ubuntu bash
```

Tu es maintenant “dans” un container Ubuntu. Tu peux explorer :

```bash
ls /                  # Le filesystem du container (pas celui de ton hôte !)
cat /etc/os-release   # C'est bien Ubuntu
ps aux                # Très peu de processus (juste bash et ps)
whoami                # root (par défaut — on verra pourquoi c'est un problème)
exit                  # Quitter le container (il s'arrête)
```

> **Point crucial :** quand tu quittes le container, tout ce que tu as fait dedans **disparaît**. Si tu as créé un fichier, il est perdu. Le container est **éphémère** par nature. C’est un concept fondamental : les containers naissent, vivent et meurent — les données qui doivent survivre doivent être dans un **volume** (chapitre 5).

### Exposer un port

Par défaut, un container est isolé du réseau de la machine hôte. Pour accéder à un service qui tourne dans un container depuis ton navigateur, tu dois **mapper un port** :

```bash
docker run -d -p 8080:80 nginx
```

`-p 8080:80` signifie : “le port 8080 de ma machine → le port 80 du container”. Tu peux maintenant ouvrir `http://localhost:8080` dans ton navigateur et voir la page par défaut de Nginx.

```
Port machine hôte     Port container
      8080       →        80
```

> **📋 CONTAINER — Épisode 2**
> 
> Sami installe Docker sur sa machine de travail et lance son premier container PostgreSQL :
> 
> ```bash
> docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=secret postgres:16
> ```
> 
> Il s’y connecte avec `psql` et crée une table. Puis il arrête le container (`docker stop`), le relance (`docker start`), et constate que ses données sont toujours là. Mais quand il **supprime** le container (`docker rm`) et en crée un nouveau, les données ont disparu. Il comprend la différence entre arrêter et supprimer, et pourquoi il faut un volume.

## Très utile en pratique

### Nommer ses containers

```bash
docker run -d --name mon_nginx -p 8080:80 nginx
docker stop mon_nginx
docker start mon_nginx
docker logs mon_nginx
```

Beaucoup plus pratique que d’utiliser l’ID hexadécimal (`a3f2b1c9d8e7...`).

### Le cycle de vie complet

```
docker create  →  docker start  →  docker stop  →  docker rm
   (créé)           (en cours)       (arrêté)       (supprimé)

  ou directement :
docker run  =  docker create + docker start
```

Un container arrêté **existe encore** (tu peux le voir avec `docker ps -a`, le redémarrer avec `docker start`). Il ne disparaît que quand tu le supprimes (`docker rm`).

### Le nettoyage

Les containers arrêtés et les images téléchargées s’accumulent. Pour nettoyer :

```bash
# Supprimer tous les containers arrêtés
docker container prune

# Supprimer toutes les images non utilisées
docker image prune

# Tout nettoyer d'un coup (containers arrêtés + images non utilisées + réseaux + cache)
docker system prune
```

### Le flag `--rm` : containers jetables

```bash
docker run --rm -it ubuntu bash
```

Le `--rm` supprime automatiquement le container quand il s’arrête. Parfait pour les utilisations ponctuelles (tester une commande, lancer un outil, explorer).

## Bonus

### Voir les ressources consommées

```bash
docker stats
```

Affiche en temps réel le CPU, la mémoire, le réseau et le disque de chaque container — l’équivalent d’un `top` pour les containers.

### Inspecter un container en détail

```bash
docker inspect mon_nginx
```

Renvoie un JSON détaillé avec toute la configuration du container : réseau (adresse IP), volumes, variables d’environnement, état, etc. Utile pour le troubleshooting.

## ❌ Erreur classique

```bash
# Oublier -d (le terminal est bloqué)
docker run nginx         # ← Ton terminal est pris. Ctrl+C pour arrêter.
docker run -d nginx      # ← Tourne en arrière-plan, ton terminal est libre.

# Oublier -p (le service n'est pas accessible)
docker run -d nginx      # ← Nginx tourne mais tu ne peux pas y accéder
docker run -d -p 8080:80 nginx   # ← Accessible sur localhost:8080

# Confondre stop et rm
docker stop mon_container   # ← Le container existe encore (arrêté)
docker rm mon_container     # ← Le container est supprimé définitivement

# Confondre le port hôte et le port container
docker run -d -p 80:8080 nginx   # ← Inverse ! C'est hôte:container
docker run -d -p 8080:80 nginx   # ← Correct : port 8080 de l'hôte → port 80 du container
```

## Exercices

**Guidé :** Lance un container Nginx en arrière-plan, expose-le sur le port 8080, vérifie dans ton navigateur, regarde les logs, puis arrête-le et supprime-le.

**Autonome :** Lance un container `python:3.12` en mode interactif (`-it`), tape `python3` à l’intérieur, exécute `print("Hello from a container!")`, puis quitte. Observe que le container s’arrête quand tu quittes.

## ✅ Tu sais maintenant…

- Installer Docker et vérifier l’installation
- Lancer un container avec `docker run`
- Les flags essentiels : `-d` (détaché), `-it` (interactif), `-p` (port), `--name` (nom), `--rm` (jetable)
- Le cycle de vie : run → stop → rm (ou start pour redémarrer)
- Que les containers sont éphémères — les données disparaissent à la suppression
- Les commandes de base : `docker ps`, `docker logs`, `docker exec`, `docker stop`, `docker rm`

-----

# Chapitre 4 — Images Docker : comprendre, chercher, utiliser

## Le minimum à savoir

### Image vs container

L’**image** est le plan de construction. Le **container** est l’instance en cours d’exécution.

```
Image (template)          Container (instance)
┌──────────────┐          ┌──────────────┐
│ Python 3.12  │  ──►     │ Python 3.12  │  ← en cours d'exécution
│ + Flask      │  ──►     │ + Flask      │  ← avec sa couche d'écriture
│ + mon app    │  ──►     │ + mon app    │  ← processus actifs
└──────────────┘          └──────────────┘
   (lecture seule)          (vivant, éphémère)
```

Une image peut générer **plusieurs containers** identiques, comme un moule peut produire plusieurs gâteaux.

### Docker Hub : le “GitHub des images”

[Docker Hub](https://hub.docker.com) est le registry public par défaut. Quand tu fais `docker run nginx`, Docker télécharge l’image `nginx` depuis Docker Hub.

Il existe deux types d’images sur Docker Hub :

- **Images officielles** : maintenues par Docker et/ou les éditeurs (nginx, postgres, python, ubuntu…). Elles ont un badge “Official Image” et sont régulièrement mises à jour et scannées. C’est ce qu’il faut utiliser.
- **Images communautaires** : publiées par n’importe qui (`utilisateur/nom_image`). **Attention** : n’importe qui peut publier une image sur Docker Hub. Une image communautaire peut contenir du code malveillant, des CVE non corrigées, ou des backdoors. En environnement professionnel, on n’utilise que des images officielles ou des images d’un registry privé.

### Les tags : choisir la version

Chaque image a des **tags** qui identifient une version :

```bash
docker run python:3.12        # Python 3.12 (version spécifique)
docker run python:3.12-slim   # Version allégée (moins de packages système)
docker run python:3.12-alpine # Version ultra-légère (basée sur Alpine Linux)
docker run python:latest      # La dernière version (⚠️ change au fil du temps !)
docker run python              # Équivalent de python:latest
```

> **Règle importante :** ne jamais utiliser `latest` en production. Le tag `latest` change quand une nouvelle version est publiée. Ton container pourrait se comporter différemment d’un jour à l’autre. Utilise toujours un tag de version spécifique (`python:3.12`, `postgres:16`, `nginx:1.25`).

### Les variantes d’images

|Variante            |Taille typique|Contenu                                     |Usage                                             |
|--------------------|--------------|--------------------------------------------|--------------------------------------------------|
|`python:3.12`       |~900 Mo       |OS Debian complet + Python + outils de build|Développement, CI                                 |
|`python:3.12-slim`  |~150 Mo       |Debian minimal + Python                     |Production (bon compromis)                        |
|`python:3.12-alpine`|~50 Mo        |Alpine Linux + Python                       |Quand la taille compte (attention : compatibilité)|
|**distroless**      |~20 Mo        |Juste le runtime, pas de shell              |Production sécurisée                              |


> **Conseil pour débuter :** commence avec les images `slim`. Elles offrent un bon compromis entre taille raisonnable et compatibilité. Les images `alpine` sont plus petites mais peuvent causer des problèmes de compatibilité (musl vs glibc). Les images distroless sont pour la production durcie — pas de shell, pas d’outils de debug, surface d’attaque minimale.

### Gérer les images localement

```bash
# Télécharger une image sans lancer de container
docker pull nginx:1.25

# Lister les images sur ta machine
docker images

# Supprimer une image
docker rmi nginx:1.25

# Voir la taille de toutes les images
docker images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}"
```

### Les couches d’une image

```bash
# Voir les couches et les instructions qui les ont créées
docker history python:3.12-slim
```

Chaque ligne correspond à une couche. Tu peux voir la taille de chaque couche et l’instruction Dockerfile qui l’a créée. C’est utile pour comprendre pourquoi une image est grosse.

## Très utile en pratique

### Inspecter une image avant de l’utiliser

```bash
# Voir les métadonnées complètes
docker inspect python:3.12-slim

# Voir le user par défaut, les ports exposés, les variables d'environnement
docker inspect --format='{{.Config.User}}' python:3.12-slim
docker inspect --format='{{.Config.ExposedPorts}}' nginx:1.25
```

C’est le réflexe d’audit : avant de lancer une image en production, inspecte-la. Quel utilisateur ? Quels ports ? Quelles variables d’environnement par défaut ?

### Chercher des images

```bash
# Chercher sur Docker Hub depuis le terminal
docker search postgres

# Filtrer les images officielles
docker search --filter is-official=true postgres
```

En pratique, la recherche sur le site web Docker Hub est plus pratique (tu vois la documentation, les tags disponibles, les instructions d’utilisation).

### Sauvegarder et charger des images (hors ligne)

```bash
# Exporter une image dans un fichier
docker save nginx:1.25 -o nginx.tar

# Importer une image depuis un fichier
docker load -i nginx.tar
```

Utile pour transférer des images vers des machines sans accès Internet.

## Bonus

### Comprendre le pull rate limit de Docker Hub

Docker Hub limite le nombre de téléchargements d’images :

- Utilisateur anonyme : 100 pulls par 6 heures
- Utilisateur authentifié (gratuit) : 200 pulls par 6 heures
- Abonnement payant : illimité

En CI/CD, ces limites sont vite atteintes. C’est une des raisons pour lesquelles les entreprises utilisent un **registry privé** qui met en cache les images officielles (voir chapitre 9).

### Les images multi-architectures

Une même image peut contenir des variantes pour différentes architectures CPU (amd64, arm64). Quand tu fais `docker pull nginx`, Docker télécharge automatiquement la variante correspondant à ton architecture. C’est transparent, mais c’est important si tu développes sur un Mac avec puce Apple (arm64) et que tu déploies sur un serveur x86_64 (amd64).

## ❌ Erreur classique

```bash
# Utiliser "latest" en production
docker run myapp:latest    # ❌ "latest" peut changer à tout moment
docker run myapp:1.5.2     # ✅ Version fixée et prévisible

# Utiliser une image communautaire non vérifiée en production
docker run random_user/mysteriousapp    # ❌ Qui a construit ça ? Qu'est-ce qu'il y a dedans ?
docker run library/nginx:1.25           # ✅ Image officielle

# Accumuler des images sans nettoyer
docker images              # ← 50 images, 30 Go de disque
docker image prune -a      # ← Supprime les images non utilisées
```

## ✅ Tu sais maintenant…

- La différence entre image (template) et container (instance)
- Docker Hub et les images officielles vs communautaires
- Les tags et pourquoi ne pas utiliser `latest`
- Les variantes d’images (full, slim, alpine, distroless)
- Gérer les images localement (pull, images, rmi, history, inspect)

-----

# Chapitre 5 — Réseau, volumes et persistance

## Le minimum à savoir

### Le réseau Docker

Par défaut, Docker crée un réseau virtuel isolé. Les containers sur le même réseau peuvent communiquer entre eux par leur **nom** (DNS interne). Les containers sur des réseaux différents ne peuvent pas se voir.

```bash
# Créer un réseau
docker network create mon_reseau

# Lancer deux containers sur le même réseau
docker run -d --name web --network mon_reseau nginx
docker run -d --name db --network mon_reseau postgres:16 -e POSTGRES_PASSWORD=secret

# Depuis le container "web", on peut joindre "db" par son nom
docker exec web ping db    # ← "db" est résolu en adresse IP automatiquement
```

> **Pourquoi c’est important :** quand ton application Django doit se connecter à PostgreSQL, tu n’as pas besoin de connaître l’adresse IP du container PostgreSQL (elle change à chaque fois). Tu utilises simplement le **nom du container** comme hostname (`db` dans l’exemple ci-dessus). Docker résout le nom en adresse IP automatiquement.

### L’exposition de ports (rappel et approfondissement)

```bash
docker run -d -p 8080:80 nginx
#              ↑      ↑
#           hôte    container
```

Sans `-p`, le container est isolé du réseau de la machine hôte. Le port est accessible à l’intérieur du réseau Docker, mais pas depuis ton navigateur ou depuis l’extérieur.

Avec `-p 8080:80`, le port 80 du container est accessible via le port 8080 de la machine hôte.

> **Sécurité :** par défaut, `-p 8080:80` expose le port sur **toutes les interfaces réseau** de la machine (0.0.0.0). Pour limiter à localhost uniquement : `-p 127.0.0.1:8080:80`.

### Les volumes : la persistance des données

Les containers sont **éphémères** : quand un container est supprimé, tout ce qu’il contenait disparaît. C’est un problème pour les bases de données, les fichiers uploadés, les logs.

La solution : les **volumes**. Un volume est un espace de stockage qui existe **en dehors du container** et qui survit à sa destruction.

```bash
# Créer un volume nommé
docker volume create mes_donnees

# Lancer un container avec le volume monté
docker run -d --name ma_db \
  -v mes_donnees:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:16
```

`-v mes_donnees:/var/lib/postgresql/data` signifie : “monte le volume `mes_donnees` dans le dossier `/var/lib/postgresql/data` du container”. PostgreSQL stocke ses données dans ce dossier — elles sont maintenant persistées dans le volume.

Si tu supprimes le container et en crées un nouveau avec le même volume, les données sont toujours là :

```bash
docker rm -f ma_db    # Supprime le container
docker run -d --name ma_db_v2 \
  -v mes_donnees:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:16
# ← Les données de l'ancienne base sont toujours là !
```

### Les 3 types de montages

|Type            |Syntaxe                            |Usage                                                                        |
|----------------|-----------------------------------|-----------------------------------------------------------------------------|
|**Volume nommé**|`-v mon_volume:/chemin`            |Données de production (bases de données, fichiers uploadés) — géré par Docker|
|**Bind mount**  |`-v /chemin/hôte:/chemin/container`|Développement (monter ton code source dans le container)                     |
|**tmpfs**       |`--tmpfs /chemin`                  |Données temporaires en mémoire uniquement                                    |

```bash
# Volume nommé (production)
docker run -v pgdata:/var/lib/postgresql/data postgres:16

# Bind mount (développement — ton code est synchronisé en temps réel)
docker run -v $(pwd)/mon_app:/app python:3.12

# tmpfs (données sensibles temporaires — jamais écrites sur disque)
docker run --tmpfs /tmp myapp
```

> **À retenir :** utilise des **volumes nommés** pour les données de production et des **bind mounts** pour le développement (voir ton code modifié en direct dans le container).

### Les variables d’environnement

Les variables d’environnement sont le mécanisme standard pour configurer un container sans modifier l’image :

```bash
docker run -d \
  -e POSTGRES_USER=medflow \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=patients \
  postgres:16
```

Chaque image a ses propres variables d’environnement documentées sur Docker Hub. PostgreSQL utilise `POSTGRES_PASSWORD`, MySQL utilise `MYSQL_ROOT_PASSWORD`, etc.

> **Attention sécurité :** passer des mots de passe en clair avec `-e` les rend visibles dans `docker inspect` et dans l’historique des commandes. En production, on utilise des secrets (voir chapitres 8 et 25). Pour le développement et l’apprentissage, `-e` suffit.

> **📋 CONTAINER — Épisode 3**
> 
> Sami crée un réseau Docker dédié pour MedFlow, lance PostgreSQL avec un volume persistant, Redis sans volume (le cache est éphémère par nature), et connecte l’application Django aux deux services par leur nom DNS interne. Premier stack fonctionnel en local — Django parle à PostgreSQL via `db:5432` et à Redis via `redis:6379`, sans adresses IP en dur.

## Très utile en pratique

### Les drivers réseau Docker

|Driver   |Description                                                      |Usage                                        |
|---------|-----------------------------------------------------------------|---------------------------------------------|
|`bridge` |Réseau isolé par défaut                                          |Le plus courant — containers sur un même hôte|
|`host`   |Pas d’isolation réseau (le container utilise le réseau de l’hôte)|Performance maximale, mais pas d’isolation   |
|`none`   |Pas de réseau                                                    |Containers qui n’ont pas besoin de réseau    |
|`overlay`|Réseau multi-hôtes                                               |Docker Swarm / environnements multi-serveurs |

```bash
# Le réseau bridge par défaut
docker run -d nginx    # ← Utilise le bridge par défaut

# Un réseau bridge nommé (recommandé)
docker network create mon_app
docker run -d --network mon_app --name web nginx
docker run -d --network mon_app --name api myapp
# web et api peuvent se joindre par nom
```

> **Bonne pratique :** crée toujours un réseau nommé pour tes applications. Le réseau bridge par défaut ne supporte pas la résolution DNS par nom de container.

### Gérer les volumes

```bash
# Lister les volumes
docker volume ls

# Inspecter un volume (voir où il est stocké sur l'hôte)
docker volume inspect mes_donnees

# Supprimer un volume (⚠️ les données sont perdues !)
docker volume rm mes_donnees

# Supprimer les volumes non utilisés
docker volume prune
```

### Cas pratique complet : stack minimale

```bash
# Créer le réseau
docker network create medflow

# Lancer PostgreSQL avec persistance
docker run -d --name db \
  --network medflow \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=medflow \
  postgres:16

# Lancer Redis (cache — pas besoin de volume)
docker run -d --name redis \
  --network medflow \
  redis:7

# Lancer l'application (en bind mount pour le dev)
docker run -d --name web \
  --network medflow \
  -p 8000:8000 \
  -v $(pwd):/app \
  -e DATABASE_URL=postgresql://postgres:secret@db/medflow \
  -e REDIS_URL=redis://redis:6379 \
  python:3.12 python /app/manage.py runserver 0.0.0.0:8000
```

C’est fonctionnel, mais gérer 3 commandes `docker run` manuellement est ingérable dès que la stack grossit. C’est exactement le problème que Docker Compose résout (chapitre 8).

## Bonus

### Inspecter le réseau

```bash
# Voir les containers connectés à un réseau
docker network inspect medflow

# Depuis l'intérieur d'un container, voir la config réseau
docker exec web cat /etc/hosts
docker exec web ip addr
```

### Le read-only filesystem

Tu peux lancer un container avec un filesystem en **lecture seule** pour réduire la surface d’attaque :

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run nginx
```

L’application ne peut rien écrire sauf dans `/tmp` et `/run` (montés en tmpfs, en mémoire). Un attaquant qui compromet l’application ne peut pas déposer de fichier sur le disque.

## ❌ Erreur classique

```bash
# Oublier le volume sur la base de données
docker run -d postgres:16      # ❌ Les données disparaîtront à la suppression

# Utiliser le réseau bridge par défaut et s'attendre à la résolution DNS
docker run -d --name web nginx
docker run -d --name db postgres:16
docker exec web ping db        # ❌ Ne fonctionne PAS sur le bridge par défaut
# → Crée un réseau nommé !

# Exposer un port sur toutes les interfaces
docker run -d -p 5432:5432 postgres:16    # ❌ PostgreSQL accessible depuis Internet !
docker run -d -p 127.0.0.1:5432:5432 postgres:16   # ✅ Uniquement en local
```

## 🧩 Mini-projet (chapitres 3-5)

Crée une stack “blog” minimale :

1. Un container **PostgreSQL** avec un volume persistant et un mot de passe configuré
1. Un container **Nginx** qui sert une page HTML (montée en bind mount depuis ton hôte)
1. Les deux containers sur un **réseau nommé**
1. Nginx accessible sur le port 8080 de ton hôte
1. Vérifie que les données PostgreSQL survivent à un `docker rm` + recréation du container

## ✅ Tu sais maintenant…

- Créer un réseau Docker et y connecter des containers
- Exposer un port avec `-p hôte:container`
- Persister des données avec les volumes (et la différence volume nommé vs bind mount)
- Configurer un container avec les variables d’environnement (`-e`)
- Pourquoi ne pas utiliser le réseau bridge par défaut

-----

# PARTIE II — CONSTRUIRE ET COMPOSER

-----

# Chapitre 6 — Écrire un Dockerfile : de zéro à l’image

## Le minimum à savoir

### Qu’est-ce qu’un Dockerfile ?

Un Dockerfile est un **fichier texte** qui décrit, étape par étape, comment construire une image Docker. C’est la recette de construction de ton container. Chaque ligne est une instruction que Docker exécute dans l’ordre.

### Le prérequis : comprendre YAML et les fichiers de configuration

Avant d’aller plus loin, un mot sur les fichiers de configuration. Docker utilise des Dockerfiles (syntaxe propre), Docker Compose utilise des fichiers YAML, et Kubernetes utilise aussi du YAML. Le YAML est un format texte structuré très lisible, basé sur l’**indentation** (comme Python). Voici un aperçu rapide :

```yaml
# Ceci est un commentaire YAML
nom: Alice
age: 25
langages:
  - Python
  - Bash
  - Go
serveur:
  host: 192.168.1.1
  port: 8080
```

Les règles essentielles du YAML : **2 espaces** pour l’indentation (pas de tabulations), les listes commencent par un tiret (`-`), les clés-valeurs sont séparées par un deux-points et un espace (`clé: valeur`). On utilisera le YAML à partir du chapitre 8 (Docker Compose) et du chapitre 14 (Kubernetes).

### Les instructions essentielles du Dockerfile

```dockerfile
# Chaque Dockerfile commence par FROM — l'image de base
FROM python:3.12-slim

# Définir le dossier de travail dans le container
WORKDIR /app

# Copier des fichiers depuis ta machine vers le container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables d'environnement
ENV FLASK_APP=app.py

# Port que l'application écoute (documentaire — n'expose pas réellement)
EXPOSE 5000

# La commande qui se lance quand le container démarre
CMD ["python", "app.py"]
```

Détaillons chaque instruction :

|Instruction |Rôle                                                  |Exemple                   |
|------------|------------------------------------------------------|--------------------------|
|`FROM`      |Image de base (obligatoire, toujours en premier)      |`FROM python:3.12-slim`   |
|`WORKDIR`   |Définit le dossier de travail                         |`WORKDIR /app`            |
|`COPY`      |Copie des fichiers de l’hôte vers l’image             |`COPY app.py /app/`       |
|`RUN`       |Exécute une commande pendant la construction          |`RUN pip install flask`   |
|`ENV`       |Définit une variable d’environnement                  |`ENV DEBUG=false`         |
|`EXPOSE`    |Documente le port utilisé (ne l’expose pas réellement)|`EXPOSE 8080`             |
|`CMD`       |Commande par défaut au démarrage du container         |`CMD ["python", "app.py"]`|
|`ENTRYPOINT`|Point d’entrée fixe (CMD devient les arguments)       |`ENTRYPOINT ["python"]`   |

### Construire et tester

**Étape 1 — Crée une application simple** (`app.py`) :

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello depuis un container Docker !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**Étape 2 — Crée le fichier des dépendances** (`requirements.txt`) :

```
flask==3.0.*
```

**Étape 3 — Crée le Dockerfile :**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Étape 4 — Construis l’image :**

```bash
docker build -t mon_app .
```

`-t mon_app` donne un nom (tag) à l’image. Le `.` indique que le contexte de build est le dossier actuel.

**Étape 5 — Lance le container :**

```bash
docker run -d -p 5000:5000 mon_app
```

Ouvre `http://localhost:5000` — tu vois “Hello depuis un container Docker !”

### Le `.dockerignore`

Comme un `.gitignore`, le `.dockerignore` exclut des fichiers du contexte de build. C’est important pour la **performance** (ne pas envoyer des Go de fichiers inutiles au daemon Docker) et la **sécurité** (ne pas inclure de secrets dans l’image).

```
# .dockerignore
.git
.env
__pycache__
*.pyc
node_modules
.vscode
```

> **📋 CONTAINER — Épisode 4 (partie 1)**
> 
> Sami écrit le Dockerfile pour l’application Django de MedFlow. Première version : image de base `python:3.12` (image complète), pas de `.dockerignore`, copie de tout le repo (y compris le `.git` de 200 Mo et le fichier `.env` avec les secrets). L’image fait 1.2 Go. Premier réflexe d’optimisation au chapitre suivant.

## Très utile en pratique

### L’ordre des instructions : optimiser le cache

Docker met en cache chaque couche. Si une instruction n’a pas changé, Docker réutilise le cache au lieu de la reconstruire. L’astuce : **mettre les instructions qui changent le moins souvent en premier**.

```dockerfile
# ✅ BON ORDRE — les dépendances changent rarement, le code change souvent
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .              # ← Change rarement
RUN pip install --no-cache-dir -r requirements.txt   # ← Mis en cache si requirements.txt n'a pas changé
COPY . .                              # ← Change à chaque modification du code
CMD ["python", "app.py"]

# ❌ MAUVAIS ORDRE — tout est reconstruit à chaque changement de code
FROM python:3.12-slim
WORKDIR /app
COPY . .                              # ← Change à chaque modification
RUN pip install --no-cache-dir -r requirements.txt   # ← Reconstruit à chaque fois !
CMD ["python", "app.py"]
```

### La différence CMD vs ENTRYPOINT

`CMD` est la commande par défaut, remplaçable à l’exécution. `ENTRYPOINT` est le point d’entrée fixe.

```dockerfile
# Avec CMD — la commande peut être remplacée
CMD ["python", "app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app python test.py     → exécute python test.py (remplace CMD)

# Avec ENTRYPOINT + CMD — ENTRYPOINT est fixe, CMD fournit les arguments par défaut
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app test.py            → exécute python test.py
```

Pour un débutant, utilise `CMD`. `ENTRYPOINT` est utile quand ton container est un outil en ligne de commande.

## Bonus

### Les labels

Les labels ajoutent des métadonnées à l’image :

```dockerfile
LABEL maintainer="sami@example.com"
LABEL version="1.0"
LABEL description="Application MedFlow"
```

### Les arguments de build (ARG)

`ARG` permet de passer des variables au moment du build (pas au runtime) :

```dockerfile
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim
```

```bash
docker build --build-arg PYTHON_VERSION=3.11 -t mon_app .
```

> **Attention sécurité :** ne passe JAMAIS de secrets via `ARG`. Les valeurs `ARG` sont visibles dans l’historique des couches (`docker history`).

## ❌ Erreur classique

```dockerfile
# Mettre COPY . . avant RUN pip install → le cache est invalidé à chaque changement de code

# Oublier --no-cache-dir dans pip install → l'image est plus grosse pour rien
RUN pip install flask                        # ❌ Conserve le cache pip dans l'image
RUN pip install --no-cache-dir flask         # ✅ Pas de cache inutile

# Utiliser ADD au lieu de COPY (sauf besoin spécifique)
ADD app.py /app/     # ❌ ADD fait des choses en plus (décompression, URL) — trop magique
COPY app.py /app/    # ✅ COPY est simple et prévisible
```

## ✅ Tu sais maintenant…

- Écrire un Dockerfile de base (`FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`)
- Construire une image avec `docker build -t nom .`
- L’importance du `.dockerignore`
- L’optimisation du cache par l’ordre des instructions

-----

# Chapitre 7 — Optimiser et durcir ses images

## Le minimum à savoir

### Le multi-stage build

C’est LA technique d’optimisation la plus importante. L’idée : utiliser une première image pour **compiler/construire**, puis copier uniquement le résultat dans une deuxième image plus légère.

```dockerfile
# Étape 1 : construction (image lourde avec les outils de build)
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Étape 2 : production (image légère, juste le nécessaire)
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["python", "app.py"]
```

L’image finale ne contient **pas** les outils de build, pas le cache pip, pas les headers de compilation. Elle est beaucoup plus petite et a une surface d’attaque réduite.

### L’utilisateur non-root

Par défaut, les processus dans un container tournent en **root**. C’est dangereux : si un attaquant exploite une faille dans l’application, il est root dans le container (UID 0). Sans user namespace remapping ni mode rootless, cet UID 0 correspond à celui de l’hôte. Les mécanismes d’isolation (namespaces, capabilities) limitent ce que ce root peut faire, mais en cas de faille d’isolation ou de mauvaise configuration, l’impact peut devenir critique.

```dockerfile
FROM python:3.12-slim
WORKDIR /app

# Créer un utilisateur non-root
RUN useradd --create-home --shell /bin/bash appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Basculer vers l'utilisateur non-root
USER appuser

# L'application écoute sur un port > 1024 (les ports < 1024 nécessitent root)
EXPOSE 8000
CMD ["python", "app.py"]
```

> **À retenir pour un entretien :** “En production, les containers ne doivent jamais tourner en root. On crée un utilisateur dédié dans le Dockerfile avec `USER`. C’est la mesure de sécurité la plus impactante et la plus simple à mettre en place.”

### Scanner ses images

Les images Docker contiennent des packages système et des bibliothèques qui peuvent avoir des **vulnérabilités connues** (CVE). Un scanner analyse l’image et liste les CVE trouvées.

```bash
# Installer Trivy (le scanner open source le plus populaire)
# Sur Linux :
sudo apt-get install trivy
# Ou via Docker lui-même :
docker run --rm aquasec/trivy image python:3.12-slim

# Scanner une image
trivy image mon_app:latest
```

Le scan va lister les CVE par sévérité (CRITICAL, HIGH, MEDIUM, LOW). L’objectif n’est pas d’avoir 0 CVE (c’est souvent impossible — les images de base ont des CVE dans les bibliothèques système), mais de n’avoir aucune CVE **critique ou haute** exploitable.

> **Point important :** un scan est un **signal**, pas un verdict. Une CVE dans une bibliothèque que ton application n’utilise pas n’est pas un risque réel. Mais une CVE critique dans OpenSSL sur une image exposée à Internet est un problème urgent.

> **📋 CONTAINER — Épisode 4 (partie 2)**
> 
> Sami optimise le Dockerfile de MedFlow. Image de base `python:3.12` (1.2 Go, 147 CVE) → multi-stage build avec `python:3.12-slim` (180 Mo, 12 CVE en low/medium), utilisateur non-root, `.dockerignore` qui exclut `.git`, `.env`, et `__pycache__`. Le scan Trivy est ajouté au pipeline GitLab CI : le build échoue si une CVE critique est détectée.

## Très utile en pratique

### Choisir la bonne image de base

|Image de base              |Taille |Surface d’attaque        |Compatibilité   |Usage recommandé            |
|---------------------------|-------|-------------------------|----------------|----------------------------|
|`python:3.12`              |~900 Mo|Large (Debian complète)  |Excellente      |Dev, CI, debug              |
|`python:3.12-slim`         |~150 Mo|Moyenne                  |Très bonne      |**Production (recommandé)** |
|`python:3.12-alpine`       |~50 Mo |Petite                   |Attention (musl)|Quand la taille est critique|
|`gcr.io/distroless/python3`|~20 Mo |Minimale (pas de shell !)|Limitée         |Production durcie           |


> **Conseil :** commence avec `slim`. C’est le meilleur compromis pour la plupart des cas. Alpine peut causer des problèmes de compatibilité avec certaines bibliothèques Python (car Alpine utilise `musl` au lieu de `glibc`). Distroless est le choix le plus sécurisé mais rend le debugging très difficile (pas de shell dans le container).

### Regrouper les RUN et nettoyer

```dockerfile
# ❌ 3 couches inutilement séparées
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*

# ✅ 1 seule couche, nettoyée
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
```

Le `rm -rf /var/lib/apt/lists/*` supprime le cache apt — inutile dans l’image finale. Chaque `RUN` crée une couche, et chaque couche ajoute à la taille de l’image.

### Le read-only filesystem

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run mon_app
```

Toute tentative d’écriture sur le filesystem (sauf `/tmp` et `/run`) échoue. C’est une protection forte contre les attaquants qui déposent des fichiers (webshells, outils) après une compromission.

## Bonus

### Hadolint : le linter de Dockerfile

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

Hadolint analyse ton Dockerfile et signale les mauvaises pratiques (utiliser `latest`, ne pas fixer les versions des packages, ne pas nettoyer le cache apt, etc.).

### Le Dockerfile de production type

```dockerfile
# --- Stage 1 : Build ---
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Stage 2 : Production ---
FROM python:3.12-slim
WORKDIR /app

# Créer un utilisateur non-root
RUN useradd --create-home --no-log-init --shell /bin/false appuser

# Copier les dépendances depuis le stage de build
COPY --from=builder /install /usr/local

# Copier le code
COPY --chown=appuser:appuser . .

# Basculer vers l'utilisateur non-root
USER appuser

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

## ✅ Tu sais maintenant…

- Le multi-stage build pour réduire la taille des images
- L’importance de l’utilisateur non-root (`USER` dans le Dockerfile)
- Scanner les images avec Trivy
- Choisir la bonne image de base (slim vs alpine vs distroless)
- Les bonnes pratiques : regrouper les RUN, nettoyer le cache, `.dockerignore`

## 💬 Questions d’entretien typiques

- **Pourquoi ne pas utiliser le tag `latest` en production ?** → Parce que `latest` change à chaque push. Le déploiement n’est plus déterministe — on ne sait pas quelle version tourne réellement. On utilise des tags de version spécifiques.
- **Qu’est-ce qu’un multi-stage build ?** → Une technique Dockerfile qui utilise une première image pour compiler/construire, puis copie uniquement le résultat dans une image finale légère. L’image de production ne contient pas les outils de build.
- **Pourquoi ne pas exécuter en root dans un container ?** → Si un attaquant exploite une faille, il est root dans le container. Avec un user non-root, l’impact est limité. C’est la mesure de sécurité la plus simple et la plus impactante.

-----

# Chapitre 8 — Docker Compose : orchestrer plusieurs containers

## Le minimum à savoir

### Le problème

Au chapitre 5, on a lancé 3 containers avec 3 commandes `docker run` séparées. Chaque commande a une douzaine de flags (-d, -p, -v, -e, –name, –network). C’est ingérable dès que l’application a plus de 2 services. Et si tu dois partager la configuration avec un collègue, il doit retaper les mêmes commandes.

**Docker Compose** résout ça : tu décris toute ta stack dans **un seul fichier YAML**, et tu la lances avec **une seule commande**.

### Le fichier `docker-compose.yml`

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db/medflow
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=medflow

  redis:
    image: redis:7

volumes:
  pgdata:
```

Ce fichier remplace les 3 commandes `docker run` du chapitre 5. Docker Compose crée automatiquement un réseau dédié et y connecte tous les services.

### Les commandes Compose

```bash
# Lancer toute la stack en arrière-plan
docker compose up -d

# Voir l'état des services
docker compose ps

# Voir les logs de tous les services
docker compose logs

# Voir les logs d'un service spécifique
docker compose logs web

# Arrêter et supprimer tout (containers + réseau, mais PAS les volumes)
docker compose down

# Arrêter et supprimer tout Y COMPRIS les volumes (⚠️ données perdues)
docker compose down -v

# Reconstruire les images après un changement de Dockerfile
docker compose build
docker compose up -d --build    # build + relance en une commande
```

> **Note :** la commande est `docker compose` (avec un espace, pas un tiret). L’ancienne syntaxe `docker-compose` (avec un tiret) est dépréciée.

### Décortiquer le fichier

```yaml
services:           # La liste des containers à lancer
  web:              # Nom du service (= nom du container sur le réseau)
    build: .        # Construit l'image depuis le Dockerfile dans le dossier courant
    # OU
    image: nginx:1.25   # Utilise une image existante
    
    ports:
      - "8000:8000"     # Mapping de port hôte:container
    
    volumes:
      - ./code:/app     # Bind mount (développement)
      - data:/var/lib/data   # Volume nommé (persistance)
    
    environment:        # Variables d'environnement
      - DEBUG=true
      - DB_HOST=db
    
    depends_on:         # Ce service démarre après db et redis
      - db
      - redis

volumes:            # Déclaration des volumes nommés
  data:
```

> **`depends_on` :** attention, `depends_on` garantit l’**ordre de démarrage** des containers, mais PAS que le service est prêt. PostgreSQL peut être démarré (le container tourne) mais pas encore prêt à accepter des connexions (le serveur SQL n’a pas fini de s’initialiser). En production, l’application doit gérer les retries de connexion.

> **📋 CONTAINER — Épisode 5 (partie 1)**
> 
> Sami écrit le `docker-compose.yml` de MedFlow : Django (build depuis le Dockerfile) + PostgreSQL (image officielle, volume persistant) + Redis (image officielle, pas de volume) + Celery (même image que Django, commande différente) + Nginx (reverse proxy). Un `docker compose up -d` et toute la stack tourne. Le nouveau développeur qui arrive fait un `git clone` + `docker compose up -d` et a tout l’environnement de développement en 2 minutes.

## Très utile en pratique

### Un Compose complet pour MedFlow

```yaml
services:
  web:
    build: .
    command: gunicorn medflow.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./src:/app
      - static:/app/static
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
      - REDIS_URL=redis://redis:6379
      - SECRET_KEY=dev-secret-key-change-in-prod
    depends_on:
      - db
      - redis

  celery:
    build: .
    command: celery -A medflow worker --loglevel=info
    volumes:
      - ./src:/app
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=medflow
    ports:
      - "127.0.0.1:5432:5432"

  redis:
    image: redis:7-alpine

  nginx:
    image: nginx:1.25
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - static:/app/static:ro
    depends_on:
      - web

volumes:
  pgdata:
  static:
```

### Les fichiers `.env` pour les variables

Au lieu de mettre les variables en clair dans le YAML :

```bash
# Fichier .env (à la racine, à côté de docker-compose.yml)
POSTGRES_PASSWORD=secret
DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
SECRET_KEY=ma-cle-secrete
```

```yaml
# docker-compose.yml
services:
  web:
    build: .
    env_file:
      - .env
```

> **Sécurité :** le fichier `.env` doit être dans le `.gitignore` — ne jamais commiter des secrets dans Git.

### Exécuter des commandes dans un service

```bash
# Ouvrir un shell dans le container web
docker compose exec web bash

# Lancer une migration Django
docker compose exec web python manage.py migrate

# Créer un superuser
docker compose exec web python manage.py createsuperuser
```

## Bonus

### Les profils (pour les services optionnels)

```yaml
services:
  web:
    build: .
    # ...
  
  debug:
    image: busybox
    profiles:
      - debug
    command: sleep infinity
```

```bash
docker compose up -d              # Lance web uniquement
docker compose --profile debug up -d   # Lance web + debug
```

### Health checks dans Compose

```yaml
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
  
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy    # Attend que db soit VRAIMENT prête
```

## ❌ Erreur classique

```yaml
# Oublier de déclarer les volumes nommés
services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
# ❌ Erreur : volume "pgdata" non déclaré
# Il faut ajouter :
volumes:
  pgdata:

# Indentation YAML incorrecte
services:
web:           # ❌ Il manque 2 espaces d'indentation
    image: nginx

services:
  web:         # ✅ Correct
    image: nginx

# Utiliser docker-compose (avec tiret) au lieu de docker compose (avec espace)
docker-compose up    # ⚠️ Ancienne syntaxe, dépréciée
docker compose up    # ✅ Syntaxe actuelle
```

## ✅ Tu sais maintenant…

- Décrire une stack multi-containers dans un fichier `docker-compose.yml`
- Les commandes : `up -d`, `down`, `logs`, `exec`, `build`, `ps`
- Les options clés : `build`, `image`, `ports`, `volumes`, `environment`, `depends_on`
- Utiliser un fichier `.env` pour les variables sensibles

-----

# Chapitre 9 — Registries et gestion des images

## Le minimum à savoir

### Qu’est-ce qu’un registry ?

Un registry est un **entrepôt d’images Docker**. C’est là que les images sont stockées, versionnées et distribuées. Le registry le plus connu est **Docker Hub**, mais en entreprise, on utilise un **registry privé**.

### Pourquoi un registry privé ?

- **Sécurité :** tu contrôles ce qui entre et sort — pas d’images communautaires non vérifiées
- **Confidentialité :** tes images d’application ne sont pas publiques
- **Performance :** pas de pull rate limit, le registry est sur ton réseau
- **Conformité :** certaines réglementations exigent que les artefacts logiciels soient hébergés en interne

### Les options de registries privés

|Registry                               |Type                    |Particularité                                          |
|---------------------------------------|------------------------|-------------------------------------------------------|
|**Docker Hub** (plan payant)           |Cloud public            |Le plus connu, repos privés possibles                  |
|**Harbor**                             |Self-hosted, open source|Scan de vulnérabilités intégré (Trivy), signature, RBAC|
|**GitLab Container Registry**          |Intégré à GitLab        |Gratuit si tu utilises GitLab CI                       |
|**AWS ECR**                            |Cloud AWS               |Intégré à EKS, scan natif                              |
|**Azure ACR**                          |Cloud Azure             |Intégré à AKS                                          |
|**GCP Artifact Registry**              |Cloud GCP               |Intégré à GKE                                          |
|**GitHub Container Registry** (ghcr.io)|Cloud GitHub            |Intégré à GitHub Actions                               |

### Pousser une image vers un registry

```bash
# 1. Se connecter au registry
docker login registry.example.com

# 2. Tagger l'image avec le nom complet du registry
docker tag mon_app:latest registry.example.com/mon_equipe/mon_app:1.0.0

# 3. Pousser
docker push registry.example.com/mon_equipe/mon_app:1.0.0
```

Le format du nom d’une image complète :

```
registry.example.com / mon_equipe / mon_app : 1.0.0
       ↑                   ↑          ↑        ↑
    registry          namespace     image     tag
```

### La stratégie de tags

**Ne jamais utiliser `latest` en production.** Le tag `latest` change à chaque push — tu ne sais pas quelle version tourne.

Stratégies recommandées :

|Stratégie         |Exemple             |Usage               |
|------------------|--------------------|--------------------|
|Version sémantique|`mon_app:1.2.3`     |Releases officielles|
|SHA du commit Git |`mon_app:a3f2b1c`   |Chaque build CI     |
|Date              |`mon_app:2025-04-07`|Builds quotidiens   |


> **À retenir pour un entretien :** “En production, on utilise des tags de version spécifiques, jamais `latest`. Ça garantit que le déploiement est déterministe — on sait exactement quelle version tourne.”

## Très utile en pratique

### La supply chain des images

C’est un sujet de sécurité critique : **d’où viennent tes images ?**

Les risques :

- **Typosquatting :** une image `ngimx` (au lieu de `nginx`) qui contient du code malveillant
- **Image compromise :** une image communautaire légitime dont l’auteur a été compromis ou est malveillant
- **Image obsolète :** une image avec des CVE connues non corrigées

Les protections :

- N’utiliser que des images **officielles** ou **vérifiées** (badge sur Docker Hub)
- Scanner toutes les images avec **Trivy/Grype** avant déploiement
- Utiliser un **registry privé** qui met en cache les images officielles
- **Signer** les images avec **Cosign** (projet Sigstore) et vérifier les signatures avant déploiement

### Cosign : signer et vérifier les images

```bash
# Installer cosign
# (voir https://docs.sigstore.dev/cosign/installation/)

# Signer une image
cosign sign registry.example.com/mon_app:1.0.0

# Vérifier la signature
cosign verify registry.example.com/mon_app:1.0.0
```

En combinant signature + admission controller K8s (voir chapitre 22), tu peux empêcher le déploiement de toute image non signée.

## Bonus

### Le SBOM (Software Bill of Materials)

Un SBOM est l’**inventaire complet** de tous les composants logiciels d’une image (packages système, bibliothèques, dépendances). C’est l’équivalent d’une liste d’ingrédients pour une image Docker.

```bash
# Générer un SBOM avec Syft
syft mon_app:latest

# Docker a un SBOM intégré
docker sbom mon_app:latest
```

Quand une CVE critique est annoncée (type Log4Shell), le SBOM te permet de savoir instantanément quels containers sont affectés.

## ✅ Tu sais maintenant…

- Ce qu’est un registry et pourquoi utiliser un registry privé
- Pousser une image vers un registry (`tag` + `push`)
- La stratégie de tags (jamais `latest` en production)
- Les risques de supply chain des images et les protections (scan, signature, SBOM)

-----

# Chapitre 10 — Capstone Partie II : containeriser une application complète

Cet exercice intègre tout ce que tu as appris dans les chapitres 6 à 9.

## L’exercice

**Objectif :** containeriser une application web multi-composants et la déployer avec Docker Compose.

**L’application :** un blog simple avec :

- Un **backend** Python/Flask (ou Django) qui sert l’API
- Une **base de données** PostgreSQL
- Un **cache** Redis
- Un **reverse proxy** Nginx

**Les étapes :**

1. **Écrire le Dockerfile** pour le backend :
- Image de base `slim`
- Multi-stage build
- Utilisateur non-root
- `.dockerignore` complet
1. **Écrire le `docker-compose.yml`** :
- 4 services (backend, db, redis, nginx)
- Volume persistant pour PostgreSQL
- Bind mount pour le code source (développement)
- Fichier `.env` pour les variables sensibles
- Réseau nommé
- Health check sur PostgreSQL
1. **Scanner l’image** avec Trivy
1. **Documenter** : un `README.md` avec les instructions de démarrage

**Checklist de validation :**

|Critère                                                           |Vérifié ?|
|------------------------------------------------------------------|---------|
|L’image backend fait moins de 200 Mo                              |         |
|Le scan Trivy ne montre aucune CVE critique                       |         |
|L’application tourne avec un utilisateur non-root                 |         |
|Les données PostgreSQL survivent à un `docker compose down` + `up`|         |
|Les secrets ne sont pas dans le Dockerfile ni dans le YAML        |         |
|Le `.dockerignore` exclut `.git`, `.env`, `__pycache__`           |         |
|`docker compose up -d` lance tout en une commande                 |         |
|L’application est accessible sur `http://localhost`               |         |


> **📋 CONTAINER — Épisode 5 (partie 2)**
> 
> Sami livre la stack Docker Compose de MedFlow. Résultat : image de production 180 Mo (vs 1.2 Go au départ), scan Trivy propre, utilisateur non-root, secrets dans un `.env` hors du repo Git. Le nouveau développeur qui rejoint l’équipe clone le repo et fait `docker compose up -d` — tout l’environnement de développement est prêt en 2 minutes. Le CTO est convaincu. Prochaine étape : Kubernetes pour la production.

## ✅ Tu sais maintenant…

- Containeriser une application multi-composants de A à Z
- Appliquer les bonnes pratiques : multi-stage, non-root, scan, secrets externalisés
- Documenter pour que n’importe qui puisse lancer la stack

-----

# PARTIE III — KUBERNETES : LES FONDAMENTAUX

-----

# Chapitre 11 — Pourquoi Kubernetes : quand Docker ne suffit plus

## Le minimum à savoir

### Les limites de Docker seul

Docker Compose est parfait pour le développement et les petits déploiements. Mais imagine que ton application doit :

- Tourner sur **plusieurs serveurs** (pas un seul)
- **Résister à la panne** d’un serveur (si un serveur tombe, l’application continue)
- **Scaler automatiquement** (ajouter des instances quand il y a plus de trafic, en retirer quand le trafic baisse)
- Se **mettre à jour sans interruption** (rolling update — les utilisateurs ne voient pas la mise à jour)
- **Redémarrer automatiquement** un container qui plante (self-healing)

Docker Compose ne sait pas faire ça. Il gère des containers sur **une seule machine**. Pour gérer des containers sur **plusieurs machines**, il faut un **orchestrateur**. Et l’orchestrateur dominant, c’est **Kubernetes**.

### Kubernetes en une phrase

Kubernetes (souvent abrégé **K8s** — K + 8 lettres + s) est un système qui **gère automatiquement le déploiement, le scaling et le cycle de vie de containers sur un ensemble de serveurs**.

Tu lui dis “je veux 3 instances de mon application web, toujours disponibles”, et Kubernetes s’assure que c’est le cas : il les répartit sur les serveurs disponibles, les redémarre si elles plantent, en ajoute si tu augmentes le nombre, et les met à jour sans interruption.

### Le paradigme déclaratif

C’est le concept fondamental de Kubernetes :

- **Impératif** (Docker) : tu dis “lance ce container sur ce serveur avec ces options” — tu décris les **actions**
- **Déclaratif** (Kubernetes) : tu dis “je veux 3 instances de cette application, accessibles sur le port 80” — tu décris l’**état désiré**, et K8s se débrouille pour l’atteindre et le maintenir

```
TOI : "Je veux 3 replicas de mon_app"
         │
         ▼
KUBERNETES : vérifie en permanence
         │
    ┌────┴────┐
    │ 3 pods  │  ← État actuel = état désiré → tout va bien
    │ tournent│
    └─────────┘
         │
    Un pod plante
         │
    ┌────┴────┐
    │ 2 pods  │  ← État actuel ≠ état désiré → K8s relance un pod
    │ tournent│
    └────┬────┘
         │
    K8s crée un nouveau pod
         │
    ┌────┴────┐
    │ 3 pods  │  ← État restauré
    │ tournent│
    └─────────┘
```

> **À retenir pour un entretien :** “Kubernetes fonctionne sur un modèle déclaratif : on décrit l’état désiré dans des fichiers YAML, et Kubernetes travaille en permanence pour atteindre et maintenir cet état. Si un container plante, K8s le relance. Si un serveur tombe, K8s redéploie les containers sur les serveurs restants.”

### Les options pour utiliser Kubernetes

|Option                         |Complexité |Usage                                            |
|-------------------------------|-----------|-------------------------------------------------|
|**minikube**                   |Très simple|Apprendre et tester sur son laptop               |
|**kind** (Kubernetes in Docker)|Simple     |CI/CD, tests automatisés                         |
|**k3s**                        |Légère     |Edge computing, Raspberry Pi, petits déploiements|
|**EKS** (AWS)                  |Managée    |Production sur AWS                               |
|**AKS** (Azure)                |Managée    |Production sur Azure                             |
|**GKE** (Google Cloud)         |Managée    |Production sur GCP                               |
|**K8s vanilla** (auto-hébergé) |Complexe   |Quand tu veux tout contrôler (rare)              |


> **Pour ce cours :** installe **minikube** pour suivre les exercices. C’est un cluster K8s complet qui tourne sur ton laptop.

```bash
# Installer minikube (Linux)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Démarrer le cluster
minikube start

# Vérifier
kubectl get nodes
```

### Kubernetes n’est pas toujours la réponse

Kubernetes ajoute une **complexité opérationnelle significative**. Pour une petite application avec peu de trafic et une petite équipe, Docker Compose sur un seul serveur est souvent suffisant et beaucoup plus simple.

Kubernetes se justifie quand tu as besoin de :

- Haute disponibilité (l’application ne doit jamais tomber)
- Scaling automatique (le trafic varie)
- Déploiements sans interruption (rolling updates)
- Multi-services avec des équipes différentes (chacune déploie indépendamment)

> **📋 CONTAINER — Épisode 5 (partie 3)**
> 
> Le CTO de MedFlow veut passer en production. Docker Compose sur un seul serveur n’est pas suffisant : l’application doit être hautement disponible (données de santé), scaler pendant les pics d’utilisation (9h-12h), et se mettre à jour sans interruption. La décision est prise : EKS (Kubernetes managé sur AWS). Sami installe minikube pour prototyper la migration avant de passer sur EKS.

## Très utile en pratique

### kubectl : l’outil de base

`kubectl` est la commande pour interagir avec un cluster Kubernetes. C’est l’équivalent de `docker` pour Docker.

```bash
# Installer kubectl
# Voir : https://kubernetes.io/docs/tasks/tools/

# Vérifier la connexion au cluster
kubectl cluster-info

# Voir les nœuds du cluster
kubectl get nodes
```

On utilisera `kubectl` en détail au chapitre 14.

### Kubernetes managé vs auto-hébergé

En entreprise, la quasi-totalité des déploiements Kubernetes sont **managés** (EKS, AKS, GKE). Le cloud provider gère le Control Plane (API Server, etcd, Scheduler…) — tu ne gères que tes applications et la configuration. Héberger et maintenir son propre cluster K8s (vanilla) est complexe et réservé aux équipes avec une forte expertise.

## ✅ Tu sais maintenant…

- Pourquoi Kubernetes existe (les limites de Docker seul)
- Le paradigme déclaratif (état désiré vs état actuel)
- Les options pour utiliser K8s (minikube pour apprendre, managé pour la production)
- Que Kubernetes n’est pas toujours nécessaire (Docker Compose suffit souvent)

-----

# Chapitre 12 — Architecture Kubernetes : les composants du cluster

## Le minimum à savoir

### Le cluster : la vue d’ensemble

Un cluster Kubernetes est composé de deux types de machines :

- Le **Control Plane** (plan de contrôle) : le “cerveau” qui gère le cluster
- Les **Worker Nodes** (nœuds de travail) : les machines qui font tourner les containers

```
┌─────────────────────────────────────────────────┐
│                CONTROL PLANE                     │
│                                                  │
│  ┌──────────┐ ┌──────┐ ┌───────────┐ ┌────────┐│
│  │API Server│ │ etcd │ │ Scheduler │ │Ctrl Mgr││
│  └──────────┘ └──────┘ └───────────┘ └────────┘│
└─────────────────────┬───────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────┴───┐  ┌──────┴────┐  ┌────┴──────┐
│  Node 1   │  │  Node 2   │  │  Node 3   │
│ ┌───────┐ │  │ ┌───────┐ │  │ ┌───────┐ │
│ │kubelet│ │  │ │kubelet│ │  │ │kubelet│ │
│ │Pod Pod│ │  │ │Pod Pod│ │  │ │Pod    │ │
│ │Pod    │ │  │ │Pod    │ │  │ │Pod Pod│ │
│ └───────┘ │  │ └───────┘ │  │ └───────┘ │
└───────────┘  └───────────┘  └───────────┘
    WORKER NODES
```

### Les composants du Control Plane

|Composant             |Rôle                                                           |Analogie simple                                         |
|----------------------|---------------------------------------------------------------|--------------------------------------------------------|
|**API Server**        |Le point d’entrée unique — toutes les commandes passent par lui|La réception d’un hôtel : tout le monde passe par là    |
|**etcd**              |La base de données du cluster — stocke tout l’état             |Le registre de l’hôtel : qui est dans quelle chambre    |
|**Scheduler**         |Décide sur quel nœud placer chaque pod                         |Le concierge qui attribue les chambres                  |
|**Controller Manager**|Vérifie que l’état actuel correspond à l’état désiré           |Le responsable qualité qui vérifie que tout est en ordre|


> **Point critique :** tout passe par l’**API Server**. Quand tu tapes `kubectl get pods`, ta commande va à l’API Server. Quand le Scheduler place un pod, il parle à l’API Server. Quand un kubelet signale l’état d’un pod, il parle à l’API Server. **Contrôler l’accès à l’API Server, c’est contrôler le cluster** (voir chapitre 25 sur la sécurité).

> **Point critique :** **etcd** contient l’intégralité de l’état du cluster, y compris les Secrets. Si etcd est compromis, tout le cluster est compromis. En production, etcd doit être chiffré, sauvegardé, et accessible uniquement au Control Plane.

### Les composants des Worker Nodes

|Composant            |Rôle                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------|
|**kubelet**          |L’agent sur chaque nœud — reçoit les instructions de l’API Server et gère les containers localement|
|**kube-proxy**       |Gère le réseau — route le trafic vers les bons pods                                                |
|**Container runtime**|Exécute les containers (containerd)                                                                |

### Le flux simplifié

```
1. Tu écris un manifest YAML qui dit "je veux 3 replicas de mon_app"
2. Tu tapes : kubectl apply -f manifest.yaml
3. kubectl envoie le manifest à l'API Server
4. L'API Server stocke l'état désiré dans etcd
5. Le Controller Manager détecte : "l'état désiré dit 3 pods, l'état actuel dit 0"
6. Le Scheduler choisit sur quels nœuds placer les 3 pods
7. Les kubelets des nœuds choisis créent les containers
8. Le Controller Manager vérifie en continu que 3 pods tournent
```

## Très utile en pratique

### Kubernetes managé : ce que le cloud gère pour toi

Avec EKS, AKS ou GKE, le **Control Plane est géré par le cloud provider**. Tu ne vois pas les machines qui font tourner l’API Server, etcd, le Scheduler. Tu ne les maintiens pas, tu ne les patches pas. Tu ne gères que les Worker Nodes (et même ceux-là peuvent être managés avec des node pools auto-scalés).

C’est un avantage énorme : maintenir un Control Plane K8s est un travail à plein temps. Avec un service managé, tu te concentres sur tes applications.

### Inspecter le cluster

```bash
# Voir les nœuds
kubectl get nodes

# Voir les composants du Control Plane
kubectl get componentstatuses    # ou kubectl get cs

# Voir tout dans tous les namespaces
kubectl get all --all-namespaces
```

## Bonus

### La haute disponibilité du Control Plane

En production, le Control Plane doit être en haute disponibilité : **3 nœuds etcd minimum** (consensus par Raft), **API Server répliqué** derrière un load balancer. Les services managés (EKS, AKS, GKE) gèrent ça automatiquement — c’est l’un des avantages principaux.

## ✅ Tu sais maintenant…

- L’architecture Control Plane + Worker Nodes
- Le rôle de chaque composant (API Server, etcd, Scheduler, Controller Manager, kubelet)
- Que tout passe par l’API Server (implications en sécurité)
- Que etcd est la base de données la plus critique du cluster
- La différence entre K8s auto-hébergé et managé

-----

# Chapitre 13 — Les objets Kubernetes essentiels

## Le minimum à savoir

### Le Pod

Le **Pod** est la plus petite unité déployable dans Kubernetes. Un Pod contient **un ou plusieurs containers** qui partagent le même réseau et le même stockage.

En pratique, un Pod contient presque toujours **un seul container**. Les cas multi-containers (sidecar pattern) sont avancés.

```yaml
# Un Pod simple (on ne déploie presque jamais un Pod seul en production)
apiVersion: v1
kind: Pod
metadata:
  name: mon-pod
spec:
  containers:
  - name: mon-app
    image: nginx:1.25
    ports:
    - containerPort: 80
```

> **Règle :** on ne déploie presque **jamais** un Pod directement. On utilise un **Deployment** qui gère les Pods pour nous (scaling, updates, self-healing). Le Pod seul est utile pour comprendre le concept, pas pour la production.

### Le Deployment

Le **Deployment** est l’objet qu’on utilise pour déployer une application. Il gère un ensemble de Pods identiques (les **replicas**) et s’assure qu’ils sont toujours au nombre demandé.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3          # Je veux 3 instances de mon application
  selector:
    matchLabels:
      app: web         # Ce Deployment gère les Pods avec le label "app: web"
  template:
    metadata:
      labels:
        app: web       # Les Pods créés auront ce label
    spec:
      containers:
      - name: web
        image: mon_app:1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:            # Ressources minimales demandées
            memory: "128Mi"
            cpu: "100m"
          limits:              # Ressources maximales autorisées
            memory: "256Mi"
            cpu: "500m"
```

Le Deployment crée automatiquement un **ReplicaSet** (qui gère les replicas) qui crée les **Pods**. La chaîne est : Deployment → ReplicaSet → Pods.

> **À retenir pour un entretien :** “Un Deployment gère le cycle de vie d’un groupe de Pods identiques. Si un Pod plante, le Deployment en recrée un. Pour une mise à jour, le Deployment fait un rolling update : il crée les nouveaux Pods un par un et supprime les anciens progressivement, sans interruption de service.”

### Le Service

Les Pods sont **éphémères** : ils peuvent être recréés avec une adresse IP différente à tout moment (crash, mise à jour, scaling). Le **Service** donne une **adresse stable** à un groupe de Pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web           # Ce Service cible les Pods avec le label "app: web"
  ports:
  - port: 80           # Le port du Service
    targetPort: 8000   # Le port du container dans le Pod
  type: ClusterIP      # Accessible uniquement à l'intérieur du cluster
```

Les types de Service :

|Type            |Accessible depuis                                  |Usage                       |
|----------------|---------------------------------------------------|----------------------------|
|**ClusterIP**   |Intérieur du cluster uniquement                    |Communication entre services|
|**NodePort**    |Extérieur via un port sur chaque nœud (30000-32767)|Tests, petits déploiements  |
|**LoadBalancer**|Extérieur via un load balancer cloud               |Production (EKS, AKS, GKE)  |

Le service discovery fonctionne par **DNS** : dans le cluster, `web-service` résout automatiquement vers les Pods avec le label `app: web`. Comme le réseau Docker nommé, mais à l’échelle du cluster.

### Le Namespace

Un **Namespace** est un espace logique qui sépare les ressources dans le cluster. C’est comme des dossiers sur ton ordinateur.

```bash
kubectl get namespaces
# NAME              STATUS   AGE
# default           Active   1d
# kube-system       Active   1d    ← les composants internes de K8s
# kube-public       Active   1d
```

```bash
# Créer un namespace
kubectl create namespace staging

# Déployer dans un namespace
kubectl apply -f deployment.yaml -n staging

# Voir les ressources d'un namespace
kubectl get pods -n staging
```

Usages : séparer les environnements (dev, staging, prod), séparer les équipes, appliquer des quotas de ressources par namespace.

> **Point important :** un Namespace n’est **pas** une frontière de sécurité en soi. Sans Network Policies (chapitre 24), les Pods de namespaces différents peuvent communiquer entre eux.

### ConfigMap et Secret

**ConfigMap** : stocker de la configuration non sensible (URLs, paramètres, fichiers de configuration).

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "db-service"
  LOG_LEVEL: "info"
```

**Secret** : stocker des données sensibles (mots de passe, clés API, certificats).

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  DATABASE_PASSWORD: c2VjcmV0    # ← "secret" encodé en base64
```

> **⚠️ Piège fondamental :** les Secrets Kubernetes sont encodés en **base64**, PAS chiffrés. `echo "c2VjcmV0" | base64 -d` donne “secret” en clair. Toute identité disposant des droits RBAC adéquats (ou tout accès à etcd insuffisamment protégé) peut les lire. En production, il faut chiffrer etcd au repos et/ou utiliser un gestionnaire de secrets externe (HashiCorp Vault, AWS Secrets Manager). On verra ça au chapitre 25.

> **À retenir pour un entretien :** “Les Secrets Kubernetes sont en base64, pas chiffrés. C’est une fausse sécurité. En production, il faut du chiffrement au repos (encryption at rest dans etcd) et idéalement un vault externe.”

## Très utile en pratique

### Les labels et sélecteurs : le mécanisme de liaison

Les **labels** sont des paires clé-valeur attachées aux objets. Les **sélecteurs** permettent de sélectionner des objets par leurs labels. C’est le mécanisme qui lie un Service à ses Pods, un Deployment à ses Pods, etc.

```yaml
# Le Deployment crée des Pods avec le label app: web
# Le Service sélectionne les Pods avec le label app: web
# → Le Service route le trafic vers les bons Pods
```

Si les labels ne correspondent pas entre le Deployment, les Pods et le Service, rien ne fonctionne. C’est la cause n°1 de troubleshooting en K8s pour les débutants.

### Utiliser les ConfigMaps et Secrets dans un Pod

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: mon_app:1.0.0
        envFrom:
        - configMapRef:
            name: app-config      # Toutes les clés du ConfigMap deviennent des variables d'env
        - secretRef:
            name: app-secrets     # Toutes les clés du Secret deviennent des variables d'env
```

## ✅ Tu sais maintenant…

- Le Pod (unité de base, rarement utilisé seul)
- Le Deployment (gère les Pods : replicas, rolling updates, self-healing)
- Le Service (donne une adresse stable à un groupe de Pods)
- Le Namespace (séparation logique, pas une frontière de sécurité en soi)
- Les ConfigMaps et Secrets (configuration et données sensibles — Secrets en base64, pas chiffrés !)
- Les labels et sélecteurs (le mécanisme qui lie tout ensemble)

## 💬 Questions d’entretien typiques

- **Pourquoi un Service est-il nécessaire si les Pods existent déjà ?** → Les Pods sont éphémères et changent d’adresse IP à chaque recréation. Le Service fournit une adresse stable et un nom DNS qui pointe toujours vers les bons Pods, via le mécanisme de labels/sélecteurs.
- **Quelle est la différence entre un Deployment et un Pod ?** → On ne déploie pas de Pods seuls en production. Un Deployment gère un groupe de Pods identiques : il assure le nombre de replicas demandé, redémarre les Pods qui plantent, et gère les mises à jour sans interruption (rolling update).
- **Les Secrets Kubernetes sont-ils sécurisés ?** → Non par défaut. Ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC appropriés peut les lire. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe.

-----

# Chapitre 14 — Déployer sur Kubernetes : kubectl et les manifests

## Le minimum à savoir

### Les commandes kubectl essentielles

```bash
# --- LECTURE ---
kubectl get pods                     # Lister les Pods
kubectl get deployments              # Lister les Deployments
kubectl get services                 # Lister les Services
kubectl get all                      # Tout lister

# --- DÉTAILS ---
kubectl describe pod mon-pod         # Détails complets d'un Pod (événements, état, erreurs)
kubectl logs mon-pod                 # Logs du container dans le Pod
kubectl logs -f mon-pod              # Logs en temps réel (follow)

# --- INTERACTION ---
kubectl exec -it mon-pod -- bash     # Shell dans le container
kubectl port-forward mon-pod 8080:80 # Accès local au port 80 du Pod

# --- DÉPLOIEMENT ---
kubectl apply -f manifest.yaml       # Appliquer un manifest (créer ou mettre à jour)
kubectl delete -f manifest.yaml      # Supprimer les ressources décrites dans le manifest

# --- SCALING ---
kubectl scale deployment web --replicas=5   # Passer à 5 instances
```

### Déployer pas à pas

**1. Crée le manifest du Deployment** (`deployment.yaml`) :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:1.25
        ports:
        - containerPort: 80
```

**2. Crée le manifest du Service** (`service.yaml`) :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
  type: NodePort
```

**3. Applique les manifests :**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

**4. Vérifie :**

```bash
kubectl get pods              # 3 pods en Running
kubectl get services          # Le service avec son NodePort
kubectl describe deployment web   # Détails du Deployment
```

**5. Teste :**

```bash
# Avec minikube
minikube service web-service --url
# Ouvre l'URL dans ton navigateur
```

### Le rolling update

Pour mettre à jour l’application, modifie l’image dans le manifest et réapplique :

```bash
# Modifier l'image dans deployment.yaml : image: nginx:1.26
kubectl apply -f deployment.yaml

# Observer le rolling update en temps réel
kubectl rollout status deployment web

# Historique des déploiements
kubectl rollout history deployment web

# Revenir en arrière (rollback)
kubectl rollout undo deployment web
```

Kubernetes crée les nouveaux Pods un par un et supprime les anciens progressivement. À aucun moment l’application n’est indisponible.

> **📋 CONTAINER — Épisode 6**
> 
> Sami déploie la stack MedFlow sur minikube. Django tourne dans un Deployment (3 replicas), PostgreSQL dans un StatefulSet avec PVC (on verra ça au chapitre 15), Redis dans un Deployment. Un Service de type ClusterIP expose chaque composant en interne. Il fait un rolling update de Django en changeant la version de l’image — les 3 pods sont remplacés un par un sans interruption.

## Très utile en pratique

### Mettre plusieurs objets dans un seul fichier

Tu peux séparer les manifests par `---` dans un seul fichier :

```yaml
# stack.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  # ...
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  # ...
```

```bash
kubectl apply -f stack.yaml    # Applique tous les objets d'un coup
```

### Dry run : tester sans appliquer

```bash
kubectl apply -f manifest.yaml --dry-run=client   # Vérifie la syntaxe sans rien créer
kubectl diff -f manifest.yaml                       # Montre ce qui changerait
```

## Bonus

### Helm et Kustomize : gérer les manifests dans la vraie vie

En production, personne ne gère des dizaines de fichiers YAML à la main. Deux outils dominent :

**Helm** est un “gestionnaire de packages” pour Kubernetes. Il regroupe tous les manifests d’une application dans un **chart** (un package) avec des variables personnalisables. Au lieu de modifier les YAML un par un, tu changes les variables dans un fichier `values.yaml`.

```bash
# Installer une application avec Helm
helm install mon-app bitnami/postgresql --set auth.postgresPassword=secret

# Lister les installations
helm list

# Mettre à jour
helm upgrade mon-app bitnami/postgresql --set auth.postgresPassword=newsecret
```

**Kustomize** est une approche plus légère : tu gardes tes manifests YAML standards et tu crées des **overlays** (surcouches) pour chaque environnement (dev, staging, prod) sans dupliquer les fichiers.

```bash
# Appliquer avec un overlay
kubectl apply -k overlays/production/
```

Tu n’as pas besoin de maîtriser ces outils pour débuter, mais sache qu’ils existent : dans un vrai environnement K8s, tu les rencontreras systématiquement.

## ❌ Erreur classique

```bash
# Labels qui ne correspondent pas entre Deployment et Service
# → Le Service ne trouve pas les Pods → pas de trafic routé
# Vérifier : kubectl describe service web-service → Endpoints doit montrer des IPs

# Oublier le containerPort
# → Le Pod tourne mais le trafic n'arrive pas

# Confondre kubectl apply et kubectl create
kubectl create -f manifest.yaml    # Crée — échoue si ça existe déjà
kubectl apply -f manifest.yaml     # Crée OU met à jour — idempotent ← Préfère celui-ci
```

## ✅ Tu sais maintenant…

- Les commandes kubectl essentielles (get, describe, logs, exec, apply, delete)
- Écrire et appliquer des manifests YAML
- Le rolling update et le rollback
- Le port-forward pour tester localement

-----

# Chapitre 15 — Stockage, Ingress et configuration avancée

## Le minimum à savoir

### Le stockage persistant

Les Pods sont éphémères — comme les containers Docker. Pour les données qui doivent persister (bases de données), Kubernetes utilise un système de stockage en 3 couches :

- **PersistentVolume (PV)** : un espace de stockage provisionné (un disque EBS sur AWS, un disque Azure, un partage NFS)
- **PersistentVolumeClaim (PVC)** : une “demande” de stockage faite par un Pod (“je veux 10 Go de stockage”)
- **StorageClass** : le type de stockage disponible (SSD rapide, HDD pas cher, etc.)

```yaml
# PVC : le Pod demande du stockage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data
spec:
  accessModes:
    - ReadWriteOnce       # Un seul Pod peut écrire à la fois
  resources:
    requests:
      storage: 10Gi       # 10 Go demandés
```

Le PVC est ensuite monté dans le Pod :

```yaml
spec:
  containers:
  - name: db
    image: postgres:16
    volumeMounts:
    - name: data
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: db-data
```

### Le StatefulSet (pour les bases de données)

Le **StatefulSet** est l’objet K8s conçu pour les applications avec état (bases de données, systèmes distribués). Contrairement au Deployment :

- Chaque Pod a un **nom stable** (db-0, db-1, db-2 au lieu de noms aléatoires)
- Chaque Pod a son **propre volume persistant**
- Les Pods sont créés et supprimés **dans l’ordre** (important pour les réplications)

### L’Ingress : exposer à l’extérieur

Un Service de type `ClusterIP` n’est accessible que depuis l’intérieur du cluster. Pour exposer une application sur Internet avec un nom de domaine et du HTTPS, on utilise un **Ingress** :

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: app.medflow.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
  tls:
  - hosts:
    - app.medflow.com
    secretName: tls-cert       # Certificat TLS dans un Secret
```

L’Ingress a besoin d’un **Ingress Controller** installé dans le cluster (nginx-ingress, traefik, HAProxy). C’est le composant qui lit les règles Ingress et configure le reverse proxy.

### Les probes : le self-healing en action

Les probes sont des vérifications automatiques de santé :

```yaml
spec:
  containers:
  - name: web
    image: mon_app:1.0.0
    livenessProbe:              # Le container est-il vivant ?
      httpGet:
        path: /health
        port: 8000
      periodSeconds: 10
    readinessProbe:             # Le container est-il prêt à recevoir du trafic ?
      httpGet:
        path: /ready
        port: 8000
      initialDelaySeconds: 5
```

|Probe        |Question                                |Si elle échoue                                     |
|-------------|----------------------------------------|---------------------------------------------------|
|**Liveness** |“Le container est-il vivant ?”          |K8s le **redémarre**                               |
|**Readiness**|“Le container est-il prêt ?”            |K8s **retire** le Pod du Service (plus de trafic)  |
|**Startup**  |“Le container a-t-il fini de démarrer ?”|K8s **attend** avant de vérifier liveness/readiness|

### Resource requests et limits

```yaml
resources:
  requests:          # "Je voudrais au minimum..."
    memory: "128Mi"
    cpu: "100m"      # 100 millicores = 0.1 CPU
  limits:            # "Je ne dois pas dépasser..."
    memory: "256Mi"
    cpu: "500m"      # 500 millicores = 0.5 CPU
```

- **Requests** : ce que le Scheduler utilise pour décider sur quel nœud placer le Pod. Si le nœud n’a pas assez de ressources “disponibles” (en requests), le Pod n’y sera pas placé.
- **Limits** : le maximum que le container peut consommer. Si le container dépasse la limite mémoire → **OOMKilled**. S’il dépasse la limite CPU → **throttling** (ralentissement).

> **Bonne pratique :** mets toujours des requests et des limits. Sans limits, un container peut consommer toutes les ressources du nœud et impacter les autres Pods.

## ✅ Tu sais maintenant…

- Le stockage persistant (PV, PVC, StorageClass)
- Le StatefulSet pour les applications avec état
- L’Ingress pour exposer des applications sur Internet
- Les probes pour le self-healing (liveness, readiness, startup)
- Les resource requests et limits

-----

# Chapitre 16 — Capstone Partie III : déployer une application sur Kubernetes

## L’exercice

**Objectif :** déployer la stack MedFlow sur un cluster Kubernetes de lab (minikube/kind).

**Les composants :**

1. **Django** : Deployment (3 replicas) + Service ClusterIP + probes liveness/readiness
1. **PostgreSQL** : StatefulSet + PVC (10 Gi) + Service ClusterIP
1. **Redis** : Deployment (1 replica) + Service ClusterIP
1. **Ingress** : expose Django sur un hostname local

**Les étapes :**

1. Écrire les manifests YAML pour chaque composant
1. Créer un ConfigMap pour les variables non sensibles
1. Créer un Secret pour le mot de passe de la base de données
1. Déployer avec `kubectl apply -f`
1. Vérifier que tout tourne (`kubectl get all`, `kubectl logs`)
1. Simuler un crash : `kubectl delete pod` → observer le self-healing
1. Faire un rolling update en changeant la version de l’image
1. Faire un rollback

**Checklist :**

|Critère                                             |Vérifié ?|
|----------------------------------------------------|---------|
|3 replicas Django tournent                          |         |
|PostgreSQL a un volume persistant                   |         |
|Les probes liveness/readiness sont configurées      |         |
|Les resource requests et limits sont définies       |         |
|Les secrets ne sont pas en clair dans les manifests |         |
|Le self-healing fonctionne (delete pod → recréation)|         |
|Le rolling update fonctionne sans interruption      |         |

## ✅ Tu sais maintenant…

- Déployer une application multi-composants sur Kubernetes
- Combiner Deployment, Service, ConfigMap, Secret, PVC, Ingress
- Vérifier, diagnostiquer et mettre à jour un déploiement K8s

-----

# PARTIE IV — OPÉRATIONS ET CYCLE DE VIE

-----

# Chapitre 17 — CI/CD et containers : du code au déploiement

## Le minimum à savoir

### Le pipeline containerisé

En production, personne ne fait `docker build` et `kubectl apply` manuellement. Un **pipeline CI/CD** automatise tout le processus :

```
Code pushé   →   Build de    →   Scan de     →   Push au    →   Déploiement
sur Git          l'image         sécurité        registry       sur K8s
```

Chaque étape est automatisée. Si le scan de sécurité trouve une CVE critique, le pipeline s’arrête et le déploiement n’a pas lieu.

### Les outils CI/CD courants

|Outil             |Particularité                                 |
|------------------|----------------------------------------------|
|**GitHub Actions**|Intégré à GitHub, gratuit pour l’open source  |
|**GitLab CI**     |Intégré à GitLab, très populaire en entreprise|
|**Jenkins**       |Le vétéran, auto-hébergé, très configurable   |

### Exemple de pipeline GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - scan
  - deploy

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

scan:
  stage: scan
  script:
    - trivy image --exit-code 1 --severity CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy:
  stage: deploy
  script:
    - kubectl set image deployment/web web=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main
```

### Les secrets dans la CI/CD

> **⚠️ Piège majeur :** ne JAMAIS mettre de secrets (mots de passe, clés API, tokens) en clair dans les fichiers de pipeline, les Dockerfiles, ou les variables d’environnement du dépôt Git.

Les solutions :

- Variables protégées de la CI (GitLab CI Protected Variables, GitHub Secrets)
- Vault externe (HashiCorp Vault, AWS Secrets Manager)
- OIDC pour l’authentification au registry (pas de mot de passe stocké)

## Bonus

### GitOps : Git comme source de vérité

Le principe GitOps : l’état du cluster Kubernetes est décrit dans un repo Git. Un outil (**ArgoCD**, **Flux**) surveille ce repo et synchronise automatiquement le cluster avec ce qui est décrit dans Git. Pour déployer, tu fais un commit dans Git — l’outil applique les changements.

Avantages : audit trail complet (chaque déploiement est un commit), rollback par revert Git, review des changements de configuration par merge request. C’est le modèle vers lequel la plupart des organisations matures convergent, mais il n’est pas indispensable pour commencer.

### Les stratégies de déploiement avancées

|Stratégie                      |Comment                                    |Avantage                  |Inconvénient                           |
|-------------------------------|-------------------------------------------|--------------------------|---------------------------------------|
|**Rolling update** (défaut K8s)|Remplacement progressif des Pods           |Pas d’interruption        |Les deux versions coexistent brièvement|
|**Blue/Green**                 |Deux environnements complets, bascule      |Rollback instantané       |Double les ressources                  |
|**Canary**                     |Nouvelle version sur un % du trafic d’abord|Teste en production réelle|Plus complexe à configurer             |

## ✅ Tu sais maintenant…

- Le pipeline CI/CD containerisé (build → scan → push → deploy)
- Les secrets dans la CI/CD (jamais en clair)
- Le concept de GitOps (Git comme source de vérité)
- Les stratégies de déploiement (rolling, blue/green, canary)

-----

# Chapitre 18 — Monitoring, logs et observabilité

## Le minimum à savoir

### Pourquoi centraliser les logs

Les containers sont éphémères. Quand un Pod est supprimé ou recréé, ses logs disparaissent. Sans centralisation, tu ne peux pas diagnostiquer un problème survenu il y a 30 minutes si le Pod a été recréé depuis.

**Convention containers :** les applications doivent logger sur **stdout/stderr** (pas dans des fichiers). Docker et Kubernetes captent automatiquement stdout/stderr.

```bash
# Voir les logs d'un Pod
kubectl logs mon-pod
kubectl logs -f mon-pod              # En temps réel
kubectl logs mon-pod --previous      # Logs de l'instance précédente (après un crash)
```

### La stack de monitoring standard

Le standard de facto pour le monitoring Kubernetes :

- **Prometheus** : collecte les métriques (CPU, mémoire, latence, erreurs, métriques custom)
- **Grafana** : affiche les métriques dans des dashboards visuels
- **Loki** (ou EFK) : centralise les logs
- **AlertManager** : envoie des alertes (email, Slack, PagerDuty) quand un seuil est dépassé

### Les métriques à surveiller

|Métrique                 |Pourquoi                                 |
|-------------------------|-----------------------------------------|
|CPU par Pod              |Détecter les surcharges                  |
|Mémoire par Pod          |Prévenir les OOMKilled                   |
|Nombre de Pods ready     |Vérifier que l’application est disponible|
|Taux d’erreurs HTTP (5xx)|Détecter les problèmes applicatifs       |
|Latence (p50, p95, p99)  |Détecter les ralentissements             |
|Restarts de Pods         |Détecter les crashs en boucle            |

### Les outils du quotidien

```bash
# Voir les ressources consommées par les Pods
kubectl top pods
kubectl top nodes

# Le dashboard Kubernetes (interface web)
kubectl proxy
# → http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

# k9s — le terminal interactif pour K8s (très recommandé)
# Installer : https://k9scli.io/
k9s
```

> **⚠️ Sécurité :** le Kubernetes Dashboard exposé sans authentification est une vulnérabilité critique. Des clusters de production ont été compromis parce que le Dashboard était accessible sur Internet sans mot de passe. Toujours protéger par RBAC et authentification.

## ✅ Tu sais maintenant…

- Pourquoi centraliser les logs (éphémérité des containers)
- La stack Prometheus + Grafana pour le monitoring
- Les métriques clés à surveiller
- Les outils du quotidien (kubectl top, k9s, Dashboard — avec précaution)

-----

# Chapitre 19 — Troubleshooting containers et Kubernetes

## Le minimum à savoir

### La démarche systématique

Quand un Pod ne fonctionne pas, suis cette démarche :

```
1. kubectl get pods           → Quel est l'état du Pod ? (Running, CrashLoopBackOff, Pending, Error)
2. kubectl describe pod X     → Quels événements ? Quelles erreurs ?
3. kubectl logs X             → Que dit l'application ?
4. kubectl exec -it X -- sh   → Explorer l'intérieur du container
```

### Les états de Pod et leur signification

|État                |Signification                           |Action                                                      |
|--------------------|----------------------------------------|------------------------------------------------------------|
|**Running**         |Le Pod tourne                           |OK (mais vérifier les logs quand même)                      |
|**Pending**         |Le Pod attend d’être placé sur un nœud  |Vérifier les ressources disponibles, les taints/tolerations |
|**CrashLoopBackOff**|Le container plante en boucle           |`kubectl logs` pour voir l’erreur, `kubectl logs --previous`|
|**ImagePullBackOff**|L’image ne peut pas être téléchargée    |Vérifier le nom de l’image, les credentials du registry     |
|**OOMKilled**       |Le container a dépassé sa limite mémoire|Augmenter les limits ou optimiser l’application             |
|**Error**           |Le container s’est terminé en erreur    |`kubectl logs`                                              |
|**Terminating**     |Le Pod est en cours de suppression      |Vérifier les finalizers, les PVC                            |

### Les problèmes les plus courants

**1. CrashLoopBackOff :**

```bash
kubectl logs mon-pod                  # Voir pourquoi ça plante
kubectl logs mon-pod --previous       # Logs de l'instance précédente
kubectl describe pod mon-pod          # Section "Events" en bas
```

**2. Le Service ne route pas le trafic :**

```bash
kubectl describe service web-service  # Vérifier "Endpoints" — si vide, les labels ne matchent pas
kubectl get endpoints web-service     # Doit lister les IPs des Pods
```

**3. Le Pod reste en Pending :**

```bash
kubectl describe pod mon-pod          # Section "Events" — souvent "Insufficient cpu/memory"
kubectl get nodes                     # Vérifier la capacité des nœuds
```

**4. OOMKilled :**

```bash
kubectl describe pod mon-pod          # "Last State: Terminated, Reason: OOMKilled"
# → Augmenter la limit mémoire ou optimiser l'application
```

> **📋 CONTAINER — Épisode 7**
> 
> Incident en staging : les pods Django redémarrent en boucle (CrashLoopBackOff). `kubectl describe pod` montre un OOMKilled — la limite mémoire est à 256 Mi, l’application en consomme 400 Mi sous charge. Sami augmente les limits à 512 Mi, ajoute des alertes Prometheus sur la consommation mémoire (alerte à 80% de la limit), et documente le seuil. L’incident est résolu en 15 minutes grâce à la démarche systématique.

## ✅ Tu sais maintenant…

- La démarche de troubleshooting (get → describe → logs → exec)
- Les états de Pod et leur signification
- Les problèmes les plus courants et comment les résoudre

-----

# Chapitre 20 — Capstone Partie IV : pipeline CI/CD et monitoring

Exercice intégrateur : mettre en place un pipeline CI/CD simplifié (build → scan Trivy → push → deploy sur minikube), ajouter un monitoring basique (kubectl top + alertes manuelles), et simuler un incident (OOMKilled) pour le diagnostiquer.

-----

# PARTIE V — SÉCURITÉ DES CONTAINERS

-----

# Chapitre 21 — Surface d’attaque des containers : comprendre les risques

## Le minimum à savoir

### Le modèle de menaces

La sécurité des containers ne se résume pas à “scanner les images”. Il y a **6 surfaces d’attaque** à comprendre :

```
┌─────────────────────────────────────────────────┐
│                SUPPLY CHAIN                      │
│  Images malveillantes, dépendances compromises  │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              BUILD / CI/CD                       │
│  Secrets en clair, pipeline compromis            │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              RUNTIME                             │
│  Container escape, privilèges excessifs,         │
│  Docker socket exposé                            │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│           ORCHESTRATEUR (K8s)                    │
│  RBAC trop permissif, API Server exposé,         │
│  Secrets en clair dans etcd                      │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              RÉSEAU                              │
│  Pas de Network Policies → mouvement latéral     │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              DONNÉES                             │
│  Secrets, volumes, données sensibles             │
└─────────────────────────────────────────────────┘
```

### Les 5 risques à connaître absolument

**1. Le container escape :** un attaquant sort du container pour atteindre la machine hôte. Rare mais catastrophique. Vecteurs : vulnérabilité kernel, Docker socket monté, capabilities SYS_ADMIN, hostPID/hostNetwork.

**2. Le Docker socket :** si un container a accès à `/var/run/docker.sock`, il peut créer de nouveaux containers avec des privilèges root sur l’hôte → **compromission totale de la machine**. C’est la faille la plus courante et la plus dangereuse en environnement container.

```bash
# ❌ JAMAIS en production
docker run -v /var/run/docker.sock:/var/run/docker.sock myapp
# → Ce container a un accès root sur la machine hôte
```

**3. L’exécution en root :** par défaut, les containers tournent en root (UID 0). Sans user namespace remapping ou mode rootless, cet UID 0 est le même que sur l’hôte. Les mécanismes d’isolation limitent ses pouvoirs, mais en cas de faille d’isolation ou de mauvaise configuration (capabilities excessives, volumes sensibles montés), l’impact peut être critique — jusqu’à la compromission de l’hôte.

**4. Les images non fiables :** une image Docker Hub communautaire peut contenir du code malveillant, des backdoors, des cryptominers. C’est la supply chain de l’image.

**5. Les Secrets en clair :** les Secrets K8s en base64, les variables d’environnement visibles dans `docker inspect`, les secrets dans les layers de l’image.

> **À retenir pour un entretien :** “Les principaux risques des containers sont : le container escape (sortir du container vers l’hôte), l’exécution en root, le Docker socket monté dans un container, les images non fiables (supply chain), et les secrets mal gérés. La mesure la plus impactante est de ne pas exécuter en root et de ne jamais monter le Docker socket.”

> **📋 CONTAINER — Épisode 8**
> 
> Pendant son audit, Sami découvre que le pipeline GitLab CI de MedFlow monte le Docker socket pour pouvoir construire des images Docker dans la CI. C’est une pratique courante mais dangereuse : n’importe quel job CI a un accès root sur le runner. Il remplace par kaniko (un outil de build d’images qui ne nécessite pas le Docker socket). Il découvre aussi que les secrets de production (clé API, mot de passe de la base de données) sont en clair dans les variables d’environnement GitLab CI, accessibles par tous les développeurs.

## Très utile en pratique

### Checklist de sécurité rapide

|Risque                 |Vérification                                      |Remédiation                                        |
|-----------------------|--------------------------------------------------|---------------------------------------------------|
|Image non fiable       |D’où vient l’image ?                              |Images officielles + registry privé                |
|CVE dans l’image       |Scan Trivy/Grype                                  |Mettre à jour l’image de base                      |
|Exécution en root      |`docker inspect --format='{{.Config.User}}'`      |`USER nonroot` dans le Dockerfile                  |
|Docker socket monté    |`docker inspect` — vérifier les volumes           |Supprimer le montage                               |
|Capabilities excessives|`docker inspect --format='{{.HostConfig.CapAdd}}'`|`--cap-drop ALL --cap-add` uniquement le nécessaire|
|Secrets dans l’image   |`docker history` — vérifier les ARG/ENV           |Multi-stage build, vault externe                   |
|Secrets K8s en base64  |`kubectl get secret -o yaml`                      |Chiffrement etcd + vault externe                   |
|Pas de Network Policies|`kubectl get networkpolicies`                     |Default deny + ouverture sélective                 |
|RBAC trop permissif    |`kubectl get clusterrolebindings`                 |Principe de moindre privilège                      |
|API Server exposé      |Vérifier l’accès réseau                           |Firewall, authentification, audit logs             |

## ✅ Tu sais maintenant…

- Les 6 surfaces d’attaque des containers
- Les 5 risques à connaître (escape, Docker socket, root, images, secrets)
- La checklist de sécurité rapide

## 💬 Questions d’entretien typiques

- **Pourquoi le Docker socket est-il dangereux ?** → Le Docker socket (`/var/run/docker.sock`) permet de contrôler le daemon Docker. Si un container y a accès, il peut créer de nouveaux containers avec des privilèges root sur l’hôte — c’est une compromission totale de la machine.
- **Qu’est-ce qu’un container escape ?** → C’est quand un attaquant sort de l’isolation du container pour atteindre la machine hôte. Les vecteurs incluent des vulnérabilités kernel, des capabilities excessives (SYS_ADMIN), ou un Docker socket monté. C’est rare mais l’impact est maximal.
- **Quels sont les principaux risques de sécurité des containers ?** → Le Docker socket exposé, l’exécution en root, les images non fiables (supply chain), les secrets mal gérés (base64 dans K8s), et l’absence de segmentation réseau (Network Policies).

-----

# Chapitre 22 — Sécuriser les images : de la construction au déploiement

## Le minimum à savoir

### Les 4 piliers de la sécurité des images

**1. Choisir la bonne base :** images officielles, versions `slim` ou `distroless`, éviter les images communautaires non vérifiées.

**2. Scanner :** Trivy, Grype, Snyk — automatisé dans le pipeline CI, bloquer les CVE critiques.

**3. Signer :** Cosign (Sigstore) — prouver que l’image vient de ta CI et n’a pas été modifiée.

**4. Contrôler l’admission :** OPA/Gatekeeper ou Kyverno — empêcher le déploiement d’images non signées ou non scannées sur le cluster K8s.

### Politique d’images en entreprise

```
Développeur construit  →  CI scanne  →  CI signe  →  Push au   →  K8s vérifie
l'image                   avec Trivy    avec Cosign   registry     la signature
                              ↓                                      ↓
                        CVE critique ?                        Signature valide ?
                              ↓                                      ↓
                          OUI → BLOQUÉ                       NON → REFUSÉ
                          NON → OK                           OUI → DÉPLOYÉ
```

> **📋 CONTAINER — Épisode 9 (partie 1)**
> 
> Sami met en place la politique d’images MedFlow : registry privé Harbor, scan Trivy dans la CI (0 CVE critical/high pour passer), signature Cosign, et un admission webhook Kyverno qui refuse toute image non signée. Un développeur essaie de déployer une image Docker Hub → refusé. Sami lui explique le workflow : “on ne bloque pas le travail, on fournit les images validées.”

## ✅ Tu sais maintenant…

- Les 4 piliers : base fiable, scan, signature, contrôle d’admission
- Le workflow de sécurité des images en entreprise

-----

# Chapitre 23 — Sécuriser le runtime : isolation et contrôle d’exécution

## Le minimum à savoir

### Les 4 mesures essentielles

**1. Utilisateur non-root :** `USER nonroot` dans le Dockerfile, `runAsNonRoot: true` dans le Pod spec K8s.

**2. Capabilities minimales :** `--cap-drop ALL` puis `--cap-add` uniquement ce qui est nécessaire. En K8s : Pod Security Standards.

**3. Read-only filesystem :** `readOnlyRootFilesystem: true` dans le Pod spec — le container ne peut rien écrire sur son filesystem (sauf les volumes montés).

**4. Pod Security Standards (K8s) :** trois niveaux — Privileged (aucune restriction), Baseline (restrictions minimales), Restricted (hardening strict).

```yaml
# Pod spec durci
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
  containers:
  - name: web
    image: mon_app:1.0.0
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

> **À retenir pour un entretien :** “Pour sécuriser le runtime, les mesures essentielles sont : exécuter en non-root, supprimer toutes les capabilities Linux sauf celles nécessaires, monter le filesystem en lecture seule, et appliquer les Pod Security Standards restricted.”

## Très utile en pratique

### Falco : la détection runtime

**Falco** (CNCF) surveille les containers en temps réel et détecte les comportements anormaux :

- Un shell est lancé dans un container de production
- Un processus lit `/etc/shadow`
- Une connexion réseau sortante vers une IP suspecte
- Un fichier est écrit dans `/usr/bin/`

C’est l’IDS (système de détection d’intrusion) pour les containers.

### Docker rootless et user namespace remapping

Au-delà du `USER nonroot` dans le Dockerfile, deux mécanismes renforcent l’isolation au niveau de l’hôte :

**Docker en mode rootless** : le daemon Docker lui-même tourne sans root. L’avantage est fondamental : même une faille dans le daemon Docker ne donne pas root sur l’hôte. Docker rootless est supporté depuis Docker 20.10+ mais nécessite une configuration spécifique. **Podman** fonctionne nativement en rootless.

**User namespace remapping** : le UID 0 (root) dans le container est mappé vers un UID non privilégié sur l’hôte (par exemple 100000). Même si un attaquant est root dans le container, il est un utilisateur sans privilège sur l’hôte. C’est une couche de défense en profondeur. Configuration dans `/etc/docker/daemon.json` :

```json
{
  "userns-remap": "default"
}
```

> **En résumé :** `USER nonroot` dans le Dockerfile empêche l’application de tourner en root dans le container. Le user namespace remapping empêche root dans le container d’être root sur l’hôte. Docker rootless empêche le daemon lui-même de tourner en root. Ce sont 3 couches de défense complémentaires.

Ces mécanismes ne sont pas magiques — ils ont des contraintes (compatibilité avec certains volumes, certains réseaux, performance). Mais pour les environnements où la sécurité est une priorité, ils réduisent significativement le risque de container escape.

## ✅ Tu sais maintenant…

- Les 4 mesures de hardening runtime (non-root, capabilities, read-only, PSS)
- Falco pour la détection d’anomalies en runtime
- Docker rootless et user namespace remapping comme couches de défense supplémentaires

## 💬 Questions d’entretien typiques

- **Comment sécuriser le runtime d’un container ?** → Exécuter en non-root (USER dans le Dockerfile + runAsNonRoot dans K8s), supprimer toutes les capabilities (cap-drop ALL), filesystem read-only, et appliquer les Pod Security Standards restricted.
- **Qu’est-ce que le user namespace remapping ?** → C’est un mécanisme qui mappe le UID 0 (root) du container vers un UID non privilégié sur l’hôte. Même si un attaquant devient root dans le container, il est un utilisateur sans privilège sur la machine hôte.
- **Quelle est la différence entre Docker classique et Docker rootless ?** → En Docker classique, le daemon tourne en root — un accès au Docker socket donne l’équivalent de root sur l’hôte. En rootless, le daemon tourne sans root, ce qui réduit l’impact d’une compromission du daemon.

-----

# Chapitre 24 — Sécuriser le réseau : segmentation et chiffrement

## Le minimum à savoir

### Le réseau K8s par défaut est PLAT

Par défaut dans Kubernetes, **tous les Pods peuvent communiquer avec tous les Pods**, dans tous les namespaces. C’est exactement comme un réseau d’entreprise sans aucune segmentation — si un attaquant compromet un Pod, il peut atteindre tous les autres.

### Network Policies : le pare-feu de K8s

Les **Network Policies** sont les règles de firewall de Kubernetes. Elles contrôlent quels Pods peuvent communiquer entre eux.

```yaml
# Default deny — RIEN ne communique sauf ce qui est explicitement autorisé
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}      # S'applique à TOUS les pods du namespace
  policyTypes:
  - Ingress
  - Egress
```

```yaml
# Autoriser le trafic web → db uniquement
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-to-db
spec:
  podSelector:
    matchLabels:
      app: db
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: web
    ports:
    - port: 5432
```

> **Important :** les Network Policies ne fonctionnent que si le CNI (Container Network Interface) du cluster les supporte. **Calico** et **Cilium** les supportent. Le CNI par défaut de certains services managés ne les supporte pas toujours — vérifie.

### Le service mesh (avancé)

Pour aller plus loin : un **service mesh** (Istio, Linkerd) ajoute automatiquement le **mTLS** (chiffrement mutuel) entre tous les services. Chaque communication inter-Pod est chiffrée sans modification du code applicatif.

## ✅ Tu sais maintenant…

- Le réseau K8s est plat par défaut (pas de segmentation)
- Les Network Policies pour segmenter (default deny + règles explicites)
- Le service mesh pour le chiffrement inter-services (mTLS)

-----

# Chapitre 25 — Sécuriser Kubernetes : RBAC, Secrets et API Server

## Le minimum à savoir

### Le RBAC (Role-Based Access Control)

Le RBAC contrôle **qui peut faire quoi** dans le cluster.

|Objet                 |Portée         |Rôle                                               |
|----------------------|---------------|---------------------------------------------------|
|**Role**              |Un namespace   |Permissions dans un namespace                      |
|**ClusterRole**       |Tout le cluster|Permissions globales                               |
|**RoleBinding**       |Un namespace   |Lie un utilisateur/service account à un Role       |
|**ClusterRoleBinding**|Tout le cluster|Lie un utilisateur/service account à un ClusterRole|

```yaml
# Un Role qui permet de lire les Pods dans le namespace "staging"
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: staging
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

> **⚠️ Le piège :** le ClusterRoleBinding `cluster-admin` donne **tous les droits sur tout le cluster**. C’est souvent attribué par défaut à tous les développeurs par commodité — c’est l’équivalent de donner root à tout le monde.

> **À retenir pour un entretien :** “Le RBAC dans Kubernetes fonctionne par le principe de moindre privilège : chaque utilisateur et chaque service account ne doit avoir que les permissions strictement nécessaires. Le cluster-admin ne devrait être attribué qu’aux administrateurs du cluster.”

### Les Service Accounts

Chaque Pod a un **Service Account** (SA) qui lui donne des droits sur l’API K8s. Par défaut :

- Un SA `default` est automatiquement créé dans chaque namespace
- Le token du SA est automatiquement monté dans chaque Pod
- Ce token permet d’appeler l’API Server depuis le Pod

**Le risque :** si un attaquant compromet un Pod avec un SA trop permissif, il peut utiliser le token pour lire des Secrets, créer des Pods, ou même prendre le contrôle du cluster.

**La remédiation :**

```yaml
spec:
  automountServiceAccountToken: false   # Ne pas monter le token automatiquement
```

### Les Secrets : le vrai problème

Rappel : les Secrets K8s sont en **base64, pas chiffrés**. Les remédiations :

1. **Chiffrement au repos :** configurer le chiffrement d’etcd (EncryptionConfiguration) pour que les Secrets soient chiffrés sur disque
1. **Vault externe :** utiliser HashiCorp Vault, AWS Secrets Manager, ou Azure Key Vault via External Secrets Operator — les secrets ne sont jamais stockés dans K8s
1. **Rotation :** les secrets doivent pouvoir être changés sans redéploiement

### L’API Server : le point de contrôle

L’API Server est le point d’entrée unique du cluster. Le sécuriser est prioritaire :

- **Ne jamais l’exposer sur Internet** sans authentification
- **Audit logs :** activer les logs d’audit pour tracer qui fait quoi
- **Authentification :** OIDC (SSO), certificats clients — pas de tokens statiques

### Les outils d’audit

```bash
# kube-bench — vérifie le cluster contre le CIS Kubernetes Benchmark
docker run --rm -v /etc:/node/etc -v /var:/node/var aquasec/kube-bench

# kubeaudit — audite les manifests et les configurations
kubeaudit all
```

> **📋 CONTAINER — Épisode 9 (partie 2)**
> 
> Audit de sécurité du cluster EKS de MedFlow. Résultats : 3 service accounts avec `cluster-admin` (dont 2 inutiles), pas de Network Policies, Secrets en base64 sans chiffrement etcd, audit logs désactivés. Plan de remédiation : réduire les RBAC au strict nécessaire, activer les Network Policies (default deny), migrer les secrets vers AWS Secrets Manager via External Secrets Operator, activer les audit logs.

## ✅ Tu sais maintenant…

- Le RBAC (Role, ClusterRole, RoleBinding — moindre privilège)
- Les Service Accounts et leurs risques (token monté par défaut)
- Les Secrets K8s (base64, pas chiffrés — vault externe recommandé)
- La sécurité de l’API Server (pas d’exposition Internet, audit logs)
- Les outils d’audit (kube-bench, kubeaudit)

## 💬 Questions d’entretien typiques

- **Comment fonctionne le RBAC dans Kubernetes ?** → K8s utilise des Roles (permissions dans un namespace) et ClusterRoles (permissions globales), liés à des utilisateurs ou Service Accounts via des Bindings. Le principe est le moindre privilège — chaque identité ne doit avoir que les droits strictement nécessaires.
- **Pourquoi les Secrets Kubernetes ne sont-ils pas suffisants seuls ?** → Parce qu’ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC adéquats ou tout accès à etcd insuffisamment protégé peut les lire en clair. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe (HashiCorp Vault, AWS Secrets Manager).
- **Qu’est-ce qu’un Service Account et pourquoi est-ce un risque ?** → Chaque Pod a un Service Account avec un token API monté automatiquement. Si un attaquant compromet le Pod et que le SA a des droits excessifs, il peut utiliser le token pour interagir avec l’API Server (lire des Secrets, créer des Pods, etc.). La remédiation : désactiver le montage automatique du token et appliquer le moindre privilège.

-----

# Chapitre 26 — Détection et réponse aux incidents dans les containers

## Le minimum à savoir

### Le défi de l’éphémérité

Les containers meurent et renaissent en permanence. Un container compromis peut être détruit et recréé par K8s en quelques secondes — **les preuves disparaissent**. Sans externalisation des logs et des métriques, le forensic est impossible.

### La détection runtime

**Falco** (CNCF) est l’outil de référence pour la détection d’anomalies dans les containers :

```yaml
# Exemples de règles Falco
- rule: Terminal shell in container
  desc: Détecte l'ouverture d'un shell dans un container
  condition: container and proc.name in (bash, sh, zsh)
  output: "Shell ouvert dans le container (user=%user.name container=%container.name)"
  priority: WARNING
```

### La réponse

1. **Isoler :** appliquer une Network Policy deny all sur le Pod compromis (coupure réseau immédiate)
1. **Capturer :** sauvegarder l’état du container avant sa destruction (`kubectl cp`, export des logs, snapshot du volume)
1. **Analyser :** examiner les logs K8s, les audit logs de l’API Server, les alertes Falco, corréler avec les logs applicatifs centralisés
1. **Remédier :** corriger la vulnérabilité, mettre à jour l’image, renforcer les politiques

### Les indicateurs de compromission (IoC) spécifiques aux containers

- Processus non attendu dans le container (shell, wget, curl, netcat)
- Connexions réseau sortantes vers des IPs/domaines inconnus
- Écriture dans des répertoires système (`/usr/bin`, `/etc`)
- Tentative de montage de volumes non autorisés
- Utilisation de capabilities inhabituelles
- Appels API K8s depuis un Pod applicatif

## ✅ Tu sais maintenant…

- Le défi de l’éphémérité pour le forensic
- Falco pour la détection runtime
- La démarche de réponse (isoler → capturer → analyser → remédier)
- Les IoC spécifiques aux containers

-----

# PARTIE VI — ARCHITECTURES ET PATTERNS AVANCÉS

-----

# Chapitre 27 — Microservices, patterns et anti-patterns

## Le minimum à savoir

### Monolithe vs Microservices

|Aspect     |Monolithe                                  |Microservices                            |
|-----------|-------------------------------------------|-----------------------------------------|
|Structure  |1 application, 1 déploiement               |N services indépendants                  |
|Déploiement|Tout ou rien                               |Service par service                      |
|Scaling    |L’application entière                      |Chaque service indépendamment            |
|Complexité |Simple au début, difficile à grande échelle|Complexe dès le début (réseau, debugging)|
|Équipe     |1 équipe, 1 codebase                       |N équipes, N codebases                   |

**L’erreur classique :** migrer vers des microservices trop tôt. Si ton équipe est petite et ton application simple, un monolithe bien structuré est plus simple et plus rapide. Les microservices se justifient quand l’application est grande, l’équipe est grande, et les besoins de scaling sont différents par composant.

> **À retenir pour un entretien :** “Les microservices ne sont pas toujours la bonne réponse. Un monolithe containerisé est déjà un énorme progrès. La migration vers les microservices se justifie quand la taille de l’équipe et de l’application le nécessite.”

### Les anti-patterns de sécurité dans les microservices

- **Confiance aveugle au trafic interne :** “les requêtes viennent de l’intérieur du cluster, donc elles sont fiables” → faux si un Pod est compromis
- **Absence d’AuthN/AuthZ inter-services :** chaque service devrait vérifier l’identité et les droits de l’appelant
- **Secrets partagés :** un secret commun à tous les services → si un service est compromis, tous les secrets fuient

## ✅ Tu sais maintenant…

- La différence entre monolithe et microservices (et quand migrer)
- Les anti-patterns de sécurité des microservices

-----

# Chapitre 28 — Multi-tenancy, scaling et production

## Le minimum à savoir

### Le scaling automatique

|Type                               |Ce qu’il scale         |Comment                                                                |
|-----------------------------------|-----------------------|-----------------------------------------------------------------------|
|**HPA** (Horizontal Pod Autoscaler)|Le nombre de Pods      |Ajoute/retire des Pods selon la charge (CPU, mémoire, métriques custom)|
|**VPA** (Vertical Pod Autoscaler)  |Les ressources d’un Pod|Ajuste les requests/limits selon l’utilisation réelle                  |
|**Cluster Autoscaler**             |Le nombre de nœuds     |Ajoute/retire des nœuds selon les besoins de scheduling                |

```yaml
# HPA — scaler entre 3 et 10 replicas selon le CPU
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70    # Scale up si CPU > 70%
```

### La haute disponibilité

- **PodDisruptionBudget :** garantir qu’un nombre minimum de Pods reste actif pendant les maintenances
- **Anti-affinity :** répartir les Pods sur différents nœuds (si un nœud tombe, l’application continue)
- **Multi-AZ :** répartir les nœuds sur plusieurs zones de disponibilité

## ✅ Tu sais maintenant…

- Le scaling automatique (HPA, VPA, Cluster Autoscaler)
- Les mécanismes de haute disponibilité (PDB, anti-affinity, multi-AZ)

-----

# PARTIE VII — SYNTHÈSE

-----

# Chapitre 29 — Cas de synthèse : audit de sécurité d’un environnement containerisé

## L’exercice

Un cluster Kubernetes de production avec des faiblesses volontaires. L’étudiant doit :

1. **Auditer les images :** scanner avec Trivy, vérifier les images de base, chercher les secrets dans les layers
1. **Auditer le runtime :** vérifier les users (root ?), les capabilities, le filesystem read-only, le Docker socket
1. **Auditer K8s :** kube-bench, RBAC (cluster-admin partout ?), Service Accounts, Secrets, Network Policies
1. **Produire un rapport :** matrice des risques classée P0/P1/P2, plan de remédiation, quick wins

> **📋 CONTAINER — Épisode final**
> 
> 6 mois plus tard. MedFlow tourne sur EKS. Images signées avec Cosign et scannées par Trivy dans la CI, Network Policies en default deny (seuls les flux explicitement autorisés passent), RBAC minimal (chaque développeur n’a accès qu’à son namespace), secrets dans AWS Secrets Manager via External Secrets Operator, Falco en détection runtime, monitoring Prometheus/Grafana, logs centralisés dans Loki. Un audit externe confirme la posture. Sami rédige le runbook d’exploitation et forme l’équipe dev sur les bonnes pratiques. Le CTO : “Il y a 6 mois on ne savait pas ce qu’était un Dockerfile.”

-----

# Chapitre 30 — Le métier et les perspectives

## Le minimum à savoir

### Les métiers

|Métier                             |Focus                                           |Compétences clés                       |
|-----------------------------------|------------------------------------------------|---------------------------------------|
|**DevOps Engineer**                |Automatiser le build, test, déploiement         |CI/CD, Docker, K8s, IaC                |
|**SRE** (Site Reliability Engineer)|Fiabilité et performance en production          |Monitoring, troubleshooting, SLO/SLA   |
|**Platform Engineer**              |Construire la plateforme pour les développeurs  |K8s, abstractions, developer experience|
|**Cloud Security Engineer**        |Sécuriser les environnements cloud et containers|Hardening, audit, compliance, détection|

### Les certifications

|Certification                                        |Organisme            |Focus                |Difficulté            |
|-----------------------------------------------------|---------------------|---------------------|----------------------|
|**CKA** (Certified Kubernetes Administrator)         |CNCF/Linux Foundation|Administration K8s   |Intermédiaire         |
|**CKAD** (Certified Kubernetes Application Developer)|CNCF/Linux Foundation|Développement sur K8s|Intermédiaire         |
|**CKS** (Certified Kubernetes Security Specialist)   |CNCF/Linux Foundation|Sécurité K8s         |Avancé (prérequis CKA)|


> **Conseil :** la CKA est la certification la plus demandée. Elle valide ta capacité à administrer un cluster K8s. La CKS est le complément sécurité — très valorisée dans les profils cyber/cloud security.

### L’écosystème en mouvement

- **eBPF :** technologie kernel Linux qui révolutionne l’observabilité et la sécurité des containers (Cilium, Tetragon, Falco) — sans modifier les applications
- **WebAssembly (Wasm) :** alternative émergente aux containers pour certains cas d’usage — plus léger, sandboxé, portable
- **Kubernetes sans Kubernetes :** des abstractions qui masquent la complexité (AWS Fargate, Google Cloud Run, Azure Container Apps) — tu déploies des containers sans gérer le cluster

### La veille

Les sources essentielles : le blog CNCF, KubeCon (la conférence de référence — vidéos gratuites sur YouTube), le Kubernetes security mailing list, learnk8s.io (ressources d’apprentissage), et les rapports annuels de sécurité Kubernetes (Sysdig, Datadog).

## ✅ Tu sais maintenant…

- Les métiers liés aux containers et à Kubernetes
- Les certifications de référence (CKA, CKAD, CKS)
- Les tendances technologiques (eBPF, Wasm, abstractions serverless)

-----

# ANNEXES

-----

## Annexe A — Glossaire

|Terme                     |Définition                                                                              |
|--------------------------|----------------------------------------------------------------------------------------|
|**Alpine**                |Distribution Linux ultra-légère (~5 Mo), souvent utilisée comme image de base           |
|**API Server**            |Point d’entrée unique du cluster Kubernetes — tout passe par lui                        |
|**ArgoCD**                |Outil GitOps — synchronise l’état du cluster K8s avec un repo Git                       |
|**Base64**                |Encodage (PAS chiffrement) utilisé pour les Secrets K8s                                 |
|**Bind mount**            |Montage d’un dossier de l’hôte dans un container                                        |
|**Bridge**                |Driver réseau Docker par défaut — réseau isolé                                          |
|**Capability**            |Permission granulaire du kernel Linux attribuée à un container                          |
|**cgroup**                |Control Group — mécanisme Linux de limitation des ressources (CPU, RAM)                 |
|**CKA**                   |Certified Kubernetes Administrator — certification CNCF                                 |
|**CKS**                   |Certified Kubernetes Security Specialist — certification CNCF                           |
|**ClusterIP**             |Type de Service K8s accessible uniquement à l’intérieur du cluster                      |
|**CNCF**                  |Cloud Native Computing Foundation — gouvernance de Kubernetes et des projets associés   |
|**CNI**                   |Container Network Interface — plugin réseau pour Kubernetes (Calico, Cilium)            |
|**ConfigMap**             |Objet K8s pour stocker de la configuration non sensible                                 |
|**Container escape**      |Sortie d’un container pour atteindre la machine hôte                                    |
|**containerd**            |Runtime de containers de haut niveau utilisé par Docker et K8s                          |
|**Cosign**                |Outil de signature d’images Docker (projet Sigstore)                                    |
|**CRI**                   |Container Runtime Interface — interface standard entre K8s et les runtimes              |
|**Deployment**            |Objet K8s qui gère le déploiement et le scaling d’une application                       |
|**Distroless**            |Image Docker minimale sans shell ni outils — surface d’attaque minimale                 |
|**Docker Compose**        |Outil pour gérer des applications multi-containers sur un seul hôte                     |
|**Docker Hub**            |Registry public par défaut pour les images Docker                                       |
|**Docker socket**         |`/var/run/docker.sock` — accès au daemon Docker (⚠️ donne un contrôle total)             |
|**Dockerfile**            |Fichier texte décrivant la construction d’une image Docker                              |
|**eBPF**                  |Extended Berkeley Packet Filter — technologie kernel pour l’observabilité et la sécurité|
|**EKS**                   |Elastic Kubernetes Service — K8s managé par AWS                                         |
|**etcd**                  |Base de données distribuée du cluster K8s — contient tout l’état                        |
|**Falco**                 |Outil CNCF de détection d’anomalies runtime dans les containers                         |
|**GitOps**                |Modèle où Git est la source de vérité pour l’état du cluster                            |
|**Grafana**               |Outil de dashboards pour le monitoring                                                  |
|**Grype**                 |Scanner de vulnérabilités pour les images Docker                                        |
|**Harbor**                |Registry Docker open source avec scan intégré                                           |
|**HPA**                   |Horizontal Pod Autoscaler — scaling automatique du nombre de Pods                       |
|**Ingress**               |Objet K8s qui expose des applications HTTP/HTTPS au monde extérieur                     |
|**Kaniko**                |Outil de build d’images Docker sans Docker socket                                       |
|**kubectl**               |Outil CLI pour interagir avec un cluster Kubernetes                                     |
|**kubelet**               |Agent sur chaque nœud K8s qui gère les containers localement                            |
|**Kyverno**               |Admission controller K8s pour les politiques de sécurité                                |
|**Layer**                 |Couche d’une image Docker — chaque instruction Dockerfile crée une couche               |
|**LoadBalancer**          |Type de Service K8s qui crée un load balancer cloud                                     |
|**Loki**                  |Système de centralisation de logs (Grafana Labs)                                        |
|**minikube**              |Cluster K8s local pour l’apprentissage et le développement                              |
|**mTLS**                  |Mutual TLS — chiffrement mutuel entre services                                          |
|**Multi-stage build**     |Technique Dockerfile qui sépare build et production pour réduire la taille              |
|**Namespace**             |Espace logique de séparation dans un cluster K8s                                        |
|**Network Policy**        |Règle de pare-feu entre les Pods dans K8s                                               |
|**NodePort**              |Type de Service K8s accessible via un port sur chaque nœud                              |
|**OCI**                   |Open Container Initiative — standard ouvert pour les images et runtimes                 |
|**OPA/Gatekeeper**        |Admission controller K8s pour les politiques de sécurité                                |
|**OverlayFS**             |Filesystem par couches utilisé par Docker                                               |
|**PersistentVolumeClaim** |Demande de stockage persistant dans K8s                                                 |
|**Pod**                   |Plus petite unité déployable dans K8s — contient un ou plusieurs containers             |
|**Pod Security Standards**|Niveaux de restriction de sécurité K8s (Privileged, Baseline, Restricted)               |
|**Prometheus**            |Système de monitoring et d’alerting (standard K8s)                                      |
|**RBAC**                  |Role-Based Access Control — système de permissions dans K8s                             |
|**Registry**              |Entrepôt d’images Docker (Docker Hub, Harbor, ECR, ACR)                                 |
|**ReplicaSet**            |Objet K8s qui maintient un nombre de Pods (géré par le Deployment)                      |
|**Rolling update**        |Mise à jour progressive des Pods sans interruption                                      |
|**runc**                  |Runtime de containers de bas niveau (standard OCI)                                      |
|**SBOM**                  |Software Bill of Materials — inventaire des composants d’une image                      |
|**Seccomp**               |Filtrage des appels système Linux pour les containers                                   |
|**Secret**                |Objet K8s pour stocker des données sensibles (⚠️ base64, pas chiffré)                    |
|**Service**               |Objet K8s qui donne une adresse réseau stable à un groupe de Pods                       |
|**Service Account**       |Identité d’un Pod dans K8s (avec un token API)                                          |
|**Service Mesh**          |Couche d’infrastructure pour la communication inter-services (Istio, Linkerd)           |
|**Sidecar**               |Container auxiliaire dans un Pod (ex : proxy, collecteur de logs)                       |
|**StatefulSet**           |Objet K8s pour les applications avec état (bases de données)                            |
|**StorageClass**          |Type de stockage disponible dans un cluster K8s                                         |
|**Tag**                   |Version d’une image Docker (ex : `nginx:1.25`)                                          |
|**Trivy**                 |Scanner de vulnérabilités pour les images Docker (open source)                          |
|**Volume**                |Espace de stockage persistant dans Docker ou K8s                                        |
|**Wasm**                  |WebAssembly — alternative émergente aux containers                                      |

-----

## Annexe B — Cheat sheets

### Commandes Docker essentielles

```bash
# Images
docker build -t nom:tag .          # Construire
docker images                       # Lister
docker pull nom:tag                 # Télécharger
docker rmi nom:tag                  # Supprimer

# Containers
docker run -d --name X -p H:C img  # Lancer
docker ps / docker ps -a            # Lister
docker stop X / docker rm X         # Arrêter / Supprimer
docker logs X / docker logs -f X    # Logs
docker exec -it X bash              # Shell dans le container
docker inspect X                    # Détails

# Nettoyage
docker system prune                 # Tout nettoyer
```

### Commandes kubectl essentielles

```bash
# Lecture
kubectl get pods/deploy/svc/all     # Lister
kubectl describe pod X              # Détails + événements
kubectl logs X / kubectl logs -f X  # Logs

# Interaction
kubectl exec -it X -- bash          # Shell dans le Pod
kubectl port-forward X 8080:80      # Accès local

# Déploiement
kubectl apply -f manifest.yaml      # Appliquer
kubectl delete -f manifest.yaml     # Supprimer
kubectl scale deploy X --replicas=N # Scaler
kubectl rollout undo deploy X       # Rollback
```

-----

## Annexe C — Tableau d’outils de référence

|Catégorie         |Outil            |Gratuit/Payant|Usage                                   |Limites                       |
|------------------|-----------------|--------------|----------------------------------------|------------------------------|
|Build             |Docker           |Gratuit (CE)  |Construction d’images                   |Daemon en root                |
|Build sans socket |Kaniko           |Gratuit       |Build en CI sans Docker socket          |Plus lent                     |
|Alternative Docker|Podman           |Gratuit       |Containers sans daemon root             |Écosystème plus petit         |
|Scan images       |Trivy            |Gratuit       |Scan CVE images + IaC + SBOM            |Faux positifs possibles       |
|Scan images       |Grype            |Gratuit       |Scan CVE images                         |Moins de features que Trivy   |
|Scan images       |Snyk Container   |Freemium      |Scan + monitoring continu               |Plan gratuit limité           |
|Signature         |Cosign (Sigstore)|Gratuit       |Signature et vérification d’images      |Nécessite une PKI ou Fulcio   |
|SBOM              |Syft             |Gratuit       |Génération de SBOM                      |—                             |
|Registry          |Harbor           |Gratuit       |Registry privé avec scan intégré        |Auto-hébergé (maintenance)    |
|Registry          |Docker Hub       |Freemium      |Registry public                         |Pull rate limit               |
|Orchestration     |Kubernetes       |Gratuit       |Orchestration de containers             |Complexité opérationnelle     |
|K8s local         |minikube         |Gratuit       |Cluster K8s local                       |Un seul nœud                  |
|K8s managé        |EKS/AKS/GKE      |Payant        |K8s en production                       |Coût cloud                    |
|Monitoring        |Prometheus       |Gratuit       |Métriques et alertes                    |Stockage long terme limité    |
|Dashboards        |Grafana          |Gratuit (OSS) |Visualisation                           |—                             |
|Logs              |Loki             |Gratuit       |Centralisation des logs                 |Moins riche qu’Elasticsearch  |
|Détection runtime |Falco            |Gratuit       |Détection d’anomalies containers        |Règles à maintenir            |
|Détection eBPF    |Tetragon         |Gratuit       |Observabilité et sécurité kernel        |Récent, écosystème jeune      |
|Audit K8s         |kube-bench       |Gratuit       |CIS Kubernetes Benchmark                |Audit ponctuel                |
|Admission         |Kyverno          |Gratuit       |Politiques de sécurité K8s              |—                             |
|Admission         |OPA/Gatekeeper   |Gratuit       |Politiques de sécurité K8s (Rego)       |Langage Rego à apprendre      |
|GitOps            |ArgoCD           |Gratuit       |Synchronisation Git → K8s               |Configuration initiale        |
|Service Mesh      |Istio            |Gratuit       |mTLS, observabilité, routing            |Complexe, overhead performance|
|CLI K8s           |k9s              |Gratuit       |Terminal interactif K8s                 |—                             |
|Lint Dockerfile   |Hadolint         |Gratuit       |Vérification bonnes pratiques Dockerfile|—                             |

-----

## Annexe D — Templates opérationnels

### Dockerfile de production (Python)

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --no-log-init --shell /bin/false appuser
COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app.wsgi:application"]
```

### Network Policy — Default Deny

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### Checklist de sécurité container

- [ ] Images officielles ou registry privé uniquement
- [ ] Scan Trivy : 0 CVE critique/haute
- [ ] Image signée avec Cosign
- [ ] Utilisateur non-root (`USER` dans Dockerfile, `runAsNonRoot` dans K8s)
- [ ] Capabilities : `drop ALL`, ajouter uniquement le nécessaire
- [ ] Filesystem read-only (`readOnlyRootFilesystem: true`)
- [ ] Secrets dans un vault externe (pas en base64 dans K8s)
- [ ] Network Policies en default deny
- [ ] RBAC : moindre privilège (pas de cluster-admin sauf admins)
- [ ] Service Account : `automountServiceAccountToken: false` sauf besoin
- [ ] Resource requests et limits définis
- [ ] Probes liveness et readiness configurées
- [ ] Logs centralisés (pas dans le container)
- [ ] Monitoring et alertes actifs (Prometheus)
- [ ] Détection runtime (Falco)
- [ ] API Server non exposé sur Internet
- [ ] Audit logs K8s activés

-----

## Annexe E — Ressources et formation

### Labs gratuits

|Ressource                                       |Usage                                       |
|------------------------------------------------|--------------------------------------------|
|**Killercoda** (killercoda.com)                 |Exercices K8s interactifs dans le navigateur|
|**Play with Docker** (labs.play-with-docker.com)|Lab Docker en ligne gratuit                 |
|**Play with K8s** (labs.play-with-k8s.com)      |Lab K8s en ligne gratuit                    |
|**KodeKloud**                                   |Cours et labs K8s (certains gratuits)       |

### Certifications

|Certification|Prérequis             |Format                 |Coût (~)|
|-------------|----------------------|-----------------------|--------|
|CKA          |Expérience K8s basique|Pratique (2h, terminal)|~395 USD|
|CKAD         |Expérience K8s basique|Pratique (2h, terminal)|~395 USD|
|CKS          |CKA valide            |Pratique (2h, terminal)|~395 USD|

### Livres

- *Kubernetes Up & Running* (Hightower, Burns, Beda) — la référence pour démarrer
- *Container Security* (Liz Rice) — excellent pour le volet sécurité

### Conférences

- **KubeCon + CloudNativeCon** — la conférence de référence (vidéos gratuites sur YouTube)
- **Docker Con** — conférence Docker

-----

## Annexe F — Hardening checklist par priorité

### P0 — Quick wins (immédiat)

- Utilisateur non-root dans tous les containers
- Scanner toutes les images avec Trivy
- Supprimer les montages de Docker socket
- Ne pas utiliser `latest` en production
- Mettre des resource limits sur tous les Pods

### P1 — Fondations (1-3 mois)

- Registry privé avec scan intégré
- Network Policies (default deny)
- RBAC minimal (supprimer les cluster-admin inutiles)
- Secrets dans un vault externe
- Monitoring et alertes (Prometheus + Grafana)
- Logs centralisés

### P2 — Hardening avancé (3-6 mois)

- Signature d’images (Cosign) + admission controller
- Pod Security Standards (Restricted)
- Seccomp profiles
- Détection runtime (Falco)
- Audit logs K8s
- Service mesh (mTLS inter-services)

-----

## Annexe G — Mapping de la bibliothèque

|Thématique                                       |Cours principal   |Ce cours                                        |
|-------------------------------------------------|------------------|------------------------------------------------|
|Infrastructure IT (virtualisation, réseau, cloud)|**Cours Infra IT**|Fondations (Ch.1-2), réseau (Ch.5, 24)          |
|Sécurité applicative (vulnérabilités, DevSecOps) |**Cours AppSec**  |Images (Ch.7, 22), pipeline (Ch.17)             |
|Détection SOC                                    |**Cours SOC**     |Logs containers → SIEM (Ch.18, 26)              |
|Incident Response                                |**Cours IR**      |Forensic container (Ch.26)                      |
|Digital Forensic                                 |**Cours Forensic**|Analyse de layers, capture d’état (Ch.26)       |
|CTI                                              |**Cours CTI**     |Supply chain d’images comme vecteur (Ch.9, 22)  |
|Active Directory                                 |**Cours AD**      |Containers dans les environnements AD (contexte)|
|Linux (scripting Bash)                           |**Cours Bash**    |Namespaces, cgroups, kernel (Ch.2)              |
|Python (scripting)                               |**Cours Python**  |Dockerfile Python, automatisation (Ch.6, 12)    |

-----

# Annexe — Questions types d'entretien et réponses types

## Questions essentielles

- **Question :** Quelle est la différence entre un container et une VM ?
  - **Réponse type :** Un container partage le kernel de l'hôte et embarque uniquement l'application et ses dépendances. Il démarre en quelques secondes et consomme très peu de ressources. Une VM embarque un OS complet avec son propre kernel, ce qui offre une isolation plus forte mais la rend beaucoup plus lourde. En résumé : le container est plus léger et plus rapide, mais l'isolation est moins forte car le kernel est partagé.

- **Question :** Qu'est-ce qu'une image Docker et comment on la construit ?
  - **Réponse type :** Une image est un template en lecture seule qui contient tout ce qu'il faut pour faire tourner une application : code, dépendances, configuration. On la construit avec un Dockerfile, un fichier texte qui décrit les étapes de construction. Chaque instruction crée une couche (layer). On utilise `docker build` pour produire l'image à partir du Dockerfile.

- **Question :** Comment sécurisez-vous une image Docker ?
  - **Réponse type :** Plusieurs bonnes pratiques : partir d'une image officielle ou minimale (slim, distroless), utiliser un multi-stage build pour ne garder que le nécessaire, ne jamais tourner en root (instruction USER), scanner les vulnérabilités avec Trivy, et ne pas embarquer de secrets dans l'image. En production, on signe les images avec Cosign et on utilise un registry privé.

- **Question :** Qu'est-ce que Kubernetes et pourquoi on l'utilise ?
  - **Réponse type :** Kubernetes est un orchestrateur de containers. Quand on a beaucoup de containers répartis sur plusieurs serveurs, Docker seul ne suffit plus pour gérer le scaling, le self-healing, les mises à jour sans coupure, et la répartition de charge. Kubernetes automatise tout ça. Il gère le cycle de vie des containers à l'échelle d'un cluster.

- **Question :** Quels sont les objets Kubernetes essentiels à connaître ?
  - **Réponse type :** Le Pod, c'est la plus petite unité — un ou plusieurs containers qui tournent ensemble. Le Deployment gère le déploiement et le scaling des Pods. Le Service donne une adresse réseau stable à un groupe de Pods. Le Namespace permet de séparer logiquement les ressources. Et les Secrets/ConfigMaps gèrent la configuration et les données sensibles.

## Questions complémentaires

- **Question :** Quels sont les principaux risques de sécurité liés aux containers ?
  - **Réponse type :** Les risques majeurs : tourner en root dans le container (un escape mène directement au root de l'hôte), utiliser des images vulnérables ou non vérifiées (supply chain), monter le Docker socket dans un container (c'est comme donner les clés de l'hôte), ne pas mettre de Network Policies (par défaut tous les Pods se parlent), et stocker des secrets en clair dans les manifests Kubernetes.

- **Question :** C'est quoi Docker Compose et dans quel cas on l'utilise ?
  - **Réponse type :** Docker Compose permet de définir et lancer plusieurs containers ensemble via un fichier YAML. Typiquement, une application avec un backend, une base de données et un cache Redis. On décrit les services, les réseaux et les volumes dans un docker-compose.yml, et un seul `docker compose up` lance tout. C'est surtout utilisé en développement et en environnement de test.

- **Question :** Comment fonctionne le RBAC dans Kubernetes ?
  - **Réponse type :** Le RBAC (Role-Based Access Control) contrôle qui peut faire quoi dans le cluster. On définit des Roles (permissions sur un namespace) ou ClusterRoles (permissions globales), puis on les lie à des utilisateurs ou des Service Accounts via des RoleBindings. Le principe c'est le moindre privilège : on ne donne que les droits strictement nécessaires.

## Questions les plus probables en entretien

1. Différence container vs VM ?
2. Comment sécuriser une image Docker ?
3. Pourquoi Kubernetes ? Quels objets essentiels ?
4. Quels risques de sécurité avec les containers ?
5. C'est quoi un Dockerfile, un Pod, un Deployment, un Service ?

## Réponses flash

- **Container vs VM** → Container = partage kernel, léger, rapide, isolation moindre. VM = OS complet, plus lourd, isolation forte.
- **Image** → Template read-only, construit via Dockerfile, chaque instruction = une layer.
- **Sécurité image** → Image minimale, multi-stage, non-root, scan Trivy, pas de secrets, signature Cosign.
- **Kubernetes** → Orchestrateur : scaling, self-healing, rolling updates, load balancing sur un cluster.
- **Objets K8s** → Pod (unité de base), Deployment (scaling/déploiement), Service (réseau stable), Namespace (isolation logique).
- **Risques sécu** → Root dans container, images vulnérables, Docker socket monté, pas de Network Policy, secrets en clair.
- **RBAC K8s** → Roles + RoleBindings, moindre privilège, pas de cluster-admin sauf admins.

---

# Conclusion

Tu as maintenant une compréhension solide de l’écosystème containers — de la théorie à la pratique, de Docker à Kubernetes, de l’utilisation à la sécurisation.

**Pour continuer à progresser :**

- Monte un lab avec minikube et déploie tes propres applications
- Passe la CKA si tu vises un poste DevOps/SRE
- Passe la CKS si tu vises un poste sécurité cloud/containers
- Suis KubeCon sur YouTube pour rester à jour
- Lis le code des Helm charts et des operators pour comprendre les patterns avancés

L’écosystème containers est vaste et en constante évolution. Ce cours t’a donné les fondations solides pour y naviguer — le reste viendra avec la pratique.
