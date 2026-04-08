# OSINT EXPERT & CRYPTO-ACTIFS

*Investigation numérique & financière — Suivre l'argent à travers les blockchains et les juridictions*

**Cours complet — 30 chapitres • 7 parties • 7 annexes**

*OSINT avancé • Blockchain analysis • Investigation financière • OPSEC • Corrélation • Production de renseignement*

---

## Table des matières

- [Fil rouge : Opération NEXUS](#fil-rouge--opération-nexus)
- **PARTIE I — POSTURE, OPSEC ET MÉTHODOLOGIE (Ch.1-3)**
  - [Ch.1 — Posture de l'expert OSINT/Crypto](#chapitre-1--posture)
  - [Ch.2 — OPSEC opérationnelle avancée](#chapitre-2--opsec)
  - [Ch.3 — Méthodologie d'investigation avancée](#chapitre-3--méthodologie)
- **PARTIE II — OSINT FINANCIER ET CORPORATE (Ch.4-7)**
  - [Ch.4 — OSINT corporate : registres, UBO et sociétés](#chapitre-4--osint-corporate)
  - [Ch.5 — OSINT sur personnes physiques et PEP/sanctions](#chapitre-5--osint-personnes)
  - [Ch.6 — Techniques de recherche avancées](#chapitre-6--recherche-avancée)
  - [Ch.7 — SOCMINT, avatars et automatisation](#chapitre-7--socmint-et-automatisation)
- **PARTIE III — FONDAMENTAUX BLOCKCHAIN ET CRYPTO-ACTIFS (Ch.8-11)**
  - [Ch.8 — Bitcoin : le modèle UTXO et l'investigation](#chapitre-8--bitcoin)
  - [Ch.9 — Ethereum, chaînes EVM, Solana et au-delà](#chapitre-9--ethereum-et-au-delà)
  - [Ch.10 — Stablecoins : USDT, USDC et le nerf de la guerre](#chapitre-10--stablecoins)
  - [Ch.11 — Privacy coins, mixing et techniques d'évasion](#chapitre-11--privacy-et-mixing)
- **PARTIE IV — TRAÇAGE ET INVESTIGATION BLOCKCHAIN (Ch.12-16)**
  - [Ch.12 — Cluster analysis et heuristiques](#chapitre-12--clustering)
  - [Ch.13 — Traçage bout en bout](#chapitre-13--traçage)
  - [Ch.14 — Investigation DeFi : DEX, lending, bridges et NFT](#chapitre-14--defi)
  - [Ch.15 — Outils d'investigation blockchain](#chapitre-15--outils)
  - [Ch.16 — Cadre juridique, réglementaire et coopération](#chapitre-16--cadre-juridique)
- **PARTIE V — ÉCOSYSTÈME CRIMINEL ET ASSET RECOVERY (Ch.17-20)**
  - [Ch.17 — Ransomware, darknet markets et cybercriminalité](#chapitre-17--cybercriminalité)
  - [Ch.18 — Fraude crypto : rug pulls, Ponzi et scams](#chapitre-18--fraude)
  - [Ch.19 — Blanchiment crypto : placement, layering, intégration](#chapitre-19--blanchiment)
  - [Ch.20 — Asset recovery : de l'investigation à la saisie](#chapitre-20--asset-recovery)
- **PARTIE VI — CORRÉLATION, ANALYSE ET PRODUCTION (Ch.21-24)**
  - [Ch.21 — Relier une adresse blockchain à une identité](#chapitre-21--attribution)
  - [Ch.22 — Workflow intégré : OSINT + crypto + bases internes](#chapitre-22--workflow-intégré)
  - [Ch.23 — Production de renseignement](#chapitre-23--production)
  - [Ch.24 — Capitalisation, veille et formation](#chapitre-24--capitalisation)
- **PARTIE VII — CAS DE SYNTHÈSE (Ch.25-30)**
  - [Ch.25 — Cas complet : synthèse NEXUS](#chapitre-25--nexus)
  - [Ch.26 — Cas complet : traçage ransomware](#chapitre-26--cas-ransomware)
  - [Ch.27 — Cas complet : rug pull multi-chain](#chapitre-27--cas-rug-pull)
  - [Ch.28 — Cas complet : financement illicite via crowdfunding](#chapitre-28--cas-financement)
  - [Ch.29 — Cas complet : investigation Monero](#chapitre-29--cas-monero)
  - [Ch.30 — Exercice : sollicitation métier complète](#chapitre-30--exercice)
- **ANNEXES**

---

## Fil rouge : Opération NEXUS

> **Contexte narratif — ce fil rouge traverse les 24 premiers chapitres et se conclut au Ch.25.**
>
> **Sofia Kessler**, chargée de recherche en renseignement OSINT/Crypto au sein de la **Cellule de Renseignement Financier** (CRF) d'un État européen, reçoit une sollicitation du département « blanchiment et criminalité organisée ».
>
> **La sollicitation :** un réseau de blanchiment présumé opère entre la France, Chypre, Dubaï, et les blockchains Bitcoin et Ethereum. Point de départ : une Déclaration de Soupçon (DS) d'une banque française signalant des flux suspects entre le compte d'une société française (**NEXUS Consulting SARL**, Paris, capital 1 000 €, CA déclaré 2,5 M€ — incohérent) et un exchange crypto (**WireEx**, basé en Estonie). Montant cumulé : 2,3 M€ en 8 mois. Le dirigeant déclaré : **Andreï Volkov**, ressortissant letton, PEP de second rang (ancien conseiller municipal à Riga).
>
> **Ce que Sofia doit découvrir :** qui est réellement derrière NEXUS Consulting (l'UBO), quelle est la chaîne de sociétés, d'où viennent les fonds crypto et où vont-ils, le réseau utilise-t-il des protocoles DeFi, des mixers, ou des bridges, et quelle est la destination finale (cashout). L'investigation va mobiliser chaque compétence du cours — de l'OPSEC à l'asset recovery.

---

## PARTIE I — POSTURE, OPSEC ET MÉTHODOLOGIE

*Avant d'investiguer : comprendre le rôle, sécuriser l'investigation, et maîtriser la méthode.*

---

### Chapitre 1 — Posture de l'expert OSINT/Crypto en service de renseignement

#### 1.1 Rôle : référent méthode, technique et qualité

Le chargé de recherche OSINT/Crypto n'est pas un simple exécutant. C'est un expert à triple casquette. **Référent méthode :** il définit et fait évoluer les procédures d'investigation du service, forme les enquêteurs métiers, les accompagne sur les cas complexes, et garantit l'homogénéité des pratiques. **Référent technique :** il connaît l'écosystème d'outils (OSINT et crypto), évalue les solutions du marché, rédige les cahiers des charges, et maintient les capacités techniques (avatars, infrastructure, scripts). **Référent qualité et sécurité :** il garantit la rigueur analytique (niveaux de confiance, traçabilité, reproductibilité), la conformité légale, et la sécurité opérationnelle.

#### 1.2 Contexte : investigations financières

Ce poste s'inscrit dans un service de renseignement financier (TRACFIN en France, FinCEN aux US, FIU-NL aux Pays-Bas, NCA au UK) ou une unité spécialisée. Le cadre principal est la LCB-FT (Lutte contre le Blanchiment de Capitaux et le Financement du Terrorisme). L'OSINT et le traçage crypto sont des compléments essentiels aux techniques classiques d'investigation financière (réquisitions bancaires, coopération internationale via les CRF).

Les domaines d'intervention : le **blanchiment** (identifier les UBO, cartographier les montages, tracer les flux crypto — chaîne de sociétés écrans BVI → Chypre → France avec cashout BTC), la **fraude fiscale** (patrimoine dissimulé, crypto non déclarée — wallet Ethereum avec 500 K€ non déclaré identifié via ENS + OSINT), le **financement du terrorisme** (flux crypto vers zones sensibles, campagnes de crowdfunding), la **corruption** (due diligence PEP, liens d'intérêts, patrimoine incohérent), et la **cybercriminalité financière** (paiements ransomware tracés jusqu'au cashout).

#### 1.3 Produits attendus

La **note d'analyse** (réponse structurée à une sollicitation — faits, inférences, lacunes, confiance), le **rapport d'investigation crypto** (traçage complet — adresses, transactions, clustering, exchanges, identification, graphe de flux), la **fiche capacitaire** (documentation d'un outil, d'une méthode, ou d'un espace numérique), le **cahier des charges** (spécifications pour acquisition d'un outil), la **veille technologique** (synthèse des évolutions), et le **support de formation** (sensibilisation des enquêteurs métier).

#### 1.4 Fil rouge — NEXUS : la sollicitation

> **🔍 NEXUS — Épisode 1**
>
> Sofia reçoit la sollicitation : « Identifier les bénéficiaires effectifs de NEXUS Consulting SARL, cartographier le réseau de sociétés liées, et tracer les flux crypto associés au compte WireEx. Périmètre : France, Chypre, Lettonie, Dubaï, blockchains BTC et ETH. Délai : 3 semaines. Classification : TLP:AMBER. »
>
> Sofia formule 4 questions de renseignement : QR1 — qui est le bénéficiaire effectif réel de NEXUS ? QR2 — quel est le réseau de sociétés et la structure capitalistique ? QR3 — d'où viennent les fonds crypto et où vont-ils ? QR4 — le schéma est-il compatible avec du blanchiment organisé ?

---

### Chapitre 2 — OPSEC opérationnelle avancée

#### 2.1 Threat model

L'OPSEC doit être calibrée sur le threat model. Dans un service de renseignement financier, les menaces sont plus élevées que pour un consultant privé. La **criminalité organisée** dispose de capacités de contre-surveillance numérique (monitoring des consultations de registres, détection de profils LinkedIn qui visitent leurs pages), de corruption potentielle, et de risque de violence physique — impact si compromission : compromission de l'enquête, risque pour l'agent, destruction de preuves. La **menace interne** (fuite, compromission d'un collègue) est gérée par le cloisonnement. Les **services étrangers** (espionnage, ingérence) sont une menace dans les enquêtes à dimension géopolitique.

#### 2.2 Infrastructure d'investigation

Chaque investigation a son environnement dédié. **VM dédiée** par enquête (Whonix pour l'anonymat réseau, ou VM cloisonnée avec VPN dédié — snapshot initial, pas de rémanence entre enquêtes). **VPN non-corporate** (le VPN du service est lié à l'organisation — utiliser un VPN commercial dédié à l'OSINT, jamais le même que le VPN de bureau). **Navigateur** profil vierge (pas de cookies, pas de sessions personnelles, pas de comptes connectés). **DNS chiffré** (DoH ou DoT — les requêtes DNS en clair révèlent les domaines investigués). **Stockage chiffré** (les données d'enquête sont sensibles — chiffrement au repos obligatoire).

#### 2.3 Gestion des avatars

Chaque avatar a une **légende complète** résistant à un contrôle OSINT (nom cohérent avec la nationalité, photo IA non détectable en reverse image search — vérifier avec TinEye/Google Images, biographie plausible avec parcours professionnel et centres d'intérêt, historique de publications cohérent). L'**infrastructure** est totalement cloisonnée (une VM par avatar, un VPN par avatar, un email par avatar, un numéro de téléphone par avatar — zéro lien avec l'identité réelle). La **maturation** est indispensable (un avatar créé le jour de l'investigation est détectable — publications pendant plusieurs semaines, suivi de comptes cohérents, interactions avec du contenu du secteur). Le **registre interne** documente chaque avatar (date de création, légende, infrastructure, enquêtes associées, date de destruction). La **destruction** après usage est propre (suppression des comptes, purge de la VM, mise à jour du registre).

#### 2.4 Empreinte comportementale

Les plateformes détectent les comportements d'investigation. Le **browser fingerprint** (résolution, polices, extensions, WebGL renderer, timezone — utiliser des profils navigateur aléatoires ou un outil anti-fingerprint comme Multilogin). Les **empreintes comportementales** (vitesse de scroll, mouvements de souris, durée de session — un comportement trop « mécanique » déclenche des alertes). Le **presse-papiers** (le copier-coller peut être lu par JavaScript — vider entre les sessions). Les **métadonnées** des fichiers créés (rapports, screenshots, PDF contiennent auteur, machine, date — nettoyer systématiquement avec ExifTool ou mat2 avant toute diffusion).

---

### Chapitre 3 — Méthodologie d'investigation avancée

#### 3.1 Le cycle du renseignement adapté

Chaque investigation suit un cycle structuré. **Réception** (le département métier formule sa demande). **Cadrage** (reformuler en questions précises, définir le périmètre — quelles entités, quelles juridictions, quelles blockchains — les sources à consulter, le délai). **Collection** (interroger les sources — registres, OSINT technique, réseaux sociaux, bases internes, dark web, blockchain). **Traitement** (nettoyer, normaliser, dédupliquer les données collectées). **Corrélation** (croiser les découvertes OSINT avec les bases internes et les données blockchain). **Analyse** (formuler des conclusions avec niveaux de confiance, identifier les lacunes). **Production** (rédiger la note d'analyse ou le rapport d'investigation). **Feedback** (le métier confirme si la réponse est suffisante ou si un approfondissement est nécessaire).

#### 3.2 Investigations multi-entités, multi-juridictions

Les enquêtes financières impliquent souvent des chaînes de sociétés dans plusieurs pays. Les **sociétés écrans** (shell companies) sont des structures sans activité réelle, créées pour opacifier la propriété — juridictions typiques : BVI, Panama, Seychelles, Delaware. Les **prête-noms** (nominees) prêtent leur nom comme dirigeants ou actionnaires — red flag : même personne dirige 50+ sociétés (vérifiable sur OpenCorporates). Les **chaînes de participation** (A → B → C → D dans différents pays — chaque maillon est une juridiction à investiguer). Les **trusts et fondations** séparent propriété légale et bénéficiaire — très opaques dans certaines juridictions.

#### 3.3 Entity resolution et pivoting

L'entity resolution détermine si deux entrées différentes désignent la même entité — le défi central de l'investigation multi-sources. Les variantes (translitération cyrillique/arabe/chinois, erreurs typographiques, alias, noms d'usage), les homonymes (distinguer deux « Jean Dupont » avec des attributs incomplets), et la méthode (croiser minimum 2 attributs indépendants — nom + date de naissance, nom + adresse, email + téléphone — avant de conclure à une correspondance ; documenter le raisonnement). Outils : fuzzy matching (rapidfuzz, Jaro-Winkler distance), dédoublonnage dans pandas, entity resolution dans Maltego.

#### 3.4 Data quality

Des données de mauvaise qualité produisent de mauvaises analyses. Nettoyage (supprimer doublons, corriger formats — pandas, OpenRefine), normalisation (format unique : noms NOM Prénom, dates ISO 8601, adresses structurées), déduplication (identifier les entrées désignant la même entité — rapidfuzz, dedupe), enrichissement (ajouter des attributs via APIs — Shodan, VirusTotal, OpenCorporates), et validation (vérifier la cohérence interne des données).

---

## PARTIE II — OSINT FINANCIER ET CORPORATE

*L'investigation financière en sources ouvertes — registres, sociétés, patrimoine, sanctions.*

---

### Chapitre 4 — OSINT corporate : registres, UBO et investigation de sociétés

#### 4.1 Registres d'entreprises par juridiction

Chaque pays a son registre — l'accès, le contenu, et la transparence varient énormément. **France** : Infogreffe (comptes, statuts), Pappers (gratuit, excellent pour débuter), Bodacc (publications légales), INPI (marques, brevets, registre UBO — accès restreint aux autorités). **UK** : Companies House (gratuit, très complet — dirigeants, comptes, filing history, PSC Register pour les UBO — le gold standard de la transparence). **USA** : SEC EDGAR (sociétés cotées — filings, rapports annuels, gratuit), State registries (LLC/Corp par État — variable). **Luxembourg** : LBR (payant, registre UBO accès restreint). **Suisse** : Zefix + registres cantonaux (gratuit, pas de registre UBO public). **Chypre** : DRCOR (partiellement en ligne). **BVI/Seychelles/Panama** : registres très opaques, souvent inaccessibles → les données viennent des fuites (ICIJ Offshore Leaks). **Multi-pays** : OpenCorporates (agrégateur gratuit/partiel), Orbis/BvD (payant, le plus complet pour les chaînes de participation internationales).

#### 4.2 Workflow d'investigation corporate

Identifier la société dans le registre local (SIREN, Company Number, EIN) → extraire dirigeants, actionnaires, adresse, capital, objet social, date de création. Filiales et participations : rapports annuels, Orbis, ICIJ Offshore Leaks. Identifier le UBO : registre si disponible, sinon OSINT (rapports annuels, presse, leaks, réseaux sociaux des dirigeants). Screening des dirigeants et UBO : PEP ? Sanctions ? Contentieux ? Liens avec d'autres structures suspectes ? Analyse financière : bilans, CA, résultat — cohérence entre l'activité déclarée et les chiffres (un capital de 1 000 € avec un CA de 2,5 M€ est un signal d'alerte). OSINT technique : domaine web, DNS, certificats (crt.sh), emails exposés. Cartographier le réseau : graphe de liens (Maltego, Obsidian, yEd).

#### 4.3 Montages financiers opaques

La **société écran** (entité sans activité réelle — red flags : pas de site web, pas d'employés LinkedIn, adresse de domiciliation, capital minimum). Le **trust** (séparation propriété légale / bénéficiaire — opacité totale dans certaines juridictions). Le **nominee director** (tiers prêtant son nom — même personne dirige 50+ sociétés). Le **layering/cascade** (chaîne A→B→C→D dans différents pays — pas de logique économique, juridictions opaques). Le **round-tripping** (argent envoyé offshore puis réinjecté comme investissement étranger — flux circulaires, mêmes montants, mêmes dates). Le **trade-based laundering** (surfacturation/sous-facturation de biens — prix incohérents avec le marché).

#### 4.4 Fil rouge — NEXUS : l'investigation corporate

> **🔍 NEXUS — Épisode 2**
>
> Sofia interroge Pappers : NEXUS Consulting SARL, capital 1 000 €, créée il y a 2 ans, gérant Andreï Volkov, adresse de domiciliation dans le 8ème arrondissement de Paris (société de domiciliation — red flag #1). CA déclaré 2,5 M€ pour une société de « conseil en stratégie » avec 0 employé LinkedIn (red flag #2). Sofia pivote vers la Lettonie (Lursoft) : Volkov est dirigeant de 2 sociétés lettones inactives. Puis vers Chypre (DRCOR) : une société OMEGA HOLDINGS LTD avec Volkov comme directeur et un actionnaire chypriote (probablement nominee). L'OSINT technique sur le domaine nexus-consulting.fr révèle un certificat SSL avec un SAN incluant omega-holdings.com.cy — le lien technique entre les deux sociétés est confirmé.

---

### Chapitre 5 — OSINT sur personnes physiques et PEP/sanctions

L'investigation sur personnes physiques opère dans un cadre légal strict (base légale documentée, proportionnalité, RGPD — seules les données pertinentes pour l'enquête sont collectées). Le **patrimoine** (registres immobiliers — Patrim en France, Land Registry UK ; véhicules, bateaux, avions — registres aéronautiques). Les **mandats sociaux** (dirigeant de quelles sociétés — OpenCorporates, registres nationaux ; révèle le réseau d'intérêts et les liens entre entités). Les **réseaux sociaux** (LinkedIn — parcours pro, réseau, recommandations ; Twitter/X — opinions, activité ; Instagram — train de vie incohérent avec les revenus déclarés ; Telegram — groupes, channels).

Le **screening sanctions et PEP** : OFAC SDN List (la plus impactante — extraterritorialité US, inclut des adresses crypto spécifiques), EU Sanctions Map (mesures restrictives par régime/pays), ONU Consolidated List (Conseil de Sécurité), UK OFSI (post-Brexit), OpenSanctions (agrégateur open source — sanctions + PEP + listes nationales), World-Check/Refinitiv et Dow Jones (commerciaux, PEP + adverse media). Les **leaks et investigations journalistiques** : ICIJ Offshore Leaks (Panama Papers, Pandora Papers, Paradise Papers — recherche par nom/société), OCCRP (criminalité organisée et corruption).

Fil rouge : Sofia screene Volkov — PEP de second rang confirmé (conseiller municipal Riga 2012-2016), présent dans les Pandora Papers (lien avec un trust chypriote via OMEGA HOLDINGS), aucune sanction, mais 1 contentieux commercial en Lettonie (créance impayée).

---

### Chapitre 6 — Techniques de recherche avancées

Les **Google Dorks** de niveau expert (documents financiers : site:target.com filetype:pdf "rapport annuel" ; organigrammes : filetype:xlsx "email" ; documents internes exposés : filetype:pptx "confidentiel" ; mentions dans des PDF officiels : "Viktor Petrov" filetype:pdf site:gov.* ; recherche temporelle : after:2023-01-01 before:2024-12-31 ; directory listing : intitle:"index of" site:target.com). La **recherche multi-langues** (translitération cyrillique — Сергей Иванов = Sergey/Sergei/Sergeï Ivanov ; arabe — aucun standard unique, tester toutes les variantes ; chinois — pinyin + caractères ; construction de matrice de variantes systématique ; moteurs locaux — Yandex pour l'index russophone, Baidu pour le chinois).

Le **deep web et les bases spécialisées** (bases judiciaires — Legifrance, PACER US ; bases immobilières ; archives web — Wayback Machine pour voir les versions passées d'un site ; bases d'appels d'offres ; bases de brevets). L'**OSINT technique** appliquée à l'investigation financière (Whois, DNS — les enregistrements d'un domaine révèlent l'hébergeur, les emails associés, et les autres domaines du même propriétaire ; crt.sh — les certificats SSL révèlent les SAN et les liens entre domaines ; Shodan/Censys — infrastructure exposée ; la corrélation technique — même IP ou même certificat pour 2 domaines = même propriétaire probable).

---

### Chapitre 7 — SOCMINT, avatars et automatisation pour l'investigation

*Ce chapitre couvre 3 blocs complémentaires mais distincts — chacun est une compétence à part entière.*

#### 7.1 SOCMINT — Social Media Intelligence

L'analyse de réseau social pour l'investigation financière. L'**analyse structurelle** (qui suit qui, qui interagit avec qui — les connexions LinkedIn d'un suspect révèlent son réseau professionnel, ses partenaires commerciaux, et ses associés). L'**analyse de contenu** (publications, check-ins, photos — le train de vie incohérent avec les revenus déclarés est un signal d'alerte classique en investigation financière ; les photos Instagram de montres de luxe et de voyages quand le suspect déclare 30 K€/an). L'**analyse temporelle** (quand le suspect publie, quand les transactions crypto ont lieu — une corrélation temporelle entre un post forum et une transaction 5 min après = même acteur probable). La cartographie relationnelle (visualisation du réseau en graphe — Maltego, Gephi, yEd — les nœuds centraux sont les acteurs clés, les liens périphériques révèlent les complices).

#### 7.2 Avatars opérationnels

La maturation d'un profil LinkedIn crédible dans le secteur financier pour observer les connexions du suspect — sans interaction directe (l'observation est légale, l'approche sous fausse identité pose des questions légales et éthiques selon les juridictions). Le profil doit être cohérent (parcours plausible, photo crédible, publications régulières dans le domaine, connexions organiques). Rappel : LinkedIn notifie les visites de profil — ne JAMAIS accéder connecté à un vrai profil pendant une investigation. Utiliser un avatar mature ou le mode déconnecté (recherche Google site:linkedin.com).

#### 7.3 Automatisation et data science pour l'investigation

L'automatisation comme multiplicateur de force pour l'investigateur — pas un substitut au raisonnement, un accélérateur. **Python — requests** pour interroger les APIs (OpenCorporates, Shodan, VirusTotal, explorateurs blockchain — Etherscan API). **pandas** pour le traitement de données (nettoyage, normalisation, dédoublonnage, jointures — transformer un export CSV de transactions en tableau analysable). **networkx** pour les graphes de relations (construire le graphe de liens entre les entités découvertes — visualiser les connexions, identifier les nœuds centraux, détecter les clusters). **fuzzy matching** (rapidfuzz, Jaro-Winkler) pour l'entity resolution automatisée (trouver les correspondances approximatives entre les noms dans différentes bases). Le **scraping structuré éthique** (Scrapy, Beautiful Soup — automatiser la collecte de registres publics, surveiller les changements de dirigeants, monitorer les dépôts de brevets — dans le cadre légal et les CGU). Le NLP basique (extraction d'entités nommées — spaCy — pour identifier automatiquement les noms, organisations, et lieux dans un corpus de documents).

---

## PARTIE III — FONDAMENTAUX BLOCKCHAIN ET CRYPTO-ACTIFS

*Les concepts techniques que l'investigateur doit maîtriser — pas un cours de développement blockchain mais les fondamentaux pour tracer efficacement.*

---

### Chapitre 8 — Bitcoin : le modèle UTXO et l'investigation

#### 8.1 Le modèle UTXO

Bitcoin n'a pas de « solde de compte ». Il fonctionne avec des **UTXO** (Unspent Transaction Outputs) — des « billets » numériques de montants variés. Quand Alice veut envoyer 0,5 BTC à Bob, elle dépense un UTXO de 1 BTC : 0,5 va à Bob (output 1), 0,5 revient à Alice comme « monnaie » (output 2 — la change address). La transaction consomme des inputs (UTXO existants) et crée des outputs (nouveaux UTXO). Ce modèle est fondamental pour le clustering (Ch.12) : si une transaction a 2 inputs d'adresses différentes, le signataire détient les clés privées des deux → elles appartiennent au même wallet.

#### 8.2 Les adresses Bitcoin

Legacy (1... — P2PKH), SegWit compatible (3... — P2SH-P2WPKH), SegWit natif (bc1q... — P2WPKH), et Taproot (bc1p... — P2TR). L'investigateur doit reconnaître les types : le passage d'un type à un autre dans les outputs d'une même transaction est un indice pour la change detection (la change address est souvent d'un type différent des outputs « réels »).

#### 8.3 Anatomie d'une transaction

Les **inputs** (d'où viennent les fonds — référence à un UTXO précédent), les **outputs** (où vont les fonds — adresse de destination + montant), la **change address** (monnaie rendue à l'expéditeur), les **frais** (différence entre inputs et outputs — payés au mineur), et le **timestamp** (horodatage du bloc = moment de la confirmation). L'**analyse des frais** : des frais très élevés peuvent indiquer une urgence (transfert en panique) ou une erreur (souvent documentée et discutée publiquement).

#### 8.4 Lecture d'un explorateur

Blockchain.com (simple, clair, bon pour débuter), OXT.me (visualisation avancée, clustering natif, graphes de transactions — l'outil open source de référence pour les investigateurs Bitcoin), Blockchair (multi-chain, requêtes SQL-like). Ce que l'investigateur lit : le solde actuel, le nombre total de transactions, la première et la dernière transaction (ancienneté du wallet), les montants (petits montants réguliers = usage courant ; gros montants ponctuels = consolidation ou transfert), et les services identifiés (les outils commerciaux labelisent les adresses d'exchanges, de mixers, de darknet markets).

#### 8.5 Fil rouge — NEXUS : les premiers BTC

> **🔍 NEXUS — Épisode 3**
>
> Sofia identifie l'adresse Bitcoin associée au compte WireEx de NEXUS Consulting (fournie dans la DS de la banque). Exploration sur OXT.me : 127 transactions sur 8 mois, volume cumulé de 42 BTC (≈ 2,3 M€ au taux moyen), première transaction il y a 9 mois, pattern de consolidation régulier (petits dépôts → gros retraits). Les retraits convergent vers 3 adresses qui semblent liées (même type bc1q, timing cohérent).

---

### Chapitre 9 — Ethereum, chaînes EVM, Solana et au-delà

#### 9.1 Le modèle de comptes Ethereum

Contrairement à Bitcoin (UTXO), Ethereum utilise un modèle de **comptes** avec solde. Deux types : **EOA** (Externally Owned Account — contrôlé par une clé privée, possédé par une personne ou une entité) et **Contract Account** (contrôlé par le code du smart contract — les protocoles DeFi, les tokens, les NFT sont des contrats). Les transactions Ethereum : from (expéditeur), to (destinataire — une adresse EOA ou un contrat), value (montant en ETH), gas (coût computationnel), et **input data** (les appels de fonctions smart contract sont dans l'input data — c'est là que se trouvent les interactions DeFi).

#### 9.2 Tokens et events

Les **tokens ERC-20** (tokens fongibles — USDT, USDC, DAI, WETH) sont des smart contracts qui émettent des **Transfer events** dans les logs. Ces events sont la trace du mouvement des tokens — chaque transfert de USDT est enregistré dans les logs du contrat USDT, traçable sur Etherscan. Les **tokens ERC-721** (NFT — chaque token est unique, les transfers sont traçables de la même manière). La lecture d'**Etherscan** : transactions (flux ETH), internal transactions (appels entre contrats — souvent invisibles dans les explorateurs basiques mais essentiels pour le traçage DeFi), token transfers (mouvements de tokens ERC-20), et event logs (la source la plus riche — chaque interaction avec un smart contract génère des events loggés).

#### 9.3 Les chaînes EVM compatibles

BSC/BNB Chain, Polygon, Arbitrum, Optimism, Avalanche, Base — même modèle qu'Ethereum (comptes, EVM, smart contracts, tokens ERC-20), mêmes outils d'investigation (BscScan, PolygonScan — même interface qu'Etherscan), mêmes patterns. La différence : les frais sont beaucoup plus bas → les criminels utilisent ces chaînes pour le layering à moindre coût. Le traçage est identique — un swap sur PancakeSwap (BSC) se trace comme un swap sur Uniswap (Ethereum).

#### 9.4 Solana et les chaînes non-EVM

**Solana** utilise un modèle hybride (comptes + programmes au lieu de smart contracts, SPL tokens au lieu d'ERC-20). L'écosystème Solana est devenu un terrain de forte activité retail et de fraude (meme coins, rug pulls, pump and dump — souvent plus rapides et moins chers que sur Ethereum). L'investigation Solana utilise **Solscan** et **Solana Explorer**. Les spécificités : les adresses sont en base58 (pas en hex comme Ethereum), les programmes (smart contracts Solana) ont une structure différente, et l'écosystème DeFi Solana (Raydium, Jupiter, Orca) a ses propres patterns.

Les **autres chaînes non-EVM** à connaître : **TRON** (TRC-20 — véhicule dominant pour USDT, traçable via Tronscan — traité en détail au Ch.10), **Cosmos** (écosystème de blockchains interconnectées via IBC — Inter-Blockchain Communication), **TON** (The Open Network — lié à Telegram, adoption croissante pour les paiements crypto via Telegram), et **Ripple/XRP** (paiements transfrontaliers, utilisé par certaines institutions financières).

La logique d'investigation pour une chaîne inconnue : identifier l'explorateur officiel, comprendre le modèle (UTXO vs compte), identifier le format des adresses, et vérifier si les outils commerciaux (Chainalysis, TRM Labs) couvrent cette chaîne. La couverture des outils commerciaux est le facteur limitant — les chaînes non couvertes nécessitent une investigation manuelle via les explorateurs.

#### 9.5 Fil rouge — NEXUS : le wallet Ethereum

> **🔍 NEXUS — Épisode 4**
>
> Sofia découvre qu'une partie des BTC retirés de WireEx a été convertie en ETH sur un exchange secondaire. Le wallet Ethereum (0x7a3b...) interagit avec Uniswap (swap ETH → USDT), puis un bridge vers Polygon, puis un transfert USDT vers TRON. Le pattern est celui d'un layering multi-chain classique. Sofia note que l'adresse Ethereum est liée à un ENS : a.volkov.eth — une erreur OPSEC majeure du suspect.

---

### Chapitre 10 — Stablecoins : USDT, USDC et le nerf de la guerre

*Les stablecoins sont devenus le véhicule dominant du blanchiment crypto — comprendre leur fonctionnement et leur traçabilité est une compétence critique.*

#### 10.1 Qu'est-ce qu'un stablecoin

Un token indexé sur une monnaie fiat (1 USDT ≈ 1 USD). Les principaux : **USDT/Tether** (le plus utilisé, multi-chain — Ethereum, TRON, BSC, Solana — émetteur centralisé basé aux BVI, le plus gros volume de transactions crypto au monde), **USDC/Circle** (le plus régulé, émetteur US, Ethereum + multi-chain), **DAI** (décentralisé, collatéralisé par des crypto-actifs, Ethereum — pas d'émetteur centralisé, pas de gel possible).

#### 10.2 Pourquoi les stablecoins dominent le blanchiment

Pas de **volatilité** (les criminels ne veulent pas perdre 30 % en une journée — le BTC fluctue, l'USDT non). **Liquidité massive** (paires de trading universelles sur tous les exchanges et DEX). **TRON + USDT** : frais quasi nuls, transactions rapides — c'est devenu le rail de paiement dominant pour le blanchiment en Asie (OTC desks, P2P, mules). Et les **stablecoins sont universellement acceptés** (tout exchange, tout DEX, tout OTC desk accepte l'USDT).

#### 10.3 Traçabilité et gel

Le traçage des stablecoins suit le même principe que les tokens ERC-20/TRC-20 — les Transfer events sont dans les logs du smart contract. La spécificité : les émetteurs centralisés **Tether et Circle peuvent geler des adresses** — c'est un levier d'enquête puissant. Tether a gelé des centaines de millions en USDT liés à des activités illicites sur demande des autorités. L'OFAC sanctionne des adresses USDT/USDC spécifiques (adresses Lazarus, Tornado Cash). Les exchanges conformés (Binance, Coinbase, Kraken) bloquent les transactions vers/depuis les adresses sanctionnées.

#### 10.4 Investigation TRON

Tronscan est l'explorateur de référence pour TRON. Les patterns de blanchiment sur TRON : micro-transactions USDT en grand volume (centaines de petits transferts → consolidation → OTC desk), OTC desks asiatiques (conversion USDT → CNY, souvent liés à des réseaux criminels — pig butchering, fraude), et cashout via plateformes P2P (Paxful, LocalBitcoins — maintenant fermé, remplacé par Bisq et alternatives). Fil rouge : les USDT de NEXUS transitent par TRON vers un OTC desk chinois (Fengshui Trading — 12 adresses de distribution).

---

### Chapitre 11 — Privacy coins, mixing et techniques d'évasion

#### 11.1 Les privacy coins

**Monero** (XMR) est la privacy coin de référence — ring signatures (chaque transaction inclut des « leurres » qui masquent le vrai expéditeur), stealth addresses (chaque transaction crée une adresse unique pour le destinataire), et RingCT (les montants sont chiffrés). Résultat : quasi intraçable on-chain. La **stratégie d'investigation Monero** ne repose pas sur le traçage on-chain (impossible en pratique) mais sur les points périphériques : les conversions BTC/ETH → XMR via un exchange KYC (réquisition pour identifier le compte), les erreurs OPSEC (adresse XMR publiée sur un forum, même username sur un forum et un exchange, IP leak via un nœud Monero), les entrées/sorties de Monero (les fonds viennent de quelque part et repartent quelque part — les points de conversion sont traçables), et l'OSINT classique sur l'individu. Le traçage Monero pur est un défi, mais l'investigation ne se limite jamais à la blockchain.

**Zcash** (ZEC) offre des shielded transactions optionnelles — en pratique, beaucoup de transactions restent transparentes (les utilisateurs n'activent pas le shielding), ce qui rend une partie du réseau traçable. **Dash** a un mixing optionnel (PrivateSend) mais est moins privé que revendiqué.

#### 11.2 Les mixers et tumblers

Les **mixers centralisés** reçoivent les crypto d'un utilisateur et renvoient des crypto « propres » (d'un autre utilisateur) — en déclin car saisis par les autorités. Le **CoinJoin décentralisé** (Wasabi Wallet, Samourai Wallet — saisi en 2024) combine les inputs de plusieurs utilisateurs dans une même transaction pour casser l'heuristique common-input — chaque participant apporte ses fonds et reçoit le même montant sur une nouvelle adresse, mais l'observateur ne peut pas savoir quel input correspond à quel output. **Tornado Cash** (mixer Ethereum via smart contract, sanctionné OFAC en août 2022) fonctionne avec des dépôts à montant fixe (0.1/1/10/100 ETH) — le pattern est détectable (montant fixe, délai d'attente, retrait depuis une adresse vierge). Le **chain hopping** (BTC → XMR → BTC, ou ETH → BSC via bridge) change de blockchain pour compliquer le traçage. Les **peel chains** (petits montants envoyés séquentiellement depuis un wallet central, le reste revient — pattern de « pelage » récurrent et détectable).

**Détection :** les outils commerciaux identifient les adresses de mixers connus et les patterns de mixing. Un flux qui passe par un mixer identifié est flaggé — cela ne casse pas le traçage en amont, mais complique le traçage en aval.

---

## PARTIE IV — TRAÇAGE ET INVESTIGATION BLOCKCHAIN

*Le cœur opérationnel — les techniques pour suivre les fonds d'un point de départ à un point d'arrivée.*

**Discipline analytique transversale à cette partie :** le risque de sur-attribution est le piège principal de l'investigation blockchain. Une adresse qui reçoit des fonds d'un mixer n'est pas nécessairement criminelle (le mixer est aussi utilisé pour la confidentialité légitime). Un wallet qui interagit avec un exchange n'appartient pas forcément à l'exchange (c'est peut-être un hot wallet de transit). Chaque conclusion doit porter un **niveau de confiance explicite** : fait observé (l'adresse X a reçu 5 BTC de l'adresse Y — observable, vérifiable), inférence probable (les adresses X et Z appartiennent au même wallet — clustering, confiance haute si common-input), inférence possible (le wallet appartient à un utilisateur de l'exchange W — attribution outil commercial, confiance modérée), hypothèse (le propriétaire du wallet est le suspect V — requiert une corrélation OSINT, confiance variable). Ne JAMAIS présenter une inférence comme un fait.

---

### Chapitre 12 — Cluster analysis et heuristiques d'investigation

#### 12.1 Heuristiques Bitcoin

Le **common-input ownership** : si 2 adresses sont inputs d'une même transaction, il faut posséder les clés privées des deux pour signer → elles appartiennent au même wallet. Fiabilité : haute — cassée uniquement par CoinJoin (qui mélange délibérément les inputs de plusieurs utilisateurs). Le **change detection** : quand on envoie 0,5 BTC depuis un UTXO de 1 BTC, 0,5 revient à une change address identifiable par des indices (montant rond envoyé, nouveau type d'adresse en sortie, première apparition de l'adresse). Fiabilité : moyenne — les heuristiques ne sont pas infaillibles. Le **peel chain** : pattern de distribution séquentielle (un wallet central envoie de petits montants à des adresses successives, le reste revient au wallet → une chaîne de « pelures »). Le **behavioral clustering** (même pattern de timing, de montants, de destinations → les habitudes persistent). L'**exchange identification** (taille du cluster, patterns hot/cold wallets — les outils commerciaux maintiennent des bases d'attribution massives).

#### 12.2 Clustering Ethereum

Différent d'UTXO : pas de common-input ni de change address (le modèle de comptes n'a pas ces concepts). Le clustering Ethereum repose sur l'analyse des **interactions avec les smart contracts** (mêmes protocoles DeFi utilisés, mêmes tokens échangés), les **patterns de gas price** (certains wallets utilisent un gas price caractéristique), les **internal transactions** (appels entre contrats qui lient des adresses), et les **token transfers** (le même token transféré entre des adresses liées).

#### 12.3 Limites analytiques du clustering

Le clustering n'est pas infaillible. Le CoinJoin casse le common-input. La change detection est heuristique et peut être fausse. L'attribution des outils commerciaux repose sur des données propriétaires non vérifiables. Et un cluster « exchange » peut contenir des milliers d'utilisateurs — l'adresse de dépôt d'un exchange n'identifie pas l'utilisateur sans réquisition. **Règle :** documenter la méthode de clustering utilisée, le niveau de confiance de chaque regroupement, et les limites connues.

---

### Chapitre 13 — Traçage bout en bout : du point de départ au rapport

Le workflow complet. **Point de départ** (adresse connue — paiement ransomware, wallet dark market, signalée dans une DS, identifiée via OSINT). **Exploration** (historique complet — première transaction, volume total, patterns d'activité, solde actuel, services identifiés). **Clustering** (regrouper les adresses du même wallet — méthodes Ch.12). **Suivi des hops** (transaction par transaction, documenter montants et adresses ; attention aux splits — un montant divisé en plusieurs destinations — et aux merges — plusieurs sources consolidées vers une seule adresse). **Identification des services** (quand les fonds arrivent sur un exchange, mixer, DEX, bridge = point d'ancrage — l'attribution est faite par les outils commerciaux ou par OSINT). **Corrélation OSINT** (relier adresses/services à des identités — Ch.21). **Rapport** (graphe de flux annoté, tableau d'adresses avec clustering et attribution, timeline, conclusions, niveaux de confiance pour chaque attribution).

Le **traçage multi-chain** : les fonds traversent les bridges (dépôt sur chaîne source + retrait sur chaîne destination, corrélables par montant, timing, et contrat du bridge utilisé). Les outils multi-chain (TRM Labs, Chainalysis) suivent les flux cross-chain — en open source, la corrélation manuelle est possible mais laborieuse.

**Documentation :** chaque hop est documenté (adresse source, adresse destination, montant, txid, timestamp, service identifié le cas échéant, et niveau de confiance de l'attribution).

---

### Chapitre 14 — Investigation DeFi : DEX, lending, bridges et NFT

*La DeFi est devenue le terrain de prédilection du layering — chaque protocole est un vecteur d'opacification avec ses techniques de traçage spécifiques.*

Les **DEX** (Uniswap, PancakeSwap, SushiSwap, Jupiter/Raydium sur Solana) : les swaps sont enregistrés dans les event logs du smart contract (Swap events sur Etherscan) → traçables. Pas de KYC, mais la traçabilité on-chain est intacte — un swap ETH → USDT est visible dans les logs du pool de liquidité. Le **lending** (Aave, Compound) : dépôt de collatéral + emprunt → stratégie de layering (déposer des ETH « sales », emprunter des USDC « propres » — les deux opérations sont traçables dans les logs du contrat mais la séparation collatéral/emprunt complique l'attribution). Les **bridges** (transfert de valeur entre blockchains — le point de pivot critique dans le traçage multi-chain ; corrélation : montant, timing, contrat utilisé). Les **NFT et wash trading** (vente fictive à soi-même pour gonfler le prix → blanchiment par l'art numérique ; détectable par analyse du graphe — même wallet achète et vend). Le **yield farming** (apport de liquidité dans un pool → retrait depuis un autre wallet — technique de layering avancée). Fil rouge : Sofia identifie que le réseau NEXUS utilise Aave pour le layering (dépôt ETH → emprunt USDC → bridge vers Polygon → USDT sur TRON).

---

### Chapitre 15 — Outils d'investigation blockchain

Les **explorateurs** : Blockchain.com (Bitcoin simple), OXT.me (Bitcoin avancé — clustering natif, graphes), Blockchair (multi-chain, requêtes), Etherscan (référence Ethereum — transactions, internal txs, token transfers, event logs, contract source), BscScan/PolygonScan (chaînes EVM), Tronscan (TRON/USDT), Solscan (Solana). Les **outils commerciaux** : Chainalysis Reactor (leader mondial — clustering massif, attribution, utilisé par la majorité des LEA et CRF), Elliptic (multi-chain, compliance), Crystal Blockchain (scoring de risque, interface intuitive), TRM Labs (25+ chains, cross-chain, agences US), Arkham Intelligence (attribution communautaire d'adresses — modèle innovant). Les **outils open source** : Breadcrumbs.app (tracing visuel gratuit — bon pour débuter, limité en volume), WalletExplorer (clustering Bitcoin), GraphSense (académique — AIT Vienna), Orbit (OSINT Ethereum), Maltego transforms blockchain (pivots entre adresses/transactions/entités), Chainalysis Sanctions Oracle (screening gratuit — vérifier si une adresse est sanctionnée OFAC).

Le **choix d'outil** : investigation judiciaire/renseignement → Chainalysis/TRM (attribution et clustering massifs, admissibilité) ; compliance → Elliptic/Crystal (scoring de risque automatisé) ; recherche initiale → Breadcrumbs + explorateurs ; screening rapide → Sanctions Oracle.

---

### Chapitre 16 — Cadre juridique, réglementaire et coopération internationale

**MiCA** (Markets in Crypto-Assets — règlement UE 2024) : obligation de travel rule pour les VASP (Virtual Asset Service Providers), enregistrement, compliance AML, supervision. La **travel rule** (obligation de transmettre les informations expéditeur/destinataire entre VASP pour les transferts > 1 000 € — impact : les VASP régulés connaissent l'identité des deux parties). **FATF/GAFI** (recommandations internationales AML/CFT appliquées aux crypto — les « Red Flag Indicators » pour les VASP sont un outil d'analyse). La **régulation par juridiction** (les exchanges KYC-friendly — Binance, Coinbase, Kraken — coopèrent avec les autorités ; les zones grises — exchanges offshore sans KYC réel, DEX décentralisés — pas d'entité à réquisitionner ; les OTC desks — souvent non régulés, point de cashout critique).

La **coopération internationale** : MLA (Mutual Legal Assistance — réquisitions pour les exchanges étrangers, processus lent — mois), Europol/IACCC (Internet and Crypto Crimes Center — coordination européenne), réseau Egmont des CRF (échange de renseignement financier entre CRF — canal plus rapide que la MLA). Les **réquisitions judiciaires** (obtenir les données KYC d'un exchange — les grands exchanges ont des équipes LEA dédiées ; les données incluent : identité vérifiée, adresses de dépôt/retrait, historique de transactions, IP de connexion, appareils utilisés).

---

## PARTIE V — ÉCOSYSTÈME CRIMINEL CRYPTO ET ASSET RECOVERY

---

### Chapitre 17 — Ransomware, darknet markets et cybercriminalité financière

Le traçage des **paiements ransomware** : pattern typique (victime → adresse unique par victime → consolidation → mixer/chain hop → exchange → cashout fiat). Le cashout (exchange à KYC faible, OTC desks, P2P, ou conversion directe en biens). L'attribution (les outils commerciaux maintiennent des clusters pour les principaux groupes — LockBit, BlackBasta, Cl0p). Cas : Colonial Pipeline (DarkSide 2021, $2,3M récupérés par saisie de clé privée par le DOJ). Les **darknet markets** (escrow — le marché détient les fonds, adresses identifiables ; multisig 2-of-3 ; tumbling intégré ; tendance Monero-only pour échapper au traçage Bitcoin — cf. cours Dark Web). Le **financement du terrorisme** via crypto (campagnes de crowdfunding, donations via channels Telegram, flux vers des zones de conflit — screening OFAC). La **cybercriminalité financière DPRK** (Lazarus — milliards volés en crypto, mécanismes de blanchiment massifs — cf. cours APT Ch.30).

---

### Chapitre 18 — Fraude crypto : rug pulls, Ponzi, pig butchering et scams

Les **rug pulls** (les créateurs retirent toute la liquidité du pool DEX — signaux : token récent, équipe anonyme, code non audité, liquidité non verrouillée ; le traçage post-rug pull suit les fonds vers le cashout). Les **Ponzi/pyramides** (rendements irréalistes, pas de produit réel — les fonds des nouveaux entrants payent les anciens ; le traçage montre la structure pyramidale des flux). Le **pig butchering** (arnaque sentimentale + investissement fictif — contact via dating apps, plateforme fausse, retrait impossible ; les fonds vont vers des OTC desks en Asie du Sud-Est — souvent liés à des réseaux de traite humaine). Le **phishing crypto** (vol de seed phrases, faux exchanges, faux support). Le **wash trading NFT** (vente à soi-même pour gonfler le prix puis vente à un vrai acheteur — détectable par analyse du graphe). Les **meme coins comme véhicule de manipulation de marché** (pump and dump coordonné, insider trading on-chain — détectable par l'analyse temporelle des achats pré-lancement, surtout sur Solana et BSC).

---

### Chapitre 19 — Blanchiment crypto : placement, layering, intégration

Le modèle en 3 phases. **Placement** (fonds illicites → wallet — paiement ransomware, vente dark market, fraude, corruption, vol crypto). **Layering** (opacification — mixers/CoinJoin, chain hopping BTC→XMR→USDT, DEX swaps sur plusieurs chaînes, bridges cross-chain, peel chains, DeFi lending/yield farming, passages par de multiples wallets intermédiaires, conversion en NFT). **Intégration** (conversion fiat — exchange KYC faible, P2P/Bisq, OTC desks surtout asiatiques, cartes crypto prépayées, achat immobilier/biens de luxe/véhicules, réseaux de mules, néo-banques). L'**OFAC et les sanctions crypto** (adresses spécifiques sanctionnées — Tornado Cash, adresses Lazarus, wallets liés au financement du terrorisme ; les stablecoins centralisés gèlent les adresses sanctionnées ; MiCA oblige les VASP à screener). Fil rouge : Sofia reconstitue le schéma complet de NEXUS — placement via WireEx, layering via DeFi + bridges + TRON, intégration via OTC desk chinois.

---

### Chapitre 20 — Asset recovery : de l'investigation à la saisie

*L'aboutissement opérationnel du traçage — transformer une investigation en recouvrement concret.*

Le processus : **identification des points d'ancrage** (exchange KYC où le suspect a un compte, stablecoin centralisé dont les adresses sont gelables, wallet dont la clé privée peut être saisie). **Réquisition judiciaire** pour les données KYC de l'exchange (identité, adresses de dépôt/retrait, historique, IP, appareils — processus variable selon l'exchange et la juridiction). **Gel préventif** (demande de gel à l'exchange — les grands exchanges coopèrent, les petits moins ; gel des stablecoins via Tether/Circle — effet immédiat, levier puissant). **Saisie de clé privée** (si la clé est obtenue par perquisition physique — hardware wallet saisi, seed phrase trouvée —, les fonds sont saisissables directement ; cas : Colonial Pipeline $2,3M, saisies Silk Road). **Coopération internationale** (MLA pour les exchanges étrangers — processus long ; réseau CARIN/Camden pour le recouvrement d'actifs transfrontalier ; réseau Egmont pour le renseignement financier).

Les **limites** : DeFi (pas d'entité centralisée à réquisitionner — les fonds dans un pool de liquidité ou un contrat de lending ne sont pas saisissables sans la clé privée), Monero (intraçable on-chain → impossible de suivre les fonds), exchanges offshore non coopératifs (pas de réponse aux réquisitions, pas d'accord de coopération), juridictions opaques (BVI, Seychelles — pas de réponse aux MLA dans des délais raisonnables), et la vitesse (les fonds crypto se déplacent en minutes — le processus juridique prend des semaines/mois → les fonds sont souvent déjà partis quand la réquisition arrive).

---

## PARTIE VI — CORRÉLATION, ANALYSE ET PRODUCTION DE RENSEIGNEMENT

---

### Chapitre 21 — Relier une adresse blockchain à une identité

Le Graal de l'investigation crypto — et souvent, ce qui fait basculer une enquête, c'est une **erreur OPSEC du suspect**, pas une prouesse technique de l'investigateur.

Les méthodes d'attribution : **Exchange KYC** (l'adresse appartient à un exchange identifié → réquisition judiciaire pour les données KYC du titulaire du compte). **OSINT directe** (l'adresse est publiée publiquement — adresse BTC dans un profil Telegram, thread Reddit, QR code tweeté, page de donation, bio Twitter, communiqué de presse). **Fuites de données** (l'adresse apparaît dans un breach — leak Mt.Gox, breach Ledger, bases de données d'exchanges piratés : correspondances email↔adresse). **ENS / domaines blockchain** (suspect.eth résout vers 0x1234... — un nom ENS est un lien direct entre un pseudonyme et une adresse ; de nombreux suspects enregistrent un ENS lié à leur identité réelle par commodité). **Métadonnées de transactions** (OP_RETURN sur Bitcoin, input data sur Ethereum — messages, signatures, références embarqués dans les transactions).

Les **erreurs OPSEC récurrentes** des suspects — ce fil transversal est critique car c'est souvent le point de bascule d'une enquête : **adresse postée publiquement** (profil forum, channel Telegram, page de donation), **ENS lié à l'identité réelle** (a.volkov.eth → Andreï Volkov), **QR code visible** dans une photo ou une vidéo (screenshot de wallet, photo de point de vente), **wallet connecté à un service identifiable** (un ENS, un profil Tornado Cash, un nom de domaine), **même email/username** entre un service crypto et un réseau social (l'email d'inscription sur l'exchange est le même que le LinkedIn), **screenshot révélateur** (le suspect montre un screenshot de portefeuille avec l'adresse visible, ou un historique de transactions identifiable), **réutilisation de wallets** entre activités licites et illicites (le même wallet reçoit un salaire et des paiements de ransomware), et **corrélation temporelle** (post forum + transaction 5 minutes après = même acteur probable, publication sur un réseau social et mouvement de fonds corrélé dans le temps).

Fil rouge : Sofia relie le wallet Ethereum de NEXUS à Volkov via 3 erreurs OPSEC convergentes — l'ENS a.volkov.eth (confiance haute), un screenshot de wallet sur un profil VKontakte (confiance haute), et la corrélation temporelle entre les publications LinkedIn de Volkov et les mouvements de fonds (confiance modérée).

---

### Chapitre 22 — Workflow intégré : OSINT + crypto + bases internes

Le processus complet pour une enquête typique du service. **Sollicitation métier** (le département formule la question). **OSINT sur le suspect** (registres, réseaux sociaux, mandats, patrimoine, PEP/sanctions — Ch.4-6). **Traçage crypto** (explorer, clusterer, tracer, identifier les services — Ch.12-14). **Corrélation OSINT-crypto** (le suspect a-t-il publié cette adresse ? est-elle liée à un exchange où il a un compte identifié ? la temporalité des publications et des transactions est-elle corrélée ?). **Corrélation bases internes** (le suspect est-il déjà connu du service ? d'autres DS ? des signalements partenaires ? des enquêtes antérieures ?). **Analyse** (synthèse des trois sources — OSINT + crypto + interne — niveaux de confiance, hypothèses concurrentes via ACH si la situation est ambiguë). **Production** (note d'analyse + rapport de traçage crypto + graphe de liens). **Feedback** (le métier valide ou demande un approfondissement).

---

### Chapitre 23 — Production de renseignement : notes, rapports et restitution

La **note d'analyse** : en-tête (référence, date, TLP, auteur, demandeur, version), objet (résumé en 2-3 lignes), contexte (sollicitation, informations initiales, périmètre, délai), méthodologie (sources, outils, période de collecte, OPSEC, blockchains analysées), faits établis (chaque fait = source + date + méthode + confiance), volet crypto (adresses, clustering, flux, services, graphe), analyse (inférences, corrélations, hypothèses concurrentes — ACH si pertinent), lacunes (ce qui manque et pourquoi), conclusions (réponse à la question, confiance globale), et recommandations (réquisitions, gels, approfondissements, alertes).

Les **niveaux de confiance** : fait observé/documenté (observable, vérifiable, reproductible — « l'adresse X a reçu 5 BTC de l'adresse Y le 15/03/2025 » — Etherscan, txid), inférence probable (clustering, corrélation forte — « les adresses X et Z appartiennent au même wallet avec une confiance haute basée sur le common-input »), inférence possible (attribution outil commercial, corrélation partielle — « le wallet est probablement lié à l'exchange W selon Chainalysis, confiance modérée »), et hypothèse (requiert des données supplémentaires — « le propriétaire du wallet pourrait être Volkov — requiert confirmation via réquisition KYC, confiance faible sans corrélation OSINT additionnelle »). **Ne JAMAIS** présenter une inférence comme un fait — la rigueur protège la crédibilité de l'analyste et du service.

La **restitution** au magistrat/à la hiérarchie : pas de jargon blockchain (pas de « UTXO », pas de « common-input clustering » — « les fonds ont été tracés de l'adresse A vers l'adresse B, puis convertis en USDT et transférés vers un bureau de change crypto en Chine »), des graphes de flux simplifiés et visuels, des montants en fiat (pas en ETH — « 340 000 € » pas « 120 ETH »), et des conclusions actionnables (« nous recommandons le gel des USDT identifiés et la réquisition à l'exchange WireEx pour les données d'identification du titulaire du compte »).

---

### Chapitre 24 — Capitalisation, veille et formation des enquêteurs

La **capitalisation** (fiches techniques — documentation de chaque méthode/outil/espace numérique ; fiches enquête — les techniques qui ont fonctionné deviennent des modèles ; base de knowledge — wiki interne, registre d'avatars, registre d'outils). La **veille technologique** (évolutions des outils OSINT/crypto, nouvelles blockchains et protocoles DeFi, nouvelles techniques de blanchiment, réglementation — MiCA, sanctions, travel rule ; sources : Chainalysis Crypto Crime Report, blogs Elliptic/TRM Labs, FATF updates, communauté Twitter/X crypto-compliance, rapports Europol IOCTA). La **formation des enquêteurs métiers** (sensibilisation aux fondamentaux crypto — « qu'est-ce qu'un wallet, une adresse, un exchange ? », démonstration des outils de traçage — « voici comment suivre un flux BTC en 5 minutes », et accompagnement sur les cas complexes — le référent n'est pas seulement un exécutant, il fait monter le niveau de tout le service).

---

## PARTIE VII — CAS DE SYNTHÈSE

*6 cas complets qui mobilisent toutes les compétences du cours.*

---

### Chapitre 25 — Cas complet : synthèse NEXUS

Synthèse du fil rouge sous forme de cas autonome. De la DS initiale à la note d'analyse finale.

**OSINT corporate :** NEXUS Consulting SARL (France, capital 1 000 €, CA 2,5 M€ — incohérent, gérant Volkov, domiciliation — red flags multiples) → OMEGA Holdings LTD (Chypre, même dirigeant Volkov, actionnaire nominee chypriote) → trust chypriote (UBO = Volkov via les Pandora Papers) → société Dubaï DIFC (même réseau, lien confirmé par OSINT technique — même certificat SSL). **Screening :** Volkov PEP confirmé, Pandora Papers, 1 contentieux Lettonie, aucune sanction.

**Traçage crypto :** BTC via WireEx (42 BTC sur 8 mois) → clustering (47 adresses liées) → conversion en ETH sur exchange secondaire → wallet Ethereum 0x7a3b... (lié à a.volkov.eth — erreur OPSEC) → swap USDT via Uniswap → bridge vers Polygon → transfert USDT vers TRON → distribution vers 12 adresses → OTC desk chinois (Fengshui Trading). Layering DeFi : utilisation d'Aave (dépôt ETH → emprunt USDC → bridge).

**Corrélation :** wallet Ethereum ↔ Volkov via ENS + screenshot VKontakte + corrélation temporelle. Bases internes : 3 DS antérieures sur des sociétés du même réseau (signalées par d'autres banques).

**Conclusion :** blanchiment organisé via crypto avec layering DeFi multi-chain, confiance élevée. Le réseau opère entre la France, Chypre, Dubaï, et la Chine via les blockchains BTC, ETH, Polygon, et TRON. L'UBO est Volkov, PEP, utilisant un réseau de sociétés écrans et un schéma de conversion crypto sophistiqué.

**Recommandations :** gel des USDT identifiés via demande à Tether, réquisition WireEx (Estonie — coopération UE) pour les données KYC complètes, signalement via le réseau Egmont pour l'OTC desk chinois, et transmission au parquet pour les suites judiciaires. **Livrables :** note d'analyse (10 pages), rapport de traçage crypto (graphe de flux annoté + tableau d'adresses), graphe de liens (réseau de sociétés + personnes + wallets), timeline.

---

### Chapitre 26 — Cas complet : traçage ransomware et identification du cashout

Une entreprise française a payé 5 BTC de rançon. L'adresse de paiement est connue (bc1q...). Le cas couvre : exploration (historique, volume, première tx), clustering (common-input → 23 adresses liées au même wallet), traçage sur 7 hops (consolidation → CoinJoin → exchange estonien → conversion USDT → bridge TRON → OTC desk), identification des services (le CoinJoin est identifié par Chainalysis, l'exchange par les attributions connues), screening sanctions (les adresses post-CoinJoin ne sont pas sanctionnées mais sont liées à un cluster ransomware connu — BlackBasta), corrélation OSINT (l'adresse de collecte apparaît dans un thread de négociation sur un forum dark web — pseudonyme « xDarkNet_777 » lié à un channel Telegram avec 14 membres), et recommandations (réquisition exchange estonien, gel USDT via Tether, signalement CERT national + ANSSI, partage IoC TLP:AMBER avec le secteur via l'ISAC).

---

### Chapitre 27 — Cas complet : rug pull multi-chain et traçage des créateurs

Un token lancé sur Ethereum (« GreenEnergy Token ») attire 800 investisseurs pour $2,3M de liquidité. Les créateurs retirent toute la liquidité (rug pull classique). Le cas couvre : analyse on-chain du contrat (pas de time lock, pas d'audit, le propriétaire peut retirer — le code est lisible sur Etherscan), traçage post-rug pull (ETH → swap USDT via Uniswap → bridge BSC → nouvelle liquidity pool BSC → nouveau rug pull sous un autre nom « SolarWind Token » → même pattern), identification des créateurs (le deployer du contrat GreenEnergy est lié par internal transactions à un wallet qui a interagi avec un exchange KYC — Binance, dépôt de 50 ETH 2 semaines avant le lancement), corrélation avec des rug pulls antérieurs (même wallet deployer, même pattern de code, même schéma de bridge — 4 rug pulls en 6 mois, $8M cumulés), et recommandations (réquisition Binance pour le wallet deployer, alerte communautaire sur le deployer address pour prévenir le prochain rug pull).

---

### Chapitre 28 — Cas complet : financement illicite via crowdfunding crypto

Un channel Telegram appelle aux donations en BTC pour une cause humanitaire qui s'avère être un front pour le financement d'une entité sanctionnée. Le cas couvre : collecte OSINT sur le channel (historique — créé 3 mois avant, 2 400 membres, administrateurs — 2 profils anonymes avec des numéros de téléphone géolocalisés au Moyen-Orient, contenu — propagande mélangée à des appels aux dons), traçage des donations BTC (3 adresses publiées → cluster de 67 adresses liées → consolidation → conversion en USDT via un exchange offshore → transfert vers des adresses liées à une entité sanctionnée OFAC), screening sanctions (2 des adresses de destination sont dans la liste OFAC SDN → confirmation du lien avec l'entité sanctionnée), et production d'un rapport d'alerte avec recommandations (signalement au magistrat, notification Europol/IACCC, partage TLP:RED avec les CRF partenaires via Egmont, et signalement à Telegram pour suppression du channel).

---

### Chapitre 29 — Cas complet : investigation Monero — quand la blockchain ne suffit pas

Un suspect utilise exclusivement Monero pour recevoir et envoyer des fonds liés à la vente de données volées sur un darknet market. Le cas illustre les limites du traçage on-chain (ring signatures, stealth addresses — pas de traçabilité directe sur Monero) et les stratégies alternatives : identifier les **points de conversion** (le suspect achète du XMR avec du BTC sur un exchange KYC — Kraken — traçable côté BTC, réquisition côté exchange pour identifier le compte), les **erreurs OPSEC** (le suspect utilise le même username « d4rktr4der » sur le darknet market et sur un exchange Telegram OTC — lien identité pseudonyme ↔ numéro de téléphone ; il a publié une adresse XMR de réception dans un post public sur un forum — lien adresse ↔ pseudonyme), l'**OSINT classique** (le username « d4rktr4der » apparaît aussi sur un profil GitHub avec un email personnel — pivot vers l'identité réelle), et la **corrélation temporelle** (un retrait XMR de l'exchange et un achat immobilier le même jour — les montants correspondent après conversion). Le cas démontre que l'investigation crypto est une compétence hybride — quand la blockchain ne donne rien, l'OSINT, les erreurs OPSEC du suspect, et les points de conversion compensent.

---

### Chapitre 30 — Exercice : sollicitation métier complète (non guidé)

Un exercice non guidé (pas de solution pas-à-pas) : l'étudiant reçoit une sollicitation métier réaliste et doit produire la note d'analyse complète. **Scénario :** « L'individu X, soupçonné de blanchir les produits d'une fraude à la TVA via crypto, possède une société à Dubaï (DIFC) et un wallet Ethereum identifié (0xabc...). Il est potentiellement PEP (ancien directeur d'une agence gouvernementale d'un pays d'Asie centrale). Que pouvez-vous trouver ? ». L'exercice mobilise toutes les compétences : cadrage (formuler les QR, définir le périmètre), OSINT corporate (registre DIFC/DED Dubaï, screening PEP), OSINT personne physique (réseaux sociaux, mandats, patrimoine), traçage wallet Ethereum (Etherscan, interactions DeFi, bridges, tokens), corrélation OSINT-crypto-bases internes, analyse avec ACH si ambiguïté, et production de la note + rapport crypto. **Grille d'auto-évaluation** fournie : cadrage structuré (oui/non), sources pertinentes consultées (liste), clustering effectué, flux tracés, services identifiés, corrélation OSINT-crypto réalisée, niveaux de confiance spécifiés, limites mentionnées, livrables produits (note + graphe de flux + graphe de liens).

---

## ANNEXES

---

### Annexe A — Glossaire OSINT + Crypto

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — méthode d'analyse structurée |
| **AML** | Anti-Money Laundering — lutte anti-blanchiment |
| **Bridge** | Protocole de transfert de valeur entre blockchains |
| **Chain hopping** | Passer d'une blockchain à une autre pour compliquer le traçage |
| **CoinJoin** | Technique de mélange de transactions Bitcoin (combine les inputs de plusieurs utilisateurs) |
| **Cluster analysis** | Regroupement d'adresses d'un même wallet via heuristiques |
| **CRF** | Cellule de Renseignement Financier (TRACFIN en France) |
| **DEX** | Decentralized Exchange (Uniswap, PancakeSwap, Jupiter) |
| **DeFi** | Finance Décentralisée — protocoles financiers sans intermédiaire |
| **DS** | Déclaration de Soupçon — signalement d'une institution financière à la CRF |
| **ENS** | Ethereum Name Service (pseudonyme.eth → adresse 0x...) |
| **Entity resolution** | Déterminer si deux entrées désignent la même entité |
| **EOA** | Externally Owned Account — compte Ethereum contrôlé par une clé privée |
| **ERC-20** | Standard de token fongible sur Ethereum (USDT, USDC, DAI) |
| **ERC-721** | Standard de token non fongible (NFT) sur Ethereum |
| **EVM** | Ethereum Virtual Machine — environnement d'exécution compatible multi-chaînes |
| **FATF / GAFI** | Groupe d'Action Financière Internationale |
| **Gas** | Unité de coût computationnel sur Ethereum |
| **KYC** | Know Your Customer — vérification d'identité obligatoire |
| **LCB-FT** | Lutte Contre le Blanchiment et le Financement du Terrorisme |
| **Layering** | Phase d'opacification dans le schéma de blanchiment |
| **Mempool** | File d'attente des transactions non confirmées |
| **MiCA** | Markets in Crypto-Assets — réglementation UE 2024 |
| **Mixer / Tumbler** | Service de mélange de transactions pour opacifier l'origine |
| **MLA** | Mutual Legal Assistance — coopération judiciaire internationale |
| **Nominee** | Tiers prêtant son nom comme dirigeant/actionnaire |
| **OFAC** | Office of Foreign Assets Control — sanctions US |
| **OPSEC** | Operations Security — sécurité opérationnelle de l'investigateur |
| **OTC desk** | Over-The-Counter — bureau de change crypto hors exchange |
| **Peel chain** | Pattern de distribution séquentielle depuis un wallet central |
| **PEP** | Politically Exposed Person — personne politiquement exposée |
| **PIR** | Priority Intelligence Requirement — question de renseignement prioritaire |
| **Privacy coin** | Cryptomonnaie conçue pour la confidentialité (Monero, Zcash) |
| **Rug pull** | Arnaque où les créateurs retirent toute la liquidité |
| **Shell company** | Société écran sans activité réelle |
| **SOCMINT** | Social Media Intelligence |
| **Stablecoin** | Token indexé sur une monnaie fiat (USDT, USDC, DAI) |
| **TLP** | Traffic Light Protocol (RED/AMBER/GREEN/CLEAR) |
| **Travel Rule** | Obligation de transmettre les infos expéditeur/destinataire entre VASP |
| **UBO** | Ultimate Beneficial Owner — bénéficiaire effectif réel |
| **UTXO** | Unspent Transaction Output — modèle de transaction Bitcoin |
| **VASP** | Virtual Asset Service Provider — prestataire de services crypto |
| **Wash trading** | Vente fictive à soi-même pour gonfler les prix |
| **WORM** | Write Once Read Many — stockage immuable |

---

### Annexe B — Registres d'entreprises par juridiction

| Pays | Registre | Accès | UBO | Particularités |
|------|----------|-------|-----|---------------|
| France | Infogreffe, Pappers, Bodacc, INPI | Pappers gratuit, Infogreffe premium | Registre INPI (restreint) | Comptes annuels déposés |
| UK | Companies House | Gratuit, très complet | PSC Register (public) | Gold standard transparence |
| USA | SEC EDGAR (cotées), State registries | EDGAR gratuit, States variable | FinCEN BOI (2024) | Varie par État |
| Luxembourg | LBR | Payant | Registre UBO (restreint) | Centre financier majeur |
| Suisse | Zefix + cantonaux | Gratuit | Pas de registre public | Opacité légale |
| Chypre | DRCOR | Partiellement en ligne | En cours de mise en place | Juridiction très utilisée |
| Émirats (Dubaï) | DIFC / DED | Partiellement en ligne | Variable | Free zones multiples |
| BVI/Seychelles/Panama | Registres très opaques | Souvent inaccessibles | Non disponible | → ICIJ Offshore Leaks |
| Multi-pays | OpenCorporates (gratuit), Orbis/BvD (payant) | Variable | Agrégation | Orbis = le plus complet |
| Leaks | ICIJ Offshore Leaks | Gratuit | Données fuitées | Panama/Pandora/Paradise Papers |

---

### Annexe C — Checklists opérationnelles

**Checklist OPSEC investigation :** VM dédiée activée ? VPN non-corporate activé ? Navigateur profil vierge ? Pas de connexion à un compte réel ? Avatar mature si interaction ? DNS chiffré ? Métadonnées nettoyées avant diffusion ? Stockage chiffré ? Documentation de la session (sources, méthodes, horodatage) ?

**Checklist investigation crypto :** Adresse(s) de départ identifiée(s) et blockchain confirmée ? Exploration complète de l'historique ? Clustering effectué (common-input, change detection) ? Flux tracés en amont et en aval ? Services identifiés (exchanges, mixers, DEX, bridges) ? Screening sanctions (OFAC, Sanctions Oracle) ? Corrélation OSINT (adresse publiée, ENS, forums, leaks, erreurs OPSEC) ? Corrélation bases internes ? Graphe de flux annoté produit ? **Niveaux de confiance spécifiés pour CHAQUE attribution ?** Limites analytiques documentées ?

**Checklist note d'analyse :** En-tête complet (référence, date, TLP, auteur, demandeur) ? Contexte et méthodologie décrits ? Faits / inférences / lacunes clairement distingués ? Niveau de confiance pour chaque conclusion ? Limites explicitement mentionnées ? Annexes de preuves (captures horodatées, graphes, tableaux d'adresses) ? Métadonnées du document nettoyées ? TLP défini ? Peer review 4 yeux effectué ?

---

### Annexe D — Templates de livrables

#### Note d'analyse OSINT/Crypto (structure)

```
EN-TÊTE : Référence | Date | TLP | Auteur | Demandeur | Version
OBJET : Résumé en 2-3 lignes
CONTEXTE : Sollicitation, informations initiales, périmètre, délai
MÉTHODOLOGIE : Sources, outils, période de collecte, OPSEC, blockchains
FAITS ÉTABLIS : Chaque fait = source + date + méthode + confiance
VOLET CRYPTO : Adresses, clustering, flux, services, graphe
ANALYSE : Inférences, corrélations, hypothèses concurrentes (ACH)
LACUNES : Ce qui manque et pourquoi
CONCLUSIONS : Réponse à la question, confiance globale
RECOMMANDATIONS : Réquisitions, gels, approfondissements, alertes
ANNEXES : Graphe de flux, graphe de liens, timeline, tableaux d'adresses
```

#### Rapport de traçage crypto (structure)

```
EN-TÊTE : Référence | Date | TLP | Blockchains analysées
ADRESSE(S) DE DÉPART : [liste avec blockchain et première observation]
CLUSTERING : [méthode, résultat, nombre d'adresses liées, confiance]
GRAPHE DE FLUX : [visuel annoté — montants, directions, services]
TABLEAU D'ADRESSES : [adresse | blockchain | cluster | attribution | confiance]
SERVICES IDENTIFIÉS : [exchange, mixer, DEX, bridge — méthode d'identification]
SCREENING SANCTIONS : [résultat OFAC, Sanctions Oracle]
CORRÉLATION OSINT : [liens adresse ↔ identité, méthode, confiance]
TIMELINE : [chronologie des mouvements de fonds]
CONCLUSIONS : [schéma global, flux total, destination finale]
LIMITES : [chaînes non couvertes, attributions non confirmées]
```

---

### Annexe E — Outils par catégorie

| Catégorie | Outil | Type | Usage |
|-----------|-------|------|-------|
| **OSINT corporate** | Pappers, Companies House, SEC EDGAR | Registres | Investigation de sociétés |
| | OpenCorporates | Agrégateur | Recherche multi-pays |
| | Orbis / BvD | Commercial | Chaînes de participation internationales |
| | ICIJ Offshore Leaks | Base de leaks | Panama/Pandora/Paradise Papers |
| **OSINT personnes** | OpenSanctions | Agrégateur | Sanctions + PEP screening |
| | OFAC SDN List | Sanctions US | Screening (inclut adresses crypto) |
| | LinkedIn, Twitter/X | Réseaux sociaux | Réseau, activité, train de vie |
| **OSINT technique** | crt.sh | Certificats | Liens entre domaines via SAN |
| | Whois, DNS | Infrastructure | Propriétaire, hébergeur, email |
| | Shodan, Censys | Scan | Infrastructure exposée |
| **Blockchain — Explorateurs** | Blockchain.com, OXT.me | Bitcoin | Exploration, clustering (OXT) |
| | Etherscan | Ethereum | Référence — tx, tokens, events |
| | BscScan, PolygonScan | Chaînes EVM | Même interface qu'Etherscan |
| | Tronscan | TRON | USDT sur TRON |
| | Solscan | Solana | DeFi et NFT Solana |
| | Blockchair | Multi-chain | Requêtes SQL-like |
| **Blockchain — Commercial** | Chainalysis Reactor | Investigation | Leader mondial, LEA/CRF |
| | TRM Labs | Investigation | 25+ chains, cross-chain |
| | Elliptic | Compliance | Multi-chain, scoring |
| | Crystal Blockchain | Compliance | Scoring de risque |
| | Arkham Intelligence | Attribution | Attribution communautaire |
| **Blockchain — Open source** | Breadcrumbs.app | Tracing visuel | Gratuit, bon pour débuter |
| | WalletExplorer | Clustering BTC | Attribution de services |
| | Chainalysis Sanctions Oracle | Screening | Vérification sanctions gratuite |
| **Data science** | Python (requests, pandas) | Programmation | APIs, traitement de données |
| | networkx | Graphes | Graphe de liens/relations |
| | rapidfuzz | Matching | Entity resolution |
| | Maltego | Graphe d'entités | Pivots multi-sources |

---

### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Investigation OSINT + crypto | **Ce cours** | — |
| OSINT techniques générales | **Cours OSINT Mastery** | Ce cours (workflows spécifiques investigation financière) |
| Dark web (navigation, investigation) | **Cours Dark Web** | Ce cours (Ch.17 darknet markets crypto) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | Ce cours (Ch.17-19 volet financier) |
| CTI (renseignement de menace) | **Cours CTI** | Ce cours (Ch.23 production de renseignement — même méthodologie) |
| Intelligence économique | **Cours IE** | Ce cours (Ch.4-5 due diligence corporate — complémentaire) |
| APT (acteurs étatiques) | **Cours APT** | Ce cours (Ch.17 DPRK financement, Ch.19 blanchiment étatique) |
| GRC (conformité) | **Cours GRC** | Ce cours (Ch.16 MiCA, compliance crypto) |

---

### Annexe G — Ressources et formation

#### Formations et certifications

| Formation | Organisme | Focus |
|-----------|----------|-------|
| SANS FOR498 | SANS | OSINT formalisé (Battlefield OSINT) |
| SANS FOR589 | SANS | Cybercrime Intelligence (crypto focus) |
| Certified Cryptocurrency Investigator | Chainalysis | Traçage blockchain avec Reactor |
| ACFCS (Certified Financial Crime Specialist) | ACFCS | Investigation financière globale |
| OSCP (Certified OSINT Professional) | McAfee Institute | OSINT certification |
| Blockchain Intelligence Certification | BIG | Investigation blockchain |

#### Livres de référence

| Titre | Auteur | Sujet |
|-------|--------|-------|
| *Mastering Bitcoin* | A. Antonopoulos | Bitcoin en profondeur (UTXO, scripts) |
| *Mastering Ethereum* | A. Antonopoulos & G. Wood | Ethereum, smart contracts, EVM |
| *OSINT Techniques* | M. Bazzell | Méthodes et outils OSINT complets |
| *Crypto Crime Investigation* | N. Furneaux | Investigation crypto pour LEA |

#### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| Crypto Crime Report | Chainalysis | Tendances criminelles crypto, case studies |
| Illicit Finance Report | TRM Labs | Blanchiment, sanctions, DeFi |
| IOCTA | Europol | Menaces cyber organisées en Europe |
| Red Flag Indicators | FATF/GAFI | Indicateurs de blanchiment crypto |
| Internet Organised Crime Threat Assessment | Europol | Évaluation annuelle des menaces |

#### Communautés et veille

| Ressource | Type | Usage |
|-----------|------|-------|
| OSINT Framework | Annuaire d'outils | Référence complète par catégorie |
| Bellingcat guides | Méthodologie | GEOINT, vérification, investigation |
| Trace Labs OSINT CTF | Compétition | Pratique OSINT éthique (missing persons) |
| start.me/p/OSINT | Listes curated | Collections communautaires |
| Twitter/X #CryptoCompliance | Communauté | Veille réglementation et techniques |
| Chainalysis Blog | Blog | Analyses de cas, nouvelles techniques |

---

---

# Annexe — Questions types d'entretien et réponses types

## Questions essentielles

- **Question :** Qu'est-ce que le cluster analysis en investigation blockchain ?
  - **Réponse type :** Le clustering regroupe plusieurs adresses blockchain qui appartiennent vraisemblablement au même acteur. L'heuristique principale sur Bitcoin c'est le co-spending : si deux adresses apparaissent comme inputs d'une même transaction, elles sont contrôlées par la même entité (il faut les deux clés privées pour signer). Ça permet de reconstituer le portefeuille réel d'un suspect au-delà de l'adresse unique. Les outils comme Chainalysis Reactor ou OXT font ce clustering automatiquement et attribuent les clusters à des services connus (exchanges, mixers, darknet markets).

- **Question :** Comment relie-t-on une adresse blockchain à une identité réelle ?
  - **Réponse type :** On croise plusieurs sources. Côté blockchain : tracer les flux vers un exchange régulé qui applique le KYC — l'exchange peut fournir l'identité sur réquisition. Côté OSINT : chercher l'adresse dans les leaks, les forums, les réseaux sociaux. Parfois le suspect a publié son adresse sur un profil, utilisé un ENS (Ethereum Name Service) lié à un pseudonyme, ou fait un screenshot de son wallet. C'est souvent une erreur OPSEC du suspect qui fait basculer l'enquête, pas le traçage technique seul.

- **Question :** Quels sont les principaux mécanismes d'évasion blockchain que vous connaissez ?
  - **Réponse type :** Les mixers et tumblers (CoinJoin, Tornado Cash) mélangent les fonds de plusieurs utilisateurs pour rompre le lien entre source et destination. Les privacy coins (Monero avec RingCT, Zcash avec zk-SNARKs) offrent de la confidentialité native. Le chain hopping (passer d'une blockchain à une autre via des bridges ou des DEX) complique le traçage. Et le peel chain : l'attaquant envoie un petit montant à une nouvelle adresse et le reste à lui-même, et répète l'opération pour disperser les fonds.

- **Question :** Pourquoi l'OPSEC est-elle essentielle pour un investigateur OSINT ?
  - **Réponse type :** Parce que les cibles — criminalité organisée, acteurs étatiques — peuvent avoir des capacités de contre-surveillance. Si je consulte un profil LinkedIn avec mon vrai compte, la cible voit la visite. Si mes requêtes DNS sont en clair, mon activité d'investigation est visible. L'OPSEC inclut : VM dédiée par enquête, VPN non-corporate, navigateur vierge, DNS chiffré, avatars pour les interactions, et cloisonnement strict entre les enquêtes.

- **Question :** Décrivez votre méthodologie face à une sollicitation d'investigation crypto.
  - **Réponse type :** Je commence par formuler les questions de renseignement — que cherche-t-on exactement. Puis je fais l'OSINT corporate et personnes en parallèle du traçage blockchain. Pour le traçage : j'identifie les adresses de départ, je trace les flux entrants et sortants, j'identifie les services (exchanges, mixers, bridges) par clustering, et je cherche les points de cashout. Je corrèle les résultats on-chain avec l'OSINT classique (registres, réseaux sociaux, leaks). Je produis une note d'analyse structurée avec niveaux de confiance et limites explicites.

## Questions complémentaires

- **Question :** Quelle est la différence entre le modèle UTXO (Bitcoin) et le modèle compte (Ethereum) pour l'investigation ?
  - **Réponse type :** Bitcoin utilise des UTXO (Unspent Transaction Outputs) — chaque transaction consomme des outputs précédents et en crée de nouveaux. Ça permet le co-spending analysis pour le clustering. Ethereum utilise un modèle de comptes avec soldes — il n'y a pas de co-spending, mais les interactions avec les smart contracts (DeFi, DEX) laissent des traces exploitables. Ethereum est aussi plus transparent sur les tokens (ERC-20, NFT), ce qui donne plus de points de pivot.

## Questions les plus probables en entretien

1. Cluster analysis : c'est quoi, comment ça marche ?
2. Comment lier une adresse blockchain à une identité ?
3. Mécanismes d'évasion blockchain ?
4. OPSEC de l'investigateur ?
5. Méthodologie face à une investigation crypto ?

## Réponses flash

- **Clustering** → Co-spending (BTC) = mêmes inputs = même entité. Regroupe les adresses en portefeuilles. Outils = Chainalysis, OXT.
- **Attribution** → Tracer vers un exchange KYC + OSINT (leaks, réseaux sociaux, ENS, erreurs OPSEC). Corrélation on-chain + off-chain.
- **Évasion** → Mixers (CoinJoin, Tornado Cash), privacy coins (Monero), chain hopping (bridges/DEX), peel chains.
- **OPSEC** → VM dédiée, VPN non-corporate, navigateur vierge, DNS chiffré, avatars, cloisonnement par enquête.
- **Méthodologie** → Questions de renseignement → OSINT corporate + personnes → traçage blockchain → corrélation → note d'analyse avec niveaux de confiance.
- **UTXO vs compte** → BTC = UTXO, co-spending pour clustering. ETH = comptes, pas de co-spending mais traces smart contracts.

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à l'investigation numérique et financière — la double compétence OSINT avancé + analyse blockchain qui permet de « suivre l'argent » dans l'économie numérique, quelles que soient les juridictions et les blockchains traversées.
>
> L'opération NEXUS illustre une conviction opérationnelle : l'investigation crypto n'est jamais purement technique. Le traçage blockchain est un outil puissant — mais c'est souvent une erreur OPSEC du suspect (un ENS lié à son nom, un screenshot de wallet, un username réutilisé) qui fait basculer l'enquête. La double compétence OSINT + crypto est plus que la somme de ses parties : c'est la corrélation entre les deux qui produit le renseignement actionnable.
>
> Le cours assume trois convictions. Première : la rigueur analytique est non négociable — distinguer le fait de l'inférence, documenter les niveaux de confiance, et expliciter les limites protège l'analyste, le service, et l'enquête. Deuxième : la blockchain est publique mais pas transparente — le traçage demande de la méthode, des outils, et de la persévérance, pas de la magie. Troisième : l'investigation ne se limite jamais à la blockchain — les registres, les réseaux sociaux, les bases internes, les fuites, et les erreurs du suspect sont autant de vecteurs de découverte que les transactions on-chain.
>
> *Tracer • Corréler • Analyser • Restituer — avec rigueur et discernement.*

