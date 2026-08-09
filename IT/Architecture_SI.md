# Architecture des systèmes d'information
## Comprendre, lire et concevoir un système d'information

**Tranches T1 à T8 — Cours intégral, chapitres 1 à 50**
*Version 1.8 · 2 août 2026*

---

## Les huit principes de lecture

*Ces principes s'appliquent aux cinquante chapitres. Ils portent chacun un nom, employé dans tout le cours, et une référence courte pour la production éditoriale.*

| # | Nom du principe | Énoncé |
|---|---|---|
| **R1** | **Principe des trois flux** | Métier, dépendance, exploitation — et ne jamais les confondre |
| **R2** | **Principe de la contrainte** | La taille ne justifie jamais une brique · la contrainte, oui |
| **R3** | **Principe de coupe** | On descend dans un mécanisme jusqu'au niveau nécessaire à la décision |
| **R4** | **Principe du coût** | Ajouter n'est jamais gratuit : contrainte résolue **et** coût introduit |
| **R5** | **Principe du visuel** | Le schéma porte l'information, il ne l'accompagne pas |
| **R6** | **Principe du modèle** | Un modèle pédagogique n'est pas une loi technique |
| **R7** | **Principe d'hypothèse** | Une observation produit une hypothèse, pas une identification |
| **R8** | **Principe de preuve** | Un schéma révèle une intention de redondance · seul un test établit une capacité |

### principe des trois flux — Trois familles de flux, pas deux

| Famille | Définition | Exemples | Effet de sa rupture |
|---|---|---|---|
| **Flux métier** | Ce que le service transporte ou traite | Une page, un fichier, une requête, un enregistrement | Le service ne rend plus son objet |
| **Flux de dépendance** | Ce **sans quoi le service ne peut pas s'établir** | Résolution de noms · authentification · validation de certificat · synchronisation d'horloge · découverte de service | **Le service s'arrête, sans qu'on comprenne pourquoi** |
| **Flux d'exploitation** | Ce qui permet de tenir, observer et restaurer le service | Journaux, métriques, supervision, sauvegarde, administration | Le service continue · **on devient aveugle** |

⚠️ **La correction que cette règle apporte** : une version antérieure de cette structure rangeait la collecte de journaux avec la résolution de noms. C'est faux, et pédagogiquement dangereux : cela enseignerait qu'un service s'arrête quand la collecte tombe, alors qu'il continue — et que le vrai problème est ailleurs. **Tout ce qui n'est pas le contenu utile n'est pas un flux de dépendance.**

### R2 · Principe de la contrainte

> **La taille d'une organisation ne justifie jamais seule un composant. C'est la contrainte qui le justifie.**

Une organisation de douze mille personnes n'a aucun besoin de principe d'une infrastructure d'annuaire complexe. Quand elle en a une, c'est le résultat d'une acquisition, d'une exigence d'isolation ou d'une dette historique — jamais du nombre de salariés.

**Application** : les trois architectures de référence — Atelier Martin, HELIOMED, Novaris — sont toujours présentées avec **la contrainte** qui explique chaque écart, jamais avec la seule taille. La question posée à chaque composant est : *à partir de quelle contrainte devient-il nécessaire ?*

### R3 · Principe de coupe

> **On descend dans le fonctionnement interne d'un mécanisme uniquement jusqu'au niveau nécessaire pour comprendre une décision d'architecture.**

**Le test, appliqué à la résolution de noms** :

| Dans le périmètre | Hors périmètre |
|---|---|
| Client → résolution → adresse → connexion | Le format des messages du protocole |
| Récursif et faisant autorité | Les algorithmes de sélection de serveur |
| Cache, et ce qu'il masque | La configuration d'un logiciel de résolution |
| Redondance, et ce qui tombe sans elle | Les enregistrements exotiques |
| Vue interne et vue externe distinctes | La signature cryptographique des zones, sauf effet architectural |

**La même coupe s'applique partout** : annuaire, certificats, routage, répartition de charge, stockage, orchestration.

### R4 · Principe du coût

> **Avant d'ajouter un composant, être capable d'énoncer la contrainte qu'il résout **et** le coût qu'il introduit.**

C'est la conséquence directe du principe 1. Elle devient le **principe 9** de la doctrine, et elle est appliquée à chaque chapitre de la Partie II sous la forme d'une rubrique obligatoire :

| Composant | Contrainte résolue | **Coût introduit** |
|---|---|---|
| Répartiteur de charge | Continuité malgré la panne d'un membre | Un composant de plus à exploiter, à corriger, à surveiller · un point de rupture nouveau s'il n'est pas redondé |
| Infrastructure de clés interne | Maîtrise des certificats internes | Une hiérarchie à maintenir, des expirations à suivre, une révocation à faire fonctionner |
| Segmentation supplémentaire | Limitation de la propagation | Des flux à ouvrir, à documenter, à maintenir · un dépannage plus difficile |
| Second site | Continuité en cas de sinistre | Un basculement à tester régulièrement, sans quoi il ne fonctionnera pas |
| Orchestration de conteneurs | Densité, reproductibilité, mise à l'échelle | **Un système distribué complet à exploiter** |

⚠️ **Le réflexe que cette règle combat** : construire une architecture en collectionnant des briques. *Ajouter n'est jamais gratuit.*

### R6 · Principe du modèle

Ce cours emploie des **modèles simplifiés** pour rendre les mécanismes lisibles. Un modèle est un outil de raisonnement, pas une description exhaustive du réel.

> **Chaque fois qu'une règle est énoncée sous une forme absolue — toujours, jamais, sans exception — elle est un raccourci pédagogique et doit être signalée comme tel.**

**Les trois formulations à employer** :

| Au lieu de | Écrire |
|---|---|
| « X se passe toujours ainsi » | « Dans le modèle employé ici, X se passe ainsi » |
| « Y ne peut jamais » | « Y suppose généralement, et le contourner exige de … » |
| « Z est le plus … » | « Z est une cause fréquente de … » — sauf si c'est une doctrine assumée |

⚠️ **Pourquoi cette règle est critique dans ce volume précisément** : l'architecture est le domaine où les exceptions sont la norme. Un lecteur qui apprend une fausse loi la transportera dans tous les volumes suivants — et il la défendra en réunion.

**Les formulations fortes sont conservées quand elles expriment une doctrine** — *toute architecture est un compromis*, *ajouter n'est jamais gratuit*. Elles sont supprimées quand elles prétendent établir un classement factuel sans données.

### R7 · Principe d'hypothèse

Cohérente avec les volumes Renseignement et Asset Management de la collection.

> **Lire un schéma produit des hypothèses à confirmer, jamais des identifications certaines.**

**Application aux exercices** : la consigne n'est jamais *« identifiez ce composant »* mais **« proposez le rôle le plus probable, et indiquez ce qu'il faudrait vérifier »**. Un port ouvert, une position, un ensemble de connexions constituent un faisceau — pas une preuve.

### R8 · Principe de preuve

> **Un schéma permet d'identifier une *intention* de redondance. Seul un test permet d'établir une *capacité* de basculement.**

**Ce que deux composants dessinés côte à côte peuvent partager sans que rien ne le montre** : une alimentation · un hôte de virtualisation · un stockage · un site · un segment réseau · une dépendance commune à un service tiers.

**Application** : chaque fois que ce cours conclut à une redondance, il précise **ce qu'il faudrait vérifier** pour que la conclusion tienne.

### R5 · Principe du visuel

Les 115 000 mots annoncés étaient une **estimation, pas une cible**. Ce volume est le plus graphique de la collection.

> **Le schéma peut remplacer le texte. Il n'a pas à l'accompagner.**

Certaines explications de topologie doivent tendre vers 30 % de texte et 70 % de représentation. Si quatre-vingt-cinq mille mots et cent bons schémas enseignent mieux que cent vingt mille mots et soixante schémas, c'est le premier qu'il faut produire.

---

## Table des matières

- [Comprendre, lire et concevoir un système d'information](#comprendre-lire-et-concevoir-un-système-dinformation)
- [Les huit principes de lecture](#les-huit-principes-de-lecture)
  - [principe des trois flux — Trois familles de flux, pas deux](#principe-des-trois-flux--trois-familles-de-flux-pas-deux)
  - [R2 · Principe de la contrainte](#r2-·-principe-de-la-contrainte)
  - [R3 · Principe de coupe](#r3-·-principe-de-coupe)
  - [R4 · Principe du coût](#r4-·-principe-du-coût)
  - [R6 · Principe du modèle](#r6-·-principe-du-modèle)
  - [R7 · Principe d'hypothèse](#r7-·-principe-dhypothèse)
  - [R8 · Principe de preuve](#r8-·-principe-de-preuve)
  - [R5 · Principe du visuel](#r5-·-principe-du-visuel)
  - [Les trois niveaux de lecture](#les-trois-niveaux-de-lecture)
  - [Comment lire les blocs de ce cours](#comment-lire-les-blocs-de-ce-cours)
- [PARTIE I — Lire un système d'information](#partie-i--lire-un-système-dinformation)
  - [Chapitre 1 — Pourquoi un système d'information ressemble à ça](#chapitre-1--pourquoi-un-système-dinformation-ressemble-à-ça)
  - [Chapitre 2 — Le vocabulaire](#chapitre-2--le-vocabulaire)
  - [Chapitre 3 — Comment lire un schéma](#chapitre-3--comment-lire-un-schéma)
  - [Chapitre 4 — La sédimentation](#chapitre-4--la-sédimentation)
  - [Chapitre 5 — Les grandes zones](#chapitre-5--les-grandes-zones)
  - [Chapitre 6 — Le poste utilisateur](#chapitre-6--le-poste-utilisateur)
  - [Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur](#chapitre-7--ce-que-fait-un-architecte-ce-que-fait-un-lecteur)
- [Registre de cohérence — fin de T1 (chapitres 1 à 7)](#registre-de-cohérence--fin-de-t1-chapitres-1-à-7)
  - [Règles verrouillées, et leur application](#règles-verrouillées-et-leur-application)
  - [Termes arrêtés](#termes-arrêtés)
  - [Renvois émis vers des chapitres non rédigés](#renvois-émis-vers-des-chapitres-non-rédigés)
  - [État du fil rouge](#état-du-fil-rouge)
  - [Écarts au plan validé](#écarts-au-plan-validé)
- [PARTIE II — Les composants d'infrastructure](#partie-ii--les-composants-dinfrastructure)
- [Préambule — Le socle réseau minimal](#préambule--le-socle-réseau-minimal)
  - [P.1 Deux niveaux d'adressage, et pourquoi il en faut deux](#p1-deux-niveaux-dadressage-et-pourquoi-il-en-faut-deux)
  - [P.2 Adresse, sous-réseau, passerelle](#p2-adresse-sous-réseau-passerelle)
  - [P.3 Ports et état d'une connexion](#p3-ports-et-état-dune-connexion)
  - [P.4 Traduction d'adresses](#p4-traduction-dadresses)
  - [P.5 Deux familles d'adressage](#p5-deux-familles-dadressage)
  - [P.6 Ce que ce préambule permet de faire](#p6-ce-que-ce-préambule-permet-de-faire)
  - [Chapitre 8 — Le commutateur](#chapitre-8--le-commutateur)
  - [Chapitre 9 — Le routeur](#chapitre-9--le-routeur)
  - [Chapitre 10 — Le pare-feu](#chapitre-10--le-pare-feu)
  - [Chapitre 11 — Le mandataire sortant](#chapitre-11--le-mandataire-sortant)
  - [Chapitre 12 — Le mandataire inverse](#chapitre-12--le-mandataire-inverse)
  - [Chapitre 13 — Le répartiteur de charge](#chapitre-13--le-répartiteur-de-charge)
  - [Chapitre 14 — La résolution de noms](#chapitre-14--la-résolution-de-noms)
  - [Chapitre 15 — L'attribution d'adresses](#chapitre-15--lattribution-dadresses)
  - [Chapitre 16 — L'annuaire](#chapitre-16--lannuaire)
  - [Chapitre 17 — L'infrastructure de clés](#chapitre-17--linfrastructure-de-clés)
- [PARTIE III — Les serveurs et l'exécution](#partie-iii--les-serveurs-et-lexécution)
  - [Chapitre 18 — Le serveur web](#chapitre-18--le-serveur-web)
  - [Chapitre 19 — Le serveur applicatif](#chapitre-19--le-serveur-applicatif)
  - [Chapitre 20 — La base de données](#chapitre-20--la-base-de-données)
  - [Chapitre 21 — Le serveur de fichiers](#chapitre-21--le-serveur-de-fichiers)
  - [Chapitre 22 — La messagerie](#chapitre-22--la-messagerie)
  - [Chapitre 23 — La virtualisation](#chapitre-23--la-virtualisation)
- [PARTIE IV — Les réseaux et les zones](#partie-iv--les-réseaux-et-les-zones)
  - [Chapitre 24 — Le réseau local et la segmentation](#chapitre-24--le-réseau-local-et-la-segmentation)
  - [Chapitre 25 — La zone démilitarisée](#chapitre-25--la-zone-démilitarisée)
  - [Chapitre 26 — Le réseau étendu et les sites distants](#chapitre-26--le-réseau-étendu-et-les-sites-distants)
  - [Chapitre 27 — Le réseau d'administration](#chapitre-27--le-réseau-dadministration)
  - [Chapitre 28 — Le réseau industriel](#chapitre-28--le-réseau-industriel)
- [PARTIE V — Les flux](#partie-v--les-flux)
  - [Chapitre 29 — Suivre une requête](#chapitre-29--suivre-une-requête)
  - [Chapitre 30 — Suivre une authentification](#chapitre-30--suivre-une-authentification)
  - [Chapitre 31 — Suivre une session](#chapitre-31--suivre-une-session)
  - [Chapitre 32 — Suivre une donnée](#chapitre-32--suivre-une-donnée)
  - [Chapitre 33 — Suivre un secret](#chapitre-33--suivre-un-secret)
  - [Chapitre 34 — Suivre un journal](#chapitre-34--suivre-un-journal)
  - [Chapitre 35 — Du serveur au service](#chapitre-35--du-serveur-au-service)
- [PARTIE VI — Lire une architecture](#partie-vi--lire-une-architecture)
  - [Chapitre 36 — La grille de lecture en sept passes](#chapitre-36--la-grille-de-lecture-en-sept-passes)
  - [Chapitre 37 — Dix architectures](#chapitre-37--dix-architectures)
  - [Chapitre 38 — Les tiers sur un schéma](#chapitre-38--les-tiers-sur-un-schéma)
- [PARTIE VII — Les architectures modernes](#partie-vii--les-architectures-modernes)
  - [Chapitre 39 — Le cloud](#chapitre-39--le-cloud)
  - [Chapitre 40 — L'hybride](#chapitre-40--lhybride)
  - [Chapitre 41 — Conteneurs et orchestration](#chapitre-41--conteneurs-et-orchestration)
  - [Chapitre 42 — Microservices, fonctions et services en ligne](#chapitre-42--microservices-fonctions-et-services-en-ligne)
- [PARTIE VIII — La vue cybersécurité](#partie-viii--la-vue-cybersécurité)
  - [Chapitre 43 — Où peut-on agir ?](#chapitre-43--où-peut-on-agir-)
  - [Chapitre 44 — Placer les dispositifs](#chapitre-44--placer-les-dispositifs)
  - [Chapitre 45 — Ce que l'architecture impose au reste](#chapitre-45--ce-que-larchitecture-impose-au-reste)
- [PARTIE IX — Concevoir](#partie-ix--concevoir)
  - [Chapitre 46 — Les quatre questions du concepteur](#chapitre-46--les-quatre-questions-du-concepteur)
  - [Chapitre 47 — Concevoir sous contrainte](#chapitre-47--concevoir-sous-contrainte)
  - [Chapitre 48 — Quatre conceptions guidées](#chapitre-48--quatre-conceptions-guidées)
  - [Chapitre 49 — Critiquer une architecture](#chapitre-49--critiquer-une-architecture)
  - [Chapitre 50 — Ce qu'un schéma ne dira jamais](#chapitre-50--ce-quun-schéma-ne-dira-jamais)
- [Cas de synthèse](#cas-de-synthèse)
  - [Cas A — Le schéma qu'on vous donne le premier jour](#cas-a--le-schéma-quon-vous-donne-le-premier-jour)
  - [Cas B — Le service qui tombe](#cas-b--le-service-qui-tombe)
  - [Cas C — Concevoir sous contrainte réelle](#cas-c--concevoir-sous-contrainte-réelle)
- [ANNEXES](#annexes)
  - [Plan d'accès](#plan-daccès)
- [Annexe A — Glossaire](#annexe-a--glossaire)
- [Annexe B — Fiches composants](#annexe-b--fiches-composants)
- [Annexe B bis — Index des notions à reconnaître](#annexe-b-bis--index-des-notions-à-reconnaître)
- [Annexe C — La grille en sept passes](#annexe-c--la-grille-en-sept-passes)
- [Annexe D — Conventions de schéma](#annexe-d--conventions-de-schéma)
- [Annexe E — Catalogue des schémas](#annexe-e--catalogue-des-schémas)
- [Annexe F — Les dix architectures](#annexe-f--les-dix-architectures)
- [Annexe G — Pièges de lecture](#annexe-g--pièges-de-lecture)
- [Annexe H — Ce qui n'est jamais dessiné](#annexe-h--ce-qui-nest-jamais-dessiné)
- [Annexe I — Les cinq actions et leurs emplacements](#annexe-i--les-cinq-actions-et-leurs-emplacements)
- [Annexe J — Grille de conception et registre des compromis](#annexe-j--grille-de-conception-et-registre-des-compromis)
  - [J.1 Fiche de contraintes](#j1-fiche-de-contraintes)
  - [J.2 Registre des compromis](#j2-registre-des-compromis)
  - [J.3 Ce qui reste à vérifier](#j3-ce-qui-reste-à-vérifier)
  - [J.4 Grille de critique en six points](#j4-grille-de-critique-en-six-points)
- [Annexe K — Raccordement aux autres volumes](#annexe-k--raccordement-aux-autres-volumes)
- [Annexe L — Checklists](#annexe-l--checklists)
  - [L.1 — Devant un schéma inconnu](#l1--devant-un-schéma-inconnu)
  - [L.5 — Avant de conclure à un point de rupture](#l5--avant-de-conclure-à-un-point-de-rupture)
  - [L.2 — Avant de croire à une sauvegarde](#l2--avant-de-croire-à-une-sauvegarde)
  - [L.3 — Avant de croire à une séparation sans fil](#l3--avant-de-croire-à-une-séparation-sans-fil)
  - [L.4 — Avant de croire à un découplage asynchrone](#l4--avant-de-croire-à-un-découplage-asynchrone)
  - [L.6 — Avant d'affirmer le rôle d'un composant](#l6--avant-daffirmer-le-rôle-dun-composant)
  - [L.7 — Avant de critiquer](#l7--avant-de-critiquer)
  - [L.8 — Avant de concevoir](#l8--avant-de-concevoir)
  - [L.9 — Avant de livrer une conception](#l9--avant-de-livrer-une-conception)
  - [L.10 — Avant de placer un dispositif](#l10--avant-de-placer-un-dispositif)
- [Journal des modifications](#journal-des-modifications)

---

### Les trois niveaux de lecture

**Ce cours distingue trois statuts, et il ne faut pas les confondre.** Vingt-cinq acronymes mémorisés au même niveau ne servent à rien ; trois catégories bien tenues changent une carrière.

| Niveau | Ce qu'on attend de vous | Exemples |
|---|---|---|
| 🧠 **À MAÎTRISER** | **Savoir raisonner avec.** C'est le corps du cours : vous devez pouvoir expliquer le rôle, les dépendances, l'effet d'une panne et les compromis | Résolution de noms · routage · pare-feu · segmentation · identité · certificats · flux · virtualisation · stockage |
| 🔭 **À RECONNAÎTRE** | **Savoir ce que ça signifie quand ça apparaît** sur un schéma ou dans une réunion — et quelle question poser. Pas configurer, pas concevoir | BGP · MPLS · SD-WAN · VXLAN · HSM · NAC · hyperconvergence · maillage de services |
| 📚 **À APPROFONDIR** | **Savoir que ça existe et où chercher.** Leur maîtrise relève d'une formation dédiée | Configuration des protocoles de routage · administration d'un réseau de stockage · conception d'un système distribué |

⚠️ **Le contrat pédagogique du niveau 🔭 est explicite** : *vous n'avez pas besoin de savoir configurer ces technologies pour ce cours. Vous devez en revanche comprendre ce qu'elles impliquent lorsqu'elles apparaissent.*

**Chaque bloc 🔭 répond à six questions, et à six seulement** :

```
   ①  Qu'est-ce que c'est ?
   ②  Quel problème cela résout-il ?
   ③  Où le rencontre-t-on dans un SI ?
   ④  Qu'est-ce que cela change dans les flux et les dépendances ?
   ⑤  Quel nouveau coût ou risque cela introduit-il ?
   ⑥  Que demander si je le vois sur un schéma ou l'entends en réunion ?
```

---

### Comment lire les blocs de ce cours

| Bloc | Signification |
|---|---|
| 🖼 **SCHÉMA** | Représentation. **Elle porte l'information, elle ne l'illustre pas** |
| ❓ **QUE VOYEZ-VOUS ?** | Questions posées **avant** l'explication. Cherchez avant de lire |
| 👁 **CE QU'IL FALLAIT OBSERVER** | Ce qui distingue un œil exercé d'un débutant |
| 🔴 **FIL ROUGE** | Un fragment du schéma d'HELIOMED s'éclaire |
| 🏭 **TROIS TAILLES** | Le même composant chez Atelier Martin, HELIOMED et Novaris |
| ⚖️ **CONTRAINTE ET COÛT** | Ce que le composant résout, ce qu'il coûte — *principe du coût* |
| 🔥 **SCÉNARIO** | Une panne réelle : symptôme · hypothèse naïve · dépendance réelle · ce que le schéma aurait dû montrer |
| 🗣 **VOCABULAIRE DE RÉUNION** | Ce que vous entendrez · ce que la personne veut dire · **ce qu'il faut vérifier avant de le croire** |
| 🔭 **À RECONNAÎTRE** | Une technologie que vous rencontrerez sans avoir à la maîtriser · six questions |
| 🔬 **MINI-LAB** | Exercice sur schéma, avec corrigé commenté |
| 🎯 **QUELLE ERREUR ÇA ÉVITE ?** | Une situation · la mauvaise décision · ce qui l'aurait évitée |
| 👁 **CE QU'IL FALLAIT OBSERVER** | Ce qui distingue un œil exercé d'un débutant |
| 🏭 **TROIS TAILLES** | Le même composant chez Atelier Martin, HELIOMED et Novaris |
| ⚖️ **CONTRAINTE ET COÛT** | Ce que le composant résout · ce qu'il coûte — *principe du coût* |
| ⚠️ **PIÈGE** | Erreur de lecture fréquente |
| 📌 **LIMITES** | Ce que le schéma ne dit pas |

---

## PARTIE I — Lire un système d'information

Cette partie ne vous apprendra aucun composant. Elle installe **un regard** : quatre questions, six contraintes, trois familles de flux, et l'idée que tout ce que vous verrez est le produit d'arbitrages faits par d'autres, à des époques différentes.

À la fin, vous ne saurez pas encore lire le schéma du chapitre 1. Vous saurez **quoi y chercher**.

---

### Chapitre 1 — Pourquoi un système d'information ressemble à ça

#### 1.1 Le schéma que vous ne comprenez pas encore

Voici le système d'information du groupe HELIOMED, en décembre 2025. C'est le schéma que le cours va éclairer, fragment par fragment.

🖼 **SCHÉMA 1.1 — HELIOMED, vue d'ensemble** · *Version graphique à produire : quatre bandes horizontales colorées par zone, composants iconographiés, flux principaux en trait plein, flux de dépendance en pointillé.*

```
                            I N T E R N E T
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
              [ pare-feu ]                  [ pare-feu ]
                    └──────────────┬──────────────┘
                                   │
   ╔═══════════════════════════════╪═══════════════════════════════╗
   ║  ZONE DÉMILITARISÉE           │                               ║
   ║                    ┌──────────┴──────────┐                    ║
   ║              [ mandataire inverse ]  [ relais messagerie ]     ║
   ║                          │                                    ║
   ║              [ répartiteur de charge ]                        ║
   ╚══════════════════════════╪════════════════════════════════════╝
                              │
   ╔══════════════════════════╪════════════════════════════════════╗
   ║  RÉSEAU INTERNE          │                                    ║
   ║              ┌───────────┴───────────┐                        ║
   ║        [ web 1 ]  [ web 2 ]  [ web 3 ]                        ║
   ║              └───────────┬───────────┘                        ║
   ║                    [ applicatif ]                             ║
   ║                          │                                    ║
   ║                  [ base de données ]                          ║
   ║                                                               ║
   ║   [ annuaire ]   [ fichiers ]   [ sauvegarde ]   [ postes ]   ║
   ╚═══════════════════════════════════════════════════════════════╝
                              │
   ╔══════════════════════════╪════════════════════════════════════╗
   ║  SITE INDUSTRIEL — Saint-Étienne                              ║
   ║        [ supervision ]  ──  [ automates ]                     ║
   ╚═══════════════════════════════════════════════════════════════╝
```

❓ **QUE VOYEZ-VOUS ?**

Ne cherchez pas à comprendre. Répondez seulement à ceci, et notez vos réponses :

1. Combien de zones distinguez-vous ?
2. Par où arrive un utilisateur venu d'Internet ?
3. Où sont les données ?
4. Qu'est-ce qui, sur ce schéma, peut tomber sans que le service s'arrête ?
5. **Qu'est-ce qui manque ?**

**La cinquième question est la plus importante du cours**, et vous ne pouvez pas encore y répondre. À la fin du chapitre 50, vous saurez qu'il manque au moins onze choses sur ce schéma — dont la résolution de noms, la synchronisation d'horloge, les chemins d'administration, et l'ensemble des services en ligne utilisés par les métiers.

👁 **CE QU'IL FALLAIT OBSERVER, dès maintenant**

| Observation | Ce qu'elle indique |
|---|---|
| Deux pare-feu côte à côte | Une redondance : l'un peut tomber |
| Trois serveurs web, un seul applicatif | La redondance s'arrête à mi-parcours — **c'est un choix, pas un oubli** |
| Une seule base de données | Le point de rupture le plus probable du schéma |
| Le site industriel n'a qu'un lien | Il est relié, mais peu |
| L'annuaire est dessiné, sans aucun trait | **Personne ne s'y connecte, sur ce schéma. C'est faux, et c'est normal** |

**La dernière ligne contient déjà tout le cours.** L'annuaire est utilisé par presque tout ce qui figure sur ce schéma, et aucun trait ne le montre. Ce n'est pas une erreur du dessinateur : c'est une convention. Les schémas ne dessinent pas les flux de dépendance — c'est la règle principe des trois flux, et c'est le chapitre 30.

#### 1.2 Ce que ce cours n'est pas

Quatre disciplines voisines sont régulièrement confondues avec celle-ci. Autant le dire en dix lignes.

| Ce n'est pas… | Qui s'en occupe | Ce que ce cours en retient |
|---|---|---|
| **L'architecture d'entreprise** | Urbanistes, référentiels de cadrage | Rien. Ce cours ne produit ni cartographie d'entreprise, ni référentiel de transformation |
| **Le fonctionnement des composants** | Formations produit, documentation éditeur | Uniquement ce qui éclaire une décision — *principe de coupe* |
| **L'administration système et réseau** | Exploitation | Aucune commande, aucune configuration |
| **L'ingénierie et le dimensionnement** | Architectes techniques, ingénieurs | Le raisonnement, pas les calculs |

**Ce que ce cours enseigne, et qu'aucune des quatre ne fait** :

> **Pourquoi les choses sont agencées ainsi, ce que chaque agencement résout, ce qu'il coûte — et comment raisonner un agencement nouveau.**

⚠️ **La confusion à éviter dès maintenant.** Un cours *« comment fonctionne un système d'information »* expliquerait le détail d'un protocole de résolution de noms. Celui-ci explique **pourquoi la résolution de noms est le point de rupture le plus spectaculaire d'une architecture**. Ce n'est pas le même objet, et ce n'est pas le même métier.

#### 1.3 Les quatre questions du lecteur

Le modèle de poche du cours. Devant n'importe quel schéma, quatre questions — et l'ordre compte.

🖼 **SCHÉMA 1.2 — Les quatre questions** · *Quatre bandeaux, le quatrième distinct : il ne décrit pas le système, il décrit ce qu'on peut y faire.*

```
   ┌───────────────────────────────────────────────────┐
   │  ①  QU'EST-CE QUI CIRCULE ?                       │
   │      métier · dépendance · exploitation           │
   ├───────────────────────────────────────────────────┤
   │  ②  PAR OÙ ?                                      │
   │      le chemin, dans l'ordre, sans en sauter      │
   ├───────────────────────────────────────────────────┤
   │  ③  QU'EST-CE QUI S'ARRÊTE SI ÇA TOMBE ?          │
   │      ruptures · redondances · dégradations        │
   ├═══════════════════════════════════════════════════┤
   │  ④  OÙ PEUT-ON AGIR ?                             │
   │      observer · filtrer · authentifier            │
   │      · segmenter · journaliser                    │
   └───────────────────────────────────────────────────┘
```

| Question | Ce qu'elle permet | Chapitres |
|---|---|---|
| ① Qu'est-ce qui circule ? | Distinguer trois familles de flux, dont deux invisibles | 3, 29-35 |
| ② Par où ? | Reconstituer un chemin complet, y compris ce qui n'est pas dessiné | 29-35 |
| ③ Qu'est-ce qui s'arrête ? | Identifier les points de rupture réels, pas les composants qui font peur | 35 |
| ④ **Où peut-on agir ?** | **Le raccordement à toute la collection** | 43-45 |

**La quatrième est la porte de sortie du cours.** Elle ne décrit pas le système : elle décrit ce qu'on peut en faire — et elle est déterminée par des décisions prises avant vous, souvent des années avant.

🧪 **EN PRATIQUE — le test des quatre questions**

Prenez le schéma d'architecture de votre organisation. Posez les quatre questions. Comptez les réponses obtenues sans appeler personne.

| Réponses sur 4 | Ce que cela dit |
|---|---|
| 4 | Vous lisez déjà une architecture |
| 2 à 3 | Vous reconnaissez les composants, pas les flux |
| 0 à 1 | Vous regardez un dessin |

**La question ① est celle qui échoue le plus souvent**, y compris chez des professionnels expérimentés — parce que personne n'enseigne que trois choses différentes circulent.

#### 1.4 Les six contraintes qui produisent toute architecture

**Le principe fondateur du cours** :

> ### Toute architecture est un compromis.

Elle n'a pas été conçue : elle a été **négociée**, entre six contraintes qui se contredisent deux à deux.

| Contrainte | Ce qu'elle demande | Avec quoi elle entre en conflit |
|---|---|---|
| **Disponibilité** | Que le service tienne malgré les pannes | Le **coût** — chaque redondance double quelque chose |
| **Performance** | Que ce soit rapide | La **sécurité** — chaque contrôle ajoute un temps |
| **Coût** | Que ce soit finançable | **Tout le reste** |
| **Sécurité** | Que ce soit cloisonné, contrôlé, tracé | La **performance** et la **simplicité d'exploitation** |
| **Conformité** | Que ce soit démontrable et conforme aux règles | Le **coût** et le **délai** |
| **Histoire** | Que ce qui existe continue de fonctionner | **Tout le reste** |

⚠️ **La sixième est celle qu'on oublie, et c'est souvent la plus puissante.** Une architecture doit composer avec ce qui est déjà là : un progiciel qui exige une version ancienne, une base qu'on ne peut pas migrer, un site racheté avec son propre annuaire. Le chapitre 4 lui est consacré.

##### Ce que la contradiction produit concrètement

🖼 **SCHÉMA 1.3 — Trois arbitrages, trois architectures différentes** · *Trois variantes du même besoin, avec le curseur déplacé.*

```
  BESOIN : publier une application interne pour 200 salariés nomades

  ARBITRAGE A — coût prioritaire
  Internet ──► [ pare-feu ] ──► [ serveur applicatif ]
  → simple · peu cher · une panne = service arrêté · exposition directe

  ARBITRAGE B — disponibilité prioritaire
  Internet ──► [ pare-feu ×2 ] ──► [ répartiteur ×2 ] ──► [ serveurs ×3 ]
  → tient aux pannes · trois fois plus de composants à exploiter

  ARBITRAGE C — sécurité prioritaire
  Internet ──► [ pare-feu ] ──► [ mandataire inverse ] ──► [ authentification ]
            ──► [ serveur applicatif ]  (aucune exposition directe)
  → contrôlé · un composant de plus · une latence · une dépendance forte
    à l'authentification
```

**Aucun des trois n'est meilleur.** Ils répondent à trois arbitrages différents, et chacun serait une erreur dans le contexte des deux autres.

**Ce que le lecteur doit savoir faire à la fin du cours** : regarder une architecture réelle et **reconstituer l'arbitrage** qui l'a produite. C'est la définition de *raisonner*.

#### 1.5 Les trois familles de flux

Première présentation ; le chapitre 3 la développe et la Partie V l'exploite.

| Famille | Question | Sur les schémas |
|---|---|---|
| **Flux métier** | Qu'est-ce que le service transporte ou traite ? | **Dessiné** |
| **Flux de dépendance** | Sans quoi le service ne peut pas s'établir ? | **Rarement dessiné** |
| **Flux d'exploitation** | Ce qui permet de tenir, observer, restaurer | **Presque jamais dessiné** |

**L'exemple qui installe la distinction** — un salarié ouvre une application interne :

```
  FLUX MÉTIER          poste ──► mandataire ──► web ──► applicatif ──► base
                       (le chemin dessiné)

  FLUX DE DÉPENDANCE   poste ──► résolution de noms      ← sans elle : rien
                       poste ──► annuaire                ← sans lui : pas d'accès
                       poste ──► validation certificat   ← sans elle : avertissement
                       serveurs ──► serveur de temps     ← sans lui : rejets

  FLUX D'EXPLOITATION  serveurs ──► collecte de journaux ← sans elle : on est aveugle
                       serveurs ──► supervision          ← sans elle : on ne sait pas
                       serveurs ──► sauvegarde           ← sans elle : pas de reprise
```

**Trois observations essentielles.**

**Les flux de dépendance ne sont presque jamais sur le schéma**, et pourtant leur rupture **arrête le service**. C'est l'explication structurelle du *« tout est vert et pourtant ça ne marche pas »*.

**Les flux d'exploitation ne conditionnent pas le service.** Si la collecte de journaux tombe, l'application continue de fonctionner — vous devenez aveugle, ce qui est grave autrement. **Ne pas confondre les deux est une compétence.**

**Les trois empruntent des chemins différents**, traversent des zones différentes, et échouent pour des raisons différentes.

⚠️ **PIÈGE — l'erreur de catégorie**
Ranger la sauvegarde ou la journalisation parmi les dépendances conduit à surdimensionner ce qui n'a pas besoin de l'être, et à sous-estimer ce qui compte vraiment. Le test tient en une question : **si ce flux s'arrête, le service continue-t-il de rendre son objet ?** Si oui, c'est de l'exploitation.

#### 1.6 Les trois architectures de référence

Trois organisations accompagneront tout le cours, à côté d'HELIOMED. Elles servent une seule chose : montrer **à partir de quelle contrainte un composant apparaît**.

| | **ATELIER MARTIN** | **HELIOMED** | **GROUPE NOVARIS** |
|---|---|---|---|
| Effectif | 40 | 1 380 | 12 000 |
| Sites | 1 | 3 | 40, 6 pays |
| Informatique | 1 personne à mi-temps | 14 personnes | 180 personnes |
| Activité | Menuiserie industrielle | Dispositifs médicaux connectés | Distribution |

⚠️ **Le principe de la contrainte s'applique à chaque comparaison** :

> **La taille ne justifie jamais seule une brique d'architecture. C'est la contrainte qui la justifie.**

**Ce que cela interdit d'écrire**, et ce qui sera systématiquement reformulé :

| Formulation interdite | Formulation retenue |
|---|---|
| « Une organisation de 12 000 personnes a plusieurs forêts d'annuaire » | « Novaris a plusieurs forêts **parce qu'elle a absorbé quatre sociétés en huit ans et n'a jamais fusionné les annuaires** » |
| « Une PME n'a pas de zone démilitarisée » | « Atelier Martin n'en a pas **parce qu'elle ne publie aucun service : la contrainte n'existe pas** » |
| « À partir de 1 000 salariés, il faut une infrastructure de clés interne » | « HELIOMED en a une **parce qu'elle doit émettre des certificats pour des équipements médicaux qu'aucune autorité publique ne signera** » |

**La question posée à chaque composant, dans les cinquante chapitres** :

> ### À partir de quelle contrainte ce composant devient-il nécessaire ?

#### 1.7 La doctrine — neuf principes

> **1. Toute architecture est un compromis.** Elle n'a pas été conçue, elle a été négociée.

> **2. Aucune architecture n'a été construite d'un bloc.** Le legacy est l'état normal.

> **3. Un composant s'explique par ce qui se passe s'il disparaît.**

> **4. Le service compte, pas le serveur.**

> **5. Suivre un flux vaut mieux que lire une boîte.**

> **6. Le système d'information n'existe que pour traiter de la donnée.**

> **7. Concevoir, c'est choisir ce qu'on accepte de perdre.**

> **8. La taille ne justifie jamais une brique. La contrainte, oui.**

> **9. Ajouter n'est jamais gratuit.** Avant d'ajouter un composant, savoir énoncer la contrainte qu'il résout **et** le coût qu'il introduit.

> **10. Un schéma révèle une *intention* de redondance ; seul un test établit une *capacité* de basculement.**

> **11. Un composant qu'on ne sait pas exploiter dégrade l'architecture au lieu de l'améliorer.**

> **12. Une architecture dessinée n'est pas une architecture réelle.** *(chapitre 50)*

#### 1.8 La phrase fondatrice

> ### Apprendre à raisonner une architecture, c'est savoir reconstituer les arbitrages qui l'ont produite — et énoncer ceux qu'on propose.

Elle explique pourquoi ce cours consacre un chapitre à la sédimentation avant tout composant, pourquoi chaque brique porte son coût, et pourquoi il se termine sur ce qu'un schéma ne dira jamais.

**Ce que le lecteur saura faire au chapitre 50**, et qui est différent de savoir concevoir :

> *Poser les bonnes questions, proposer une architecture justifiée, et identifier ce qu'il lui reste à vérifier.*

🔴 **FIL ROUGE — décembre 2025 : Amélie regarde un schéma**

*Le fil rouge de ce cours suit six semaines. Il se termine exactement là où commence le volume Asset Management de cette collection — à la même réunion, à la même phrase.*

Amélie Roux est administratrice système à Nantes depuis quatre ans. Elle connaît bien la vingtaine de serveurs de la recherche et développement, la chaîne de construction logicielle, et le réseau du bâtiment.

**Le 15 décembre 2025**, Claire Nadeau, responsable de la sécurité du groupe, lui propose une mission d'un an : établir l'inventaire du système d'information d'HELIOMED. Trois sources donnent trois chiffres différents — 96, 71 et 118 serveurs — et personne ne sait lequel est vrai.

**Amélie accepte, et demande le schéma d'architecture du groupe.**

Ce qu'elle reçoit est le schéma 1.1. Il date de mars 2023, il fait une page, et il porte la mention *« version de travail »*.

**Voici ce qu'elle comprend en le lisant**, et voici ce qu'elle ne comprend pas.

| Ce qu'elle comprend | Ce qu'elle ne comprend pas |
|---|---|
| Il y a des zones séparées | Pourquoi la zone du milieu s'appelle « démilitarisée » |
| Les serveurs web sont en trois exemplaires | Pourquoi trois, et pourquoi l'applicatif est seul |
| Il y a un « mandataire inverse » | À quoi il sert — elle croit que c'est un pare-feu |
| Le site industriel est à part | Pourquoi il n'a qu'un seul lien |
| La base de données est en bas | S'il y en a une seule, et ce qui se passe si elle tombe |

**Les cinq questions qu'elle pose à Malik Ferhaoui, responsable de l'exploitation**, et qui structurent le cours :

1. *« Le mandataire inverse, c'est un pare-feu ? »* → chapitre 12
2. *« Pourquoi trois serveurs web et un seul applicatif ? »* → chapitres 13 et 35
3. *« Si la base tombe, qu'est-ce qui s'arrête ? »* → chapitre 35
4. *« Où sont les postes de travail ? Ils ne sont pas dessinés. »* → chapitre 6
5. *« Et l'annuaire, personne ne s'y connecte ? »* → chapitre 30

**La réponse de Malik à la cinquième question** est celle qu'Amélie retiendra, et elle contient le cours entier :

> *« Tout le monde s'y connecte. On ne le dessine jamais, sinon le schéma serait illisible. »*

**Ce qu'Amélie note dans son carnet, le 15 décembre** :

> *Je ne pourrai pas inventorier ce système tant que je ne saurai pas ce que je regarde. Avant de compter, il faut comprendre.*

**Livrable de l'épisode.** Le schéma de mars 2023, et la liste de ses cinq questions — qui deviendra, au fil du cours, la liste de ce que le schéma ne dit pas.

→ La suite en 🔴 §2.6, quand un mot employé par trois personnes désignera trois choses différentes.

#### Synthèse mentale du chapitre 1

Toute architecture est un compromis : elle n'a pas été conçue, elle a été négociée entre six contraintes qui se contredisent deux à deux — disponibilité, performance, coût, sécurité, conformité, et l'histoire, qu'on oublie et qui est souvent la plus puissante. Trois arbitrages différents produisent trois architectures différentes pour un même besoin, et aucune n'est meilleure : chacune serait une erreur dans le contexte des deux autres. Quatre questions structurent la lecture, et la première échoue le plus souvent parce que personne n'enseigne que trois choses différentes circulent : le flux métier, dessiné · le flux de dépendance, rarement dessiné et dont la rupture arrête le service · le flux d'exploitation, presque jamais dessiné et dont la rupture rend aveugle sans arrêter le service. Confondre les deux derniers conduit à surdimensionner ce qui n'en a pas besoin. Enfin, la taille d'une organisation ne justifie jamais un composant : la contrainte, oui — et ajouter n'est jamais gratuit.

**Trois questions de vérification**

1. Un même besoin peut produire trois architectures différentes. Qu'est-ce qui les distingue, et laquelle est la meilleure ?
2. La collecte de journaux s'interrompt. Le service s'arrête-t-il ? À quelle famille de flux appartient-elle, et pourquoi la distinction compte-t-elle ?
3. Sur un schéma, un annuaire est dessiné sans aucun trait de connexion. Est-ce une erreur ? Que cela vous apprend-il sur les schémas en général ?

→ **Chapitre 2 — Le vocabulaire** : trois personnes emploient le mot « serveur », et désignent trois choses différentes.

---

### Chapitre 2 — Le vocabulaire

> Ce chapitre est court et il n'est pas facultatif. La moitié des malentendus d'architecture viennent de mots que trois personnes emploient en désignant trois choses.

#### 2.1 Les mots qui désignent trois choses

##### « Serveur »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | **Une machine** — physique ou virtuelle |
| Le développeur | **Un logiciel qui écoute** — un serveur web, un serveur de base de données |
| Le métier | **Un service** — « le serveur de paie est tombé » |

**Une même machine peut donc porter trois serveurs**, et un même serveur peut être réparti sur trois machines. Quand quelqu'un dit *« on a 96 serveurs »*, la première question utile est : *machines, logiciels ou services ?*

##### « Application »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | Un processus installé sur une machine |
| Le développeur | Un ensemble de code déployé |
| Le métier | **Ce qu'il ouvre le matin** — qui peut mobiliser huit composants |
| L'achat | Une licence, un contrat |

##### « Service »

Le mot le plus polysémique du domaine, et le plus important.

| Sens | Exemple | Chapitre |
|---|---|---|
| **Service technique** | Un processus qui tourne en arrière-plan | 18-23 |
| **Service réseau** | Ce qui écoute sur un port | 8-17 |
| **Service métier** | Ce qui produit une valeur pour l'organisation | **35** |
| Service au sens contractuel | Ce qui est facturé, avec un engagement | 38 |

⚠️ **Ce cours emploie « service » au sens métier** — chapitre 35 — sauf mention explicite. C'est le sens qui permet de décider.

##### Les autres pièges

| Mot | Ambiguïté |
|---|---|
| **Plateforme** | Un ensemble matériel · un socle logiciel · un produit commercial |
| **Instance** | Une machine · un processus · un locataire chez un fournisseur |
| **Cluster** | Un groupe de machines redondantes · un groupe qui répartit la charge · un orchestrateur — **trois choses différentes** |
| **Nœud** | Une machine · un point du réseau · un membre d'un cluster |
| **Environnement** | Production, recette, développement · ou le contexte technique d'exécution |

#### 2.2 Le vocabulaire minimal

Douze mots suffisent pour lire un schéma. Les voici, définis pour la lecture — pas pour l'exactitude protocolaire *(principe de coupe)*.

| Terme | Ce qu'il faut en savoir pour lire |
|---|---|
| **Client** | Ce qui demande. Un poste, mais aussi un serveur qui en appelle un autre |
| **Serveur** | Ce qui répond. Le rôle, pas la machine |
| **Protocole** | La convention de dialogue. Sur un schéma, il indique **la nature du flux** |
| **Port** | Le numéro qui identifie le service sur une machine. Il dit **quoi**, pas **où** |
| **Adresse** | Où se trouve une machine sur le réseau. Elle change |
| **Nom** | Ce qu'on retient. Il faut le traduire en adresse — chapitre 14 |
| **Segment** | Un morceau de réseau, isolé des autres par un équipement |
| **Zone** | Un regroupement de segments partageant un même niveau de confiance |
| **Flux** | Ce qui circule entre deux points, dans une direction |
| **Session** | Une conversation en cours, avec un état — chapitre 31 |
| **Redondance** | Deux exemplaires d'un même rôle, dont un peut tomber |
| **Point de rupture** | Ce qui, en tombant, arrête un service. **La notion la plus utile du cours** |

**Ce qui ne figure pas dans cette liste, volontairement** : les couches d'un modèle en sept niveaux, les classes d'adresses, les mécanismes de contrôle de congestion. Ils ne servent pas à lire un schéma — *principe de coupe*.

#### 2.3 Le vocabulaire du terrain

Comme dans les autres volumes de la collection : ce que dit le cours, et ce que vous entendrez.

| Terme du cours | Ce que vous entendrez | Nuance à ne pas perdre |
|---|---|---|
| Mandataire inverse | « **le reverse** », « le proxy », « le frontal » | On l'appelle « proxy » alors qu'il fait l'inverse — chapitre 12 |
| Mandataire sortant | « **le proxy** » | Même mot, fonction opposée |
| Répartiteur de charge | « **le load balancer** », « le LB », « la VIP » | La « VIP » désigne l'adresse virtuelle, pas l'équipement |
| Zone démilitarisée | « **la DMZ** » | Le mot est militaire et trompeur — chapitre 25 |
| Point de rupture unique | « **le SPOF** » | — |
| Résolution de noms | « **le DNS** » | Souvent employé pour désigner le service **et** le serveur |
| Annuaire | « **l'AD** », « le LDAP », « le domaine » | Trois choses différentes, souvent confondues |
| Infrastructure de clés | « **la PKI** », « les certifs » | — |
| Poste d'administration | « **le bastion** », « le jump », « le rebond » | — |
| Segment réseau | « **le VLAN** », « le subnet » | Deux notions distinctes, souvent alignées mais pas toujours |
| Flux de dépendance | *(aucun terme courant)* | **L'absence de mot est le problème** — règle principe des trois flux |
| Orchestrateur | « **le cluster** », « K8s », « la plateforme » | — |

⚠️ **La ligne « flux de dépendance » est la plus significative du tableau.** Il n'existe pas de terme courant pour désigner ce sans quoi un service ne peut pas s'établir. C'est l'une des raisons pour lesquelles ces flux sont invisibles sur les schémas : **on ne dessine pas ce qu'on ne nomme pas.**

#### 2.4 Lire un protocole sur un schéma

Sans entrer dans leur fonctionnement, six protocoles suffisent à identifier la nature d'un flux.

| Ce qui est écrit | Ce que ça vous dit du flux |
|---|---|
| `443`, `HTTPS` | Une consultation web chiffrée — flux **métier**, le plus courant |
| `80`, `HTTP` | Idem, non chiffré. Sur un schéma récent, c'est une **question à poser** |
| `53`, `DNS` | Résolution de noms — flux de **dépendance** |
| `389`, `636`, `LDAP` | Annuaire — flux de **dépendance** |
| `123`, `NTP` | Synchronisation d'horloge — flux de **dépendance**, presque jamais dessiné |
| `514`, `syslog` | Journaux — flux d'**exploitation** |
| `3389`, `22` | Administration à distance — flux d'**exploitation**, **le plus sensible** |
| `1433`, `3306`, `5432` | Bases de données — flux **métier**, entre serveurs |

**Ce que ce tableau permet immédiatement** : classer un flux dans l'une des trois familles sans rien connaître du protocole. C'est le principe de coupe appliqué — juste ce qu'il faut pour décider.

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. Aucun numéro de port n'y figure. Vous ne pouvez donc pas savoir quels flux le traversent réellement. **C'est le cas de la majorité des schémas d'architecture**, et c'est la première chose qui manque quand on veut raisonner.

#### 2.5 🔬 Mini-lab 1 — Quatre phrases, quatre malentendus

**Objectif** — Repérer une ambiguïté de vocabulaire et poser la question qui la lève.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §2.1 à §2.3
**Compétences validées** — ✔ identifier un mot polysémique ✔ formuler la question qui désambiguïse ✔ reconnaître les conséquences d'un malentendu

**Les phrases** :

```
① « On a 96 serveurs. »
② « L'application de paie est tombée ce matin. »
③ « Il faut mettre l'application derrière le proxy. »
④ « On a un cluster de trois nœuds. »
```

**Consigne** : pour chacune, dites quelles interprétations sont possibles, la question à poser, et ce que coûte le malentendu.

---

**Corrigé**

| # | Interprétations possibles | Question à poser | Ce que coûte le malentendu |
|---|---|---|---|
| **①** | 96 machines · 96 systèmes · 96 services · 96 lignes dans un référentiel | *« Machines physiques, machines virtuelles, ou services ? »* | Un dénominateur faux pour tout le reste — c'est le volume Asset Management |
| **②** | Un processus · un serveur · **un service métier composé de six composants** | *« Qu'est-ce qui ne marche plus, du point de vue de l'utilisateur ? »* | On redémarre une machine alors que le problème est ailleurs |
| **③** | Mandataire **sortant** — pour que l'application accède à Internet · mandataire **inverse** — pour qu'on y accède depuis Internet. **Fonctions opposées** | *« Pour sortir, ou pour entrer ? »* | On ouvre un flux dans le mauvais sens, ou on expose ce qui ne devait pas l'être |
| **④** | Trois machines redondantes · trois machines qui se répartissent la charge · trois nœuds d'un orchestrateur | *« Si un nœud tombe, que se passe-t-il ? »* | On croit avoir une redondance qu'on n'a pas |

**La phrase ③ est celle qui produit les erreurs les plus coûteuses**, parce que le même mot désigne deux fonctions opposées et que personne ne pense à demander.

**L'erreur attendue** : traiter ① comme une question de comptage. C'est une question de **définition** — et c'est exactement le chapitre 2 du volume Asset Management.

#### 2.6 🔴 FIL ROUGE — décembre 2025 : trois personnes, trois « serveurs »

Amélie reprend les trois chiffres de décembre — 96, 71, 118 — et pose à chacun une seule question : *« quand tu dis serveur, tu comptes quoi ? »*

| Interlocuteur | Ce qu'il compte | Chiffre |
|---|---|---|
| Malik Ferhaoui, exploitation | Des **machines** — physiques et virtuelles — qu'il administre | 96 |
| La comptabilité | Des **immobilisations** — du matériel acheté et non amorti | 71 |
| L'outil de scan | Des **adresses ayant répondu** — donc ni les machines éteintes, ni celles hors du segment balayé | 118 |

**Trois définitions, trois périmètres, aucune intersection complète.** Et une découverte : le scan compte **118 adresses**, pas 118 machines — deux serveurs à deux interfaces réseau y comptent quatre fois.

**Ce qu'Amélie note** :

> *Personne ne s'est trompé. Nous avons trois réponses à trois questions différentes, et nous n'avons posé aucune des trois.*

**Ce qui est décidé** : avant tout comptage, écrire ce que le mot désigne. Cette décision sera formalisée en janvier — c'est le chapitre 2 du volume Asset Management, et c'est la réunion de deux heures qui y est racontée.

→ La suite en 🔴 §3.7, quand Amélie apprendra à lire un schéma — et surtout ce qu'il ne dit pas.

#### Synthèse mentale du chapitre 2

Trois mots portent l'essentiel des malentendus d'architecture — serveur, application, service — et chacun désigne au moins trois choses selon qui parle. Une même machine peut porter trois serveurs, et un même serveur être réparti sur trois machines : la question utile devant un chiffre est toujours *machines, logiciels ou services ?* Douze termes suffisent pour lire un schéma, et le plus utile d'entre eux est le point de rupture. Six protocoles suffisent à classer un flux dans l'une des trois familles sans rien connaître de leur fonctionnement. Enfin, il n'existe pas de terme courant pour désigner un flux de dépendance — et cette absence de mot est l'une des raisons pour lesquelles ces flux ne sont jamais dessinés : on ne dessine pas ce qu'on ne nomme pas.

**Trois questions de vérification**

1. Quelqu'un vous annonce un nombre de serveurs. Quelle question posez-vous, et pourquoi ce n'est pas une question de comptage ?
2. « Mets l'application derrière le proxy. » Pourquoi cette phrase est-elle dangereuse, et que demandez-vous ?
3. Pourquoi l'absence de terme courant pour « flux de dépendance » a-t-elle un effet concret sur les schémas ?

→ **Chapitre 3 — Comment lire un schéma** : les conventions, et surtout ce qu'un schéma choisit de ne pas montrer.

---

### Chapitre 3 — Comment lire un schéma

> Chapitre méta, et l'un des plus utiles du cours. Personne n'enseigne à lire un schéma ; on suppose que c'est évident. Ce ne l'est pas.

#### 3.1 Ce qu'une boîte représente

**Le problème** : une boîte sur un schéma peut représenter cinq choses différentes, et rien ne l'indique.

| Ce que la boîte peut être | Comment le deviner |
|---|---|
| Une **machine** physique ou virtuelle | Nom d'hôte, mention d'un système |
| Un **rôle** — « serveur web » sans dire combien | Nom générique, absence de nom d'hôte |
| Un **groupe** — trois machines dessinées en une | Mention d'un nombre, boîtes empilées |
| Un **service** — un ensemble de composants | Nom métier, positionnement isolé |
| Un **fournisseur externe** — une boîte noire | Nom commercial, position en bordure |

⚠️ **Une confusion fréquente, et coûteuse** : lire un **rôle** comme une **machine**. « Serveur web » sur un schéma ne dit pas s'il y en a un ou douze — donc ne dit pas si c'est un point de rupture.

**La question à poser devant toute boîte** : *combien y en a-t-il réellement, et que se passe-t-il si l'un tombe ?*

#### 3.2 Ce qu'un trait représente

Un trait est encore plus ambigu qu'une boîte.

| Ce que le trait peut être | Fréquence |
|---|---|
| Un **câble** — une liaison physique | Sur les schémas physiques |
| Un **flux** — quelque chose circule | Sur les schémas de flux |
| Une **relation logique** — « dépend de », « appartient à » | Sur les schémas logiques |
| Une **adjacence réseau** — « peut joindre » | Fréquent, et rarement explicité |
| **Rien de précis** — le dessinateur reliait deux choses proches | **Plus fréquent qu'on ne croit** |

**Trois questions devant tout trait** :

```
1. Qui initie ? (le sens compte, et il est rarement fléché)
2. Qu'est-ce qui circule ? (quelle famille de flux)
3. Est-ce permis, ou seulement possible ?
```

⚠️ **La troisième est la plus importante en sécurité.** Un trait indique souvent une **possibilité technique**, pas une autorisation. Deux machines dans le même segment sont reliées, que ce soit voulu ou non.

#### 3.3 Les quatre vues d'un même système

**Une architecture ne se représente pas d'un seul schéma.** Il en faut au moins quatre, et confondre les vues est une source d'erreur permanente.

🖼 **SCHÉMA 3.1 — Le même système, quatre vues** · *Quatre panneaux côte à côte, mêmes composants, représentations différentes.*

| Vue | Ce qu'elle montre | Ce qu'elle cache | Qui la produit |
|---|---|---|---|
| **Physique** | Machines, câbles, baies, sites | Ce qui s'exécute dessus | Infrastructure |
| **Logique** | Rôles, zones, relations | Le nombre réel de machines | Architecture |
| **Flux** | Ce qui circule, dans quel sens, sur quel protocole | La topologie physique | Sécurité, réseau |
| **Service** | Ce qui produit une valeur métier | **Presque toute la technique** | Métier, continuité |

**Exemple, sur le même objet** :

```
VUE PHYSIQUE      3 machines dans la baie B12, site de Lyon

VUE LOGIQUE       [ serveurs web ] ──► [ applicatif ] ──► [ base ]

VUE FLUX          poste ──443──► mandataire ──8080──► web
                  web ──1433──► base
                  web ──389──► annuaire        ← dépendance

VUE SERVICE       « Télésuivi HelioLink » — disponible 24/7,
                  dépend de : authentification, base, réseau Lyon
```

**Ce que la comparaison enseigne** : la vue service ne mentionne aucune machine, et la vue physique ne mentionne aucun service. **Aucune des deux ne ment ; elles répondent à deux questions différentes.**

👁 **CE QU'IL FALLAIT OBSERVER** — la vue flux est la seule qui fasse apparaître l'annuaire. C'est pour cela qu'elle est la plus utile en sécurité, et la plus rare dans les organisations.

#### 3.4 Ce qui n'est jamais dessiné

**La liste la plus utile du chapitre.** Elle sera complétée au chapitre 50.

| Ce qui manque presque toujours | Pourquoi | Conséquence |
|---|---|---|
| **La résolution de noms** | Tout le monde s'y connecte, le schéma serait illisible | Sa panne paraît inexplicable |
| **L'annuaire** | Idem | On sous-estime son caractère critique |
| **La synchronisation d'horloge** | Considérée comme acquise | Une dérive produit des rejets d'authentification incompréhensibles |
| **Les chemins d'administration** | Ils ne servent pas le métier | **Ce sont souvent les plus sensibles** — chapitre 27 |
| **Les sauvegardes** | Elles ne participent pas au service nominal | On découvre en incident qu'elles passent par un chemin non protégé |
| **Les postes de travail** | Trop nombreux | **La majorité des incidents commence là** — chapitre 6 |
| **Les services en ligne** | Pas chez nous, donc pas dessinés | Chapitre 38 |
| **Les liens partenaires** | Anciens, oubliés | Chapitre 38 |
| **Les certificats et leur autorité** | Invisibles quand ça marche | Une expiration arrête un service sans prévenir |
| **Le temps** | Un schéma est instantané | On ne voit ni l'historique, ni ce qui est en cours de migration |
| **Les versions** | Ça alourdirait | On ne peut pas raisonner l'obsolescence |

🎯 **L'exercice à faire une fois dans sa carrière** : prenez le schéma de votre organisation et **dessinez au crayon les onze éléments ci-dessus**. La page devient illisible en quatre minutes. C'est exactement pour cela qu'ils ne sont pas dessinés — et c'est exactement pour cela qu'il faut savoir qu'ils existent.

#### 3.5 Les conventions courantes

Elles ne sont pas normalisées, mais elles reviennent.

| Convention | Signification habituelle |
|---|---|
| Position **haute** = extérieur | Internet en haut, données en bas |
| Position **basse** = données | La base est presque toujours au fond — chapitre 20 |
| Un **nuage** | Quelque chose qu'on ne maîtrise pas ou qu'on ne détaille pas |
| Des boîtes **empilées** | Plusieurs exemplaires du même rôle |
| Un trait **pointillé** | Un flux logique, une relation, ou un lien non permanent |
| Une **double ligne** | Une redondance, ou un lien à haut débit |
| Un composant **à cheval sur deux zones** | Il traverse une frontière — **toujours un point d'attention** |

⚠️ **Aucune de ces conventions n'est garantie.** Sur un schéma inconnu, la première question est : *y a-t-il une légende ?* S'il n'y en a pas — cas majoritaire — les conventions ci-dessus sont des hypothèses à vérifier, pas des certitudes.

#### 3.6 🔬 Mini-lab 2 — Un schéma à cinq boîtes

**Objectif** — Lire un schéma minimal et formuler ce qu'il ne dit pas.
**Durée** 25 min · **Difficulté** 🟢 débutant · **Prérequis** §3.1 à §3.5
**Compétences validées** — ✔ interroger une boîte ✔ interroger un trait ✔ identifier la vue employée ✔ lister l'invisible

**Le schéma** :

```
        Internet
            │
      [ pare-feu ]
            │
      [ serveur web ]
            │
      [ base de données ]
            │
      [ sauvegarde ]
```

❓ **QUE VOYEZ-VOUS ?**

1. Combien de machines ce schéma représente-t-il ?
2. Quelle vue est-ce ?
3. Que se passe-t-il si le serveur web tombe ?
4. Citez cinq choses qui manquent.
5. Le trait entre la base et la sauvegarde : qui initie ?

---

**Corrigé**

**1. On ne sait pas.** Chaque boîte peut être une machine, un rôle ou un groupe. Rien ne l'indique. **C'est la bonne réponse** — et c'est la première question à poser à l'auteur du schéma.

**2. Une vue logique**, probablement. Aucun protocole, aucune adresse, aucun site : ce n'est ni une vue physique, ni une vue de flux. Ce n'est pas non plus une vue service — aucun nom métier.

**3. On ne sait pas non plus.** S'il est unique, le service s'arrête. S'il représente un groupe, il ne se passe rien. **Le schéma ne permet pas de répondre à la question la plus importante qu'on puisse lui poser.**

**4. Ce qui manque** — au moins :

| Manquant | Effet |
|---|---|
| Résolution de noms | Sans elle, personne n'atteint le serveur |
| Authentification | Où prouve-t-on son identité ? |
| Chemins d'administration | Comment ces machines sont-elles administrées ? |
| Postes de travail | Les utilisateurs internes n'apparaissent pas |
| Protocoles et sens des flux | On ne sait pas ce qui circule |
| Journalisation, supervision | Aucun flux d'exploitation |
| Certificats | Le flux est-il chiffré ? |
| Le nombre d'exemplaires | Voir question 3 |

**5. La sauvegarde initie presque toujours.** C'est contre-intuitif au vu du sens de lecture du schéma, qui suggère un flux descendant. **Et c'est un point de sécurité majeur** : si la sauvegarde initie, elle possède un accès à la base — donc à toutes les données. Le trait ne dit rien du sens, et le sens change tout.

**Les deux erreurs attendues**

1. **Répondre « cinq machines ».** Le schéma ne le dit pas, et l'admettre est la compétence visée.
2. **Répondre « le service s'arrête » à la question 3.** C'est probable, ce n'est pas établi — et la différence entre les deux est ce que ce cours enseigne.

#### 3.7 🔴 FIL ROUGE — décembre 2025 : ce que le schéma ne dit pas

Amélie applique au schéma 1.1 les questions du §3.4. Elle liste ce qui n'y figure pas, et demande à Malik de confirmer.

| Élément absent | Existe-t-il ? | Réponse de Malik |
|---|---|---|
| Résolution de noms | **Oui**, deux serveurs | *« On ne les dessine jamais »* |
| Synchronisation d'horloge | **Oui** | *« Je n'y avais jamais pensé »* |
| Chemins d'administration | **Oui** | *« On passe par le réseau d'admin, il n'est pas sur ce schéma »* |
| Postes de travail | **620** | *« Ils sont partout, ça n'aurait pas de sens de les dessiner »* |
| Services en ligne | **« Une trentaine ? »** | *« Là, je ne sais pas. Ce n'est pas moi qui les gère »* |
| Sauvegarde | Oui | *« Elle est dessinée, mais son chemin ne l'est pas »* |
| Site de Nantes | **Oui** | *« Il n'est pas sur ce schéma. C'est un oubli »* |

**Deux réponses comptent plus que les autres.**

La cinquième — *« je ne sais pas »* — désigne un périmètre entier que personne ne suit. Ce sera le point le plus coûteux du volume Asset Management.

La septième — *« c'est un oubli »* — révèle que le schéma officiel du groupe **ne mentionne pas l'un de ses trois sites**. Depuis mars 2023.

**Ce qu'Amélie note** :

> *Le schéma n'est pas faux. Il est incomplet, et personne ne sait de combien. C'est exactement le problème que je suis censée résoudre.*

→ La suite en 🔴 §4.6, quand elle comprendra pourquoi l'architecture est « bizarre ».

#### Synthèse mentale du chapitre 3

Une boîte peut représenter cinq choses — machine, rôle, groupe, service ou fournisseur — et rien ne l'indique : la confusion coûteuse est de lire un rôle comme une machine, parce qu'elle empêche de savoir si c'est un point de rupture. Un trait est plus ambigu encore, et trois questions le désambiguïsent : qui initie, qu'est-ce qui circule, est-ce permis ou seulement possible. Quatre vues sont nécessaires pour représenter un système, et confondre les vues est une erreur permanente : la vue service ne mentionne aucune machine, la vue physique aucun service, et aucune ne ment. La vue de flux est la seule qui fasse apparaître les dépendances, ce qui la rend la plus utile en sécurité et la plus rare en pratique. Enfin, onze éléments ne sont presque jamais dessinés, dont la résolution de noms, l'annuaire, les chemins d'administration et les postes de travail — et si l'on tentait de les dessiner, la page deviendrait illisible en quatre minutes.

**Trois questions de vérification**

1. Un schéma porte une boîte « serveur web ». Quelles questions posez-vous avant d'en tirer une conclusion sur la disponibilité ?
2. Un trait relie une base de données à une sauvegarde. Pourquoi le sens compte-t-il, et qu'implique chaque réponse ?
3. Citez cinq éléments qui ne figurent sur aucun schéma d'architecture, et l'effet de leur absence.

---

### Chapitre 4 — La sédimentation

> Le chapitre qui explique pourquoi les systèmes d'information sont « bizarres ». Il évite plus de jugements naïfs que tout le reste du cours.

#### 4.1 Aucune architecture n'a été construite d'un bloc

**Le constat**, et il est vérifiable sur n'importe quel système en service depuis plus de cinq ans :

> Ce que vous regardez n'est pas une architecture. C'est un **empilement de décisions** prises à des époques différentes, sous des contraintes différentes, par des gens différents — dont la plupart ne travaillent plus là.

**Ce que le débutant pense** : *ils auraient dû refaire propre.*
**Ce que le praticien sait** : *ils n'en avaient pas la possibilité.*

**Les cinq raisons pour lesquelles on ne refait pas** :

| Raison | Mécanisme |
|---|---|
| **Le coût** | Reconstruire coûte plus cher que maintenir, souvent d'un ordre de grandeur |
| **Le risque** | Un système qui fonctionne mal fonctionne quand même. Une migration peut échouer |
| **La dépendance** | Un composant ancien porte une intégration que plus personne ne sait refaire |
| **L'absence de fenêtre** | Le service ne peut pas s'arrêter assez longtemps |
| **La perte de connaissance** | Personne ne sait plus exactement ce que fait le composant |

⚠️ **La cinquième est rarement avouée, et elle explique beaucoup de situations.** Un système qu'on ne comprend plus ne se remplace pas : on l'entoure.

#### 4.2 Les couches historiques, et comment on les reconnaît

🖼 **SCHÉMA 4.1 — Les strates d'un système d'information** · *Coupe géologique : quatre strates superposées, chacune datée, avec les composants caractéristiques.*

```
  ┌─────────────────────────────────────────────────────────┐
  │  STRATE 4 — 2018 →     Cloud, conteneurs, services      │
  │                        en ligne, interfaces applicatives│
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 3 — 2005-2018  Virtualisation, web interne,     │
  │                        annuaire unifié, mobilité        │
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 2 — 1995-2005  Client-serveur, bases            │
  │                        relationnelles, réseau local     │
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 1 — avant 1995 Applications centralisées,       │
  │                        terminaux, traitements par lots  │
  └─────────────────────────────────────────────────────────┘
       Les quatre coexistent dans la plupart des organisations.
```

**Les signes de reconnaissance sur un schéma** :

| Signe | Strate probable | Ce qu'il implique |
|---|---|---|
| Un traitement nocturne, en lot | 1 ou 2 | Une fenêtre à respecter, un ordre à ne pas casser |
| Un serveur avec un nom de personne ou de planète | 2 | Antérieur aux conventions de nommage |
| Un client lourd installé sur les postes | 2 | Une migration de poste devient un projet applicatif |
| Une base au format ancien | 2 | Souvent le point de blocage d'une modernisation |
| Une machine virtuelle qui n'a jamais redémarré depuis des années | 3 | Personne n'ose |
| Un composant unique sans redondance au milieu d'un ensemble redondé | 2 ou 3 | Il n'a pas été inclus dans la modernisation |
| Une passerelle entre deux zones qui ne devraient pas communiquer | Toutes | **Le résultat d'un besoin urgent, jamais reconsidéré** |
| Une interface applicative « v1 » toujours en service à côté d'une « v3 » | 4 | Des clients n'ont pas migré |

**La dernière ligne du tableau est la plus instructive** : une passerelle inexplicable est presque toujours l'empreinte d'une urgence ancienne. Quelqu'un avait besoin que deux choses communiquent, vite. La solution devait être provisoire. Elle a douze ans.

🔭 **À RECONNAÎTRE — architectures centralisées historiques**

**① Pourquoi ce bloc existe.** Un cours d'architecture ne doit pas laisser croire que tout système d'information réel se compose de machines virtuelles, de conteneurs et de services en ligne. **Ce n'est pas le cas.**

> **Vous rencontrerez encore des architectures centralisées autour de systèmes de type mainframe, particulièrement dans certains grands systèmes d'information historiques et dans les secteurs fortement transactionnels** — banque, assurance, transport, administration.

**② Ce qu'il faut en savoir.** Le modèle est différent de tout ce que ce cours décrit : un système central très puissant, des traitements par lots, une fiabilité et une capacité transactionnelle qui restent difficiles à égaler, et un écosystème logiciel accumulé sur des décennies.

**③ Ce qu'il ne faut surtout pas en conclure.**

| Ce qu'un débutant pense | Ce qu'un praticien sait |
|---|---|
| « C'est ancien, donc dépassé » | **Ancien ne veut dire ni inutile, ni mauvais, ni non critique** |
| « Il faudrait migrer » | Cela a été étudié · le coût, le risque et l'absence de fenêtre l'ont écarté — §4.1 |
| « Personne ne sait plus le faire tourner » | Parfois vrai, et c'est précisément l'argument **contre** une migration précipitée |

**④ Ce que cela change en lecture.** Sur un schéma, il apparaît généralement comme une boîte à part, reliée au reste par un nombre restreint de flux — souvent des échanges de fichiers nocturnes, ou une passerelle applicative. **Ces flux sont exactement le genre de dépendance que le §29.5 apprend à chercher.**

**⑤ En réunion** : *« ça vient du mainframe »* → **par quel flux, à quelle fréquence, et que se passe-t-il si l'échange nocturne échoue ?**

⚠️ **Ce bloc est le prolongement direct de ce chapitre** : une strate ancienne n'est pas une erreur. C'est une décision, prise et reconduite, dont il faut connaître la raison avant de la juger.

#### 4.3 Les quatre événements qui sédimentent

| Événement | Ce qu'il laisse |
|---|---|
| **Une acquisition** | Un second annuaire, un second réseau, des conventions différentes, souvent un lien direct « temporaire » |
| **Une migration inachevée** | Deux systèmes qui font la même chose, dont un qu'on n'ose pas éteindre |
| **Une urgence** | Un contournement qui devient permanent |
| **Un départ** | Un composant que plus personne ne comprend |

**L'acquisition est le plus puissant des quatre.** Elle ajoute d'un coup une architecture entière, conçue ailleurs, avec d'autres arbitrages — et la fusion complète n'est presque jamais menée à son terme.

🏭 **TROIS TAILLES — la sédimentation**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Âge du système | 12 ans | 24 ans | 40 ans, par accumulation |
| Strates coexistantes | 2 | 3 | **4** |
| Acquisitions absorbées | 0 | 1 (2019) | **7** |
| Annuaires | 1 | 1, plus un hérité | **4 forêts** |

⚠️ **Application du principe de la contrainte** : Novaris n'a pas quatre forêts d'annuaire *parce qu'elle compte douze mille salariés*. Elle en a quatre **parce qu'elle a absorbé sept sociétés en quinze ans et que trois fusions d'annuaire ont été arbitrées comme trop risquées**. Une organisation de même taille née d'une croissance interne en aurait une seule.

#### 4.4 Comment on lit une architecture sédimentée

**La méthode**, en trois questions :

```
1. Qu'est-ce qui ne ressemble pas au reste ?
   → conventions de nommage, technologies, positionnement

2. Qu'est-ce qui devrait être là et n'y est pas ?
   → une redondance absente au milieu d'un ensemble redondé

3. Qu'est-ce qui relie deux choses qui ne devraient pas être reliées ?
   → une passerelle, un flux transverse, un compte partagé
```

**Chacune de ces anomalies a une date**, et retrouver cette date explique l'architecture mieux que n'importe quel document.

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous arrivez dans une organisation. Le schéma comporte une passerelle directe entre la zone bureautique et le réseau industriel, ce qui contredit toutes les bonnes pratiques. Que faites-vous ?*
**Vous demandez sa date et son motif avant de la critiquer.** Dans la majorité des cas, elle répond à un besoin réel — un export de données de production vers un outil de gestion — décidé un jour où il fallait aller vite. La mauvaise décision évitée : **proposer sa suppression en réunion sans savoir ce qu'elle porte**, se voir opposer un usage métier qu'on ignorait, et perdre la crédibilité nécessaire pour obtenir la vraie correction — qui est souvent de remplacer le flux, pas de le couper.

#### 4.5 📌 Ce que la sédimentation n'excuse pas

Le chapitre pourrait produire un excès inverse : tout expliquer par l'histoire et ne rien remettre en cause.

| La sédimentation explique | Elle n'excuse pas |
|---|---|
| Qu'un composant ancien existe | Qu'on ne sache pas ce qu'il fait |
| Qu'une passerelle ait été créée en urgence | Qu'elle ne soit pas documentée douze ans après |
| Qu'une migration soit inachevée | Qu'aucune décision n'ait été prise sur son achèvement |
| Qu'un annuaire hérité subsiste | Qu'on ignore qui y a des droits |

**La distinction** : la sédimentation explique **l'existence** d'un état ; elle n'explique jamais **l'absence de décision** à son sujet. C'est exactement la distinction que fait le volume Maintien en condition de sécurité entre un écart connu et décidé, et un écart ignoré.

#### 4.6 🔴 FIL ROUGE — décembre 2025 : pourquoi c'est « bizarre »

Amélie a relevé sur le schéma 1.1 trois éléments qui la gênent :

| Anomalie | Ce qu'elle en pense |
|---|---|
| Trois serveurs web, un seul applicatif | *« C'est incohérent »* |
| Une machine nommée `HERMES` au milieu de noms normalisés | *« Ils ont oublié de la renommer »* |
| Un lien direct entre le réseau bureautique et le site industriel | *« Ça ne devrait pas exister »* |

**Elle demande à Malik.** Les trois réponses sont datées.

| Anomalie | L'histoire | Ce que ça change |
|---|---|---|
| **Un seul applicatif** | En 2021, le passage à deux exemplaires a été chiffré. L'éditeur du progiciel facturait une seconde licence au prix de la première. **Arbitrage assumé, écrit, révisé chaque année** | Ce n'est pas une incohérence : c'est un compromis coût/disponibilité documenté |
| **`HERMES`** | Serveur de 2011, portant l'ancien outil de gestion de production. **Personne ne sait exactement ce qu'il fait encore.** Il reçoit un flux quotidien de l'usine | Ce n'est pas un oubli de nommage : c'est un composant que l'organisation n'a pas su remplacer |
| **Le lien bureautique-industriel** | Créé en 2018 pour un export de données de production vers le contrôle de gestion. Devait durer « le temps du projet » | Ce n'est pas une négligence : c'est une urgence de 2018 devenue permanente |

**Ce qu'Amélie comprend, et qu'elle note** :

> *Aucune des trois choses que je trouvais bizarres n'est une erreur. Deux sont des arbitrages, et une est une dette. Mais je ne pouvais pas faire la différence en regardant le schéma.*

**Le point que Malik ajoute**, et qui est le principe 2 du cours formulé par quelqu'un qui l'a vécu :

> *« Il n'y a jamais eu un moment où on a dessiné tout ça. On a ajouté des morceaux pendant vingt ans, chaque fois pour une bonne raison. Le résultat n'a été décidé par personne. »*

**Ce que cet épisode change pour la suite** : Amélie cesse de chercher les erreurs et commence à chercher **les dates**. C'est ce qui lui permettra, en février, de distinguer les cinq zones non couvertes de son inventaire — certaines sont des choix, d'autres des oublis, et la différence n'est visible que par l'histoire.

→ La suite en 🔴 §5.6, avec les zones.

#### Synthèse mentale du chapitre 4

Ce que vous regardez n'est pas une architecture mais un empilement de décisions prises à des époques différentes, par des gens différents, dont la plupart ne travaillent plus là. On ne refait pas propre pour cinq raisons, dont la moins avouée pèse lourd : un système qu'on ne comprend plus ne se remplace pas, on l'entoure. Quatre événements sédimentent — acquisition, migration inachevée, urgence, départ — et l'acquisition est le plus puissant, parce qu'elle ajoute d'un coup une architecture entière conçue ailleurs. Trois questions permettent de lire une architecture sédimentée : qu'est-ce qui ne ressemble pas au reste, qu'est-ce qui devrait être là et n'y est pas, qu'est-ce qui relie deux choses qui ne devraient pas l'être — et chaque anomalie a une date qui explique l'architecture mieux que n'importe quel document. Enfin, la sédimentation explique l'existence d'un état ; elle n'excuse jamais l'absence de décision à son sujet.

**Trois questions de vérification**

1. Un schéma comporte une passerelle qui contredit toutes les bonnes pratiques. Quelle est votre première question, et pourquoi pas votre première critique ?
2. Pourquoi « ils auraient dû refaire propre » est-il presque toujours un jugement naïf ?
3. Quelle est la différence entre ce que la sédimentation explique et ce qu'elle n'excuse pas ?

---

### Chapitre 5 — Les grandes zones

#### 5.1 Pourquoi on sépare

**Le principe**, et il est unique :

> **On sépare ce qui n'a pas le même niveau de confiance, ni les mêmes conséquences en cas de compromission.**

Le reste — les noms, les technologies, le nombre de zones — en découle largement.

**Ce qu'une séparation apporte, et ce qu'elle coûte** :

⚖️ **CONTRAINTE ET COÛT — la segmentation**

| Contrainte résolue | Coût introduit |
|---|---|
| Limiter la propagation d'une compromission | Des flux à ouvrir, documenter et maintenir |
| Contrôler ce qui traverse une frontière | Un dépannage plus difficile — « ça ne passe pas, mais où ? » |
| Appliquer des règles différentes par niveau de sensibilité | Une complexité qui croît avec le nombre de zones |
| Démontrer un cloisonnement en audit | **Un risque de contournement si les flux deviennent trop pénibles** |

⚠️ **Le dernier point est le plus mal anticipé** : une segmentation trop stricte produit des contournements — un compte partagé, un flux ouvert « temporairement », une machine à cheval sur deux zones. **Une zone contournée est pire qu'une zone absente**, parce qu'on croit qu'elle protège.

#### 5.2 Les six zones de référence

🖼 **SCHÉMA 5.1 — Les six zones** · *Bandes concentriques ou empilées, du moins fiable au plus sensible, avec les frontières marquées.*

```
   ╔═══════════════════════════════════════════════════════╗
   ║  EXTÉRIEUR — Internet, partenaires, mobilité          ║
   ║  Confiance : aucune                                   ║
   ╠═══════════════════════════════════════════════════════╣
   ║  BORDURE — pare-feu, accès distant, publication       ║
   ║  Rôle : filtrer, contrôler ce qui traverse            ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ZONE DÉMILITARISÉE — ce qui est exposé volontairement ║
   ║  Confiance : faible. Compromettable par conception    ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INTERNE — postes, serveurs métier, données           ║
   ║  Confiance : moyenne. C'est là qu'est la valeur       ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ADMINISTRATION — ce qui pilote tout le reste         ║
   ║  Confiance : maximale requise. **Rarement dessinée**  ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INDUSTRIEL / SPÉCIFIQUE — contraintes inversées      ║
   ║  Confiance : à part. Autres règles — chapitre 28      ║
   ╚═══════════════════════════════════════════════════════╝
```

| Zone | Ce qu'on y trouve | Ce qui la caractérise |
|---|---|---|
| **Extérieur** | Ce qu'on ne maîtrise pas | Aucune confiance, aucune hypothèse |
| **Bordure** | Pare-feu, passerelles d'accès distant | **Exposée par conception** — chapitre 10 |
| **Zone démilitarisée** | Ce qui doit être joignable de l'extérieur | On suppose qu'elle **sera** compromise |
| **Interne** | Postes, serveurs, données | Le plus grand volume, la plus grande valeur |
| **Administration** | Postes d'administration, consoles, orchestration | **Sa compromission donne tout le reste** |
| **Industriel** | Automates, supervision | Priorités inversées — chapitre 28 |

**La zone d'administration est la plus importante et la moins dessinée.** C'est le chapitre 27, et c'est le principal angle mort des schémas.

#### 5.3 Ce qui définit une frontière

Une zone n'est pas définie par un trait sur un schéma, mais par **ce qui doit être traversé pour passer**.

| Type de frontière | Ce qui la matérialise | Force | Ce qui la contourne |
|---|---|---|---|
| **Physique** | Réseaux distincts, sans lien | Maximale — et rare | Un support amovible · un portable branché aux deux |
| **Filtrage** | Un pare-feu entre deux segments | Forte, si les règles sont fines | Une règle trop large · un chemin oublié |
| **Segmentation logique** | Des segments distincts, routés | Moyenne — dépend du routage | Une route ajoutée sans filtrage |
| **Applicative** | Un mandataire inverse, une passerelle | Forte sur un protocole, nulle sur les autres | Tout ce qui n'emprunte pas ce protocole |
| **Déclarative** | *« C'est la DMZ »*, sans mécanisme | **Nulle** | Rien à contourner |

⚠️ **La dernière ligne est le piège de lecture le plus fréquent.** Sur beaucoup de schémas, une zone est dessinée sans qu'aucun mécanisme ne la matérialise réellement. **La question à poser devant toute frontière** : *qu'est-ce qui empêche de passer ?*

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. La zone démilitarisée est matérialisée par des pare-feu en haut, mais **rien n'est dessiné entre elle et le réseau interne**. Soit la frontière existe et n'est pas représentée, soit elle n'existe pas. Le schéma ne permet pas de trancher — et c'est la question la plus importante qu'on puisse lui poser.

#### 5.4 Les composants à cheval

**Le cas le plus intéressant en lecture** : un composant qui appartient à deux zones.

| Exemple | Pourquoi il est à cheval | Ce que ça implique |
|---|---|---|
| Un mandataire inverse | Il reçoit de l'extérieur, appelle l'intérieur | **C'est sa fonction** — chapitre 12 |
| Un serveur de sauvegarde | Il atteint toutes les zones | Sa compromission donne accès à toutes les données |
| Un poste d'administration | Il pilote plusieurs zones | Chapitre 27 |
| Un serveur avec deux interfaces réseau | Souvent un contournement historique | **À interroger systématiquement** |
| Un poste portable d'intervenant | Il se branche successivement sur deux réseaux | **Un pont différé** — §28.5 |

**La règle de lecture** : tout composant à cheval sur deux zones est **soit une frontière assumée, soit une brèche**. Il n'y a pas de troisième possibilité, et la distinction se fait en demandant si c'était voulu.

⚠️ **Le cas de la sauvegarde mérite une remarque.** C'est le composant le plus transverse d'une architecture : il atteint tout, pour tout copier. **Sa compromission donne accès à l'ensemble des données de l'organisation, sans jamais toucher à un seul serveur de production.** Et il n'est presque jamais dans la zone d'administration.

🔭 **À RECONNAÎTRE — architectures de calcul intensif**

**① Ce que c'est.** Des architectures optimisées pour des **calculs massifs, souvent parallèles** : simulation, recherche, modélisation, apprentissage automatique à grande échelle.

**② Ce qui les rend différentes d'un système d'information de gestion** :

| | Système de gestion | Calcul intensif |
|---|---|---|
| Ce qui compte | Disponibilité, cohérence, sécurité | **Débit de calcul, interconnexion entre nœuds, débit de stockage** |
| L'unité de travail | Une transaction | **Un travail soumis, qui dure des heures ou des jours** |
| Le réseau | Relie des services | **Relie des nœuds qui calculent ensemble** — la latence entre eux est structurante |
| L'arrêt | Un incident | **Une file d'attente qui s'allonge** |

**③ Ce qu'il faut en retenir en architecture.** Une zone de calcul intensif obéit à d'autres priorités, comme le réseau industriel du §28.1 — **et pour les mêmes raisons de fond : ses contraintes ne sont pas celles du reste du système d'information.** Y appliquer les règles du système de gestion sans discernement produit les mêmes blocages.

**④ En réunion** : *« c'est sur le cluster de calcul »* → **une zone à part, avec ses propres règles. Qui l'administre ? Quels flux la relient au reste ?**

📚 **À approfondir ailleurs** : c'est un domaine à part entière, avec sa propre ingénierie.

#### 5.5 Combien de zones, et pourquoi

**La question qui revient en conception** : *faut-il six zones ?*

| Nombre de zones | Quand c'est justifié | Ce que ça coûte |
|---|---|---|
| **2** — interne, extérieur | Aucun service publié, aucun actif à part | Presque rien |
| **3** — + DMZ | Un service est publié | Deux jeux de règles |
| **4** — + administration | Il y a des administrateurs distincts des utilisateurs | Des postes dédiés |
| **5** — + industriel ou spécifique | Un environnement aux contraintes inversées | Une autonomie à construire |
| **6 et plus** | Des entités, des sensibilités ou des obligations distinctes | **Une complexité qui croît vite** |

⚠️ **Le principe de la contrainte s'applique intégralement** : le nombre de zones ne se déduit pas de la taille. **Il se déduit du nombre de niveaux de confiance réellement différents.** Une organisation de deux mille personnes avec un seul métier et aucun service publié peut légitimement n'avoir que trois zones.

🔥 **SCÉNARIO — la zone existe sur le schéma, pas sur le réseau**

| Question | Réponse |
|---|---|
| Symptôme | Un audit demande la preuve du cloisonnement. Le schéma montre trois zones |
| Hypothèse naïve | « Le schéma fait foi » |
| Dépendance réelle | **Aucun équipement ne filtre entre deux d'entre elles.** Elles sont routées, pas filtrées |
| Ce que le schéma aurait dû montrer | Ce qui matérialise chaque frontière |
| Comment le vérifier en dix minutes | Depuis une machine de la zone A, tenter de joindre une machine de la zone B |

⚠️ **Ce test est le plus rentable du chapitre**, et il ne demande aucun outil : **une connexion réussie entre deux zones censées être séparées vaut tous les schémas du monde.**

#### 5.6 🔴 FIL ROUGE — décembre 2025 : combien de zones ?

Amélie compte les zones du schéma 1.1 : trois — démilitarisée, interne, industriel.

**Elle vérifie auprès de Malik.** Il y en a **six**.

| Zone | Sur le schéma ? | Réalité |
|---|---|---|
| Extérieur | Implicite | — |
| Bordure | Les deux pare-feu | Correct |
| Zone démilitarisée | Oui | Correct |
| Interne | Oui | **En réalité trois segments** : serveurs, postes Lyon, postes Nantes |
| **Administration** | **Non** | Existe : un segment dédié, deux postes, un accès depuis Lyon uniquement |
| Industriel | Oui | Correct, mais **le lien de 2018 le traverse** |

**Deux découvertes.**

La zone interne du schéma en cache trois, dont deux sur des sites différents. Le schéma représente une frontière là où il y en a plusieurs.

La zone d'administration n'est pas dessinée **et elle est la plus sensible**. Amélie demande pourquoi.

> *« Parce que ce schéma, on le montre aux clients »*, répond Malik.

**Ce qu'Amélie note**, et qui est un principe de lecture à part entière :

> *Un schéma est fait pour quelqu'un. Celui-ci est fait pour rassurer un client. Il ne ment pas — il ne montre pas ce qui ne le regarde pas. Je dois savoir pour qui un schéma a été dessiné avant de le lire.*

→ La suite en 🔴 §6.6, avec les 620 postes qui ne sont sur aucun schéma.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans une autre zone » | Une séparation existe sur le schéma | **Qu'est-ce qui la matérialise ?** — §5.3 |
| « C'est cloisonné » | Idem | Testé depuis quand ? |
| « Le serveur a une patte dans les deux » | Deux interfaces réseau | **La frontière n'existe plus à cet endroit** |
| « La sauvegarde accède à tout » | Constat de fait | **C'est le composant le plus transverse — où est-il ?** |

---

### Chapitre 6 — Le poste utilisateur

> Placé ici, en Partie I, parce que c'est là que commence la majorité des flux et la majorité des incidents — et qu'il ne figure sur presque aucun schéma.

#### 6.1 Le grand absent

**Le réflexe de tout débutant** : *Internet → pare-feu → serveur*.

**La réalité, en volume** : dans une organisation ordinaire, la majorité écrasante des connexions part d'un poste **interne**, pas d'Internet. Et la majorité des compromissions y commence.

**Pourquoi il n'est jamais dessiné** :

| Raison | Effet |
|---|---|
| Il y en a des centaines | Les dessiner rendrait le schéma illisible |
| Ils sont considérés comme uniformes | **Ils ne le sont pas** — §6.3 |
| Ils appartiennent à un autre périmètre | Souvent gérés par une autre équipe |
| **Ils ne « produisent » rien** | Erreur : ils consomment tout, et ils accèdent à tout |

⚠️ **La conséquence de lecture** : sur un schéma sans poste, vous ne voyez ni le point de départ de la plupart des flux, ni la surface d'attaque principale. **C'est l'omission la plus lourde des schémas d'architecture.**

#### 6.2 Ce qu'un poste contient et ce qu'il ouvre

🖼 **SCHÉMA 6.1 — Ce qu'un poste atteint**

```
                        [ services en ligne ]
                                  ▲
   [ Internet ] ◄───────────  [ POSTE ]  ───────────► [ serveurs internes ]
                                  │  │                  fichiers · applicatifs
                    stockage      │  └──► [ annuaire ]   messagerie · bases
                    amovible ◄────┘        (dépendance)
```

| Ce qu'il contient | Ce que ça implique |
|---|---|
| Des identifiants en mémoire | Une compromission donne accès à ce que l'utilisateur atteint |
| Des documents locaux | Souvent une copie de données sensibles |
| **Des sessions ouvertes** | Vers des services en ligne, **sans nouvelle authentification** |
| Des accès enregistrés | Mots de passe du navigateur, clés, jetons — §33 |
| Des logiciels non maîtrisés | Extensions, outils installés par l'utilisateur |

**Ce qu'il ouvre** : tout ce que son utilisateur a le droit d'atteindre — et **le poste ne fait aucune distinction entre un accès légitime et un accès détourné**.

⚠️ **La ligne des sessions ouvertes est celle qu'on sous-estime le plus.** Un second facteur d'authentification protège la connexion ; il ne protège pas une session déjà ouverte. **Un poste compromis hérite de toutes les sessions actives**, sans avoir à s'authentifier nulle part.

#### 6.3 Les quatre types de postes

| Type | Où il est | Ce qui change |
|---|---|---|
| **Fixe interne** | Sur le réseau de l'organisation | Le cas de référence |
| **Nomade** | Partout | Il n'est plus derrière le pare-feu. **Il l'est parfois par un tunnel, parfois pas** |
| **Virtualisé** | Le poste est ailleurs, l'écran est ici | Les données ne quittent pas le centre. **Une dépendance forte au réseau** |
| **Non maîtrisé** | Poste personnel, poste de prestataire | **Le cas le plus mal traité** — §38.4 |

**Le poste nomade est celui qui casse le raisonnement en zones du chapitre 5.** Un poste hors des murs n'est plus dans la zone interne — mais il y accède.

🖼 **SCHÉMA 6.2 — Les deux chemins d'un poste nomade**

```
  A — TUNNEL COMPLET
      poste ══tunnel══► réseau interne ──► serveurs
                                       └─► Internet
      → tout le trafic remonte · les contrôles internes s'appliquent
      → le lien du siège porte tout le trafic Internet des nomades

  B — TUNNEL PARTIEL
      poste ══tunnel══► réseau interne ──► serveurs internes
      poste ──────────────────────────────► Internet (direct)
      → moins de charge sur le lien
      → ⚠️ le trafic Internet du poste n'est plus filtré ni journalisé
      → le poste est simultanément dans DEUX réseaux
```

⚠️ **Le mode B crée une situation que le chapitre 5 interdirait sur un serveur** : le poste est simultanément connecté au réseau interne et à Internet, **sans qu'aucun équipement ne s'interpose**. C'est un composant à cheval — §5.4 — et il y en a des centaines.

**La question à poser devant tout schéma** : *les postes nomades passent-ils par le même chemin que les postes internes ?*

🏭 **TROIS TAILLES — les postes**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Nombre | 35 | 620 | ≈ 11 000 |
| Nomades | 3 | 180 | ≈ 4 000 |
| Postes non maîtrisés | **Oui** — le gérant utilise son portable personnel | Prestataires, encadré | Encadré, avec accès dédié |
| Poste virtualisé | Non | Pour les prestataires uniquement | Pour plusieurs métiers |

⚠️ **Principe de la contrainte** : Atelier Martin n'a pas de poste virtualisé *parce qu'elle est petite* — elle n'en a pas **parce qu'aucune contrainte ne le justifie** : pas de prestataire distant, pas de données à confiner, pas de parc hétérogène à uniformiser. Une entreprise de 35 personnes avec des sous-traitants dans trois pays en aurait un.

#### 6.4 Le poste dans les flux

Reprenons les trois familles du principe des trois flux, du point de vue du poste.

| Famille | Ce qui part du poste |
|---|---|
| **Métier** | Requêtes web, ouverture de fichiers, messagerie, impression |
| **Dépendance** | Résolution de noms · authentification à l'ouverture de session · validation de certificats · **obtention d'une adresse au démarrage** |
| **Exploitation** | Remontée d'inventaire · télémétrie de sécurité · télédistribution de logiciels · sauvegarde éventuelle |

**Le flux de dépendance le plus méconnu** : à l'ouverture de session, un poste interne interroge l'annuaire, applique des politiques, monte des lecteurs réseau, synchronise son horloge. **Si l'un de ces éléments manque, l'utilisateur constate un poste « lent » ou « bloqué »** — et le diagnostic est difficile parce qu'aucun de ces flux n'est sur le schéma.

🔥 **SCÉNARIO — l'ouverture de session prend cinq minutes**

| Question | Réponse |
|---|---|
| Symptôme | Les sessions s'ouvrent, très lentement. Uniquement sur un site |
| Hypothèse naïve | « Les postes sont vieux » |
| Dépendance réelle | **Un des flux d'ouverture attend l'expiration d'un délai** : un lecteur réseau injoignable, un contrôleur d'annuaire distant, une politique qui référence un serveur disparu |
| Ce que le schéma aurait dû montrer | Ce que fait un poste au démarrage — **jamais représenté** |
| Comment le reconnaître | **Une lenteur constante, à la seconde près, est un délai d'attente, pas une charge** |

⚠️ **Un indice de diagnostic utile, et rien de plus** : une lenteur **qui varie** oriente vers une question de charge · une lenteur **constante et reproductible, à la seconde près**, oriente vers un délai d'attente sur quelque chose d'injoignable.

📌 **Ce n'est pas une loi.** Une lenteur constante peut aussi venir d'un traitement systématiquement coûteux, d'une résolution de noms lente mais réussie, ou d'un chiffrement mal négocié. **C'est une piste à explorer en premier, pas une conclusion.**

#### 6.5 🔬 Mini-lab 3 — Où commence le flux ?

**Objectif** — Reconstituer le point de départ réel des flux d'une organisation.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §6.1 à §6.4

**La situation** : une organisation de 400 personnes. Un incident est survenu — un rançongiciel a chiffré un serveur de fichiers. Le schéma d'architecture montre : Internet → pare-feu → zone démilitarisée → serveurs internes → serveur de fichiers.

❓ **Questions**
1. En regardant ce schéma, par où l'attaquant est-il entré ?
2. Qu'est-ce que le schéma ne permet pas d'envisager ?
3. Quelle est l'hypothèse la plus probable, statistiquement ?

---

**Corrigé**

**1.** Le schéma suggère une entrée par Internet, via la zone démilitarisée. C'est la seule voie qu'il représente.

**2.** Il ne permet pas d'envisager **le poste utilisateur**, qui n'y figure pas. Ni le poste nomade, ni le prestataire, ni le stockage amovible, ni la messagerie ouverte sur un poste.

**3.** L'hypothèse la plus probable est **le poste** : pièce jointe ouverte, identifiants dérobés, session détournée. Le serveur de fichiers a été atteint **avec des droits légitimes**, depuis l'intérieur.

**La leçon** : *un schéma qui ne montre pas les postes oriente le diagnostic vers la mauvaise hypothèse.* Ce n'est pas un défaut du dessin — c'est un défaut de lecture, si le lecteur oublie ce qui n'est pas dessiné.

#### 6.6 🔴 FIL ROUGE — décembre 2025 : 620 postes invisibles

Amélie demande à Malik où sont les postes sur le schéma 1.1.

> *« Ils ne sont pas dessinés. Il y en a 620, ça n'aurait pas de sens. »*

**Elle pose alors trois questions**, et les réponses la surprennent :

| Question | Réponse |
|---|---|
| Combien de postes nomades ? | **180** — un tiers du parc |
| Comment reviennent-ils sur le réseau interne ? | Par un tunnel, vers la passerelle d'accès distant — **qui n'est pas sur le schéma non plus** |
| Y a-t-il des postes non maîtrisés ? | **Oui** — ceux des prestataires de l'infogérant, qui administrent les serveurs |

**La troisième réponse est celle qui compte.** Des postes qu'HELIOMED ne maîtrise pas ont un accès d'administration à ses serveurs. Ils ne figurent sur aucun schéma, dans aucun inventaire, et personne n'en connaît le nombre.

⚠️ **Et le tunnel de la deuxième réponse pose une question qu'Amélie ne sait pas encore formuler** : complet ou partiel ? — §6.3. Personne, chez HELIOMED, ne connaît la réponse en décembre 2025.

**Ce qu'Amélie note** :

> *Le schéma montre ce qui est à nous. Il ne montre ni ce qui vient de l'extérieur, ni ce qui appartient à d'autres — alors que c'est par là que passent les accès les plus puissants.*

**Ce que cet épisode annonce** : la question des postes de prestataires reviendra en septembre 2029 dans le volume Renseignement, quand un prestataire compromis fera l'objet d'une évaluation — et en mai 2030, quand un compte de prestataire de 2028, toujours actif, sera découvert dans une fuite.

→ La suite en 🔴 §7.5, avec la question qu'Amélie finit par poser à Claire.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « L'utilisateur a cliqué » | Un poste est peut-être compromis | **Ce qui compte n'est pas le clic, c'est ce que ce poste atteint** |
| « Ils sont en télétravail » | Postes nomades | **Tunnel complet ou partiel ?** — §6.3 |
| « C'est un poste perso » | Poste non maîtrisé | **Qu'atteint-il ? Avec quels droits ?** |
| « Le poste rame » | Lenteur | **Constante ou variable ?** La réponse oriente la recherche — elle ne la conclut pas |

---

### Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur

#### 7.1 Deux métiers, deux temporalités

| | **L'architecte** | **Le lecteur** |
|---|---|---|
| Quand | **Avant** — au moment de décider | **Après** — sur ce qui existe |
| Son objet | Un système qui n'existe pas encore | Un système qui existe et qu'il n'a pas conçu |
| Sa contrainte | Choisir sous incertitude | Comprendre sans documentation |
| Son livrable | Une décision et ses justifications | Une compréhension, et des questions |
| Son erreur type | Optimiser une contrainte au détriment des autres | **Juger sans connaître l'histoire** |

**Ce cours forme d'abord le second, puis le premier.** L'ordre n'est pas négociable : on ne peut concevoir que ce qu'on sait lire.

#### 7.2 Ce qu'un lecteur peut décider

Contrairement à une idée répandue, **lire une architecture permet de décider beaucoup**, sans être architecte.

| Décision | Ce que la lecture apporte |
|---|---|
| Où placer un dispositif de sécurité | Les points de passage réels — chapitre 44 |
| Si une vulnérabilité nous concerne | L'exposition du composant affecté |
| Ce qu'on peut isoler pendant un incident | Les dépendances — chapitre 35 |
| Ce qu'on peut arrêter pour une maintenance | Ce qui tombe avec |
| Ce qu'il faut inventorier en priorité | Les points de rupture |
| Si une demande de flux est légitime | Ce qu'elle traverse |
| Ce qu'il faut journaliser | Les points de passage |

**Sept décisions, aucune ne nécessite d'être architecte.** C'est la valeur pratique de ce cours pour la majorité de ses lecteurs.

#### 7.3 Ce que ce cours ne rendra pas capable de faire

Par honnêteté, et pour que la Partie IX soit lue avec les bonnes attentes.

| Hors de portée | Pourquoi |
|---|---|
| Dimensionner une infrastructure | Exige des mesures, des essais, une expérience produit |
| Choisir entre deux produits | Dépend du contexte, des contrats, des compétences |
| Concevoir un système à forte contrainte | Haute disponibilité stricte, temps réel, très grande échelle |
| Garantir qu'une architecture fonctionnera | Seul l'essai le démontre |

**Ce que la Partie IX apporte réellement** :

> Poser les bonnes questions, proposer une architecture justifiée pour un besoin courant, énoncer ses compromis — et identifier ce qu'il reste à vérifier.

⚠️ **Le lecteur qui terminera ce cours en pensant *« je sais concevoir une architecture »* l'aura mal lu.** Celui qui le terminera en pensant *« je sais quoi demander, quoi proposer, et quoi vérifier »* en aura tiré l'essentiel.

#### 7.4 Comment progresser après ce cours

| Étape | Comment |
|---|---|
| **Lire des architectures réelles** | Demander les schémas de votre organisation, et poser les questions du chapitre 36 |
| **Suivre un flux de bout en bout** | Une fois, en vrai, avec l'exploitation. C'est irremplaçable |
| **Assister à une revue d'architecture** | Écouter les arbitrages se faire |
| **Reconstituer une histoire** | Demander à quelqu'un d'ancien pourquoi un composant est là |
| **Dessiner** | Le chapitre 50 en fait un exercice |

**La deuxième ligne est celle qui fait la différence.** Suivre une requête réelle, de la frappe au clavier jusqu'à l'écriture en base, en observant chaque étape, enseigne en une journée ce qu'aucun cours ne transmet.

#### 7.5 🔴 FIL ROUGE — décembre 2025 : la question d'Amélie

Le 19 décembre, Amélie rend compte à Claire Nadeau de ses deux semaines. Elle n'a rien inventorié.

**Ce qu'elle a produit** : une liste de vingt-trois questions, et une observation.

**L'observation** :

> *Le schéma qu'on m'a donné date de mars 2023, il ne mentionne pas le site de Nantes, il ne montre ni les postes, ni la zone d'administration, ni les services en ligne, ni les prestataires. Il n'est pas faux. Il a été fait pour montrer à un client que nous avons une zone démilitarisée.*

**La question qu'elle pose à Claire** :

> *« Est-ce que tu veux que je compte ce qui est sur le schéma, ou que je découvre ce qui existe ? »*

**La réponse de Claire**, qui ouvre le volume suivant :

> *« Les deux. Mais dans cet ordre-là : d'abord comprendre, ensuite compter. Sinon tu vas compter des choses dont tu ne sauras pas si elles comptent. »*

**Ce qui est décidé le 19 décembre** : Amélie consacre janvier à comprendre le système avant de l'inventorier. Sa mission d'inventaire démarre officiellement le 5 janvier 2026.

**Le 11 décembre, Sonia Weber avait demandé** : *« Bon. Combien on en a, alors ? »* — et Claire avait répondu qu'elle ne pouvait pas encore le dire.

**Le 19 décembre, la raison est claire.** Ce n'est pas un problème de comptage. C'est un problème de compréhension, puis de définition.

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> ✓ que **toute architecture est un compromis** entre six contraintes qui se contredisent — et que la sixième, l'histoire, est souvent la plus puissante ;
> ✓ distinguer **trois familles de flux** — métier, dépendance, exploitation — et savoir que la confusion entre les deux dernières fait surdimensionner ce qui n'en a pas besoin ;
> ✓ poser les **quatre questions du lecteur** devant n'importe quel schéma ;
> ✓ que **trois mots** — serveur, application, service — désignent chacun au moins trois choses, et quelle question les désambiguïse ;
> ✓ qu'une **boîte** peut représenter cinq choses et un **trait** cinq autres, et quelles questions poser à chacun ;
> ✓ que quatre **vues** sont nécessaires, et qu'aucune ne ment ;
> ✓ **onze éléments qui ne sont jamais dessinés**, et l'effet de leur absence ;
> ✓ qu'une architecture est un **empilement daté**, et que chaque anomalie a une histoire qu'il faut demander avant de critiquer ;
> ✓ que la **taille ne justifie jamais une brique** — la contrainte, oui ;
> ✓ qu'une **zone** se définit par ce qu'il faut traverser, pas par un trait ;
> ✓ que le **poste utilisateur** est le point de départ de la plupart des flux et le grand absent des schémas ;
> ✓ qu'un schéma est toujours **fait pour quelqu'un**, et qu'il faut savoir pour qui avant de le lire.
>
> **Ce que vous ne savez pas encore** : à quoi servent les composants que vous avez appris à repérer, ce qui se passe quand ils disparaissent, et à partir de quelle contrainte ils deviennent nécessaires. C'est l'objet de la Partie II.

---

## Registre de cohérence — fin de T1 (chapitres 1 à 7)

### Règles verrouillées, et leur application

| Règle | Application en T1 |
|---|---|
| **principe des trois flux — trois familles de flux** | Introduite §1.5, tableau des protocoles §2.4, appliquée §6.4 |
| **R2 — la taille ne justifie pas** | Énoncée §1.6 avec trois formulations interdites, appliquée §4.3 et §6.3 |
| **R3 — profondeur limitée** | §2.2 : liste des notions volontairement exclues |
| **R4 — coût d'une brique** | Principe 9, appliqué §5.1 sur la segmentation |
| **R5 — le schéma porte l'information** | 7 schémas ASCII en 7 chapitres, ratio texte/représentation tenu |

### Termes arrêtés

| Terme retenu | Écarté |
|---|---|
| **Flux métier / de dépendance / d'exploitation** | « flux de contrôle » (trop large — voir principe des trois flux) |
| **Mandataire inverse** / **mandataire sortant** | « proxy » seul (ambigu) |
| **Point de rupture** | « SPOF » (sigle, une seule mention) |
| **Zone démilitarisée** | — (terme conservé, avec réserve §5.2) |
| **Résolution de noms** | « DNS » (cité, non employé comme terme du cours) |
| **Poste d'administration** | « bastion » (terme du terrain) |
| **Sédimentation** | « dette technique » (notion voisine, plus étroite) |

### Renvois émis vers des chapitres non rédigés

§1.1→50 · §1.3→43-45 · §1.5→29-35 · §2.1→35 · §2.3→12, 14, 25, 27 · §3.4→6, 27, 38, 50 · §4.5→volume MCS · §5.2→10, 27, 28 · §6.3→38 · §7.2→35, 44

### État du fil rouge

| Élément | Valeur figée |
|---|---|
| Épisodes | §1.8 (15/12/2025) · §2.6 · §3.7 · §4.6 · §5.5 · §6.6 · §7.5 (19/12/2025) |
| Personnages | Amélie Roux (administratrice système, Nantes, 4 ans d'ancienneté) · Claire Nadeau (RSSI) · Malik Ferhaoui (exploitation) · Sonia Weber (DSI) |
| Chiffres figés | 96 / 71 / 118 serveurs · 620 postes dont 180 nomades · schéma daté de mars 2023 · 3 sites · lien bureautique-industriel créé en 2018 · serveur `HERMES` de 2011 · second exemplaire applicatif refusé en 2021 pour cause de licence · 23 questions produites |
| Dates figées | 15/12/2025 proposition · 19/12/2025 point avec Claire · 05/01/2026 démarrage officiel |
| Raccordement | §7.5 se raccorde au §1.10 du volume Asset Management (réunion du 11/12/2025 et démarrage du 05/01/2026) |
| Prochain épisode | Partie II — les composants, un par un |

### Écarts au plan validé

**Aucun écart de structure.** Deux précisions :

1. **Le mini-lab 1 a été placé au chapitre 2** plutôt qu'au chapitre 3, parce que l'ambiguïté de vocabulaire se travaille avant la lecture de schéma. Le lab 2 est au chapitre 3, le lab 3 au chapitre 6. La numérotation des quinze labs reste conforme.
2. **Le §5.5 introduit un principe de lecture non prévu** — *un schéma est fait pour quelqu'un* — qui prolonge le chapitre 3 et annonce le chapitre 50. À réutiliser en Partie VI.

---

## PARTIE II — Les composants d'infrastructure

> **Format uniforme, dix chapitres courts.** Chacun répond à cinq questions, toujours dans le même ordre :
>
> **① À quoi ça sert** · **② Que se passe-t-il s'il disparaît** · **③ Que fait-il à la donnée** *(principe 6)* · **④ Comment on le reconnaît sur un schéma** · **⑤ ⚖️ Contrainte résolue et coût introduit** *(principe du coût)*
>
> **Ce que cette partie n'enseigne pas** : la configuration, les commandes, le détail des protocoles. *Principe de coupe.*

---

## Préambule — Le socle réseau minimal

> **Pourquoi ce préambule existe.** Les dix chapitres qui suivent supposent quelques notions sans lesquelles on ne peut pas répondre à la question centrale du cours : **qu'est-ce qui rend deux zones joignables ?**
>
> **Application stricte du principe de coupe** : ce qui suit tient en cinq pages. Vous n'y trouverez ni calcul d'adressage, ni protocole de routage, ni commande. Uniquement ce qui permet de comprendre pourquoi un flux passe ou ne passe pas.

### P.1 Deux niveaux d'adressage, et pourquoi il en faut deux

```
   NIVEAU LIAISON        Adresse gravée dans l'interface réseau.
                         Sert à joindre une machine SUR LE MÊME SEGMENT.
                         Ne sort jamais du segment.

   NIVEAU RÉSEAU         Adresse IP, attribuée, modifiable.
                         Sert à joindre une machine N'IMPORTE OÙ.
                         Traverse les routeurs.
```

**Pourquoi deux ?** Parce qu'ils répondent à deux questions différentes : *qui est ici, à côté de moi* et *où se trouve cette machine dans l'ensemble*.

**Ce que cela explique en lecture de schéma** :

| Observation | Explication |
|---|---|
| Un commutateur relie sans routeur | Il travaille au niveau liaison : tout est « à côté » |
| Deux machines ne se joignent pas malgré un câble commun | Elles sont dans des sous-réseaux différents |
| Un routeur est nécessaire entre deux segments | Le niveau liaison ne sort pas du segment |

### P.2 Adresse, sous-réseau, passerelle

**Trois notions, et une seule règle à retenir.**

| Notion | Ce que c'est | À quoi ça sert en lecture |
|---|---|---|
| **Adresse** | L'identifiant d'une machine sur le réseau | Elle change · elle ment · elle est réattribuée |
| **Masque de sous-réseau** | Ce qui définit **jusqu'où s'étend « à côté »** | Il découpe l'espace d'adressage en segments |
| **Passerelle par défaut** | Où envoyer ce qui n'est pas « à côté » | **Sans elle, une machine ne sort pas de son segment** |

> **La règle unique** : une machine regarde si la destination est dans son sous-réseau. **Si oui**, elle la joint directement. **Si non**, elle envoie à sa passerelle, et c'est le routeur qui prend le relais.

🖼 **SCHÉMA P.1 — La décision que prend toute machine**

```
   Machine A veut joindre une destination
                    │
        ┌───────────┴────────────┐
        │  La destination est-elle  │
        │  dans MON sous-réseau ?   │
        └───────────┬────────────┘
             ┌──────┴──────┐
            OUI            NON
             │              │
       joindre         envoyer à
      directement    LA PASSERELLE
             │              │
      commutateur      routeur, puis
      seulement        éventuellement
                       d'autres routeurs
```

⚠️ **Ce que cela explique** : une machine sans passerelle configurée fonctionne parfaitement **à l'intérieur de son segment** et ne joint rien au-delà. C'est un symptôme fréquent, et il ressemble à une panne applicative.

### P.3 Ports et état d'une connexion

| Notion | Ce qu'il faut en savoir |
|---|---|
| **Port** | Un numéro qui identifie **le service** sur une machine. L'adresse dit *où*, le port dit *quoi* |
| **Connexion** | Un échange établi entre deux couples adresse-port, avec un état : en cours d'établissement, établie, fermée |
| **Sens d'établissement** | **Qui a initié.** C'est ce qui distingue un flux entrant d'un flux sortant |

> **La notion la plus utile du préambule** : un pare-feu qui autorise un flux **sortant** laisse revenir les réponses de ce flux, parce qu'il **suit l'état des connexions**. C'est pourquoi *« autoriser vers Internet »* ne signifie pas *« autoriser depuis Internet »*.

⚠️ **Ce que cela change en lecture** : sur un schéma, une flèche sans sens est ambiguë — §3.2. **Le sens d'établissement est l'information la plus déterminante d'un flux**, et c'est celle qui manque le plus souvent.

### P.4 Traduction d'adresses

**Un mécanisme omniprésent dans les architectures réelles, et quasi absent des schémas.**

**Le problème qu'il résout** : les adresses employées à l'intérieur d'une organisation ne sont pas utilisables directement sur Internet. Il faut donc les traduire au passage.

🖼 **SCHÉMA P.2 — Les deux traductions**

```
  SORTANTE — plusieurs machines internes derrière une adresse publique

     10.0.4.23 ──┐
     10.0.4.24 ──┼──► [ traduction ] ──► 203.0.113.7 ──► Internet
     10.0.4.25 ──┘
     → Vu de l'extérieur, les trois machines ont LA MÊME adresse.

  ENTRANTE — une adresse publique redirigée vers une machine interne

     Internet ──► 203.0.113.7:443 ──► [ traduction ] ──► 10.0.4.80:8443
     → C'est ainsi qu'un service interne devient joignable de l'extérieur.
```

**Les quatre conséquences en lecture**, et elles comptent toutes :

| Conséquence | Où elle se manifeste |
|---|---|
| **L'adresse observée n'est pas celle de la machine d'origine** | Journaux d'un serveur derrière une traduction · investigation |
| Plusieurs machines partagent une adresse vue de l'extérieur | Blocage d'une adresse : on bloque tout le monde |
| Un service exposé n'est pas à l'adresse qu'on croit | Publication, pare-feu |
| **Un composant intermédiaire peut aussi masquer l'origine** | Mandataire inverse, répartiteur de charge — §34.1 |

⚠️ **La première ligne est la plus lourde de conséquences.** Elle explique pourquoi corréler un journal applicatif avec un utilisateur réel est difficile — §34.1 — et pourquoi une adresse dans un journal n'identifie pas une machine sans information complémentaire.

### P.5 Deux familles d'adressage

📌 **Ce qu'il faut savoir, et rien de plus** :

| | **IPv4** | **IPv6** |
|---|---|---|
| Espace d'adressage | Limité — d'où la traduction d'adresses | Très vaste |
| Traduction d'adresses | **Structurante** : la quasi-totalité des réseaux internes en dépend | **Généralement inutile** — les machines peuvent avoir une adresse routable |
| Conséquence en lecture | L'adresse observée n'est souvent pas l'origine | **L'adresse observée peut être celle de la machine** |
| Présence | Partout | Croissante, souvent en parallèle du premier |

⚠️ **Pourquoi cela figure dans ce cours** : le modèle mental *« adresse interne + traduction »* que nous employons dans tout le volume **n'est pas universel**. Une machine peut disposer simultanément des deux familles — c'est la double pile — et suivre alors **deux chemins différents selon la famille employée**.

**La question de lecture qui en découle** : *ce schéma décrit-il un adressage, ou les deux ?* Dans la majorité des schémas, la question n'est pas tranchée — et un flux peut passer dans une famille et être bloqué dans l'autre.

### P.6 Ce que ce préambule permet de faire

☐ Expliquer pourquoi deux machines d'un même segment se joignent sans routeur
☐ Expliquer pourquoi une machine sans passerelle ne sort pas de son segment
☐ Distinguer le sens d'établissement d'un flux, et savoir pourquoi il détermine tout
☐ Comprendre pourquoi une adresse dans un journal n'identifie pas une machine
☐ Savoir qu'un service exposé n'est pas nécessairement à l'adresse annoncée
☐ Savoir que le modèle « adresse interne + traduction » n'est pas universel

**Ce qu'il ne permet pas, volontairement** : dimensionner un plan d'adressage, choisir un protocole de routage, configurer quoi que ce soit — *principe de coupe*.

---

### Chapitre 8 — Le commutateur

#### 8.1 À quoi ça sert

Relier des machines à l'intérieur d'un même segment, et acheminer les échanges de l'une à l'autre **sans les diffuser à toutes**.

**Pourquoi ça existe.** Avant le commutateur, les machines partageaient un même support : chacune voyait tout ce qui passait, et deux machines qui émettaient en même temps se gênaient. Le commutateur résout les deux problèmes d'un coup — il apprend quelle machine est derrière quel port, et n'envoie qu'à la bonne.

**Ce qu'il faut en retenir pour raisonner**, et rien de plus :

> **Un commutateur crée un espace où les machines se joignent directement. Il ne crée aucune frontière de filtrage.**

#### 8.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Une trame arrive sur le port 3
   ②  Le commutateur note : « cette machine est derrière le port 3 »
   ③  Il regarde la destination
        ├── il sait où elle est  ──► il envoie sur ce port UNIQUEMENT
        └── il ne sait pas       ──► il envoie sur TOUS les ports
   ④  La réponse lui apprend où se trouve la destination
```

**Trois conséquences en lecture d'architecture** :

| Mécanisme | Conséquence |
|---|---|
| Il **apprend** les emplacements | Une machine déplacée est retrouvée automatiquement |
| Il **diffuse** ce qu'il ne connaît pas | Un segment très large produit du trafic inutile partout |
| Il **ne filtre pas** | Deux machines du même segment se joignent, sauf mécanisme dédié — §24.1 |

#### 8.3 Les segments logiques

**Le mécanisme qui change tout, et qu'aucun schéma logique ne montre** : un même commutateur physique peut porter plusieurs segments logiques indépendants. Deux machines branchées côte à côte dans la même baie peuvent être **aussi séparées que si elles étaient dans deux bâtiments**.

```
   UN SEUL COMMUTATEUR PHYSIQUE

   ports 1-8    ─── segment « postes »      ┐
   ports 9-16   ─── segment « serveurs »    ├─ trois segments,
   ports 17-24  ─── segment « supervision » ┘  aucun ne voit les autres

   Pour qu'ils communiquent : il faut un ROUTEUR.
```

⚠️ **Ce que cela impose en lecture** : un schéma physique qui montre un seul commutateur peut décrire une architecture **logiquement segmentée**. Et l'inverse : deux commutateurs dessinés séparément peuvent porter **le même segment**. **La question à poser : combien de segments, et non combien d'équipements.**

#### 8.4 Trois architectures, trois usages

```
  A — COMMUTATEUR UNIQUE
      [ commutateur ] ─── 20 machines
      → simple · une panne = tout le site
      → convient quand l'interruption tolérable est large

  B — DEUX COMMUTATEURS EN CASCADE
      [ cœur ] ─── [ étage 1 ]
              └─── [ étage 2 ]
      → une panne d'étage n'affecte qu'un étage
      → une panne du cœur affecte tout · le cœur est le point de rupture

  C — CŒUR REDONDÉ
      [ cœur A ] ══╗
                   ╠═══ [ étage 1 ] [ étage 2 ]
      [ cœur B ] ══╝
      → une panne de cœur est absorbée
      → deux équipements à configurer de façon cohérente
      → ⚠️ **Principe de preuve** : sont-ils sur la même alimentation ?
```

**La contrainte qui fait passer de A à C** n'est pas le nombre de machines : c'est **la durée d'interruption tolérable comparée au délai de remplacement d'un équipement**. Si remplacer prend quatre heures et qu'une journée d'arrêt est acceptable, A suffit.

#### 8.5 Ce qu'il fait à la donnée

Il la transporte. Pour accomplir sa fonction, il interprète les informations d'adressage de niveau liaison — **sans avoir besoin d'interpréter le contenu applicatif**. Il voit passer ce qui traverse le segment, ce qui en fait un point d'observation possible — chapitre 43.

#### 8.6 S'il disparaît

| Ce qui tombe | Délai | Compréhensible pour l'utilisateur ? |
|---|---|---|
| Tout ce qui y est raccordé | Immédiat | ✅ « plus de réseau ici » |

**C'est la panne la plus localisée et la plus totale du cours** : un segment entier disparaît, et le reste du système ne s'en aperçoit pas — **sauf s'il en dépend**.

🔥 **SCÉNARIO — le commutateur de l'étage tombe**

| Question | Réponse |
|---|---|
| Symptôme observé | Quarante personnes sans réseau, le reste du site fonctionne |
| Hypothèse naïve | « Panne réseau générale » |
| Dépendance réelle | Ces quarante postes · **et tout service hébergé sur ce segment** |
| Ce que le schéma aurait dû montrer | Quels serveurs sont sur ce segment |
| Concevoir différemment | Ne pas mélanger postes et serveurs sur un même segment |

#### 8.7 Sur un schéma

Souvent absent. Quand il figure, c'est sur une vue physique. Sur une vue logique, il est **implicite** : deux machines dessinées dans la même zone sont supposées reliées.

⚠️ **Le piège de lecture** : l'absence de commutateur ne signifie pas qu'il n'y en a pas — elle signifie que la vue ne s'y intéresse pas. **La question « qui peut joindre qui à l'intérieur d'une zone » reste ouverte**, et la réponse par défaut est « tout le monde ».

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut probablement dire | À vérifier avant de le croire |
|---|---|---|
| « C'est sur le même switch » | Les machines sont sur le même segment | **Même équipement ≠ même segment.** Combien de segments logiques ? |
| « On a mis un VLAN » | Un segment logique a été créé | Le routage entre segments est-il filtré, ou juste routé ? |
| « Le cœur de réseau » | Le commutateur central | Est-il redondé ? Les deux exemplaires partagent-ils l'alimentation ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Relier des machines proches efficacement | Un équipement à alimenter, corriger, surveiller |
| Segmenter logiquement sans recâbler | **Une configuration à maintenir, souvent non documentée** |
| Redonder le cœur | Deux configurations à tenir cohérentes · un mécanisme de bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : 2, dont un pour l'atelier. HELIOMED : une trentaine, dont deux en cœur redondé. Novaris : plusieurs centaines. **La contrainte qui fait passer de 2 à 30 n'est pas le nombre de salariés, c'est le nombre de bâtiments et de segments à isoler.**

---

### Chapitre 9 — Le routeur

#### 9.1 À quoi ça sert

Faire communiquer des segments différents. Sans lui, deux segments coexistent sans se voir.

**Pourquoi ça existe.** Le niveau liaison ne sort pas du segment — §P.1. Dès qu'on découpe un réseau en plusieurs segments, il faut un composant capable de faire passer un échange de l'un à l'autre : c'est le routeur.

> **La formule qui distingue routeur et pare-feu, et qu'il faut retenir** :
> **Le routeur dit *où* ça va. Le pare-feu dit *si* ça a le droit.**

#### 9.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Un paquet arrive, avec une adresse de destination
   ②  Le routeur consulte sa table :
         « pour atteindre 10.0.7.0/24, envoyer vers l'interface 2 »
   ③  Il modifie certains champs de transit
   ④  Il transmet
   ⑤  Le routeur suivant recommence
```

**Ce qui compte en architecture, et rien de plus** :

| Notion | Pourquoi elle compte en lecture |
|---|---|
| **Table de routage** | Elle décide du chemin. **Une entrée manquante rend une zone injoignable sans qu'aucun filtre ne l'interdise** |
| **Route par défaut** | Où va ce qui n'est pas connu. Généralement vers Internet |
| **Chemin asymétrique** | L'aller et le retour peuvent emprunter des routes différentes — **c'est ce qui casse certains pare-feu à état** |

⚠️ **La troisième ligne explique une famille entière d'incidents.** Un pare-feu qui suit l'état des connexions doit voir l'aller **et** le retour. Si le retour passe ailleurs, il refuse un trafic pourtant légitime — et le diagnostic est difficile parce que la configuration paraît correcte.

🔭 **À RECONNAÎTRE — BGP**

**① Qu'est-ce que c'est.** Un protocole qui permet à des systèmes de routage indépendants d'**échanger des informations de joignabilité** et d'appliquer des **politiques** sur les chemins retenus.

**② Quel problème il résout.** À grande échelle, on ne maintient pas à la main *« pour joindre ce réseau, passer par ce routeur »*. Et surtout : quand plusieurs chemins existent, **il faut pouvoir choisir selon d'autres critères que la distance** — un contrat, un coût, une préférence, une politique.

**③ Où on le rencontre.**

```
                    Entreprise
                        │
              ┌─────────┴─────────┐
              │                   │
          [ FAI A ]           [ FAI B ]
              │                   │
              └──── Internet ─────┘
```

| Contexte | Pourquoi BGP apparaît |
|---|---|
| **Deux fournisseurs d'accès** | Annoncer ses adresses aux deux, et choisir par où sortir et entrer |
| Interconnexion avec un opérateur | Échanger les réseaux joignables de part et d'autre |
| Grands centres de données | Routage interne à grande échelle |
| Liaison privée vers un fournisseur cloud | L'échange de routes se fait fréquemment ainsi |

**④ Ce que cela change.** Le chemin **n'est plus déterminé par votre seule configuration** : il résulte d'un échange avec des systèmes que vous ne contrôlez pas. Une annonce mal formée peut rendre une plage d'adresses injoignable — ou détourner du trafic.

> ⚠️ **Le point qui compte en architecture** : *BGP ne demande pas simplement quel chemin est le plus court. Les politiques comptent, et elles sont décidées de part et d'autre.*

**⑤ Le coût.** Une compétence rare · une configuration dont une erreur a des effets externes visibles · **une dépendance à ce que le partenaire annonce**.

**⑥ Le vocabulaire à reconnaître** : **ASN** — le numéro qui identifie un système autonome · **préfixe** — une plage d'adresses annoncée · **annonce de route** · **peering** — l'accord d'échange entre deux systèmes.

🗣 **En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est en BGP avec les deux opérateurs » | **Multi-hébergement.** Que se passe-t-il si l'un tombe ? La bascule a-t-elle été testée ? |
| « On annonce notre préfixe » | Vos adresses sont visibles depuis Internet par ce chemin. **Qui peut modifier cette annonce ?** |
| « Ils ne nous annoncent plus la route » | Une destination est devenue injoignable **sans qu'aucun équipement ne soit en panne** |

📚 **À approfondir ailleurs** : les attributs de sélection de chemin, la sécurisation des annonces, la conception d'un routage de centre de données.

#### 9.3 Trois architectures de routage

```
  A — ROUTEUR UNIQUE, ROUTE PAR DÉFAUT
      segments internes ──► [ routeur ] ──► Internet
      → simple · tout passe par un point · un point de rupture

  B — ROUTAGE INTERNE + SORTIE SÉPARÉE
      segments ──► [ routeur interne ] ──► [ pare-feu ] ──► Internet
      → le routage interne survit à une panne de la sortie
      → deux équipements, deux configurations

  C — MULTI-SITES
      site A ──► [ routeur A ] ══lien══ [ routeur B ] ◄── site B
                       └────► Internet          └────► Internet
      → chaque site sort localement, et joint l'autre par le lien
      → si le lien tombe, chaque site reste autonome pour Internet
      → mais pas pour les services hébergés dans l'autre site — §26
```

**La contrainte qui décide entre B et C** : *un site doit-il continuer à fonctionner si le lien vers le siège tombe ?* — et la réponse est presque toujours partielle, §26.1.

#### 9.4 Ce qu'il fait à la donnée

Il l'achemine. Pour décider du chemin, il interprète les informations d'adressage réseau, et il modifie certains champs au passage — c'est le mécanisme normal du transit. **Il n'a pas besoin d'interpréter le contenu applicatif**, ce qui en fait un point de contrôle sur les trajets, pas sur les contenus.

#### 9.5 S'il disparaît

Les segments deviennent des îlots. Chacun fonctionne, aucun ne se parle.

🔥 **SCÉNARIO — le routeur inter-sites tombe**

| Question | Réponse |
|---|---|
| Symptôme | Les postes de Nantes n'atteignent plus les serveurs de Lyon. Internet fonctionne à Nantes |
| Hypothèse naïve | « Les serveurs de Lyon sont tombés » |
| Dépendance réelle | Le lien · **et tout ce qui est centralisé à Lyon** : annuaire, applications, fichiers |
| Ce que le schéma aurait dû montrer | **Ce qui est local à Nantes, et ce qui ne l'est pas** — §26.2 |
| Concevoir différemment | Un contrôleur d'annuaire et une résolution de noms locaux |

⚠️ **C'est une panne qui *ressemble* à une panne applicative** : les machines répondent, mais pas à travers les segments. C'est l'un des cas où le diagnostic est le plus souvent orienté au mauvais endroit.

#### 9.6 Sur un schéma

Représenté à la jonction de deux zones ou de deux sites. **Souvent fusionné avec le pare-feu** dans les petites organisations — un seul boîtier fait les deux, ce que le schéma ne dit pas.

⚠️ **Ce que cette fusion masque** : la question *« ce flux est-il permis, ou seulement possible ? »* — §3.2. Quand routeur et pare-feu sont un seul objet sur le schéma, on ne sait pas si un flux passe parce qu'il est autorisé ou parce que personne n'a écrit de règle.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est routé » | Un chemin existe entre les deux | **Routé ne veut pas dire autorisé.** Y a-t-il un filtre sur ce chemin ? |
| « Il n'y a pas de route » | La table ne connaît pas la destination | Est-ce un oubli, ou une décision ? |
| « Ça passe par le WAN » | Le trafic emprunte le lien inter-sites | Quelle latence ? Que se passe-t-il si le lien tombe ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Faire communiquer des segments séparés | Un point de passage supplémentaire à sécuriser |
| Choisir des chemins, en gérer plusieurs | Une configuration de routage à maintenir · **un diagnostic plus difficile** |
| Sortir localement par site | Autant de sorties à surveiller — §11 |

---

### Chapitre 10 — Le pare-feu

> **Le composant le plus dessiné du cours, et celui dont le schéma dit le moins.**

#### 10.1 À quoi ça sert

Autoriser ou refuser un flux entre deux zones, selon des règles.

**Pourquoi ça existe.** Un routeur fait passer tout ce qui est routable. Dès qu'on veut que certaines choses passent et d'autres non, il faut un composant qui décide — et qui garde une trace de sa décision.

#### 10.2 Comment il fonctionne, juste assez pour raisonner

**Trois générations coexistent**, et elles ne voient pas la même chose :

| Génération | Ce qu'elle examine | Ce qu'elle ne voit pas |
|---|---|---|
| **Filtrage simple** | Adresses, ports, sens | Si le flux correspond vraiment au service annoncé |
| **Suivi d'état** | Les mêmes, **plus l'état de la connexion** | Le contenu |
| **Inspection applicative** | Le contenu, si le flux n'est pas chiffré **ou s'il est déchiffré** | Ce qui reste chiffré de bout en bout |

> **La notion la plus utile : le suivi d'état.** Un pare-feu qui suit l'état sait qu'une réponse appartient à une connexion qu'il a déjà autorisée. **C'est pourquoi autoriser un flux sortant ne signifie pas autoriser un flux entrant** — §P.3.

🖼 **SCHÉMA 10.1 — Ce que le suivi d'état change**

```
  SANS SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     règle 2 : autoriser Internet → interne, ports 1024-65535
                                    ▲
                        il faut ouvrir le retour EN GRAND

  AVEC SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     (les réponses reviennent automatiquement)
                                    ▲
                        aucune règle entrante nécessaire
```

⚠️ **Ce que cela explique en lecture** : un jeu de règles qui autorise de larges plages entrantes signale souvent un équipement ancien, ou une configuration héritée d'une époque où le suivi d'état n'existait pas. **C'est un signe de strate** — §4.2.

#### 10.3 Le même composant, trois placements différents

**C'est en variant le placement qu'on comprend la fonction.**

```
  A — PARE-FEU UNIQUE, EN COUPURE
      Internet ──► [ FW ] ──► serveur
      → une seule frontière · le serveur est derrière un filtre
      → contourné ou compromis : plus rien ne protège

  B — DEUX PARE-FEU, ZONE INTERMÉDIAIRE
      Internet ──► [ FW-1 ] ──► DMZ ──► [ FW-2 ] ──► interne
      → deux frontières · un composant compromis en DMZ ne suffit pas
      → deux jeux de règles à maintenir, souvent deux constructeurs

  C — SERVICE EN LIGNE ET LIEN PRIVÉ
      Internet ──► [ service du fournisseur ]
                            │  lien privé
                            ▼
                     [ réseau interne ]
      → la frontière côté Internet ne vous appartient plus
      → le pare-feu ne protège plus que le lien privé
```

| Placement | Ce que le pare-feu protège | Ce qu'il ne protège pas |
|---|---|---|
| **A** | Le serveur, contre l'extérieur | Rien à l'intérieur · rien s'il est contourné |
| **B** | L'interne, même si la DMZ tombe | Les échanges au sein de chaque zone |
| **C** | Le lien privé | **Tout ce qui se passe côté fournisseur** |

**Les six questions à poser devant tout pare-feu sur un schéma** :

```
1. Quelle frontière matérialise-t-il exactement ?
2. Qu'est-ce qui le contourne ? (un lien direct, une machine à deux interfaces)
3. Combien de règles, et depuis quand ont-elles été revues ?
4. Qui l'administre, et depuis où ?  ← §27
5. Que se passe-t-il s'il tombe ?
6. Que signifie « paire redondée » ici ?  ← §10.5
```

⚠️ **La question 3 est celle qui révèle le plus.** Un pare-feu dont les règles n'ont pas été revues depuis six ans autorise probablement des flux dont personne ne connaît plus l'usage. **Une règle ne se supprime jamais spontanément** — chaque projet en ajoute, aucun n'en retire.

#### 10.4 Ce qu'il fait à la donnée

Selon sa génération : il regarde les extrémités et les ports, ou il inspecte le contenu applicatif, ou il déchiffre pour inspecter — auquel cas **il voit tout en clair**, ce qui en fait un actif extrêmement sensible.

#### 10.5 « Paire redondée » : ce que cela signifie réellement

**Deux pare-feu côte à côte sur un schéma peuvent décrire trois choses différentes.**

| Mode | Comportement | Ce que ça protège |
|---|---|---|
| **Actif / passif** | Le second attend. Il prend le relais si le premier tombe | Une panne matérielle · **pas une erreur de configuration, qui est répliquée** |
| **Actif / actif** | Les deux traitent du trafic | Une panne matérielle, et la charge |
| **En série** | Deux barrières successives, souvent de constructeurs différents | Une faille propre à un constructeur |

⚠️ **Principe de preuve, appliqué au pare-feu** — ce qu'une paire ne protège pas :

| Ce qui reste partagé | Conséquence |
|---|---|
| **La configuration** | Une règle erronée est répliquée sur les deux |
| **La version logicielle** | Une vulnérabilité les affecte tous les deux |
| **L'alimentation, la baie, le site** | Un incident physique les emporte ensemble |
| **L'administrateur** | Une erreur humaine s'applique aux deux |

> **Une paire redondée protège contre la panne d'un équipement. Elle ne protège contre à peu près rien d'autre.**

#### 10.6 S'il disparaît

**Trois cas opposés, et c'est ce qui rend ce composant intéressant** :

| Configuration | S'il tombe | Ce que ça révèle |
|---|---|---|
| En coupure, sans contournement | **Plus rien ne passe.** Le service s'arrête | La frontière était réelle |
| En redondance | Le second prend le relais | Si la bascule fonctionne — *principe de preuve* |
| **Contourné par un chemin oublié** | **Rien ne change** | **La frontière était fictive** |

🔥 **SCÉNARIO — le pare-feu tombe et rien ne se passe**

| Question | Réponse |
|---|---|
| Symptôme | Un pare-feu est arrêté pour maintenance. **Aucun utilisateur ne signale quoi que ce soit** |
| Hypothèse naïve | « La bascule a fonctionné » |
| Dépendance réelle | **Peut-être aucune** : le trafic passait peut-être déjà ailleurs |
| Ce que le schéma aurait dû montrer | Tous les chemins entre les deux zones, pas seulement celui-ci |
| Ce qu'il faut vérifier | Le compteur de sessions du pare-feu passif : **a-t-il vraiment repris le trafic ?** |

⚠️ **C'est l'un des tests les plus instructifs qu'on puisse faire sur une architecture** : arrêter un composant en fenêtre planifiée et regarder si quelque chose change. Quand rien ne change, ce n'est pas toujours une bonne nouvelle.

#### 10.7 Sur un schéma

Presque toujours dessiné, presque toujours à une frontière. **Deux pare-feu côte à côte** signalent une redondance ; **deux pare-feu en série** signalent une double barrière.

⚠️ **Le piège de lecture le plus fréquent du cours** : un pare-feu dessiné ne dit rien de ses règles. Une frontière peut être matérialisée par un équipement dont la règle est *« tout autoriser »*.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans la DMZ » | Le composant est publié | **Y a-t-il une seconde frontière ?** — §25.1 |
| « On a une paire HA » | Deux pare-feu redondés | Actif/passif ou actif/actif ? La bascule a-t-elle été testée ? |
| « Le flux est ouvert » | Une règle autorise ce trafic | Dans quel sens ? Depuis quand ? Qui l'a demandée ? |
| « On va mettre une règle any-any en attendant » | Autoriser tout, temporairement | **« En attendant » dure en moyenne plusieurs années** — §4.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Contrôler ce qui traverse une frontière | **Un ensemble de règles qui ne fait que croître** |
| Tracer les flux refusés | Un volume de journaux considérable |
| Inspecter le contenu | Une latence · un déchiffrement à opérer · **un point où tout passe en clair** |
| Redonder | Deux équipements, et une bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : un boîtier tout-en-un qui fait routeur, pare-feu et accès distant. HELIOMED : deux en redondance. Novaris : plusieurs dizaines. **La contrainte qui les multiplie est le nombre de frontières à contrôler, pas la taille.**

---

### Chapitre 11 — Le mandataire sortant

#### 11.1 À quoi ça sert

Concentrer les accès des postes internes vers l'extérieur, en un point unique où l'on peut filtrer, journaliser et authentifier.

**Pourquoi ça existe.** Sans lui, six cents postes sortent chacun de leur côté à travers le pare-feu. On peut filtrer par adresse et par port — mais pas savoir *quel site* a été consulté, ni *par qui*, ni bloquer une catégorie de destinations. Le mandataire déplace le point de décision du niveau réseau au niveau applicatif.

#### 11.2 Comment il fonctionne, juste assez pour raisonner

```
   SANS MANDATAIRE
      poste ──────────────────────► Internet
      Le pare-feu voit : une adresse interne, une adresse externe, un port.

   AVEC MANDATAIRE
      poste ──► [ mandataire ] ──► Internet
                      │
                      ├── il connaît L'UTILISATEUR (authentification)
                      ├── il connaît LA DESTINATION demandée
                      ├── il peut refuser selon une catégorie
                      └── il journalise les deux
```

**Deux modes de mise en œuvre**, et ils ne produisent pas le même résultat :

| Mode | Comment | Ce qui change |
|---|---|---|
| **Déclaré** | Le poste est configuré pour l'utiliser | **Contournable** : un logiciel qui ignore la configuration sort directement, si le pare-feu le permet |
| **Imposé** | Le trafic est redirigé sans que le poste le sache | Non contournable, mais certains protocoles s'en accommodent mal |

⚠️ **La différence est décisive en lecture.** Un mandataire déclaré protège les usages **coopératifs**. Il ne protège pas contre un logiciel malveillant, qui n'a aucune raison de respecter la configuration du navigateur. **La question à poser : le pare-feu autorise-t-il une sortie directe, ou tout doit-il passer par le mandataire ?**

#### 11.3 Deux architectures de sortie

```
  A — SORTIE CENTRALISÉE
      postes site A ──┐
      postes site B ──┼──► [ mandataire siège ] ──► Internet
      postes site C ──┘
      → un point de contrôle et de journalisation unique
      → un point de rupture pour tout accès Internet
      → depuis un site distant : le trafic remonte au siège, latence
      → si le lien inter-sites tombe : plus d'Internet sur le site

  B — SORTIE LOCALE PAR SITE
      postes site A ──► [ mandataire local ] ──► Internet
      postes site B ──► [ mandataire local ] ──► Internet
      → moins de latence, pas de dépendance au lien inter-sites
      → autant de points de contrôle à maintenir et à surveiller
      → journalisation répartie : la corréler devient un travail
```

**La contrainte qui décide** : *le site doit-il continuer à accéder à Internet si le lien vers le siège tombe ?*

⚠️ **Un troisième cas, de plus en plus fréquent** : les postes nomades. **Hors des murs, ils ne passent par aucun mandataire** — sauf si un tunnel les y ramène. Une organisation avec un tiers de postes nomades a donc, en pratique, **deux politiques de sortie différentes** : une pour les postes internes, une pour les nomades. Le schéma n'en montre qu'une.

#### 11.4 Ce qu'il fait à la donnée

Il voit **toutes les destinations** consultées depuis l'organisation, et selon sa configuration, le contenu. C'est une source de journaux particulièrement riche sur le comportement des postes — chapitre 34.

📌 **Et c'est un point sensible en soi** : le journal d'un mandataire contient l'historique de navigation de chaque salarié, nominativement. Sa conservation et son accès relèvent d'obligations qui dépassent le cadre de ce cours.

#### 11.5 S'il disparaît

**Plus aucun poste n'accède à Internet** — alors que le réseau fonctionne parfaitement.

🔥 **SCÉNARIO — « j'ai du réseau mais pas Internet »**

| Question | Réponse |
|---|---|
| Symptôme | Les postes joignent les serveurs internes. Aucun site externe ne s'ouvre |
| Hypothèse naïve | « Le lien Internet est coupé » |
| Dépendance réelle | Le mandataire · **et la résolution de noms, si elle est faite par lui** |
| Ce que le schéma aurait dû montrer | Que la sortie Internet est **applicative**, pas seulement réseau |
| Comment vérifier en trente secondes | Depuis un poste : tenter une connexion directe vers une adresse externe. Si elle passe, le réseau va bien |

⚠️ **C'est l'une des pannes les plus déroutantes pour un utilisateur**, parce que tous les symptômes qu'il connaît — « le réseau » — sont normaux.

#### 11.6 Sur un schéma

Entre le réseau interne et la bordure. **Souvent absent des schémas centrés sur les serveurs**, parce qu'il concerne les postes — chapitre 6.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça sort par le proxy » | Le flux passe par le mandataire sortant | Déclaré ou imposé ? **Une sortie directe est-elle possible ?** |
| « Il faut l'autoriser dans le proxy » | Ajouter une destination à la liste | Qui décide ? Combien d'exceptions existent déjà ? |
| « On a bypassé le proxy pour ce serveur » | Une exception a été créée | **Depuis quand ? Est-elle encore justifiée ?** — §4.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Contrôler et tracer les accès sortants | **Un point de rupture pour tout accès Internet** |
| Filtrer les destinations | Une liste à maintenir · des faux blocages · **des contournements si trop strict** |
| Authentifier les accès sortants | Une dépendance à l'annuaire |
| Journaliser la navigation | Un volume important, et des données nominatives à encadrer |

⚠️ **La ligne du filtrage illustre le principe du coût** : filtrer les destinations résout une contrainte réelle, et produit des contournements si le filtrage devient pénible — quelqu'un finira par ouvrir un accès direct « pour tester ». **Ajouter n'est jamais gratuit.**

🏭 **TROIS TAILLES** — Atelier Martin : **aucun mandataire**, sortie directe filtrée par le boîtier tout-en-un. HELIOMED : un mandataire au siège, sortie centralisée. Novaris : sortie locale par site, **parce que quarante sites qui remontent leur trafic au siège saturent les liens et ajoutent une latence inacceptable**.

---

### Chapitre 12 — Le mandataire inverse

> **Le composant que ce cours voit le plus souvent mal compris**, et celui dont le nom trompe le plus.

#### 12.1 À quoi ça sert

Recevoir les demandes venues de l'extérieur **à la place** des serveurs internes, et les relayer. L'extérieur ne parle jamais au serveur : il parle au mandataire.

🖼 **SCHÉMA 12.1 — Ce que le mandataire inverse change**

```
  SANS                Internet ──────────────► [ serveur web ]
                      Le serveur est joignable directement.
                      Son adresse est publique. Sa version est visible.
                      Une faille du serveur est directement exploitable.

  AVEC                Internet ──► [ mandataire ] ──► [ serveur web ]
                      Le serveur n'est joignable que par le mandataire.
                      L'extérieur ne connaît que l'adresse du mandataire.
                      Une faille du serveur exige d'abord de passer le mandataire.
```

#### 12.2 Les quatre fonctions qu'il assure réellement

**On croit qu'il en a une. Il en a quatre, et elles s'ajoutent progressivement dans une architecture.**

| # | Fonction | Ce qu'elle apporte | Quand elle apparaît |
|---|---|---|---|
| **1** | **Masquer** | Le serveur n'est pas exposé directement | Dès qu'un service est publié |
| **2** | **Terminer le chiffrement** | Un seul point où gérer les certificats | Dès qu'il y a plus d'un serveur |
| **3** | **Authentifier** | On prouve son identité **avant** d'atteindre l'application | **Souvent sa vraie raison d'être** |
| **4** | **Router selon le contenu** | Un même point d'entrée pour plusieurs applications | Quand les applications se multiplient |

⚠️ **La fonction 3 est celle qu'on oublie et qui compte le plus.** Placer l'authentification devant l'application signifie qu'une faille de l'application **n'est pas atteignable par un anonyme**. C'est un changement de nature, pas un raffinement.

#### 12.3 Ce qu'il fait à la donnée

Cela dépend du mode de terminaison retenu. **Dans le modèle employé dans ce cours, le mandataire termine le chiffrement** : il lit le contenu, parfois le modifie — en-têtes, cache, compression — et le rechiffre ou non vers le serveur. **C'est alors un point où le contenu est en clair**, donc un point d'observation et un point de risque.

⚠️ **Ce n'est pas une propriété obligatoire d'un mandataire inverse.** Un mandataire peut relayer un flux chiffré sans le terminer ; il ne voit alors que les extrémités.

🖼 **SCHÉMA 12.2 — Les trois modes de terminaison du chiffrement**

```
  A — TERMINAISON AU SERVEUR  (« passthrough »)
      client ══chiffré══════════════════════════► serveur
      Le mandataire relaie sans ouvrir.
      → aucune inspection possible · aucun contrôle applicatif
      → aucune authentification préalable possible
      → le certificat est géré sur chaque serveur

  B — TERMINAISON AU MANDATAIRE, PUIS CLAIR
      client ══chiffré══► [ mandataire ] ──clair──► serveur
      → inspection et authentification possibles
      → le trafic interne circule en clair
      → un seul certificat à gérer

  C — TERMINAISON PUIS RECHIFFREMENT
      client ══chiffré══► [ mandataire ] ══chiffré══► serveur
      → inspection ET trafic interne protégé
      → deux jeux de certificats à gérer
      → charge de chiffrement doublée
```

| Mode | Voit le contenu | Trafic interne protégé | Authentification possible | Coût |
|---|---|---|---|---|
| **A** | ❌ | ✅ | ❌ | Certificats sur chaque serveur |
| **B** | ✅ | ❌ | ✅ | Le plus simple, et le plus courant |
| **C** | ✅ | ✅ | ✅ | Deux gestions de certificats, charge doublée |

**Ce que le mode change en lecture** : la question *« qui voit le contenu en clair ? »* n'a pas la même réponse selon les trois — et **aucun schéma ne le dit**. C'est une question à poser.

⚠️ **La conséquence en sécurité, souvent mal comprise** : en mode B, le trafic entre le mandataire et le serveur est en clair **sur votre réseau interne**. Ce n'est un problème que si ce réseau n'est pas maîtrisé — c'est un arbitrage, pas une faute.

🔭 **À RECONNAÎTRE — WAF**

**① Qu'est-ce que c'est.** Un dispositif qui **analyse et filtre le trafic web applicatif** selon des règles de sécurité — contenu des requêtes, paramètres, en-têtes.

**② Quel problème il résout.** Un pare-feu réseau décide si un flux passe ; il ne regarde pas *ce que la requête demande*. Un mandataire inverse relaie ; il ne juge pas le contenu. **Le WAF comble cet écart.**

**③ Les trois se distinguent, et se confondent en pratique** :

| | **Pare-feu** | **Mandataire inverse** | **WAF** |
|---|---|---|---|
| Décide selon | Adresses, ports, état | Le chemin, le nom demandé | **Le contenu applicatif de la requête** |
| Question posée | *Ce flux a-t-il le droit de passer ?* | *Quel serveur doit répondre ?* | *Cette requête est-elle légitime ?* |
| Voit le contenu | Selon la génération | Si le chiffrement y est terminé | **Nécessairement** |

⚠️ **Les trois peuvent être trois équipements, un seul équipement, ou un service en ligne.** Sur un schéma, une même boîte peut porter les trois — et rien ne le dit.

**④ Ce que cela change.** Le WAF **doit voir le contenu en clair**, donc il impose le mode B ou C du §12.3. Il devient un point où tout le trafic web est lisible.

**⑤ Le coût.** Des faux blocages qui cassent des usages légitimes · un réglage long, souvent en mode observation pendant des semaines · une latence · **un composant de plus sur le chemin critique**.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un WAF devant » | **En mode blocage ou en mode observation ?** Beaucoup restent en observation des années |
| « Le WAF bloque » | Une règle a été déclenchée. Légitime ou faux positif ? |
| « C'est protégé, il y a un firewall » | **Un pare-feu réseau ne juge pas le contenu d'une requête web** |

---

🔭 **À RECONNAÎTRE — CDN**

**① Qu'est-ce que c'est.** Un réseau de serveurs répartis qui **servent des contenus au plus près de l'utilisateur**, en s'intercalant devant votre serveur d'origine.

**② Quel problème il résout.** La latence, la charge, et l'absorption des pointes — y compris malveillantes.

**③ Ce que cela change au dessin naïf.**

```
   SANS          Utilisateur ──────────────► serveur d'origine

   AVEC          Utilisateur ──► [ CDN ] ──► serveur d'origine
                                    │
                              répond directement
                              si le contenu est en cache
```

**④ Les cinq questions que le CDN impose**, et ce sont elles qui font sa valeur pédagogique :

| Question | Pourquoi elle compte |
|---|---|
| **Où le chiffrement est-il terminé ?** | Chez le fournisseur du CDN — **il voit le contenu en clair** |
| **Qu'est-ce qui est mis en cache ?** | Une page personnalisée mise en cache par erreur est servie à un autre utilisateur |
| **Quelle adresse voit l'origine ?** | Celle du CDN, pas celle de l'utilisateur — §P.4, §34.2 |
| **Que se passe-t-il si le CDN tombe ?** | Selon la configuration : plus rien, ou un repli vers l'origine qui ne tiendra pas la charge |
| **Où placer le WAF ?** | Souvent chez le fournisseur du CDN, puisque c'est là que le contenu est lisible |

⚠️ **La deuxième ligne produit des incidents réels et embarrassants** : un contenu personnalisé — un panier, un nom, une page authentifiée — mis en cache et servi à d'autres. **La règle de cache est une décision de sécurité, pas un réglage de performance.**

**⑤ Le coût.** Une dépendance à un tiers pour la disponibilité de votre site · un point où le contenu est en clair hors de chez vous · **une origine qui doit rester protégée** — sinon on la contourne en s'adressant directement à elle.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est derrière un CDN » | **L'origine est-elle joignable directement ?** Si oui, le CDN se contourne |
| « Le CDN gère le TLS » | Il voit tout en clair. **Rechiffre-t-il vers l'origine ?** |
| « On a purgé le cache » | Un contenu obsolète était servi. **Combien de temps l'a-t-il été ?** |

#### 12.4 Mandataire inverse ou répartiteur de charge ?

**Une confusion fréquente, après celle avec le pare-feu**, et la distinction est utile.

| | **Mandataire inverse** | **Répartiteur de charge** |
|---|---|---|
| Sa raison d'être | **Masquer et contrôler** | **Distribuer et absorber les pannes** |
| Décide selon | Le contenu de la demande — chemin, nom demandé | La disponibilité et la charge des membres |
| Nombre de cibles | Une ou plusieurs | **Plusieurs, par définition** |
| Authentifie | Souvent | Rarement |

⚠️ **En pratique, un même équipement fait souvent les deux** — et c'est pourquoi les deux termes sont employés indifféremment en réunion. **La question qui tranche** : *cet équipement existe-t-il pour cacher le serveur, ou pour en avoir plusieurs ?* La réponse dit à quoi on renoncerait en le supprimant.

#### 12.5 La confusion avec le pare-feu

Celle d'Amélie au §1.8, et elle est universelle.

| | Pare-feu | Mandataire inverse |
|---|---|---|
| Décide | Si le flux passe | Ce qui est servi, et par quel serveur |
| Voit | Les extrémités, parfois le contenu | Le contenu **si le chiffrement y est terminé** — modes B et C |
| Termine la connexion | Non | **Oui en modes B et C**, non en mode A |
| Peut authentifier | Rarement | **Oui, et c'est souvent sa vraie raison d'être** |
| S'il tombe | Selon la configuration | **Les accès externes seuls** |

#### 12.6 S'il disparaît

Tout ce qui est publié devient injoignable de l'extérieur — **et reste joignable de l'intérieur**.

🔥 **SCÉNARIO — le mandataire fonctionne, le service ne répond plus**

| Question | Réponse |
|---|---|
| Symptôme | Les clients externes obtiennent une erreur. Le mandataire répond, sa supervision est verte |
| Hypothèse naïve | « Le mandataire est en panne » |
| Dépendance réelle | **Le serveur derrière lui**. Le mandataire va bien : il n'a plus personne à qui parler |
| Ce que le schéma aurait dû montrer | Les contrôles de santé entre le mandataire et ses cibles |
| Comment vérifier | Le journal du mandataire : il enregistre l'échec de connexion vers l'arrière |

⚠️ **Ce scénario illustre une règle générale** : un composant intermédiaire en bonne santé ne dit rien de la santé du service. **La supervision d'un mandataire doit porter sur ce qu'il obtient de ses cibles, pas sur son propre état.**

#### 12.7 Sur un schéma

En zone démilitarisée, entre la bordure et l'interne. **Reconnaissable à sa position** : tout ce qui vient de l'extérieur y converge.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est derrière le reverse » | Le service n'est pas exposé directement | **Quel mode de terminaison ?** Y a-t-il un chemin direct depuis l'interne ? |
| « Le frontal termine le TLS » | Mode B ou C | Rechiffre-t-il vers l'arrière, ou le trafic interne est-il en clair ? |
| « C'est une VIP » | Une adresse virtuelle portée par le mandataire ou le répartiteur | Combien de cibles derrière ? Une seule ? |
| « Il faut publier l'appli » | La rendre joignable depuis l'extérieur | Par où ? Avec quelle authentification en amont ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas exposer directement les serveurs | Un composant de plus à exploiter et corriger |
| Concentrer le chiffrement et les certificats | Une gestion de certificats · **un point où tout est en clair, en modes B et C** |
| Authentifier avant d'atteindre l'application | **Une dépendance forte à l'annuaire** |
| Router selon le contenu | Une configuration qui devient vite complexe |
| Servir de point d'entrée unique | **Un point de rupture pour tous les accès externes** |

🏭 **TROIS TAILLES** — Atelier Martin : **aucun**. Elle ne publie aucun service : la contrainte n'existe pas. HELIOMED : un couple redondé, parce qu'elle publie une plateforme de télésuivi accessible à ses clients. Novaris : une ferme par région, parce que la latence et la réglementation imposent une terminaison locale.

---

### Chapitre 13 — Le répartiteur de charge

#### 13.1 À quoi ça sert

Distribuer les demandes entre plusieurs exemplaires d'un même rôle, et **retirer automatiquement ceux qui ne répondent plus**.

**Pourquoi ça existe.** Dès qu'on veut qu'une panne d'un serveur ne soit pas visible, il faut quelqu'un qui sache que ce serveur ne répond plus, et qui envoie ailleurs. C'est ce que fait le contrôle de santé — et c'est la vraie fonction du répartiteur, davantage que la répartition elle-même.

#### 13.2 Le contrôle de santé : ce qui décide de tout

```
   Toutes les N secondes, le répartiteur interroge chaque membre :

   ①  TEST DE CONNEXION      le port répond-il ?
       → détecte une machine éteinte
       → ne détecte PAS une application bloquée

   ②  TEST APPLICATIF        une page de test répond-elle correctement ?
       → détecte une application en erreur
       → ne détecte PAS une base inaccessible derrière

   ③  TEST DE BOUT EN BOUT   une requête qui traverse toute la chaîne
       → détecte tout
       → coûte plus cher, et peut faire sortir TOUS les membres
         si la panne est en aval
```

⚠️ **Le troisième cas produit un incident classique** : la base tombe, le test de bout en bout échoue sur tous les serveurs, le répartiteur les retire tous, et **le service ne répond plus du tout** — alors qu'il aurait pu servir des pages d'erreur. **Un contrôle de santé trop profond transforme une dégradation en arrêt.**

#### 13.3 Le paradoxe du composant de disponibilité

> **Il crée un point de rupture en résolvant un point de rupture.**

C'est pourquoi il est presque systématiquement redondé — et cette redondance pose exactement les mêmes questions que celle du pare-feu, §10.5.

#### 13.4 La session, et pourquoi elle limite tout

**Répartir des demandes est simple. Répartir des demandes qui appartiennent à une session ne l'est pas.**

| Situation | Ce que le répartiteur doit faire |
|---|---|
| L'application ne garde aucun état | Rien de particulier — n'importe quel membre convient |
| L'application garde la session localement | **Renvoyer l'utilisateur toujours sur le même membre** |
| La session est partagée | N'importe quel membre convient |

⚠️ **Le deuxième cas est très répandu, et il annule une partie du bénéfice.** Si le répartiteur doit renvoyer chaque utilisateur sur « son » serveur, alors la panne de ce serveur **déconnecte ses utilisateurs** — la redondance protège les nouveaux venus, pas ceux qui étaient en cours de travail. C'est le §31.2.

#### 13.5 Trois architectures de répartition

```
  A — RÉPARTITION PAR LA RÉSOLUTION DE NOMS
      Le nom renvoie plusieurs adresses, le client en choisit une.
      → aucun équipement · aucun coût
      → aucun contrôle de santé : un serveur mort reçoit quand même
      → les caches retardent tout changement

  B — RÉPARTITEUR DÉDIÉ
      [ répartiteur ] ──► [ web 1 ] [ web 2 ] [ web 3 ]
      → contrôle de santé · retrait automatique
      → un composant de plus, à redonder

  C — RÉPARTITION INTÉGRÉE À LA PLATEFORME
      L'orchestrateur ou le fournisseur cloud s'en charge.
      → rien à exploiter · rien à dessiner
      → une dépendance à la plateforme · une visibilité réduite
```

⚠️ **Le mode A explique un incident fréquent** : trois adresses derrière un nom, un serveur tombe, **et un tiers des utilisateurs obtient une erreur** — parce que rien ne retire l'adresse morte. Sur un schéma, la répartition paraît identique dans les trois modes.

#### 13.6 Ce qu'il fait à la donnée

Il l'achemine. Selon son niveau, il lit le contenu — auquel cas il fait aussi office de mandataire inverse, et les deux composants se confondent souvent dans un même équipement — §12.4.

#### 13.7 S'il disparaît

🔥 **SCÉNARIO — tout tombe alors que tous les serveurs vont bien**

| Question | Réponse |
|---|---|
| Symptôme | Service inaccessible. Les trois serveurs web répondent normalement en direct |
| Hypothèse naïve | « Un problème applicatif » |
| Dépendance réelle | Le répartiteur — **le seul composant sur le chemin qui ne soit pas redondé** |
| Ce que le schéma aurait dû montrer | S'il est unique ou en paire |
| Concevoir différemment | Le redonder · ou prévoir un chemin de secours documenté vers un serveur direct |

**C'est le composant dont la panne est la plus contre-intuitive du cours** : il a été ajouté pour la disponibilité, et son absence arrête tout.

#### 13.8 Sur un schéma

Juste avant un groupe de boîtes identiques. **La présence de trois serveurs web sans répartiteur dessiné est une question à poser** : soit il existe et n'est pas représenté, soit la répartition se fait par la résolution de noms — mode A, qui n'a pas les mêmes propriétés.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça passe par le load balancer » | Un répartiteur est sur le chemin | **Est-il redondé ?** Quel type de contrôle de santé ? |
| « On a de la persistance de session » | L'utilisateur est renvoyé sur le même serveur | **Alors la redondance ne protège pas les sessions en cours** |
| « On a mis deux nœuds » | Deux membres derrière le répartiteur | Sur des hôtes différents ? — *principe de preuve* |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Continuer malgré la panne d'un membre | **Un composant à redonder lui-même** |
| Absorber une charge croissante | Un contrôle de santé à régler — trop profond, il aggrave |
| Retirer un serveur pour maintenance sans coupure | Une gestion de session à traiter — §31 |

---

### Chapitre 14 — La résolution de noms

> **Un composant dont la disparition produit des effets particulièrement déroutants**, et l'un des moins dessinés.

#### 14.1 À quoi ça sert

Traduire un nom en adresse. Rien de plus, et c'est un préalable à presque tout.

**Pourquoi ça existe.** Les adresses changent, et personne ne les retient. Le nom est un identifiant stable ; l'adresse est un détail d'implémentation. Cette indirection est ce qui permet de déplacer un service sans reconfigurer ses clients.

#### 14.2 La séquence complète

🖼 **SCHÉMA 14.1 — Ce qui se passe réellement**

```
   Utilisateur saisit  www.exemple.fr
            │
            ▼
   ┌──────────────────┐
   │   RÉSOLVEUR      │  ← celui que le poste interroge (« récursif »)
   └────────┬─────────┘
            │
      ┌─────┴─────┐
      │ en cache ? │
      └─────┬─────┘
       ┌────┴────┐
      OUI       NON
       │         │
       │         ▼
       │    interroge les serveurs FAISANT AUTORITÉ
       │    pour ce nom, de proche en proche
       │         │
       │         ▼
       │    obtient l'adresse, et la MET EN CACHE
       │    pour la durée de vie annoncée
       │         │
       └────┬────┘
            ▼
        adresse
            │
            ▼
   Client ─────────► serveur
```

#### 14.3 Les cinq notions qui suffisent à raisonner

| Notion | Ce qu'elle est | Pourquoi elle compte en architecture |
|---|---|---|
| **Résolveur récursif** | Celui que le poste interroge | **Sa panne arrête presque tout, en interne** |
| **Serveur faisant autorité** | Celui qui détient la réponse pour un nom | **Sa panne rend votre organisation injoignable de l'extérieur** |
| **Cache** | La réponse conservée un temps | Masque une panne, **puis l'aggrave d'un coup** |
| **Durée de vie** | Combien de temps la réponse est conservée | **Elle détermine le délai d'un changement d'adresse** |
| **Vue interne / vue externe** | Un même nom, deux réponses selon l'origine | Un service peut être atteint par deux chemins différents |

⚠️ **Deux pannes très différentes** que le mot « DNS » recouvre :

| Ce qui tombe | Qui est affecté | Symptôme |
|---|---|---|
| Le **résolveur récursif** | **Vos utilisateurs** | Plus rien ne fonctionne en interne |
| Le serveur **faisant autorité** | **Vos clients externes** | Votre organisation disparaît d'Internet, l'interne va bien |

**Confondre les deux conduit à chercher au mauvais endroit** — et c'est exactement le cas de synthèse B.

#### 14.4 La durée de vie, et pourquoi elle décide d'une migration

**Le mécanisme, souvent mal compris** :

```
   Vous changez l'adresse d'un service à 10 h 00.
   La durée de vie annoncée est de 24 heures.

   10 h 00   ┃ nouvelle adresse publiée
             ┃
   10 h 05   ┃ un client qui n'a jamais résolu → nouvelle adresse ✅
             ┃ un client qui a résolu à 9 h 00 → ANCIENNE adresse ❌
             ┃
   Jusqu'à   ┃ des clients continuent d'aller à l'ancienne adresse
   le lende- ┃ ⚠️ L'ancien serveur doit rester en service
   main 9 h  ┃
```

⚠️ **La conséquence pratique** : **on ne coupe jamais l'ancien serveur le jour de la bascule.** Et si l'on prévoit une migration, on réduit la durée de vie **plusieurs jours avant** — sinon le changement met une journée à se propager, et personne ne sait quels clients sont passés.

#### 14.5 Les deux vues, et le piège qu'elles créent

```
   VUE EXTERNE                       VUE INTERNE
   portail.exemple.fr → 203.0.113.7  portail.exemple.fr → 10.0.4.80
   (adresse du mandataire)            (adresse du serveur, en direct)

   → un client externe passe par le mandataire, et par ses contrôles
   → un poste interne va DIRECTEMENT au serveur
```

⚠️ **Ce que cela signifie en sécurité** : un contrôle placé sur le mandataire — authentification, inspection, journalisation — **ne s'applique pas aux accès internes**. C'est le §29.3, et c'est l'une des raisons pour lesquelles un dispositif placé en frontal couvre moins qu'on ne le croit — §44.4.

#### 14.6 Ce qu'il fait à la donnée

Rien — il ne voit pas le contenu. Mais il voit **toutes les intentions** : chaque nom demandé, par qui, quand. C'est une source de journaux particulièrement riche.

#### 14.7 S'il disparaît

L'essentiel des connexions établies à partir d'un nom échoue, et de façon déroutante : le réseau fonctionne, les serveurs fonctionnent, et rien n'est joignable.

📌 **Ce qui continue de fonctionner, et qu'il faut savoir** :

| Cas | Pourquoi la résolution n'est pas nécessaire |
|---|---|
| Une connexion vers une adresse écrite en dur | Il n'y a pas de nom à traduire |
| Une connexion déjà établie | La traduction a eu lieu avant |
| Un nom encore en cache | Le cache répond à la place du serveur |
| Un service découvert par un autre mécanisme | Découverte de service, configuration distribuée |
| Un client qui passe par un intermédiaire résolvant lui-même | Le mandataire fait la traduction |

🔥 **SCÉNARIO — panne progressive de résolution**

| Question | Réponse |
|---|---|
| Symptôme | À 9 h 15, deux signalements. À 9 h 40, quarante. À 10 h, tout le site |
| Hypothèse naïve | « Ça se dégrade, c'est probablement la charge » |
| Dépendance réelle | **Les caches expirent un par un.** La panne date de 9 h 00 |
| Ce que le schéma aurait dû montrer | Le résolveur, et combien il y en a |
| Comment le reconnaître | **Une panne qui s'aggrave par vagues sans cause apparente est très souvent une panne de résolution ou de certificat** |

🔥 **SCÉNARIO — un résolveur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines résolutions sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Le réseau est chargé » |
| Dépendance réelle | Les clients interrogent le premier serveur, attendent l'expiration du délai, puis basculent sur le second |
| Ce que le schéma aurait dû montrer | Que les deux résolveurs sont **configurés sur les postes**, et dans quel ordre |
| Concevoir différemment | Vérifier que les postes connaissent bien les deux, et non un seul |

⚠️ **Ce second scénario est fréquent et rarement diagnostiqué correctement.** Une redondance de résolution ne fonctionne que si les clients connaissent les deux serveurs. Beaucoup n'en connaissent qu'un — et la redondance existe sur le schéma sans exister en pratique. **Principe de preuve.**

#### 14.8 Sur un schéma

**Presque jamais.** C'est l'exemple canonique du flux de dépendance du principe des trois flux.

⚠️ **La question à poser devant tout schéma** : *où est la résolution de noms, et combien y en a-t-il ?* Si personne ne sait répondre, vous venez d'identifier une dépendance non maîtrisée — et c'est fréquemment l'une des plus structurantes du système.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le DNS est sur les DC » | Les contrôleurs d'annuaire assurent aussi la résolution | **Alors une panne d'annuaire est aussi une panne de résolution** — deux dépendances en une |
| « C'est un problème de DNS » | Une résolution échoue | Récursif ou faisant autorité ? Interne ou externe ? |
| « On a baissé le TTL » | La durée de vie a été réduite | Depuis quand ? Une migration est-elle en cours ? |
| « Il faut créer une entrée » | Ajouter un nom | Dans quelle vue — interne, externe, ou les deux ? |

⚠️ **La première ligne est structurante** : quand la résolution est portée par les contrôleurs d'annuaire, une seule panne produit **deux effets qui n'ont apparemment aucun rapport** — plus d'authentification, et plus de résolution. Le diagnostic devient difficile.

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Désigner les services par un nom stable | **Une dépendance universelle et invisible** |
| Changer une adresse sans changer les configurations | Un délai de propagation lié aux caches |
| Distinguer vue interne et externe | Une double configuration à maintenir cohérente · **des contrôles qui ne s'appliquent pas partout** |
| Redonder | Efficace **uniquement si les clients connaissent les deux serveurs** |

🏭 **TROIS TAILLES** — Atelier Martin : la résolution est portée par le boîtier tout-en-un, **et c'est un point de rupture assumé**. HELIOMED : deux résolveurs internes, portés par les contrôleurs d'annuaire. Novaris : une infrastructure dédiée, **parce que porter la résolution sur les contrôleurs d'annuaire cumule deux pannes en une, ce qu'une organisation de cette taille ne peut pas se permettre**.

---

### Chapitre 15 — L'attribution d'adresses

#### 15.1 À quoi ça sert

Donner automatiquement à une machine qui démarre son adresse, son masque, sa passerelle et l'adresse de son résolveur.

**Pourquoi ça existe.** Configurer six cents postes à la main est impossible ; et un plan d'adressage qui change imposerait de tous les reprendre. L'attribution automatique rend le poste **indifférent au réseau sur lequel il est branché**.

#### 15.2 La séquence, et ce qu'elle distribue

```
   ①  La machine démarre. Elle n'a pas d'adresse.
   ②  Elle demande, en diffusion : « quelqu'un peut-il me configurer ? »
   ③  Le serveur répond, et propose :
         · une adresse, pour une DURÉE limitée (le bail)
         · un masque de sous-réseau
         · une passerelle par défaut
         · l'adresse d'un ou plusieurs résolveurs
         · parfois : un domaine, un serveur de temps, un mandataire
   ④  La machine accepte, et renouvelle avant expiration du bail
```

⚠️ **Ce qu'il faut retenir de l'étape ③** : ce composant ne distribue pas seulement une adresse. **Il distribue la configuration réseau complète.** Une erreur dans l'adresse du résolveur distribuée, et six cents postes perdent la résolution de noms — §14.

#### 15.3 Le bail, et pourquoi la panne est différée

```
   Bail de 8 jours, renouvelé à mi-parcours.

   Jour 0    Le serveur tombe.
   Jour 0    RIEN ne se passe. Toutes les machines ont une adresse valide.
   Jour 4    Les premiers renouvellements échouent → les machines gardent
             leur adresse et réessaient
   Jour 8    Les premiers baux expirent → les premières machines
             perdent leur adresse
   Jour 8-16 Les machines tombent une par une, dans un ordre
             qui paraît aléatoire
```

⚠️ **C'est la panne différée par excellence**, et la plus difficile à relier à sa cause : **plusieurs jours peuvent séparer l'incident de ses premiers effets**, et les effets arrivent progressivement.

🔥 **SCÉNARIO — des postes tombent au hasard depuis trois jours**

| Question | Réponse |
|---|---|
| Symptôme | Chaque jour, quelques postes n'ont plus de réseau. Aucun point commun apparent |
| Hypothèse naïve | « Un problème matériel sur les postes » ou « le commutateur » |
| Dépendance réelle | Le serveur d'attribution, arrêté **il y a plusieurs jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'y figure jamais |
| Comment le reconnaître | **Les postes touchés sont ceux qui ont redémarré ou dont le bail a expiré** — pas un groupe géographique |

#### 15.4 Ce qu'il fait à la donnée

Rien. Mais il sait **quelle machine est apparue, quand, et avec quelle identité matérielle** — une source précieuse pour l'inventaire, et presque jamais exploitée. C'est le chapitre 11 du volume Asset Management.

#### 15.5 Sur un schéma

Jamais. Flux de dépendance.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Il est en DHCP » | La machine reçoit sa configuration automatiquement | **Son adresse change-t-elle ?** Cela affecte les règles de filtrage par adresse |
| « On lui a mis une IP fixe » | Adresse configurée en dur, ou réservée | En dur sur la machine, ou réservée sur le serveur ? Ce n'est pas la même chose |
| « Un poste a pris une mauvaise IP » | Conflit ou serveur non autorisé | **Un serveur d'attribution non déclaré sur le réseau est un incident de sécurité** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas configurer chaque machine à la main | **Une machine peut apparaître sans être déclarée nulle part** |
| Changer un plan d'adressage sans toucher aux postes | Une dépendance de plus au démarrage |
| Distribuer toute la configuration réseau | **Une erreur se propage à l'ensemble du parc** |

⚠️ **La ligne du milieu à droite** est l'origine d'un problème traité dans deux autres volumes : une machine branchée obtient une adresse et fonctionne, **sans avoir été inventoriée, autorisée ni supervisée**.

---

### Chapitre 16 — L'annuaire

> ⚠️ **Précision de vocabulaire, à poser avant tout.**
>
> **Service d'annuaire** est le concept général : un composant qui détient des identités, des groupes et des règles.
> **Active Directory** en est l'implémentation la plus répandue en entreprise, et c'est elle que ce chapitre décrit — parce qu'elle rend le concept concret.
>
> **Les propriétés décrites ici — contrôleurs, domaines, forêts, relations d'approbation, politiques — sont celles de ce modèle.** D'autres services d'identité existent et fonctionnent autrement : annuaires ouverts, fournisseurs d'identité en ligne, bases d'identités applicatives. Ne transportez pas ce modèle sur eux sans vérifier.
>
> ⚠️ **Et surtout** : **LDAP n'est pas l'authentification.** C'est un protocole d'interrogation et de modification d'annuaire. Dans un domaine Active Directory, l'authentification s'appuie principalement sur **Kerberos**, et la résolution de noms y joue un rôle structurant. Un schéma qui montre uniquement un flux LDAP vers l'annuaire ne montre donc pas tout le mécanisme d'authentification.

#### 16.1 À quoi ça sert

Détenir les identités, les groupes et les règles, et répondre à deux questions : *qui es-tu* et *à quoi as-tu droit*.

**Pourquoi ça existe.** Sans lui, chaque application détient ses propres comptes. Un salarié qui part doit être retiré de trente endroits — et il le sera de vingt-huit. La centralisation résout le problème du cycle de vie des identités, et en crée un autre : **une dépendance universelle**.

#### 16.2 Les trois mécanismes, et pourquoi il faut les distinguer

| Mécanisme | Ce qu'il fait | Sur un schéma |
|---|---|---|
| **LDAP** | Interroge et modifie l'annuaire : chercher un utilisateur, lister un groupe | Ports 389 / 636 |
| **Kerberos** | **Authentifie** : délivre un ticket qui prouve l'identité, sans renvoyer le mot de passe | Rarement dessiné |
| **Résolution de noms** | **Localise les contrôleurs** eux-mêmes | Jamais dessiné |

⚠️ **La troisième ligne explique un incident très fréquent** : dans un domaine Active Directory, un poste trouve ses contrôleurs **par la résolution de noms**. Si celle-ci est défaillante, **le poste ne trouve pas l'annuaire** — et le symptôme est une panne d'authentification, alors que l'annuaire fonctionne parfaitement.

> **Deux composants invisibles, et l'un dépend de l'autre.** C'est le chemin de diagnostic le plus difficile du cours.

#### 16.3 La cascade d'une panne

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT      ← rien ne se voit
              │  (les tickets déjà délivrés restent valides)
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les tickets expirent · les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```

🔥 **SCÉNARIO — un contrôleur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines ouvertures de session sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Les postes sont lents » |
| Dépendance réelle | Les clients tentent le premier contrôleur, attendent l'expiration du délai, basculent |
| Ce que le schéma aurait dû montrer | Combien de contrôleurs, **et s'ils sont sur des hôtes différents** — *principe de preuve* |
| Concevoir différemment | Vérifier que la bascule est effective, et non seulement configurée |

#### 16.4 Les notions qui suffisent à raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Contrôleur** | La machine qui répond. **Un domaine fonctionne avec un seul ; deux ou plus sont recommandés pour la disponibilité** — ⚠️ **Principe de preuve** : deux contrôleurs sur le même hôte ne constituent pas une redondance |
| **Domaine, forêt** | *(vocabulaire Active Directory)* Le périmètre d'une identité. Une acquisition en ajoute souvent un |
| **Relation d'approbation** | Ce qui permet à une identité d'un périmètre d'accéder à un autre — **et ce qui propage une compromission** |
| **Groupe** | L'unité de droit réelle. Les droits individuels restent minoritaires dans les modèles bien tenus |
| **Politiques** | Des règles appliquées automatiquement aux postes à l'ouverture de session |

⚠️ **Sur les relations d'approbation** : elles sont pratiques et elles ont une conséquence lourde. Une compromission dans le périmètre A peut devenir une compromission dans le périmètre B. **Sur un schéma, une flèche entre deux annuaires mérite toujours une question : dans quel sens, et avec quelle portée ?**

#### 16.5 Ce qu'il fait à la donnée

Il ne la voit pas. Mais il **décide qui la voit** — ce qui en fait, avec la sauvegarde, l'actif dont la compromission a les conséquences les plus larges.

#### 16.6 Sur un schéma

Dessiné comme une boîte, **sans aucun trait** — le cas du §1.1. Tout s'y connecte, rien ne le montre.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça tape l'AD » | Le composant s'authentifie contre l'annuaire | **Par quel mécanisme ?** LDAP pour interroger, ou Kerberos pour authentifier ? |
| « Il est dans le domaine » | La machine est jointe à l'annuaire | Alors elle dépend de lui **et de la résolution de noms** au démarrage |
| « On a un trust avec l'autre forêt » | Une relation d'approbation existe | **Dans quel sens ? Depuis quand ? Qui l'a demandée ?** |
| « Le DNS est sur les DC » | Deux fonctions sur les mêmes machines | **Une panne, deux effets sans rapport apparent** — §14 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Une identité unique pour de nombreux services | **Une dépendance universelle** · une compromission qui donne tout |
| Gérer les droits par groupes | Des groupes qui s'accumulent et ne se réduisent jamais seuls |
| Appliquer des politiques automatiquement | Un empilement difficile à auditer |
| Fédérer plusieurs périmètres | **Une compromission qui peut traverser la relation d'approbation** |

🏭 **TROIS TAILLES** — Atelier Martin : un contrôleur, **et c'est un point de rupture assumé faute de budget**. HELIOMED : deux contrôleurs, plus un annuaire hérité de l'acquisition de 2019 que personne n'a fusionné. Novaris : quatre forêts, **parce que sept acquisitions en quinze ans et trois fusions arbitrées comme trop risquées** — jamais parce que douze mille salariés.

---

### Chapitre 17 — L'infrastructure de clés

#### 17.1 À quoi ça sert

Émettre, publier et révoquer des certificats.

**Ce qu'un certificat fait exactement**, parce que la formulation courante est imprécise :

> Un certificat **lie une identité — ou un attribut — à une clé publique**, et cette liaison est attestée par une autorité au sein d'une chaîne de confiance.

⚠️ **Un certificat ne chiffre rien par lui-même.** Il permet à un protocole de vérifier à qui l'on parle ; le chiffrement de l'échange est ensuite assuré par le protocole. Un certificat peut aussi servir à signer sans qu'aucun chiffrement de transport n'intervienne.

#### 17.2 La chaîne de confiance, en une image

```
   [ AUTORITÉ RACINE ]        ← son certificat est INSTALLÉ sur les machines
            │                    C'est ce qui fonde toute la confiance
            ▼
   [ AUTORITÉ INTERMÉDIAIRE ] ← elle signe au quotidien
            │                    La racine reste hors ligne
            ▼
   [ CERTIFICAT DU SERVEUR ]  ← présenté au client

   Le client vérifie : ce certificat est-il signé par une autorité
   à laquelle JE fais confiance ?
        ├── OUI  ──► accepté
        └── NON  ──► avertissement, ou refus
```

⚠️ **Le point qui décide de tout** : *à quelles autorités le client fait-il confiance ?* Un navigateur fait confiance à une liste préinstallée d'autorités publiques. **Une machine de votre organisation fait en plus confiance à votre autorité interne, si vous l'y avez déployée.**

**D'où la formulation exacte** : un certificat émis par une autorité privée n'est reconnu que par **les systèmes qui font confiance à cette chaîne** — vos machines si vous l'y avez déployée, celles d'un partenaire à qui vous l'avez transmise, et **aucune machine que vous ne contrôlez pas si vous ne l'avez pas fait**.

#### 17.3 La révocation, et pourquoi elle est le maillon faible

**Le problème** : un certificat a une date d'expiration. Que faire s'il faut l'invalider **avant** ?

```
   ①  L'autorité publie une liste de certificats révoqués
   ②  Le client la télécharge, ou interroge un service dédié
   ③  Il vérifie que le certificat présenté n'y figure pas

   ⚠️  Que se passe-t-il si l'étape ② échoue ?
        ├── mode strict   : le client REFUSE  → indisponibilité
        └── mode souple   : le client ACCEPTE → la révocation ne sert à rien
```

⚠️ **Le comportement varie fortement selon le client, le mécanisme et la configuration.** Certains refusent, beaucoup acceptent, d'autres ne vérifient pas du tout ; des mécanismes récents améliorent la situation en faisant transmettre l'état de révocation par le serveur lui-même.

> **Ce qu'il faut en retenir en architecture** : **on ne peut pas supposer qu'une révocation sera effective partout et immédiatement.** Ce n'est pas un mécanisme inutile, c'est un mécanisme dont l'effet dépend de choses que vous ne contrôlez pas.

📌 **Ce que cela impose en conception** : ne pas compter sur la révocation seule. **Des certificats de courte durée** réduisent la fenêtre d'exposition sans dépendre d'un mécanisme fragile — au prix d'un renouvellement fréquent, donc automatisé.

🔭 **À RECONNAÎTRE — HSM**

**① Qu'est-ce que c'est.** Un équipement matériel dédié qui **protège des clés cryptographiques et exécute les opérations qui les utilisent**.

**② Quel problème il résout.** La question fondamentale de tout ce chapitre :

> ### Où vit réellement la clé privée ?

Si elle est dans un fichier sur un serveur, **quiconque accède à ce serveur — ou à ses sauvegardes — l'obtient**. Le concept architectural du HSM n'est pas son fonctionnement cryptographique interne, c'est celui-ci :

> **La clé sensible peut être *utilisée* sans jamais être *exportée* comme un simple fichier.**

L'application demande une signature ou un déchiffrement ; l'équipement l'exécute et renvoie le résultat. **La clé ne sort pas.**

**③ Où on le rencontre.** À la racine d'une autorité de certification interne · pour signer du code ou des micrologiciels · dans les traitements de paiement · partout où une clé compromise aurait des conséquences irréversibles.

**④ Ce que cela change.** Une dépendance nouvelle : **si l'équipement est indisponible, les opérations qui en dépendent échouent**. Et une question de sauvegarde qui n'a pas de réponse simple — une clé qu'on ne peut pas exporter ne se sauvegarde pas comme un fichier ; il existe des mécanismes de séquestre, et ils sont eux-mêmes sensibles.

**⑤ Le coût.** Un équipement onéreux · une exploitation spécialisée · **une cérémonie de clés** pour les opérations sensibles, avec plusieurs porteurs · une redondance qui doit être prévue dès l'origine.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « La racine est dans un HSM » | Bon signe. **Est-il redondé ? Où est le séquestre ?** |
| « La clé est dans un fichier sur le serveur » | **Alors elle est aussi dans les sauvegardes** — §33.2 |
| « On signe avec le HSM » | **Que se passe-t-il s'il est indisponible au moment de signer ?** |

📚 **À approfondir ailleurs** : les niveaux de certification, les cérémonies de clés, l'intégration applicative.

#### 17.4 S'il disparaît

Rien **immédiatement**. Puis, à chaque expiration de certificat, un service tombe — sans préavis et sans lien apparent avec la panne.

🔥 **SCÉNARIO — un service tombe sans que rien n'ait changé**

| Question | Réponse |
|---|---|
| Symptôme | Un service refuse les connexions à un horaire précis et net. Aucune intervention |
| Hypothèse naïve | « Une tâche planifiée a cassé quelque chose » |
| Dépendance réelle | **Un certificat a expiré.** L'heure exacte est le signe distinctif |
| Ce que le schéma aurait dû montrer | Rien — les certificats ne sont jamais dessinés |
| Comment le reconnaître | **Une panne à un horaire net, sans intervention, oriente vers une échéance** : expiration de certificat, rotation de secret, fin de durée de vie. La date exacte d'un certificat est inscrite dedans — elle n'est pas nécessairement minuit |
| Concevoir différemment | Surveiller les dates d'expiration · automatiser le renouvellement |

🔥 **SCÉNARIO — la chaîne fonctionne, la révocation non**

| Question | Réponse |
|---|---|
| Symptôme | Certains clients — souvent les plus stricts — refusent la connexion. La plupart l'acceptent |
| Hypothèse naïve | « Un problème sur ces postes » |
| Dépendance réelle | Le service de révocation est injoignable. Les clients en mode strict refusent |
| Ce que le schéma aurait dû montrer | Que la vérification de révocation est **un flux sortant, vers un service souvent externe** |
| Concevoir différemment | Vérifier que ce flux est autorisé dans le pare-feu — **il ne l'est pas toujours** |

⚠️ **Ce second scénario est un cas d'école** : une organisation bloque les sorties Internet non autorisées, et bloque au passage la vérification de révocation. Les certificats fonctionnent, jusqu'au jour où un client strict apparaît.

#### 17.5 Ce qu'il faut en savoir pour raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Autorité** | Qui signe. Publique ou interne, et cela change tout |
| **Chaîne de confiance** | Si un maillon n'est pas reconnu, le certificat est refusé |
| **Expiration** | **La première cause d'incident liée aux certificats** |
| **Révocation** | Un mécanisme fragile · rarement testé · **au comportement variable selon les clients** |
| **Interne contre publique** | Un certificat privé n'est reconnu que par les systèmes qui font confiance à cette chaîne |
| **Inventaire des certificats** | **Presque jamais tenu** — et c'est ce qui produit les expirations surprises |

#### 17.6 Sur un schéma

Jamais. Les certificats sont invisibles tant qu'ils fonctionnent.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le certif a expiré » | Une date est dépassée | **Combien d'autres expirent dans les 90 jours ?** Existe-t-il un inventaire ? |
| « On a notre propre PKI » | Une autorité interne existe | Sa chaîne est-elle déployée partout où elle doit l'être ? |
| « Il y a une erreur de certificat » | Le client refuse ou avertit | Expiration · chaîne non reconnue · **nom qui ne correspond pas** — trois causes distinctes |
| « On a mis un wildcard » | Un certificat couvre plusieurs noms | **Sa compromission affecte tous ces noms à la fois** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Émettre des certificats sans passer par un tiers | **Une hiérarchie à maintenir des années** · des expirations à suivre |
| Émettre pour des noms ou des usages non couverts par les autorités publiques | Une révocation qui doit fonctionner réellement, et qui est rarement testée |
| Authentifier des machines entre elles | Un inventaire des certificats — **presque jamais tenu** |
| Un certificat couvrant plusieurs noms | Une compromission de portée élargie |

🏭 **TROIS TAILLES** — Atelier Martin : **aucune infrastructure interne**, uniquement des certificats publics achetés. HELIOMED : une interne, **parce qu'elle doit émettre des certificats sur des noms internes que les autorités publiques ne délivrent pas, et parce qu'elle veut maîtriser sa propre chaîne de confiance**. Novaris : une hiérarchie à deux niveaux, pour cloisonner l'émission par entité.

---

#### 🔬 Mini-lab 4 — Dix composants sans légende

**Objectif** — **Proposer le rôle le plus probable** de chaque composant, et dire ce qu'il faudrait vérifier.
**Durée** 30 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

```
                        Internet
                            │
                        ┌───┴───┐
                        │   A   │
                        └───┬───┘
              ┌─────────────┼─────────────┐
          ┌───┴───┐                   ┌───┴───┐
          │   B   │                   │   C   │
          └───┬───┘                   └───────┘
          ┌───┴───┐
          │   D   │
          └───┬───┘
        ┌─────┼─────┐
      [E1]  [E2]  [E3]
              │
          ┌───┴───┐        ┌───────┐        ┌───────┐
          │   F   │        │   G   │        │   H   │
          └───────┘        └───────┘        └───────┘
                          (aucun trait)    (aucun trait)

  Indices : C reçoit les courriels · G répond à des requêtes sur le port 53
            H répond sur les ports 389 et 636 · F contient les données
```

❓ **Pour chaque composant A à H** : proposez le rôle le plus probable, indiquez **ce qu'il faudrait vérifier pour le confirmer**, et dites lesquels sont probablement des points de rupture.

⚠️ **Le principe d'hypothèse s'applique** : un port, une position et un ensemble de connexions constituent un **faisceau**, pas une preuve. Un service peut écouter sur un port non standard, un composant peut cumuler deux rôles, et une position peut être trompeuse.

---

**Corrigé**

| Réf | Rôle **probable** | Sur quel faisceau | **À vérifier pour confirmer** | Rupture ? |
|---|---|---|---|---|
| **A** | Pare-feu | Position en bordure, tout converge | Est-ce un pare-feu seul, ou un boîtier cumulant routage et accès distant ? | Probable, sauf redondance non représentée |
| **B** | Mandataire inverse | Reçoit de l'extérieur, relaie vers l'intérieur | **Quel mode de terminaison** ? §12 · redondé ? | Probable, pour l'externe seulement |
| **C** | Relais de messagerie | L'indice fourni | Relaie-t-il vers un serveur interne, ou vers un service en ligne ? | Probable |
| **D** | Répartiteur de charge | Placé avant un groupe identique | La répartition se fait-elle bien ici, ou par la résolution de noms ? | **Probable** — §13 |
| **E1-E3** | Serveurs web | Trois exemplaires derrière un répartiteur | **Sur des hôtes différents ?** · **où vivent les sessions ?** — *principe de preuve*, §31.2 | **Indéterminé** |
| **F** | Base de données | L'indice, et la position en bas | Unique, ou répliquée sans que le schéma le montre ? | Probable, et le plus lourd de conséquences |
| **G** | Service de résolution de noms | Port 53 | Récursif, faisant autorité, ou les deux ? Combien y en a-t-il ? | Probable, **et invisible** |
| **H** | Service d'annuaire | Ports 389 et 636 | **Ces ports ne montrent que l'interrogation.** L'authentification passe par d'autres mécanismes — §16 | Probable, **et invisible** |

**Les quatre erreurs attendues** *(cohérentes avec le principe d'hypothèse)*

1. **Répondre avec certitude.** Aucune de ces identifications n'est établie. Un service peut écouter sur un port inhabituel, un composant peut cumuler deux rôles, une position peut être trompeuse. **Principe d'hypothèse.**
2. **Confondre A et B.** Les deux sont en bordure. La distinction se fait par ce qui les suit : A reçoit tout, B ne relaie que le web.
3. **Ne pas retenir G et H comme ruptures probables** parce qu'aucun trait ne les relie. **C'est le piège central** : leur absence de connexion ne signifie pas qu'ils sont isolés, mais que le dessinateur a renoncé à représenter des dépendances universelles.
4. **Conclure que E1-E3 constituent une redondance.** Rien ne l'établit : ils peuvent partager un hôte, et les sessions peuvent être locales. **Principe de preuve** — le schéma montre une *intention* de redondance.

**La leçon** : sur huit composants, **cinq sont des ruptures probables, dont deux ne sont reliés à rien** — et la seule redondance apparente n'est pas vérifiée.

---

#### 🔬 Mini-lab 5 — Que se passe-t-il si on retire cette boîte ?

**Objectif** — Prévoir l'effet de la disparition d'un composant, y compris différé.
**Durée** 25 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

Pour chacun, dire : **ce qui tombe · quand · et si l'utilisateur comprend**.

---

**Corrigé**

| Composant retiré | Ce qui tombe | Délai | L'utilisateur comprend-il ? |
|---|---|---|---|
| **Commutateur d'un étage** | Tout l'étage | Immédiat | ✅ Oui — « plus de réseau ici » |
| **Routeur inter-sites** | Les échanges entre sites | Immédiat | ⚠️ Partiellement — « le serveur de Lyon ne répond plus » |
| **Pare-feu en coupure** | Tout ce qui traverse | Immédiat | ⚠️ Non — tout paraît fonctionner localement |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ **Non** — « j'ai du réseau mais pas Internet » |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ Non — l'interne fonctionne |
| **Répartiteur de charge** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ **Non** — c'est le plus contre-intuitif |
| **Résolution de noms** | Presque tout | **Différé** — les caches masquent, puis tout tombe | ❌ **Non — la panne la plus déroutante** |
| **Attribution d'adresses** | Les machines, une par une | **Différé de plusieurs heures ou jours** | ❌ Non — aucun lien apparent |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ Partiellement |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé de plusieurs mois** | ❌ **Non — la plus difficile à diagnostiquer** |

**Ce que le tableau enseigne, et qui est le cœur de la partie** :

> **Les composants dont la panne est la plus incompréhensible sont exactement ceux qui ne sont pas dessinés.**

Résolution de noms, attribution d'adresses, annuaire, certificats : quatre flux de dépendance, quatre pannes différées ou inexplicables, zéro représentation sur les schémas. C'est la règle principe des trois flux démontrée par ses conséquences.

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> ✓ ce que fait chacun des **dix composants d'infrastructure**, et surtout **ce qui se passe s'il disparaît** ;
> ✓ distinguer **routeur et pare-feu** — où ça va, et si ça a le droit ;
> ✓ distinguer **mandataire sortant et mandataire inverse**, deux fonctions opposées sous un même mot ;
> ✓ que le **répartiteur de charge crée un point de rupture en en résolvant un** ;
> ✓ que les **quatre composants les moins dessinés** produisent les pannes les plus incompréhensibles ;
> ✓ pour chaque composant, **la contrainte qu'il résout et le coût qu'il introduit** — et qu'ajouter n'est jamais gratuit ;
> ✓ qu'**aucun de ces composants n'apparaît par la taille de l'organisation**, mais par une contrainte identifiable ;
> ✓ **le socle réseau minimal** : deux niveaux d'adressage · sous-réseau et passerelle · sens d'établissement d'une connexion · traduction d'adresses · et que le modèle « adresse interne + traduction » n'est pas universel ;
> ✓ que **LDAP interroge et Kerberos authentifie** — trois mécanismes, pas un ;
> ✓ que **le chiffrement peut être terminé à trois endroits différents**, et que le schéma ne le dit jamais.
>
> **Ce que vous ne savez pas encore** : ce qui s'exécute sur les serveurs, et pourquoi on les sépare. C'est l'objet de la Partie III.

---

## PARTIE III — Les serveurs et l'exécution

> **Le fil de la partie**, et la réponse est toujours la même :
>
> ### Pourquoi cette séparation ? — **Parce qu'on sépare ce qui n'a pas les mêmes contraintes.**
>
> Pas les mêmes exigences de disponibilité, pas les mêmes cycles de mise à jour, pas les mêmes profils de charge, pas les mêmes conséquences en cas de compromission. Chaque séparation que vous verrez sur un schéma répond à l'une de ces quatre raisons.

---

### Chapitre 18 — Le serveur web

#### 18.1 À quoi ça sert

Recevoir une demande venue d'un navigateur, servir ce qui est statique, et transmettre le reste à ce qui sait le traiter.

**Pourquoi ça existe comme couche séparée.** Servir un fichier et exécuter une logique métier n'ont ni les mêmes contraintes, ni les mêmes cycles de mise à jour, ni les mêmes profils de charge. Les séparer permet de redonder l'un sans redonder l'autre — et c'est exactement l'arbitrage du schéma 1.1.

#### 18.2 Ce qu'il fait à la donnée

Il la met en forme et la transporte.

⚠️ **Une précision qui compte** : un serveur web n'est pas *par nature* dépourvu d'état. **L'absence d'état est une décision de conception**, prise précisément pour le rendre interchangeable. Un serveur web qui conserve des sessions localement, des fichiers téléversés ou un cache applicatif **a un état** — et il n'est alors plus interchangeable, quelle que soit la façon dont le schéma le représente. C'est le §31.2.

#### 18.3 Trois architectures de frontal

```
  A — TOUT SUR UNE MACHINE
      [ web + application + base ]
      → simple · un seul composant à exploiter
      → une mise à jour applicative impose d'arrêter le tout
      → convient à une petite application interne — §48.1

  B — WEB SÉPARÉ DE L'APPLICATION
      [ web ×2 ] ──► [ application ] ──► [ base ]
      → le frontal se redonde facilement, l'application non
      → deux cycles de mise à jour indépendants
      → la redondance s'arrête à mi-parcours — c'est un ARBITRAGE

  C — CONTENU STATIQUE SÉPARÉ
      [ diffusion de contenu ] ──► fichiers, images, scripts
      [ web ×2 ] ──────────────► pages dynamiques
      → le trafic le plus volumineux ne touche plus vos serveurs
      → une dépendance à un tiers · §38
```

**La contrainte qui fait passer de A à B** n'est pas la charge : c'est **le besoin de mettre à jour l'un sans arrêter l'autre**. Beaucoup d'architectures à trois niveaux existent pour cette raison, pas pour la performance.

#### 18.4 S'il disparaît

Si un exemplaire tombe et qu'il y en a d'autres derrière un répartiteur : rien. S'il est seul : le service s'arrête.

🔥 **SCÉNARIO — un serveur sur trois tombe, et un tiers des utilisateurs est déconnecté**

| Question | Réponse |
|---|---|
| Symptôme | Un serveur redémarre. **Un tiers des utilisateurs perd sa session en cours** |
| Hypothèse naïve | « La répartition ne fonctionne pas » |
| Dépendance réelle | **Les sessions étaient locales au serveur** — §31.2 |
| Ce que le schéma aurait dû montrer | Où vivent les sessions |
| Concevoir différemment | Un magasin de sessions partagé, **avec le composant supplémentaire que cela suppose** |

⚠️ **La redondance fonctionnait parfaitement.** Elle protégeait les nouveaux venus, pas les utilisateurs en cours de travail. **C'est une distinction que le schéma ne peut pas exprimer.**

#### 18.5 Sur un schéma

En haut du groupe applicatif, souvent en plusieurs exemplaires. **Trois boîtes identiques côte à côte désignent presque toujours des serveurs web.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le frontal » | Le serveur web, ou le mandataire inverse | **Les deux mots désignent souvent deux composants différents** |
| « C'est du stateless » | Le serveur ne garde pas de session | **Et le panier ? Les fichiers téléversés ? Le cache ?** |
| « On a scalé horizontalement » | Des exemplaires ont été ajoutés | Sur des hôtes différents ? Les sessions suivent-elles ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Servir des contenus à grande échelle | Une couche de plus dans le chemin |
| Se redonder facilement, s'il a été conçu sans état | **Un état qu'il faut alors mettre ailleurs** — §31 |
| Séparer les cycles de mise à jour | Deux composants à exploiter au lieu d'un |

⚠️ **La deuxième ligne est le vrai sujet, et elle illustre le principe du coût.** Un serveur web est redondable **lorsqu'il a été conçu pour ne rien garder**. Ce « rien » doit alors vivre ailleurs, et ce déplacement crée de nouvelles dépendances, souvent un composant supplémentaire. **L'absence d'état n'est pas une propriété magique du frontal : c'est un compromis qui déplace le problème.**

---

### Chapitre 19 — Le serveur applicatif

#### 19.1 À quoi ça sert

Exécuter la logique métier : calculer, décider, orchestrer, appeler la base.

**Pourquoi c'est le composant le plus important du chemin, en sécurité.** C'est le seul qui connaisse simultanément **l'utilisateur réel et l'action métier** — §43.3. Un journal de pare-feu dit *« une adresse a ouvert une connexion »* ; un journal d'applicatif dit *« Marie a exporté quatre mille lignes »*.

#### 19.2 Ce qu'il fait à la donnée

Il la traite, la transforme, décide qui a le droit de la voir. **C'est là que réside la logique d'autorisation** — donc le composant dont la compromission permet de contourner les règles métier.

⚠️ **Une conséquence importante et mal connue** : l'applicatif interroge très souvent la base avec **un compte de service unique**, pas avec l'identité de l'utilisateur. **Le journal de la base ne voit donc pas l'utilisateur final.** Corréler exige de traverser deux journaux, et suppose une horloge commune — §34.1.

#### 19.3 Pourquoi il est souvent le point de rupture

| Raison | Explication |
|---|---|
| **Il porte de l'état** | Sessions, files de traitement, caches applicatifs |
| **Il est difficile à redonder** | Deux exemplaires supposent que l'état soit partagé ou externalisé |
| **Les licences le limitent** | Un second exemplaire est parfois facturé au prix du premier — §4.6 |
| **Les traitements planifiés** | Certains ne doivent s'exécuter **qu'une fois** — deux exemplaires les dupliquent |

⚠️ **La dernière ligne est un piège classique de redondance.** Une application qui exécute un traitement nocturne, redondée sans précaution, l'exécute **deux fois** — avec des conséquences métier parfois graves. C'est l'une des raisons pour lesquelles la redondance applicative est plus difficile qu'elle n'en a l'air.

#### 19.4 S'il disparaît

Le site s'affiche et **plus rien ne fonctionne**. C'est un symptôme reconnaissable : la page se charge, les boutons ne répondent plus, des erreurs apparaissent.

🔥 **SCÉNARIO — le site s'affiche, rien ne marche**

| Question | Réponse |
|---|---|
| Symptôme | La page d'accueil s'affiche normalement. Toute action produit une erreur |
| Hypothèse naïve | « Le site est tombé » |
| Dépendance réelle | Le serveur web va bien — **c'est ce qui est derrière qui ne répond plus** |
| Ce que le schéma aurait dû montrer | La séparation web / applicatif, et le contrôle de santé entre les deux |
| Comment vérifier en trente secondes | La page statique s'affiche → web ✅ · une action échoue → applicatif ou base ❌ |

**Ce diagnostic en deux temps est l'un des plus utiles du cours**, et il ne demande aucun accès technique.

#### 19.5 Sur un schéma

Entre le web et la base. **Souvent en un seul exemplaire là où le web en compte trois** — et c'est le §1.1.

👁 **CE QU'IL FALLAIT OBSERVER** — la rupture de symétrie est une information, pas une erreur. Trois web et un applicatif signalent un arbitrage : ici, le coût de licence de 2021 — §4.6. **Un lecteur exercé voit la rupture et demande son histoire ; un débutant conclut à une incohérence.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le backend » | L'applicatif, ou la base, ou les deux | **Lequel exactement ?** |
| « L'appli est down » | Le service ne rend plus son objet | Le web répond-il encore ? La distinction oriente le diagnostic |
| « On ne peut pas le doubler » | Un second exemplaire est impossible | **Pourquoi ?** Licence · état local · traitement planifié · trois causes distinctes |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Séparer la logique de la présentation | Une couche, une latence, un composant de plus |
| Mutualiser la logique entre plusieurs frontaux | **Souvent un point de rupture**, car difficile à redonder |
| Concentrer les règles d'autorisation | Une compromission qui donne accès aux données métier |

---

### Chapitre 20 — La base de données

> **Pourquoi elle se trouve au fond dans ce modèle.**

#### 20.1 À quoi ça sert

Conserver les données de manière durable, cohérente et interrogeable, en gérant les accès concurrents.

**Pourquoi ça existe comme composant séparé.** Deux utilisateurs qui modifient la même donnée au même instant doivent obtenir un résultat cohérent. C'est ce problème — la concurrence — qui justifie un composant spécialisé, davantage que le stockage lui-même.

#### 20.2 Pourquoi elle est au fond, et pourquoi c'est un choix

🖼 **SCHÉMA 20.1 — La raison de l'empilement**

```
   EXPOSÉ, REMPLAÇABLE           web ×3      ← perte = aucune conséquence
        ▲                          │
        │                          ▼
        │                     applicatif      ← perte = service arrêté,
        │                          │             données intactes
        ▼                          ▼
   PROTÉGÉ, IRREMPLAÇABLE       base ×1       ← perte = données perdues

   Dans ce modèle : plus on descend, moins de composants,
   plus de valeur, moins d'exposition, plus de conséquences.
```

⚠️ **Ce schéma décrit le modèle à trois niveaux, pas une propriété générale des systèmes d'information.** Les architectures modernes le cassent régulièrement — stockage objet joignable directement, sources de données multiples, données réparties. Le chapitre 42 y revient.

**Les quatre raisons de cette position** :

| Raison | Explication |
|---|---|
| **Valeur** | Ce qui est irremplaçable doit être le plus loin de l'extérieur |
| **Exposition** | Chaque couche traversée est un contrôle de plus |
| **Redondance décroissante** | Redonder une base est difficile et coûteux |
| **Cycle de vie** | Une base vit dix ou vingt ans ; une couche web se remplace tous les trois ans |

#### 20.3 Trois façons de tenir une base

```
  A — EXEMPLAIRE UNIQUE
      [ base ]
      → simple · une panne = arrêt · restauration depuis sauvegarde
      → convient quand l'interruption tolérable dépasse
        le délai de restauration MESURÉ

  B — RÉPLICATION AVEC BASCULE
      [ primaire ] ══► [ secondaire ]
      → interruption courte SI la bascule fonctionne — ⚠️ *principe de preuve*
      → deux exemplaires à exploiter, corriger, surveiller
      → attention : réplication ASYNCHRONE = perte possible
        des dernières transactions

  C — RÉPARTITION SUR PLUSIEURS NŒUDS
      [ nœud 1 ] [ nœud 2 ] [ nœud 3 ]
      → tolérance à la panne d'un nœud
      → un système distribué complet à exploiter — §47.3
```

⚠️ **Le passage de A à B ne se justifie pas par la taille**, mais par la comparaison entre **l'interruption tolérable** et **le délai de restauration mesuré**. Si restaurer prend deux heures et que quatre heures d'arrêt sont acceptables, **l'option A suffit** — et coûte trois fois moins.

⚠️ **Le point que le mode B cache** : une réplication **asynchrone** copie les transactions avec un léger retard. En cas de bascule, **les dernières transactions peuvent être perdues**. C'est un compromis entre performance et perte de données tolérable — et il doit figurer au registre des compromis, §46.5.

#### 20.4 Ce qu'il fait à la donnée

Dans ce modèle, elle **porte l'état durable principal** du service.

⚠️ **Ce qu'il ne faut pas en conclure** : la base n'*est* pas la donnée. Elle est **un endroit où une partie de la donnée réside**. Le chapitre 32 montrera que la même donnée existe simultanément dans des réplicas, des sauvegardes, des exports, des rapports, des environnements de recette et des messageries. Confondre les deux conduit à sous-évaluer un périmètre d'impact — §32.2.

#### 20.5 S'il disparaît

Dans le modèle à trois niveaux employé ici, ce qui en dépend s'arrête. Et contrairement aux couches au-dessus, sa perte peut être **définitive** : un serveur web se réinstalle en une heure, une base perdue sans sauvegarde valide ne se reconstitue pas.

📌 **Ce qui nuance ce modèle**, et qu'il faut connaître :

| Cas | Effet réel |
|---|---|
| L'application dispose d'un cache | Elle sert des données en lecture pendant un temps |
| Les écritures sont mises en file | Elles sont rejouées ensuite, sans perte |
| L'application utilise plusieurs sources de données | Seule une partie du service s'arrête |
| Base répliquée avec bascule automatique | Interruption courte, **si la bascule fonctionne** — ⚠️ *principe de preuve* |

🔥 **SCÉNARIO — la base répond, le service est lent puis s'arrête**

| Question | Réponse |
|---|---|
| Symptôme | Ralentissement progressif sur deux heures, puis arrêt |
| Hypothèse naïve | « Trop de charge » |
| Dépendance réelle | **Le stockage sous-jacent est saturé.** La base fonctionne, elle ne peut plus écrire |
| Ce que le schéma aurait dû montrer | Que la base dépend d'un stockage partagé, souvent commun à d'autres machines |
| Concevoir différemment | Superviser l'espace disponible, pas seulement l'état du service |

⚠️ **Ce scénario illustre une dépendance en cascade que les schémas ne montrent jamais** : base → stockage → et parfois le même stockage porte l'hyperviseur qui héberge la base.

#### 20.6 Sur un schéma

En bas, dans la grande majorité des représentations. Fréquemment en un seul exemplaire, parfois en deux avec une mention de réplication.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est en cluster » | Plusieurs nœuds de base | **Actif/passif ou actif/actif ? Stockage partagé ou non ?** |
| « On a de la réplication » | Une copie existe | **Synchrone ou asynchrone ?** Combien de données peut-on perdre ? |
| « La bascule est automatique » | Un mécanisme existe | **Quand a-t-elle été testée pour la dernière fois ?** — *principe de preuve* |
| « La base est saturée » | Un seuil est atteint | Espace disque · connexions · mémoire · trois causes distinctes |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Conserver des données cohérentes et durables | **Souvent le point de rupture principal** |
| Gérer les accès concurrents | Une administration spécialisée |
| Se répliquer pour la disponibilité | Une complexité importante · **un basculement à tester** · une perte possible en asynchrone |

⚠️ **Principes du coût et de preuve, appliqués** : une réplication non testée n'est pas une redondance, c'est une **croyance**. Elle figure au schéma, elle rassure, et personne ne sait si le basculement fonctionne.

---

### Chapitre 21 — Le serveur de fichiers

#### 21.1 À quoi ça sert

Stocker des documents accessibles par les postes, avec des droits par dossier.

**Pourquoi ça existe encore.** Malgré les outils collaboratifs, le partage de fichiers reste le socle documentaire de la majorité des organisations — parce qu'il est simple, universel, et qu'il ne demande aucun apprentissage.

#### 21.2 Ce qu'il fait à la donnée

Il la conserve **sans la structurer**. C'est ce qui le rend à la fois indispensable et incontrôlable : **personne ne sait exactement ce qu'il contient**. C'est le sujet du chapitre 8 du volume Asset Management.

#### 21.3 Le problème des droits

```
   Année 1    Une arborescence propre, des droits par service
   Année 2    « Marie a besoin d'accéder à ce dossier »  → droit individuel
   Année 3    Un projet transverse  → un groupe créé pour l'occasion
   Année 4    Le projet est fini. Le groupe existe toujours
   Année 5    Marie change de service. Son droit individuel reste
   Année 8    Plus personne ne sait qui a accès à quoi
```

⚠️ **Les droits sur un partage de fichiers ne se réduisent jamais spontanément.** Chaque exception ajoutée y reste, et l'arborescence devient inauditable en quelques années. C'est le même mécanisme que les règles de pare-feu — §10.3 — et la même conclusion : **ce qui s'accumule sans processus de retrait devient ingérable**.

#### 21.4 S'il disparaît

Les utilisateurs perdent leurs documents partagés.

⚠️ **Une distinction importante pour la vue service** : **le service métier ne s'arrête pas toujours, mais le travail s'arrête.** Un service de commande en ligne continue de fonctionner sans le partage de fichiers ; l'équipe qui le pilote, non. C'est le §35.4 — dégradation contre arrêt.

🔥 **SCÉNARIO — le partage est chiffré par un rançongiciel**

| Question | Réponse |
|---|---|
| Symptôme | Les fichiers sont illisibles. Le serveur fonctionne |
| Hypothèse naïve | « Le serveur a été compromis » |
| Dépendance réelle | **Un poste utilisateur**, avec les droits de son utilisateur — mini-lab 3 |
| Ce que le schéma aurait dû montrer | **Les postes**, absents de la quasi-totalité des schémas — §6.1 |
| Ce qui décide de la suite | **La sauvegarde est-elle atteignable depuis le même compte ?** Si oui, elle est chiffrée aussi |

⚠️ **La dernière ligne est celle qui décide de la gravité.** Un rançongiciel qui atteint les sauvegardes transforme un incident en catastrophe. **La question de conception : la sauvegarde est-elle accessible depuis le réseau bureautique, et avec quel compte ?**

#### 21.5 Sur un schéma

Une boîte isolée en zone interne, souvent sans trait — comme l'annuaire. Tous les postes s'y connectent, personne ne le dessine.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur le P: » | Un lecteur réseau monté | **Vers quel serveur ? Quels droits ?** |
| « Tout le monde y a accès » | Les droits sont larges | « Tout le monde » inclut-il les comptes de service et les prestataires ? |
| « On a des snapshots » | Des copies existent | **Sont-elles atteignables par un compte compromis ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Partager des documents avec des droits | **Une arborescence de droits qui devient inauditable** |
| Centraliser pour sauvegarder | Un volume qui croît sans limite naturelle |
| Offrir un accès simple | **Une cible de choix pour un rançongiciel** |

---

### Chapitre 22 — La messagerie

#### 22.1 À quoi ça sert

Recevoir, stocker et distribuer les courriels, et servir de **moyen de récupération** pour de nombreux services.

#### 22.2 Ce qu'il fait à la donnée

Il en conserve des années, souvent sans limite, et c'est **le plus grand entrepôt non structuré de l'organisation** — contrats, mots de passe échangés, pièces jointes sensibles, historique de décisions.

#### 22.3 La dépendance croisée, et pourquoi elle est structurante

```
   Un service quelconque
        │
        └── « mot de passe oublié » ──► envoie un lien à l'adresse
                                          de messagerie
                                              │
                                              ▼
                                    Qui contrôle la messagerie
                                    contrôle la RÉINITIALISATION
                                    de ce service
```

⚠️ **La conséquence, souvent mal évaluée** : la messagerie est simultanément **une voie d'entrée majeure** et **le point de récupération de nombreux comptes**. Une compromission de messagerie est rarement une compromission de messagerie seule.

**Ce que cela impose en conception** : les comptes d'administration ne doivent pas dépendre de la messagerie pour leur récupération — sinon la chaîne est circulaire.

#### 22.4 Deux architectures

```
  A — MESSAGERIE INTERNE
      Internet ──► [ relais ] ──► [ serveur de messagerie ]
      → maîtrise complète · données chez vous
      → un service critique à exploiter, corriger, sauvegarder
      → une exposition permanente sur Internet

  B — MESSAGERIE EN LIGNE
      Internet ──► [ service du fournisseur ]
                          │
                    identités synchronisées
                          ▼
                   [ annuaire interne ]
      → plus de serveur à exploiter
      → une dépendance de disponibilité hors de vos mains
      → ⚠️ le lien d'identités devient critique — §40.2
```

⚠️ **Ce que le passage de A à B ne supprime pas** : les données existent toujours, la voie d'entrée existe toujours, et la dépendance croisée du §22.3 existe toujours. **Ce qui change, c'est qui exploite** — et le fait que les cinq actions du chapitre 43 ne s'appliquent plus à l'infrastructure, mais seulement à la configuration, aux identités et aux données — §42.5.

#### 22.5 S'il disparaît

| Effet | Portée |
|---|---|
| Plus de courriels | Immédiat, visible |
| **Plus de réinitialisation de mot de passe** | Différé, et bloquant |
| Plus de notifications applicatives | Différé — des processus métier s'arrêtent silencieusement |

🔥 **SCÉNARIO — la messagerie tombe, et un processus métier s'arrête sans que personne ne le voie**

| Question | Réponse |
|---|---|
| Symptôme | Trois jours plus tard : des commandes n'ont pas été validées |
| Hypothèse naïve | « Les commerciaux n'ont pas fait leur travail » |
| Dépendance réelle | **Le circuit de validation passe par des notifications par courriel** |
| Ce que le schéma aurait dû montrer | Que la messagerie est une **dépendance de processus**, pas seulement un outil |
| Concevoir différemment | Identifier les processus métier qui en dépendent — **presque personne ne l'a fait** |

#### 22.6 Sur un schéma

Un relais en zone démilitarisée, et un serveur ou un service en ligne à l'intérieur. **Le relais est souvent le seul élément dessiné.**

⚠️ **Et il reste souvent dessiné après une migration** — c'est l'anomalie n° 1 du cas de synthèse A : un relais devenu inutile, toujours exposé, que plus personne ne surveille.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est passé sur le cloud » | La messagerie est externalisée | **Le relais interne existe-t-il encore ? Est-il encore exposé ?** |
| « Les mails ne partent pas » | Un blocage d'envoi | Relais · réputation · quota · trois causes distinctes |
| « Il a cliqué sur un lien » | Un poste est peut-être compromis | Ce qui compte n'est pas le clic, c'est **ce que ce poste atteint** — §6.2 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Communiquer avec l'extérieur | **Une voie d'entrée majeure, et historiquement l'une des plus fréquentes** |
| Conserver l'historique des échanges | Un volume et une valeur qui croissent indéfiniment |
| Servir de secours d'authentification | **Une dépendance croisée** |
| Porter des notifications de processus | **Des processus métier qui s'arrêtent silencieusement** en cas de panne |

---

### Chapitre 23 — La virtualisation

#### 23.1 À quoi ça sert

Faire tourner plusieurs machines logiques sur une machine physique, et les déplacer entre machines physiques.

**Pourquoi ça existe.** Un serveur physique dédié à une application utilise une fraction de sa capacité. La virtualisation densifie — et, accessoirement, elle rend une machine **déplaçable**, ce qui change complètement la gestion des pannes matérielles.

#### 23.2 Les quatre objets à distinguer

**C'est la distinction qui manque dans la plupart des schémas.**

| Objet | Ce que c'est | Ce qui se passe s'il tombe |
|---|---|---|
| **L'hôte** | La machine physique | Ses machines s'arrêtent, **ou basculent si le mécanisme existe et fonctionne** |
| **Le stockage partagé** | Où résident les disques des machines | **Tout s'arrête** — c'est le point de rupture réel de la plupart des plateformes |
| **Le réseau de la plateforme** | Ce qui relie hôtes et stockage | Les machines perdent leurs disques — effet identique |
| **Le plan de gestion** | La console qui pilote l'ensemble | Rien immédiatement · **on ne peut plus rien administrer, ni créer, ni basculer** |

⚠️ **Le stockage partagé est un point de rupture rarement dessiné, et aux conséquences très larges.** Dix hôtes redondés, quarante machines réparties, **un seul stockage** : c'est une configuration très répandue, et son point de rupture est l'objet qui ne figure sur aucun schéma logique.

#### 23.3 La redondance qui n'en est pas

🖼 **SCHÉMA 23.1 — Ce que le schéma logique cache**

```
   CE QUE LE SCHÉMA MONTRE          LA RÉALITÉ PHYSIQUE

      [web 1] [web 2] [web 3]         ┌──── HÔTE A ────┐
           redondés                   │ web1 web2 web3 │
                                      └────────────────┘
                                      L'hôte tombe : les trois tombent.
```

**Les quatre questions à poser devant toute redondance**, et elles découlent du principe de preuve :

```
1. Les exemplaires sont-ils sur des HÔTES différents ?
2. Ces hôtes utilisent-ils le MÊME STOCKAGE ?
3. Sont-ils dans la même BAIE, sur la même ALIMENTATION ?
4. Sont-ils sur le MÊME SITE ?
```

⚠️ **Une réponse « non » à la question 1 suffit à annuler la redondance.** Une réponse « oui » aux trois suivantes la réduit à une protection contre la seule panne d'hôte — ce qui est déjà utile, mais bien moins que ce que le schéma laisse croire.

📌 **Il existe des mécanismes qui empêchent deux machines d'un même rôle de se retrouver sur le même hôte.** Ils sont efficaces, et **ils doivent être configurés** : par défaut, la plateforme place où elle veut.

🔭 **À RECONNAÎTRE — VDI et publication d'applications**

**① Qu'est-ce que c'est.** *Virtual Desktop Infrastructure* — le poste de travail ne s'exécute plus devant l'utilisateur, mais dans le centre de données. **L'utilisateur n'a plus qu'un écran, un clavier et une session distante.**

**② Quel problème il résout.** Les données ne quittent pas le centre · un poste perdu ne contient rien · les prestataires distants travaillent sans qu'on leur confie quoi que ce soit · un parc hétérogène devient uniforme.

**③ Ce que cela change au raisonnement.**

```
   POSTE CLASSIQUE
      [ utilisateur ] ──► [ son poste ] ──► application

   VDI
      [ terminal ] ──session distante──► [ poste centralisé ] ──► application
           │                                      │
      ne contient rien              c'est ICI que tout s'exécute
```

> **La question que le VDI oblige à poser, et qui vaut au-delà de lui** : *où s'exécute réellement l'application ?*

⚠️ **Deux variantes à distinguer** : on peut publier **un poste complet** — l'utilisateur voit un bureau — ou **une application seule**, qui apparaît dans son environnement habituel. **Citrix** est le nom historique et majeur de cet écosystème ; vous l'entendrez employé comme synonyme de la fonction elle-même.

**④ Les dépendances que cela crée.**

| Nouvelle dépendance | Effet |
|---|---|
| **Le réseau** | Une coupure ne ralentit plus le travail : **elle l'arrête** |
| **La plateforme centrale** | Une panne affecte tous les utilisateurs simultanément |
| **Le service de courtage de session** | Composant peu connu, et point de rupture réel |
| L'impression, les périphériques | Chaque redirection est une intégration à maintenir |

⚠️ **Le renversement le plus important** : dans un parc classique, une panne réseau dégrade le travail. **En VDI, elle l'interrompt totalement** — le poste de l'utilisateur n'est plus chez lui.

**⑤ Le coût.** Une infrastructure centrale dimensionnée pour tous les utilisateurs simultanés · une expérience dégradée sur les usages graphiques ou latents · **une concentration du risque** · une compétence spécialisée.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « Ils sont en VDI » | **Poste complet ou application publiée ?** |
| « Les prestas passent par Citrix » | Bon modèle — §6.3, poste non maîtrisé | **Que peuvent-ils faire depuis la session ?** |
| « Le VDI rame » | Réseau · plateforme · stockage · trois causes distinctes |

---

🔭 **À RECONNAÎTRE — hyperconvergence**

**① Qu'est-ce que c'est.** Une architecture où **le calcul et le stockage sont réunis dans des nœuds standardisés**, pilotés comme un ensemble par une couche logicielle.

**② Quel problème elle résout.** L'architecture classique sépare les deux, avec un réseau de stockage dédié entre les deux — §23.4. Cela fonctionne, et cela demande trois compétences distinctes et trois équipes.

**③ Ce que cela change.**

```
   ARCHITECTURE CLASSIQUE
      [ serveurs ] ═══ réseau de stockage ═══ [ baie ]
      → trois éléments · trois compétences · trois contrats

   HYPERCONVERGENCE
      [ nœud : calcul + stockage ]
      [ nœud : calcul + stockage ]   ──► cluster piloté par logiciel
      [ nœud : calcul + stockage ]
      → un seul élément · une seule compétence · on ajoute un nœud pour croître
```

⚠️ **④ Le point qui compte, et il est contre-intuitif** :

> **La simplification physique déplace la complexité dans le logiciel.**

Il n'y a plus de baie à administrer — **il y a une couche de stockage distribuée**, avec ses règles de réplication, son quorum, et ses comportements en cas de perte de nœuds. Le point de rupture n'a pas disparu, **il a changé de nature**.

**⑤ Le coût.** Une croissance par blocs — on ajoute calcul et stockage ensemble, même si l'on n'a besoin que de l'un · une dépendance forte à un fournisseur · **une compétence sur le comportement distribué**, pas sur du matériel.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est en HCI » | **Combien de nœuds ? Combien peut-on en perdre ?** — voir le quorum, §23.6 |
| « On n'a plus de SAN » | Le stockage est distribué sur les nœuds. **Avec quelle réplication ?** |
| « On ajoute un nœud pour du stockage » | On ajoute aussi du calcul, et on le paie |

#### 23.4 Le stockage — bloc, fichier, objet

> **Le composant le plus présent sur les schémas d'infrastructure et le moins compris.** Il est aussi le point de rupture caché de la plupart des plateformes de virtualisation — §23.2.

##### Les trois familles

```
  BLOC       « Voici un disque. Débrouille-toi. »
             Le serveur voit un volume brut, il y installe son système
             de fichiers. Utilisé par : machines virtuelles, bases de données.

  FICHIER    « Voici un dossier partagé. »
             Plusieurs serveurs montent le même partage et y lisent
             et écrivent des fichiers. Utilisé par : partages bureautiques,
             données applicatives partagées.

  OBJET      « Voici une adresse. Dépose ton fichier, récupère-le par son nom. »
             Pas de système de fichiers, pas de montage. On dépose et on lit
             par une interface applicative. Utilisé par : sauvegardes,
             archives, contenus web, données massives.
```

| | **Bloc** | **Fichier** | **Objet** |
|---|---|---|---|
| Ce que le serveur voit | Un disque | Un dossier réseau | **Rien — une adresse à appeler** |
| Plusieurs serveurs simultanément | Difficile | **Oui, c'est son objet** | Oui |
| Modification partielle d'un contenu | Oui | Oui | **Non — on remplace l'objet entier** |
| Sur un schéma | Un lien vers une baie | Un serveur de fichiers | **Souvent un nuage, ou rien** |
| Qui l'utilise typiquement | Virtualisation, bases | Postes, applications partagées | Sauvegardes, archives, web |

⚠️ **La ligne « modification partielle » explique la plupart des choix.** Une base de données réécrit constamment de petits fragments : elle a besoin de **bloc**. Une archive s'écrit une fois et se relit : **objet** convient, et coûte bien moins cher.

##### Les architectures de stockage sur un schéma

```
  A — STOCKAGE LOCAL
      [ serveur ] avec ses disques
      → simple · aucune dépendance externe
      → la machine ne peut pas se déplacer — pas de bascule à chaud

  B — STOCKAGE PARTAGÉ EN RÉSEAU (bloc)
      [ hôte 1 ] ──┐
      [ hôte 2 ] ──┼──► [ baie de stockage ]
      [ hôte 3 ] ──┘
      → les machines se déplacent entre hôtes
      → ⚠️ LA BAIE EST LE POINT DE RUPTURE RÉEL — §23.2
      → un réseau de stockage dédié, souvent invisible sur les schémas

  C — SERVEUR DE FICHIERS (fichier)
      [ postes et serveurs ] ──► [ serveur de fichiers ]
      → partage simple · droits par dossier — §21
      → cible de choix pour un rançongiciel

  D — STOCKAGE OBJET
      [ applications ] ──interface──► [ stockage objet ]
      → capacité quasi illimitée · souvent chez un tiers
      → ⚠️ accessible par une clé, pas par le réseau : un filtrage
        réseau ne le protège pas
```

⚠️ **Le mode D mérite une attention particulière en lecture.** Un stockage objet n'est pas atteint par le réseau interne mais **par une interface applicative avec une clé**. Cela signifie que :

- il peut être joignable **depuis n'importe où**, si la clé fuit ;
- un pare-feu ne le protège pas ;
- **il n'apparaît sur aucun schéma réseau**, parce qu'il n'y a pas de lien à dessiner.

C'est l'un des composants les plus fréquemment oubliés des inventaires — volume Asset Management.

##### Réplication, instantané, sauvegarde — les trois qu'on confond

> **La confusion la plus lourde de conséquences du chapitre.**

| | **Réplication** | **Instantané** | **Sauvegarde** |
|---|---|---|---|
| Ce que c'est | Une copie **continue** vers un autre stockage | Un **état figé** à un instant, sur le même stockage | Une copie **indépendante**, ailleurs |
| Protège contre | La panne d'un stockage | Une **erreur récente** — suppression, mise à jour ratée | **Tout**, y compris la perte du site |
| Ne protège **pas** contre | **Une suppression** — elle est répliquée aussitôt | **La perte du stockage** — l'instantané est dessus | Rien, si elle n'a jamais été testée |
| Délai de restauration | Immédiat, par bascule | Minutes | **Heures à jours** |
| Coût | Élevé — un second stockage complet | Faible | Moyen |

⚠️ **Les trois lignes du milieu contiennent l'essentiel** :

**Une réplication n'est pas une sauvegarde.** Elle copie tout, y compris les erreurs. Un fichier supprimé par erreur est supprimé des deux côtés en quelques secondes. **Un rançongiciel est répliqué.**

**Un instantané n'est pas une sauvegarde.** Il vit sur le même stockage que la donnée d'origine. Si la baie tombe, ou si elle est chiffrée, **les instantanés disparaissent avec**.

**Une sauvegarde n'en est une que si elle est indépendante** — autre support, autre système, **idéalement hors ligne ou en écriture unique**. Et si elle n'a jamais été restaurée pour de vrai, c'est une croyance — *principe de preuve*.

🔥 **SCÉNARIO — « on a des snapshots » ne suffit pas**

| Question | Réponse |
|---|---|
| Symptôme | Un rançongiciel a chiffré les partages. L'équipe annonce des instantanés toutes les heures |
| Hypothèse naïve | « On restaure, on perd une heure » |
| Dépendance réelle | **Les instantanés sont sur la même baie**, et le compte compromis pouvait les supprimer |
| Ce que le schéma aurait dû montrer | Où vivent les instantanés, et qui peut les supprimer |
| Concevoir différemment | Une copie **hors du périmètre atteignable** par un compte d'exploitation |

🔥 **SCÉNARIO — la baie tombe, dix hôtes redondés s'arrêtent**

| Question | Réponse |
|---|---|
| Symptôme | Dix hôtes de virtualisation en bonne santé. **Quarante machines arrêtées** |
| Hypothèse naïve | « Un problème d'hyperviseur » |
| Dépendance réelle | **Le stockage partagé** — la dépendance commune que le schéma logique ne montre pas |
| Ce que le schéma aurait dû montrer | La baie, et le fait que tous les hôtes en dépendent |
| Concevoir différemment | Un second stockage, avec réplication **et bascule testée** — ou accepter et le déclarer |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur la baie » | Stockage partagé en bloc | **Une seule baie ? C'est le point de rupture réel** |
| « On a des snapshots » | Des états figés existent | **Sur le même stockage ? Qui peut les supprimer ?** |
| « C'est répliqué » | Une copie continue existe | **Ce n'est pas une sauvegarde** — une suppression est répliquée |
| « C'est dans le bucket » | Stockage objet | **Joignable par clé, pas par le réseau.** Qui a la clé ? |
| « On est en NAS » | Stockage fichier | Partagé par combien de serveurs ? Qui a les droits ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Déplacer une machine entre hôtes | **Un stockage partagé qui devient la dépendance commune** |
| Partager des données entre serveurs | Des droits à tenir · une performance à surveiller |
| Stocker sans limite (objet) | **Un accès par clé, qu'aucun filtrage réseau ne protège** |
| Restaurer rapidement (instantané) | **Aucune protection contre la perte du stockage** |
| Restaurer en toute circonstance (sauvegarde) | Un délai long · un dispositif à exploiter · **un test à faire** |

🔭 **À RECONNAÎTRE — réseau de stockage dédié**

**① Qu'est-ce que c'est.** Un réseau **distinct du réseau de données**, réservé aux échanges entre les serveurs et les baies de stockage. **Fibre Channel** en est la technologie historique et dominante.

**② Quel problème il résout.** Les échanges avec le stockage sont massifs et sensibles à la latence. Les isoler du trafic ordinaire évite qu'une sauvegarde ne ralentisse une application.

**③ Ce que cela change en lecture de schéma.**

```
   [ serveur 1 ] ──┬── réseau Ethernet ──► le reste du SI
                   └── réseau de stockage ──► [ baie ]
                          ▲
             DEUX réseaux, deux cartes, deux jeux d'équipements
             Le second n'apparaît presque jamais sur un schéma logique
```

**Le vocabulaire à reconnaître** :

| Terme | Ce que c'est |
|---|---|
| **SAN** | Le réseau de stockage lui-même |
| **Fibre Channel** | La technologie dominante de ces réseaux |
| **Commutateur FC** | L'équipement qui les relie — l'équivalent du commutateur Ethernet |
| **Zoning** | Qui a le droit de parler à quoi — l'équivalent d'un filtrage |
| **LUN** | Le volume présenté à un serveur |

**④ Ce que cela change.** Une infrastructure entière, avec ses équipements, ses règles et ses pannes, **qui ne figure sur aucun schéma applicatif** — et qui est pourtant le chemin par lequel toutes les données transitent.

**⑤ Le coût.** Une compétence rare · des équipements dédiés · une évolution coûteuse. **C'est ce qui explique en partie l'attrait de l'hyperconvergence.**

**⑥ En réunion** : *« c'est sur le SAN »* → **combien de baies ? les serveurs voient-ils tous les mêmes volumes ?** · *« il y a un problème de zoning »* → un serveur ne voit plus son volume, **sans qu'aucune panne matérielle ne soit en cause**.

---

🔭 **À RECONNAÎTRE — immutabilité du stockage**

**① Qu'est-ce que c'est.** Un mécanisme qui **empêche la modification ou la suppression d'un objet pendant une durée déterminée**, y compris par un compte administrateur. On l'appelle couramment *Object Lock* sur les stockages objet.

**② Quel problème il résout.** Celui du §23.4 : une sauvegarde atteignable par un compte compromis est chiffrée ou supprimée avec le reste. **L'immutabilité rend cette suppression impossible, même avec les droits nécessaires.**

**③ Où on le rencontre.** Sur les stockages objet servant de destination de sauvegarde, et comme argument commercial majeur des solutions de protection contre les rançongiciels.

**④ Ce que cela change.**

```
   SAUVEGARDE ORDINAIRE
      compte compromis ──► peut supprimer ──► plus de sauvegarde

   SAUVEGARDE IMMUABLE
      compte compromis ──► ne peut pas supprimer avant la fin du délai
      ⚠️ MAIS : peut cesser d'en créer de nouvelles
```

⚠️ **Les deux réserves à connaître, et elles sont importantes** :

> **L'immutabilité n'est pas une sauvegarde à elle seule.** Elle protège une copie existante ; elle ne garantit ni que cette copie soit complète, ni qu'elle soit exploitable.

> **Une sauvegarde non modifiable reste inutile si elle n'a jamais été restaurée.** C'est le principe de preuve appliqué au stockage.

**⑤ Le coût.** Un volume qui ne peut plus être réduit avant l'échéance — **une erreur de configuration de durée coûte cher** · une gestion du cycle de vie plus rigide.

**⑥ En réunion** : *« nos sauvegardes sont immuables »* → **pour combien de temps ? l'administrateur du stockage peut-il modifier ce délai ? et quand a-t-on restauré pour la dernière fois ?**

---

🔭 **À RECONNAÎTRE — quorum**

> **Plus fondamental que son apparence**, et c'est le concept qui explique pourquoi trois nœuds ne signifient pas trois fois plus de sécurité.

**① Qu'est-ce que c'est.** Le mécanisme par lequel **un ensemble distribué décide quelle partie a le droit de continuer** lorsque ses membres ne peuvent plus communiquer entre eux.

**② Quel problème il résout.** Le lecteur voit trois nœuds et pense *« redondant »*. Mais que se passe-t-il si le réseau se coupe **entre** les nœuds ?

```
   AVANT              [ A ] ── [ B ] ── [ C ]     tout va bien

   COUPURE            [ A ] ──X── [ B ] ── [ C ]

   SANS QUORUM        A pense être seul survivant → il continue
                      B et C pensent que A est mort → ils continuent
                      ⚠️ DEUX systèmes actifs, deux vérités divergentes
                         → c'est le « split-brain »

   AVEC QUORUM        A est en minorité (1 sur 3) → IL S'ARRÊTE
                      B et C sont majoritaires (2 sur 3) → ils continuent
                      → une seule vérité subsiste
```

⚠️ **③ Ce que cela impose, et qui surprend** :

> **Un membre en bonne santé peut être contraint de s'arrêter, non parce qu'il est en panne, mais parce qu'il ne peut pas prouver qu'il est du bon côté.**

**Deux conséquences pratiques** :

| Conséquence | Explication |
|---|---|
| **Un nombre impair est préférable** | Avec deux nœuds, une coupure donne 1 contre 1 : **aucun n'est majoritaire, tout s'arrête** |
| **Il faut parfois un arbitre** | Un troisième élément — un témoin, un disque, un service tiers — dont le seul rôle est de départager |

**④ Où on le rencontre.** Clusters de bases de données · plateformes de virtualisation · stockage distribué · orchestrateurs de conteneurs · hyperconvergence. **Partout où plusieurs machines doivent se mettre d'accord.**

**⑤ Le coût.** Un membre ou un arbitre supplémentaire · **un comportement en cas de coupure qu'il faut connaître avant l'incident** · une architecture réseau entre nœuds qui devient critique.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a deux nœuds en cluster » | **Que se passe-t-il si le lien entre eux tombe ?** Y a-t-il un arbitre ? |
| « Le cluster s'est arrêté tout seul » | **Perte de quorum** — les nœuds ont refusé de continuer sans majorité |
| « On a trois nœuds sur deux sites » | **Deux d'un côté, un de l'autre.** Si le site majoritaire tombe, le troisième s'arrête aussi |

⚠️ **La dernière ligne est un piège classique de conception multi-sites** : trois nœuds répartis 2+1 ne protègent pas contre la perte du site qui en porte deux. **Il faut un arbitre sur un troisième emplacement.**

#### 23.6 Le plan de gestion

**Le composant le moins dessiné et le plus critique de la partie.**

| | |
|---|---|
| Ce que c'est | La console qui pilote l'ensemble des hôtes et des machines |
| Ce qu'il permet | Créer, supprimer, déplacer, cloner, **accéder à la console d'une machine sans passer par son système** |
| Ce qu'une compromission donne | **L'accès à toutes les machines qu'il pilote** — y compris en copiant leurs disques |
| Sur les schémas | **Jamais** |

⚠️ **La troisième ligne mérite d'être développée.** Qui contrôle le plan de gestion peut **cloner une machine** et en examiner le disque hors ligne — sans jamais s'authentifier sur son système, sans laisser de trace dans ses journaux. **Aucun contrôle placé à l'intérieur d'une machine ne protège contre cela.**

C'est le §3.4 et le chapitre 27 : **le chemin d'administration est plus puissant que ce qu'il administre**, et il n'est pas représenté.

#### 23.7 S'il disparaît

🔥 **SCÉNARIO — deux machines redondées tombent ensemble**

| Question | Réponse |
|---|---|
| Symptôme | Les deux exemplaires d'un service s'arrêtent simultanément |
| Hypothèse naïve | « Un problème applicatif commun » |
| Dépendance réelle | **Elles partagent l'hôte** — ou le stockage, ou l'alimentation |
| Ce que le schéma aurait dû montrer | La couche physique sous les machines |
| Concevoir différemment | Une règle d'anti-affinité, configurée **et vérifiée** |

🔥 **SCÉNARIO — le plan de gestion tombe pendant une panne**

| Question | Réponse |
|---|---|
| Symptôme | Un hôte est en panne. **La bascule ne se déclenche pas** |
| Hypothèse naïve | « La bascule ne fonctionne pas » |
| Dépendance réelle | **C'est le plan de gestion qui l'orchestre.** S'il est lui-même hébergé sur la plateforme, il peut être tombé avec |
| Ce que le schéma aurait dû montrer | Où s'exécute le plan de gestion |
| Concevoir différemment | Ne pas héberger le plan de gestion sur la plateforme qu'il pilote — **ou en avoir conscience** |

⚠️ **Ce second scénario est une dépendance circulaire classique**, et on la retrouve partout : l'outil qui répare dépend de ce qu'il répare. **C'est une question à poser systématiquement en conception.**

#### 23.8 Ce qu'il fait à la donnée

L'hôte ne la lit pas, mais il **y a accès** : qui contrôle l'hyperviseur contrôle la mémoire et les disques de toutes les machines qu'il porte.

#### 23.9 Sur un schéma

Souvent absente. On dessine des serveurs sans dire lesquels sont virtuels ni sur quoi ils reposent.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a deux nœuds mais le stockage est commun » | La redondance porte sur les hôtes seuls | **C'est une phrase précieuse** — elle nomme exactement le point de rupture |
| « On va migrer la VM à chaud » | La déplacer sans l'arrêter | Suppose un stockage partagé — **donc une dépendance commune** |
| « C'est virtualisé » | La machine est logique | **Sur quel hôte ? Avec quoi d'autre ?** |
| « On a du HA sur le cluster » | Un mécanisme de bascule existe | **Testé quand ? Le plan de gestion est-il hors du cluster ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Densifier, déplacer, provisionner rapidement | **Un plan de gestion dont la compromission donne tout** |
| Basculer une machine en cas de panne d'hôte | **Un stockage partagé qui devient le point de rupture réel** |
| Créer une machine en minutes | **Des machines créées sans être déclarées** — volume Asset Management |
| Migrer à chaud | Une dépendance forte au stockage partagé |

🏭 **TROIS TAILLES** — Atelier Martin : deux hôtes, pas de stockage partagé, pas de bascule automatique — **la contrainte de continuité ne le justifie pas**. HELIOMED : six hôtes, stockage partagé, bascule testée deux fois par an. Novaris : plusieurs centaines d'hôtes, **parce qu'elle exploite quatre mille machines** — pas parce qu'elle est grande.

---

#### 🔬 Mini-lab 6 — Attribuer un rôle à sept serveurs

**Objectif** — Proposer un rôle probable à partir des seules connexions, et dire ce qui reste à vérifier.
**Durée** 30 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 18 à 23

**Les données** — sept serveurs, et les connexions observées sur une journée :

```
SRV-01  reçoit : 443 depuis la DMZ        émet : 8080 vers SRV-02, 389 vers SRV-06
SRV-02  reçoit : 8080 depuis SRV-01       émet : 1433 vers SRV-03, 389 vers SRV-06
SRV-03  reçoit : 1433 depuis SRV-02       émet : rien (hors sauvegarde)
SRV-04  reçoit : 445 depuis 600 postes    émet : 389 vers SRV-06
SRV-05  reçoit : 25 depuis la DMZ         émet : 443 vers Internet, 389 vers SRV-06
SRV-06  reçoit : 389 et 636 de partout    émet : 389 vers SRV-07
SRV-07  reçoit : 389 depuis SRV-06        émet : 389 vers SRV-06
```

❓ **Questions**
1. Quel est le rôle de chaque serveur ?
2. Lesquels sont des points de rupture ?
3. Qu'est-ce qui manque dans ces données ?

---

**Corrigé**

**1. Les rôles**

| Réf | Rôle | Raisonnement |
|---|---|---|
| **SRV-01** | Serveur web | Reçoit du web depuis la DMZ, relaie vers un applicatif |
| **SRV-02** | Serveur applicatif | Entre le web et la base — position et ports |
| **SRV-03** | Base de données | Reçoit du 1433, **n'émet rien** : le fond de la pile |
| **SRV-04** | Serveur de fichiers | Port 445, six cents postes |
| **SRV-05** | Relais de messagerie | Port 25 entrant, 443 sortant |
| **SRV-06** | Contrôleur d'annuaire | **Reçoit de partout**, ports 389 et 636. ⚠️ Ces ports ne montrent que l'interrogation |
| **SRV-07** | Second contrôleur, **probablement** | Échanges mutuels avec SRV-06 — compatibles avec une réplication, à confirmer |

**2. Les points de rupture**

| Serveur | Rupture ? | Nuance |
|---|---|---|
| SRV-01 | ⚠️ **Indéterminé** | Un seul est listé, mais il peut y en avoir d'autres non observés |
| **SRV-02** | ✅ **Oui** | Seul applicatif, tout le service en dépend |
| **SRV-03** | ✅ **Oui, le plus grave** | Base unique, perte potentiellement définitive |
| **SRV-04** | ✅ Oui | Pour le partage de fichiers uniquement |
| **SRV-05** | ✅ Oui | Pour la messagerie entrante |
| SRV-06 / 07 | ⚠️ **Indéterminé** | Deux contrôleurs suggèrent une redondance. **Principe de preuve : partagent-ils un hôte, un stockage, un site, une alimentation ?** Le dossier ne le dit pas |

**3. Ce qui manque** — et c'est la vraie question du lab :

| Manquant | Pourquoi c'est décisif |
|---|---|
| **La résolution de noms** | Aucun flux port 53 n'apparaît. Elle existe pourtant : sans elle, aucune de ces connexions n'aurait lieu. **Elle est hors du périmètre d'observation** |
| **La synchronisation d'horloge** | Idem. Sans elle, les authentifications 389 échoueraient |
| **Les hôtes de virtualisation** | Ces sept serveurs sont peut-être trois machines physiques |
| **Les chemins d'administration** | Aucun flux 22 ou 3389 : soit ils ne sont pas observés, soit l'administration passe ailleurs |
| **Les sauvegardes** | Mentionnées entre parenthèses, non détaillées |

**Les trois erreurs attendues**

1. **Conclure que SRV-01 n'est pas un point de rupture** parce qu'il « doit y en avoir d'autres ». Les données ne le disent pas — la bonne réponse est *indéterminé*.
2. **Oublier la résolution de noms** parce qu'elle n'apparaît dans aucune ligne. C'est le piège central : **une observation de flux ne montre que ce qu'on a observé**.
3. **Conclure que SRV-06 et SRV-07 forment une redondance établie.** Les échanges mutuels en sont un **indice**, pas une preuve : rien ne dit qu'ils ne partagent pas un hôte, un stockage ou un site. **Principe de preuve** — seul un test établit une capacité de basculement.

---

> ### 🎓 À ce stade de la Partie III, vous savez…
>
> ✓ que l'on sépare des serveurs **parce qu'ils n'ont pas les mêmes contraintes** — disponibilité, cycle, charge, conséquence d'une compromission ;
> ✓ pourquoi un serveur web est **facile à redonder** — il ne garde rien — et pourquoi ce « rien » doit alors vivre ailleurs ;
> ✓ pourquoi la **base se trouve au fond dans le modèle à trois niveaux**, et pourquoi une réplication non testée est une croyance, pas une redondance ;
> ✓ que la **messagerie** est simultanément une voie d'entrée majeure et le moyen de récupération de nombreux comptes ;
> ✓ que trois serveurs **dessinés redondés peuvent tourner sur le même hôte physique** — l'un des écarts les plus fréquents entre schéma et réalité ;
> ✓ que le **plan de gestion de la virtualisation** n'est jamais dessiné et donne accès à tout ce qu'il pilote ;
> ✓ **déduire le rôle d'un serveur de ses seules connexions**, et reconnaître ce qu'une observation de flux ne montre pas.
>
> **Ce que vous ne savez pas encore** : comment ces serveurs sont répartis dans des zones et des segments, et ce que cette répartition permet ou interdit. C'est l'objet de la Partie IV.

---

## PARTIE IV — Les réseaux et les zones

> Le chapitre 5 a posé les six zones de référence. Cette partie descend d'un cran : **comment une frontière est réellement matérialisée**, et ce qu'elle permet ou interdit.
>
> Deux chapitres traitent de zones que les schémas ne montrent presque jamais — l'administration et l'industriel — et ce sont les deux plus importants de la partie.

---

### Chapitre 24 — Le réseau local et la segmentation

#### 24.1 Le segment, unité de base

**Un segment est un ensemble de machines qui se joignent directement**, sans traverser d'équipement de routage.

> **La règle de lecture, formulée précisément** :
>
> **Placer deux systèmes dans un même segment ne crée pas entre eux la frontière de filtrage inter-segments que le schéma fait apparaître.** Leur isolation éventuelle est à chercher ailleurs — et le schéma ne la montre pas.

📌 **Ce qui peut isoler deux machines d'un même segment**, et qu'aucun schéma de zones ne représente :

| Mécanisme | Où il s'applique | Ce qu'il coûte |
|---|---|---|
| Pare-feu local sur l'hôte | Sur chaque machine | Une configuration à déployer et maintenir sur chaque poste |
| Isolation de ports, réseaux virtuels isolés | Sur le commutateur | Une configuration réseau fine |
| Contrôle d'accès au réseau | À la connexion | Un composant supplémentaire, et des exceptions à gérer |
| Politiques distribuées, microsegmentation | Par un dispositif dédié | **Un système complet à exploiter** |

⚠️ **La conséquence à retenir** : un pare-feu entre deux zones ne dit rien des échanges **à l'intérieur** de chaque zone. Sans l'un des mécanismes ci-dessus, une compromission dans un segment de six cents postes atteint les autres sans traverser la frontière dessinée. **La question de lecture n'est donc pas « sont-ils isolés ? » mais « par quel mécanisme le seraient-ils ? »**

#### 24.2 Segmenter, et jusqu'où

| Découpage | Ce qu'il isole | Coût | Quand il se justifie |
|---|---|---|---|
| Par **fonction** — postes, serveurs, impression | La contamination entre familles d'usage | Faible | **Presque toujours** |
| Par **sensibilité** — production, recette, développement | Les environnements | Faible à moyen | Dès qu'un environnement contient des données réelles |
| Par **service métier** | La propagation entre applications | **Moyen à élevé** | Quand les conséquences d'une propagation diffèrent fortement |
| Par **poste** — isolation totale | Tout | **Très élevé** | Rarement, et jamais sans outillage dédié |

⚖️ **CONTRAINTE ET COÛT — la segmentation fine**

| Résout | Coûte |
|---|---|
| Limiter la propagation latérale | Des dizaines de flux à ouvrir, documenter, maintenir |
| Appliquer des règles par population | **Un diagnostic plus long** — *« ça ne passe pas, mais où ? »* |
| Démontrer un cloisonnement | **Des contournements si le processus d'ouverture est trop lent** |

⚠️ **Principe du coût, appliqué** : la ligne du bas est la plus importante. Une segmentation dont l'ouverture de flux demande trois semaines produit, en dix-huit mois, un ensemble de contournements — machines à double interface, comptes partagés, règles « temporaires ». **Une segmentation contournée protège moins qu'une segmentation absente, parce qu'on croit qu'elle protège.**

#### 24.3 Le coût réel d'une segmentation, chiffré

**Ce qu'on oublie d'évaluer avant de segmenter** :

```
   Segmenter un parc en 6 zones au lieu de 2

   ①  Recenser les flux existants        → 2 à 4 semaines
   ②  Les documenter et les valider      → chaque flux a un demandeur
                                            à retrouver
   ③  Écrire les règles                  → 50 à 300 règles selon le parc
   ④  Basculer                           → par lots, avec retours arrière
   ⑤  Traiter les flux oubliés           → ⚠️ LE PLUS LONG
                                            on ne les découvre qu'en cassant
   ⑥  Maintenir                          → chaque projet ajoute des flux
```

⚠️ **L'étape ⑤ est celle qui fait échouer les projets de segmentation.** On ne connaît pas les flux existants : on les découvre en les coupant. **La seule méthode qui fonctionne est d'observer d'abord, filtrer ensuite** — passer plusieurs semaines en mode « journalisation sans blocage » avant d'appliquer la moindre règle.

🔥 **SCÉNARIO — la segmentation casse un flux que personne ne connaissait**

| Question | Réponse |
|---|---|
| Symptôme | Trois semaines après la segmentation, une facturation mensuelle échoue |
| Hypothèse naïve | « Un problème applicatif » |
| Dépendance réelle | **Un flux mensuel entre deux serveurs**, jamais documenté, coupé par une règle |
| Ce que le schéma aurait dû montrer | Les flux périodiques — **ils n'apparaissent dans aucune observation courte** |
| Concevoir différemment | Observer **au moins un cycle métier complet** avant de filtrer — un mois, parfois un trimestre |

⚠️ **Les flux périodiques sont l'angle mort de toute observation.** Un flux trimestriel n'apparaît pas dans deux semaines de journalisation. **C'est la raison pour laquelle une segmentation casse toujours quelque chose, trois mois après.**

🔭 **À RECONNAÎTRE — VXLAN et EVPN**

**① Le problème.** Dans un grand environnement virtualisé, on veut parfois qu'une machine **conserve son segment logique quel que soit l'hôte physique où elle s'exécute** — y compris après une migration vers une autre baie, voire un autre site. Le découpage physique du réseau ne le permet pas naturellement.

**② La solution.** Construire des **réseaux logiques par-dessus une infrastructure IP existante**.

```
        RÉSEAU LOGIQUE (overlay)
   ╔══════════════════════════════════╗
   ║  segment « production »          ║   ← les machines s'y voient
   ║  segment « recette »             ║      comme si elles étaient
   ╚══════════════════════════════════╝      côte à côte
                  ▲  encapsulation
                  │
   ────────────────────────────────────
        RÉSEAU PHYSIQUE IP (underlay)
        [ commutateur ] ── [ commutateur ] ── [ commutateur ]
```

**③ Le vocabulaire à reconnaître, et rien de plus** :

| Terme | Ce que c'est |
|---|---|
| **Underlay** | Le réseau physique IP, qui transporte |
| **Overlay** | Le réseau logique construit au-dessus |
| **VXLAN** | Le mécanisme d'encapsulation qui rend cela possible |
| **VTEP** | Le point où l'encapsulation commence et se termine |
| **EVPN** | **Un mécanisme de contrôle** fréquemment employé pour distribuer les informations nécessaires à ces réseaux logiques |

**④ Ce que cela change en lecture.** Deux machines qui se voient dans le même segment **peuvent être dans deux baies différentes, voire deux salles**. Le schéma logique et le schéma physique divergent radicalement — c'est le §3.3 poussé à son extrême.

**⑤ Le coût.** Une complexité de diagnostic considérable — **un problème peut venir du réseau logique ou du réseau physique, et les symptômes se ressemblent** · une compétence rare · une dépendance au mécanisme de contrôle.

⚠️ **Un point de sécurité souvent mal compris** : étendre un segment entre deux salles ou deux sites **étend aussi le domaine de propagation d'une compromission** — §24.1. La souplesse d'exploitation se paie en surface d'attaque.

**⑥ En réunion** : *« c'est du VXLAN »* → **quel est le réseau physique sous-jacent ? un problème peut venir des deux** · *« on étend le VLAN entre les deux salles »* → **on étend aussi ce qui peut s'y propager**.

📚 **À approfondir ailleurs** : la conception d'un réseau de centre de données, la configuration des mécanismes de contrôle.

#### 24.4 L'accès sans fil

> **Un trou visible dans la plupart des schémas** : les postes sont dessinés — quand ils le sont — reliés par un trait, comme s'ils étaient tous câblés. La majorité ne l'est plus.

##### Le chemin d'un poste sans fil

```
   [ poste ]
       │  ① association au point d'accès
       ▼
   [ point d'accès ]
       │  ② le poste est-il autorisé ? contre quoi ?
       ▼
   [ contrôleur ]  ── ou une configuration distribuée
       │  ③ dans quel segment le poste est-il placé ?
       ▼
   [ réseau d'accès ]
       │  ④ ce segment est-il filtré ? traité comme l'interne ?
       ▼
   [ le reste du système d'information ]
```

⚠️ **Les étapes ② et ③ sont invisibles sur tout schéma**, et ce sont elles qui décident de tout.

##### La question qui structure la lecture

> ### Le Wi-Fi est-il un réseau distinct, ou seulement une autre manière d'entrer dans le même segment ?

**Trois réponses possibles, et elles décrivent trois architectures très différentes** :

```
  A — LE WI-FI EST UNE PORTE SUR LE SEGMENT INTERNE
      [ poste sans fil ] ──► même segment que les postes câblés
      → simple · rien à configurer de plus
      → ⚠️ le périmètre physique du bâtiment ne protège plus rien :
        quiconque obtient la clé est DANS le réseau interne

  B — LE WI-FI EST UN SEGMENT À PART, ROUTÉ VERS L'INTERNE
      [ poste sans fil ] ──► segment sans fil ──► [ filtrage ] ──► interne
      → une frontière existe · on peut restreindre ce que le sans-fil atteint
      → le modèle courant, et le bon compromis dans la plupart des cas

  C — LE WI-FI EST TRAITÉ COMME L'EXTÉRIEUR
      [ poste sans fil ] ──► segment isolé ──► Internet
                                  └──► accès distant ──► interne
      → le poste sans fil n'a aucun privilège du fait d'être dans le bâtiment
      → il revient par le même chemin qu'un poste nomade — §6.3
      → cohérent, et exigeant : le tunnel devient obligatoire pour tous
```

⚠️ **Le mode A est fréquent et rarement assumé comme un choix.** Il transforme une clé partagée — ou un compte d'annuaire — en **entrée directe sur le réseau interne**, sans traverser aucune frontière. Le pare-feu du périmètre n'y peut rien : l'entrée se fait derrière lui.

##### Les réseaux multiples, et ce qu'ils ne garantissent pas

**Une même infrastructure sans fil porte généralement plusieurs réseaux annoncés** :

| Réseau | Qui s'y connecte | Où il devrait aboutir |
|---|---|---|
| **Entreprise** | Postes gérés, authentifiés individuellement | Segment interne ou segment sans fil filtré |
| **Invités** | N'importe qui, avec un code | **Internet seulement, jamais l'interne** |
| **Appareils** | Imprimantes, équipements industriels, capteurs | Un segment dédié, très restreint |
| **Personnel** | Téléphones des salariés | Souvent confondu avec « invités » — à trancher |

⚠️ **Deux réseaux annoncés séparément ne sont pas nécessairement deux segments.** C'est le §24.1 appliqué au sans-fil : **la séparation visible pour l'utilisateur ne dit rien de la séparation réseau**. La question à poser : *ces réseaux aboutissent-ils dans des segments différents, et qu'est-ce qui filtre entre eux ?*

##### Les deux façons d'autoriser un poste

| Méthode | Ce qui authentifie | Ce que ça implique |
|---|---|---|
| **Clé partagée** | Une clé, connue de tous les postes | **Un départ n'invalide rien** · la clé circule · aucune identité individuelle dans les journaux |
| **Authentification individuelle** | Le poste ou l'utilisateur, contre l'annuaire | Une identité par connexion · **une dépendance à l'annuaire pour se connecter au réseau** |

⚠️ **La seconde ligne crée une dépendance nouvelle et peu anticipée** : si l'annuaire est indisponible, **les postes sans fil ne se connectent plus au réseau du tout**. C'est un flux de dépendance de plus — principe des trois flux — et il précède même l'ouverture de session.

🔥 **SCÉNARIO — le sans-fil ne fonctionne plus, le câblé oui**

| Question | Réponse |
|---|---|
| Symptôme | Les postes câblés fonctionnent. Aucun poste sans fil ne se connecte |
| Hypothèse naïve | « Panne des points d'accès » |
| Dépendance réelle | **L'authentification sans fil s'appuie sur l'annuaire ou un service dédié**, indisponible |
| Ce que le schéma aurait dû montrer | Contre quoi le sans-fil authentifie |
| Comment le reconnaître | **Les postes déjà connectés restent connectés** · seules les nouvelles associations échouent |

🔥 **SCÉNARIO — un visiteur atteint un serveur interne**

| Question | Réponse |
|---|---|
| Symptôme | Un audit montre qu'un poste sur le réseau invités joint un serveur de fichiers |
| Hypothèse naïve | « Une erreur de configuration du point d'accès » |
| Dépendance réelle | **Les deux réseaux annoncés aboutissent dans le même segment** — mode A |
| Ce que le schéma aurait dû montrer | Où aboutit chaque réseau sans fil |
| Concevoir différemment | Un segment par usage, avec un filtrage explicite entre eux |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a un SSID invités » | Un réseau séparé est annoncé | **Aboutit-il dans un segment distinct ?** Annoncé ≠ segmenté |
| « Le Wi-Fi est en 802.1X » | Authentification individuelle | **Contre quoi ? Que se passe-t-il si ce service tombe ?** |
| « C'est le même réseau que le filaire » | Mode A | **Alors le périmètre physique ne protège plus rien** |
| « On a changé la clé » | Clé partagée | **Combien de fois en cinq ans ? Qui la connaît ?** |
| « Les AP sont gérés par un contrôleur » | Configuration centralisée | **Le contrôleur est-il un point de rupture ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Connecter des postes sans câblage | **Une entrée qui contourne le périmètre physique** |
| Authentifier individuellement | Une dépendance de plus, **avant même l'ouverture de session** |
| Séparer les usages par réseau annoncé | Autant de segments et de règles à tenir — sinon la séparation est cosmétique |
| Couvrir un site entier | Des équipements nombreux, à corriger et à surveiller |

🏭 **TROIS TAILLES** — Atelier Martin : un point d'accès, clé partagée, **même segment que les postes câblés** — mode A, non identifié comme un choix. HELIOMED : trois réseaux annoncés, authentification individuelle, segment sans fil filtré vers l'interne — mode B. Novaris : contrôleurs redondés par région, quatre usages séparés, **parce que des magasins accueillent du public et que le réseau invités doit être totalement disjoint**.

🔭 **À RECONNAÎTRE — NAC**

**① Qu'est-ce que c'est.** *Network Access Control* — un dispositif qui répond à une question que la plupart des réseaux ne posent jamais :

> ### Qui décide qu'un équipement a le droit d'entrer sur le réseau ?

**② Quel problème il résout.** Par défaut, **un câble branché fonctionne**. Un poste inconnu obtient une adresse — §15.5 — et se retrouve dans le segment, avec tout ce que cela implique — §24.1. Le NAC insère une décision avant l'accès.

**③ Où on le rencontre.** Sur le réseau filaire des sites accueillant du public ou des visiteurs, et **systématiquement associé au sans-fil d'entreprise** — §24.4.

**④ Ce que cela change.**

```
   SANS NAC
      [ terminal ] ──► réseau d'accès ──► segment ──► tout

   AVEC NAC
      [ terminal ]
           ▼
      réseau d'accès
           ▼
      [ CONTRÔLE D'ACCÈS ]   ← qui es-tu ? es-tu conforme ?
           ▼
      segment et politique APPROPRIÉS
           │
           ├── poste géré et conforme  → segment interne
           ├── poste géré non conforme → segment de remédiation
           ├── équipement reconnu       → segment dédié
           └── inconnu                  → segment invité, ou rien
```

⚠️ **Ce que le schéma montre et qui compte** : le NAC ne fait pas qu'autoriser ou refuser. **Il place le terminal dans un segment en fonction de ce qu'il est.** C'est un mécanisme de segmentation dynamique, et c'est ce qui le rend puissant.

**802.1X** est la technologie fréquemment associée — vous en entendrez le nom, vous n'avez pas à en connaître le détail.

**⑤ Le coût.** Un projet long, parce qu'il faut d'abord **savoir ce qui se connecte** — imprimantes, capteurs, équipements industriels, prestataires · des exceptions inévitables pour ce qui ne sait pas s'authentifier · **une dépendance de plus au démarrage** — §24.4 · un mode dégradé à définir : *que fait-on si le NAC tombe, on laisse tout entrer ou plus rien ?*

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a du NAC » | **Sur tout le parc, ou seulement le sans-fil ?** Le filaire est souvent laissé de côté |
| « On est en 802.1X » | Authentification à la connexion. **Contre quoi ? Et les équipements qui ne le savent pas ?** |
| « On a mis des exceptions par adresse matérielle » | Une liste de dérogations. **Combien ? Depuis quand ? Une adresse matérielle se falsifie** |
| « Si le NAC tombe, on ouvre tout » | Mode dégradé permissif. **C'est un choix — est-il assumé et écrit ?** |

#### 24.5 Trois architectures de segmentation

```
  A — DEUX ZONES
      [ postes ] │ [ serveurs ]
      → simple · une frontière à tenir
      → une compromission de poste atteint tous les postes

  B — SEGMENTATION PAR FONCTION
      [ postes ] │ [ serveurs ] │ [ impression ] │ [ admin ] │ [ industriel ]
      → le modèle courant · bon rapport effet/coût
      → 5 frontières, quelques dizaines de règles

  C — MICROSEGMENTATION
      chaque machine a sa propre politique
      → propagation quasi impossible
      → ⚠️ un système complet à exploiter, et une visibilité
        totale des flux exigée en préalable
```

**La contrainte qui fait passer de A à B** : la présence d'actifs dont la compromission a des conséquences très différentes — un automate industriel, un serveur de sauvegarde, un poste d'administration.

⚠️ **Le mode C n'est pas une version améliorée de B.** C'est un changement de nature : il suppose de connaître **tous** les flux, en permanence. Une organisation qui n'a pas réussi B ne réussira pas C.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est segmenté » | Plusieurs zones existent | **Combien ? Et à l'intérieur de chacune ?** |
| « On a un VLAN par service » | Segmentation logique fine | **Le routage entre eux est-il filtré, ou juste routé ?** |
| « On va tout ouvrir en attendant » | Une règle large, temporaire | **« En attendant » dure des années** — §4.3 |
| « Ça marchait avant » | Un flux a été coupé | **Un flux périodique ?** — §24.3 |

🏭 **TROIS TAILLES**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Segments | **2** — bureautique, atelier | 9 | Plusieurs centaines |
| Ce qui les justifie | La séparation atelier/bureau, pour la disponibilité de production | Postes par site, serveurs, DMZ, administration, industriel, recette | **Cloisonnement par entité après acquisitions**, plus les usages |

**Novaris n'a pas des centaines de segments parce qu'elle est grande** : elle en a parce que **sept acquisitions ont apporté sept plans d'adressage** qu'aucune fusion n'a rationalisés. Une organisation de même taille née d'une croissance interne en aurait dix fois moins.

---

### Chapitre 25 — La zone démilitarisée

> **Le concept le plus cité du domaine et le moins compris.**

#### 25.1 Ce que c'est réellement

**Le nom trompe.** Il évoque une zone neutre entre deux camps. La réalité est différente et plus simple :

> **La zone démilitarisée est l'endroit où l'on place ce qui doit être joignable depuis l'extérieur — en supposant qu'il sera compromis.**

**C'est une hypothèse de conception, pas une protection.** On n'y met pas des choses parce qu'elles y sont en sécurité ; on les y met **pour que leur compromission ne donne pas accès au reste**.

🖼 **SCHÉMA 25.1 — Les deux frontières**

```
        Internet
            │
      ┌─────┴─────┐  ← FRONTIÈRE 1 : ce qui entre, très filtré
      │  filtrage │     « seul le port 443 vers le mandataire »
      └─────┬─────┘
   ╔════════╪════════════════════════════════╗
   ║  ZONE DÉMILITARISÉE                     ║
   ║  [ mandataire ]  [ relais messagerie ]  ║
   ╚════════╪════════════════════════════════╝
      ┌─────┴─────┐  ← FRONTIÈRE 2 : LA PLUS IMPORTANTE
      │  filtrage │     « le mandataire peut joindre UNIQUEMENT
      └─────┬─────┘       le serveur web, sur le port 8080 »
   ╔════════╪════════════════════════════════╗
   ║  RÉSEAU INTERNE                         ║
   ╚═════════════════════════════════════════╝
```

⚠️ **La frontière 2 est celle qui définit une vraie zone démilitarisée**, et c'est celle qu'on oublie. Une « DMZ » qui peut joindre librement le réseau interne n'en est pas une : **c'est un segment exposé**.

**Le test qui tranche, en une question** : *si le mandataire était compromis, que pourrait-il atteindre ?*

| Réponse | Diagnostic |
|---|---|
| Un serveur, sur un port | **C'est une DMZ** |
| Plusieurs serveurs, sur plusieurs ports | Une DMZ affaiblie · à interroger |
| Tout le réseau interne | **Ce n'est pas une DMZ**, c'est un segment exposé |

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. La frontière 1 est dessinée — deux pare-feu. **La frontière 2 ne l'est pas.** C'est la question que le §5.3 posait sans pouvoir la trancher, et c'est la première à poser à l'auteur du schéma.

#### 25.2 Le flux retour, et pourquoi il annule tout

**Le point le plus subtil du chapitre, et le plus souvent mal conçu.**

Une DMZ ne sert à rien si le flux **de la DMZ vers l'interne** est trop large. Or il faut bien qu'il existe : le mandataire doit joindre le serveur web.

```
   BIEN CONÇU
      mandataire ──► serveur web       port 8080, uniquement
      Rien d'autre. Le mandataire ne peut joindre aucun autre serveur.

   MAL CONÇU — cas 1
      mandataire ──► TOUT L'INTERNE    ports 80, 443
      « C'est juste du web » — mais tout serveur interne exposant
      du web devient atteignable depuis la DMZ.

   MAL CONÇU — cas 2
      mandataire ──► base de données   port 1433
      Le mandataire court-circuite l'applicatif.
      L'architecture en couches est contournée par une règle de pare-feu.

   MAL CONÇU — cas 3
      mandataire ──► annuaire          ports 389, 636
      Nécessaire s'il authentifie — mais cela signifie qu'un
      mandataire compromis peut interroger l'annuaire.
```

⚠️ **Le cas 3 est légitime et il a un coût.** Placer l'authentification sur le mandataire — §12.2, fonction 3 — impose de lui donner accès à l'annuaire. **C'est un compromis, pas une erreur** : on gagne un contrôle avant l'application, on donne à un composant exposé une visibilité sur l'annuaire. **Principe du coût.**

#### 25.3 Les trois erreurs de conception classiques

| Erreur | Ce qu'elle produit |
|---|---|
| **Pas de frontière 2** | La DMZ devient un tremplin vers l'interne |
| **Un composant de la DMZ joignant la base de données** | Le contournement complet de l'architecture en couches |
| **Un serveur à double interface**, une patte dans chaque zone | **La frontière n'existe plus** — §5.4 |

⚠️ **La troisième est la plus discrète, et ses conséquences sont les plus larges.** Une machine avec deux interfaces réseau, une dans chaque zone, **ne traverse aucun pare-feu**. Elle est le pare-feu — et elle n'en a ni les règles, ni les journaux, ni la surveillance. Sur un schéma, elle apparaît comme un composant ordinaire à cheval sur une frontière.

#### 25.4 Trois architectures de publication

```
  A — PUBLICATION DIRECTE
      Internet ──► [ FW ] ──► serveur (en interne)
      → aucune DMZ · le serveur exposé est dans le réseau interne
      → une faille du serveur donne un pied dans l'interne
      → convient quand rien de sensible n'est autour

  B — DMZ CLASSIQUE
      Internet ──► [ FW ] ──► DMZ ──► [ FW ] ──► interne
      → le modèle de référence
      → deux jeux de règles · un composant dédié à exploiter

  C — PUBLICATION PAR UN TIERS
      Internet ──► [ service du fournisseur ] ──► lien sortant ──► interne
      → rien n'est exposé : c'est VOTRE serveur qui va vers le tiers
      → aucun flux entrant à ouvrir
      → une dépendance complète au fournisseur — §38
```

⚠️ **Le mode C mérite d'être connu**, parce qu'il inverse la logique : au lieu d'ouvrir un flux entrant, le serveur interne établit lui-même une connexion **sortante** vers un service qui reçoit les clients. **Il n'y a plus rien à exposer** — et il y a un tiers dans le chemin, qui voit tout.

#### 25.5 La passerelle d'interconnexion

> **Une fonction architecturale, pas un équipement.** C'est la notion que vous rencontrerez dans les recommandations publiques françaises, et elle mérite d'être nommée.

**La définition** :

> **Une passerelle d'interconnexion est l'ensemble des composants et des fonctions par lesquels deux systèmes ou deux zones de confiance distincts sont autorisés à échanger.**

⚠️ **C'est beaucoup plus juste que *« une passerelle, c'est un pare-feu »***. Un pare-feu est un composant possible de la passerelle ; il n'en est pas la définition.

🖼 **SCHÉMA 25.2 — Une passerelle comme assemblage**

```
                    PASSERELLE D'INTERCONNEXION
          ┌──────────────────────────────────────────┐
  SI A    │  filtrage réseau                         │   SI B
 ────────►│  relais ou mandataire applicatif         ├────────►
          │  contrôle protocolaire ou de contenu     │
          │  authentification                        │
          │  journalisation                          │
          │  éventuellement rupture de flux          │
          └──────────────────────────────────────────┘
```

**Le concept fort** :

> **Interconnecter deux systèmes d'information, ce n'est pas créer une route entre eux. C'est décider quels échanges sont permis, par quels intermédiaires, avec quelle confiance et quelle traçabilité.**

##### Les six choses que la passerelle matérialise

| # | Ce qu'elle établit | Pourquoi c'est une décision, pas une configuration |
|---|---|---|
| **1** | **Une frontière de confiance** | Les deux côtés n'ont pas le même niveau de confiance — c'est le §5.1 |
| **2** | **Une réduction des flux** | On n'ouvre pas les deux réseaux l'un à l'autre : on autorise ce qui est nécessaire |
| **3** | **Des fonctions intermédiaires** | Filtrage, mandataire, contrôle de contenu, terminaison — selon ce que l'échange exige |
| **4** | **Un point de concentration** | Excellent pour contrôler et observer · **et une dépendance forte** |
| **5** | **Une question de sens** | Un flux de A vers B n'implique en rien que B vers A soit autorisé — §P.3 |
| **6** | **Une question de protocoles** | Certaines architectures évitent même la communication directe, par un relais ou un échange contrôlé |

⚠️ **Le point 6 mérite un mot** : quand la différence de confiance est très forte, on renonce à la communication directe. Les données transitent par un relais qui les reconstitue, ou par un mécanisme d'échange où aucune connexion ne traverse la frontière. **C'est le modèle A du §28.4, appliqué au-delà de l'industriel.**

##### Connectivité et contrôle de frontière ne sont pas la même chose

**Un exercice qui vaut d'être fait, parce que les deux sont constamment confondus** :

```
                    CONNECTIVITÉ
   Site A ══════════════════════════════════ Site B
            MPLS · Internet · SD-WAN
                         ≠
                CONTRÔLE DE FRONTIÈRE
   SI A ─────► [ passerelle d'interconnexion ] ─────► SI B
```

| | Ce à quoi ça répond |
|---|---|
| **Connectivité** | *Comment les paquets rejoignent-ils l'autre environnement ?* |
| **Passerelle** | *Sous quelles conditions avons-nous décidé qu'ils pouvaient y entrer ?* |

**Un SD-WAN peut transporter un flux vers un autre site. Une passerelle décide ensuite si ce flux entre dans le système cible, et comment.** Les deux fonctions sont parfois portées par le même équipement ou le même contrat — **les responsabilités architecturales restent distinctes**.

##### Le principe à retenir

> ### Relier deux réseaux ne signifie pas qu'ils doivent devenir un seul périmètre de confiance.

**C'est la raison d'être de tout ce chapitre** : les zones, le filtrage, les mandataires, l'authentification, les flux explicitement autorisés — toutes ces notions existent pour que **l'interconnexion ne soit pas une extension de confiance**.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça passe par la passerelle d'interco » | Les échanges traversent une architecture de contrôle dédiée | **Quelles fonctions contient-elle réellement ?** |
| « On ouvre l'interconnexion » | De nouveaux flux entre deux périmètres vont être autorisés | **Quels flux exactement, dans quel sens ?** |
| « Les deux SI sont interconnectés » | Une connectivité existe | **Routage complet, ou seulement quelques services ?** |
| « C'est filtré » | Un mécanisme de contrôle existe | **À quel niveau, et selon quelle politique ?** |

⚠️ **La troisième ligne est celle qui révèle le plus.** *« Interconnectés »* recouvre aussi bien *« trois flux applicatifs autorisés »* que *« les deux réseaux se voient entièrement »* — et l'écart entre les deux est considérable.

#### 25.6 Ce que la DMZ ne protège pas

| Elle protège | Elle ne protège pas |
|---|---|
| L'interne, si un composant exposé est compromis | **Les échanges entre composants de la DMZ** |
| Contre une exposition directe des serveurs internes | Contre une faille du mandataire lui-même |
| Contre un balayage depuis Internet | **Contre un poste interne compromis** — §6.1 |

⚠️ **La dernière ligne est celle qu'on oublie systématiquement.** Toute l'architecture de la DMZ suppose que la menace vient de l'extérieur. **Elle est sans effet sur la menace qui commence sur un poste** — et c'est une voie d'entrée majeure.

🔥 **SCÉNARIO — la DMZ n'a servi à rien**

| Question | Réponse |
|---|---|
| Symptôme | Compromission du serveur de fichiers interne. La DMZ n'a rien vu |
| Hypothèse naïve | « La DMZ a été franchie » |
| Dépendance réelle | **L'entrée s'est faite par un poste utilisateur.** La DMZ n'était pas sur le chemin |
| Ce que le schéma aurait dû montrer | Les postes — §6.1 |
| Concevoir différemment | Segmenter à l'intérieur, pas seulement au périmètre — §24.2 |

#### 25.7 Sur un schéma

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans la DMZ » | Le composant est exposé | **Que peut-il joindre en interne ?** C'est la seule question qui compte |
| « On va ouvrir un flux depuis la DMZ » | Une règle de la frontière 2 | Vers quoi exactement ? Un serveur, ou une plage ? |
| « Le serveur a deux pattes » | Deux interfaces réseau, deux zones | **La frontière n'existe plus à cet endroit** |
| « C'est une DMZ, c'est sécurisé » | Confusion fréquente | La DMZ **suppose la compromission**, elle ne l'empêche pas |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Publier des services sans exposer l'interne | Des composants dédiés à exploiter et corriger en priorité |
| Contenir une compromission attendue | **Des flux traversants à définir finement** — et à ne pas élargir |
| Séparer les cycles de mise à jour | **Une administration à part** — chapitre 27 |
| Authentifier en amont | Un accès à l'annuaire depuis une zone exposée |

🏭 **TROIS TAILLES** — Atelier Martin : **aucune DMZ**, parce qu'elle ne publie aucun service. HELIOMED : une, parce qu'elle publie une plateforme client. Novaris : plusieurs, séparées par usage — publication web, échanges partenaires, accès distant — **parce que ces trois usages n'ont ni les mêmes flux entrants ni les mêmes conséquences en cas de compromission**.

---

### Chapitre 26 — Le réseau étendu et les sites distants

#### 26.1 Ce que la distance change

| Contrainte | Effet |
|---|---|
| **Latence** | Certaines applications deviennent inutilisables au-delà d'un seuil |
| **Débit** | Partagé entre tous les usages du site |
| **Disponibilité** | Un lien unique est un point de rupture pour tout un site |
| **Coût** | La redondance d'un lien double une facture récurrente |

**La question de lecture** : *ce site fonctionne-t-il si le lien tombe ?* Trois réponses possibles, et chacune décrit une architecture différente :

| Réponse | Architecture |
|---|---|
| **Non, rien ne fonctionne** | Tout est centralisé. Site totalement dépendant |
| **Partiellement** | Des services locaux — annuaire, fichiers — subsistent |
| **Oui** | Site autonome, avec ses propres dépendances locales |

⚠️ **La deuxième est très répandue, et elle est rarement documentée.** Personne ne sait exactement ce qui subsiste, **parce que personne n'a coupé le lien pour voir**.

#### 26.2 Les dépendances locales

**Ce qui doit être local pour qu'un site survive à une coupure** — et c'est le principe des trois flux appliqué à la géographie :

| Service | Local ? | Effet si distant et le lien tombe |
|---|---|---|
| **Résolution de noms** | Devrait l'être | Plus rien ne fonctionne sur le site |
| **Contrôleur d'annuaire** | Devrait l'être | Plus d'ouverture de session |
| **Attribution d'adresses** | Devrait l'être | Panne différée, au fil des redémarrages |
| Fichiers | Selon l'usage | Travail bloqué, service non |
| Applications métier | Rarement | Le site est à l'arrêt fonctionnel |
| Accès Internet | Selon | Sortie centralisée ou locale : deux architectures — §11.3 |

**Les trois premières lignes sont les trois flux de dépendance des chapitres 14 à 16.** Un site sans elles n'a aucune autonomie, quelle que soit la qualité de son réseau local.

⚠️ **Un piège fréquent sur le contrôleur d'annuaire local** : il existe, il fonctionne, **et il réplique depuis le siège**. Si le lien tombe longtemps, la réplication s'interrompt — les authentifications continuent, mais les changements de mot de passe faits au siège ne sont pas connus localement. **L'autonomie n'est pas totale, elle est datée.**

#### 26.3 Trois architectures de sites

```
  A — TOUT CENTRALISÉ
      site distant ══lien══► [ siège : tout ]
      → simple · rien à exploiter sur site
      → le lien tombe : le site est à l'arrêt complet
      → convient si le lien est très fiable et l'arrêt tolérable

  B — SOCLE LOCAL
      site distant : [ résolution ] [ annuaire ] [ fichiers ]
                            ══lien══► [ siège : applications ]
      → les postes démarrent, les sessions s'ouvrent, le travail
        local continue
      → les applications métier restent indisponibles
      → ⚠️ c'est l'architecture la plus répandue, et son autonomie
        n'est presque jamais testée

  C — SITE AUTONOME
      site distant : tout ce dont il a besoin
                            ══lien══► [ siège : consolidation ]
      → autonomie complète
      → autant de systèmes à exploiter que de sites
```

**La contrainte qui décide** : *combien de temps le site peut-il rester arrêté ?* — et la réponse chiffrée détermine directement le choix.

🔭 **À RECONNAÎTRE — MPLS**

**① Qu'est-ce que c'est.** Vous le rencontrerez presque toujours comme **un service d'opérateur permettant d'interconnecter plusieurs sites** au sein d'un réseau privé porté par cet opérateur.

**② Quel problème il résout.** Relier dix agences au siège sans construire dix liaisons dédiées, avec des garanties de service que l'accès Internet ordinaire n'offre pas — débit engagé, latence, priorisation.

**③ Où on le rencontre.** *« Nos agences sont sur le MPLS »* est une phrase que vous entendrez. Elle désigne le réseau étendu de l'organisation, souscrit auprès d'un opérateur.

**④ Ce que cela change.**

```
   [ agence 1 ] ──┐
   [ agence 2 ] ──┼──► [ réseau de l'opérateur ] ──► [ siège ]
   [ agence 3 ] ──┘
```

Les sites se voient comme s'ils étaient sur un même réseau privé. **Le routage est simplifié**, et la qualité de service est contractuelle.

⚠️ **⑤ Le risque, et c'est l'erreur la plus fréquente sur ce sujet** :

> **Un réseau privé d'opérateur n'est pas un chiffrement de bout en bout.**

« Privé » signifie *séparé du trafic des autres clients par le mécanisme de l'opérateur*, pas *illisible par l'opérateur*. **La question professionnelle devient donc** : *quelles garanties le service apporte-t-il réellement, et faut-il ajouter du chiffrement au-dessus ?*

Autres coûts : une dépendance forte à un opérateur unique · un délai de raccordement d'un nouveau site en semaines ou en mois · un coût récurrent élevé comparé à un accès Internet.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « Les sites sont sur le MPLS » | **Le trafic est-il chiffré au-dessus ?** Et si le lien tombe, que reste-t-il ? |
| « On a du QoS sur le MPLS » | Des flux sont priorisés. **Lesquels, et selon quel engagement contractuel ?** |
| « On sort par le siège » | Sortie Internet centralisée — §11.3 |

---

🔭 **À RECONNAÎTRE — SD-WAN**

**① Qu'est-ce que c'est.** Et c'est ici qu'il faut être précis, parce que la confusion est constante :

> **Le SD-WAN n'est pas un nouveau type de liaison. C'est une couche de pilotage qui utilise plusieurs transports et décide comment les flux les empruntent, selon des politiques.**

**② Quel problème il résout.** Un site dispose souvent de plusieurs accès — un lien opérateur, un accès Internet, une connexion cellulaire de secours. Sans pilotage, on choisit **une** route par destination. Le SD-WAN permet de choisir **par flux**, selon des critères applicatifs.

**③ Où on le rencontre.** Dans les architectures multi-sites récentes, et dans toute organisation qui a migré des applications vers des services en ligne — parce que faire remonter au siège un trafic destiné à Internet devient absurde.

🖼 **SCHÉMA 26.1 — Ce que le SD-WAN ajoute**

```
                         ┌── MPLS ──────────┐
  [ Site A ] ─[SD-WAN]───├── Internet ──────┼───[SD-WAN]─ [ SI / Cloud ]
                         └── 4G / 5G ───────┘

  SANS SD-WAN      destination → route → lien
  AVEC SD-WAN      application + qualité du lien + politique → lien

     Téléphonie    → le lien de plus faible latence
     Progiciel     → le lien opérateur
     Web et SaaS   → sortie Internet locale
     Secours       → connexion cellulaire
```

**④ Les quatre implications architecturales**, et c'est ce que le lecteur doit retenir :

| # | Implication |
|---|---|
| **1** | **Il existe un plan de pilotage supplémentaire.** Des équipements appliquent sur site des politiques définies ailleurs. Une architecture qui paraît avoir trois liens indépendants **peut dépendre d'un contrôleur central** |
| **2** | **Le chemin devient dynamique.** Deux connexions vers la même application n'ont pas nécessairement emprunté le même lien. Cela complique le dépannage, la journalisation et le filtrage |
| **3** | **La sortie Internet locale contourne le datacenter.** Le modèle *agence → siège → pare-feu central → Internet* devient *agence → Internet directement* — **et les contrôles centraux ne s'appliquent plus** |
| **4** | **Le SD-WAN apporte de la connectivité et du pilotage**, pas de la sécurité par magie. Les fonctions de sécurité dépendent de l'architecture et du produit |

⚠️ **La troisième implication est la plus lourde en sécurité.** Elle déplace le point où l'on peut agir — chapitre 43 — sans que rien sur le schéma ne le signale.

**⑤ Le coût**

> **Le SD-WAN simplifie le pilotage de plusieurs liens, et rend le chemin réel d'un flux beaucoup moins évident à déduire d'un schéma statique.**

Plus : un plan de pilotage qui devient un composant critique · une dépendance à un fournisseur · des politiques à maintenir.

**⑥ En réunion**

| Ce que vous entendrez | Ce que cela signifie probablement | À vérifier |
|---|---|---|
| « Le site est en SD-WAN » | Plusieurs transports pilotés par une couche logique | **Quels transports ? Qui décide du chemin ?** |
| « On fait du breakout local » | Le trafic Internet sort directement du site | **Quels contrôles restent sur ce chemin ?** |
| « Ça bascule automatiquement » | Une politique choisit un autre lien | **Sous quelles conditions ? Testé ? En combien de temps ?** |
| « Le SD-WAN prend le meilleur lien » | Il applique des métriques et des politiques | **Meilleur selon quel critère ?** |

📚 **À approfondir ailleurs** : la conception d'une politique de pilotage, les mécanismes propres à chaque constructeur.

#### 26.4 Le lien lui-même

| Configuration | Ce qu'elle protège | Principe de preuve |
|---|---|---|
| Lien unique | Rien | — |
| Deux liens, même opérateur | Une panne d'équipement | **Pas une panne de l'opérateur** |
| Deux liens, deux opérateurs | Une panne d'opérateur | **Pas une coupure de la tranchée commune** |
| Deux liens, deux opérateurs, deux arrivées physiques | La plupart des cas | Le coût est nettement supérieur |

⚠️ **La ligne « même tranchée » est réelle et fréquente.** Deux opérateurs différents peuvent emprunter le même fourreau à l'entrée du bâtiment. Une pelleteuse coupe les deux. **La question à poser : les deux liens entrent-ils par le même endroit ?**

🔥 **SCÉNARIO — le lien fonctionne, le site est bloqué**

| Question | Réponse |
|---|---|
| Symptôme | Le lien est supervisé au vert. Les utilisateurs du site ne peuvent plus travailler |
| Hypothèse naïve | « Problème réseau » |
| Dépendance réelle | **L'authentification centrale.** Le lien porte les paquets, mais un composant au siège ne répond plus |
| Ce que le schéma aurait dû montrer | Ce qui est local et ce qui est distant — §26.2 |
| Concevoir différemment | Superviser **le service rendu**, pas seulement le lien |

⚠️ **C'est l'illustration du §35.2** : la supervision d'un lien ne dit rien de la disponibilité d'un service qui l'emprunte.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le site est coupé » | Le lien est indisponible | **Ou un service central l'est.** Ce n'est pas la même chose |
| « On a un lien de secours » | Un second lien existe | Même opérateur ? Même arrivée physique ? **Testé ?** |
| « Ils ont un DC local » | Un contrôleur d'annuaire sur site | **Réplique-t-il ? Depuis quand ?** L'autonomie est datée |
| « Ils sortent par le siège » | Sortie Internet centralisée | Si le lien tombe : plus d'Internet non plus — §11.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Centraliser l'exploitation | **Un site totalement dépendant du lien** |
| Un socle local | Des composants à exploiter sur chaque site |
| Redonder le lien | Une facture récurrente doublée · **et souvent une fausse redondance** — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : un site, la question ne se pose pas. HELIOMED : trois sites, avec résolution et annuaire locaux à Nantes et Saint-Étienne, **mais applications centralisées à Lyon** — autonomie partielle, jamais testée. Novaris : quarante sites, socle local standardisé, **parce que la coupure d'un lien ne doit pas arrêter un magasin**.

---

### Chapitre 27 — Le réseau d'administration

> **Invisible sur les schémas, décisif en sécurité.** L'un des deux chapitres les plus importants de la partie.

#### 27.1 Pourquoi il existe

**Le constat de départ** : administrer un système suppose des accès **plus puissants** que ceux nécessaires pour l'utiliser.

| Ce qu'un utilisateur peut faire | Ce qu'un administrateur peut faire |
|---|---|
| Consulter ses données | Consulter toutes les données |
| Utiliser une application | Arrêter, modifier, contourner l'application |
| Ouvrir sa session | **Ouvrir n'importe quelle session** |
| — | **Effacer les traces de son passage** |

> **Le chemin d'administration est plus puissant que ce qu'il administre.** C'est pourquoi il justifie une zone à part.

⚠️ **La dernière ligne du tableau est celle qui change tout en réponse à incident** : un administrateur — ou quelqu'un qui a pris sa place — peut modifier les journaux. **C'est pourquoi les journaux d'administration doivent partir ailleurs, immédiatement** — §34.3.

#### 27.2 Ce qu'on y trouve

🖼 **SCHÉMA 27.1 — Le chemin d'administration**

```
   [ poste d'administrateur ]
              │
              ▼  authentification renforcée
   ┌──────────────────────┐
   │  POSTE DE REBOND     │  ← unique point de passage
   │  (« bastion »)       │     journalisé, parfois enregistré
   └──────────┬───────────┘
              │
   ┌──────────┼──────────┬──────────────┐
   ▼          ▼          ▼              ▼
 serveurs   réseau   virtualisation   sauvegarde
                       (plan de
                        gestion)
```

| Composant | Rôle | Ce qui arrive s'il manque |
|---|---|---|
| **Poste dédié** | Un poste qui ne sert qu'à administrer | Un poste bureautique compromis donne l'administration |
| **Point de rebond** | Le passage unique et journalisé | Aucune trace centralisée des actions privilégiées |
| **Coffre de secrets** | Stocke et renouvelle les identifiants privilégiés | Des mots de passe partagés, jamais changés — §33 |
| **Segment isolé** | Non joignable depuis le réseau bureautique | Le rebond est atteignable par un poste compromis |

#### 27.3 Les quatre chemins d'administration qu'on oublie

**Le rebond couvre les serveurs. Il ne couvre presque jamais ces quatre-là** :

| Chemin oublié | Pourquoi il échappe | Ce qu'il donne |
|---|---|---|
| **Le plan de gestion de virtualisation** | Interface web, souvent accessible depuis le bureautique | **L'accès aux disques de toutes les machines** — §23.4 |
| **Les interfaces d'administration matérielle** | Cartes de gestion à distance, sur un réseau à part | **Un accès en dessous du système** |
| **Les consoles des équipements réseau** | Administrées par une autre équipe | Le routage et le filtrage |
| **Les accès des prestataires** | Contractuels, hors processus | **Des postes que vous ne maîtrisez pas** — §38.4 |

⚠️ **Le deuxième est le plus méconnu.** Les cartes de gestion à distance permettent d'allumer, éteindre, réinstaller une machine et d'accéder à sa console **sans passer par son système d'exploitation**. Aucun contrôle placé dans le système ne les voit. **Elles sont sur un réseau à part, souvent oublié dans les revues.**

🔭 **À RECONNAÎTRE — PAM**

**① Qu'est-ce que c'est.** *Privileged Access Management* — l'ensemble des dispositifs qui **encadrent les accès privilégiés** : ceux qui permettent de tout faire.

**② Quel problème il résout.** Sans lui, les comptes d'administration sont partagés, leurs mots de passe ne changent jamais, et **rien ne dit qui a fait quoi**. Le §27.2 décrit les composants ; le PAM est le nom de leur assemblage.

**③ Ce qu'il apporte, selon les solutions** :

| Fonction | Ce qu'elle change |
|---|---|
| **Coffre de secrets privilégiés** | Le mot de passe d'administration n'est plus connu de personne — on l'emprunte |
| **Rotation automatique** | Il change après chaque usage · un départ n'oblige plus à tout changer à la main |
| **Contrôle d'accès** | Qui peut emprunter quel accès, quand, pour quelle durée |
| **Élévation à la demande** | On n'est pas administrateur en permanence, on le devient pour une tâche |
| **Traçabilité** | Qui a emprunté quoi, et quand |
| **Enregistrement de session** | Ce qui a été fait, rejouable |

⚠️ **La quatrième ligne est la plus structurante en architecture** : elle transforme un état permanent — *cette personne est administrateur* — en un **événement daté et motivé**. C'est ce qui rend l'accès privilégié auditable.

**④ Ce que cela change dans les flux.** Un composant de plus **sur le chemin de toute administration**. Et une dépendance : le §27.4 montre qu'un point de passage unique est aussi un point de rupture — **si le PAM est indisponible, on ne peut plus administrer**.

**⑤ Le coût.** Une solution à exploiter et à sécuriser fortement — **elle détient les clés du système d'information** · une adoption difficile, parce qu'elle ajoute des étapes à des gens pressés · **des accès de secours à prévoir**, et à protéger tout autant.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un PAM » | **Tous les accès privilégiés y passent-ils ?** Il y a presque toujours des exceptions |
| « Les mots de passe sont dans le coffre » | **Sont-ils tournés ? Quelqu'un les connaît-il encore ?** |
| « On a un compte de secours » | Légitime et nécessaire. **Où est-il ? Qui y accède ? Est-il surveillé ?** |
| « Les sessions sont enregistrées » | **Qui relit les enregistrements, et dans quel cas ?** |

⚠️ **Le compte de secours mérite l'attention** : toute solution de PAM en a un, parce qu'il faut pouvoir intervenir quand elle est en panne. **C'est le compte le plus puissant de l'organisation, et il est souvent le moins surveillé.**

📚 **À approfondir ailleurs** : c'est le sujet du volume *Identités et accès* de cette collection.

#### 27.4 Les trois configurations réelles

| Configuration | Description | Fréquence |
|---|---|---|
| **Aucune séparation** | On administre depuis son poste bureautique | **Fréquente**, surtout en petite structure |
| **Rebond sans isolation** | Un point de rebond existe, mais joignable depuis le réseau bureautique | Fréquente — **protection partielle** |
| **Isolation complète** | Poste dédié, segment isolé, rebond journalisé, coffre | Minoritaire |

⚠️ **La deuxième est trompeuse.** Un point de rebond joignable depuis un poste bureautique compromis ne protège pas : **il ajoute une étape, pas une frontière**. La question à poser : *depuis quel poste peut-on l'atteindre ?*

🔥 **SCÉNARIO — le poste d'un administrateur est compromis**

| Question | Réponse |
|---|---|
| Symptôme | Un administrateur a ouvert une pièce jointe |
| Hypothèse naïve | « Un poste de plus à réinstaller » |
| Dépendance réelle | **Ce poste atteint le rebond, donc tous les serveurs** — configuration 1 ou 2 |
| Ce que le schéma aurait dû montrer | Depuis quels postes le rebond est atteignable |
| Ce qui décide de la gravité | **L'administrateur utilise-t-il le même poste pour la messagerie et l'administration ?** |

🔥 **SCÉNARIO — on ne peut plus administrer pendant l'incident**

| Question | Réponse |
|---|---|
| Symptôme | Compromission en cours. **Le rebond est dans le périmètre suspect** |
| Hypothèse naïve | « On se connecte quand même, il faut agir » |
| Dépendance réelle | **S'y connecter expose des identifiants privilégiés à l'attaquant** |
| Ce que le schéma aurait dû montrer | Un chemin d'administration de secours, hors du périmètre courant |
| Concevoir différemment | **Prévoir un accès de secours** — c'est une décision d'architecture, prise des années plus tôt |

⚠️ **Ce second scénario est celui qu'on découvre en crise**, et il n'a pas de solution improvisée. C'est le §45.4.

#### 27.5 Pourquoi il n'est jamais dessiné

| Raison | Réalité |
|---|---|
| Il ne sert pas le métier | Vrai, et sans importance |
| Il alourdirait le schéma | Vrai |
| **Il révèle comment on entre partout** | **La vraie raison, souvent inavouée** — §5.5 |

⚠️ **La conséquence en lecture** : un schéma sans chemin d'administration **ne montre pas le chemin le plus court vers la compromission totale**. C'est une omission lourde de conséquences, et elle est très répandue.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On passe par le bastion » | Un rebond existe | **Depuis quel poste peut-on l'atteindre ?** |
| « Les admins ont un compte séparé » | Deux identités par personne | **Sur le même poste ? Alors la séparation est partielle** |
| « L'infogérant se connecte en VPN » | Un accès distant de prestataire | **Vers quoi ? Depuis quel poste ? Tracé comment ?** |
| « L'iLO/iDRAC est sur un autre réseau » | Interfaces de gestion matérielle isolées | **Qui peut atteindre ce réseau ?** C'est le chemin le plus puissant |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Empêcher qu'un poste bureautique compromis donne l'administration | **Un poste supplémentaire par administrateur** |
| Journaliser et tracer les actions privilégiées | Un volume de journaux et un dispositif à exploiter |
| Cloisonner les identités d'administration | Des identités et des mots de passe supplémentaires à gérer |
| Un point de passage unique | **Un point de rupture** : s'il tombe, on ne peut plus rien administrer |

🏭 **TROIS TAILLES** — Atelier Martin : aucune séparation, **et c'est un risque assumé faute de moyens** — l'unique informaticien administre depuis son poste. HELIOMED : segment dédié, deux postes, accès depuis Lyon uniquement. Novaris : rebond avec enregistrement de session, coffre de secrets, **parce que 180 personnes ont des droits d'administration et qu'une traçabilité individuelle est exigée**.

---

### Chapitre 28 — Le réseau industriel

> **Où les règles s'inversent.** Le second chapitre décisif de la partie.

#### 28.1 L'inversion des priorités

| | Système de gestion | Système industriel |
|---|---|---|
| Priorité 1 | **Confidentialité** | **Disponibilité et sûreté** |
| Priorité 2 | Intégrité | Intégrité |
| Priorité 3 | Disponibilité | Confidentialité |
| Cycle de vie d'un équipement | 3 à 6 ans | **15 à 30 ans** |
| Fenêtre d'arrêt | Nuits, week-ends | **Arrêts de production planifiés à l'année** |
| Correctif | Appliqué selon un processus | **Validé par le constructeur, ou interdit** |
| Conséquence d'une erreur | Perte de données, indisponibilité | **Atteinte à la sécurité des personnes** |
| Qui décide | La direction des systèmes d'information | **La production, et parfois un organisme certificateur** |

> **Ce n'est pas que l'industriel soit « en retard ».** Ses contraintes sont différentes, et elles sont plus fortes. Un système qui pilote une machine ne peut pas redémarrer parce qu'un correctif l'exige.

⚠️ **La dernière ligne est celle qu'on oublie et qui bloque tous les projets** : modifier un système industriel peut invalider une certification, une garantie constructeur, ou une homologation de sûreté. **Ce n'est pas une question de volonté.**

#### 28.2 Ce qu'on y trouve

| Composant | Ce qu'il fait | Ce qui le caractérise |
|---|---|---|
| **Automate** | Pilote une machine ou un processus | Ancien, peu de mémoire, **souvent sans authentification** |
| **Poste de supervision** | Affiche et commande | Un système ancien, **figé par le constructeur** |
| **Historisation** | Enregistre les mesures | Souvent le point de contact avec le monde de gestion |
| **Poste d'ingénierie** | Programme les automates | **Le composant le plus sensible** — il peut modifier le programme |
| **Passerelle** | Fait communiquer les deux mondes | Le point le plus exposé |

⚠️ **Le poste d'ingénierie mérite une attention particulière.** Il détient les programmes des automates, souvent les seuls exemplaires. **Sa compromission permet de modifier ce qu'une machine fait physiquement** — et sa perte peut rendre un automate impossible à reprogrammer.

#### 28.3 Pourquoi l'authentification y est souvent absente

**Ce n'est pas une négligence, et c'est important à comprendre pour ne pas juger** :

| Raison | Explication |
|---|---|
| **L'ancienneté** | Un automate de 2004 ne connaît pas la notion d'authentification |
| **La sûreté** | En cas d'urgence, un opérateur doit pouvoir agir **sans délai** |
| **La disponibilité** | Un mécanisme d'authentification est un composant de plus qui peut tomber |
| **L'isolement supposé** | Le réseau était censé être séparé — et il l'était, en 2004 |

> **La sécurité de ces systèmes reposait sur l'isolement physique. C'est cet isolement qui a disparu**, pas la conception qui était mauvaise.

#### 28.4 La frontière entre les deux mondes

🖼 **SCHÉMA 28.1 — Les trois modèles de frontière**

```
  MODÈLE A — séparation totale
     [ gestion ]        [ industriel ]
     Aucun lien. Les données transitent par support amovible.
     → sûr, contraignant, de moins en moins praticable
     → ⚠️ le support amovible devient lui-même le vecteur

  MODÈLE B — passerelle unidirectionnelle
     [ gestion ] ◄──── [ historisation ] ◄──── [ industriel ]
     Les données remontent, rien ne descend.
     → le modèle de référence
     → ⚠️ suppose que RIEN n'ait besoin de descendre — vérifier

  MODÈLE C — lien filtré bidirectionnel
     [ gestion ] ◄───► [ pare-feu ] ◄───► [ industriel ]
     → le plus répandu en pratique, et le plus exposé
     → ⚠️ chaque règle ajoutée réduit la séparation
```

⚠️ **Le lien du §4.6 chez HELIOMED relève du modèle C**, créé en 2018 pour un export vers le contrôle de gestion, jamais reconsidéré. **La question de lecture devant toute passerelle industrielle** : *dans quel sens circule-t-elle, et qui l'a décidé quand ?*

#### 28.5 Les quatre chemins qui traversent malgré la séparation

**Même en modèle A, quatre chemins existent souvent** — et aucun n'est dessiné :

| Chemin | Pourquoi il existe | Ce qu'il permet |
|---|---|---|
| **Le poste d'ingénierie** | Il est parfois connecté aux deux mondes | Un pont direct |
| **La télémaintenance constructeur** | Contractuelle, souvent permanente | **Un accès distant d'un tiers** |
| **Le support amovible** | Transferts de programmes et de données | Le vecteur classique |
| **Le poste portable d'un intervenant** | Il se branche sur les deux réseaux, à des moments différents | Un pont différé |

⚠️ **La deuxième ligne est celle qui inquiète le plus en audit.** Une télémaintenance constructeur donne un accès distant permanent à un système de production, souvent créé il y a dix ans, rarement révisé, et **presque jamais dessiné**.

🔥 **SCÉNARIO — la production s'arrête après une mise à jour bureautique**

| Question | Réponse |
|---|---|
| Symptôme | Une ligne de production s'arrête. Aucune intervention sur le réseau industriel |
| Hypothèse naïve | « Une panne mécanique » |
| Dépendance réelle | **Le poste de supervision dépend d'un service du réseau bureautique** — annuaire, résolution, licence |
| Ce que le schéma aurait dû montrer | Les dépendances du réseau industriel **vers** le réseau de gestion |
| Concevoir différemment | Rendre le réseau industriel autonome pour ses dépendances — §26.2 |

⚠️ **C'est le scénario qui justifie la séparation mieux que n'importe quel argument de sécurité** : une dépendance non maîtrisée du monde industriel vers le monde de gestion **transforme un incident bureautique en arrêt de production**.

#### 28.6 Ce qu'on peut faire, et ce qu'on ne peut pas

| Action | Sur un réseau de gestion | Sur un réseau industriel |
|---|---|---|
| **Corriger** | Selon un processus | **Validé par le constructeur, ou interdit** |
| **Installer un agent** | Oui | **Non** — ressources, garantie, certification |
| **Scanner activement** | Oui | **Non** — un balayage peut arrêter un automate |
| **Observer passivement** | Oui | **Oui** — c'est la méthode de référence |
| **Segmenter** | Oui | **Oui, et c'est la mesure principale** |
| **Journaliser** | Oui | Partiellement — beaucoup d'équipements ne produisent rien |

⚠️ **La ligne du scan actif n'est pas une précaution excessive** : certains automates anciens cessent de fonctionner face à un trafic qu'ils n'attendent pas. **C'est un cas où un outil de sécurité peut provoquer l'incident qu'il devait prévenir.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est isolé » | Le réseau industriel est séparé | **Les quatre chemins du §28.5 existent-ils ?** |
| « On ne peut pas patcher » | Le constructeur ne valide pas | **Est-ce vérifié, ou supposé ?** Parfois la validation existe |
| « Le constructeur a un accès » | Télémaintenance | **Permanent ou à la demande ? Tracé ? Depuis quand ?** |
| « On a mis une DMZ industrielle » | Une zone intermédiaire | **Quel modèle — A, B ou C ?** Le sens des flux décide de tout |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Remonter des données de production vers la gestion | **Un chemin vers le monde industriel** |
| Superviser à distance | Un accès distant à protéger particulièrement |
| Séparer totalement | Des transferts manuels, lents, **eux-mêmes risqués** |
| Rendre l'industriel autonome | Des composants dupliqués — résolution, annuaire, temps |

🏭 **TROIS TAILLES** — Atelier Martin : deux machines à commande numérique, **sur le même segment que la bureautique** — et c'est le risque le plus élevé de son architecture, non identifié comme tel. HELIOMED : segment séparé à Saint-Étienne, avec le lien de 2018. Novaris : sans objet — pas d'activité industrielle.

⚠️ **La ligne Atelier Martin est la plus instructive de tout le tableau des trois tailles.** Une petite organisation n'échappe pas à la contrainte industrielle : **elle l'ignore**. L'absence de segmentation n'est pas un arbitrage quand personne n'a posé la question.

---

#### 🔬 Mini-lab 7 — Tracer les zones sur un schéma qui n'en montre aucune

**Objectif** — Reconstituer un découpage en zones à partir des seuls composants et flux.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 24 à 28

**Le schéma fourni** — aucune zone n'est représentée :

```
   Internet ─── [ P1 ] ─── [ P2 ] ─── [ S1 ] ─── [ S2 ] ─── [ S3 ]
                              │                     │
                           [ S4 ]                [ S5 ]
                              │
                        [ 400 postes ]
                              │
                           [ S6 ] ─── [ S7 ] ─── [ automates ]

   P1 : filtre les flux entrants          S4 : annuaire
   P2 : reçoit du 443, émet du 8080       S5 : base de données
   S1 : serveur web                       S6 : poste de supervision
   S2 : serveur applicatif                S7 : passerelle
   S3 : serveur de fichiers
```

❓ **Questions**
1. Combien de zones distinguez-vous, et où passent les frontières ?
2. Quels composants sont mal placés ?
3. Que manque-t-il ?

---

**Corrigé**

**1. Cinq zones**

| Zone | Composants | Frontière |
|---|---|---|
| Extérieur | Internet | — |
| Bordure | **P1** | Entre Internet et la DMZ |
| Zone démilitarisée | **P2** | **Frontière 2 non représentée** — §25.1 |
| Interne | S1, S2, S3, S4, S5, les 400 postes | — |
| Industriel | S6, S7, automates | Aucun équipement de filtrage entre l'interne et S6 |

**2. Trois anomalies de placement**

| Anomalie | Pourquoi c'est grave |
|---|---|
| **Aucune frontière entre la DMZ et l'interne** | P2 compromis atteint directement S1, puis tout le reste — §25.2 |
| **S6 est joignable depuis le segment des 400 postes** | Un poste compromis atteint la supervision industrielle **sans traverser aucun filtre** |
| **S4 (annuaire) dans le même segment que 400 postes** | Il devrait être dans un segment serveurs distinct |

**3. Ce qui manque** — au moins six éléments :

| Manquant | Effet |
|---|---|
| **Résolution de noms** | Sans elle, aucun de ces flux |
| **Réseau d'administration** | Comment administre-t-on ces sept serveurs ? Depuis les 400 postes ? |
| Sauvegarde | Aucun composant, alors que S5 contient les données |
| Les segments internes | 400 postes et 5 serveurs dans une même zone : sont-ils dans le même segment ? |
| Les sens de flux | Aucun trait n'est fléché |
| **Le sens de la passerelle S7** | Modèle B ou C ? La réponse change tout — §28.3 |

**Les trois erreurs attendues**

1. **Compter quatre zones** en oubliant la bordure. P1 et P2 ne jouent pas le même rôle.
2. **Ne pas relever l'absence de frontière 2.** C'est l'anomalie la plus discrète du dossier, et la plus lourde : rien ne la signale, seule son absence la trahit.
3. **Traiter le lien vers S6 comme normal** parce qu'il est dessiné. Un trait indique une possibilité, pas une autorisation — §3.2.

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> ✓ qu'un **pare-feu entre deux zones ne protège en rien des échanges à l'intérieur** de chaque zone ;
> ✓ qu'une **segmentation contournée protège moins qu'une segmentation absente** ;
> ✓ que la zone démilitarisée se définit par sa **seconde frontière**, celle qu'on oublie de dessiner ;
> ✓ que la question à poser à un site distant est : **qu'est-ce qui survit si le lien tombe** — et que personne ne le sait, faute d'avoir essayé ;
> ✓ que le **chemin d'administration est plus puissant que ce qu'il administre**, et qu'il n'est jamais dessiné — souvent pour de mauvaises raisons ;
> ✓ qu'un **rebond joignable depuis un poste bureautique ajoute une étape, pas une frontière** ;
> ✓ que dans le monde **industriel les priorités s'inversent**, et que ce n'est pas un retard mais une contrainte plus forte ;
> ✓ qu'une **absence de segmentation n'est pas un arbitrage quand personne n'a posé la question** ;
> ✓ que le **sans-fil peut être une porte directe sur le segment interne**, et que deux réseaux annoncés ne sont pas deux segments.
>
> **Ce que vous ne savez pas encore** : ce qui circule réellement dans tout cela, par quels chemins, et pourquoi certains chemins ne sont jamais dessinés. C'est l'objet de la Partie V — le cœur du cours.

---

## PARTIE V — Les flux

> **Le cœur du cours.** Sept chapitres, un par chose qui circule.
>
> **Pourquoi cette partie compte plus que les autres** : reconnaître un composant s'apprend en une heure. Suivre ce qui circule à travers dix composants, y compris ce qui n'est pas dessiné, est la compétence qui distingue un lecteur d'un spectateur.
>
> **Rappel du principe des trois flux** — trois familles, et ne jamais les confondre :
>
> | Famille | Question | Si elle s'arrête |
> |---|---|---|
> | **Métier** | Que transporte le service ? | Le service ne rend plus son objet |
> | **Dépendance** | Sans quoi ne peut-il pas s'établir ? | **Le service s'arrête, sans qu'on comprenne pourquoi** |
> | **Exploitation** | Comment tient-on, observe-t-on, restaure-t-on ? | Le service continue · **on devient aveugle** |

---

### Chapitre 29 — Suivre une requête

#### 29.1 Les douze étapes d'une requête ordinaire

Un salarié tape une adresse dans son navigateur. Voici ce qui se passe réellement — et **sur ces douze étapes, cinq figurent au schéma**.

🖼 **SCHÉMA 29.1 — Une requête, de bout en bout** · *Version graphique : douze étapes numérotées, les flux de dépendance en pointillé d'une autre couleur.*

```
 ①  Le poste doit traduire le nom en adresse
        poste ┄┄┄► [ résolution de noms ]        ← DÉPENDANCE
 ②  Réponse : une adresse
 ③  Le poste ouvre une connexion vers cette adresse
        poste ────► [ pare-feu ]                 ← peut refuser
 ④  Traversée du filtrage
        [ pare-feu ] ────► [ mandataire inverse ]
 ⑤  Négociation du chiffrement
        poste ┄┄┄► validation du certificat      ← DÉPENDANCE
 ⑥  Le mandataire termine la connexion et en ouvre une autre
 ⑦  Le mandataire demande une authentification
        [ mandataire ] ┄┄┄► [ annuaire ]         ← DÉPENDANCE
 ⑧  Le répartiteur choisit un serveur web
        [ répartiteur ] ────► [ web 2 ]
 ⑨  Le serveur web transmet à l'applicatif
        [ web 2 ] ────► [ applicatif ]
 ⑩  L'applicatif vérifie les droits, interroge la base
        [ applicatif ] ────► [ base ]
 ⑪  Dans cette architecture simplifiée, la réponse suit le chemin inverse
 ⑫  Chaque composant traversé écrit un journal
        chacun ┄┄┄► [ collecte ]                 ← EXPLOITATION
```

⚠️ **Sur l'étape ⑪** : le chemin de retour identique est vrai **dans cette architecture**, où chaque composant termine la connexion et en ouvre une autre. Ce n'est pas une règle générale — un routage asymétrique, un réseau de diffusion de contenu, un cache intermédiaire ou une architecture distribuée produisent des chemins de retour différents, **et c'est précisément ce qui rend certains diagnostics difficiles**.

#### 29.2 Ce que le schéma d'architecture montre de tout cela

| Étape | Sur le schéma 1.1 ? |
|---|---|
| ①② résolution de noms | ❌ |
| ③④ pare-feu | ✅ |
| ⑤ certificat | ❌ |
| ⑥ mandataire inverse | ✅ |
| ⑦ authentification | ❌ |
| ⑧ répartiteur | ✅ |
| ⑨⑩ web, applicatif, base | ✅ |
| ⑫ journalisation | ❌ |

**Cinq étapes visibles sur douze.** Et les sept invisibles comprennent **les trois qui peuvent faire échouer la requête sans qu'aucun composant dessiné ne soit en panne**.

⚠️ **PIÈGE — le diagnostic par le schéma**
Face à une requête qui échoue, un lecteur qui ne connaît que le schéma cherche parmi cinq composants. Un lecteur exercé en examine douze — et commence souvent par ceux qui ne sont pas dessinés, parce que ce sont ceux dont la panne est la moins visible.

#### 29.3 Le même service, quatre chemins différents

**C'est la section qui change la lecture d'un schéma**, et elle est rarement enseignée.

🖼 **SCHÉMA 29.2 — Quatre chemins vers le même service**

```
  ① UTILISATEUR EXTERNE
     Internet ──► [ FW ] ──► [ mandataire ] ──► [ web ] ──► [ app ]
     → passe par TOUS les contrôles
     → authentifié en amont · journalisé au mandataire · inspecté

  ② UTILISATEUR INTERNE
     poste ──────────────────────────────────► [ web ] ──► [ app ]
     → NE PASSE PAS par le mandataire
     → la résolution interne renvoie l'adresse du serveur — §14.5
     → aucun des contrôles du mandataire ne s'applique

  ③ UTILISATEUR NOMADE
     poste ══tunnel══► réseau interne ─────────► [ web ]
        OU
     poste ──► Internet ──► [ mandataire ] ──► [ web ]
     → DEUX chemins possibles selon la configuration
     → et souvent, personne ne sait lequel est emprunté

  ④ APPEL ENTRE SERVEURS
     [ autre application ] ─────────────────────► [ app ]
     → pas d'utilisateur · pas de mandataire
     → authentification par certificat ou par secret — §33
     → souvent le chemin le moins contrôlé de tous
```

| Chemin | Contrôles traversés | Journalisé où |
|---|---|---|
| ① Externe | Pare-feu · mandataire · application | Trois endroits |
| ② Interne | **Application seulement** | Un endroit |
| ③ Nomade | Variable, selon le chemin | Variable |
| ④ Serveur à serveur | **Souvent aucun** | Application, si elle le fait |

⚠️ **Ce que ce tableau impose en lecture** : un schéma dessine généralement le chemin ①. **C'est le mieux contrôlé, et c'est le moins fréquent en volume.** Les chemins ② et ④ portent l'essentiel du trafic réel, et ils traversent le moins de contrôles.

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez un dispositif de contrôle sur le mandataire inverse. Est-ce que tous les accès au service sont contrôlés ?*
**Non — seulement les accès externes.** Les postes internes atteignent souvent le serveur directement, sans traverser le mandataire, parce que la résolution interne leur donne l'adresse du serveur. La mauvaise décision évitée : **croire qu'un contrôle placé sur un chemin couvre tous les chemins**, et découvrir en incident que la compromission est passée par l'intérieur. C'est le chapitre 44.

#### 29.4 Reconstituer un chemin quand on n'a pas le schéma

**La méthode, en quatre questions** — utilisable en réunion, sans document :

```
1. D'où part la demande ?     poste interne · Internet · autre serveur
2. Quel NOM est demandé ?     → quelle vue de résolution s'applique ?
3. Que répond ce nom          → l'adresse du mandataire, ou celle du serveur ?
   depuis CET endroit ?
4. Que traverse-t-on          → chaque frontière est un point de contrôle
   entre les deux ?              et un point de journalisation
```

⚠️ **La question 3 est celle qui révèle le plus.** Deux personnes qui demandent le même nom depuis deux endroits différents peuvent obtenir deux adresses différentes — et donc suivre deux chemins avec deux niveaux de contrôle. **Un schéma ne peut pas exprimer cela.**

#### 29.5 Ce qui casse une requête, par étape

| Étape | Ce qui peut échouer | Symptôme caractéristique |
|---|---|---|
| ①② | Résolution indisponible ou mauvaise réponse | « Le site n'existe pas » · panne par vagues — §14.7 |
| ③④ | Règle de pare-feu, ou flux jamais ouvert | Délai d'attente, sans message |
| ⑤ | Certificat expiré, chaîne non reconnue | Avertissement de sécurité · **panne à un horaire net, sans intervention** — §17.4 |
| ⑥ | Mandataire arrêté ou saturé | Erreur immédiate, seulement de l'extérieur |
| ⑦ | Annuaire indisponible | Authentification refusée · cascade progressive — §16.3 |
| ⑧ | Tous les membres retirés par le contrôle de santé | **Le service tombe alors que les serveurs vont bien** — §13.2 |
| ⑨⑩ | Applicatif ou base indisponible | La page s'affiche, les actions échouent — §19.4 |

**Ce tableau est un outil de diagnostic à lui seul.** Le symptôme désigne l'étape, et l'étape désigne le composant — y compris quand il n'est pas dessiné.

---

### Chapitre 30 — Suivre une authentification

> Le flux de dépendance le plus universel, et le moins représenté.

#### 30.1 Trois questions à ne jamais confondre

**La distinction que presque personne ne fait, et qui structure tout le chapitre** :

| Question | Nom | Où elle se traite |
|---|---|---|
| **Qui es-tu ?** | Authentification | Annuaire, fournisseur d'identité, mandataire |
| **As-tu le droit de faire ceci ?** | Autorisation | **L'application, presque toujours** |
| **Qu'as-tu fait ?** | Traçabilité | L'application, et les journaux |

⚠️ **Confondre les deux premières est une erreur de lecture courante sur ce sujet.** Un mandataire qui authentifie sait *qui* entre ; il ne sait pas *ce que cette personne a le droit de faire*. **L'autorisation reste dans l'application** — et c'est pourquoi une faille d'autorisation n'est pas rattrapée par un mandataire, si bien configuré soit-il.

#### 30.2 Où l'on prouve son identité, et combien de fois

**Le constat** : dans une journée ordinaire, un utilisateur s'authentifie bien plus souvent qu'il ne le croit — et la plupart de ces authentifications sont invisibles.

| Moment | Contre quoi | Visible ? |
|---|---|---|
| Ouverture de session du poste | Annuaire | ✅ |
| Montage des lecteurs réseau | Annuaire | ❌ |
| Ouverture de la messagerie | Annuaire ou service en ligne | ❌ |
| Accès à une application interne | Annuaire, via le mandataire | ❌ |
| Accès à un service en ligne | Fédération ou compte propre | Selon |
| Appel d'un serveur vers un autre | Certificat ou secret — §33 | ❌ |
| Accès d'un administrateur | Second facteur, compte distinct | ✅ |

**Dans cet exemple, six des sept authentifications sont invisibles pour l'utilisateur**, et toutes dépendent d'un composant que le schéma ne montre pas.

#### 30.3 Ce qui se passe quand l'annuaire tombe

🖼 **SCHÉMA 30.1 — La cascade**

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT     ← rien ne se voit
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les jetons expirent, les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```

⚠️ **La cascade est progressive, et c'est ce qui la rend difficile à diagnostiquer.** Pendant les premières minutes, la majorité des utilisateurs ne constate rien. Les signalements arrivent par vagues, sur des symptômes différents, et rien ne les relie apparemment.

🔥 **SCÉNARIO — l'annuaire répond, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | Les contrôleurs répondent aux requêtes de test. Les ouvertures de session échouent |
| Hypothèse naïve | « L'annuaire est en panne » |
| Dépendance réelle | **La résolution de noms** : le poste ne trouve plus ses contrôleurs — §16.2 |
| Ce que le schéma aurait dû montrer | Que l'annuaire se localise par la résolution de noms |
| Comment le reconnaître | Interroger le contrôleur **par son adresse** fonctionne · par son nom, non |

⚠️ **C'est le chemin de diagnostic le plus difficile du cours** : deux composants invisibles, et l'un dépend de l'autre.

#### 30.4 Les trois modèles d'authentification

```
  A — CHAQUE APPLICATION AUTHENTIFIE
      [ app 1 : ses comptes ]  [ app 2 : ses comptes ]  [ app 3 : ... ]
      → aucune dépendance commune : une panne n'affecte qu'une application
      → autant de bases d'identités que d'applications
      → un départ suppose N suppressions, et il y en aura N-2

  B — AUTHENTIFICATION CENTRALISÉE
      [ app 1 ] [ app 2 ] [ app 3 ] ──► [ annuaire ]
      → un départ = une action · une politique commune
      → ⚠️ UNE DÉPENDANCE UNIVERSELLE
      → une compromission de l'annuaire donne tout

  C — FÉDÉRATION
      [ app ] ──► [ fournisseur d'identité ] ──► [ annuaire interne ]
                          (souvent externe)
      → fonctionne pour des applications hors de votre réseau
      → ⚠️ la dépendance sort de l'organisation
      → si le fournisseur est indisponible, VOUS ne pouvez rien faire
```

| Modèle | Départ d'un salarié | Panne du composant central | Maîtrise |
|---|---|---|---|
| **A** | N actions, et des oublis | Une application seulement | Complète |
| **B** | Une action | **Tout est bloqué** | Complète |
| **C** | Une action | **Tout est bloqué, et vous n'y pouvez rien** | Partielle |

⚠️ **Le modèle C déplace la dépendance hors de l'organisation.** C'est un arbitrage classique : on gagne en simplicité et en fonctionnalités, on perd la maîtrise de la disponibilité. **Principe du coût.**

#### 30.5 Le second facteur, et où il se place

| Placement | Ce qu'il protège | Ce qu'il ne protège pas |
|---|---|---|
| À l'ouverture de session du poste | L'accès au poste | Ce qui est déjà ouvert |
| Au mandataire inverse | Les accès **externes** | **Les accès internes directs** — §29.3 |
| Dans l'application | Cette application | Les autres |
| À l'accès distant | L'entrée sur le réseau | Ce qui se passe ensuite |

⚠️ **La deuxième ligne est une erreur de conception courante sur ce sujet** : placer le second facteur au mandataire, et croire l'application protégée. **Un poste interne l'atteint sans passer par là.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a du SSO » | Une authentification unique existe | **Contre quoi ? Pour quelles applications ? Et les autres ?** |
| « C'est fédéré » | Modèle C | **Le fournisseur est-il externe ? Que fait-on s'il tombe ?** |
| « On a mis du MFA » | Un second facteur | **Placé où ?** Il ne protège que ce qui passe par lui |
| « Il a les droits » | Confusion authentification / autorisation | **Qui les lui a donnés, et où sont-ils vérifiés ?** |

⚖️ **CONTRAINTE ET COÛT — l'authentification centralisée**

| Résout | Coûte |
|---|---|
| Une identité unique, des droits gérés en un point | **Une dépendance universelle** |
| Retirer un accès partout en une action | Une panne qui bloque tout progressivement |
| Appliquer une politique commune | Une compromission qui donne accès à tout |

---

### Chapitre 31 — Suivre une session

#### 31.1 Ce qu'une session change

**Le problème** : la plupart des échanges web sont **sans mémoire**. Chaque requête arrive sans savoir ce qui la précède. Il faut donc un mécanisme pour se souvenir qu'un utilisateur est déjà authentifié.

**Ce mécanisme — un jeton, un cookie — a une conséquence d'architecture majeure** :

> **Là où la session est stockée détermine ce que la redondance peut réellement apporter.**

#### 31.2 Les trois emplacements possibles

🖼 **SCHÉMA 31.1 — Où vit la session, et ce que ça change**

```
  A — SESSION LOCALE AU SERVEUR
      [web 1] session ici
      [web 2]                ← si l'utilisateur bascule ici : DÉCONNECTÉ
      → la redondance existe, elle ne protège pas l'utilisateur

  B — SESSION PARTAGÉE
      [web 1] ──┐
      [web 2] ──┼──► [ magasin de sessions ]
      [web 3] ──┘
      → bascule transparente · MAIS un composant de plus,
        et un nouveau point de rupture

  C — SESSION CHEZ LE CLIENT
      Le jeton est porté par le navigateur, signé, non stocké côté serveur
      → aucune dépendance à un magasin central
      → MAIS la révocation immédiate exige de réintroduire
        un mécanisme d'état ou de contrôle
```

| Modèle | Redondance réelle ? | Révocation immédiate ? | Composant de plus ? |
|---|---|---|---|
| **A — locale** | ❌ Apparente seulement | ✅ | Non |
| **B — partagée** | ✅ | ✅ | **Oui, et il devient critique** |
| **C — chez le client** | ✅ | ⚠️ **Différée, ou au prix d'un état réintroduit** | Non |

⚠️ **Le modèle A explique de nombreuses architectures où la redondance ne tient pas ses promesses.** Trois serveurs, un répartiteur, et pourtant les utilisateurs sont déconnectés dès qu'un serveur redémarre. Le schéma montre une redondance ; le comportement en session la contredit.

📌 **Le vrai compromis du modèle C**, plus intéressant que « on ne peut pas révoquer » :

Un jeton autoporté est vérifiable sans interroger personne — c'est tout son intérêt. **Le revers est qu'il reste valide jusqu'à son expiration, même si l'on souhaite l'invalider avant.** Plusieurs stratégies rétablissent une révocation, et **chacune réintroduit une part de ce que le modèle C cherchait à éviter** :

| Stratégie | Ce qu'elle réintroduit |
|---|---|
| Durée de vie très courte + renouvellement | Des appels fréquents au service d'émission |
| Liste de jetons révoqués | Un état partagé à consulter |
| Numéro de version de session | Une consultation à chaque requête |
| Introspection du jeton | Une dépendance au service d'émission |
| Révocation du jeton de renouvellement | Une révocation **différée**, pas immédiate |

⚠️ **C'est un compromis d'architecture, pas une impossibilité technique.** La question n'est pas *« peut-on révoquer ? »* mais **« à quel prix, et sous quel délai ? »**

#### 31.3 Le magasin de sessions, composant invisible et critique

**Le modèle B ajoute un composant qui n'apparaît sur presque aucun schéma**, et qui a trois propriétés :

| Propriété | Conséquence |
|---|---|
| **Toutes les requêtes le consultent** | Une latence ajoutée à chaque requête |
| **Sa panne déconnecte tout le monde** | **Un point de rupture qui n'est pas dessiné** |
| Il contient les sessions actives | **Sa compromission permet d'usurper des sessions en cours** |

🔥 **SCÉNARIO — tout le monde est déconnecté d'un coup**

| Question | Réponse |
|---|---|
| Symptôme | Tous les utilisateurs sont déconnectés simultanément. Les serveurs web vont bien |
| Hypothèse naïve | « Un redémarrage applicatif » |
| Dépendance réelle | **Le magasin de sessions** — modèle B |
| Ce que le schéma aurait dû montrer | Ce composant, et le fait que toutes les requêtes le traversent |
| Concevoir différemment | Le redonder · ou accepter le modèle A avec ses limites, en le sachant |

#### 31.4 Où passe le jeton, et où il fuit

| Endroit | Risque |
|---|---|
| Dans le navigateur | Vol par une extension, par un logiciel malveillant sur le poste |
| Dans les journaux | **S'il apparaît dans une adresse consultée, il est journalisé partout** |
| Chez le mandataire inverse | Il le voit en clair, en modes B et C — §12.3 |
| Dans les caches intermédiaires | Un jeton mis en cache peut être servi à un autre |

**La deuxième ligne est un cas d'école** : un jeton passé dans une adresse est enregistré par le poste, le mandataire, le pare-feu, le serveur web et la collecte de journaux. **Il devient lisible par tous ceux qui ont accès aux journaux** — et c'est le chapitre 34.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a de la persistance de session » | Le répartiteur renvoie sur le même serveur | **Modèle A** — la redondance ne protège pas les sessions |
| « Les sessions sont dans Redis » | Modèle B | **Le magasin est-il redondé ? Il n'est sur aucun schéma** |
| « On utilise des JWT » | Modèle C | **Quelle durée de vie ? Comment révoque-t-on ?** |
| « Les gens se font déconnecter » | Symptôme | **Tous en même temps, ou un tiers ?** La réponse désigne le modèle |

⚠️ **La dernière ligne est un excellent outil de diagnostic** : *tous en même temps* désigne le magasin partagé · *un tiers seulement* désigne un serveur redémarré avec des sessions locales.

---

### Chapitre 32 — Suivre une donnée

> **Principe 6 : le système d'information n'existe que pour traiter de la donnée.** Ce chapitre suit un enregistrement de sa création à sa destruction.

#### 32.1 Le cycle complet

🖼 **SCHÉMA 32.1 — Une donnée, de la saisie à l'oubli**

```
  ①  SAISIE          poste utilisateur
  ②  TRANSIT         mandataire · web · applicatif
  ③  STOCKAGE        base de données
  ④  RÉPLICATION     base secondaire, éventuellement autre site
  ⑤  SAUVEGARDE      support de sauvegarde, souvent hors ligne
  ⑥  COPIE           export, tableur, rapport, environnement de recette
  ⑦  DIFFUSION       courriel, partage de fichiers, service en ligne
  ⑧  ARCHIVAGE       stockage long terme
  ⑨  SUPPRESSION     de la base — mais pas des copies
```

⚠️ **L'étape ⑨ ne supprime que ⑨.** Une donnée effacée de la base subsiste dans les sauvegardes, les réplicas, les exports, les courriels et les environnements de recette. **C'est le principal écart entre la suppression déclarée et la suppression réelle.**

#### 32.2 Les copies qu'on ne voit jamais

| Copie | Où elle naît | Pourquoi elle échappe |
|---|---|---|
| **L'environnement de recette** | Copie de production pour tester | **Contient de vraies données, avec des protections moindres** |
| **L'export tableur** | Un utilisateur qui extrait | Part sur un poste, un partage, un courriel |
| **La sauvegarde** | Automatique | Souvent conservée bien au-delà du besoin |
| **Le cache** | Intermédiaires techniques | Invisible et temporaire — mais réel |
| **Le rapport** | Outil décisionnel | Une seconde base, avec ses propres droits |
| **Le journal applicatif** | La journalisation elle-même | **Il peut contenir la donnée** — §31.4 |
| **La messagerie** | Un fichier envoyé une fois | Conservé indéfiniment, chez l'expéditeur et le destinataire |

**La première ligne est la plus significative en sécurité** : un environnement de recette contient les données de production avec des protections inférieures, et il est **presque toujours hors du périmètre des schémas et des inventaires**.

⚠️ **La sixième mérite d'être signalée** : une application qui journalise le contenu de ses requêtes pour faciliter le diagnostic **duplique la donnée dans un système dont la rétention et les droits sont différents**. C'est une copie que personne n'a décidée.

#### 32.3 Ce qui multiplie les copies sans qu'on le décide

| Mécanisme | Combien de copies il crée |
|---|---|
| Une réplication de base | +1, en permanence |
| Une sauvegarde quotidienne conservée 30 jours | **+30** |
| Un environnement de recette rafraîchi mensuellement | +1, à jour d'un mois |
| Un outil décisionnel | +1, avec ses propres droits |
| Un export mensuel envoyé par courriel | **+N, indéfiniment** |

⚠️ **Le calcul est instructif.** Une base unique, sauvegardée quotidiennement sur trente jours, répliquée, copiée en recette et alimentant un outil décisionnel, **existe en trente-quatre exemplaires** — dont trente-trois ne sont sur aucun schéma.

#### 32.4 Le chemin de la sauvegarde, et pourquoi il compte

**Un flux d'exploitation qui n'apparaît nulle part, et qui est le plus transverse de l'architecture.**

```
   [ base ] ◄──── [ serveur de sauvegarde ] ────► [ support ]
       ▲                    │                        │
       │                    │  il atteint AUSSI :    │
       │                    ├──► serveurs de fichiers │
       │                    ├──► machines virtuelles  │
       │                    └──► annuaire             │
       │                                              │
   Trois questions :
      ① Qui initie ? (§3.6 — la sauvegarde, presque toujours)
      ② Avec quel compte ? (il atteint tout, donc il peut tout lire)
      ③ Le support est-il atteignable depuis le réseau ?
```

⚠️ **La troisième question décide de la gravité d'un rançongiciel.** Une sauvegarde atteignable en écriture depuis un compte compromis est chiffrée avec le reste. **C'est le scénario du §21.4**, et c'est ce qui distingue un incident d'une catastrophe.

🔥 **SCÉNARIO — la donnée effacée réapparaît**

| Question | Réponse |
|---|---|
| Symptôme | Une donnée supprimée sur demande réapparaît trois mois plus tard |
| Hypothèse naïve | « Une erreur de manipulation » |
| Dépendance réelle | **Une restauration partielle depuis une sauvegarde antérieure à la suppression** |
| Ce que le schéma aurait dû montrer | Le cycle complet, et les points où la donnée persiste |
| Concevoir différemment | Traiter la suppression comme un **processus sur toutes les copies**, pas comme une action sur la base |

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous devez évaluer l'impact d'une compromission de la base de production. Où cherchez-vous ?*
**Pas seulement dans la base.** Vous listez les neuf étapes : où sont les réplicas, les sauvegardes, la recette, les exports, les rapports, les journaux. Dans la majorité des cas, **la donnée existe en plusieurs endroits**, dont plusieurs ne sont sur aucun schéma. La mauvaise décision évitée : **déclarer un périmètre d'impact qui ne couvre qu'une fraction des copies**, et devoir le corriger publiquement quelques jours plus tard.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « La donnée a été supprimée » | Effacée de la base | **Et les sauvegardes ? La recette ? Les exports ?** |
| « La recette est une copie de prod » | Données réelles hors production | **Avec quelles protections ? Qui y a accès ?** |
| « On sauvegarde tout » | Un dispositif existe | **Le support est-il atteignable depuis le réseau ?** |
| « On a extrait un fichier » | Un export a été fait | **Où est-il maintenant ?** C'est une copie de plus |

---

### Chapitre 33 — Suivre un secret

#### 33.1 Ce qu'on appelle un secret

Mot de passe de service, clé d'interface applicative, certificat client, jeton d'accès, chaîne de connexion à une base. **Ils ont une propriété commune** : celui qui les détient est authentifié **sans être un utilisateur**.

⚠️ **C'est cette propriété qui les rend dangereux** : un secret volé ne déclenche aucun second facteur, aucune alerte de connexion inhabituelle, aucune expiration de session. **Il fonctionne exactement comme il est censé fonctionner.**

#### 33.2 Où ils vivent, et qui les voit en clair

| Emplacement | Fréquence | Qui le voit en clair |
|---|---|---|
| **Dans un fichier de configuration** | **Très fréquent** | Toute personne ayant accès au serveur · **et aux sauvegardes** |
| Dans le code source | Fréquent, et grave | Tous ceux qui ont accès au dépôt · **son historique le conserve** |
| Dans une variable d'environnement | Fréquent | Les processus, les journaux de démarrage, les outils de diagnostic |
| Dans un coffre à secrets | Le bon modèle | L'application, à l'exécution seulement |
| **Dans un ticket, un courriel, un tableur** | **Fréquent, jamais avoué** | Tous les destinataires, indéfiniment |

⚠️ **La deuxième ligne mérite d'être soulignée** : un secret retiré du code source reste dans l'historique du dépôt. **Le supprimer ne le supprime pas.** Seule sa rotation le rend inoffensif.

⚠️ **La première ligne aussi, et pour une raison qu'on oublie** : un secret dans un fichier de configuration se retrouve **dans toutes les sauvegardes** de ce serveur. Une sauvegarde de trois ans conserve un secret de trois ans — qui n'a peut-être jamais été changé.

#### 33.3 Le chemin d'un secret

```
  ① CRÉATION      qui le génère, et avec quelle qualité
  ② STOCKAGE      fichier · coffre · code
  ③ DISTRIBUTION  comment il arrive sur le serveur
                  → souvent manuellement, par quelqu'un qui l'a vu
  ④ USAGE         chargé en mémoire, parfois écrit dans un journal
  ⑤ ROTATION      changé, ou jamais
  ⑥ RÉVOCATION    ce qui se passe s'il fuit
```

**Les étapes ⑤ et ⑥ sont celles qui manquent presque toujours.** Un secret non tournant reste valide indéfiniment, et sa révocation n'a jamais été testée.

⚠️ **L'étape ③ est la plus sous-estimée.** Un secret distribué manuellement a été vu par au moins une personne, et il figure probablement dans un échange écrit — courriel, ticket, message. **La chaîne de confidentialité est rompue dès la mise en service.**

#### 33.4 Le coffre à secrets, et son paradoxe

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne plus stocker de secret en clair | Un composant de plus, **dont la panne empêche les applications de démarrer** |
| Tourner automatiquement | Une intégration applicative — pas toujours possible |
| Tracer qui accède à quoi | Une exploitation supplémentaire |

⚠️ **Le paradoxe, et il est réel** : un coffre indisponible peut empêcher le démarrage de tout ce qui en dépend. **Principe du coût en action** — et une nouvelle dépendance circulaire : le coffre a lui-même besoin d'un secret pour démarrer.

📌 **Comment on résout ce paradoxe en pratique** : les applications conservent le secret en mémoire après l'avoir obtenu. Une panne du coffre n'arrête donc pas ce qui tourne — **elle empêche seulement ce qui redémarre**. C'est une nuance importante : la panne est **différée jusqu'au prochain redémarrage**, comme celle de l'attribution d'adresses, §15.3.

🔥 **SCÉNARIO — l'application ne redémarre plus**

| Question | Réponse |
|---|---|
| Symptôme | L'application tourne. Après un redémarrage planifié, elle refuse de se lancer |
| Hypothèse naïve | « La mise à jour a cassé quelque chose » |
| Dépendance réelle | **Le coffre à secrets est injoignable** — ou le secret a expiré |
| Ce que le schéma aurait dû montrer | Que l'application dépend du coffre **au démarrage** |
| Comment le reconnaître | **Elle fonctionnait, elle ne redémarre plus, rien d'autre n'a changé** |

#### 33.5 Sur un schéma

Jamais. Un secret n'est ni un composant, ni un flux dessinable — c'est un attribut d'un flux existant.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le mot de passe est dans le fichier de conf » | Secret en clair sur le serveur | **Et dans toutes les sauvegardes** |
| « On l'a mis dans le vault » | Un coffre est utilisé | **Est-il un point de rupture au démarrage ?** |
| « On va le changer » | Rotation ponctuelle | **Combien d'endroits faut-il modifier ?** C'est ce qui empêche les rotations |
| « C'est un compte de service » | Une identité non humaine | **Depuis quand son secret n'a-t-il pas changé ?** |

---

### Chapitre 34 — Suivre un journal

> Le flux d'exploitation par excellence. **Sa rupture n'arrête aucun service — elle rend aveugle.**

#### 34.1 D'où naît un journal, et ce que chacun voit

| Source | Ce qu'elle voit | Ce qu'elle ne voit pas |
|---|---|---|
| **Poste** | L'activité de l'utilisateur, les processus | Ce qui se passe sur le réseau après |
| **Pare-feu** | Ce qui traverse, et ce qui est refusé | Le contenu, sauf inspection |
| **Mandataire** | Les destinations, le contenu si déchiffré | **Ce qui ne passe pas par lui** — §29.3 |
| **Serveur web** | Les requêtes reçues | **L'identité réelle si un mandataire est devant** |
| **Applicatif** | Les actions métier, les autorisations | Ce qui se passe sous lui |
| **Base** | Les requêtes, parfois les données lues | **L'utilisateur final**, si l'applicatif utilise un compte unique |
| **Annuaire** | Les authentifications | Ce qui est fait après |

#### 34.2 La perte d'identité en chemin

**Le problème le plus structurant du chapitre.**

```
   Marie ──► [ mandataire ] ──► [ web ] ──► [ app ] ──► [ base ]

   JOURNAL DU MANDATAIRE   « marie.durand a demandé /dossiers/4821 »
   JOURNAL DU WEB          « 10.0.2.15 a demandé /dossiers/4821 »
                             ↑ l'adresse du MANDATAIRE, pas de Marie
   JOURNAL DE L'APPLICATIF « utilisateur marie.durand a consulté
                             le dossier 4821 »   ← le seul complet
   JOURNAL DE LA BASE      « svc_app a exécuté SELECT ... »
                             ↑ le COMPTE DE SERVICE, pas Marie
```

⚠️ **Quatre journaux, deux identités différentes, et un seul qui relie l'utilisateur à l'action métier.** C'est le §43.3 : **l'applicatif est le seul point qui connaisse simultanément l'utilisateur réel et l'action**.

**Ce que cela impose** : corréler un journal de base avec un utilisateur réel exige de traverser trois journaux — et **cela suppose qu'ils partagent une horloge**. C'est pourquoi la synchronisation d'horloge est un flux de dépendance, principe des trois flux.

📌 **Les mécanismes qui atténuent le problème** : un mandataire peut transmettre l'adresse d'origine dans un en-tête · une application peut propager l'identité de l'utilisateur jusqu'à la base. **Les deux existent, les deux se configurent, et ni l'un ni l'autre n'est activé par défaut.**

#### 34.3 Le chemin d'un journal

```
  ① PRODUCTION     le composant écrit
  ② STOCKAGE LOCAL avec une rotation qui l'efface après N jours
  ③ TRANSPORT      vers une collecte centrale — souvent en clair
  ④ COLLECTE       normalisation, horodatage
  ⑤ CONSERVATION   pour une durée définie… ou pas
  ⑥ EXPLOITATION   recherche, alerte, corrélation
```

**Les trois points de perte** :

| Point | Ce qui se perd | Pourquoi personne ne le voit |
|---|---|---|
| **② → ③** | Si le transport échoue, la rotation locale efface | **Rien n'alerte sur l'absence de journaux** |
| **⑤** | Une conservation trop courte | On ne s'en aperçoit qu'au moment d'enquêter |
| **④** | Un format non reconnu est ingéré sans être exploitable | Le volume est correct, la recherche ne trouve rien |

⚠️ **Le premier est le plus pernicieux** : une chaîne de collecte cassée ne produit **aucun signal**. L'absence de journaux ressemble exactement à l'absence d'activité. **La seule protection est de superviser le volume reçu par source** — et de s'alerter quand il tombe à zéro.

⚠️ **Le deuxième est le plus coûteux.** Le délai moyen entre une compromission et sa détection dépasse souvent la durée de conservation des journaux. **On enquête alors sur une période dont il ne reste rien.**

🔥 **SCÉNARIO — l'enquête porte sur une période dont il ne reste rien**

| Question | Réponse |
|---|---|
| Symptôme | Une compromission est découverte. Elle date d'il y a quatre mois |
| Hypothèse naïve | « On va regarder les journaux » |
| Dépendance réelle | **La conservation est de 90 jours.** Il ne reste rien |
| Ce que le schéma aurait dû montrer | La durée de conservation, par source |
| Concevoir différemment | **Aligner la conservation sur le délai de détection observé**, pas sur le coût du stockage |

#### 34.4 Ce que la journalisation dit de l'architecture

**Une observation qui vaut méthode**, et il faut la formuler précisément :

> **Un composant peut produire un journal s'il est *en position de savoir* quelque chose.**

**Deux façons de l'être** :

| Position | Ce que le composant sait | Exemples |
|---|---|---|
| **Sur un chemin** | Ce qui le traverse | Pare-feu, mandataire, commutateur, routeur |
| **À l'origine d'une décision** | Ce qu'il a décidé, **sans qu'aucun flux ne traverse quoi que ce soit** | Une application qui autorise ou refuse · un poste qui lance un processus · un annuaire qui valide une identité |

⚠️ **La seconde ligne est celle que le modèle du point de passage manque.** Une application qui journalise *« Marie a exporté 4 000 lignes »* produit un événement métier **que rien n'a traversé au sens réseau**. C'est même la seule source capable de le produire — §34.2.

**Ce que cela donne comme méthode de lecture** :

```
   Devant chaque composant, une seule question :
   « Est-il en position de savoir quelque chose que personne d'autre ne sait ? »

   → OUI, et il journalise           ✅
   → OUI, et il ne journalise pas    ⚠️ angle mort — c'est le plus grave
   → NON                             pas de journal à en attendre
```

⚠️ **La deuxième ligne définit un angle mort structurel** : un composant qui sait et qui ne dit rien. C'est le cas de la plupart des applications métier — elles connaissent l'utilisateur et l'action, et elles ne journalisent que les erreurs techniques.

C'est le chapitre 43.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On log tout » | Beaucoup de sources sont collectées | **Combien de temps ? Et l'identité est-elle préservée ?** |
| « On a un SIEM » | Une collecte centrale existe | **Toutes les sources y arrivent-elles réellement ?** |
| « On n'a pas les logs » | La période est hors rétention | Combien de jours ? **Aligné sur quoi ?** |
| « L'IP dans le log est celle du proxy » | La perte d'identité — §34.2 | L'en-tête d'origine est-il transmis ? |

---

### Chapitre 35 — Du serveur au service

> Le chapitre qui transforme une lecture technique en décision métier.

#### 35.1 Ce qu'est un service

> **Un service est ce qui produit une valeur pour l'organisation.** Il ne correspond à aucun composant : il en mobilise plusieurs, et personne ne le voit sur un schéma technique.

**Exemple, chez HELIOMED** :

| Service métier | Composants mobilisés |
|---|---|
| **« Télésuivi HelioLink »** | Mandataire inverse · répartiteur · 3 serveurs web · applicatif · base · annuaire · résolution de noms · lien Internet · certificats |

**Neuf composants pour un service.** Et parmi eux, trois — annuaire, résolution, certificats — ne figurent sur aucun schéma.

#### 35.2 Ce qui tombe si ceci tombe

**La question centrale du cours**, et la méthode pour y répondre.

🖼 **SCHÉMA 35.1 — L'arbre de dépendance d'un service**

```
                  SERVICE « Télésuivi »
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   [ accès ]        [ traitement ]     [ données ]
        │                 │                 │
  ┌─────┼─────┐     ┌─────┼─────┐          ▼
  ▼     ▼     ▼     ▼     ▼     ▼      [ base ] ◄── point de rupture
lien  mandat. répart. web×3 applic.
      ▲         ▲          ▲
      │         │          │
      └─────────┴──────────┴──── [ résolution ] ◄── point de rupture invisible
                                 [ annuaire ]   ◄── point de rupture invisible
                                 [ certificats ]◄── point de rupture différé
```

**La lecture donne quatre points de rupture**, dont **trois ne sont pas sur le schéma d'architecture** :

| Composant | Effet de sa perte | Visible ? |
|---|---|---|
| **Base de données** | Service arrêté, données potentiellement perdues | ✅ |
| **Applicatif** | Service arrêté | ✅ |
| **Résolution de noms** | Service injoignable | ❌ |
| **Annuaire** | Authentification impossible | ❌ |
| **Certificats** | Service refusé par les navigateurs, **à une date connue d'avance** | ❌ |

#### 35.3 La superposition des flux

**La section la plus importante du chapitre**, et celle qui transforme la lecture d'une architecture.

**Ce que le lecteur croit voir** :

```
   User ──────► App ──────► DB
```

**Ce qui existe réellement** :

🖼 **SCHÉMA 35.2 — Dix flux superposés sur un même service**

```
                        [ résolution ]
                              ▲
                              ┊ ①
                              ┊
   [ poste ] ══②══► [ frontal ] ══③══► [ app ] ══④══► [ base ]
       ┊  ┊              ┊  ┊             ┊  ┊           ┊
       ┊  └──⑤──► [ annuaire ] ◄──⑤──────┘  ┊           ┊
       ┊                    ┊                ┊           ┊
       ┊                    ┊         ⑥──► [ secrets ]   ┊
       ┊                    ┊                            ┊
       └──⑦──┐              ┊              ┊             ┊
              ▼             ▼              ▼             ▼
          [ collecte de journaux ] ◄──────⑦─────────────┘
                                                         ┊
   [ administration ] ══⑧══► tous les composants         ⑧
                                                         ┊
   [ sauvegarde ] ◄══⑨══════════════════════════════════┘
                                                         ┊
   [ supervision ] ◄══⑩══════════════════════════════════┘
```

| # | Flux | Famille | Dessiné ? | Si interrompu |
|---|---|---|---|---|
| ① | **Résolution de noms** | Dépendance | ❌ | Le service devient injoignable |
| ② | **Requête utilisateur** | Métier | ✅ | Le service ne rend plus son objet |
| ③ | **Frontal vers application** | Métier | ✅ | Idem |
| ④ | **Application vers base** | Métier | ✅ | Idem |
| ⑤ | **Authentification** | Dépendance | ❌ | Plus personne ne peut entrer |
| ⑥ | **Secrets** | Dépendance | ❌ | L'application ne démarre plus — §33.3 |
| ⑦ | **Journaux** | Exploitation | ❌ | Le service continue · **on devient aveugle** |
| ⑧ | **Administration** | Exploitation | ❌ | On ne peut plus intervenir |
| ⑨ | **Sauvegarde** | Exploitation | ❌ | On ne peut plus restaurer |
| ⑩ | **Supervision** | Exploitation | ❌ | On ne sait plus si ça marche |

**Trois flux sur dix sont dessinés.** Et les sept invisibles se répartissent exactement selon le principe des trois flux : **trois dépendances dont la rupture arrête le service, quatre flux d'exploitation dont la rupture rend aveugle sans arrêter.**

#### 35.4 La méthode, en cinq étapes

```
1. NOMMER LE SERVICE      du point de vue du métier, pas de la technique
2. SUIVRE LE FLUX MÉTIER  les douze étapes du §29.1
3. AJOUTER LES DÉPENDANCES résolution · identité · certificats
                           · secrets · temps
4. AJOUTER L'EXPLOITATION  journaux · supervision · sauvegarde
                           · administration
5. TESTER CHAQUE NŒUD     « si celui-ci tombe, le service rend-il
                            encore son objet ? »
```

⚠️ **Les étapes 3 et 4 distinguent une cartographie utile d'une cartographie décorative.** Sans elles, on obtient un arbre où tous les points de rupture sont déjà connus — et qui n'apprend rien.

**Le rendu attendu** — une page par service critique :

```
SERVICE : ..............................
FLUX MÉTIER      n composants : ........................
DÉPENDANCES      n composants : ........................
EXPLOITATION     n composants : ........................
POINTS DE RUPTURE   n dont n INVISIBLES sur le schéma
CE QUI N'EST PAS TESTÉ : ...............................
```

⚠️ **La dernière ligne est celle qui a le plus de valeur en comité.** Elle transforme une cartographie technique en constat décisionnel — **principe de preuve**.

#### 35.5 Les trois niveaux de dégradation

| Niveau | Ce qui se passe | Exemple |
|---|---|---|
| **Arrêt** | Le service ne rend plus rien | Base indisponible |
| **Dégradation** | Le service fonctionne partiellement | Un serveur web sur trois : plus lent |
| **Cécité** | Le service fonctionne, on ne le voit plus | Collecte de journaux arrêtée |

**Les trois niveaux correspondent aux trois familles de flux de principe des trois flux** : métier → arrêt ou dégradation · dépendance → arrêt · exploitation → cécité. C'est ce qui rend la taxonomie utile.

⚠️ **Mais la correspondance n'est pas une loi, et il faut le dire.** La famille décrit **la fonction principale d'un flux, pas une garantie sur l'effet de sa panne**. Trois contre-exemples courants :

| Situation | Pourquoi elle sort du modèle |
|---|---|
| Un stockage saturé par les journaux | Un flux d'exploitation finit par **arrêter** le service |
| Une sauvegarde qui verrouille une ressource | Idem |
| Un outil de déploiement indispensable à un basculement | Un flux d'exploitation devient une dépendance en situation de panne |

**Et symétriquement** : certains flux métier disparaissent sans arrêter le service — une fonctionnalité secondaire, un export périodique.

> **La taxonomie est un modèle de raisonnement. Employez-la pour poser les bonnes questions, pas pour prédire des effets.**

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*On vous demande combien de temps le service « Télésuivi » peut rester indisponible. Que répondez-vous ?*
**Vous ne répondez pas — vous demandez d'abord de quoi il dépend.** Un service dont l'arbre comporte neuf composants dont trois invisibles n'a pas un seul délai de reprise : il en a autant que de causes possibles. La mauvaise décision évitée : **s'engager sur un délai de rétablissement calculé sur les seuls composants dessinés**, et découvrir en crise qu'une expiration de certificat ou une panne de résolution demande un délai tout autre.

---

#### 🔬 Mini-lab 8 — Tracer six flux sur un même schéma

**Objectif** — Distinguer les trois familles sur une architecture unique.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 29 à 34

Sur le schéma 1.1, tracez et classez : ① une requête d'un client externe · ② une authentification d'un salarié interne · ③ une sauvegarde nocturne · ④ un journal du mandataire vers la collecte · ⑤ la mise à jour d'un certificat · ⑥ un export de données vers un tableur.

---

**Corrigé**

| # | Flux | Famille | Chemin | Visible sur le schéma ? |
|---|---|---|---|---|
| **①** | Requête client | **Métier** | Internet → pare-feu → mandataire → répartiteur → web → applicatif → base | **Partiellement** — la résolution et l'authentification manquent |
| **②** | Authentification interne | **Dépendance** | Poste → annuaire | ❌ **Aucun trait** |
| **③** | Sauvegarde nocturne | **Exploitation** | Base → serveur de sauvegarde → support | ❌ Le serveur est dessiné, **son chemin non** |
| **④** | Journal vers collecte | **Exploitation** | Chaque composant → collecte | ❌ **La collecte n'est pas sur le schéma** |
| **⑤** | Mise à jour de certificat | **Dépendance** | Autorité → mandataire, manuellement ou automatiquement | ❌ Rien |
| **⑥** | Export vers tableur | **Métier**, sortant | Base → applicatif → poste → **fichier local** | ❌ **Le poste n'est pas dessiné** |

**Le bilan : un flux sur six est représenté, et partiellement.**

**Les trois erreurs attendues**

1. **Classer ③ en dépendance.** La sauvegarde n'arrête pas le service : elle empêche de le restaurer. C'est de l'exploitation — principe des trois flux.
2. **Oublier ⑥.** Un export n'est pas un flux technique, c'est pourtant celui par lequel les données sortent du périmètre contrôlé — §32.2.
3. **Tracer ② vers le mandataire** au lieu de l'annuaire. L'authentification d'un salarié interne ne passe pas par le mandataire inverse : le chemin interne est plus court, et différemment contrôlé — §29.3.

---

#### 🔬 Mini-lab 9 — Les points de rupture d'un service

**Objectif** — Construire un arbre de dépendance et identifier les ruptures invisibles.
**Durée** 35 min · **Difficulté** 🔴 avancé · **Prérequis** chapitre 35

**Le service** : « Commande en ligne » d'une organisation de distribution. Composants connus : deux serveurs web, un applicatif, une base répliquée, un mandataire inverse, un lien Internet redondé, un service de paiement externe.

❓ Construisez l'arbre, identifiez les points de rupture, classez-les par visibilité.

---

**Corrigé**

| Composant | Rupture ? | Visible ? | Nuance |
|---|---|---|---|
| Lien Internet | ⚠️ **Indéterminé** | ✅ | Annoncé redondé. **Deux liens du même opérateur, sur le même point d'entrée du bâtiment, ne redondent pas grand-chose** — *principe de preuve* |
| Mandataire inverse | ⚠️ **Indéterminé** | ✅ | **Un seul est mentionné** — à vérifier |
| Serveurs web ×2 | ❌ | ✅ | Sauf si sessions locales — §31.2 |
| **Applicatif** | ✅ **Oui** | ✅ | Unique |
| Base répliquée | ⚠️ | ✅ | **Le basculement a-t-il été testé ?** — §20 |
| **Résolution de noms** | ✅ **Oui** | ❌ | |
| **Annuaire ou fournisseur d'identité** | ✅ **Oui** | ❌ | |
| **Certificats** | ✅ **Oui**, à date connue | ❌ | |
| **Service de paiement externe** | ✅ **Oui** | ✅ | **Hors de votre maîtrise** — chapitre 38 |
| **Magasin de sessions** | ⚠️ | ❌ | **N'a pas été mentionné : existe-t-il ?** |

**Sept points de rupture ou incertitudes, dont quatre invisibles.**

**Les deux questions qui font la différence** :

1. *Le mandataire inverse est-il redondé ?* Il n'est mentionné qu'au singulier. Un seul mandataire annule la redondance de tout ce qui est derrière.
2. *Où sont les sessions ?* Si elles sont locales aux serveurs web, la redondance affichée ne protège pas l'utilisateur en cours de commande — §31.2. **La question n'a pas été posée dans l'énoncé, et c'est volontaire.**

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> ✓ suivre une **requête en douze étapes**, dont sept ne figurent sur aucun schéma ;
> ✓ que **six authentifications sur sept sont invisibles** pour l'utilisateur, et toutes dépendent d'un composant non dessiné ;
> ✓ décrire la **cascade progressive** d'une panne d'annuaire, et pourquoi elle est difficile à diagnostiquer ;
> ✓ que **l'emplacement de la session détermine ce que la redondance apporte réellement** ;
> ✓ suivre une **donnée en neuf étapes**, et savoir que la supprimer de la base ne la supprime que de la base ;
> ✓ qu'un **secret retiré du code source reste dans l'historique** — seule sa rotation le rend inoffensif ;
> ✓ que la **rupture d'un journal n'arrête rien et rend aveugle**, et que la conservation est souvent plus courte que le délai de détection ;
> ✓ construire l'**arbre de dépendance d'un service** en ajoutant les invisibles — l'étape qui distingue une cartographie utile d'une cartographie décorative ;
> ✓ que les **trois niveaux de dégradation** — arrêt, dégradation, cécité — correspondent exactement aux trois familles de flux.
>
> **Ce que vous ne savez pas encore** : comment appliquer tout cela de façon systématique à une architecture inconnue. C'est l'objet de la Partie VI, et de sa grille en sept passes.

---

## PARTIE VI — Lire une architecture

> Tout ce qui précède devient ici une **méthode**. Trois chapitres : la grille, dix architectures de complexité croissante, et ce que les tiers ajoutent à un schéma.

---

### Chapitre 36 — La grille de lecture en sept passes

#### 36.1 Pourquoi une méthode plutôt qu'un œil

**Le problème du lecteur non méthodique** : il regarde d'abord ce qui l'intéresse, ce qu'il reconnaît, ou ce qui est au centre du dessin. Il manque systématiquement les mêmes choses — les frontières implicites, les flux invisibles, ce qui n'a pas de doublure.

**Ce qu'une grille apporte** : un ordre fixe, qui garantit qu'on regarde ce qu'on n'aurait pas regardé.

🖼 **SCHÉMA 36.1 — Les sept passes**

```
  ①  LES ZONES        Où sont les frontières, et qu'est-ce qui les matérialise ?
  ②  L'ENTRÉE         Par où arrive un utilisateur externe ? Et un interne ?
  ③  LES DONNÉES      Où sont-elles, où vont leurs copies ?
  ④  L'IDENTITÉ       Où s'authentifie-t-on, contre quoi, combien de fois ?
  ⑤  LES FLUX         Quel chemin suit une requête ordinaire, en douze étapes ?
  ⑥  LES RUPTURES     Qu'est-ce qui n'a pas de doublure ?
  ⑦  L'INVISIBLE      Qu'est-ce qui n'est pas dessiné et existe pourtant ?
```

**L'ordre n'est pas négociable.** Chaque passe s'appuie sur la précédente : on ne peut pas suivre un flux (⑤) sans connaître les frontières (①) ; on ne peut pas identifier les ruptures (⑥) sans avoir suivi les flux.

#### 36.2 Les sept passes, en détail

**① LES ZONES** — *Où sont les frontières ?*

| Question | Ce qu'on cherche |
|---|---|
| Combien de zones ? | Comparer aux six de référence — §5.2 |
| Qu'est-ce qui matérialise chaque frontière ? | Filtrage, segmentation, ou **rien** — §5.3 |
| Y a-t-il une seconde frontière après la DMZ ? | §25.1 |
| Un composant est-il à cheval ? | Frontière assumée ou brèche — §5.4 |

**② L'ENTRÉE** — *Par où entre-t-on ?*

Trois entrées à chercher, pas une : l'utilisateur **externe** · l'utilisateur **interne**, dont le chemin est souvent plus court · l'**administrateur**, dont le chemin n'est jamais dessiné — §27.

**③ LES DONNÉES** — *Où sont-elles ?*

On applique le §32.1 : base, réplicas, sauvegardes, recette, exports, rapports. **La question utile n'est pas où elles sont stockées, mais en combien d'endroits elles existent.**

**④ L'IDENTITÉ** — *Où s'authentifie-t-on ?*

| Question | Pourquoi |
|---|---|
| Contre quel composant ? | Annuaire, fédération, ou base applicative — §30.3 |
| Combien de fois sur un même parcours ? | Une seule authentification pour dix accès est un choix, avec ses conséquences |
| Que se passe-t-il si ce composant tombe ? | §30.2 |

**⑤ LES FLUX** — *Quel chemin suit une requête ?*

Les douze étapes du §29.1, en distinguant les trois familles. **C'est la passe la plus longue et la plus productive.**

**⑥ LES RUPTURES** — *Qu'est-ce qui n'a pas de doublure ?*

| Question | Piège |
|---|---|
| Quels composants sont uniques ? | Un rôle dessiné une fois peut être plusieurs — §3.1 |
| Les exemplaires sont-ils sur des hôtes différents ? | §23 — la redondance qui n'en est pas |
| Le basculement a-t-il été testé ? | §20 — une réplication non testée est une croyance |
| Où sont les sessions ? | §31.2 — la redondance qui ne protège pas |

**⑦ L'INVISIBLE** — *Qu'est-ce qui n'est pas dessiné ?*

La liste du §3.4, à passer systématiquement : résolution de noms · annuaire · horloge · administration · sauvegardes · postes · services en ligne · liens partenaires · certificats · versions · le temps.

#### 36.3 Une lecture entièrement déroulée

**La méthode ne s'apprend pas en la lisant.** Voici les sept passes appliquées de bout en bout au schéma 1.1, telles qu'un lecteur exercé les conduirait — avec ses hésitations.

##### Passe ① — Les zones

*« Je compte trois zones dessinées : la DMZ, l'interne, l'industriel. Plus l'extérieur, implicite, et la bordure — les deux pare-feu. Cela fait cinq. »*

*« La frontière 1 est matérialisée : deux pare-feu. La frontière 2, entre DMZ et interne, **n'est pas dessinée**. Soit elle existe et n'est pas représentée, soit elle n'existe pas. C'est ma première question. »*

*« Le site industriel n'a qu'un lien. Par quoi passe-t-il ? Rien ne l'indique. Deuxième question. »*

**Constat de passe** : 5 zones · 1 frontière matérialisée sur 3 · 2 questions.

##### Passe ② — L'entrée

*« Utilisateur externe : Internet → pare-feu → mandataire. Clair. »*

*« Utilisateur interne : **rien n'est dessiné**. Les postes n'apparaissent pas. Or c'est de là que part la majorité des flux — §6.1. Et selon ce que répond la résolution interne, ils atteignent peut-être le serveur web directement, sans passer par le mandataire — §14.5. Troisième question. »*

*« Administrateur : **aucun chemin**. Quatrième question, et c'est celle qui compte le plus — §27.5. »*

**Constat de passe** : 1 entrée sur 3 dessinée.

##### Passe ③ — Les données

*« Une base est dessinée. Un serveur de fichiers aussi. Une sauvegarde. »*

*« Mais où sont les copies ? Réplicas ? Environnement de recette ? Exports ? Rapports ? **Rien** — §32.2. Cinquième question. »*

*« Et le chemin de la sauvegarde n'est pas dessiné : elle atteint la base, mais par où, et avec quel compte ? Sixième question — §21.4. »*

**Constat de passe** : 3 emplacements dessinés · nombre réel inconnu.

##### Passe ④ — L'identité

*« L'annuaire est dessiné. **Aucun trait ne s'y connecte.** C'est le cas canonique : tout s'y connecte, rien ne le montre — §1.1. »*

*« Combien de contrôleurs ? Un seul est dessiné. Si c'est le seul, c'est un point de rupture majeur. **Et même s'il y en a deux : sur des hôtes différents ?** — *principe de preuve*, §16.4. Septième question. »*

*« Où s'authentifie-t-on ? Sur le mandataire, ou dans l'application ? La réponse change ce qu'un poste interne traverse. Huitième question — §30.5. »*

**Constat de passe** : 1 composant dessiné, 0 relation, 2 questions.

##### Passe ⑤ — Les flux

*« Je suis une requête externe : douze étapes, cinq visibles — §29.1. »*

*« Je suis une requête interne : le chemin est plus court, et il ne traverse pas le mandataire. **Aucun des contrôles du mandataire ne s'y applique.** »*

*« Je suis une authentification : poste → annuaire. Non dessiné. »*

*« Je suis un journal : chaque composant → collecte. **La collecte n'est pas sur le schéma.** »*

**Constat de passe** : sur 4 flux suivis, 1 est partiellement dessiné.

##### Passe ⑥ — Les ruptures

*« Composants uniques dessinés : l'applicatif, la base, le mandataire — s'il est seul, ce que le schéma ne dit pas. »*

*« Composants uniques **non dessinés** : la résolution de noms, l'annuaire, les certificats. »*

*« Redondance apparente : trois serveurs web. **Sur des hôtes différents ? Où vivent les sessions ?** Sans réponse, je ne peux pas conclure — *principe de preuve*, §31.2. Neuvième et dixième questions. »*

**Constat de passe** : 3 ruptures visibles · 3 invisibles · 1 redondance non vérifiable.

##### Passe ⑦ — L'invisible

*« Je passe la liste de l'annexe H. »*

| Élément | Présent ? |
|---|---|
| Résolution de noms | ❌ |
| Annuaire | Dessiné, **non relié** |
| Synchronisation d'horloge | ❌ |
| Chemins d'administration | ❌ |
| Postes de travail | ❌ |
| Postes de prestataires | ❌ |
| Sauvegardes et leur chemin | Partiellement |
| Services en ligne | ❌ |
| Liens partenaires | ❌ |
| Certificats | ❌ |
| Environnements de recette | ❌ |
| Collecte de journaux | ❌ |
| Versions | ❌ |
| Le temps — date du schéma | ❌ |

**Constat de passe** : 12 éléments absents sur 14.

##### Le rendu, en une page

```
ARCHITECTURE : HELIOMED        DATE DU SCHÉMA : mars 2023 (non portée)
LU PAR : ...                   DATE DE LECTURE : ...

ZONES        5 · 1 frontière matérialisée sur 3
             frontière DMZ→interne : NON REPRÉSENTÉE
ENTRÉES      externe ✅ · interne ❌ · admin ❌
DONNÉES      3 emplacements dessinés · nombre réel inconnu
IDENTITÉ     1 annuaire dessiné, 0 relation · nombre de contrôleurs inconnu
FLUX         requête externe : 12 étapes, 5 visibles
             3 autres flux suivis : aucun dessiné
RUPTURES     3 visibles · 3 invisibles · 1 redondance non vérifiable
INVISIBLE    12 éléments absents sur 14

LES TROIS QUESTIONS À POSER À L'AUTEUR :
  1. Existe-t-il un filtrage entre la DMZ et le réseau interne ?
     → si non, ce n'est pas une DMZ
  2. Depuis quels postes administre-t-on ces serveurs ?
     → c'est le chemin le plus court vers la compromission totale
  3. Les trois serveurs web sont-ils sur des hôtes différents,
     et où vivent les sessions ?
     → sinon la redondance affichée ne protège pas
```

⚠️ **Sur les dix questions relevées, trois seulement sont posées.** C'est délibéré — §49.3, quatrième erreur : *une liste de dix recommandations est reçue comme un jugement global ; une recommandation unique, chiffrée et justifiée est reçue comme une contribution.* Les sept autres attendront.

**Durée réelle de cette lecture** : environ une heure, sans aucun accès technique, sans documentation, sans réunion.

#### 36.4 Le rendu d'une lecture

**Une lecture produit un document d'une page**, pas une opinion.

```
ARCHITECTURE : ................  DATE DU SCHÉMA : ........
LU PAR : .............           DATE DE LECTURE : ........

ZONES        n zones · frontières matérialisées : ...
             frontières déclaratives : ...
ENTRÉES      externe : ...  interne : ...  admin : ...
DONNÉES      en n endroits : ...
IDENTITÉ     contre : ...  si indisponible : ...
FLUX         requête type : ... étapes, dont ... invisibles
RUPTURES     n identifiées, dont n invisibles
INVISIBLE    n éléments absents du schéma

LES TROIS QUESTIONS À POSER À L'AUTEUR :
  1. ...   2. ...   3. ...
```

**La dernière section est la plus utile.** Une lecture ne se conclut pas par un jugement mais par **trois questions** — et c'est aussi ce qui la rend acceptable par ceux qui ont conçu l'architecture. Le chapitre 49 y revient.

⚠️ **Le temps que prend une lecture complète** : une heure pour une architecture simple, une demi-journée pour un système réel. **Ce n'est pas un exercice de dix minutes**, et une lecture bâclée produit exactement les jugements naïfs du chapitre 4.

### Chapitre 37 — Dix architectures

> Complexité croissante. Chacune suit le format : schéma · questions · lecture commentée · **ce qu'il fallait observer**.
>
> Les quatre premières sont développées ici ; les six suivantes figurent en annexe F, avec leur lecture complète.

#### 37.1 Architecture 1 — Une application interne, trois composants

```
   [ 40 postes ] ──► [ serveur applicatif ] ──► [ base ]
```

❓ **Trois questions** : où s'authentifie-t-on ? · qu'est-ce qui n'est pas dessiné ? · quel est le point de rupture ?

**Lecture** — c'est l'architecture d'Atelier Martin. Deux composants, un point de rupture par composant, aucune redondance. **Et c'est un choix cohérent** : quarante utilisateurs, une interruption d'une journée est tolérable, le coût d'une redondance n'est pas justifié par la contrainte.

👁 **CE QU'IL FALLAIT OBSERVER**
L'authentification n'est pas représentée. Deux cas possibles, et ils changent tout : soit l'application a sa propre base d'utilisateurs — auquel cas les mots de passe vivent dans la base, et leur qualité dépend de l'éditeur — soit elle interroge un annuaire, qui devient alors un troisième point de rupture invisible.

#### 37.2 Architecture 2 — Un site web public

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ web ] ──► [ base ]
```

❓ Où passe la frontière 2 ? · qui voit le contenu en clair ? · que se passe-t-il si le certificat expire ?

**Lecture** — le mandataire termine le chiffrement : **il voit tout en clair**. C'est le point le plus sensible du schéma, et il est en zone démilitarisée, c'est-à-dire dans la zone dont on suppose qu'elle sera compromise.

👁 **CE QU'IL FALLAIT OBSERVER**
Aucune frontière n'est représentée entre le mandataire et le serveur web. Si elle n'existe pas, un mandataire compromis atteint directement le web, puis la base. **La DMZ n'en est alors pas une** — §25.1.

#### 37.3 Architecture 3 — Trois niveaux, avec redondance partielle

C'est le schéma 1.1, celui d'HELIOMED.

❓ Où s'arrête la redondance ? · combien de points de rupture invisibles ? · pourquoi un seul applicatif ?

**Lecture** — quatre points de rupture, dont trois invisibles : base, applicatif, résolution de noms, annuaire. La redondance visible — trois serveurs web — porte sur le composant le plus facile à redonder et le moins critique.

👁 **CE QU'IL FALLAIT OBSERVER**
**La rupture de symétrie est une information, pas une erreur.** Trois web et un applicatif signalent un arbitrage : ici, le coût de licence de 2021 — §4.6. Un lecteur exercé demande l'histoire ; un débutant conclut à une incohérence. C'est le chapitre 4.

#### 37.4 Architecture 4 — Un système hérité mal documenté

```
   [ postes ] ──► [ AS400-PROD ] ──► ?
                        │
                   [ HERMES ] ──► [ export nocturne ] ──► [ décisionnel ]
                        ▲
                        └─── [ automates usine ]
```

❓ Que fait `HERMES` ? · qui l'administre ? · que se passe-t-il s'il tombe ?

**Lecture** — c'est le cas du §4.6. Un composant de 2011, portant un ancien outil de gestion de production, recevant un flux quotidien de l'usine. **Personne ne sait exactement ce qu'il fait encore.**

👁 **CE QU'IL FALLAIT OBSERVER**
Trois signes convergent : un nom hors convention · une position à cheval entre deux mondes · un flux nocturne. **Les trois désignent une strate ancienne** — §4.2. La bonne réaction n'est pas de proposer sa suppression, c'est de demander sa date et son motif. Il porte peut-être une intégration que plus personne ne sait refaire.

#### 37.5 Deux mauvaises architectures

> **Aussi formateur que les bonnes.** Apprendre à repérer l'excès d'architecture est aussi important que d'en repérer l'insuffisance.

##### Architecture 4 bis — l'insuffisance

```
                       Internet
                          │
                    [ pare-feu ]
                          │
        ┌─────────┬───────┴───────┬─────────┐
        │         │               │         │
   [ postes ] [ admin ]    [ application ] [ base ]
```

❓ **Qu'est-ce qui vous gêne ?**

| # | Constat | Pourquoi c'est grave |
|---|---|---|
| 1 | **Une seule zone** | Le pare-feu ne protège que du dehors. Tout est joignable de partout à l'intérieur — §24.1 |
| 2 | **L'administration au même niveau que les postes** | Un poste compromis atteint les outils d'administration — §27 |
| 3 | **La base joignable depuis les postes** | L'architecture en couches n'existe pas : on peut contourner l'application |
| 4 | **Aucune DMZ** | Si un service est publié, il l'est depuis l'interne |
| 5 | Ce qu'on ne voit pas | Résolution, annuaire, sauvegarde, journalisation — §3.4 |

⚠️ **Et pourtant, cette architecture n'est pas nécessairement fautive.** Chez une organisation de trente personnes, sans service publié, sans données sensibles, avec un informaticien à mi-temps, **elle peut être un arbitrage défendable** — §48.1. Ce qui la rend fautive, c'est de la trouver dans une organisation de sept cents personnes qui publie un portail client.

> **La question n'est jamais « cette architecture est-elle bonne ? » mais « pour quelle contrainte a-t-elle été conçue, et cette contrainte est-elle encore la bonne ? »**

##### Architecture 4 ter — l'excès

```
   40 salariés · 1 site · 1 application métier · 1 informaticien
                              │
                    2 centres de données
                              │
                        4 pare-feu
                              │
                     orchestration de conteneurs
                              │
                       maillage de services
                              │
                        12 microservices
                              │
                     2 fournisseurs cloud
```

❓ **Qu'est-ce qui justifie chacune de ces briques ?**

| Brique | Contrainte invoquée | Contrainte réelle |
|---|---|---|
| Deux centres de données | « Continuité » | **Quelle interruption est tolérable ? Personne ne l'a chiffrée** |
| Quatre pare-feu | « Sécurité » | Combien de frontières y a-t-il réellement à contrôler ? |
| Orchestration de conteneurs | « Modernité » | **Aucune** — une seule application, pas de variabilité de charge |
| Maillage de services | « Observabilité » | Aucune — douze services que rien n'obligeait à séparer |
| Douze microservices | « Agilité » | **Aucune** — une équipe, un cycle de livraison |
| Deux fournisseurs cloud | « Résilience » | **Deux plateformes à maîtriser au lieu d'une** |

⚠️ **Le diagnostic, et il est sévère** : cette architecture consomme probablement **cinq à huit exploitants** là où l'organisation en a **un**. Selon le §47.2, elle se dégradera en trois ans jusqu'au niveau réel de compétence disponible — **après avoir coûté le prix de l'ambition**.

**Ce qu'un lecteur exercé dit en réunion** :

> *« Je ne vois pas laquelle de ces briques répond à une contrainte chiffrée. Pouvez-vous me dire, pour chacune, quelle interruption ou quelle perte elle évite ? »*

**C'est la question du principe 9** — *ajouter n'est jamais gratuit* — appliquée à une architecture entière.

👁 **CE QU'IL FALLAIT OBSERVER, dans les deux cas**

| Architecture | L'erreur du lecteur débutant |
|---|---|
| **L'insuffisante** | Conclure « c'est mal fait » sans demander la taille, l'exposition et les moyens |
| **L'excessive** | Conclure « c'est bien fait » parce que les briques sont modernes |

> **Les deux erreurs sont la même** : juger l'architecture sans connaître la contrainte.

#### 37.6 Les six architectures suivantes

Développées en annexe F, avec le même format :

| # | Architecture | Ce qu'elle enseigne |
|---|---|---|
| 5 | Haute disponibilité complète | Le coût de la symétrie, et ce qu'elle ne couvre pas |
| 6 | Multi-sites | L'autonomie locale, et ce qui manque pour l'obtenir |
| 7 | Hybride | Un point de fragilité récurrent — chapitre 40 |
| 8 | Industrielle | L'inversion des priorités — chapitre 28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation, sans documentation |
| 10 | Le système complet d'HELIOMED | La synthèse du fil rouge |

⚠️ **La neuvième est la plus formatrice**, et c'est celle que vous rencontrerez en arrivant quelque part.

---

### Chapitre 38 — Les tiers sur un schéma

#### 38.1 Ce qui n'est pas chez vous et vous concerne

| Type de tiers | Ce qu'il apporte | Ce qu'il vous coûte en maîtrise |
|---|---|---|
| **Service en ligne** | Une fonction sans infrastructure | Aucune visibilité, aucun contrôle de disponibilité |
| **Prestataire d'infogérance** | Des compétences et une astreinte | **Des accès d'administration à votre système** |
| **Partenaire connecté** | Un échange automatisé | Un chemin d'entrée dont vous ne maîtrisez pas l'extrémité |
| **Fournisseur de composants** | Du logiciel intégré à vos produits | Une exposition héritée |
| **Fournisseur d'identité externe** | Une authentification simplifiée | **Une dépendance de disponibilité hors de vos mains** |

#### 38.2 Comment on les représente

🖼 **SCHÉMA 38.1 — Les trois façons de dessiner un tiers**

```
  A — LE NUAGE           [ ~~~ service ~~~ ]
      Ce qu'on ne détaille pas. Honnête, et peu informatif.

  B — LA BOÎTE NOIRE     ┌───────────────┐
                         │  fournisseur  │  ← on dessine l'interface,
                         └───────┬───────┘     pas l'intérieur
                                 │
                          protocole, sens,
                          authentification

  C — L'OMISSION         (rien)
      Le cas majoritaire. Le tiers n'est pas dessiné du tout.
```

**Le modèle B est le seul utile.** Il ne prétend pas décrire ce qu'on ne connaît pas, et il documente ce qui compte : **l'interface, le sens du flux, et la nature de l'authentification.**

#### 38.3 Les trois questions à poser à tout tiers

```
1. Que peut-il atteindre chez nous ?
   → un flux entrant · un accès d'administration · rien

2. Que pouvons-nous faire s'il tombe ?
   → rien, dégradé, ou fonctionnement autonome

3. Comment s'authentifie-t-il, et qui peut révoquer cet accès ?
   → et surtout : quelqu'un le pourrait-il en urgence, un dimanche ?
```

**La troisième est celle qu'on ne pose jamais.** Un accès de prestataire créé en 2018 fonctionne encore en 2026, et personne ne sait qui a le pouvoir de le couper.

#### 38.4 Le cas du prestataire d'infogérance

**L'un des tiers les plus puissants et les moins représentés**, et le §6.6 l'a annoncé.

| Ce qu'il possède | Conséquence |
|---|---|
| Des comptes d'administration sur vos serveurs | Une compromission chez lui devient une compromission chez vous |
| Des postes que vous ne maîtrisez pas | Hors de votre inventaire, hors de votre supervision |
| Un accès distant permanent | Un chemin d'entrée toujours ouvert |
| Une connaissance de votre architecture | Souvent supérieure à la vôtre |

⚠️ **Sur un schéma, il apparaît au mieux comme un nuage à côté du pare-feu.** Sa position réelle est **au cœur de la zone d'administration** — §27. **C'est l'un des écarts les plus importants entre l'architecture dessinée et l'architecture réelle en matière de sécurité.**

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Des compétences et une astreinte sans les recruter | **Des accès privilégiés hors de votre maîtrise** |
| Une capacité 24 heures sur 24 | Une dépendance contractuelle à la sécurité d'un tiers |
| Un coût prévisible | **Une surface d'attaque qui n'apparaît sur aucun schéma** |

🏭 **TROIS TAILLES** — Atelier Martin : un prestataire local, **avec un accès permanent et aucune traçabilité** — le risque le plus élevé de son architecture après le segment industriel. HELIOMED : un infogérant sur le parc bureautique et le support, accès via le rebond. Novaris : plusieurs prestataires, accès nominatifs, sessions enregistrées — **parce que la traçabilité individuelle est une exigence contractuelle de ses clients**.

---

## PARTIE VII — Les architectures modernes

> **Toujours : comment les lire, jamais comment les déployer.** Ces quatre chapitres n'enseignent aucune technologie ; ils enseignent ce que chacune change dans la lecture d'un schéma.

---

### Chapitre 39 — Le cloud

#### 39.1 La question qui structure tout le chapitre

> **Qu'est-ce qui disparaît du schéma sans disparaître du système ?**

C'est la seule question utile pour lire une architecture cloud. Le fournisseur masque une partie de l'infrastructure — mais le réseau, les identités, les données, les dépendances, les secrets et la résilience **existent toujours**. Ils ont simplement changé de forme, et souvent de responsable.

#### 39.2 Ce qui change et ce qui ne change pas

| Ne change pas | Change |
|---|---|
| Les trois familles de flux | **Qui exploite quoi** |
| Les points de rupture | Leur emplacement et leur visibilité |
| La nécessité d'authentifier | Le composant qui le fait |
| Le fait que la donnée soit quelque part | **Où « quelque part » se trouve** |
| La sédimentation | Elle **s'accélère** — le provisionnement est instantané |

⚠️ **La dernière ligne mérite d'être développée.** Créer une machine prenait des semaines ; cela prend des minutes. **La sédimentation du chapitre 4 s'accélère donc d'un ordre de grandeur** : des ressources créées pour un essai, jamais supprimées, jamais inventoriées. C'est le sujet central du volume Asset Management.

#### 39.3 La frontière de responsabilité

🖼 **SCHÉMA 39.1 — Où passe la ligne**

```
                    SUR SITE    INFRA.     PLATE-    LOGICIEL
                                LOUÉE      FORME     EN LIGNE

  Données             VOUS       VOUS       VOUS       VOUS
  Accès et identités  VOUS       VOUS       VOUS       VOUS
  Configuration       VOUS       VOUS       VOUS       VOUS
  Application         VOUS       VOUS       VOUS      fournisseur
  Exécution           VOUS       VOUS     fournisseur fournisseur
  Système             VOUS       VOUS     fournisseur fournisseur
  Virtualisation      VOUS     fournisseur fournisseur fournisseur
  Matériel            VOUS     fournisseur fournisseur fournisseur
```

**Les trois premières lignes restent des responsabilités à gouverner, même lorsque leur mise en œuvre est partagée avec le fournisseur.** Quel que soit le modèle, **vous répondez des données que vous y placez, des identités qui y accèdent et des choix de configuration qui vous sont offerts** — même si les moyens techniques de les mettre en œuvre varient fortement d'un service à l'autre — et ce sont précisément les sujets des volumes Asset Management et Identités de cette collection.

⚠️ **Une nuance qui compte, surtout en logiciel en ligne** : *responsable* ne signifie pas *maître de tous les réglages*. Le fournisseur décide de ce qui est configurable, et une partie de la configuration lui appartient — chiffrement au repos, cloisonnement entre clients, durée de conservation des journaux. **Vous êtes responsable de ce que vous pouvez régler, et vous dépendez de lui pour le reste.**

> **La question de lecture** : *quels réglages ce service m'expose-t-il, et lesquels décide-t-il à ma place ?*

⚠️ **Une erreur de lecture courante** : croire que la ligne descend uniformément. Elle descend **par composant**, et une organisation utilise généralement les quatre modèles simultanément. **Il n'y a pas une frontière, il y en a une par service.**

#### 39.4 Six comparaisons, et ce que chacune coûte

**C'est le cœur du chapitre.** Pour chaque transformation : *qu'est-ce que je n'exploite plus ? qu'est-ce que je dois toujours concevoir ? quelle nouvelle dépendance ai-je achetée ?*

##### A — Sur site contre infrastructure louée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Matériel, alimentation, virtualisation | **Système, correctifs, sauvegardes, réseau, identités** | La disponibilité du fournisseur · sa facturation à l'usage |

⚠️ **Ce qui surprend le plus** : les correctifs système restent entièrement à votre charge. **Louer une machine ne la maintient pas.**

##### B — Infrastructure louée contre plateforme managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Système, correctifs, une partie de la disponibilité | **L'application, les données, les accès, l'architecture** | Le calendrier de version du fournisseur · **une réversibilité faible** |

⚠️ **Le coût caché de B** : le fournisseur décide quand la version change. **Vous n'êtes plus maître du calendrier**, ce qui est un gain d'exploitation et une perte de maîtrise.

##### C — Machine virtuelle contre conteneur

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un système par application | **L'image, les dépendances embarquées, l'orchestration** | **Un système distribué complet** — §41 |

⚠️ **Le piège** : le conteneur ne supprime pas le système, **il le déplace dans l'image**. Une image jamais reconstruite embarque des composants jamais corrigés. La maintenance n'a pas disparu, elle a changé de main — et souvent, de personne responsable.

##### D — Base auto-hébergée contre base managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Correctifs, sauvegardes automatiques, réplication | **Le schéma de données, les accès, la performance** | Le calendrier de version · **des limitations sur ce qu'on peut faire** |

⚠️ **Ce qu'on découvre après** : certaines opérations d'administration ne sont plus possibles. **Le confort a un prix qui se paie en flexibilité.**

##### E — Monolithe contre microservices

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un déploiement couplé pour tout | **Les contrats entre services, la cohérence des données** | **Le réseau devient un composant du système** — §42.1 |

⚠️ **Le changement de nature** : entre deux microservices, un appel **traverse le réseau**, et hérite donc de tous ses modes de défaillance — perte, latence, duplication, réponse jamais reçue alors que l'action a eu lieu. Chaque appel devient un point de rupture potentiel, **qui n'existait pas dans le monolithe**.

##### F — Tunnel chiffré contre interconnexion dédiée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Une passerelle et son chiffrement | **Le routage, les identités, la résolution de noms** | Un lien contractuel · un délai de mise en place de plusieurs semaines |

⚠️ **Ce que l'interconnexion ne supprime pas** : elle donne un lien privé et performant. **Elle ne résout ni l'identité, ni la résolution de noms, ni les dépendances applicatives** — c'est le §40.2.

🔭 **À RECONNAÎTRE — SASE, SSE, CASB**

> ⚠️ **Avertissement préalable, et il est important.** Ces trois sigles viennent en partie de **taxonomies de marché**. Leur périmètre varie d'un fournisseur à l'autre, et deux produits portant le même sigle ne font pas nécessairement la même chose.

**① Ce que chacun désigne**

| Sigle | Ce qu'il recouvre |
|---|---|
| **SASE** | La **convergence de fonctions réseau et de sécurité distribuées**, délivrées notamment depuis le cloud — le pilotage du réseau étendu et les contrôles de sécurité dans une même offre |
| **SSE** | Le **sous-ensemble orienté sécurité** : les mêmes contrôles, **sans la composante réseau étendu** |
| **CASB** | Les **contrôles et la visibilité appliqués à l'usage des services en ligne** — qui utilise quoi, avec quelles données |

**② Quel problème cela résout.** Le §11.3 l'a posé : quand les applications sont en ligne et les postes nomades, **faire remonter le trafic au siège pour le contrôler n'a plus de sens**. Les contrôles doivent se déplacer là où sont les utilisateurs.

```
   MODÈLE HISTORIQUE
      [ poste ] ──► siège ──► [ contrôles ] ──► Internet
      → tout remonte · latence · le lien du siège porte tout

   MODÈLE DISTRIBUÉ
      [ poste ] ──► [ point de présence du fournisseur ] ──► Internet
                            │
                     les contrôles sont ICI
      → le poste nomade est contrôlé sans passer par le siège
```

**③ Ce que cela change dans les flux.** **Les contrôles quittent votre infrastructure.** Le point où l'on peut agir — chapitre 43 — n'est plus chez vous : il est chez un fournisseur, dans un point de présence que vous ne voyez pas.

**④ Le coût.** Une dépendance de disponibilité majeure — **si le service est indisponible, vos postes n'accèdent plus à rien** · une visibilité qui dépend de ce que le fournisseur expose · une réversibilité faible · **et un contrôle qui voit tout le trafic de vos salariés**, y compris personnel.

⚠️ **⑤ La phrase à retenir** :

> **Ces sigles décrivent des familles de capacités et des modèles d'architecture. Ils ne garantissent pas une implémentation identique d'un fournisseur à l'autre.**

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On passe en SASE » | **Quelles fonctions exactement ?** Le sigle ne le dit pas |
| « Le CASB voit nos SaaS » | **Ceux qu'il connaît.** Et les autres — §38.1 ? |
| « Les postes sortent par le SSE » | **Que se passe-t-il si le service est indisponible ?** |
| « C'est du Zero Trust » | Un modèle, pas un produit. **Quelle décision d'architecture cela recouvre-t-il ici ?** |

📚 **À approfondir ailleurs** : ces sujets relèvent des volumes *Identités et accès* et *Détection* de cette collection.

#### 39.5 Ce qui devient invisible

| Élément | Sur site | Dans le cloud |
|---|---|---|
| Le réseau | Segments, équipements | **Des règles logiques**, sans équipement à pointer |
| Les machines | Une baie, un hôte | **Un identifiant, une région** |
| Les frontières | Un pare-feu | Des groupes de règles, **beaucoup plus nombreux** |
| La sauvegarde | Un serveur | Une option de configuration — **activée ou non** |
| La redondance | Des équipements visibles | **Une case cochée** — ou pas |

⚠️ **Les deux dernières lignes produisent le plus de mauvaises surprises.** Une ressource cloud sans sauvegarde configurée n'a **aucune** sauvegarde — il n'existe pas de dispositif central qui rattrape l'oubli. **Sur site, quelqu'un finit par s'apercevoir qu'un serveur n'est pas sauvegardé. Dans le cloud, personne.**

🔥 **SCÉNARIO — la ressource supprimée par erreur n'était pas sauvegardée**

| Question | Réponse |
|---|---|
| Symptôme | Une base est supprimée. Aucune sauvegarde n'existe |
| Hypothèse naïve | « La sauvegarde a échoué » |
| Dépendance réelle | **Elle n'avait jamais été activée.** Ce n'est pas une option par défaut |
| Ce que le schéma aurait dû montrer | Rien — une sauvegarde cloud n'est pas un composant, c'est un paramètre |
| Concevoir différemment | Vérifier la configuration, pas l'existence d'un composant |

#### 39.6 Ce qui reste entièrement à votre charge

**La liste que le lecteur doit retenir**, parce qu'elle survivra à tous les modèles :

```
   ☐ Les DONNÉES : où elles sont, qui y accède, combien de copies
   ☐ Les IDENTITÉS : qui peut faire quoi, et qui peut le changer
   ☐ La CONFIGURATION : ce qui est activé, exposé, sauvegardé
   ☐ Les DÉPENDANCES : ce que votre service appelle, et réciproquement
   ☐ Les SECRETS : où ils vivent, qui les voit — §33
   ☐ La RÉSILIENCE : ce qui se passe si une région tombe
   ☐ La RÉVERSIBILITÉ : ce que coûterait un changement de fournisseur
```

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans le cloud » | La ressource est chez un fournisseur | **Quel modèle ?** La frontière de responsabilité change du tout au tout |
| « C'est managé » | Le fournisseur exploite une partie | **Laquelle exactement ?** Les correctifs ? Les sauvegardes ? |
| « On est multi-région » | La ressource existe à deux endroits | **Basculement automatique ou manuel ? Testé ?** — *principe de preuve* |
| « Le cloud est plus sûr » | Le fournisseur sécurise son socle | **Les trois premières lignes du §39.3 restent à vous** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Provisionner en minutes, payer à l'usage | **Des ressources créées sans être déclarées** |
| Déléguer l'exploitation de couches basses | Une dépendance à un tiers, et une visibilité réduite |
| Absorber une charge variable | **Une facture variable**, et des ressources oubliées qui coûtent |
| Bénéficier de services managés | Une réversibilité faible · **un calendrier de version subi** |

---

### Chapitre 40 — L'hybride

> **Un point de fragilité récurrent des architectures modernes**, et l'un des plus fréquents.

#### 40.1 Ce qu'est une architecture hybride

Un système dont une partie est sur site et une partie chez un fournisseur, **avec des flux entre les deux**. C'est la situation de la quasi-totalité des organisations, et elle est rarement le résultat d'une décision unique.

⚠️ **C'est presque toujours un état de sédimentation**, pas un choix d'architecture : une application est passée en ligne, puis une autre, puis la messagerie — et personne n'a jamais dessiné l'ensemble.

#### 40.2 Les trois liens, et leurs fragilités

🖼 **SCHÉMA 40.1 — Les trois liens d'une architecture hybride**

```
   ┌──────────────┐                        ┌──────────────┐
   │   SUR SITE   │                        │    CLOUD     │
   │              │  ① lien réseau         │              │
   │  [annuaire]──┼───────────────────────►│  [ services ]│
   │              │  ② synchronisation     │              │
   │  [postes]  ──┼───────────────────────►│              │
   │              │     d'identités        │              │
   │  [données] ──┼───────────────────────►│  [ copies ]  │
   └──────────────┘  ③ flux de données     └──────────────┘
```

| Lien | Ce qui le rend fragile |
|---|---|
| **① Réseau** | Souvent unique, parfois un simple accès Internet. **Sa perte coupe tout l'hybride** |
| **② Identités** | La synchronisation d'annuaire est un flux de dépendance critique. **Une panne bloque les authentifications côté cloud** |
| **③ Données** | Réplications, sauvegardes croisées, exports. **Le plus difficile à cartographier** |

#### 40.3 Le lien d'identités, en détail

**Un composant particulièrement fragile, et presque jamais supervisé.**

```
   [ annuaire interne ]
            │
            │  un composant de synchronisation
            │  s'exécute quelque part — souvent sur UNE machine
            ▼
   [ fournisseur d'identité en ligne ]
            │
            ▼
   [ services en ligne ]
```

**Ce qui casse, par ordre de fréquence** :

| Cause | Symptôme | Délai |
|---|---|---|
| Le composant de synchronisation est arrêté | Les créations et suppressions ne remontent plus | **Invisible pendant des jours** |
| Son certificat ou son secret a expiré | Idem | Idem |
| La machine qui l'héberge a été migrée ou supprimée | Idem | Idem |
| Le lien réseau est coupé | Les authentifications échouent, si le mode est direct | Immédiat |

⚠️ **La première ligne produit un incident silencieux et grave** : un salarié qui part est désactivé dans l'annuaire interne, **et reste actif côté cloud**. Personne ne s'en aperçoit — jusqu'à un audit, ou pire.

🔥 **SCÉNARIO — tout fonctionne, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | L'annuaire interne répond. Les services en ligne répondent. **Les nouveaux mots de passe ne fonctionnent pas** |
| Hypothèse naïve | « Les utilisateurs se trompent » |
| Dépendance réelle | **Le composant de synchronisation est arrêté depuis trois jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'est presque jamais dessiné |
| Comment le reconnaître | **Les anciens mots de passe fonctionnent, les nouveaux non.** C'est signé |
| Concevoir différemment | Superviser le composant **et la fraîcheur de la synchronisation**, pas seulement son état |

#### 40.4 La question à poser à toute architecture hybride

> **Que peut-on faire si le lien tombe ?**

| Réponse | Ce qu'elle révèle |
|---|---|
| Rien des deux côtés | Une dépendance mutuelle totale — le pire cas |
| Le local fonctionne, le cloud non | Le cas courant |
| Le cloud fonctionne, le local non | **Fréquent et rarement anticipé** : les postes nomades vont bien, le siège est bloqué |
| Les deux fonctionnent en autonomie | Rare, et coûteux à obtenir |

**Comme au §26.1, personne ne connaît la réponse**, parce que personne n'a coupé le lien pour voir.

#### 40.5 Trois architectures hybrides

```
  A — EXTENSION SIMPLE
      [ sur site ] ══lien══► [ quelques services en ligne ]
      → identités synchronisées · données majoritairement sur site
      → si le lien tombe : le sur site continue, le cloud est isolé

  B — BASCULE PROGRESSIVE
      [ sur site : legacy ] ◄══lien══► [ cloud : nouveau ]
      → les deux côtés portent du métier · flux dans les deux sens
      → si le lien tombe : LES DEUX sont dégradés
      → ⚠️ un état très répandu, et le plus fragile des trois

  C — CLOUD PRINCIPAL, SUR SITE RÉSIDUEL
      [ cloud : tout ] ◄══lien══ [ sur site : industriel, legacy ]
      → le cloud est autonome · le résiduel dépend du lien
      → si le lien tombe : seul le résiduel est isolé
```

⚠️ **Le mode B est un état de transition qui dure des années.** Il combine les contraintes des deux mondes et les avantages d'aucun — et il n'a été choisi par personne.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est en hybride » | Une partie est en ligne | **Quel mode ? Que se passe-t-il si le lien tombe ?** |
| « Les identités sont synchronisées » | Un composant réplique l'annuaire | **Où s'exécute-t-il ? Est-il supervisé ? Quelle fraîcheur ?** |
| « On a une interco » | Un lien privé existe | Redondé ? Et l'identité passe-t-elle par là ? |
| « Ça marche depuis chez moi » | Le nomade accède au cloud directement | **Il ne teste pas le lien du siège** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Adopter des services en ligne sans tout migrer | **Une architecture à deux mondes, avec les contraintes des deux** |
| Conserver les identités internes | **Un composant de synchronisation critique et invisible** |
| Garder des données sur site | Des flux de données à cartographier — le plus difficile |

---

### Chapitre 41 — Conteneurs et orchestration

#### 41.1 Ce qui change réellement

**La transformation en une ligne** :

```
   SERVEUR PHYSIQUE   1 machine · 1 système · 1 application
          ▼
   MACHINE VIRTUELLE  1 machine physique · N systèmes · N applications
          ▼
   CONTENEUR          1 système · N applications isolées
                      → le système n'est plus dupliqué
          ▼
   FONCTION           plus de machine visible du tout
                      → le code s'exécute à la demande
```

⚠️ **Ce que chaque étape supprime, et ce qu'elle déplace** :

| Transformation | Ce qui disparaît | Où cela va |
|---|---|---|
| Physique → virtuel | La dépendance à un matériel précis | **Vers l'hyperviseur et le stockage partagé** — §23.2 |
| Virtuel → conteneur | Un système par application | **Vers l'image**, qui embarque les dépendances |
| Conteneur → orchestration | Le placement manuel | **Vers le plan de contrôle**, qui décide où tourne quoi |
| Orchestration → fonction | La notion de serveur | **Vers la plateforme**, entièrement |

> **Rien ne disparaît du système. Tout se déplace — et souvent vers un composant que le schéma ne montre pas.**

#### 41.2 Pourquoi ces schémas sont illisibles

**Le problème** : un schéma de conteneurs représente souvent des dizaines d'objets éphémères, sans hiérarchie apparente, avec un vocabulaire propre.

**La cause** : on tente de représenter des **instances** alors que ce qui compte est la **structure**.

🖼 **SCHÉMA 41.1 — Deux façons de dessiner le même cluster**

```
  ILLISIBLE — les instances
     [c1][c2][c3][c4][c5][c6][c7][c8][c9][c10][c11][c12]...
     Quarante boîtes, sans hiérarchie, qui changent toutes les heures.

  LISIBLE — les classes et les frontières
     ┌─────────── CLUSTER ───────────────────────────┐
     │  ENTRÉE     [ contrôleur d'entrée ]           │
     │                     │                         │
     │  SERVICES    [ front ×n ] [ api ×n ]          │
     │                     │                         │
     │  ÉTAT        [ base ] ← hors du cluster       │
     │                                               │
     │  PLAN DE CONTRÔLE  [ orchestrateur ]          │
     └───────────────────────────────────────────────┘
```

**La règle de lecture** : dans un cluster, on ne lit pas les instances, on lit **quatre choses** :

| Quoi | Question | Pourquoi c'est celle-là |
|---|---|---|
| **L'entrée** | Par où arrive une requête externe ? | C'est le seul point stable du cluster |
| **Les services** | Quels rôles, en combien d'exemplaires *variables* ? | Le nombre change ; le rôle non |
| **L'état** | **Où sont les données ?** | Presque toujours **à l'extérieur** du cluster |
| **Le plan de contrôle** | Qui pilote ? | **Sa compromission donne tout le cluster** |

⚠️ **La troisième ligne est la plus importante en lecture.** Les conteneurs sont conçus pour être jetables ; ce qui ne l'est pas — les données — vit ailleurs. **Un schéma de cluster qui montre une base à l'intérieur est soit une simplification, soit une architecture à interroger.**

#### 41.3 Les quatre nouvelles dépendances

**Ce que l'orchestration ajoute, et qui n'existait pas avant** :

| Dépendance | Ce qu'elle fait | Si elle tombe |
|---|---|---|
| **Le plan de contrôle** | Décide où tourne quoi, redémarre ce qui échoue | Ce qui tourne continue · **rien ne peut plus être déployé, redémarré ni réparé** |
| **Le registre d'images** | Fournit les images au démarrage | **Un conteneur qui redémarre ne repart pas** |
| **La découverte de service** | Traduit un nom de service en adresse d'instance | **Les services ne se trouvent plus entre eux** |
| **La configuration distribuée** | Fournit les paramètres et les secrets | Les instances redémarrées échouent |

⚠️ **Les quatre partagent la même propriété** : leur panne **n'arrête pas ce qui tourne**, elle empêche **ce qui redémarre**. C'est le même mécanisme que le coffre à secrets, §33.4, et que l'attribution d'adresses, §15.3 — **une panne différée jusqu'au prochain événement**.

🔥 **SCÉNARIO — le cluster fonctionne, mais plus rien ne peut être réparé**

| Question | Réponse |
|---|---|
| Symptôme | Les applications répondent. Un déploiement échoue. Un conteneur mort ne repart pas |
| Hypothèse naïve | « Un problème avec le déploiement » |
| Dépendance réelle | **Le plan de contrôle est indisponible** — ou le registre d'images |
| Ce que le schéma aurait dû montrer | Que le plan de contrôle est un composant, avec sa propre disponibilité |
| Ce qui aggrave | **Chaque conteneur qui meurt ne revient pas.** La dégradation est progressive et irréversible |

⚠️ **C'est un cas de dégradation lente que rien ne signale.** Le service fonctionne à quatre-vingt-quinze pour cent, puis quatre-vingts, puis soixante — sans qu'aucune alerte ne se déclenche, parce que **le service répond toujours**.

#### 41.4 La découverte de service

**Un mécanisme qui mérite d'être compris**, parce qu'il n'apparaît nulle part et qu'il remplace quelque chose de familier.

```
   HORS CLUSTER
      app ──► résolution de noms ──► adresse fixe ──► base

   DANS UN CLUSTER
      app ──► découverte de service ──► adresse d'une instance
                                         qui change fréquemment
```

📌 **Une précision importante** : la découverte de service n'est **pas** un remplacement du mécanisme de résolution de noms. C'est une **fonction** — fournir un nom stable pour un ensemble d'instances qui changent — et elle est **fréquemment implémentée avec la résolution de noms elle-même**, avec des durées de vie très courtes. D'autres implémentations existent : registre dédié, mandataire local, configuration distribuée.

> **Ce qui change n'est pas le protocole. C'est que le nom désigne désormais un *service*, dont les instances apparaissent et disparaissent.**

⚠️ **Ce que cela change en lecture** : dans un cluster, **l'adresse n'a plus aucune signification durable**. Une règle de pare-feu par adresse ne fonctionne pas · un journal contenant une adresse n'identifie rien · un blocage par adresse est inopérant. **Tout doit se raisonner par identité de service, pas par adresse.**

C'est aussi ce qui rend l'inventaire d'un cluster particulièrement difficile — volume Asset Management, chapitre 6.

🔭 **À RECONNAÎTRE — maillage de services**

> **L'exemple parfait du principe du coût** : une brique résout un problème réel **et** en introduit un.

**① Qu'est-ce que c'est.** Une couche qui s'insère entre les services pour prendre en charge ce qu'ils devraient sinon implémenter chacun de leur côté : identité entre services, chiffrement, politiques d'appel, télémétrie, routage.

**② Ce que cela change conceptuellement.**

```
   SANS
      [ service A ] ◄──────────────► [ service B ]
      chaque service gère lui-même : chiffrement, réessais,
      identité, mesure

   AVEC
      [ A ] ◄─► [ couche ] ◄─────► [ couche ] ◄─► [ B ]
      la couche est déployée à côté de chaque service
      et intercepte tout ce qui entre et sort
```

**③ Ce qu'il apporte** : une identité par service, vérifiée à chaque appel · un chiffrement systématique entre services · des politiques centralisées — qui a le droit d'appeler qui · une télémétrie uniforme sans modifier le code · un routage fin pour les déploiements progressifs.

**④ Ce qu'il coûte** : **un composant à côté de chaque service** — donc autant de composants que d'instances · un plan de contrôle supplémentaire, critique · une latence ajoutée à chaque appel · **une compétence rare** · un diagnostic plus difficile, parce qu'un appel traverse maintenant deux intermédiaires.

⚠️ **⑤ Le message principal, et il est doctrinal** :

> **Tous les environnements de microservices n'ont pas besoin d'un maillage de services.**

Avec cinq services et une équipe, il apporte plus de complexité qu'il n'en résout. Avec quatre-vingts services et six équipes, il devient difficile de s'en passer. **La contrainte qui le justifie est le nombre d'interactions à gouverner, pas la modernité** — principe de la contrainte.

**⑥ En réunion** : *« on a un service mesh »* → **combien de services ? quelle contrainte cela résout-il que le code ne pourrait pas ?** · *« le mesh chiffre tout »* → **entre services seulement · et vers l'extérieur du cluster ?**

#### 41.5 Trois architectures de cluster

```
  A — CLUSTER MANAGÉ, APPLICATIONS SANS ÉTAT
      Le fournisseur exploite le plan de contrôle.
      Les données sont dans une base managée, hors cluster.
      → le modèle le plus simple · le moins d'exploitation
      → une dépendance forte au fournisseur

  B — CLUSTER AUTOGÉRÉ
      Vous exploitez le plan de contrôle, les nœuds, le réseau,
      le stockage, la découverte, le registre.
      → maîtrise complète
      → ⚠️ un système distribué complet · 2 à 4 exploitants minimum

  C — CLUSTER AVEC DONNÉES À L'INTÉRIEUR
      La base est dans le cluster, sur du stockage persistant.
      → une seule plateforme à exploiter
      → ⚠️ le cas le plus difficile : les conteneurs sont jetables,
        les données ne le sont pas. Les deux logiques s'opposent
```

⚠️ **Le mode C n'est pas fautif** — il existe des raisons de le choisir. **Il est simplement celui qui demande le plus de compétence**, et c'est souvent celui qu'on adopte sans le savoir, en installant une base dans le cluster « pour commencer ».

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur le cluster » | L'application tourne dans l'orchestrateur | **Et les données ? Dedans ou dehors ?** |
| « Ça scale automatiquement » | Le nombre d'instances varie | **Et la base derrière ? Elle ne scale pas toute seule** |
| « On a trois nœuds » | Trois machines portent le cluster | Le plan de contrôle est-il sur ces mêmes nœuds ? |
| « Le pod a redémarré » | Une instance a été recréée | **Ce qu'elle contenait localement est perdu** |
| « C'est déclaratif » | L'état voulu est décrit, l'orchestrateur l'applique | **Que se passe-t-il si le plan de contrôle ne peut plus l'appliquer ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Déployer de façon reproductible, mettre à l'échelle | **Un système distribué complet à exploiter** |
| Remplacer une instance sans interruption | **Quatre nouvelles dépendances**, toutes à panne différée |
| Densifier l'usage du matériel | Des actifs éphémères invisibles aux inventaires |
| Raisonner par service et non par machine | **Les adresses perdent leur signification** — journaux, filtrage, blocage |

🏭 **TROIS TAILLES** — Atelier Martin : **aucun conteneur**, et aucune contrainte ne le justifierait. HELIOMED : un petit cluster à Nantes pour la chaîne de construction, **parce que les développeurs en avaient besoin** — pas pour la production. Novaris : plusieurs clusters de production, **parce que la variabilité de charge saisonnière l'impose**.

---

### Chapitre 42 — Microservices, fonctions et services en ligne

#### 42.1 Pourquoi le schéma explose

**Le mécanisme** : découper une application en dix services indépendants multiplie par dix le nombre de boîtes, et par bien plus le nombre de flux entre elles.

| Architecture | Composants | Flux internes possibles |
|---|---|---|
| Application monolithique | 1 | 0 |
| Trois niveaux | 3 | 2 |
| **Dix microservices** | **10** | **jusqu'à 45** |

**Ce qu'on gagne** : chaque service évolue et se déploie indépendamment. **Ce qu'on perd** : la lisibilité, et la capacité à répondre simplement à *qu'est-ce qui tombe si ceci tombe*.

#### 42.2 Le changement de nature qu'on sous-estime

> **Dans un monolithe, un appel entre deux modules peut échouer fonctionnellement — mais il ne peut pas échouer *à cause du réseau*. Entre deux microservices, il le peut.**

**Ce qui apparaît**, ce n'est pas l'échec : c'est **une classe d'échec nouvelle**. L'appel peut être perdu, dupliqué, retardé, ou réussir sans que l'appelant le sache.

**Ce que cela introduit, et qui n'existait pas** :

| Problème nouveau | Ce qu'il faut concevoir |
|---|---|
| L'appel peut échouer | Une politique de réessai — **et le risque de doubler une action** |
| L'appel peut être lent | Un délai maximal — **et que fait-on quand il expire ?** |
| Le service appelé peut être saturé | Un mécanisme qui cesse d'appeler plutôt que d'aggraver |
| La cohérence n'est plus garantie automatiquement | **Une transaction unique ne couvre plus naturellement deux services** — §42.2 |
| L'ordre des appels compte | Une orchestration, explicite ou implicite |

⚠️ **La quatrième ligne est celle qui coûte le plus cher en conception.** Dans un monolithe, une base garantit qu'une opération réussit entièrement ou pas du tout. Entre deux services, **une opération peut réussir d'un côté et échouer de l'autre**.

📌 **Des mécanismes existent pour rétablir cette cohérence**, et il faut les connaître pour ne pas croire à une impossibilité :

| Approche | Principe | Coût |
|---|---|---|
| **Transaction distribuée** | Un coordinateur valide ou annule partout | **Lourde · lente · couplage fort** — souvent évitée |
| **Compensation** | Chaque étape a son action inverse, déclenchée en cas d'échec | Une action inverse à écrire pour chaque étape |
| **Cohérence différée** | On accepte un état incohérent temporaire, réconcilié ensuite | **Le métier doit accepter ce délai** |
| **Idempotence** | Rejouer une action produit le même résultat | À concevoir dans chaque service |

> **Ce n'est donc pas une impossibilité technique. C'est un coût de conception qui n'existait pas dans le monolithe — et une décision métier : qu'accepte-t-on comme état intermédiaire ?**

#### 42.3 Comment on lit malgré tout

**On ne lit pas un schéma de microservices comme un schéma classique.** Trois questions remplacent les sept passes :

```
1. QUEL EST LE CHEMIN D'UNE REQUÊTE TYPE ?
   Un seul parcours, pas la carte complète.

2. QUELS SERVICES SONT SUR CE CHEMIN ?
   Ce sont eux qui comptent. Les autres sont annexes.

3. LESQUELS N'ONT PAS D'ALTERNATIVE ?
   Ce sont les points de rupture — et ils sont peu nombreux.
```

**C'est le §35.4 appliqué** : on ne cartographie pas tout, on suit un service et on remonte ses dépendances.

🔥 **SCÉNARIO — un service lent en fait tomber cinq**

| Question | Réponse |
|---|---|
| Symptôme | Cinq services deviennent indisponibles. Un sixième est simplement lent |
| Hypothèse naïve | « Une panne générale » |
| Dépendance réelle | **Le service lent bloque ceux qui l'appellent**, qui bloquent à leur tour leurs appelants |
| Ce que le schéma aurait dû montrer | Les délais maximaux, et ce qui se passe à leur expiration |
| Concevoir différemment | Un mécanisme qui **cesse d'appeler** un service en difficulté plutôt que d'attendre |

⚠️ **Cette propagation en cascade est spécifique aux architectures distribuées**, et elle est contre-intuitive : **la lenteur se propage plus loin que la panne**. Un service arrêté échoue vite ; un service lent immobilise ses appelants.

🔭 **À RECONNAÎTRE — passerelle d'interfaces applicatives**

**① Qu'est-ce que c'est.** Une **façade contrôlée vers un ensemble d'interfaces applicatives**. C'est la formulation qui compte : ce n'est pas un mandataire inverse moderne, c'est une façade **avec une politique**.

**② Quel problème elle résout.** Quand dix services exposent chacun leur interface, chacun doit gérer l'authentification, les quotas, les versions, la journalisation. **La passerelle centralise ce qui est commun**, et laisse aux services ce qui est métier.

**③ Ce qu'elle centralise** :

| Fonction | Ce que le service n'a plus à faire |
|---|---|
| **Routage** | Savoir quelle version répond à quel appelant |
| **Authentification** | Vérifier un jeton — elle le fait en amont |
| **Quotas et limitation de débit** | Se protéger d'un appelant trop gourmand |
| **Transformations** | Adapter un format entre appelant et service |
| **Observabilité** | Produire une mesure uniforme de tous les appels |
| **Politiques d'interface** | Versions, dépréciation, contrats |

⚠️ **④ Le recouvrement avec le mandataire inverse est réel**, et il faut le nommer plutôt que de l'ignorer :

| | Mandataire inverse | Passerelle d'interfaces |
|---|---|---|
| Ce qu'il expose | **Des applications** | **Des interfaces applicatives** |
| Sa logique | Masquer, terminer, relayer | **Gouverner un contrat d'interface** |
| Ce qu'il connaît | Un chemin, un nom | **Une opération, un appelant, un quota** |

**En pratique, un même produit fait souvent les deux.** La question qui tranche : *existe-t-il parce qu'on publie des applications, ou parce qu'on gouverne des interfaces ?*

**⑤ Le coût.** Un point de passage obligé pour tous les appels — **donc un point de rupture** · une configuration qui grossit avec le nombre d'interfaces · une latence · **et le risque qu'elle devienne un fourre-tout** où l'on place de la logique métier qui n'y a pas sa place.

**⑥ En réunion** : *« ça passe par l'API gateway »* → **est-elle redondée ? qu'authentifie-t-elle exactement ?** · *« on a mis du rate limiting »* → **par appelant ou global ? que se passe-t-il quand la limite est atteinte ?**

---

🔭 **À RECONNAÎTRE — consensus distribué**

> **Conceptuel, et volontairement court.** Vous n'aurez pas à l'implémenter ; vous devez comprendre pourquoi c'est difficile.

**① Le problème.** Plusieurs machines doivent **se mettre d'accord sur un état commun**, malgré les pannes, les délais et les messages perdus.

**② Pourquoi c'est difficile.** Voici la phrase à retenir :

> **Répliquer une donnée est facile à dessiner. Maintenir un état cohérent entre plusieurs nœuds qui ne se font pas confiance sur le timing est un problème d'une tout autre nature.**

Deux nœuds qui reçoivent deux ordres contradictoires au même instant doivent aboutir au **même résultat**. Sans mécanisme, ils divergent — c'est le split-brain du §23.5.

**③ Où cela apparaît.** Dans tout ce qui doit décider collectivement : quel nœud est le maître · quelle configuration est la bonne · quel ordre les écritures ont-elles eu. **Orchestrateurs, bases distribuées, stockage réparti, services de configuration.**

**④ Ce que vous rencontrerez comme noms.** **Raft** et **Paxos** sont les algorithmes que vous verrez cités. Vous n'avez pas à les connaître — vous devez savoir que **c'est de cela qu'on parle**, et que leur présence signale un système distribué avec ses propres modes de défaillance.

**⑤ Ce que cela impose en architecture.** Un nombre de membres qui compte — §23.5, quorum · une latence entre membres qui devient structurante · **et une règle générale** :

> **Un système qui garantit une forte cohérence entre plusieurs nœuds paie ce choix en disponibilité ou en performance. Ce n'est pas un défaut d'implémentation, c'est un arbitrage.**

**⑥ En réunion** : *« c'est du Raft »* → un système distribué avec quorum. **Combien de membres ? Que se passe-t-il si la majorité est perdue ?**

#### 42.4 La communication asynchrone

> **Le modèle que le reste du chapitre n'a pas traité**, et qui change complètement la nature des pannes.

##### Le principe

Tout ce qui précède raisonne en **appels synchrones** : A appelle B et attend la réponse. Il existe un second modèle, aussi répandu :

```
   SYNCHRONE
      [ A ] ──appel──► [ B ]
      A attend. Si B est lent, A est lent. Si B tombe, A échoue.

   ASYNCHRONE
      [ A ] ──dépose──► [ FILE ] ──consomme──► [ B ]
      A dépose un message et continue. B le traite quand il peut.
      Si B tombe, A ne s'en aperçoit pas.
```

**Le composant intermédiaire** — file de messages, courtier, bus d'événements — porte les messages entre les deux. Il change trois choses fondamentales :

| | Synchrone | Asynchrone |
|---|---|---|
| A sait si B a traité | **Oui, immédiatement** | **Non** — il sait seulement qu'il a déposé |
| B tombe | A échoue | **A continue** · les messages s'accumulent |
| B est lent | A est lent | A n'est pas affecté · **la file grandit** |
| Ordre du traitement | Garanti par l'appel | **À concevoir** |
| Diagnostic | Le chemin est visible | **Le lien de cause à effet est rompu dans le temps** |

##### Ce que le découplage fait gagner

**C'est réel, et c'est pourquoi ce modèle existe** :

| Gain | Pourquoi |
|---|---|
| **B peut tomber sans arrêter A** | Le service reste disponible pour l'utilisateur |
| **Absorber une pointe de charge** | La file sert de tampon : A dépose vite, B rattrape ensuite |
| **Plusieurs consommateurs** | On ajoute des instances de B pour traiter plus vite |
| **Plusieurs destinataires** | Un même événement peut intéresser trois services, sans que l'émetteur les connaisse |
| **Découplage des versions** | A et B évoluent séparément |

⚠️ **Le quatrième gain est le plus structurant en architecture** : l'émetteur ne sait pas qui consomme. **Cela signifie qu'on peut ajouter un consommateur sans toucher à l'émetteur** — et aussi qu'**on ne sait plus, en lisant le code de A, ce que son message déclenche**.

##### Les sept problèmes qu'on achète

**Aucun n'existait dans le modèle synchrone.**

| # | Problème | Ce qu'il faut concevoir |
|---|---|---|
| **1** | **Accumulation** | La file grandit si B est plus lent que A. **Que faire quand elle est pleine ?** |
| **2** | **Retard** | Le traitement n'est plus immédiat. **Le métier accepte-t-il ce délai ?** |
| **3** | **Doublons** | Un message peut être livré deux fois. **B doit être idempotent** |
| **4** | **Ordre** | Deux messages peuvent arriver dans le désordre. Souvent garanti seulement partiellement |
| **5** | **Rejeu** | Que fait-on d'un message qui échoue ? Le remettre ? Combien de fois ? |
| **6** | **Message empoisonné** | Un message qui échoue toujours bloque la file — d'où une **file d'échecs** dédiée |
| **7** | **Observabilité** | **Le lien entre la cause et l'effet est rompu** : A a déposé à 10 h, B a échoué à 14 h |

⚠️ **Le troisième est celui qu'on découvre le plus tard et qui coûte le plus cher.** La plupart des systèmes de messagerie garantissent **au moins une livraison**, pas exactement une. **Un message de débit bancaire livré deux fois débite deux fois** — sauf si le consommateur a été conçu pour reconnaître qu'il l'a déjà traité. C'est l'idempotence du §42.2.

⚠️ **Le sixième mérite d'être connu, parce qu'il porte un nom qu'on entendra** : un message que le consommateur n'arrive jamais à traiter est écarté vers une **file d'échecs** — souvent appelée *dead-letter queue*. **Personne ne la regarde**, et c'est là que les messages perdus finissent.

##### Les trois topologies à reconnaître

```
  A — FILE POINT À POINT
      [ A ] ──► [ file ] ──► [ B ]
      Un message, un consommateur. Le message est retiré une fois traité.
      → traitement de travaux, commandes à exécuter

  B — PUBLICATION / ABONNEMENT
      [ A ] ──► [ sujet ] ──┬──► [ B ]
                            ├──► [ C ]
                            └──► [ D ]
      Un message, plusieurs destinataires. Chacun a sa copie.
      → événements métier : « une commande a été passée »
      → ⚠️ l'émetteur ignore combien de services l'écoutent

  C — JOURNAL D'ÉVÉNEMENTS
      [ A ] ──► [ journal ordonné, conservé ] ◄── [ B ] lit à son rythme
      Les messages sont conservés et relisibles.
      → un nouveau consommateur peut REJOUER l'historique
      → ⚠️ le journal devient un actif de données à part entière
```

⚠️ **Le mode C brouille une frontière du cours** : le journal d'événements **est à la fois un flux et un stockage**. Il contient l'historique, il peut être rejoué, et il porte donc des données au sens du §32 — avec les copies, la rétention et les obligations qui vont avec.

##### Le point de rupture déplacé

> **Le courtier devient le composant dont tout dépend.**

| S'il tombe | Effet |
|---|---|
| **Les producteurs** | Ne peuvent plus déposer — **ils échouent, ou accumulent localement** |
| **Les consommateurs** | Ne reçoivent plus rien · **ils ne le signalent pas, ils attendent** |
| **Les messages en attente** | Perdus s'ils n'étaient pas persistés |

⚠️ **La deuxième ligne est celle qui rend le diagnostic difficile.** Un consommateur privé de messages **ressemble exactement à un consommateur qui n'a rien à faire**. Rien n'alerte — c'est le même mécanisme que la collecte de journaux interrompue, §34.3.

📌 **La seule protection est de superviser le débit** : messages déposés, messages consommés, taille de la file. **Une file qui ne bouge plus est un incident silencieux.**

🔥 **SCÉNARIO — les commandes ne partent plus depuis trois jours**

| Question | Réponse |
|---|---|
| Symptôme | Le site de commande fonctionne. Les clients confirment. **Rien n'arrive en logistique** |
| Hypothèse naïve | « Un problème dans le système logistique » |
| Dépendance réelle | **Le consommateur est arrêté.** Les messages s'accumulent dans la file depuis trois jours |
| Ce que le schéma aurait dû montrer | La file, et le fait que le producteur ne sait pas si quelqu'un consomme |
| Comment le reconnaître | **Aucune erreur nulle part** — chaque composant fait exactement ce qu'on lui demande |
| Concevoir différemment | Superviser **la taille de la file et l'âge du plus ancien message**, pas l'état des services |

⚠️ **C'est le scénario le plus caractéristique de l'asynchrone** : le découplage a parfaitement fonctionné. **A n'a jamais été affecté par la panne de B — et c'est exactement le problème.**

🔥 **SCÉNARIO — le rejeu produit des doublons**

| Question | Réponse |
|---|---|
| Symptôme | Après un incident, des opérations métier apparaissent en double |
| Hypothèse naïve | « Un bug applicatif » |
| Dépendance réelle | **Des messages ont été rejoués**, et le consommateur n'était pas idempotent |
| Ce que le schéma aurait dû montrer | Rien — c'est une propriété du consommateur, pas de la topologie |
| Concevoir différemment | **Chaque consommateur doit pouvoir reconnaître un message déjà traité** |

##### Quand choisir l'asynchrone

| Le besoin | Modèle |
|---|---|
| L'utilisateur attend le résultat | **Synchrone** |
| Le traitement est long et l'utilisateur n'a pas à attendre | **Asynchrone** |
| Plusieurs services doivent réagir au même événement | **Asynchrone**, publication/abonnement |
| La charge arrive par pointes | **Asynchrone**, la file amortit |
| Le résultat doit être cohérent immédiatement | **Synchrone** |
| Le service appelé est peu fiable ou lent | **Asynchrone**, pour le découpler |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Découpler la disponibilité de deux services | **Un courtier à exploiter, et dont tout dépend** |
| Absorber les pointes de charge | Une file à surveiller · **une accumulation silencieuse possible** |
| Permettre plusieurs consommateurs | L'émetteur ne sait plus ce qu'il déclenche |
| Réessayer sans perdre | **Des doublons à gérer dans chaque consommateur** |
| Rejouer l'historique | Un stockage de données à part entière, avec ses obligations |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est asynchrone » | Un intermédiaire porte les messages | **Que se passe-t-il si le consommateur est arrêté ?** |
| « Il y a du retard dans la queue » | Accumulation | **Depuis quand ? Quel est l'âge du plus ancien message ?** |
| « On a mis un retry » | Réessai automatique | **Le consommateur est-il idempotent ?** Sinon, doublons |
| « C'est parti dans la DLQ » | File d'échecs | **Qui la regarde ? Depuis combien de temps ?** |
| « On publie un événement » | Publication/abonnement | **Combien de services l'écoutent ? L'émetteur ne le sait pas** |
| « Le broker est down » | Le courtier est indisponible | **Les messages en attente étaient-ils persistés ?** |

🏭 **TROIS TAILLES** — Atelier Martin : aucun courtier, **et aucune contrainte ne le justifierait**. HELIOMED : une file pour les remontées de dispositifs médicaux, **parce que les appareils émettent en continu et que le traitement ne doit pas les bloquer**. Novaris : un bus d'événements central, **parce que sept systèmes doivent réagir à une même commande** — et c'est la contrainte, pas la taille.

#### 42.5 Les fonctions

| | |
|---|---|
| **Ce que c'est** | Du code exécuté à la demande, sans serveur visible |
| **Ce qui change en lecture** | Il n'y a **rien à dessiner** entre les appels |
| **Le point de rupture** | La plateforme qui les exécute, et les services qu'elles appellent |
| **Ce qui devient difficile** | Savoir ce qui existe : une fonction créée n'apparaît nulle part |

⚠️ **Deux propriétés qui surprennent** :

**Le démarrage à froid.** Une fonction qui n'a pas été appelée depuis un moment met plus longtemps à répondre — le temps que la plateforme la charge. **Cela change le comportement observé selon la fréquence d'appel**, et rend le diagnostic déroutant.

**L'absence de limite naturelle.** Une fonction peut être appelée un million de fois sans que rien ne l'empêche — sauf ce qu'elle appelle derrière. **Une base dimensionnée pour cent connexions simultanées ne survit pas à mille fonctions déclenchées ensemble.** La contrainte s'est déplacée, elle n'a pas disparu.

#### 42.6 Le service en ligne, boîte noire sur votre schéma

**Un cas très répandu dans les architectures modernes**, et le §38.2 en donne la représentation : modèle B, la boîte noire avec son interface documentée.

**Les cinq questions, reprises du §38.3 et complétées** :

| Question | Pourquoi elle compte |
|---|---|
| Que peut-il atteindre chez nous ? | Souvent : l'annuaire, par fédération |
| Que faisons-nous s'il tombe ? | **Aucune action possible de votre part** |
| Comment s'authentifie-t-il ? | Fédération, jeton, clé d'interface |
| **Où sont nos données chez lui ?** | La question qu'on ne pose qu'après l'incident |
| **Que se passe-t-il si nous partons ?** | La réversibilité — presque jamais évaluée à la souscription |

⚠️ **La différence fondamentale avec un composant sur site** : **vous ne pouvez agir sur aucune de ses couches internes.** Vous ne le corrigez pas, vous ne le redondez pas, vous n'observez pas son infrastructure.

📌 **Mais les cinq actions du chapitre 43 ne sont pas toutes indisponibles pour autant** — elles se déplacent :

| Action | Dans l'infrastructure du fournisseur | **Ce que vous pouvez malgré tout** |
|---|---|---|
| **Observer** | ❌ | Les journaux d'audit du service, s'il en expose · les appels par interface |
| **Filtrer** | ❌ | Restreindre les origines autorisées · un dispositif intermédiaire d'accès |
| **Authentifier** | ❌ | **Entièrement** : c'est vous qui décidez du fournisseur d'identité et du second facteur |
| **Segmenter** | ❌ | Cloisonner par droits et par espaces, pas par réseau |
| **Journaliser** | ❌ | Récupérer les journaux exposés, et les collecter chez vous |

> **La formulation exacte** : vous perdez le **contrôle de l'infrastructure**, pas toute capacité d'action. Ce qui vous reste est **au niveau de la configuration, des identités et des données** — et c'est loin d'être rien.

⚠️ **Ce qui varie énormément d'un service à l'autre** : la richesse des journaux exposés, la granularité des droits, et la possibilité d'exiger un second facteur. **Ce sont des critères de choix**, et ils s'évaluent avant de souscrire — pas après.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a découpé en microservices » | Plusieurs services indépendants | **Combien d'appels sur le chemin d'une requête ? Que se passe-t-il si l'un est lent ?** |
| « C'est du serverless » | Des fonctions | **Qu'appellent-elles ? La base derrière tient-elle la charge ?** |
| « C'est un SaaS » | Un service en ligne | **Que peut-il atteindre chez nous ?** |
| « L'API est down » | Un service ne répond plus | Le vôtre, ou celui d'un tiers ? La réponse change tout |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Faire évoluer chaque service indépendamment | **Le réseau devient un composant du système** |
| Mettre à l'échelle par service | Des délais, des réessais, une cohérence à concevoir |
| Ne plus exploiter de serveur | **Une dépendance totale à une plateforme** |
| Consommer un service prêt à l'emploi | **Aucune action possible sur son infrastructure** — tout se joue en configuration |

---

> ### 🎓 À ce stade des Parties VI et VII, vous savez…
>
> ✓ appliquer **sept passes dans un ordre non négociable**, et produire une lecture d'une page qui se termine par **trois questions, pas un jugement** ;
> ✓ lire quatre architectures de complexité croissante, et **reconnaître une strate ancienne à trois signes convergents** ;
> ✓ que le prestataire d'infogérance est **au cœur de la zone d'administration** alors qu'il est dessiné en nuage à côté du pare-feu ;
> ✓ que la frontière de responsabilité cloud **descend par composant, pas uniformément** — et que la gouvernance des données et des accès reste vôtre, même quand leur mise en œuvre est partagée ;
> ✓ qu'une **ressource cloud sans sauvegarde configurée n'a aucune sauvegarde** ;
> ✓ que le point de fragilité le plus souvent négligé d'une architecture hybride est le lien des **identités**, et qu'il produit les pannes les plus incompréhensibles ;
> ✓ lire un cluster par ses **quatre éléments** — entrée, services, état, plan de contrôle — et non par ses instances ;
> ✓ qu'un schéma de microservices ne se lit pas en entier : **on suit un chemin, pas une carte** ;
> ✓ que sur un service en ligne, **les cinq actions ne s'appliquent pas à son infrastructure** et se déplacent vers la configuration, les identités et les données ;
> ✓ que la **communication asynchrone découple les disponibilités** — et qu'elle produit en échange accumulation silencieuse, doublons, désordre et perte du lien de cause à effet ;
> ✓ distinguer **bloc, fichier et objet**, et surtout **réplication, instantané et sauvegarde** — les trois qu'on confond constamment.
>
> **Ce que vous ne savez pas encore** : où l'on peut agir sur tout cela. C'est l'objet de la Partie VIII, et c'est le raccordement à toute la collection.

---

## PARTIE VIII — La vue cybersécurité

> **Le raccordement à toute la collection.** Les mêmes schémas, la quatrième question : **où peut-on agir ?**
>
> Cette partie n'enseigne aucune technique de sécurité. Elle enseigne où une technique peut être appliquée — et surtout **où elle ne peut pas l'être**, parce que des décisions prises avant vous l'ont rendu impossible.

---

### Chapitre 43 — Où peut-on agir ?

#### 43.1 Les cinq actions

Toute la sécurité opérationnelle se ramène à cinq actions applicables à un point d'une architecture.

🖼 **SCHÉMA 43.1 — Les cinq actions**

```
   OBSERVER      voir ce qui passe, sans l'empêcher
   FILTRER       empêcher ce qui ne doit pas passer
   AUTHENTIFIER  exiger une preuve d'identité avant de laisser passer
   SEGMENTER     empêcher deux choses de se joindre
   JOURNALISER   conserver la trace de ce qui s'est passé
```

**Deux propriétés qui structurent le chapitre** :

| Propriété | Conséquence |
|---|---|
| **Chaque action exige un point d'observation ou de décision** | Ce qui ne traverse aucun composant capable d'observer, de décider ou de tracer échappe à toute action |
| **Chaque action a un coût** | *Principe du coût* : latence, exploitation, faux positifs, volume |

> **Corollaire** : les points où l'on peut agir sont les **points de passage réseau** et les **composants capables de produire un événement**. Cartographier les uns revient largement à cartographier les autres — §34.4.

📌 **Nuance importante** : tout ne passe pas par le réseau. **Une application produit un événement métier — « Marie a exporté 4 000 lignes » — sans qu'aucun intermédiaire ne le voie passer.** C'est même la seule source capable de le produire, §34.2. De même, un poste observe une activité locale que rien ne traverse.

> **Le modèle du point de passage vaut pour le réseau. Pour l'observation, la question est plus large : quel composant est en position de savoir ?**

#### 43.2 Où chaque action est possible

| Action | Points possibles | Où c'est **impossible** |
|---|---|---|
| **Observer** | Pare-feu · mandataires · commutateurs · postes · serveurs | Dans un flux chiffré non terminé · **chez un tiers** |
| **Filtrer** | Pare-feu · mandataires · segments | À l'intérieur d'un segment · **chez un tiers** |
| **Authentifier** | Mandataire inverse · applicatif · annuaire · accès distant | Entre deux serveurs qui se font confiance par adresse |
| **Segmenter** | Entre zones · entre segments · au niveau du poste | **Entre machines d'un même segment**, sans mesure explicite |
| **Journaliser** | Tout composant qui traverse un flux | Ce qui ne traverse aucun composant journalisant |

⚠️ **La colonne de droite est la plus utile du chapitre.** Elle dit ce qu'aucun produit ne résoudra, parce que l'architecture ne le permet pas. Trois cas reviennent :

**① À l'intérieur d'un segment.** Sans mécanisme dédié — pare-feu local, isolation de ports, microsegmentation — six cents postes d'un même segment se joignent librement, et aucun pare-feu périmétrique n'y change rien. §24.1.

**② Dans un flux chiffré non terminé.** Un flux chiffré de bout en bout ne s'observe pas en chemin. Pour le voir, il faut le terminer — c'est ce que fait un mandataire inverse en modes B et C, §12.3.

**③ Chez un tiers.** Sur un service en ligne, **les cinq actions ne sont pas applicables à son infrastructure**. Elles se déplacent vers ce que vous maîtrisez encore : configuration, identités, données, journaux exposés — §42.5.

#### 43.3 Les points de passage d'une architecture type

Reprenons le schéma 1.1 et marquons ce qui est possible où.

```
                        INTERNET
                            │
   ┌────────────────────────┼─────────────────────────────────┐
   │  [ pare-feu ]          │   OBS ✓  FILT ✓  AUTH ✗  SEG ✓  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ mandataire ]        │   OBS ✓✓ FILT ✓  AUTH ✓✓ SEG ✗  JOURN ✓✓
   │       ↑ le point le plus riche : il voit le contenu en clair
   │         MAIS uniquement pour les accès EXTERNES — §29.3
   ├────────────────────────┼─────────────────────────────────┤
   │  [ répartiteur ]       │   OBS ✓  FILT ~  AUTH ✗  SEG ✗  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ web ×3 ]            │   OBS ✓  FILT ✗  AUTH ~  SEG ✗  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ applicatif ]        │   OBS ✓  FILT ✗  AUTH ✓✓ SEG ✗  JOURN ✓✓
   │       ↑ le seul point qui connaisse l'UTILISATEUR
   │         et l'ACTION MÉTIER — §34.2
   ├────────────────────────┼─────────────────────────────────┤
   │  [ base ]              │   OBS ✓  FILT ✗  AUTH ~  SEG ✗  JOURN ✓
   │       ↑ voit les requêtes, PAS l'utilisateur final
   └────────────────────────┴─────────────────────────────────┘
```

👁 **CE QU'IL FALLAIT OBSERVER**

**Deux points concentrent la valeur, et ce ne sont pas les mêmes.**

Le **mandataire inverse** est le point le plus riche techniquement : il voit tout le trafic externe en clair, il peut filtrer, authentifier et journaliser. **Et il ne voit que les accès externes** — §29.3.

L'**applicatif** est le seul point qui connaisse simultanément **l'utilisateur réel et l'action métier**. Un journal d'applicatif dit *« Marie a exporté 4 000 lignes »* ; un journal de pare-feu dit *« une adresse a ouvert une connexion »*. **C'est la différence entre une trace exploitable et une trace technique.**

⚠️ **Aucun de ces deux points n'est celui où l'on met le plus de moyens en pratique** — les moyens vont majoritairement au périmètre, qui voit le moins.

#### 43.4 Ce qui rend une action impossible, par cause

**Quatre causes, et elles n'appellent pas les mêmes réponses** :

| Cause | Exemple | Que faire |
|---|---|---|
| **Architecturale** | Pas de point de passage entre deux machines d'un segment | **Changer l'architecture**, ou déclarer non couvert |
| **Technique** | Le composant ne sait pas produire de journal | Observer ailleurs sur le chemin |
| **Contractuelle** | Un service en ligne ne donne pas accès à ses journaux | Négocier, ou accepter et déclarer |
| **Organisationnelle** | Le composant est administré par une autre équipe | **La plus fréquente, et la seule qui se résolve sans budget** |

⚠️ **La quatrième mérite d'être nommée** : beaucoup d'angles morts ne sont ni techniques ni budgétaires. **Ils existent parce que personne n'a demandé.** C'est le cas des journaux d'un équipement réseau, d'un progiciel métier, ou d'un service géré par une filiale.

#### 43.5 Le coût de chaque action

⚖️ **CONTRAINTE ET COÛT**

| Action | Coût principal | Ce qui la fait abandonner |
|---|---|---|
| **Observer** | Volume, stockage, exploitation | **Personne ne regarde ce qui est collecté** |
| **Filtrer** | Faux blocages, règles à maintenir | Une règle trop stricte casse un usage légitime |
| **Authentifier** | Latence, dépendance à l'annuaire, friction | **Les utilisateurs contournent** — §24.2 |
| **Segmenter** | Flux à ouvrir, dépannage difficile | Le processus d'ouverture devient trop lent |
| **Journaliser** | Volume, rétention, coût de stockage | **La rétention est réduite pour tenir le budget** — §34.3 |

⚠️ **La dernière ligne est celle qui coûte le plus cher en incident.** La rétention est le premier poste réduit quand le budget serre, et c'est exactement ce qui empêche d'enquêter plus tard.

🔥 **SCÉNARIO — le contrôle existe, il ne voit rien**

| Question | Réponse |
|---|---|
| Symptôme | Une compromission interne s'est déroulée pendant onze jours. **Aucune alerte** |
| Hypothèse naïve | « Le dispositif de détection a échoué » |
| Dépendance réelle | **Il était placé au périmètre.** L'activité était entièrement interne — §44.4 |
| Ce que le schéma aurait dû montrer | Les points de passage internes, et ce qu'ils observent |
| Concevoir différemment | **Segmenter d'abord** : sans point de passage, il n'y a rien à observer |

⚠️ **Ce scénario ferme la boucle du cours** : **segmenter n'est pas seulement une mesure de protection, c'est une condition de détection** — §45.3. Dans une architecture plate, un mouvement latéral ne traverse aucun point observable : **il est invisible par construction**.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a de la visibilité » | Des sondes ou des agents existent | **Sur quel périmètre ? Combien de flux y passent ?** |
| « Tout est loggé » | Beaucoup de sources sont collectées | **Combien de temps ? Et l'identité est-elle préservée ?** |
| « On a mis un WAF » | Un filtrage applicatif en frontal | **Il ne voit que les accès externes** — §29.3 |
| « Ce n'est pas possible techniquement » | Une action est écartée | **Architecturale, technique, contractuelle ou organisationnelle ?** — §43.4 |

---

### Chapitre 44 — Placer les dispositifs

#### 44.1 Le principe

> **Le bon emplacement d'un dispositif dépend de l'architecture, pas du produit.**

Un même produit placé à deux endroits différents ne voit pas la même chose, ne protège pas les mêmes actifs, et ne produit pas les mêmes traces.

#### 44.2 Les emplacements, par dispositif

| Dispositif | Emplacement pertinent | Ce qu'il voit | Ce qu'il **ne voit pas** |
|---|---|---|---|
| **Pare-feu** | Entre deux zones | Ce qui traverse la frontière | **Ce qui reste dans une zone** |
| **Détection sur poste** | Sur chaque poste et serveur | L'activité locale, les processus | Ce qui se passe sur ce qui n'en porte pas |
| **Sonde réseau** | Sur un point de passage, en dérivation | Les flux qui y transitent | **Les flux chiffrés · ceux qui ne passent pas là** |
| **Scanner de vulnérabilités** | Au plus près des cibles | Ce qu'il peut joindre | **Ce qui est derrière un filtre, ou éteint** |
| **Collecte de journaux** | Centralisée, alimentée par tous | Ce que les sources envoient | **Ce qui n'est pas configuré pour émettre** |
| **Point d'authentification** | Mandataire, applicatif, ou les deux | Les accès qui y passent | **Les accès internes directs** — §29.3 |

⚠️ **La colonne de droite définit la couverture réelle.** Un dispositif ne protège que ce qu'il voit, et un schéma dit exactement ce qu'il voit.

#### 44.3 Le même dispositif, trois emplacements — l'exemple de la sonde

**C'est l'exercice qui installe le principe.**

```
  A — SONDE AU PÉRIMÈTRE
      Internet ──►[SONDE]──► [ FW ] ──► DMZ ──► interne
      VOIT     : ce qui entre et sort
      NE VOIT PAS : tout le trafic interne — postes vers serveurs
      COUVERTURE RÉELLE : faible en volume, forte en visibilité externe

  B — SONDE ENTRE POSTES ET SERVEURS
      [ postes ] ──►[SONDE]──► [ serveurs ]
      VOIT     : le mouvement latéral, la reconnaissance, la collecte
      NE VOIT PAS : ce qui reste entre postes
      COUVERTURE RÉELLE : la phase la plus longue d'une compromission

  C — SONDE DEVANT LA BASE
      [ applicatif ] ──►[SONDE]──► [ base ]
      VOIT     : les requêtes vers les données
      NE VOIT PAS : qui les a demandées — §34.2
      COUVERTURE RÉELLE : étroite, mais sur l'actif le plus sensible
```

| Emplacement | Volume de trafic observé | Phase d'attaque couverte |
|---|---|---|
| **A — périmètre** | Faible | Accès initial |
| **B — postes/serveurs** | **Élevé** | **Reconnaissance, mouvement latéral, collecte** |
| **C — devant la base** | Faible | Exfiltration |

⚠️ **Le placement A est un réflexe courant, et c'est celui qui observe le plus petit volume de trafic.** Le placement B couvre la phase la plus longue d'une compromission — celle qui dure des jours ou des semaines. **Et il exige un point de passage, donc une segmentation** : c'est le §45.3.

#### 44.4 Les quatre emplacements impossibles, et ce qu'on fait alors

| Situation | Pourquoi c'est impossible | Ce qu'on fait |
|---|---|---|
| **Un agent sur un automate industriel** | Constructeur ne le supporte pas, ressources insuffisantes, garantie perdue | Observation passive du réseau · segmentation stricte · §28.6 |
| **Un scanner authentifié sur un système hérité** | Pas de compte disponible, risque d'indisponibilité | Inventaire déclaratif · scan passif · **périmètre déclaré non couvert** |
| **Une sonde sur un flux chiffré de bout en bout** | Rien à voir sans le terminer | Journalisation aux extrémités · métadonnées uniquement |
| **Un contrôle sur un service en ligne** | Ce n'est pas chez vous | Configuration du service · **journaux du fournisseur, s'il en donne** |

**Le point commun des quatre réponses** : quand une action est impossible à un endroit, **on la déplace, on la remplace, ou on déclare la zone non couverte**. On ne fait jamais semblant.

⚠️ **C'est exactement la doctrine des périmètres déclarés non couverts du volume Maintien en condition de sécurité.** Une zone où l'on ne peut pas agir est acceptable **si elle est déclarée** ; elle est dangereuse quand elle est ignorée.

#### 44.5 L'erreur de placement la plus coûteuse

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez une sonde réseau sur le lien Internet pour détecter les intrusions. Quelle proportion de l'activité de votre organisation voyez-vous ?*
**Une fraction — et pas celle que vous croyez.** Vous voyez ce qui entre et sort. Vous ne voyez **rien** de ce qui se passe entre les six cents postes et les serveurs internes, c'est-à-dire là où se déroule l'essentiel d'une compromission après l'accès initial. La mauvaise décision évitée : **placer les moyens au périmètre en croyant couvrir l'organisation**, et découvrir en incident que les onze jours d'activité interne n'ont laissé aucune trace exploitable.

🔥 **SCÉNARIO — le scanner ne voit pas ce qu'il devrait voir**

| Question | Réponse |
|---|---|
| Symptôme | Un scan hebdomadaire remonte 40 machines. L'inventaire en compte 214 |
| Hypothèse naïve | « Le scanner est mal configuré » |
| Dépendance réelle | **Il est placé dans un segment, et le filtrage inter-segments le bloque** |
| Ce que le schéma aurait dû montrer | Depuis où le scanner opère, et ce qu'il peut joindre |
| Concevoir différemment | Un point de scan par zone · ou des règles dédiées, **et alors le scanner devient un chemin privilégié à protéger** |

⚠️ **La dernière ligne est un compromis qu'on oublie** : donner au scanner le droit de joindre tout le parc en fait **une cible de choix**. Un scanner compromis dispose d'un accès réseau que personne d'autre n'a. **Principe du coût.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est couverts à 95 % » | Un agent est déployé sur 95 % des machines | **Et les 5 % restants ? Ce sont souvent les plus anciennes** |
| « La sonde ne voit rien » | Peu d'alertes | **Est-elle bien placée ?** Peu d'alertes peut vouloir dire peu de trafic observé |
| « Le scan est passé » | Un balayage a eu lieu | **Combien de machines a-t-il vues, sur combien d'attendues ?** |
| « On mettra un agent plus tard » | Un périmètre non couvert | **Est-ce déclaré quelque part, ou oublié ?** |

---

### Chapitre 45 — Ce que l'architecture impose au reste

> Le chapitre de raccordement. Il explique pourquoi les autres volumes de la collection demandent d'assumer certains compromis : **ils sont déterminés ici**.

#### 45.1 Ce que l'architecture impose au maintien en condition de sécurité

| Ce que l'architecture détermine | Conséquence sur le maintien |
|---|---|
| **L'interruptibilité** | Un composant qui ne peut pas s'arrêter ne sera pas corrigé — quelle que soit la politique |
| **La redondance** | Sans elle, toute correction impose une interruption |
| **Le nombre de composants uniques** | Chaque point de rupture est une fenêtre de maintenance négociée |
| **Les dépendances** | Corriger un composant peut arrêter un service qu'on ne soupçonnait pas |
| **Le cycle de vie du plus ancien composant** | Il fixe le plancher de modernisation de tout ce qui en dépend |

> **La formulation qui résume** : *aucune politique de correctifs ne rattrape une architecture non interruptible.*

**C'est le principe 7 du volume Maintien en condition de sécurité** — *le coût du maintien se décide en conception, pas en exploitation* — et ce chapitre en donne la démonstration architecturale.

🔥 **SCÉNARIO — le correctif ne sera jamais appliqué**

| Question | Réponse |
|---|---|
| Symptôme | Une vulnérabilité critique reste ouverte depuis quatorze mois |
| Hypothèse naïve | « L'équipe ne fait pas son travail » |
| Dépendance réelle | **Le composant est unique, et son arrêt stoppe une chaîne de production** |
| Ce que le schéma aurait dû montrer | Qu'aucune redondance n'existe sur ce composant |
| Concevoir différemment | **La décision qui a produit cette situation date de la conception**, pas de l'exploitation |

#### 45.2 Ce que l'architecture impose à l'inventaire

| Ce que l'architecture détermine | Conséquence sur l'inventaire |
|---|---|
| **Ce qui est découvrable** | Un actif sur un segment non balayé n'apparaîtra pas |
| **Ce qui a une adresse stable** | Un actif éphémère échappe aux méthodes classiques — §41.4 |
| **Ce qui appartient à un tiers** | Ne se découvre pas : **se déclare** |
| **Ce qui est derrière un filtre** | Invisible au scanner, existant quand même — §44.5 |
| **Le nombre de zones** | Chaque zone est une campagne de découverte distincte |

**Les cinq lignes annoncent le chapitre 11 du volume Asset Management**, et elles expliquent pourquoi cinq zones sont restées non couvertes chez HELIOMED en février 2026 : **ce n'était pas un défaut de méthode, c'était une conséquence de l'architecture.**

#### 45.3 Ce que l'architecture impose à la détection

| Ce que l'architecture détermine | Conséquence sur la détection |
|---|---|
| **Les points de passage** | Ce sont les seuls endroits où l'on peut observer — §43.1 |
| **Le chiffrement de bout en bout** | Rend la sonde réseau inopérante sur le contenu |
| **La position du mandataire** | Détermine si l'identité réelle est visible en aval — §34.2 |
| **La segmentation** | Détermine si un mouvement latéral traverse un point observable |
| **Les composants sans agent** | Créent des angles morts structurels |

⚠️ **La quatrième ligne est celle qui décide de tout.** Dans une architecture plate, un mouvement latéral ne traverse **aucun** point observable : il est invisible par construction. **Segmenter n'est donc pas seulement une mesure de protection, c'est une condition de détection.**

#### 45.4 Ce que l'architecture impose à la réponse à incident

| Ce que l'architecture détermine | Conséquence sur la réponse |
|---|---|
| **Les dépendances** | Ce qu'on peut isoler sans arrêter un service |
| **La segmentation** | Si l'isolement est possible du tout |
| **Les chemins d'administration** | Si l'on peut encore administrer un système compromis — §27.4 |
| **Les sauvegardes et leur chemin** | Si la restauration est possible depuis un environnement sain |
| **La journalisation et sa rétention** | **Si l'on peut savoir ce qui s'est passé** — §34.3 |

⚠️ **La troisième ligne est celle qu'on découvre en crise.** Si le chemin d'administration passe par le réseau compromis, on ne peut plus administrer sans risquer d'exposer des identifiants privilégiés. **C'est une décision d'architecture prise des années plus tôt qui détermine ce qu'on peut faire un dimanche soir.**

🔥 **SCÉNARIO — on ne peut isoler que tout ou rien**

| Question | Réponse |
|---|---|
| Symptôme | Compromission confirmée sur un serveur. **Aucun confinement partiel possible** |
| Hypothèse naïve | « Il faut couper le réseau » |
| Dépendance réelle | **Une seule zone** : isoler ce serveur suppose de savoir ce qui en dépend, et rien ne le dit |
| Ce que le schéma aurait dû montrer | L'arbre de dépendance du service — §35.2 |
| Ce que cela coûte | **On coupe tout, ou on ne coupe rien.** Les deux options sont mauvaises |

#### 45.5 Le tableau de synthèse

**Ce que le lecteur doit emporter du chapitre** :

| Une décision d'architecture… | …détermine des années plus tard |
|---|---|
| Redonder ou non | **Si un correctif pourra être appliqué** |
| Segmenter ou non | **Si une compromission sera visible** |
| Isoler l'administration ou non | **Si l'on pourra intervenir pendant un incident** |
| Journaliser et conserver ou non | **Si l'on pourra savoir ce qui s'est passé** |
| Documenter les dépendances ou non | **Si l'on pourra confiner sans tout casser** |

> **Aucune de ces cinq lignes ne se rattrape par un produit, un budget ou une procédure.** Elles sont déterminées à la conception, et c'est pourquoi ce volume est le premier de la collection.

#### 45.6 🔬 Mini-lab 10 — Placer les cinq actions

**Objectif** — Décider où placer chaque action sur une architecture donnée, et déclarer les zones non couvrables.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 43 à 45

**L'architecture** : celle du mini-lab 7 — cinq zones, aucune frontière entre DMZ et interne, un annuaire dans le segment des 400 postes, une supervision industrielle joignable depuis les postes.

**Le budget** : trois actions seulement peuvent être financées cette année.

❓ Lesquelles, où, et que déclarez-vous non couvert ?

---

**Corrigé**

**Les trois actions retenues, et leur justification**

| # | Action | Emplacement | Pourquoi celle-ci |
|---|---|---|---|
| **1** | **Segmenter** | Entre les 400 postes et le segment industriel | **Un poste compromis atteint aujourd'hui la supervision sans traverser aucun filtre.** C'est le chemin le plus court vers le risque le plus grave — atteinte à la sûreté, §28.1 |
| **2** | **Segmenter** | Frontière 2, entre DMZ et interne | Sans elle, la DMZ n'en est pas une. Un composant exposé compromis atteint tout — §25.1 |
| **3** | **Journaliser** | Applicatif et annuaire | Les deux seuls points qui connaissent **l'utilisateur réel et l'action** — §43.3 |

**Pourquoi pas les autres**

| Écartée | Motif |
|---|---|
| Sonde réseau au périmètre | Voit ce qui entre, pas les 400 postes — §44.4 |
| Détection sur poste | Souhaitable, mais ne corrige pas les deux brèches structurelles |
| Authentification renforcée | Pertinente, et sans effet tant que la segmentation manque |

**Ce qu'on déclare non couvert**

> *Les échanges à l'intérieur du segment des 400 postes ne sont ni observés, ni filtrés. Une compromission d'un poste atteint les 399 autres sans traverser aucun point de contrôle. Cette situation est connue, non traitée cette année faute de moyens, et réexaminée au budget suivant.*

**Les trois erreurs attendues**

1. **Choisir la sonde réseau au périmètre.** C'est le réflexe, et c'est l'erreur du §44.4 — elle voit le moins de l'activité réelle.
2. **Choisir l'authentification renforcée en premier.** Elle est utile, et elle ne change rien tant qu'un poste compromis atteint la supervision industrielle par un chemin direct.
3. **Ne rien déclarer non couvert.** Trois actions ne couvrent pas tout. **Ce qui n'est pas traité doit être écrit** — sinon c'est un angle mort, pas un arbitrage.

---

> ### 🎓 À ce stade de la Partie VIII, vous savez…
>
> ✓ que toute la sécurité opérationnelle se ramène à **cinq actions**, et que chacune exige un **point d'observation ou de décision** ;
> ✓ que les points où l'on peut agir sont **exactement les points de passage** de l'architecture ;
> ✓ **où chaque action est impossible** — à l'intérieur d'un segment, dans un flux chiffré non terminé, chez un tiers ;
> ✓ que le **mandataire inverse** est le point le plus riche techniquement, et qu'il **ne voit que les accès externes** ;
> ✓ que l'**applicatif** est le seul point qui connaisse l'utilisateur réel et l'action métier — et qu'il reçoit rarement les moyens ;
> ✓ que le **bon emplacement dépend de l'architecture, pas du produit** ;
> ✓ que face à un emplacement impossible, on **déplace, on remplace, ou on déclare non couvert** — jamais on ne fait semblant ;
> ✓ que **segmenter est une condition de détection**, pas seulement une mesure de protection ;
> ✓ qu'une décision d'architecture prise il y a des années détermine **ce que vous pourrez faire un dimanche soir**.
>
> **Ce que vous ne savez pas encore** : comment proposer vous-même une architecture, et comment critiquer celle des autres. C'est l'objet de la Partie IX.

---

## PARTIE IX — Concevoir

> **Le miroir de la lecture.** Quarante-cinq chapitres ont appris à reconstituer les arbitrages d'autrui ; cinq apprennent à énoncer les siens.
>
> ⚠️ **Cette partie ne rend pas architecte.** Elle apprend à proposer une architecture justifiée pour un besoin courant, à énoncer ses compromis, et à identifier ce qu'il reste à vérifier. C'est le §7.3, et il faut le relire avant d'aborder ces chapitres.

---

### Chapitre 46 — Les quatre questions du concepteur

#### 46.1 La symétrie

🖼 **SCHÉMA 46.1 — Lire et concevoir**

```
   LIRE                              CONCEVOIR
   ─────────────────────             ──────────────────────────
   ① Qu'est-ce qui circule ?    ⟷    ① Que doit-on servir, à qui ?
   ② Par où ?                   ⟷    ② Quelles contraintes s'imposent ?
   ③ Qu'est-ce qui tombe        ⟷    ③ Qu'accepte-t-on de perdre ?
     si ça tombe ?
   ④ Où peut-on agir ?          ⟷    ④ Quels compromis assume-t-on,
                                        et les a-t-on écrits ?
```

**La symétrie n'est pas décorative** : chaque question de conception se vérifie par la question de lecture correspondante. Une architecture qu'on ne saurait pas lire est une architecture mal conçue.

#### 46.2 ① Que doit-on servir, à qui ?

**La question qu'on saute**, et dont l'absence produit les architectures les plus coûteuses.

| Sous-question | Pourquoi elle compte |
|---|---|
| **Quel service métier ?** | Formulé du point de vue de l'utilisateur, pas de la technique — §35.1 |
| **Combien d'utilisateurs, où ?** | 40 sur un site et 4 000 sur trois continents ne produisent pas la même architecture |
| **Quels usages, à quels moments ?** | Charge continue ou pics · heures ouvrées ou permanent |
| **Quelles données, de quelle sensibilité ?** | **Principe 6** — c'est la donnée qui commande |
| **Qui exploitera ?** | Une personne à mi-temps ou une équipe de vingt |

⚠️ **La dernière est la plus négligée et la plus déterminante.** Une architecture qui exige davantage de compétences que l'organisation n'en possède **échouera**, quelle que soit sa qualité technique. C'est le facteur qui explique le plus d'échecs de modernisation.

#### 46.3 ② Quelles contraintes s'imposent ?

Les six contraintes du §1.4, appliquées au cas.

##### Le vocabulaire professionnel : les exigences non fonctionnelles

Les six contraintes du §1.4 portent un nom dans le métier : ce sont des **exigences non fonctionnelles**. Elles ne décrivent pas *ce que le système fait* — c'est le rôle des exigences fonctionnelles — mais **sous quelles conditions il doit le faire**.

| Exigence | La question qu'elle pose | Ce qui la chiffre |
|---|---|---|
| **Disponibilité** | Combien de temps peut-il être arrêté ? | **Durée d'interruption tolérable** |
| **Reprise** | Combien de données peut-on perdre ? | **Perte de données tolérable** |
| **Performance** | Combien de temps pour répondre ? | Temps de réponse, volume, concurrence |
| **Capacité** | Jusqu'où peut-il croître ? | Nombre d'utilisateurs, volume de données |
| **Sécurité** | Que doit-on protéger, et contre quoi ? | Sensibilité, exposition, obligations |
| **Maintenabilité** | Comment le fait-on évoluer ? | Fréquence des changements, interruptibilité |
| **Exploitabilité** | **Qui le tiendra au quotidien ?** | **Nombre d'exploitants disponibles** |

##### Les trois durées, et pourquoi il ne faut pas les confondre

**Le lecteur entendra deux acronymes en réunion. Ils ne désignent pas la même chose que la tolérance métier, et la confusion est très fréquente.**

| Notion | La question qu'elle pose | Qui la fixe |
|---|---|---|
| **Tolérance métier maximale** | *« Combien de temps puis-je supporter l'arrêt avant que cela devienne inacceptable ? »* | **Le métier**, et lui seul |
| **RTO** — objectif de délai de reprise | *« Sous combien de temps visons-nous effectivement la restauration ? »* | **Un engagement**, pris au regard des moyens |
| **RPO** — objectif de perte de données | *« Quelle quantité de données, exprimée en temps, acceptons-nous de perdre ? »* | Le métier, avec le coût comme contrainte |

⚠️ **La distinction entre les deux premières est celle qu'on manque presque toujours.** Elles peuvent être différentes, et elles le sont souvent :

```
   Tolérance métier   « quatre heures d'arrêt sont supportables »
   RTO visé           « nous nous engageons sur deux heures »
                      → une marge, choisie délibérément
   RTO réel MESURÉ    « la dernière restauration a pris six heures »
                      → ⚠️ l'écart entre l'engagement et le réel
```

> **Le RTO est un objectif, pas une propriété du système.** Un RTO de deux heures affiché sur une architecture dont la restauration n'a jamais été chronométrée est **une intention**, pas un engagement tenable — *principe de preuve*.

**Le RPO se traduit directement en décision d'architecture** :

| RPO exigé | Ce qu'il impose |
|---|---|
| 24 heures | Une sauvegarde quotidienne suffit |
| 8 heures | Trois sauvegardes par jour — §48.1 |
| 15 minutes | **Une réplication**, et probablement asynchrone |
| Zéro perte | **Une réplication synchrone** — coûteuse, et elle ralentit les écritures |

⚠️ **La dernière ligne est celle qui surprend** : exiger zéro perte de données **dégrade la performance**, parce que chaque écriture doit être confirmée des deux côtés avant d'être validée. **C'est un arbitrage, pas un idéal gratuit** — *principe du coût*.

⚠️ **Les deux premières exigences du tableau ci-dessus se chiffrent en durée, et ce sont elles qui déterminent l'essentiel d'une architecture.** *« Il faut que ce soit fiable »* n'est pas une exigence ; *« une interruption de quatre heures en journée est tolérable, une perte de plus de quinze minutes de données ne l'est pas »* en est une — et elle décide à elle seule de la présence ou non d'une redondance.

⚠️ **La dernière est celle que personne n'écrit**, et le §47.3 montre qu'elle fait échouer davantage d'architectures que toutes les autres réunies.

🧪 **EN PRATIQUE — la fiche de contraintes**

```
DISPONIBILITÉ   Interruption tolérable : ......  Perte de données tolérable : ......
PERFORMANCE     Temps de réponse attendu : ......  Volume : ......
COÛT            Budget d'investissement : ......  Budget récurrent : ......
SÉCURITÉ        Sensibilité des données : ......  Exposition nécessaire : ......
CONFORMITÉ      Obligations applicables : ......  Preuve à produire : ......
HISTOIRE        Existant à intégrer : ......  Ce qu'on ne peut pas changer : ......
```

**Les deux premières lignes sont celles qui se chiffrent, et qu'on ne chiffre jamais.** *« Il faut que ce soit disponible »* n'est pas une contrainte ; *« une interruption de quatre heures en journée est tolérable, une perte de données de plus de quinze minutes ne l'est pas »* en est une — et elle détermine à elle seule la moitié de l'architecture.

#### 46.4 ③ Qu'accepte-t-on de perdre ?

> **Principe 7 : concevoir, c'est choisir ce qu'on accepte de perdre.**

**Parce que les six contraintes se contredisent, il faut en dégrader certaines.** La question n'est pas *lesquelles satisfaire* mais **lesquelles sacrifier, et de combien**.

| Ce qu'on peut accepter de perdre | Ce que ça permet |
|---|---|
| De la disponibilité | Une architecture simple, peu coûteuse, exploitable par une personne |
| De la performance | Des contrôles supplémentaires, du chiffrement, de la journalisation |
| Du budget | De la redondance, de la segmentation, des compétences |
| De la simplicité | De la sécurité et de la disponibilité |
| **De la fonctionnalité** | La ligne qu'on n'envisage jamais, et qui règle beaucoup de problèmes |

⚠️ **La dernière ligne mérite un développement.** Beaucoup de complexité d'architecture vient de fonctionnalités marginales : un accès depuis l'extérieur pour trois personnes, un export en temps réel utilisé une fois par mois, une compatibilité avec un système que deux clients utilisent encore. **Renoncer à une fonctionnalité est souvent l'arbitrage le moins cher, et le moins proposé.**

#### 46.5 ④ Quels compromis assume-t-on, et les a-t-on écrits ?

**La différence entre un compromis assumé et un compromis subi** est qu'il est écrit.

🧪 **EN PRATIQUE — le registre des compromis**

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | Revoir si |
|---|---|---|---|---|---|---|
| 1 | Un seul serveur applicatif | Coût | Disponibilité | Interruption de 4 h possible | *(nom)* | Le coût de licence change |
| 2 | Pas de zone démilitarisée | Simplicité | Sécurité | Publication directe, aucun service publié aujourd'hui | *(nom)* | Un service devient public |

**Ce document est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**, et c'est lui qui permettra, dans dix ans, de répondre à la question du chapitre 4 : *pourquoi c'est comme ça ?*

> **Une architecture livrée sans registre de compromis condamne ses successeurs à les redécouvrir — ou à les juger naïvement.**

---

### Chapitre 47 — Concevoir sous contrainte

#### 47.1 Les arbitrages classiques, et ce qu'ils coûtent

| Arbitrage | Ce qu'on gagne | Ce qu'on perd | Quand il est juste |
|---|---|---|---|
| **Redonder ou non** | Continuité | Coût ×2, complexité, un composant de plus à exploiter | Quand l'interruption tolérable est inférieure au délai de remise en service |
| **Segmenter finement ou non** | Limitation de la propagation | Flux à maintenir, dépannage plus long | Quand les conséquences d'une propagation sont graves |
| **Centraliser ou distribuer** | Simplicité, économies | Dépendance au lien, latence | Quand le lien est fiable et la latence acceptable |
| **Internaliser ou externaliser** | Maîtrise, ou compétences | Compétences à tenir, ou dépendance | Selon ce que l'organisation sait exploiter |
| **Chiffrer partout ou aux frontières** | Confidentialité | Visibilité perdue, complexité de gestion des clés | Selon la sensibilité et la capacité de détection |
| **Authentifier une fois ou à chaque étape** | Confort, ou cloisonnement | Un jeton unique qui ouvre tout, ou de la friction | Selon la sensibilité des étapes |

#### 47.2 L'architecture qui optimise tout n'existe pas

⚠️ **Le réflexe du débutant en conception** : produire une architecture qui coche toutes les cases. Elle est redondée, segmentée, chiffrée, journalisée, authentifiée à chaque étape.

**Ce qui se passe ensuite**, dans l'ordre :

```
Mois 1    L'architecture est validée. Elle est excellente sur le papier.
Mois 6    Le déploiement prend du retard : trop de composants à intégrer.
Mois 12   L'exploitation ne suit pas — deux personnes pour quinze composants.
Mois 18   Des contournements apparaissent pour tenir les délais.
Mois 24   La segmentation est partiellement désactivée « en attendant ».
Mois 36   L'architecture réelle ressemble à celle qu'on voulait éviter,
          avec le coût de celle qu'on a conçue.
```

> **Une architecture qu'une organisation ne sait pas exploiter se dégrade jusqu'à son niveau réel de compétence — en ayant coûté le prix de l'ambition.**

**Ce que ce principe explique, et qui vaut d'être énoncé explicitement** :

| Affirmation courante | Ce que le principe y oppose |
|---|---|
| « L'orchestration de conteneurs est plus moderne » | Elle introduit un système distribué complet à exploiter. **Plus moderne n'est pas plus adapté** |
| « Les microservices sont un signe de maturité » | Ils multiplient les composants et les flux. **La maturité est de savoir les exploiter** |
| « Plusieurs fournisseurs cloud, c'est plus résilient » | C'est deux plateformes à maîtriser au lieu d'une |
| « Plus de segmentation, c'est plus sûr » | Jusqu'au point où les flux deviennent ingérables et sont contournés — §24.2 |
| « Nous avons de la haute disponibilité » | **Une redondance non testée est une croyance** — *principe de preuve* |

> **Formulation générale, à rapprocher du principe du coût** : *un composant techniquement excellent que personne ne sait exploiter dégrade l'architecture au lieu de l'améliorer.*

**Le test à s'appliquer** : *combien de personnes faudra-t-il pour tenir cette architecture, et les avons-nous ?*

#### 47.3 Concevoir pour ce qu'on sait exploiter

| Signe qu'une architecture est trop ambitieuse | Ce qu'on fait |
|---|---|
| Elle exige une compétence que personne n'a | La simplifier, ou acquérir la compétence **avant** |
| Elle comporte plus de composants que d'exploitants | Réduire, ou externaliser une partie |
| Elle suppose des procédures qui n'existent pas | Les écrire, ou choisir un modèle qui s'en passe |
| **Son basculement n'est testable que rarement** | Choisir un modèle testable — §20 |

**La quatrième ligne est celle qu'on découvre le plus tard.** Une redondance qui ne peut être testée qu'une fois par an, pendant une fenêtre difficile à obtenir, **ne sera pas testée** — et une redondance non testée est une croyance.

---

### Chapitre 48 — Quatre conceptions guidées

> **Le vrai exercice de synthèse du cours.** Chaque cas suit dix étapes — et l'étape ④ est celle qui manque partout ailleurs.

#### 48.0 Avertissement sur les chiffres de ce chapitre

⚠️ **Les valeurs employées dans les corrigés qui suivent — 0,3 personne, 0,6 personne, un coût multiplié par 2,5 — sont des données de scénario, pas des ratios universels.**

Elles servent à rendre un arbitrage lisible : *cette option consomme deux fois plus d'exploitation que celle-là*. **Elles ne se transposent pas.** La charge réelle d'exploitation d'un composant dépend de l'outillage, du niveau d'automatisation, des compétences en place, du nombre d'environnements et des engagements de service.

> **Ce qu'il faut retenir n'est pas le chiffre. C'est la démarche : chiffrer avant d'arbitrer, et confronter le total à la capacité réellement disponible.**

**Comment obtenir vos propres chiffres** : demandez à l'équipe d'exploitation combien de temps elle consacre par mois à un composant comparable déjà en service. C'est la seule source fiable, et elle est disponible en une conversation.

#### 48.1 Le déroulé en dix étapes

```
 ①  LE BESOIN            Quel service, pour qui, avec quelles données
 ②  LES CONTRAINTES      Chiffrées. Les non chiffrées se demandent
 ③  PREMIÈRE PROPOSITION La solution qui vient spontanément
 ④  CRITIQUE             On applique la grille du chapitre 49
                         A SA PROPRE proposition
 ⑤  SECONDE PROPOSITION  Ce que la critique fait changer
 ⑥  LES COMPROMIS        Le registre
 ⑦  LES FLUX             Une requête type, en douze étapes
 ⑧  LES RUPTURES         L'arbre de dépendance
 ⑨  L'EXPLOITATION       Qui tiendra cela, et le sait-on faire ?
 ⑩  CE QU'ON IGNORE      Ce qu'il reste à vérifier
```

⚠️ **Une remarque essentielle avant de commencer** :

> **Il n'existe pas *le* corrigé d'une architecture.** Chaque cas ci-dessous admet **plusieurs réponses défendables**. Ce qui distingue une bonne réponse d'une mauvaise n'est pas le schéma produit — c'est **la qualité de l'arbitrage énoncé et la lucidité sur ce qui reste à vérifier**.
>
> Si votre proposition diffère de celle présentée et que vous savez dire quelle contrainte vous avez privilégiée et laquelle vous avez dégradée, **votre réponse est valide**.

> Format des cas : le besoin · les contraintes · deux options · la critique · l'architecture retenue · le registre.

#### 48.2 Cas 1 — Une application interne pour 200 utilisateurs

**Le besoin** : une application de gestion, 200 utilisateurs sur un site, données internes non sensibles, budget contraint, une personne à mi-temps pour exploiter.

**Les contraintes chiffrées** :

```
DISPONIBILITÉ   Interruption tolérable : une demi-journée
                Perte de données tolérable : 24 h (sauvegarde quotidienne)
COÛT            Investissement limité · exploitation : 0,5 personne
SÉCURITÉ        Interne uniquement · aucune exposition externe
HISTOIRE        Aucun existant
```

**Deux options** :

| | **Option A — simple** | **Option B — redondée** |
|---|---|---|
| Composants | 1 applicatif, 1 base | 2 applicatifs, 1 répartiteur, base répliquée |
| Coût | ×1 | **≈ ×2,5** avec l'exploitation |
| Interruption en cas de panne | 2 à 4 h | Quelques minutes |
| Exploitants nécessaires | 0,3 personne | **≈ 1 personne** |

⚠️ **Le réflexe à installer ici, et à appliquer partout** :

| Ce que le schéma montre | Ce qu'il faut vérifier |
|---|---|
| Redondance **logique** | Redondance **physique** — hôtes, stockage, site, alimentation |
| Séparation **logique** | Séparation **physique** — ou mécanisme équivalent |
| Chemin **logique** | Chemin **réseau** réel — routage, traduction d'adresses |
| Service **logique** | Processus **réels** qui le rendent |

**Retenu : l'option A.** L'interruption tolérable est d'une demi-journée ; l'option B résout un problème qui n'existe pas, et **exige deux fois plus d'exploitation que l'organisation ne peut fournir** — §47.3.

**④ Critique de sa propre proposition** — grille du chapitre 49 :

| Point | Constat |
|---|---|
| ① Fort | Proportionnée à la capacité d'exploitation. Deux composants, 0,3 exploitant |
| ② Faible | Aucune tolérance de panne · la sauvegarde quotidienne laisse 24 h de saisie exposée |
| ③ Rupture | Les deux composants — **et l'hôte de virtualisation s'ils le partagent** — *principe de preuve* |
| ④ Dépendance cachée | **L'authentification** : contre quoi ? Si c'est l'annuaire, il devient une troisième rupture invisible |
| ⑤ Risque principal | Une panne matérielle un lundi matin : une demi-journée d'arrêt, acceptable · **et jusqu'à 24 h de saisie perdue, qui ne l'est peut-être pas** |
| ⑥ Amélioration | **Une seule** : passer la sauvegarde à trois fois par jour. Coût quasi nul, **ramène la perte maximale de 24 h à 8 h** |

**⑤ Ce que la critique fait changer** : l'architecture reste l'option A, **avec une sauvegarde trois fois par jour**. La critique n'a pas remis en cause la conception — elle a corrigé un paramètre dont personne n'avait chiffré l'effet.

**⑥ Registre des compromis** :

| Compromis | Privilégié | Dégradé | Conséquence acceptée | Revoir si |
|---|---|---|---|---|
| Aucune redondance | Coût, exploitabilité | Disponibilité | Interruption jusqu'à 4 h | L'application devient critique |
| Sauvegarde 3 fois par jour | Coût | Perte de données | Jusqu'à 8 h de saisie perdue **au lieu de 24 h** | Le volume de saisie augmente |
| Authentification contre l'annuaire | Simplicité, gouvernance | Disponibilité | L'annuaire devient une dépendance | L'annuaire devient instable |

**⑨ L'exploitation** : 0,3 personne. L'organisation en dispose. Validé.

**⑩ Ce qu'on ignore encore** : contre quoi l'application authentifie · si l'hôte est partagé avec d'autres services critiques · **si la restauration de la sauvegarde a déjà été testée** — *principe de preuve*.

#### 48.3 Cas 2 — Un service exposé sur Internet

**Le besoin** : publier un portail client, 3 000 clients, données personnelles, interruption tolérable de 2 h en journée.

**Les deux options portent sur l'exposition** :

| | **Option A — publication directe** | **Option B — mandataire inverse** |
|---|---|---|
| Le serveur est joignable | Directement depuis Internet | **Uniquement par le mandataire** |
| Authentification | Dans l'application | **Possible avant l'application** |
| Composants | 2 | 3 |
| Une faille applicative | Exploitable directement | **Nécessite d'abord de passer le mandataire** |

**Retenu : l'option B.** Le surcoût d'un composant est faible ; le gain est structurel — l'application n'est plus exposée, et l'authentification peut précéder son atteinte.

⚠️ **Ce que le registre doit écrire, et qu'on oublie** : le mandataire voit tout le trafic en clair. **C'est un compromis, pas un pur gain** — on concentre le risque en un point pour le retirer d'un autre.

#### 48.4 Cas 3 — Une extension cloud d'un existant

**Le besoin** : ajouter un service accessible depuis l'extérieur, en conservant les identités et une partie des données sur site.

**La question qui décide** : *que se passe-t-il si le lien tombe ?* — §40.3

| Option | Le lien tombe | Coût |
|---|---|---|
| **A — identités synchronisées** | Le cloud continue de fonctionner en autonomie | Une synchronisation à exploiter et superviser |
| **B — identités interrogées en direct** | **Le cloud devient inaccessible** | Plus simple, plus fragile |

**Retenu : l'option A**, avec une condition écrite au registre : **la synchronisation doit être supervisée**, faute de quoi son arrêt passera inaperçu jusqu'à ce que les mots de passe divergent — §40.2.

#### 48.5 Cas 4 — Une reprise d'existant

> **Le cas réel**, et le plus difficile. C'est celui que vous rencontrerez.

**La situation** : une application métier de 2009, base ancienne, client lourd sur 300 postes, un serveur unique jamais redémarré depuis quatorze mois, éditeur toujours actif mais version non supportée. Il faut « moderniser ».

**Ce qu'un débutant propose** : tout refaire.
**Ce que le chapitre 4 enseigne** : commencer par comprendre pourquoi c'est comme ça.

**Les quatre questions préalables** :

| Question | Pourquoi |
|---|---|
| **Qu'est-ce qui dépend de ce système ?** | Souvent plus que prévu — des exports, des interfaces oubliées |
| **Pourquoi n'a-t-il jamais été mis à jour ?** | La réponse est presque toujours *une dépendance qu'on ne sait pas refaire* |
| **Que se passe-t-il s'il tombe demain ?** | Cela chiffre l'urgence réelle |
| **Combien de temps l'éditeur le supportera-t-il ?** | Cela fixe l'horizon |

**Les trois stratégies possibles, et leurs compromis** :

| Stratégie | Ce qu'elle résout | Ce qu'elle coûte | Quand elle est juste |
|---|---|---|---|
| **Remplacer** | Tout | Long, cher, risqué, mobilise le métier | Quand l'éditeur arrête, ou que le besoin a changé |
| **Encapsuler** | L'exposition et la surveillance | Ne résout pas l'obsolescence | Quand le remplacement n'est pas finançable maintenant |
| **Sanctuariser** | Le risque immédiat | Fige le système, dette différée | **Quand rien d'autre n'est possible — et à condition de l'écrire** |

**Retenu, dans la majorité des cas réels : encapsuler, puis planifier le remplacement.** Isoler le système dans un segment dédié, placer un mandataire devant, journaliser ses accès, et inscrire son remplacement au plan avec une échéance.

⚠️ **Ce qui distingue une sanctuarisation d'un abandon** : une date de réexamen, un propriétaire nommé, et un compromis écrit. Sans ces trois éléments, ce n'est pas une décision — c'est un renoncement qui se déguise. **C'est exactement la doctrine du volume Maintien en condition de sécurité.**

#### 48.6 Le capstone — une conception qui évolue

> **L'exercice principal de la Partie IX.** Une architecture ne se conçoit pas d'un coup : elle se corrige à chaque contrainte nouvelle. Voici comment.

##### Version 0 — le besoin brut

> *Une organisation de 300 personnes veut publier un portail permettant à ses 600 clients de consulter leurs dossiers et de déposer des documents.*

**Rien d'autre.** Aucune contrainte chiffrée. C'est la situation réelle, et la première tâche est de le dire.

##### Version 1 — votre première proposition

**Avant de lire la suite, dessinez.** Une page, dix minutes.

Une proposition raisonnable ressemble à ceci :

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ portail ] ──► [ base ]
```

**Quatre composants.** C'est proportionné à un besoin qu'on ne connaît pas encore.

---

##### ⚡ ÉVÉNEMENT 1 — « L'entreprise exige 99,95 % de disponibilité »

**Ce que cela signifie réellement**, et c'est la première chose à faire :

| Engagement | Indisponibilité tolérée par an | Par mois |
|---|---|---|
| 99 % | 3,65 jours | 7 h 18 |
| 99,9 % | 8 h 45 | 43 min |
| **99,95 %** | **4 h 22** | **21 min** |
| 99,99 % | 52 min | 4 min |

⚠️ **Vingt et une minutes par mois** signifie qu'**aucune intervention manuelle n'est possible** : le temps de détecter, comprendre et agir dépasse déjà le budget. **Il faut donc de la bascule automatique.**

**Ce qui change** :

```
   Internet ──► [ pare-feu ×2 ] ──► [ mandataire ×2 ] ──► [ portail ×2 ]
                                                              │
                                                     [ base répliquée ]
```

**Ce que cela coûte, et qu'il faut écrire** : le nombre de composants double · une bascule automatique à configurer **et à tester** · les sessions doivent être partagées, sinon la redondance ne protège pas les utilisateurs en cours — §31.2. **Un composant de plus** : le magasin de sessions.

---

##### ⚡ ÉVÉNEMENT 2 — « Ce sont des données de santé »

**Ce que cela change** : la contrainte de sécurité devient dominante, et des obligations s'ajoutent.

**Quatre conséquences d'architecture** :

| Conséquence | Effet sur le schéma |
|---|---|
| Chiffrement de bout en bout exigé | **Le mandataire passe en mode C** — terminaison puis rechiffrement, §12.3 |
| Traçabilité des accès aux dossiers | La journalisation applicative devient **une exigence, pas un confort** |
| Cloisonnement renforcé | Une frontière entre le portail et la base, distincte de la DMZ |
| Localisation des données | **Contraint le choix d'hébergement** — potentiellement, tout ce qui précède |

⚠️ **Ce que beaucoup oublient** : les **sauvegardes** portent les mêmes données et les mêmes obligations. Et les **environnements de recette**, s'ils contiennent des données réelles — §32.2.

**Ce qui change** : le mode de terminaison, un segment supplémentaire, une journalisation applicative détaillée, et **une revue de tous les endroits où la donnée existe**.

---

##### ⚡ ÉVÉNEMENT 3 — « Le budget est réduit de 30 % »

**La première réaction, et elle est mauvaise** : retirer un exemplaire de chaque composant.

**La bonne démarche** : reprendre les contraintes et demander **laquelle on dégrade**.

| Option | Ce qu'on perd | Ce qu'on garde |
|---|---|---|
| Retirer la redondance du portail | **L'engagement de 99,95 %** — il faut le renégocier | La sécurité |
| Retirer le chiffrement interne | Une exigence liée aux données de santé | **Non négociable** |
| Retirer le magasin de sessions | La redondance ne protège plus les sessions en cours | Une redondance partielle |
| **Renoncer au dépôt de documents** | Une fonctionnalité | **Tout le reste**, et une simplification importante |

⚠️ **La quatrième ligne est celle qu'on n'envisage jamais** — §46.4. Le dépôt de documents est ce qui impose le stockage, les analyses de contenu, une part importante des obligations et une bonne partie du volume. **Y renoncer en version 1, quitte à l'ajouter plus tard, peut absorber les 30 % à lui seul.**

> **Concevoir, c'est choisir ce qu'on accepte de perdre. Et la fonctionnalité est un candidat légitime.**

---

##### ⚡ ÉVÉNEMENT 4 — « Il y aura deux sites »

❓ **La question à poser avant de dessiner quoi que ce soit** : *deux sites pour quoi faire ?*

| Motif invoqué | Ce que cela impose réellement |
|---|---|
| **Continuité en cas de sinistre** | Une réplication des données · **un basculement testé** · un plan documenté |
| **Répartition de charge** | Des données cohérentes entre les deux — **très difficile** |
| **Proximité géographique** | Une réplication en lecture seule peut suffire |
| **« Parce qu'on a deux salles »** | **Rien.** Ce n'est pas une contrainte |

⚠️ **Le quatrième cas est très répandu**, et il produit des architectures à deux sites dont le second n'a jamais été testé — et ne fonctionnerait pas.

**Si le motif est la continuité**, ce qui change :

```
   SITE A                              SITE B
   [ pare-feu ×2 ]                     [ pare-feu ×2 ]
   [ mandataire ×2 ]                   [ mandataire ×2 ]
   [ portail ×2 ]                      [ portail ×2 ]
   [ base primaire ] ══réplication══► [ base secondaire ]
          │                                   │
          └────── résolution de noms ─────────┘
                  qui bascule les clients

   ⚠️ Trois questions nouvelles :
      · la réplication est-elle synchrone ? sinon, combien perd-on ?
      · qui décide de basculer, et en combien de temps ?
      · les certificats et l'annuaire sont-ils disponibles sur les deux sites ?
```

**Ce que cela coûte** : le double de tout · **un basculement à tester au moins deux fois par an** · une décision de bascule qui doit être prise par quelqu'un, la nuit.

---

##### ⚡ ÉVÉNEMENT 5 — « L'équipe d'exploitation compte trois personnes »

> **L'événement qui remet tout en cause**, et c'est volontaire.

**Le calcul** :

| Composant | Exploitants nécessaires |
|---|---|
| Deux sites, chacun complet | ≈ 1,5 |
| Base répliquée avec bascule testée | ≈ 0,5 |
| Magasin de sessions | ≈ 0,2 |
| Chiffrement de bout en bout, certificats | ≈ 0,3 |
| Journalisation applicative détaillée | ≈ 0,3 |
| **Total pour ce seul service** | **≈ 2,8** |

⚠️ **Trois personnes exploitent tout le système d'information**, pas seulement ce portail. **L'architecture consomme la quasi-totalité de la capacité pour un seul service.**

**Selon le §47.2, elle se dégradera** : la bascule ne sera pas testée, les certificats expireront, la réplication tombera sans que personne ne le voie.

**Les trois options honnêtes** :

| Option | Ce qu'elle implique |
|---|---|
| **Recruter** | Un coût récurrent, et un délai de plusieurs mois |
| **Externaliser l'exploitation** | Un prestataire · **et les accès privilégiés qui vont avec** — §38.4 |
| **Simplifier l'architecture** | Renégocier l'engagement de disponibilité |

⚠️ **La troisième est très répandue, et rarement avouée.** Elle suppose de retourner voir le métier et de dire : *« l'engagement de 99,95 % coûte deux exploitants que nous n'avons pas. Que se passe-t-il réellement si le portail est indisponible quatre heures ? »*

**Dans la majorité des cas, la réponse est « pas grand-chose »** — et l'engagement avait été énoncé sans avoir été chiffré.

---

##### ⑩ La question finale

> ### Expliquez ce que vous avez volontairement décidé de ne pas faire.

**C'est le livrable qui distingue un concepteur d'un assembleur de briques.**

**Une réponse attendue ressemble à ceci** :

> *Nous avons renoncé au dépôt de documents en version 1, ce qui absorbe la contrainte budgétaire et supprime une part importante des obligations liées au stockage. Nous avons renoncé au second site, faute de capacité d'exploitation pour le maintenir en état de fonctionner — un second site non testé aurait donné une illusion de continuité. Nous avons renégocié l'engagement à 99,9 %, ce qui autorise une intervention humaine et divise par deux la complexité. Nous avons conservé le chiffrement de bout en bout et la journalisation applicative, qui ne sont pas négociables au regard des données traitées.*
>
> *Ce que nous n'avons pas pu vérifier : le délai réel de restauration de la base · la capacité du lien Internet à absorber le volume · si l'équipe sait exploiter un magasin de sessions.*

⚠️ **Remarquez ce que cette réponse contient** : quatre renoncements motivés, deux non-négociables, et trois incertitudes déclarées. **Aucune ligne ne décrit un composant.**

##### Les cinq enseignements du capstone

| # | Enseignement |
|---|---|
| **1** | Une contrainte non chiffrée ne se conçoit pas — **elle se demande** |
| **2** | Un engagement de disponibilité se traduit en **minutes par mois**, et cela change tout |
| **3** | Une contrainte nouvelle ne s'ajoute pas : **elle oblige à en dégrader une autre** |
| **4** | **Renoncer à une fonctionnalité est un arbitrage légitime**, et souvent le moins cher |
| **5** | **La capacité d'exploitation est la contrainte qui décide**, et elle arrive toujours en dernier |

#### 48.7 🔬 Mini-labs 11 et 12

**🔬 Mini-lab 11 — Concevoir pour trois organisations** · *45 min · 🟠*
Même besoin — publier un service de suivi pour des clients — chez Atelier Martin, HELIOMED et Novaris. Produire trois architectures différentes, et **justifier chaque écart par une contrainte, jamais par la taille** — *principe de la contrainte*.

**🔬 Mini-lab 12 — Le registre des compromis** · *30 min · 🟠*
À partir d'une architecture fournie, reconstituer le registre des compromis qui l'a produite : quelle contrainte a été privilégiée à chaque endroit, laquelle a été dégradée, et ce qui devrait déclencher un réexamen.

---

### Chapitre 49 — Critiquer une architecture

> La compétence de fin de cours, et la plus délicate à exercer.

#### 49.1 La grille en six points

```
  ①  POINT FORT             Ce qui est bien pensé, et pourquoi
  ②  POINT FAIBLE           Ce qui est fragile, et sous quelle condition
  ③  POINT DE RUPTURE       Ce qui n'a pas de doublure
  ④  DÉPENDANCE CACHÉE      Ce dont tout dépend et qui n'est pas dessiné
  ⑤  RISQUE PRINCIPAL       Le scénario le plus probable et le plus coûteux
  ⑥  AMÉLIORATION           Le meilleur rapport effet/coût — une seule
```

**L'ordre compte, et le premier point aussi.** Une critique qui commence par les faiblesses ne sera pas entendue par ceux qui ont conçu l'architecture. **Commencer par ce qui est bien pensé n'est pas une politesse : c'est une condition d'efficacité.**

#### 49.2 Ce qui distingue une critique utile

| Critique inutile | Critique utile |
|---|---|
| « Il n'y a pas de zone démilitarisée » | « Aucun service n'est publié aujourd'hui. Si l'un devait l'être, la publication directe deviendrait un problème — c'est le déclencheur à surveiller » |
| « L'applicatif n'est pas redondé » | « L'applicatif est unique. Est-ce un arbitrage documenté ? Si oui, quelle interruption a été jugée tolérable ? » |
| « Cette passerelle ne devrait pas exister » | « Cette passerelle date de 2018 et porte un export vers le contrôle de gestion. Le besoin existe-t-il encore, et peut-il passer autrement ? » |
| « C'est du legacy » | « Ce composant a quinze ans. Que dépend de lui, et l'éditeur le supporte-t-il encore ? » |

⚠️ **Le point commun des critiques utiles** : elles **posent une question** au lieu d'énoncer un verdict, et elles supposent que la personne en face avait une raison — chapitre 4.

#### 49.3 Les cinq erreurs du critique débutant

| Erreur | Pourquoi c'est une erreur |
|---|---|
| **Juger sans demander l'histoire** | §4.4 — chaque anomalie a une date |
| **Comparer à un idéal théorique** | Aucune architecture réelle n'y ressemble |
| **Traiter la taille comme une norme** | *Principe de la contrainte* |
| **Proposer dix améliorations** | Aucune ne sera faite. **Une seule sera peut-être faite** |
| **Oublier le coût de sa propre proposition** | *Principe du coût* — ajouter n'est jamais gratuit |

**La quatrième est la plus coûteuse en crédibilité.** Une liste de dix recommandations est reçue comme un jugement global ; une recommandation unique, chiffrée et justifiée est reçue comme une contribution.

#### 49.4 Formuler une critique qui sera entendue

🧪 **EN PRATIQUE — le format en cinq lignes**

```
CE QUI FONCTIONNE      [1 à 2 éléments, précis]
CE QUE J'AI OBSERVÉ    [le constat, factuel, sans jugement]
CE QUE JE N'AI PAS SU  [ce qui manque pour conclure — souvent l'histoire]
LE RISQUE              [scénario, probabilité, conséquence]
CE QUE JE PROPOSE      [une action, son coût, son effet attendu]
```

**La troisième ligne est celle qui change la réception.** Dire *« je n'ai pas su pourquoi l'applicatif n'est pas redondé »* ouvre une conversation ; dire *« l'applicatif n'est pas redondé »* ferme la porte.

#### 49.5 🔬 Mini-lab 13 — Critiquer trois architectures

**Objectif** — Appliquer la grille en six points et produire une critique en cinq lignes.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 36, 47, 49

Trois architectures : celle d'Atelier Martin · celle du mini-lab 7 · celle du §37.4, avec `HERMES`.

---

**Corrigé — Atelier Martin**

| Point | Constat |
|---|---|
| ① Fort | **L'architecture est proportionnée** : deux segments, peu de composants, exploitable par une personne à mi-temps. C'est cohérent |
| ② Faible | Les machines à commande numérique sont sur le segment bureautique |
| ③ Rupture | Le contrôleur d'annuaire unique · le pare-feu tout-en-un |
| ④ Dépendance cachée | Le prestataire local, **avec un accès permanent et aucune traçabilité** |
| ⑤ Risque principal | Un poste bureautique compromis atteint les machines de production. **Conséquence : arrêt de production, et potentiellement sûreté** |
| ⑥ Amélioration | **Une seule** : séparer le segment atelier. Coût faible, effet majeur |

**La critique en cinq lignes** :

> *Ce qui fonctionne : l'architecture est dimensionnée pour ce que l'organisation peut exploiter, ce qui est rare et précieux.*
> *Ce que j'ai observé : les deux machines à commande numérique sont sur le même segment que les postes bureautiques.*
> *Ce que je n'ai pas su : si cette situation résulte d'un choix ou de l'absence de question posée.*
> *Le risque : un poste compromis — une voie d'entrée majeure — atteint directement les machines de production. Conséquence : arrêt de production, et selon les machines, question de sûreté.*
> *Ce que je propose : séparer le segment atelier. Un commutateur et une règle de filtrage sur le boîtier existant. Coût faible, c'est la seule action que je recommande cette année.*

⚠️ **Ce que la critique ne dit pas** : que l'absence d'annuaire redondé est un problème. Elle en est un techniquement, et **elle n'est pas la priorité** — §49.3, quatrième erreur.

⚠️ **Cohérence avec le §36.4** : la grille en six points **relève** six éléments, la critique formulée **n'en propose qu'un**. Les cinq autres constats servent à établir que le sixième est bien le plus urgent — ils ne sont pas énoncés en réunion.

---

### Chapitre 50 — Ce qu'un schéma ne dira jamais

> **Clôture du cours.** Il apprend la leçon qui empêche de terminer ce livre avec une confiance excessive.

#### 50.1 Le tableau visible / invisible

| Ce qu'un schéma montre | Ce qu'il ne montrera jamais |
|---|---|
| Les segments et les zones | **Les procédures d'exploitation** |
| Les pare-feu | **Les règles réellement en place** |
| Les serveurs | **Ce qui s'y exécute vraiment** |
| Les liens | **Ce qui les traverse** |
| Les flux dessinés | **Les flux de dépendance** — principe des trois flux |
| Les services | **Les contraintes métier qui les ont produits** |
| La redondance | **Si elle a déjà été testée** |
| Les composants | **Les compétences pour les exploiter** |
| L'agencement | **Les décisions et les arbitrages** |
| Le nominal | **Les contournements en place depuis trois ans** |
| Les versions, parfois | **Les correctifs réellement appliqués** |
| L'instantané | **L'histoire, et ce qui est en cours de migration** |

**Les quatre dernières lignes font la leçon.** Un schéma décrit un système ; il ne décrit ni l'organisation qui le tient, ni l'histoire qui l'a produit, ni l'écart entre l'intention et le réel.

#### 50.2 Les deux écarts symétriques

| Écart | Fréquence | Comment on le détecte |
|---|---|---|
| **Dessiné et jamais construit** | Fréquent | Le composant n'apparaît dans aucun inventaire, aucun journal, aucune facture |
| **Construit et jamais dessiné** | **Plus fréquent encore** | Un flux observé sans origine documentée · une machine qui répond et n'est nulle part |

⚠️ **Le second est le plus dangereux.** Il désigne exactement ce que le volume Asset Management appelle un actif orphelin ou une informatique parallèle : quelque chose existe, fonctionne, expose — et n'est connu de personne.

#### 50.3 Comment on vérifie

| Méthode | Ce qu'elle révèle | Coût |
|---|---|---|
| **Suivre un flux en vrai**, avec l'exploitation | L'écart entre le chemin dessiné et le chemin réel | Une demi-journée |
| **Comparer avec l'inventaire** | Ce qui existe et n'est pas dessiné | Selon la qualité de l'inventaire |
| **Lire les règles de pare-feu** | Ce qui est réellement autorisé, contre ce qui est supposé l'être | Quelques heures, souvent instructives |
| **Regarder les journaux** | Les flux qui existent vraiment | Variable |
| **Demander à quelqu'un d'ancien** | L'histoire, les contournements, les raisons | **Une heure, le meilleur rapport du tableau** |

⚠️ **La dernière ligne est la plus efficace et la moins pratiquée.** Une conversation d'une heure avec quelqu'un présent depuis dix ans apprend davantage sur une architecture que trois jours de lecture de documents.

#### 50.4 La phrase de clôture

> ### Une architecture dessinée n'est pas une architecture réelle.

**Ce que cela impose** :

| Devant un schéma | La bonne posture |
|---|---|
| Il est complet | **Il ne l'est jamais** — la question est de savoir de combien |
| Il est à jour | **Datez-le**, et demandez ce qui a changé depuis |
| Il est vrai | Il représente une intention. Vérifiez ce qui a été construit |
| Il est neutre | **Il a été fait pour quelqu'un** — §5.5 |

#### 50.5 🔬 Mini-lab 14 — Dessiner l'architecture de votre organisation

**Objectif** — Produire un schéma, puis lister ce qu'il tait.
**Durée** 2 h · **Difficulté** 🔴 avancé · **Prérequis** l'ensemble du cours

```
1. Dessinez l'architecture de votre organisation, ou d'un service
   que vous connaissez. Une page, à la main.

2. Appliquez les sept passes du chapitre 36 à VOTRE schéma.

3. Listez les onze éléments du §3.4 qui n'y figurent pas.

4. Écrivez les trois questions que vous ne savez pas trancher.

5. Allez poser ces trois questions.
```

**Ce que l'exercice produit systématiquement** : entre trois et six découvertes, dont au moins une concerne un flux ou un composant dont l'existence n'était pas connue de la personne qui a dessiné.

#### 50.6 🔴 FIL ROUGE — décembre 2025 : ce qu'Amélie a compris

*Dernier épisode du cours. Il se raccorde au premier chapitre du volume Asset Management.*

Le 19 décembre, Amélie remet à Claire Nadeau un document de deux pages. Il ne contient aucun inventaire.

**Page 1 — le schéma redessiné.** Le même que celui de mars 2023, avec onze ajouts au crayon : la résolution de noms, l'annuaire relié à tout, la synchronisation d'horloge, le réseau d'administration, les 620 postes, les 180 nomades, la passerelle d'accès distant, le site de Nantes, les postes de prestataires, la collecte de journaux, et une zone marquée d'un point d'interrogation : *services en ligne — nombre inconnu*.

**Page 2 — ce que le schéma ne dit pas.** Vingt-trois lignes, chacune une question sans réponse.

**Ce que Claire lui dit en le lisant** :

> *« C'est la première fois en trois ans que je vois ce document. »*

**Ce qu'Amélie écrit en conclusion**, et qui est la phrase qui ouvre le volume suivant :

> *Le schéma de mars 2023 n'était pas faux. Il montrait ce que quelqu'un avait choisi de montrer, à un moment, pour une raison. Mon travail ne consiste pas à le corriger. Il consiste à savoir de combien il s'écarte de ce qui existe — et à écrire cet écart.*

**Le 5 janvier 2026, sa mission d'inventaire démarre.** Elle sait ce qu'elle regarde.

---

> ### 🎓 Ce que vous savez faire
>
> **Lire**
> ☐ Poser les quatre questions du lecteur devant n'importe quel schéma
> ☐ Appliquer les sept passes dans l'ordre, et produire une lecture d'une page
> ☐ Distinguer trois familles de flux, et savoir laquelle arrête un service
> ☐ Suivre une requête en douze étapes, dont sept ne sont pas dessinées
> ☐ Reconnaître une strate ancienne à trois signes convergents
> ☐ Identifier les points de rupture, y compris ceux qui ne sont reliés à rien
>
> **Comprendre**
> ☐ Expliquer ce que chaque composant résout et ce qu'il coûte
> ☐ Reconstituer l'arbitrage qui a produit une architecture
> ☐ Dire à partir de quelle contrainte un composant devient nécessaire
> ☐ Construire l'arbre de dépendance d'un service métier
> ☐ Dire où l'on peut agir, et où c'est structurellement impossible
>
> **Concevoir et critiquer**
> ☐ Chiffrer des contraintes plutôt que de les énoncer
> ☐ Proposer une architecture proportionnée à ce que l'organisation sait exploiter
> ☐ Écrire un registre des compromis
> ☐ Critiquer en six points, et ne recommander qu'une seule action
> ☐ Formuler une critique en cinq lignes qui sera entendue
>
> **Savoir ce qu'on ne sait pas**
> ☐ Lister ce qu'un schéma ne dit pas
> ☐ Distinguer ce qui a été dessiné et jamais construit de l'inverse
> ☐ Poser trois questions plutôt qu'un jugement
>
> ---
>
> **Ce que ce cours ne vous a pas appris** : dimensionner, choisir un produit, administrer un composant, concevoir un système à forte contrainte. Ces métiers existent, et ils s'apprennent ailleurs.
>
> **Ce que seule la pratique donne** : le sens de ce qui va casser avant que ça casse, la mémoire des architectures qu'on a vues échouer, et la patience de demander l'histoire avant de juger.

---

## Cas de synthèse

---

### Cas A — Le schéma qu'on vous donne le premier jour

> **Durée** 2 h · **Livrables** : lecture en sept passes · liste de l'invisible · trois questions
> **Prérequis** : chapitres 3, 4, 36, 50

#### A.1 La situation

Vous arrivez comme référent sécurité dans une organisation de 700 personnes, secteur des services, trois sites. On vous remet un schéma daté de **mars 2021** et un accès en lecture à l'outil d'inventaire.

```
                          Internet
                              │
                        [ FW-EXT ]
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   [ WEB-PUB ]          [ MAIL-RELAY ]        [ VPN-GW ]
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                        [ FW-INT ]
                              │
   ┌──────────────┬───────────┼───────────┬──────────────┐
   │              │           │           │              │
[ APP-01 ]   [ DB-01 ]   [ FILE-01 ]  [ DC-01 ]    [ SAUV-01 ]
                              │
                     [ segment postes ]
```

**Informations complémentaires** :

```
· L'outil d'inventaire compte 214 machines. Le schéma en montre 8.
· Le site de Bordeaux a été ouvert en 2023.
· Une migration de messagerie vers un service en ligne a eu lieu en 2024.
· MAIL-RELAY existe toujours dans l'inventaire.
· L'auteur du schéma a quitté l'organisation en 2022.
```

#### A.2 Les questions

| # | Question |
|---|---|
| 1 | Appliquez les sept passes. Que produisez-vous ? |
| 2 | Combien de zones, et lesquelles sont réellement matérialisées ? |
| 3 | Que manque-t-il, et pourquoi ? |
| 4 | Quels éléments ont probablement changé depuis mars 2021 ? |
| 5 | Quelles **trois questions** posez-vous, et à qui ? |
| 6 | Quatre anomalies sont insérées dans le dossier. Lesquelles ? |

#### A.3 Corrigé — les sept passes

**① LES ZONES** — Trois apparentes : extérieur, une zone entre les deux pare-feu, l'interne. **La seconde frontière existe** — c'est `FW-INT` — ce qui est rare et bon signe.

⚠️ **Mais** : rien ne matérialise de frontière **à l'intérieur** de la zone interne. `DC-01`, `DB-01` et le segment des postes semblent joignables entre eux. §24.1.

**② L'ENTRÉE** — Trois entrées dessinées : web, messagerie, accès distant. **Une quatrième n'est pas dessinée : l'administration** — §27.3. Et une cinquième, invisible : les postes eux-mêmes, qui ne figurent que comme « segment postes » sans détail.

**③ LES DONNÉES** — `DB-01` et `FILE-01` sont dessinés. Les copies ne le sont pas : réplicas, environnements de recette, exports, et depuis 2024 **les données de messagerie chez un fournisseur** — §32.2.

**④ L'IDENTITÉ** — `DC-01` est dessiné, **relié à rien**. Cas canonique du §1.1. Et depuis la migration de 2024, une question nouvelle : **la messagerie en ligne s'authentifie-t-elle contre `DC-01`, ou possède-t-elle ses propres identités ?**

**⑤ LES FLUX** — Une requête externe suit les étapes du §29.1. Aucun des sept flux invisibles n'est représenté.

**⑥ LES RUPTURES** — Au moins six, dont trois invisibles :

| Composant | Rupture ? | Visible ? |
|---|---|---|
| `FW-EXT`, `FW-INT` | Oui, sauf redondance non dessinée | ✅ |
| `APP-01`, `DB-01` | **Oui**, uniques | ✅ |
| `VPN-GW` | Oui, pour les nomades | ✅ |
| Résolution de noms | **Oui** | ❌ |
| `DC-01` | **Oui**, unique | ✅ dessiné, ❌ non relié |
| Certificats | **Oui**, à date connue | ❌ |

**⑦ L'INVISIBLE** — Onze éléments manquants (§3.4), plus quatre propres au dossier : **le site de Bordeaux**, ouvert deux ans après le schéma · **le service de messagerie en ligne** de 2024 · **les 206 machines** que l'inventaire connaît et que le schéma ignore · **les prestataires**.

#### A.4 Corrigé — les quatre anomalies insérées

| # | Anomalie | Ce qu'elle révèle |
|---|---|---|
| **1** | **`MAIL-RELAY` existe encore dans l'inventaire après la migration de 2024** | Un composant **construit, dessiné, et devenu inutile** — mais toujours exposé. C'est un actif zombie, encore joignable depuis Internet |
| **2** | **Le site de Bordeaux n'est pas sur le schéma** | Le schéma date de 2021, le site de 2023. **Ce n'est pas une erreur, c'est une péremption** — §50.4 |
| **3** | **8 machines dessinées contre 214 inventoriées** | Le schéma est une vue logique de rôles, pas de machines — §3.1. Mais l'écart de 206 n'est documenté nulle part |
| **4** | **`DC-01` est unique et relié à rien** | Deux problèmes en un : un point de rupture majeur, et l'invisibilité universelle de l'annuaire |

⚠️ **L'anomalie 1 est la plus discrète, et ses conséquences sont les plus larges.** Un relais de messagerie devenu inutile après une migration reste exposé sur Internet, n'est plus surveillé par personne, et **continue d'être corrigé au mieux par habitude**. C'est le cas d'école du décommissionnement inachevé, traité dans le volume Asset Management.

#### A.5 Corrigé — les trois questions

**À qui, et lesquelles** — trois questions seulement, et le choix des destinataires compte autant que celui des questions.

| # | Question | À qui | Pourquoi celle-ci |
|---|---|---|---|
| **1** | *« `MAIL-RELAY` est-il encore utilisé, et est-il encore joignable depuis Internet ? »* | Exploitation | **Un composant exposé sans usage est le meilleur rapport risque/effort du dossier** |
| **2** | *« Comment administre-t-on ces machines, et depuis quel poste ? »* | Exploitation | §27 — le chemin le plus court vers la compromission totale n'est pas dessiné |
| **3** | *« Depuis la migration de 2024, les identités de la messagerie viennent-elles de `DC-01` ? »* | DSI ou responsable messagerie | §40.2 — la synchronisation d'identités est un point de fragilité récurrent d'une architecture hybride |

**Ce qu'on ne demande pas le premier jour**, et pourquoi :

| Question écartée | Motif |
|---|---|
| *« Pourquoi n'y a-t-il qu'un seul serveur applicatif ? »* | Elle sonne comme un reproche. Elle viendra, après avoir compris l'histoire — §4.4 |
| *« Pourquoi le schéma n'est-il pas à jour ? »* | Sans objet : aucun schéma ne l'est. §50.4 |
| *« Où est la documentation ? »* | Elle n'existe probablement pas, et la demander ne produit rien |

⚠️ **Avertissement sur les barèmes de ces trois cas**

Les barèmes qui suivent notent **des comportements, pas des réponses**. Ils récompensent le fait de poser la bonne question, de dater un schéma, de relever une absence — jamais le fait d'écrire exactement la même phrase que le corrigé.

**Conformément au §48.0** : sur les cas de conception, **plusieurs architectures sont défendables**. Une proposition qui diffère du corrigé et qui énonce clairement la contrainte privilégiée et la contrainte dégradée **obtient le plein barème**.

**Et conformément au principe d'hypothèse** : une identification de composant formulée avec certitude perd des points, même si elle est juste. **Ce qu'on note est la démarche, pas la chance.**

#### A.6 Le barème

| Critère | Pts |
|---|---|
| Relever `MAIL-RELAY` comme zombie exposé | **20** |
| Relever l'absence de chemin d'administration | **20** |
| Dater le schéma et identifier les deux événements postérieurs | 15 |
| Identifier `DC-01` comme rupture, malgré l'absence de trait | 15 |
| Distinguer l'écart 8/214 comme choix de vue, pas comme erreur | 10 |
| Poser la question de la migration de messagerie | 10 |
| Formuler trois questions et pas dix | 10 |

**Élimination** : commencer par critiquer l'architecture avant d'avoir demandé son histoire — §4.4.

---

### Cas B — Le service qui tombe

> **Durée** 1 h 30 · **Livrable** : liste ordonnée des causes possibles, et vérifications
> **Prérequis** : chapitres 29 à 35, 43

#### B.1 La situation

**Mardi 10 h 15.** Le service « Portail clients » est inaccessible depuis l'extérieur. Vous n'avez que le schéma 1.1 et quinze minutes avant le point de crise.

**Les faits rapportés** :

```
· Les clients externes obtiennent une erreur de connexion.
· Les salariés internes accèdent normalement au portail.
· La supervision est au vert sur les trois serveurs web,
  sur l'applicatif et sur la base.
· L'incident a commencé « vers 9 h 40 ».
· Aucune intervention n'était planifiée.
```

#### B.2 Les questions

1. Que vous dit le fait que l'interne fonctionne et l'externe non ?
2. Listez les causes possibles, **par ordre de probabilité**.
3. Quelles vérifications, dans quel ordre, et en combien de temps ?
4. Que dit la supervision au vert, et que ne dit-elle pas ?

#### B.3 Corrigé — ce que la dissymétrie révèle

**L'information la plus précieuse du dossier est que l'interne fonctionne.**

Elle élimine d'emblée tout ce qui est commun aux deux chemins :

| Éliminé | Pourquoi |
|---|---|
| Serveurs web | L'interne les atteint |
| Applicatif, base | Idem |
| Annuaire | L'authentification interne fonctionne |
| Segment serveurs | Joignable |

**Ce qui reste : ce qui est propre au chemin externe** — §29.3.

```
   CHEMIN EXTERNE          Internet → FW → mandataire → répartiteur → web
   CHEMIN INTERNE          poste → répartiteur → web
                                    ▲
                          la divergence est ici
```

#### B.4 Corrigé — les causes, par ordre de probabilité

| # | Cause | Probabilité | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Certificat expiré** sur le mandataire | **Élevée** | Cause fréquente, effet exactement conforme aux symptômes, **survient sans intervention** — §17 |
| **2** | **Résolution de noms externe** défaillante | **Élevée** | Un enregistrement public **modifié, supprimé, ou dont les serveurs faisant autorité ne répondent plus**. L'interne utilise une vue différente — §14 |
| **3** | Mandataire inverse en panne ou saturé | Moyenne | Sa panne n'affecte que l'externe — §12 |
| **4** | Règle de pare-feu modifiée | Moyenne | « Aucune intervention planifiée » n'exclut pas une intervention non planifiée |
| **5** | Lien Internet dégradé | Faible | Affecterait aussi la sortie des postes |
| **6** | Attaque en déni de service | Faible | Possible, à ne pas privilégier faute d'élément |

⚠️ **Les deux premières partagent une propriété qui explique leur rang** : elles **peuvent survenir sans que personne n'ait rien fait de visible ce jour-là**.

📌 **Une précision, parce que le mot « expiration » recouvre trois choses différentes en résolution de noms** :

| Ce qui expire | Effet |
|---|---|
| **La durée de vie d'une réponse en cache** | Le client redemande. **Si les serveurs faisant autorité répondent, rien ne change** |
| **L'enregistrement du nom de domaine lui-même** | Le nom cesse d'être délégué — le service devient injoignable de l'extérieur |
| **Un certificat** | Le client refuse la connexion, à l'heure inscrite dans le certificat |

⚠️ **Seules les deux dernières arrêtent un service.** La première est un mécanisme normal — elle ne devient un problème que si la réponse obtenue au renouvellement a changé, ou si les serveurs faisant autorité ne répondent plus.

#### B.5 Corrigé — les vérifications, dans l'ordre

| Ordre | Vérification | Durée | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Ouvrir le service depuis l'extérieur et lire l'erreur exacte** | 2 min | Une erreur de certificat, de nom ou de connexion **désigne directement une des trois premières causes** |
| **2** | Vérifier la date d'expiration du certificat du mandataire | 3 min | Coût nul, cause n° 1 |
| **3** | Résoudre le nom public depuis l'extérieur | 3 min | Cause n° 2 |
| **4** | État du mandataire : processus, charge, journaux depuis 9 h 30 | 5 min | Cause n° 3 |
| **5** | Journal du pare-feu : changement de configuration récent | 5 min | Cause n° 4 |

**Total : moins de vingt minutes**, et les trois premières vérifications couvrent les deux causes les plus probables pour huit minutes de travail.

⚠️ **L'erreur classique** : commencer par les serveurs web, parce qu'ils sont au centre du schéma et qu'on sait les vérifier. **Ils sont déjà éliminés par le fait que l'interne fonctionne.**

#### B.6 Corrigé — ce que la supervision au vert dit et ne dit pas

| Elle dit | Elle ne dit pas |
|---|---|
| Les processus tournent | Que le service est rendu |
| Les machines répondent | Que le certificat est valide |
| La base accepte des connexions | Que le chemin externe fonctionne |
| Les indicateurs surveillés sont normaux | **Ce qui n'est pas surveillé** |

> **Une supervision au vert pendant un incident signifie que l'incident se produit là où l'on ne regarde pas.** C'est une information, pas une contradiction.

**Ce que l'incident révèle sur la supervision**, et qui est le vrai livrable du cas : **rien ne surveille l'expiration des certificats, ni la résolution du nom depuis l'extérieur.** Ce sont deux flux de dépendance — principe des trois flux — et ils ne sont ni dessinés, ni supervisés.

#### B.7 Le barème

| Critère | Pts |
|---|---|
| Exploiter la dissymétrie interne/externe pour éliminer | **25** |
| Placer certificat et résolution en tête | **20** |
| Commencer par lire l'erreur exacte | 15 |
| Vérifications ordonnées par coût croissant | 15 |
| Expliquer ce que la supervision au vert signifie | 15 |
| Conclure sur ce qui n'est pas supervisé | 10 |

**Élimination** : commencer par redémarrer un serveur web.

---

### Cas C — Concevoir sous contrainte réelle

> **Durée** 2 h 30 · **Livrables** : architecture · registre des compromis · liste de ce qui reste à vérifier
> **Prérequis** : Partie IX

#### C.1 La situation

**L'organisation** : 450 personnes, deux sites, fabricant de composants électroniques.

**Le besoin** : publier un portail permettant à 80 clients de suivre l'avancement de leurs commandes et de télécharger des documents techniques.

**Les contraintes**, telles qu'elles vous sont données — et deux ne sont pas chiffrées :

```
DISPONIBILITÉ   « Il faut que ce soit fiable »
PERFORMANCE     Non exprimée
COÛT            60 k€ d'investissement · 1,5 personne à l'exploitation, en tout
SÉCURITÉ        Documents techniques = propriété industrielle. Sensible.
CONFORMITÉ      Données de contact clients
HISTOIRE        L'ERP existant contient les données de commande.
                Version 2019, éditeur actif, interface applicative disponible.
                Aucune zone démilitarisée aujourd'hui. Rien n'est publié.
```

#### C.2 Les questions

1. Que faites-vous des deux contraintes non chiffrées ?
2. Produisez deux options, avec leurs compromis.
3. Retenez-en une, et écrivez le registre.
4. Que reste-t-il à vérifier avant de s'engager ?

#### C.3 Corrigé — les contraintes non chiffrées

**C'est la première tâche, et la plus déterminante** — §46.3.

| Contrainte | Ce qu'on demande | Pourquoi |
|---|---|---|
| **Disponibilité** | *« Si le portail est indisponible une demi-journée en semaine, que se passe-t-il ? »* | *« Fiable »* ne se conçoit pas. **Une réponse chiffrée détermine la moitié de l'architecture** |
| **Performance** | *« Combien de clients simultanés, et quelle taille de documents ? »* | 80 clients qui consultent occasionnellement et 80 qui téléchargent des fichiers lourds ne produisent pas la même architecture |

**Réponses obtenues** *(à supposer pour la suite)* : une demi-journée est tolérable · consultations occasionnelles, documents jusqu'à 50 Mo.

⚠️ **Ce que cette réponse change immédiatement** : une interruption d'une demi-journée tolérable **élimine la nécessité d'une redondance complète**, et libère l'essentiel du budget pour la sécurité — qui est la contrainte réellement forte ici.

#### C.4 Corrigé — les deux options

| | **Option A — publication directe** | **Option B — zone démilitarisée avec mandataire** |
|---|---|---|
| Composants nouveaux | 1 serveur portail | Mandataire inverse · serveur portail · segment DMZ · règles |
| Accès à l'ERP | Le portail interroge l'ERP directement | **Le portail interroge une copie**, alimentée depuis l'ERP |
| Exposition de l'ERP | **L'ERP est atteignable depuis un serveur exposé** | L'ERP n'est jamais atteignable depuis l'extérieur |
| Investissement | ≈ 20 k€ | ≈ 45 k€ |
| Exploitation | 0,2 personne | **0,6 personne** |
| Une faille du portail | Donne accès à l'ERP de 2019, non supporté | Donne accès à une copie de données |

**Retenu : l'option B**, et le raisonnement tient en une ligne :

> **La contrainte forte de ce dossier n'est pas la disponibilité, c'est la propriété industrielle.** L'option A place un serveur exposé en communication directe avec un progiciel de 2019 — c'est-à-dire le composant le moins maintenable de l'organisation.

⚠️ **Le point de conception le plus important est la copie de données.** Le portail ne lit pas l'ERP : il lit une base alimentée par un export périodique. Cela dégrade la fraîcheur — les données ont jusqu'à une heure de retard — et **supprime tout chemin depuis l'extérieur vers l'ERP**. C'est un compromis, et il doit être écrit.

#### C.5 Corrigé — le registre des compromis

| # | Compromis | Privilégié | Dégradé | Conséquence acceptée | Revoir si |
|---|---|---|---|---|---|
| **1** | Aucune redondance du portail | Coût, exploitation | Disponibilité | Interruption jusqu'à une demi-journée | La tolérance métier change · le nombre de clients croît |
| **2** | **Copie de données au lieu d'accès direct à l'ERP** | **Sécurité** | Fraîcheur | Données à jour à une heure près | Un besoin de temps réel apparaît |
| **3** | Mandataire inverse unique | Coût | Disponibilité externe | Le portail devient injoignable si le mandataire tombe | La disponibilité devient critique |
| **4** | Authentification par comptes locaux au portail | Simplicité, indépendance | Gouvernance des identités | 80 comptes à gérer séparément | Le nombre de clients dépasse ~200 |
| **5** | Pas de détection sur le serveur portail | Coût | Observabilité | On dépend des journaux du mandataire | Le budget le permet l'an prochain |

**Ce que le registre rend possible dans dix ans** : quelqu'un qui découvrira ce portail comprendra **pourquoi il lit une copie** au lieu de l'ERP — et ne conclura pas à une incohérence. C'est le chapitre 4, par anticipation.

#### C.6 Corrigé — ce qui reste à vérifier

**La section qui distingue une proposition d'un engagement** — §7.3.

| # | À vérifier | Pourquoi | Qui |
|---|---|---|---|
| 1 | **L'interface de l'ERP 2019 permet-elle l'export nécessaire ?** | Toute l'option B en dépend | Éditeur |
| 2 | Quelle est la charge réelle des téléchargements de 50 Mo ? | Dimensionne le lien Internet | Métier + réseau |
| 3 | Le lien Internet actuel supporte-t-il un usage entrant ? | Aujourd'hui il ne sert qu'à sortir | Réseau |
| 4 | **Qui exploitera le mandataire ?** | 0,6 personne sur 1,5 disponible : est-ce tenable ? | DSI |
| 5 | Les documents techniques sont-ils tous partageables ? | Certains peuvent être sous accord de confidentialité | Juridique, R&D |
| 6 | Le basculement en cas de panne du portail a-t-il un mode dégradé ? | Envoi manuel par courriel ? | Métier |

⚠️ **La question 4 est celle qui peut faire échouer le projet**, et c'est le §47.3 : une architecture qui consomme 0,6 exploitant sur 1,5 disponible laisse 0,9 pour tout le reste du système d'information. **Si la réponse est non, l'option A revient sur la table — avec ses compromis, écrits.**

#### C.7 Le barème

| Critère | Pts |
|---|---|
| Chiffrer les deux contraintes manquantes **avant** de concevoir | **25** |
| Identifier que la contrainte forte est la propriété industrielle, pas la disponibilité | **20** |
| Proposer la copie de données plutôt que l'accès direct à l'ERP | **20** |
| Registre des compromis complet, avec conditions de réexamen | 15 |
| Liste de ce qui reste à vérifier, dont la capacité d'exploitation | 15 |
| Ne pas surconcevoir | 5 |

**Élimination** : proposer une architecture redondée sans avoir chiffré la disponibilité tolérable.

📌 **Une autre architecture que l'option B est recevable** si elle est justifiée par un arbitrage écrit. Ce qui n'est pas recevable, c'est d'arbitrer sans avoir demandé les deux contraintes manquantes — §46.3.

---

## ANNEXES

### Plan d'accès

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme | **A** — glossaire |
| Retrouver un composant et son rôle | **B** — fiches composants |
| Lire une architecture méthodiquement | **C** — la grille en sept passes |
| Comprendre une convention de dessin | **D** — conventions |
| Retrouver un schéma du cours | **E** — catalogue |
| Voir une architecture type commentée | **F** — dix architectures |
| Vérifier que je ne tombe pas dans un piège | **G** — pièges de lecture |
| Savoir ce qui n'est jamais dessiné | **H** — liste de contrôle |
| Placer un dispositif | **I** — les cinq actions |
| Concevoir et écrire mes compromis | **J** — grille de conception |
| Relier ce cours aux autres volumes | **K** — raccordement |
| Une liste à cocher | **L** — checklists |

---

## Annexe A — Glossaire

**Actif éphémère** — Composant dont la durée de vie est inférieure au cycle d'observation. §41
**Adresse** — Identifiant d'une machine sur le réseau. **Elle change, elle est réattribuée, et derrière une traduction elle n'identifie pas l'origine.** §P.2, §P.4
**Active Directory** — Implémentation de référence d'un service d'annuaire en entreprise. **Ce cours l'utilise pour rendre le concept concret ; ses propriétés ne sont pas celles de tous les services d'identité.** §16
**Double pile** — Coexistence des deux familles d'adressage sur une même machine. **Deux chemins possibles, deux jeux de règles.** §P.5
**Annuaire** — Composant détenant identités, groupes et règles. Répond à *qui es-tu* et *à quoi as-tu droit*. §16
**Arbitrage** — Choix entre deux contraintes contradictoires. **Toute architecture en est faite.** §1.4
**Bordure** — Zone de contact avec l'extérieur : pare-feu, accès distant. §5.2
**Chemin d'administration** — Voie par laquelle on pilote un système. **Plus puissante que ce qu'elle administre.** §27
**Compromis** — Arbitrage assumé et **écrit**. S'il n'est pas écrit, il est subi. §46.5
**Contrainte** — L'une des six forces qui produisent une architecture : disponibilité, performance, coût, sécurité, conformité, **histoire**. §1.4
**Dégradation** — État où le service fonctionne partiellement. À distinguer de l'arrêt et de la cécité. §35.4
**Flux de dépendance** — Ce sans quoi un service **ne peut pas s'établir**. Rarement dessiné. principe des trois flux
**Flux d'exploitation** — Ce qui permet de tenir, observer, restaurer. Sa rupture **rend aveugle sans arrêter**. principe des trois flux
**Flux métier** — Ce que le service transporte ou traite. Le seul généralement dessiné. principe des trois flux
**Frontière** — Ce qu'il faut traverser pour passer d'une zone à une autre. **Une frontière déclarative n'en est pas une.** §5.3
**Kerberos** — Protocole d'authentification employé dans un domaine Active Directory. **À ne pas confondre avec LDAP, qui interroge l'annuaire sans assurer l'authentification.** §16
**Mandataire inverse** — Reçoit de l'extérieur à la place des serveurs internes. **Voit le contenu si le chiffrement y est terminé — modes B et C du §12.**
**Masque de sous-réseau** — Ce qui définit jusqu'où s'étend « à côté ». §P.2
**Passerelle par défaut** — Où une machine envoie ce qui n'est pas dans son sous-réseau. **Sans elle, elle ne sort pas de son segment.** §P.2
**Mandataire sortant** — Concentre les accès internes vers l'extérieur. Fonction opposée du précédent. §11
**Point de rupture** — Ce qui, en tombant, arrête un service. **La notion la plus utile du cours.** §2.2
**Répartiteur de charge** — Distribue entre plusieurs exemplaires. **Crée un point de rupture en en résolvant un.** §13
**Résolution de noms** — Traduit un nom en adresse. **Sa panne est la plus déroutante d'un système d'information.** §14
**Réplication** — Copie continue vers un autre stockage. **Protège de la panne, pas de la suppression : celle-ci est répliquée aussi.** §23.4
**Sauvegarde** — Copie **indépendante**, sur un autre support. **La seule des trois qui protège de tout — si elle a été testée.** §23.4
**Instantané** — État figé à un instant, **sur le même stockage**. Protège d'une erreur récente, pas de la perte du stockage. §23.4
**Stockage bloc / fichier / objet** — Trois façons d'exposer du stockage : un disque · un dossier partagé · une adresse à appeler. §23.4
**RPO** — Objectif de perte de données, exprimé en temps. *Combien de minutes de données accepte-t-on de perdre ?* §46.3
**RTO** — Objectif de délai de reprise. *Sous combien de temps vise-t-on la restauration ?* **À ne pas confondre avec la tolérance métier maximale, qui est une contrainte, ni avec le délai réel, qui se mesure.** §46.3
**Courtier de messages** — Composant qui porte des messages entre un producteur et un consommateur. **Découple leur disponibilité, et devient le point dont tout dépend.** §42.4
**File d'échecs** — Où finissent les messages qu'un consommateur n'arrive jamais à traiter. **Personne ne la regarde.** §42.4
**Idempotence** — Propriété d'une opération qu'on peut rejouer sans changer le résultat. **Indispensable dès qu'un message peut être livré deux fois.** §42.4
**Overlay / underlay** — Réseau logique construit au-dessus d'un réseau physique IP. **Le schéma logique et le schéma physique divergent alors radicalement.** §24.3
**Passerelle d'interconnexion** — **L'ensemble des composants et fonctions** par lesquels deux zones de confiance distinctes sont autorisées à échanger. Ce n'est pas un équipement. §25.5
**Quorum** — Mécanisme par lequel un ensemble distribué décide **quelle partie a le droit de continuer** quand ses membres ne communiquent plus. §23.5
**Split-brain** — Situation où deux parties d'un même système, séparées, continuent chacune de leur côté avec des vérités divergentes. §23.5
**Sens d'établissement** — Qui a initié une connexion. **L'information la plus déterminante d'un flux, et la plus souvent absente des schémas.** §P.3
**Sédimentation** — Empilement de décisions prises à des époques différentes. **L'état normal de tout système en service.** Ch. 4
**Segment** — Ensemble de machines qui se joignent directement, sans traverser d'équipement de routage. **Les y placer ne crée pas entre elles la frontière de filtrage inter-segments visible sur le schéma ; leur isolation éventuelle est à chercher ailleurs.** §24.1
**Service** — Ce qui produit une valeur pour l'organisation. Ne correspond à aucun composant. §35.1
**Strate** — Couche historique d'une architecture, reconnaissable à ses conventions et ses technologies. §4.2
**Terminaison du chiffrement** — Point où un flux chiffré est ouvert. **Détermine qui voit le contenu en clair.** Trois modes, §12
**Traduction d'adresses** — Mécanisme qui remplace une adresse au passage. **L'adresse observée n'est alors pas celle de l'origine.** §P.4
**Vue** — Représentation partielle d'un système : physique, logique, flux, service. **Aucune ne ment.** §3.3
**Zone** — Regroupement de segments partageant un niveau de confiance. Six de référence. §5.2
**Zone démilitarisée** — Ce qui doit être joignable de l'extérieur, **en supposant que ce sera compromis**. Définie par sa **seconde** frontière. §25

---

## Annexe B — Fiches composants

*Format uniforme : rôle · s'il disparaît · effet sur la donnée · reconnaissance · contrainte et coût.*

| Composant | S'il disparaît | Délai | Compréhensible ? |
|---|---|---|---|
| **Commutateur** | Un segment entier | Immédiat | ✅ |
| **Routeur** | Les échanges entre segments | Immédiat | ⚠️ |
| **Pare-feu** | Tout ce qui traverse · **ou rien, s'il est contourné** | Immédiat | ⚠️ |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ |
| **Répartiteur** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ |
| **Résolution de noms** | Presque tout | **Différé — caches** | ❌ |
| **Attribution d'adresses** | Les machines une par une | **Différé, jours** | ❌ |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé, mois** | ❌ |
| **Serveur web** | Rien si redondé | Immédiat | ✅ |
| **Applicatif** | Le service · le site s'affiche, rien ne marche | Immédiat | ⚠️ |
| **Base de données** | Tout ce qui en dépend · **perte possiblement définitive** | Immédiat | ⚠️ |
| **Serveur de fichiers** | Le travail, pas toujours le service | Immédiat | ✅ |
| **Messagerie** | Les courriels · **et la réinitialisation des mots de passe** | Immédiat puis différé | ⚠️ |
| **Hôte de virtualisation** | Ses machines | Immédiat | ⚠️ |
| **Stockage partagé** | **Toute la plateforme** | Immédiat | ⚠️ |
| **Stockage objet** | Ce qui l'appelle | Immédiat | ⚠️ — **joignable par clé, pas par le réseau** |
| **Plan de gestion** | Rien · **on ne peut plus rien administrer** | Immédiat | ❌ |

⚠️ **Les six lignes marquées ❌ sont les six composants dont la panne est incompréhensible.** Cinq d'entre eux ne sont jamais dessinés.

---

## Annexe B bis — Index des notions à reconnaître

> **Les vingt-deux technologies que vous rencontrerez sans avoir à les maîtriser.** Chacune est traitée là où elle devient naturelle, jamais en catalogue.

| Notion | Ce qu'il faut en retenir en une ligne | Où |
|---|---|---|
| **BGP** | Les politiques comptent autant que la distance · le chemin dépend de ce que d'autres annoncent | §9.2 |
| **MPLS** | Un réseau privé d'opérateur **n'est pas un chiffrement** | §26.3 |
| **SD-WAN** | Pas un nouveau câble : une couche de pilotage · **le chemin devient dynamique** | §26.3 |
| **VXLAN / EVPN** | Réseau logique au-dessus du physique · **étendre un segment étend la propagation** | §24.3 |
| **WAF** | Le seul des trois qui juge **le contenu** d'une requête web | §12.3 |
| **CDN** | Le chiffrement est terminé chez un tiers · **une page personnalisée en cache est servie à un autre** | §12.3 |
| **Passerelle d'interfaces** | Une façade **avec une politique**, pas un mandataire moderne | §42.3 |
| **Maillage de services** | Tous les environnements de microservices n'en ont pas besoin | §41.4 |
| **HSM** | La clé peut être **utilisée sans être exportée** | §17.3 |
| **PAM** | Transforme un état permanent en **événement daté et motivé** · attention au compte de secours | §27.3 |
| **NAC** | Place le terminal **dans un segment selon ce qu'il est** · que fait-on s'il tombe ? | §24.4 |
| **SASE / SSE / CASB** | Des familles de capacités, **pas des implémentations identiques** | §39.4 |
| **VDI** | *Où s'exécute réellement l'application ?* · une panne réseau **arrête** le travail | §23.3 |
| **Hyperconvergence** | La simplification physique **déplace la complexité dans le logiciel** | §23.3 |
| **Réseau de stockage dédié** | Une infrastructure entière absente de tous les schémas logiques | §23.5 |
| **Immutabilité** | Protège une copie existante · **n'empêche pas de cesser d'en créer** | §23.5 |
| **Quorum** | Un membre sain peut devoir **s'arrêter faute de majorité** · deux nœuds ne suffisent pas | §23.5 |
| **Consensus distribué** | La forte cohérence se paie en disponibilité ou en performance | §42.3 |
| **Mainframe** | **Ancien ne veut dire ni inutile, ni non critique** | §4.2 |
| **Calcul intensif** | Une zone aux priorités inversées, comme l'industriel | §5.4 |

⚠️ **Le contrat, rappelé** : ces vingt-deux notions relèvent du niveau 🔭. **On attend de vous que vous sachiez ce qu'elles impliquent, et quelle question poser — pas que vous sachiez les configurer.**

---

## Annexe C — La grille en sept passes

```
①  ZONES        Combien ? Qu'est-ce qui matérialise chaque frontière ?
                Y a-t-il une seconde frontière après la DMZ ?
                Un composant est-il à cheval ?

②  ENTRÉE       Utilisateur externe : par où ?
                Utilisateur interne : par où ? (souvent plus court)
                Administrateur : par où ? (jamais dessiné)

③  DONNÉES      Où sont-elles ? En combien d'endroits existent-elles ?
                Réplicas · sauvegardes · recette · exports · rapports

④  IDENTITÉ     Contre quoi s'authentifie-t-on ?
                Combien de fois sur un parcours ?
                Que se passe-t-il si ce composant tombe ?

⑤  FLUX         Quel chemin suit une requête, en douze étapes ?
                Quelle famille pour chaque flux ?

⑥  RUPTURES     Quels composants sont uniques ?
                Les exemplaires sont-ils sur des hôtes différents ?
                Le basculement a-t-il été testé ?
                Où sont les sessions ?

⑦  INVISIBLE    Les onze éléments de l'annexe H
```

**Rendu attendu** : une page, se terminant par **trois questions, pas un jugement**.
**Durée réelle** : 1 h pour une architecture simple, une demi-journée pour un système réel.

---

## Annexe D — Conventions de schéma

| Convention | Signification habituelle | Fiabilité |
|---|---|---|
| Position haute | Extérieur, Internet | Élevée |
| Position basse | Données | Élevée |
| Nuage | Ce qu'on ne maîtrise ou ne détaille pas | Élevée |
| Boîtes empilées | Plusieurs exemplaires | Moyenne |
| Trait pointillé | Flux logique, relation, lien non permanent | **Faible** |
| Double ligne | Redondance ou haut débit | **Faible** |
| Composant à cheval | Traverse une frontière — **toujours à interroger** | Élevée |

⚠️ **Aucune convention n'est normalisée.** Première question devant un schéma inconnu : *y a-t-il une légende ?*

**Ce qu'une boîte peut représenter** : machine · rôle · groupe · service · fournisseur externe. §3.1
**Ce qu'un trait peut représenter** : câble · flux · relation logique · adjacence · **rien de précis**. §3.2

---

## Annexe E — Catalogue des schémas

| # | Schéma | Chapitre |
|---|---|---|
| 1.1 | HELIOMED, vue d'ensemble | §1.1 |
| 1.2 | Les quatre questions du lecteur | §1.3 |
| 1.3 | Trois arbitrages, trois architectures | §1.4 |
| 3.1 | Le même système, quatre vues | §3.3 |
| 4.1 | Les strates d'un système d'information | §4.2 |
| 5.1 | Les six zones | §5.2 |
| 6.1 | Ce qu'un poste atteint | §6.2 |
| 6.2 | Les deux chemins d'un poste nomade | §6.3 |
| 10.1 | Ce que le suivi d'état change | §10.2 |
| P.1 | La décision que prend toute machine | §P.2 |
| P.2 | Les deux traductions d'adresses | §P.4 |
| 12.1 | Ce que le mandataire inverse change | §12 |
| 12.2 | Les trois modes de terminaison du chiffrement | §12 |
| 14.1 | La place réelle de la résolution de noms | §14 |
| 20.1 | Pourquoi la base est au fond | §20 |
| 23.1 | La redondance qui n'en est pas | §23.3 |
| 23.2 | Bloc, fichier, objet · quatre architectures de stockage | §23.4 |
| 25.1 | Les deux frontières d'une DMZ | §25.1 |
| 27.1 | Le chemin d'administration | §27.2 |
| 28.1 | Les trois modèles de frontière industrielle | §28.3 |
| 29.1 | Une requête, de bout en bout | §29.1 |
| 29.2 | Quatre chemins vers le même service | §29.3 |
| 30.1 | La cascade d'une panne d'annuaire | §30.2 |
| 31.1 | Où vit la session | §31.2 |
| 32.1 | Une donnée, de la saisie à l'oubli | §32.1 |
| 35.1 | L'arbre de dépendance d'un service | §35.2 |
| 35.2 | Dix flux superposés sur un même service | §35.3 |
| 36.1 | Les sept passes | §36.1 |
| 38.1 | Les trois façons de dessiner un tiers | §38.2 |
| 39.1 | Où passe la frontière de responsabilité | §39.2 |
| 40.1 | Les trois liens d'une architecture hybride | §40.2 |
| 41.1 | Deux façons de dessiner un cluster | §41.2 |
| 43.1 | Les cinq actions | §43.1 |
| 46.1 | Lire et concevoir | §46.1 |

---

## Annexe F — Les dix architectures

| # | Architecture | Ce qu'elle enseigne | Où |
|---|---|---|---|
| 1 | Application interne, trois composants | Une architecture proportionnée · l'authentification non représentée | §37.1 |
| 2 | Site web public | Qui voit le contenu en clair · la frontière 2 | §37.2 |
| 3 | Trois niveaux, redondance partielle | **La rupture de symétrie est une information** | §37.3 |
| 4 | Système hérité mal documenté | Trois signes convergents d'une strate ancienne | §37.4 |
| 5 | Haute disponibilité complète | Le coût de la symétrie · ce qu'elle ne couvre pas | Cas B |
| 6 | Multi-sites | L'autonomie locale et ses trois dépendances | §26.2 |
| 7 | Hybride | Le lien d'identités, point de fragilité récurrent | §40 |
| 8 | Industrielle | L'inversion des priorités | §28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation | Cas A |
| 10 | HELIOMED complet | La synthèse du fil rouge | §1.1 + ajouts §50.6 |

---

## Annexe G — Pièges de lecture

| # | Piège | Détection |
|---|---|---|
| 1 | Lire un **rôle** comme une machine | *Combien y en a-t-il réellement ?* |
| 2 | Croire qu'un **trait** signifie une autorisation | *Est-ce permis, ou seulement possible ?* |
| 3 | Confondre **mandataire sortant et inverse** | *Pour entrer, ou pour sortir ?* |
| 4 | Prendre une **frontière déclarative** pour une frontière | *Qu'est-ce qui empêche de passer ?* |
| 5 | Oublier la **seconde frontière** d'une DMZ | Elle n'est presque jamais dessinée |
| 6 | Croire une **redondance** dessinée | *Sur des hôtes différents ? Le basculement est-il testé ?* |
| 7 | Oublier que la **session** peut annuler la redondance | *Où vit la session ?* |
| 8 | Ne pas voir les composants **reliés à rien** | Annuaire, résolution : tout s'y connecte |
| 9 | Chercher une panne parmi les **composants dessinés** | Sept étapes sur douze sont invisibles |
| 10 | Juger une anomalie sans demander sa **date** | Chaque anomalie a une histoire |
| 11 | Déduire une architecture de la **taille** | *Principe de la contrainte* |
| 12 | Oublier le **poste utilisateur** | La majorité des flux et des incidents |
| 13 | Oublier le **prestataire** | Dessiné en nuage, présent au cœur de l'administration |
| 14 | Croire qu'un **service en ligne** se sécurise comme le reste | Les cinq actions ne s'appliquent pas à son infrastructure — elles se déplacent — §42.5 |
| 15 | Lire un **cluster** par ses instances | Quatre éléments : entrée, services, état, plan de contrôle |
| 16 | Placer un dispositif au **périmètre** en croyant tout couvrir | Il ne voit pas l'interne |
| 17 | Proposer **dix améliorations** | Une seule sera peut-être faite |
| 18 | Croire un schéma **à jour** | Datez-le |
| 19 | Prendre une **identification** pour une certitude | *Principe d'hypothèse* — port et position font un faisceau, pas une preuve |
| 20 | Conclure à une **redondance** parce qu'elle est dessinée | *Principe de preuve* — hôte, stockage, site, alimentation partagés ? |
| 21 | Croire qu'un mandataire inverse **voit toujours le contenu** | Trois modes de terminaison — §12 |
| 22 | Confondre **LDAP et authentification** | LDAP interroge · d'autres mécanismes authentifient — §16 |
| 23 | Croire qu'un **certificat chiffre** | Il lie une identité à une clé ; le protocole chiffre — §17 |
| 24 | Prendre une **adresse dans un journal** pour l'origine | Traduction d'adresses, mandataires — §P.4, §34.1 |
| 25 | Supposer que le modèle **IPv4 + traduction** est universel | §P.5 |
| 26 | Croire que **la base est la donnée** | Elle en porte une partie — §20, §32.2 |
| 27 | Croire qu'un **jeton autoporté ne peut pas être révoqué** | C'est un compromis de coût et de délai — §31.2 |
| 28 | Confondre **réplication et sauvegarde** | La réplication copie aussi les suppressions — §23.4 |
| 29 | Confondre **instantané et sauvegarde** | L'instantané vit sur le même stockage — §23.4 |
| 30 | Oublier le **stockage objet** parce qu'il n'a pas de lien réseau | Il est joignable par clé, depuis n'importe où — §23.4 |
| 31 | Croire que sur un service en ligne **on ne peut rien faire** | Les actions se déplacent vers la configuration et les identités — §42.6 |
| 32 | Croire que deux **réseaux sans fil annoncés** sont deux segments | Annoncé ≠ segmenté — §24.4 |
| 33 | Oublier que le **sans-fil contourne le périmètre physique** | Mode A : la clé donne l'accès interne — §24.4 |
| 34 | Croire qu'une **file asynchrone** protège de tout | Elle déplace la panne : accumulation silencieuse — §42.4 |
| 35 | Ne pas rendre un **consommateur idempotent** | Au moins une livraison ≠ exactement une — §42.4 |
| 36 | Confondre **tolérance métier, RTO visé et délai réel** | Trois choses différentes — §46.3 |
| 37 | Transposer un **ratio d'exploitation** d'un corrigé | Ce sont des données de scénario — §48.0 |

---

## Annexe H — Ce qui n'est jamais dessiné

**Liste de contrôle. À passer sur tout schéma, systématiquement.**

☐ **Résolution de noms** — sa panne arrête presque tout, de façon différée
☐ **Annuaire** — dessiné parfois, relié jamais
☐ **Synchronisation d'horloge** — sa dérive produit des rejets d'authentification
☐ **Chemins d'administration** — le chemin le plus court vers la compromission totale
☐ **Postes de travail** — la majorité des flux et des incidents
☐ **Postes de prestataires** — hors inventaire, avec des droits d'administration
☐ **Sauvegardes et leur chemin** — le serveur est parfois dessiné, jamais son chemin
☐ **Services en ligne** — pas chez vous, donc absents
☐ **Liens partenaires** — anciens, oubliés
☐ **Certificats et leur autorité** — invisibles tant qu'ils fonctionnent
☐ **Environnements de recette** — données de production, protections moindres
☐ **Collecte de journaux** — flux d'exploitation
☐ **Versions** — impossible de raisonner l'obsolescence sans elles
☐ **Le temps** — un schéma est un instantané, sans histoire ni migration en cours

⚠️ **Dessinez-les tous sur votre schéma : la page devient illisible en quatre minutes.** C'est pourquoi ils n'y sont pas — et pourquoi il faut savoir qu'ils existent.

---

## Annexe I — Les cinq actions et leurs emplacements

| Action | Possible | **Impossible** |
|---|---|---|
| **Observer** | Pare-feu · mandataires · commutateurs · postes · serveurs | Flux chiffré non terminé · **chez un tiers** |
| **Filtrer** | Pare-feu · mandataires · entre segments | **Dans un segment** · chez un tiers |
| **Authentifier** | Mandataire inverse · applicatif · annuaire · accès distant | Entre serveurs se faisant confiance par adresse |
| **Segmenter** | Entre zones · entre segments · au poste | **Dans un segment**, sans mesure explicite |
| **Journaliser** | Tout composant traversé | Ce qui ne traverse aucun composant journalisant |

**Les deux points les plus riches** :

| Point | Ce qu'il apporte | Sa limite |
|---|---|---|
| **Mandataire inverse** | Voit tout le trafic externe **en clair** · filtre · authentifie · journalise | **Ne voit que l'externe** |
| **Applicatif** | Le seul qui connaisse **l'utilisateur réel et l'action métier** | Reçoit rarement les moyens |

**Face à un emplacement impossible** : on **déplace**, on **remplace**, ou on **déclare non couvert**. Jamais on ne fait semblant.

⚠️ **Sur un service en ligne** : les cinq actions ne s'appliquent pas à son infrastructure, **et elles se déplacent** vers la configuration, les identités, les données et les journaux exposés — §42.5. **« Impossible » y signifie « pas sur ses couches internes », pas « rien à faire ».**

---

## Annexe J — Grille de conception et registre des compromis

### J.1 Fiche de contraintes

```
SERVICE         .................................
UTILISATEURS    Combien : ......  Où : ......  Quand : ......
DONNÉES         Nature : ......  Sensibilité : ......
DISPONIBILITÉ   Interruption tolérable : ......
                Perte de données tolérable : ......
PERFORMANCE     Temps de réponse : ......  Volume : ......
COÛT            Investissement : ......  Récurrent : ......
                EXPLOITANTS DISPONIBLES : ......   ← la ligne décisive
SÉCURITÉ        Exposition nécessaire : ......
CONFORMITÉ      Obligations : ......  Preuve à produire : ......
HISTOIRE        Existant à intégrer : ......
                Ce qu'on ne peut pas changer : ......
```

⚠️ **La ligne « exploitants disponibles » est celle qui explique le plus d'échecs.** §47.3

### J.2 Registre des compromis

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | **Revoir si** |
|---|---|---|---|---|---|---|

**C'est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**.

### J.3 Ce qui reste à vérifier

| # | À vérifier | Pourquoi | Qui | Avant quand |
|---|---|---|---|---|

**Une proposition sans cette section est un engagement déguisé.**

### J.4 Grille de critique en six points

```
① POINT FORT          Ce qui est bien pensé, et pourquoi     ← toujours en premier
② POINT FAIBLE        Ce qui est fragile, sous quelle condition
③ POINT DE RUPTURE    Ce qui n'a pas de doublure
④ DÉPENDANCE CACHÉE   Ce dont tout dépend et qui n'est pas dessiné
⑤ RISQUE PRINCIPAL    Scénario le plus probable et le plus coûteux
⑥ AMÉLIORATION        UNE SEULE, avec son coût et son effet
```

**Format en cinq lignes** : ce qui fonctionne · ce que j'ai observé · **ce que je n'ai pas su** · le risque · ce que je propose.

---

## Annexe K — Raccordement aux autres volumes

| Ce que l'architecture détermine | Volume concerné | Chapitre |
|---|---|---|
| **L'interruptibilité** — un composant qui ne peut s'arrêter ne sera pas corrigé | Maintien en condition de sécurité | §45.1 |
| **Les fenêtres de maintenance** | MCS | §45.1 |
| **Ce qui est découvrable** — un actif derrière un filtre est invisible au scanner | Asset Management | §45.2 |
| **Les actifs éphémères** | Asset Management | §41 |
| **Les points de passage** — les seuls endroits où observer | Détection et journalisation | §45.3 |
| **La perte d'identité en chemin** | Détection | §34.1 |
| **La rétention des journaux** | Détection · Réponse à incident | §34.2 |
| **Ce qu'on peut isoler** | Réponse à incident | §45.4 |
| **Si l'on peut encore administrer un système compromis** | Réponse à incident | §45.4 |
| **Les chemins d'administration** | Identités et accès | §27 |
| **La fédération et ses dépendances** | Identités et accès | §30.3 |
| **L'exposition d'un composant** | Industrialiser la remédiation | §45.1 |

**Les huit volumes et leurs limites fondamentales** :

| Volume | Limite |
|---|---|
| **Architecture des SI** | **Toute architecture est un compromis sédimenté** |
| Asset Management | La représentation n'est jamais le système |
| Cyber Threat Intelligence | L'incertitude ne se supprime pas |
| Maintien en condition de sécurité | Le système change avec le temps |
| Détection et journalisation | On ne voit que là où l'on regarde |
| Industrialiser la remédiation | La capacité est finie, le flux ne l'est pas |
| Réponse à incident | On décide sans savoir |
| Identités et accès | Les droits s'accumulent, ils ne se réduisent jamais seuls |

---

## Annexe L — Checklists

### L.1 — Devant un schéma inconnu
☐ Y a-t-il une légende ? · ☐ De quand date-t-il ? · ☐ **Pour qui a-t-il été fait ?** · ☐ Quelle vue est-ce ? · ☐ Que représente une boîte ici ? · ☐ Que représente un trait ?

### L.5 — Avant de conclure à un point de rupture
☐ Est-ce un rôle ou une machine ? · ☐ Combien d'exemplaires réels ? · ☐ Sur des hôtes différents ? · ☐ **Même stockage, même site, même alimentation ?** · ☐ **Le basculement a-t-il été testé, et quand ?** · ☐ Où vivent les sessions ?

### L.2 — Avant de croire à une sauvegarde
☐ Est-ce une réplication, un instantané ou une sauvegarde ? · ☐ **Sur quel stockage vit-elle ?** · ☐ Un compte d'exploitation compromis peut-il la supprimer ? · ☐ **Quand a-t-elle été restaurée pour de vrai ?**

### L.3 — Avant de croire à une séparation sans fil
☐ Combien de réseaux annoncés ? · ☐ **Chacun aboutit-il dans un segment distinct ?** · ☐ Qu'est-ce qui filtre entre eux ? · ☐ Le réseau entreprise aboutit-il dans le segment interne ? · ☐ **Contre quoi authentifie-t-on, et que se passe-t-il si ce service tombe ?**

### L.4 — Avant de croire à un découplage asynchrone
☐ Que se passe-t-il si le consommateur est arrêté ? · ☐ **Qui supervise la taille de la file et l'âge du plus ancien message ?** · ☐ Le consommateur est-il idempotent ? · ☐ **Qui regarde la file d'échecs ?** · ☐ Les messages en attente sont-ils persistés ?

### L.6 — Avant d'affirmer le rôle d'un composant
☐ Sur quel faisceau — port, position, connexions ? · ☐ **Le port peut-il être non standard ?** · ☐ Le composant cumule-t-il deux rôles ? · ☐ **Qu'est-ce qui confirmerait ?** · ☐ Ai-je écrit « probablement » plutôt qu'une affirmation ?

### L.7 — Avant de critiquer
☐ Ai-je demandé la date ? · ☐ Ai-je demandé le motif ? · ☐ Ai-je commencé par un point fort ? · ☐ **Ai-je une seule recommandation ?** · ☐ Ai-je chiffré son coût ?

### L.8 — Avant de concevoir
☐ Le service est-il formulé côté métier ? · ☐ L'interruption tolérable est-elle **chiffrée** ? · ☐ La perte de données tolérable est-elle chiffrée ? · ☐ **Combien d'exploitants disponibles ?** · ☐ Qu'accepte-t-on de perdre ? · ☐ Ai-je envisagé de renoncer à une fonctionnalité ?

### L.9 — Avant de livrer une conception
☐ Registre des compromis écrit ? · ☐ Conditions de réexamen ? · ☐ Ce qui reste à vérifier ? · ☐ L'architecture est-elle exploitable par l'organisation telle qu'elle est ?

### L.10 — Avant de placer un dispositif
☐ Que voit-il depuis cet emplacement ? · ☐ **Que ne voit-il pas ?** · ☐ Quelle proportion des flux y passe ? · ☐ Est-ce le point le plus riche disponible ? · ☐ Que déclare-t-on non couvert ?

---

## Journal des modifications

| Version | Date | Nature |
|---|---|---|
| 1.0 | 02/08/2026 | Première rédaction : 9 parties, 50 chapitres, 3 cas de synthèse, 14 mini-labs, 12 annexes, 26 schémas |
| 1.8 | 02/08/2026 | **Couche de culture architecturale.** Ajout de **trois niveaux de lecture explicites** — 🧠 à maîtriser · 🔭 à reconnaître · 📚 à approfondir — pour éviter qu'un lecteur ne mémorise vingt-deux acronymes au même rang que les notions fondamentales. **Vingt-deux blocs 🔭 À RECONNAÎTRE**, dispersés là où chaque notion devient naturelle et jamais en catalogue de fin d'ouvrage, chacun répondant à six questions : ce que c'est · le problème résolu · où on le rencontre · l'effet sur les flux et dépendances · le coût introduit · **ce qu'il faut demander en réunion**. Répartition : BGP (§9.2) · MPLS et SD-WAN (§26.3) · VXLAN et EVPN (§24.3) · WAF et CDN (§12.3) · passerelle d'interconnexion (§25.5) · HSM (§17.3) · PAM (§27.3) · NAC (§24.4) · SASE, SSE et CASB (§39.4) · VDI et hyperconvergence (§23.3) · réseau de stockage dédié, immutabilité et quorum (§23.5) · maillage de services (§41.4) · passerelle d'interfaces et consensus distribué (§42.3) · mainframe (§4.2) · calcul intensif (§5.4). **Index en annexe B bis.** Deux notions traitées avec une prudence particulière : les sigles de marché — *ils décrivent des familles de capacités, pas des implémentations identiques* — et la passerelle d'interconnexion, présentée comme **une fonction architecturale et non un équipement**, avec le principe qui la fonde : *relier deux réseaux ne signifie pas qu'ils doivent devenir un seul périmètre de confiance*. |
| 1.7 | 02/08/2026 | **Version de stabilisation. Contenu gelé.** ① **Numérotations corrigées** : sections 35.4 et 45.5 dupliquées · **annexe L normalisée en L.1 à L.10**. ② **Absolus résiduels** repris : dix-sept classements empiriques non démontrés reformulés — *la plus fréquente* devient *très répandue* ou *courante*, selon le cas. ③ **Responsabilité cloud harmonisée** : les données et les accès ne « ne bougent jamais » plus — ils **restent des responsabilités à gouverner, même lorsque leur mise en œuvre est partagée avec le fournisseur**. ④ **Chapitre 34 corrigé** : la journalisation ne suit plus *exactement les points de passage* mais **les points en position de savoir** — un composant peut être sur un chemin, ou à l'origine d'une décision sans qu'aucun flux ne le traverse. ⑤ **Renvois internes vérifiés** : 165 renvois contrôlés · **deux épisodes du fil rouge, perdus lors des réécritures des chapitres 5 et 6, ont été restaurés** — les six zones et les 620 postes invisibles. ⑥ **Catalogue des schémas complété** : les 4 schémas ajoutés en densification y figurent. ⑦ **Légende des blocs complétée** : les cinq blocs récurrents non documentés y sont. ⑧ **Les huit règles éditoriales sont devenues des principes nommés** — trois flux, contrainte, coupe, coût, visuel, modèle, hypothèse, **preuve** — et les références nues *R7*, *R8* du corps du texte ont été remplacées par leur nom. |
| 1.6 | 02/08/2026 | **Passe éditoriale finale.** **Superlatifs** : dix-neuf formulations qui prétendaient à une fréquence factuelle sans données ont été ramenées à des constats hedgés — *la voie d'entrée la plus fréquente* devient *une voie d'entrée majeure*, *l'état le plus fréquent* devient *un état très répandu*, *la base est toujours au fond* devient *dans le modèle à trois niveaux*. Les superlatifs exprimant un **jugement pédagogique assumé** — *le piège de lecture le plus fréquent du cours*, *la question la plus utile* — sont conservés : ils engagent l'auteur, pas une statistique. **Cohérence texte / corrigés** : avertissement ajouté en tête des barèmes des trois cas — ils notent des comportements, pas des réponses · une architecture différente du corrigé obtient le plein barème si l'arbitrage est écrit (§48.0) · une identification formulée avec certitude perd des points même si elle est juste *(principe d'hypothèse)* · rappel explicite dans le mini-lab 13 que la grille relève six points et n'en propose qu'un (§36.4, §49.3). |
| 1.5 | 02/08/2026 | **Comblement des trois manques de couverture.** **Accès sans fil** (§24.4) : le chemin poste → point d'accès → contrôleur → segment, la question *le sans-fil est-il un réseau distinct ou une autre porte sur le même segment ?*, les trois modes, réseaux multiples annoncés contre segments réels, clé partagée contre authentification individuelle. **Communication asynchrone** (§42.4) : file, courtier, publication/abonnement, journal d'événements · les cinq gains du découplage et **les sept problèmes qu'on achète** — accumulation, retard, doublons, ordre, rejeu, file d'échecs, observabilité · le courtier comme nouveau point de rupture · deux scénarios dont l'accumulation silencieuse. **RTO et RPO** (§46.3) : introduits en distinguant explicitement tolérance métier maximale, objectif de reprise et délai réel mesuré · traduction du RPO en décisions d'architecture. **Avertissement sur les chiffres d'exploitation** en tête du chapitre 48 : ce sont des données de scénario, pas des ratios transposables. Six pièges et deux checklists ajoutés. |
| 1.4 | 02/08/2026 | **Passe d'édition technique, après troisième revue.** Correction de **douze formulations erronées ou trop absolues** : erreur arithmétique sur la fréquence de sauvegarde (24 h → 8 h est une division par trois) · les trois sens du mot « expiration » en résolution de noms · un appel entre modules d'un monolithe **peut** échouer fonctionnellement, ce qui disparaît est la classe d'échec réseau · les transactions distribuées existent, avec leurs quatre approches et leur coût · la découverte de service n'est pas un remplacement du DNS, elle est souvent implémentée avec lui · sur un service en ligne les cinq actions **se déplacent** vers configuration, identités et données au lieu de disparaître · une action exige un **point d'observation ou de décision**, pas nécessairement un point de passage réseau · lenteur constante contre variable est un **indice**, pas une loi · un domaine d'annuaire fonctionne avec un seul contrôleur, deux étant recommandés · le comportement de vérification de révocation **varie fortement** selon les clients · une panne à horaire net **oriente** vers une échéance sans la prouver · le modèle de responsabilité cloud nuancé : *responsable* ne signifie pas *maître de tous les réglages*. **Ajout du stockage d'infrastructure** (§23.4) : bloc, fichier et objet · quatre architectures · et surtout la distinction **réplication / instantané / sauvegarde**, avec ce que chacune ne protège pas. Quatre pièges et une checklist ajoutés. |
| 1.3 | 02/08/2026 | **Achèvement de la densification.** 75 500 → 76 000 mots. Chapitres restés à moitié traités repris au même format : zones et frontières (§5), poste utilisateur avec les deux chemins d'un nomade (§6), segmentation avec son coût chiffré et l'angle mort des flux périodiques (§24), cycle de la donnée et calcul du nombre réel de copies (§32), placement d'une même sonde à trois endroits (§44), et **lecture entièrement déroulée des sept passes** sur le schéma d'HELIOMED, à la première personne (§36.3). Ajout du tableau de synthèse du chapitre 45 : cinq décisions d'architecture, cinq conséquences des années plus tard, aucune rattrapable par un produit ou un budget. **Totaux : 38 scénarios de panne · 34 tableaux de vocabulaire de réunion · 33 schémas.** |
| 1.2 | 02/08/2026 | **Passe de densification, après seconde revue externe.** +17 500 mots, placés uniquement là où le raisonnement manquait — aucune définition ajoutée. **Partie II entièrement réécrite** : chaque composant gagne son mécanisme interne « juste assez pour raisonner », des architectures comparatives, un scénario de panne au format *symptôme / hypothèse naïve / dépendance réelle / ce que le schéma aurait dû montrer*, et un tableau **vocabulaire de réunion** avec ce qu'il faut vérifier avant de croire une affirmation. **Parties III, IV et V densifiées** de la même façon. Ajouts structurants : les **quatre chemins vers un même service** (§29.3) · la **superposition de dix flux** sur un service unique, dont trois seulement sont dessinés (§35.3) · les **six comparaisons cloud** avec la grille *je n'exploite plus / je conçois toujours / quelle dépendance ai-je achetée* (§39.4) · le **lien de synchronisation d'identités** comme composant critique invisible (§40.3) · **deux mauvaises architectures**, l'insuffisante et l'excessive (§37.5) · et le **capstone de conception itérative** en cinq événements, où la capacité d'exploitation arrive en dernier et remet tout en cause (§48.5). Dix-huit scénarios de panne ajoutés. Vingt-quatre tableaux de vocabulaire de réunion. |
| 1.1 | 02/08/2026 | **Passe de précision technique, après revue externe.** Trois règles nouvelles : **R6** un modèle pédagogique n'est pas une loi technique · **R7** une observation produit une hypothèse, pas une identification · **R8** un schéma révèle une intention de redondance, seul un test établit une capacité. Ajout d'un **préambule « socle réseau minimal »** — deux niveaux d'adressage, sous-réseau, passerelle, sens d'établissement, traduction d'adresses, deux familles d'adressage. Ajout du **schéma des trois modes de terminaison du chiffrement**. Correction de treize formulations absolues devenues fausses hors de leur modèle : dépendance à la résolution de noms · service d'annuaire contre Active Directory · LDAP contre authentification · rôle exact d'un certificat · portée d'une autorité privée · ce qu'un commutateur et un routeur interprètent · isolation à l'intérieur d'un segment · terminaison du chiffrement · effet d'une panne de base · absence d'état d'un serveur web · révocation d'un jeton autoporté · chemin de retour d'une requête · correspondance entre familles de flux et niveaux de dégradation. **Mini-labs d'identification transformés en labs d'hypothèses.** Ajout du vocabulaire des **exigences non fonctionnelles**, du réflexe **logique contre physique**, de trois blocs **« le même composant, plusieurs placements »**, et du déroulé de conception en dix étapes avec autocritique. Passe anti-superlatifs et anti-fausse-précision. Deux principes de doctrine ajoutés. Neuf pièges ajoutés à l'annexe G. |

**Les huit principes appliqués** : R1 trois flux · R2 contrainte · R3 coupe · R4 coût · R5 visuel · R6 modèle · R7 hypothèse · R8 preuve.

**Prochaine revue recommandée** : février 2027. Ce cours contient peu de données périssables — c'est une conséquence du principe de coupe.

---

*Fin du document.*
