# Python pour OSINT & Web Scraping

## De la collecte web à l’automatisation d’enquête

-----

> **Prérequis :** avoir terminé un cours Python débutant. Tu dois être à l’aise avec les variables, listes, dictionnaires, boucles, fonctions, fichiers, gestion d’erreurs.
> 
> **Aucun prérequis web :** pas besoin de connaître HTTP, HTML, ni les APIs. On part de zéro côté web.

-----

## Avant-propos

Ce cours n’est pas un cours de Python. C’est un cours d’**enquête en sources ouvertes** qui se sert de Python comme outil. La nuance compte. Un analyste OSINT qui code **simplement mais proprement** vaut mieux qu’un excellent codeur qui collecte sans cadre.

Toute la pédagogie s’organise autour de quatre réflexes :

1. **Penser avant de coder** — quelle question, quelle source, quelle méthode minimale.
1. **Minimiser** — collecter ce qui répond à la question, pas plus.
1. **Tracer** — garder la trace de ce qu’on a collecté, quand et pourquoi.
1. **Respecter** — le droit applicable, les conditions du site, et l’infrastructure de la cible.

Ces réflexes seront rappelés à chaque chapitre. Ils ne sont pas optionnels.

-----

## Avertissement légal et éthique

Ce cours forme à la collecte de **données publiquement accessibles** à des fins défensives : veille, CTI, journalisme, recherche, transparence, sécurité. Il **ne forme pas** à :

- contourner des protections techniques,
- s’authentifier sur des comptes qui ne sont pas les tiens,
- collecter massivement des données personnelles,
- harceler une personne ou une entité,
- enfreindre les CGU d’un service.

Les exemples utilisent des sites conçus pour l’apprentissage (`books.toscrape.com`, `quotes.toscrape.com`, `httpbin.org`) ou des sources publiques explicitement ouvertes. Toute autre cible est sous **ta responsabilité**.

-----

## Glossaire — Les mots à connaître

Reviens ici à chaque fois qu’un terme te semble flou.

### OSINT et enquête

|Terme           |Définition simple                                                                              |
|----------------|-----------------------------------------------------------------------------------------------|
|**OSINT**       |Open-Source Intelligence — renseignement de sources ouvertes (publiques).                      |
|**CTI**         |Cyber Threat Intelligence — renseignement sur les menaces cyber.                               |
|**Source**      |Un site, un flux, une API d’où provient une donnée.                                            |
|**Sourcing**    |Le fait de tracer la provenance d’une donnée.                                                  |
|**Pivot**       |Un élément (domaine, email, hash) qui permet de rebondir d’une source à une autre.             |
|**Traçabilité** |Capacité à remonter à quand, comment, depuis où une donnée a été collectée.                    |
|**Minimisation**|Principe : ne collecter que ce dont tu as besoin.                                              |
|**OPSEC**       |Operational Security — bonnes pratiques pour ne pas se compromettre soi-même pendant l’enquête.|

### Web

|Terme         |Définition simple                                                       |
|--------------|------------------------------------------------------------------------|
|**URL**       |Adresse d’une ressource web (`https://exemple.fr/page`).                |
|**HTTP**      |Protocole de communication client/serveur du web.                       |
|**Requête**   |Demande envoyée par ton script au serveur.                              |
|**Réponse**   |Ce que le serveur renvoie (statut + headers + corps).                   |
|**Statut**    |Code numérique de la réponse (200 = OK, 404 = pas trouvé, etc.).        |
|**Header**    |Métadonnée d’une requête ou d’une réponse (langue, type, User-Agent…).  |
|**User-Agent**|Header qui dit qui fait la requête (un navigateur, un script, un robot).|
|**Cookie**    |Petite donnée stockée côté client pour identifier une session.          |

### HTML et parsing

|Terme            |Définition simple                                                             |
|-----------------|------------------------------------------------------------------------------|
|**HTML**         |Langage de structure des pages web.                                           |
|**Balise**       |Élément HTML (`<p>`, `<a>`, `<div>`…).                                        |
|**Attribut**     |Information attachée à une balise (`href`, `class`, `id`).                    |
|**DOM**          |Représentation en arbre du HTML, telle que vue par le navigateur.             |
|**Sélecteur CSS**|Expression pour cibler des éléments dans le DOM (`.classe`, `#id`, `div > a`).|
|**Parser**       |Programme qui transforme du HTML brut en structure exploitable.               |
|**Scraper**      |Programme qui extrait des données d’une page.                                 |
|**Crawler**      |Programme qui parcourt un site en suivant les liens.                          |

### Données et bonnes pratiques

|Terme         |Définition simple                                                                                                                                            |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**API**       |Interface conçue pour qu’un programme dialogue avec un service.                                                                                              |
|**REST**      |Style d’API courant fondé sur HTTP.                                                                                                                          |
|**JSON**      |Format de données structurées (`{"clé": "valeur"}`).                                                                                                         |
|**Rate limit**|Limite du nombre de requêtes par unité de temps.                                                                                                             |
|**robots.txt**|Fichier dans lequel un site indique aux robots les zones qu’il préfère autoriser ou interdire au parcours automatisé. Convention, pas autorisation juridique.|
|**CGU / ToS** |Conditions générales d’utilisation d’un service.                                                                                                             |
|**Open data** |Données publiques mises à disposition de tous, souvent en CSV/JSON.                                                                                          |

-----

## Comment penser une collecte OSINT

Avant la moindre ligne de code, un analyste se pose **quatre questions**. Cet ordre n’est pas négociable.

```
1. QUESTION    → Quelle question d’enquête je cherche à répondre ?
                 ↓
2. SOURCE      → Quelle source publique y répond ?
                 ↓
3. MÉTHODE     → Quelle méthode minimale suffit ?
                 (lecture humaine ? API ? RSS ? scraping ?)
                 ↓
4. TRACES      → Quelles traces je conserve pour rendre
                 l’enquête reproductible ?
```

Tout le cours s’articule autour de cette boucle. À la fin, tu auras une **fiche d’enquête** type que tu rempliras pour chaque projet.

> **À retenir :** on ne scrape **jamais** « pour voir ». Si tu n’as pas répondu aux quatre questions ci-dessus, n’écris pas de code.

-----

## La grande différence avec le scripting Python pur

Dans ton cours Python initial, tu manipulais **ton ordinateur** : variables, fichiers, dossiers, scripts. Ici, tu manipules **le web**, c’est-à-dire des serveurs **distants** que tu **ne contrôles pas**. Cela change tout.

|Scripting local               |Collecte web                                             |
|------------------------------|---------------------------------------------------------|
|Le code dépend de toi         |Le code dépend d’un serveur distant                      |
|Une erreur t’affecte toi      |Une erreur peut perturber un service public              |
|Pas de cadre légal particulier|Cadre légal applicable (CGU, RGPD, droit pénal)          |
|Aucune empreinte externe      |Chaque requête laisse une trace dans les logs du serveur |
|Tu peux relancer 1000 fois    |Relancer 1000 fois peut s’apparenter à du déni de service|

Tu vas devoir apprendre des **réflexes nouveaux** : prudence, lenteur volontaire, journalisation systématique, et minimisation.

-----

## Table des matières

### Partie I — Fondations

- **Chapitre 0 — Préparer son environnement de travail**
- Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?
- Chapitre 2 — Cadre légal, éthique et OPSEC du scraping
- Chapitre 3 — Comment fonctionne le web (vu côté collecteur)
- Chapitre 4 — Choisir la source la plus propre

### Partie II — Premières collectes

- Chapitre 5 — Premières requêtes avec `requests`
- Chapitre 6 — Parser du HTML avec BeautifulSoup
- Chapitre 7 — Extraction structurée d’une page

### Partie III — Structurer et nettoyer les données

- Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)
- Chapitre 9 — Nettoyer, normaliser, enrichir

### Partie IV — Passer à l’échelle

- Chapitre 10 — Pagination et collecte multi-pages
- Chapitre 11 — Utiliser des APIs publiques
- Chapitre 12 — Bonnes pratiques professionnelles

### Partie V — Enquête, veille et reporting

- Chapitre 13 — Veille et détection de changements
- Chapitre 14 — Du script au rapport d’enquête

### Partie VI — Projet final

- Chapitre 15 — Outil OSINT de collecte web défensive

### Annexes

- A — Sites d’entraînement légaux
- B — Modules à explorer ensuite
- C — Repères juridiques à vérifier avant usage réel
- D — Modèle de fiche d’enquête

-----

# Chapitre 0 — Préparer son environnement de travail

Avant d’écrire la moindre requête, on installe **l’atelier**. Un atelier propre, c’est ce qui distingue un script jetable d’un projet OSINT sérieux. Ce chapitre prend 15 minutes, et tu n’y reviendras presque jamais.

## Le minimum à savoir

### Pourquoi un atelier propre ?

Sans atelier, tes scripts vont :

- mélanger ton code, tes données collectées et tes configurations,
- installer des bibliothèques qui polluent ton Python système,
- perdre la trace de ce qui a été installé (et donc casser à la prochaine machine),
- exposer accidentellement tes clés API si tu versionnes le tout sur Git.

Un atelier propre règle ces quatre problèmes d’un coup.

### L’arborescence standard

Crée un dossier de travail pour le cours, et organise-le ainsi :

```
osint-collecte/
├── src/              ← ton code Python
├── data/
│   ├── raw/          ← collectes brutes (HTML, JSON), JAMAIS modifiées
│   └── processed/    ← données nettoyées et exploitables
├── logs/             ← journaux d’exécution
├── reports/          ← rapports lisibles par un humain
├── config/           ← paramètres (URLs, délais, etc.)
├── .gitignore        ← ce qu’on ne versionne pas
├── requirements.txt  ← liste des bibliothèques
└── README.md         ← documentation du projet
```

> **Règle d’or :** `data/raw/` est **intouchable**. Une fois une collecte écrite dedans, on n’y touche plus. Tout le travail se fait dans `data/processed/`. Si tu casses quelque chose, tu peux toujours rejouer depuis le brut.

### Les commandes pour créer la structure

**Linux / Mac :**

```bash
mkdir -p osint-collecte/{src,data/raw,data/processed,logs,reports,config}
cd osint-collecte
touch .gitignore requirements.txt README.md
```

**Windows (PowerShell) :**

```powershell
mkdir osint-collecte
cd osint-collecte
mkdir src, data\raw, data\processed, logs, reports, config
New-Item .gitignore, requirements.txt, README.md
```

### L’environnement virtuel : isoler les dépendances

Un environnement virtuel (`venv`) est un dossier qui contient une copie isolée de Python et ses bibliothèques. Tout ce que tu installes dedans **n’affecte que ce projet**.

**Créer et activer :**

```bash
# Création (une seule fois)
python3 -m venv .venv

# Activation (à chaque session)
# Linux / Mac :
source .venv/bin/activate
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1
```

Tu sauras que c’est activé parce que ton prompt change : il commence par `(.venv)`.

Pour désactiver : `deactivate`.

> **À retenir :** dès que tu travailles sur le projet, tu actives le venv. Sinon, tu installes tes bibliothèques au mauvais endroit.

### Installer les bibliothèques du cours

Une fois le venv activé :

```bash
pip install requests beautifulsoup4 lxml
```

- **`requests`** : pour faire des requêtes HTTP.
- **`beautifulsoup4`** : pour parser le HTML.
- **`lxml`** : parser HTML/XML rapide, utilisé par BeautifulSoup.

Vérifie :

```bash
pip list
```

### Geler les dépendances dans `requirements.txt`

Pour qu’un autre puisse reproduire ton environnement :

```bash
pip freeze > requirements.txt
```

Ce fichier liste précisément les versions installées. Sur une autre machine :

```bash
pip install -r requirements.txt
```

> **Pourquoi c’est crucial en OSINT :** une enquête doit être **reproductible**. Sans `requirements.txt`, ton script qui marchait il y a six mois peut casser sur une version récente d’une bibliothèque, et tu ne pourras plus refaire la collecte.

### Le fichier `.gitignore`

Si tu utilises Git (recommandé), tu dois **exclure** :

- ton environnement virtuel (lourd, recréable),
- tes données collectées (parfois sensibles, parfois personnelles),
- tes logs (verbeux),
- tes secrets (clés API).

Contenu typique de `.gitignore` :

```
# Environnement virtuel
.venv/
__pycache__/
*.pyc

# Données et logs (selon le projet)
data/raw/
data/processed/
logs/

# Secrets
.env
config/secrets.*

# Système
.DS_Store
Thumbs.db
```

> **Risque réel :** sans `.gitignore`, tu peux pousser sur GitHub une clé API, et un bot la trouvera en moins d’une heure pour s’en servir à ta place.

## Très utile en pratique

### Le fichier `README.md` minimal

Un README, c’est la première chose qu’on lit. Même pour un projet personnel, écris-en un dès le début :

```markdown
# osint-collecte

Mon atelier d’apprentissage pour le cours OSINT & scraping.

## Installation

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Usage

À venir.

## Limites et cadre

Projet pédagogique. Ne pas utiliser contre des cibles non autorisées.
```

### Tester que tout fonctionne

Crée un fichier `src/test_install.py` :

```python
import requests
from bs4 import BeautifulSoup

print("Modules importés avec succès.")
print(f"Version requests : {requests.__version__}")
```

Lance-le :

```bash
python src/test_install.py
```

Si tu vois les versions sans erreur, ton atelier est prêt.

### L’éditeur

N’importe quel éditeur fait l’affaire, mais **VS Code** avec l’extension Python est un excellent choix pour ce cours :

- coloration syntaxique,
- détection automatique du venv,
- terminal intégré,
- gestion de Git directement dans l’interface.

## ❌ Erreur classique

```bash
# Installer sans avoir activé le venv
$ pip install requests
# → installe dans le Python système, pollue, et la prochaine fois
#   sur un autre projet tu auras des conflits.

# Solution : toujours activer le venv AVANT pip install.
```

```
# Versionner ses données collectées
git add data/raw/
# → tu pousses potentiellement des données personnelles sur GitHub.
#   Le .gitignore est là pour éviter ça.
```

```bash
# Lancer python tout court alors qu'on est en venv
$ python script.py
# → sur certains systèmes, ça contourne le venv.
# Sur Linux/Mac, utilise `python3` explicitement, ou vérifie avec :
$ which python
```

## Exercices

**Guidé :** Crée l’arborescence ci-dessus, active un venv, installe `requests` et `beautifulsoup4`, génère `requirements.txt`, et lance le script `test_install.py`.

**Autonome :** Écris un `README.md` complet pour ton atelier, avec : objectif, prérequis, installation, structure des dossiers, et un rappel sur le cadre éthique (3-4 lignes).

## ✅ Tu sais maintenant…

- Pourquoi un atelier propre est indispensable en OSINT
- Créer une arborescence standard `src` / `data` / `logs` / `reports` / `config`
- Créer et activer un environnement virtuel
- Installer des bibliothèques et figer les versions dans `requirements.txt`
- Protéger tes secrets et données avec `.gitignore`

-----

# PARTIE I — FONDATIONS

> **Objectif de la partie :** comprendre **ce qu’on fait, pourquoi, et dans quel cadre**. Aucune ligne de code de scraping dans cette partie. Ce sont les fondations conceptuelles, juridiques et techniques. C’est aussi la partie qui te distingue d’un simple « scrapeur » : un analyste sérieux sait poser le cadre avant de toucher au clavier.

-----

# Chapitre 1 — Qu’est-ce que l’OSINT et le web scraping ?

## Le minimum à savoir

### Définitions, clairement

**OSINT (Open-Source Intelligence)** = renseignement obtenu à partir de **sources publiquement accessibles**. Les sources peuvent être :

- des sites web (médias, blogs, forums),
- des registres publics (entreprises, marques, domaines),
- des bases open data (gouvernementales, ONG),
- des médias sociaux (parties publiques uniquement),
- des publications scientifiques, des archives, etc.

**Scraping** = extraire automatiquement des données depuis une page web destinée à être lue par un humain (HTML).

**Crawling** = parcourir automatiquement un site en suivant ses liens, sans nécessairement en extraire des données.

**API (Application Programming Interface)** = une interface **prévue par le site** pour qu’un programme accède aux données, généralement en format JSON, souvent avec authentification et règles d’usage claires.

**Collecte manuelle** = un humain lit, copie, prend des captures d’écran. Lent, mais indispensable pour la vérification.

### Tableau comparatif

|Approche               |Vitesse |Stabilité    |Légitimité             |Quand l’utiliser                                            |
|-----------------------|--------|-------------|-----------------------|------------------------------------------------------------|
|**Manuel**             |⚪ Lent  |🟢 Très stable|🟢 Toujours OK          |Vérification, faibles volumes, sources sensibles            |
|**API**                |🟢 Rapide|🟢 Très stable|🟢 Cadre clair (CGU API)|Dès qu’elle existe — c’est presque toujours la bonne réponse|
|**Flux RSS / Atom**    |🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Veille d’actualités, blogs, publications régulières         |
|**Sitemap / open data**|🟢 Rapide|🟢 Stable     |🟢 Prévu pour ça        |Inventaire d’un site, datasets publics                      |
|**Scraping**           |🟡 Moyen |🔴 Fragile    |🟡 Cadre flou           |Dernier recours, quand rien d’autre n’existe                |

### La pyramide de la collecte OSINT

```
                  ┌─────────────────────┐
                  │   1. Lecture humaine │ ← toujours par là qu’on commence
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │     2. API officielle│
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   3. RSS / Atom      │
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   4. Sitemap / Open  │
                  │      Data            │
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │   5. Scraping HTML   │ ← dernier recours
                  └──────────────────────┘
```

> **À retenir :** on monte la pyramide **dans l’ordre**. On ne scrape pas un site dont l’API existe. On ne crawle pas un site qui publie un sitemap. Cette discipline est ce qui fait la différence entre un analyste OSINT pro et un script-kiddie.

### Cas d’usage défensifs typiques

|Domaine                   |Exemple concret                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------|
|**CTI**                   |Suivre les bulletins publics d’un éditeur de logiciels pour repérer les CVE critiques.     |
|**Brand protection**      |Surveiller la création de domaines proches de ta marque (typosquatting).                   |
|**Veille concurrentielle**|Suivre les annonces d’embauche d’un concurrent pour détecter une réorientation stratégique.|
|**Journalisme**           |Vérifier des prises de position publiques d’un acteur sur plusieurs années.                |
|**Recherche académique**  |Constituer un corpus de publications scientifiques d’un domaine.                           |
|**Transparence publique** |Suivre les modifications d’un règlement gouvernemental.                                    |
|**Sécurité de marque**    |Repérer les copies frauduleuses d’un site officiel.                                        |

### Ce que le scraping **n’est pas**

- **Ce n’est pas du hacking.** Tu accèdes à la même chose qu’un navigateur — tu n’exploites aucune faille.
- **Ce n’est pas une autorisation universelle.** Le fait qu’une page soit publique ne signifie pas que tu peux l’aspirer en masse.
- **Ce n’est pas magique.** Si le site change son HTML demain, ton script casse.
- **Ce n’est pas anonyme.** Chaque requête laisse une trace dans les logs du serveur cible : IP, User-Agent, horodatage, URL.

## Très utile en pratique

### Quand préférer une API à un scraper

Toujours, quand :

- l’API existe et donne accès aux données qui t’intéressent,
- les CGU de l’API t’autorisent ton usage,
- les rate limits sont compatibles avec ton volume.

L’API est **stable** (le site peut changer son HTML, l’API change rarement), **rapide**, **contractuelle** (tu sais ce que tu as le droit de faire), et **traçable** (souvent via une clé qui t’identifie).

### Quand préférer la lecture manuelle

- Quand le volume est petit (10-20 pages).
- Quand la source est sensible (forum spécialisé, presse engagée).
- Quand il faut interpréter le contenu, pas juste l’extraire.
- Quand l’automatisation présenterait un risque légal ou éthique.

### Notion de « source autoritative »

Une **source autoritative**, c’est la source d’origine — celle qui a publié l’information en premier. Privilégier les sources autoritatives :

- évite la déformation,
- permet de citer correctement,
- limite la duplication de données.

Exemple : pour une mention d’entreprise, le registre officiel des entreprises est autoritatif. Un agrégateur tiers ne l’est pas.

## Bonus

### L’écosystème OSINT au-delà de Python

Pour situer Python dans le paysage :

- **Maltego** : plateforme graphique de pivots OSINT.
- **SpiderFoot** : outil d’automatisation OSINT modulaire.
- **Recon-ng** : framework de reconnaissance en ligne de commande.

Ces outils existent et sont puissants. Apprendre à scripter en Python te donne quelque chose qu’ils n’ont pas : la flexibilité totale. Tu peux construire **exactement** ce dont tu as besoin, sans dépendance.

## ❌ Erreur classique

```
# Croire que "public" = "tout permis"
"Cette page est publique, donc je peux l’aspirer en boucle, vendre les
 données et en faire ce que je veux."
→ Faux. Le fait qu’une page soit accessible ne libère pas du droit
   applicable (CGU, RGPD, droits voisins, etc.).

# Sauter directement au scraping
"J’ai besoin des actualités de ce média, je vais scraper leur site."
→ Vérifie d’abord : ont-ils un flux RSS ? Une API ? Un sitemap ?
   Dans 80 % des cas, oui.

# Confondre OSINT et "espionnage en ligne"
"OSINT = trouver des trucs cachés sur les gens."
→ Non. OSINT = utiliser des sources publiques avec rigueur et éthique.
```

## Exercices

**Guidé :** Pour chacun des besoins suivants, dis quelle méthode est la plus appropriée (manuelle / API / RSS / sitemap / open data / scraping) et pourquoi :

1. Récupérer la météo de Paris pour les 7 prochains jours.
1. Surveiller les communiqués de presse d’une administration française.
1. Vérifier une information de CV à partir d’une page professionnelle publique fournie par la personne (lecture manuelle, sans automatisation).
1. Récupérer la liste des entreprises créées en 2024 en France.
1. Suivre les changements de tarification d’un concurrent.

**Autonome :** Choisis un sujet d’intérêt personnel (sport, jeu vidéo, actualité scientifique…) et :

1. Formule **une** question d’enquête claire en une phrase.
1. Liste 3 sources publiques pertinentes.
1. Pour chaque source, indique la méthode de collecte appropriée et justifie en 2 lignes.

## ✅ Tu sais maintenant…

- Distinguer OSINT, scraping, crawling, API et collecte manuelle
- Identifier les grands cas d’usage défensifs
- Choisir la méthode de collecte adaptée à un besoin
- La hiérarchie : manuel → API → RSS → sitemap/open data → scraping
- Ce que le scraping n’est **pas** (ni hacking, ni anonyme, ni stable)

-----

# Chapitre 2 — Cadre légal, éthique et OPSEC du scraping

> **Avertissement :** ce chapitre fournit des **repères**, pas un conseil juridique. Le droit applicable varie selon ton pays, ton statut (particulier, entreprise, journaliste, chercheur), la nature de la donnée et l’usage final. En cas de doute sur un projet réel, consulte un juriste.

## Le minimum à savoir

### Les 5 questions à se poser avant de scraper

Avant chaque collecte, ce mini-questionnaire :

```
1. La source est-elle publiquement accessible
   sans authentification ni contournement ?

2. Les CGU autorisent-elles cet usage automatisé ?

3. Le robots.txt comporte-t-il des restrictions
   pertinentes pour ce que je veux faire ?

4. La donnée comporte-t-elle des éléments personnels ?
   Si oui, ma collecte respecte-t-elle le principe
   de minimisation et un cadre juridique clair ?

5. Si le site m’écrivait demain pour me demander
   pourquoi je collecte, ma réponse serait-elle solide ?
```

> **Important :** CGU et robots.txt sont **deux choses distinctes**. Les CGU sont un texte contractuel, le robots.txt est une convention technique. Ils doivent être vérifiés séparément. Un robots.txt permissif ne dispense pas de lire les CGU, et inversement.

Si tu réponds **NON** ou **« je ne sais pas »** à l’une de ces questions, **arrête** la collecte automatisée et documente le doute avant d’aller plus loin. En enquête sérieuse, un doute non levé se transcrit dans la fiche d’enquête : c’est une trace honnête, pas une faiblesse.

### Données publiques ≠ données librement exploitables

C’est l’erreur la plus commune. Le fait qu’une donnée soit visible sans connexion ne signifie pas :

- qu’elle est libre de droits (un texte sur un blog reste protégé par le droit d’auteur),
- qu’elle peut être collectée massivement,
- qu’elle peut être republiée,
- qu’elle peut être traitée à des fins commerciales,
- qu’elle peut être croisée avec d’autres sources pour profiler des personnes.

**Une donnée publique reste soumise à un cadre.** Le scraping ne crée pas de droit ; il ne fait que techniquement automatiser une consultation.

### Le fichier `robots.txt`

C’est un fichier texte placé à la racine d’un site (`https://exemple.fr/robots.txt`) dans lequel le propriétaire indique aux robots ce qu’il accepte d’être parcouru.

Exemple :

```
User-agent: *
Disallow: /admin/
Disallow: /api/private/
Allow: /
Crawl-delay: 5

Sitemap: https://exemple.fr/sitemap.xml
```

Lecture :

- `User-agent: *` → règles pour tous les robots.
- `Disallow: /admin/` → ne pas parcourir cette section.
- `Crawl-delay: 5` → attendre 5 secondes entre deux requêtes.
- `Sitemap:` → emplacement du plan du site (bonus pour toi !).

> **Important :** `robots.txt` est une **convention**, pas une loi. Le respecter n’est pas une obligation juridique stricte, mais le **bafouer** est un signal très net que ta démarche est problématique. En pratique : on respecte robots.txt.

### Les CGU (Conditions Générales d’Utilisation)

Les CGU sont un **contrat** entre le service et toi. Beaucoup interdisent :

- l’accès automatisé,
- l’extraction massive,
- la réutilisation commerciale,
- la constitution de bases dérivées.

Lire les CGU avant de scraper professionnellement n’est pas optionnel. La portée juridique des CGU dépend de plusieurs facteurs (acceptation effective, position du droit local), mais leur violation peut t’exposer à des poursuites civiles, voire pénales selon le contexte.

### Le RGPD en 5 principes (UE)

Si tu touches à des **données personnelles** (un nom, un email, une photo identifiable…), tu entres dans le périmètre du RGPD. Cinq principes à retenir :

1. **Finalité** : tu dois savoir pour quoi tu collectes, et le dire clairement.
1. **Minimisation** : tu collectes le strict nécessaire.
1. **Base légale** : tu dois pouvoir justifier ta collecte (intérêt légitime, mission d’intérêt public, etc.).
1. **Conservation limitée** : tu ne gardes pas indéfiniment.
1. **Droits des personnes** : la personne peut demander accès, rectification, suppression.

Pour un projet OSINT défensif sérieux qui touche des données personnelles, un **registre des traitements** simplifié est une bonne pratique.

### Ce qu’on ne fait **jamais**

- Contourner une authentification.
- Utiliser un compte qui n’est pas le sien.
- Exploiter une faille technique (CAPTCHA bypass, exploitation d’une vulnérabilité).
- Scraper massivement des données personnelles pour profilage commercial.
- Republier des contenus protégés sans autorisation.
- Surcharger un site (assimilable à un déni de service).
- Constituer des listes de prospection à partir d’emails moissonnés.

## Très utile en pratique

### Le principe de minimisation, en action

Tu surveilles un blog d’expert pour de la veille. La minimisation, c’est :

- ❌ Aspirer tout le blog tous les jours pour tout garder.
- ✅ Récupérer la liste des nouveaux articles publiés depuis ta dernière collecte.

Tu surveilles les annonces d’embauche d’un concurrent. La minimisation, c’est :

- ❌ Stocker le profil complet de chaque candidat mentionné.
- ✅ Stocker uniquement intitulé du poste, date de publication et URL.

### La traçabilité, en pratique

Chaque enregistrement de ta collecte doit contenir, au minimum :

|Champ         |Exemple                         |
|--------------|--------------------------------|
|`source_url`  |`https://exemple.fr/article/123`|
|`collected_at`|`2026-05-17T14:32:11Z`          |
|`tool`        |`mon-collecteur/0.3.1`          |
|`status_code` |`200`                           |
|`content_hash`|`a3f5...` (SHA-256 du HTML brut)|

Ces métadonnées sont **non négociables**. Sans elles, ta collecte n’est pas reproductible et n’a aucune valeur d’enquête.

### Identifier honnêtement ton script

Quand tu envoies une requête, le serveur reçoit un header `User-Agent`. Par défaut, `requests` envoie quelque chose comme `python-requests/2.31.0`. C’est honnête, mais peu informatif.

**Bonne pratique** : un User-Agent identifiable, qui dit qui tu es et comment te contacter en cas de problème :

```
MonOutilOSINT/0.1 (+contact: osint-projet@example.org)
```

> **OPSEC :** utilise idéalement une adresse **dédiée au projet** (ex. `osint-veille@<ton-domaine>`, un alias, ou une boîte spécifique), **pas** ton adresse personnelle principale. Si quelqu’un veut te recontacter ou te signaler un problème, c’est très bien. Si l’adresse fuit dans des dumps, des spams ou des listes, tu veux que ce soit l’alias projet, pas ta boîte principale.

**Mauvaise pratique** : se faire passer pour un navigateur récent pour échapper aux filtres anti-bot. Sauf cas pédagogique très balisé, c’est un signal d’intention douteuse.

### Charte personnelle de l’analyste OSINT

Voici un modèle, à adapter et signer (au sens : à t’engager intérieurement à respecter) :

```
1. Je collecte des données publiques pour des finalités défensives,
   de veille, de recherche ou de transparence.
2. Je respecte robots.txt et les CGU des sites que je consulte.
3. Je collecte le minimum nécessaire à ma question d’enquête.
4. Je trace systématiquement la source, la date et la méthode.
5. Je ne contourne aucune protection technique.
6. Je n’utilise pas mes outils contre des personnes physiques
   sans cadre légal explicite (mission, mandat, ordre légitime).
7. Je ne republie pas de données protégées sans autorisation.
8. Je respecte le rythme des serveurs (rate limit volontaire).
9. Je m’identifie honnêtement (User-Agent, contact).
10. En cas de doute, je m’arrête et je consulte.
```

## ❌ Erreur classique

```
# Croire que robots.txt protège juridiquement
"Le site a un robots.txt qui interdit le scraping, donc je m’expose
 à des poursuites si je passe outre."
→ Pas si simple. robots.txt est une convention, pas un dispositif
   contractuel. Mais l’ignorer est un signal fort de mauvaise foi
   qui pèsera lourd si un litige survient.

# Croire que l’absence de robots.txt = autorisation
"Pas de robots.txt, donc je peux tout faire."
→ Faux. Les CGU s’appliquent, le droit d’auteur s’applique, le RGPD
   s’applique. robots.txt n’est qu’un signal additionnel.

# Tester le scraper agressif directement sur la cible
"Je veux voir à partir de combien de requêtes le site bloque."
→ Ne fais jamais ça. Tu peux dégrader un service public, exposer
   ton IP, et déclencher des procédures de sécurité automatiques.
   Pour tester un scraper, utilise des sites bac à sable
   (toscrape.com, httpbin.org).

# Confondre "données accessibles" et "données librement réutilisables"
"Cet article de presse est lisible sans abonnement, je peux le
 republier sur mon site."
→ Faux. Le droit d’auteur s’applique indépendamment du paywall.
```

## Bonus

### Affaires juridiques de référence (à titre culturel)

> Ces affaires sont citées **à titre indicatif**. Elles évoluent, leurs conclusions ne sont pas transposables tel quel à ton cas. Pour un projet réel, vérifie l’état du droit avec un juriste.

- **hiQ Labs vs LinkedIn (États-Unis)** : longue bataille judiciaire sur le scraping de profils publics, illustrant la complexité du « public » en pratique.
- **Ryanair vs PR Aviation (UE)** : a précisé que les CGU peuvent restreindre l’usage automatisé même si les données ne sont pas protégées par un droit sui generis.
- **Décisions CNIL** : sanctions répétées sur des moissonnages d’emails à des fins commerciales.

L’annexe C de ce cours liste des ressources pour aller plus loin.

## Exercices

**Guidé :** Récupère manuellement (dans ton navigateur) les fichiers `robots.txt` de trois sites de natures différentes :

1. un grand média (ex. `lemonde.fr/robots.txt`),
1. une administration publique (ex. `service-public.fr/robots.txt`),
1. un site bac à sable (`books.toscrape.com/robots.txt`).

Pour chacun, identifie :

- les sections interdites (`Disallow`),
- la présence éventuelle d’un `Crawl-delay`,
- la présence d’un `Sitemap`.

**Autonome :** Rédige ta propre charte OSINT en 10 règles maximum. Garde-la dans `config/charte.md` à la racine de ton projet. C’est un engagement, pas une décoration.

## ✅ Tu sais maintenant…

- Les 5 questions préalables à toute collecte
- Que « données publiques » ne signifie pas « données librement exploitables »
- Lire et interpréter un `robots.txt`
- Les 5 principes RGPD applicables aux données personnelles
- Ce qu’on ne fait jamais
- Identifier honnêtement son script via User-Agent
- Tenir un cadre éthique personnel

-----

# Chapitre 3 — Comment fonctionne le web (vu côté collecteur)

Avant de coder une requête, il faut comprendre **ce qu’on demande, à qui, et ce qu’on récupère**. Ce chapitre est volontairement dense — c’est le socle technique de tout ce qui suit.

## Le minimum à savoir

### Le modèle client / serveur

```
        REQUÊTE
   ┌──────────────────────►
[CLIENT]                  [SERVEUR]
   │  (ton navigateur       │  (le site web)
   │   ou ton script)       │
   ◄──────────────────────┘
        RÉPONSE
```

À chaque action sur le web, ton **client** (navigateur ou script Python) envoie une **requête** à un **serveur**, et reçoit une **réponse**.

Une requête, c’est : « donne-moi cette URL ». Une réponse, c’est : « voilà le contenu (ou voilà pourquoi je ne peux pas) ».

### Anatomie d’une URL

```
https://www.exemple.fr:443/articles/2026/recent?page=2&sort=date#commentaires
  │       │           │   │                     │                │
  │       │           │   │                     │                └── Fragment (côté client uniquement)
  │       │           │   │                     └─────────────────── Query string (paramètres)
  │       │           │   └───────────────────────────────────────── Chemin (path)
  │       │           └───────────────────────────────────────────── Port (souvent implicite : 443 pour HTTPS)
  │       └───────────────────────────────────────────────────────── Hôte (host)
  └─────────────────────────────────────────────────────────────────── Schéma (protocole)
```

|Partie      |Rôle                                                               |
|------------|-------------------------------------------------------------------|
|**Schéma**  |`https` ou `http`. HTTPS = chiffré, HTTP = en clair.               |
|**Hôte**    |Le serveur cible. Souvent un sous-domaine (`www`).                 |
|**Port**    |Le canal d’écoute. 443 pour HTTPS, 80 pour HTTP. Souvent implicite.|
|**Chemin**  |Le « dossier/fichier » côté serveur.                               |
|**Query**   |Paramètres après le `?`, séparés par `&`. Clé/valeur.              |
|**Fragment**|Après le `#`. **Jamais envoyé au serveur** — ancre côté client.    |


> **À retenir :** le fragment (`#...`) ne sert qu’au navigateur pour scroller jusqu’à une ancre. Il n’est **pas** envoyé dans la requête HTTP.

### HTTPS vs HTTP

**HTTPS** chiffre la communication entre toi et le serveur. **HTTP** la laisse en clair. Aujourd’hui, presque tous les sites sont en HTTPS.

Pour un scraper, ça change peu — `requests` gère HTTPS de manière transparente. Mais à savoir : HTTPS protège **le contenu**, pas l’identité (le serveur sait toujours qui tu es par ton IP).

### Une requête HTTP en détail

Une requête HTTP, en réalité, ressemble à ceci (côté coulisses) :

```
GET /articles/123 HTTP/1.1
Host: www.exemple.fr
User-Agent: MonOutilOSINT/0.1
Accept: text/html
Accept-Language: fr-FR,fr;q=0.9

(corps vide pour un GET)
```

Trois parties :

1. **Ligne de requête** : méthode (`GET`), chemin (`/articles/123`), version HTTP.
1. **Headers** : métadonnées (qui demande, ce qu’il accepte, etc.).
1. **Corps** (optionnel) : pour les requêtes qui envoient des données (POST, PUT).

Et une réponse :

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1532

<!DOCTYPE html>
<html>...
```

1. **Ligne de statut** : version, code, message.
1. **Headers** : métadonnées de la réponse.
1. **Corps** : le contenu (HTML, JSON, image, etc.).

### Les méthodes HTTP

Tu en croiseras surtout deux :

|Méthode |Sens                           |Quand                                        |
|--------|-------------------------------|---------------------------------------------|
|**GET** |« Donne-moi cette ressource »  |Lecture. C’est 95 % de ce qu’un scraper fait.|
|**POST**|« Voici des données à traiter »|Envoi de formulaire, création de ressource.  |

Les autres (`PUT`, `DELETE`, `HEAD`, `OPTIONS`) existent, mais sont rares en OSINT défensif.

### Les codes de statut

|Code         |Famille             |Sens                                      |
|-------------|--------------------|------------------------------------------|
|**200**      |2xx — Succès        |OK, la ressource est dans le corps.       |
|**301 / 302**|3xx — Redirection   |La ressource a déménagé.                  |
|**400**      |4xx — Erreur client |Ta requête est malformée.                 |
|**401**      |4xx                 |Authentification requise.                 |
|**403**      |4xx                 |Accès interdit.                           |
|**404**      |4xx                 |Pas trouvé.                               |
|**429**      |4xx                 |**Trop de requêtes** — tu vas trop vite.  |
|**500**      |5xx — Erreur serveur|Le serveur a planté.                      |
|**503**      |5xx                 |Service indisponible (souvent temporaire).|


> **À retenir :** un `200` n’est **pas** une garantie de succès logique. Un site peut renvoyer une page d’erreur ou « contenu introuvable » en `200`. Toujours vérifier le **contenu**, pas juste le statut.

### Les headers importants

|Header                    |Rôle                                                        |
|--------------------------|------------------------------------------------------------|
|`User-Agent`              |Dit qui fait la requête.                                    |
|`Accept`                  |Types de contenu acceptés (`text/html`, `application/json`).|
|`Accept-Language`         |Langues préférées.                                          |
|`Referer`                 |D’où vient la requête (page précédente).                    |
|`Cookie`                  |Données de session côté client.                             |
|`Content-Type` (réponse)  |Format du corps renvoyé.                                    |
|`Content-Length` (réponse)|Taille du corps.                                            |

### HTML, balises, attributs

Le HTML est un langage de **structure**. Il décrit la mise en forme d’une page sous forme d’arborescence.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Mon article</title>
  </head>
  <body>
    <article class="post" id="article-123">
      <h1>Titre de l'article</h1>
      <p class="lead">Introduction.</p>
      <a href="https://exemple.fr/source">Source</a>
    </article>
  </body>
</html>
```

- Une **balise** est délimitée par `<...>` et `</...>` (ou auto-fermée comme `<img />`).
- Un **attribut** est une info dans la balise ouvrante (`class="post"`, `href="..."`).
- La **classe** (`class`) sert à grouper des éléments stylés similairement.
- L’**identifiant** (`id`) est unique dans la page.

### Le DOM : l’arbre des éléments

Une fois la page chargée, le navigateur en construit une représentation en **arbre** : le **DOM (Document Object Model)**.

```
html
├── head
│   └── title
└── body
    └── article (.post #article-123)
        ├── h1
        ├── p (.lead)
        └── a (href=...)
```

C’est dans cet arbre que tu vas naviguer pour extraire ce qui t’intéresse, en utilisant des **sélecteurs CSS**.

### Les sélecteurs CSS

Quelques exemples qui couvrent 90 % des cas :

|Sélecteur         |Cible                                          |
|------------------|-----------------------------------------------|
|`a`               |Toutes les balises `<a>`                       |
|`.post`           |Tous les éléments avec `class="post"`          |
|`#article-123`    |L’élément avec `id="article-123"`              |
|`article p`       |Tous les `<p>` à l’intérieur d’un `<article>`  |
|`article > h1`    |Les `<h1>` enfants **directs** d’un `<article>`|
|`a[href^="https"]`|Les `<a>` dont `href` commence par `https`     |
|`p.lead`          |Les `<p>` qui ont la classe `lead`             |

Ces sélecteurs sont les mêmes qu’en CSS pour styliser une page. BeautifulSoup les comprend tels quels.

### Site statique vs site dynamique

|Type         |Comment ça marche                                                                                   |Conséquence pour le scraping                                 |
|-------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
|**Statique** |Le serveur envoie directement le HTML final.                                                        |`requests` reçoit ce que tu vois. Facile à scraper.          |
|**Dynamique**|Le serveur envoie un squelette + du JavaScript. Le navigateur exécute le JS pour construire la page.|`requests` ne reçoit **que** le squelette. Le contenu manque.|

**Comment savoir ?** Dans ton navigateur, ouvre la page, fais clic droit → **« Afficher le code source »** (pas « Inspecter »). Si tu vois le texte qui t’intéresse dans le code source brut, c’est statique. Sinon, c’est dynamique et `requests` ne suffira pas.

> **À retenir :** pour les sites dynamiques, on commence **toujours** par chercher la source plus propre (API, RSS, sitemap). Les outils de pilotage de navigateur (Playwright, Selenium) sont un **dernier recours** dans un cadre autorisé.

### Les DevTools du navigateur

Apprends à utiliser les outils de développement de ton navigateur (F12 ou clic droit → « Inspecter ») :

|Onglet                      |À quoi ça sert                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------|
|**Elements** (ou Inspecteur)|Voir et explorer le DOM, identifier les sélecteurs.                                                       |
|**Network** (ou Réseau)     |Voir toutes les requêtes que la page fait. Indispensable pour repérer un endpoint JSON appelé par la page.|
|**Console**                 |Tester des sélecteurs, lire les erreurs JS.                                                               |


> **Méthode** : sur la page, clic droit sur l’élément qui t’intéresse → « Inspecter ». Le DOM s’ouvre exactement sur ce nœud. Tu peux y lire la classe, l’id, la hiérarchie. C’est comme ça qu’on construit un sélecteur CSS fiable.

## Très utile en pratique

### Reconnaître un site dynamique en 30 secondes

1. Ouvre la page dans ton navigateur.
1. Clic droit → « Afficher le code source » (Ctrl+U).
1. Ctrl+F → cherche un mot que tu vois à l’écran.
1. Trouvé ? → Statique. Pas trouvé ? → Dynamique.

C’est la première chose à faire avant d’écrire le moindre scraper.

### Identifier un endpoint JSON publiquement appelé par la page

Beaucoup de sites « dynamiques » récupèrent leurs données en appelant une URL JSON depuis le navigateur. C’est souvent **bien plus propre à exploiter** que le HTML rendu.

1. Ouvre les DevTools (F12) → onglet **Network**.
1. Recharge la page.
1. Filtre sur **XHR** ou **Fetch**.
1. Repère les réponses en JSON.
1. Clique → onglet **Response** → tu vois la donnée brute.

Si tu trouves un endpoint qui sert exactement ce qui t’intéresse, **change de stratégie** : interroge cet endpoint directement (chapitre 11), c’est plus stable et plus propre que de scraper le HTML rendu.

> **Vocabulaire :** on ne parle pas d’« API cachée ». L’endpoint est appelé en clair par la page que tu visites — il est publiquement observable. On parle simplement de **l’endpoint JSON appelé par la page**.

### Pourquoi un scraper casse

Un scraper est par nature **fragile**. Voici les causes typiques de casse :

|Cause                           |Symptôme                                                   |Mitigation                                             |
|--------------------------------|-----------------------------------------------------------|-------------------------------------------------------|
|**Changement de HTML**          |Le sélecteur ne trouve plus rien.                          |Sélecteurs robustes (id stables, attributs `data-*`).  |
|**Classes CSS dynamiques**      |Classes du genre `css-x7f3k2`, qui changent à chaque build.|Cibler par structure plutôt que par classe.            |
|**Contenu chargé en JavaScript**|Données absentes du HTML brut.                             |API ou RSS ; en dernier recours, navigateur automatisé.|
|**Pagination modifiée**         |Les pages 2, 3… renvoient autre chose.                     |Détection d’arrêt explicite ; logs.                    |
|**Redirections (301/302)**      |Tu collectes la mauvaise URL.                              |Lire `response.url` après la requête.                  |
|**Erreurs réseau (timeouts)**   |Requêtes qui pendent ou échouent.                          |Timeout obligatoire, retries.                          |
|**Encodage**                    |Caractères cassés (`Ã©` au lieu de `é`).                   |Forcer `utf-8`, vérifier `response.encoding`.          |
|**Contenu personnalisé**        |Pages qui changent selon la langue, le pays, la session.   |Headers explicites, isolation de session.              |
|**Anti-bot**                    |Captcha, bannissement IP, 403 systématique.                |Signal qu’il faut chercher l’API ou abandonner.        |


> **À retenir :** un scraper sera révisé. Plusieurs fois. C’est normal. La qualité d’un scraper se mesure non pas à sa beauté du premier jour, mais à la facilité avec laquelle on le maintient quand le site change.

## ❌ Erreur classique

```
# Confondre "ce que je vois dans le navigateur"
# et "ce que requests reçoit"

L’apprenant ouvre la page, voit les données, écrit son scraper,
et obtient une page vide → c’était un site dynamique.

→ Toujours faire le test "Afficher le code source" avant de coder.

# Oublier l’encodage
Le HTML est en UTF-8, mais le système suppose autre chose.
Résultat : "Caf\u00e9" ou "Café" devient "Café".

→ Toujours forcer encoding="utf-8" en écriture, et vérifier
   response.encoding en lecture.

# Cibler par classe générée dynamiquement
Le scraper utilise .css-x7f3k2 comme sélecteur. Une semaine
plus tard, c’est .css-y9h4m1 et tout casse.

→ Préférer les id stables, les attributs sémantiques
   (data-testid, role), ou la structure (article > h1).

# Considérer un 200 comme une réussite
Le site renvoie 200 + page "article introuvable".
Le scraper enregistre du vide en pensant que tout va bien.

→ Vérifier le contenu en plus du statut.
```

## Bonus

### Les en-têtes de sécurité (culture générale)

Tu croiseras parfois des headers comme :

- `Content-Security-Policy` (CSP)
- `Strict-Transport-Security` (HSTS)
- `X-Frame-Options`

Ce sont des mécanismes de **défense du site**, qui n’affectent pas directement le scraping en lecture, mais qui te donnent une indication sur le sérieux de l’hébergeur.

### Cookies et sessions

Un cookie est un petit fichier que le serveur demande au client de garder. À la requête suivante, le client renvoie ce cookie, ce qui permet au serveur de « reconnaître » la session.

En OSINT défensif, on touche peu aux cookies — on travaille sur des contenus accessibles **sans session**. Si une donnée nécessite d’être connecté pour être vue, c’est qu’elle n’est pas vraiment publique.

## Exercices

**Guidé :** Sur la page `https://books.toscrape.com/` :

1. Ouvre les DevTools, onglet Elements.
1. Trouve la balise contenant le premier livre.
1. Note sa balise, ses classes, et la hiérarchie jusqu’au titre du livre.
1. Construis un sélecteur CSS qui ciblerait **uniquement** les titres de livres.

**Autonome :** Trouve un site **public non sensible** (idéalement un média, une documentation, un site institutionnel ou un site d’open data) qui charge certaines de ses données via JavaScript :

1. Identifie-le (clic droit → « Afficher le code source », données absentes du HTML brut).
1. Ouvre l’onglet Network des DevTools, recharge, filtre sur XHR/Fetch.
1. Identifie un endpoint JSON appelé par la page.
1. Note son URL et la structure de sa réponse (clés principales).

> **Important :** l’objectif de cet exercice est **uniquement d’observer** le mécanisme dans les DevTools. **Ne lance aucune collecte automatisée** sur cet endpoint à ce stade. La question « ai-je le droit d’interroger cet endpoint en boucle ? » se traite avec la fiche d’enquête et les chapitres suivants, pas par curiosité technique.

## ✅ Tu sais maintenant…

- Décomposer une URL et lire ses parties
- Le modèle requête/réponse HTTP
- Les principaux codes de statut (200, 301, 403, 404, 429, 500)
- Les headers utiles (`User-Agent`, `Accept`, etc.)
- Lire un arbre HTML et utiliser les sélecteurs CSS
- Distinguer site statique et site dynamique en 30 secondes
- Repérer un endpoint JSON appelé par la page via les DevTools
- Anticiper les causes typiques de casse d’un scraper

-----

# Chapitre 4 — Choisir la source la plus propre

Avant d’écrire ton premier scraper, **un dernier réflexe à intégrer** : chercher systématiquement la source la plus propre. C’est ce qui transforme un script jetable en démarche d’enquête durable.

## Le minimum à savoir

### La hiérarchie des sources

Quand tu as identifié l’information que tu cherches, monte la pyramide **dans cet ordre** :

```
1. API officielle              → propre, contractuel, stable
        ↓ (si absente)
2. Flux RSS / Atom             → léger, prévu pour ça
        ↓
3. Sitemap XML                 → inventaire complet du site
        ↓
4. Open data (CSV, JSON)       → données publiées intentionnellement
        ↓
5. Scraping HTML               → dernier recours
```

À chaque étape, demande-toi : **« Cette source répond-elle à ma question ? »** Si oui, arrête de monter, descends à l’étape « écrire le code ».

### Pourquoi cet ordre ?

|Critère                  |API      |RSS          |Sitemap |Open data|Scraping     |
|-------------------------|---------|-------------|--------|---------|-------------|
|Prévu pour les programmes|✅        |✅            |✅       |✅        |❌            |
|Stable dans le temps     |🟢        |🟢            |🟢       |🟢        |🔴            |
|Charge serveur           |🟢 Faible |🟢 Faible     |🟢 Faible|🟢 Faible |🔴 Plus lourde|
|Cadre légal clair        |🟢 CGU API|🟢            |🟢       |🟢 Licence|🟡 Flou       |
|Effort de développement  |🟡 Moyen  |🟢 Très faible|🟢 Faible|🟢 Faible |🔴 Élevé      |

À chaque ligne, le scraping perd. Ce n’est pas un hasard si on le place en dernier.

### Reconnaître une API

Une API REST t’expose des données sous forme d’URLs qui renvoient du **JSON** (généralement). Exemple :

```
https://api.exemple.fr/v1/articles?published=2026-05
```

Réponse :

```json
{
  "articles": [
    {"id": 123, "title": "Hello", "published_at": "2026-05-10"},
    {"id": 124, "title": "World", "published_at": "2026-05-11"}
  ],
  "next": "https://api.exemple.fr/v1/articles?page=2"
}
```

Pour savoir si un site propose une API :

- Cherche `<site> API` sur ton moteur préféré.
- Vérifie `<site>/api`, `<site>/developers`, `<site>/dev`.
- Lis la documentation des grandes plateformes (la plupart en proposent).

### Reconnaître un flux RSS / Atom

Un flux RSS, c’est un fichier XML standardisé que les sites publient pour signaler leurs **nouveaux contenus**. C’est **fait pour la veille**.

Exemple typique d’URL :

```
https://exemple.fr/feed
https://exemple.fr/rss
https://exemple.fr/atom.xml
https://exemple.fr/index.xml
```

Contenu d’un flux RSS (simplifié) :

```xml
<rss version="2.0">
  <channel>
    <title>Mon blog</title>
    <link>https://exemple.fr</link>
    <item>
      <title>Mon article</title>
      <link>https://exemple.fr/article-1</link>
      <pubDate>Mon, 12 May 2026 10:00:00 GMT</pubDate>
      <description>Résumé de l’article...</description>
    </item>
  </channel>
</rss>
```

C’est **structuré**, **léger**, **prévu pour les programmes**. Pour de la veille de blogs, médias, podcasts, agences gouvernementales : c’est presque toujours le bon choix.

> **Comment trouver le flux d’un site ?** Beaucoup de sites mettent un lien « RSS » dans leur footer. Sinon, regarde dans le code source de la page : un `<link rel="alternate" type="application/rss+xml" href="...">` indique le flux.

### Reconnaître un sitemap XML

Un sitemap, c’est un **plan du site** au format XML, listant les URLs publiques. Il est destiné aux moteurs de recherche, mais tu peux l’utiliser pour :

- inventorier les pages d’un site sans crawler,
- détecter les nouvelles publications,
- découvrir des sections que la navigation ne met pas en avant.

Localisation habituelle :

```
https://exemple.fr/sitemap.xml
https://exemple.fr/sitemap_index.xml
```

Et son emplacement est souvent indiqué dans le `robots.txt` (`Sitemap: https://...`).

Contenu :

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://exemple.fr/article-1</loc>
    <lastmod>2026-05-12</lastmod>
  </url>
  <url>
    <loc>https://exemple.fr/article-2</loc>
    <lastmod>2026-05-13</lastmod>
  </url>
</urlset>
```

### Reconnaître un dataset open data

Les administrations, ONG, institutions de recherche publient leurs données en accès libre, souvent en CSV, JSON ou API dédiée.

Portails à connaître :

- **France** : `data.gouv.fr`
- **Union européenne** : `data.europa.eu`
- **International** : `data.worldbank.org`, `data.un.org`
- **Recherche** : Zenodo, OpenAIRE

Pour un sujet donné, avant de scraper : **vérifie qu’un dataset open data n’existe pas déjà**. Tu gagnes du temps et tu obtiens des données autoritatives.

### Quand le scraping est-il justifié ?

|Situation                                                                                            |Justifié ?                             |
|-----------------------------------------------------------------------------------------------------|---------------------------------------|
|Le site n’a ni API, ni RSS, ni sitemap, ni open data, et l’information est essentielle à ton enquête.|✅                                      |
|Le site a une API mais elle ne couvre pas l’info que tu cherches.                                    |✅ (raisonnable)                        |
|Le site a un RSS mais tu trouves le scraping « plus pratique ».                                      |❌                                      |
|Tu veux scraper « pour t’entraîner ».                                                                |✅ uniquement sur des sites bac à sable.|

## Très utile en pratique

### Méthode en 5 étapes pour choisir la bonne source

```
1. Définir précisément la donnée cherchée.

2. Vérifier les sources alternatives :
   - L’éditeur a-t-il une API ?
   - Y a-t-il un flux RSS sur cette section ?
   - robots.txt mentionne-t-il un sitemap ?
   - Existe-t-il un dataset open data sur le sujet ?

3. Si oui à une de ces options : changer de stratégie,
   ne pas scraper.

4. Si non : vérifier robots.txt et CGU pour le scraping.

5. Si OK : scraper, le plus poliment possible.
```

### Cas d’usage classés

|Besoin                                          |Source idéale              |
|------------------------------------------------|---------------------------|
|Suivre les nouveaux articles d’un blog          |RSS                        |
|Suivre les communiqués officiels d’un ministère |RSS + open data            |
|Récupérer la météo                              |API (Open-Meteo)           |
|Lister tous les articles d’un site              |Sitemap                    |
|Obtenir des statistiques économiques            |Open data (INSEE, Eurostat)|
|Suivre les commits d’un projet open source      |API GitHub                 |
|Récupérer les modifications d’une page Wikipedia|API MediaWiki              |
|Suivre les nouveaux noms de domaine en `.fr`    |Open data AFNIC            |
|Comparer des prix sur un site sans API ni RSS   |Scraping (avec précautions)|

## ❌ Erreur classique

```
# Ignorer la documentation officielle
"Le site n’a probablement pas d’API."
→ Tu n’en sais rien tant que tu n’as pas regardé.
   Cherche "<site> developer", "<site> API", "<site> docs".

# Scraper un site qui publie un RSS
"Je vais scraper la page des actualités pour suivre les nouveaux articles."
→ Le RSS te donne exactement ça, en plus propre.
   Vérifie /feed, /rss, /atom.xml, /index.xml.

# Confondre sitemap et liste exhaustive
"Le sitemap doit contenir toutes les URLs du site."
→ Pas forcément. Beaucoup de sites n’y mettent que les pages
   destinées à l’indexation. Lis ce que le sitemap propose,
   ne suppose pas.

# Pousser une API jusqu’au rate limit
"L’API marche, je vais aspirer tout d’un coup."
→ Toute API a des limites. Lis la doc, respecte les rate limits.
   Un compte bloqué est un compte qui ne sert plus à rien.
```

## Bonus

### Parser un flux RSS rapidement

`feedparser` est la bibliothèque Python de référence pour lire les flux RSS / Atom :

```bash
pip install feedparser
```

```python
import feedparser

flux = feedparser.parse("https://exemple.fr/feed")
for article in flux.entries[:5]:
    print(article.title, "-", article.link)
```

C’est plus simple et plus stable que de parser le XML à la main. On y reviendra dans la partie sur les sources alternatives au scraping.

### Lire un sitemap

Un sitemap est du XML simple, parsable avec la bibliothèque standard :

```python
import requests
from xml.etree import ElementTree as ET

# Remplace l’URL par celle d’un site qui expose réellement un sitemap.
# Vérifie d’abord son existence (souvent indiquée dans robots.txt).
SITEMAP_URL = "https://exemple.fr/sitemap.xml"

r = requests.get(SITEMAP_URL, timeout=10)
root = ET.fromstring(r.content)
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [loc.text for loc in root.findall(".//sm:loc", ns)]
print(f"{len(urls)} URLs trouvées")
```

## Exercices

**Guidé :** Pour `https://www.lemonde.fr` :

1. Cherche si un flux RSS existe (inspecte la page d’accueil, cherche un lien « RSS »).
1. Vérifie le `robots.txt`.
1. Y a-t-il un `Sitemap:` mentionné ?
1. Compare : si tu voulais suivre les nouveaux articles, quelle serait la méthode la plus propre ?

**Autonome :** Choisis trois sites de natures différentes que tu consultes régulièrement (un média, une administration, une plateforme). Pour chacun, identifie :

1. Existe-t-il une API publique ?
1. Existe-t-il un flux RSS ?
1. Existe-t-il un sitemap ?
1. Existent des datasets open data sur des sujets connexes ?

Compile tes résultats dans un tableau Markdown.

## 🧩 Mini-projet de Partie I — *Fiche d’enquête*

Avant de passer à la pratique, prépare le **gabarit de fiche d’enquête** que tu rempliras pour chaque mini-projet du reste du cours. Crée le fichier `config/fiche-enquete.md` :

```markdown
# Fiche d’enquête

## Métadonnées
- Titre :
- Auteur :
- Date de création :
- Version :

## Question
- Question d’enquête (1 phrase) :

## Sources
- Sources envisagées :
- API officielle disponible ? (oui/non, URL) :
- Flux RSS disponible ? (oui/non, URL) :
- Sitemap disponible ? (oui/non, URL) :
- Open data pertinent ? (oui/non, URL) :

## Méthode
- Méthode retenue :
- Justification (pourquoi pas une source plus propre ?) :

## Cadre
- robots.txt vérifié (oui/non, extraits pertinents) :
- CGU vérifiées (oui/non) :
- Base légale et finalité :
- Données personnelles concernées ? (oui/non, lesquelles) :

## Collecte
- Données minimales collectées (liste exhaustive) :
- Format de sortie :
- Volume attendu :
- Délai entre requêtes :
- Plafond de volume :

## Limites
- Angles morts identifiés :
- Risques techniques (site dynamique, anti-bot) :
- Risques éthiques :
```

Cette fiche t’accompagnera dans tous les projets suivants.

## ✅ Tu sais maintenant…

- La hiérarchie des sources : API > RSS > sitemap > open data > scraping
- Pourquoi cet ordre n’est pas négociable
- Reconnaître une API, un flux RSS, un sitemap, un dataset open data
- Trouver ces ressources sur un site donné
- La méthode en 5 étapes pour choisir la bonne source
- Quand le scraping est réellement justifié

-----

> **🎯 Tu as terminé la Partie I.**
> 
> Tu n’as pas encore écrit une seule requête. C’est volontaire. Tout ce qui suit — `requests`, BeautifulSoup, APIs, veille — va beaucoup plus loin et beaucoup plus vite parce que tu as posé les fondations.
> 
> La Partie II commence par `requests` : la bibliothèque qui fait dialoguer ton script avec le web.

-----

# PARTIE II — PREMIÈRES COLLECTES

> **Objectif de la partie :** récupérer **une** page web, en extraire ce qu’on veut, et le faire proprement. On reste sur une page à la fois. Toute la mécanique multi-pages, APIs, et passage à l’échelle viendra dans les parties suivantes.
> 
> **Pré-requis pour cette partie :** ta fiche d’enquête est remplie (cible identifiée, méthode justifiée, robots.txt vérifié). Si ce n’est pas le cas, retour au chapitre 4.

-----

# Chapitre 5 — Premières requêtes avec `requests`

C’est ton premier chapitre où on touche au clavier pour faire dialoguer ton script avec un serveur. La règle d’or de ce chapitre : **on récupère, on sauvegarde, on parse hors ligne**. On ne tape pas le serveur dix fois pendant qu’on debug le parser.

> **Checklist avant chaque requête réelle :**
> 
> - ☑ Cible pédagogique (`toscrape.com`, `httpbin.org`) ou autorisée par les CGU
> - ☑ `robots.txt` consulté
> - ☑ CGU vérifiées si cible réelle
> - ☑ User-Agent identifiable défini
> - ☑ `timeout=` défini sur toutes les requêtes
> - ☑ Volume limité (plafond explicite)
> - ☑ Sauvegarde brute dans `data/raw/` prévue
> 
> Si une case n’est pas cochée, ne lance pas le script.

## Le minimum à savoir

### Installation rappel

Si tu as fait le chapitre 0, c’est déjà installé. Sinon :

```bash
source .venv/bin/activate
pip install requests
```

Vérifie :

```python
import requests
print(requests.__version__)
```

### La première requête

```python
import requests

response = requests.get("https://httpbin.org/get", timeout=10)
print(response.status_code)
print(response.text[:200])
```

Trois choses essentielles :

1. **`requests.get(url, ...)`** envoie une requête GET.
1. **`timeout=10`** : **non négociable**. Sans timeout, ton script peut pendre indéfiniment si le serveur ne répond pas.
1. **`response`** est l’objet qui contient toute la réponse.

> **À retenir :** **jamais** de `requests.get()` sans `timeout=`. C’est la première règle des scripts web.

### L’objet Response

|Attribut              |Contenu                                    |
|----------------------|-------------------------------------------|
|`response.status_code`|Code de statut (`200`, `404`, etc.)        |
|`response.text`       |Corps de la réponse en `str` (texte décodé)|
|`response.content`    |Corps de la réponse en `bytes` (brut)      |
|`response.headers`    |Dictionnaire des headers de réponse        |
|`response.encoding`   |Encodage utilisé pour décoder `.text`      |
|`response.url`        |URL finale (après éventuelles redirections)|
|`response.history`    |Liste des redirections qui ont précédé     |
|`response.json()`     |Parse le corps comme JSON (si applicable)  |

Exemple :

```python
import requests

r = requests.get("https://httpbin.org/get", timeout=10)

print(f"Statut       : {r.status_code}")
print(f"URL finale   : {r.url}")
print(f"Encodage     : {r.encoding}")
print(f"Type contenu : {r.headers.get('Content-Type')}")
print(f"Taille       : {len(r.content)} octets")
```

### `text` vs `content`

- `response.text` → la réponse **décodée** en chaîne de caractères, prête à manipuler.
- `response.content` → la réponse **brute** en bytes, telle qu’elle est arrivée sur le câble.

Quand utiliser quoi ?

|Cas                                                   |À utiliser|
|------------------------------------------------------|----------|
|Parser du HTML/JSON pour exploitation immédiate       |`.text`   |
|Sauvegarder fidèlement la page pour retraitement futur|`.content`|
|Télécharger une image, un PDF, un fichier binaire     |`.content`|


> **Bonne pratique OSINT :** quand tu sauvegardes une page brute dans `data/raw/`, écris `.content` en mode binaire (`"wb"`). C’est la **preuve** de ce que tu as reçu, indépendante de l’encodage.

### Sauvegarder une page proprement

```python
import requests
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

url = "https://books.toscrape.com/"
headers = {"User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"}

r = requests.get(url, headers=headers, timeout=10)
r.raise_for_status()  # lève une exception si statut >= 400

# Construire un nom de fichier traçable
host = urlparse(url).netloc.replace(".", "_")
run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
chemin = Path("data/raw") / f"{run_id}_{host}.html"
chemin.parent.mkdir(parents=True, exist_ok=True)

chemin.write_bytes(r.content)
print(f"Sauvegardé : {chemin} ({len(r.content)} octets, statut {r.status_code})")
```

Quelques détails importants :

- **`headers={"User-Agent": ...}`** : on s’identifie honnêtement.
- **`r.raise_for_status()`** : transforme une réponse 4xx/5xx en exception. Pratique pour ne pas continuer à parser une page d’erreur.
- **`datetime.now(timezone.utc)`** : horodatage **explicitement en UTC**, sans ambiguïté de fuseau. C’est essentiel quand plusieurs personnes ou machines collaborent.
- **`run_id`** : c’est ton identifiant d’exécution. Il sera réutilisé pour nommer le HTML brut, le log, les données traitées et le rapport produit par cette même collecte. On y reviendra dans les parties suivantes — pour l’instant, retiens juste l’idée.
- **`Path.write_bytes()`** : écriture brute, sans transformation.

> **Nuance sur `raise_for_status()`** : pour un script pédagogique, c’est très bien — ça t’évite de parser une page d’erreur. Mais dans un outil d’enquête avancé, une réponse `403`, `404` ou `500` est elle-même une information utile (la page existait avant, la cible bloque, le serveur est en panne). On garde alors la réponse + métadonnées (statut, headers) dans les logs, même si on ne parse pas le contenu. On y reviendra au chapitre 12.

### Gérer les erreurs réseau

```python
import requests

try:
    r = requests.get("https://exemple-introuvable.invalid", timeout=5)
    r.raise_for_status()
except requests.exceptions.Timeout:
    print("Le serveur n’a pas répondu à temps.")
except requests.exceptions.ConnectionError:
    print("Impossible de se connecter au serveur.")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erreur générique : {e}")
```

|Exception         |Cause                                                             |
|------------------|------------------------------------------------------------------|
|`Timeout`         |Le serveur ne répond pas dans le délai imparti.                   |
|`ConnectionError` |DNS, réseau, refus de connexion.                                  |
|`HTTPError`       |Statut 4xx ou 5xx (uniquement si `raise_for_status()` est appelé).|
|`RequestException`|Classe parente — tout le reste.                                   |


> **À retenir :** capturer `RequestException` en dernier filet de sécurité est une bonne pratique. Mais distinguer les cas (Timeout vs Connection vs HTTPError) permet des réactions plus fines.

## Très utile en pratique

### Le User-Agent identifiable

Sans header explicite, `requests` envoie un User-Agent type `python-requests/2.31.0`. C’est honnête, mais peu informatif.

Pour un outil OSINT, identifie-toi proprement :

```python
HEADERS = {
    "User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "fr,en;q=0.8",
}

r = requests.get(url, headers=HEADERS, timeout=10)
```

> **Rappel :** **pas** d’usurpation de navigateur (Chrome récent, etc.) pour contourner des filtres anti-bot. C’est un signal d’intention douteuse et ça nuit à la traçabilité de ton enquête.

### Vérifier et corriger l’encodage

```python
r = requests.get(url, timeout=10)

print(r.encoding)            # ce que requests a deviné
print(r.headers.get("Content-Type"))
# Souvent : 'text/html; charset=utf-8'

# Si l’encodage est mal détecté :
r.encoding = "utf-8"         # forcer
print(r.text[:200])          # maintenant correct
```

Symptôme classique d’encodage cassé : tu vois `Caf\xc3\xa9` au lieu de `Café`, ou `Ã©` au lieu de `é`. C’est presque toujours un problème UTF-8 mal interprété.

### Pattern de fonction `fetch` réutilisable

Un mini-module à garder sous la main :

```python
# src/fetch.py
import logging
import requests
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse

USER_AGENT = "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
HEADERS = {"User-Agent": USER_AGENT, "Accept-Language": "fr,en;q=0.8"}

logger = logging.getLogger(__name__)


def fetch(url, session=None, raw_dir="data/raw", run_id=None, timeout=10):
    """Récupère une URL, sauvegarde le contenu brut, retourne (Response, chemin).

    - `session` : une `requests.Session` partagée (recommandé pour les collectes multi-pages).
      Si non fournie, une session jetable est créée pour cette requête.
    - `run_id` : identifiant d’exécution **partagé** entre toutes les requêtes d’une même
      collecte. Si non fourni, un nouveau `run_id` est calculé — à éviter pour les
      collectes multi-pages, où toutes les pages doivent partager le même `run_id`.

    Lève une exception en cas d’erreur HTTP ou réseau.
    """
    session = session or requests.Session()
    if run_id is None:
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    r = session.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()

    parsed = urlparse(url)
    host = parsed.netloc.replace(".", "_")
    path_safe = parsed.path.strip("/").replace("/", "_") or "index"
    out = Path(raw_dir) / f"{run_id}_{host}_{path_safe}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(r.content)

    logger.info("Fetched %s (%d bytes, status %d) -> %s",
                url, len(r.content), r.status_code, out)
    return r, out
```

Ce pattern (fetch + sauvegarde brute + retour structuré) est la **brique de base** de tous tes scrapers. Tu vas le réutiliser dans toute la partie II et III.

### Une seule requête, plusieurs analyses

Quand tu mets au point ton parser (chapitre 6), tu vas vouloir itérer **vite** sans retaper le serveur. La méthode :

1. Fais **une** requête, sauvegarde le HTML dans `data/raw/`.
1. Travaille sur le **fichier local** pour tester tous tes sélecteurs.
1. Relance une requête réelle uniquement quand tu veux des données fraîches.

C’est plus rapide pour toi, plus respectueux pour le serveur, et ça rend ton enquête reproductible.

## Bonus

### `requests.Session()` : préfiguration du chapitre 11

Si tu fais plusieurs requêtes vers le même site, une `Session` partage cookies et headers et réutilise la connexion sous-jacente :

```python
import requests

with requests.Session() as session:
    session.headers.update({"User-Agent": "MonOutil/0.1"})
    r1 = session.get("https://example.com/", timeout=10)
    r2 = session.get("https://example.com/about", timeout=10)
```

C’est plus efficace et c’est la bonne pratique dès qu’on dépasse une requête isolée. On y reviendra au chapitre 11 (bonnes pratiques pro).

### `verify=False` : à ne **pas** utiliser

Tu croiseras dans des tutos `requests.get(url, verify=False)` pour ignorer les erreurs de certificat SSL. **Ne fais jamais ça en production OSINT** : tu désactives un mécanisme de sécurité qui protège ta connexion contre les interceptions. Si un site a un vrai problème de certificat, c’est un signal qu’il faut interroger.

## ❌ Erreur classique

```python
# Oublier le timeout
r = requests.get(url)
# ❌ Si le serveur ne répond pas, ton script attend... indéfiniment.

r = requests.get(url, timeout=10)  # ✅

# Considérer un 200 comme un succès logique
r = requests.get(url, timeout=10)
if r.status_code == 200:
    parse(r.text)
# ❌ Certains sites renvoient 200 + page "ressource introuvable"
# → toujours vérifier aussi que le contenu correspond à ce qu’on attend.

# User-Agent qui se fait passer pour Chrome
HEADERS = {"User-Agent": "Mozilla/5.0 ... Chrome/120 ..."}
# ❌ Sauf cas pédagogique très balisé, c’est de l’usurpation.
# Le serveur peut légitimement traiter ton script comme un humain
# et tu pollues ses statistiques d’usage.

# Confondre .text et .content quand on sauvegarde
chemin.write_text(r.text)
# ❌ Tu sauvegardes une version déjà décodée. Si requests s’est trompé
# sur l’encodage, tu sauvegardes du texte cassé.

chemin.write_bytes(r.content)  # ✅ — préserve le brut

# Capturer Exception largement
try:
    r = requests.get(url, timeout=10)
except Exception:
    pass
# ❌ Tu masques tout, y compris les bugs de ton propre code.
# Capture les exceptions du module requests, pas tout.
```

## Exercices

**Guidé :**

1. Récupère la page d’accueil de `https://httpbin.org/`.
1. Affiche : statut, URL finale, encodage détecté, `Content-Type`, taille en octets, et 3 headers de réponse de ton choix.
1. Sauvegarde le contenu brut dans `data/raw/`.

**Autonome :** Écris un script `src/fetch_cli.py` qui :

1. Prend une URL en argument (`sys.argv[1]`).
1. Vérifie qu’elle commence par `http://` ou `https://`.
1. Fait la requête avec User-Agent identifiable et timeout.
1. Gère séparément `Timeout`, `ConnectionError`, `HTTPError`.
1. Sauvegarde le HTML dans `data/raw/<horodatage>_<host>.html`.
1. Affiche un résumé (statut, taille, durée de la requête, chemin du fichier).

Astuce : pour mesurer la durée, utilise `time.perf_counter()` autour de l’appel.

## ✅ Tu sais maintenant…

- Installer et utiliser `requests` pour faire une requête GET
- Lire l’objet `Response` (`status_code`, `text`, `content`, `headers`, etc.)
- Gérer les erreurs réseau avec `Timeout`, `ConnectionError`, `HTTPError`
- Imposer un timeout (toujours)
- Identifier honnêtement ton script via User-Agent
- Sauvegarder le contenu brut dans `data/raw/` de manière traçable
- Le réflexe : **fetch une fois, parse hors ligne**

-----

# Chapitre 6 — Parser du HTML avec BeautifulSoup

Tu as récupéré une page HTML. C’est une grosse soupe de balises. **BeautifulSoup** est la bibliothèque qui transforme cette soupe en arbre exploitable.

## Le minimum à savoir

### Installation rappel

```bash
pip install beautifulsoup4 lxml
```

`beautifulsoup4` est la bibliothèque, `lxml` est le parser rapide qu’elle peut utiliser en interne.

### Premier parsing

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Bonjour</h1>
    <p class="lead">Premier paragraphe.</p>
    <a href="https://exemple.fr">Lien</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")

print(soup.h1.get_text())            # "Bonjour"
print(soup.p.get_text())              # "Premier paragraphe."
print(soup.a.get("href"))             # "https://exemple.fr"
```

### Choix du parser

|Parser         |Caractéristiques                                    |Quand                                       |
|---------------|----------------------------------------------------|--------------------------------------------|
|`"html.parser"`|Intégré à Python, pas d’installation supplémentaire.|Petits scripts, dépannage.                  |
|`"lxml"`       |Rapide, robuste, supporte du XML.                   |Recommandé pour tout projet sérieux.        |
|`"html5lib"`   |Très tolérant aux erreurs HTML.                     |Sites au HTML « cassé » qui posent problème.|

Tous donnent le même objet `soup` derrière. On utilisera `"lxml"` par défaut.

### Charger depuis un fichier (ton flux de travail principal)

Souvenir du chapitre 5 : tu as sauvegardé une page dans `data/raw/`. Tu vas parser **ce fichier**, pas retaper le serveur.

```python
from bs4 import BeautifulSoup
from pathlib import Path

html_brut = Path("data/raw/20260517T140000Z_books_toscrape_com.html").read_bytes()
soup = BeautifulSoup(html_brut, "lxml")
```

Note : on passe `bytes`, BeautifulSoup gère l’encodage à partir des balises `<meta charset>` du HTML. C’est plus fiable que de décoder soi-même.

### Naviguer dans l’arbre : `find` et `find_all`

```python
# Trouver le premier élément qui correspond
title = soup.find("h1")
print(title.get_text())

# Trouver TOUS les éléments qui correspondent
liens = soup.find_all("a")
print(f"{len(liens)} liens trouvés")
for lien in liens:
    print(lien.get("href"), "—", lien.get_text(strip=True))
```

Filtrage par classe, id, attribut :

```python
soup.find("article", class_="post")          # ⚠ class_ avec underscore (class est réservé en Python)
soup.find(id="article-123")
soup.find("a", attrs={"data-type": "ext"})
soup.find_all("p", class_="lead")
```

### Naviguer avec les sélecteurs CSS : `select` et `select_one`

Souvent plus naturel quand on vient des DevTools, parce qu’on utilise la même syntaxe :

```python
soup.select_one("h1")                       # premier h1
soup.select("article p")                     # tous les p dans un article
soup.select(".post .lead")                   # paragraphes .lead dans un .post
soup.select_one("#article-123 > h1")         # h1 enfant direct
soup.select("a[href^='https']")              # liens commençant par https
```

**`find` vs `select` ?** Les deux marchent. Règles pratiques :

- `find/find_all` : plus pythonique, idéal pour des recherches simples par balise + classe + attribut.
- `select/select_one` : plus expressif, idéal quand le sélecteur est complexe ou quand tu l’as construit dans les DevTools.

Tu peux mélanger les deux dans le même script — choisis le plus lisible cas par cas.

### Extraire le texte

```python
tag = soup.select_one("h1")

print(tag.get_text())                # texte avec espaces internes potentiels
print(tag.get_text(strip=True))      # texte nettoyé (recommandé)
print(tag.text)                      # raccourci de .get_text()
```

`strip=True` enlève les espaces et retours à la ligne en début/fin. C’est presque toujours ce que tu veux.

### Extraire des attributs

```python
lien = soup.select_one("a")

# Méthode crochets : crash si l’attribut n’existe pas
href = lien["href"]                  # ❌ KeyError si pas de href

# Méthode .get() : retourne None si absent (plus sûr)
href = lien.get("href")              # ✅
href = lien.get("href", "")          # ✅ avec valeur par défaut
```

> **Bonne pratique :** utilise toujours `.get("attribut")` quand tu n’es pas absolument certain que l’attribut existe.

### Itérer proprement

```python
# Extraire texte et URL de tous les liens d’une page
for lien in soup.find_all("a"):
    texte = lien.get_text(strip=True)
    url = lien.get("href")
    if texte and url:                # filtre les liens vides
        print(f"{texte} -> {url}")
```

## Très utile en pratique

### La méthodologie : Inspect → Sélecteur → Test

Pour chaque champ que tu veux extraire :

```
1. Va sur la page dans ton navigateur.
2. Clic droit sur la donnée qui t’intéresse → Inspecter.
3. Note la balise, ses classes, sa hiérarchie.
4. Construis le sélecteur CSS le plus simple qui cible cette donnée
   sans en attraper d’autres.
5. Teste sur le HTML sauvegardé hors ligne.
6. Vérifie le résultat sur 3-4 items différents — pas juste le premier.
```

**Le test sur plusieurs items est crucial.** Un sélecteur qui marche sur le premier livre peut échouer sur le quatrième parce que la promo est sur une autre balise, ou parce que l’auteur manque.

### Choisir un sélecteur robuste

Tous les sélecteurs ne se valent pas dans le temps :

|Sélecteur               |Robustesse                                            |
|------------------------|------------------------------------------------------|
|`#article-main h1`      |🟢 Très robuste (id stable, hiérarchie sémantique)     |
|`article > h1`          |🟢 Robuste (structure HTML5 stable)                    |
|`.titre-principal`      |🟡 Dépend des conventions du site                      |
|`.css-x7f3k2`           |🔴 Très fragile (classe générée, change à chaque build)|
|`div > div > div > span`|🔴 Très fragile (dépend de la structure exacte)        |

**Réflexe pro :** quand plusieurs sélecteurs sont possibles, prends celui qui repose sur la **sémantique** (`article`, `header`, `nav`, `time`, `data-*`) plutôt que sur la mise en page.

### Workflow recommandé

```
┌─────────────────────────────────────────────────┐
│  src/fetch.py    →  télécharge + sauvegarde brut │
│                     dans data/raw/               │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  src/parse.py    →  lit data/raw/ et applique    │
│                     les sélecteurs                │
│                     ITÈRE ICI                     │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  Liste de dicts prête pour le stockage           │
│  (chapitre 8)                                    │
└─────────────────────────────────────────────────┘
```

Ce découpage te permet de modifier ton parser **autant de fois que nécessaire** sans toucher au serveur. C’est la différence entre un débutant qui spamme le site et un pro qui itère localement.

### Nettoyer le texte extrait

Le HTML contient souvent des artefacts invisibles :

- Espaces multiples : `Bonjour    le    monde`.
- Espaces insécables : `\xa0` (s’affichent comme un espace, mais ne match pas `" "`).
- Retours à la ligne au milieu d’un texte.

Helper pratique :

```python
import re

def clean(text):
    if text is None:
        return ""
    # Remplace les espaces insécables et autres par des espaces normaux
    text = text.replace("\xa0", " ")
    # Compacte les espaces multiples
    text = re.sub(r"\s+", " ", text)
    return text.strip()
```

À utiliser sur **tout** texte qui vient d’une page web.

## Bonus

### XPath (mention culturelle)

`lxml` (sans BeautifulSoup) permet d’utiliser **XPath**, un langage de sélection encore plus puissant que CSS pour des cas tordus :

```python
from lxml import html

tree = html.fromstring(r.content)
titres = tree.xpath("//article//h2/text()")
```

XPath excelle pour les sélections « relatives au texte » (« le `<td>` qui suit le `<td>` contenant ‘Total’ »). En pratique, les sélecteurs CSS de BeautifulSoup couvrent 95 % des cas. Garde XPath dans un coin de ta tête pour les 5 % restants.

### Récupérer les microdonnées : `<script type="application/ld+json">`

Beaucoup de sites (médias, e-commerce) intègrent des métadonnées structurées en JSON-LD pour le SEO. C’est **un cadeau** pour un scraper :

```python
import json

scripts = soup.find_all("script", type="application/ld+json")
for s in scripts:
    try:
        data = json.loads(s.string)
        print(data.get("@type"), "-", data.get("headline", data.get("name")))
    except json.JSONDecodeError:
        continue
```

Quand le JSON-LD existe, **utilise-le en priorité** : il est explicitement publié pour la consommation programmatique, c’est plus stable et plus propre que de parser le HTML rendu.

## ❌ Erreur classique

```python
# Cibler par classe générée dynamiquement
titres = soup.select(".css-x7f3k2")
# ❌ Marchera une semaine. Préfère .article > h1 ou article header h1.

# Accéder à un attribut absent avec les crochets
href = lien["href"]
# ❌ KeyError sur un lien qui n’a pas de href (ex. <a name="ancre">)
href = lien.get("href")  # ✅

# Parser le serveur en boucle pendant qu’on développe
for i in range(10):
    r = requests.get(url, ...)
    soup = BeautifulSoup(r.text, "lxml")
    test_selecteur(soup)
# ❌ Tu martèles le serveur sans raison.
# ✅ Sauvegarde une fois, itère sur le fichier local.

# Confondre la présence visuelle et la présence dans le HTML brut
# Tu vois la donnée à l’écran mais ton scraper ne la trouve pas.
# → C’est probablement chargé en JavaScript après le HTML initial.
# Vérifie : Ctrl+U dans le navigateur, cherche la donnée dans le source brut.

# Ne tester son sélecteur que sur le premier item
livres = soup.select(".product")[:1]  # ⚠ marche, mais tu n’as pas testé la robustesse
# ✅ Toujours boucler sur 3-5 items différents avant de considérer le scraper "fini".
```

## Exercices

**Guidé :** Sur le HTML de `https://quotes.toscrape.com` (sauvegardé localement) :

1. Charge le fichier dans `BeautifulSoup`.
1. Trouve toutes les citations affichées sur la page (ce sont les `<div class="quote">`).
1. Pour chaque citation, extrais et affiche le texte de la citation seul (sélecteur `.text`).

**Autonome :** Sur le même HTML :

1. Pour chaque citation, extrais aussi : l’auteur, et la liste des tags.
1. Affiche le tout sous forme propre : `« texte » — auteur (tags)`.
1. Vérifie que ton script trouve bien **10 citations** sur la page (c’est le nombre attendu).

## ✅ Tu sais maintenant…

- Charger une page HTML dans `BeautifulSoup` (avec parser `lxml`)
- Naviguer dans l’arbre avec `find` / `find_all` ou `select` / `select_one`
- Choisir un sélecteur **robuste** (sémantique > classe générée)
- Extraire texte avec `.get_text(strip=True)` et attributs avec `.get("attr")`
- Le workflow : fetch une fois → parser hors ligne → itérer librement
- Nettoyer le texte (espaces insécables, espaces multiples)
- Repérer et exploiter le JSON-LD quand il existe

-----

# Chapitre 7 — Extraction structurée d’une page

Récupérer du texte, c’est bien. Construire une **structure** exploitable, c’est mieux. Ce chapitre te fait passer du « j’ai sorti des trucs de la page » au « j’ai produit un dataset propre, traçable et prêt à stocker ».

## Le minimum à savoir

### Le modèle « un item = un dict »

L’unité de base d’une collecte structurée, c’est l’**enregistrement** : un dictionnaire qui regroupe tous les champs d’un item, plus les **métadonnées de collecte**.

```python
{
    "texte": "La vie, c'est ce qui t'arrive pendant que tu fais d’autres plans.",
    "auteur": "John Lennon",
    "tags": ["change", "deep-thoughts", "thinking", "world"],
    "source_url": "https://quotes.toscrape.com/page/1/",
    "collected_at": "2026-05-17T14:32:11Z",
    "tool": "mon-collecteur/0.1"
}
```

Quatre catégories de champs :

1. **Données du domaine** (`texte`, `auteur`, `tags`) — ce qui t’intéresse.
1. **Source** (`source_url`) — d’où vient la donnée.
1. **Temporalité** (`collected_at`) — quand tu l’as collectée.
1. **Outil** (`tool`) — avec quoi.

Les trois dernières sont **obligatoires**. Sans elles, ton enregistrement n’a aucune valeur d’enquête (rappel chapitre 2 : traçabilité).

### Le pattern de boucle d’extraction

```python
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from pathlib import Path

URL_SOURCE = "https://quotes.toscrape.com/"
TOOL = "mon-collecteur/0.1"

html = Path("data/raw/quotes_page1.html").read_bytes()
soup = BeautifulSoup(html, "lxml")

resultats = []
collected_at = datetime.now(timezone.utc).isoformat()

for bloc in soup.select(".quote"):
    enregistrement = {
        "texte": bloc.select_one(".text").get_text(strip=True),
        "auteur": bloc.select_one(".author").get_text(strip=True),
        "tags": [t.get_text(strip=True) for t in bloc.select(".tag")],
        "source_url": URL_SOURCE,
        "collected_at": collected_at,
        "tool": TOOL,
    }
    resultats.append(enregistrement)

print(f"{len(resultats)} citations extraites")
```

Trois principes que ce pattern illustre :

1. **Boucle par bloc parent** (`.quote`) — chaque bloc devient un enregistrement.
1. **Sélection relative au bloc** (`bloc.select_one(...)`) — pas de risque de mélanger les items.
1. **Ajout systématique des métadonnées** — à chaque itération.

### Gérer les champs manquants

Si un site est cohérent, tous les blocs ont tous les champs. Dans la vraie vie, c’est l’exception. Voici comment se protéger :

```python
def safe_text(elt, selecteur, default=""):
    """Renvoie le texte d’un sous-élément, ou default si absent."""
    cible = elt.select_one(selecteur)
    return cible.get_text(strip=True) if cible else default


def safe_attr(elt, selecteur, attr, default=""):
    """Renvoie un attribut d’un sous-élément, ou default si absent."""
    cible = elt.select_one(selecteur)
    return cible.get(attr, default) if cible else default
```

Et dans la boucle :

```python
for bloc in soup.select(".article"):
    enregistrement = {
        "titre": safe_text(bloc, "h2"),
        "date": safe_attr(bloc, "time", "datetime"),
        "auteur": safe_text(bloc, ".byline .author", default="(inconnu)"),
        "resume": safe_text(bloc, ".excerpt"),
        ...
    }
```

> **À retenir :** un parser robuste produit toujours une sortie. Il ne plante pas sur un champ manquant — il enregistre la valeur manquante (`""`, `None`, `"(inconnu)"`) pour qu’on puisse la repérer en aval.

### Extraire des liens (cas typique)

```python
from urllib.parse import urljoin

def extraire_liens(soup, url_de_base):
    """Liste tous les liens d’une page en URLs absolues."""
    liens = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith(("javascript:", "mailto:", "tel:", "#")):
            continue
        # Reconstruire l’URL absolue depuis une éventuelle URL relative
        url_complete = urljoin(url_de_base, href)
        liens.append({
            "texte": a.get_text(strip=True),
            "url": url_complete,
        })
    return liens
```

Trois points importants :

- **Filtrer les liens non navigables** (`javascript:`, `mailto:`, ancres `#`).
- **`urljoin`** convertit une URL relative (`/article/123`) en absolue à partir de l’URL de la page.
- **Garder le texte du lien** : c’est souvent une métadonnée précieuse.

### Extraire un tableau HTML

```python
def extraire_tableau(soup, selecteur="table"):
    """Extrait un tableau HTML en liste de dicts (premier <tr> = entêtes)."""
    table = soup.select_one(selecteur)
    if table is None:
        return []

    lignes = table.find_all("tr")
    if not lignes:
        return []

    entetes = [th.get_text(strip=True) for th in lignes[0].find_all(["th", "td"])]
    donnees = []
    for ligne in lignes[1:]:
        cellules = [td.get_text(strip=True) for td in ligne.find_all(["th", "td"])]
        if len(cellules) == len(entetes):
            donnees.append(dict(zip(entetes, cellules)))
    return donnees
```

Pour Wikipedia et autres sites riches en tableaux, ce pattern résout 90 % des besoins.

## Très utile en pratique

### Normaliser au moment de l’extraction

Plutôt que de stocker des données « sales » et nettoyer plus tard, profite de la boucle d’extraction pour nettoyer en passant. Quelques règles :

|Champ                          |Normalisation suggérée                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------------------|
|Texte libre                    |`strip()`, suppression des espaces insécables, espaces multiples compactés.                         |
|URL                            |Conversion en absolu (`urljoin`).                                                                   |
|Date affichée (« 12 mai 2026 »)|Conserver telle quelle dans un champ `date_affichee`. Tenter le parsing dans `date_iso` si possible.|
|Liste de tags                  |Trim chaque tag, ne pas inclure les vides.                                                          |
|Nombres affichés (`"1 234 €"`) |Conserver le brut **et** une version numérique séparée.                                             |


> **Bonne pratique :** quand la valeur n’est pas évidente à parser (date locale, nombre formaté), garde **les deux** versions : le brut tel qu’extrait, et la version normalisée. Si la normalisation se trompe, tu peux corriger sans recollecter.

### Le cas particulier de l’extraction d’emails

Extraire des emails depuis une page est techniquement trivial avec une regex :

```python
import re

emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", soup.get_text())
```

**Mais c’est précisément un cas où il faut s’imposer un cadre strict.** Tu peux légitimement vouloir extraire :

- des **contacts institutionnels** (`contact@`, `presse@`, `info@`) sur une page de mentions légales ou « nous joindre »,
- des **adresses de responsables identifiés** (auteur d’une publication scientifique, responsable de communication désigné publiquement).

Tu ne dois **pas** :

- moissonner massivement les emails d’un site pour constituer une liste de prospection,
- collecter des emails personnels qui ne sont pas explicitement publiés dans un cadre professionnel,
- agréger des emails de différentes sources pour profiler des personnes,
- vendre, partager ou exporter des listes d’emails collectés.

> **Rappel RGPD :** une adresse email est une donnée personnelle. Sa collecte automatisée tombe sous le RGPD dès qu’il s’agit d’une personne physique. Pour un usage défensif sérieux, limite-toi aux contacts professionnels explicitement publiés à des fins de contact, et applique la minimisation.

Si le cadre est solide, un helper raisonnable :

```python
import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def extraire_contacts_institutionnels(soup):
    """Extrait les emails qui ressemblent à des contacts institutionnels."""
    prefixes_inst = ("contact", "info", "presse", "press", "media",
                     "communication", "support", "rh", "hr")
    texte = soup.get_text(" ", strip=True)
    emails = set(EMAIL_RE.findall(texte))
    institutionnels = {e for e in emails
                       if e.split("@")[0].lower().startswith(prefixes_inst)}
    return sorted(institutionnels)
```

Note bien que cet helper **filtre** vers des préfixes manifestement institutionnels. Il ne ramasse pas tout.

### Toujours conserver l’URL source

Dans chaque enregistrement, le champ `source_url` permet à toi et à un tiers de :

- vérifier la donnée en l’ouvrant dans un navigateur,
- relancer une collecte sur cette page seule,
- savoir si une donnée vient de la home page, d’un article, d’une catégorie.

C’est **non négociable**.

### Quand le sélecteur change selon la position

Sur certaines pages, le premier item a une structure légèrement différente des autres (parce qu’il est mis en avant). Deux approches :

```python
# Option 1 : filtrer le premier item (souvent en plus dans la liste générale)
items = soup.select(".article")[1:]  # ignore le mis-en-avant

# Option 2 : extraire séparément
mis_en_avant = soup.select_one(".featured-article")
items = soup.select(".article-list .article")
```

À choisir selon ce que tu veux conserver dans ton dataset.

## Bonus

### Les microdonnées JSON-LD, encore (mais en pratique)

Si un site fournit du JSON-LD, ton extraction devient quasi triviale :

```python
import json

ld_scripts = soup.find_all("script", type="application/ld+json")

articles = []
for script in ld_scripts:
    try:
        data = json.loads(script.string)
    except (json.JSONDecodeError, TypeError):
        continue

    # JSON-LD peut être un objet, une liste, ou un @graph
    items = data if isinstance(data, list) else [data]
    for item in items:
        if item.get("@type") in ("NewsArticle", "Article", "BlogPosting"):
            articles.append({
                "titre": item.get("headline"),
                "auteur": (item.get("author") or {}).get("name"),
                "date_publication": item.get("datePublished"),
                "url": item.get("url") or item.get("mainEntityOfPage"),
            })
```

Quand c’est disponible, c’est **le** bon chemin. Vérifie systématiquement avant d’aller scraper le HTML rendu.

### `<time datetime="...">` pour les dates machines

Les bons sites utilisent la balise `<time>` avec un attribut `datetime` au format ISO 8601 :

```html
<time datetime="2026-05-17T10:00:00Z">17 mai 2026</time>
```

Tu peux extraire :

- la version humaine : `time.get_text(strip=True)` → `"17 mai 2026"`
- la version machine : `time.get("datetime")` → `"2026-05-17T10:00:00Z"`

Toujours préférer la version machine pour le stockage et le tri.

## ❌ Erreur classique

```python
# Boucle qui plante sur le 4e item
for bloc in soup.select(".article"):
    enr = {
        "auteur": bloc.select_one(".author").get_text(strip=True),
        # ❌ Si l’item 4 n’a pas .author, AttributeError sur None
    }
# ✅ Utiliser safe_text() ou tester explicitement
for bloc in soup.select(".article"):
    auteur_elt = bloc.select_one(".author")
    enr = {
        "auteur": auteur_elt.get_text(strip=True) if auteur_elt else "",
    }

# Oublier de convertir les URLs relatives
for a in soup.find_all("a"):
    liens.append(a.get("href"))
    # ❌ Tu obtiens "/article/123" — inutilisable hors contexte.
# ✅ Reconstruire en absolu :
for a in soup.find_all("a"):
    href = a.get("href")
    if href:
        liens.append(urljoin(url_source, href))

# Confondre date affichée et date machine
date = bloc.select_one("time").get_text(strip=True)  # "il y a 3 jours"
# ❌ Impossible à comparer, à trier.
# ✅ Utiliser l’attribut datetime :
date = bloc.select_one("time").get("datetime")  # "2026-05-14T10:00:00Z"

# Oublier les métadonnées de collecte
enregistrement = {"titre": "...", "auteur": "..."}
# ❌ Pas de source_url, pas de collected_at, pas de tool
#    → l’enregistrement n’est pas traçable, donc inexploitable
#    pour une enquête sérieuse.

# Stocker les caractères "sales" tels quels
enr["texte"] = bloc.get_text()  # Contient des \xa0, retours à la ligne en boucle
# ✅ Passer par clean(...) avant de stocker.
```

## Exercices

**Guidé :** Sur le HTML de `https://books.toscrape.com/` (sauvegardé) :

1. Identifie le bloc parent qui correspond à un livre (regarde dans les DevTools).
1. Écris une boucle d’extraction qui produit une liste de dicts avec : `titre`, `prix`, `disponibilite`, `note_etoiles` (en nombre, 1-5), `source_url`, `collected_at`, `tool`.
1. Affiche les 5 premiers enregistrements.
1. Vérifie qu’il y a bien 20 livres sur la première page.

**Autonome :** Sur une page Wikipedia choisie qui contient au moins un tableau :

1. Identifie le tableau qui t’intéresse (par sa légende ou son titre proche).
1. Extrais-le en liste de dicts avec la fonction `extraire_tableau()` du chapitre.
1. Nettoie les cellules : suppression des références `[1]`, `[2]`, espaces insécables, espaces multiples.
1. Affiche le résultat sous forme de tableau lisible.
1. Joins à chaque ligne les métadonnées `source_url` et `collected_at`.

## 🧩 Mini-projet de Partie II — *Collecteur de citations*

**Objectif :** construire ton premier vrai script d’extraction structurée, de bout en bout.

**Cible :** `https://quotes.toscrape.com/` (site **fait** pour l’apprentissage, sans cadre légal limitant).

**Cahier des charges :**

1. **Configuration** dans `config/config.json` :
- `url_source` : l’URL de la page.
- `user_agent` : ton User-Agent identifiable.
- `output_dir` : dossier de sortie (par défaut `data/raw/`).
1. **Fetch** (`src/fetch.py`) :
- Récupère la page.
- Sauvegarde le HTML brut dans `data/raw/<horodatage>_quotes.html`.
- Gère les erreurs réseau.
1. **Parse** (`src/parse.py`) :
- Charge le HTML sauvegardé.
- Pour chaque citation, produit un dict avec : `texte`, `auteur`, `tags`, `source_url`, `collected_at`, `tool`.
- Utilise les helpers `safe_text()` et `clean()`.
1. **Orchestration** (`src/main.py`) :
- Lit la config.
- Appelle fetch puis parse.
- Affiche un résumé : nombre de citations extraites, premier et dernier auteur, durée totale.
1. **Fiche d’enquête** : remplis ta fiche `config/fiche-enquete.md` pour ce projet (oui, même pour un site bac à sable — l’habitude se prend là).

Note : on ne stocke pas encore le résultat en CSV/JSON — c’est le chapitre 8.

> **Rappel `.gitignore` :** si tu versionnes ce projet sur Git, **ne versionne pas** `data/raw/` ni `data/processed/`. Garde uniquement le code (`src/`), la **configuration d’exemple** (sans secrets), et la documentation (`README.md`, fiche d’enquête vierge). Les collectes sont reproductibles à partir du code ; pas besoin de les pousser, et ça peut contenir des informations qu’on ne veut pas exposer publiquement.

## ✅ Tu sais maintenant…

- Construire un enregistrement complet (données + source + horodatage + outil)
- Boucler par bloc parent pour produire une liste structurée
- Gérer les champs manquants avec `safe_text()` / `safe_attr()`
- Extraire et normaliser des liens en URLs absolues
- Extraire un tableau HTML en liste de dicts
- Encadrer strictement l’extraction d’emails (contacts institutionnels uniquement)
- Exploiter le JSON-LD et les balises `<time>` quand ils existent
- Le réflexe : **toujours** conserver `source_url`, `collected_at`, `tool`

-----

> **🎯 Tu as terminé la Partie II.**
> 
> Tu sais maintenant récupérer une page, la parser, et en sortir un dataset structuré en mémoire. Mais en mémoire, ça ne suffit pas — il faut le stocker, le nettoyer, le dédupliquer pour qu’il soit exploitable.
> 
> La Partie III s’occupe de ça : CSV / JSON / JSONL, organisation des dossiers, normalisation, déduplication.

-----

# PARTIE III — STRUCTURER ET NETTOYER LES DONNÉES

> **Objectif de la partie :** transformer une collecte brute en un dataset propre, dédupliqué, daté, prêt à être analysé ou versionné. Tu vas apprendre à stocker tes résultats dans les bons formats, à organiser ton dossier de sortie, à nettoyer le texte et à dédupliquer.
> 
> À la fin de cette partie, tu auras un pipeline `raw → processed → exploitable`.

-----

# Chapitre 8 — Stocker les résultats (CSV, JSON, JSONL)

Tu as construit une liste de dicts en Partie II. Elle vit en mémoire et disparaît à la fin du script. Il est temps de la **persister** correctement.

## Le minimum à savoir

### La règle d’or : `raw` est intouchable

Rappel du chapitre 0 :

```
data/
├── raw/        ← HTML brut horodaté, JAMAIS modifié
└── processed/  ← données extraites, nettoyées, exploitables
```

`data/raw/` contient **les preuves**. Tu n’y touches jamais. Si tu casses ton parsing, tu peux toujours rejouer depuis `raw/` sans relancer la moindre requête.

Tous les formats de sortie de ce chapitre (CSV, JSON, JSONL) vivent dans `data/processed/`.

### Choisir entre CSV, JSON et JSONL

|Format                |Cas idéal                                                                       |Avantages                                                                                 |Limites                                                    |
|----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------|
|**CSV**               |Données tabulaires, mêmes champs partout (citations, livres, lignes de tableau).|Ouvert dans n’importe quel tableur. Léger. Universel.                                     |Ne supporte pas les structures imbriquées (listes, objets).|
|**JSON**              |Données hétérogènes ou imbriquées (un objet riche par enquête).                 |Fidèle aux structures Python. Lisible humainement.                                        |Doit être chargé en entier ; pas pratique pour l’append.   |
|**JSONL** (JSON Lines)|Collectes longues, append-friendly, streaming.                                  |Une ligne = un objet. Lecture/écriture incrémentale. Excellent pour les grosses collectes.|Pas un standard universel pour les tableurs.               |


> **Règle pratique :**
> 
> - Quelques centaines d’items homogènes destinés à un tableur → **CSV**.
> - Données structurées avec listes ou imbrications → **JSON**.
> - Collecte par flux, append au fil de l’eau, gros volumes → **JSONL**.

### Écrire en CSV avec `csv.DictWriter`

```python
import csv
from pathlib import Path

resultats = [
    {"texte": "...", "auteur": "Einstein", "source_url": "...", "collected_at": "..."},
    {"texte": "...", "auteur": "Wilde",    "source_url": "...", "collected_at": "..."},
]

chemin = Path("data/processed/quotes.csv")
chemin.parent.mkdir(parents=True, exist_ok=True)

# Champs explicites : tu décides de l’ordre des colonnes
champs = ["texte", "auteur", "source_url", "collected_at"]

with chemin.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=champs)
    writer.writeheader()
    writer.writerows(resultats)

print(f"{len(resultats)} lignes écrites dans {chemin}")
```

Trois points cruciaux :

- **`encoding="utf-8"`** : pour les accents et caractères non-ASCII.
- **`newline=""`** : sur Windows, sans ça, tu obtiens des doubles sauts de ligne.
- **`fieldnames`** : tu maîtrises l’ordre des colonnes. Indispensable pour des fichiers comparables d’une exécution à l’autre.

### Quand un champ est une liste (cas des tags)

CSV n’aime pas les listes. Deux options :

```python
# Option 1 : joindre avec un séparateur
enregistrement["tags"] = "|".join(enregistrement["tags"])

# Option 2 : exporter en JSON plutôt
```

Le séparateur `|` est plus sûr que `,` ou `;` (rares dans les tags). Au moment de relire :

```python
tags = ligne["tags"].split("|") if ligne["tags"] else []
```

### Écrire en JSON

```python
import json
from pathlib import Path

chemin = Path("data/processed/quotes.json")
chemin.parent.mkdir(parents=True, exist_ok=True)

with chemin.open("w", encoding="utf-8") as f:
    json.dump(resultats, f, indent=2, ensure_ascii=False)

print(f"{len(resultats)} enregistrements écrits dans {chemin}")
```

Deux arguments qui changent tout :

- **`indent=2`** : indentation lisible. Sans ça, tout est sur une ligne.
- **`ensure_ascii=False`** : conserve les caractères Unicode (`é`, `中`, `→`) au lieu de les échapper en `\u00e9`. Plus lisible et plus léger.

### Écrire en JSONL (un objet par ligne)

```python
import json
from pathlib import Path

chemin = Path("data/processed/quotes.jsonl")
chemin.parent.mkdir(parents=True, exist_ok=True)

with chemin.open("w", encoding="utf-8") as f:
    for item in resultats:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
```

Pour relire :

```python
with chemin.open("r", encoding="utf-8") as f:
    for ligne in f:
        item = json.loads(ligne)
        # traiter item
```

JSONL brille pour les **collectes incrémentales** : tu peux ouvrir le fichier en mode `"a"` (append) et ajouter des enregistrements au fil de l’eau, sans tout recharger en mémoire.

### Convention de nommage des fichiers

Un nom de fichier propre est un nom **traçable** :

```
<run_id>_<source>_<sujet>.<format>

Exemples :
20260517T140000Z_quotes_toscrape_collection.csv
20260517T143012Z_books_toscrape_inventory.json
20260517T150000Z_legifrance_decret_2026-401.json
```

Composantes :

- **`run_id`** (horodatage UTC ISO compact) : identifie une exécution unique.
- **`source`** : nom court de la cible.
- **`sujet`** : ce qu’on a collecté.

> **À retenir :** ton `run_id` est partagé entre le HTML brut (`data/raw/`), les données traitées (`data/processed/`), le log (`logs/`) et le rapport (`reports/`). C’est ce qui permet de **tout retrouver** d’une exécution donnée en une recherche.

### Les métadonnées au niveau du dataset

Au-delà des métadonnées **par enregistrement** (`source_url`, `collected_at`, `tool`), un dataset complet doit aussi porter ses propres métadonnées **globales**. Format recommandé en JSON :

```python
sortie = {
    "metadata": {
        "tool": "mon-collecteur",
        "tool_version": "0.1.0",
        "run_id": "20260517T140000Z",
        "collected_at": "2026-05-17T14:00:00Z",
        "source_url": "https://quotes.toscrape.com/",
        "count": len(resultats),
    },
    "data": resultats,
}

with chemin.open("w", encoding="utf-8") as f:
    json.dump(sortie, f, indent=2, ensure_ascii=False)
```

C’est ce qu’un analyste qui reçoit ton fichier veut voir en premier : « ça vient d’où, c’est de quand, combien il y en a ».

## Très utile en pratique

### Déduplication par clé naturelle

À chaque collecte, tu risques d’avoir des doublons (même citation sur deux pages, même article dans deux flux). On déduplique avec une **clé naturelle** stable :

```python
def dedupliquer(items, cle):
    """Garde le premier exemplaire de chaque clé."""
    vus = set()
    uniques = []
    for item in items:
        valeur = item.get(cle)
        if valeur and valeur not in vus:
            vus.add(valeur)
            uniques.append(item)
    return uniques


# Exemple : dédupliquer des articles par URL
articles_uniques = dedupliquer(articles, "source_url")
print(f"{len(articles)} → {len(articles_uniques)} après déduplication")
```

> **Choix de la clé** : utilise quelque chose de **stable** et **unique**. `source_url` canonisée est souvent le meilleur choix **quand chaque item correspond à une page distincte** (un article = une URL). Si plusieurs items viennent d’une même page (citations, livres, lignes de tableau), utilise plutôt un `item_id` construit par hash sur les champs métier (voir juste après).

### Hash d’un enregistrement pour déduplication fine

Quand aucun champ unique n’existe :

```python
import hashlib
import json

def hash_enregistrement(item, champs):
    """Hash SHA-256 de la concaténation de certains champs."""
    base = json.dumps([item.get(c, "") for c in champs], ensure_ascii=False)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


# Exemple :
for item in resultats:
    item["item_id"] = hash_enregistrement(item, ["texte", "auteur"])
```

Le `item_id` est désormais stable : si tu re-collectes la même citation demain, elle aura le même hash. Idéal pour la détection de doublons et la comparaison entre collectes (chapitre 13).

### Organisation des dossiers : récap

```
data/
├── raw/
│   ├── 20260517T140000Z_quotes_toscrape.html
│   ├── 20260517T143012Z_books_toscrape.html
│   └── ...
├── processed/
│   ├── 20260517T140000Z_quotes_toscrape_collection.json
│   └── ...
└── reports/  (vient au chapitre 14)
```

Une exécution = un `run_id` = un fichier par étape, tous reliés.

### Lire un CSV existant

```python
import csv
from pathlib import Path

with Path("data/processed/quotes.csv").open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    enregistrements = list(reader)

print(f"{len(enregistrements)} lignes lues")
```

`DictReader` te donne directement des dicts avec les en-têtes comme clés. C’est presque toujours ce que tu veux.

## Bonus

### SQLite en mention

Quand JSON/CSV deviennent insuffisants (gros volumes, requêtes croisées, jointures), Python intègre **SQLite** sans installation supplémentaire :

```python
import sqlite3

con = sqlite3.connect("data/processed/collecte.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS quotes (texte TEXT, auteur TEXT, url TEXT)")
cur.executemany("INSERT INTO quotes VALUES (?, ?, ?)",
                [(q["texte"], q["auteur"], q["source_url"]) for q in resultats])
con.commit()
con.close()
```

C’est hors-scope pour ce cours, mais à connaître pour quand tes datasets grandissent.

### Une fonction d’écriture qui choisit le bon format

```python
import csv
import json
from pathlib import Path

def write(items, chemin, format="auto"):
    """Écrit items dans chemin. Format auto-détecté par extension."""
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)

    if format == "auto":
        format = chemin.suffix.lstrip(".").lower()

    if format == "csv":
        champs = list(items[0].keys()) if items else []
        with chemin.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=champs)
            writer.writeheader()
            writer.writerows(items)
    elif format == "json":
        with chemin.open("w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
    elif format == "jsonl":
        with chemin.open("w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
    else:
        raise ValueError(f"Format inconnu : {format}")
```

À glisser dans `src/store.py` de ton projet.

## ❌ Erreur classique

```python
# Oublier encoding="utf-8" sur Windows
with open("sortie.csv", "w") as f:
    csv.writer(f).writerows(...)
# ❌ Caractères accentués cassés, BOM parasites
# ✅ Toujours encoding="utf-8" en lecture et écriture

# Oublier newline="" pour CSV
with open("sortie.csv", "w", encoding="utf-8") as f:
    ...
# ❌ Sur Windows : double saut de ligne entre chaque ligne
# ✅ newline="" obligatoire pour CSV

# Écraser une collecte précédente
with open("data/processed/quotes.json", "w") as f:
    json.dump(...)
# ❌ La collecte d’hier est perdue.
# ✅ Toujours préfixer avec un run_id horodaté.

# Stocker une liste Python dans une cellule CSV
ligne = {"tags": ["a", "b", "c"]}
csv.DictWriter(...).writerow(ligne)
# ❌ Tu obtiens "['a', 'b', 'c']" littéralement — pas exploitable
# ✅ Joindre avec un séparateur : "|".join(tags)
# ✅ Ou stocker en JSON plutôt qu’en CSV

# Polluer le dossier courant
json.dump(items, open("sortie.json", "w"))
# ❌ Le fichier atterrit n’importe où, écrase peut-être autre chose
# ✅ Toujours dans data/processed/, avec mkdir(parents=True, exist_ok=True)
```

## Exercices

**Guidé :** Reprends le mini-projet « collecteur de citations » du chapitre 7 et ajoute :

1. Une fonction `write_csv(items, chemin)` qui écrit les citations dans `data/processed/<run_id>_quotes.csv`. Sérialise les tags avec `|`.
1. Une fonction `write_json(items, chemin, source_url)` qui écrit un fichier `data/processed/<run_id>_quotes.json` au format `{metadata: {...}, data: [...]}`.
1. Une exécution qui produit les deux fichiers en parallèle.

**Autonome :** Écris un script `src/append_jsonl.py` qui :

1. Prend un fichier JSONL en argument (créé s’il n’existe pas).
1. Demande à l’utilisateur de saisir une note (`titre`, `contenu`) en boucle.
1. Ajoute chaque note au JSONL en mode append, avec `id` (hash) et `created_at` (UTC ISO).
1. S’arrête sur saisie vide.

À la fin, ouvre le fichier et vérifie que chaque ligne est un JSON valide indépendant.

## ✅ Tu sais maintenant…

- Choisir entre CSV, JSON et JSONL selon le cas
- Écrire en CSV (avec `encoding`, `newline`, `fieldnames` explicites)
- Écrire en JSON (`indent`, `ensure_ascii=False`)
- Écrire en JSONL pour les collectes append-friendly
- Ajouter des métadonnées globales `{metadata: {...}, data: [...]}`
- Dédupliquer par clé naturelle ou par hash
- Nommer tes fichiers avec un `run_id` partagé entre raw / processed / logs / reports
- Organiser proprement `data/raw/` et `data/processed/`

-----

# Chapitre 9 — Nettoyer, normaliser, enrichir

Tu as collecté, tu as stocké. Maintenant tu vas transformer ces données brutes en dataset **propre et exploitable**. Un dataset propre, c’est celui qu’on peut trier, filtrer, comparer dans le temps, et croiser avec d’autres sources sans surprise.

## Le minimum à savoir

### Le pipeline `raw → processed`

Le principe :

```
data/raw/        →    src/clean.py    →    data/processed/
(intouchable)         (transformation)     (exploitable)
```

`clean.py` lit un fichier brut, applique des transformations, et écrit un nouveau fichier. À aucun moment on ne modifie le brut. Si la transformation se trompe, on relance `clean.py` ; pas besoin de retoucher au serveur.

### Nettoyer le texte

On reprend le helper du chapitre 6, en le complétant :

```python
import re
import unicodedata

def clean_text(text):
    """Nettoie un texte extrait du web."""
    if text is None:
        return ""
    # Normalisation Unicode (caractères composés -> forme stable)
    text = unicodedata.normalize("NFKC", text)
    # Espaces insécables et autres → espace normal
    text = text.replace("\xa0", " ").replace("\u200b", "")
    # Compacte les espaces multiples et trim
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

|Opération      |Pourquoi                                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
|`NFKC`         |Convertit les variantes Unicode (`é` en deux caractères vs un seul) en forme canonique. Indispensable pour comparer et dédupliquer.|
|`\xa0` → espace|L’espace insécable s’affiche comme un espace mais ne match pas `" "` — source de bugs invisibles.                                  |
|`\u200b`       |Zero-Width Space, parfois inséré par des CMS et invisible à l’œil nu.                                                              |
|`\s+` → `" "`  |Compacte tabulations, retours à la ligne, espaces multiples.                                                                       |

À appliquer à **tout** champ texte qui vient du web.

### Normaliser les URLs

Une URL peut s’écrire de plusieurs façons qui pointent vers la même ressource. Pour dédupliquer correctement, il faut la **canoniser**.

```python
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode, urljoin

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_cid", "mc_eid", "ref", "ref_src", "_ga",
}

def canonical_url(url):
    """Renvoie une version canonique d’une URL (sans tracking, normalisée)."""
    p = urlparse(url)

    # Schéma et hôte en minuscules
    scheme = p.scheme.lower()
    host = p.netloc.lower()

    # Retirer le port par défaut
    if (scheme == "http" and host.endswith(":80")) or \
       (scheme == "https" and host.endswith(":443")):
        host = host.rsplit(":", 1)[0]

    # Path : enlever le slash final sauf pour la racine
    path = p.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")

    # Query : retirer les paramètres de tracking, trier le reste
    params = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
              if k.lower() not in TRACKING_PARAMS]
    params.sort()
    query = urlencode(params)

    # Pas de fragment (#) — il n’a pas de sens côté serveur
    return urlunparse((scheme, host, path, "", query, ""))
```

Exemple :

```python
print(canonical_url("https://Exemple.fr/Article/?utm_source=newsletter&id=42"))
# → https://exemple.fr/Article?id=42

print(canonical_url("https://exemple.fr/article"))
print(canonical_url("https://exemple.fr/article/"))
# → https://exemple.fr/article  (les deux)
```

Maintenant, deux URLs « équivalentes » se ressemblent vraiment. La déduplication devient fiable.

### Construire une URL absolue à partir d’une relative

Rappel chapitre 7 : `urljoin` reconstruit l’URL complète à partir de l’URL de la page et d’une URL relative trouvée dans un `href`.

```python
from urllib.parse import urljoin

page = "https://exemple.fr/section/index.html"

print(urljoin(page, "article-1.html"))   # https://exemple.fr/section/article-1.html
print(urljoin(page, "/contact"))          # https://exemple.fr/contact
print(urljoin(page, "https://autre.fr")) # https://autre.fr  (URL déjà absolue conservée)
```

### Extraire le domaine

Pour comparer ou regrouper par site :

```python
from urllib.parse import urlparse

def domain_of(url):
    return urlparse(url).netloc.lower()

print(domain_of("https://www.exemple.fr/article"))
# → www.exemple.fr
```

Mais attention : `www.exemple.fr` et `exemple.fr` sont techniquement deux hôtes différents. Pour traiter `news.bbc.co.uk` correctement (extraire `bbc.co.uk` comme domaine racine), il faut `tldextract` :

```bash
pip install tldextract
```

```python
import tldextract

t = tldextract.extract("https://news.bbc.co.uk/article")
print(t.domain)         # bbc
print(t.suffix)         # co.uk
print(t.registered_domain)  # bbc.co.uk
```

`tldextract` connaît la liste à jour des suffixes publics et fait le travail proprement. À ajouter à `requirements.txt` quand tu travailles avec des URLs variées.

### Trier et filtrer une liste de dicts

```python
articles = [
    {"titre": "C", "date": "2026-05-15"},
    {"titre": "A", "date": "2026-05-12"},
    {"titre": "B", "date": "2026-05-14"},
]

# Trier par date
articles.sort(key=lambda a: a["date"])

# Trier par date décroissante
articles.sort(key=lambda a: a["date"], reverse=True)

# Filtrer
recents = [a for a in articles if a["date"] >= "2026-05-13"]
```

`sorted(iterable, key=..., reverse=...)` crée une nouvelle liste si tu ne veux pas modifier l’originale.

### Déduplication, encore (avec URL canonisée)

```python
def dedupliquer_par_url(items):
    """Déduplique en utilisant l’URL canonique.

    À utiliser UNIQUEMENT quand chaque item correspond à une page distincte
    (ex. liste d’articles dont chaque titre pointe vers sa propre URL).
    Pour plusieurs items issus de la même page (citations, livres, lignes
    de tableau...), source_url est partagée — utiliser `dedupliquer(items, "item_id")`
    avec un hash construit sur les champs métier.
    """
    vus = set()
    uniques = []
    for item in items:
        url = canonical_url(item.get("source_url", ""))
        if url and url not in vus:
            vus.add(url)
            uniques.append(item)
    return uniques
```

C’est l’association `clean_text` + `canonical_url` + `dedupliquer` qui transforme un dataset brut en dataset exploitable.

### Enrichir un enregistrement

L’enrichissement, c’est ajouter de la valeur sans recollecter. Quelques enrichissements courants :

```python
def enrichir(item):
    """Enrichit un enregistrement avec des champs dérivés."""
    url = item.get("source_url", "")
    item["domain"] = domain_of(url)
    item["url_canonical"] = canonical_url(url)
    if "texte" in item:
        item["text_length"] = len(item["texte"])
        item["word_count"] = len(item["texte"].split())
    return item
```

Ce ne sont pas de **nouvelles** données — ce sont des **vues** sur les données existantes, calculées pour faciliter l’analyse en aval.

## Très utile en pratique

### Le helper `safe_parse_date`

Les dates affichées sur le web sont infiniment variées (« 17 mai 2026 », « il y a 3 jours », « 2026-05-17T10:00:00Z », « 05/17/26 »). Une stratégie défensive :

```python
from datetime import datetime

def safe_parse_date(value):
    """Tente de parser une date ISO. Retourne None sinon."""
    if not value:
        return None
    # ISO 8601 (le cas idéal — depuis <time datetime="...">)
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None
```

> **Bonne pratique :** garde **toujours** la version brute (`date_affichee`) **en plus** de la version parsée (`date_iso`). Si le parsing se trompe, tu peux corriger sans recollecter.

### Validation simple

Quelques regex utiles pour valider — sans tomber dans l’over-engineering :

```python
import re

URL_RE = re.compile(r"^https?://[\w.-]+(?:/[\w./?=&%-]*)?$", re.I)
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_url(s):
    return bool(URL_RE.match(s)) if s else False

def is_valid_email(s):
    return bool(EMAIL_RE.match(s)) if s else False
```

À utiliser pour signaler les enregistrements suspects, **pas** pour rejeter silencieusement (mieux vaut un dataset honnête avec un champ `valid_url: False` qu’un dataset amputé).

### Le pattern de pipeline

```python
# src/clean.py
from pathlib import Path
import json

def clean_pipeline(items, source_url):
    """Pipeline complet : nettoyage + normalisation + enrichissement + déduplication.

    Adapté à des items multiples extraits d’une même page (citations, livres,
    lignes de tableau). On déduplique sur un `item_id` calculé à partir des
    champs métier, pas sur `source_url` (qui serait partagée par tous les items).
    """
    out = []
    for it in items:
        cleaned = {
            "texte": clean_text(it.get("texte")),
            "auteur": clean_text(it.get("auteur")),
            "tags": [clean_text(t) for t in it.get("tags", []) if t.strip()],
            "source_url": canonical_url(it.get("source_url", source_url)),
            "collected_at": it.get("collected_at"),
            "tool": it.get("tool"),
        }
        cleaned = enrichir(cleaned)
        # Identifiant stable construit sur les champs métier
        cleaned["item_id"] = hash_enregistrement(cleaned, ["texte", "auteur"])
        out.append(cleaned)

    out = dedupliquer(out, "item_id")
    out.sort(key=lambda x: x.get("collected_at", ""), reverse=True)
    return out
```

> **Choisir la bonne clé de déduplication :**
> 
> |Type de dataset                                                            |Clé recommandée                   |
> |---------------------------------------------------------------------------|----------------------------------|
> |Liste d’articles (1 article = 1 URL)                                       |`source_url` canonisée            |
> |Citations, livres, lignes de tableau (plusieurs items par page)            |`item_id` = hash sur champs métier|
> |Profils avec identifiant naturel (n° SIRET, ISBN, identifiant scientifique)|Champ ID natif                    |
> 
> En cas de doute, **construis un `item_id` par hash**. C’est l’option la plus défensive.

Ce module reçoit un dataset brut et produit un dataset propre, dans `data/processed/`. C’est la dernière étape avant l’analyse.

### Détection de langue (en bonus)

Pour des sources internationales, savoir dans quelle langue est un texte est précieux :

```bash
pip install langdetect
```

```python
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0   # reproductibilité

def detect_lang(text):
    try:
        return detect(text[:500]) if text else None
    except Exception:
        return None
```

> **Limites :** `langdetect` se trompe sur les textes courts (< 30 mots), les textes mixtes, et certaines langues proches (catalan vs espagnol). À utiliser comme **indication**, pas comme vérité absolue.

## Bonus

### Mise en cache HTTP pour le développement

Pendant que tu mets au point ton script de nettoyage, tu ne veux pas non plus retélécharger le HTML. Une `requests.Session()` + `requests-cache` font ça pour toi :

```bash
pip install requests-cache
```

```python
import requests_cache

session = requests_cache.CachedSession("cache_dev", expire_after=3600)
r = session.get(url, timeout=10)   # première fois : requête réelle
r = session.get(url, timeout=10)   # ensuite : récupéré depuis le cache local
```

À utiliser **uniquement en développement**. En production, on veut des données fraîches et un cache explicite.

## ❌ Erreur classique

```python
# Comparer des URLs sans normaliser
"https://exemple.fr/page" == "https://Exemple.fr/page/"
# → False, mais c’est la même ressource.
# ✅ Toujours canonical_url() avant comparaison.

# Considérer "" et None comme équivalents
if item["auteur"] == "":
    item["auteur"] = "(inconnu)"
# ❌ Casse si auteur vaut None
# ✅ if not item.get("auteur"): ...

# Modifier la liste qu’on parcourt
for item in items:
    if not item["texte"]:
        items.remove(item)
# ❌ Comportement imprévisible
# ✅ items = [i for i in items if i["texte"]]

# Croire que les espaces insécables sont des espaces
"Bonjour\xa0monde".split(" ")  # ❌ ["Bonjour\xa0monde"] (un seul élément)
# ✅ Toujours clean_text() avant traitement

# Sur-nettoyer et perdre l’information brute
item["texte"] = clean_text(item["texte"]).lower().replace("'", "")
# ❌ Tu écrases la donnée originale. Plus moyen de revenir en arrière.
# ✅ Garder l’original ET ajouter une version normalisée si nécessaire :
item["texte_normalized"] = clean_text(item["texte"]).lower()
```

## Exercices

**Guidé :**

1. Reprends le fichier JSON produit au chapitre 8 à partir du mini-projet « Collecteur de citations ».
1. Écris `src/clean.py` qui :
- lit le fichier brut depuis `data/processed/`,
- applique `clean_text` sur chaque champ texte,
- applique `canonical_url` sur les URLs,
- construit un `item_id` par hash sur les champs métier (`texte`, `auteur`),
- déduplique les enregistrements par `item_id`,
- écrit le résultat dans `data/processed/<run_id>_quotes_clean.json`.
1. Compare le nombre d’enregistrements avant/après.

**Autonome :** Écris un script `src/url_inventory.py` qui :

1. Prend en argument un fichier JSON contenant une liste d’URLs (collectées précédemment).
1. Pour chaque URL : canonise, extrait le domaine racine avec `tldextract`, et regroupe.
1. Produit un fichier `data/processed/<run_id>_domains.csv` listant chaque domaine avec le nombre d’URLs associées, trié par fréquence décroissante.

## 🧩 Mini-projet de Partie III — *Extracteur de tableaux Wikipedia*

**Objectif :** combiner toutes les briques des parties II et III sur un cas réel.

**Cible :** une page Wikipedia de ton choix contenant **au moins un tableau de données structurées** (liste de pays, classement, comparaison technique, etc.).

**Contraintes pédagogiques :**

- Respecter le `robots.txt` de Wikipedia.
- Identifier honnêtement ton User-Agent.
- Ne pas dépasser quelques requêtes.
- Wikipedia propose une API officielle (MediaWiki) — pour cet exercice, on scrape **délibérément** le HTML pour s’entraîner. Pour une enquête réelle, on utiliserait l’API.

**Cahier des charges :**

1. **Fiche d’enquête** (`config/fiche-enquete-wiki.md`) remplie avant de coder.
1. **`src/fetch.py`** : récupère la page Wikipedia, sauvegarde le HTML brut dans `data/raw/`.
1. **`src/parse.py`** :
- charge le HTML sauvegardé,
- identifie le tableau pertinent (par sa légende, son `id`, ou son rang dans la page),
- extrait les lignes en liste de dicts,
- applique `clean_text` sur chaque cellule,
- retire les références de type `[1]`, `[note]`.
1. **`src/clean.py`** :
- canonise les URLs trouvées dans les cellules,
- construit un `item_id` par hash sur les champs métier de chaque ligne (par exemple `nom_du_pays` + `année`, ou `produit` + `version`),
- déduplique les lignes par `item_id`,
- enrichit chaque ligne avec `source_url`, `collected_at`, `tool`, `run_id`.
1. **`src/store.py`** : écrit à la fois en CSV (en sérialisant les champs de type liste avec `|` si nécessaire) **et** en JSON avec métadonnées globales.
1. **`src/main.py`** : orchestre, affiche un résumé.

**Livrable :** une exécution complète qui produit :

```
data/raw/<run_id>_wikipedia_<sujet>.html
data/processed/<run_id>_wikipedia_<sujet>.csv
data/processed/<run_id>_wikipedia_<sujet>.json
```

…tous trois reliés par le même `run_id`.

> **Rappel** : `data/raw/` et `data/processed/` restent hors de Git.

## ✅ Tu sais maintenant…

- Nettoyer un texte web (Unicode, espaces insécables, espaces multiples)
- Canoniser une URL (schéma, hôte, slash final, tracking)
- Reconstruire des URLs absolues avec `urljoin`
- Extraire le domaine racine avec `tldextract`
- Trier et filtrer des listes de dicts
- Dédupliquer par URL canonique ou par hash
- Enrichir un enregistrement (champs dérivés)
- Le pipeline `raw → clean → enrich → dedup → processed`

-----

> **🎯 Tu as terminé la Partie III.**
> 
> Tu sais maintenant produire un dataset propre, complet, traçable et dédupliqué à partir d’une seule page. Mais une enquête sérieuse ne s’arrête presque jamais à **une** page : il faut souvent parcourir des dizaines, voire des centaines de pages, ou interroger une API.
> 
> La Partie IV s’attaque à ce passage à l’échelle : pagination, APIs, bonnes pratiques professionnelles (rate limiting, retries, logs, configuration).

-----

# PARTIE IV — PASSER À L’ÉCHELLE

> **Objectif de la partie :** sortir d’une page unique. Plusieurs pages, plusieurs requêtes, des APIs, une architecture qui tient. Cette partie introduit les outils qui distinguent un script jetable d’un outil OSINT durable : rate limiting, retries, logs, configuration externe, sessions.
> 
> **Garde en tête :** monter à l’échelle, c’est aussi multiplier l’impact sur les serveurs cibles. Tout ce qu’on apprend ici doit être appliqué **avec retenue volontaire**, jamais pour pousser à fond.

-----

# Chapitre 10 — Pagination et collecte multi-pages

Tu sais collecter une page. Maintenant : comment passer à 5, 50, 500 pages, **sans devenir une nuisance** et **sans casser à la première erreur**.

## Le minimum à savoir

### Les principaux schémas de pagination

Avant d’écrire la moindre boucle, identifie **comment** le site pagine. Quatre patterns courants :

|Schéma                    |Exemple d’URL              |Comment savoir ?                                            |
|--------------------------|---------------------------|------------------------------------------------------------|
|**Query string `?page=N`**|`/articles?page=2`         |Aller à la page 2 et observer l’URL.                        |
|**Path `/page/N/`**       |`/articles/page/2/`        |Idem. Très courant sur WordPress.                           |
|**Offset / limit**        |`/items?offset=20&limit=10`|Souvent les APIs et les sites avec pas d’items configurable.|
|**Next link**             |`<a rel="next" href="...">`|Lien explicite « page suivante » dans le HTML.              |

Cas particulier : **infinite scroll** (chargement automatique au défilement). Sous le capot, c’est presque toujours une API JSON appelée par la page → voir le chapitre 11. **Ne pas essayer de scraper le HTML rendu** pour ce cas.

### Boucle de collecte avec arrêt explicite

La règle d’or : **deux conditions d’arrêt**, jamais une seule.

```python
import time
from pathlib import Path

BASE_URL = "https://quotes.toscrape.com/page/{page}/"
MAX_PAGES = 20           # plafond dur — sécurité anti-boucle infinie
DELAY = 1.0              # secondes entre deux requêtes

resultats = []
for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page)
    print(f"[{page}/{MAX_PAGES}] {url}")

    r, _ = fetch(url)   # fetch défini au chapitre 5
    items = parse(r.content, source_url=url)

    if not items:
        print("Plus de résultats, arrêt.")
        break

    resultats.extend(items)
    time.sleep(DELAY)

print(f"Total collecté : {len(resultats)} items sur {page} pages")
```

Quatre éléments cruciaux :

1. **`MAX_PAGES`** : plafond inconditionnel. Même si le site renvoie indéfiniment des pages, ton script s’arrête.
1. **Arrêt si liste vide** : signal naturel de fin de pagination.
1. **`time.sleep(DELAY)`** : pause entre deux requêtes.
1. **Log de progression** : indispensable pour suivre, debug, et abandonner si besoin (Ctrl+C).

### Jitter : ne pas être trop régulier

Une cadence parfaitement fixe (« exactement 1 requête par seconde, pendant 1 heure ») produit des pics réguliers qui pèsent inutilement sur le serveur. Un peu d’aléa dans le délai lisse la charge, réduit ces pics, et rend la collecte plus respectueuse :

```python
import time
import random

def polite_sleep(base=1.0, jitter=0.5):
    """Dort base + un peu d’aléa, pour éviter une cadence parfaitement régulière."""
    time.sleep(base + random.uniform(0, jitter))
```

`polite_sleep(1.0, 0.5)` dort entre 1.0 et 1.5 seconde. C’est suffisant pour le confort des deux côtés.

> **À retenir :** le jitter est une **politesse réseau**, pas un mécanisme de contournement anti-bot. On ne cherche pas à « ressembler à un humain » pour passer sous les radars : on cherche à étaler la charge sur le serveur. Si le site bloque ou impose une limite explicite, on ralentit ou on arrête — on ne ruse pas. Et si `robots.txt` annonce `Crawl-delay: 5`, on met `DELAY = 5` et on arrête de discuter.

### Pagination par « next link »

C’est le pattern le plus propre : tu suis le lien explicite plutôt que de deviner.

```python
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def next_page(soup, current_url):
    """Cherche un lien rel=next ou un sélecteur explicite."""
    # Méthode 1 : la balise <link rel="next">
    link = soup.find("link", rel="next")
    if link and link.get("href"):
        return urljoin(current_url, link["href"])
    # Méthode 2 : un <a rel="next">
    a = soup.find("a", rel="next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    # Méthode 3 : sélecteur dédié sur la page (à adapter selon le site)
    a = soup.select_one(".next a") or soup.select_one("a.next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    return None
```

Et la boucle devient :

```python
url = BASE_URL
pages_visitees = 0
while url and pages_visitees < MAX_PAGES:
    r, _ = fetch(url)
    soup = BeautifulSoup(r.content, "lxml")
    items = parse(soup, source_url=url)
    resultats.extend(items)
    pages_visitees += 1
    url = next_page(soup, url)
    polite_sleep()
```

C’est plus robuste qu’une boucle basée sur `page=N`, parce que **tu n’inventes pas d’URLs** — tu suis ce que le site te donne.

### Plafond de volume

Au-delà des pages, un plafond sur le **nombre d’items** est une bonne ceinture de sécurité :

```python
MAX_PAGES = 50
MAX_ITEMS = 1000

for page in range(1, MAX_PAGES + 1):
    ...
    if len(resultats) >= MAX_ITEMS:
        print(f"Plafond {MAX_ITEMS} items atteint, arrêt.")
        break
```

## Très utile en pratique

### Tracer chaque page : le journal de collecte

Pour rendre la collecte **reproductible**, journalise chaque page :

```python
import csv
from datetime import datetime, timezone

journal = []  # ou ouvrir un CSV en append

for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page)
    started = datetime.now(timezone.utc).isoformat()
    try:
        r, fichier_brut = fetch(url)
        journal.append({
            "page": page,
            "url": url,
            "status": r.status_code,
            "bytes": len(r.content),
            "raw_file": str(fichier_brut),
            "started_at": started,
            "error": "",
        })
    except Exception as e:
        journal.append({
            "page": page,
            "url": url,
            "status": "",
            "bytes": 0,
            "raw_file": "",
            "started_at": started,
            "error": str(e),
        })
        # on continue les autres pages
    polite_sleep()
```

Puis on écrit `journal` dans `logs/<run_id>_pagination.csv`. C’est précieux quand quelque chose s’est mal passé : tu sais exactement quelles pages ont réussi, lesquelles ont échoué, et tu peux reprendre.

### Continuer ou arrêter sur erreur ?

Trois stratégies, à choisir selon le contexte :

|Stratégie                                                             |Pour quoi                                                   |
|----------------------------------------------------------------------|------------------------------------------------------------|
|**Strict** : on s’arrête à la première erreur réseau                  |Petites collectes critiques où on veut tout ou rien.        |
|**Tolérant** : on logge l’erreur et on continue                       |Grandes collectes où une page perdue est acceptable.        |
|**Retry + tolérant** : on retente N fois, puis on logge et on continue|Le bon compromis pour la plupart des cas (voir chapitre 12).|


> **Bonne pratique OSINT** : tolérance par défaut, **mais** chaque page perdue est **explicitement loguée** dans le journal de collecte. Pas de perte silencieuse.

### Détecter la fin de pagination proprement

Quelques signaux fiables de fin :

- Le sélecteur d’items ne renvoie rien sur la page.
- L’URL `next` est absente.
- Le serveur renvoie un 404 sur la page suivante.

**Signaux à ignorer** (ils peuvent être trompeurs) :

- Un 500 isolé : peut être temporaire — on retente.
- Une page avec moins d’items qu’habituellement : peut être la dernière page incomplète, pas une erreur.

### Le squelette réutilisable

```python
# src/paginate.py
import time, random, logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def polite_sleep(base=1.0, jitter=0.5):
    time.sleep(base + random.uniform(0, jitter))


def next_page(soup, current_url):
    """Cherche un lien rel=next ou un sélecteur explicite vers la page suivante."""
    link = soup.find("link", rel="next")
    if link and link.get("href"):
        return urljoin(current_url, link["href"])
    a = soup.find("a", rel="next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    a = soup.select_one(".next a") or soup.select_one("a.next")
    if a and a.get("href"):
        return urljoin(current_url, a["href"])
    return None


def collect_paginated(start_url, fetch, parse, max_pages=50,
                      max_items=1000, delay=1.0):
    """Collecte paginée par suivi de next link.

    fetch(url) -> (response, raw_file_path)
    parse(soup, source_url) -> list[dict]
    """
    url = start_url
    pages = 0
    items_total = []
    journal = []

    while url and pages < max_pages and len(items_total) < max_items:
        pages += 1
        try:
            r, raw = fetch(url)
            soup = BeautifulSoup(r.content, "lxml")
            items = parse(soup, source_url=url)
            items_total.extend(items)
            journal.append({"url": url, "status": r.status_code,
                            "items": len(items), "raw_file": str(raw)})
            url = next_page(soup, url)
        except Exception as e:
            logger.warning("Erreur sur %s : %s", url, e)
            journal.append({"url": url, "status": "error",
                            "items": 0, "error": str(e)})
            break
        polite_sleep(delay)

    return items_total, journal
```

À glisser dans ton projet `src/paginate.py`. C’est la brique que tu vas réutiliser dès qu’une collecte dépasse une seule page.

## Bonus

### Checkpoint et reprise

Pour les grosses collectes, sauvegarder après chaque page permet de reprendre sans tout refaire :

```python
import json
from pathlib import Path

checkpoint = Path("data/processed/checkpoint.json")

# Si un checkpoint existe : reprendre depuis là
if checkpoint.exists():
    state = json.loads(checkpoint.read_text(encoding="utf-8"))
    url = state["next_url"]
    items_total = state["items"]
else:
    url = START_URL
    items_total = []

while url:
    ...
    # Après chaque page, sauvegarder l’état
    checkpoint.write_text(json.dumps({
        "next_url": url,
        "items": items_total,
    }, ensure_ascii=False), encoding="utf-8")
```

À la fin, supprime le checkpoint. C’est une logique simple, utile dès que la collecte dépasse quelques minutes.

### Pagination par cursor (avancé)

Certaines APIs paginent par **cursor** : la réponse contient un jeton qu’on renvoie pour la suivante. C’est plus stable que `page=N` quand les données changent en cours de collecte. On y reviendra au chapitre 11.

## ❌ Erreur classique

```python
# Pas de plafond
page = 1
while True:
    fetch(f"/page/{page}")
    page += 1
# ❌ Si le site renvoie indéfiniment (page 9999, 10000…), ton script
# ne s’arrête jamais. Plafond DUR obligatoire.

# Pas de pause
for page in range(1, 100):
    fetch(...)
    parse(...)
# ❌ 100 requêtes en quelques secondes = comportement abusif.
# Au minimum time.sleep(1) entre chaque.

# Confondre fin de pagination et erreur réseau
if r.status_code != 200:
    break
# ❌ Un 503 transitoire peut faire croire à la fin de la pagination.
# ✅ Distinguer les statuts : 404 → fin probable, 5xx → retry.

# Inventer des URLs au lieu de suivre les liens
for page in range(1, 100):
    fetch(f"/page/{page}")
# ❌ Si le site a moins de 100 pages, tu fais des requêtes inutiles
# (et tu charges des pages 404 répétées).
# ✅ Détecte la fin via la liste vide ou via next link.

# Tout perdre sur une exception
try:
    for page in range(...):
        ...
except Exception:
    pass
# ❌ Tu perds tous les items collectés avant l’erreur.
# ✅ Try/except à l’intérieur de la boucle, par page.
```

## Exercices

**Guidé :** Sur `https://quotes.toscrape.com/page/{N}/` :

1. Récupère les 5 premières pages avec une pause de 1 seconde entre chaque.
1. Concatène toutes les citations en une seule liste.
1. Affiche le total et le nombre d’auteurs distincts.
1. Sauvegarde un journal `logs/<run_id>_pagination.csv` avec une ligne par page (page, URL, statut, nombre d’items).

**Autonome :** Sur `https://books.toscrape.com/` :

1. Identifie le schéma de pagination utilisé (regarde le lien « next »).
1. Parcours **toute** la pagination en suivant les `next link`.
1. Plafond : 50 pages, 1500 items.
1. Pour chaque livre : titre, prix, disponibilité, note (1-5), URL canonique.
1. Sauvegarde en JSON Lines dans `data/processed/<run_id>_books.jsonl`.
1. Log structuré dans `logs/<run_id>_pagination.csv`.

## ✅ Tu sais maintenant…

- Reconnaître les schémas de pagination (query, path, offset, next link)
- Écrire une boucle de collecte avec **deux** conditions d’arrêt (plafond + fin détectée)
- Espacer les requêtes avec `time.sleep` + jitter
- Suivre un `next link` plutôt qu’inventer des URLs
- Tracer chaque page dans un journal de collecte
- Distinguer fin de pagination, erreur transitoire, et erreur définitive
- Le squelette réutilisable `collect_paginated()`

-----

# Chapitre 11 — Utiliser des APIs publiques

C’est le chapitre où tu apprends à exploiter des APIs proprement. Et c’est aussi le chapitre où tu vas comprendre **pourquoi l’API est presque toujours préférable au scraping** quand elle existe.

## Le minimum à savoir

### Pourquoi préférer une API

|Critère       |Scraping HTML                                   |API                                                  |
|--------------|------------------------------------------------|-----------------------------------------------------|
|Stabilité     |🔴 Le site peut changer son HTML demain.         |🟢 Les APIs ont des versions et un cycle de vie clair.|
|Cadre légal   |🟡 CGU générales, parfois floues sur le scraping.|🟢 CGU spécifiques de l’API, claires.                 |
|Données       |🟡 Telles qu’affichées (parfois moins riches).   |🟢 Souvent plus riches que ce qui est affiché.        |
|Charge serveur|🔴 Plus lourde (HTML, CSS, JS).                  |🟢 Strict minimum (JSON).                             |
|Identification|🟡 Anonyme par défaut.                           |🟢 Via clé API : tu sais qui tu es, le serveur aussi. |


> **Quand l’API existe et couvre ton besoin, tu l’utilises. Point.** Le scraping ne devient pertinent que si l’API n’existe pas ou ne couvre pas ton cas d’usage.

### Une requête API en pratique

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "current": "temperature_2m,relative_humidity_2m",
}
headers = {"User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"}

r = requests.get(url, params=params, headers=headers, timeout=10)
r.raise_for_status()

data = r.json()
print(data["current"])
```

Trois nouveautés par rapport au scraping HTML :

1. **`params={...}`** : `requests` construit l’URL complète (`?latitude=48.85&...`) pour toi. Plus lisible et plus sûr (échappement automatique).
1. **`r.json()`** : parse la réponse JSON en dict/list Python. Pas de BeautifulSoup à l’horizon.
1. **`User-Agent`** : recommandé même pour les APIs publiques. Plusieurs APIs gratuites le **demandent** explicitement.

### Le JSON, en deux minutes

JSON (JavaScript Object Notation) est un format de données structurées que toute API REST utilise. Quatre types :

|Type JSON                                       |Équivalent Python                             |
|------------------------------------------------|----------------------------------------------|
|`{"clé": "valeur"}`                             |`dict`                                        |
|`["a", "b", "c"]`                               |`list`                                        |
|`"texte"`, `42`, `3.14`, `true`, `false`, `null`|`str`, `int`, `float`, `True`, `False`, `None`|

Une réponse typique :

```json
{
  "current": {
    "temperature_2m": 21.4,
    "relative_humidity_2m": 65
  },
  "elevation": 35.0,
  "timezone": "Europe/Paris"
}
```

Côté Python :

```python
data = r.json()
print(data["current"]["temperature_2m"])  # 21.4
```

### Gérer les erreurs spécifiques aux APIs

```python
try:
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentification refusée (clé API manquante ou invalide).")
    elif e.response.status_code == 403:
        print("Accès interdit (droits insuffisants).")
    elif e.response.status_code == 429:
        print("Rate limit atteint, ralentir.")
    else:
        print(f"Erreur HTTP : {e.response.status_code}")
except ValueError:
    print("La réponse n’est pas du JSON valide.")
except requests.exceptions.RequestException as e:
    print(f"Erreur réseau : {e}")
```

Les codes typiques d’une API :

|Code |Sens API                                 |
|-----|-----------------------------------------|
|`200`|Succès.                                  |
|`201`|Création réussie (pour les POST).        |
|`204`|Succès sans contenu.                     |
|`400`|Requête malformée (paramètres invalides).|
|`401`|Authentification requise/invalide.       |
|`403`|Authentifié mais pas autorisé.           |
|`404`|Ressource inexistante.                   |
|`429`|**Rate limit dépassé**.                  |
|`5xx`|Erreur côté serveur — à retenter.        |

### Authentification : la clé API

Beaucoup d’APIs te demandent une **clé** pour t’identifier. Deux modes :

```python
# Mode 1 : clé en paramètre de query
r = requests.get(url, params={"key": API_KEY, "q": "Paris"})

# Mode 2 : header Authorization (plus courant)
headers = {"Authorization": f"Bearer {API_TOKEN}"}
r = requests.get(url, headers=headers)
```

### Stocker une clé API en sécurité

**Jamais en dur dans le code.** Trois bonnes pratiques :

1. **Variable d’environnement** :

```python
import os
API_KEY = os.getenv("MON_API_KEY")
if not API_KEY:
    raise RuntimeError("Définis la variable d’environnement MON_API_KEY")
```

Tu définis la variable hors de ton code :

```bash
export MON_API_KEY="abc123..."     # Linux/Mac
$env:MON_API_KEY = "abc123..."     # PowerShell
```

1. **Fichier `.env`** (non versionné, dans `.gitignore`) lu par `python-dotenv` :

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # charge .env
API_KEY = os.getenv("MON_API_KEY")
```

1. **Gestionnaire de secrets** (avancé) : Keychain, KeePass, Vault…

> **Risque réel :** une clé API commitée sur GitHub est trouvée et exploitée par des bots en moins d’une heure. Tu peux te retrouver avec une facture, un compte bloqué, ou pire — un mauvais usage attribué à toi. **Jamais en dur, jamais commitée.**

### Rate limits côté API

Les APIs sérieuses te disent leurs limites dans les headers de réponse :

```python
print(r.headers.get("X-RateLimit-Limit"))      # par ex. "60"
print(r.headers.get("X-RateLimit-Remaining"))  # par ex. "12"
print(r.headers.get("X-RateLimit-Reset"))      # timestamp avant remise à zéro
```

Et quand tu dépasses : `429 Too Many Requests`, souvent avec un header `Retry-After: 30` (secondes à attendre).

```python
if r.status_code == 429:
    retry_after = int(r.headers.get("Retry-After", 60))
    print(f"Rate limit atteint, attente de {retry_after} s...")
    time.sleep(retry_after)
```

> **À retenir :** **respecte** les rate limits. Un compte qui ignore les limites finit bloqué, et il finit **bien** par être bloqué. Ralentir volontairement est plus rentable que se faire bannir.

### Pagination d’API

Trois patterns courants :

```python
# 1. page / per_page
r = requests.get(url, params={"page": 2, "per_page": 100})

# 2. offset / limit
r = requests.get(url, params={"offset": 200, "limit": 100})

# 3. cursor (jeton renvoyé par la réponse précédente)
cursor = None
while True:
    params = {"limit": 100}
    if cursor:
        params["cursor"] = cursor
    r = requests.get(url, params=params, timeout=10)
    data = r.json()
    items.extend(data["results"])
    cursor = data.get("next_cursor")
    if not cursor:
        break
```

Le pattern « cursor » est le plus robuste pour les APIs qui changent en cours de collecte (ajouts, suppressions). Lis toujours la doc de l’API avant.

## Très utile en pratique

### Le pattern complet pour une API publique

```python
# src/api_client.py
import os
import time
import logging
import requests
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url, api_key=None, user_agent=None, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if user_agent:
            self.session.headers["User-Agent"] = user_agent
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"

    def get(self, path, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        for attempt in range(3):
            r = self.session.get(url, params=params, timeout=self.timeout)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 30))
                logger.warning("Rate limit, attente %ds (essai %d/3)", wait, attempt + 1)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError("Trop de rate limits successifs")
```

Cet objet `ApiClient` encapsule : `User-Agent`, clé API, session HTTP, retries sur 429, timeout. C’est ton point d’entrée pour toute API.

> **Note :** ce client gère explicitement le `429` (rate limit). Les erreurs `5xx` transitoires (502, 503, 504) ne sont pas retentées ici — elles le seront proprement avec `Retry` + backoff exponentiel au chapitre 12. Pour l’instant, elles remontent en exception et l’appelant décide.

### Exemple complet sans clé : Open-Meteo

```python
client = ApiClient(
    "https://api.open-meteo.com",
    user_agent="MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
)

data = client.get("/v1/forecast", params={
    "latitude": 48.85,
    "longitude": 2.35,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Paris",
})

print(data["daily"])
```

Cette API ne demande pas de clé et fournit des données météo riches. Idéale pour s’entraîner.

### Exemple avec clé : pattern défensif

Un exemple générique (le nom de l’API n’a pas d’importance, le pattern est le même) :

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CTI_API_KEY")
if not API_KEY:
    raise RuntimeError("Définis CTI_API_KEY dans ton .env")

client = ApiClient(
    base_url="https://api.exemple-cti.example/v1",
    api_key=API_KEY,
    user_agent="MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
)

# Exemple d’interrogation
indicators = client.get("/indicators/recent", params={"limit": 50})
```

Avant d’interroger une API CTI avec une vraie clé, **lis ses CGU** : usage défensif, données autorisées, rate limits, conditions de partage des résultats. Une API qui t’autorise à interroger ne t’autorise pas toujours à republier.

### APIs sans clé utiles pour s’entraîner

|API                          |Sans clé ?|Cas d’usage                                 |
|-----------------------------|----------|--------------------------------------------|
|**Open-Meteo**               |✅         |Météo, climat.                              |
|**REST Countries**           |✅         |Données pays (frontières, devises, langues).|
|**Hacker News API**          |✅         |Actualité tech.                             |
|**MediaWiki / Wikipedia API**|✅         |Articles, métadonnées, modifications.       |
|**JSONPlaceholder**          |✅         |Bac à sable pour apprendre.                 |
|**Datagouv.fr API**          |✅         |Open data administratif français.           |

Pour les APIs avec clé orientées CTI/OSINT, va voir : VirusTotal (clé gratuite avec rate limit serré), urlscan.io, AbuseIPDB, OTX AlienVault, Shodan (clé payante). **Toutes** demandent de respecter strictement leurs CGU.

## Bonus

### Sauvegarder la réponse brute

Comme pour le HTML : sauvegarde toujours la réponse JSON brute dans `data/raw/` avant de la transformer.

```python
import json
from pathlib import Path
from datetime import datetime, timezone

def save_api_response(data, source, run_id, raw_dir="data/raw"):
    """Sauvegarde une réponse JSON brute avec métadonnées."""
    out = Path(raw_dir) / f"{run_id}_{source}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    wrapped = {
        "metadata": {
            "source": source,
            "run_id": run_id,
            "collected_at": datetime.now(timezone.utc).isoformat(),
        },
        "data": data,
    }
    out.write_text(json.dumps(wrapped, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    return out
```

Ça garantit la **reproductibilité** : tu peux refaire ton analyse plus tard sans réinterroger l’API.

### Identifier les endpoints d’API d’un site

Souvenir du chapitre 3 : si une page charge ses données en JavaScript, le navigateur appelle un endpoint JSON publiquement observable. Tu peux souvent passer du scraping HTML à un usage d’API « non documentée ». Précautions :

- **Vérifie les CGU** : l’absence de doc ne signifie pas l’absence de cadre.
- **Ne contourne aucune authentification** : si l’endpoint exige un token de session, c’est qu’il n’est pas destiné à l’usage automatisé.
- **Respecte la même politesse** que pour une API documentée : rate limit, User-Agent.

Si tu n’es pas certain du cadre, **demande**. Beaucoup de sites répondent positivement à un mail « j’ai vu votre endpoint X, puis-je l’interroger à hauteur de Y requêtes/heure pour Z ? ».

## ❌ Erreur classique

```python
# Clé API en dur dans le code
API_KEY = "sk_live_abc123..."   # ❌ commit accidentel = clé compromise
# ✅ os.getenv("API_KEY") + .env dans .gitignore

# Ignorer le 429
r = requests.get(url, params=...)
if r.status_code == 200:
    process(r.json())
# ❌ Tous les 429 sont ignorés silencieusement → données manquantes
# ✅ Gérer explicitement le 429 avec Retry-After

# Confondre params et data
r = requests.get(url, data={"q": "Paris"})
# ❌ data= envoie un corps en POST. Pour GET avec query, c’est params=.
r = requests.get(url, params={"q": "Paris"})   # ✅

# Oublier r.raise_for_status() puis appeler r.json()
r = requests.get(url, timeout=10)
data = r.json()
# ❌ Si la réponse est une page d’erreur HTML, r.json() lève ValueError
# ✅ raise_for_status() d’abord, json() ensuite

# Marteler une API gratuite
for i in range(10000):
    requests.get(url, params={...})
# ❌ Ban quasi garanti, perte de la ressource pour tous les autres
# ✅ Respecter les rate limits annoncés + plafond local
```

## Exercices

**Guidé :**

1. Choisis l’API Open-Meteo.
1. Pour une liste de 5 villes (lat/lon), récupère la température actuelle.
1. Sauvegarde chaque réponse brute dans `data/raw/<run_id>_openmeteo_<ville>.json`.
1. Produit un fichier `data/processed/<run_id>_meteo.csv` avec colonnes : `ville`, `latitude`, `longitude`, `temperature`, `collected_at`.
1. Respecte une pause de 1 seconde entre chaque ville.

**Autonome :**

1. Choisis une API publique sans clé qui t’intéresse (REST Countries, MediaWiki, etc.).
1. Identifie un endpoint et un paramètre intéressants.
1. Écris `src/api_explore.py` qui : prend un argument en CLI, interroge l’API, sauvegarde la réponse brute, et affiche un résumé.
1. Gère explicitement les erreurs 404 et 429.
1. Documente dans un mini-README : URL de l’API, endpoint utilisé, rate limit annoncé, lien vers les CGU.

## 🧩 Mini-projet de Partie IV (1/2) — *Inventaire DNS d’une liste de domaines*

**Objectif :** combiner des sources publiques d’infrastructure (principalement DNS, éventuellement RDAP) et un peu de Python pour produire un inventaire minimal d’une liste de domaines fournis en entrée. Cas d’usage défensif typique : avoir une vue d’ensemble des serveurs d’un périmètre qu’on connaît.

**Cible :** **uniquement** des domaines que tu administres, ou des domaines publics manifestement de test (`example.com`, `iana.org`).

**Outils :**

- `dnspython` (`pip install dnspython`) pour les résolutions DNS classiques (A, AAAA, MX, NS, TXT) — c’est plus propre qu’une API tierce pour ces données.
- Optionnellement, une API publique RDAP pour récupérer les infos d’enregistrement quand elles sont disponibles (`https://rdap.org/`).

**Cahier des charges :**

1. **Entrée** : `config/domaines.txt` (un domaine par ligne).
1. **Pour chaque domaine** :
- résolution A, AAAA, MX, NS, TXT,
- éventuellement appel RDAP (gestion d’erreur si non disponible),
- délai de 1 s entre deux domaines.
1. **Sortie** :
- `data/processed/<run_id>_dns_inventory.json` avec une entrée structurée par domaine,
- `logs/<run_id>_dns.log` avec progression et erreurs.
1. **Fiche d’enquête** remplie en amont.
1. **Aucune** tentative de zone transfer ou de fuzzing — c’est de la résolution publique normale.

## ✅ Tu sais maintenant…

- Distinguer scraping et exploitation d’API (et préférer l’API quand elle existe)
- Faire une requête API avec `params`, `headers`, `timeout`
- Exploiter une réponse JSON avec `.json()`
- Gérer les codes spécifiques aux APIs (401, 403, 429)
- Stocker une clé API hors du code (env, `.env`)
- Respecter les rate limits (`429`, `Retry-After`)
- Pagination d’API (page, offset, cursor)
- Pattern `ApiClient` réutilisable avec session, retries 429, User-Agent
- Sauvegarder la réponse brute dans `data/raw/` pour reproductibilité

-----

# Chapitre 12 — Bonnes pratiques professionnelles

Tu sais collecter, parser, stocker, paginer, interroger des APIs. Ce chapitre rassemble les **outils qui transforment un script qui marche en outil qui dure**. Pas de nouveau concept de collecte ici — uniquement de la robustesse, de la lisibilité, et de la maintenance.

## Le minimum à savoir

### `requests.Session()` : la base

Tu l’as vue en bonus au chapitre 5. Maintenant on l’adopte par défaut :

```python
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)",
    "Accept-Language": "fr,en;q=0.8",
})

# Toutes les requêtes utilisent les mêmes headers et réutilisent la connexion
r1 = session.get("https://exemple.fr/page1", timeout=10)
r2 = session.get("https://exemple.fr/page2", timeout=10)
```

Avantages :

- Headers partagés en une seule définition.
- Réutilisation de la connexion TCP/TLS (plus rapide).
- Gestion automatique des cookies (utile pour suivre une session si nécessaire).

### Retries avec backoff exponentiel

Plutôt que d’abandonner à la première erreur réseau, on retente avec un délai qui **augmente** à chaque essai :

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

def make_session():
    session = requests.Session()
    session.headers["User-Agent"] = "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"

    retry = Retry(
        total=4,                       # nombre max d’essais
        backoff_factor=1.5,            # délai = backoff * (2 ** (essai - 1))
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods={"GET", "HEAD"},
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
```

Avec `backoff_factor=1.5`, les délais sont : 0, 1.5, 3, 6, 12 s.

> **Important :** ce retry **automatique** se déclenche sur les statuts définis. Pour autant, tu dois **toujours** plafonner par toi-même (`MAX_PAGES`, `MAX_ITEMS`) — la combinaison « retry + plafond » te protège de tous les côtés.

### Le module `logging` : la base professionnelle

`print()` est très bien pour débug rapide. Pour un outil maintenable, on passe à `logging` :

```python
import logging
from datetime import datetime, timezone
from pathlib import Path

def setup_logging(run_id, log_dir="logs", level=logging.INFO):
    """Configure logs vers fichier ET console."""
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = Path(log_dir) / f"{run_id}.log"

    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    logging.basicConfig(
        level=level,
        format=fmt,
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger("collecteur")
    logger.info("Démarrage run_id=%s", run_id)
    return logger
```

Usage dans le code :

```python
logger = logging.getLogger(__name__)

logger.debug("Détail technique pour le développement")
logger.info("Information attendue (avancement normal)")
logger.warning("Quelque chose d’anormal mais non bloquant")
logger.error("Erreur — on continue avec d’autres données")
logger.critical("Erreur grave — arrêt du programme")
```

Niveaux à retenir :

|Niveau    |Quand l’utiliser                           |
|----------|-------------------------------------------|
|`DEBUG`   |Détails utiles uniquement en développement.|
|`INFO`    |Étapes normales du programme.              |
|`WARNING` |Anomalie qu’on tolère.                     |
|`ERROR`   |Échec d’une opération.                     |
|`CRITICAL`|Échec qui arrête le programme.             |


> **À retenir :** un `logger.info("Récupération de %s", url)` qui passe sa variable en argument séparé est plus performant qu’un f-string, parce que le formatage n’a lieu que si le niveau est actif. À adopter par habitude.

### Configuration externe

**Tout** ce qui change entre deux exécutions ou deux utilisateurs doit sortir du code. Trois mécanismes complémentaires :

**1. Arguments CLI avec `argparse`**

```python
import argparse

def parse_args():
    p = argparse.ArgumentParser(description="Collecteur OSINT")
    p.add_argument("--config", default="config/config.yaml", help="Fichier de config")
    p.add_argument("--target", required=True, help="URL ou identifiant de cible")
    p.add_argument("--max-pages", type=int, default=20)
    p.add_argument("--delay", type=float, default=1.0)
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args()
```

**2. Fichier de configuration (`config/config.yaml` ou `config/config.json`)**

```yaml
# config/config.yaml
output_dir: data/processed
raw_dir: data/raw
log_dir: logs
user_agent: "MonOutilOSINT/0.1 (+contact: osint-projet@example.org)"
default_timeout: 10
default_delay: 1.5
max_pages: 50
max_items: 1000
```

```python
import yaml
from pathlib import Path

config = yaml.safe_load(Path("config/config.yaml").read_text(encoding="utf-8"))
```

(Nécessite `pip install pyyaml` ; alternative sans dépendance : JSON.)

**3. Variables d’environnement (secrets uniquement)**

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CTI_API_KEY")
```

Règle simple :

|Type                               |Où ?                              |
|-----------------------------------|----------------------------------|
|Paramètres de runtime              |CLI args                          |
|Paramètres stables d’un déploiement|Fichier de config                 |
|Secrets                            |Variables d’environnement / `.env`|

### Séparation code / données / config / secrets

Arborescence d’un projet OSINT mature :

```
osint-collecte/
├── src/                  ← code Python
│   ├── __init__.py
│   ├── fetch.py
│   ├── parse.py
│   ├── clean.py
│   ├── store.py
│   ├── paginate.py
│   ├── api_client.py
│   ├── report.py         (chapitre 14)
│   └── main.py
├── config/
│   ├── config.yaml       ← paramètres (versionné)
│   ├── targets.txt       ← cibles (selon le projet : versionné ou non)
│   └── fiche-enquete.md  ← gabarit (versionné)
├── data/
│   ├── raw/              ← collectes brutes (NON versionné)
│   └── processed/        ← données traitées (NON versionné)
├── logs/                 ← journaux (NON versionné)
├── reports/              ← rapports (selon sensibilité)
├── tests/                ← tests (versionné)
├── .env                  ← secrets (NON versionné)
├── .env.example          ← modèle de .env (versionné)
├── .gitignore
├── requirements.txt
└── README.md
```

Le `.env.example` est un détail qui change tout : il documente quelles variables d’environnement sont attendues, sans les valeurs réelles. Toi ou un collègue n’a qu’à le copier en `.env` et remplir.

```
# .env.example
CTI_API_KEY=
WEATHER_API_KEY=
```

### Reproductibilité

Pour qu’une enquête soit reproductible, conserve :

1. **`requirements.txt`** figé (`pip freeze > requirements.txt`).
1. **Version Python** documentée dans le README (`Python 3.12+`).
1. **`run_id` partagé** entre tous les artefacts d’une exécution.
1. **Fiche d’enquête** complète, archivée dans `reports/`.
1. **Le code lui-même versionné** (Git), avec une **release** ou un **commit** identifiable cité dans le rapport.

> **À retenir :** une enquête OSINT non reproductible n’a pas de valeur d’enquête. Un collègue (ou toi-même dans six mois) doit pouvoir refaire la collecte et arriver au même résultat.

### Documentation : le README minimum vital

```markdown
# Mon collecteur OSINT

## Objectif
Une phrase. Pour quoi ce projet existe.

## Limites et cadre
- Sources autorisées : <liste>
- Cibles interdites : <liste>
- Base légale et finalité : <résumé>

## Installation
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env  # puis remplir

## Usage
    python -m src.main --target <url> --max-pages 20

## Structure
- `src/` : code
- `config/` : paramètres et cibles
- `data/raw/` : collectes brutes (non versionné)
- `data/processed/` : données traitées (non versionné)
- `logs/` : journaux

## Cadre éthique
Ce projet collecte uniquement des données publiques, dans le respect
de robots.txt et des CGU des sites cibles. Pour toute question :
osint-projet@example.org

## Auteur et licence
<...>
```

## Très utile en pratique

### Pattern de `main.py` complet

Voici à quoi ressemble un point d’entrée mature :

```python
# src/main.py
import sys
import logging
import yaml
from datetime import datetime, timezone
from pathlib import Path

from src.fetch import make_session, fetch
from src.parse import parse_page
from src.paginate import collect_paginated
from src.store import write
from src.clean import clean_pipeline


def main():
    args = parse_args()
    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logger = setup_logging(run_id, log_dir=config["log_dir"])

    logger.info("Cible : %s", args.target)
    logger.info("Max pages : %d, délai : %.1fs", args.max_pages, args.delay)

    session = make_session()

    try:
        items, journal = collect_paginated(
            args.target,
            fetch=lambda url: fetch(url, session=session,
                                    raw_dir=config["raw_dir"], run_id=run_id),
            parse=parse_page,
            max_pages=args.max_pages,
            max_items=config["max_items"],
            delay=args.delay,
        )
    except Exception as e:
        logger.critical("Collecte interrompue : %s", e)
        sys.exit(1)

    logger.info("Collecte terminée : %d items, %d pages", len(items), len(journal))

    cleaned = clean_pipeline(items, source_url=args.target)
    out = Path(config["output_dir"]) / f"{run_id}_collecte.json"
    write({"metadata": {"run_id": run_id, "tool": "collecteur/0.1",
                        "count": len(cleaned), "target": args.target},
           "data": cleaned}, out, format="json")
    logger.info("Sortie : %s", out)


if __name__ == "__main__":
    main()
```

Tu reconnais toutes les briques des chapitres précédents : `fetch`, `parse`, `paginate`, `clean`, `store`. Le `main` les **orchestre**, mais ne fait pas de travail de collecte lui-même.

### OPSEC : rappel final

|Réflexe                                  |Pourquoi                                           |
|-----------------------------------------|---------------------------------------------------|
|User-Agent identifiable                  |Honnêteté, traçabilité, contact en cas de problème.|
|Timeout obligatoire                      |Pas de script qui pend.                            |
|Rate limit volontaire                    |Respect du serveur, anti-bannissement.             |
|Pas d’usurpation anti-bot                |Question éthique et signal d’intention.            |
|Secrets hors code                        |Pas de fuite via Git.                              |
|VPN si besoin (selon contexte)           |Séparer ses identités d’enquête et personnelles.   |
|`data/raw/` et `data/processed/` hors Git|Pas de fuite de données sensibles.                 |
|Logs structurés et conservés             |Reproductibilité, traçabilité.                     |

### Tests basiques (bonus)

Pour les fonctions pures (parsing, nettoyage), des tests `pytest` simples valent leur pesant d’or :

```python
# tests/test_clean.py
from src.clean import clean_text, canonical_url

def test_clean_text_removes_nbsp():
    assert clean_text("Bonjour\xa0le\xa0monde") == "Bonjour le monde"

def test_canonical_url_removes_utm():
    url = "https://Ex.fr/page?utm_source=x&id=42"
    assert canonical_url(url) == "https://ex.fr/page?id=42"
```

`pytest` détecte automatiquement les fichiers `test_*.py` et les fonctions `test_*`. Lance avec :

```bash
pip install pytest
pytest
```

C’est hors-scope pour ce cours, mais à adopter dès qu’un projet dépasse quelques scripts.

## Bonus

### `requests-cache` pour le développement

Évite de retélécharger la même page pendant que tu mets au point ton parser :

```python
import requests_cache
session = requests_cache.CachedSession("dev_cache", expire_after=3600)
```

**À désactiver en production** — tu veux des données fraîches.

### Niveau `logging` configurable

```python
# Permettre -v pour DEBUG, -vv pour tout, sinon INFO
def log_level(verbose):
    return [logging.WARNING, logging.INFO, logging.DEBUG][min(verbose, 2)]
```

```python
logging.basicConfig(level=log_level(args.verbose), ...)
```

## ❌ Erreur classique

```python
# Hardcoder les paramètres dans le script
TARGET = "https://exemple.fr"
MAX_PAGES = 20
# ❌ Pour changer une cible, il faut éditer le code.
# ✅ argparse + config.yaml.

# print() pour tout
print(f"Récupération de {url}")
# ❌ Pas de niveaux, pas de fichier de log, pas de timestamps automatiques.
# ✅ logging.info("Récupération de %s", url)

# Logger les secrets
logger.info("Auth header : %s", session.headers)
# ❌ Tu loggues ta clé API en clair dans logs/...log
# ✅ Filtrer les headers sensibles avant de logger

# Capture trop large
try:
    ...
except Exception:
    pass
# ❌ Tu masques tous les bugs, y compris dans ton propre code.
# ✅ Capture des exceptions spécifiques + logging.error pour les inattendues.

# Pas de requirements.txt
# ❌ Personne ne peut reproduire ton environnement, y compris toi dans 6 mois.
# ✅ pip freeze > requirements.txt après chaque ajout de dépendance.

# Versionner data/raw/ ou .env
# ❌ Fuite de données + secrets exposés
# ✅ .gitignore strict, .env.example pour documenter
```

## Exercices

**Guidé :**

1. Reprends le mini-projet « Collecteur de citations » et refactorise-le pour utiliser :
- `requests.Session()` avec User-Agent partagé,
- `Retry` automatique sur les statuts transitoires,
- `logging` avec fichier `logs/<run_id>.log`,
- `argparse` pour `--url`, `--max-pages`, `--delay`, `-v`,
- `config/config.yaml` pour les paramètres stables.
1. Vérifie qu’il fonctionne toujours sans paramètres explicites (valeurs par défaut sensées).
1. Vérifie qu’il logge bien la durée totale et le nombre de retries effectués.

**Autonome :**

1. Écris un script `src/check.py` qui charge `config/config.yaml`, vérifie que tous les dossiers `raw_dir`, `output_dir`, `log_dir` existent (et les crée sinon), et qu’une variable d’environnement `CTI_API_KEY` est définie (sans afficher sa valeur).
1. Affiche un rapport `✓` / `✗` par vérification.
1. Renvoie un code de sortie 0 si tout va bien, 1 sinon.
1. Documente l’usage dans le README.

## 🧩 Mini-projet de Partie IV (2/2) — *Collecteur d’articles publics*

**Objectif :** un collecteur d’articles paginé, complet et professionnel. C’est l’occasion de mettre ensemble pagination, sessions, retries, logs, configuration externe.

**Cibles autorisées (par ordre de préférence, conformément à la doctrine API > RSS > sitemap > open data > scraping) :**

- soit un **site bac à sable** qui pagine en HTML (`books.toscrape.com`, `quotes.toscrape.com` avec sa pagination par `/page/N/`) ;
- soit un **blog technique public** qui **n’expose ni RSS ni sitemap exploitable** pour le besoin précis du projet ;
- soit un **flux RSS ou un sitemap** lorsqu’il existe — dans ce cas, **le projet doit consommer cette source propre** plutôt que scraper le HTML rendu, et on adapte l’architecture en conséquence (parsing XML via `feedparser` ou `xml.etree`).

Le but pédagogique reste le même : pagination, sessions, retries, logs, configuration externe — mais on n’invente pas une raison de scraper si une source plus propre est disponible.

**Cahier des charges :**

1. **Configuration** (`config/articles.yaml`) :
- URL de départ,
- `max_pages`,
- `max_items`,
- `delay`,
- `output_dir`, `raw_dir`, `log_dir`.
1. **Architecture** :
- `src/fetch.py` : session, retries, sauvegarde brute.
- `src/parse.py` : extraction des articles (titre, URL canonique, date, auteur, résumé, tags).
- `src/paginate.py` : collecte multi-pages avec `next link`.
- `src/clean.py` : nettoyage + canonisation + déduplication par URL canonique (chaque article = une URL distincte, donc `source_url` convient).
- `src/store.py` : sortie en JSON Lines (append-friendly).
- `src/main.py` : orchestration + CLI + logging.
1. **Politesse** :
- `Crawl-delay` de robots.txt respecté.
- User-Agent identifiable.
- Plafonds explicites.
1. **Reproductibilité** :
- `run_id` partagé entre `data/raw/`, `data/processed/`, `logs/`.
- `requirements.txt` figé.
- `README.md` avec installation, usage, cadre éthique.
1. **Livrables** :
- Une exécution complète avec ses artefacts.
- Le journal `logs/<run_id>.log` lisible et complet.
- Le dataset propre dans `data/processed/<run_id>_articles.jsonl`.

> **Rappel** : `data/` et `.env` restent hors de Git. Ne pousse que `src/`, `config/` (sans secrets), `requirements.txt`, `README.md`, et éventuellement `tests/`.

## ✅ Tu sais maintenant…

- Utiliser `requests.Session()` par défaut
- Configurer `Retry` avec backoff exponentiel pour les statuts transitoires
- Mettre en place `logging` avec fichier + console et niveaux pertinents
- Sortir les paramètres du code : `argparse` + `config.yaml` + `.env`
- Architecturer un projet OSINT mature (`src/`, `data/`, `config/`, `logs/`, `reports/`)
- Documenter avec un README clair et un `.env.example`
- Tenir une enquête **reproductible** (run_id, requirements.txt, version Python, code versionné)
- Orchestrer une collecte complète depuis un `main.py` lisible

-----

> **🎯 Tu as terminé la Partie IV.**
> 
> Tu sais maintenant collecter à l’échelle, exploiter des APIs et structurer un projet professionnel. Mais l’OSINT ne s’arrête pas à la collecte ponctuelle. Une bonne partie du métier consiste à **surveiller dans le temps** : détecter les nouvelles publications, repérer les changements, produire des rapports lisibles.
> 
> La Partie V s’attaque à ça : veille et reporting.

-----

# PARTIE V — ENQUÊTE, VEILLE ET REPORTING

> **Objectif de la partie :** dépasser la collecte ponctuelle. Apprendre à **surveiller dans le temps**, à **détecter les changements**, et à transformer des données en **rapport exploitable par un humain**.
> 
> Cette partie te fait basculer du « script qui collecte » à l’**outil d’enquête**.

-----

# Chapitre 13 — Veille et détection de changements

Une collecte unique te donne un instantané. Une veille te donne un **mouvement**. C’est souvent ce qui compte vraiment : qu’est-ce qui a changé, depuis quand, et dans quel sens ?

## Le minimum à savoir

### Le principe : snapshots et comparaison

```
T0 : collecte n°1 → snapshot_T0
T1 : collecte n°2 → snapshot_T1
                       ↓
          comparer(snapshot_T0, snapshot_T1)
                       ↓
        ajouts / retraits / modifications
```

Chaque exécution de ton veilleur produit un **snapshot** complet (dataset propre), horodaté et conservé. La veille consiste à comparer deux snapshots successifs et à isoler les différences.

### Hasher pour comparer rapidement

Comparer deux datasets dict par dict est coûteux. On préfère calculer un **hash** par enregistrement et travailler sur les hashes.

```python
import hashlib
import json

def hash_record(record, fields):
    """Hash SHA-256 stable sur certains champs d’un enregistrement."""
    base = json.dumps([record.get(f, "") for f in fields],
                      ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()
```

> **Crucial : ne hash que ce qui compte.** Si tu hashes le HTML brut, il change à chaque requête (timestamps, jetons CSRF, nonces, scripts d’analytics). Hash uniquement les **champs métier** qui te disent réellement « cet item est le même ».

|Pour quoi        |Hasher quoi                                                                          |
|-----------------|-------------------------------------------------------------------------------------|
|Article          |`titre` + `url` (ou `titre` + `auteur` + `date`)                                     |
|Prix d’un produit|`référence_produit` (`item_id`) — la valeur du prix change, mais l’item reste le même|
|Citation         |`texte` + `auteur`                                                                   |
|Annonce d’emploi |`titre` + `entreprise` + `localisation`                                              |

### Définir ce qui « compte » comme changement

Une fois les items identifiés (par hash de leurs **clés** stables), tu peux comparer leurs **valeurs** changeantes :

```python
# Clés stables (identifient l’item)
KEY_FIELDS = ["titre", "url"]

# Valeurs surveillées (signalent un changement)
WATCHED_FIELDS = ["prix", "disponibilite", "resume"]


def index_by_key(items):
    """Indexe une liste d’items par leur hash de clé."""
    return {hash_record(it, KEY_FIELDS): it for it in items}


def diff(old, new):
    """Retourne (ajoutés, retirés, modifiés)."""
    old_idx = index_by_key(old)
    new_idx = index_by_key(new)

    ajoutes = [new_idx[k] for k in new_idx.keys() - old_idx.keys()]
    retires = [old_idx[k] for k in old_idx.keys() - new_idx.keys()]

    modifies = []
    for k in old_idx.keys() & new_idx.keys():
        old_v = old_idx[k]
        new_v = new_idx[k]
        changements = {
            f: {"avant": old_v.get(f), "apres": new_v.get(f)}
            for f in WATCHED_FIELDS
            if old_v.get(f) != new_v.get(f)
        }
        if changements:
            modifies.append({
                "key": k,
                "titre": new_v.get("titre"),
                "changements": changements,
            })

    return ajoutes, retires, modifies
```

Ce pattern (clés stables + valeurs surveillées) est extrêmement puissant. Tu sais exactement quels items sont apparus, quels items ont disparu, et quels champs ont changé sur les items qui restent.

> **À adapter à chaque cas d’usage :**
> 
> |Type de dataset   |Clés stables (`KEY_FIELDS`)          |Valeurs surveillées (`WATCHED_FIELDS`)|
> |------------------|-------------------------------------|--------------------------------------|
> |Articles d’un site|`url`                                |`titre`, `resume`                     |
> |Produit e-commerce|`product_id`                         |`prix`, `disponibilite`, `note`       |
> |Annonces d’emploi |`titre`, `entreprise`, `localisation`|`description`, `statut`               |
> |Bulletin officiel |`reference`, `date`                  |`texte_normalise`                     |
> 
> **Règle :** la clé identifie l’item de façon stable ; la valeur surveillée est ce dont le changement t’intéresse.

### Stocker les snapshots dans le temps

Une organisation simple, robuste, lisible :

```
data/snapshots/
├── 20260517T080000Z/
│   ├── articles.json          (snapshot complet)
│   └── meta.json              (run_id, source, count, hash global)
├── 20260518T080000Z/
│   ├── articles.json
│   └── meta.json
└── 20260519T080000Z/
    ├── articles.json
    └── meta.json
```

Chaque exécution produit un dossier horodaté avec son `run_id`. Le dernier snapshot est facilement repérable par tri sur le nom.

```python
from pathlib import Path

def latest_snapshot(snap_dir="data/snapshots"):
    """Renvoie le chemin du snapshot le plus récent, ou None."""
    base = Path(snap_dir)
    if not base.exists():
        return None
    dossiers = sorted([d for d in base.iterdir() if d.is_dir()])
    return dossiers[-1] if dossiers else None
```

### Le squelette d’un veilleur

```python
# src/watch.py
import json
import logging
from pathlib import Path
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def run_watch(collect_fn, snap_dir="data/snapshots", change_log="logs/changes.log"):
    """Lance une collecte et compare au snapshot précédent.

    collect_fn() -> list[dict] : fonction qui produit le nouveau dataset.
    """
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # 1. Collecte
    new_items = collect_fn()

    # 2. Charger snapshot précédent
    prev = latest_snapshot(snap_dir)
    if prev:
        old_items = json.loads((prev / "articles.json").read_text(encoding="utf-8"))
        ajoutes, retires, modifies = diff(old_items, new_items)
        logger.info("Diff vs %s : +%d ajoutés, -%d retirés, ~%d modifiés",
                    prev.name, len(ajoutes), len(retires), len(modifies))
    else:
        ajoutes, retires, modifies = new_items, [], []
        logger.info("Premier snapshot, %d items collectés", len(new_items))

    # 3. Sauver le nouveau snapshot
    out = Path(snap_dir) / run_id
    out.mkdir(parents=True, exist_ok=True)
    (out / "articles.json").write_text(
        json.dumps(new_items, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "meta.json").write_text(json.dumps({
        "run_id": run_id,
        "count": len(new_items),
        "diff_vs_previous": {
            "previous": prev.name if prev else None,
            "added": len(ajoutes),
            "removed": len(retires),
            "modified": len(modifies),
        }
    }, indent=2), encoding="utf-8")

    # 4. Logguer les changements en clair
    if prev and (ajoutes or retires or modifies):
        with open(change_log, "a", encoding="utf-8") as f:
            f.write(f"\n=== {run_id} (vs {prev.name}) ===\n")
            for a in ajoutes:
                f.write(f"+ AJOUTÉ : {a.get('titre')} — {a.get('url')}\n")
            for r in retires:
                f.write(f"- RETIRÉ : {r.get('titre')} — {r.get('url')}\n")
            for m in modifies:
                f.write(f"~ MODIFIÉ : {m['titre']}\n")
                for ch_field, ch in m["changements"].items():
                    f.write(f"    {ch_field}: {ch['avant']!r} -> {ch['apres']!r}\n")

    return {"ajoutes": ajoutes, "retires": retires, "modifies": modifies}
```

### Bonnes pratiques de cadence

|Cas                                            |Fréquence raisonnable              |
|-----------------------------------------------|-----------------------------------|
|Veille de blog/média                           |1× par jour                        |
|Suivi de bulletins officiels (CERT, ministères)|1× à 4× par jour                   |
|Page « emplois » d’une entreprise              |1× par jour                        |
|Page produit (prix, disponibilité)             |1× à 4× par jour                   |
|Quasi temps réel                               |Quelques fois par heure **au plus**|


> **À retenir :** la veille n’est pas une **course**. Tu veux détecter un changement dans la journée, rarement à la minute. Une cadence d’une fois par jour est presque toujours suffisante pour un cas OSINT défensif. Plus rapide → tu marteles le serveur sans gain réel.

### Ce qu’on ne fait **pas** avec un veilleur

- **Imiter un service de monitoring payant** sans en avoir le droit (bypass d’un produit commercial).
- **Surveiller en permanence** une page qu’on n’a manifestement pas besoin de surveiller en temps réel.
- **Veiller sur des contenus accessibles uniquement en session connectée** : si tu dois te connecter, ce n’est pas du public.
- **Veiller sur des données personnelles** sans cadre légal explicite.

## Très utile en pratique

### Comparer du texte avec `difflib`

Quand un même item a changé en interne (texte d’un article modifié, par exemple), tu veux savoir **où** :

```python
import difflib

def text_diff(old_text, new_text, context=2):
    """Retourne les lignes différentes au format unified diff."""
    old_lines = old_text.splitlines(keepends=True)
    new_lines = new_text.splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        old_lines, new_lines,
        fromfile="avant", tofile="apres",
        n=context,
    ))
```

Pratique pour les bulletins, communiqués, mentions légales, conditions d’utilisation.

### Comparaison rapide par hash global

Pour décider en deux lignes si quelque chose a changé sans rentrer dans le détail :

```python
import hashlib
import json

def dataset_hash(items, fields):
    """Hash d’un dataset entier sur les champs sélectionnés."""
    parts = sorted(hash_record(it, fields) for it in items)
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


if dataset_hash(new_items, KEY_FIELDS + WATCHED_FIELDS) \
        == dataset_hash(old_items, KEY_FIELDS + WATCHED_FIELDS):
    logger.info("Aucun changement.")
    return
```

Utile pour court-circuiter la suite quand rien n’a bougé.

### Alertes : du plus simple au plus complet

|Niveau|Mécanisme                                                |Cas d’usage                                       |
|------|---------------------------------------------------------|--------------------------------------------------|
|0     |Rien, juste les logs                                     |Veille personnelle, on lit les logs à son rythme. |
|1     |Fichier `changes.log` (texte)                            |Veille structurée — on consulte en fin de journée.|
|2     |Notification système (`notify-send`, `terminal-notifier`)|Veille personnelle réactive.                      |
|3     |Email                                                    |Veille pour soi ou pour un petit groupe.          |
|4     |Webhook Slack/Discord                                    |Équipe collaborative.                             |


> **Précautions** sur les niveaux 3 et 4 : ne diffuse pas plus que ce que tu as collecté. Si la collecte respecte la minimisation, l’alerte aussi. Pas de fuite de données sensibles par un webhook mal configuré.

### Le réflexe : un changelog humain

En plus du `changes.log` machine, tiens un **journal de veille** humain dans `reports/` :

```markdown
# Journal de veille — Section publications [domaine.fr/publications]

## 2026-05-18
- Nouveau document : "Note d’information n°2026-12" (publiée 2026-05-17).
- Modification : page "À propos" — mise à jour du conseil d’administration.

## 2026-05-17
- Aucun changement.

## 2026-05-16
- Nouveau document : "Bilan annuel 2025".
```

Trois lignes par jour suffisent. Ce journal a souvent **plus de valeur** que le dataset lui-même, parce qu’il raconte une histoire dans le temps.

## Bonus

### Hash du HTML normalisé

Si tu n’as pas de dataset propre mais juste une page (cas d’une veille « brute »), tu peux hasher le HTML **normalisé** (parsé et reformaté) plutôt que brut :

```python
from bs4 import BeautifulSoup
import hashlib

def stable_html_hash(html_bytes):
    """Hash du texte visible, après nettoyage des scripts et styles."""
    soup = BeautifulSoup(html_bytes, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    texte = soup.get_text(" ", strip=True)
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()
```

C’est plus stable que `hashlib.sha256(html_bytes)` pour une veille naïve.

### Webhook Discord/Slack (avec précautions)

Exemple minimal Discord :

```python
import requests

def notify_discord(webhook_url, message):
    requests.post(webhook_url, json={"content": message[:1900]}, timeout=10)
```

- **Webhook URL** = secret. Mets-la dans `.env`.
- **Ne pousse jamais** de données personnelles ou sensibles dans un webhook public.
- **Tronque** les messages — la plupart des services rejettent les longs payloads.

## ❌ Erreur classique

```python
# Hasher le HTML brut
hash1 = hashlib.sha256(html_today).hexdigest()
hash2 = hashlib.sha256(html_yesterday).hexdigest()
# ❌ Les hashes diffèrent à cause de timestamps, nonces, scripts dynamiques.
# La page semble changer tous les jours alors qu’elle est stable.
# ✅ Hash sur du texte visible normalisé OU sur des champs métier.

# Veille toutes les minutes
# ❌ Tu marteles le site sans gain, et tu finis par te faire bloquer.
# ✅ 1× à 4× par jour suffit dans 99 % des cas.

# changes.log qui grossit sans bornes
with open("changes.log", "a") as f:
    f.write("...")
# ❌ Au bout de 2 ans, fichier illisible et impossible à analyser.
# ✅ Roulement par mois : changes-2026-05.log, changes-2026-06.log

# Alerter sur tout changement, même cosmétique
# ❌ Si tu surveilles le HTML brut sans normalisation, tu reçois
# une alerte à chaque visite. Fatigue d’alerte → tu finis par les ignorer.
# ✅ N’alerte que sur changements de champs surveillés.

# Comparer le snapshot d’hier au snapshot d’aujourd’hui sans vérifier
# que les deux ont été collectés au même endroit
# ❌ Si tu changes la cible entretemps, tu détectes des "changements"
# qui n’en sont pas.
# ✅ Stocker la cible dans le meta.json et vérifier l’égalité avant diff.
```

## Exercices

**Guidé :**

1. À partir du mini-projet « Collecteur d’articles publics » de la Partie IV, écris `src/watch.py` qui :
- relance la collecte,
- compare avec le snapshot précédent,
- écrit le diff dans `logs/changes.log`.
1. Lance deux fois à 10 minutes d’intervalle.
1. Simule un changement en éditant le snapshot précédent (modifier un titre, en supprimer un, en ajouter un fictif) et relance — vérifie que les trois cas sont détectés.

**Autonome :**

1. Écris un script `src/section_watcher.py` qui surveille **un seul** sélecteur CSS sur une page publique (par exemple le contenu d’un `<main>` ou d’une section précise).
1. Stocke le texte normalisé dans des fichiers horodatés dans `data/snapshots/<run_id>/section.txt`.
1. À chaque exécution, si le texte diffère du snapshot précédent, génère un diff Markdown lisible dans `reports/<run_id>_section_diff.md`.
1. Pense à respecter la cadence (1×/jour suffit).

## 🧩 Mini-projet de Partie V (1/2) — *Veilleur de page publique*

**Objectif :** un outil complet de veille avec snapshots versionnés, détection structurée des changements, et notification minimale.

**Cible :** la page d’accueil ou une section d’un site **public et non sensible** (idéalement une page institutionnelle, un blog technique, un site bac à sable).

**Cahier des charges :**

1. **Configuration** (`config/watch.yaml`) :
- liste d’URLs à surveiller,
- sélecteurs CSS par URL pour cibler ce qui compte,
- cadence recommandée (commentaire informatif).
1. **Architecture** :
- `src/fetch.py` (réutilisé),
- `src/parse.py` : extraction par URL et sélecteur,
- `src/diff.py` : `index_by_key`, `diff`, `dataset_hash`,
- `src/watch.py` : orchestration, snapshots, journal,
- `src/main.py` : CLI, logs, `run_id`.
1. **Sorties** :
- `data/snapshots/<run_id>/<url_safe_name>.json` (snapshot par URL),
- `data/snapshots/<run_id>/meta.json`,
- `logs/changes.log` cumulatif,
- `reports/<run_id>_summary.md` (résumé humain de l’exécution).
1. **Exécution** :
- lancement manuel (puis, en bonus, via cron / Tâches planifiées),
- sortie 0 si exécution OK, indépendamment de la présence de changements,
- log clair de ce qui a été fait.
1. **Politesse** :
- User-Agent identifiable,
- délai de 2 secondes entre deux URLs,
- plafond global de 30 URLs.

## ✅ Tu sais maintenant…

- Concevoir une veille comme une **succession de snapshots** comparés
- Hasher des **champs métier** (et pas du HTML brut) pour comparer
- Distinguer clés stables et valeurs surveillées
- Calculer `ajoutés / retirés / modifiés` entre deux datasets
- Comparer du texte avec `difflib`
- Organiser tes snapshots par dossier horodaté
- Choisir une cadence raisonnable (pas de course inutile)
- Émettre des alertes proportionnées (du fichier au webhook)

-----

# Chapitre 14 — Du script au rapport d’enquête

Une enquête se termine **toujours** par un rapport lisible par un humain. Pas par un CSV brut, pas par un JSON imbriqué. Ce chapitre te fait passer de la donnée structurée au **livrable**.

## Le minimum à savoir

### Donnée ≠ rapport

|Donnée                |Rapport                          |
|----------------------|---------------------------------|
|`CSV`, `JSON`, `JSONL`|Markdown, HTML, PDF              |
|Lit par un programme  |Lu par un humain                 |
|Brut, exhaustif       |Synthétique, hiérarchisé         |
|Pas de contexte       |Source, méthode, dates, auteur   |
|Pas d’interprétation  |Conclusion bornée par la collecte|

Tu ne **publies** jamais le CSV. Tu publies un rapport qui s’**appuie** sur le CSV.

> **Rappel minimisation :** le rapport ne contient que **ce qui sert la conclusion**. Le dataset complet reste dans `data/processed/` (ou en annexe), pas dans le corps du rapport. C’est cohérent avec la minimisation appliquée à la collecte (chapitre 2) : on collecte le minimum nécessaire, on rapporte le minimum nécessaire.

### Anatomie d’un rapport OSINT

```
1. Métadonnées (qui, quand, quoi, sur quelle base)
2. Résumé exécutif (3-5 lignes maximum)
3. Périmètre et limites (ce que le rapport couvre, ce qu’il ne couvre pas)
4. Méthode (sources, outil, version, run_id)
5. Résultats
   5.1 Vue d’ensemble (chiffres clés, top-N)
   5.2 Détails (tableaux, échantillons, anomalies)
6. Conclusion (bornée à ce que la collecte autorise)
7. Reproductibilité (commande exacte pour régénérer)
```

Cette structure n’est pas négociable pour un rapport d’enquête sérieux. Elle protège contre les deux dérives classiques : conclusions trop larges et résultat irreproductible.

### Le bloc de métadonnées (obligatoire)

```markdown
---
title: Inventaire des publications — site exemple.fr
author: A. Dupont (osint-projet@example.org)
date: 2026-05-17
run_id: 20260517T140000Z
tool: mon-collecteur/0.3.1
sources:
  - https://exemple.fr/publications
data: data/processed/20260517T140000Z_publications.json
base_legale: Veille publique défensive (intérêt légitime)
limites: |
  Collecte ponctuelle d’une seule section du site,
  pendant 2 minutes, le 17 mai 2026 à 14:00 UTC.
  Ne reflète pas les changements ultérieurs.
---
```

Au format Markdown, on utilise un **front matter YAML**. C’est parsable par les outils standards (Pandoc, etc.) et lisible humainement.

### Générer du Markdown depuis Python

```python
from datetime import datetime, timezone

def generate_report(items, source_url, run_id, tool, output_path):
    """Génère un rapport Markdown simple à partir d’un dataset."""
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    auteurs = sorted({it.get("auteur", "(inconnu)") for it in items})

    lines = [
        "---",
        f"title: Rapport de collecte — {source_url}",
        f"date: {date}",
        f"run_id: {run_id}",
        f"tool: {tool}",
        f"source: {source_url}",
        f"count: {len(items)}",
        "---",
        "",
        f"# Rapport de collecte — {source_url}",
        "",
        "## Résumé",
        "",
        f"- **{len(items)}** items collectés",
        f"- **{len(auteurs)}** auteurs distincts",
        f"- Date de collecte : {date} (UTC)",
        "",
        "## Métadonnées",
        "",
        f"- `run_id` : `{run_id}`",
        f"- Outil : `{tool}`",
        f"- Source : <{source_url}>",
        "",
        "## Top 5 auteurs",
        "",
    ]

    from collections import Counter
    top = Counter(it.get("auteur", "(inconnu)") for it in items).most_common(5)
    lines.append("| Auteur | Nombre |")
    lines.append("|---|---|")
    for auteur, n in top:
        lines.append(f"| {auteur} | {n} |")

    lines += [
        "",
        "## Limites",
        "",
        "Ce rapport reflète une collecte ponctuelle à la date indiquée. ",
        "Il ne reflète pas les éventuelles modifications ultérieures de la source. ",
        "Pour rejouer la collecte, voir la section *Reproductibilité*.",
        "",
        "## Reproductibilité",
        "",
        "```bash",
        f"python -m src.main --target {source_url} --max-pages 50",
        "```",
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
```

### Générer un tableau Markdown depuis une liste de dicts

```python
def md_table(rows, columns=None, max_rows=None):
    """Renvoie une table Markdown à partir de dicts."""
    if not rows:
        return "*(aucune donnée)*"
    columns = columns or list(rows[0].keys())
    if max_rows:
        rows = rows[:max_rows]
    out = ["| " + " | ".join(columns) + " |"]
    out.append("|" + "|".join(["---"] * len(columns)) + "|")
    for r in rows:
        vals = [str(r.get(c, "")).replace("|", "\\|") for c in columns]
        out.append("| " + " | ".join(vals) + " |")
    return "\n".join(out)
```

Note le `\\|` : les pipes dans une cellule Markdown doivent être échappés, sinon ils cassent le tableau.

### Statistiques basiques utiles

```python
from collections import Counter

def stats(items):
    """Statistiques minimales sur un dataset."""
    domains = Counter(it.get("domain", "") for it in items)
    auteurs = Counter(it.get("auteur", "") for it in items)
    return {
        "count": len(items),
        "domains_uniques": len([d for d in domains if d]),
        "top_domains": domains.most_common(5),
        "auteurs_uniques": len([a for a in auteurs if a]),
        "top_auteurs": auteurs.most_common(5),
        "premier_horodatage": min((it.get("collected_at") for it in items), default=None),
        "dernier_horodatage": max((it.get("collected_at") for it in items), default=None),
    }
```

Ces 6-7 chiffres suffisent pour la majorité des rapports. Inutile de calculer dix indicateurs si ton lecteur en regardera trois.

## Très utile en pratique

### Borner les conclusions à la collecte

C’est **la** règle d’or du rapport OSINT :

> Tout ce qu’on écrit doit être étayé par la collecte. Tout ce qui n’est pas étayé doit être explicitement formulé comme une hypothèse, une question, ou un angle mort.

|❌ Conclusion non bornée                     |✅ Conclusion bornée                                                                                          |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|« L’entreprise X a réorienté sa stratégie. »|« Au cours des 12 dernières semaines, 8 des 10 nouvelles offres d’emploi publiées portent sur le domaine Y. »|
|« Personne ne parle de ce sujet. »          |« Aucune des 250 publications collectées sur le site Z entre A et B ne mentionne ce sujet. »                 |

La nuance est constante : on parle de **ce qu’on a vu**, pas de **ce qui existe**. C’est ce qui fait la différence entre un rapport solide et une opinion habillée.

### Conservation des preuves

Le rapport vit dans `reports/`. Mais il **pointe** vers les preuves :

```
reports/
├── 20260517_inventaire_publications.md
├── 20260517_inventaire_publications.html  (export)
└── ...

data/raw/                    ← intouché (preuves brutes)
data/processed/              ← intouché (datasets exploités)
logs/                        ← intouché (journal d’exécution)
```

Un lecteur sceptique doit pouvoir :

1. lire ton rapport,
1. ouvrir le dataset cité dans les métadonnées,
1. ouvrir le HTML brut correspondant,
1. relire ton journal d’exécution,
1. relancer ta commande pour comparer.

Si l’un de ces cinq éléments manque, le rapport est invérifiable.

### Minimisation, jusque dans le rapport

Tu as collecté avec minimisation (chapitre 2). Tu **rapportes** avec minimisation aussi :

- Ne mets pas de données personnelles dans le rapport si elles ne sont pas indispensables à la conclusion.
- Ne reproduis pas des textes longs : résume, cite court, lie vers la source.
- Ne mets pas dans le rapport ce que tu as collecté « au cas où ».

### Conversion Markdown → HTML / PDF (en bonus)

Pour livrer à un destinataire non technique :

```bash
# Markdown -> HTML simple
pip install markdown
python -c "import markdown, pathlib; print(markdown.markdown(pathlib.Path('reports/x.md').read_text()))" > reports/x.html

# Markdown -> HTML stylé / PDF (avec Pandoc, installé séparément)
pandoc reports/x.md -o reports/x.html
pandoc reports/x.md -o reports/x.pdf
```

Pandoc n’est pas un package Python ; il s’installe via le système. C’est l’outil de référence pour les conversions de documents.

## Bonus

### Génération depuis un template

Quand les rapports deviennent récurrents, un moteur de templates est plus propre :

```bash
pip install jinja2
```

```python
from jinja2 import Template

TEMPLATE = """\
# Rapport de veille — {{ titre }}

**Période** : {{ debut }} → {{ fin }}
**run_id** : `{{ run_id }}`

## Résumé

- {{ nb_items }} items collectés
- {{ nb_changements }} changements détectés

## Changements

{% for c in changements %}
- {{ c.titre }} ({{ c.date }})
{% endfor %}
"""

rapport = Template(TEMPLATE).render(
    titre="exemple.fr",
    debut="2026-05-10", fin="2026-05-17",
    run_id=run_id, nb_items=len(items), nb_changements=len(changements),
    changements=changements,
)
```

Pratique dès que la même structure se répète à chaque exécution.

### Indicateurs visuels

Pour les rapports lus en ligne, des indicateurs simples améliorent la lecture :

```
✓ Collecte réussie sur 12/12 sources
⚠ 2 sources avec un avertissement (timeouts ponctuels)
✗ 0 source en échec total
```

À utiliser avec parcimonie — ne transforme pas un rapport en sapin de Noël.

## ❌ Erreur classique

```
# Rapport sans métadonnées
"# Analyse rapide
Ces données montrent que..."

❌ Pas de date, pas de source, pas de méthode. Invérifiable, donc inutile.
✅ Front matter YAML obligatoire en tête.

# Conclusions plus larges que la collecte
"L'entreprise X investit massivement dans Y."

❌ Sur quelle base ? Combien de signaux ? Sur quelle période ?
✅ Borner précisément : "Sur la période A-B, sur la source C,
   X publications mentionnent Y."

# Inclure des données personnelles inutiles
Tableau avec nom, email, téléphone, adresse — alors que seul le nom
sert l'analyse.

❌ Violation de la minimisation, surface RGPD inutile.
✅ Ne garder que les colonnes qui servent la conclusion.

# Rapport non reproductible
"Voir les pièces jointes."

❌ Quelles pièces ? Quelle version ? Quelle commande ?
✅ Bloc "Reproductibilité" avec commande exacte et run_id.

# Copier-coller massif du dataset
Le rapport contient 300 lignes d’un tableau collé tel quel.

❌ Pas de hiérarchie, pas de synthèse.
✅ Mettre les chiffres clés et un échantillon de 10 lignes max ;
   joindre le dataset complet en annexe.
```

## Exercices

**Guidé :**

1. Reprends le dataset produit par le mini-projet « Collecteur d’articles publics » (Partie IV).
1. Écris `src/report.py` qui produit un rapport Markdown contenant :
- front matter complet,
- résumé (3-5 lignes),
- tableau top-5 auteurs,
- tableau top-5 domaines (si pertinent),
- 5 derniers articles avec titre + date + URL,
- bloc « Reproductibilité » avec la commande exacte.
1. Génère le rapport dans `reports/<run_id>_articles.md`.

**Autonome :**

1. Ajoute à ton veilleur (mini-projet Partie V 1/2) la génération d’un rapport hebdomadaire.
1. Le rapport `reports/<semaine>_veille.md` couvre les 7 derniers jours et liste :
- tous les snapshots de la semaine,
- les ajouts/retraits/modifications par jour,
- une synthèse globale (X ajouts, Y modifications, Z retraits).
1. Inclus un graphique ASCII très simple (ex. nombre de changements par jour avec `▆▂▅█▃`).

## 🧩 Mini-projet de Partie V (2/2) — *Synthétiseur de veille hebdomadaire*

**Objectif :** consolider les snapshots d’une semaine en un rapport unique exploitable.

**Entrée :** le dossier `data/snapshots/` produit par le veilleur de la Partie V (1/2).

**Cahier des charges :**

1. **Configuration** (`config/synth.yaml`) :
- nombre de jours à couvrir (défaut : 7),
- format de sortie (`md`, `html`),
- dossier de sortie,
- chemins des snapshots.
1. **Module** `src/synth.py` :
- charge tous les snapshots sur la période,
- calcule les diffs jour par jour,
- agrège : ajouts cumulés, retraits cumulés, modifications,
- identifie les **items revus** (modifiés plus d’une fois) — signal d’activité.
1. **Sortie** : `reports/<periode>_synthese.md` avec :
- front matter complet,
- résumé exécutif,
- tableau des changements par jour,
- liste des items les plus actifs,
- section « Limites » (sources non couvertes, jours manquants),
- bloc reproductibilité.
1. **Bonus** : générer aussi un export HTML lisible dans un navigateur.

## ✅ Tu sais maintenant…

- Distinguer **donnée** (CSV/JSON) et **rapport** (livrable humain)
- Structurer un rapport OSINT : métadonnées → résumé → méthode → résultats → limites → reproductibilité
- Inclure systématiquement un front matter YAML (date, run_id, tool, source, base légale)
- Générer du Markdown depuis Python (tableaux, statistiques)
- Borner les conclusions à ce que la collecte autorise
- Appliquer la minimisation **jusque dans le rapport**
- Lier le rapport à ses preuves (`data/raw/`, `data/processed/`, `logs/`)
- Convertir en HTML/PDF avec Pandoc en bonus

-----

> **🎯 Tu as terminé la Partie V.**
> 
> Tu sais maintenant **surveiller dans le temps**, **détecter des changements** et **produire un rapport** exploitable par un humain. C’est l’aboutissement d’un cycle OSINT complet : collecter, structurer, comparer, restituer.
> 
> Il ne reste qu’une étape : **mettre tout ça ensemble** dans un véritable petit outil OSINT. C’est l’objet de la Partie VI.

-----

# PARTIE VI — PROJET FINAL

> **Objectif de la partie :** assembler **toutes les briques** des parties précédentes dans un véritable petit outil OSINT défensif. Tu vas livrer un projet présentable, reproductible, documenté, et conforme à tout ce qu’on a vu.
> 
> À la fin, tu auras un outil que tu peux montrer en portfolio, réutiliser dans une mission, ou faire évoluer pour un cas réel.

-----

# Chapitre 15 — Outil OSINT de collecte web défensive

## Présentation

Tu vas construire **`osint-web-collector`** : un collecteur web qui, à partir d’une liste d’URLs publiques, produit un inventaire structuré (liens, titres, métadonnées visibles), avec stockage, logs, et rapport.

Ce n’est pas un défi technique — toutes les briques ont déjà été vues. C’est un **exercice d’intégration** : prendre des modules cohérents, les faire dialoguer, les documenter, et livrer un tout présentable.

### Ce que le projet doit faire

```
                     ┌────────────────────┐
config/targets.txt   │                    │   data/raw/<run_id>_*.html
       ──────────►   │                    │   ──────────────────────►
                     │                    │
config/config.yaml   │   osint-web-       │   data/processed/<run_id>.csv
       ──────────►   │   collector        │   data/processed/<run_id>.json
                     │                    │   ──────────────────────►
.env (secrets)       │                    │
       ──────────►   │                    │   reports/<run_id>.md
                     │                    │   logs/<run_id>.log
                     └────────────────────┘   ──────────────────────►
```

### Ce que le projet ne doit **pas** faire

- Contourner un anti-bot.
- S’authentifier sur des services qui ne sont pas les tiens.
- Collecter massivement des données personnelles.
- Marteler une cible (toujours plafonner et espacer).
- Imiter un service de monitoring payant.

Ces interdits sont rappelés dans le README du projet, pas en ornement, mais comme **contrat de fonctionnement**.

## Cahier des charges

### Entrée

1. **`config/targets.txt`** : une URL publique par ligne. Commentaires possibles avec `#`.
   
   ```
   # Liste des cibles
   https://books.toscrape.com/
   https://quotes.toscrape.com/
   ```
1. **`config/config.yaml`** : paramètres globaux.
   
   ```yaml
   user_agent: "osint-web-collector/1.0 (+contact: osint-projet@example.org)"
   timeout: 10
   delay: 1.5
   max_pages_per_target: 5      # pour cible avec pagination
   max_items_total: 2000
   raw_dir: data/raw
   processed_dir: data/processed
   log_dir: logs
   report_dir: reports
   ```
1. **`.env`** (optionnel, pour les éventuelles APIs) : secrets, jamais versionné.

### Traitement (par URL)

Pour chaque URL de `targets.txt` :

1. **Vérification préalable** : récupérer et logger le `robots.txt` du domaine. Respecter `Crawl-delay` s’il est défini (override le `delay` config s’il est plus strict).
1. **Fetch propre** : User-Agent identifiable, timeout, retries, sauvegarde brute dans `data/raw/<run_id>_<host>_<path>.html`.
1. **Extraction** : liens (avec URLs canoniques), titres (`<title>`, `<h1>`, `<h2>`), métadonnées visibles (`<meta name=...>`, JSON-LD si présent), date détectée (`<time datetime=...>` ou `<meta property="article:published_time">`).
1. **Normalisation** : `clean_text` + `canonical_url`, déduplication par `item_id` (hash sur champs métier).
1. **Robustesse** : un site qui répond `5xx` ou qui timeout **ne fait pas planter** la collecte ; l’erreur est loguée, on passe à la cible suivante.

### Sortie

Tous les artefacts d’une exécution partagent le **même `run_id`** (UTC, ISO compact, ex. `20260520T143012Z`).

|Artefact            |Chemin                                |Contenu                                                                |
|--------------------|--------------------------------------|-----------------------------------------------------------------------|
|HTML brut           |`data/raw/<run_id>_<host>_<path>.html`|Tel que reçu, intouché.                                                |
|Inventaire des liens|`data/processed/<run_id>_links.csv`   |Une ligne = un lien (URL canonique, texte, page source, domaine).      |
|Inventaire par URL  |`data/processed/<run_id>_pages.json`  |Une entrée = une URL cible, avec ses métadonnées.                      |
|Journal d’exécution |`logs/<run_id>.log`                   |Logs structurés (INFO/WARNING/ERROR).                                  |
|Rapport             |`reports/<run_id>.md`                 |Markdown avec front matter, résumé, top-N, anomalies, reproductibilité.|

## Architecture

### Arborescence

```
osint-web-collector/
├── src/
│   ├── __init__.py
│   ├── config.py           # chargement config.yaml + .env
│   ├── robots.py           # lecture et interprétation robots.txt
│   ├── fetch.py            # session, retries, sauvegarde brute
│   ├── parse.py            # extraction liens / titres / méta / dates
│   ├── clean.py            # clean_text, canonical_url, déduplication
│   ├── store.py            # CSV / JSON / JSONL
│   ├── report.py           # rapport Markdown
│   └── main.py             # orchestration + CLI
├── config/
│   ├── config.yaml
│   ├── targets.txt
│   └── fiche-enquete.md    # gabarit
├── data/
│   ├── raw/                # .gitkeep, contenu non versionné
│   └── processed/          # .gitkeep, contenu non versionné
├── logs/                   # .gitkeep
├── reports/                # .gitkeep
├── tests/
│   ├── test_clean.py
│   └── test_parse.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE                  # MIT ou autre, selon ton choix
```

### Responsabilités des modules

|Module     |Rôle                                                                                   |S’appuie sur                    |
|-----------|---------------------------------------------------------------------------------------|--------------------------------|
|`config.py`|Charger `config.yaml`, lire `.env`, créer les dossiers.                                |`yaml`, `dotenv`, `pathlib`     |
|`robots.py`|Lire `robots.txt`, déterminer si une URL est autorisée et quel `Crawl-delay` appliquer.|`urllib.robotparser`, `requests`|
|`fetch.py` |Session HTTP partagée, `Retry`, User-Agent, timeout, sauvegarde brute.                 |`requests`, `urllib3`           |
|`parse.py` |Extraire liens, titres, métadonnées, dates.                                            |`bs4`, `urllib.parse`           |
|`clean.py` |Nettoyer texte, canoniser URLs, calculer `item_id`, dédupliquer.                       |`unicodedata`, `re`, `hashlib`  |
|`store.py` |Écrire CSV et JSON avec métadonnées globales.                                          |`csv`, `json`                   |
|`report.py`|Générer le rapport Markdown.                                                           |`collections.Counter`           |
|`main.py`  |Lire la config, parcourir les cibles, orchestrer, écrire la sortie, générer le rapport.|Tous les modules ci-dessus      |

### Squelette de `main.py`

```python
# src/main.py
import sys
import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

from src.config import load_config, setup_dirs
from src.robots import RobotsCache
from src.fetch import make_session, fetch
from src.parse import extract_page
from src.clean import clean_page, dedup_links
from src.store import write_links_csv, write_pages_json
from src.report import generate_report


def parse_args():
    p = argparse.ArgumentParser(description="osint-web-collector")
    p.add_argument("--config", default="config/config.yaml")
    p.add_argument("--targets", default="config/targets.txt")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args()


def setup_logging(run_id, log_dir, verbose=False):
    log_file = Path(log_dir) / f"{run_id}.log"
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"),
                  logging.StreamHandler()],
    )
    return logging.getLogger("collector")


def main():
    args = parse_args()
    config = load_config(args.config)
    setup_dirs(config)

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    logger = setup_logging(run_id, config["log_dir"], args.verbose)
    logger.info("Démarrage run_id=%s", run_id)

    # Charger les cibles
    targets = [line.strip() for line in Path(args.targets).read_text(encoding="utf-8").splitlines()
               if line.strip() and not line.strip().startswith("#")]
    logger.info("%d cibles à collecter", len(targets))

    session = make_session(config["user_agent"])
    robots = RobotsCache(session)

    pages = []
    all_links = []

    for i, url in enumerate(targets, 1):
        logger.info("[%d/%d] %s", i, len(targets), url)

        if not robots.is_allowed(url, config["user_agent"]):
            logger.warning("  → bloqué par robots.txt, ignoré")
            continue

        delay = max(config["delay"], robots.crawl_delay(url))

        try:
            r, raw_path = fetch(url, session=session,
                                raw_dir=config["raw_dir"], run_id=run_id,
                                timeout=config["timeout"])
            page = extract_page(r.content, source_url=url)
            page = clean_page(page)
            page["raw_file"] = str(raw_path)
            page["status_code"] = r.status_code
            page["run_id"] = run_id
            page["tool"] = "osint-web-collector/1.0"
            pages.append(page)
            all_links.extend(page["links"])
        except Exception as e:
            logger.error("  → erreur : %s", e)
            pages.append({
                "source_url": url, "error": str(e),
                "run_id": run_id, "tool": "osint-web-collector/1.0",
            })

        # Politesse
        robots.sleep_after(url, base=delay)

    # Dédup et écriture
    all_links = dedup_links(all_links)

    csv_path = Path(config["processed_dir"]) / f"{run_id}_links.csv"
    json_path = Path(config["processed_dir"]) / f"{run_id}_pages.json"
    report_path = Path(config["report_dir"]) / f"{run_id}.md"

    write_links_csv(all_links, csv_path)
    write_pages_json(pages, json_path, run_id=run_id,
                     tool="osint-web-collector/1.0")
    generate_report(pages, all_links, report_path, run_id=run_id)

    logger.info("Sortie CSV    : %s", csv_path)
    logger.info("Sortie JSON   : %s", json_path)
    logger.info("Rapport       : %s", report_path)
    logger.info("Fin run_id=%s : %d pages, %d liens uniques",
                run_id, len(pages), len(all_links))


if __name__ == "__main__":
    sys.exit(main() or 0)
```

Note : `robots.py` et le détail des autres modules sont **à toi à implémenter**. Toutes les briques techniques sont dans les chapitres 5 à 14.

## Étapes proposées

Une progression réaliste, à faire dans l’ordre :

1. **Initialiser le squelette** (chapitre 0 + chapitre 12) : arborescence, venv, `requirements.txt`, `.gitignore`, `README.md` initial.
1. **`config.py`** : charger `config.yaml`, lire `.env`, créer les dossiers manquants.
1. **`robots.py`** : utiliser `urllib.robotparser` pour vérifier l’autorisation par URL et lire le `Crawl-delay`.
1. **`fetch.py`** : `make_session()` avec `Retry`, `fetch()` qui accepte `session` et `run_id` (chapitre 12).
1. **`parse.py`** : `extract_page(html_bytes, source_url)` qui renvoie `{title, h1, h2, meta, links, published_at, source_url}`.
1. **`clean.py`** : `clean_page` (texte + canonisation des URLs), `dedup_links` (par URL canonique).
1. **`store.py`** : CSV + JSON avec métadonnées globales.
1. **`report.py`** : rapport Markdown complet (chapitre 14).
1. **`main.py`** : orchestration, logs, gestion d’erreurs.
1. **Tests** sur 2-3 cibles éthiques (sites bac à sable).
1. **README** complet, `.env.example`, `LICENSE`.
1. **Revue personnelle** avec la checklist ci-dessous.

## Checklist de revue personnelle

Avant de considérer le projet « livré », vérifie chaque case :

### Technique

- ☑ Le script tombe **proprement** si une cible est inaccessible (pas de plantage global).
- ☑ Toutes les requêtes ont un `timeout`.
- ☑ Toutes les requêtes utilisent une `Session` partagée avec `Retry`.
- ☑ Le User-Agent est identifiable et identique à `config.yaml`.
- ☑ Le `Crawl-delay` de `robots.txt` est respecté quand il est plus strict que `delay`.
- ☑ Un plafond explicite limite le volume total collecté.
- ☑ Les sorties dans `data/processed/` sont reproductibles à partir des `data/raw/`.

### Traçabilité

- ☑ Un seul `run_id` partagé entre HTML brut, CSV, JSON, log et rapport.
- ☑ Chaque enregistrement contient `source_url`, `collected_at`, `tool`, `run_id`.
- ☑ Le rapport contient son front matter complet.
- ☑ Le rapport cite les chemins exacts des datasets et logs.

### Documentation

- ☑ `README.md` complet (objectif, installation, usage, limites, cadre éthique, contact).
- ☑ `.env.example` documente les secrets attendus.
- ☑ Fiche d’enquête remplie pour l’exécution de référence.
- ☑ La commande de reproduction est dans le README **et** dans le rapport.

### Sécurité / éthique

- ☑ Aucune clé API ou secret dans le code (vérifier avec `git log -p` ou `git secrets`).
- ☑ `data/raw/`, `data/processed/`, `logs/`, `.env` sont dans `.gitignore`.
- ☑ Le projet n’imite pas un service commercial protégé.
- ☑ Les cibles d’exemple sont éthiques (bac à sable ou cibles autorisées explicitement).
- ☑ Aucune donnée personnelle inutile dans les datasets ou le rapport.

### Robustesse

- ☑ Le script tourne deux fois de suite sans rien casser.
- ☑ Une cible qui renvoie `404` n’interrompt pas la collecte.
- ☑ Une cible qui timeout n’interrompt pas la collecte.
- ☑ Un `429` est respecté (attente + retry contrôlé).

## Livrables attendus

1. **Le dépôt** (Git fortement recommandé) avec arborescence standard et toutes les cases ci-dessus cochées.
1. **Une exécution de référence** : un `run_id` complet dont tous les artefacts (`raw`, `processed`, `logs`, `reports`) sont conservés et liés.
1. **Le `README.md`** avec installation, usage, limites, base légale, contact.
1. **La fiche d’enquête** remplie pour l’exécution de référence.
1. **Optionnel mais recommandé** : 2-3 tests `pytest` sur les fonctions pures de `clean.py` et `parse.py`.

## Extensions possibles (pour aller plus loin)

Une fois la version de base livrée, plusieurs directions :

|Extension                                                                       |Difficulté|Apport                                   |
|--------------------------------------------------------------------------------|----------|-----------------------------------------|
|Mode **veille** : 2ᵉ commande qui compare avec le snapshot précédent            |🟡         |Réutilise tout le chapitre 13.           |
|Sortie HTML stylée pour le rapport                                              |🟢         |Pandoc ou `markdown` package.            |
|Plugin RSS / sitemap : si la cible expose un flux, l’utiliser au lieu de scraper|🟡         |Cohérence avec la doctrine du chapitre 4.|
|Test d’intégration avec `requests-mock`                                         |🟡         |Tester sans toucher au réseau.           |
|Mode interactif : choix des cibles via prompts plutôt que `targets.txt`         |🟢         |Confort utilisateur.                     |
|Export SQLite                                                                   |🟡         |Quand le volume dépasse JSON.            |
|Webhook de notification                                                         |🟡         |Veille collaborative.                    |


> **Conseil :** ne te lance dans les extensions qu’**après** avoir une version de base parfaitement propre. Mieux vaut un outil minimal et carré qu’un outil ambitieux et fragile.

## ✅ Tu sais maintenant…

- Concevoir et architecturer un projet OSINT complet
- Implémenter chaque module en s’appuyant sur les chapitres précédents
- Orchestrer le tout dans un `main.py` lisible
- Documenter, tester, et livrer un projet présentable en portfolio
- Auto-évaluer ton outil sur les critères technique, traçabilité, documentation, sécurité, robustesse

-----

# Annexes

## Annexe A — Sites d’entraînement légaux et reproductibles

|Site                                                                      |Pour quoi                                                                                       |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|`https://books.toscrape.com`                                              |Catalogue paginé. Idéal pour `requests`, BeautifulSoup, pagination.                             |
|`https://quotes.toscrape.com`                                             |Citations paginées avec variantes (JS, login factice). Excellent pour s’entraîner.              |
|`https://httpbin.org`                                                     |Bac à sable HTTP : statuts personnalisés, headers, délais. Indispensable pour tester `requests`.|
|`https://jsonplaceholder.typicode.com`                                    |API REST fictive pour s’entraîner aux APIs.                                                     |
|`https://api.open-meteo.com`                                              |API météo réelle, sans clé. Très bien pour s’entraîner aux APIs publiques.                      |
|`https://restcountries.com`                                               |API REST sur les pays. Sans clé.                                                                |
|`https://en.wikipedia.org/api/rest_v1/`                                   |API Wikipedia (lecture, modifications, métadonnées). Doc claire, rate limit raisonnable.        |
|`https://news.ycombinator.com` / API : `https://github.com/HackerNews/API`|API Hacker News (lecture seule). Sans clé.                                                      |
|`https://www.data.gouv.fr/api/`                                           |Open data administratif français.                                                               |
|`https://data.europa.eu/api/hub/search`                                   |Portail européen d’open data.                                                                   |

## Annexe B — Modules à explorer ensuite

|Module                   |Pour quoi                                                                                                        |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|
|`tldextract`             |Extraction propre du domaine racine (gère les TLD composés comme `.co.uk`).                                      |
|`requests-cache`         |Cache HTTP transparent en développement.                                                                         |
|`feedparser`             |Parser RSS/Atom robuste.                                                                                         |
|`scrapy`                 |Framework de crawling à grande échelle, avec planification, middlewares, pipelines.                              |
|`playwright` / `selenium`|Navigateurs automatisés pour sites réellement dynamiques — **outils avancés**, à utiliser dans un cadre autorisé.|
|`dnspython`              |Résolution DNS programmatique (A, AAAA, MX, NS, TXT, etc.).                                                      |
|`python-whois` / RDAP    |Infos d’enregistrement de domaines (RDAP est l’approche moderne).                                                |
|`pandas`                 |Analyse de datasets une fois propres : agrégations, jointures, exports.                                          |
|`pytest`                 |Tests unitaires et d’intégration.                                                                                |
|`pyyaml`                 |Lecture/écriture YAML, pour les configurations.                                                                  |
|`jinja2`                 |Templates pour les rapports récurrents.                                                                          |
|`pandoc` (externe)       |Conversion Markdown ↔ HTML ↔ PDF.                                                                                |

## Annexe C — Repères juridiques à vérifier avant usage réel

> **Rappel essentiel :** ce qui suit n’est ni un conseil juridique, ni un état exhaustif du droit applicable. Le droit évolue. Pour un projet réel et engageant (entreprise, mission, journalisme), consulte un juriste.

|Cadre                                         |Pour vérifier                                                                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|**RGPD (UE)**                                 |Toute collecte qui touche à des données personnelles. Vérifier finalité, base légale, minimisation, durée de conservation, droits des personnes.|
|**LCEN + Code pénal (FR, art. 323-1 et s.)**  |Atteintes aux systèmes de traitement automatisé de données. **Ne jamais** contourner une protection technique.                                  |
|**Droit d’auteur**                            |Textes, images, vidéos, bases de données. Le fait qu’un contenu soit accessible ne le rend pas réutilisable.                                    |
|**Droit sui generis sur les bases de données**|Extraction « substantielle » d’une base de données protégée.                                                                                    |
|**CGU / ToS**                                 |Force contractuelle variable selon les juridictions, mais leur violation peut t’exposer.                                                        |
|**Affaires de référence**                     |hiQ Labs vs LinkedIn (US), Ryanair vs PR Aviation (UE), décisions CNIL. À titre culturel uniquement — chaque cas est spécifique.                |

**Réflexe :** en cas de doute sur une cible réelle, documente le doute dans la fiche d’enquête **et** consulte avant d’agir.

## Annexe D — Modèle de fiche d’enquête

À copier dans `config/fiche-enquete.md` et à remplir avant chaque projet.

```markdown
# Fiche d’enquête

## Métadonnées
- Titre :
- Auteur :
- Date de création :
- Version :
- run_id de référence :

## Question
- Question d’enquête (1 phrase) :

## Sources envisagées
- Sources possibles :
- API officielle disponible ? (oui/non, URL, lien CGU) :
- Flux RSS / Atom disponible ? (oui/non, URL) :
- Sitemap disponible ? (oui/non, URL) :
- Open data pertinent ? (oui/non, URL, licence) :
- Scraping HTML envisagé ? (oui/non) :

## Méthode retenue
- Méthode :
- Justification (pourquoi pas une source plus propre ?) :

## Cadre
- robots.txt vérifié ? (oui/non, extraits pertinents) :
- CGU vérifiées ? (oui/non, points marquants) :
- Base légale et finalité :
- Données personnelles concernées ? (oui/non, lesquelles, minimisation appliquée) :

## Collecte
- Données minimales collectées (liste exhaustive) :
- Format de sortie attendu :
- Volume attendu :
- Délai entre requêtes :
- Plafond de volume :
- User-Agent utilisé :

## Limites et angles morts
- Angles morts identifiés :
- Risques techniques (site dynamique, anti-bot, encodage) :
- Risques éthiques :
- Doutes non levés (à documenter !) :

## Reproductibilité
- Commande exacte :
- Version Python :
- requirements.txt figé (oui/non) :
- Chemins des artefacts produits :
```

-----

# Conclusion du cours

Tu es arrivé au bout du cours. Faisons le point.

## Ce que tu sais faire maintenant

**Méthode**

- Poser les 4 questions préalables à toute collecte.
- Lire un `robots.txt` et appliquer ses contraintes.
- Choisir entre API, RSS, sitemap, open data et scraping — dans cet ordre.
- Documenter une enquête dans une fiche structurée.

**Technique**

- Faire des requêtes HTTP propres avec `requests` (timeout, User-Agent, retries).
- Parser du HTML avec BeautifulSoup (sélecteurs robustes, méthodologie Inspect → Sélecteur → Test).
- Extraire des données structurées en respectant un modèle `{données + source + horodatage + outil}`.
- Stocker en CSV, JSON, JSONL selon le cas.
- Nettoyer, normaliser, dédupliquer.
- Paginer une collecte avec deux conditions d’arrêt.
- Consommer une API REST et gérer rate limits et authentification.
- Mettre en place sessions, retries, logs, configuration externe.

**Enquête**

- Construire un veilleur basé sur des snapshots versionnés.
- Détecter les changements (ajouts / retraits / modifications).
- Produire un rapport OSINT structuré, borné à la collecte, reproductible.

**Architecture**

- Organiser un projet (`src/`, `data/`, `config/`, `logs/`, `reports/`).
- Séparer code, données, configuration, secrets.
- Documenter avec README et `.env.example`.
- Auto-évaluer son projet avec une checklist sérieuse.

## Ce que ce cours ne couvre pas (et où aller ensuite)

- **Sites réellement dynamiques** : Playwright, Selenium. À approcher **dans un cadre autorisé** uniquement.
- **Crawling à grande échelle** : Scrapy, avec middlewares, planification, pipelines.
- **Analyse de données** : pandas, visualisation, NLP.
- **Reverse engineering d’endpoints d’API non documentées** : précautions juridiques importantes.
- **Sécurité opérationnelle avancée** (VPN d’investigation, environnements isolés, persona OSINT) : sujet à part entière.
- **Aspects organisationnels** : gestion d’équipe d’analystes, partage sécurisé des données, archivage long terme.

Chacun de ces domaines vaut son propre cours. Tu as maintenant la base technique et méthodologique pour les aborder sereinement.

## Le mot de la fin

Tu as appris à collecter du web. Mais la **valeur** ne vient pas du code que tu écris : elle vient de la **question** que tu poses, et de la **rigueur** avec laquelle tu cherches la réponse.

Un mauvais analyste avec un excellent scraper produit du bruit. Un bon analyste avec un scraper modeste produit de la connaissance.

Vise toujours la deuxième catégorie.

Bonne collecte. **Et bonne enquête.**

-----

*Fin du cours.*