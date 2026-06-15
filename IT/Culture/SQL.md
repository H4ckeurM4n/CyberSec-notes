# SQL et bases de données relationnelles

## De zéro à l’interrogation de données — Guide pour débutant absolu

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais ouvert une base de données de sa vie.
> Tout ce dont tu as besoin, c’est un ordinateur (Windows, Mac ou Linux) et l’envie d’apprendre.

-----

## Ce que ce cours est — et ce qu’il n’est pas

Ce cours t’apprend à **comprendre et utiliser** une base de données relationnelle avec SQL.

Tu apprendras à :

- comprendre ce qu’est une base de données et pourquoi on en utilise
- lire les données d’une base avec `SELECT`
- filtrer, trier, limiter les résultats
- croiser plusieurs tables avec des jointures
- faire des statistiques (`COUNT`, `SUM`, `AVG`, `GROUP BY`)
- insérer, modifier, supprimer des données avec prudence
- créer une table simple avec ses contraintes
- comprendre les transactions et l’intégrité des données
- repérer et éviter les erreurs SQL fréquentes
- avoir les bases utiles pour le développement, la data, l’administration et la cybersécurité

Ce cours **n’est pas** :

- un cours d’administration de base de données (DBA)
- un cours de modélisation avancée (formes normales en profondeur, UML)
- un cours d’optimisation SQL (requêtes complexes, plans d’exécution avancés)
- un cours sur PostgreSQL, MySQL ou Oracle en profondeur
- un cours NoSQL (MongoDB, Redis, etc.)
- un cours offensif sur l’injection SQL (la sécurité est traitée en **défensif** uniquement)

-----

## Guide de lecture

|Section                   |Niveau           |Objectif                                           |
|--------------------------|-----------------|---------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel      |Ce qu’il faut retenir pour ne pas être perdu       |
|**Très utile en pratique**|🟡 Bon à connaître|Ce qui te rend opérationnel pour de vraies requêtes|
|**Bonus**                 |🔴 Avancé         |Pour aller plus loin — tu peux y revenir plus tard |

### Parcours recommandés

|Parcours                      |Chapitres         |Objectif                                                                      |
|------------------------------|------------------|------------------------------------------------------------------------------|
|**🎯 Découverte / entretien**  |Ch.1-19 + Ch.32   |Comprendre SQL, savoir lire et croiser des données, être crédible en entretien|
|**🔧 Opérationnel (data, dev)**|Ch.1-26 + Ch.31-32|Savoir aussi modifier et structurer des données                               |
|**🚀 Complet**                 |Tout              |Bonnes pratiques, index, sécurité, Python — pour le terrain                   |


> **Important :** la Partie VII (Ch.27-30) est marquée **Bonus / Pour aller plus loin**. Tu peux finir le cœur du cours (Ch.1-26 + Skills Assessment) sans elle. Ces chapitres viennent enrichir ta pratique, pas la conditionner.

-----

## Glossaire — Les mots à connaître

Reviens ici chaque fois qu’un terme te semble flou.

|Terme               |Définition simple                                                                              |
|--------------------|-----------------------------------------------------------------------------------------------|
|**Base de données** |Un système organisé de stockage et de gestion de données                                       |
|**SGBD**            |Système de Gestion de Base de Données — le moteur qui exécute SQL (SQLite, PostgreSQL, MySQL…) |
|**SQL**             |Le langage standard pour interroger et manipuler des bases de données relationnelles           |
|**Table**           |Un tableau de données — l’équivalent d’une feuille Excel structurée                            |
|**Ligne (row)**     |Un enregistrement dans une table (un livre, un lecteur, un emprunt)                            |
|**Colonne (column)**|Un champ dans une table (le titre d’un livre, la ville d’un lecteur)                           |
|**Schéma**          |La structure de la base : quelles tables, quelles colonnes, quels types                        |
|**Clé primaire**    |Une colonne qui identifie de manière unique chaque ligne d’une table                           |
|**Clé étrangère**   |Une colonne qui pointe vers la clé primaire d’une autre table — crée une relation              |
|**Relation**        |Le lien entre deux tables (un emprunt est lié à un lecteur et à un livre)                      |
|**Requête**         |Une instruction SQL qu’on envoie à la base (ex : `SELECT * FROM books`)                        |
|**NULL**            |L’absence de valeur (différent de zéro et de chaîne vide)                                      |
|**Jointure (JOIN)** |Une opération qui combine les données de plusieurs tables                                      |
|**Agrégation**      |Un calcul sur un groupe de lignes (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)                        |
|**Transaction**     |Un ensemble de modifications qu’on valide ou qu’on annule en bloc                              |
|**Index**           |Une structure qui accélère les recherches sur une colonne                                      |
|**Vue**             |Une requête enregistrée qu’on utilise comme une table                                          |
|**Contrainte**      |Une règle imposée à une colonne (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`)                 |
|**Dialecte SQL**    |Une variante de SQL propre à un SGBD (la syntaxe varie un peu entre SQLite, PostgreSQL, MySQL…)|
|**Injection SQL**   |Une attaque qui consiste à injecter du SQL malveillant via une entrée utilisateur mal protégée |

-----

## Comment penser une requête SQL

Avant d’écrire la moindre ligne de SQL, il faut comprendre la logique de base. **Toute requête SQL répond à une question :**

```
   QUESTION                  REQUÊTE                  RÉSULTAT
   "Quels lecteurs       →   SELECT * FROM      →     Une liste
    habitent à Paris ?"      readers WHERE            de lignes
                             city = 'Paris';
```

Concrètement, **6 grandes opérations** suffisent à résoudre 90% des questions :

1. **Choisir** une table (`FROM`)
1. **Choisir** des colonnes (`SELECT`)
1. **Filtrer** les lignes (`WHERE`)
1. **Croiser** plusieurs tables (`JOIN`)
1. **Regrouper** pour calculer (`GROUP BY` + `COUNT`/`SUM`/`AVG`)
1. **Trier et limiter** (`ORDER BY` + `LIMIT`)

Tout le reste est de la nuance ou de la combinaison de ces 6 briques. Garde ça en tête à chaque chapitre.

-----

## Fil rouge : Nora à la médiathèque

> **Contexte narratif**
> 
> **Nora**, 28 ans, vient d’être recrutée à la médiathèque municipale de Saint-Cloud. Son poste est hybride : agent d’accueil, responsable des données, et “personne qui sait gérer l’informatique” pour la petite équipe. La médiathèque a une base de données SQLite qui stocke les livres, les auteurs, les lecteurs, les emprunts, les comptes du personnel, et un journal de connexions.
> 
> Personne avant elle ne savait écrire de requêtes SQL. Le directeur veut maintenant des **statistiques régulières** : combien de lecteurs sont actifs, quels livres sont les plus empruntés, quels lecteurs ont des retards récurrents, quels emails sont en double dans la base, et — plus inquiétant — y a-t-il des tentatives de connexion suspectes sur les comptes du personnel ?
> 
> Nora va apprendre SQL chapitre par chapitre, et chaque épisode du fil rouge correspond à une vraie demande qu’elle reçoit dans son travail.

-----

## Table des matières

**PARTIE I — COMPRENDRE LES BASES (Ch.1-4)**

1. [Pourquoi les bases de données existent](#chapitre-1--pourquoi-les-bases-de-données-existent)
1. [Comprendre le modèle relationnel](#chapitre-2--comprendre-le-modèle-relationnel)
1. [SQL, SGBD et dialectes](#chapitre-3--sql-sgbd-et-dialectes)
1. [Installer et explorer l’environnement de lab](#chapitre-4--installer-et-explorer-lenvironnement-de-lab)

**PARTIE II — LIRE DES DONNÉES (Ch.5-10)**

1. [Première requête avec SELECT](#chapitre-5--première-requête-avec-select)
1. [Améliorer l’affichage : alias, DISTINCT, commentaires](#chapitre-6--alias-distinct-commentaires)
1. [Filtrer avec WHERE](#chapitre-7--filtrer-avec-where)
1. [Conditions multiples : AND, OR, NOT](#chapitre-8--conditions-multiples)
1. [Filtres utiles : LIKE, IN, BETWEEN, NULL](#chapitre-9--like-in-between-null)
1. [Trier, limiter et paginer](#chapitre-10--trier-limiter-paginer)

**PARTIE III — CALCULER ET REGROUPER (Ch.11-14)**

1. [Fonctions et calculs simples](#chapitre-11--fonctions-et-calculs)
1. [Fonctions d’agrégation](#chapitre-12--fonctions-dagrégation)
1. [Regrouper avec GROUP BY](#chapitre-13--group-by)
1. [Filtrer les groupes avec HAVING](#chapitre-14--having)

**PARTIE IV — CROISER LES TABLES (Ch.15-19)**

1. [Comprendre les relations entre tables](#chapitre-15--relations-entre-tables)
1. [Première jointure avec INNER JOIN](#chapitre-16--inner-join)
1. [LEFT JOIN et données sans correspondance](#chapitre-17--left-join)
1. [Jointures sur plusieurs tables](#chapitre-18--jointures-multi-tables)
1. [Pièges classiques des jointures](#chapitre-19--pièges-des-jointures)

**PARTIE V — MODIFIER LES DONNÉES (Ch.20-23)**

1. [Ajouter des données avec INSERT](#chapitre-20--insert)
1. [Modifier avec UPDATE](#chapitre-21--update)
1. [Supprimer avec DELETE](#chapitre-22--delete)
1. [Transactions : BEGIN, COMMIT, ROLLBACK](#chapitre-23--transactions)

**PARTIE VI — CRÉER ET STRUCTURER UNE BASE (Ch.24-26)**

1. [Créer une table avec CREATE TABLE](#chapitre-24--create-table)
1. [Types de données et contraintes](#chapitre-25--types-et-contraintes)
1. [Modélisation simple](#chapitre-26--modélisation-simple)

**PARTIE VII — POUR ALLER PLUS LOIN (Ch.27-30) — 🔴 BONUS**

1. [Bonnes pratiques SQL et vues](#chapitre-27--bonnes-pratiques-et-vues)
1. [Index et performance : introduction](#chapitre-28--index-et-performance)
1. [Sécurité et SQL injection : aperçu défensif](#chapitre-29--sécurité-et-sql-injection)
1. [SQL depuis Python : passerelle](#chapitre-30--sql-depuis-python)

**PARTIE VIII — SYNTHÈSE (Ch.31-32)**

1. [Skills Assessment — Évaluation finale](#chapitre-31--skills-assessment)
1. [Synthèse et boîte à outils SQL](#chapitre-32--synthèse)

**ANNEXES**

-----

# PARTIE I — COMPRENDRE LES BASES

-----

# Chapitre 1 — Pourquoi les bases de données existent

## Le minimum à savoir

### Le problème : pourquoi pas Excel ?

Imagine que tu gères une médiathèque avec un fichier Excel. Une feuille pour les livres, une pour les lecteurs, une pour les emprunts. Au début, tout va bien. Puis, peu à peu :

- Le fichier dépasse 50 000 lignes — il devient lent à ouvrir
- Deux personnes veulent le modifier en même temps — l’une perd son travail
- Tu cherches “tous les emprunts d’Alice Martin” — il faut faire un filtre, copier-coller, recouper avec une autre feuille
- Tu écris “Allice Martin” dans une ligne et “Alice Martin” dans une autre — Excel ne sait pas que c’est la même personne
- Tu envoies le fichier par mail à un collègue, il en fait une copie, modifie sa version — laquelle est la vraie ?

C’est exactement le problème que les **bases de données** résolvent.

### Qu’est-ce qu’une base de données ?

Une base de données est un système conçu pour :

- **Stocker** beaucoup de données de manière structurée
- **Chercher** rapidement, même dans des millions de lignes
- **Gérer** plusieurs utilisateurs en même temps sans conflits
- **Garantir** la cohérence des données (pas de doublons, pas d’incohérences)
- **Sécuriser** l’accès (qui peut lire, qui peut modifier)
- **Sauvegarder** et restaurer en cas de problème

Tu interagis avec elle via un **langage** : SQL.

### Où trouve-t-on des bases de données ?

**Partout.** Chaque fois que tu utilises une application qui mémorise quelque chose, il y a probablement une base de données derrière :

|Application                  |Ce que la base stocke                      |
|-----------------------------|-------------------------------------------|
|Site e-commerce              |Produits, clients, commandes, paiements    |
|Réseau social                |Utilisateurs, posts, messages, likes       |
|Application bancaire         |Comptes, transactions, virements           |
|Outil RH                     |Salariés, contrats, congés, paies          |
|Système de tickets (helpdesk)|Tickets, utilisateurs, échanges            |
|SIEM (cybersécurité)         |Logs, alertes, indicateurs de compromission|
|Bibliothèque/médiathèque     |Livres, lecteurs, emprunts, retards        |

Comprendre SQL te donne accès à **toutes ces données** — c’est l’une des compétences les plus universelles en informatique.

### Excel vs base de données : la comparaison

|Aspect            |Excel / fichier texte      |Base de données            |
|------------------|---------------------------|---------------------------|
|Volume            |Quelques milliers de lignes|Millions, milliards        |
|Recherche         |Lente, manuelle            |Rapide, structurée         |
|Multi-utilisateurs|Conflits fréquents         |Géré nativement            |
|Cohérence         |Aucune garantie            |Contraintes strictes       |
|Relations         |Difficile                  |Natif (jointures)          |
|Sécurité          |Fichier protégé ou pas     |Permissions par utilisateur|
|Sauvegarde        |Manuelle                   |Automatisable              |
|Langage           |Formules Excel             |SQL (universel)            |


> **À retenir :** Excel n’est pas mauvais — il est parfait pour de petits volumes et de l’analyse ponctuelle. Mais dès qu’il faut **stocker durablement**, **partager** et **chercher efficacement**, la base de données est l’outil adapté.

> **📋 FIL ROUGE — Épisode 1**
> 
> Premier jour de Nora à la médiathèque. La directrice lui montre l’organisation actuelle : un fichier Excel “Liste_lecteurs_2024_v17_final_def.xlsx” et une autre feuille pour les emprunts. Trois personnes ont chacune leur propre version sur leur poste. Pour savoir si Alice Martin a rendu son livre, il faut ouvrir deux fichiers et croiser à la main. Heureusement, l’ancien stagiaire informatique a laissé une **base SQLite** `bibliotheque.db` mais personne ne sait l’utiliser. C’est ce que Nora va apprendre.

## ✅ Tu sais maintenant…

- Pourquoi les fichiers Excel atteignent vite leurs limites
- Ce qu’apporte une base de données (volume, recherche, cohérence, multi-utilisateurs)
- Que SQL est le langage universel pour parler aux bases de données
- Que les bases de données sont partout — apprendre SQL ouvre l’accès à toutes les applications qui en utilisent

-----

# Chapitre 2 — Comprendre le modèle relationnel

## Le minimum à savoir

### Les briques fondamentales

Une base de données **relationnelle** est organisée en **tables**, chacune ressemblant à un tableau structuré.

```
Table : readers
┌────┬────────────┬───────────┬──────────────────────┬────────┐
│ id │ first_name │ last_name │ email                │ city   │
├────┼────────────┼───────────┼──────────────────────┼────────┤
│ 1  │ Alice      │ Martin    │ alice@example.com    │ Paris  │
│ 2  │ Karim      │ Bernard   │ karim@example.com    │ Lyon   │
│ 3  │ Léa        │ Dubois    │ lea.dubois@mail.fr   │ Paris  │
└────┴────────────┴───────────┴──────────────────────┴────────┘
   ↑       ↑           ↑             ↑                  ↑
 colonnes (champs) — chacune a un nom et un type
```

Vocabulaire :

|Terme                  |Signification                                           |
|-----------------------|--------------------------------------------------------|
|**Table**              |Un tableau de données (`readers` = les lecteurs)        |
|**Colonne (column)**   |Un champ — une propriété (`first_name`, `email`, `city`)|
|**Ligne (row, record)**|Un enregistrement — une instance (un lecteur précis)    |
|**Valeur**             |Le contenu d’une cellule (`Alice`, `Paris`)             |


> **Note :** une table SQL ressemble à une feuille Excel, à une grande différence près — chaque colonne a un **type fixé** (texte, nombre, date…) et des **règles** qui empêchent les incohérences.

### La clé primaire

La **clé primaire** (primary key) est une colonne qui identifie de façon **unique** chaque ligne d’une table. Souvent, c’est une colonne `id` qui contient un nombre auto-incrémenté.

```
readers
┌────┬────────────┐
│ id │ first_name │  ← id est la clé primaire
├────┼────────────┤
│ 1  │ Alice      │
│ 2  │ Karim      │
│ 3  │ Léa        │  ← chaque id est unique
└────┴────────────┘
```

Pourquoi c’est crucial ? Parce que dans la vraie vie, plusieurs personnes peuvent s’appeler “Alice Martin”. Mais l’**id** est unique. Quand tu cherches “le lecteur d’id 1”, il n’y en a qu’un — pas d’ambiguïté.

### Plusieurs tables, et des liens entre elles

Une médiathèque ne stocke pas que des lecteurs. Elle stocke aussi des **livres** :

```
Table : books
┌────┬─────────────────────┬────────────────────┐
│ id │ title               │ category           │
├────┼─────────────────────┼────────────────────┤
│ 4  │ Les Misérables      │ Roman              │
│ 7  │ 1984                │ Roman              │
│ 12 │ Sapiens             │ Histoire           │
└────┴─────────────────────┴────────────────────┘
```

Et des **emprunts** — c’est ici que la magie du modèle relationnel opère :

```
Table : loans
┌────┬───────────┬─────────┬────────────┐
│ id │ reader_id │ book_id │ loan_date  │
├────┼───────────┼─────────┼────────────┤
│ 1  │ 1         │ 4       │ 2026-01-10 │  ← Alice (id=1) a emprunté Les Misérables (id=4)
│ 2  │ 2         │ 7       │ 2026-01-12 │  ← Karim (id=2) a emprunté 1984 (id=7)
│ 3  │ 1         │ 12      │ 2026-01-15 │  ← Alice (id=1) a aussi emprunté Sapiens (id=12)
└────┴───────────┴─────────┴────────────┘
```

Au lieu de répéter “Alice Martin” et “Les Misérables” dans chaque ligne d’emprunt, on stocke seulement les **identifiants** : `reader_id = 1` et `book_id = 4`.

### La clé étrangère

`reader_id` dans la table `loans` est une **clé étrangère** (foreign key). Elle pointe vers la **clé primaire** `id` de la table `readers`. C’est ce qui crée la **relation** entre les deux tables.

```
   loans                                  readers
   ┌────┬───────────┬─────────┐          ┌────┬────────────┐
   │ id │ reader_id │ book_id │          │ id │ first_name │
   ├────┼───────────┼─────────┤          ├────┼────────────┤
   │ 1  │     1 ────┼─────────┼─────────→│ 1  │ Alice      │
   │ 2  │     2 ────┼─────────┼─────────→│ 2  │ Karim      │
   └────┴───────────┴─────────┘          └────┴────────────┘
            clé étrangère                       clé primaire
```

> **À retenir :** la clé primaire **identifie**, la clé étrangère **relie**. C’est le concept central du modèle relationnel — la “relation” dans “base de données relationnelle” vient de là.

### Pourquoi séparer les données ?

Trois raisons fondamentales :

1. **Éviter les doublons** : on stocke “Alice Martin” une seule fois (dans `readers`), pas dans chaque emprunt
1. **Garantir la cohérence** : si Alice change d’email, on le modifie en un seul endroit
1. **Permettre les relations** : un lecteur peut avoir 50 emprunts sans qu’on duplique 50 fois ses informations

> **📋 FIL ROUGE — Épisode 2**
> 
> Nora ouvre la base `bibliotheque.db` et découvre 8 tables : `readers`, `books`, `authors`, `categories`, `book_authors`, `loans`, `staff_users`, `login_events`. Au début, ça l’intimide. Puis elle comprend la logique : chaque entité a sa table (lecteurs, livres, auteurs…), et les tables d’**association** comme `book_authors` ou `loans` font le lien entre elles. Le schéma devient lisible.

## Très utile en pratique

### Les types de relations

|Relation                       |Exemple                                                                       |Comment c’est modélisé                                    |
|-------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------|
|**Un-à-plusieurs (1-N)**       |Un lecteur a plusieurs emprunts                                               |Une clé étrangère dans la table “côté plusieurs”          |
|**Plusieurs-à-plusieurs (N-N)**|Un livre peut avoir plusieurs auteurs ; un auteur peut écrire plusieurs livres|Une table d’**association** intermédiaire (`book_authors`)|
|**Un-à-un (1-1)**              |Un utilisateur a un profil détaillé                                           |Rare, géré par une clé étrangère unique                   |

On reverra tout ça en détail au Ch.15 quand on attaquera les jointures.

## ✅ Tu sais maintenant…

- Une base relationnelle est composée de **tables** (lignes + colonnes)
- La **clé primaire** identifie de façon unique chaque ligne
- La **clé étrangère** relie une table à une autre
- Les données sont **séparées** pour éviter les doublons et garantir la cohérence
- Les relations 1-N et N-N sont les patterns de base du modèle relationnel

-----

# Chapitre 3 — SQL, SGBD et dialectes

## Le minimum à savoir

### SQL vs SGBD : la confusion classique

Beaucoup de débutants confondent **SQL** et le **moteur** de base de données. C’est comme confondre “le français” et “un livre français”.

|Concept |Définition                                                     |Exemples                                             |
|--------|---------------------------------------------------------------|-----------------------------------------------------|
|**SQL** |Le **langage** standardisé pour parler aux bases relationnelles|(un seul SQL — défini par les normes ISO)            |
|**SGBD**|Le **moteur** qui exécute le SQL                               |SQLite, PostgreSQL, MySQL/MariaDB, SQL Server, Oracle|


> **Phrase à retenir :** SQL est le langage. SQLite, PostgreSQL, MySQL ou SQL Server sont des moteurs qui comprennent ce langage avec quelques variantes.

### Les SGBD que tu rencontreras

|SGBD               |Particularité                           |Cas d’usage typique                                           |
|-------------------|----------------------------------------|--------------------------------------------------------------|
|**SQLite**         |Léger (un fichier `.db`), pas de serveur|Apps mobiles, sites web légers, prototypage, **apprentissage**|
|**PostgreSQL**     |Open source, très complet, robuste      |Applications web modernes, data, géographie                   |
|**MySQL / MariaDB**|Open source, très répandu               |Sites web (WordPress, etc.), applis classiques                |
|**SQL Server**     |Microsoft, solide en entreprise         |ERP, environnements Windows                                   |
|**Oracle**         |Historique, puissant, payant            |Grandes banques, ERP critiques                                |

**Tous comprennent le SQL standard.** Si tu sais écrire `SELECT * FROM users WHERE city = 'Paris'`, ça marche partout.

### Les dialectes : les petites différences

Chaque SGBD ajoute ses propres extensions au SQL standard. C’est ce qu’on appelle un **dialecte**.

Exemples :

|Tâche                |SQLite               |PostgreSQL            |MySQL             |
|---------------------|---------------------|----------------------|------------------|
|Concaténer du texte  |`'a' || 'b'`         |`'a' || 'b'`          |`CONCAT('a', 'b')`|
|Date du jour         |`DATE('now')`        |`CURRENT_DATE`        |`CURDATE()`       |
|Auto-incrément       |`INTEGER PRIMARY KEY`|`SERIAL` ou `IDENTITY`|`AUTO_INCREMENT`  |
|Limiter les résultats|`LIMIT 10`           |`LIMIT 10`            |`LIMIT 10`        |

**90% du SQL est identique entre tous les SGBD.** Les 10% qui varient sont les fonctions de date, l’auto-incrément, la concaténation, et quelques détails. On apprend SQLite dans ce cours, mais ce que tu apprends est transférable à 90% sur PostgreSQL ou MySQL.

### Pourquoi SQLite pour ce cours ?

Pour apprendre, SQLite est imbattable :

- **Pas de serveur** : la base est un seul fichier `.db` — tu copies, tu déplaces, tu sauvegardes facilement
- **Installation triviale** : déjà inclus dans Python, dans macOS, dans la plupart des Linux
- **Outils gratuits** : DB Browser for SQLite te donne une interface graphique en 2 minutes
- **Syntaxe SQL standard** : ce que tu apprends marchera (à 90%) sur PostgreSQL et MySQL
- **Suffisant pour de vraies applications** : SQLite est utilisé par des milliards d’apps mobiles, le navigateur Firefox, etc.

> **À retenir :** apprendre sur SQLite **n’est pas** apprendre un truc obsolète ou un jouet. C’est apprendre SQL avec l’environnement le plus simple possible. Tu transféreras 90% de ce que tu sais quand tu passeras à PostgreSQL ou MySQL.

## ✅ Tu sais maintenant…

- SQL est le **langage**, le SGBD est le **moteur**
- Les SGBD principaux : SQLite, PostgreSQL, MySQL, SQL Server, Oracle
- Les **dialectes** sont les petites variantes propres à chaque moteur
- SQLite est parfait pour apprendre — et ce que tu apprends est transférable

-----

# Chapitre 4 — Installer et explorer l’environnement de lab

## Le minimum à savoir

### Les outils que tu vas utiliser

1. **DB Browser for SQLite** : interface graphique recommandée pour débuter (gratuite, multi-plateforme)
1. **`sqlite3`** : l’outil en ligne de commande SQLite, parfois déjà installé selon le système, sinon installable séparément (paquet `sqlite3` sous Linux/Mac, téléchargeable sur sqlite.org pour Windows)
1. **Module Python `sqlite3`** : intégré nativement à Python, utile pour interroger SQLite depuis un script (voir Ch.30)

### Installer DB Browser for SQLite

C’est l’outil que je te recommande pour démarrer. Tu ouvres ta base, tu vois les tables, tu cliques pour explorer, tu écris tes requêtes dans une fenêtre dédiée.

**Téléchargement :** <https://sqlitebrowser.org> (gratuit, open source, Windows/Mac/Linux)

**Installation :**

- **Windows** : télécharge le `.msi`, double-clic, suivant-suivant-terminer
- **Mac** : télécharge le `.dmg`, glisse dans Applications
- **Linux (Ubuntu/Debian)** : `sudo apt install sqlitebrowser`

Une fois installé, lance l’application. Tu vois 4 onglets en haut :

- **Structure de la base** (les tables, les colonnes, les contraintes)
- **Parcourir les données** (visualiser et éditer les lignes)
- **Modifier les pragmas** (paramètres avancés — on s’en fiche pour l’instant)
- **Exécuter le SQL** (où tu vas passer 95% de ton temps)

### La base de démo : `bibliotheque.db`

Pour pratiquer, il te faut une base remplie de données. Voici le **script SQL complet** qui crée la base “bibliothèque” qu’on utilisera tout au long du cours.

**Marche à suivre :**

1. Ouvre DB Browser for SQLite
1. Clique sur **“Nouvelle base de données”** → enregistre-la sous `bibliotheque.db`
1. Va dans l’onglet **“Exécuter le SQL”**
1. Colle l’intégralité du script ci-dessous
1. Clique sur le bouton ▶ (“Exécuter”)
1. Dans le menu : **Fichier → Enregistrer les changements**

**Script `bibliotheque.sql`** (le code complet est aussi disponible en Annexe H) :

```sql
-- =============================================================
-- Base de démo : médiathèque municipale
-- =============================================================
-- Ce script est idempotent : tu peux le ré-exécuter, il se nettoie tout seul.

-- 1. Désactiver temporairement les FK pour pouvoir DROP dans n'importe quel ordre
PRAGMA foreign_keys = OFF;

-- 2. Supprimer les tables si elles existent déjà (ordre inverse des dépendances)
DROP TABLE IF EXISTS login_events;
DROP TABLE IF EXISTS staff_users;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS book_authors;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS readers;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS categories;

-- 3. Réactiver les FK pour qu'elles soient vraiment appliquées
PRAGMA foreign_keys = ON;

-- =============================================================
-- Création des tables
-- =============================================================

-- Catégories de livres
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO categories (id, name) VALUES
    (1, 'Roman'),
    (2, 'Histoire'),
    (3, 'Science'),
    (4, 'Bande dessinée'),
    (5, 'Jeunesse'),
    (6, 'Polar');

-- Auteurs
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

INSERT INTO authors (id, name, country) VALUES
    (1, 'Victor Hugo', 'France'),
    (2, 'George Orwell', 'Royaume-Uni'),
    (3, 'Yuval Noah Harari', 'Israël'),
    (4, 'J.K. Rowling', 'Royaume-Uni'),
    (5, 'Albert Camus', 'France'),
    (6, 'Stephen King', 'États-Unis'),
    (7, 'Agatha Christie', 'Royaume-Uni'),
    (8, 'Hergé', 'Belgique'),
    (9, 'Claire Morel', 'France'),
    (10, 'Marc Dumas', 'France'),
    (11, 'Mary Shelley', 'Royaume-Uni');     -- auteur sans livre dans la base

-- Livres
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    category_id INTEGER,
    publication_year INTEGER,
    isbn TEXT UNIQUE,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO books (id, title, category_id, publication_year, isbn) VALUES
    (1, 'Les Misérables', 1, 1862, '978-2-07-040922-8'),
    (2, '1984', 1, 1949, '978-0-452-28423-4'),
    (3, 'Sapiens', 2, 2011, '978-0-06-231609-7'),
    (4, 'Harry Potter à l''école des sorciers', 5, 1997, '978-2-07-054127-9'),
    (5, 'L''Étranger', 1, 1942, '978-2-07-036002-4'),
    (6, 'Ça', 6, 1986, '978-2-253-15124-5'),
    (7, 'Le Crime de l''Orient-Express', 6, 1934, '978-2-253-00642-2'),
    (8, 'Tintin au Tibet', 4, 1960, '978-2-203-00120-3'),
    (9, 'Notre-Dame de Paris', 1, 1831, '978-2-07-040909-9'),
    (10, 'Animal Farm', 1, 1945, '978-0-452-28424-1'),
    (11, 'Harry Potter et la Chambre des Secrets', 5, 1998, '978-2-07-054128-6'),
    (12, 'La Peste', 1, 1947, '978-2-07-036042-0'),
    (13, 'Shining', 6, 1977, '978-2-253-15127-6'),
    (14, 'Dix petits nègres', 6, 1939, '978-2-253-00643-9'),
    (15, 'Histoire d''un pays sans nom', 2, 2018, '978-2-07-014123-7');

-- Table d'association livres ↔ auteurs (relation N-N)
CREATE TABLE book_authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

INSERT INTO book_authors (book_id, author_id) VALUES
    (1, 1), (9, 1),                  -- Hugo
    (2, 2), (10, 2),                  -- Orwell
    (3, 3),                            -- Harari
    (4, 4), (11, 4),                  -- Rowling
    (5, 5), (12, 5),                  -- Camus
    (6, 6), (13, 6),                  -- King
    (7, 7), (14, 7),                  -- Christie
    (8, 8),                            -- Hergé
    (15, 9), (15, 10);                 -- Histoire d'un pays sans nom : coécrit Morel + Dumas

-- Lecteurs
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    city TEXT,
    phone TEXT,
    registration_date TEXT NOT NULL
);

INSERT INTO readers (id, first_name, last_name, email, city, phone, registration_date) VALUES
    (1, 'Alice', 'Martin', 'alice.martin@example.com', 'Paris', '0612345678', '2023-03-15'),
    (2, 'Karim', 'Bernard', 'karim.bernard@example.com', 'Lyon', '0698765432', '2023-04-02'),
    (3, 'Léa', 'Dubois', 'lea.dubois@example.com', 'Paris', NULL, '2023-05-10'),
    (4, 'Thomas', 'Petit', 'thomas.petit@example.com', 'Marseille', '0623456789', '2023-06-21'),
    (5, 'Sophie', 'Leroy', 'sophie.leroy@example.com', 'Paris', '0634567890', '2023-09-05'),
    (6, 'Mehdi', 'Garcia', 'mehdi.garcia@example.com', 'Lyon', NULL, '2024-01-12'),
    (7, 'Camille', 'Rousseau', 'camille.rousseau@example.com', 'Bordeaux', '0645678901', '2024-02-28'),
    (8, 'Hugo', 'Moreau', 'hugo.moreau@example.com', 'Paris', '0656789012', '2024-04-15'),
    (9, 'Yasmine', 'Lefevre', 'yasmine.lefevre@example.com', 'Marseille', NULL, '2024-07-03'),
    (10, 'Alice', 'Martin', 'alice.martin@example.com', 'Toulouse', '0667890123', '2024-09-18'),
    (11, 'Pierre', 'Roux', 'pierre.roux@example.com', 'Lyon', '0678901234', '2024-11-22'),
    (12, 'Inès', 'Vincent', NULL, 'Paris', '0689012345', '2025-01-08'),
    (13, 'David', 'Fournier', 'david.fournier@example.com', 'Bordeaux', NULL, '2025-02-14'),
    (14, 'Sarah', 'Mercier', 'sarah.mercier@example.com', 'Paris', '0690123456', '2025-04-30'),
    (15, 'Lucas', 'Blanc', 'lucas.blanc@example.com', 'Toulouse', '0601234567', '2025-08-11');

-- Emprunts
CREATE TABLE loans (
    id INTEGER PRIMARY KEY,
    reader_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL DEFAULT 'borrowed',
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (status IN ('borrowed', 'returned', 'late'))
);

INSERT INTO loans (id, reader_id, book_id, loan_date, return_date, status) VALUES
    (1, 1, 1, '2025-01-10', '2025-01-25', 'returned'),
    (2, 2, 2, '2025-01-15', '2025-02-05', 'returned'),
    (3, 1, 3, '2025-02-20', '2025-03-10', 'returned'),
    (4, 3, 4, '2025-03-01', NULL, 'late'),
    (5, 4, 5, '2025-03-15', '2025-04-02', 'returned'),
    (6, 1, 6, '2025-04-10', NULL, 'borrowed'),
    (7, 5, 7, '2025-04-22', '2025-05-12', 'returned'),
    (8, 2, 8, '2025-05-05', NULL, 'late'),
    (9, 6, 9, '2025-05-18', '2025-06-08', 'returned'),
    (10, 7, 10, '2025-06-01', '2025-06-22', 'returned'),
    (11, 1, 11, '2025-06-15', '2025-07-05', 'returned'),
    (12, 8, 12, '2025-07-10', NULL, 'borrowed'),
    (13, 3, 13, '2025-07-25', NULL, 'late'),
    (14, 9, 14, '2025-08-12', '2025-09-01', 'returned'),
    (15, 4, 15, '2025-08-30', NULL, 'borrowed'),
    (16, 5, 1, '2025-09-15', '2025-10-05', 'returned'),
    (17, 1, 2, '2025-10-02', NULL, 'borrowed'),
    (18, 11, 3, '2025-10-18', NULL, 'borrowed'),
    (19, 13, 6, '2025-11-05', NULL, 'borrowed'),
    (20, 1, 4, '2025-11-20', NULL, 'late');

-- Comptes du personnel (pour l'angle cyber)
CREATE TABLE staff_users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
);

INSERT INTO staff_users (id, username, full_name, role, is_active, created_at) VALUES
    (1, 'nora.benali', 'Nora Benali', 'admin', 1, '2025-01-15'),
    (2, 'jean.dupont', 'Jean Dupont', 'staff', 1, '2023-09-01'),
    (3, 'sophie.morel', 'Sophie Morel', 'staff', 1, '2024-03-12'),
    (4, 'olivier.bernard', 'Olivier Bernard', 'staff', 0, '2022-06-20'),
    (5, 'admin', 'Admin Initial', 'admin', 1, '2022-01-01');

-- Journal de connexions au système interne
CREATE TABLE login_events (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    event_time TEXT NOT NULL,
    success INTEGER NOT NULL,
    ip_address TEXT
);

INSERT INTO login_events (id, username, event_time, success, ip_address) VALUES
    (1, 'nora.benali', '2025-11-20 08:32:15', 1, '192.168.1.42'),
    (2, 'jean.dupont', '2025-11-20 09:01:43', 1, '192.168.1.51'),
    (3, 'sophie.morel', '2025-11-20 09:15:02', 1, '192.168.1.55'),
    (4, 'admin', '2025-11-20 23:14:01', 0, '203.0.113.42'),
    (5, 'admin', '2025-11-20 23:14:08', 0, '203.0.113.42'),
    (6, 'admin', '2025-11-20 23:14:14', 0, '203.0.113.42'),
    (7, 'admin', '2025-11-20 23:14:19', 0, '203.0.113.42'),
    (8, 'admin', '2025-11-20 23:14:25', 0, '203.0.113.42'),
    (9, 'admin', '2025-11-20 23:14:31', 0, '203.0.113.42'),
    (10, 'admin', '2025-11-20 23:14:37', 0, '203.0.113.42'),
    (11, 'admin', '2025-11-20 23:14:42', 0, '203.0.113.42'),
    (12, 'admin', '2025-11-20 23:14:48', 0, '203.0.113.42'),
    (13, 'admin', '2025-11-20 23:14:54', 0, '203.0.113.42'),
    (14, 'admin', '2025-11-20 23:15:01', 1, '203.0.113.42'),
    (15, 'nora.benali', '2025-11-21 08:28:55', 1, '192.168.1.42'),
    (16, 'jean.dupont', '2025-11-21 08:55:12', 1, '192.168.1.51'),
    (17, 'olivier.bernard', '2025-11-21 14:32:09', 0, '198.51.100.7');
```

> **Astuce :** ce script est aussi en **Annexe H** à la fin du cours, prêt à être copié-collé.

> **⚠️ Important — SQLite et les clés étrangères :** par défaut, SQLite **n’applique pas automatiquement** les contraintes `FOREIGN KEY` dans toutes les sessions. Il faut les activer explicitement avec `PRAGMA foreign_keys = ON;` au début de chaque session. Le script de la base le fait déjà, mais si tu ouvres une nouvelle session SQLite (par exemple via `sqlite3 bibliotheque.db` en ligne de commande), pense à ré-exécuter `PRAGMA foreign_keys = ON;` avant tes manipulations. Sinon, certaines erreurs de clé étrangère que tu attends (par exemple aux Ch.22 sur `DELETE`) ne se produiront pas.

### Premières commandes en ligne de commande SQLite

Si tu préfères le terminal, ouvre un terminal et lance :

```bash
sqlite3 bibliotheque.db
```

Tu obtiens un prompt `sqlite>`. Quelques commandes utiles (les “méta-commandes” commencent par un point) :

```
.tables                 -- Liste les tables
.schema                 -- Affiche la structure de toutes les tables
.schema readers         -- Affiche la structure de la table readers
.headers on             -- Affiche les noms de colonnes dans les résultats
.mode column            -- Affichage en colonnes alignées (plus lisible)
.quit                   -- Quitter sqlite3
```

Puis tu peux taper du SQL directement :

```sql
SELECT * FROM readers LIMIT 5;
```

> **📋 FIL ROUGE — Épisode 3**
> 
> Nora installe DB Browser, ouvre `bibliotheque.db`, et explore la structure. Elle découvre que la base contient bien tout ce dont elle a besoin : 8 tables, des données réalistes, et même un journal de connexions. Elle clique sur “Parcourir les données” pour voir les premières lignes — déjà, elle commence à comprendre la logique. Maintenant, il faut apprendre à interroger.

## ✅ Tu sais maintenant…

- Installer DB Browser for SQLite (interface graphique recommandée pour débuter)
- Créer une base SQLite à partir d’un script SQL
- La base de démo `bibliotheque.db` contient 8 tables prêtes à l’emploi
- Les méta-commandes utiles de `sqlite3` en ligne de commande (`.tables`, `.schema`, `.headers on`)

-----

# PARTIE II — LIRE DES DONNÉES

-----

# Chapitre 5 — Première requête avec SELECT

## Le minimum à savoir

### La requête de base : `SELECT ... FROM`

Toute lecture de données commence par `SELECT` :

```sql
SELECT * FROM readers;
```

Décomposé :

- `SELECT` → “je veux lire”
- `*` → “toutes les colonnes”
- `FROM readers` → “depuis la table `readers`”
- `;` → fin de la requête

Le résultat : toutes les lignes et toutes les colonnes de la table `readers`.

### Sélectionner certaines colonnes

Plutôt que tout afficher, choisis les colonnes utiles :

```sql
SELECT first_name, last_name, email
FROM readers;
```

Tu obtiens uniquement le prénom, le nom et l’email — plus lisible quand la table a beaucoup de colonnes.

### L’ordre des colonnes

L’ordre dans lequel tu listes les colonnes après `SELECT` est l’ordre dans lequel elles s’affichent :

```sql
SELECT email, last_name, first_name
FROM readers;
```

Ça affiche d’abord l’email, puis le nom, puis le prénom. Tu choisis ton ordre.

### Le point-virgule final

En SQL, chaque requête se termine par un point-virgule `;`. C’est ce qui dit au moteur “j’ai fini, exécute”.

Dans DB Browser, tu peux te passer du `;` quand tu n’exécutes qu’une seule requête. Mais prends le réflexe — c’est obligatoire dans la plupart des outils.

### La convention : SQL en MAJUSCULES

Par convention, on écrit les **mots-clés SQL** (`SELECT`, `FROM`, `WHERE`…) en majuscules, et les **noms de tables/colonnes** en minuscules. C’est juste une convention de lisibilité — SQL n’est pas sensible à la casse pour les mots-clés :

```sql
-- ✅ Convention recommandée (lisible)
SELECT first_name, last_name FROM readers;

-- ⚠️ Marche aussi, mais moins lisible
select first_name, last_name from readers;
```

> **📋 FIL ROUGE — Épisode 4**
> 
> La directrice demande à Nora : “Combien de lecteurs avons-nous, et qui sont-ils ?”. Nora ouvre DB Browser et tape sa toute première requête : `SELECT * FROM readers;`. Le résultat s’affiche : 15 lecteurs. Premier succès. Mais elle réalise vite qu’afficher *toutes* les colonnes est trop bavard — elle simplifie : `SELECT first_name, last_name, city FROM readers;`. Plus lisible.

## Très utile en pratique

### `SELECT *` vs colonnes explicites

|Approche                |Quand l’utiliser                                    |
|------------------------|----------------------------------------------------|
|`SELECT *`              |Pour explorer une table, voir ce qu’elle contient   |
|`SELECT col1, col2, ...`|Pour les requêtes finales, les rapports, les exports|


> **Bonne pratique :** `SELECT *` est pratique pour explorer, mais évite-le dans les requêtes “de production”. Pourquoi ? Parce que si la table évolue (nouvelles colonnes), ton résultat change sans que tu ne contrôles rien.

## ❌ Erreur classique

```sql
-- Oublier le FROM
SELECT first_name, last_name;       -- ❌ "no such column" ou "missing FROM clause"
SELECT first_name, last_name FROM readers;  -- ✅

-- Mettre une virgule de trop
SELECT first_name, last_name, FROM readers;  -- ❌ erreur de syntaxe
SELECT first_name, last_name FROM readers;   -- ✅

-- Confondre nom de colonne et nom de table
SELECT readers FROM readers;        -- ❌ "readers" n'est pas une colonne
SELECT * FROM readers;              -- ✅
```

## 💡 Exercices

1. Affiche tous les livres (table `books`).
1. Affiche uniquement le titre et l’année de publication des livres.
1. Affiche le nom complet et la ville des lecteurs.

## ✅ Tu sais maintenant…

- La structure de base : `SELECT colonnes FROM table;`
- `SELECT *` pour toutes les colonnes
- Choisir et ordonner les colonnes manuellement
- La convention : mots-clés SQL en majuscules
- Le point-virgule final

-----

# Chapitre 6 — Améliorer l’affichage : alias, DISTINCT, commentaires

## Le minimum à savoir

### Renommer une colonne avec `AS` (alias)

Tu peux donner un nom temporaire à une colonne dans le résultat :

```sql
SELECT first_name AS prenom, last_name AS nom, email AS courriel
FROM readers;
```

Le résultat affiche les colonnes sous les noms `prenom`, `nom`, `courriel`, sans modifier la table elle-même.

> **À retenir :** un alias ne change rien dans la base — il modifie seulement l’**affichage**. C’est utile pour rendre les résultats plus lisibles, ou pour franciser un export.

Le `AS` est même optionnel — ces deux requêtes sont équivalentes :

```sql
SELECT first_name AS prenom FROM readers;
SELECT first_name prenom FROM readers;       -- même chose, mais moins lisible
```

> **Bonne pratique :** garde le `AS` pour la clarté. Tu le verras partout.

### Éliminer les doublons avec `DISTINCT`

Sans `DISTINCT`, SQL te montre toutes les lignes — y compris les valeurs répétées :

```sql
SELECT city FROM readers;
-- Paris, Lyon, Paris, Marseille, Paris, Lyon, ... (avec doublons)
```

Avec `DISTINCT`, tu n’obtiens que les valeurs **uniques** :

```sql
SELECT DISTINCT city FROM readers;
-- Paris, Lyon, Marseille, Bordeaux, Toulouse (sans doublons)
```

C’est l’équivalent de “supprimer les doublons” dans Excel.

### Commentaires SQL

Comme dans les autres langages, tu peux annoter ton code :

```sql
-- Ceci est un commentaire sur une ligne (deux tirets)

/* Ceci est un commentaire
   sur plusieurs lignes
   (style C) */

SELECT first_name, last_name   -- commentaire en fin de ligne
FROM readers;
```

> **Bonne pratique :** commente tes requêtes complexes. Tu te remercieras dans 6 mois quand tu reliras.

> **📋 FIL ROUGE — Épisode 5**
> 
> La directrice demande à Nora : “Dans quelles villes nos lecteurs habitent-ils ?”. Nora utilise `DISTINCT` :
> 
> ```sql
> SELECT DISTINCT city FROM readers;
> ```
> 
> Résultat : Paris, Lyon, Marseille, Bordeaux, Toulouse. 5 villes. Elle peut maintenant proposer de cibler des animations dans chacune.

## Très utile en pratique

### `DISTINCT` sur plusieurs colonnes

`DISTINCT` s’applique à **la combinaison** de toutes les colonnes sélectionnées :

```sql
SELECT DISTINCT first_name, city FROM readers;
-- Élimine les couples (prénom, ville) en double
```

Donc deux Alice dans deux villes différentes apparaîtront **deux fois** — c’est le couple qui doit être unique.

## ❌ Erreur classique

```sql
-- Mettre AS au mauvais endroit
SELECT AS prenom first_name FROM readers;     -- ❌ AS vient APRÈS la colonne
SELECT first_name AS prenom FROM readers;      -- ✅

-- DISTINCT mal placé
SELECT first_name, DISTINCT city FROM readers; -- ❌ DISTINCT s'applique à toute la sélection
SELECT DISTINCT city FROM readers;             -- ✅
```

## ✅ Tu sais maintenant…

- Renommer une colonne dans le résultat avec `AS`
- Éliminer les doublons avec `DISTINCT`
- Commenter avec `--` ou `/* ... */`

-----

# Chapitre 7 — Filtrer avec WHERE

## Le minimum à savoir

### Le besoin : ne pas tout afficher

Souvent, tu ne veux pas **toutes** les lignes — seulement celles qui correspondent à un critère. C’est le rôle de `WHERE` :

```sql
SELECT *
FROM readers
WHERE city = 'Paris';
```

`WHERE` filtre les lignes : seules celles où `city` vaut `'Paris'` sont retournées.

### Les opérateurs de comparaison

|Opérateur   |Signification    |Exemple                   |
|------------|-----------------|--------------------------|
|`=`         |Égal             |`city = 'Paris'`          |
|`<>` ou `!=`|Différent        |`city <> 'Paris'`         |
|`<`         |Inférieur        |`publication_year < 2000` |
|`>`         |Supérieur        |`publication_year > 2000` |
|`<=`        |Inférieur ou égal|`publication_year <= 2000`|
|`>=`        |Supérieur ou égal|`publication_year >= 1990`|


> **Attention :** en SQL, l’égalité s’écrit avec **un seul** `=` (pas deux comme en Python ou JavaScript). Pour la différence, c’est `<>` (la forme standard) ou `!=` (acceptée par la plupart des SGBD).

### Texte vs nombre : guillemets ou pas ?

Le **texte** se met entre **guillemets simples** `'...'`. Les **nombres** s’écrivent **sans guillemets**.

```sql
SELECT * FROM readers WHERE city = 'Paris';            -- texte → quotes
SELECT * FROM books WHERE publication_year >= 2000;    -- nombre → pas de quotes
SELECT * FROM books WHERE id = 5;                      -- nombre → pas de quotes
```

> **Important :** SQL utilise les **guillemets simples** `'...'` pour le texte. Les guillemets doubles `"..."` ont une autre signification (noms d’identifiants) — ne les utilise pas pour du texte, ou tu auras des erreurs surprenantes.

### Les apostrophes dans le texte

Si ton texte contient une apostrophe, double-la :

```sql
SELECT * FROM books WHERE title = 'L''Étranger';
--                                  ↑↑
--                            apostrophe doublée
```

C’est la façon standard d’échapper une apostrophe en SQL.

> **📋 FIL ROUGE — Épisode 6**
> 
> La directrice demande : “Combien de lecteurs habitent à Paris ?”. Nora tape :
> 
> ```sql
> SELECT * FROM readers WHERE city = 'Paris';
> ```
> 
> Elle compte 5 lignes dans le résultat. Pour automatiser le compte, elle préfigure ce qu’elle apprendra au Ch.12 — `COUNT()`. Mais pour l’instant, voir la liste lui suffit.

## Très utile en pratique

### `WHERE` sur des nombres et des dates

```sql
-- Livres publiés au 21e siècle
SELECT * FROM books WHERE publication_year >= 2000;

-- Lecteurs inscrits depuis 2025
SELECT * FROM readers WHERE registration_date >= '2025-01-01';
```

> **Note SQLite :** SQLite stocke les dates comme du **texte** au format `'YYYY-MM-DD'`. Tant que tes dates respectent ce format, les comparaisons `<`, `>`, `=` fonctionnent comme avec des nombres.

### Filtrer sur la sortie de DB Browser

Quand tu cliques sur “Exécuter”, DB Browser affiche le résultat sous la requête. Si le résultat est long, fais défiler. Le bas de l’écran indique le nombre de lignes retournées — pratique pour vérifier qu’on a bien ce qu’on attend.

## ❌ Erreur classique

```sql
-- Utiliser == au lieu de =
SELECT * FROM readers WHERE city == 'Paris';   -- ❌ Pas standard
SELECT * FROM readers WHERE city = 'Paris';    -- ✅

-- Mettre des nombres entre quotes (ça marche, mais c'est mauvaise pratique)
SELECT * FROM books WHERE id = '5';            -- ⚠️ Fonctionne mais sale
SELECT * FROM books WHERE id = 5;              -- ✅

-- Oublier les quotes pour le texte
SELECT * FROM readers WHERE city = Paris;      -- ❌ "no such column: Paris"
SELECT * FROM readers WHERE city = 'Paris';    -- ✅

-- Utiliser des guillemets doubles pour le texte
SELECT * FROM readers WHERE city = "Paris";    -- ⚠️ peut donner des résultats inattendus
SELECT * FROM readers WHERE city = 'Paris';    -- ✅
```

## 💡 Exercices

1. Affiche les livres publiés avant 1950.
1. Affiche les lecteurs habitant à Lyon.
1. Affiche les emprunts dont le statut est `'late'`.

## ✅ Tu sais maintenant…

- Filtrer les lignes avec `WHERE`
- Les opérateurs : `=`, `<>`, `!=`, `<`, `>`, `<=`, `>=`
- Texte entre guillemets simples, nombres sans guillemets
- Échapper une apostrophe en la doublant (`'L''Étranger'`)

-----

# Chapitre 8 — Conditions multiples : AND, OR, NOT

## Le minimum à savoir

### Combiner des conditions avec `AND`

`AND` impose que **toutes** les conditions soient vraies :

```sql
SELECT *
FROM books
WHERE publication_year >= 2000
  AND category_id = 1;
```

→ Les livres publiés depuis 2000 **ET** de catégorie 1 (Roman).

### Au moins une condition avec `OR`

`OR` accepte une ligne si **au moins une** des conditions est vraie :

```sql
SELECT *
FROM readers
WHERE city = 'Paris'
   OR city = 'Lyon';
```

→ Les lecteurs qui habitent Paris **OU** Lyon.

### Inverser avec `NOT`

`NOT` inverse une condition :

```sql
SELECT *
FROM loans
WHERE NOT status = 'returned';
```

→ Les emprunts qui ne sont **pas** retournés (donc en cours ou en retard).

### La priorité : parenthèses obligatoires si tu mélanges AND et OR

`AND` est prioritaire sur `OR` (comme `*` est prioritaire sur `+` en maths). Donc cette requête :

```sql
SELECT *
FROM books
WHERE category_id = 1 OR category_id = 6 AND publication_year >= 2000;
```

est lue par SQL comme :

```sql
WHERE category_id = 1 OR (category_id = 6 AND publication_year >= 2000)
```

Ce n’est probablement pas ce que tu voulais. Pour éviter toute ambiguïté, **utilise des parenthèses** :

```sql
SELECT *
FROM books
WHERE (category_id = 1 OR category_id = 6)
  AND publication_year >= 2000;
```

> **À retenir :** dès que tu mélanges `AND` et `OR`, mets des parenthèses. Ce n’est pas du zèle — c’est la seule façon de garantir que ta requête fait ce que tu crois qu’elle fait.

> **📋 FIL ROUGE — Épisode 7**
> 
> La directrice veut une promotion : “envoie un email aux lecteurs habitant Paris ou Lyon, inscrits depuis 2024”. Nora écrit :
> 
> ```sql
> SELECT first_name, last_name, email
> FROM readers
> WHERE (city = 'Paris' OR city = 'Lyon')
>   AND registration_date >= '2024-01-01';
> ```
> 
> Elle obtient 5 lecteurs. Sans les parenthèses, elle aurait récupéré tous les Parisiens (peu importe la date) **plus** les Lyonnais inscrits depuis 2024 — résultat très différent.

## Très utile en pratique

### Quand `OR` est répétitif, utilise `IN` (Ch.9)

Tu verras au prochain chapitre que :

```sql
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille'
```

s’écrit plus proprement avec :

```sql
WHERE city IN ('Paris', 'Lyon', 'Marseille')
```

## ❌ Erreur classique

```sql
-- Oublier les parenthèses quand on mélange AND et OR
WHERE city = 'Paris' OR city = 'Lyon' AND age > 30
-- → SQL lit : WHERE city = 'Paris' OR (city = 'Lyon' AND age > 30)
-- → probablement pas ce que tu voulais
WHERE (city = 'Paris' OR city = 'Lyon') AND age > 30   -- ✅

-- Confondre AND et OR sur le sens commun
-- "lecteurs habitant à Paris ET Lyon"
WHERE city = 'Paris' AND city = 'Lyon'    -- ❌ aucune ligne ! Une ville ne peut pas valoir deux choses à la fois
WHERE city = 'Paris' OR city = 'Lyon'     -- ✅ "à Paris OU à Lyon"
```

## 💡 Exercices

1. Affiche les livres de catégorie Roman (id=1) **et** publiés avant 1950.
1. Affiche les lecteurs habitant à Paris, Lyon ou Bordeaux.
1. Affiche les emprunts qui ne sont pas en retard (`status` différent de `'late'`).

## ✅ Tu sais maintenant…

- Combiner des conditions avec `AND` (toutes vraies)
- Accepter avec `OR` (au moins une vraie)
- Inverser avec `NOT`
- Utiliser des parenthèses dès que tu mélanges `AND` et `OR`

-----

# Chapitre 9 — Filtres utiles : LIKE, IN, BETWEEN, NULL

## Le minimum à savoir

### Recherche par motif avec `LIKE`

`LIKE` permet de chercher un motif dans du texte. Deux caractères spéciaux :

|Caractère|Signification                                      |
|---------|---------------------------------------------------|
|`%`      |N’importe quelle séquence de caractères (même vide)|
|`_`      |Exactement un caractère                            |

Exemples :

```sql
-- Tous les livres dont le titre contient "Harry"
SELECT * FROM books WHERE title LIKE '%Harry%';

-- Tous les emails se terminant par "@example.com"
SELECT * FROM readers WHERE email LIKE '%@example.com';

-- Tous les noms commençant par "Mar"
SELECT * FROM readers WHERE last_name LIKE 'Mar%';

-- Mots de 4 lettres commençant par "L"
SELECT * FROM books WHERE title LIKE 'L___';
```

> **Note :** par défaut, `LIKE` est **insensible à la casse** dans SQLite (`'PARIS'` = `'Paris'`). Dans PostgreSQL, c’est sensible — utilise `ILIKE` pour insensibiliser.

### Liste de valeurs avec `IN`

Plus propre que des `OR` à répétition :

```sql
-- Avec OR (verbeux)
SELECT * FROM readers
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille';

-- Avec IN (concis)
SELECT * FROM readers
WHERE city IN ('Paris', 'Lyon', 'Marseille');
```

L’inverse existe aussi : `NOT IN` :

```sql
SELECT * FROM readers
WHERE city NOT IN ('Paris', 'Lyon');
-- → toutes les villes SAUF Paris et Lyon
```

### Plage de valeurs avec `BETWEEN`

```sql
-- Livres publiés entre 1990 et 2000 (inclus)
SELECT * FROM books
WHERE publication_year BETWEEN 1990 AND 2000;
```

`BETWEEN a AND b` est **inclusif** des deux bornes. C’est équivalent à :

```sql
WHERE publication_year >= 1990 AND publication_year <= 2000
```

### Le cas particulier : `NULL`

`NULL` représente l’**absence de valeur**. Ce n’est ni `0`, ni la chaîne vide `''` — c’est “rien”.

**Important :** on ne peut **pas** comparer `NULL` avec `=` :

```sql
SELECT * FROM readers WHERE phone = NULL;        -- ❌ ne renvoie jamais rien
SELECT * FROM readers WHERE phone IS NULL;       -- ✅ correct

SELECT * FROM readers WHERE phone IS NOT NULL;   -- ✅ ceux qui ont un téléphone
```

> **À retenir :** `NULL` n’est égal à rien — pas même à lui-même. Utilise toujours `IS NULL` ou `IS NOT NULL`. C’est l’une des erreurs les plus fréquentes en SQL.

> **📋 FIL ROUGE — Épisode 8**
> 
> La directrice : “Combien de lecteurs n’ont pas de téléphone enregistré ? Il faut leur demander à leur prochaine visite.” Nora :
> 
> ```sql
> SELECT first_name, last_name FROM readers WHERE phone IS NULL;
> ```
> 
> 4 lecteurs. Elle imprime la liste. Si elle avait écrit `WHERE phone = NULL`, elle aurait obtenu 0 résultats — et conclu à tort que tous les lecteurs ont un téléphone.

## Très utile en pratique

### `LIKE` avec recherche multilingue

`LIKE '%harry%'` est insensible à la casse en SQLite par défaut, mais peut ne pas trouver `'Harry'` dans certains environnements. Pour être sûr :

```sql
SELECT * FROM books WHERE LOWER(title) LIKE '%harry%';
```

`LOWER()` met le texte en minuscules — la comparaison devient garantie insensible à la casse.

### `NULL` et opérations

Toute opération impliquant `NULL` produit `NULL` :

```sql
SELECT 5 + NULL;    -- → NULL
SELECT 'a' || NULL; -- → NULL
```

C’est pour ça que `WHERE col = NULL` ne marche pas : `col = NULL` produit `NULL`, pas `TRUE` — et `WHERE` ne garde que les `TRUE`.

## ❌ Erreur classique

```sql
-- Comparer NULL avec =
WHERE phone = NULL;          -- ❌ ne renvoie rien
WHERE phone IS NULL;         -- ✅

-- Confondre chaîne vide et NULL
WHERE email = '';            -- ne trouve QUE les emails vides (chaîne de longueur 0)
WHERE email IS NULL;         -- trouve les emails non renseignés (rien du tout)

-- Les deux peuvent coexister dans une base mal nettoyée :
-- email = '' (vide) ≠ email IS NULL (absent)
```

## 💡 Exercices

1. Affiche les livres dont le titre contient “Potter”.
1. Affiche les lecteurs habitant à Paris, Lyon **ou** Bordeaux (avec `IN`).
1. Affiche les livres publiés entre 1900 et 1950 (avec `BETWEEN`).
1. Affiche les lecteurs qui n’ont pas d’email.

## ✅ Tu sais maintenant…

- `LIKE '%motif%'` pour chercher un motif dans du texte
- `IN (...)` pour une liste de valeurs
- `BETWEEN a AND b` pour une plage (inclusive)
- `IS NULL` / `IS NOT NULL` pour les valeurs absentes
- `NULL` ≠ chaîne vide `''` ≠ zéro `0`

-----

# Chapitre 10 — Trier, limiter et paginer

## Le minimum à savoir

### Trier avec `ORDER BY`

Par défaut, SQL ne garantit **aucun ordre** dans les résultats. Pour trier, utilise `ORDER BY` :

```sql
-- Par ordre alphabétique sur le nom
SELECT * FROM readers ORDER BY last_name;

-- Par année de publication, du plus récent au plus ancien
SELECT * FROM books ORDER BY publication_year DESC;
```

|Mot-clé        |Effet                              |
|---------------|-----------------------------------|
|(rien) ou `ASC`|Croissant (ascending) — A→Z, 0→9   |
|`DESC`         |Décroissant (descending) — Z→A, 9→0|

### Trier sur plusieurs colonnes

Quand plusieurs lignes ont la même valeur sur la première colonne, on trie par la suivante :

```sql
-- D'abord par catégorie (alphabétique), puis par année (du plus récent)
SELECT title, category_id, publication_year
FROM books
ORDER BY category_id ASC, publication_year DESC;
```

### Limiter le nombre de résultats avec `LIMIT`

Pour ne récupérer que les N premières lignes :

```sql
-- Les 5 lecteurs inscrits le plus récemment
SELECT * FROM readers
ORDER BY registration_date DESC
LIMIT 5;
```

> **À retenir :** `LIMIT` se met **toujours à la fin** de la requête, après `ORDER BY`. Sans `ORDER BY`, `LIMIT 5` te donne 5 lignes “au hasard” — pas forcément les plus récentes.

### Paginer avec `LIMIT` + `OFFSET`

`OFFSET` saute un nombre de lignes avant de commencer :

```sql
-- Lignes 11 à 20 (saut de 10, prend 10)
SELECT * FROM readers
ORDER BY id
LIMIT 10 OFFSET 10;
```

C’est le mécanisme classique de la pagination dans une application web :

- Page 1 : `LIMIT 10 OFFSET 0`
- Page 2 : `LIMIT 10 OFFSET 10`
- Page 3 : `LIMIT 10 OFFSET 20`
- Page N : `LIMIT 10 OFFSET (N-1) * 10`

> **📋 FIL ROUGE — Épisode 9**
> 
> La directrice : “Donne-moi les 10 derniers lecteurs inscrits, on va leur envoyer un mot de bienvenue.” Nora :
> 
> ```sql
> SELECT first_name, last_name, registration_date
> FROM readers
> ORDER BY registration_date DESC
> LIMIT 10;
> ```
> 
> Parfait. Le `DESC` fait remonter les plus récents en premier, le `LIMIT 10` coupe le résultat aux 10 premiers.

## Très utile en pratique

### Trier par plusieurs critères avec sens différent

```sql
-- Par catégorie alphabétique, puis par année DÉCROISSANTE dans chaque catégorie
ORDER BY category_id ASC, publication_year DESC;
```

C’est très utile pour des rapports structurés — d’abord regroupé, puis trié finement à l’intérieur.

### Trier sur un alias

Tu peux trier sur le nom donné par `AS` :

```sql
SELECT title, 2026 - publication_year AS age_du_livre
FROM books
ORDER BY age_du_livre DESC;
```

## ❌ Erreur classique

```sql
-- LIMIT sans ORDER BY
SELECT * FROM readers LIMIT 5;
-- ❌ Te donne 5 lignes "quelconques" — pas forcément les premières/dernières
SELECT * FROM readers ORDER BY id LIMIT 5;   -- ✅ explicite l'ordre

-- ORDER BY après LIMIT
SELECT * FROM readers LIMIT 5 ORDER BY id;   -- ❌ syntaxe incorrecte
SELECT * FROM readers ORDER BY id LIMIT 5;   -- ✅ ORDER BY avant LIMIT

-- Croire que tri ASC = ordre par défaut partout
-- → C'est vrai en pratique, mais sans ORDER BY explicite, le moteur n'a aucune obligation
```

## 💡 Exercices

1. Affiche tous les livres triés par année du plus ancien au plus récent.
1. Affiche les 3 livres les plus récents.
1. Affiche les 5 lecteurs habitant à Paris, par ordre alphabétique sur le nom.
1. Affiche les pages 2 et 3 (10 lecteurs par page) triés par date d’inscription.

## ✅ Tu sais maintenant…

- Trier avec `ORDER BY col ASC` ou `ORDER BY col DESC`
- Trier sur plusieurs colonnes
- Limiter le nombre de résultats avec `LIMIT`
- Paginer avec `LIMIT` + `OFFSET`
- Toujours combiner `LIMIT` avec un `ORDER BY` explicite

-----

# PARTIE III — CALCULER ET REGROUPER

-----

# Chapitre 11 — Fonctions et calculs simples

## Le minimum à savoir

### Calculs dans `SELECT`

Tu peux faire des calculs directement dans la sélection :

```sql
SELECT title, publication_year, 2026 - publication_year AS age_du_livre
FROM books;
```

Le résultat ajoute une colonne calculée `age_du_livre`. Cette colonne n’existe pas dans la table — elle est calculée à la volée pour le résultat.

### Concaténation de texte

En SQLite (et PostgreSQL), on concatène avec `||` :

```sql
SELECT first_name || ' ' || last_name AS full_name
FROM readers;
```

→ `'Alice' || ' ' || 'Martin'` = `'Alice Martin'`

> **Note dialecte :** MySQL utilise `CONCAT(a, b, c)` au lieu de `||`. SQLite et PostgreSQL utilisent `||`. C’est l’un des points où les dialectes diffèrent.

### Fonctions de texte essentielles

|Fonction             |Effet               |Exemple                            |
|---------------------|--------------------|-----------------------------------|
|`UPPER(s)`           |Majuscules          |`UPPER('alice')` → `'ALICE'`       |
|`LOWER(s)`           |Minuscules          |`LOWER('ALICE')` → `'alice'`       |
|`LENGTH(s)`          |Longueur            |`LENGTH('Alice')` → `5`            |
|`TRIM(s)`            |Supprime espaces    |`TRIM('  abc  ')` → `'abc'`        |
|`SUBSTR(s, début, n)`|Extrait n caractères|`SUBSTR('Bonjour', 1, 3)` → `'Bon'`|

```sql
SELECT UPPER(title) AS titre_majuscules, LENGTH(title) AS longueur
FROM books;
```

### Fonctions de date (SQLite)

SQLite stocke les dates comme du texte au format `'YYYY-MM-DD'`. Quelques fonctions utiles :

```sql
-- Date du jour
SELECT DATE('now');                        -- → '2026-05-03'

-- Extraire une partie d'une date
SELECT strftime('%Y', loan_date) AS annee FROM loans;     -- → '2025', '2025', ...
SELECT strftime('%m', loan_date) AS mois  FROM loans;     -- → '01', '02', ...
SELECT strftime('%Y-%m', loan_date) AS annee_mois FROM loans; -- → '2025-01', ...

-- Nombre de jours depuis une date
SELECT julianday('now') - julianday(loan_date) AS jours_depuis_emprunt
FROM loans;
```

> **Note dialecte :** chaque SGBD a ses propres fonctions de date. PostgreSQL utilise `EXTRACT(YEAR FROM date)`, MySQL utilise `YEAR(date)`. SQLite utilise `strftime()`. Quand tu changes de SGBD, c’est l’un des points à adapter.

> **📋 FIL ROUGE — Épisode 10**
> 
> La directrice : “Affiche-moi le nom complet de chaque lecteur en majuscules pour les badges.” Nora :
> 
> ```sql
> SELECT UPPER(first_name || ' ' || last_name) AS nom_badge
> FROM readers
> ORDER BY last_name;
> ```
> 
> Génial — la concaténation et `UPPER()` font tout en une seule requête.

## Très utile en pratique

### Combiner texte et calculs

```sql
SELECT first_name || ' ' || last_name || ' (inscrit en ' || strftime('%Y', registration_date) || ')' AS description
FROM readers;
-- → 'Alice Martin (inscrit en 2023)', 'Karim Bernard (inscrit en 2023)', ...
```

C’est le même principe qu’une f-string Python, en SQL.

## ❌ Erreur classique

```sql
-- Confondre la chaîne 'NULL' et la valeur NULL
SELECT 'a' || NULL || 'b';      -- → NULL (toute opération avec NULL donne NULL)
-- Pour gérer ça, utilise COALESCE :
SELECT 'a' || COALESCE(NULL, '') || 'b';   -- → 'ab' (COALESCE remplace NULL par '')

-- Utiliser CONCAT en SQLite
SELECT CONCAT(first_name, ' ', last_name) FROM readers;   -- ❌ pas en SQLite/PostgreSQL
SELECT first_name || ' ' || last_name FROM readers;        -- ✅
```

## 💡 Exercices

1. Affiche le nom complet de chaque lecteur (prénom + espace + nom).
1. Affiche les titres des livres en majuscules.
1. Affiche, pour chaque emprunt, l’année de l’emprunt extraite avec `strftime`.

## ✅ Tu sais maintenant…

- Faire des calculs dans `SELECT` (`2026 - year`, etc.)
- Concaténer du texte avec `||` (SQLite/PostgreSQL)
- Les fonctions de texte : `UPPER`, `LOWER`, `LENGTH`, `TRIM`, `SUBSTR`
- Les fonctions de date SQLite : `DATE('now')`, `strftime()`, `julianday()`
- `COALESCE(x, valeur_par_défaut)` pour gérer les `NULL`

-----

# Chapitre 12 — Fonctions d’agrégation

## Le minimum à savoir

### Le concept : compter, additionner, calculer une moyenne

Les **fonctions d’agrégation** réduisent plusieurs lignes en une seule valeur. Les 5 essentielles :

|Fonction        |Effet                                          |
|----------------|-----------------------------------------------|
|`COUNT(*)`      |Compte les lignes                              |
|`COUNT(colonne)`|Compte les valeurs **non nulles** d’une colonne|
|`SUM(colonne)`  |Additionne les valeurs                         |
|`AVG(colonne)`  |Moyenne                                        |
|`MIN(colonne)`  |Plus petite valeur                             |
|`MAX(colonne)`  |Plus grande valeur                             |

### Compter

```sql
-- Combien de lecteurs au total ?
SELECT COUNT(*) FROM readers;
-- → 15

-- Combien de lecteurs ont un email renseigné ?
SELECT COUNT(email) FROM readers;
-- → 14 (un lecteur a NULL dans email)
```

> **À retenir :** `COUNT(*)` compte **toutes les lignes**. `COUNT(colonne)` compte **uniquement les lignes où la colonne n’est pas NULL**. Cette distinction est l’une des subtilités les plus importantes du SQL.

### Additionner et moyenner

```sql
-- Année moyenne de publication
SELECT AVG(publication_year) FROM books;
-- → ~1973.5

-- Année du livre le plus ancien et du plus récent
SELECT MIN(publication_year), MAX(publication_year) FROM books;
-- → 1831, 2018
```

### Combiner plusieurs agrégations

```sql
SELECT
    COUNT(*) AS nb_livres,
    MIN(publication_year) AS plus_ancien,
    MAX(publication_year) AS plus_recent,
    AVG(publication_year) AS annee_moyenne
FROM books;
```

→ Une ligne, quatre statistiques.

### Compter avec condition

Tu peux combiner `COUNT(*)` et `WHERE` :

```sql
-- Combien de lecteurs habitent à Paris ?
SELECT COUNT(*) FROM readers WHERE city = 'Paris';
-- → 5
```

> **📋 FIL ROUGE — Épisode 11**
> 
> La directrice prépare le rapport annuel : “Donne-moi les chiffres clés.” Nora :
> 
> ```sql
> SELECT
>     COUNT(*) AS nb_lecteurs,
>     COUNT(email) AS nb_avec_email,
>     COUNT(phone) AS nb_avec_phone
> FROM readers;
> ```
> 
> Résultat : 15 lecteurs, 14 ont un email, 11 ont un téléphone. Sans `COUNT(colonne)` qui exclut les `NULL`, elle aurait dû faire trois requêtes séparées.

## Très utile en pratique

### Arrondir une moyenne

```sql
SELECT ROUND(AVG(publication_year), 0) AS annee_moyenne FROM books;
-- → 1974 (au lieu de 1973.5)
```

### `COUNT(DISTINCT col)`

Compter les valeurs **uniques** d’une colonne :

```sql
SELECT COUNT(DISTINCT city) FROM readers;
-- → 5 (le nombre de villes distinctes)
```

C’est très utile pour des analyses : combien de catégories, combien d’utilisateurs uniques, combien de pays différents…

## ❌ Erreur classique

```sql
-- Confondre COUNT(*) et COUNT(colonne)
SELECT COUNT(*) FROM readers;        -- 15 (toutes les lignes)
SELECT COUNT(email) FROM readers;    -- 14 (sans les NULL)
SELECT COUNT(phone) FROM readers;    -- 11 (sans les NULL)

-- Mélanger agrégation et colonne brute SANS GROUP BY
SELECT first_name, COUNT(*) FROM readers;    -- ❌ erreur ou résultat absurde
-- → on verra GROUP BY au prochain chapitre

-- Compter avec MAX au lieu de COUNT
SELECT MAX(id) FROM readers;
-- → renvoie l'id le plus grand, pas le nombre de lecteurs !
```

## 💡 Exercices

1. Combien de livres dans la table `books` ?
1. Quel est le livre le plus ancien (année) et le plus récent ?
1. Combien de catégories distinctes existent dans `books` ?
1. Quelle est l’année moyenne de publication ? Arrondis-la.

## ✅ Tu sais maintenant…

- Les 5 agrégations : `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- La différence cruciale : `COUNT(*)` (toutes les lignes) vs `COUNT(colonne)` (sans les NULL)
- `COUNT(DISTINCT col)` pour les valeurs uniques
- Combiner agrégations et `WHERE` pour des stats filtrées

-----

# Chapitre 13 — Regrouper avec GROUP BY

## Le minimum à savoir

### Le besoin : statistiques par catégorie

Au chapitre précédent, on a fait `COUNT(*)` sur toute la table. Mais souvent, tu veux des **statistiques par groupe** : combien de livres par catégorie ? Combien d’emprunts par lecteur ?

C’est le rôle de `GROUP BY`.

### La structure : `GROUP BY` + agrégation

```sql
SELECT category_id, COUNT(*) AS nb_livres
FROM books
GROUP BY category_id;
```

Résultat (exemple) :

|category_id |nb_livres|
|------------|---------|
|1 (Roman)   |6        |
|2 (Histoire)|2        |
|4 (BD)      |1        |
|5 (Jeunesse)|2        |
|6 (Polar)   |4        |

→ Une ligne par catégorie, avec le nombre de livres dans chacune.

### La règle d’or

Avec `GROUP BY`, **chaque colonne du `SELECT` doit être** :

- soit dans le `GROUP BY`,
- soit utilisée dans une fonction d’agrégation (`COUNT`, `SUM`, etc.).

Cette requête est correcte :

```sql
SELECT category_id, COUNT(*)
FROM books
GROUP BY category_id;
```

Celle-ci ne l’est pas (`title` n’est ni groupée ni agrégée) :

```sql
SELECT title, category_id, COUNT(*)    -- ❌
FROM books
GROUP BY category_id;
```

> **À retenir :** quand tu groupes, tu ne peux afficher que ce qui est constant dans le groupe (les colonnes du `GROUP BY`) ou un calcul sur le groupe (une agrégation). Sinon, ça n’a pas de sens — quelle valeur de `title` afficher pour la catégorie qui en contient 6 ?

### Combiner plusieurs agrégations

```sql
SELECT category_id,
       COUNT(*) AS nb_livres,
       MIN(publication_year) AS plus_ancien,
       MAX(publication_year) AS plus_recent
FROM books
GROUP BY category_id;
```

Pour chaque catégorie : le nombre, le plus ancien, le plus récent.

### Grouper sur plusieurs colonnes

```sql
-- Nombre d'emprunts par lecteur ET par statut
SELECT reader_id, status, COUNT(*) AS nb
FROM loans
GROUP BY reader_id, status;
```

Tu obtiens une ligne par couple (reader_id, status). C’est utile pour des analyses croisées.

> **📋 FIL ROUGE — Épisode 12**
> 
> La directrice : “Combien de livres a-t-on dans chaque catégorie ? On va voir si on est équilibrés.” Nora :
> 
> ```sql
> SELECT category_id, COUNT(*) AS nb_livres
> FROM books
> GROUP BY category_id
> ORDER BY nb_livres DESC;
> ```
> 
> 6 romans, 4 polars, 2 histoires, 2 jeunesse, 1 BD. La directrice constate qu’il manque cruellement de BD et de livres jeunesse — un nouvel achat est planifié.

## Très utile en pratique

### Grouper + filtrer + trier

Tu peux combiner `WHERE`, `GROUP BY` et `ORDER BY` :

```sql
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
WHERE loan_date >= '2025-01-01'         -- filtre AVANT le groupage
GROUP BY reader_id
ORDER BY nb_emprunts DESC;              -- trier les groupes
```

L’ordre est : `WHERE` filtre les lignes, puis `GROUP BY` regroupe ce qui reste, puis `ORDER BY` trie le résultat.

## ❌ Erreur classique

```sql
-- Mettre une colonne non-groupée dans le SELECT
SELECT first_name, COUNT(*)
FROM readers
GROUP BY city;     -- ❌ first_name n'est ni groupé ni agrégé
                   --    SQLite renvoie une valeur arbitraire (silencieusement)
                   --    PostgreSQL renvoie une erreur claire

-- Oublier le GROUP BY
SELECT category_id, COUNT(*) FROM books;     -- ❌ résultat bizarre
SELECT category_id, COUNT(*) FROM books GROUP BY category_id;   -- ✅
```

## 💡 Exercices

1. Combien de lecteurs habitent dans chaque ville (`city`) ?
1. Combien d’emprunts pour chaque lecteur (`reader_id`) ? Trie par nombre décroissant.
1. Pour chaque catégorie, combien de livres et quelle année moyenne de publication ?

## ✅ Tu sais maintenant…

- `GROUP BY col` regroupe les lignes par la valeur de `col`
- Chaque colonne du `SELECT` doit être soit dans `GROUP BY`, soit dans une agrégation
- Combiner `GROUP BY` avec `WHERE` (avant) et `ORDER BY` (après)
- Grouper sur plusieurs colonnes pour des analyses croisées

-----

# Chapitre 14 — Filtrer les groupes avec HAVING

## Le minimum à savoir

### Le problème : filtrer après agrégation

`WHERE` filtre les **lignes** avant le regroupement. Mais que faire si tu veux filtrer les **groupes** après calcul ?

Exemple : “Quels lecteurs ont emprunté 3 livres ou plus ?”

Tu ne peux pas écrire `WHERE COUNT(*) >= 3` — `COUNT(*)` n’existe qu’après agrégation. Il faut une autre clause : `HAVING`.

### `WHERE` vs `HAVING`

```sql
-- ❌ Ne marche pas : COUNT(*) n'est pas connu au moment du WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3
GROUP BY reader_id;

-- ✅ Correct : HAVING filtre les groupes après agrégation
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;
```

> **À retenir :** `WHERE` filtre les **lignes** (avant `GROUP BY`). `HAVING` filtre les **groupes** (après `GROUP BY`). Tu peux utiliser les deux dans la même requête — ils ne servent pas à la même chose.

### L’exemple combiné

```sql
-- Lecteurs ayant eu plus de 2 emprunts en retard
SELECT reader_id, COUNT(*) AS nb_retards
FROM loans
WHERE status = 'late'                  -- ← filtre les lignes "en retard"
GROUP BY reader_id
HAVING COUNT(*) >= 2;                  -- ← garde les lecteurs avec ≥ 2 retards
```

L’ordre logique :

1. `WHERE status = 'late'` → on ne garde que les emprunts en retard
1. `GROUP BY reader_id` → on regroupe par lecteur
1. `HAVING COUNT(*) >= 2` → on garde les groupes ayant au moins 2 retards

> **📋 FIL ROUGE — Épisode 13**
> 
> La directrice : “Identifie les lecteurs qui ont plus d’un retard. On va leur envoyer un rappel.” Nora :
> 
> ```sql
> SELECT reader_id, COUNT(*) AS nb_retards
> FROM loans
> WHERE status = 'late'
> GROUP BY reader_id
> HAVING COUNT(*) >= 2;
> ```
> 
> Elle identifie les “récidivistes”. Sans `HAVING`, elle aurait obtenu tous les lecteurs avec leur nombre de retards (y compris ceux qui en ont 1) — `HAVING` lui permet de cibler spécifiquement les problématiques.

## Très utile en pratique

### Le tableau récapitulatif

|Clause  |Filtre quoi ?       |Quand ?         |Peut utiliser des agrégations ?|
|--------|--------------------|----------------|-------------------------------|
|`WHERE` |Lignes individuelles|Avant `GROUP BY`|❌ Non                          |
|`HAVING`|Groupes             |Après `GROUP BY`|✅ Oui                          |

### Sans `GROUP BY` ?

`HAVING` peut techniquement s’utiliser sans `GROUP BY` (la table est alors traitée comme un seul groupe), mais c’est rare. Le cas standard est `GROUP BY ... HAVING ...`.

## ❌ Erreur classique

```sql
-- Mettre une condition d'agrégation dans WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3      -- ❌ COUNT(*) n'existe pas à ce stade
GROUP BY reader_id;

-- ✅ Correct
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;

-- Mettre une condition simple dans HAVING (techniquement possible mais inefficace)
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING reader_id = 1;     -- ⚠️ ça marche, mais c'est plus efficace dans WHERE

-- ✅ Plus efficace
SELECT reader_id, COUNT(*)
FROM loans
WHERE reader_id = 1
GROUP BY reader_id;
```

## 💡 Exercices

1. Quelles villes ont au moins 3 lecteurs ?
1. Quels livres ont été empruntés au moins 2 fois ?
1. Quels lecteurs ont au moins 2 emprunts encore en cours (`status = 'borrowed'`) ?

## ✅ Tu sais maintenant…

- `WHERE` filtre les lignes (avant `GROUP BY`)
- `HAVING` filtre les groupes (après `GROUP BY`)
- `HAVING` peut utiliser des fonctions d’agrégation, `WHERE` non
- Combiner les deux dans une même requête est non seulement possible mais recommandé pour les conditions appropriées

-----

# PARTIE IV — CROISER LES TABLES

-----

# Chapitre 15 — Comprendre les relations entre tables

## Le minimum à savoir

### Pourquoi croiser les tables ?

Reprenons la base. Si on veut afficher “Alice a emprunté Les Misérables le 10 janvier 2025”, l’information est répartie sur **trois tables** :

```
readers              loans                       books
┌────┬────────────┐  ┌────┬───────────┬─────────┐  ┌────┬─────────────────┐
│ id │ first_name │  │ id │ reader_id │ book_id │  │ id │ title           │
├────┼────────────┤  ├────┼───────────┼─────────┤  ├────┼─────────────────┤
│ 1  │ Alice      │  │ 1  │ 1         │ 1       │  │ 1  │ Les Misérables  │
└────┴────────────┘  └────┴───────────┴─────────┘  └────┴─────────────────┘
       ↑                       ↑           ↑                  ↑
    "Alice"              "id du lecteur"  "id du livre"   "Les Misérables"
```

Pour reconstituer la phrase complète, il faut **joindre** les tables sur leurs identifiants.

C’est ce que fait `JOIN`.

### Les types de relations

|Relation                       |Exemple                                                          |Modélisation                                |
|-------------------------------|-----------------------------------------------------------------|--------------------------------------------|
|**1-N** (un-à-plusieurs)       |Un lecteur a plusieurs emprunts                                  |Clé étrangère dans la table “côté plusieurs”|
|**N-N** (plusieurs-à-plusieurs)|Un livre a plusieurs auteurs ; un auteur a écrit plusieurs livres|Table d’**association** intermédiaire       |

### Une relation 1-N : `readers` → `loans`

Un lecteur peut avoir plusieurs emprunts, mais un emprunt appartient à un seul lecteur.

```
readers (côté "1")              loans (côté "N")
┌────┬────────────┐              ┌────┬───────────┬─────────┐
│ id │ first_name │              │ id │ reader_id │ book_id │
├────┼────────────┤              ├────┼───────────┼─────────┤
│ 1  │ Alice      │ ←──────────  │ 1  │ 1         │ 1       │
│    │            │ ←──────────  │ 3  │ 1         │ 3       │
│    │            │ ←──────────  │ 6  │ 1         │ 6       │
│ 2  │ Karim      │ ←──────────  │ 2  │ 2         │ 2       │
└────┴────────────┘              └────┴───────────┴─────────┘
```

Alice (id=1) a 3 emprunts. Karim (id=1) en a un. La clé étrangère `reader_id` dans `loans` pointe vers `readers.id`.

### Une relation N-N : `books` ↔ `authors`

Un livre peut avoir plusieurs auteurs (un livre coécrit), et un auteur peut avoir écrit plusieurs livres. On ne peut pas modéliser ça avec une simple clé étrangère — il faut une **table d’association**.

```
books                book_authors                  authors
┌────┬──────────┐   ┌─────────┬───────────┐       ┌────┬─────────────────┐
│ id │ title    │   │ book_id │ author_id │       │ id │ name            │
├────┼──────────┤   ├─────────┼───────────┤       ├────┼─────────────────┤
│ 1  │ Les Mis. │ ←─│ 1       │ 1         │──→    │ 1  │ Victor Hugo     │
│ 9  │ N-D Paris│ ←─│ 9       │ 1         │──→    │    │                 │
│ 2  │ 1984     │ ←─│ 2       │ 2         │──→    │ 2  │ George Orwell   │
└────┴──────────┘   └─────────┴───────────┘       └────┴─────────────────┘
```

La table `book_authors` ne contient que des **références** : “le livre 1 a pour auteur l’auteur 1”. Pas de doublons, pas d’incohérence — chaque relation est une ligne.

### Les tables de la base `bibliotheque.db`

|Table         |Type                            |Lien                                                                                                                                                                        |
|--------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`categories`  |Référence (catégories de livres)|—                                                                                                                                                                           |
|`authors`     |Référence (auteurs)             |—                                                                                                                                                                           |
|`books`       |Entité principale (livres)      |`category_id` → `categories.id`                                                                                                                                             |
|`book_authors`|**Association N-N**             |`book_id` → `books.id`, `author_id` → `authors.id`                                                                                                                          |
|`readers`     |Entité principale (lecteurs)    |—                                                                                                                                                                           |
|`loans`       |Association + données (emprunts)|`reader_id` → `readers.id`, `book_id` → `books.id`                                                                                                                          |
|`staff_users` |Comptes du personnel            |—                                                                                                                                                                           |
|`login_events`|Événements de connexion         |lien logique `username` → `staff_users.username`, **non contraint volontairement** (un attaquant peut tenter avec des comptes inexistants — il faut pouvoir les journaliser)|


> **📋 FIL ROUGE — Épisode 14**
> 
> Nora dessine sur un papier le schéma de la base. Elle se rend compte que c’est presque un graphe : `readers` et `books` sont reliés par `loans`. `books` et `authors` sont reliés par `book_authors`. Cette représentation visuelle l’aide énormément — elle comprend que toutes les questions vont passer par les jointures.

## Très utile en pratique

### Quand utiliser une table d’association ?

Si tu te poses la question “un X peut-il avoir plusieurs Y, et un Y plusieurs X ?” — si oui, c’est du N-N → table d’association.

Exemples classiques :

- Étudiants ↔ cours
- Films ↔ acteurs
- Articles ↔ tags
- Utilisateurs ↔ rôles

## ✅ Tu sais maintenant…

- Pourquoi les données sont réparties sur plusieurs tables
- La relation **1-N** : clé étrangère côté “plusieurs”
- La relation **N-N** : table d’association intermédiaire
- Le schéma complet de la base `bibliotheque.db`

-----

# Chapitre 16 — Première jointure avec INNER JOIN

## Le minimum à savoir

### La structure d’un `INNER JOIN`

```sql
SELECT readers.first_name, readers.last_name, loans.loan_date
FROM readers
INNER JOIN loans ON readers.id = loans.reader_id;
```

Décodage :

- `FROM readers` → table principale
- `INNER JOIN loans` → joins avec la table `loans`
- `ON readers.id = loans.reader_id` → la condition de jointure (la clé)

Le résultat : une ligne par couple (lecteur, emprunt) qui matche.

### Préfixer les colonnes par le nom de table

Quand deux tables ont une colonne du même nom (par exemple `id`), il faut **préfixer** pour lever l’ambiguïté :

```sql
SELECT readers.id, loans.id     -- préfixe obligatoire si "id" existe dans les deux
FROM readers
INNER JOIN loans ON readers.id = loans.reader_id;
```

### Les alias de table avec `AS`

Pour ne pas répéter `readers.` et `loans.` partout, on utilise des **alias courts** :

```sql
SELECT r.first_name, r.last_name, l.loan_date
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id;
```

`r` = `readers`, `l` = `loans`. Beaucoup plus lisible quand la requête grossit. Comme pour les colonnes, le `AS` est optionnel :

```sql
FROM readers r INNER JOIN loans l ON r.id = l.reader_id    -- équivalent
```

### Ce que fait vraiment `INNER JOIN`

`INNER JOIN` ne garde que les lignes qui ont une **correspondance dans les deux tables**.

Si Alice a 3 emprunts, on aura 3 lignes pour Alice dans le résultat (une par emprunt).
Si Sarah a 0 emprunt, **elle n’apparaîtra pas** dans le résultat (pas de match dans `loans`).

C’est important : `INNER JOIN` peut **filtrer implicitement** les lignes sans correspondance. Si tu veux les garder, c’est `LEFT JOIN` (Ch.17).

> **📋 FIL ROUGE — Épisode 15**
> 
> La directrice : “Donne-moi la liste des emprunts avec le nom du lecteur, pas juste son id.” Nora :
> 
> ```sql
> SELECT r.first_name, r.last_name, l.loan_date, l.status
> FROM readers AS r
> INNER JOIN loans AS l ON r.id = l.reader_id
> ORDER BY l.loan_date DESC;
> ```
> 
> Le résultat affiche les emprunts récents avec les noms — beaucoup plus exploitable que des `reader_id`.

## Très utile en pratique

### Filtrer après une jointure

Tu peux toujours ajouter un `WHERE` :

```sql
-- Emprunts d'Alice uniquement
SELECT r.first_name, r.last_name, l.loan_date, l.status
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE r.first_name = 'Alice';
```

### Trier après une jointure

```sql
-- Emprunts triés par date, du plus récent au plus ancien
SELECT r.last_name, l.loan_date
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
ORDER BY l.loan_date DESC;
```

## ❌ Erreur classique

```sql
-- Oublier le ON
SELECT * FROM readers INNER JOIN loans;
-- ❌ syntaxe incorrecte (manque ON), ou pire : produit cartésien

-- Oublier de préfixer une colonne ambiguë
SELECT id FROM readers INNER JOIN loans ON readers.id = loans.reader_id;
-- ❌ "ambiguous column: id"
SELECT readers.id FROM readers INNER JOIN loans ON readers.id = loans.reader_id;
-- ✅
```

## 💡 Exercices

1. Affiche le titre de chaque livre et le nom de sa catégorie (jointure `books` + `categories`).
1. Affiche tous les emprunts avec le nom du lecteur **et** le titre du livre (jointure `loans` + `readers` + `books`).
1. Affiche uniquement les emprunts en retard avec nom du lecteur.

## ✅ Tu sais maintenant…

- La structure : `FROM table1 INNER JOIN table2 ON condition`
- L’utilisation des alias de table (`r`, `l`, `b`…) pour la lisibilité
- `INNER JOIN` ne garde que les lignes avec correspondance dans les **deux** tables
- Combiner jointure + `WHERE` + `ORDER BY`

-----

# Chapitre 17 — LEFT JOIN et données sans correspondance

## Le minimum à savoir

### Le besoin : trouver “ce qui manque”

`INNER JOIN` est génial quand toutes les lignes ont une correspondance. Mais que faire pour répondre à des questions comme :

- “Quels lecteurs n’ont **jamais** emprunté ?”
- “Quels livres n’ont **jamais** été empruntés ?”

Avec `INNER JOIN`, ces lignes sont **invisibles** — elles n’ont pas de match. Il faut `LEFT JOIN`.

### `LEFT JOIN` : garder TOUTE la table de gauche

```sql
SELECT r.first_name, r.last_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id;
```

Le résultat contient **tous** les lecteurs — y compris ceux qui n’ont jamais emprunté. Pour ces derniers, les colonnes de `loans` sont remplies de `NULL`.

```
┌────────────┬───────────┬────────────┐
│ first_name │ last_name │ loan_date  │
├────────────┼───────────┼────────────┤
│ Alice      │ Martin    │ 2025-01-10 │
│ Alice      │ Martin    │ 2025-02-20 │   ← Alice apparaît plusieurs fois (3 emprunts)
│ Alice      │ Martin    │ 2025-04-10 │
│ Karim      │ Bernard   │ 2025-01-15 │
│ Sarah      │ Mercier   │ NULL       │   ← Sarah n'a jamais emprunté
│ Inès       │ Vincent   │ NULL       │   ← Idem
└────────────┴───────────┴────────────┘
```

### Trouver les lignes “orphelines”

C’est le cas d’usage classique : trouver les lignes de la gauche **sans correspondance** à droite. On filtre avec `WHERE ... IS NULL` :

```sql
-- Lecteurs qui n'ont JAMAIS emprunté
SELECT r.first_name, r.last_name
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.id IS NULL;
```

`l.id IS NULL` signifie “il n’y a pas eu de match dans `loans`”. Donc ce lecteur n’a pas d’emprunt.

> **C’est une technique fondamentale.** Mémorise-la — elle revient sans arrêt en SQL professionnel.

### `INNER JOIN` vs `LEFT JOIN` : quand utiliser quoi ?

|Situation                                                                    |Choix                            |
|-----------------------------------------------------------------------------|---------------------------------|
|Je veux les correspondances entre deux tables                                |`INNER JOIN`                     |
|Je veux toutes les lignes de la table principale, avec ou sans correspondance|`LEFT JOIN`                      |
|Je veux ce qui n’a pas de correspondance                                     |`LEFT JOIN` + `WHERE ... IS NULL`|


> **📋 FIL ROUGE — Épisode 16**
> 
> La directrice : “Combien de nos lecteurs n’ont jamais emprunté de livre ? On va leur faire une relance.” Nora :
> 
> ```sql
> SELECT r.first_name, r.last_name, r.email
> FROM readers AS r
> LEFT JOIN loans AS l ON r.id = l.reader_id
> WHERE l.id IS NULL;
> ```
> 
> 4 lecteurs identifiés. Avec un `INNER JOIN`, ils auraient été invisibles. C’est exactement le genre de question impossible à répondre sans maîtriser le `LEFT JOIN`.

## Très utile en pratique

### Quels livres n’ont jamais été empruntés ?

```sql
SELECT b.title
FROM books AS b
LEFT JOIN loans AS l ON b.id = l.book_id
WHERE l.id IS NULL;
```

Même technique, autre angle : la table `books` à gauche, `loans` à droite, on garde les livres sans match.

### `RIGHT JOIN` ?

Il existe aussi `RIGHT JOIN` (l’inverse de `LEFT JOIN`), mais il est rare en pratique — on inverse juste l’ordre des tables et on utilise `LEFT JOIN`. SQLite ne supporte pas `RIGHT JOIN` historiquement (ajouté en version récente). Concentre-toi sur `LEFT JOIN`.

## ❌ Erreur classique

```sql
-- Oublier WHERE ... IS NULL et croire avoir un LEFT JOIN inutile
SELECT r.first_name, l.loan_date
FROM readers r LEFT JOIN loans l ON r.id = l.reader_id;
-- → renvoie tous les emprunts ET les lecteurs sans emprunt (avec NULL)
-- → si tu voulais juste les emprunts, INNER JOIN aurait suffi

-- Mettre la condition de filtrage de la table droite dans le WHERE au lieu du ON
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.status = 'returned';
-- ⚠️ Ce WHERE filtre APRÈS la jointure, donc les lecteurs sans emprunt
--    (où l.status est NULL) sont aussi exclus → ça fait un INNER JOIN déguisé.
-- Si tu veux garder tous les lecteurs et joindre seulement leurs emprunts retournés :
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id AND l.status = 'returned';
-- ↑ la condition est dans le ON
```

## 💡 Exercices

1. Liste les livres qui n’ont jamais été empruntés.
1. Liste les auteurs qui n’ont aucun livre dans la base (jointure avec `book_authors`).
1. Pour chaque lecteur, affiche son nom et le nombre de ses emprunts (utilise `LEFT JOIN` + `COUNT` + `GROUP BY`).

## ✅ Tu sais maintenant…

- `LEFT JOIN` garde **toutes** les lignes de la table de gauche
- Les colonnes de droite sont `NULL` quand il n’y a pas de match
- La technique `LEFT JOIN ... WHERE ... IS NULL` pour trouver les lignes sans correspondance
- La différence entre `WHERE` (après jointure) et conditions dans le `ON` (pendant la jointure)

-----

# Chapitre 18 — Jointures sur plusieurs tables

## Le minimum à savoir

### Joindre 3 tables (ou plus)

On peut chaîner plusieurs `JOIN`. Exemple : afficher les emprunts avec **le nom du lecteur ET le titre du livre**.

```sql
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id;
```

Décodage :

- On part de `loans` (la table centrale)
- On joint `readers` pour récupérer les noms
- On joint `books` pour récupérer les titres

Chaque ligne du résultat combine les 3 informations.

### Joindre via une table d’association (relation N-N)

Pour afficher chaque livre avec son ou ses auteurs, il faut passer par `book_authors` :

```sql
SELECT b.title, a.name AS author_name
FROM books AS b
INNER JOIN book_authors AS ba ON b.id = ba.book_id
INNER JOIN authors AS a ON ba.author_id = a.id;
```

Si un livre a deux auteurs, il apparaîtra **deux fois** dans le résultat — une fois par auteur. C’est le comportement normal du `JOIN`.

### L’ordre des jointures

L’ordre dans lequel tu chaînes les `JOIN` n’a généralement pas d’impact sur le résultat (tant que les conditions sont correctes). Mais il a un impact sur la **lisibilité** :

```sql
-- Lisible : on part de la table "centrale" et on attache les références
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id

-- Aussi correct, mais moins naturel
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
INNER JOIN books AS b ON l.book_id = b.id
```

> **À retenir :** part de la table qui te semble centrale dans la question, puis attache les autres une par une.

> **📋 FIL ROUGE — Épisode 17**
> 
> La directrice : “Donne-moi un export complet : pour chaque emprunt, qui a emprunté, quel livre, quelle catégorie, quand.” Nora chaîne 4 jointures :
> 
> ```sql
> SELECT r.first_name, r.last_name, b.title, c.name AS categorie, l.loan_date
> FROM loans AS l
> INNER JOIN readers AS r ON l.reader_id = r.id
> INNER JOIN books AS b ON l.book_id = b.id
> INNER JOIN categories AS c ON b.category_id = c.id
> ORDER BY l.loan_date DESC;
> ```
> 
> Un seul résultat, toutes les informations utiles, prêt à exporter en CSV depuis DB Browser.

## Très utile en pratique

### Mélanger `INNER` et `LEFT`

Tu peux mélanger les types de jointures dans la même requête :

```sql
-- Tous les lecteurs, avec leurs emprunts (s'ils en ont) et le titre du livre
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
LEFT JOIN books AS b ON l.book_id = b.id
ORDER BY r.last_name;
```

Le `LEFT JOIN loans` garde tous les lecteurs. Le second `LEFT JOIN books` est important : si la première jointure renvoie `NULL` (lecteur sans emprunt), un `INNER JOIN` à `books` exclurait cette ligne. Le `LEFT JOIN` la garde.

## ❌ Erreur classique

```sql
-- Mélanger les conditions ON et WHERE de manière confuse
FROM readers r INNER JOIN loans l ON r.id = l.book_id    -- ❌ erreur de logique
                                          ↑↑↑↑
                                  devrait être l.reader_id

-- Le moteur ne renverra pas d'erreur — il fera la mauvaise jointure et tu obtiendras
-- des résultats absurdes. Toujours vérifier les conditions ON.

-- Alias incohérents
FROM loans AS l INNER JOIN readers AS r ON loans.reader_id = readers.id
-- ⚠️ Tu as défini les alias l et r, utilise-les :
ON l.reader_id = r.id    -- ✅
```

## 💡 Exercices

1. Affiche tous les emprunts avec le nom du lecteur, le titre du livre et le statut.
1. Affiche tous les livres avec leur(s) auteur(s) — un livre peut apparaître plusieurs fois s’il a plusieurs auteurs.
1. Affiche pour chaque emprunt en retard : le nom du lecteur, le titre du livre et la catégorie.

## ✅ Tu sais maintenant…

- Chaîner plusieurs `JOIN` (`INNER JOIN ... INNER JOIN ...`)
- Utiliser une table d’association pour les relations N-N
- Mélanger `INNER` et `LEFT JOIN` selon le besoin
- Toujours utiliser des alias quand tu as plus de 2 tables

-----

# Chapitre 19 — Pièges classiques des jointures

## Le minimum à savoir

Les jointures sont la partie la plus piégeuse de SQL. Ce chapitre regroupe les erreurs typiques — celles qui font que ta requête “marche” mais te donne des résultats faux. **C’est probablement le chapitre le plus important du cours pour éviter les bugs en production.**

### Piège n°1 : la jointure cartésienne

Si tu oublies la condition `ON`, ou si tu utilises l’ancienne syntaxe avec une virgule, tu obtiens un **produit cartésien** : chaque ligne de la première table est combinée avec **toutes** les lignes de la seconde.

```sql
-- Syntaxe ancienne, dangereuse
SELECT * FROM readers, loans;
-- → 15 lecteurs × 20 emprunts = 300 lignes !
-- → Toutes les combinaisons, sans aucun lien logique
```

15 × 20 = 300 lignes au lieu de 20. Avec 100 000 utilisateurs et 1 000 000 commandes, tu fais exploser la base.

> **À retenir :** **n’utilise jamais la syntaxe avec virgule** pour joindre deux tables. Toujours `INNER JOIN ... ON ...`. C’est une cause classique de “ma requête prend des heures et plante” en production.

### Piège n°2 : oublier la condition `ON`

Avec la syntaxe `JOIN` moderne, oublier le `ON` est une erreur de syntaxe (le moteur la refuse). Mais si tu utilises l’ancienne syntaxe ou si tu omets une partie de la condition, tu retombes sur un produit cartésien.

```sql
-- Erreur subtile : la condition n'est pas complète
SELECT * FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id
INNER JOIN authors a ON 1 = 1;        -- ❌ "1 = 1" est toujours vrai
-- → produit cartésien sur la jointure des auteurs !
```

### Piège n°3 : les doublons après jointure

Si tu fais une jointure sur une table N-N (comme `book_authors`), un livre avec 2 auteurs apparaîtra **2 fois**. Si tu calcules `COUNT(*)`, tu sur-compteras.

```sql
-- Combien de livres ?
SELECT COUNT(*) FROM books;
-- → 15

-- Combien de livres après jointure avec auteurs ?
SELECT COUNT(*) FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id;
-- → 16 (un livre est compté 2 fois car il a 2 auteurs co-écrits)
```

**Solution :** utilise `COUNT(DISTINCT b.id)` au lieu de `COUNT(*)` :

```sql
SELECT COUNT(DISTINCT b.id) FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id;
-- → 15
```

### Piège n°4 : confondre `WHERE` et condition de jointure

Vu au Ch.17 : mettre une condition sur la table de droite dans `WHERE` (au lieu de `ON`) transforme un `LEFT JOIN` en `INNER JOIN` déguisé.

```sql
-- ❌ Le WHERE exclut les lecteurs sans emprunt — pas l'effet voulu
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.status = 'returned';

-- ✅ Mettre la condition dans le ON pour vraiment garder tous les lecteurs
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id AND l.status = 'returned';
```

### Piège n°5 : choisir le mauvais type de jointure

|Question                                     |Bon type                             |
|---------------------------------------------|-------------------------------------|
|“Quels lecteurs ont emprunté ?”              |`INNER JOIN` (correspondances)       |
|“Liste tous les lecteurs avec leurs emprunts”|`LEFT JOIN` (tous, même sans emprunt)|
|“Quels lecteurs n’ont jamais emprunté ?”     |`LEFT JOIN ... WHERE ... IS NULL`    |

Si tu utilises `INNER JOIN` pour la 2e ou 3e question, tu **excluras silencieusement** des données sans t’en rendre compte. Toujours te poser la question “qu’est-ce qui se passe pour les lignes sans correspondance ?”.

> **📋 FIL ROUGE — Épisode 18**
> 
> Nora avait livré un rapport “Combien de livres dans la base”, après l’avoir joint à `book_authors` pour avoir aussi les auteurs. Résultat : 16 livres. La directrice s’étonne — la fois précédente, il y en avait 15. Nora cherche, comprend que le livre coécrit est compté 2 fois, et corrige avec `COUNT(DISTINCT b.id)`. Petit incident, gros enseignement.

## Très utile en pratique

### Vérifier après chaque jointure

Quand tu écris une jointure complexe, **vérifie le nombre de lignes** :

```sql
-- D'abord, compte les lignes de la table principale
SELECT COUNT(*) FROM loans;     -- 20

-- Puis le résultat après jointure : tu dois avoir 20 lignes (ou plus si N-N)
SELECT COUNT(*) FROM loans l
INNER JOIN readers r ON l.reader_id = r.id;    -- doit aussi être 20
```

Si tu as plus, tu as probablement un produit cartésien ou un doublon. Si tu as moins, tu as exclu des lignes (peut-être à tort).

## ❌ Erreur classique (synthèse)

|Erreur                                |Symptôme                             |Solution                                              |
|--------------------------------------|-------------------------------------|------------------------------------------------------|
|Syntaxe virgule sans condition        |Beaucoup trop de lignes              |Utiliser `INNER JOIN ... ON ...`                      |
|`INNER` au lieu de `LEFT`             |Lignes manquantes                    |Vérifier qui doit être dans le résultat               |
|Condition dans `WHERE` au lieu de `ON`|`LEFT JOIN` se comporte comme `INNER`|Mettre les conditions sur la table droite dans le `ON`|
|`COUNT(*)` après jointure N-N         |Surcomptage                          |Utiliser `COUNT(DISTINCT col)`                        |
|Mauvaise condition `ON`               |Résultats absurdes                   |Relire et vérifier les `id`                           |

## 💡 Exercices

1. Combien y a-t-il de **livres distincts** parmi les emprunts (jointure `loans` + `books`) ?
1. Trouve les lecteurs qui ont au moins un emprunt en retard, sans doublons (utilise `DISTINCT`).
1. Vérifie : combien de lignes y a-t-il dans `book_authors` ? Combien de livres distincts ? Pourquoi la différence ?

## ✅ Tu sais maintenant…

- Le produit cartésien et comment l’éviter
- Les doublons après jointure N-N (utilise `COUNT(DISTINCT)`)
- La différence cruciale entre condition dans `ON` et dans `WHERE`
- Comment vérifier qu’une jointure ne casse pas les données
- Les 5 grands pièges et comment les détecter

## 🧩 Capstone Partie IV — Mini-projet

Crée un rapport “activité de la médiathèque” avec :

1. Le top 5 des lecteurs les plus actifs (nom + nombre d’emprunts).
1. La liste des livres jamais empruntés.
1. Le nombre d’emprunts par catégorie de livre.
1. La liste des lecteurs avec leurs emprunts en retard (s’ils en ont).

Utilise les jointures, agrégations et `LEFT JOIN ... IS NULL` selon les questions.

-----

# PARTIE V — MODIFIER LES DONNÉES

> **⚠️ Important — À partir de cette partie, travaille sur une copie de la base.**
> 
> Les chapitres `INSERT`, `UPDATE` et `DELETE` modifient réellement les données. Avant de commencer :
> 
> - **Option simple :** copie le fichier `bibliotheque.db` en `bibliotheque_lab.db` et travaille sur la copie. Si tu casses quelque chose, tu réimportes le script du Ch.4.
> - **Option recommandée :** apprends et utilise systématiquement les transactions (`BEGIN ... ROLLBACK`) pour t’entraîner sans altérer la base. Le Ch.23 te l’apprend formellement, mais tu peux déjà l’utiliser dès maintenant.
> 
> Si tu casses la base par accident, ce n’est pas grave : il te suffit de relancer le script du Ch.4 (qui est rejouable grâce aux `DROP TABLE IF EXISTS`).

-----

# Chapitre 20 — Ajouter des données avec INSERT

## Le minimum à savoir

### La structure de base

```sql
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES ('Marie', 'Lefort', 'marie.lefort@example.com', 'Paris', '2025-12-01');
```

Décodage :

- `INSERT INTO readers` → “ajouter dans la table `readers`”
- `(first_name, last_name, email, city, registration_date)` → les colonnes que tu remplis
- `VALUES (...)` → les valeurs, **dans le même ordre** que les colonnes

### Insérer plusieurs lignes en une fois

```sql
INSERT INTO readers (first_name, last_name, email, city, registration_date)
VALUES
    ('Marie', 'Lefort', 'marie@example.com', 'Paris', '2025-12-01'),
    ('Paul', 'Dupuis', 'paul@example.com', 'Lyon', '2025-12-02'),
    ('Anne', 'Roy', NULL, 'Bordeaux', '2025-12-03');
```

Une seule requête, trois lignes ajoutées.

### Omettre des colonnes : valeurs par défaut

Tu peux omettre certaines colonnes — elles prendront leur valeur par défaut (souvent `NULL`, ou ce qui est défini dans `CREATE TABLE`).

```sql
-- email et phone ne sont pas listés → ils prendront NULL
INSERT INTO readers (first_name, last_name, city, registration_date)
VALUES ('Sophia', 'Lambert', 'Paris', '2025-12-04');
```

> **À retenir :** une colonne marquée `NOT NULL` (sans valeur par défaut) doit obligatoirement recevoir une valeur — sinon erreur.

### L’ordre des valeurs doit correspondre à l’ordre des colonnes

```sql
INSERT INTO readers (first_name, last_name, email)
VALUES ('Marie', 'Lefort', 'marie@example.com');     -- ✅ correspondance

INSERT INTO readers (first_name, last_name, email)
VALUES ('marie@example.com', 'Marie', 'Lefort');     -- ❌ ordre inversé
-- → Marie devient l'email, "Marie" devient le first_name (l'email)
-- → SQL ne détecte pas l'erreur, c'est une catastrophe silencieuse
```

> **Bonne pratique :** **toujours** lister explicitement les colonnes dans `INSERT INTO ... (...)`. Ne jamais utiliser la syntaxe sans colonnes (`INSERT INTO readers VALUES (...)`) — si la table évolue, ton script casse silencieusement.

### Que se passe-t-il si la colonne `id` n’est pas fournie ?

Pour une colonne `INTEGER PRIMARY KEY`, SQLite (et la plupart des SGBD) génère automatiquement la valeur suivante. Tu n’as pas besoin de la fournir :

```sql
INSERT INTO readers (first_name, last_name, registration_date)
VALUES ('Marie', 'Lefort', '2025-12-01');
-- → id sera attribué automatiquement (16, par exemple)
```

> **📋 FIL ROUGE — Épisode 19**
> 
> Une nouvelle famille s’inscrit à la médiathèque. Trois personnes : les deux parents et l’enfant. Nora ajoute les trois en une seule requête :
> 
> ```sql
> INSERT INTO readers (first_name, last_name, email, city, registration_date)
> VALUES
>     ('Julien', 'Mercier', 'julien.mercier@example.com', 'Saint-Cloud', '2026-05-03'),
>     ('Sandra', 'Mercier', 'sandra.mercier@example.com', 'Saint-Cloud', '2026-05-03'),
>     ('Léo', 'Mercier', NULL, 'Saint-Cloud', '2026-05-03');
> ```
> 
> Les trois nouveaux lecteurs sont enregistrés. Léo (l’enfant) n’a pas d’email — `NULL` est accepté car la colonne le permet.

## ❌ Erreur classique

```sql
-- Insérer du texte sans guillemets
INSERT INTO readers (first_name, last_name, registration_date)
VALUES (Marie, Lefort, 2025-12-01);             -- ❌ erreur ou comportement bizarre
INSERT INTO readers (first_name, last_name, registration_date)
VALUES ('Marie', 'Lefort', '2025-12-01');       -- ✅

-- Violer une contrainte NOT NULL
INSERT INTO readers (first_name, city)
VALUES ('Marie', 'Paris');         -- ❌ last_name est NOT NULL → erreur

-- Violer une contrainte UNIQUE (ex : email déjà utilisé)
INSERT INTO readers (first_name, last_name, email, registration_date)
VALUES ('Bob', 'Smith', 'alice.martin@example.com', '2025-12-01');
-- ❌ erreur si email a une contrainte UNIQUE et que cet email existe déjà
```

> **Note sur notre base de démo :** dans `readers`, la colonne `email` n’est volontairement **pas** déclarée `UNIQUE`. C’est ce qui permet d’avoir deux Alice Martin avec le même email — et d’avoir une vraie réponse à la question “quels emails sont en double ?” (Q9 du Skills Assessment). Dans une vraie application, tu mettrais probablement `UNIQUE` sur l’email pour garantir qu’il identifie un seul lecteur. C’est un choix de modélisation qui dépend du métier.

## ✅ Tu sais maintenant…

- Insérer une ligne : `INSERT INTO table (col1, col2) VALUES (val1, val2);`
- Insérer plusieurs lignes en une requête
- Omettre les colonnes optionnelles (elles prendront `NULL` ou la valeur par défaut)
- Toujours **lister explicitement** les colonnes pour éviter les surprises

-----

# Chapitre 21 — Modifier avec UPDATE

## Le minimum à savoir

### La structure de base

```sql
UPDATE readers
SET email = 'alice.martin.new@example.com'
WHERE id = 1;
```

Décodage :

- `UPDATE readers` → modifier la table `readers`
- `SET email = ...` → la colonne et sa nouvelle valeur
- `WHERE id = 1` → **uniquement** la ligne où `id = 1`

### Modifier plusieurs colonnes

```sql
UPDATE readers
SET email = 'new@example.com', city = 'Lyon'
WHERE id = 1;
```

Sépare les colonnes par des virgules dans `SET`.

### **LA RÈGLE ABSOLUE : toujours faire un `SELECT` avant**

> **⚠️ Avant tout `UPDATE`, fais TOUJOURS un `SELECT` avec le même `WHERE`** pour vérifier ce que tu vas modifier.

```sql
-- 1. Vérifier ce qu'on va modifier
SELECT * FROM readers WHERE id = 1;

-- 2. Si c'est bien la ligne attendue, modifier
UPDATE readers
SET email = 'alice.martin.new@example.com'
WHERE id = 1;
```

C’est la règle d’or. Toute personne qui a fait du SQL en production a déjà fait l’erreur de modifier toute une table en oubliant le `WHERE`. C’est ainsi qu’on perd ses données.

### L’ERREUR FATALE : oublier le `WHERE`

```sql
UPDATE readers
SET city = 'Paris';
-- ❌ ❌ ❌ MET TOUS LES LECTEURS À PARIS
```

Sans `WHERE`, SQL applique l’`UPDATE` à **toutes les lignes** de la table. Pour 15 lecteurs, c’est gênant. Pour 1 million d’utilisateurs, c’est une catastrophe — et la plupart du temps, c’est irréversible (sauf si tu travailles dans une transaction, voir Ch.23).

> **À retenir :** `UPDATE` sans `WHERE` modifie **toute la table**. C’est l’erreur n°1 en SQL. Le mécanisme de protection s’appelle… le `SELECT` préalable et la transaction.

### Modifier en se basant sur la valeur actuelle

Tu peux référencer la valeur existante dans `SET` :

```sql
-- Ajouter " (vérifié)" à la fin de tous les emails
UPDATE readers
SET email = email || ' (vérifié)'
WHERE id = 1;
```

> **📋 FIL ROUGE — Épisode 20**
> 
> Une lectrice signale qu’elle a déménagé. Nora lui demande son ancien et son nouveau nom de ville pour bien identifier. Avant de modifier, elle vérifie :
> 
> ```sql
> SELECT * FROM readers WHERE last_name = 'Martin' AND city = 'Paris';
> ```
> 
> Plusieurs lignes — il y a 2 Alice Martin ! Nora demande l’id de la lectrice et corrige :
> 
> ```sql
> SELECT * FROM readers WHERE id = 10;
> -- (vérification)
> UPDATE readers SET city = 'Toulouse' WHERE id = 10;
> ```
> 
> Une seule ligne modifiée. Sans le `SELECT` préalable, elle aurait pu modifier la mauvaise Alice.

## Très utile en pratique

### Combiner `UPDATE` et calcul

```sql
-- Marquer comme retournés tous les emprunts en retard de plus de 30 jours
UPDATE loans
SET status = 'returned', return_date = DATE('now')
WHERE status = 'late'
  AND julianday('now') - julianday(loan_date) > 30;
```

Trois choses à noter :

- On modifie deux colonnes en une fois
- La condition `WHERE` peut être complexe
- `julianday()` permet de calculer une différence de jours

## ❌ Erreur classique

```sql
-- L'erreur fatale : oublier le WHERE
UPDATE readers SET city = 'Paris';      -- ❌ ❌ ❌

-- Confondre UPDATE et SELECT
UPDATE readers WHERE id = 1 SET city = 'Lyon';   -- ❌ syntaxe incorrecte
UPDATE readers SET city = 'Lyon' WHERE id = 1;   -- ✅

-- Mettre les valeurs sans guillemets
UPDATE readers SET city = Paris WHERE id = 1;    -- ❌ "Paris" pris comme une colonne
UPDATE readers SET city = 'Paris' WHERE id = 1;  -- ✅
```

## 💡 Exercices

1. Modifie l’email du lecteur d’id 3 vers `'lea.dubois.nouveau@example.com'`. Fais d’abord un `SELECT` !
1. Marque comme `'returned'` tous les emprunts dont le `return_date` est renseigné mais qui sont encore en `'late'`.
1. Mets la ville en majuscules pour tous les lecteurs habitant à Paris (utilise `UPPER`).

## ✅ Tu sais maintenant…

- La structure : `UPDATE table SET col = val WHERE condition;`
- **TOUJOURS faire un `SELECT` avec le même `WHERE` avant**
- L’erreur fatale : `UPDATE` sans `WHERE` modifie toute la table
- Modifier plusieurs colonnes en une requête
- Référencer la valeur existante dans `SET` (`SET col = col + 1`)

-----

# Chapitre 22 — Supprimer avec DELETE

## Le minimum à savoir

### La structure de base

```sql
DELETE FROM readers
WHERE id = 1;
```

Aussi simple que dangereux. Une seule ligne, mais qui supprime définitivement.

### **LA MÊME RÈGLE ABSOLUE : `SELECT` avant `DELETE`**

> **⚠️ Avant tout `DELETE`, fais TOUJOURS un `SELECT` avec le même `WHERE`** pour vérifier ce que tu vas supprimer.

```sql
-- 1. Vérifier
SELECT * FROM readers WHERE id = 1;

-- 2. Si c'est bien la ligne attendue, supprimer
DELETE FROM readers WHERE id = 1;
```

### L’ERREUR FATALE : oublier le `WHERE`

```sql
DELETE FROM readers;
-- ❌ ❌ ❌ SUPPRIME TOUS LES LECTEURS
```

Sans `WHERE`, **toutes les lignes** de la table sont supprimées. Le contenu est perdu, la table reste (vide). Avec une transaction (Ch.23), on peut annuler. Sans transaction, c’est définitif.

### `DELETE` ne supprime pas la table

`DELETE` supprime des **lignes**, pas la table elle-même. Pour supprimer la table : `DROP TABLE` (à manier avec extrême précaution, voir Ch.24).

|Commande                          |Effet                                                |
|----------------------------------|-----------------------------------------------------|
|`DELETE FROM readers WHERE id = 1`|Supprime une ligne                                   |
|`DELETE FROM readers`             |Supprime **toutes** les lignes (la table reste, vide)|
|`DROP TABLE readers`              |Supprime la table elle-même                          |

### Le piège : les contraintes de clé étrangère

Si tu essaies de supprimer un lecteur qui a des emprunts (dans `loans`), SQL peut **refuser** la suppression à cause de la contrainte `FOREIGN KEY`. C’est une protection — sans elle, tu aurais des emprunts pointant vers un lecteur fantôme.

```sql
DELETE FROM readers WHERE id = 1;
-- ❌ "FOREIGN KEY constraint failed" si Alice a des emprunts dans loans
```

**Solutions :**

1. Supprimer d’abord les lignes liées :

```sql
DELETE FROM loans WHERE reader_id = 1;
DELETE FROM readers WHERE id = 1;
```

1. Ou, mieux, ne pas supprimer mais marquer comme inactif (**soft delete**) :

```sql
-- Hypothétique : si readers avait une colonne is_active (ce qui n'est pas le cas
-- dans notre base de démo). Dans staff_users, en revanche, cette colonne existe :
UPDATE staff_users SET is_active = 0 WHERE id = 4;
```

Cette deuxième approche est très fréquente en pratique — on garde l’historique. La table `staff_users` de notre base de démo l’illustre déjà : Olivier Bernard (id=4) a `is_active = 0`.

> **📋 FIL ROUGE — Épisode 21**
> 
> Un lecteur fantôme : un test inscrit pendant l’apprentissage de Nora a été créé par erreur. Elle veut le supprimer. D’abord, vérification :
> 
> ```sql
> SELECT * FROM readers WHERE first_name = 'Test';
> ```
> 
> Une seule ligne (id=99). Elle vérifie qu’il n’a pas d’emprunt :
> 
> ```sql
> SELECT * FROM loans WHERE reader_id = 99;
> ```
> 
> Aucune. Suppression sécurisée :
> 
> ```sql
> DELETE FROM readers WHERE id = 99;
> ```
> 
> Une ligne supprimée.

## Très utile en pratique

### Le `DELETE` conditionnel

```sql
-- Supprimer les comptes de personnel inactifs depuis plus de 2 ans
DELETE FROM staff_users
WHERE is_active = 0
  AND created_at < DATE('now', '-2 years');
```

Cette requête combine `WHERE` et calcul de date — typique d’une opération de nettoyage.

## ❌ Erreur classique

```sql
-- Oublier le WHERE
DELETE FROM readers;        -- ❌ supprime TOUS les lecteurs

-- Confondre DELETE et DROP TABLE
DELETE TABLE readers;       -- ❌ syntaxe incorrecte
DROP TABLE readers;         -- ❌ supprime la table elle-même !

-- Croire que DELETE est annulable sans transaction
-- → c'est définitif sauf si tu es dans une transaction (BEGIN ... COMMIT/ROLLBACK)
-- → voir Ch.23
```

## 💡 Exercices

1. Supprime les emprunts retournés depuis plus de 30 jours (utilise `julianday`).
1. Supprime les comptes `staff_users` inactifs (`is_active = 0`).
1. Vérifie : combien de lignes contient maintenant chaque table ?

## ✅ Tu sais maintenant…

- La structure : `DELETE FROM table WHERE condition;`
- **TOUJOURS faire un `SELECT` avant** (la règle d’or se répète)
- L’erreur fatale : `DELETE` sans `WHERE` vide la table
- Les contraintes `FOREIGN KEY` peuvent bloquer une suppression
- L’alternative “soft delete” (marquer comme inactif au lieu de supprimer)

-----

# Chapitre 23 — Transactions : BEGIN, COMMIT, ROLLBACK

## Le minimum à savoir

### Le problème : et si je me trompe ?

Tu lances un `UPDATE`, tu te rends compte 2 secondes après que tu as oublié le `WHERE`. Tu as modifié toute la table. Que faire ?

Sans transaction : **rien**. Les modifications sont permanentes.

Avec transaction : tu peux **annuler**.

### Le concept

Une **transaction** est un **bloc** de modifications qu’on valide ou qu’on annule en bloc. Tant que tu n’as pas validé, rien n’est définitif.

```sql
BEGIN;                                         -- ouvrir la transaction

UPDATE readers SET city = 'Paris' WHERE id = 1;
DELETE FROM loans WHERE id = 99;

-- À ce stade, rien n'est encore enregistré définitivement.

COMMIT;                                        -- valider (rendre permanent)
-- OU
ROLLBACK;                                      -- annuler tout
```

### Les 3 mots-clés

|Mot-clé                           |Effet                                                    |
|----------------------------------|---------------------------------------------------------|
|`BEGIN;` (ou `BEGIN TRANSACTION;`)|Ouvre une transaction                                    |
|`COMMIT;`                         |Valide tout — les modifications deviennent permanentes   |
|`ROLLBACK;`                       |Annule tout — la base revient à l’état d’avant le `BEGIN`|

### Le scénario typique

```sql
BEGIN;

-- Faire les modifications
UPDATE readers SET city = 'Lyon' WHERE id = 1;

-- Vérifier
SELECT * FROM readers WHERE id = 1;

-- Si OK :
COMMIT;

-- Si pas OK :
ROLLBACK;
```

> **À retenir :** mettre tes opérations risquées (UPDATE/DELETE/INSERT en masse) dans `BEGIN ... COMMIT` te donne un filet de sécurité. C’est la pratique professionnelle standard.

### ACID en aperçu

Les transactions garantissent les propriétés **ACID** :

|Lettre        |Signification         |Ce que ça veut dire                                        |
|--------------|----------------------|-----------------------------------------------------------|
|**A**tomicité |“Tout ou rien”        |Soit toutes les modifs sont appliquées, soit aucune        |
|**C**ohérence |Règles respectées     |La base reste valide (contraintes respectées)              |
|**I**solation |Pas d’interférence    |Plusieurs transactions parallèles ne se voient pas en cours|
|**D**urabilité|Permanent après COMMIT|Une fois commité, ça reste — même en cas de crash          |


> **À retenir :** ACID c’est la garantie offerte par tout SGBD relationnel sérieux. C’est ce qui te permet de faire des virements bancaires sans qu’une coupure de courant ne crée d’incohérence.

> **📋 FIL ROUGE — Épisode 22**
> 
> Nora doit faire un nettoyage : marquer comme `'returned'` une vingtaine d’emprunts anciens, et supprimer 5 lecteurs de test. Elle ouvre une transaction :
> 
> ```sql
> BEGIN;
> UPDATE loans SET status = 'returned', return_date = '2024-12-31' WHERE status = 'late' AND loan_date < '2024-06-01';
> DELETE FROM readers WHERE first_name = 'Test';
> -- Vérification
> SELECT COUNT(*) FROM loans WHERE status = 'late';
> SELECT COUNT(*) FROM readers WHERE first_name = 'Test';
> -- Tout est bon
> COMMIT;
> ```
> 
> Si elle avait constaté une erreur, `ROLLBACK` aurait tout annulé. Filet de sécurité activé.

## Très utile en pratique

### Quand utiliser une transaction ?

|Opération                                                            |Transaction recommandée ?|
|---------------------------------------------------------------------|-------------------------|
|`SELECT` simple                                                      |Non                      |
|`INSERT` ponctuel                                                    |Optionnel                |
|`UPDATE` ou `DELETE` sur plusieurs lignes                            |**Oui**                  |
|Plusieurs modifications liées (ex : transfert d’un compte à un autre)|**Oui, obligatoire**     |
|Migration de données, refonte de la base                             |**Oui, obligatoire**     |

### Le cas d’école : le transfert bancaire

```sql
BEGIN;
UPDATE comptes SET solde = solde - 100 WHERE id = 1;     -- débite Alice
UPDATE comptes SET solde = solde + 100 WHERE id = 2;     -- crédite Bob
COMMIT;
```

Si la deuxième requête échoue (panne, erreur), un `ROLLBACK` annule la première. **Sans transaction**, Alice perdrait 100€ et Bob ne les recevrait pas — l’argent disparaîtrait.

C’est pour ça que toutes les applications financières utilisent des transactions.

## ❌ Erreur classique

```sql
-- Oublier le COMMIT (les modifs ne sont pas enregistrées définitivement)
BEGIN;
UPDATE readers SET city = 'Paris' WHERE id = 1;
-- (la session se ferme sans COMMIT)
-- → les modifications sont annulées par le SGBD au moment de la déconnexion

-- Faire un COMMIT accidentel à la place de ROLLBACK
BEGIN;
DELETE FROM readers;        -- ❌ erreur ! Toute la table
COMMIT;                      -- ❌ ❌ tu valides l'erreur
-- → trop tard, c'est permanent (sauf sauvegarde)

-- Bonne pratique : faire un SELECT après les modifs et avant le COMMIT
BEGIN;
UPDATE readers SET city = 'Paris' WHERE last_name = 'Martin';
SELECT * FROM readers WHERE last_name = 'Martin';   -- vérifier
COMMIT;   -- ou ROLLBACK selon le résultat
```

## 💡 Exercices

1. Ouvre une transaction. Insère un nouveau lecteur. Vérifie avec un `SELECT`. Annule avec `ROLLBACK`. Vérifie qu’il n’est plus là.
1. Refais la même chose, mais cette fois `COMMIT`. Vérifie qu’il est bien là après.
1. Ouvre une transaction, supprime tous les emprunts retournés (`DELETE FROM loans WHERE status = 'returned'`), regarde le nombre de lignes restantes, puis `ROLLBACK`. Vérifie que la base est revenue à l’état initial.

## ✅ Tu sais maintenant…

- Une transaction est un bloc `BEGIN ... COMMIT;` (ou `ROLLBACK;`)
- `BEGIN` ouvre, `COMMIT` valide définitivement, `ROLLBACK` annule
- Les transactions sont ton filet de sécurité pour les opérations risquées
- Les propriétés **ACID** : Atomicité, Cohérence, Isolation, Durabilité
- Toutes les applications critiques utilisent des transactions

-----

# PARTIE VI — CRÉER ET STRUCTURER UNE BASE

-----

# Chapitre 24 — Créer une table avec CREATE TABLE

## Le minimum à savoir

### La structure de base

```sql
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    city TEXT
);
```

Décodage :

- `CREATE TABLE readers` → crée une table nommée `readers`
- `(...)` → la liste des colonnes
- Pour chaque colonne : un nom, un type, et éventuellement des contraintes

### Anatomie d’une définition de colonne

```
nom_colonne    TYPE       contrainte1 contrainte2 ...
─────────────  ─────────  ───────────────────────
first_name     TEXT       NOT NULL
id             INTEGER    PRIMARY KEY
email          TEXT       UNIQUE
status         TEXT       DEFAULT 'borrowed'
```

### Supprimer une table : `DROP TABLE`

```sql
DROP TABLE readers;        -- ❌ ❌ ❌ supprime DÉFINITIVEMENT la table et toutes ses données
```

> **⚠️ Extrême prudence avec `DROP TABLE`**. Contrairement à `DELETE`, qui ne supprime que les lignes, `DROP TABLE` détruit la structure elle-même. Sans sauvegarde, c’est irréversible.

### Modifier une table existante : `ALTER TABLE`

```sql
ALTER TABLE readers ADD COLUMN birth_date TEXT;        -- ajouter une colonne
ALTER TABLE readers RENAME TO members;                  -- renommer la table
```

> **Note :** SQLite a longtemps eu un support limité de `ALTER TABLE` (pas de `DROP COLUMN` jusqu’en SQLite 3.35). C’est l’un des points où les SGBD diffèrent. Pour ce cours, on se concentre sur `CREATE TABLE`.

### `IF NOT EXISTS` : créer seulement si la table n’existe pas

```sql
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL
);
```

Pratique pour les scripts d’initialisation : si la table existe déjà, on ne tente pas de la recréer (et donc pas d’erreur).

> **📋 FIL ROUGE — Épisode 23**
> 
> La directrice veut ajouter une fonctionnalité : suivre les **événements organisés** par la médiathèque (ateliers, conférences, club de lecture). Nora crée une nouvelle table :
> 
> ```sql
> CREATE TABLE events (
>     id INTEGER PRIMARY KEY,
>     title TEXT NOT NULL,
>     event_date TEXT NOT NULL,
>     max_participants INTEGER DEFAULT 20,
>     description TEXT
> );
> ```
> 
> Une table avec sa clé primaire, des contraintes simples, et une valeur par défaut. La structure est faite — il reste à insérer des données et à l’utiliser.

## ❌ Erreur classique

```sql
-- Oublier les virgules entre colonnes
CREATE TABLE readers (
    id INTEGER PRIMARY KEY
    first_name TEXT NOT NULL              -- ❌ pas de virgule après PRIMARY KEY
);

-- Mettre une virgule en trop après la dernière colonne
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,            -- ❌ virgule de trop
);

-- Confondre DROP TABLE et DELETE
DROP TABLE readers;       -- détruit la table
DELETE FROM readers;       -- vide la table mais la garde
```

## ✅ Tu sais maintenant…

- Créer une table avec `CREATE TABLE nom (colonne TYPE contrainte, ...)`
- Supprimer une table avec `DROP TABLE` (irréversible !)
- `IF NOT EXISTS` pour les scripts d’initialisation
- `ALTER TABLE` pour modifier (de manière limitée en SQLite)

-----

# Chapitre 25 — Types de données et contraintes

## Le minimum à savoir

### Les types de données SQLite

SQLite utilise un système de types simple, dit “à classes de stockage” :

|Type     |Contenu                                           |
|---------|--------------------------------------------------|
|`INTEGER`|Nombre entier (`5`, `-12`, `42000`)               |
|`REAL`   |Nombre décimal (`3.14`, `1.5`, `-0.001`)          |
|`TEXT`   |Chaîne de caractères (`'Bonjour'`, `'2026-05-03'`)|
|`BLOB`   |Données binaires (image, fichier — rare)          |
|`NULL`   |Absence de valeur                                 |

Pour les **dates**, SQLite n’a pas de type dédié — on utilise `TEXT` au format `'YYYY-MM-DD'` ou `'YYYY-MM-DD HH:MM:SS'`. C’est suffisant pour 99% des cas.

> **Note :** PostgreSQL et MySQL ont des types plus stricts (`VARCHAR(50)`, `DATE`, `TIMESTAMP`, `BOOLEAN`…). En SQLite, c’est plus laxiste — un peu comme Python par rapport à C. Tu reverras les vrais types fixes quand tu passeras à un autre SGBD.

### Les contraintes essentielles

|Contrainte                               |Effet                                      |
|-----------------------------------------|-------------------------------------------|
|`PRIMARY KEY`                            |Identifiant unique de la table             |
|`NOT NULL`                               |Valeur obligatoire (pas de NULL)           |
|`UNIQUE`                                 |Toutes les valeurs doivent être différentes|
|`DEFAULT valeur`                         |Valeur par défaut si non fournie           |
|`CHECK (condition)`                      |Règle de validation personnalisée          |
|`FOREIGN KEY (col) REFERENCES table(col)`|Clé étrangère vers une autre table         |

### Exemple complet

```sql
CREATE TABLE loans (
    id INTEGER PRIMARY KEY,
    reader_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL DEFAULT 'borrowed',
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (status IN ('borrowed', 'returned', 'late'))
);
```

Ce que ça garantit :

- `id` : identifiant unique automatique
- `reader_id`, `book_id`, `loan_date` : ne peuvent pas être `NULL`
- `return_date` : peut être `NULL` (pour les emprunts en cours)
- `status` : si non fourni, vaut `'borrowed'` ; et ne peut être que `'borrowed'`, `'returned'` ou `'late'` (grâce au `CHECK`)
- Les `reader_id` et `book_id` doivent exister respectivement dans `readers.id` et `books.id`

### Pourquoi les contraintes sont cruciales

Sans contraintes, ta base se remplit de données incohérentes :

- Des emprunts qui pointent vers des lecteurs qui n’existent pas
- Des `status` avec des valeurs comme `'lost'`, `'pending'`, `'???'`, `''`, `NULL`…
- Des emails dupliqués sur 12 utilisateurs différents
- Des dates au format `'15/03/2025'` mélangées avec `'2025-03-15'`

Les contraintes forcent la qualité dès l’**écriture** — c’est beaucoup mieux que de nettoyer après coup.

> **À retenir :** chaque fois que tu crées une table, demande-toi pour chaque colonne : peut-elle être vide ? Doit-elle être unique ? Y a-t-il une valeur par défaut sensée ? Y a-t-il un lien vers une autre table ?

> **📋 FIL ROUGE — Épisode 24**
> 
> La directrice veut ajouter un système de réservation. Nora conçoit la table avec contraintes :
> 
> ```sql
> CREATE TABLE reservations (
>     id INTEGER PRIMARY KEY,
>     reader_id INTEGER NOT NULL,
>     book_id INTEGER NOT NULL,
>     reservation_date TEXT NOT NULL DEFAULT (DATE('now')),
>     status TEXT NOT NULL DEFAULT 'pending',
>     FOREIGN KEY (reader_id) REFERENCES readers(id),
>     FOREIGN KEY (book_id) REFERENCES books(id),
>     CHECK (status IN ('pending', 'fulfilled', 'cancelled'))
> );
> ```
> 
> Cette table est **autoprotégée** : impossible d’insérer un statut farfelu, impossible de réserver pour un lecteur qui n’existe pas. La qualité des données est garantie par la structure.

## Très utile en pratique

### `PRIMARY KEY` composite

Pour une table d’association comme `book_authors`, la clé primaire combine deux colonnes :

```sql
CREATE TABLE book_authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),     -- combinaison unique
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
```

Un même couple `(book_id, author_id)` ne peut pas apparaître deux fois — pas de doublon possible.

## ❌ Erreur classique

```sql
-- Oublier NOT NULL sur une colonne qui ne devrait jamais être vide
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT          -- ⚠️ peut être NULL → un user sans email passe
);

-- Oublier UNIQUE sur une colonne qui devrait l'être
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL  -- ⚠️ deux users peuvent avoir le même email
);
-- ✅
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);

-- Oublier la FOREIGN KEY (alors la cohérence n'est pas garantie)
CREATE TABLE loans (
    reader_id INTEGER       -- ⚠️ peut pointer vers un id inexistant
);
```

## 💡 Exercices

1. Crée une table `categories_v2` avec `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL UNIQUE`, et `description TEXT`.
1. Crée une table `subscriptions` (abonnements payants des lecteurs) avec `id`, `reader_id` (FK vers `readers`), `start_date`, `end_date`, `subscription_type` (avec `CHECK` sur 3 valeurs autorisées : ‘monthly’, ‘yearly’, ‘lifetime’).
1. Insère deux lignes valides dans `subscriptions`. Tente une 3e avec un type non autorisé — observe l’erreur.

## ✅ Tu sais maintenant…

- Les types SQLite : `INTEGER`, `REAL`, `TEXT`, `BLOB`
- Les contraintes : `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY`
- Les contraintes garantissent la qualité des données dès l’écriture
- `PRIMARY KEY` composite pour les tables d’association

-----

# Chapitre 26 — Modélisation simple

## Le minimum à savoir

### Le défi : passer d’un besoin métier à des tables

Quand on dit “je veux gérer une médiathèque”, il faut traduire ça en :

- Quelles **entités** principales ?
- Quels **attributs** pour chaque entité ?
- Quelles **relations** entre les entités ?

C’est l’exercice de **modélisation**.

### La méthode en 4 étapes

**Étape 1 — Identifier les entités principales**

Une entité = une “chose” du monde réel qu’on veut suivre.

Pour la médiathèque :

- Lecteurs
- Livres
- Auteurs
- Catégories

Chaque entité devient une **table**.

**Étape 2 — Lister les attributs de chaque entité**

Un attribut = une caractéristique. Chaque attribut devient une **colonne**.

`readers` :

- `first_name`, `last_name`, `email`, `city`, `phone`, `registration_date`

`books` :

- `title`, `publication_year`, `isbn`

**Étape 3 — Identifier les relations**

- Un livre appartient à **une** catégorie → relation 1-N → clé étrangère `category_id` dans `books`
- Un livre peut avoir **plusieurs** auteurs, et un auteur **plusieurs** livres → relation N-N → table d’association `book_authors`
- Un lecteur peut faire **plusieurs** emprunts, et un emprunt concerne **un** livre et **un** lecteur → table `loans` avec `reader_id` et `book_id`

**Étape 4 — Ajouter une clé primaire à chaque table**

Toujours `id INTEGER PRIMARY KEY`.

### Trois principes simples

1. **Chaque entité a sa table.** N’écrase pas plusieurs entités dans une seule table.
1. **Pas de répétition d’information.** Si tu te retrouves à recopier le même nom 50 fois, sépare en deux tables.
1. **Une cellule = une seule valeur.** Pas de “Hugo, Camus, Orwell” dans une cellule — utilise une table d’association.

> **À retenir :** ces trois principes correspondent à la **première forme normale (1NF)** de la théorie relationnelle. On en reste là — les formes 2NF et 3NF sont des raffinements utiles mais pas indispensables pour débuter.

### Aperçu des formes normales

|Forme|Idée                        |Exemple                                                |
|-----|----------------------------|-------------------------------------------------------|
|1NF  |Une cellule = une valeur    |Pas de “Hugo, Orwell” dans une cellule                 |
|2NF  |Une table = un sujet        |Pas mélanger lecteurs et emprunts dans la même table   |
|3NF  |Pas de dépendance transitive|Stocker `category_id` dans `books`, pas `category_name`|


> **Pour aller plus loin :** la modélisation poussée (UML, MCD, MLD, formes normales BCNF/4NF/5NF) est un sujet de cours dédié. Pour démarrer, retiens les 3 principes ci-dessus — ils couvrent 95% des cas.

> **📋 FIL ROUGE — Épisode 25**
> 
> La directrice veut ajouter le suivi des **dons de livres** par les lecteurs. Nora applique la méthode :
> 
> 1. **Entité** : un don
> 1. **Attributs** : qui a donné ? quel livre ? quand ? statut (accepté/refusé/en attente) ?
> 1. **Relations** : un don concerne un lecteur (1-N depuis `readers`) et peut concerner un livre (référence vers `books` une fois accepté)
> 
> Sa table :
> 
> ```sql
> CREATE TABLE donations (
>     id INTEGER PRIMARY KEY,
>     donor_reader_id INTEGER NOT NULL,
>     proposed_title TEXT NOT NULL,
>     book_id INTEGER,
>     donation_date TEXT NOT NULL,
>     status TEXT NOT NULL DEFAULT 'pending',
>     FOREIGN KEY (donor_reader_id) REFERENCES readers(id),
>     FOREIGN KEY (book_id) REFERENCES books(id),
>     CHECK (status IN ('pending', 'accepted', 'refused'))
> );
> ```
> 
> Le `book_id` est nullable : tant que le don n’est pas accepté, il n’y a pas de livre dans le catalogue. Modélisation propre.

## Très utile en pratique

### Quand séparer ou non ?

**Sépare** quand :

- Une entité existe **indépendamment** (un auteur existe même s’il n’a écrit qu’un livre)
- Tu vas avoir des **relations N-N** (livres ↔ auteurs)
- Tu auras des **statistiques par groupe** (livres par catégorie)

**Garde dans une seule table** quand :

- L’attribut est trivial (une simple colonne `city` dans `readers` suffit — pas besoin de table `cities`)
- Il n’y a pas de duplication problématique

### Le piège des “vraies” et “fausses” duplications

Stocker “Paris” 100 fois dans la colonne `city` de `readers` n’est **pas** une duplication problématique — c’est juste de la donnée. Mais stocker `"Paris, France"` 100 fois si tu as déjà une table `countries` avec `France` dedans, c’est un problème (3NF).

Pour démarrer, sois pragmatique : une simple colonne `city` suffit. Tu sépareras en table `cities` le jour où tu en auras besoin (statistiques, géolocalisation, multi-langue…).

## ✅ Tu sais maintenant…

- Identifier les entités, attributs et relations à partir d’un besoin métier
- Les 3 principes : une entité = une table, pas de répétition, une cellule = une valeur
- L’aperçu des formes normales (1NF, 2NF, 3NF)
- Quand séparer ou non en plusieurs tables

## 🧩 Capstone Partie VI — Mini-projet

La médiathèque veut un système d’**ateliers** payants pour les lecteurs. Chaque atelier a un titre, une description, une date, un nombre maximum de participants, un prix. Les lecteurs peuvent s’inscrire à plusieurs ateliers, et un atelier peut avoir plusieurs participants.

**Tâche :**

1. Identifie les entités, attributs et relations.
1. Crée les tables nécessaires avec contraintes.
1. Insère 3 ateliers et 5 inscriptions.
1. Écris une requête qui affiche pour chaque atelier le nombre d’inscrits actuels.

-----

# PARTIE VII — POUR ALLER PLUS LOIN — 🔴 BONUS

> **Important :** cette partie est **bonus**. Tu peux finir le cœur du cours (Ch.1-26) et le Skills Assessment (Ch.31) sans elle. Reviens ici quand tu te sens à l’aise avec les bases — ces chapitres enrichissent la pratique mais ne la conditionnent pas.

-----

# Chapitre 27 — Bonnes pratiques SQL et vues

## Le minimum à savoir

### Les bonnes pratiques d’écriture

Une requête lisible, c’est une requête qu’on peut **comprendre, déboguer et modifier** sans douleur. Quelques règles simples :

**1. Indenter et aérer**

```sql
-- ❌ Illisible
SELECT r.first_name,r.last_name,b.title,l.loan_date FROM loans l INNER JOIN readers r ON l.reader_id=r.id INNER JOIN books b ON l.book_id=b.id WHERE l.status='late' ORDER BY l.loan_date DESC;

-- ✅ Lisible
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status = 'late'
ORDER BY l.loan_date DESC;
```

**2. Mots-clés SQL en MAJUSCULES**, noms de tables/colonnes en minuscules.

**3. Alias courts et significatifs** : `r` pour `readers`, `b` pour `books`, `l` pour `loans`.

**4. Éviter `SELECT *` dans les requêtes finales** — préfère lister les colonnes nécessaires.

**5. Commenter les requêtes complexes**

```sql
-- Lecteurs ayant emprunté plus de 3 livres en 2025
-- (utilisé pour les invitations à la soirée des grands lecteurs)
SELECT r.first_name, r.last_name, COUNT(*) AS nb_emprunts_2025
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE l.loan_date >= '2025-01-01'
GROUP BY r.id, r.first_name, r.last_name
HAVING COUNT(*) > 3;
```

**6. Toujours faire un `SELECT` avant `UPDATE` ou `DELETE`** (rappelé au Ch.21-22).

**7. Utiliser des transactions** pour les modifications importantes (Ch.23).

**8. Limiter les résultats avec `LIMIT`** quand tu explores.

### Les vues : enregistrer une requête sous un nom

Une **vue** (view) est une requête enregistrée que tu peux utiliser comme une table. Elle ne stocke pas de données — elle exécute la requête sous-jacente à chaque appel.

```sql
-- Créer une vue
CREATE VIEW active_loans AS
SELECT r.first_name, r.last_name, b.title, l.loan_date, l.status
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status IN ('borrowed', 'late');

-- L'utiliser comme une table
SELECT * FROM active_loans;
SELECT * FROM active_loans WHERE status = 'late';
```

**Pourquoi c’est utile :**

- Simplifier les requêtes complexes pour les utilisateurs
- Éviter de réécrire la même jointure 50 fois
- Masquer la complexité du schéma sous-jacent

**Limites :**

- Une vue n’**accélère pas** les requêtes — c’est juste une simplification d’écriture
- Modifier les données **à travers** une vue est limité et dépend du SGBD

> **À retenir :** les vues sont un outil de **lisibilité**, pas de performance. Pour la performance, on utilise les **index** (Ch.28).

### Supprimer une vue

```sql
DROP VIEW active_loans;
```

> **📋 FIL ROUGE — Épisode 26**
> 
> Nora se rend compte qu’elle écrit la même requête (lecteurs + livres + emprunts) dix fois par jour, légèrement adaptée à chaque fois. Elle crée une vue :
> 
> ```sql
> CREATE VIEW v_loans_full AS
> SELECT l.id, r.first_name, r.last_name, b.title, c.name AS category, l.loan_date, l.status
> FROM loans AS l
> INNER JOIN readers AS r ON l.reader_id = r.id
> INNER JOIN books AS b ON l.book_id = b.id
> INNER JOIN categories AS c ON b.category_id = c.id;
> ```
> 
> Maintenant, n’importe quelle question sur les emprunts se résume à `SELECT ... FROM v_loans_full WHERE ...`. Plus simple, plus rapide à écrire, et l’équipe peut l’utiliser sans connaître le détail des jointures.

## ✅ Tu sais maintenant…

- Les bonnes pratiques d’écriture (indentation, majuscules, alias, commentaires)
- Les vues comme requêtes enregistrées (`CREATE VIEW`, `DROP VIEW`)
- Les vues simplifient l’écriture mais n’accélèrent pas les requêtes

-----

# Chapitre 28 — Index et performance : introduction

## Le minimum à savoir

### Pourquoi une requête est-elle parfois lente ?

Quand tu écris `SELECT * FROM readers WHERE email = 'alice@example.com'`, le moteur doit parcourir **toutes les lignes** de la table pour trouver celles qui correspondent. Sur 15 lignes, c’est instantané. Sur 10 millions, c’est très lent.

**L’index** est la solution.

### L’analogie du livre

Imagine un livre de 1000 pages. Tu cherches le mot “transaction”.

- **Sans index** : tu parcours toutes les pages une par une.
- **Avec un index** (à la fin du livre) : tu vas directement à la page indiquée.

Un **index SQL** fonctionne pareil — c’est une structure annexe qui pointe rapidement vers les lignes contenant une certaine valeur.

### Créer un index

```sql
CREATE INDEX idx_readers_email
ON readers(email);
```

Décodage :

- `CREATE INDEX idx_readers_email` → un index nommé (par convention : `idx_table_colonne`)
- `ON readers(email)` → sur la colonne `email` de la table `readers`

Maintenant, `SELECT * FROM readers WHERE email = 'alice@example.com'` est ultra-rapide même avec des millions de lignes.

### Les colonnes naturellement indexées

|Colonne                   |Indexée par défaut ?         |
|--------------------------|-----------------------------|
|`PRIMARY KEY`             |✅ Oui, automatiquement       |
|`UNIQUE`                  |✅ Oui, automatiquement       |
|Colonne avec `FOREIGN KEY`|❌ Non, à indexer manuellement|
|Colonnes ordinaires       |❌ Non                        |


> **À retenir :** les clés primaires et `UNIQUE` sont déjà indexées. Pour le reste — surtout les clés étrangères et les colonnes souvent filtrées — il faut créer l’index manuellement.

### Quand créer un index ?

**Bonnes raisons :**

- Une colonne est souvent dans le `WHERE`
- Une colonne est souvent dans les conditions `JOIN ... ON`
- Une colonne est souvent dans `ORDER BY`

**Mauvaises raisons :**

- “Au cas où” → un index a un coût (voir ci-dessous)
- Indexer toutes les colonnes → ralentit énormément les écritures

### Le coût d’un index

Un index a deux coûts :

1. **Espace disque** : l’index est une structure annexe qui prend de la place
1. **Ralentissement des écritures** : à chaque `INSERT`/`UPDATE`/`DELETE`, l’index doit être mis à jour

Sur les bases en lecture quasi-exclusive, indexer généreusement. Sur les bases en écriture intensive, indexer parcimonieusement. C’est un arbitrage classique.

### Mention : `EXPLAIN QUERY PLAN`

SQLite (et tous les SGBD) ont une commande pour voir comment une requête sera exécutée :

```sql
EXPLAIN QUERY PLAN
SELECT * FROM readers WHERE email = 'alice@example.com';
```

Le résultat te dit si l’index est utilisé. C’est utile pour le debug de performance, mais c’est un sujet plus avancé — on le mentionne ici, on n’en fait pas plus.

> **📋 FIL ROUGE — Épisode 27**
> 
> La base est encore petite, mais Nora anticipe sa croissance. Elle ajoute deux index sur les colonnes les plus filtrées :
> 
> ```sql
> CREATE INDEX idx_loans_reader_id ON loans(reader_id);
> CREATE INDEX idx_loans_book_id ON loans(book_id);
> ```
> 
> Désormais, les jointures `loans` ↔ `readers` et `loans` ↔ `books` seront rapides même avec 100 000 emprunts.

## ❌ Erreur classique

```sql
-- Croire qu'indexer tout est gratuit
-- → Sur une table avec 50 colonnes, tu ne crées pas 50 index !
-- → Indexer ce qui est *réellement* utilisé dans WHERE / JOIN / ORDER BY

-- Oublier d'indexer une FOREIGN KEY
-- → Les jointures sur cette colonne seront lentes
-- → Toujours indexer les FK que tu joindras

-- Croire qu'un index sur (a, b) accélère un WHERE b = ...
-- → Un index composite est ordonné — il accélère a, ou (a, b), mais pas b seul
```

## ✅ Tu sais maintenant…

- Un index accélère les recherches comme l’index d’un livre
- Les `PRIMARY KEY` et `UNIQUE` sont auto-indexées
- Les `FOREIGN KEY` ne le sont **pas** par défaut — à indexer manuellement
- Un index a un coût (espace + écritures)
- `EXPLAIN QUERY PLAN` permet de vérifier l’utilisation des index

-----

# Chapitre 29 — Sécurité et SQL injection : aperçu défensif

> **Cadre de ce chapitre :** les exemples ci-dessous servent uniquement à comprendre le mécanisme de la vulnérabilité pour mieux s’en protéger. Ils ne doivent être testés que dans un environnement de lab personnel (ta propre base SQLite). Tester l’injection SQL sur un système qui ne t’appartient pas est illégal.

## Le minimum à savoir

### Le problème : entrée utilisateur + concaténation

Imagine une application web qui cherche un livre par titre. L’utilisateur tape `Harry Potter` dans un formulaire, et le code construit une requête comme ça :

```python
# Code DANGEREUX (à NE PAS faire)
recherche = "Harry Potter"
requete = "SELECT * FROM books WHERE title = '" + recherche + "'"
```

La requête devient : `SELECT * FROM books WHERE title = 'Harry Potter'`. Tout va bien.

**Mais que se passe-t-il si l’utilisateur tape :**

```
' OR '1'='1
```

La requête devient : `SELECT * FROM books WHERE title = '' OR '1'='1'`. Comme `'1'='1'` est toujours vrai, **tous les livres sont retournés**. C’est l’**injection SQL** la plus simple.

Pire encore, avec une entrée comme :

```
'; DROP TABLE books; --
```

La requête devient : `SELECT * FROM books WHERE title = ''; DROP TABLE books; --'`. Le `;` clôt la première requête, le `DROP TABLE` détruit la table, et le `--` commente le reste. **La table `books` disparaît.**

### Pourquoi c’est dangereux ?

L’injection SQL permet à un attaquant de :

- **Lire** des données qu’il ne devrait pas voir (mots de passe, données privées)
- **Modifier** des données (s’élever en admin, fausser des comptes)
- **Supprimer** des tables entières
- **Exécuter** des commandes selon le SGBD

C’est l’une des vulnérabilités web les plus anciennes et les plus répandues — encore aujourd’hui dans le top 10 OWASP.

### La solution : les requêtes préparées

Au lieu de **concaténer** l’entrée utilisateur, on utilise des **paramètres** (placeholders). Le moteur SQL traite l’entrée comme une **valeur**, jamais comme du code.

```python
# Code SÛR (à faire)
recherche = "Harry Potter"
cursor.execute(
    "SELECT * FROM books WHERE title = ?",
    (recherche,)
)
```

Le `?` est un placeholder. La valeur passée comme tuple `(recherche,)` est traitée comme une chaîne, **pas interprétée comme du SQL**. Même si l’utilisateur tape `' OR '1'='1`, la chaîne complète est cherchée comme titre — aucune injection possible.

> **À retenir :** **ne concatène jamais d’entrée utilisateur dans une requête SQL**. Utilise toujours les paramètres de ton driver (`?` en SQLite, `%s` en PostgreSQL Python, `?` ou `:name` ailleurs). C’est la règle n°1 de la sécurité SQL.

### Les autres bonnes pratiques

**Le principe de moindre privilège** : un compte applicatif ne devrait avoir que les permissions strictement nécessaires. Le compte qui sert le site web n’a pas besoin de pouvoir `DROP TABLE` ou `CREATE USER`.

**La validation côté application** : vérifier le format de l’entrée (un email ressemble-t-il à un email ? une date est-elle valide ?) avant de la passer à SQL. C’est une couche de défense supplémentaire.

**La journalisation** : enregistrer les requêtes (ou au moins celles qui échouent) permet de détecter une attaque en cours. C’est ce que fait la table `login_events` dans notre base.

> **📋 FIL ROUGE — Épisode 28**
> 
> Nora regarde la table `login_events` et constate quelque chose d’étrange :
> 
> ```sql
> SELECT username,
>        COUNT(*) AS nb_tentatives,
>        SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS echecs
> FROM login_events
> GROUP BY username
> ORDER BY echecs DESC;
> ```
> 
> Le compte `admin` a **10 échecs** suivis d’une **réussite**, tous depuis l’IP `203.0.113.42`. C’est le pattern typique d’une attaque par **brute-force réussie**. Nora alerte la directrice et bloque immédiatement le compte. Un audit est déclenché.
> 
> *Sans la journalisation des connexions et la capacité d’analyse SQL, cette attaque serait passée inaperçue.*

## Très utile en pratique

### Détecter une attaque par brute-force

```sql
-- Comptes ayant subi plus de 5 échecs en moins de 10 minutes
SELECT username, ip_address, COUNT(*) AS nb_echecs,
       MIN(event_time) AS premier, MAX(event_time) AS dernier
FROM login_events
WHERE success = 0
GROUP BY username, ip_address
HAVING COUNT(*) >= 5
   AND julianday(MAX(event_time)) - julianday(MIN(event_time)) < 0.007;     -- ~10 min
```

C’est une requête de détection typique en cybersécurité. Le SQL est un outil **central** pour analyser les logs.

## ❌ Erreur classique

```python
# La concaténation, l'erreur n°1
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")    # ❌ injection possible

# Les f-strings ne protègent PAS — c'est juste de la concaténation déguisée
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")         # ❌ même problème

# La bonne approche : paramètres
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))        # ✅
```

## ✅ Tu sais maintenant…

- L’injection SQL exploite la concaténation d’entrées utilisateur
- Les requêtes préparées (paramètres `?`) protègent automatiquement
- Le principe de moindre privilège pour les comptes applicatifs
- La détection d’attaques via l’analyse des logs (le SQL est l’outil central)

-----

# Chapitre 30 — SQL depuis Python : passerelle

## Le minimum à savoir

Ce chapitre est volontairement court. Son but : **te donner le pont** entre ton cours Python et ton cours SQL. Tu sauras ouvrir une base, faire une requête, lire les résultats — c’est tout ce qu’il faut pour démarrer.

### Le module `sqlite3`

Python intègre nativement le support de SQLite via le module `sqlite3` — pas besoin d’installer quoi que ce soit.

### Le pattern minimal en 5 lignes

```python
import sqlite3

# 1. Se connecter à la base
conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# 2. Exécuter une requête
cursor.execute("SELECT first_name, last_name FROM readers WHERE city = 'Paris'")

# 3. Lire les résultats
for row in cursor.fetchall():
    print(row)

# 4. Fermer la connexion
conn.close()
```

Décodage :

- `connect()` ouvre la base (le fichier `.db`)
- `cursor()` crée un curseur — l’objet qui exécute les requêtes
- `execute()` lance une requête SQL
- `fetchall()` récupère toutes les lignes
- `close()` ferme proprement

### Avec paramètres : la bonne pratique

**Toujours** utiliser les paramètres (`?` en SQLite) plutôt que la concaténation :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# Variable issue d'une entrée utilisateur (par exemple)
ville = "Paris"

# ❌ JAMAIS faire ça
# cursor.execute(f"SELECT * FROM readers WHERE city = '{ville}'")

# ✅ Toujours faire ça
cursor.execute(
    "SELECT first_name, last_name FROM readers WHERE city = ?",
    (ville,)            # tuple — n'oublie pas la virgule pour 1 seul paramètre
)

for row in cursor.fetchall():
    print(row)

conn.close()
```

> **À retenir :** la sécurité SQL en Python tient en une règle. **Ne jamais concaténer.** Toujours utiliser `?` et un tuple. Cette règle te protège de 99% des injections SQL.

### Insérer, modifier, supprimer : `commit()` obligatoire

Pour les modifications, il faut explicitement valider avec `conn.commit()` :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# Insérer une ligne
cursor.execute(
    "INSERT INTO readers (first_name, last_name, registration_date) VALUES (?, ?, ?)",
    ("Marie", "Lefort", "2026-05-03")
)

conn.commit()           # ← VALIDER les modifications
conn.close()
```

Sans `commit()`, les modifications sont perdues à la fermeture. C’est l’équivalent du `COMMIT` SQL qu’on a vu au Ch.23.

### Le `with` : commit/rollback automatique

Python permet d’utiliser `with` pour gérer automatiquement les transactions sur une connexion SQLite :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
try:
    with conn:                    # ← gère le commit/rollback automatique
        cursor = conn.cursor()
        cursor.execute("INSERT INTO readers (first_name, last_name, registration_date) VALUES (?, ?, ?)",
                       ("Marie", "Lefort", "2026-05-03"))
        # Si tout va bien à la sortie du with → COMMIT automatique
        # Si une exception est levée → ROLLBACK automatique
finally:
    conn.close()                  # fermeture explicite
```

> **⚠️ Attention à un piège fréquent :** avec `sqlite3`, le bloc `with` **ne ferme pas** la connexion — il gère seulement la transaction (commit en cas de succès, rollback en cas d’erreur). Pour fermer proprement, il faut un `conn.close()` explicite (typiquement dans un `finally`, ou en utilisant `contextlib.closing`).

Pour avoir une vraie fermeture automatique, on peut combiner avec `contextlib.closing` :

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect("bibliotheque.db")) as conn:
    with conn:                    # transaction (commit/rollback)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM readers")
        for row in cursor.fetchall():
            print(row)
# Ici la connexion est fermée automatiquement
```

Pour démarrer, retiens simplement : **`with conn:` gère la transaction, `conn.close()` ferme la connexion**. Les deux sont à connaître.

> **📋 FIL ROUGE — Épisode 29**
> 
> Nora veut automatiser un rapport quotidien. Plutôt que d’ouvrir DB Browser chaque matin, elle écrit un petit script Python :
> 
> ```python
> import sqlite3
> 
> conn = sqlite3.connect("bibliotheque.db")
> try:
>     cursor = conn.cursor()
> 
>     cursor.execute("SELECT COUNT(*) FROM loans WHERE status = 'late'")
>     nb_retards = cursor.fetchone()[0]
> 
>     cursor.execute("SELECT COUNT(*) FROM readers")
>     nb_lecteurs = cursor.fetchone()[0]
> 
>     print(f"Rapport du jour : {nb_lecteurs} lecteurs, {nb_retards} emprunts en retard")
> finally:
>     conn.close()
> ```
> 
> Quelques lignes — et le script peut être lancé chaque matin par une tâche planifiée. C’est exactement la passerelle entre SQL et Python qu’elle cherchait.

## Très utile en pratique

### `fetchall()`, `fetchone()`, `fetchmany(n)`

|Méthode       |Renvoie                                   |
|--------------|------------------------------------------|
|`fetchall()`  |Toutes les lignes (liste de tuples)       |
|`fetchone()`  |Une seule ligne (tuple), ou `None` si vide|
|`fetchmany(n)`|Les n prochaines lignes                   |

Pour des requêtes qui ne renvoient qu’une valeur (comme `COUNT(*)`), `fetchone()[0]` est idéal.

### Le résultat sous forme de dictionnaire

Par défaut, les lignes sont des **tuples** (`row[0]`, `row[1]`…). Pour les avoir comme dictionnaires (`row['first_name']`) :

```python
conn = sqlite3.connect("bibliotheque.db")
conn.row_factory = sqlite3.Row     # ← active le mode "dict-like"
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name FROM readers")
for row in cursor.fetchall():
    print(row['first_name'], row['last_name'])
```

Plus lisible quand tu as beaucoup de colonnes.

## ❌ Erreur classique

```python
# Oublier le commit après une modification
cursor.execute("INSERT INTO readers ...")
# pas de commit → perdu

# Concaténation au lieu de paramètres
cursor.execute(f"SELECT * FROM readers WHERE id = {user_id}")    # ❌ injection
cursor.execute("SELECT * FROM readers WHERE id = ?", (user_id,)) # ✅

# Oublier la virgule dans le tuple à 1 élément
cursor.execute("SELECT * FROM readers WHERE id = ?", (1))     # ❌ "1" n'est pas un tuple
cursor.execute("SELECT * FROM readers WHERE id = ?", (1,))    # ✅ tuple à 1 élément
```

## ✅ Tu sais maintenant…

- Le pattern minimal `sqlite3` en Python : `connect`, `cursor`, `execute`, `fetchall`, `close`
- Toujours utiliser `?` et un tuple, jamais la concaténation
- `commit()` obligatoire pour les modifications
- `with conn:` gère automatiquement le commit/rollback, mais **ne ferme pas** la connexion
- `conn.close()` (souvent dans un `finally`) ferme explicitement la connexion
- C’est ta passerelle vers le cours Python complet

-----

# PARTIE VIII — SYNTHÈSE

-----

# Chapitre 31 — Skills Assessment — Évaluation finale

## Objectif

Tu vas exploiter une base **inconnue à toi** (mais que tu as construite au Ch.4) — la base `bibliotheque.db`. Réponds aux 12 questions ci-dessous en écrivant les requêtes SQL correspondantes.

**Cette évaluation valide :**

- Lecture de données (Ch.5-10)
- Calculs et agrégations (Ch.11-14)
- Jointures (Ch.15-19)
- Modifications avec sécurité (Ch.20-23)
- Compréhension du modèle (Ch.2, 15)
- Détection d’anomalies (angle cyber)

## Préparation

```sql
-- Vérifier que la base est bien chargée
.tables
-- Doit lister : authors, book_authors, books, categories, loans, login_events, readers, staff_users
```

## Les 12 questions

**1. Combien y a-t-il de lecteurs au total ?**

<details>
<summary>💡 Indice</summary>

Une simple agrégation `COUNT(*)` sur la table `readers`.

</details>

-----

**2. Quels sont les 10 derniers lecteurs inscrits ? (nom, prénom, date d’inscription)**

<details>
<summary>💡 Indice</summary>

`ORDER BY registration_date DESC` + `LIMIT 10`.

</details>

-----

**3. Quels livres n’ont jamais été empruntés ?**

<details>
<summary>💡 Indice</summary>

`LEFT JOIN` entre `books` et `loans`, puis `WHERE l.id IS NULL`.

</details>

-----

**4. Quels sont les 5 lecteurs ayant le plus emprunté ? (nom + nombre d’emprunts)**

<details>
<summary>💡 Indice</summary>

Jointure `readers` + `loans`, `GROUP BY` sur le lecteur, `ORDER BY COUNT(*) DESC LIMIT 5`.

</details>

-----

**5. Quels lecteurs ont des emprunts en retard ? (nom + titre du livre)**

<details>
<summary>💡 Indice</summary>

Jointure `readers` + `loans` + `books`, `WHERE l.status = 'late'`.

</details>

-----

**6. Combien de livres existe-t-il par catégorie ? (catégorie + nombre, trié)**

<details>
<summary>💡 Indice</summary>

Jointure `books` + `categories`, `GROUP BY c.name`, `ORDER BY COUNT(*) DESC`.

</details>

-----

**7. Quel(s) auteur(s) est/sont le(s) plus emprunté(s) ?**

<details>
<summary>💡 Indice</summary>

Jointure `loans` + `books` + `book_authors` + `authors`, `GROUP BY` sur l’auteur, trier par nombre.

</details>

-----

**8. Quels lecteurs n’ont jamais emprunté ?**

<details>
<summary>💡 Indice</summary>

Comme la question 3, mais cette fois `LEFT JOIN` depuis `readers`.

</details>

-----

**9. Quels emails de lecteurs sont en double dans la base ?**

<details>
<summary>💡 Indice</summary>

`GROUP BY email` puis `HAVING COUNT(*) > 1`.

</details>

-----

**10. Quels comptes du personnel ont eu le plus d’échecs de connexion ? (cyber)**

<details>
<summary>💡 Indice</summary>

Jointure `staff_users` + `login_events`, `WHERE success = 0`, `GROUP BY` sur l’utilisateur.

</details>

-----

**11. Quels livres ont été empruntés au moins 2 fois ?**

<details>
<summary>💡 Indice</summary>

Jointure `books` + `loans`, `GROUP BY` sur le livre, `HAVING COUNT(*) >= 2`.

</details>

-----

**12. Question synthèse : écris une requête qui résume l’activité d’**Alice Martin** (id=1) — combien d’emprunts au total, combien retournés, combien en cours, combien en retard.**

<details>
<summary>💡 Indice</summary>

Une seule requête avec plusieurs `COUNT` conditionnels :

```sql
COUNT(*) AS total,
COUNT(CASE WHEN status = 'returned' THEN 1 END) AS retournes,
...
```

</details>

## Bonus cyber : la tentative de brute-force

Regarde la table `login_events` : tu y verras **10 échecs** sur le compte `admin` depuis l’IP `203.0.113.42`, suivis d’**1 réussite** depuis la même IP. C’est le pattern typique d’une attaque par brute-force qui a réussi.

Écris une requête simple qui détecte un compte ayant subi beaucoup d’échecs **et** au moins une réussite depuis la même IP :

```sql
SELECT username, ip_address,
       COUNT(*) AS nb_total,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs,
       SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) AS nb_succes
FROM login_events
GROUP BY username, ip_address
HAVING nb_echecs >= 5 AND nb_succes >= 1;
```

> **Limite de cette requête :** elle détecte **beaucoup d’échecs + au moins une réussite** depuis la même IP, mais ne prouve pas formellement que les échecs sont consécutifs ni que la réussite vient *après*. Pour cela, il faudrait des fonctions de fenêtre (window functions) — un sujet plus avancé. En pratique, cette requête simple suffit comme **premier signal d’alerte** : un analyste reprendra ensuite manuellement les événements triés par date pour confirmer.

## Solutions

Les solutions complètes sont disponibles dans l’**Annexe F — Requêtes types**. Mais essaie d’abord par toi-même !

-----

# Chapitre 32 — Synthèse et boîte à outils SQL

## L’ordre d’écriture d’une requête

Quand tu écris une requête, l’ordre est :

```sql
SELECT     -- 1. Quelles colonnes ?
FROM       -- 2. Quelle table ?
JOIN       -- 3. Quelles tables croiser ?
WHERE      -- 4. Quelles lignes filtrer (avant agrégation) ?
GROUP BY   -- 5. Comment regrouper ?
HAVING     -- 6. Quels groupes garder ?
ORDER BY   -- 7. Comment trier ?
LIMIT      -- 8. Combien de lignes ?
```

## L’ordre logique d’exécution (interne)

Le moteur SQL **n’exécute pas** les clauses dans l’ordre où tu les écris. Il les exécute dans cet ordre logique :

```
FROM / JOIN  →  WHERE  →  GROUP BY  →  HAVING  →  SELECT  →  ORDER BY  →  LIMIT
```

C’est important à comprendre pour deux raisons :

1. Les **alias définis dans `SELECT`** ne peuvent pas être utilisés dans `WHERE` (le `WHERE` est exécuté avant le `SELECT`). Mais ils peuvent être utilisés dans `ORDER BY`.
1. `WHERE` filtre **avant** agrégation, `HAVING` filtre **après**. C’est ce qu’on a vu au Ch.14.

> **À retenir :** ce n’est pas exactement l’ordre d’exécution interne du moteur (qui peut optimiser), mais c’est le **modèle mental** correct pour comprendre ce qui se passe.

## Les commandes SQL essentielles

```
-- Lecture
SELECT, FROM, WHERE, AND, OR, NOT
DISTINCT, AS
LIKE, IN, BETWEEN, IS NULL, IS NOT NULL
ORDER BY, ASC, DESC, LIMIT, OFFSET

-- Calcul et regroupement
COUNT, SUM, AVG, MIN, MAX
GROUP BY, HAVING

-- Jointures
INNER JOIN, LEFT JOIN, ON

-- Modification
INSERT INTO ... VALUES
UPDATE ... SET ... WHERE
DELETE FROM ... WHERE

-- Transactions
BEGIN, COMMIT, ROLLBACK

-- Structure
CREATE TABLE, DROP TABLE, ALTER TABLE
CREATE INDEX, CREATE VIEW
PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT
```

## Les erreurs fréquentes (synthèse)

|Erreur                       |Symptôme                      |Solution                                |
|-----------------------------|------------------------------|----------------------------------------|
|Oublier `WHERE` dans `UPDATE`|Toute la table modifiée       |Faire un `SELECT` avant                 |
|Oublier `WHERE` dans `DELETE`|Toute la table vidée          |Faire un `SELECT` avant + transaction   |
|`WHERE col = NULL`           |Aucun résultat                |Utiliser `IS NULL`                      |
|Confondre `WHERE` et `HAVING`|Erreur “aggregate not allowed”|`WHERE` avant agrégation, `HAVING` après|
|`SELECT *` après jointure    |Doublons silencieux           |`COUNT(DISTINCT)` ou colonnes explicites|
|Oublier `ON`                 |Produit cartésien             |Toujours `INNER JOIN ... ON ...`        |
|Concatener entrée utilisateur|Injection SQL                 |Utiliser `?` et paramètres              |

## Quand utiliser quelle clause ?

```
J'ai besoin de…                          Outil
────────────────────────────────────     ──────────────
Lire des lignes                          SELECT
Filtrer ces lignes                       WHERE
Combiner deux tables                     INNER JOIN
Garder les lignes même sans match        LEFT JOIN
Trouver "ce qui n'a pas de match"        LEFT JOIN ... WHERE ... IS NULL
Compter par catégorie                    GROUP BY + COUNT(*)
Filtrer ces groupes                      HAVING
Trier le résultat                        ORDER BY
Limiter le nombre de lignes              LIMIT
Pagination                               LIMIT + OFFSET
Recherche par motif                      LIKE '%motif%'
Plage de valeurs                         BETWEEN a AND b
Liste de valeurs                         IN (...)
Valeur absente                           IS NULL
Modifier des données                     UPDATE ... WHERE + SELECT préalable
Supprimer des données                    DELETE ... WHERE + SELECT préalable + transaction
Sécuriser un bloc de modifications       BEGIN ... COMMIT (ou ROLLBACK)
Accélérer une recherche                  CREATE INDEX
Simplifier des requêtes complexes        CREATE VIEW
```

## La suite logique

|Cours                                         |Quand le faire                                       |
|----------------------------------------------|-----------------------------------------------------|
|**PostgreSQL** ou **MySQL**                   |Pour passer à un SGBD professionnel (web, entreprise)|
|**Modélisation avancée**                      |Quand tu conçois des bases de plus de 10 tables      |
|**Performance et optimisation**               |Quand les requêtes deviennent lentes                 |
|**NoSQL** (MongoDB, Redis)                    |Pour comprendre les alternatives au relationnel      |
|**Data Engineering** (Spark, dbt)             |Pour le big data et les pipelines analytiques        |
|**Sécurité offensive** (SQL injection avancée)|Si tu vas vers le pentest                            |

-----

# ANNEXES

-----

## Annexe A — Glossaire complet

|Terme                          |Définition                                                                                |
|-------------------------------|------------------------------------------------------------------------------------------|
|**ACID**                       |Propriétés des transactions : Atomicité, Cohérence, Isolation, Durabilité                 |
|**Agrégation**                 |Fonction qui calcule une valeur unique sur un groupe (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)|
|**Alias**                      |Nom temporaire donné à une colonne ou une table avec `AS`                                 |
|**Base de données**            |Système organisé de stockage et de gestion de données                                     |
|**Clé étrangère (FOREIGN KEY)**|Colonne qui pointe vers la clé primaire d’une autre table                                 |
|**Clé primaire (PRIMARY KEY)** |Colonne(s) qui identifie(nt) de façon unique chaque ligne                                 |
|**Colonne**                    |Champ d’une table (équivalent : attribut, propriété)                                      |
|**Contrainte**                 |Règle imposée à une colonne (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`)                |
|**Cursor (curseur)**           |Objet qui exécute des requêtes en Python (et autres langages)                             |
|**DDL**                        |Data Definition Language : `CREATE`, `ALTER`, `DROP`                                      |
|**DML**                        |Data Manipulation Language : `SELECT`, `INSERT`, `UPDATE`, `DELETE`                       |
|**Dialecte**                   |Variante de SQL propre à un SGBD                                                          |
|**Entité**                     |Concept du monde réel modélisé en table                                                   |
|**Index**                      |Structure annexe qui accélère les recherches                                              |
|**Injection SQL**              |Attaque exploitant la concaténation d’entrée utilisateur                                  |
|**Jointure (JOIN)**            |Opération qui combine les données de plusieurs tables                                     |
|**Ligne (row)**                |Enregistrement dans une table                                                             |
|**NULL**                       |Absence de valeur (différent de zéro et de chaîne vide)                                   |
|**OFFSET**                     |Saut d’un nombre de lignes pour la pagination                                             |
|**Paramètre (placeholder)**    |`?` ou `:nom` dans une requête, remplacé par une valeur sécurisée                         |
|**Relation**                   |Lien entre deux tables (1-N ou N-N)                                                       |
|**Requête**                    |Instruction SQL envoyée au moteur                                                         |
|**Requête préparée**           |Requête avec paramètres, protégée contre l’injection                                      |
|**Schéma**                     |Structure de la base : tables, colonnes, contraintes                                      |
|**SGBD**                       |Système de Gestion de Base de Données (SQLite, PostgreSQL, MySQL…)                        |
|**SQL**                        |Structured Query Language — le langage standard                                           |
|**SQLite**                     |SGBD léger, embarqué, basé sur un fichier                                                 |
|**Table**                      |Tableau structuré de données                                                              |
|**Table d’association**        |Table intermédiaire pour modéliser une relation N-N                                       |
|**Transaction**                |Bloc de modifications validable (`COMMIT`) ou annulable (`ROLLBACK`)                      |
|**Vue (VIEW)**                 |Requête enregistrée utilisable comme une table                                            |

-----

## Annexe B — Commandes SQL essentielles

### Lecture

```sql
SELECT col1, col2 FROM table;
SELECT * FROM table;
SELECT DISTINCT col FROM table;
SELECT col AS alias FROM table;

-- Filtrage
WHERE col = valeur
WHERE col <> valeur, !=
WHERE col > / < / >= / <=
WHERE col LIKE '%motif%'
WHERE col IN (val1, val2, val3)
WHERE col BETWEEN a AND b
WHERE col IS NULL / IS NOT NULL
WHERE cond1 AND cond2
WHERE cond1 OR cond2
WHERE NOT cond

-- Tri et limite
ORDER BY col ASC / DESC
LIMIT n
LIMIT n OFFSET m
```

### Agrégation

```sql
SELECT COUNT(*) FROM table;
SELECT COUNT(col) FROM table;        -- exclut les NULL
SELECT COUNT(DISTINCT col) FROM table;
SELECT SUM(col), AVG(col), MIN(col), MAX(col) FROM table;

GROUP BY col
HAVING agrégation cond
```

### Jointures

```sql
FROM table1 INNER JOIN table2 ON table1.col = table2.col
FROM table1 LEFT JOIN table2 ON ...
-- Pour trouver les "orphelins" :
FROM t1 LEFT JOIN t2 ON ... WHERE t2.id IS NULL
```

### Modification

```sql
INSERT INTO table (col1, col2) VALUES (val1, val2);
INSERT INTO table (col1, col2) VALUES (a, b), (c, d), (e, f);

UPDATE table SET col = val WHERE cond;          -- TOUJOURS avec WHERE
DELETE FROM table WHERE cond;                    -- TOUJOURS avec WHERE
```

### Transactions

```sql
BEGIN;
-- modifications
COMMIT;     -- ou ROLLBACK;
```

### Structure

```sql
CREATE TABLE nom (
    id INTEGER PRIMARY KEY,
    col TEXT NOT NULL,
    autre TEXT UNIQUE,
    valeur INTEGER DEFAULT 0,
    FOREIGN KEY (col) REFERENCES autre_table(id),
    CHECK (cond)
);

DROP TABLE nom;
ALTER TABLE nom ADD COLUMN col TYPE;

CREATE INDEX idx_nom ON table(col);
DROP INDEX idx_nom;

CREATE VIEW vue AS SELECT ...;
DROP VIEW vue;
```

-----

## Annexe C — Fonctions SQLite utiles

### Texte

```sql
UPPER('alice')              -- 'ALICE'
LOWER('ALICE')              -- 'alice'
LENGTH('Alice')             -- 5
TRIM('  abc  ')             -- 'abc'
SUBSTR('Bonjour', 1, 3)     -- 'Bon'
REPLACE('abc', 'b', 'B')    -- 'aBc'

-- Concaténation (SQLite/PostgreSQL)
'a' || 'b'                  -- 'ab'
COALESCE(NULL, 'défaut')    -- 'défaut' (si premier est NULL)
```

### Dates

```sql
DATE('now')                 -- date du jour : '2026-05-03'
DATETIME('now')             -- date + heure
strftime('%Y', date)        -- année
strftime('%Y-%m', date)     -- année-mois
strftime('%H:%M', heure)    -- heure-minute
julianday('now')            -- nombre de jours depuis le 24 nov 4714 av. J.-C.
julianday('now') - julianday(date)    -- différence en jours
DATE('now', '-7 days')      -- il y a 7 jours
DATE('now', '+1 month')     -- dans 1 mois
```

### Numériques

```sql
ABS(x)                       -- valeur absolue
ROUND(3.14159, 2)            -- 3.14
MAX(a, b)                    -- max de 2 valeurs (différent de l'agrégation MAX !)
MIN(a, b)                    -- idem pour min
RANDOM()                     -- nombre aléatoire
```

### Conditionnel

```sql
CASE
    WHEN cond1 THEN val1
    WHEN cond2 THEN val2
    ELSE valeur_par_defaut
END

COALESCE(col1, col2, 'défaut')   -- premier non-NULL
NULLIF(col, valeur)              -- NULL si col = valeur, sinon col
```

-----

## Annexe D — Différences SQLite / PostgreSQL / MySQL

|Tâche                       |SQLite                |PostgreSQL                    |MySQL                       |
|----------------------------|----------------------|------------------------------|----------------------------|
|Auto-incrément              |`INTEGER PRIMARY KEY` |`SERIAL` ou `IDENTITY`        |`AUTO_INCREMENT`            |
|Concaténation               |`'a' || 'b'`          |`'a' || 'b'`                  |`CONCAT('a', 'b')`          |
|Date du jour                |`DATE('now')`         |`CURRENT_DATE`                |`CURDATE()`                 |
|Extraire année              |`strftime('%Y', date)`|`EXTRACT(YEAR FROM date)`     |`YEAR(date)`                |
|Booléen                     |`INTEGER` (0/1)       |`BOOLEAN` natif               |`BOOLEAN` (alias de TINYINT)|
|Texte limité                |`TEXT` (illimité)     |`VARCHAR(50)`                 |`VARCHAR(50)`               |
|Insensible à la casse (LIKE)|par défaut            |`ILIKE`                       |par défaut                  |
|`LIMIT` + `OFFSET`          |`LIMIT 10 OFFSET 20`  |idem (et `OFFSET 20 LIMIT 10`)|idem                        |
|Méta-commandes              |`.tables`, `.schema`  |`\dt`, `\d`                   |`SHOW TABLES`, `DESCRIBE`   |


> **À retenir :** 90% du SQL est identique. Les 10% qui varient concernent surtout : auto-incrément, fonctions de date, concaténation, et certaines fonctions de texte. Quand tu changes de SGBD, c’est ce que tu adaptes.

-----

## Annexe E — Pièges classiques

|Piège                                   |Exemple incorrect                    |Correction                                                        |
|----------------------------------------|-------------------------------------|------------------------------------------------------------------|
|Oublier `WHERE` dans `UPDATE`           |`UPDATE readers SET city = 'Paris';` |`UPDATE readers SET city = 'Paris' WHERE id = 1;`                 |
|Oublier `WHERE` dans `DELETE`           |`DELETE FROM readers;`               |`DELETE FROM readers WHERE id = 1;`                               |
|Confondre `NULL` et chaîne vide         |`WHERE col = ''`                     |`WHERE col = ''` (chaîne vide) **ou** `WHERE col IS NULL` (absent)|
|`= NULL` au lieu de `IS NULL`           |`WHERE col = NULL`                   |`WHERE col IS NULL`                                               |
|`WHERE` agrégation                      |`WHERE COUNT(*) > 5`                 |`HAVING COUNT(*) > 5`                                             |
|`COUNT(col)` ne compte pas les NULL     |`COUNT(email)` peut être < `COUNT(*)`|C’est normal, c’est même utile                                    |
|Jointure sans `ON`                      |`SELECT * FROM a, b`                 |`SELECT * FROM a INNER JOIN b ON a.id = b.a_id`                   |
|Doublons après JOIN N-N                 |`COUNT(*)` après `JOIN book_authors` |`COUNT(DISTINCT b.id)`                                            |
|`SELECT *` partout                      |Risqué, perd en clarté               |Lister les colonnes explicitement                                 |
|Pas de transaction sur opération risquée|`UPDATE` massif sans `BEGIN`         |`BEGIN; UPDATE...; COMMIT;`                                       |
|Concatener entrée utilisateur           |`... + user_input + ...`             |`... ? ...` avec paramètres                                       |

-----

## Annexe F — Requêtes types (et solutions du Skills Assessment)

### Solutions du Ch.31

**Q1 — Combien y a-t-il de lecteurs ?**

```sql
SELECT COUNT(*) FROM readers;
```

**Q2 — Les 10 derniers lecteurs inscrits**

```sql
SELECT first_name, last_name, registration_date
FROM readers
ORDER BY registration_date DESC
LIMIT 10;
```

**Q3 — Livres jamais empruntés**

```sql
SELECT b.title
FROM books AS b
LEFT JOIN loans AS l ON b.id = l.book_id
WHERE l.id IS NULL;
```

**Q4 — Top 5 lecteurs**

```sql
SELECT r.first_name, r.last_name, COUNT(*) AS nb
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
GROUP BY r.id, r.first_name, r.last_name
ORDER BY nb DESC
LIMIT 5;
```

**Q5 — Lecteurs avec emprunts en retard**

```sql
SELECT r.first_name, r.last_name, b.title
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status = 'late';
```

**Q6 — Livres par catégorie**

```sql
SELECT c.name, COUNT(*) AS nb
FROM books AS b
INNER JOIN categories AS c ON b.category_id = c.id
GROUP BY c.name
ORDER BY nb DESC;
```

**Q7 — Auteur le plus emprunté**

```sql
SELECT a.name, COUNT(*) AS nb_emprunts
FROM authors AS a
INNER JOIN book_authors AS ba ON a.id = ba.author_id
INNER JOIN books AS b ON ba.book_id = b.id
INNER JOIN loans AS l ON b.id = l.book_id
GROUP BY a.id, a.name
ORDER BY nb_emprunts DESC
LIMIT 1;
```

**Q8 — Lecteurs n’ayant jamais emprunté**

```sql
SELECT r.first_name, r.last_name
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.id IS NULL;
```

**Q9 — Emails en double**

```sql
SELECT email, COUNT(*) AS nb
FROM readers
WHERE email IS NOT NULL
GROUP BY email
HAVING nb > 1;
```

**Q10 — Comptes avec le plus d’échecs**

```sql
-- Version avec jointure : affiche aussi les comptes à 0 échec (rapport plus complet)
SELECT s.username, s.full_name, COUNT(le.id) AS nb_echecs
FROM staff_users AS s
LEFT JOIN login_events AS le
       ON s.username = le.username
      AND le.success = 0
GROUP BY s.id, s.username, s.full_name
ORDER BY nb_echecs DESC;

-- Version sans jointure : ne liste que les comptes ayant au moins un échec
-- (et inclut aussi les tentatives sur des comptes inexistants)
SELECT username, COUNT(*) AS nb_echecs
FROM login_events
WHERE success = 0
GROUP BY username
ORDER BY nb_echecs DESC;
```

> **Pourquoi deux versions ?** La première donne un rapport propre pour la directrice (tous les comptes connus, avec leur compteur d’échecs même à zéro). La seconde sert à l’analyse cyber pure — elle révèle aussi les tentatives sur des comptes **qui n’existent pas** dans `staff_users` (typique d’un attaquant qui essaie des noms d’utilisateurs au hasard).

**Q11 — Livres empruntés au moins 2 fois**

```sql
SELECT b.title, COUNT(*) AS nb
FROM books AS b
INNER JOIN loans AS l ON b.id = l.book_id
GROUP BY b.id, b.title
HAVING nb >= 2;
```

**Q12 — Activité d’Alice (id=1)**

```sql
SELECT
    r.first_name || ' ' || r.last_name AS lecteur,
    COUNT(*) AS total,
    SUM(CASE WHEN l.status = 'returned' THEN 1 ELSE 0 END) AS retournes,
    SUM(CASE WHEN l.status = 'borrowed' THEN 1 ELSE 0 END) AS en_cours,
    SUM(CASE WHEN l.status = 'late' THEN 1 ELSE 0 END) AS en_retard
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE r.id = 1
GROUP BY r.id, r.first_name, r.last_name;
```

-----

## Annexe G — SQL pour la cybersécurité

Le SQL est un outil **central** en cybersécurité défensive — pour analyser les logs, détecter les anomalies, comprendre le comportement utilisateur. Voici quelques patterns utiles.

### Détecter une attaque par brute-force

```sql
-- Comptes ayant subi 5+ échecs depuis la même IP
SELECT username, ip_address, COUNT(*) AS nb_echecs,
       MIN(event_time) AS premier, MAX(event_time) AS dernier
FROM login_events
WHERE success = 0
GROUP BY username, ip_address
HAVING nb_echecs >= 5
ORDER BY nb_echecs DESC;
```

### Repérer un pattern brute-force réussi

```sql
-- Comptes avec beaucoup d'échecs ET au moins une réussite depuis la même IP
SELECT username, ip_address,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs,
       SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) AS nb_succes
FROM login_events
GROUP BY username, ip_address
HAVING nb_echecs >= 5 AND nb_succes >= 1;
```

### Détecter les comptes inactifs (à désactiver)

```sql
-- Comptes du personnel sans connexion depuis 90 jours
SELECT s.username, s.full_name, MAX(le.event_time) AS derniere_connexion
FROM staff_users AS s
LEFT JOIN login_events AS le ON s.username = le.username AND le.success = 1
GROUP BY s.id
HAVING derniere_connexion IS NULL
   OR julianday('now') - julianday(derniere_connexion) > 90;
```

### Connexions à des heures inhabituelles

```sql
-- Connexions réussies entre 22h et 6h (potentiellement suspect)
SELECT username, event_time, ip_address
FROM login_events
WHERE success = 1
  AND (CAST(strftime('%H', event_time) AS INTEGER) >= 22
       OR CAST(strftime('%H', event_time) AS INTEGER) < 6);
```

### Détection d’utilisateur dupliqué (compte fantôme)

```sql
-- Lecteurs avec le même nom complet (et donc potentiellement doublonnés)
SELECT first_name, last_name, COUNT(*) AS nb
FROM readers
GROUP BY first_name, last_name
HAVING nb > 1;
```

### Compter les événements par fenêtre temporelle

```sql
-- Nombre de connexions par jour
SELECT DATE(event_time) AS jour, COUNT(*) AS nb_evenements,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs
FROM login_events
GROUP BY DATE(event_time)
ORDER BY jour DESC;
```

> **Ouverture :** ces requêtes sont la base de tout système de **SIEM** (Security Information and Event Management). Les outils comme Splunk, Elastic SIEM, ou QRadar utilisent du SQL (ou des langages similaires) pour détecter les anomalies en temps réel.

-----

## Annexe H — Script de la base de démo

Le script complet pour recréer la base `bibliotheque.db` est celui présenté au **Chapitre 4**. Tu peux le copier-coller dans DB Browser → “Exécuter le SQL”, puis sauvegarder.

**Rappel des 8 tables :**

1. `categories` — 6 catégories de livres
1. `authors` — 11 auteurs (dont 1 sans livre dans la base, pour les exercices `LEFT JOIN`)
1. `books` — 15 livres
1. `book_authors` — table d’association N-N (16 lignes ; un livre coécrit par 2 auteurs, pour illustrer le piège des doublons)
1. `readers` — 15 lecteurs (avec deux Alice Martin partageant le même email et 4 sans téléphone)
1. `loans` — 20 emprunts (mix returned, borrowed, late)
1. `staff_users` — 5 comptes du personnel (1 inactif, 1 compte ‘admin’ dangereux)
1. `login_events` — 17 événements (avec une attaque brute-force réussie sur ‘admin’ : 10 échecs + 1 succès)

-----

# Conclusion

Tu maîtrises maintenant les fondamentaux de SQL et des bases de données relationnelles :

- **Comprendre** ce qu’est une base, comment elle est structurée (Ch.1-4)
- **Lire** des données avec `SELECT`, filtrer, trier, limiter (Ch.5-10)
- **Calculer** et regrouper avec les agrégations (Ch.11-14)
- **Croiser** les tables avec les jointures (Ch.15-19)
- **Modifier** les données avec prudence — `INSERT`, `UPDATE`, `DELETE`, transactions (Ch.20-23)
- **Créer** une table avec contraintes (Ch.24-26)
- **Bonus** : bonnes pratiques, vues, index, sécurité, Python (Ch.27-30)

**La progression naturelle :**

- Pratique sur des bases plus grandes (Kaggle, datasets publics)
- Passe à PostgreSQL pour un environnement professionnel
- Apprends la modélisation poussée pour concevoir des bases de 20+ tables
- Explore le data engineering (Spark, dbt, Airflow)
- Va voir le NoSQL pour comprendre les alternatives

**Le SQL est l’une des compétences les plus durables en informatique.** Le langage a 50 ans, il sera encore là dans 30. Tu viens d’investir dans une compétence qui ne se démode pas.

Bon voyage dans le monde des données !