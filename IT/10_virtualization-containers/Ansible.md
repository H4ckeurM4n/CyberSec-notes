# Ansible pour débutant

## Automatiser l'administration de machines Linux pas à pas

---

> **Prérequis :** quelques bases en Linux (se déplacer dans les dossiers, éditer un fichier, lancer une commande) et savoir ouvrir un **terminal**. Le SSH est **rappelé dans le cours**. **Aucune** connaissance d'Ansible, de DevOps, de cloud ou d'« infrastructure as code » n'est nécessaire.
> Tout ce dont tu as besoin, c'est un petit **lab de machines virtuelles Linux** : une machine de contrôle et deux ou trois cibles, sous VirtualBox ou VMware.

---

## À qui s'adresse ce cours

- À un **débutant complet** en Ansible.
- À quelqu'un qui connaît **un peu Linux** et sait ouvrir un terminal.
- À quelqu'un qui a **déjà utilisé SSH**, ou qui va l'apprendre ici.
- À toute personne qui veut **automatiser l'administration de plusieurs machines Linux** sans répéter les mêmes commandes une par une.

## Ce que tu sauras faire à la fin

- Comprendre **à quoi sert Ansible** et le principe de l'**état souhaité**.
- Monter un **lab** (contrôle + cibles) et te connecter en **SSH par clé**.
- Décrire tes machines dans un **inventaire** et lancer des **commandes ad hoc**.
- Lire les **sorties** d'Ansible (`ok`, `changed`, `failed`, `skipped`, `unreachable`) et comprendre l'**idempotence**.
- Écrire des **playbooks** en YAML, lisibles et rejouables.
- Utiliser les **modules** essentiels : paquets, services, fichiers, utilisateurs.
- Rendre tes playbooks adaptables avec **variables**, **facts**, **conditions** et **boucles**.
- Générer de la configuration avec des **templates Jinja2** et redémarrer proprement avec des **handlers**.
- Protéger tes secrets avec **Ansible Vault**.
- **Organiser** un projet Ansible propre et créer un **role** simple.

---

## Comment penser Ansible (l'idée en une image)

Si tu ne retiens qu'une chose de ce cours, c'est ceci :

```
   TU DÉCRIS                 ANSIBLE COMPARE              ANSIBLE AGIT
   l'état souhaité     →     ce qui est déjà fait   →     seulement si nécessaire
   "nginx installé"          "nginx est-il là ?"          "non → je l'installe"
                                                          "oui → je ne touche à rien"
```

Avec Ansible, tu ne décris **pas** une suite d'ordres (« installe, puis démarre, puis vérifie »). Tu décris un **résultat souhaité** (« nginx doit être installé et démarré »), et Ansible se débrouille pour y arriver — **et** pour ne **rien** refaire si c'est déjà bon.

Cette propriété (« rejouer ne casse rien, ne refait que ce qui manque ») s'appelle l'**idempotence**. C'est le cœur d'Ansible, et c'est ce qui le distingue d'un simple script. On y reviendra en détail (Partie 3).

---

## Les encadrés du cours

Pour t'aider, tu croiseras de temps en temps de petits encadrés :

- **🔍 Réflexe diagnostic** — quoi regarder quand « ça ne marche pas ».
- **🛡️ Réflexe sécurité** — un bon réflexe simple (protéger une clé, ne pas écrire un mot de passe en clair).
- **🔀 À ne pas confondre** — deux notions proches à bien distinguer.
- **🧪 Lab vs production** — ce qui est acceptable pour apprendre, mais pas sur de vraies machines en service.

Ils restent **légers** : ce cours est un cours **débutant**, pas un cours d'expert.

---

## Sur la progression

Le cours est **très progressif**. On commence par comprendre (sans rien installer), puis on monte le lab, puis on agit **une commande à la fois**, et seulement ensuite on écrit des playbooks. Les notions plus avancées (variables, templates, roles) arrivent **quand tu es prêt**.

> **Conseil :** ne cherche pas à tout retenir par cœur. Le but est de comprendre le **cycle** : décrire un inventaire → agir → lire les sorties → écrire un playbook rejouable. Les commandes exactes, tu les retrouveras dans la cheat-sheet en annexe.

Ne te juge pas si un chapitre demande deux lectures. **La régularité compte plus que la vitesse.**

---

## Table des matières

**Partie 0 — Introduction** *(tu es ici)*

**Partie 1 — Préparer le lab**

**Partie 2 — Inventaire et premières commandes**

**Partie 3 — Comprendre les sorties et l'idempotence**

**Partie 4 — YAML et premiers playbooks**

**Partie 5 — Modules essentiels d'administration Linux**

**Partie 6 — Variables, facts, conditions et boucles**

**Partie 7 — Templates et handlers**

**Partie 8 — Bonnes pratiques débutant**

**Partie 9 — Ansible Vault et secrets**

**Partie 10 — Organiser un projet Ansible**

**Partie 11 — Roles simples**

**Partie 12 — Mini-projets pratiques (récapitulatif)**

**Annexes** — cheat-sheet, erreurs fréquentes, rappel YAML, rappel SSH, écosystème infra, roadmap

---
---

# PARTIE 0 — INTRODUCTION

> **Objectif de la partie :** comprendre à quoi sert Ansible et dans quel cas on l'utilise — **sans rien installer**. On pose juste les idées.

---

# Chapitre 0.1 — Pourquoi Ansible existe

## Le minimum à savoir

Imagine que tu administres **un** serveur Linux. Tu te connectes en SSH, tu installes un paquet, tu modifies un fichier de configuration, tu redémarres un service. Cinq minutes, c'est réglé.

Maintenant, imagine que tu as **vingt** serveurs. La même tâche, vingt fois. À la main. Tu te connectes, tu tapes, tu recommences. C'est **long**, c'est **fastidieux**, et surtout : à la machine n°13, tu oublies une étape. Personne ne le remarque. Trois mois plus tard, cette machine se comporte différemment des autres, et personne ne sait pourquoi.

Ce problème porte un nom : la **dérive de configuration**. Des machines censées être identiques qui **divergent** lentement, parce qu'elles ont été modifiées à la main, à des moments différents, par des personnes différentes.

**Ansible existe pour résoudre exactement ça.** Au lieu de répéter les mêmes gestes machine par machine, tu **décris une fois** ce que tu veux, et Ansible l'applique à **toutes** les machines, de façon **identique** et **rejouable**.

> **En une phrase :** Ansible automatise l'administration de plusieurs machines, pour que tu ne répètes pas les mêmes commandes une par une, et pour que tes machines restent **cohérentes** dans le temps.

## Très utile en pratique

Voici les corvées d'admin que tu fais (ou ferais) à la main, et ce qu'Ansible change :

| À la main | Avec Ansible |
|-----------|--------------|
| Se connecter à chaque serveur pour installer un paquet | Une description, appliquée à toutes les machines |
| Refaire la même config sur 20 serveurs | Le même playbook, rejoué partout |
| Oublier une étape sur une machine | L'état décrit est appliqué **partout** pareil |
| Ne plus savoir quelles machines sont à jour | Rejouer pour **vérifier** et **corriger** d'un coup |

Tu n'as **rien à taper** dans ce chapitre. C'est de la mise en place mentale.

## Exemple simple

Sans Ansible, pour installer `htop` sur trois serveurs, tu ferais :

```bash
ssh serveur1     # puis : sudo apt install htop, puis exit
ssh serveur2     # puis : sudo apt install htop, puis exit
ssh serveur3     # puis : sudo apt install htop, puis exit
```

Avec Ansible, tu écriras **une seule** instruction qui s'applique aux trois d'un coup. Et si `htop` est déjà installé sur le serveur 2, Ansible le **constatera** et ne fera rien sur celui-là. C'est ça, l'idée de départ.

## ❌ Erreur classique

> **Croire qu'Ansible sert juste à « lancer une commande à distance plus vite ».**

C'est un raccourci trompeur. Lancer une commande sur plusieurs machines, une boucle SSH le fait aussi. Ce qu'Ansible apporte en plus, c'est l'**état souhaité** et l'**idempotence** : tu décris un **résultat** que tu peux **rejouer sans risque**, pas une commande à exécuter une fois. On verra la différence concrète très vite.

## Exercices

### Guidé
Sur une feuille (ou un fichier texte), écris **3 tâches** que tu fais ou ferais à la main pour administrer un serveur Linux (par exemple : « installer un paquet », « créer un utilisateur », « démarrer un service »). Pour chacune, imagine que tu doives la faire sur **10 machines** : note ce qui devient pénible ou risqué.

### Autonome
Décris en quelques lignes une situation (vécue ou imaginée) où **deux machines censées être identiques** se sont mises à se comporter différemment. Qu'est-ce qui a divergé ? Comment l'aurais-tu remarqué ?

### Défi
Explique à un proche **non technique**, en 4-5 phrases, ce que fait Ansible — **sans** utiliser les mots « playbook » ni « serveur ». Utilise une image (une recette qu'on rejoue à l'identique, un chef qui donne les mêmes instructions à toute une brigade…).

## ✅ Tu sais maintenant…

- **Pourquoi** Ansible existe : éviter de répéter les tâches d'admin machine par machine.
- Ce qu'est la **dérive de configuration** (des machines identiques qui divergent).
- Qu'Ansible applique un **état souhaité**, de façon **identique** et **rejouable**.
- Qu'Ansible n'est **pas** seulement « lancer des commandes à distance ».

---

# Chapitre 0.2 — L'idée d'Ansible : l'état souhaité

## Le minimum à savoir

Voici la différence la plus importante à comprendre, et elle est simple.

Un **script** (en Bash, par exemple) est une **liste d'ordres** : « fais ceci, puis cela ». Il exécute, point. Si tu le relances, il refait tout — même ce qui était déjà fait. Et parfois, ça casse (par exemple, créer un utilisateur qui existe déjà provoque une erreur).

Ansible fonctionne autrement. Tu décris un **état souhaité** : « cet utilisateur **doit exister** », « ce paquet **doit être installé** », « ce service **doit tourner** ». Ansible regarde la machine, **compare** avec ce que tu as demandé, et n'agit **que** s'il y a un écart.

```
   SCRIPT (impératif)              ANSIBLE (état souhaité)
   "crée l'utilisateur bob"        "l'utilisateur bob doit exister"
   → erreur si bob existe déjà     → bob existe ? rien à faire.
                                     bob absent ? je le crée.
```

> **L'idée clé :** tu ne dis pas **comment** faire étape par étape, tu dis **ce que tu veux obtenir**. Ansible se charge d'y arriver, et de **ne rien refaire inutilement**.

## Très utile en pratique

Cette façon de penser change tout :

- Tu peux **rejouer** une description autant de fois que tu veux, sans crainte.
- Tu peux l'appliquer à **une** machine ou à **cent**, c'est la même description.
- Si une machine a **dévié**, rejouer la description la **ramène** à l'état voulu.

C'est pour ça qu'on dit qu'Ansible **maintient** un état, alors qu'un script **exécute** des ordres.

## Exemple simple

Une instruction Ansible typique ressemble à ça (ne t'inquiète pas de la syntaxe, on l'apprendra) :

```yaml
- name: S'assurer que nginx est installé
  ansible.builtin.apt:
    name: nginx
    state: present       # ← "present" = l'état souhaité : nginx DOIT être là
```

Remarque le mot **`present`** : tu ne dis pas « installe nginx », tu dis « nginx **doit être présent** ». Si c'est déjà le cas, Ansible ne fait rien. C'est subtil, mais c'est **toute** la philosophie.

## ❌ Erreur classique

> **Penser en « ordres à exécuter » au lieu de « résultat à obtenir ».**

Un débutant venant des scripts a le réflexe d'écrire « lance cette commande ». Ansible préfère « assure-toi que cet état est atteint ». Le réflexe correct : pour chaque tâche, demande-toi **« quel résultat je veux ? »** plutôt que **« quelle commande je tape ? »**. C'est ce changement d'état d'esprit qui rend Ansible puissant.

## Exercices

### Guidé
Reformule ces trois ordres en **états souhaités** :
- « installe le paquet git » → « le paquet git doit… »
- « démarre le service ssh » → « le service ssh doit… »
- « crée le dossier /opt/app » → « le dossier /opt/app doit… »

### Autonome
Explique avec tes mots la différence entre « exécuter une commande » et « décrire un état souhaité ». Donne un exemple où **relancer** un script poserait problème, mais où **relancer** une description Ansible ne poserait aucun problème.

### Défi
Le mot `state: present` a un opposé : `state: absent`. Sans encore connaître la syntaxe, devine ce que voudrait dire une tâche avec `state: absent` pour un paquet. En quoi est-ce, là aussi, un **état souhaité** plutôt qu'un ordre ?

## ✅ Tu sais maintenant…

- La différence entre un **script** (liste d'ordres) et Ansible (**état souhaité**).
- Que tu décris **ce que tu veux obtenir**, pas **comment** le faire étape par étape.
- Que cette approche rend les actions **rejouables** sans risque.
- Le sens d'un mot comme **`present`** (l'état voulu, pas l'ordre « installe »).

---

# Chapitre 0.3 — L'idempotence en une image

## Le minimum à savoir

Le mot fait peur, l'idée est simple. **Idempotent** veut dire : *qu'on l'applique une fois ou dix fois, le résultat est le même, et rejouer ne casse rien.*

Reprends l'idée de l'état souhaité. Si tu demandes « nginx doit être installé » :

- **1ʳᵉ fois** : nginx n'est pas là → Ansible l'installe. Il signale qu'il a **changé** quelque chose.
- **2ᵉ fois** : nginx est déjà là → Ansible **ne fait rien**. Il signale que tout était déjà **ok**.
- **3ᵉ, 4ᵉ, 100ᵉ fois** : toujours `ok`. Rien ne bouge.

```
   1er run :  [ nginx absent ]  →  Ansible installe  →  CHANGED  (j'ai agi)
   2e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
   3e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
```

> **C'est ça, l'idempotence :** tu peux rejouer une description Ansible autant de fois que tu veux. Elle n'agit **que** s'il y a un écart à corriger. Un script Bash avec `apt install`, lui, relancerait l'installation à chaque fois.

## Très utile en pratique

L'idempotence te donne une **tranquillité** énorme :

- Tu peux relancer un playbook **sans crainte** de tout casser ou dupliquer.
- Tu peux l'utiliser pour **vérifier** : si tout est `ok`, le parc est conforme ; si quelque chose passe en `changed`, c'est qu'une machine avait **dévié** et qu'Ansible l'a corrigée.

On reviendra **vraiment** dessus en Partie 3, avec une démonstration que tu feras toi-même. Pour l'instant, garde juste l'image.

## Exemple simple

Tu lances deux fois de suite la même description « htop doit être installé » :

```text
1er lancement →  changed   (Ansible a installé htop)
2e lancement →  ok         (htop était déjà là, rien à faire)
```

Si tu voyais `changed` **à chaque** relance, ce serait le signe que quelque chose n'est **pas** idempotent — un point qu'on apprendra à repérer.

## ❌ Erreur classique

> **Confondre « idempotent » avec « qui ne fait jamais rien ».**

Idempotent ne veut **pas** dire « passif ». Ansible **agit** quand il le faut (1ʳᵉ fois, ou quand une machine a dévié), et **se retient** quand tout est déjà bon. Le réflexe correct : voir l'idempotence comme « **agir juste ce qu'il faut, ni plus ni moins** ».

## Exercices

### Guidé
Pour chacune de ces actions, dis si elle est naturellement **idempotente** (rejouer ne change rien si c'est déjà fait) ou non :
- « s'assurer qu'un fichier contient une ligne précise »
- « ajouter une ligne à la fin d'un fichier à chaque exécution »
- « s'assurer qu'un utilisateur existe »

### Autonome
Explique en 3-4 phrases pourquoi l'idempotence rend Ansible **rassurant** à utiliser, comparé à un script qu'on hésite à relancer.

### Défi
Imagine un script qui crée un utilisateur avec la commande `useradd bob`. Que se passe-t-il si on le lance **deux fois** ? Et comment une approche en **état souhaité** (« bob doit exister ») évite-t-elle ce problème ?

## ✅ Tu sais maintenant…

- Ce que veut dire **idempotent** : rejouer donne le même résultat, sans rien casser.
- Qu'Ansible agit **seulement s'il y a un écart** (`changed`), sinon il ne fait rien (`ok`).
- Que l'idempotence rend les playbooks **rejouables sans crainte**.
- Qu'« idempotent » ne veut **pas** dire « passif » : Ansible agit **juste ce qu'il faut**.

---

# Chapitre 0.4 — Ansible dans l'écosystème infra (court)

## Le minimum à savoir

Tu entendras souvent parler d'Ansible **à côté** d'autres outils : Terraform, Docker, Kubernetes. Pour éviter toute confusion, voici **en bref** qui fait quoi. Ce n'est **pas** un comparatif détaillé — juste de quoi situer Ansible.

| Outil | Ce qu'il fait | En une phrase |
|-------|---------------|---------------|
| **Ansible** | **Configure** des machines qui existent déjà | installer, paramétrer, administrer |
| **Terraform** | **Provisionne / crée** l'infrastructure | faire naître des serveurs, des réseaux |
| **Docker** | **Package** une application en conteneur | emballer une app et ses dépendances |
| **Kubernetes** | **Orchestre** des conteneurs | faire tourner beaucoup de conteneurs à l'échelle |

> **À retenir :** ces outils sont **complémentaires**, pas concurrents. Un parcours courant : Terraform **crée** les serveurs → Ansible les **configure** → Docker/Kubernetes y **font tourner** les applications. **Mais ce cours reste centré sur Ansible** : configurer des machines Linux existantes.

## Très utile en pratique

La seule chose à retenir pour la suite : **Ansible travaille sur des machines qui existent déjà**. On ne lui demande pas de **créer** des serveurs (c'est le rôle de Terraform), ni de **packager** des applications (c'est Docker). On lui demande de **configurer** et **administrer** les machines de notre lab.

## 🔀 À ne pas confondre

> **« Configurer » (Ansible) ≠ « Créer » (Terraform).**
> Ansible suppose que la machine **existe** et qu'on peut s'y connecter en SSH. Il l'**administre**. Il ne la fait pas apparaître.

## ❌ Erreur classique

> **Vouloir « tout faire avec Ansible », y compris créer des machines.**

Le débutant enthousiaste essaie parfois d'utiliser Ansible pour provisionner des serveurs (le rôle de Terraform). Ça mène à des montages bancals. Le réflexe correct : **Ansible configure l'existant**. Pour ce cours, nos machines existent déjà (on les crée à la main dans VirtualBox/VMware en Partie 1).

## Exercices

### Guidé
Associe chaque besoin à l'outil : (a) « créer 3 serveurs », (b) « installer et configurer nginx sur ces serveurs », (c) « emballer une application en conteneur », (d) « faire tourner 50 conteneurs ». Lequel relève d'**Ansible** ?

### Autonome
En 3 phrases, explique pourquoi ces outils sont **complémentaires** plutôt que concurrents, avec l'exemple Terraform → Ansible → Docker.

### Défi
Sans chercher à les approfondir, explique pourquoi un cours **débutant Ansible** a raison de **ne pas** se disperser sur Terraform, Docker et Kubernetes en détail. Que gagne-t-on à rester focalisé ?

## ✅ Tu sais maintenant…

- Qu'Ansible **configure des machines existantes**.
- Que **Terraform** crée l'infra, **Docker** package les apps, **Kubernetes** orchestre les conteneurs.
- Que ces outils sont **complémentaires**, mais que **ce cours reste centré sur Ansible**.
- Que nos machines de lab **existent déjà** (on ne les crée pas avec Ansible).

---

## 🚩 Checkpoint — Fin de la Partie 0

Avant de monter le lab, assure-toi de pouvoir :

- [ ] Expliquer **pourquoi Ansible existe** (éviter la répétition, lutter contre la dérive de config).
- [ ] Dire ce qu'est un **état souhaité** (décrire un résultat, pas une suite d'ordres).
- [ ] Expliquer l'**idempotence** avec tes mots (rejouer ne change rien si c'est déjà fait).
- [ ] Situer Ansible : il **configure** des machines existantes (≠ Terraform/Docker/Kubernetes).

> **La suite :** en Partie 1, on **construit le lab** — une machine de contrôle et deux cibles Linux — et on établit la connexion **SSH par clé**. C'est le terrain sur lequel tu vas tout pratiquer.

---
---

# PARTIE 1 — PRÉPARER LE LAB

> **Objectif de la partie :** mettre en place l'environnement d'apprentissage et **valider la connexion** avant de faire quoi que ce soit avec Ansible. Un lab solide t'évitera des heures de confusion plus tard.

---

# Chapitre 1.1 — Control node et machines cibles

## Le minimum à savoir

Ansible repose sur une distinction très simple :

```
   ┌─────────────────┐       SSH       ┌─────────────────┐
   │  MACHINE DE     │ ──────────────▶ │     CIBLE 1     │
   │  CONTRÔLE       │ ──────────────▶ │     CIBLE 2     │
   │  (Ansible ICI)  │ ──────────────▶ │   (Cible 3)     │
   └─────────────────┘                 └─────────────────┘
   Tu pilotes d'ici         Les machines administrées
```

- La **machine de contrôle** (*control node*) : c'est là, et **seulement** là, qu'on **installe Ansible**. C'est ton poste de pilotage.
- Les **machines cibles** (*managed nodes*) : ce sont les machines qu'Ansible **administre**. On **n'installe pas** Ansible dessus.

### Le point qui surprend : « agentless »

Ansible n'installe **aucun programme permanent** sur les cibles. On dit qu'il est **agentless** (sans agent). Il se connecte en **SSH** (comme tu le ferais à la main), fait son travail en s'appuyant sur **Python** (déjà présent sur la plupart des Linux), puis se déconnecte. Rien ne reste installé sur les cibles.

> **Conséquence pratique :** si une machine est accessible en **SSH** et qu'elle a **Python**, Ansible peut l'administrer **immédiatement**. Pas de déploiement d'agent, pas de configuration lourde sur les cibles.

## Très utile en pratique

Sur la **machine de contrôle**, une seule commande confirmera (plus tard) qu'Ansible est là :

```bash
ansible --version
```

Sur les **cibles**, tu ne vérifies **pas** « si Ansible est installé » (il ne l'est pas, et c'est normal). Tu vérifieras seulement qu'elles répondent en **SSH** — c'est l'objet des chapitres suivants.

## Exemple simple

Le lab de ce cours, c'est :

```text
control   → 1 VM Linux, on y installe Ansible
cible1    → 1 VM Linux, rien à installer
cible2    → 1 VM Linux, rien à installer
(cible3)  → optionnelle, pour s'entraîner aux groupes plus tard
```

Trois petites VMs Linux sur ton ordinateur, reliées par un réseau local. C'est tout.

## 🔀 À ne pas confondre

> **« Agentless » ne veut pas dire « rien sur les cibles ».**
> Les cibles ont besoin de **SSH** (pour la connexion) et de **Python** (pour exécuter le travail). Simplement, il n'y a **pas d'agent Ansible** à installer et à maintenir.

## ❌ Erreur classique

> **Vouloir « installer Ansible sur les machines cibles ».**

Si tu viens d'outils qui posent un agent partout, tu pourrais croire qu'il faut installer Ansible sur chaque cible. **C'est inutile.** Le réflexe correct : **Ansible s'installe uniquement sur la machine de contrôle**. Les cibles n'ont besoin que de SSH et Python. Si tu te surprends à vouloir installer Ansible sur « cible1 », arrête-toi : ce n'est pas comme ça que ça marche.

## Exercices

### Guidé
Sur une feuille, dessine ton futur lab : une machine de contrôle, deux cibles, et des flèches **SSH** qui partent du contrôle vers les cibles. Écris « Ansible installé ici » sur la machine de contrôle, et « SSH + Python » sur les cibles.

### Autonome
Explique avec tes mots ce que veut dire **agentless**, et donne **un avantage** concret pour quelqu'un qui doit administrer beaucoup de machines.

### Défi
Pourquoi est-ce pratique qu'Ansible utilise **SSH** plutôt qu'un protocole spécial à lui ? (Indice : pense à ce que tu sais déjà faire avec SSH, et à ce qui est déjà en place sur tes serveurs Linux.)

## ✅ Tu sais maintenant…

- La distinction **machine de contrôle** (Ansible installé) vs **cibles** (rien d'installé).
- Ce que veut dire **agentless** : pas d'agent permanent, juste **SSH + Python** sur les cibles.
- Qu'Ansible s'installe **uniquement** sur la machine de contrôle.
- À quoi ressemble le lab du cours (1 contrôle + 2-3 cibles Linux).

---

# Chapitre 1.2 — SSH et clés

## Le minimum à savoir

Ansible n'a pas de « canal magique ». Il utilise **SSH**, exactement le même que celui que tu utilises pour te connecter à un serveur à la main. **C'est la fondation de tout le cours.**

La règle d'or :

> **Si `ssh utilisateur@cible` marche à la main, alors Ansible marchera. Si SSH ne marche pas, Ansible ne marchera pas non plus.** SSH d'abord, Ansible ensuite.

### Mot de passe ou clé ?

On peut se connecter en SSH par **mot de passe**, mais pour Ansible (et pour le confort), on utilise des **clés SSH**. Une clé SSH, c'est une **paire** :

- une **clé privée**, qui reste **secrète** sur la machine de contrôle ;
- une **clé publique**, qu'on **dépose** sur chaque cible.

Une fois la clé publique déposée, tu te connectes **sans taper de mot de passe** : la cible reconnaît ta clé.

```
   MACHINE DE CONTRÔLE                 CIBLE
   ┌──────────────────┐                ┌──────────────────┐
   │  clé PRIVÉE      │ ── prouve ───▶ │  clé PUBLIQUE    │
   │  (reste secrète) │   l'identité   │  (déposée ici)   │
   └──────────────────┘                └──────────────────┘
```

## Très utile en pratique

Les trois commandes à connaître (sur la **machine de contrôle**) :

```bash
# 1. Générer une paire de clés (si tu n'en as pas déjà)
ssh-keygen -t ed25519

# 2. Déposer la clé publique sur une cible
ssh-copy-id utilisateur@192.168.56.11

# 3. Vérifier qu'on se connecte SANS mot de passe
ssh utilisateur@192.168.56.11
```

Si la troisième commande t'ouvre une session **sans demander de mot de passe**, tout est prêt pour Ansible.

```text
$ ssh admin@192.168.56.11
Welcome to Ubuntu ...
admin@cible1:~$        ← connecté sans mot de passe : parfait
```

## Exemple simple

Tu génères ta clé une fois, puis tu la déposes sur chaque cible :

```bash
ssh-keygen -t ed25519                       # une seule fois, sur le contrôle
ssh-copy-id admin@192.168.56.11             # cible1
ssh-copy-id admin@192.168.56.12             # cible2
ssh admin@192.168.56.11                     # test : doit marcher sans mot de passe
```

## 🛡️ Réflexe sécurité

> La **clé privée** reste sur la machine de contrôle et **ne se partage jamais**. C'est elle qui ouvre l'accès à tes cibles. Traite-la comme un trousseau de clés : on ne le laisse pas traîner, on ne l'envoie pas par mail. (On reparlera de protéger les secrets en Partie 9.)

## ❌ Erreur classique

> **Essayer de faire marcher Ansible alors que SSH ne marche pas encore à la main.**

C'est **l'**erreur n°1 du débutant. On lance Ansible, ça échoue, et on cherche le problème dans Ansible… alors qu'il est dans **SSH** (mauvaise clé, mauvais utilisateur, machine pas joignable). Le réflexe correct : **toujours tester `ssh utilisateur@cible` à la main d'abord**. Si la connexion manuelle échoue, Ansible échouera aussi — Ansible ne **répare** pas SSH, il s'**appuie** dessus.

## Exercices

### Guidé
Sur ta machine de contrôle, génère une paire de clés avec `ssh-keygen -t ed25519`. Dépose la clé publique sur **une** cible avec `ssh-copy-id`. Connecte-toi ensuite avec `ssh utilisateur@cible` et vérifie que **tu n'as pas à taper de mot de passe**.

### Autonome
Explique avec tes mots la différence entre la **clé privée** et la **clé publique** : laquelle reste secrète, laquelle se distribue, et pourquoi ce système permet de se connecter sans mot de passe.

### Défi
Fais le test sur la **deuxième** cible. Puis, depuis la machine de contrôle, connecte-toi successivement aux deux cibles. Si l'une demande un mot de passe et pas l'autre, trouve **pourquoi** (la clé publique a-t-elle bien été déposée sur les deux ?).

## ✅ Tu sais maintenant…

- Qu'Ansible utilise **SSH**, et que **SSH doit marcher avant Ansible**.
- Le principe d'une **paire de clés** : privée (secrète, sur le contrôle) / publique (déposée sur les cibles).
- Générer et déposer une clé : `ssh-keygen`, `ssh-copy-id`, test avec `ssh`.
- Que la **clé privée** ne se partage jamais.

---

# Chapitre 1.3 — Installer Ansible

## Le minimum à savoir

On installe Ansible **uniquement sur la machine de contrôle**. Les cibles, elles, n'ont besoin de rien (juste SSH + Python, déjà vus).

Il y a deux façons courantes d'installer Ansible sur un Linux :

1. **Via le gestionnaire de paquets** de ta distribution — simple, parfait pour un lab.
2. **Via `pipx`** — installe Ansible dans un environnement isolé, plus propre et à jour.

> Les commandes d'installation **évoluent** avec le temps et dépendent de ta distribution. En cas de doute, la **documentation officielle d'Ansible fait foi**. Voici les deux approches générales :

## Très utile en pratique

```bash
# Option 1 — simple, pour un lab (familles Debian/Ubuntu)
sudo apt update && sudo apt install -y ansible

# Option 2 — propre et isolée (recommandée si tu connais un peu Python)
pipx install --include-deps ansible

# Vérifier que c'est installé (sur la machine de contrôle)
ansible --version
```

`ansible --version` doit afficher un numéro de version. Si la commande est introuvable, c'est qu'Ansible n'est pas (encore) installé, ou pas dans le `PATH`.

## Exemple simple

```text
$ ansible --version
ansible [core 2.x.x]
  config file = ...
  python version = 3.x.x ...
```

Cet affichage = Ansible est prêt sur ta machine de contrôle.

## 🔀 À ne pas confondre

> **Installer Ansible (sur le contrôle) ≠ préparer les cibles.**
> Tu installes Ansible **une seule fois**, sur la machine de contrôle. Tu n'installes **rien** sur les cibles. Si tu te retrouves à lancer `apt install ansible` sur « cible1 », c'est une erreur.

## ❌ Erreur classique

> **Installer Ansible sur les cibles, ou s'attendre à un décalage de version.**

Deux pièges fréquents. D'abord, installer Ansible partout (inutile : seul le contrôle en a besoin). Ensuite, s'étonner que la version du paquet de la distribution soit un peu ancienne — c'est normal. Pour un lab, ce n'est pas grave. Si tu veux la version la plus récente, l'option `pipx` est préférable. Le réflexe correct : **Ansible sur le contrôle uniquement**, et la **doc officielle** comme référence en cas de doute.

## Exercices

### Guidé
Installe Ansible sur ta machine de contrôle (choisis l'option `apt` ou `pipx`). Lance `ansible --version` et vérifie qu'un numéro de version s'affiche. Note la commande qui a fonctionné pour ta distribution.

### Autonome
Connecte-toi à une de tes **cibles** et lance `ansible --version`. Que se passe-t-il ? Explique pourquoi c'est **normal** que la commande ne soit pas trouvée sur la cible.

### Défi
Compare les deux méthodes d'installation (`apt` vs `pipx`) en une ou deux phrases chacune : avantage principal de chacune pour un débutant. Laquelle choisirais-tu et pourquoi ?

## ✅ Tu sais maintenant…

- Qu'on installe Ansible **uniquement sur la machine de contrôle**.
- Les deux méthodes courantes : **paquet de la distribution** (`apt`) ou **`pipx`** (isolé).
- Vérifier l'installation avec **`ansible --version`**.
- Que la version du paquet peut être un peu ancienne (normal pour un lab).

---

# Chapitre 1.4 — Snapshots et erreurs SSH classiques

## Le minimum à savoir

Avant de commencer à « casser » des choses en apprenant, mets en place ton **filet de sécurité** : les **snapshots**.

Un **snapshot** (instantané) est une **photo** de l'état d'une VM à un moment donné. Si un essai casse une cible, tu **restaures** le snapshot et tu repars de l'état sain en quelques secondes. VirtualBox et VMware proposent tous les deux cette fonction.

> 🧪 **Lab vs production :** en lab, les snapshots te donnent une **liberté totale** d'expérimenter. Tu tentes, tu observes, et si ça tourne mal, tu restaures. C'est exactement ce qui rend l'apprentissage **serein**. (En production, on n'a pas ce confort — d'où l'importance d'apprendre **maintenant**, en lab.)

### Les erreurs SSH les plus fréquentes

Comme Ansible passe par SSH, les premiers blocages viennent presque toujours de là :

| Message / symptôme | Cause probable | Quoi vérifier |
|--------------------|----------------|---------------|
| `Permission denied` | Mauvaise clé ou mauvais utilisateur | La clé publique est-elle déposée ? Bon utilisateur ? |
| `Connection refused` / timeout | Cible éteinte, mauvaise IP, réseau | La VM tourne ? La bonne IP ? Même réseau ? |
| Demande de mot de passe | Clé publique pas déposée | Refaire `ssh-copy-id` |
| `Host key verification failed` | Clé d'hôte changée (VM recréée) | Nettoyer l'ancienne entrée `known_hosts` |

## Très utile en pratique

```bash
# Tester la connexion à la main (TOUJOURS le premier réflexe)
ssh admin@192.168.56.11

# Voir plus de détails si ça échoue (verbeux)
ssh -v admin@192.168.56.11
```

> 🔍 **Réflexe diagnostic :** au moindre souci avec Ansible **au début du cours**, reviens à `ssh utilisateur@cible` à la main. Si ça échoue, le problème est dans **SSH/le réseau**, pas dans Ansible. Règle SSH d'abord.

## Exemple simple

Le bon ordre des opérations pour un lab sain :

```text
1. Les 3 VMs démarrent et se voient sur le réseau
2. SSH par clé fonctionne du contrôle vers chaque cible (testé à la main)
3. SNAPSHOT de chaque VM, nommé "lab-pret"   ← ton point de restauration
```

## ❌ Erreur classique

> **Monter un lab « presque bon » : pas de snapshot, réseau bancal, et chercher des bugs Ansible qui sont en réalité des bugs réseau.**

Sans snapshot, le moindre essai raté t'oblige à tout refaire. Et un réseau mal configuré transforme chaque exercice en chasse au bug qui n'a **rien à voir** avec Ansible. Le réflexe correct : **valider SSH à la main** sur chaque cible, **puis** prendre un snapshot « lab-pret » avant de continuer. Trente secondes de préparation t'épargnent des heures de frustration.

## Exercices

### Guidé
Une fois que SSH par clé fonctionne vers tes deux cibles, prends un **snapshot** de chaque VM (contrôle + cibles), nommé « lab-pret ». Tu viens de créer ton point de restauration.

### Autonome
Casse volontairement quelque chose sur une cible (par exemple, supprime la clé publique déposée, ou éteins la VM) et observe l'échec de `ssh`. Puis **restaure le snapshot** « lab-pret » et vérifie que la connexion refonctionne. Tu viens de tester ton filet de sécurité.

### Défi
Provoque une erreur `Host key verification failed` : recrée (ou réinitialise) une cible après t'y être déjà connecté, puis retente `ssh`. Lis le message. Sans forcément le résoudre, explique **pourquoi** SSH se méfie quand la clé d'hôte change (indice : c'est une protection de sécurité).

## ✅ Tu sais maintenant…

- Ce qu'est un **snapshot** et pourquoi il rend l'apprentissage **serein**.
- À prendre un snapshot **« lab-pret »** une fois SSH validé.
- Les **erreurs SSH** les plus fréquentes et quoi vérifier pour chacune.
- Le réflexe : au moindre souci, **tester `ssh` à la main d'abord**.

---

## 🚩 Checkpoint — Fin de la Partie 1

Ton lab est prêt. Avant de décrire ton parc et d'agir avec Ansible, assure-toi de pouvoir :

- [ ] Expliquer la différence **machine de contrôle** / **cibles**, et le principe **agentless**.
- [ ] Avoir **Ansible installé** sur la machine de contrôle (`ansible --version` répond).
- [ ] Te connecter en **SSH par clé** (sans mot de passe) à **chaque** cible.
- [ ] Comprendre que **SSH doit marcher avant Ansible**.
- [ ] Avoir pris un **snapshot « lab-pret »** de chaque VM.
- [ ] Reconnaître les **erreurs SSH** courantes et savoir tester `ssh` à la main.

> **🧩 Mini-projet 1 — « Le lab opérationnel ».**
> 1. Crée tes VMs : une machine de contrôle (avec Ansible) et deux cibles Linux, sur un réseau commun.
> 2. Génère une paire de clés sur le contrôle et dépose la clé publique sur **chaque** cible.
> 3. Vérifie `ssh utilisateur@cible` **sans mot de passe** vers les deux cibles.
> 4. Prends un **snapshot « lab-pret »** de chaque VM.
> Objectif : disposer d'un lab **fiable**, prêt pour la suite, avec le réflexe « je valide SSH à la main avant Ansible ».

> **La suite :** en Partie 2, on décrit nos machines dans un **inventaire**, et on lance nos **premières commandes ad hoc** avec Ansible — enfin de l'action ! On apprendra aussi à lire les premières **sorties** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).

---
---
---

# PARTIE 2 — INVENTAIRE ET PREMIÈRES COMMANDES

> **Objectif de la partie :** décrire tes machines dans un **inventaire**, puis **agir** dessus en une seule ligne avec les **commandes ad hoc**. On apprend aussi à **lire les sorties** d'Ansible — un réflexe essentiel pour la suite.

---

# Chapitre 2.1 — L'inventaire INI

## Le minimum à savoir

Avant d'agir sur des machines, Ansible doit **savoir lesquelles existent**. C'est le rôle de l'**inventaire** : un fichier qui **liste** tes machines et les **organise en groupes**.

Le format le plus simple pour débuter est le format **INI** :

```ini
# inventory.ini

[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[db]
cible3 ansible_host=192.168.56.13
```

- `[web]` et `[db]` sont des **groupes**.
- `cible1`, `cible2`, `cible3` sont des **hôtes** (les machines).
- `ansible_host=...` indique l'**adresse IP** réelle de connexion.

> **L'inventaire est la base de tout.** Toutes tes commandes et tous tes playbooks viseront un **hôte** ou un **groupe** défini ici. Un inventaire clair, c'est la moitié du travail.

### Le groupe `all`

Toutes les machines de l'inventaire appartiennent automatiquement à un groupe spécial : **`all`**. Cibler `all`, c'est cibler **toutes** les machines d'un coup.

> 💡 **Mention pour plus tard :** au début, on précise l'inventaire à chaque commande avec `-i inventory.ini`. C'est un peu répétitif. En **Partie 10**, on verra qu'un petit fichier `ansible.cfg` permet d'**éviter** de retaper `-i` à chaque fois. Pour l'instant, on garde le `-i` : c'est plus explicite pour comprendre.

## Très utile en pratique

```bash
# Visualiser l'inventaire tel qu'Ansible le comprend (vue en arbre)
ansible-inventory -i inventory.ini --graph
```

```text
@all:
  |--@web:
  |  |--cible1
  |  |--cible2
  |--@db:
  |  |--cible3
```

Cette vue `--graph` est ton **réflexe de vérification** : avant d'agir, tu regardes **qui est dans quel groupe**. C'est la meilleure protection contre l'erreur de cible.

## Exemple simple

Un inventaire minimal pour le lab du cours :

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12
```

Deux machines, un groupe `web`. C'est suffisant pour commencer.

## ❌ Erreur classique

> **Se tromper d'IP ou mettre un hôte dans le mauvais groupe.**

Une IP erronée dans `ansible_host`, et Ansible n'arrive pas à joindre la machine (ou en joint une autre !). Un hôte dans le mauvais groupe, et ta commande touche la mauvaise cible. Le réflexe correct : **vérifier l'inventaire avec `ansible-inventory --graph`** avant d'agir, et confirmer les IP avec un `ssh` à la main en cas de doute.

## Exercices

### Guidé
Crée un fichier `inventory.ini` décrivant tes deux cibles dans un groupe `web`, avec leurs vraies IP. Lance `ansible-inventory -i inventory.ini --graph` et vérifie que l'arbre correspond à ce que tu attendais.

### Autonome
Ajoute un groupe `db` avec une troisième machine (réelle ou fictive). Relance `--graph` et observe la nouvelle structure. Un hôte peut-il être dans plusieurs groupes ? Teste en mettant `cible1` à la fois dans `web` et dans un nouveau groupe `pilote`.

### Défi
Sans encore l'utiliser, ajoute une **variable de groupe** dans ton inventaire :
```ini
[web:vars]
http_port=80
```
Relance `ansible-inventory -i inventory.ini --graph --vars` (ou `--list`) et retrouve cette variable dans la sortie. On s'en servira au chapitre suivant.

## ✅ Tu sais maintenant…

- Que l'**inventaire** liste tes machines et les organise en **groupes**.
- Écrire un inventaire au format **INI** (hôtes, groupes, `ansible_host`).
- Que le groupe **`all`** désigne toutes les machines.
- Vérifier ton inventaire avec **`ansible-inventory --graph`**.
- Qu'on précise l'inventaire avec **`-i`** (et qu'`ansible.cfg` simplifiera ça plus tard).

---

# Chapitre 2.2 — Variables simples d'inventaire

## Le minimum à savoir

Parfois, une machine ou un groupe a besoin d'une **valeur particulière** : un port, un nom, un utilisateur de connexion. On peut le préciser **directement dans l'inventaire**, avec des **variables**.

### Variables d'un hôte

```ini
[web]
cible1 ansible_host=192.168.56.11 ansible_user=admin
```

Ici, `ansible_user=admin` dit à Ansible de se connecter en tant qu'`admin` sur cette machine.

### Variables d'un groupe

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[web:vars]
ansible_user=admin
http_port=80
```

`[web:vars]` définit des variables pour **toutes** les machines du groupe `web`.

> **Quelques variables spéciales utiles** (Ansible les reconnaît automatiquement) : `ansible_host` (l'IP), `ansible_user` (l'utilisateur SSH), `ansible_port` (le port SSH si différent de 22).

## Très utile en pratique

```bash
# Voir toutes les variables effectives d'un hôte
ansible-inventory -i inventory.ini --host cible1
```

```text
{
    "ansible_host": "192.168.56.11",
    "ansible_user": "admin",
    "http_port": 80
}
```

Cette commande est précieuse : elle te montre **exactement** quelles valeurs s'appliquent à une machine.

## Exemple simple

```ini
[web]
cible1 ansible_host=192.168.56.11
cible2 ansible_host=192.168.56.12

[web:vars]
ansible_user=admin
```

Les deux machines du groupe `web` se connecteront avec l'utilisateur `admin`.

## 🔀 À ne pas confondre

> **Variable d'hôte vs variable de groupe.**
> Une variable mise sur une **ligne d'hôte** ne concerne **que** cette machine. Une variable dans `[groupe:vars]` concerne **toutes** les machines du groupe. Si les deux définissent la même variable, c'est la plus **spécifique** (l'hôte) qui l'emporte.

## ❌ Erreur classique

> **Mettre une variable au mauvais endroit et obtenir une valeur inattendue.**

Tu définis `ansible_user=admin` pour le groupe, mais une ligne d'hôte précise `ansible_user=root` : sur cette machine, ce sera `root`, et tu ne comprends pas pourquoi. Le réflexe correct : utiliser **`ansible-inventory --host <machine>`** pour voir la **valeur réellement appliquée**.

## Exercices

### Guidé
Ajoute `ansible_user=<ton_utilisateur>` en variable de groupe `[web:vars]`. Lance `ansible-inventory -i inventory.ini --host cible1` et vérifie que `ansible_user` apparaît bien.

### Autonome
Ajoute une variable `http_port=8080` à **une seule** machine (sur sa ligne d'hôte), tout en gardant `http_port=80` dans `[web:vars]`. Avec `--host`, vérifie quelle valeur gagne sur cette machine, et laquelle gagne sur l'autre.

### Défi
Explique en quelques lignes l'intérêt de définir `ansible_user` dans l'inventaire plutôt que de le retaper à chaque commande. Quel lien fais-tu avec le futur fichier `ansible.cfg` (Partie 10) ?

## ✅ Tu sais maintenant…

- Définir des **variables** d'hôte (sur la ligne) et de groupe (`[groupe:vars]`).
- Les variables spéciales utiles : `ansible_host`, `ansible_user`, `ansible_port`.
- Voir les valeurs effectives avec **`ansible-inventory --host`**.
- Que la variable la plus **spécifique** (hôte) l'emporte sur celle du groupe.

---

# Chapitre 2.3 — Le ping et les commandes ad hoc

## Le minimum à savoir

Une **commande ad hoc** est une action Ansible lancée **directement en ligne de commande**, sans écrire de fichier. C'est parfait pour une action **ponctuelle** : vérifier que les machines répondent, lancer une commande rapide.

La structure d'une commande ad hoc :

```
ansible  <cible>  -m <module>  -a "<arguments>"
         ▲        ▲            ▲
         groupe   le module    les arguments
         ou hôte  à exécuter   du module
```

### Le premier réflexe : `ping`

Le tout premier test, c'est de vérifier qu'Ansible **joint** ses cibles, avec le module `ping` :

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```

> 🔀 **À ne pas confondre :** le `ping` d'Ansible n'est **pas** le `ping` réseau habituel (ICMP). Il vérifie qu'Ansible peut **se connecter en SSH** à la machine **et** y exécuter du Python. Un `ping` Ansible réussi prouve que **toute la chaîne fonctionne**.

### Une note sur les noms de modules (FQCN)

Tu remarques qu'on écrit `ansible.builtin.ping` et pas juste `ping`. C'est le **nom complet** du module (on parle de **FQCN**). On l'utilise pour **éviter les ambiguïtés** entre modules de même nom. Retiens simplement : **on écrit le nom complet `ansible.builtin.xxx`**. Pas besoin d'en savoir plus pour l'instant.

## Très utile en pratique

```bash
# Pinguer toutes les machines
ansible all -i inventory.ini -m ansible.builtin.ping

# Pinguer un seul groupe
ansible web -i inventory.ini -m ansible.builtin.ping

# Lancer une commande simple (lecture, sans danger)
ansible all -i inventory.ini -m ansible.builtin.command -a "uptime"

# Voir l'espace disque de chaque machine
ansible web -i inventory.ini -m ansible.builtin.command -a "df -h /"
```

```text
$ ansible all -i inventory.ini -m ansible.builtin.ping
cible1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
cible2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

`SUCCESS` + `"ping": "pong"` = la machine est joignable et opérationnelle. C'est le feu vert.

## Exemple simple

```bash
# "Est-ce que mes deux cibles répondent ?"
ansible web -i inventory.ini -m ansible.builtin.ping
```

Si les deux répondent `SUCCESS`, ton lab est prêt à travailler.

## ❌ Erreur classique

> **Un `ping` qui échoue avec `UNREACHABLE`, et chercher le problème dans Ansible.**

Si `ping` renvoie `UNREACHABLE`, le souci est dans la **connexion SSH**, pas dans Ansible (mauvaise IP, mauvaise clé, mauvais utilisateur, machine éteinte). Le réflexe correct : tester **`ssh utilisateur@cible` à la main**. Si ça échoue aussi, règle SSH d'abord (rappel : Partie 1).

## Exercices

### Guidé
Lance `ansible all -i inventory.ini -m ansible.builtin.ping`. Tes deux cibles doivent répondre `SUCCESS` / `pong`. Si l'une affiche `UNREACHABLE`, teste `ssh` à la main vers cette machine et corrige.

### Autonome
Avec le module `command`, récupère l'`uptime` (depuis quand la machine tourne) et l'espace disque (`df -h /`) de chaque cible. Tu viens de faire un petit **état des lieux** de ton parc en deux commandes.

### Défi
Cible **une seule** machine au lieu d'un groupe entier : `ansible cible1 -i inventory.ini -m ansible.builtin.ping`. Puis essaie de cibler le groupe `web` mais en te limitant à une machine. (Indice : il existe une option `--limit`. On la verra plus en détail en Partie 8.)

## ✅ Tu sais maintenant…

- Ce qu'est une **commande ad hoc** : agir en une ligne, sans playbook.
- La structure `ansible <cible> -m <module> -a "<args>"`.
- Le module **`ping`** comme premier test (SSH + Python), différent du ping réseau.
- Qu'on écrit les modules en **nom complet** (`ansible.builtin.xxx`).
- Lancer des commandes de lecture (`uptime`, `df`).

---

# Chapitre 2.4 — `command` et `shell`

## Le minimum à savoir

Ansible propose deux modules pour lancer une commande « brute » sur les cibles :

- **`ansible.builtin.command`** : exécute une commande **simple**, sans passer par un shell complet.
- **`ansible.builtin.shell`** : exécute une commande **via un shell**, ce qui permet les `|`, `>`, `&&`, etc.

```bash
# command : commande simple
ansible web -i inventory.ini -m ansible.builtin.command -a "hostname"

# shell : nécessaire pour les redirections, pipes, etc.
ansible web -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY"
```

> **Règle simple :** utilise **`command`** par défaut. Passe à **`shell`** seulement si tu as besoin des fonctionnalités du shell (pipes `|`, redirections `>`, `&&`). `shell` est un peu plus puissant, mais aussi un peu moins sûr (il interprète tout).

## Très utile en pratique

```bash
# command suffit pour une commande simple
ansible all -i inventory.ini -m ansible.builtin.command -a "whoami"

# shell est nécessaire ici (à cause du pipe)
ansible all -i inventory.ini -m ansible.builtin.shell -a "ps aux | grep ssh"
```

## Exemple simple

```bash
# "Quelle est la version de l'OS sur chaque machine ?"
ansible all -i inventory.ini -m ansible.builtin.shell -a "cat /etc/os-release | grep PRETTY_NAME"
```

(On utilise `shell` ici à cause du `|`.)

## 🔀 À ne pas confondre

> **`command` (simple) vs `shell` (avec shell).**
> `command` ne comprend **pas** les `|`, `>`, `&&` — si tu en as besoin, il faut `shell`. Inversement, pour une commande simple, **préfère `command`** : c'est plus prévisible.

## ❌ Erreur classique

> **Tout faire en `command`/`shell`, même quand un module dédié existe.**

On pourrait être tenté de tout faire avec `shell` : `shell -a "apt install htop"`, `shell -a "systemctl start nginx"`. Mais c'est une **mauvaise habitude** : ces commandes ne sont **pas idempotentes** (relancer relance l'action) et contournent toute l'intelligence d'Ansible. Le réflexe correct : pour installer un paquet, gérer un service, copier un fichier… **utilise le module dédié** (qu'on verra en Partie 5). Garde `command`/`shell` pour ce qui n'a **pas** de module dédié. On comprendra **pourquoi** en détail dès la Partie 3.

## Exercices

### Guidé
Lance une commande simple avec `command` (par exemple `hostname` ou `whoami`) sur tout le parc. Observe la sortie pour chaque machine.

### Autonome
Essaie de lancer une commande avec un **pipe** (`|`) en utilisant `command`. Observe que ça échoue ou se comporte mal. Refais-la avec `shell`. Tu comprends ainsi quand `shell` est nécessaire.

### Défi
Sans encore connaître les modules dédiés, réfléchis : pourquoi `shell -a "apt install htop"` est-il une **mauvaise idée** comparé à un futur module `apt` ? (Indice : que se passe-t-il si on le relance alors que htop est déjà installé ?)

## ✅ Tu sais maintenant…

- La différence entre **`command`** (commande simple) et **`shell`** (avec pipes/redirections).
- Préférer **`command`** par défaut, **`shell`** seulement si nécessaire.
- Que `command`/`shell` ne sont **pas idempotents** et qu'il faut leur préférer les **modules dédiés** quand ils existent.

---

# Chapitre 2.5 — Lire les sorties : `ok`, `changed`, `failed`, `skipped`, `unreachable`

## Le minimum à savoir

Savoir **lire ce qu'Ansible répond** est un réflexe indispensable. Chaque action, sur chaque machine, se termine dans l'un de ces **cinq états** :

| Statut | Signification |
|--------|---------------|
| **`ok`** | La machine était **déjà** dans l'état voulu : rien à faire |
| **`changed`** | Ansible a **modifié** quelque chose pour atteindre l'état voulu |
| **`failed`** | L'action a **échoué** sur cette machine |
| **`skipped`** | L'action a été **ignorée** (à cause d'une condition — on verra ça en Partie 6) |
| **`unreachable`** | Ansible **n'a pas pu joindre** la machine (problème SSH/réseau) |

> **Apprends ces cinq mots maintenant.** Ils sont ta boussole pour tout le reste du cours. La distinction la plus importante est **`ok` vs `changed`** : on l'approfondit dans la partie suivante (l'idempotence).

### Commande ad hoc vs playbook

Une **commande ad hoc** agit une fois, en ligne de commande. Un **playbook** (Partie 4) est un fichier réutilisable qui décrit plusieurs actions. Mais dans les **deux** cas, tu liras ces **mêmes** statuts.

## Très utile en pratique

Avec une commande ad hoc, le statut apparaît au début de la réponse de chaque machine :

```text
cible1 | SUCCESS => { ... }          ← tout va bien (équivaut à ok)
cible2 | CHANGED => { ... }          ← Ansible a modifié quelque chose
cible3 | UNREACHABLE! => { ... }     ← machine injoignable (SSH/réseau)
cible4 | FAILED! => { ... }          ← l'action a échoué
```

## Exemple simple

```bash
ansible all -i inventory.ini -m ansible.builtin.ping
```
```text
cible1 | SUCCESS => {"ping": "pong"}      ← ok : la machine répond
cible2 | UNREACHABLE! => {...}            ← problème SSH : à diagnostiquer
```

Ici, tu vois immédiatement que `cible2` a un souci de connexion, et que `cible1` va bien.

## 🔍 Réflexe diagnostic

> Devant une exécution, **lis les statuts d'abord** :
> - `unreachable` → problème **SSH/réseau** (teste `ssh` à la main).
> - `failed` → l'action a échoué (lis le **message d'erreur** affiché).
> - `changed` partout alors que tu rejoues → quelque chose n'est pas idempotent (Partie 3).
> - `skipped` → une condition a ignoré l'action (Partie 6).

## ❌ Erreur classique

> **Ne pas lire les statuts et croire que « ça a marché » parce qu'il n'y a pas eu d'erreur évidente.**

Un débutant lance une commande, ne voit pas de message rouge, et passe à la suite — sans vérifier. Or `unreachable` sur une machine signifie qu'elle n'a **rien** reçu, et tu pourrais ne pas t'en rendre compte. Le réflexe correct : **toujours regarder le statut de chaque machine**. Une absence d'erreur évidente n'est pas une preuve que tout s'est bien passé partout.

## Exercices

### Guidé
Lance un `ping` sur tout le parc et identifie le statut de **chaque** machine. Tout doit être `SUCCESS`. Note ce que tu vois.

### Autonome
Provoque un `unreachable` : éteins une cible (ou coupe son réseau) et relance le `ping`. Observe `UNREACHABLE` sur cette machine et `SUCCESS` sur l'autre. Rallume la cible et confirme le retour à `SUCCESS`.

### Défi
Provoque un `failed` : lance une commande qui échoue, par exemple `ansible all -i inventory.ini -m ansible.builtin.command -a "ls /dossier_qui_nexiste_pas"`. Lis le message d'erreur. En quoi `failed` (l'action a échoué) est-il **différent** de `unreachable` (la machine n'a pas été jointe) ?

## ✅ Tu sais maintenant…

- Lire les **cinq statuts** : `ok`, `changed`, `failed`, `skipped`, `unreachable`.
- Que la distinction reine est **`ok` vs `changed`** (approfondie en Partie 3).
- Que ces statuts sont les **mêmes** en ad hoc et en playbook.
- Le réflexe : **lire les statuts** pour diagnostiquer (`unreachable` = SSH, `failed` = erreur d'action).

---

## 🚩 Checkpoint — Fin de la Partie 2

Ansible **agit** maintenant sur ton parc. Avant de plonger dans l'idempotence, assure-toi de pouvoir :

- [ ] Écrire un **inventaire INI** avec des groupes et des variables simples.
- [ ] Vérifier ton inventaire avec **`ansible-inventory --graph`** et **`--host`**.
- [ ] Lancer un **`ping`** et des commandes ad hoc (`command`, `shell`).
- [ ] Savoir quand utiliser **`command`** vs **`shell`**.
- [ ] Lire les **cinq statuts** (`ok`, `changed`, `failed`, `skipped`, `unreachable`).
- [ ] Diagnostiquer un **`unreachable`** (côté SSH).

> **🧩 Mini-projet 2 — « Inventaire propre + état des lieux ».**
> 1. Écris un `inventory.ini` avec un groupe `web` (tes deux cibles) et une variable de groupe `ansible_user`.
> 2. Vérifie-le avec `ansible-inventory --graph` et `--host`.
> 3. Pingue tout le parc.
> 4. Avec des commandes ad hoc en lecture, collecte l'uptime et l'espace disque de chaque machine.
> Objectif : enchaîner **décrire → vérifier → agir → lire les sorties**, avec le réflexe « je regarde le statut de chaque machine ».
>
> **🧩 Mini-projet 3 — « Commandes ad hoc multi-machines ».**
> Sur le groupe `web`, lance trois commandes de lecture différentes (par exemple : `hostname`, `df -h /`, et la version de l'OS via `shell` + pipe). Compare les sorties entre les deux machines.

> **La suite :** en Partie 3, on s'attaque au concept qui rend Ansible **vraiment** différent d'un script : l'**idempotence**. Tu vas le **voir de tes yeux** en relançant une commande.

---
---
---

# PARTIE 3 — COMPRENDRE LES SORTIES ET L'IDEMPOTENCE

> **Objectif de la partie :** comprendre ce qui rend Ansible différent d'un simple script. Tu vas **voir de tes yeux** l'idempotence en relançant une commande, et comprendre pourquoi les **modules dédiés** sont supérieurs à `command`/`shell`.

---

# Chapitre 3.1 — `ok` vs `changed`

## Le minimum à savoir

Au chapitre précédent, tu as vu les cinq statuts. Concentrons-nous sur les **deux plus importants**, car ils expliquent tout le fonctionnement d'Ansible :

- **`changed`** : Ansible a **agi**. Il y avait un écart entre l'état voulu et l'état réel, et Ansible l'a corrigé.
- **`ok`** : Ansible **n'a rien fait**. L'état voulu était **déjà** atteint, donc il n'y avait rien à corriger.

```
   ÉTAT VOULU : "htop installé"

   Machine où htop est ABSENT   →  Ansible installe  →  CHANGED
   Machine où htop est PRÉSENT  →  Ansible vérifie   →  OK (rien à faire)
```

> **C'est la distinction reine d'Ansible.** `changed` = « j'ai modifié quelque chose ». `ok` = « c'était déjà bon, je n'ai pas touché ». Comprendre ça, c'est comprendre l'idempotence.

## Très utile en pratique

Cette distinction te permet de **lire** ce qu'Ansible a réellement fait :

- Beaucoup de `changed` au **premier** passage : normal, Ansible met les machines en conformité.
- Que des `ok` quand tu **rejoues** : parfait, tout est déjà en place, rien n'a bougé.
- Un `changed` **inattendu** quand tu rejoues : quelque chose avait changé sur la machine, et Ansible l'a corrigé (ou alors ton action n'est pas idempotente — on verra ça).

## Exemple simple

```text
1er passage :  cible1 | CHANGED   (htop a été installé)
2e passage :   cible1 | SUCCESS   (htop était déjà là, rien à faire → ok)
```

## ❌ Erreur classique

> **Croire qu'un `changed` est forcément une bonne nouvelle, ou qu'un `ok` veut dire « rien ne marche ».**

`ok` ne veut **pas** dire « échec » ou « inaction inutile » — ça veut dire « **déjà conforme** », ce qui est excellent. Et `changed` n'est pas toujours souhaitable : si tu **rejoues** un playbook et qu'une tâche repasse en `changed` sans raison, c'est suspect. Le réflexe correct : **`ok` au second passage = bon signe** ; `changed` inattendu = à investiguer.

## Exercices

### Guidé
Sans encore installer quoi que ce soit, relis dans ta tête : que signifie `ok` ? que signifie `changed` ? Écris une phrase pour chacun, avec tes propres mots.

### Autonome
Imagine une tâche « le fichier /etc/motd doit contenir le texte X ». Au premier passage, quel statut attends-tu ? Et si tu relances **sans** avoir modifié le fichier ? Et si quelqu'un a modifié le fichier à la main entre-temps ?

### Défi
Explique pourquoi voir **`ok` partout** quand on rejoue un playbook est, en réalité, **rassurant** pour un administrateur. Qu'est-ce que ça prouve sur l'état du parc ?

## ✅ Tu sais maintenant…

- Que **`changed`** = Ansible a agi (il y avait un écart) et **`ok`** = rien à faire (déjà conforme).
- Que c'est la **distinction reine** qui explique le fonctionnement d'Ansible.
- Que des **`ok` au rejeu** sont un bon signe, et qu'un **`changed` inattendu** mérite attention.

---

# Chapitre 3.2 — Voir l'idempotence en relançant

## Le minimum à savoir

L'**idempotence**, tu en as eu l'image en Partie 0. Maintenant, tu vas la **voir en vrai**. Le principe : tu lances **deux fois** la même action, et tu observes le changement de statut.

```
   1er lancement : action effectuée    →  CHANGED
   2e lancement :  rien à faire         →  OK
   3e lancement :  rien à faire         →  OK
   ... (toujours OK tant que l'état voulu est respecté)
```

> **C'est ça, l'idempotence en pratique :** la première fois, Ansible agit (`changed`). Ensuite, tant que l'état voulu est respecté, il ne fait plus rien (`ok`). Tu peux relancer cent fois, ce sera toujours `ok`.

## Très utile en pratique

On le démontre avec un module **idempotent** (le module `apt`, qu'on détaillera en Partie 5). L'idée : installer un paquet, puis relancer.

```bash
# 1er lancement : le paquet n'est pas là → Ansible l'installe
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become

# 2e lancement : EXACTEMENT la même commande
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become
```

*(Le `--become` sert à obtenir les droits root pour installer — on l'explique en Partie 4. Pour l'instant, accepte-le.)*

```text
1er lancement :  cible1 | CHANGED   (htop installé)
2e lancement :   cible1 | SUCCESS   (htop déjà là → ok, changed: false)
```

## Exemple simple

Le cœur de la démonstration tient en deux lignes de sortie :

```text
changed   ← la première fois, Ansible a agi
ok        ← la seconde fois, rien à faire
```

Si tu vois ça, **félicitations** : tu viens d'observer l'idempotence.

## 🔍 Réflexe diagnostic

> Si une action affiche **`changed` à CHAQUE** relance (jamais `ok`), c'est le signe qu'elle **n'est pas idempotente**. C'est presque toujours le cas avec `command`/`shell` (qui réexécutent aveuglément). On voit pourquoi au chapitre suivant.

## ❌ Erreur classique

> **S'inquiéter de voir `changed` au premier passage.**

Un débutant voit `changed` et croit qu'il y a un problème. **Non** : `changed` au premier passage est **normal et attendu** — Ansible met la machine en conformité. Le réflexe correct : ce qui compte, c'est le **second** passage. S'il affiche `ok`, ton action est idempotente et tout va bien.

## Exercices

### Guidé
Lance la commande d'installation de `htop` ci-dessus **une fois**, observe `changed`. Relance-la **à l'identique**, observe `ok` (`changed: false`). Tu viens de voir l'idempotence en action.

### Autonome
Crée une **dérive** : installe `htop` avec Ansible (`changed`), puis désinstalle-le **à la main** sur une cible (`sudo apt remove htop`). Relance la commande Ansible : que se passe-t-il ? Explique pourquoi Ansible réaffiche `changed`.

### Défi
Explique en quelques lignes pourquoi cette propriété fait d'Ansible un outil capable de **corriger les dérives** : si une machine s'écarte de l'état voulu, que se passe-t-il quand on rejoue ?

## ✅ Tu sais maintenant…

- **Voir** l'idempotence : `changed` au 1er passage, `ok` aux suivants.
- Qu'un module **idempotent** (comme `apt`) ne réagit que s'il y a un écart.
- Qu'un **`changed` permanent** au rejeu signale une action **non idempotente**.
- Qu'Ansible **corrige les dérives** : rejouer ramène une machine à l'état voulu.

---

# Chapitre 3.3 — Modules dédiés vs `command`/`shell`

## Le minimum à savoir

Voici **pourquoi** on t'a dit, en Partie 2, de préférer les modules dédiés. C'est une question d'**idempotence**.

Compare deux façons d'installer nginx :

```bash
# ❌ Avec shell : PAS idempotent
ansible web -i inventory.ini -m ansible.builtin.shell -a "apt install -y nginx" --become
# → relancé, il relance l'installation. TOUJOURS "changed". Il ne SAIT pas si c'est déjà fait.

# ✅ Avec le module dédié apt : IDEMPOTENT
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=nginx state=present" --become
# → relancé, il constate que nginx est là → "ok". Il déclare un ÉTAT VOULU.
```

> **La différence est fondamentale :**
> - Un **module dédié** (`apt`, `service`, `copy`…) **déclare un état** (`state: present`) et sait **vérifier** si cet état est déjà atteint. D'où l'idempotence.
> - **`command`/`shell`** **exécutent aveuglément** : ils ne savent pas si l'action est déjà faite, donc ils la refont, et signalent toujours `changed`.

## Très utile en pratique

La règle pratique pour tout le cours :

- **Pour installer un paquet** → module `apt`/`dnf` (pas `shell -a "apt install"`).
- **Pour gérer un service** → module `service` (pas `shell -a "systemctl"`).
- **Pour copier un fichier** → module `copy` (pas `shell -a "cp"`).
- **Pour créer un utilisateur** → module `user` (pas `shell -a "useradd"`).

`command`/`shell` ne servent que pour ce qui **n'a pas** de module dédié.

## Exemple simple

```text
shell -a "apt install -y htop"  (relancé)  →  changed, changed, changed...  (jamais idempotent)
apt   name=htop state=present   (relancé)  →  changed, puis ok, ok, ok...   (idempotent !)
```

## 🔀 À ne pas confondre

> **« Lancer une commande » vs « déclarer un état ».**
> `shell -a "apt install nginx"` = « lance cette commande » (impératif). `apt name=nginx state=present` = « nginx doit être présent » (état souhaité). Le second est idempotent, le premier non.

## ❌ Erreur classique

> **Reproduire ses réflexes Bash dans Ansible en utilisant `shell` partout.**

L'admin habitué à la ligne de commande écrit `shell -a "systemctl start nginx"`, `shell -a "useradd bob"`. Ça **fonctionne**, mais ça **détruit** l'idempotence et la lisibilité. Le réflexe correct : **chercher d'abord le module dédié** (on les apprend en Partie 5). Ils existent pour presque tout. Garde `command`/`shell` pour les rares cas sans module.

## Exercices

### Guidé
Installe `htop` de **deux** façons sur une cible de test (snapshot pris) : d'abord avec `shell -a "apt install -y htop"`, relancé deux fois (observe `changed` à chaque fois). Puis avec `apt name=htop state=present`, relancé deux fois (observe `changed` puis `ok`). Compare.

### Autonome
Liste **quatre** tâches d'administration courantes et, pour chacune, indique le **module dédié** que tu utiliserais plutôt que `shell` (indice : paquet, service, fichier, utilisateur).

### Défi
Explique en quelques lignes pourquoi un playbook rempli de `shell` est difficile à **rejouer en confiance**, alors qu'un playbook fait de modules dédiés peut être relancé sans crainte. Relie ta réponse à l'idempotence.

## ✅ Tu sais maintenant…

- Pourquoi les **modules dédiés** sont **idempotents** (ils déclarent et vérifient un état).
- Pourquoi **`command`/`shell`** ne le sont pas (ils exécutent aveuglément).
- La règle : **module dédié** pour paquets/services/fichiers/utilisateurs ; `shell` seulement en dernier recours.
- Que l'idempotence rend un playbook **rejouable en confiance**.

---

## 🚩 Checkpoint — Fin de la Partie 3

Tu tiens maintenant le concept central d'Ansible. Avant d'écrire des playbooks, assure-toi de pouvoir :

- [ ] Expliquer **`ok` vs `changed`** avec tes mots.
- [ ] **Démontrer** l'idempotence en relançant une commande (`changed` → `ok`).
- [ ] Expliquer pourquoi les **modules dédiés** sont idempotents et pas `command`/`shell`.
- [ ] Comprendre qu'Ansible **corrige les dérives** quand on rejoue.

> **🧩 Mini-projet 4 — « L'idempotence en pratique ».**
> 1. Installe un paquet (`htop`) sur le groupe `web` avec le module `apt` et `--become`.
> 2. Relance la commande et **observe** le passage de `changed` à `ok`.
> 3. Désinstalle le paquet à la main sur une cible, relance Ansible, observe qu'il **corrige la dérive**.
> 4. Refais l'installation avec `shell -a "apt install -y htop"` et constate qu'il affiche **toujours** `changed`.
> Objectif : **vivre** la différence entre une action idempotente (module dédié) et une action non idempotente (`shell`).

> **La suite :** en Partie 4, on passe de l'éphémère (commandes ad hoc) au **rejouable et documenté** : on apprend le **YAML** et on écrit nos premiers **playbooks**.

---
---

# PARTIE 4 — YAML ET PREMIERS PLAYBOOKS

> **Objectif de la partie :** écrire tes premiers playbooks. On apprend d'abord le **YAML** (le format des playbooks), puis on construit un playbook complet, et on découvre les options pour **vérifier avant d'agir**.

---

# Chapitre 4.1 — YAML sans peur

## Le minimum à savoir

Les playbooks Ansible s'écrivent en **YAML**, un format texte fait pour être **lisible par un humain**. Pas de programmation : juste des **clés**, des **valeurs** et des **listes**, organisées par l'**indentation**.

Les trois briques de base :

```yaml
# 1. Une paire clé : valeur
nom: serveur-web
actif: true

# 2. Une liste (chaque élément commence par un tiret)
paquets:
  - nginx
  - htop
  - git

# 3. Un dictionnaire imbriqué (l'indentation crée la hiérarchie)
serveur:
  nom: web1
  ip: 192.168.56.11
```

### LA règle d'or : l'indentation

> **En YAML, l'indentation EST la structure.** Elle se fait avec des **espaces**, **jamais** avec des tabulations. La convention : **2 espaces** par niveau, et on reste **cohérent** dans tout le fichier.

```yaml
# ✅ CORRECT
serveur:
  nom: web1
  ip: 192.168.56.11

# ❌ FAUX (ip n'est plus dans serveur)
serveur:
  nom: web1
ip: 192.168.56.11
```

Un fichier YAML commence souvent par `---` (qui marque le début du document).

## Très utile en pratique

```bash
# Vérifier qu'un fichier YAML / playbook est syntaxiquement correct (sans rien exécuter)
ansible-playbook playbook.yml --syntax-check
```

> 🔍 **Réflexe diagnostic :** `--syntax-check` attrape les erreurs d'indentation **avant** toute exécution. C'est gratuit et instantané. Prends l'habitude de le lancer dès qu'un YAML te résiste.

## Exemple simple

```yaml
---
serveur:
  nom: web1
  paquets:
    - nginx
    - htop
```

Lisible, non ? C'est tout l'intérêt du YAML : on **comprend** le fichier en le lisant.

## ❌ Erreur classique

> **Mélanger tabulations et espaces, ou se tromper de niveau d'indentation.**

C'est **l'**erreur YAML par excellence. Un copier-coller depuis le web introduit une tabulation invisible, et Ansible refuse le fichier avec un message parfois obscur. Le réflexe correct : configure ton éditeur pour afficher les caractères invisibles et **convertir les tabs en espaces**, et lance `--syntax-check` au moindre doute. La plupart des « bugs Ansible » des débutants sont des **bugs d'indentation**.

## Exercices

### Guidé
Écris un petit fichier YAML décrivant un serveur (un nom, une liste de 3 paquets, un sous-dictionnaire). Lance `ansible-playbook ton_fichier.yml --syntax-check`. Corrige jusqu'à ce qu'il n'y ait plus d'erreur de syntaxe.

### Autonome
Prends ton fichier et **casse-le** volontairement : décale une ligne, ou ajoute une tabulation. Lance `--syntax-check` et observe le message d'erreur. Apprends à relier le message à la cause.

### Défi
Réécris ton inventaire INI (Partie 2) au format **YAML** dans la tête (clés/listes). Ce n'est pas obligatoire pour le cours, mais ça t'entraîne à « penser en YAML » : hôtes, groupes, variables sous forme de clés et de listes.

## ✅ Tu sais maintenant…

- Que les playbooks s'écrivent en **YAML** : clés/valeurs, listes, dictionnaires.
- Que **l'indentation EST la structure** (espaces, jamais de tabs, 2 espaces par niveau).
- Vérifier la syntaxe avec **`--syntax-check`**.
- Que la plupart des « bugs Ansible » débutants sont des **bugs d'indentation**.

---

# Chapitre 4.2 — Anatomie d'un playbook

## Le minimum à savoir

Un **playbook** est un fichier YAML qui décrit une série d'actions **rejouables**. C'est le passage de « je tape une commande » à « j'écris une procédure que je peux relancer et partager ».

Voici un playbook complet et commenté :

```yaml
---
- name: Installer et démarrer un serveur web      # ← un PLAY (un bloc)
  hosts: web                                      # ← sur quelles machines
  become: true                                    # ← avec les droits root (Ch. 4.3)

  tasks:                                          # ← la liste des TÂCHES
    - name: Installer nginx                       # ← une TÂCHE (toujours nommée)
      ansible.builtin.apt:                        # ← le MODULE (nom complet)
        name: nginx                               # ← les arguments du module
        state: present

    - name: Démarrer et activer nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

- Un **play** associe un **groupe de machines** (`hosts`) à une **liste de tâches**.
- Une **tâche** = un **module** + ses **arguments**, avec un **`name:`** lisible.

> **Toujours nommer ses tâches.** Le `name:` apparaît dans la sortie d'exécution : il rend le déroulé **lisible** et le diagnostic **facile**.

## Très utile en pratique

```bash
# Lancer un playbook
ansible-playbook -i inventory.ini site.yml
```

À la fin, Ansible affiche un **récapitulatif** (`PLAY RECAP`) par machine :

```text
PLAY RECAP *********************************************************
cible1  : ok=2    changed=2    unreachable=0    failed=0    skipped=0
cible2  : ok=2    changed=2    unreachable=0    failed=0    skipped=0
```

Ce récapitulatif te dit, machine par machine, combien de tâches ont réussi, modifié, échoué, été ignorées ou injoignables. **C'est le premier endroit où regarder.**

## Exemple simple

Un playbook minimal à une seule tâche :

```yaml
---
- name: Vérifier la connexion
  hosts: all
  tasks:
    - name: Ping
      ansible.builtin.ping:
```

## ❌ Erreur classique

> **Oublier de nommer ses tâches, ou se tromper de niveau d'indentation entre `hosts`, `tasks` et les tâches.**

Sans `name:`, la sortie devient illisible (« tâche anonyme »). Et une mauvaise indentation entre `tasks:` et les tâches casse le playbook. Le réflexe correct : **nommer chaque tâche** et respecter l'indentation (les tâches sont **indentées sous** `tasks:`). Un `--syntax-check` confirme que la structure tient.

## Exercices

### Guidé
Écris le playbook `site.yml` qui installe et démarre nginx sur le groupe `web` (modèle ci-dessus). Lance `--syntax-check`, puis exécute-le. Vérifie le `PLAY RECAP` et l'accès à nginx (avec `curl` ou un navigateur vers l'IP d'une cible).

### Autonome
Relance **le même** playbook une seconde fois. Observe le `PLAY RECAP` : les tâches passent de `changed` à `ok` (idempotence à l'échelle du playbook). Puis arrête nginx à la main sur une cible et relance : observe qu'Ansible **corrige** la dérive.

### Défi
Ajoute une troisième tâche qui affiche un message avec le module `ansible.builtin.debug` (par exemple `msg: "nginx est prêt"`). Vérifie que la nouvelle tâche apparaît bien, nommée, dans la sortie.

## ✅ Tu sais maintenant…

- L'anatomie d'un playbook : **play → tasks → modules**, avec `hosts` et `name:`.
- Lancer un playbook avec **`ansible-playbook`**.
- Lire le **`PLAY RECAP`** comme premier réflexe.
- Qu'il faut **nommer** chaque tâche et soigner l'indentation.

---

# Chapitre 4.3 — `become` : les droits root

## Le minimum à savoir

Beaucoup d'actions d'administration (installer un paquet, modifier un fichier système, gérer un service) nécessitent les droits **root**. En Ansible, on les obtient avec **`become`** :

```yaml
- name: Installer un paquet (nécessite root)
  hosts: web
  become: true          # ← devient root (via sudo) pour les tâches de ce play
  tasks:
    - name: Installer nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```

> **Rappel (Partie 1) :** se **connecter** (avec ton utilisateur SSH, souvent non-root) et **devenir root** (`become`) sont deux étapes distinctes. La bonne pratique : se connecter en utilisateur normal, et n'élever les droits **que** quand c'est nécessaire.

`become` peut se mettre au niveau du **play** (toutes les tâches) ou d'une **tâche précise** (seulement celle-là).

## Très utile en pratique

```yaml
- name: Play mixte
  hosts: web
  tasks:
    - name: Voir qui je suis (pas besoin de root)
      ansible.builtin.command: whoami

    - name: Installer un paquet (besoin de root)
      ansible.builtin.apt:
        name: htop
        state: present
      become: true          # ← root UNIQUEMENT pour cette tâche
```

## Exemple simple

Sans `become`, une installation de paquet échoue (« permission refusée ») :

```text
FAILED! => "msg": "... Permission denied ..."
```

Avec `become: true`, elle réussit. C'est le signe qu'il fallait les droits root.

## 🛡️ Réflexe sécurité

> N'active `become` que **là où c'est nécessaire**. Donner les droits root « par confort » à des tâches qui n'en ont pas besoin est une mauvaise habitude. Élève les privilèges **au cas par cas**, pour les seules tâches qui le requièrent.

## ❌ Erreur classique

> **Oublier `become` sur une tâche qui nécessite root, et conclure qu'« Ansible ne marche pas ».**

Une installation de paquet sans `become` échoue avec « Permission denied », et le débutant croit à un bug. Le réflexe correct : si une tâche d'administration système échoue pour des raisons de **permission**, il manque probablement **`become: true`**. Lis le message d'erreur : « permission denied » est un indice clair.

## Exercices

### Guidé
Écris un playbook qui installe `htop` **sans** `become`. Lance-le : il échoue probablement avec une erreur de permission. Ajoute `become: true` et relance : il réussit. Tu comprends à quoi sert `become`.

### Autonome
Crée un playbook avec deux tâches : une qui ne nécessite pas root (`whoami`) et une qui le nécessite (installer un paquet). Mets `become` **uniquement** sur la seconde. Vérifie que tout fonctionne.

### Défi
Lance une tâche `ansible.builtin.command: whoami` **avec** puis **sans** `become: true`, et compare la sortie (le `debug` ou le retour de la commande). Que t'apprend la différence sur ce que fait réellement `become` ?

## ✅ Tu sais maintenant…

- Que **`become: true`** donne les droits **root** sur la cible.
- Que se **connecter** et **devenir root** sont deux étapes distinctes.
- Mettre `become` au niveau du **play** ou d'une **tâche** précise.
- Qu'une erreur de **permission** signale souvent un `become` manquant.

---

# Chapitre 4.4 — Vérifier avant d'agir : `--syntax-check` et `--check`

## Le minimum à savoir

Avant de lancer un playbook « pour de vrai », on prend l'habitude de le **vérifier**. Deux outils essentiels :

- **`--syntax-check`** : vérifie que la **syntaxe YAML** est correcte. Instantané, ne se connecte à rien.
- **`--check`** : lance le playbook en **simulation**. Ansible te dit **ce qu'il ferait**, **sans rien modifier** sur les machines.

```bash
ansible-playbook -i inventory.ini site.yml --syntax-check   # 1. la syntaxe est-elle bonne ?
ansible-playbook -i inventory.ini site.yml --check          # 2. qu'est-ce qui CHANGERAIT ?
ansible-playbook -i inventory.ini site.yml                  # 3. exécution réelle
```

> **L'enchaînement de prudence :** `--syntax-check` → `--check` → exécution réelle. Chaque étape attrape un type de problème différent, **avant** qu'il ne touche tes machines.

## Très utile en pratique

En mode `--check`, les tâches qui **modifieraient** quelque chose apparaissent en `changed` (mais **rien n'est réellement modifié**), et les autres en `ok`. C'est une **simulation**.

```bash
ansible-playbook -i inventory.ini site.yml --check
```

> ⚠️ **Bon à savoir :** `--check` est une **simulation très utile**, mais **pas parfaite**. Certains modules gèrent mal le mode simulation, et certains résultats dépendent de l'état réel au moment de l'exécution. Vois `--check` comme un **réflexe de prudence**, pas comme une garantie absolue.

## Exemple simple

```text
$ ansible-playbook -i inventory.ini site.yml --check
TASK [Installer nginx] ***
changed: [cible1]          ← en réalité, RIEN n'est installé : c'est une simulation
```

## 🧪 Lab vs production

> En **lab**, tu peux te permettre de lancer directement. Mais prends **dès maintenant** l'habitude de `--check` avant les actions importantes : c'est le réflexe qui, en **production**, t'évitera des catastrophes. Apprendre le bon geste en lab, c'est l'avoir acquis pour plus tard.

## ❌ Erreur classique

> **Lancer un playbook directement, sans jamais vérifier la syntaxe ni simuler.**

On écrit un playbook, on le lance, et une erreur d'indentation (ou pire, une action non voulue) se déclenche. Le réflexe correct : **`--syntax-check` systématique**, et **`--check`** avant toute action qui modifie des machines. Quelques secondes de vérification évitent bien des ennuis.

## Exercices

### Guidé
Sur ton playbook nginx, lance d'abord `--syntax-check` (corrige les erreurs éventuelles), puis `--check` (observe ce qui *changerait*), puis l'exécution réelle. Compare la sortie `--check` et la sortie réelle.

### Autonome
Modifie ton playbook (par exemple, ajoute l'installation d'un paquet supplémentaire) et lance `--check` **avant** d'exécuter. Vérifie que la simulation annonce bien le changement attendu, puis exécute pour de vrai.

### Défi
Lance `--check` sur un playbook **déjà appliqué** (donc tout est déjà conforme). Que montre la simulation (`ok` partout ou `changed` ?) ? Explique ce que ça t'apprend sur l'état actuel de tes machines.

## ✅ Tu sais maintenant…

- Vérifier la syntaxe avec **`--syntax-check`** (instantané).
- Simuler avec **`--check`** : voir ce qui changerait **sans rien modifier**.
- L'enchaînement **`--syntax-check` → `--check` → exécution**.
- Que `--check` est **utile mais pas parfait** (réflexe de prudence, pas garantie).

---

## 🚩 Checkpoint — Fin de la Partie 4

Tu sais maintenant écrire de vrais playbooks. Avant d'apprendre les modules d'administration, assure-toi de pouvoir :

- [ ] Écrire un **YAML** correct (indentation espaces, listes, dictionnaires) et le valider.
- [ ] Structurer un playbook en **play → tasks → modules**, avec des `name:` clairs.
- [ ] Utiliser **`become`** pour les actions nécessitant root.
- [ ] Lire le **`PLAY RECAP`**.
- [ ] Vérifier avec **`--syntax-check`** et simuler avec **`--check`**.

> **🧩 Mini-projet 5 — « Déployer un service web simple ».**
> Écris un playbook qui : installe nginx (module `apt`, avec `become`), le démarre et l'active (module `service`). Vérifie-le (`--syntax-check`, `--check`), exécute-le, teste l'accès web, **relance-le** pour confirmer l'idempotence (`ok` partout), puis provoque une dérive (arrête nginx à la main) et montre qu'un nouveau run la **corrige**.

> **La suite :** en Partie 5, on apprend les **modules d'administration Linux** les plus utiles : paquets, services, fichiers, permissions, utilisateurs et groupes. De quoi administrer une vraie machine proprement.

---
---
---

# PARTIE 5 — MODULES ESSENTIELS D'ADMINISTRATION LINUX

> **Objectif de la partie :** apprendre les **modules** Ansible les plus utiles pour administrer une machine Linux : paquets, services, fichiers, permissions, utilisateurs et groupes. Ce sont tes outils du quotidien.

---

# Chapitre 5.1 — Gérer les paquets (`apt` / `dnf`)

## Le minimum à savoir

Pour installer ou retirer des logiciels, on utilise le module de paquets de la distribution : **`apt`** (Debian/Ubuntu) ou **`dnf`** (Fedora/RHEL).

```yaml
- name: Installer nginx
  ansible.builtin.apt:
    name: nginx
    state: present        # ← présent = doit être installé
  become: true
```

Les états possibles :
- `state: present` → le paquet **doit être installé**.
- `state: absent` → le paquet **ne doit pas être là** (Ansible le retire s'il est présent).
- `state: latest` → le paquet doit être à sa **dernière version**.

## Très utile en pratique

```yaml
# Installer plusieurs paquets d'un coup
- name: Installer des outils de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present
    update_cache: true     # met à jour la liste des paquets avant d'installer
  become: true

# Retirer un paquet
- name: Retirer un paquet inutile
  ansible.builtin.apt:
    name: telnet
    state: absent
  become: true
```

> `update_cache: true` équivaut à un `apt update` avant l'installation : utile pour être sûr d'avoir la liste de paquets à jour.

## Exemple simple

```yaml
- name: nginx doit être installé
  ansible.builtin.apt:
    name: nginx
    state: present
  become: true
```

## 🔀 À ne pas confondre

> **`state: present` vs `state: latest`.**
> `present` = « installé » (peu importe la version, tant qu'il est là). `latest` = « à la dernière version » (Ansible mettra à jour si une version plus récente existe). Pour un débutant, `present` suffit dans la plupart des cas.

## ❌ Erreur classique

> **Utiliser `shell -a "apt install"` au lieu du module `apt`.**

Comme vu en Partie 3, `shell` n'est **pas idempotent**. Le réflexe correct : **toujours le module `apt`/`dnf`** pour les paquets. Il déclare un état, il est idempotent, et il gère les erreurs proprement.

## Exercices

### Guidé
Écris un playbook qui installe `htop`, `git` et `curl` en une seule tâche (liste), avec `update_cache: true` et `become`. Lance-le, vérifie sur la cible (`which htop`), puis relance pour confirmer l'idempotence.

### Autonome
Ajoute une tâche qui **retire** un paquet (`state: absent`). Lance avec `--check` d'abord pour voir ce qui se passerait, puis pour de vrai. Vérifie que le paquet a bien disparu.

### Défi
Teste la différence entre `present` et `latest` : installe un paquet en `present`, note sa version (`apt list --installed | grep ...` via une commande ad hoc), puis change en `latest` et observe si Ansible le met à jour. Dans quel cas préférerais-tu `latest` ?

## ✅ Tu sais maintenant…

- Installer/retirer des paquets avec **`apt`** / **`dnf`**.
- Les états **`present`**, **`absent`**, **`latest`**.
- Installer **plusieurs paquets** en liste, avec `update_cache`.
- Toujours préférer le **module** à `shell` pour les paquets.

---

# Chapitre 5.2 — Gérer les services (`service`)

## Le minimum à savoir

Pour démarrer, arrêter ou activer un service, on utilise le module **`service`** :

```yaml
- name: nginx doit tourner et démarrer au boot
  ansible.builtin.service:
    name: nginx
    state: started        # tourne MAINTENANT
    enabled: true         # démarre AUTOMATIQUEMENT au boot
  become: true
```

Les options principales :
- `state: started` / `stopped` / `restarted` → l'état de marche **maintenant**.
- `enabled: true` / `false` → démarrage **automatique au boot** ou non.

## Très utile en pratique

```yaml
# Arrêter et désactiver un service inutile
- name: Désactiver un service superflu
  ansible.builtin.service:
    name: avahi-daemon
    state: stopped
    enabled: false
  become: true
```

## Exemple simple

```yaml
- name: Démarrer ssh
  ansible.builtin.service:
    name: ssh
    state: started
  become: true
```

## 🔀 À ne pas confondre

> **`state: started` (maintenant) ≠ `enabled: true` (au boot).**
> Un service peut **tourner maintenant** sans être **activé au boot** (il ne redémarrera pas après un redémarrage de la machine), et inversement. Les deux options sont **indépendantes**. Pour qu'un service soit là « tout le temps », il faut **les deux** : `started` + `enabled`.

## ❌ Erreur classique

> **Démarrer un service sans `enabled: true`, puis s'étonner qu'il ne redémarre pas après reboot.**

`state: started` lance le service **maintenant**, mais ne garantit pas qu'il redémarrera après un redémarrage de la machine. Le réflexe correct : si tu veux qu'un service soit **toujours** présent, mets **à la fois** `state: started` **et** `enabled: true`.

## Exercices

### Guidé
Dans ton playbook nginx, ajoute (ou vérifie) une tâche `service` avec `state: started` et `enabled: true`. Lance, puis vérifie sur la cible avec une commande ad hoc (`systemctl is-active nginx`, `systemctl is-enabled nginx`).

### Autonome
Crée une tâche qui **arrête et désactive** un service de ton choix (par exemple un service présent mais inutile sur tes cibles). Vérifie le résultat. Restaure avec un snapshot si besoin.

### Défi
Démarre un service avec `state: started` **sans** `enabled`. Redémarre la VM (`sudo reboot` à la main ou via Ansible plus tard). Le service est-il toujours actif après le reboot ? Explique le rôle de `enabled`.

## ✅ Tu sais maintenant…

- Gérer les services avec **`service`** : `started`, `stopped`, `restarted`.
- La différence **`state` (maintenant)** vs **`enabled` (au boot)**.
- Qu'un service « toujours présent » nécessite **`started` + `enabled`**.

---

# Chapitre 5.3 — Fichiers et permissions (`copy`, `file`)

## Le minimum à savoir

Deux modules pour gérer fichiers et dossiers :

- **`copy`** : dépose un fichier (depuis la machine de contrôle) vers les cibles.
- **`file`** : gère l'**état** d'un fichier/dossier (existence, permissions, propriétaire).

```yaml
- name: Déposer un fichier de configuration
  ansible.builtin.copy:
    src: motd.txt              # fichier local (sur le contrôle)
    dest: /etc/motd            # destination sur la cible
    owner: root
    group: root
    mode: "0644"               # permissions (toujours entre guillemets)
  become: true

- name: Créer un dossier avec les bonnes permissions
  ansible.builtin.file:
    path: /opt/app
    state: directory
    owner: admin
    mode: "0750"
  become: true
```

## Très utile en pratique

Les **permissions** (`mode`) s'écrivent en notation octale, **entre guillemets** :
- `"0644"` → lecture/écriture pour le propriétaire, lecture pour les autres (fichiers courants).
- `"0600"` → lecture/écriture pour le propriétaire **seulement** (fichiers sensibles).
- `"0750"` → dossier accessible au propriétaire et au groupe, pas aux autres.

> 🛡️ **Réflexe sécurité :** mets les **bonnes permissions** sur les fichiers, surtout les sensibles. Un fichier de configuration en `"0777"` (accessible à tout le monde en écriture) est une mauvaise pratique. Ansible rend ces permissions **explicites et reproductibles** sur tout le parc.

## Exemple simple

```yaml
- name: Déposer une page d'accueil
  ansible.builtin.copy:
    src: index.html
    dest: /var/www/html/index.html
    mode: "0644"
  become: true
```

## ❌ Erreur classique

> **Oublier les guillemets autour du `mode`, ou se tromper de permissions.**

Écrire `mode: 0644` **sans** guillemets peut être mal interprété par YAML. Le réflexe correct : **toujours `mode: "0644"`** entre guillemets. Et réfléchis aux permissions : un fichier sensible (mot de passe, clé) doit être en `"0600"`, pas `"0644"`.

## Exercices

### Guidé
Crée un petit fichier local (`motd.txt`) et déploie-le sur tes cibles dans `/etc/motd` avec `copy`, en `mode: "0644"`. Connecte-toi en SSH à une cible et vérifie le contenu et les permissions (`ls -l /etc/motd`).

### Autonome
Crée un dossier `/opt/monapp` sur les cibles avec `file` (`state: directory`), propriétaire `root`, permissions `"0750"`. Vérifie avec `ls -ld /opt/monapp`.

### Défi
Déploie un fichier « sensible » (par exemple un faux fichier de config avec un contenu quelconque) en `mode: "0600"`. Vérifie qu'un utilisateur non propriétaire ne peut **pas** le lire. Explique pourquoi les permissions comptent pour la sécurité.

## ✅ Tu sais maintenant…

- Déposer un fichier avec **`copy`** (avec `owner`, `group`, `mode`).
- Gérer fichiers/dossiers et permissions avec **`file`**.
- Écrire le **`mode`** entre guillemets (notation octale).
- Que les **bonnes permissions** sont une base de sécurité.

---

# Chapitre 5.4 — Modifier une ligne (`lineinfile`)

## Le minimum à savoir

Parfois, tu ne veux pas remplacer **tout** un fichier, juste **t'assurer qu'une ligne précise** y figure (ou la modifier). C'est le rôle de **`lineinfile`** :

```yaml
- name: S'assurer que la connexion root SSH est désactivée
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PermitRootLogin'        # cherche cette ligne (existante ou commentée)
    line: 'PermitRootLogin no'          # et la remplace par celle-ci
  become: true
```

- `path` : le fichier à modifier.
- `regexp` : le motif de la ligne à chercher.
- `line` : la ligne voulue (ajoutée si absente, corrigée si différente).

## Très utile en pratique

`lineinfile` est **idempotent** : si la ligne voulue est déjà là, il ne fait rien (`ok`). S'il faut la modifier ou l'ajouter, il agit (`changed`). C'est parfait pour ajuster des fichiers de configuration existants.

## Exemple simple

```yaml
- name: Ajouter une ligne d'information dans un fichier
  ansible.builtin.lineinfile:
    path: /etc/motd
    line: "Machine administrée par Ansible"
  become: true
```

## 🔀 À ne pas confondre

> **`lineinfile` (une ligne) vs `template`/`copy` (tout le fichier).**
> `lineinfile` ajuste **une ligne** dans un fichier existant. Si tu dois **générer tout** un fichier de config, ce sera plutôt `template` (Partie 7) ou `copy`. Choisis selon que tu modifies **un détail** ou **tout** le fichier.

## ❌ Erreur classique

> **Utiliser `lineinfile` pour réécrire tout un fichier ligne par ligne.**

Si tu te retrouves avec dix tâches `lineinfile` pour le même fichier, c'est le signe qu'il faut plutôt un **template** (Partie 7). Le réflexe correct : `lineinfile` pour **un ou deux ajustements** ; template pour **générer** un fichier entier.

## Exercices

### Guidé
Avec `lineinfile`, assure-toi que `/etc/ssh/sshd_config` contient `PermitRootLogin no`. Lance avec `--check --diff` d'abord pour **voir** le changement, puis applique. (On verra `--diff` en Partie 8 ; il montre la ligne modifiée.)

### Autonome
Ajoute une ligne d'information dans `/etc/motd` avec `lineinfile`. Relance le playbook : la ligne ne doit **pas** être ajoutée une seconde fois (idempotence). Vérifie sur la cible.

### Défi
Modifie une option de configuration existante (par exemple un paramètre dans un fichier de ton choix) avec `regexp` + `line`. Vérifie qu'au second passage, Ansible affiche `ok` (la ligne est déjà conforme). Explique le rôle du `regexp`.

## ✅ Tu sais maintenant…

- Ajuster **une ligne** d'un fichier avec **`lineinfile`** (`path`, `regexp`, `line`).
- Que `lineinfile` est **idempotent**.
- Quand préférer `lineinfile` (un détail) vs `template`/`copy` (tout le fichier).

---

# Chapitre 5.5 — Utilisateurs et groupes (`user`, `group`)

## Le minimum à savoir

Pour gérer les comptes, deux modules : **`group`** (les groupes) et **`user`** (les utilisateurs).

```yaml
- name: Créer un groupe
  ansible.builtin.group:
    name: developpeurs
    state: present
  become: true

- name: Créer un utilisateur
  ansible.builtin.user:
    name: alice
    groups: developpeurs      # groupe secondaire
    shell: /bin/bash
    state: present
  become: true
```

- `state: present` → le compte/groupe **doit exister**.
- `state: absent` → il **ne doit pas exister** (Ansible le supprime).

## Très utile en pratique

```yaml
# Créer un utilisateur avec un dossier personnel et un shell
- name: Créer un utilisateur admin
  ansible.builtin.user:
    name: bob
    groups: sudo              # l'ajoute au groupe sudo
    shell: /bin/bash
    create_home: true
    state: present
  become: true
```

> 🛡️ **Réflexe sécurité :** gérer les comptes **par Ansible** rend la gestion des accès **centralisée et reproductible**. Créer ou retirer un utilisateur sur tout le parc devient une opération propre, plutôt que des `useradd` éparpillés à la main.

## Exemple simple

```yaml
- name: L'utilisateur alice doit exister
  ansible.builtin.user:
    name: alice
    state: present
  become: true
```

## ❌ Erreur classique

> **Oublier que `state: present` maintient le compte à chaque exécution.**

Si tu déclares `state: present` pour un utilisateur et que quelqu'un le supprime à la main, le prochain run le **recrée** (correction de dérive). C'est voulu, mais il faut le savoir. Le réflexe correct : décider explicitement l'état (`present` ou `absent`) et comprendre qu'Ansible **maintient** cet état à chaque passage.

## Exercices

### Guidé
Écris un playbook qui crée un groupe `developpeurs` et un utilisateur `alice` membre de ce groupe, avec le shell `/bin/bash`. Lance-le, vérifie sur la cible (`id alice`), puis relance pour confirmer l'idempotence.

### Autonome
Ajoute un utilisateur `bob` dans le groupe `sudo` avec un dossier personnel. Vérifie qu'il peut (en théorie) utiliser sudo. Puis crée une tâche qui **supprime** un utilisateur (`state: absent`) et teste-la sur un compte de test.

### Défi
Crée un utilisateur, supprime-le **à la main** sur une cible (`sudo userdel ...`), puis relance le playbook. Observe qu'Ansible le **recrée**. Explique en quoi ce comportement illustre la logique d'**état souhaité** et la correction de dérive.

## ✅ Tu sais maintenant…

- Gérer les **groupes** (`group`) et **utilisateurs** (`user`).
- Les options utiles : `groups`, `shell`, `create_home`, `state`.
- Que la gestion centralisée des comptes est **propre et reproductible**.
- Qu'Ansible **maintient** l'état des comptes à chaque passage.

---

## 🚩 Checkpoint — Fin de la Partie 5

Tu sais maintenant administrer une machine Linux avec Ansible. Avant de rendre tes playbooks adaptables, assure-toi de pouvoir :

- [ ] Gérer les **paquets** (`apt`/`dnf`) : présent, absent, latest, en liste.
- [ ] Gérer les **services** (`service`) : `started` vs `enabled`.
- [ ] Déposer des fichiers et gérer les **permissions** (`copy`, `file`, `mode`).
- [ ] Ajuster **une ligne** d'un fichier (`lineinfile`).
- [ ] Gérer **utilisateurs et groupes** (`user`, `group`).

> **🧩 Mini-projet 6 — « Copier un fichier sur plusieurs machines ».**
> Crée un fichier local et déploie-le sur le groupe `web` avec `copy`, en gérant propriétaire et permissions. Vérifie sur chaque cible.
>
> **🧩 Mini-projet 7 — « Créer un utilisateur sur plusieurs machines ».**
> Écris un playbook qui crée un groupe et un utilisateur (membre du groupe, avec un shell) sur tout le groupe `web`. Vérifie avec `id` sur chaque cible. Confirme l'idempotence.

> **La suite :** en Partie 6, on rend les playbooks **adaptables** : variables, facts (ce qu'Ansible sait des machines), conditions `when` et boucles `loop`. Un playbook qui s'ajuste à chaque machine.

---
---

# PARTIE 6 — VARIABLES, FACTS, CONDITIONS ET BOUCLES

> **Objectif de la partie :** rendre tes playbooks **adaptables**. Avec les variables, les facts, les conditions et les boucles, un même playbook s'ajuste à chaque machine au lieu de tout coder en dur.

---

# Chapitre 6.1 — Variables et `{{ }}`

## Le minimum à savoir

Une **variable** permet de ne pas coder une valeur « en dur ». Au lieu d'écrire `nginx` partout, tu définis une variable et tu la réutilises.

```yaml
- name: Installer le serveur web
  hosts: web
  become: true
  vars:
    paquet_web: nginx          # ← on DÉFINIT la variable
  tasks:
    - name: Installer
      ansible.builtin.apt:
        name: "{{ paquet_web }}"   # ← on UTILISE la variable avec {{ }}
        state: present
```

> **La syntaxe `{{ nom_variable }}`** sert à **utiliser** une variable. Les doubles accolades disent à Ansible : « remplace ceci par la valeur de la variable ».

## Très utile en pratique

Les variables servent à :
- Éviter de répéter une valeur (et de devoir la changer à dix endroits).
- Adapter un playbook selon le contexte (un port différent par groupe, par exemple).
- Rendre un playbook **réutilisable**.

## Exemple simple

```yaml
vars:
  port: 8080
tasks:
  - name: Afficher le port
    ansible.builtin.debug:
      msg: "Le port configuré est {{ port }}"
```

## ❌ Erreur classique

> **Oublier les guillemets autour d'une valeur qui commence par `{{ }}`.**

En YAML, une valeur qui **commence** par `{{` doit être entre guillemets : `name: "{{ paquet_web }}"`. Sans guillemets, YAML peut mal l'interpréter. Le réflexe correct : **mets des guillemets** dès qu'une valeur commence par `{{`.

## Exercices

### Guidé
Reprends ton playbook nginx et remplace le nom du paquet en dur par une variable `paquet_web` définie dans `vars:`. Vérifie que le playbook fonctionne exactement comme avant — mais maintenant, c'est paramétré.

### Autonome
Définis une variable `port` et utilise-la dans un message `debug`. Lance le playbook et observe la valeur affichée. Change la valeur de la variable et relance : le message s'adapte.

### Défi
Crée un playbook avec **deux** variables (un paquet et un port) et utilise-les dans deux tâches différentes. En quoi le fait d'avoir les valeurs **en haut** du playbook (dans `vars:`) rend-il la maintenance plus facile ?

## ✅ Tu sais maintenant…

- Définir une variable dans **`vars:`** et l'utiliser avec **`{{ }}`**.
- Que les variables évitent les répétitions et rendent les playbooks réutilisables.
- Qu'une valeur commençant par `{{` doit être **entre guillemets**.

---

# Chapitre 6.2 — `group_vars` et `host_vars`

## Le minimum à savoir

Mettre toutes les variables dans le playbook devient vite lourd. La bonne pratique : les **ranger** dans des dossiers dédiés, chargés **automatiquement** par Ansible.

```
projet/
├── inventory.ini
├── group_vars/
│   ├── all.yml          # variables pour TOUTES les machines
│   └── web.yml          # variables pour le groupe "web"
└── host_vars/
    └── cible1.yml       # variables pour l'hôte "cible1" uniquement
```

```yaml
# group_vars/web.yml
paquet_web: nginx
port_web: 80
```

> **Le principe :** Ansible charge **tout seul** les variables du bon fichier selon le groupe ou l'hôte ciblé. Une machine du groupe `web` reçoit les variables de `group_vars/web.yml`. C'est propre et organisé.

## Très utile en pratique

```bash
# Voir toutes les variables effectives d'un hôte
ansible-inventory -i inventory.ini --host cible1
```

La règle de priorité, version simple :

> **Du plus général au plus spécifique :** `group_vars/all` < `group_vars/<groupe>` < `host_vars/<hôte>`. Plus c'est **spécifique**, plus ça **l'emporte**.

## Exemple simple

```yaml
# group_vars/all.yml
fuseau_horaire: Europe/Paris

# group_vars/web.yml
paquet_web: nginx
```

Toutes les machines reçoivent `fuseau_horaire` ; celles du groupe `web` reçoivent **en plus** `paquet_web`.

## 🔍 Réflexe diagnostic

> Si une variable « ne prend pas la bonne valeur », c'est presque toujours une question de **priorité** : la même variable est définie à un endroit plus spécifique. **`ansible-inventory --host <machine>`** te montre la valeur réellement appliquée.

## ❌ Erreur classique

> **Définir une variable à plusieurs endroits et obtenir une valeur surprenante.**

Tu mets `port_web: 80` dans `group_vars/web.yml`, mais un vieux `port_web: 8080` traîne dans `host_vars/cible1.yml` : sur cible1, ce sera 8080. Le réflexe correct : connaître la règle (**spécifique > général**) et utiliser `--host` pour voir la valeur effective.

## Exercices

### Guidé
Crée un dossier `group_vars/` avec un fichier `web.yml` contenant `paquet_web: nginx`. Modifie ton playbook pour utiliser `{{ paquet_web }}` sans définir la variable dans le playbook (elle vient du `group_vars`). Vérifie que ça marche.

### Autonome
Ajoute `host_vars/cible1.yml` avec une variable spécifique à cette machine. Lance `ansible-inventory --host cible1` et `--host cible2` et compare les variables de chacune.

### Défi
Définis la **même** variable dans `group_vars/web.yml` et dans `host_vars/cible1.yml` avec des valeurs différentes. Vérifie avec `--host` laquelle gagne sur cible1. Explique la règle de priorité que tu observes.

## ✅ Tu sais maintenant…

- Ranger les variables dans **`group_vars/`** et **`host_vars/`** (chargement automatique).
- La règle de priorité simple : **spécifique > général**.
- Voir les variables effectives avec **`ansible-inventory --host`**.

---

# Chapitre 6.3 — Les facts et le module `setup`

## Le minimum à savoir

Avant d'exécuter ses tâches, Ansible **récolte automatiquement** des informations sur chaque machine : système d'exploitation, version, IP, mémoire, etc. Ce sont les **facts**.

```bash
# Voir tous les facts d'une machine
ansible cible1 -i inventory.ini -m ansible.builtin.setup

# Filtrer un fact précis
ansible cible1 -i inventory.ini -m ansible.builtin.setup -a "filter=ansible_distribution"
```

```yaml
# Utiliser un fact dans un playbook
- name: Afficher la distribution
  ansible.builtin.debug:
    msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"
```

> **Les facts sont une mine d'or :** sans rien configurer, Ansible connaît l'OS, la version, l'IP de chaque machine. Quelques facts utiles : `ansible_distribution` (Ubuntu, Debian…), `ansible_distribution_version`, `ansible_os_family` (Debian, RedHat…), `ansible_hostname`.

## Très utile en pratique

Les facts servent surtout à **adapter** un playbook : faire quelque chose **selon l'OS**, par exemple. On combine ça avec les conditions (chapitre suivant).

## Exemple simple

```yaml
- name: Afficher des infos sur la machine
  ansible.builtin.debug:
    msg: "{{ ansible_hostname }} tourne sous {{ ansible_distribution }}"
```

## 🔀 À ne pas confondre

> **Variable que tu définis vs fact qu'Ansible récolte.**
> Une **variable** (`vars`, `group_vars`), c'est **toi** qui la fixes. Un **fact** (`ansible_distribution`…), c'est Ansible qui le **découvre** sur la machine. Les deux s'utilisent avec `{{ }}`, mais l'origine diffère.

## ❌ Erreur classique

> **Inventer un nom de fact au lieu de vérifier le vrai nom.**

On écrit `{{ ansible_os }}` alors que le bon nom est `{{ ansible_os_family }}` ou `{{ ansible_distribution }}`. Le réflexe correct : lancer `ansible <machine> -m ansible.builtin.setup` (ou avec `filter=`) pour **voir les vrais noms** des facts disponibles.

## Exercices

### Guidé
Lance `ansible cible1 -i inventory.ini -m ansible.builtin.setup` et parcours la sortie. Repère `ansible_distribution`, `ansible_distribution_version` et `ansible_hostname`. Puis affiche-les dans un playbook avec `debug`.

### Autonome
Avec `filter=ansible_*`, explore quelques facts (mémoire, processeur, interfaces réseau). Affiche-en deux ou trois dans un message `debug`.

### Défi
Écris un playbook qui affiche, pour **chaque** machine, une phrase du type « cible1 : Ubuntu 24.04, famille Debian ». Tu combines plusieurs facts dans un seul message.

## ✅ Tu sais maintenant…

- Que les **facts** sont des infos qu'Ansible **récolte automatiquement** sur les machines.
- Les voir avec le module **`setup`** (et `filter=`).
- Quelques facts utiles : `ansible_distribution`, `ansible_os_family`, `ansible_hostname`.
- La différence entre une **variable** (que tu fixes) et un **fact** (qu'Ansible découvre).

---

# Chapitre 6.4 — Les conditions (`when`)

## Le minimum à savoir

**`when`** exécute une tâche **seulement si** une condition est vraie. C'est souvent combiné avec les facts pour s'adapter à chaque machine.

```yaml
- name: Installer avec apt (familles Debian/Ubuntu)
  ansible.builtin.apt:
    name: htop
    state: present
  when: ansible_os_family == "Debian"
  become: true

- name: Installer avec dnf (familles RedHat/Fedora)
  ansible.builtin.dnf:
    name: htop
    state: present
  when: ansible_os_family == "RedHat"
  become: true
```

Une tâche dont la condition est **fausse** apparaît en **`skipped`** (rappel : Partie 2).

## Très utile en pratique

`when` permet d'écrire **un seul** playbook qui fonctionne sur des machines **différentes** : Ubuntu et Fedora, par exemple. Chaque tâche s'exécute là où elle a du sens, et est ignorée ailleurs.

## Exemple simple

```yaml
- name: Message seulement pour Ubuntu
  ansible.builtin.debug:
    msg: "Cette machine est sous Ubuntu"
  when: ansible_distribution == "Ubuntu"
```

## 🔀 À ne pas confondre

> **`skipped` n'est pas une erreur.**
> Une tâche `skipped` n'a **pas** échoué : elle a été **volontairement ignorée** parce que sa condition n'était pas remplie. C'est normal et attendu. Ne confonds pas `skipped` (ignoré) avec `failed` (échoué).

## ❌ Erreur classique

> **Comparer avec `=` au lieu de `==`, ou se tromper de nom de fact.**

En condition, l'égalité s'écrit `==` (double), pas `=`. Et il faut le **bon** nom de fact (`ansible_os_family`, pas `ansible_os`). Le réflexe correct : `==` pour comparer, et vérifier les noms de facts avec `setup`.

## Exercices

### Guidé
Écris deux tâches d'installation : une avec `when: ansible_os_family == "Debian"`, une avec `when: ansible_os_family == "RedHat"`. Lance sur tes cibles (probablement Debian/Ubuntu) et observe : une tâche s'exécute, l'autre est `skipped`.

### Autonome
Crée une tâche qui n'affiche un message que si la machine s'appelle `cible1` (`when: ansible_hostname == "cible1"`). Lance sur tout le parc et observe quelles machines exécutent la tâche et lesquelles la sautent.

### Défi
Combine **deux** conditions avec `and` (par exemple : famille Debian **et** un certain nom d'hôte). Teste et observe le résultat. Comment l'ajout de conditions affine-t-il le ciblage ?

## ✅ Tu sais maintenant…

- Utiliser **`when`** pour exécuter une tâche **sous condition**.
- Combiner `when` avec les **facts** pour s'adapter à l'OS.
- Qu'une tâche non remplie passe en **`skipped`** (ignorée, pas échouée).
- Comparer avec **`==`** (et utiliser les bons noms de facts).

---

# Chapitre 6.5 — Les boucles (`loop`)

## Le minimum à savoir

**`loop`** répète une tâche sur une **liste**, au lieu de la copier-coller plusieurs fois.

```yaml
- name: Installer plusieurs paquets
  ansible.builtin.apt:
    name: "{{ item }}"          # ← "item" = l'élément courant de la boucle
    state: present
  loop:
    - htop
    - git
    - curl
  become: true
```

> **Le mot-clé `item`** représente l'élément en cours de la boucle. À chaque tour, `{{ item }}` prend la valeur suivante de la liste.

## Très utile en pratique

`loop` évite la répétition. Sans lui, tu écrirais trois tâches pour trois paquets. Avec lui, **une** tâche suffit. On peut boucler sur des paquets, des utilisateurs, des fichiers…

## Exemple simple

```yaml
- name: Créer plusieurs utilisateurs
  ansible.builtin.user:
    name: "{{ item }}"
    state: present
  loop:
    - alice
    - bob
    - charlie
  become: true
```

## 🔀 À ne pas confondre

> **Le module `apt` accepte déjà une liste de paquets** (`name: [htop, git]`) sans boucle. `loop` est plus général : il sert quand le module ne gère pas les listes lui-même (créer plusieurs utilisateurs, par exemple). Pour les paquets, les deux marchent ; pour les utilisateurs, `loop` est nécessaire.

## ❌ Erreur classique

> **Oublier `{{ item }}` dans la tâche, ou mal indenter `loop`.**

Si tu écris `loop:` mais que tu mets une valeur en dur au lieu de `{{ item }}`, la boucle ne sert à rien. Et `loop:` doit être au **même niveau** que le module, pas dedans. Le réflexe correct : utiliser **`{{ item }}`** dans les arguments, et bien aligner `loop:`.

## Exercices

### Guidé
Réécris l'installation de `htop`, `git` et `curl` avec une **boucle** `loop` (au lieu d'une liste dans `name`). Lance et vérifie que les trois paquets sont installés.

### Autonome
Crée trois utilisateurs avec une boucle `loop` sur le module `user`. Vérifie avec `id` sur la cible que les trois existent.

### Défi
Combine **boucle** et **condition** : installe une liste de paquets, mais seulement sur les machines de famille Debian (`when` + `loop`). Observe le comportement sur tes cibles.

## ✅ Tu sais maintenant…

- Répéter une tâche sur une liste avec **`loop`** et **`{{ item }}`**.
- Que `loop` évite la répétition de tâches.
- Quand `loop` est nécessaire (créer plusieurs utilisateurs) vs quand le module gère déjà les listes (paquets).

---

# Chapitre 6.6 — Afficher et diagnostiquer (`debug`)

## Le minimum à savoir

Le module **`debug`** affiche un message ou la valeur d'une variable. C'est ton outil pour **comprendre** ce qui se passe et **diagnostiquer**.

```yaml
- name: Afficher un message
  ansible.builtin.debug:
    msg: "Bonjour depuis {{ ansible_hostname }}"

- name: Afficher la valeur d'une variable
  ansible.builtin.debug:
    var: paquet_web        # affiche le contenu de la variable paquet_web
```

> Deux usages : **`msg`** pour un message libre (avec des `{{ }}` dedans), et **`var`** pour afficher directement le contenu d'une variable.

## Très utile en pratique

`debug` est précieux quand un playbook ne se comporte pas comme prévu : tu affiches la valeur d'une variable ou d'un fact pour **voir** ce qu'Ansible utilise réellement.

## Exemple simple

```yaml
- name: Vérifier une variable
  ansible.builtin.debug:
    var: ansible_distribution
```

## 🔍 Réflexe diagnostic

> Quand une condition `when` ou une variable ne se comporte pas comme tu l'attends, ajoute un **`debug`** pour **afficher** la valeur réelle. Tu verras souvent immédiatement le problème (un fait mal nommé, une variable vide, une valeur inattendue).

## ❌ Erreur classique

> **Confondre `msg` et `var`.**

`msg:` attend un **texte** (où tu peux insérer des `{{ }}`). `var:` attend un **nom de variable** (sans accolades). Écrire `var: "{{ paquet_web }}"` est redondant. Le réflexe correct : `msg` pour une phrase, `var` pour afficher une variable directement.

## Exercices

### Guidé
Ajoute une tâche `debug` qui affiche un message personnalisé avec le nom d'hôte (`msg: "Machine : {{ ansible_hostname }}"`). Lance et observe la sortie pour chaque machine.

### Autonome
Utilise `debug` avec `var:` pour afficher le contenu d'une variable que tu as définie (par exemple `paquet_web`). Vérifie que la valeur affichée correspond.

### Défi
Tu as une condition `when` qui ne se déclenche pas comme prévu. Ajoute un `debug` qui affiche le fait utilisé dans la condition (par exemple `ansible_os_family`). Utilise cet affichage pour comprendre pourquoi la condition est vraie ou fausse.

## ✅ Tu sais maintenant…

- Afficher messages et variables avec **`debug`** (`msg` et `var`).
- Utiliser `debug` pour **diagnostiquer** variables, facts et conditions.
- La différence entre **`msg`** (texte) et **`var`** (nom de variable).

---

## 🚩 Checkpoint — Fin de la Partie 6

Tes playbooks sont maintenant adaptables. Avant les templates, assure-toi de pouvoir :

- [ ] Définir et utiliser des **variables** (`vars`, `group_vars`, `host_vars`) avec la bonne priorité.
- [ ] Récolter et utiliser des **facts** (`setup`, `ansible_distribution`…).
- [ ] Écrire des conditions **`when`** (et comprendre `skipped`).
- [ ] Répéter avec des boucles **`loop`** et **`{{ item }}`**.
- [ ] Afficher et diagnostiquer avec **`debug`**.

> **🧩 Mini-projet (consolidation) — « Playbook adaptable ».**
> Écris un playbook qui : installe une liste de paquets en **boucle**, mais seulement sur les machines de la bonne famille d'OS (`when` + facts), en utilisant une **variable** pour la liste (rangée dans `group_vars`). Ajoute un `debug` qui affiche, pour chaque machine, son OS et sa version. Vérifie l'idempotence sur deux passages.

> **La suite :** en Partie 7, on génère des fichiers de configuration **dynamiques** avec les **templates Jinja2**, et on apprend à redémarrer un service **uniquement si nécessaire** grâce aux **handlers**.

---
---
---

# PARTIE 7 — TEMPLATES ET HANDLERS

> **Objectif de la partie :** générer des fichiers de configuration **dynamiques** avec les templates Jinja2 (un fichier adapté à chaque machine), et redémarrer un service **uniquement si nécessaire** grâce aux handlers.

---

# Chapitre 7.1 — Les templates Jinja2 (`template`)

## Le minimum à savoir

Avec `copy`, tu déposes un fichier **tel quel**, identique partout. Mais souvent, tu veux un fichier **adapté à chaque machine** : son nom d'hôte, son IP, un port spécifique. C'est le rôle du module **`template`** et du moteur **Jinja2**.

Un **template** est un fichier de configuration contenant des **variables** `{{ }}`. Ansible le **génère** pour chaque machine avec ses valeurs propres.

```jinja
{# fichier templates/motd.j2 #}
Bienvenue sur {{ ansible_hostname }}
OS : {{ ansible_distribution }} {{ ansible_distribution_version }}
Cette machine est administrée par Ansible.
```

```yaml
- name: Générer le message du jour personnalisé
  ansible.builtin.template:
    src: motd.j2               # le template (sur le contrôle)
    dest: /etc/motd            # le fichier généré (sur la cible)
  become: true
```

> **Le fichier généré sera différent sur chaque machine** : `cible1` aura son nom, `cible2` le sien. C'est toute la puissance des templates. Par convention, les templates ont l'extension **`.j2`** (pour Jinja2).

## Très utile en pratique

Jinja2 permet aussi des **conditions** et des **boucles** **dans** le fichier généré :

```jinja
{# Selon l'OS #}
{% if ansible_os_family == "Debian" %}
# Configuration Debian
{% endif %}

{# Une liste d'utilisateurs autorisés #}
{% for utilisateur in utilisateurs_autorises %}
AllowUsers {{ utilisateur }}
{% endfor %}
```

- `{{ }}` insère une **valeur**.
- `{% if %}` / `{% endif %}` : une **condition**.
- `{% for %}` / `{% endfor %}` : une **boucle**.

## Exemple simple

```jinja
{# templates/index.html.j2 #}
<h1>Bienvenue sur {{ ansible_hostname }}</h1>
```

```yaml
- name: Déployer une page d'accueil personnalisée
  ansible.builtin.template:
    src: index.html.j2
    dest: /var/www/html/index.html
  become: true
```

Chaque serveur affichera **son propre** nom dans la page.

## 🔀 À ne pas confondre

> **`copy` (fichier identique) vs `template` (fichier généré).**
> `copy` dépose un fichier **tel quel**, le même partout. `template` **génère** un fichier en remplaçant les `{{ }}` par les valeurs de chaque machine. Dès qu'un fichier doit **varier** selon la cible, c'est un **template**.

## ❌ Erreur classique

> **Utiliser `copy` puis se retrouver à maintenir dix versions d'un fichier de config.**

Si tu copies un fichier de config et que tu dois l'adapter machine par machine, tu finis avec dix fichiers presque identiques. Le réflexe correct : dès qu'un fichier varie selon la machine, **un seul template** avec des variables remplace les dix copies.

## Exercices

### Guidé
Crée un template `motd.j2` qui affiche le nom d'hôte et l'OS de chaque machine. Déploie-le avec `template` dans `/etc/motd`. Connecte-toi en SSH à chaque cible et vérifie que le contenu est **personnalisé**.

### Autonome
Crée un template de page web (`index.html.j2`) affichant le nom de la machine, et déploie-le dans `/var/www/html/`. Accède à chaque serveur (navigateur ou `curl`) et vérifie que chacun affiche son propre nom.

### Défi
Utilise une **boucle Jinja2** (`{% for %}`) dans un template pour générer une liste à partir d'une variable (par exemple une liste d'utilisateurs définie en `group_vars`). Vérifie le fichier généré sur la cible.

## ✅ Tu sais maintenant…

- Générer des fichiers **dynamiques** avec **`template`** et **Jinja2**.
- Insérer des valeurs (`{{ }}`), des conditions (`{% if %}`) et des boucles (`{% for %}`) dans un template.
- La convention d'extension **`.j2`**.
- La différence **`copy`** (identique) vs **`template`** (adapté à chaque machine).

---

# Chapitre 7.2 — `copy` vs `template` (bien choisir)

## Le minimum à savoir

Maintenant que tu connais les deux, voici comment **choisir** :

| Situation | Module à utiliser |
|-----------|-------------------|
| Le fichier est **identique** sur toutes les machines | **`copy`** |
| Le fichier doit **varier** selon la machine (nom, IP, port…) | **`template`** |
| Tu veux ajuster **une seule ligne** d'un fichier existant | **`lineinfile`** (Partie 5) |

> **En résumé :** `copy` = fichier figé, `template` = fichier généré, `lineinfile` = une ligne. Trois outils, trois usages.

## Très utile en pratique

Beaucoup de fichiers de configuration réels (nginx, ssh…) contiennent des valeurs spécifiques à la machine. Dans la vraie vie, on utilise donc surtout **`template`** pour les configs, et `copy` pour les fichiers statiques (un script, une image, un fichier de licence).

## Exemple simple

- Un logo identique partout → `copy`.
- Une config nginx avec le nom du serveur → `template`.

## ❌ Erreur classique

> **Hésiter entre les deux et choisir au hasard.**

Le réflexe correct est simple : **« est-ce que ce fichier doit être différent selon la machine ? »** Si oui → `template`. Si non → `copy`. Cette seule question tranche presque toujours.

## Exercices

### Guidé
Liste trois fichiers que tu pourrais déployer (par exemple : un logo, une config nginx, un script). Pour chacun, dis si tu utiliserais `copy` ou `template`, et **pourquoi**.

### Autonome
Prends un fichier que tu as déployé avec `copy` et qui gagnerait à être personnalisé. Transforme-le en `template` avec au moins une variable. Compare le résultat sur deux machines.

### Défi
Explique en quelques lignes pourquoi, dans un vrai projet, on utilise surtout `template` pour les fichiers de configuration. Qu'apporte la génération dynamique par rapport à des copies figées ?

## ✅ Tu sais maintenant…

- Choisir entre **`copy`** (identique), **`template`** (généré) et **`lineinfile`** (une ligne).
- La question qui tranche : « ce fichier doit-il varier selon la machine ? ».
- Que les configs réelles utilisent surtout **`template`**.

---

# Chapitre 7.3 — Les handlers (`notify`)

## Le minimum à savoir

Quand tu modifies la configuration d'un service, il faut souvent le **redémarrer** pour appliquer le changement. Mais le redémarrer **à chaque** exécution (même quand rien n'a changé) provoque des interruptions inutiles. La solution : les **handlers**.

Un **handler** est une tâche spéciale qui ne s'exécute **que si elle est notifiée** par un changement.

```yaml
tasks:
  - name: Déployer la config nginx
    ansible.builtin.template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Redémarrer nginx        # ← notifie le handler SI cette tâche change qqch
    become: true

handlers:
  - name: Redémarrer nginx          # ← le handler (déclenché seulement si notifié)
    ansible.builtin.service:
      name: nginx
      state: restarted
    become: true
```

> **Le mécanisme :** si la tâche de config **change** quelque chose (`changed`), elle **notifie** le handler, qui s'exécute **à la fin** du play. Si la config n'a **pas** changé (`ok`), le handler **ne s'exécute pas**. Résultat : **on ne redémarre que si nécessaire.**

## Très utile en pratique

```
   Config modifiée (changed)  →  handler notifié  →  service redémarré
   Config inchangée (ok)       →  handler NON notifié →  service PAS redémarré
```

C'est exactement ce qu'on veut : pas de redémarrage inutile, mais un redémarrage **garanti** quand la config change.

## Exemple simple

```yaml
tasks:
  - name: Modifier la config SSH
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^#?PermitRootLogin'
      line: 'PermitRootLogin no'
    notify: Redemarrer ssh
    become: true

handlers:
  - name: Redemarrer ssh
    ansible.builtin.service:
      name: ssh
      state: restarted
    become: true
```

## 🔀 À ne pas confondre

> **Tâche normale vs handler.**
> Une **tâche** s'exécute à chaque fois (selon son idempotence). Un **handler** ne s'exécute **que s'il est notifié** par un changement, et **une seule fois** à la fin, même s'il est notifié plusieurs fois. C'est fait pour les actions « à déclencher si quelque chose a changé ».

## ❌ Erreur classique

> **Mettre un `restart` directement dans les tâches au lieu d'utiliser un handler.**

Une tâche `service: state=restarted` placée dans les `tasks` redémarre le service **à chaque** exécution, même quand rien n'a changé — interruptions inutiles. Le réflexe correct : mettre le redémarrage dans un **handler**, notifié par la tâche de config. Le service ne redémarre **que** quand sa config change réellement.

## Exercices

### Guidé
Transforme ton playbook nginx : déploie la config par `template` (ou modifie une ligne par `lineinfile`), et **notifie** un handler « Redémarrer nginx ». Lance le playbook : le handler se déclenche (config posée). Relance-le : le handler **ne se déclenche pas** (rien n'a changé).

### Autonome
Crée un handler pour redémarrer SSH, notifié par une modification de `sshd_config`. Vérifie qu'il ne se déclenche que lorsque la config change réellement. (Attention : teste sur une cible avec snapshot, pour ne pas te couper l'accès.)

### Défi
Mets **deux** tâches qui notifient le **même** handler. Observe qu'il ne s'exécute **qu'une seule fois** à la fin, même notifié deux fois. Explique pourquoi ce comportement est utile.

## ✅ Tu sais maintenant…

- Ce qu'est un **handler** : une tâche déclenchée **uniquement si notifiée** par un changement.
- Utiliser **`notify`** pour relier une tâche à un handler.
- Que le handler s'exécute **à la fin** du play, **une seule fois**.
- Que les handlers évitent les **redémarrages inutiles**.

---

## 🚩 Checkpoint — Fin de la Partie 7

Tu sais maintenant générer de la config et redémarrer proprement. Avant les bonnes pratiques, assure-toi de pouvoir :

- [ ] Générer des fichiers dynamiques avec **`template`** + **Jinja2** (`{{ }}`, `{% if %}`, `{% for %}`).
- [ ] Choisir entre **`copy`**, **`template`** et **`lineinfile`**.
- [ ] Utiliser des **handlers** avec **`notify`** pour redémarrer un service seulement si nécessaire.

> **🧩 Mini-projet 8 — « Générer une configuration avec template ».**
> Déploie un fichier de configuration (par exemple un `motd` ou une page web) **personnalisé par machine** grâce à un template Jinja2. Vérifie que chaque cible a sa version.
>
> **🧩 Mini-projet 9 — « Handler conditionnel ».**
> Déploie une config de service par template, avec un **handler** de redémarrage notifié. Lance deux fois : observe que le service ne redémarre **qu'au premier passage** (quand la config change), pas au second.

> **La suite :** en Partie 8, on apprend les **bons réflexes** du débutant : nommer ses tâches, vérifier avant d'agir (`--check`, `--diff`), cibler avec prudence (`--limit`), et les bases de sécurité (clés SSH, pas de secret en clair).

---
---

# PARTIE 8 — BONNES PRATIQUES DÉBUTANT

> **Objectif de la partie :** acquérir les bons réflexes sans alourdir. Quelques habitudes simples qui font la différence entre un playbook fragile et un playbook fiable.

---

# Chapitre 8.1 — Lisibilité et modules dédiés

## Le minimum à savoir

Deux habitudes qui rendent tes playbooks **lisibles et fiables** :

1. **Nommer chaque tâche** avec un `name:` clair. Le nom apparaît dans la sortie : un playbook bien nommé **se lit comme une procédure**.
2. **Préférer les modules dédiés** à `command`/`shell` (rappel Partie 3). Un module dédié est idempotent et explicite.

```yaml
# ✅ BON : nommé, module dédié
- name: Installer nginx
  ansible.builtin.apt:
    name: nginx
    state: present

# ❌ MOINS BON : pas de nom, shell non idempotent
- ansible.builtin.shell: apt install -y nginx
```

## Très utile en pratique

Un playbook lisible, c'est :
- des `name:` qui décrivent **ce que fait** chaque tâche ;
- des modules dédiés plutôt que du `shell` ;
- une structure claire (un play par objectif).

C'est ce qui te permet, dans six mois, de **relire** ton playbook et de le comprendre — et à un collègue de le reprendre.

## Exemple simple

```yaml
- name: Configurer le serveur web
  hosts: web
  become: true
  tasks:
    - name: Installer nginx
      ansible.builtin.apt:
        name: nginx
        state: present

    - name: Démarrer et activer nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

On **lit** ce playbook comme une recette.

## ❌ Erreur classique

> **Des tâches sans nom et des `shell` partout.**

Un playbook fait de tâches anonymes et de `shell` est illisible et fragile. Le réflexe correct : **nomme** chaque tâche, et **cherche le module dédié** avant de sortir `shell`.

## Exercices

### Guidé
Reprends un de tes playbooks et vérifie que **chaque** tâche a un `name:` clair. Renomme celles qui sont vagues (« tâche 1 » → « Installer nginx »).

### Autonome
Cherche dans tes playbooks un `command`/`shell` que tu pourrais remplacer par un module dédié. Réécris-le. Vérifie que le comportement est identique mais désormais idempotent.

### Défi
Donne ton playbook à relire à quelqu'un (ou relis-le toi-même à voix haute). Est-ce qu'on **comprend** ce qu'il fait juste en lisant les `name:` ? Si non, améliore-les.

## ✅ Tu sais maintenant…

- **Nommer** chaque tâche pour la lisibilité.
- Préférer les **modules dédiés** à `command`/`shell`.
- Qu'un playbook lisible **se lit comme une procédure**.

---

# Chapitre 8.2 — Vérifier avant d'agir (`--check`, `--diff`)

## Le minimum à savoir

Tu connais déjà `--check` (Partie 4). Ajoute **`--diff`** : il **montre les changements** qu'Ansible ferait (les lignes modifiées d'un fichier, par exemple).

```bash
ansible-playbook -i inventory.ini site.yml --check --diff
```

- **`--check`** : simule (ne modifie rien).
- **`--diff`** : montre **le détail** de ce qui changerait.

Combinés, ils te donnent un **aperçu précis** avant d'agir.

## Très utile en pratique

`--diff` est particulièrement utile avec les **templates** et **`lineinfile`** : il t'affiche **exactement** les lignes ajoutées ou modifiées dans le fichier, avant que tu n'appliques.

```text
--- avant
+++ après
-PermitRootLogin yes
+PermitRootLogin no
```

## Exemple simple

```bash
ansible-playbook -i inventory.ini hardening.yml --check --diff
```
Tu **vois** ce qui changerait, sans rien toucher.

## 🔍 Réflexe diagnostic

> Avant d'appliquer une modification de config importante, lance **`--check --diff`**. Tu vois précisément ce qui va changer. Si le diff ne correspond pas à ce que tu attendais, **n'applique pas** : corrige d'abord.

## ❌ Erreur classique

> **Appliquer une modification de config sans regarder le diff.**

On modifie un fichier système (SSH, par exemple) sans vérifier, et on découvre un effet de bord après coup. Le réflexe correct : **`--check --diff`** avant d'appliquer toute modification de configuration sensible.

## Exercices

### Guidé
Sur un playbook qui modifie un fichier (template ou `lineinfile`), lance `--check --diff`. Observe les lignes affichées (avant/après). Puis applique pour de vrai et compare.

### Autonome
Modifie volontairement ton template, puis lance `--check --diff` : tu dois voir **uniquement** les lignes que tu as changées. Tu valides ainsi que ton changement est bien ciblé.

### Défi
Lance `--check --diff` sur un playbook **déjà appliqué** (tout est conforme). Le diff doit être **vide** et tout en `ok`. Explique ce que ça t'apprend sur l'état de tes machines.

## ✅ Tu sais maintenant…

- Simuler avec **`--check`** et voir le détail avec **`--diff`**.
- Que `--diff` montre les **lignes** qui changeraient (utile pour templates/`lineinfile`).
- Le réflexe : **`--check --diff`** avant toute modif de config importante.

---

# Chapitre 8.3 — Cibler avec prudence (`--limit`)

## Le minimum à savoir

Quand tu lances un playbook, il s'applique à **tout** ce que vise `hosts:`. L'option **`--limit`** permet de **restreindre** à une machine ou un sous-groupe précis — un garde-fou très utile.

```bash
# Le playbook vise "web", mais on le limite à une seule machine
ansible-playbook -i inventory.ini site.yml --limit cible1
```

> **`--limit` est ton garde-fou de périmètre.** Il te permet de **tester sur une seule machine** avant d'appliquer à tout le groupe. Indispensable pour les actions importantes.

## Très utile en pratique

La bonne démarche pour une action importante :

```
1. --check --diff           (simuler, voir ce qui changerait)
2. --limit cible1           (appliquer à UNE machine d'abord)
3. vérifier que tout va bien sur cible1
4. lancer sur tout le groupe (sans --limit)
```

Tu valides sur une machine **témoin** avant de généraliser.

## Exemple simple

```bash
ansible-playbook -i inventory.ini site.yml --limit cible1   # une seule machine
ansible-playbook -i inventory.ini site.yml                  # tout le groupe
```

## 🧪 Lab vs production

> En **lab**, l'enjeu est faible. Mais prends l'habitude de `--limit` **dès maintenant** : en **production**, appliquer une action à tout un parc d'un coup sans l'avoir testée sur une machine témoin est **risqué**. Le bon geste appris en lab te protégera plus tard.

## ❌ Erreur classique

> **Lancer un playbook sur tout le parc sans l'avoir testé sur une seule machine.**

Une erreur dans le playbook se propage alors à **toutes** les machines d'un coup. Le réflexe correct : **`--limit` sur une machine témoin d'abord**, vérifier, **puis** généraliser. C'est rapide et ça évite les incidents en chaîne.

## Exercices

### Guidé
Lance un de tes playbooks avec `--limit cible1`. Vérifie qu'il ne s'applique qu'à cette machine (l'autre n'apparaît pas dans la sortie). Puis relance sans `--limit` et observe qu'il touche tout le groupe.

### Autonome
Adopte la démarche complète sur un playbook qui modifie quelque chose : `--check --diff`, puis `--limit cible1`, vérification, puis tout le groupe. Note chaque étape.

### Défi
Combine `--limit` avec un groupe : si tu as un groupe `web` de plusieurs machines, limite à une seule d'entre elles. Réfléchis : en quoi `--limit` est-il un filet de sécurité complémentaire de `--check` ?

## ✅ Tu sais maintenant…

- Restreindre l'exécution avec **`--limit`** (une machine ou un sous-groupe).
- La démarche : **simuler → tester sur une machine témoin → généraliser**.
- Que `--limit` est un **garde-fou de périmètre** essentiel.

---

# Chapitre 8.4 — Hygiène de sécurité de base

## Le minimum à savoir

Quelques réflexes simples, sans transformer ce cours en cours de sécurité :

- **Protéger les clés SSH** : la clé privée reste sur le contrôle, ne se partage pas, ne se commite pas.
- **Pas de mot de passe en clair** dans les playbooks ou l'inventaire (on chiffrera avec Vault en Partie 9).
- **Séparer lab et production** : des inventaires distincts, pour ne jamais viser la prod en croyant viser le lab.
- **`become` au juste besoin** : root seulement là où c'est nécessaire.

## Très utile en pratique

> 🛡️ **Réflexe sécurité :** avant de versionner un projet (Git, Partie 10), demande-toi toujours : « y a-t-il un secret en clair là-dedans ? une clé privée ? un mot de passe ? ». Si oui, **ne commite pas** : chiffre d'abord (Vault) ou exclus le fichier.

## Exemple simple

Mauvais (mot de passe en clair) :
```yaml
vars:
  db_password: SuperSecret123    # ❌ JAMAIS en clair
```

Bon (on chiffrera ça avec Vault, Partie 9) :
```yaml
vars_files:
  - secrets.yml                  # ✅ fichier chiffré par Vault
```

## 🧪 Lab vs production

> En **lab**, tu peux te permettre des raccourcis (comme un mot de passe simple pour tester). Mais ne prends **jamais** l'habitude de mettre des secrets en clair, car ce réflexe te suivrait en production, où c'est dangereux.

## ❌ Erreur classique

> **Mettre un mot de passe en clair « juste pour tester », puis l'oublier et le versionner.**

« Je le chiffrerai plus tard » est la phrase qui mène à la fuite. Le réflexe correct : dès qu'il y a un secret, utilise **Vault** (Partie 9) ou exclus le fichier du dépôt. Ne laisse **jamais** un secret en clair traîner dans un projet.

## Exercices

### Guidé
Vérifie tes playbooks et ton inventaire : y a-t-il un mot de passe ou un secret en clair ? Si oui, note-le — on le chiffrera en Partie 9.

### Autonome
Crée deux inventaires distincts : `inventory_lab.ini` et `inventory_prod.ini` (même fictif). Explique pourquoi cette séparation est une bonne habitude.

### Défi
Liste les fichiers de ton projet qui ne devraient **jamais** être partagés ou versionnés en clair (clé privée, secrets…). Tu prépares ainsi le `.gitignore` de la Partie 10.

## ✅ Tu sais maintenant…

- Protéger les **clés SSH** (privée secrète, jamais partagée).
- Ne **jamais** mettre de secret en clair (→ Vault, Partie 9).
- **Séparer** les inventaires lab et production.
- Utiliser **`become`** au juste besoin.

---

## 🚩 Checkpoint — Fin de la Partie 8

Tu as les bons réflexes de base. Avant Vault, assure-toi de pouvoir :

- [ ] **Nommer** tes tâches et préférer les **modules dédiés**.
- [ ] Vérifier avec **`--check --diff`** avant d'agir.
- [ ] Cibler avec **`--limit`** (machine témoin d'abord).
- [ ] Protéger les **clés SSH** et éviter les **secrets en clair**.

> Pas de nouveau mini-projet ici : applique ces réflexes à **tous** tes playbooks existants. Reprends-les, nomme les tâches, ajoute `--check --diff` à tes habitudes, teste avec `--limit`.

> **La suite :** en Partie 9, on apprend à gérer les **secrets** proprement avec **Ansible Vault** — pour ne plus jamais écrire un mot de passe en clair.

---
---

# PARTIE 9 — ANSIBLE VAULT ET SECRETS

> **Objectif de la partie :** gérer les secrets (mots de passe, clés) **sans** les écrire en clair, grâce à Ansible Vault.

---

# Chapitre 9.1 — Pourquoi ne pas mettre de secret en clair

## Le minimum à savoir

Tes playbooks ont parfois besoin de **secrets** : un mot de passe, une clé d'API. Les écrire **en clair** est une **mauvaise pratique** :

- N'importe qui ayant accès au fichier les **lit**.
- Si tu versionnes ton projet (Git), ils se retrouvent dans l'**historique** — et un secret poussé dans Git est **compromis**, même si tu le retires ensuite.

> **La règle :** **aucun secret en clair, jamais.** Et surtout pas dans un dépôt Git. C'est exactement pour ça qu'Ansible Vault existe.

## Très utile en pratique

Un secret peut traîner dans :
- une variable de playbook (`db_password: ...`) ;
- un fichier de variables (`group_vars/...`) ;
- l'inventaire.

Partout où il y a un secret, il faut le **chiffrer** avec Vault.

## Exemple simple

À éviter absolument :
```yaml
vars:
  db_password: SuperSecret123    # ❌ lisible par tous, versionné dans Git
```

## ❌ Erreur classique

> **« Je mettrai le mot de passe en clair maintenant, je sécuriserai plus tard. »**

Le « plus tard » n'arrive jamais, et le secret finit dans Git. Le réflexe correct : **chiffrer dès le premier secret**. Ne laisse jamais un secret en clair, même temporairement, dans un projet versionné.

## Exercices

### Guidé
Cherche dans tes playbooks et ton inventaire s'il y a un secret en clair (même fictif). Note-le : on va le chiffrer au chapitre suivant.

### Autonome
Explique en 3-4 phrases pourquoi un secret poussé dans Git est considéré comme **compromis**, même après l'avoir retiré du fichier.

### Défi
Imagine les conséquences concrètes d'un mot de passe de base de données versionné en clair dans un dépôt partagé. Qui pourrait y accéder ? Pourquoi est-ce difficile à rattraper ?

## ✅ Tu sais maintenant…

- Pourquoi un secret en clair est une **faute** (lisible, versionné, compromis à vie).
- Qu'il ne faut **jamais** mettre de secret en clair, surtout dans Git.
- Que la solution est de **chiffrer** avec Ansible Vault.

---

# Chapitre 9.2 — Chiffrer avec Ansible Vault

## Le minimum à savoir

**Ansible Vault** chiffre tes secrets. Le fichier devient illisible sans le mot de passe Vault, mais reste **utilisable** par Ansible à l'exécution.

```bash
# Créer un fichier chiffré
ansible-vault create secrets.yml

# Éditer un fichier chiffré (demande le mot de passe Vault)
ansible-vault edit secrets.yml

# Afficher le contenu (sans le déchiffrer sur le disque)
ansible-vault view secrets.yml

# Chiffrer un fichier existant
ansible-vault encrypt group_vars/web/secrets.yml
```

Un fichier chiffré ressemble à ça — **illisible**, donc **versionnable sans danger** :

```text
$ANSIBLE_VAULT;1.1;AES256
66386439653...   (contenu chiffré)
```

## Très utile en pratique

Quand tu crées un fichier Vault, Ansible te demande un **mot de passe Vault**. Ce mot de passe te sera redemandé pour lire ou utiliser le fichier. Choisis-en un solide, et **ne le mets jamais dans le projet**.

## Exemple simple

```bash
ansible-vault create secrets.yml
# Ansible demande un mot de passe, puis ouvre un éditeur.
# Tu écris :  db_password: SuperSecret123
# Tu sauvegardes : le fichier est chiffré.
```

```bash
cat secrets.yml      # → contenu chiffré, illisible
```

## ❌ Erreur classique

> **Oublier son mot de passe Vault.**

Sans le mot de passe, **personne** ne peut déchiffrer le fichier — c'est le but du chiffrement. Le réflexe correct : conserver le mot de passe Vault dans un **gestionnaire de mots de passe**, jamais dans le projet. Le perdre, c'est perdre l'accès aux secrets.

## Exercices

### Guidé
Crée un fichier chiffré avec `ansible-vault create secrets.yml` contenant une variable `db_password`. Vérifie avec `cat secrets.yml` que le contenu est **illisible**. Ouvre-le avec `ansible-vault view` pour confirmer que tu peux le lire avec le mot de passe.

### Autonome
Édite le fichier avec `ansible-vault edit secrets.yml` et ajoute une seconde variable. Sauvegarde et vérifie qu'il reste chiffré. Tu maîtrises le cycle créer/éditer/voir.

### Défi
Crée un fichier de variables **en clair**, puis chiffre-le avec `ansible-vault encrypt`. Vérifie qu'il est devenu illisible. Dans quel cas cette commande (`encrypt`) est-elle utile par rapport à `create` ?

## ✅ Tu sais maintenant…

- Chiffrer des secrets avec **`ansible-vault`** (`create`, `edit`, `view`, `encrypt`).
- Qu'un fichier Vault est **illisible** sans le mot de passe (donc versionnable).
- Qu'il faut **conserver précieusement** le mot de passe Vault (hors du projet).

---

# Chapitre 9.3 — Utiliser un secret chiffré

## Le minimum à savoir

Une fois ton secret chiffré, tu l'utilises dans un playbook **comme une variable normale**. Ansible le déchiffre à la volée au moment de l'exécution.

```yaml
# secrets.yml (chiffré) contient :  db_password: SuperSecret123

- name: Configurer la base de données
  hosts: db
  vars_files:
    - secrets.yml            # ← charge le fichier chiffré
  tasks:
    - name: Afficher (pour l'exemple) que le secret est disponible
      ansible.builtin.debug:
        msg: "Le mot de passe est chargé (longueur : {{ db_password | length }})"
```

Pour lancer un playbook qui utilise des secrets Vault, il faut **fournir le mot de passe** :

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
```

`--ask-vault-pass` demande le mot de passe Vault au lancement.

## Très utile en pratique

L'organisation propre : séparer les variables **normales** des variables **secrètes**.

```
group_vars/
└── web/
    ├── vars.yml        # variables NORMALES (en clair, versionnées)
    └── vault.yml       # variables SECRÈTES (chiffrées par Vault)
```

Ansible charge **automatiquement** les deux pour le groupe `web`. Les secrets sont chiffrés, le reste reste lisible.

## Exemple simple

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
# → Ansible demande le mot de passe Vault, puis déchiffre les secrets à la volée
```

## 🔍 Réflexe diagnostic

> Une erreur **« Attempting to decrypt but no vault secrets found »** signifie que tu as **oublié `--ask-vault-pass`** (ou le fichier de mot de passe). Ansible a trouvé du contenu chiffré mais n'a pas la clé pour le lire. Ajoute `--ask-vault-pass`.

## ❌ Erreur classique

> **Lancer un playbook avec des secrets Vault sans fournir le mot de passe.**

Sans `--ask-vault-pass`, Ansible ne peut pas déchiffrer et s'arrête en erreur. Le réflexe correct : dès qu'un playbook utilise un fichier Vault, **ajoute `--ask-vault-pass`** au lancement.

## Exercices

### Guidé
Utilise la variable `db_password` (chiffrée au chapitre précédent) dans un playbook, via `vars_files: - secrets.yml`. Lance avec `--ask-vault-pass` et vérifie que ça fonctionne. Puis lance **sans** `--ask-vault-pass` et observe l'erreur.

### Autonome
Organise tes variables en `vars.yml` (clair) et `vault.yml` (chiffré) dans un `group_vars`. Place une variable normale dans l'un, un secret dans l'autre. Lance un playbook qui utilise les deux.

### Défi
Explique en quelques lignes pourquoi la **séparation** vars.yml / vault.yml est meilleure que de tout chiffrer (on perd en lisibilité) ou de tout laisser en clair (on perd les secrets). Quel équilibre apporte-t-elle ?

## ✅ Tu sais maintenant…

- Utiliser un secret chiffré comme une **variable normale** (`vars_files`).
- Fournir le mot de passe Vault avec **`--ask-vault-pass`**.
- Séparer **`vars.yml`** (clair) et **`vault.yml`** (chiffré).
- Reconnaître l'erreur « no vault secrets found ».

---

## 🚩 Checkpoint — Fin de la Partie 9

Tu sais gérer les secrets proprement. Avant d'organiser un vrai projet, assure-toi de pouvoir :

- [ ] Expliquer pourquoi un secret en clair (surtout dans Git) est une **faute**.
- [ ] Chiffrer un secret avec **`ansible-vault`** (`create`, `edit`, `view`).
- [ ] Utiliser un secret chiffré dans un playbook (`vars_files`, `--ask-vault-pass`).
- [ ] Séparer variables normales (`vars.yml`) et secrètes (`vault.yml`).

> **🧩 Mini-projet 10 — « Chiffrer une variable avec Vault ».**
> Crée un fichier `vault.yml` chiffré contenant un mot de passe. Utilise-le dans un playbook (par exemple pour configurer un fichier via template). Lance avec `--ask-vault-pass`. Vérifie qu'aucun secret n'apparaît en clair dans tes fichiers non chiffrés.

> **La suite :** en Partie 10, on passe de playbooks isolés à un **projet Ansible organisé** : arborescence, `ansible.cfg`, Git et documentation.

---
---

# PARTIE 10 — ORGANISER UN PROJET ANSIBLE

> **Objectif de la partie :** passer de petits playbooks éparpillés à un **projet propre**, structuré, versionné et documenté.

---

# Chapitre 10.1 — Une arborescence propre

## Le minimum à savoir

À mesure que ton projet grandit, il faut l'**organiser**. Voici une structure simple et standard :

```
mon-projet/
├── ansible.cfg            # configuration du projet
├── inventory.ini          # l'inventaire
├── group_vars/            # variables par groupe
│   ├── all.yml
│   └── web.yml
├── host_vars/             # variables par hôte
├── playbooks/             # les playbooks
│   └── site.yml
├── roles/                 # les roles (Partie 11)
├── templates/             # les templates Jinja2 (ou dans les roles)
├── README.md              # documentation
└── .gitignore             # fichiers à ne pas versionner
```

> **L'idée :** chaque chose à sa place. Inventaire, variables, playbooks, roles, templates sont rangés dans des dossiers prévisibles. N'importe qui (toi dans six mois, ou un collègue) **s'y retrouve**.

## Très utile en pratique

Tu n'as pas besoin de **tous** ces dossiers dès le début. Commence simple (inventaire + un playbook + `ansible.cfg`), et ajoute les dossiers (`group_vars`, `roles`…) **quand tu en as besoin**.

## Exemple simple

Un projet minimal mais propre :

```
mon-projet/
├── ansible.cfg
├── inventory.ini
└── playbooks/
    └── site.yml
```

## ❌ Erreur classique

> **Tout mettre dans un seul gros fichier, ou éparpiller les fichiers sans logique.**

Un projet désorganisé devient vite ingérable. Le réflexe correct : adopter une **structure standard** dès que le projet dépasse deux ou trois fichiers. Ça paraît superflu au début, mais ça paie très vite.

## Exercices

### Guidé
Réorganise tes fichiers existants selon l'arborescence proposée : inventaire à la racine, playbooks dans `playbooks/`, variables dans `group_vars/`. Vérifie que tout fonctionne encore.

### Autonome
Crée un dossier `templates/` et déplaces-y tes fichiers `.j2`. Ajuste les chemins `src:` si besoin. Lance un playbook pour vérifier que les templates sont toujours trouvés.

### Défi
Dessine (ou écris) l'arborescence **idéale** pour ton projet actuel. Justifie l'emplacement de chaque type de fichier. En quoi cette organisation facilite-t-elle la reprise du projet par quelqu'un d'autre ?

## ✅ Tu sais maintenant…

- Organiser un projet selon une **arborescence standard**.
- Que chaque type de fichier a son **dossier** (inventaire, variables, playbooks, roles, templates).
- Commencer **simple** et ajouter les dossiers au besoin.

---

# Chapitre 10.2 — Le fichier `ansible.cfg`

## Le minimum à savoir

Depuis le début, tu tapes `-i inventory.ini` à chaque commande. Le fichier **`ansible.cfg`**, placé à la racine de ton projet, rassemble ces réglages **une fois pour toutes**.

```ini
# ansible.cfg
[defaults]
inventory = ./inventory.ini          # plus besoin de -i !
remote_user = admin                  # utilisateur SSH par défaut
private_key_file = ~/.ssh/id_ed25519 # clé privée à utiliser
host_key_checking = False            # pratique en lab (voir avertissement)
```

> **Avec `ansible.cfg`, les commandes raccourcissent :**
> ```bash
> # Avant :
> ansible web -i inventory.ini -u admin -m ansible.builtin.ping
> # Après :
> ansible web -m ansible.builtin.ping
> ```

## Très utile en pratique

```bash
# Vérifier quel ansible.cfg est utilisé
ansible --version       # affiche le chemin du fichier de config lu
```

Quand tu lances une commande depuis un dossier contenant un `ansible.cfg`, Ansible le lit **automatiquement**.

## Exemple simple

```ini
[defaults]
inventory = ./inventory.ini
remote_user = admin
```

Avec ça, `ansible all -m ansible.builtin.ping` fonctionne **sans** `-i` ni `-u`.

## 🧪 Lab vs production

> `host_key_checking = False` désactive une vérification de sécurité SSH. **En lab**, c'est commode (les VMs changent souvent). **En production**, garde cette vérification **active** : elle protège contre certaines attaques. Ne désactive ce réglage que pour un lab.

## ❌ Erreur classique

> **Croire qu'un réglage « ne marche pas », alors qu'un autre `ansible.cfg` est lu.**

Ansible peut trouver plusieurs fichiers de config. Si tu édites le mauvais, tes changements semblent ignorés. Le réflexe correct : lancer **`ansible --version`** pour voir **quel fichier est réellement utilisé**, et travailler avec un `ansible.cfg` **à la racine de ton projet**.

## Exercices

### Guidé
Crée un `ansible.cfg` à la racine de ton projet avec `inventory`, `remote_user` et `private_key_file`. Lance une commande **sans** `-i` ni `-u` : elle doit fonctionner grâce au `ansible.cfg`. Vérifie avec `ansible --version` que c'est bien ton fichier qui est lu.

### Autonome
Compare une commande **avant** (`-i ... -u ...`) et **après** (`ansible.cfg` en place). Mesure le confort gagné. Toutes tes commandes du cours peuvent-elles maintenant se passer de `-i` ?

### Défi
Ajoute `host_key_checking = False` à ton `ansible.cfg` de lab. Explique en quelques lignes pourquoi ce réglage est pratique en lab mais **déconseillé** en production.

## ✅ Tu sais maintenant…

- Que **`ansible.cfg`** centralise la configuration (inventaire, utilisateur, clé).
- Qu'il évite de répéter **`-i`** et **`-u`** à chaque commande.
- Vérifier quel fichier est lu avec **`ansible --version`**.
- Que `host_key_checking = False` est un réglage **de lab**.

---

# Chapitre 10.3 — Git, `.gitignore` et documentation

## Le minimum à savoir

Un projet Ansible devrait être dans **Git** : historique des changements, retour arrière, travail à plusieurs. Mais attention aux **secrets**.

```gitignore
# .gitignore
*.retry
.vault_pass          # le mot de passe Vault, JAMAIS dans Git
```

> 🛡️ **Réflexe sécurité :** le `.gitignore` empêche de versionner les fichiers sensibles. Exclus tout fichier de **mot de passe Vault** et toute **clé privée**. Les fichiers **chiffrés par Vault**, eux, peuvent être versionnés (ils sont illisibles sans la clé).

### Documenter avec un README

Un fichier **`README.md`** explique le projet : à quoi il sert, comment l'utiliser, comment lancer les playbooks. Un projet sans documentation est difficile à reprendre.

## Très utile en pratique

```bash
git init
git add .
git status              # VÉRIFIER qu'aucun secret en clair n'est suivi !
git commit -m "Projet Ansible : inventaire, playbooks, role common"
```

> 🔍 **Réflexe diagnostic / sécurité :** avant **chaque** commit, lance `git status` et **vérifie** qu'aucun fichier sensible (secret en clair, clé privée) n'est sur le point d'être versionné.

## Exemple simple

Un `README.md` minimal :
```markdown
# Mon projet Ansible

Administration des serveurs web.

## Utilisation
ansible-playbook playbooks/site.yml --ask-vault-pass
```

## ❌ Erreur classique

> **Commiter une clé privée ou un secret en clair par mégarde.**

Un `git add .` un peu rapide, et un secret part dans l'historique. Le réflexe correct : un **`.gitignore`** solide **dès le début**, et un **`git status`** systématique avant chaque commit. Un secret déjà poussé doit être considéré comme **compromis** (le changer, pas juste le retirer).

## Exercices

### Guidé
Initialise Git dans ton projet. Crée un `.gitignore` excluant `.vault_pass` et les clés privées. Fais un premier commit après avoir vérifié `git status`. Confirme qu'aucun secret n'est suivi.

### Autonome
Rédige un `README.md` pour ton projet : à quoi il sert, comment lancer le playbook principal, quels prérequis. Place-le à la racine et commite-le.

### Défi
Structure ton projet complet (arborescence + `ansible.cfg` + `.gitignore` + README) et fais un commit propre. Vérifie que tes fichiers Vault chiffrés sont bien versionnés (c'est voulu) mais qu'aucun secret en clair ne l'est.

## ✅ Tu sais maintenant…

- Versionner un projet avec **Git**.
- Protéger les secrets avec un **`.gitignore`** (mot de passe Vault, clés privées).
- Que les fichiers **chiffrés par Vault** peuvent être versionnés.
- Documenter avec un **`README.md`**.
- Vérifier **`git status`** avant chaque commit.

---

## 🚩 Checkpoint — Fin de la Partie 10

Ton projet est maintenant organisé. Avant les roles, assure-toi de pouvoir :

- [ ] Organiser un projet selon une **arborescence standard**.
- [ ] Utiliser un **`ansible.cfg`** (fini les `-i` répétés).
- [ ] Versionner avec **Git** et protéger les secrets avec **`.gitignore`**.
- [ ] Documenter avec un **README**.

> **🧩 Mini-projet 11 — « Organiser un mini-projet Ansible propre ».**
> Structure ton projet : `ansible.cfg`, inventaire, `group_vars`, dossier `playbooks/`, README, `.gitignore`. Initialise Git et fais un commit propre (après `git status`). Tu as maintenant un projet réutilisable et partageable.

> **La suite :** en Partie 11, on découvre les **roles** : comment regrouper et réutiliser ton code proprement, sans aller trop loin.

---
---

# PARTIE 11 — ROLES SIMPLES

> **Objectif de la partie :** comprendre pourquoi et comment créer un **role** basique, pour organiser et réutiliser ton code. On reste simple : juste l'essentiel.

---

# Chapitre 11.1 — Pourquoi les roles existent

## Le minimum à savoir

À force d'ajouter des tâches, un playbook devient **long et difficile à relire**. Et tu te retrouves à **copier-coller** les mêmes tâches d'un projet à l'autre. Les **roles** résolvent ça : ils **regroupent et réutilisent** le code.

> **Un role**, c'est un ensemble cohérent de tâches, templates, variables et handlers, **rangés** dans une structure standard, qu'on peut **réutiliser** dans n'importe quel playbook. Par exemple, un role `common` qui installe les paquets de base et applique la config commune à toutes tes machines.

## Très utile en pratique

L'intérêt des roles :
- **Organiser** : un gros playbook devient un role bien rangé.
- **Réutiliser** : le même role s'applique dans plusieurs projets.
- **Partager** : un role est facile à donner à un collègue.

## Exemple simple

Sans role, ton playbook contient 20 tâches en vrac. Avec un role `common`, ton playbook devient :

```yaml
- name: Configuration de base
  hosts: all
  become: true
  roles:
    - common          # tout le contenu du role en une ligne
```

Limpide, non ?

## ❌ Erreur classique

> **Vouloir créer des roles trop tôt, pour tout.**

Un débutant qui découvre les roles veut tout transformer en role immédiatement. C'est prématuré. Le réflexe correct : crée un role **quand un playbook devient gros** ou **quand tu veux réutiliser** du code. Pas avant. Un petit playbook simple n'a pas besoin d'être un role.

## Exercices

### Guidé
Regarde tes playbooks actuels. Lequel est devenu **assez gros** pour justifier un role ? Lequel est encore **trop simple** pour ça ? Justifie.

### Autonome
Liste trois choses que tu refais **souvent** d'un playbook à l'autre (installer des paquets de base, créer un utilisateur admin, durcir SSH…). Ce sont de bons candidats pour un role réutilisable.

### Défi
Explique en quelques lignes la différence entre **réutiliser** un role et **copier-coller** des tâches. Pourquoi le role est-il une meilleure approche à long terme ?

## ✅ Tu sais maintenant…

- Pourquoi les **roles** existent : organiser et réutiliser le code.
- Qu'un role regroupe tâches, templates, variables et handlers.
- Qu'on appelle un role en **une ligne** dans un playbook.
- Qu'il ne faut créer des roles **ni trop tôt, ni pour tout**.

---

# Chapitre 11.2 — La structure d'un role

## Le minimum à savoir

Un role suit une **structure standard** de dossiers. Ansible sait où chercher chaque chose :

```
roles/
└── common/
    ├── tasks/main.yml          # les tâches du role (le cœur)
    ├── handlers/main.yml       # les handlers
    ├── templates/              # les templates Jinja2
    ├── files/                  # les fichiers à copier
    └── defaults/main.yml       # les variables par défaut
```

> **Les dossiers clés :**
> - **`tasks/main.yml`** : les tâches (obligatoire en pratique).
> - **`handlers/main.yml`** : les handlers.
> - **`templates/`** : les `.j2`.
> - **`files/`** : les fichiers pour `copy`.
> - **`defaults/main.yml`** : les variables par défaut (faciles à surcharger).

On crée cette structure automatiquement :

```bash
ansible-galaxy role init roles/common
```

*(`ansible-galaxy` sert ici juste à créer la structure — on n'utilise pas le côté « téléchargement de roles » dans ce cours.)*

## Très utile en pratique

Dans un role, tu n'écris plus les chemins complets : Ansible cherche **automatiquement** les templates dans `templates/`, les fichiers dans `files/`, etc. C'est l'avantage de la structure standard.

```yaml
# roles/common/tasks/main.yml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present
```

## Exemple simple

```yaml
# roles/common/tasks/main.yml
- name: Déposer le message du jour
  ansible.builtin.template:
    src: motd.j2            # cherché automatiquement dans roles/common/templates/
    dest: /etc/motd
```

## 🔀 À ne pas confondre

> **Un role n'est pas magique.** C'est juste tes tâches, templates et variables **rangés** dans des dossiers que Ansible connaît. Tu sais déjà écrire tout ce qu'il y a dedans — le role, c'est de **l'organisation**, pas une nouvelle compétence.

## ❌ Erreur classique

> **Se tromper de dossier ou de nom de fichier (`main.yml`).**

Les tâches vont dans `tasks/main.yml`, les handlers dans `handlers/main.yml` — avec ce **nom précis**. Une erreur de dossier ou de nom, et Ansible ne trouve rien. Le réflexe correct : utiliser `ansible-galaxy role init` pour créer la structure correcte, et respecter les noms `main.yml`.

## Exercices

### Guidé
Crée la structure d'un role avec `ansible-galaxy role init roles/common`. Explore les dossiers créés. Mets une tâche simple (installer un paquet) dans `roles/common/tasks/main.yml`.

### Autonome
Ajoute un template dans `roles/common/templates/` et une tâche dans `tasks/main.yml` qui l'utilise (sans chemin complet, juste le nom du fichier). Vérifie qu'Ansible le trouve automatiquement.

### Défi
Ajoute un handler dans `roles/common/handlers/main.yml` et notifie-le depuis une tâche du role. Vérifie que le mécanisme `notify` fonctionne **dans** le role comme dans un playbook normal.

## ✅ Tu sais maintenant…

- La **structure standard** d'un role (`tasks/`, `handlers/`, `templates/`, `files/`, `defaults/`).
- Créer un role avec **`ansible-galaxy role init`**.
- Qu'Ansible cherche **automatiquement** templates et fichiers dans les bons dossiers.
- Qu'un role, c'est de l'**organisation**, pas une nouvelle compétence.

---

# Chapitre 11.3 — Créer et utiliser un role simple

## Le minimum à savoir

Voici le cycle complet : transformer un playbook en role, puis l'utiliser.

**1. Le contenu du role** (`roles/common/tasks/main.yml`) :
```yaml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name:
      - htop
      - git
      - curl
    state: present

- name: Déposer le message du jour
  ansible.builtin.template:
    src: motd.j2
    dest: /etc/motd
```

**2. Le playbook qui appelle le role** (`playbooks/site.yml`) :
```yaml
- name: Configuration de base de toutes les machines
  hosts: all
  become: true
  roles:
    - common
```

**3. Lancer :**
```bash
ansible-playbook -i inventory.ini playbooks/site.yml
```

> Le playbook devient **court et clair** : il dit juste « applique le role `common` à toutes les machines ». Tout le détail est **rangé** dans le role.

## Très utile en pratique

Les **variables par défaut** du role vont dans `defaults/main.yml`. On peut les **surcharger** depuis le playbook ou les `group_vars`, ce qui rend le role **paramétrable** :

```yaml
# roles/common/defaults/main.yml
paquets_base:
  - htop
  - git
```

```yaml
# roles/common/tasks/main.yml
- name: Installer les paquets de base
  ansible.builtin.apt:
    name: "{{ paquets_base }}"
    state: present
```

## Exemple simple

```yaml
# playbooks/site.yml
- hosts: all
  become: true
  roles:
    - common
```

Trois lignes, et tout le role s'applique.

## ❌ Erreur classique

> **Mettre des valeurs en dur dans le role au lieu d'utiliser `defaults`.**

Un role avec des valeurs codées en dur n'est **pas réutilisable** : il fait toujours exactement la même chose. Le réflexe correct : mettre les valeurs configurables dans **`defaults/main.yml`** et les utiliser via `{{ }}`. Ainsi, le même role s'adapte à différents besoins.

## Exercices

### Guidé
Transforme ton playbook de configuration de base en role `common` : déplace les tâches dans `tasks/main.yml`, les templates dans `templates/`. Crée un playbook court qui appelle le role. Vérifie que tout fonctionne comme avant.

### Autonome
Mets la liste des paquets dans `defaults/main.yml` (variable `paquets_base`) et utilise-la dans le role via `{{ paquets_base }}`. Surcharge cette liste depuis un `group_vars` pour un groupe précis. Observe le résultat.

### Défi
Crée un second playbook (pour un autre groupe) qui réutilise le **même** role `common`. Tu prouves ainsi la **réutilisabilité** : un seul role, plusieurs usages. Explique l'économie de code réalisée.

## ✅ Tu sais maintenant…

- Transformer un playbook en **role** et l'appeler avec `roles:`.
- Que le playbook devient **court** (le détail est dans le role).
- Rendre un role **paramétrable** avec **`defaults/main.yml`**.
- **Réutiliser** un role dans plusieurs playbooks.

---

## 🚩 Checkpoint — Fin de la Partie 11

Tu sais créer et utiliser un role simple. Avant les mini-projets finaux, assure-toi de pouvoir :

- [ ] Expliquer **pourquoi** les roles existent (organiser, réutiliser).
- [ ] Connaître la **structure** d'un role (`tasks/`, `handlers/`, `templates/`, `files/`, `defaults/`).
- [ ] Créer un role avec **`ansible-galaxy role init`**.
- [ ] Appeler un role depuis un playbook (`roles:`) et le rendre paramétrable (`defaults`).

> **🧩 Mini-projet 12 — « Créer un role simple `common` ».**
> Crée un role `common` qui installe les paquets de base, dépose un `motd` par template, et applique une petite config commune. Rends-le paramétrable via `defaults`. Appelle-le depuis un playbook court qui vise toutes les machines. Vérifie l'idempotence.

> **La suite :** la Partie 12 regroupe **tous** les mini-projets en un parcours complet, pour consolider l'ensemble du cours.

---
---

# PARTIE 12 — MINI-PROJETS PRATIQUES (RÉCAPITULATIF)

> **Objectif de la partie :** consolider tous tes acquis. Les 12 mini-projets ci-dessous ont été **distribués** au fil des parties ; les voici **regroupés** comme un parcours complet, du lab nu au projet organisé avec roles. Reprends-les dans l'ordre pour un entraînement complet.

---

## Le parcours complet

| # | Mini-projet | Compétences | Partie |
|---|-------------|-------------|--------|
| 1 | **Mettre en place le lab Ansible** | VMs, SSH par clé, snapshots | 1 |
| 2 | **Créer un inventaire propre** | inventaire INI, groupes, variables | 2 |
| 3 | **Commandes ad hoc multi-machines** | `ping`, `command`, lecture des sorties | 2 |
| 4 | **Installer des paquets** (idempotence) | module `apt`, `changed` vs `ok` | 3 |
| 5 | **Déployer un service web simple** | playbook, `become`, `service` | 4 |
| 6 | **Copier un fichier sur plusieurs machines** | `copy`, permissions | 5 |
| 7 | **Créer un utilisateur sur plusieurs machines** | `user`, `group` | 5 |
| 8 | **Générer une configuration avec template** | `template`, Jinja2 | 7 |
| 9 | **Handler : redémarrer si nécessaire** | `notify`, handlers | 7 |
| 10 | **Chiffrer une variable avec Vault** | `ansible-vault`, `--ask-vault-pass` | 9 |
| 11 | **Organiser un mini-projet propre** | arborescence, `ansible.cfg`, Git | 10 |
| 12 | **Créer un role simple `common`** | roles, `defaults`, réutilisation | 11 |

---

## 🎯 Projet final intégrateur

Pour vraiment tout consolider, voici un **projet final** qui combine l'essentiel du cours :

**Objectif :** construire, à partir de ton lab, un projet Ansible **propre et complet** qui administre tes machines de bout en bout.

**Étapes :**
1. **Lab** : control + 2 cibles, SSH par clé, snapshots (mini-projet 1).
2. **Inventaire** : groupes `web`, variables de groupe, `ansible.cfg` (mini-projets 2 et 11).
3. **Role `common`** : paquets de base + `motd` par template + config commune (mini-projet 12).
4. **Playbook web** : installe nginx, déploie une page par template, gère le service avec un handler (mini-projets 5, 8, 9).
5. **Secret** : un mot de passe chiffré par Vault, utilisé dans un template (mini-projet 10).
6. **Organisation** : arborescence propre, README, Git avec `.gitignore` (mini-projet 11).
7. **Vérification** : tout en `--check --diff` d'abord, `--limit` sur une machine témoin, puis le groupe ; idempotence confirmée (deux passages → `ok`).

**Livrable :** un dépôt Git propre, documenté, idempotent, que tu pourrais montrer ou réutiliser.

> Ce projet final est ta **preuve de maîtrise** : il mobilise l'inventaire, les playbooks, les modules, les variables, les templates, les handlers, Vault, l'organisation et les roles. Si tu le réalises de bout en bout, tu sais administrer un parc Linux avec Ansible.

---
---

# ANNEXES

> Annexes courtes, pour référence rapide.

---

## Annexe A — Cheat-sheet des commandes

```bash
# --- Inventaire ---
ansible-inventory -i inventory.ini --graph        # voir l'inventaire en arbre
ansible-inventory -i inventory.ini --host cible1  # variables d'un hôte

# --- Commandes ad hoc ---
ansible all -i inventory.ini -m ansible.builtin.ping
ansible web -i inventory.ini -m ansible.builtin.command -a "uptime"
ansible web -i inventory.ini -m ansible.builtin.apt -a "name=htop state=present" --become

# --- Playbooks ---
ansible-playbook -i inventory.ini site.yml --syntax-check   # vérifier la syntaxe
ansible-playbook -i inventory.ini site.yml --check --diff   # simuler + voir les changements
ansible-playbook -i inventory.ini site.yml --limit cible1   # une seule machine
ansible-playbook -i inventory.ini site.yml                  # exécuter

# --- Vault ---
ansible-vault create secrets.yml                  # créer un fichier chiffré
ansible-vault edit secrets.yml                    # éditer
ansible-vault view secrets.yml                    # afficher
ansible-playbook -i inventory.ini site.yml --ask-vault-pass

# --- Roles ---
ansible-galaxy role init roles/common             # créer la structure d'un role
```

---

## Annexe B — Erreurs fréquentes

| Symptôme | Cause probable | Solution |
|----------|----------------|----------|
| `UNREACHABLE` | Problème SSH (clé, user, réseau) | Tester `ssh user@cible` à la main |
| `FAILED` + « Permission denied » | `become` manquant | Ajouter `become: true` |
| Toujours `changed` au 2e passage | Abus de `command`/`shell` | Utiliser un module dédié |
| Variable inattendue | Question de priorité | `ansible-inventory --host` |
| YAML refusé | Indentation (tabs/espaces) | `--syntax-check`, vérifier les espaces |
| « no vault secrets found » | Mot de passe Vault non fourni | Ajouter `--ask-vault-pass` |
| Tâche `skipped` | Condition `when` non remplie | Normal (pas une erreur) |

---

## Annexe C — Rappel YAML

```yaml
# Clé : valeur
nom: serveur1
actif: true

# Liste (tirets)
paquets:
  - nginx
  - git

# Dictionnaire imbriqué (indentation = hiérarchie)
serveur:
  nom: web1
  ip: 192.168.56.11
```

**Règles d'or :** indentation par **espaces** (jamais de tabs), **2 espaces** par niveau, cohérence dans tout le fichier. Une valeur commençant par `{{` se met **entre guillemets**.

---

## Annexe D — Rappel SSH

```bash
ssh-keygen -t ed25519               # générer une paire de clés (sur le contrôle)
ssh-copy-id utilisateur@cible       # déposer la clé publique sur une cible
ssh utilisateur@cible               # tester la connexion (doit être sans mot de passe)
ssh -v utilisateur@cible            # mode verbeux pour diagnostiquer
```

**Règle d'or :** SSH doit fonctionner **à la main** avant qu'Ansible ne fonctionne. Au moindre souci Ansible au début, teste `ssh` d'abord.

---

## Annexe E — Ansible vs Terraform / Docker / Kubernetes

| Outil | Rôle |
|-------|------|
| **Ansible** | **Configurer** des machines existantes |
| **Terraform** | **Provisionner / créer** l'infrastructure |
| **Docker** | **Packager** une application en conteneur |
| **Kubernetes** | **Orchestrer** des conteneurs |

Outils **complémentaires** : Terraform crée → Ansible configure → Docker/Kubernetes font tourner les apps. Ce cours reste centré sur **Ansible**.

---

## Annexe F — Roadmap après le cours

Une fois ce cours maîtrisé, tu peux explorer (dans l'ordre qui te convient) :

- **AWX / Ansible Automation Platform** : interface web, planification, logs centralisés.
- **Terraform** : créer l'infrastructure (complément d'Ansible).
- **CI/CD** : tester et déployer automatiquement tes playbooks.
- **Kubernetes** : orchestration de conteneurs.
- **Durcissement avancé** (hardening) : baselines de sécurité complètes.

Ces sujets dépassent le cadre de ce cours débutant, mais Ansible est une excellente base pour les aborder.

---

## 🎓 Mot de la fin

Tu es parti de zéro, et tu sais maintenant **automatiser l'administration de machines Linux** avec Ansible.

Tu as appris, pas à pas :

- à **comprendre** Ansible (l'état souhaité, l'idempotence) avant de l'utiliser ;
- à monter un **lab** et te connecter en **SSH par clé** ;
- à décrire ton parc avec un **inventaire** et à agir en **commandes ad hoc** ;
- à **lire les sorties** (`ok`, `changed`, `failed`, `skipped`, `unreachable`) ;
- à écrire des **playbooks** lisibles et rejouables ;
- à utiliser les **modules** essentiels (paquets, services, fichiers, utilisateurs) ;
- à rendre tes playbooks **adaptables** (variables, facts, conditions, boucles) ;
- à générer de la config avec **templates** et à redémarrer proprement avec **handlers** ;
- à protéger tes secrets avec **Vault** ;
- à **organiser** un projet et créer un **role** simple.

Garde en tête les réflexes qui font la différence : **comprendre l'état souhaité**, **lire les sorties**, **préférer les modules dédiés**, **vérifier avant d'agir** (`--check`, `--limit`), et **ne jamais laisser un secret en clair**.

La suite t'appartient : approfondis avec AWX, Terraform ou le durcissement, ou continue simplement à automatiser ton propre parc. Tu as maintenant le **socle**.

**Bon courage, et bonne automatisation. 🚀**

---
