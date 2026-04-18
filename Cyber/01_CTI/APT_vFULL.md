# AU CŒUR DES APT

*Advanced Persistent Threats — Acteurs étatiques, campagnes et géopolitique cyber*

**Cours complet — 32 chapitres • 8 parties • 8 annexes**

*Comprendre qui menace • Pourquoi • Avec quels moyens • Dans quel contexte*

-----

## Table des matières

- [Fil rouge : Opération BLACKOUT](#fil-rouge--opération-blackout)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - Ch.1 — Qu’est-ce qu’une APT : définition, frontières, typologies
  - Ch.2 — Cycle de vie d’une intrusion APT
  - Ch.3 — Tradecraft et TTP : le comment opérationnel
  - Ch.4 — Le cyber comme instrument de puissance étatique
- **PARTIE II — RUSSIE (Ch.5-7)**
  - Ch.5 — Russie : contexte, doctrine et appareil cyber
  - Ch.6 — Russie : les groupes APT en détail
  - Ch.7 — Russie : campagnes de référence et opérations d’influence
- **PARTIE III — CHINE (Ch.8-10)**
  - Ch.8 — Chine : contexte, doctrine et appareil cyber
  - Ch.9 — Chine : les groupes APT en détail
  - Ch.10 — Chine : campagnes de référence et tendances 2023-2026
- **PARTIE IV — DPRK, IRAN ET AUTRES ACTEURS (Ch.11-15)**
  - Ch.11 — DPRK : contexte, groupes et modèle unique
  - Ch.12 — DPRK : campagnes de référence et financement du régime
  - Ch.13 — Iran : contexte, doctrine et groupes APT
  - Ch.14 — Iran : campagnes de référence
  - Ch.15 — Autres acteurs étatiques, mercenaires cyber et zones grises
- **PARTIE V — PUISSANCES CYBER OCCIDENTALES ET ALLIÉES (Ch.16-19)**
  - Ch.16 — États-Unis : doctrine, agences et cyber power
  - Ch.17 — Royaume-Uni et Five Eyes
  - Ch.18 — Israël : cyber, renseignement et supériorité technologique
  - Ch.19 — Ukraine : cyberdéfense et guerre en temps réel
- **PARTIE VI — MENACES OT ET PRÉ-POSITIONNEMENT (Ch.20-23)**
  - Ch.20 — Architecture OT/ICS et protocoles industriels
  - Ch.21 — Campagnes OT/ICS destructrices
  - Ch.22 — Le pré-positionnement : la menace silencieuse
  - Ch.23 — Protection des infrastructures critiques
- **PARTIE VII — GÉOPOLITIQUE, ATTRIBUTION ET PROSPECTIVE (Ch.24-28)**
  - Ch.24 — Attribution : méthodes, limites et enjeux
  - Ch.25 — L’écosystème cyber offensif mondial
  - Ch.26 — Dissuasion, normes et responsabilité étatique
  - Ch.27 — Tendances 2024-2026 et signaux d’anticipation
  - Ch.28 — Construire une défense APT-ready
- **PARTIE VIII — ÉTUDES DE CAS INTÉGRÉES (Ch.29-32)**
  - Ch.29 — SolarWinds / SUNBURST : la supply chain comme vecteur d’espionnage
  - Ch.30 — Lazarus et l’empire crypto de la DPRK
  - Ch.31 — Volt Typhoon : le pré-positionnement stratégique
  - Ch.32 — Synthèse BLACKOUT : attribution face à l’incertitude
- **ANNEXES**
  - Annexe A — Glossaire APT/CTI (80+ termes)
  - Annexe B — Groupes APT majeurs par pays
  - Annexe C — Conventions de nommage
  - Annexe D — Timeline des cyberattaques étatiques (2007-2026)
  - Annexe E — Mapping ATT&CK par acteur
  - Annexe F — Malwares et implants emblématiques
  - Annexe G — Cadres juridiques et réglementaires par juridiction
  - Annexe H — Ressources et formation

-----

## Fil rouge : Opération BLACKOUT

> **Contexte narratif — ce fil rouge traverse le cours et se conclut au Ch.32.**
> 
> Un **opérateur de distribution d’énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
> 
> **L’intrusion** : l’attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d’une application de supervision, s’est déplacé latéralement via PsExec et Kerberoasting, puis a pivoté vers le réseau de supervision SCADA via un poste d’ingénierie à double connexion. Il a été détecté et éjecté avant d’atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
> 
> **Le mystère** : aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L’attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d’appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
> 
> L’investigation traverse le cours à travers une dizaine d’épisodes — chacun placé là où il apporte une clé analytique réelle : identification des TTP, comparaison aux profils par pays, analyse du ciblage OT, processus d’attribution et calibration de la réponse, synthèse finale au Ch.32.

-----

## PARTIE I — FONDATIONS

> **Ce que cette partie apprend.** Comprendre ce qu’est une APT comme objet d’analyse (pas juste une attaque sophistiquée), maîtriser le vocabulaire de la discipline, reconnaître la structure d’une intrusion de bout en bout, connaître les techniques de tradecraft qui distinguent l’opérateur étatique, et saisir pourquoi les États utilisent le cyberespace comme instrument de puissance.
> 
> **Ce qu’elle ne couvre pas.** Les profils d’acteurs par pays (Parties II à V), les spécificités OT (Partie VI), les enjeux d’attribution et de droit international (Partie VII).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer une APT d’autres classes de menaces, lire une matrice ATT&CK, comprendre un rapport CTI d’incident, et situer n’importe quelle cyberopération étatique dans le cadre doctrinal d’un État.

-----

### Chapitre 1 — Qu’est-ce qu’une APT : définition, frontières, typologies

#### 1.1 Définition opérationnelle : Advanced, Persistent, Threat

Le terme **APT** (Advanced Persistent Threat) désigne un adversaire généralement state-sponsored ou state-aligned qui mène des cyberopérations sophistiquées, durables et ciblées. Chaque mot compte, et chacun corrige une erreur d’interprétation fréquente.

**Advanced** ne signifie pas forcément « zero-day » ou « malware jamais vu ». Beaucoup d’APT réussissent avec des credentials volés, des vulnérabilités connues non patchées, ou du Living off the Land quasi exclusif (Volt Typhoon est l’exemple canonique). Ce qui est « advanced », c’est la combinaison de quatre éléments : **capacité d’adaptation** (l’attaquant change de TTP quand il est détecté), **tradecraft mature** (OPSEC, évasion, persistence multi-couches), **ressources conséquentes** (temps, budget, opérateurs formés, infrastructure renouvelable), et **renseignement préalable** sur la cible (reconnaissance, HUMINT, collection passive en amont).

**Persistent** signifie que l’objectif n’est pas un coup unique. L’adversaire investit dans la persistence — backdoors multiples, accès redondants, mécanismes de réinfection si éjecté. Le **dwell time** (temps écoulé entre la compromission initiale et la détection) se mesure typiquement en semaines à mois. Pour les opérations de pré-positionnement sophistiquées (Volt Typhoon dans les infrastructures US, Sandworm dans les réseaux énergétiques européens), il se mesure en **années**. La moyenne observée par Mandiant dans son rapport M-Trends est passée de 205 jours en 2014 à 10 jours en 2023 — mais cette baisse cache une bimodalité : les compromissions de ransomware sont détectées vite (impact visible), les compromissions APT silencieuses restent longtemps sous le radar.

**Threat** rappelle qu’on parle d’une menace intentionnelle, dirigée par des humains. Des opérateurs prennent des décisions en temps réel, adaptent leur approche aux contre-mesures de la victime, et ont des objectifs stratégiques définis par un commanditaire — un service de renseignement, un état-major militaire, ou un appareil gouvernemental. Cette dimension humaine distingue l’APT d’un malware automatisé ou d’un ransomware opportuniste.

La définition opérationnelle qui en résulte : une APT est un **intrusion set** suivi dans le temps, caractérisé par une victimologie cohérente, des TTP stables ou évoluant lentement, une infrastructure réutilisée, et dont les objectifs s’inscrivent dans l’agenda stratégique d’un État — directement (opérateur interne à un service) ou indirectement (contractor, proxy, hacktiviste instrumentalisé).

#### 1.2 APT vs cybercriminalité vs hacktivisme vs insider

Les différences structurantes entre les classes de menaces sont résumées dans le tableau suivant. Elles ne sont pas absolues — les frontières s’estompent, on y reviendra — mais elles fixent les repères de base.

|Critère                |APT (étatique)                                       |Cybercriminel              |Hacktiviste                  |Insider                      |
|-----------------------|:---------------------------------------------------:|:-------------------------:|:---------------------------:|:---------------------------:|
|Motivation             |Espionnage, sabotage, influence, pré-positionnement  |Profit financier           |Idéologie, réputation        |Vengeance, profit, négligence|
|Sponsor                |État, proxy, contractor                              |Autonome ou groupe organisé|Groupe idéologique           |Employé/contractant          |
|Temporalité            |Mois à années                                        |Jours à semaines           |Ponctuel                     |Variable                     |
|Sélection cibles       |Très ciblé (secteur, organisation)                   |Opportuniste ou semi-ciblé |Symboles politiques          |Leur propre organisation     |
|OPSEC                  |Très élevé (furtivité maximale)                      |Variable                   |Faible à moyen               |Variable                     |
|Tolérance au bruit     |Très faible                                          |Moyenne (smash & grab)     |Haute (cherche la visibilité)|Variable                     |
|Critère de succès      |Accès maintenu, données exfiltrées, effet stratégique|Monétisation rapide        |Impact médiatique            |Dommage ou gain personnel    |
|Adaptation aux défenses|Systématique                                         |Parfois                    |Rare                         |Aucune                       |

Les frontières sont floues, et c’est précisément ce qui rend l’analyse intéressante. **APT41** (Chine) mène simultanément des opérations d’espionnage étatique validées par le MSS et des opérations cybercriminelles personnelles pour le profit des opérateurs (les indictments DOJ de 2020 les documentent explicitement). Les **groupes ransomware russophones** (LockBit, Conti historique, BlackBasta) opèrent sous une tolérance tacite de l’État russe tant qu’ils ne ciblent pas la CEI — certains ont des liens documentés avec les services (le leak Conti en 2022 a révélé des correspondances évoquant le FSB). **Lazarus** (DPRK) utilise le cybervol de cryptomonnaies comme source de financement étatique — la méthode est du cybercrime, la finalité et l’opérateur sont étatiques. **KillNet** et **NoName057(16)** présentent une esthétique hacktiviste pro-russe mais leur coordination opérationnelle et leur protection relative suggèrent au minimum une connivence avec les services.

Ces zones grises sont traitées au Ch.15 et analysées au Ch.25. Pour l’analyste opérationnel, la règle est simple : **ne pas confondre méthode et finalité**. Un ransomware qui chiffre un hôpital peut être motivé par le profit, l’influence, ou la déstabilisation — la méthode ne détermine pas l’intention.

#### 1.3 Typologie d’objectifs APT

Les APT poursuivent cinq grands types d’objectifs, souvent combinés dans une même opération ou une même campagne.

Le **cyberespionnage** est l’objectif le plus courant en volume. Il vise la collecte de données stratégiques : propriété intellectuelle industrielle (semiconducteurs, aéronautique, pharmaceutique), plans militaires, communications diplomatiques, positions de négociation, secrets commerciaux, données personnelles de cibles d’intérêt (dissidents, journalistes, diplomates). L’espionnage cyber remplace ou complète les méthodes traditionnelles (HUMINT, SIGINT). APT29 (Russie/SVR) en est l’archétype sophistiqué ; APT10 (Chine/MSS) en est l’archétype massif.

Le **pré-positionnement** est l’objectif stratégique le plus inquiétant. Il consiste à maintenir un accès dormant dans des infrastructures critiques — énergie, eau, télécoms, transport — pour une activation future en cas de conflit. L’opération ne vise pas l’exfiltration ni le sabotage immédiat ; elle vise à disposer d’un levier. **Volt Typhoon** (Chine, traité au Ch.22 et Ch.31) en est le cas d’école moderne. Sandworm (GRU) a pratiqué le pré-positionnement sur les infrastructures européennes dans le contexte du conflit ukrainien.

Le **sabotage** vise à endommager ou détruire des systèmes. **NotPetya** (Sandworm, 2017) a causé plus de 10 milliards de dollars de dégâts mondiaux ; **Industroyer** (Sandworm, 2016) a provoqué un blackout à Kiev via la manipulation des protocoles industriels ; **Shamoon** (Iran, 2012) a détruit 30 000 postes de Saudi Aramco. Le sabotage cyber produit des effets physiques (blackouts) ou quasi physiques (destruction de capacité opérationnelle d’une organisation pendant des semaines).

L’**influence** et la **désinformation** manipulent l’opinion et déstabilisent politiquement. L’**ingérence électorale** de 2016 aux US (APT28 — DNC hack, puis publication coordonnée via WikiLeaks et DCLeaks) est le cas fondateur. Les campagnes russes contre les élections européennes, la campagne chinoise sur les réseaux sociaux occidentaux, les opérations iraniennes contre les diasporas sont la suite contemporaine. Le hack-and-leak (vol de données + publication orchestrée) est devenu un instrument standard de la guerre cognitive.

Le **financement** est l’objectif le plus caractéristique de la DPRK, mais d’autres acteurs l’emploient ponctuellement. **Lazarus** vole des crypto-actifs pour financer le programme nucléaire et balistique nord-coréen (Ch.30). Certaines opérations iraniennes ont inclus de la fraude financière pour contourner les sanctions. Ce mélange cybercrime/action étatique brouille les catégorisations classiques.

Ces objectifs ne sont pas exclusifs. Une opération APT29 classique combine espionnage (exfiltration de documents) et pré-positionnement (maintien d’accès). Une campagne Sandworm peut combiner espionnage (reconnaissance OT) et sabotage (wiper). L’analyste lit les TTP pour inférer les objectifs — et inversement, connaître les objectifs oriente l’investigation.

#### 1.4 Le vocabulaire terrain

Le vocabulaire APT a des nuances que les débutants confondent régulièrement. Les préciser évite des contresens d’analyse.

Un **intrusion set** est un ensemble d’activités malveillantes regroupées par TTP, infrastructure et victimologie communes. C’est ce que les vendors CTI appellent un « groupe APT » (APT29, Sandworm, etc.), mais c’est un **regroupement analytique**, pas forcément une seule équipe physique. L’intrusion set peut correspondre à une unité militaire précise (Sandworm = GRU Unit 74455), à un sous-ensemble d’opérateurs d’un service (APT29 regroupe plusieurs sous-groupes au sein du SVR), ou même à un consortium d’opérateurs partageant des outils (certains clusters chinois).

Un **cluster** est un regroupement préliminaire, pas encore attribué ou pas encore formellement promu au rang de groupe nommé. Mandiant utilise le préfixe **UNC** (Uncategorized) : UNC2452 était le cluster initial avant son identification comme APT29 dans l’affaire SolarWinds. Microsoft utilisait historiquement **DEV** (Developing) avant sa refonte en thèmes météo. Promouvoir un cluster en groupe nommé exige une convergence suffisante de TTP, d’infrastructure et d’objectifs dans le temps.

Une **campaign** (campagne) est une série d’intrusions liées par un objectif commun sur une période donnée. Une campagne peut être conduite par un seul groupe APT (campagne APT29 contre les ministères européens des affaires étrangères en 2023-2024) ou par plusieurs (campagne de ciblage des MSP — Managed Service Providers — impliquant APT10 et APT41 autour de 2016-2018).

Les **TTP** (Tactics, Techniques, Procedures) décrivent le « comment » de l’attaquant. Les **tactiques** sont les objectifs à haut niveau (gagner un foothold, établir la persistence). Les **techniques** sont les méthodes générales (phishing, DLL sideloading). Les **procédures** sont les implémentations spécifiques (utilisation d’un document Word avec une macro VBA spécifique, obfuscation par une méthode particulière). Les TTP sont plus durables que les IoC : un attaquant change facilement un hash de malware, rarement son tradecraft profond.

Le **tradecraft** est le savoir-faire opérationnel global : OPSEC, TTP, habitudes, réflexes, style. Un tradecraft mature est un marqueur d’acteur étatique professionnel. Reconnaître un tradecraft (la façon dont Turla compartimente son infrastructure, la manière dont APT29 abuse des services cloud légitimes) est l’un des exercices les plus sophistiqués de l’analyse CTI.

Les **IoC** (Indicators of Compromise) sont les artefacts techniques ponctuels : hash de fichier, adresse IP, domaine, clé de registre, chaîne de caractères. Les IoC vieillissent très vite (hash changé à chaque nouvelle compilation, IP brûlée dès qu’elle est signalée). Leur valeur tactique est immédiate, leur valeur stratégique est faible — d’où la **Pyramide de la Douleur** (David Bianco) qui hiérarchise les indicateurs par coût pour l’attaquant : les TTP sont tout en haut (coût élevé pour changer), les hashs sont tout en bas (coût nul). Cette pyramide structure toute la défense moderne (voir Ch.3).

#### 1.5 Le naming chaos : conventions par vendor

L’un des premiers obstacles de l’apprenant est le **naming chaos** : un même acteur peut avoir 5 à 10 noms différents selon le vendor CTI qui le désigne. Il n’existe pas d’autorité centrale de nommage — chaque éditeur utilise sa propre convention.

**Mandiant** (Google Cloud) utilise historiquement **APTxx** (pour les groupes étatiques attribués : APT28, APT29, APT41), **UNCxxx** (pour les clusters en attente), **FINxx** (pour les groupes financièrement motivés : FIN7, FIN8), et **TEMP.xxx** (préfixe temporaire).

**CrowdStrike** utilise des **animaux par pays** : Bear (Russie — Fancy Bear = APT28, Cozy Bear = APT29), Panda (Chine — Wicked Panda = APT41, Stone Panda = APT10), Chollima (DPRK — Stardust Chollima = APT38, Velvet Chollima = APT43), Kitten (Iran — Charming Kitten = APT35, Fox Kitten), Jackal (hacktivisme), Buffalo (Vietnam — OceanBuffalo = APT32), Crane (Corée du Sud), Spider (cybercrime — Scattered Spider, Wizard Spider).

**Microsoft** a refondu sa convention en 2023 autour de **thèmes météo par origine** : Blizzard (Russie — Midnight Blizzard = APT29, Forest Blizzard = APT28, Seashell Blizzard = Sandworm, Aqua Blizzard = Gamaredon, Secret Blizzard = Turla), Typhoon (Chine — Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon = APT41), Sleet (DPRK — Diamond Sleet = Lazarus, Sapphire Sleet = APT38, Emerald Sleet = Kimsuky), Sandstorm (Iran — Peach Sandstorm = APT33, Mint Sandstorm = APT35, Hazel Sandstorm = APT34, Mango Sandstorm = MuddyWater), Storm (cybercrime), Tempest (acteurs privés), Flood (DDoS).

**Kaspersky** utilise des noms variables et créatifs (Turla, Equation Group, BlueNoroff, ProjectSauron) sans convention systématique.

**Secureworks** utilise les **métaux par origine** : Bronze (Chine — Bronze Butler = Tick, Bronze President = Mustang Panda), Cobalt (Russie — Cobalt Mirage = Iran), Gold (cybercrime), Iron (Iran), Tin (DPRK).

**Palo Alto Networks / Unit 42** utilise des noms ciblés par nature (Stately Taurus, Fighting Ursa, Mushroom — plus descriptifs de TTP qu’organisés par pays).

L’**Annexe C** consolide les correspondances. Pour l’opérationnel : quand vous lisez un rapport, notez systématiquement le mapping vers APTxx (Mandiant) ou vers le nom Microsoft — ce sont les conventions les plus largement partagées.

#### 1.6 État des lieux quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement par l’écosystème CTI mondial. L’ordre de grandeur :

- **MITRE ATT&CK Groups** répertorie environ 160 groupes documentés publiquement (février 2026).
- **Malpedia** (Fraunhofer FKIE) référence plusieurs centaines de familles de malware attribuées à des acteurs étatiques.
- **CrowdStrike** déclare suivre plus de 230 acteurs (adversaires nommés, 2024 Global Threat Report).
- **Mandiant** suit plus de 300 intrusion sets dans son périmètre interne (dont beaucoup restent en UNC, non promus en APTxx publics).
- **Microsoft Threat Intelligence** publie une liste de plus de 150 threat actors nommés.

Deux implications pour l’analyste. La première : même un expert ne peut pas connaître en profondeur tous les groupes. La discipline consiste à **maîtriser les 30-40 groupes les plus actifs** (couverts par ce cours), puis à savoir **rechercher efficacement** les autres sur Mandiant, Microsoft TI, MITRE ATT&CK, Malpedia. La seconde : le nombre croît chaque année. La prolifération des capacités offensives (Ch.25) produit une fragmentation des acteurs — plus de contractors, plus de clusters éphémères, plus de difficultés d’attribution.

#### 1.7 Fil rouge — BLACKOUT Épisode 1

> **⚡ BLACKOUT — Épisode 1 : la détection**
> 
> **J+42** depuis la compromission initiale (inconnue à ce stade).
> 
> Le SOC de l’opérateur énergie européen reçoit une alerte de l’EDR sur un **poste d’ingénierie OT** situé sur un site de supervision en France. L’alerte indique un comportement anormal : `rundll32.exe` exécute une DLL non signée située dans `C:\ProgramData\Supervision\plugins\`, et un beaconing HTTPS régulier (toutes les 27 minutes, avec un jitter de ±3 minutes) vers un domaine hébergé derrière Cloudflare.
> 
> Le poste en question est un **double-connecté** : interface 1 sur le réseau IT bureautique (pour les mises à jour, les sessions administrateur), interface 2 sur le réseau de supervision SCADA. C’est un jump host typique — le point le plus sensible de l’architecture, par construction.
> 
> L’ingénieur SOC monte l’incident au CERT mandaté (un CERT privé français, qualifié PDIS par l’ANSSI). Les premières observations du CERT en triage rapide :
> 
> - Persistence via DLL sideloading d’une application de supervision légitime (`SupervisionCenter.exe` charge `plugin_common.dll` à chaque démarrage — la DLL est normalement signée, celle-ci ne l’est pas).
> - Pas de malware custom identifié après un scan initial — le C2 passe par HTTPS vers un domaine d’apparence légitime.
> - Pas de ransomware, pas d’exfiltration massive visible dans les logs réseau, pas de modification détectée sur les automates eux-mêmes.
> 
> **Premier diagnostic du CERT** : « Ce n’est pas un cybercriminel, pas un hacktiviste, pas un incident opportuniste. Le ciblage d’un poste OT, la persistence discrète, l’absence d’action visible, la patience — tous les signaux évoquent une APT en phase de reconnaissance ou de pré-positionnement. La question est : lequel, et pour quoi faire ? »
> 
> Le dossier BLACKOUT commence. Il faudra traverser les six parties suivantes pour le comprendre.

-----

### Chapitre 2 — Cycle de vie d’une intrusion APT

#### 2.1 Modèles de cycle : Kill Chain, Unified Kill Chain, ATT&CK

Plusieurs modèles structurent l’analyse d’une intrusion APT de bout en bout. Ils ne se contredisent pas ; ils offrent des vues complémentaires.

La **Cyber Kill Chain** (Lockheed Martin, 2011) propose sept phases linéaires : Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives. Simple, pédagogique, elle reste la référence conceptuelle d’entrée de gamme. Sa limite : elle suggère une progression linéaire, alors qu’une APT réelle fait des allers-retours (nouvelle reconnaissance interne après chaque étape, re-compromission si éjectée).

La **Unified Kill Chain** (Paul Pols, 2017) enrichit le modèle avec 18 phases couvrant aussi le mouvement latéral, la reconnaissance interne, les pivots vers de nouveaux réseaux, et la persistence multi-couches. Plus complète pour les intrusions sophistiquées, elle est moins pédagogique pour l’introduction mais plus fidèle à la réalité des APT.

**MITRE ATT&CK** (2013, enrichi continuellement) est le framework dominant aujourd’hui. Il organise les TTP en **14 tactiques** (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact, et — plus récentes — Reconnaissance et Resource Development). Chaque tactique contient de nombreuses **techniques** (200+ au total) et **sous-techniques** (400+). Pour chaque technique, ATT&CK documente les groupes qui l’utilisent, les malwares connus, les mitigations, et les détections. C’est à la fois un langage commun et une base de données. Dans la suite du cours, toutes les TTP sont référencées par leur identifiant ATT&CK (Txxxx).

ATT&CK couvre plusieurs matrices : **Enterprise** (Windows, Linux, macOS, cloud, containers — la plus complète), **Mobile** (iOS, Android), et **ICS** (systèmes industriels, voir Partie VI). Les matrices se complètent pour couvrir les attaques multi-environnements.

La suite du chapitre parcourt le cycle ATT&CK en l’enrichissant des spécificités APT.

#### 2.2 Reconnaissance et Resource Development

La **reconnaissance** (TA0043) est la phase où l’attaquant collecte de l’information sur la cible avant tout contact. Pour une APT étatique, cette phase dure des semaines à des mois et mobilise des sources variées : OSINT (LinkedIn pour identifier les employés et leur rôle, sites d’entreprise, conférences, presse), scan technique (Shodan, Censys pour l’infrastructure exposée), breach databases (credentials potentiellement réutilisables), et parfois HUMINT ou SIGINT quand l’acteur dispose de ces capacités.

Les APT les plus sophistiquées investissent lourdement dans la reconnaissance. APT29 est documenté pour avoir passé des mois à identifier les administrateurs SolarWinds avant la compromission initiale. APT35 (Iran) construit des profils d’ingénierie sociale extrêmement détaillés sur ses cibles (chercheurs, journalistes, dissidents) — jusqu’à des faux profils LinkedIn de « collègues » qui interagissent pendant des mois avant d’aborder l’objectif réel.

Le **Resource Development** (TA0042) est la phase où l’attaquant prépare son infrastructure et ses outils : acquisition de domaines (via des registrars permissifs, avec des identités fictives), mise en place des serveurs C2 (VPS chez des hébergeurs peu coopératifs, ou abus de services cloud légitimes), développement ou acquisition du malware, préparation des comptes d’opération (faux profils LinkedIn, faux comptes email pour le spear-phishing). Pour les APT matures, cette infrastructure est **compartimentée** : chaque opération a sa propre infrastructure, ce qui limite le risque de propagation d’une découverte.

#### 2.3 Accès initial : les vecteurs dominants 2024-2026

L’**Initial Access** (TA0001) est la phase où l’attaquant obtient son premier foothold. Cinq vecteurs dominent aujourd’hui.

**Phishing** (T1566) reste le vecteur statistiquement le plus fréquent. Le spear-phishing APT est très différent du phishing de masse : message personnalisé (fonction, projet en cours, relations), pretexte crédible (invitation à une conférence, message d’un faux collègue, notification d’un service légitime), leurre adapté (document Word avec macro, PDF avec exploit, lien vers un faux portail OAuth). APT29 a excellé dans le **phishing OAuth** — messages imitant des invitations Microsoft Teams ou des demandes d’autorisation d’application, qui, si acceptés, donnent à l’attaquant un accès persistant au compte sans avoir à voler de mot de passe.

**Exploitation d’appliances edge** (T1190) est devenue le vecteur n°1 des APT les plus sophistiquées depuis 2022-2023. Les VPN, firewalls, passerelles web et autres équipements exposés sur Internet sont des cibles privilégiées : ils ne supportent souvent pas d’EDR, leurs vulnérabilités sont exploitables massivement dès publication, et ils donnent un accès privilégié au réseau interne. Les vagues **Ivanti Connect Secure** (CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 en 2024), **Fortinet FortiOS** (multiples CVE 2022-2024), **Citrix ADC / NetScaler** (CVE-2023-4966 — Citrix Bleed), **Barracuda Email Security Gateway** (CVE-2023-2868 exploité par UNC4841/Chine pendant 8 mois), **Palo Alto GlobalProtect** (CVE-2024-3400) ont toutes été exploitées en vagues massives par des acteurs étatiques dans les heures ou jours suivant la publication.

**Supply chain compromise** (T1195) est la catégorie la plus sophistiquée. Elle a plusieurs variantes : compromission d’un éditeur logiciel pour injecter une backdoor dans son produit (SolarWinds / SUNBURST par APT29 — Ch.29 ; 3CX par Lazarus en 2023), compromission d’un MSP pour atteindre ses clients (Opération Cloud Hopper — APT10 sur des MSP internationaux), compromission de dépôts de code (attaques sur des dépendances npm, PyPI), compromission du pipeline de build (modification de binaires signés).

**Credential abuse** (T1078) exploite des credentials volés ou réutilisés. Les sources : breaches publiques (un employé utilise le même mot de passe sur un site compromis et sur son compte professionnel), **infostealers** (Lumma, RedLine, Vidar — qui volent les credentials stockés dans les navigateurs), password spray (essais automatisés de mots de passe faibles sur des comptes M365/Azure AD), **AitM** (Adversary-in-the-Middle phishing, avec outils comme Evilginx, qui capture aussi les cookies de session — permettant de contourner la MFA).

**Exploitation de vulnérabilités publiques** (T1190 aussi) sur des services web exposés (Exchange, OWA, SharePoint, logiciels métier exposés) reste un vecteur massif. Les vagues Exchange **ProxyLogon** (CVE-2021-26855, exploitée massivement par Hafnium / Chine en 2021) et **ProxyShell** (2021) ont compromis des dizaines de milliers d’organisations mondialement.

Le choix du vecteur dépend du niveau de sophistication de l’acteur, de sa patience, et du profil de la cible. Une APT sophistiquée contre une cible de haute valeur privilégiera supply chain ou exploit 0-day. Une APT opportuniste contre des cibles multiples privilégiera l’exploitation massive d’edge devices non patchés.

#### 2.4 Execution, persistence, privilege escalation

Une fois le foothold obtenu, l’attaquant doit **exécuter** son code sur la machine compromise, **persister** à travers les redémarrages et les éjections, et **escalader ses privilèges** pour accéder à plus de ressources.

L’**Execution** (TA0002) se fait via des méthodes qui varient en discrétion. Les plus sophistiquées privilégient la **Living off the Land** : exécuter du code via des outils légitimes du système plutôt qu’en déposant un binaire dédié. PowerShell (T1059.001), wmic (T1047), rundll32 (T1218.011), regsvr32 (T1218.010), mshta (T1218.005), cmd.exe avec des techniques d’obfuscation, Python/Perl interpréteurs sont les LOLBins (Living Off the Land Binaries) de référence. L’exécution sans dépôt sur disque (fileless) via PowerShell en mémoire ou via WMI event consumers est le standard APT moderne.

La **Persistence** (TA0003) doit survivre aux redémarrages et aux tentatives d’éradication. Les mécanismes courants incluent les **tâches planifiées** (T1053, Windows Task Scheduler ou Linux cron), les **services Windows** (T1543.003), les **clés de registre Run/RunOnce** (T1547.001), le **DLL sideloading** (T1574.002 — placer une DLL malveillante dans le répertoire d’une application légitime qui la charge au démarrage ; très utilisée par les APT chinoises), le **COM hijacking** (T1546.015), le **WMI event subscription** (T1546.003 — déclenchement à chaque événement système), et les **bootkits** (T1542 — persistence au niveau UEFI/BIOS, techniquement complexe mais ultra-résiliente).

Les APT les plus sophistiquées déploient de la **persistence multi-couches** : plusieurs mécanismes indépendants, sur des systèmes différents, pour garantir qu’un nettoyage partiel laisse un point de réinfection. APT29 est documenté pour avoir maintenu quatre mécanismes de persistence simultanés sur certaines compromissions importantes.

La **Privilege Escalation** (TA0004) vise à passer d’un compte limité à un compte administrateur local, puis à un compte de domaine, puis à des credentials de service ou à des comptes hautement privilégiés. Les techniques classiques : exploitation de vulnérabilités locales (Windows local privilege escalation — CVE récentes kernel, print spooler), abus de mauvaises configurations (AlwaysInstallElevated, services mal configurés avec permissions faibles), vol de tokens (T1134), DLL search order hijacking (T1574.001). Les privilèges obtenus conditionnent la suite : sans privilèges admin, l’attaquant est limité ; avec des privilèges de domaine, il peut aller quasiment partout.

#### 2.5 Defense evasion et credential access

La **Defense Evasion** (TA0005) est le théâtre principal de l’évolution du tradecraft APT. Les techniques se multiplient avec le renforcement des défenses.

**Obfuscation** (T1027) : brouiller le code pour échapper à la détection signature-based. Scripts PowerShell en base64, binaires packés, strings chiffrées, noms de fonctions randomisés. **Signed binary proxy execution** (T1218) : détourner des binaires Windows signés légitimes (rundll32, regsvr32, mshta, installutil, msiexec) pour exécuter du code malveillant — l’exécution apparaît comme provenant d’un binaire de confiance. **Process injection** (T1055) : injecter du code dans le processus d’une application légitime (explorer.exe, svchost.exe) — le malware n’a pas de processus visible distinct. **Timestomping** (T1070.006) : modifier les timestamps des fichiers pour échapper aux analyses temporelles. **Indicator removal** (T1070) : nettoyage des logs, suppression des traces, désactivation de la télémétrie EDR.

La **Credential Access** (TA0006) est une phase critique car elle conditionne le mouvement latéral. Les outils de référence sont bien connus mais évoluent constamment pour échapper aux EDR.

**Mimikatz** reste l’outil emblématique — extraction de credentials depuis la mémoire LSASS. **DCSync** (T1003.006) : simule un contrôleur de domaine pour récupérer les hashs de tous les comptes AD — devient possible dès qu’on dispose d’un compte avec les bons droits (Domain Admin, ou droits de réplication accordés). **Kerberoasting** (T1558.003) : demander des tickets Kerberos pour des comptes de service avec SPN, puis cracker les hashs hors ligne. **AS-REP Roasting** (T1558.004) : cibler les comptes qui ne nécessitent pas de pré-authentification Kerberos. **Credential dumping** de LSASS (T1003.001) directement via procdump, comsvcs.dll, ou des techniques récentes anti-EDR (NanoDump, SafetyKatz). **Cloud credential access** : vol de tokens SAML (GoldenSAML — forgeage de tokens SAML via la compromission d’ADFS, technique pivot de SolarWinds), abus d’Azure AD (vol de Primary Refresh Tokens, pass-the-cookie, abus d’applications OAuth sur-permissives).

La sophistication de la phase credential access distingue les APT modernes. Les acteurs de pointe (APT29, Sandworm) combinent plusieurs techniques en chaîne, testent les détections, et adaptent leur approche si l’EDR alerte.

#### 2.6 Discovery et lateral movement

Le **Discovery** (TA0007) est la reconnaissance interne au réseau de la victime. L’attaquant cartographie : comptes (net user, net group, AD enumeration via BloodHound / SharpHound), systèmes (net view, DNS enumeration), partages (net share), groupes privilégiés, trusts de domaine, chemins vers les cibles de valeur. **BloodHound** (outil open source, aussi utilisé par les red teamers légitimes) est devenu central : il modélise l’AD en graphe et révèle les chemins d’escalade les plus courts. Les APT sophistiquées l’utilisent couramment.

Le **Lateral Movement** (TA0008) déplace l’attaquant de la machine de foothold vers les cibles de valeur. Plusieurs techniques standards.

**Remote Services** (T1021) : RDP (T1021.001 — le plus courant), SMB/Admin Shares (T1021.002 — `\\target\C$`), WinRM, SSH. Utilisent des credentials légitimes obtenus en phase Credential Access. **PsExec** et **WMI remoting** exécutent des commandes à distance sur des machines du domaine. **Pass-the-Hash** (T1550.002) : authentification avec un hash NTLM sans avoir le mot de passe en clair. **Pass-the-Ticket** (T1550.003) : réutilisation d’un ticket Kerberos volé. **Overpass-the-Hash** : utiliser un hash NTLM pour obtenir un ticket Kerberos (contourne certaines limitations).

Les mouvements latéraux modernes sont **orientés identité** : plutôt que de pivoter machine-à-machine avec des credentials locaux, les attaquants compromettent des comptes de domaine privilégiés et utilisent leurs droits pour accéder aux ressources cibles. La compromission de comptes administrateurs de domaine ou de comptes de service permet un mouvement quasi illimité — d’où l’importance de la segmentation des comptes privilégiés (tiering AD).

Dans le cloud, le mouvement latéral prend des formes différentes : pivoter entre tenants M365 en abusant de relations de partage, se déplacer entre abonnements Azure, exploiter des relations de confiance fédérées SAML.

#### 2.7 Collection, Command and Control, Exfiltration

La **Collection** (TA0009) rassemble les données d’intérêt. Pour une APT d’espionnage, ce sont des documents (Office, PDF), des emails (Exchange, O365), des bases de données, des dumps d’AD, des artefacts de messagerie, des fichiers de code source. Les données sont stagées localement (T1074) — rassemblées dans un répertoire de collecte avant l’exfiltration — et souvent compressées et chiffrées pour faciliter le transfert.

Le **Command and Control** (TA0011) est le canal par lequel l’attaquant contrôle ses implants et reçoit les données. Les C2 modernes ont évolué massivement depuis les années 2010.

**HTTPS mimicry** (T1071.001) : C2 transitant par HTTPS vers des domaines qui imitent des services légitimes (cdn-microsoft-updates.com, office365-patches.net). Catégorisation automatique des domaines côté défense, d’où l’innovation constante côté attaquant. **Domain fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN) pour masquer la destination réelle — technique moins efficace aujourd’hui car les CDN ont restreint la pratique. **Abus de services cloud légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Dropbox comme canaux C2. APT29 est documenté pour abuser de Microsoft OneDrive et Google Drive. **DNS tunneling** (T1071.004) : encoder les communications dans des requêtes DNS — lent mais très difficile à bloquer. **Routeurs SOHO compromis** : Volt Typhoon et APT28 (MooBot campaign) ont construit des botnets de routeurs résidentiels pour faire sortir le trafic C2 depuis des IP résidentielles légitimes — rendant la détection réseau extrêmement difficile.

Le **beaconing** est le pattern caractéristique du C2 APT : l’implant « appelle » à intervalles réguliers (chaque X minutes, avec un jitter pour éviter la détection par périodicité) pour recevoir des ordres. Les intervalles sont longs pour les opérations patientes (30 minutes à 24 heures), courts pour les actions en cours (quelques secondes à quelques minutes). La détection du beaconing repose sur l’analyse statistique des patterns temporels — un domaine consulté à intervalles réguliers est suspect, même si le domaine lui-même n’est pas sur liste noire.

L’**Exfiltration** (TA0010) extrait les données collectées. Elle peut utiliser le même canal que le C2 (T1041 — Exfiltration Over C2), un canal alternatif (T1048 — webshell séparé, upload vers un service cloud), ou des supports physiques si l’accès permet (T1052 — rare en pratique APT).

Les APT sophistiquées maîtrisent l’art du **low and slow** : exfiltration étalée dans le temps, à faible débit, pendant les heures de bureau (pour se fondre dans le trafic légitime), par petits volumes. Exfiltrer 10 Go en continu sur quelques heures est détectable ; exfiltrer 100 Mo chaque jour pendant 3 mois est beaucoup moins.

#### 2.8 Impact : espionnage silencieux, destruction, pré-positionnement

La phase **Impact** (TA0040) est l’objectif final. Pour une APT d’espionnage, l’impact est paradoxalement **invisible** : les données ont été collectées et exfiltrées, la cible continue ses activités normales sans le savoir. Pour une APT destructive, l’impact est brutal : wiper qui efface les disques (NotPetya, Shamoon), manipulation OT qui provoque un blackout (Industroyer), chiffrement ransomware déployé par un acteur étatique (Iran contre Albanie 2022 — wiper+ransomware combinés).

Pour une APT de pré-positionnement (Volt Typhoon, Sandworm sur les infras critiques européennes), la phase Impact n’est **pas encore activée**. L’attaquant maintient l’accès et attend un déclencheur (conflit, ordre politique, escalade). Cette configuration — intrusion complète sans impact visible — est la plus difficile à détecter et la plus lourde de conséquences stratégiques. C’est l’enjeu central de la Partie VI.

#### 2.9 Spécificités APT dans ce cycle

Comparé à un incident de cybercrime opportuniste, une intrusion APT se caractérise par quelques spécificités transversales au cycle.

**Durée** : l’APT investit dans le temps. Une intrusion ransomware typique passe de l’accès initial à l’impact en quelques jours à quelques semaines. Une intrusion APT d’espionnage dure des mois à des années, avec des phases d’activité et de dormance.

**OPSEC** : l’APT sophistiquée ne fait pas de bruit. Elle limite ses actions aux minimums nécessaires, évite les outils bruyants, efface ses traces, et adapte son comportement à ce qu’elle détecte de la défense.

**Adaptation** : quand l’APT est détectée ou éjectée d’une partie du réseau, elle revient via ses accès redondants, change de TTP, modifie son infrastructure. L’éradication complète nécessite une réponse coordonnée — d’où la règle « scope before contain » (Ch.28).

**Objectif stratégique** : l’APT ne monétise pas. Elle collecte du renseignement, prépare un levier, ou dégrade une capacité adverse. Cela implique que l’analyse ne peut pas s’arrêter à la technique — comprendre l’objectif stratégique est indispensable pour calibrer la réponse (Ch.32 BLACKOUT).

-----

### Chapitre 3 — Tradecraft et TTP : le comment opérationnel

#### 3.1 La Pyramide de la Douleur

La **Pyramide de la Douleur** (David Bianco, 2013) hiérarchise les indicateurs défensifs par leur coût pour l’attaquant quand ils sont brûlés.

|Niveau                  |Type d’indicateur   |Coût pour l’attaquant                                 |Durée de vie    |
|------------------------|--------------------|------------------------------------------------------|----------------|
|Base (peu douloureux)   |Hash de fichier     |Trivial (recompiler)                                  |Minutes à heures|
|                        |IP                  |Faible (changer de VPS)                               |Heures à jours  |
|                        |Nom de domaine      |Faible (acheter un nouveau)                           |Jours à semaines|
|                        |Artefact réseau/hôte|Modéré (adapter l’implant)                            |Semaines à mois |
|                        |Outils              |Fort (développer de nouveau)                          |Mois à années   |
|Sommet (très douloureux)|TTP / tradecraft    |Maximum (changer les pratiques, former les opérateurs)|Années          |

La leçon défensive fondamentale : **détecter des hashes et des IP, c’est imposer une gêne d’une journée à l’attaquant. Détecter des TTP, c’est imposer un coût qui peut lui prendre des mois à absorber.** La CTI moderne oriente l’effort vers le haut de la pyramide — c’est pour cela qu’ATT&CK est devenu le langage partagé.

Pour l’analyste APT, cela signifie : un IoC (hash, IP) est utile pour une détection immédiate, mais le renseignement qui produit une valeur durable est la description des TTP. Un rapport CTI qui liste 50 hashes a peu de valeur dans trois mois ; un rapport qui décrit précisément comment APT29 abuse des tokens SAML reste utile cinq ans.

#### 3.2 Living off the Land (LotL)

Le **Living off the Land** est la pratique qui consiste à atteindre ses objectifs en utilisant exclusivement les outils légitimes présents sur le système, sans déposer de malware custom. L’avantage est la discrétion — aucun binaire suspect à détecter par signature. L’inconvénient est la traçabilité : les commandes restent loguées, et la détection se fait par anomalie comportementale.

Les **LOLBins** sont les binaires Windows qui peuvent être détournés : rundll32, regsvr32, mshta, msiexec, installutil, wmic, PowerShell, cmd, certutil, bitsadmin, schtasks, sc.exe. Le projet **LOLBAS** (lolbas-project.github.io) maintient un catalogue exhaustif avec les techniques de détournement.

Le **LotL total** (zéro malware custom) est le standard des APT les plus sophistiquées. **Volt Typhoon** est l’exemple canonique : aucun binaire malveillant identifié sur les cibles, tout passe par LOLBins + credentials légitimes. **APT29** pratique un LotL partiel — malware custom en phase 2, mais LotL en mouvement latéral et en phase d’exploration. **Sandworm** utilise davantage de malware custom (wipers, outils OT dédiés) car ses objectifs destructifs imposent des capacités spécifiques.

Pour la défense, le LotL déplace l’effort vers la **détection comportementale** : surveiller les utilisations anormales des LOLBins (PowerShell exécuté depuis un processus inhabituel, rundll32 avec des paramètres suspects, certutil utilisé pour télécharger un fichier — un usage rare pour cet outil administratif).

#### 3.3 Credential access : l’arsenal moderne

Le credential access mérite un traitement détaillé car c’est la phase la plus sensible et la plus défendable.

**Mimikatz** (Benjamin Delpy, 2011) est l’outil emblématique — extraction de credentials depuis LSASS, génération de Golden Tickets et Silver Tickets, Pass-the-Hash, Pass-the-Ticket, DCSync. Détecté par les EDR modernes, il est souvent remplacé par des **réimplémentations furtives** : NanoDump (dump de LSASS en évitant les méthodes surveillées), SafetyKatz (Mimikatz refondu en C#), Rubeus (Kerberos-focused), Impacket (Python toolkit complet utilisé par quasi tous les opérateurs offensifs).

**DCSync** (T1003.006) : technique qui simule un contrôleur de domaine demandant une réplication, pour récupérer les hashs NTLM de tous les comptes du domaine. Nécessite les droits de réplication (Replicating Directory Changes / Replicating Directory Changes All). Une fois le DCSync réussi, l’attaquant a les hashs de tous les comptes, y compris le compte KRBTGT — qui permet les Golden Tickets.

**Golden Ticket** (T1558.001) : forgeage d’un ticket Kerberos TGT valide en utilisant le hash du compte KRBTGT. Résultat : l’attaquant peut s’authentifier comme n’importe quel utilisateur, avec une validité de 10 ans par défaut, sans jamais avoir à interagir avec le contrôleur de domaine pour s’authentifier. Contrer un Golden Ticket nécessite de changer le mot de passe KRBTGT deux fois — opération lourde, souvent retardée.

**Silver Ticket** (T1558.002) : forgeage d’un ticket Kerberos de service pour un service spécifique, en utilisant le hash du compte de service. Moins puissant qu’un Golden Ticket mais moins détectable (ne sollicite pas le DC).

**Kerberoasting** (T1558.003) : demander des tickets Kerberos (TGS) pour des comptes de service ayant un SPN, puis cracker les hashs hors ligne. Fonctionne si les comptes de service ont des mots de passe faibles — ce qui est fréquent historiquement. Défense : mots de passe forts pour les comptes de service (ou managed service accounts).

**AS-REP Roasting** (T1558.004) : cibler les comptes qui n’exigent pas de pré-authentification Kerberos (setting « Do not require Kerberos preauthentication »). Pour ces comptes, un attaquant peut demander directement un AS-REP chiffré avec le hash du compte, et le cracker hors ligne. Défense : éliminer le setting sauf usage documenté.

**Pass-the-Hash** (T1550.002) : s’authentifier avec un hash NTLM sans jamais avoir le mot de passe en clair. Fonctionne pour des services qui acceptent NTLM.

**Pass-the-Ticket** (T1550.003) : réutiliser un ticket Kerberos volé sur une autre machine.

**Overpass-the-Hash** : utiliser un hash NTLM pour demander un ticket Kerberos — permet de passer de NTLM à Kerberos quand seule la deuxième authentification est acceptée.

**Dans le cloud**, l’arsenal évolue : vol de **Primary Refresh Tokens** (Azure AD), **Golden SAML** (forgeage de tokens SAML via compromission d’ADFS — pivot de SolarWinds), vol de cookies de session (**pass-the-cookie** — contourne la MFA en réutilisant des sessions authentifiées), abus d’**applications OAuth** sur-permissives (technique APT29 récurrente).

#### 3.4 Persistence moderne

La persistence moderne va bien au-delà des clés Run/RunOnce classiques.

**DLL Sideloading** (T1574.002) : placer une DLL malveillante dans le même répertoire qu’une application légitime qui la charge par défaut au lancement. L’application légitime exécute la DLL, qui est donc exécutée dans le contexte du processus légitime. Les APT chinoises en font un usage massif — il est difficile à détecter car la DLL n’est pas exécutée directement, elle est chargée par un processus signé et de confiance.

**COM Hijacking** (T1546.015) : détourner une clé de registre COM pour pointer vers un CLSID malveillant, qui sera chargé quand un composant COM légitime est invoqué par une application Windows normale.

**WMI Event Subscription** (T1546.003) : créer un consommateur WMI qui se déclenche sur un événement système (démarrage, connexion utilisateur, à une heure précise). Exécute le code malveillant sans fichier persistant facilement identifiable.

**Scheduled Tasks** (T1053) : tâches planifiées Windows, avec des mécanismes récents de création sans écrire dans le registre visible (Task Scheduler 2.0 COM interfaces).

**Service Creation / Modification** (T1543.003) : créer un service Windows qui exécute le malware à chaque démarrage, ou modifier un service existant. Techniques avancées : modifier le ServiceDll d’un service svchost.exe existant.

**Scheduled Tasks avec déclencheurs inhabituels** : tâches déclenchées à la connexion d’un périphérique USB, à une heure précise, à un événement du journal système.

**Bootkits / Rootkits UEFI** (T1542) : persistence au niveau du firmware. Survit à la réinstallation complète de l’OS. Techniquement complexe mais démontré par Turla (MoonBounce), CosmicStrand (groupe chinois suspecté), LoJax (APT28). Extrêmement difficile à détecter et éliminer — la machine doit être physiquement reflashée.

**Cloud persistence** : création de comptes de service Azure AD avec permissions étendues, enregistrement d’applications OAuth avec consentement administrateur, ajout de comptes aux rôles privilégiés d’Entra ID. Une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints.

#### 3.5 Defense evasion

La defense evasion évolue en symbiose avec les EDR et les mécanismes de détection.

**Obfuscation** (T1027) à plusieurs niveaux : scripts PowerShell en base64 (détecté par beaucoup d’EDR aujourd’hui, donc combiné avec d’autres techniques), obfuscation XOR, chiffrement AES des payloads, strings chiffrées dans les binaires, noms de variables et fonctions randomisés, control-flow flattening.

**Signed Binary Proxy Execution** (T1218) : détourner des binaires Windows signés pour exécuter du code malveillant. Outil de référence : InstallUtil.exe, MSBuild.exe, RegAsm.exe, rundll32.exe, mshta.exe. L’exécution apparaît comme provenant d’un binaire légitime signé par Microsoft, ce qui contourne beaucoup de contrôles.

**Process Injection** (T1055) : injecter du code dans un processus légitime déjà en cours (explorer.exe, svchost.exe, un processus Office). Variantes techniques : classic DLL injection, reflective DLL injection, process hollowing, AtomBombing, Early Bird APC injection, Module Stomping. Chaque nouvelle technique cherche à échapper aux contrôles EDR de la génération précédente.

**EDR Bypass** : désactivation de l’EDR via des privilèges élevés, exploitation de vulnérabilités dans les drivers EDR eux-mêmes (technique « Bring Your Own Vulnerable Driver » — BYOVD, où l’attaquant déploie un driver signé mais vulnérable pour obtenir un contexte kernel et désactiver l’EDR). Cas célèbre : **RTCore64.sys** exploité par plusieurs acteurs, **PROCEXP.SYS** (un driver Sysinternals abusé), **Ryuk** et d’autres groupes ransomware ont utilisé BYOVD systématiquement.

**Timestomping** (T1070.006) : modifier les timestamps des fichiers malveillants pour qu’ils ressemblent à des fichiers système anciens, échappant aux analyses temporelles des investigateurs.

**Log Clearing** (T1070.001) : nettoyage des logs Windows (Security, System, Application, Sysmon). Détectable si les logs sont exfiltrés en temps réel vers un SIEM — d’où l’importance du log forwarding.

**Masquerading** (T1036) : nommer les fichiers malveillants avec des noms de binaires légitimes (svchost.exe placé dans un répertoire non standard, fichier malveillant nommé « Microsoft Update »), ou modifier les métadonnées (champ Description, CompanyName).

**Anti-forensics** : détection de sandbox / VM (l’implant refuse de s’exécuter si l’environnement ressemble à une sandbox analyste), effacement auto après un délai si pas de C2 reçu, mécanismes de kill switch.

#### 3.6 Command and Control moderne

Le C2 moderne a évolué pour rendre la détection réseau beaucoup plus difficile.

**HTTPS comme standard** : la quasi-totalité des C2 APT passent par HTTPS, avec des certificats Let’s Encrypt (gratuits, faciles à obtenir). Le contenu est chiffré, seul le domaine/SNI et les patterns de trafic sont visibles au défenseur sans déchiffrement.

**Catégorisation des domaines** : les attaquants enregistrent des domaines plausibles (lookalike des marques connues, domaines techniques type `cdn-updates-microsoft.net`, domaines dans des TLD peu surveillés). Les domaines récents sont suspects, d’où la mise en **aging** — l’acteur enregistre un domaine, le laisse « vieillir » plusieurs mois sans activité, puis l’active.

**Domain Fronting** (T1090.004) : faire transiter le C2 via un CDN légitime (Fastly, Akamai, Azure CDN, AWS CloudFront), en exploitant le fait que les CDN routent le trafic basé sur le header Host HTTPS après le déchiffrement SNI. L’attaquant voit le trafic partir vers `cdn-legitimate.com`, mais le backend reçoit et répond via le C2 réel. Technique massivement utilisée entre 2015 et 2018 ; largement restreinte depuis par les CDN majeurs qui bloquent le domain fronting.

**Abus de services légitimes** (T1102) : utiliser Slack, Discord, Telegram, GitHub, Pastebin, Google Drive, OneDrive, Dropbox comme canaux C2. Le trafic semble légitime, les domaines sont blanc-listés par défaut. APT29 excelle dans cette technique — leur malware FoggyWeb communiquait via des cookies Exchange bien calibrés. Des implants récents utilisent des canaux Discord pour recevoir leurs commandes.

**DNS Tunneling** (T1071.004) : encoder les données dans les requêtes DNS (particulièrement les requêtes TXT et CNAME). Lent (limité par la taille des enregistrements et le throughput DNS), mais très difficile à bloquer car le DNS doit rester fonctionnel pour le réseau. Souvent utilisé comme canal secondaire en cas de blocage du canal primaire.

**Routeurs SOHO compromis comme relais** : **Volt Typhoon** a construit un botnet de routeurs résidentiels compromis (Cisco RV, Fortinet, NetGear, ASUS). Le trafic C2 des implants transite via ces routeurs — apparaissant depuis des IP résidentielles aux États-Unis ou en Asie, fondant le trafic malveillant dans le trafic domestique. Détection très difficile. Démantèlement partiel par le FBI en janvier 2024, mais le modèle se reproduit. **APT28** a utilisé la même approche avec son botnet **MooBot** démantelé en février 2024.

**Beaconing** : le pattern temporel est caractéristique. Interval de 30 minutes à 24 heures pour les opérations patientes ; quelques secondes pour l’interactif. **Jitter** (variation aléatoire) ajouté pour éviter la détection par analyse de périodicité. La détection statistique du beaconing (RITA, machine learning sur les timeseries de connexions) est une parade efficace — d’où les attaquants expérimentent des patterns moins réguliers (beacon irrégulier, synchronisation avec les horaires de travail pour se fondre).

#### 3.7 OPSEC des attaquants sophistiqués

L’OPSEC distingue l’APT mature de l’amateur.

**Infrastructure compartimentée** : chaque opération a sa propre infrastructure C2, ses propres domaines, ses propres identités fictives. Une compromission découverte sur une cible ne propage pas le risque aux autres opérations. APT29 et Turla sont documentés pour cette pratique.

**Infrastructure renouvelable** : les domaines, IP, certificats sont prévus pour être jetables. Quand une infrastructure est brûlée publiquement, l’opérateur migre vers une infrastructure de remplacement déjà préparée.

**Opérateurs formés** : les APT matures ont des opérateurs entraînés, qui connaissent les techniques récentes, testent leurs actions avant de les déployer, et évitent les erreurs de débutant. Les services étatiques investissent dans la formation continue.

**Séparation des rôles** : développeurs de malware, opérateurs d’intrusion, analystes du renseignement collecté sont des rôles distincts. Le développeur ne sait pas quelle cible utilisera son implant ; l’opérateur ne voit pas le renseignement final. Cette compartimentation limite l’impact d’une trahison ou d’une infiltration.

**Heures de travail** : les opérateurs étatiques travaillent à des heures de bureau du pays sponsor. Les analyses timing ont permis d’identifier des fuseaux horaires : APT29 travaille aux heures de Moscou, les APT chinoises aux heures de Pékin (avec des variations selon les bureaux régionaux MSS), Lazarus aux heures de Pyongyang. Ce signal, seul, n’est pas probant — il peut être manipulé — mais il contribue au faisceau d’attribution.

**Langage et artefacts culturels** : les commentaires dans le code, les noms de variables, les chaînes de debug trahissent parfois la langue maternelle de l’opérateur. Les APT sophistiquées nettoient systématiquement ces artefacts, mais les erreurs arrivent.

#### 3.8 L’ATT&CK framework en pratique

ATT&CK est à la fois un langage commun et une base de connaissance exploitable opérationnellement.

**Lire une matrice ATT&CK** : les colonnes sont les 14 tactiques (objectifs adversaires), les lignes sous chaque colonne sont les techniques et sous-techniques. Une intrusion est « cartographiée » en sélectionnant les techniques effectivement observées.

**Utiliser ATT&CK pour la défense** : mapper les détections existantes (quelles techniques votre SIEM/EDR/NDR détecte déjà, avec quelle fiabilité), identifier les **gaps** (quelles techniques importantes ne sont pas détectées), construire un **détection roadmap** priorisé par fréquence d’usage et impact. Des outils comme **ATT&CK Navigator** permettent la visualisation interactive.

**Prioriser par acteur** : les techniques utilisées par les acteurs pertinents pour votre secteur/géographie sont à prioriser. Si vous êtes un opérateur énergie européen, les TTP de Sandworm, Volt Typhoon, et certains clusters chinois sont plus importantes que les TTP d’APT32 (Vietnam) ou d’un groupe régional ciblant l’Amérique latine. **ATT&CK Groups** liste pour chaque groupe les techniques documentées — point de départ pour une priorisation.

**Ingérer les rapports CTI via ATT&CK** : un bon rapport CTI d’incident référence les TTP observées par leur identifiant ATT&CK. Cela permet de confronter rapidement les TTP au profil connu de groupes, et de construire des détections transférables d’un incident à l’autre.

**Les matrices spécialisées** : ATT&CK ICS (pour l’OT, voir Ch.20-21), ATT&CK Mobile (pour iOS/Android), ATT&CK Cloud (intégré à Enterprise mais avec des techniques spécifiques par plateforme). À chaque environnement sa grammaire.

La maturité CTI d’une organisation se mesure notamment à sa capacité à parler ATT&CK : non seulement connaître les techniques, mais les utiliser pour prioriser défenses, détections, exercices, et communications avec les partenaires.

-----

### Chapitre 4 — Le cyber comme instrument de puissance étatique

#### 4.1 Le modèle DIMEFIL et la place du cyber

Les analystes stratégiques classifient les instruments de puissance étatique selon le modèle **DIMEFIL** : Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement. Le cyber n’est pas une catégorie à part — il est un **instrument transverse** qui traverse tous les autres.

**Diplomatique** : attribution publique, sanctions ciblées, indictments, négociations de normes internationales (GGE, OEWG), expulsions d’opérateurs diplomatiques.

**Information** : opérations d’influence, hack-and-leak, désinformation coordonnée, contre-narratif, défense de la souveraineté informationnelle.

**Militaire** : opérations cyber offensives en soutien d’opérations conventionnelles (guerre en Ukraine), préparation du champ de bataille cyber, pré-positionnement dans les infrastructures adverses, défense cyber des systèmes militaires.

**Économique** : vol de propriété intellectuelle industrielle (espionnage économique systémique chinois), sabotage de concurrents, perturbation de chaînes d’approvisionnement.

**Financier** : cybervol pour financement étatique (DPRK), blanchiment via crypto, contournement de sanctions.

**Intelligence** : collecte cyber d’origine (SIGINT, CYBINT), pénétration de réseaux gouvernementaux adverses, collecte HUMINT facilitée par le cyber (profilage via OSINT, social engineering).

**Law Enforcement** : coopération internationale contre la cybercriminalité, extraterritorialité, saisies d’infrastructure (démantèlements Emotet, Qakbot, Hydra), exploitation judiciaire du cyber contre des menaces internes.

Chaque État dote son cyber d’une **combinaison spécifique** de ces instruments, qui reflète ses priorités et sa culture stratégique. La Russie intègre massivement le cyber dans l’information et le militaire. La Chine le concentre sur l’économique et le politique. La DPRK sur le financier. Les États-Unis sur l’intelligence, le diplomatique et le law enforcement. Israël sur le militaire et l’intelligence. Comprendre ces profils — ce que fait chaque Partie II à V — oriente l’analyse d’une cyberopération observée.

#### 4.2 Doctrines comparées : vue d’ensemble

Les doctrines cyber divergent entre blocs, et même au sein de blocs. Avant d’entrer dans le détail par pays, une vue d’ensemble fixe les repères.

**Doctrine russe** : la guerre hybride (gibridnaya voyna) intègre le cyber dans un continuum information/cyber/militaire. Pas de séparation nette entre espionnage, influence et sabotage — un même service (le GRU) mène les trois. La sophistication varie selon les services (SVR ultra-furtif, GRU destructif, FSB hétérogène). La tolérance au bruit destructif est la plus élevée de tous les blocs.

**Doctrine chinoise** : le long game. Le cyber sert d’abord l’espionnage économique massif (propriété intellectuelle, rattrapage technologique) et le pré-positionnement stratégique. Pas de destructif massif documenté (à l’exception de la période Unit 61398 avant sa réorganisation post-2014). Sophistication croissante, fragmentation croissante entre services officiels (MSS, PLA) et contractors civils. Long time preference : mois et années d’attente avant d’activer les accès.

**Doctrine nord-coréenne** : le cyber comme arme économique. RGB (Reconnaissance General Bureau) mène espionnage, destruction ponctuelle (rare), et surtout vol massif (crypto, SWIFT). Unique dans son ampleur : c’est le seul État qui finance son régime et son programme d’armement par le cybervol.

**Doctrine iranienne** : rivalité régionale et surveillance interne. Cyber centré sur Israël, Golfe, dissidents. Destructif ponctuel (wipers comme substitut aux opérations conventionnelles). Social engineering très sophistiqué (APT35). Sophistication en croissance, mais en retrait par rapport aux quatre acteurs de pointe (US, Israël, Russie, Chine).

**Doctrine américaine** : defend forward / persistent engagement. Agir en continu dans les réseaux adverses pour dégrader leurs capacités, pas seulement défendre. Cyber intégré au renseignement (NSA), au militaire (USCYBERCOM), et au law enforcement (FBI). Usage massif du droit et de l’attribution publique comme instrument diplomatique.

**Doctrine israélienne** : préemption et supériorité technologique. Cyber comme espace d’action permanent, pas réponse à agression. Intégration militaire-renseignement-privé unique. Exportation des capacités via le marché commercial (NSO, Intellexa, Candiru).

**Doctrine britannique** : disruption coordonnée avec les Five Eyes. Modèle NCSC de protection nationale influent. National Cyber Force (2020) pour les opérations offensives dédiées.

**Doctrine française** : lutte informatique offensive / défensive / d’influence (LIO/LID/L2I), officialisée en 2019. Cadre clair, capacités croissantes, ambition d’autonomie stratégique.

Ces doctrines ne sont pas hermétiques — elles évoluent, elles s’influencent (la doctrine russe de guerre hybride a inspiré certaines réflexions chinoises ; le defend forward américain a influencé le Royaume-Uni et l’Australie). Mais elles fixent des répères durables qui permettent d’interpréter une cyberopération observée.

#### 4.3 Le cyberespace comme 5ème domaine

Depuis le sommet OTAN de Varsovie (2016), le cyberespace est reconnu comme le **5ème domaine d’opérations**, après la terre, la mer, l’air et l’espace. Cette reconnaissance formalise ce qui était déjà une réalité opérationnelle depuis 2007-2010 : le cyber est un espace de confrontation militaire.

Les particularités du cyberespace comme domaine :

**Asymétrie** : un petit État peut infliger des dommages significatifs à un grand. La DPRK, avec un PIB de 30 milliards de dollars, a réalisé des vols crypto dépassant ses exportations légales. L’Iran et la Russie ont infligé des pertes industrielles se chiffrant en milliards à des économies bien plus importantes.

**Déni plausible** : l’attribution est techniquement difficile et politiquement coûteuse. Un État peut mener une opération cyber et nier publiquement pendant des années. Cette caractéristique favorise les opérations dans la zone grise (en dessous du seuil du conflit armé).

**Zone grise** : le cyber permet d’agir en dessous du seuil traditionnel du conflit armé. Des actions qui, dans le monde physique, appelleraient une réponse militaire (sabotage d’une centrale, espionnage d’un état-major) sont courantes dans le cyber avec des réponses politiques/diplomatiques seulement.

**Vitesse** : une action cyber peut se dérouler en minutes ou en heures ; une réponse diplomatique coordonnée prend des mois. Cette asymétrie temporelle favorise l’attaquant.

**Continuum** : les frontières entre espionnage, pré-positionnement, sabotage et guerre sont floues. Un même accès peut servir à l’espionnage aujourd’hui et au sabotage demain. La reconnaissance de Volt Typhoon comme pré-positionnement implique que la Chine est **déjà** en phase de préparation militaire dans les réseaux américains — sans avoir franchi aucun seuil traditionnel.

**Dual-use** : les outils cyber sont massivement dual-use. Un outil légitime de pentest (Cobalt Strike, Metasploit, Empire) est utilisé par des opérateurs autorisés et par des attaquants. Un outil comme BloodHound est utilisé par les red teams défensives et par les APT. Cette caractéristique complique la régulation export et l’attribution.

#### 4.4 Ce que les APT révèlent des intentions étatiques

La lecture géopolitique des campagnes APT est une compétence à part entière. Elle consiste à inférer les priorités stratégiques d’un État à partir des cibles qu’il attaque.

**Victimologie comme signal** : si une APT attribuable à la Chine cible systématiquement des chercheurs en semiconducteurs, on peut inférer la priorité au rattrapage technologique dans ce domaine. Si elle cible la diaspora ouïghoure, on peut inférer la priorité au contrôle politique interne projeté à l’étranger. Si APT35 (Iran) cible des chercheurs spécialisés sur le nucléaire iranien, on peut inférer la priorité à la contre-surveillance du programme national.

**Timing comme signal** : les campagnes cyber suivent souvent les évolutions politiques et militaires. Le ciblage intensifié de l’Ukraine par les groupes russes post-2022, les campagnes iraniennes post-assassinat Soleimani (2020), le ciblage chinois des think tanks Taïwan lors des élections présidentielles sont des signaux doctrinaires lisibles.

**Escalation comme signal** : le passage de l’espionnage au destructif marque une escalade. Le passage du destructif ciblé au destructif mass-market (NotPetya) marque un seuil. Le pré-positionnement massif dans les infras critiques étrangères (Volt Typhoon) marque une préparation stratégique.

**Silence comme signal** : l’absence prolongée d’activité d’un groupe très actif peut signaler une réorganisation interne, un changement de mandat, ou la préparation d’une opération majeure à venir. APT10 a eu des périodes silencieuses corrélées à des réorganisations du MSS chinois.

Pour l’analyste APT, ces signaux doivent être lus prudemment. Les biais de confirmation, les fausses corrélations, et la manipulation délibérée (false flags) peuvent tromper. La règle : une hypothèse géopolitique doit être étayée par plusieurs signaux indépendants et confrontée à des hypothèses alternatives (ACH — voir Ch.24).

#### 4.5 Fil rouge — BLACKOUT Épisode 2

> **⚡ BLACKOUT — Épisode 2 : pourquoi un opérateur énergie ?**
> 
> Le CERT élargit le cadrage de l’analyse. La question « qui attaque ? » ne peut pas être répondue sans d’abord répondre à « pourquoi cette cible ? »
> 
> **Profil de la victime** : opérateur de distribution d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), classement OIV en France (arrêté sectoriel énergie), entité essentielle NIS 2. Infrastructure de supervision SCADA reliée à plusieurs dizaines de postes de transformation haute tension. Pas de position publique politique marquée ; pas de contentieux notable avec des acteurs étatiques ; pas de rôle spécifique dans le soutien à l’Ukraine (au-delà de la solidarité européenne générale).
> 
> **Secteur d’activité** : l’énergie est un secteur **stratégique structurel**. Les cibles énergie sont attaquées par :
> 
> - **La Russie (Sandworm)** : doctrine de guerre hybride, ciblage énergie documenté depuis 2015 en Ukraine, extension à l’Europe dans le contexte du conflit ukrainien. Objectif : démonstration de capacité, pré-positionnement pour sabotage en cas d’escalade.
> - **La Chine (Volt Typhoon et clusters similaires)** : doctrine de pré-positionnement stratégique, ciblage énergie documenté aux US et dans le Pacifique (Guam), extension possible à l’Europe dans le contexte Taïwan. Objectif : capacité de dissuasion / représailles.
> - **L’Iran (groupes IRGC)** : ciblage énergie dans le contexte régional, moins présent en Europe. Objectif : démonstration de portée régionale, parfois représailles pour sanctions.
> - **Les cybercriminels** : énergie = cible à fort ROI pour ransomware (Colonial Pipeline 2021 a démontré que les opérateurs paient vite). Mais ici, pas de ransomware — élimine cette hypothèse.
> - **Les hacktivistes** : possible si le contexte politique le justifie. Ici, pas de signal hacktiviste évident — élimine cette hypothèse (pour l’instant).
> 
> **Diagnostic intermédiaire** : le profil cible + l’absence d’intention monétaire + la patience opérationnelle + le positionnement OT orientent vers **une APT étatique en phase de pré-positionnement**. Les candidats principaux sont **Sandworm (Russie)** et **Volt Typhoon ou cluster chinois similaire**. L’Iran est moins probable pour des raisons géographiques et doctrinaires. Les autres acteurs étatiques sont possibles mais improbables a priori.
> 
> Le CERT verrouille ce cadrage dans son journal d’investigation et passe au profilage détaillé des TTP, pour les confronter aux profils connus des candidats (Parties II à V du cours).

-----

## PARTIE II — RUSSIE

> **Ce que cette partie apprend.** Comprendre la doctrine cyber russe (guerre hybride, intégration information/cyber/militaire), connaître la structure de l’appareil cyber russe (SVR, GRU, FSB et leurs unités), identifier les groupes APT russes majeurs et leurs spécificités, analyser les campagnes de référence depuis SolarWinds jusqu’à la guerre en Ukraine.
> 
> **Ce qu’elle ne couvre pas.** Les aspects techniques génériques des TTP (Partie I), le détail technique des campagnes OT spécifiques comme Industroyer (Ch.21), les enjeux d’attribution formels (Ch.24).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître un tradecraft russe face à une intrusion, différencier un mode opératoire SVR/GRU/FSB, situer une campagne russe dans le cadre doctrinaire de la guerre hybride, et identifier quand le cybercrime russophone est un prolongement plausible d’une opération étatique.

-----

### Chapitre 5 — Russie : contexte, doctrine et appareil cyber

#### 5.1 Priorités géopolitiques et principes doctrinaux

Les cyberopérations russes sont compréhensibles à condition de les situer dans les priorités géopolitiques nationales. Quatre priorités structurent l’ensemble : maintien du statut de grande puissance face aux États-Unis et à la Chine, contrôle de l’étranger proche (ex-URSS — Ukraine, Biélorussie, Caucase, Asie centrale), confrontation avec l’OTAN, et préservation du régime interne face aux pressions extérieures perçues et à la dissidence.

Chaque priorité génère des cyberopérations cohérentes. Le maintien de puissance alimente l’espionnage stratégique (SVR contre les gouvernements occidentaux), l’influence électorale (ingérence 2016 aux US, campagnes européennes), et la démonstration de capacité (NotPetya). Le contrôle de l’étranger proche motive le ciblage massif de l’Ukraine (Gamaredon au quotidien, Sandworm en escalade), les opérations contre la Biélorussie et la Géorgie. La confrontation OTAN génère les attaques contre les ministères de la défense, les think tanks stratégiques, les ambassades. La préservation du régime alimente la surveillance des opposants, des journalistes, et la contre-ingérence.

La **doctrine de la guerre hybride** (gibridnaya voyna) est le cadre intégrateur. Formulée par Valery Gerasimov (chef d’état-major des armées russes, essai de 2013 devenu « doctrine Gerasimov » dans la lecture occidentale — lecture que Gerasimov a lui-même contestée), elle postule que les moyens non militaires (information, cyber, économie, pression diplomatique) ont dépassé les moyens militaires dans l’efficacité pour atteindre les objectifs stratégiques. Le cyber est intégré dans ce continuum, aux côtés de la désinformation et des opérations d’influence.

La conséquence opérationnelle majeure : **pas de séparation nette entre espionnage et action**. Un même service (le GRU notamment) mène simultanément de la collecte de renseignement, de la destruction, et de l’influence. Le renseignement collecté est utilisé pour des opérations d’influence (hack-and-leak — DNC 2016), pour du sabotage ciblé, ou pour préparer des opérations conventionnelles. Cette intégration est le trait le plus distinctif de la doctrine russe, comparée à la doctrine américaine où renseignement (NSA), militaire offensif (USCYBERCOM) et law enforcement (FBI) sont plus nettement séparés.

#### 5.2 Le SVR : espionnage stratégique furtif

Le **SVR** (Служба внешней разведки — Service de Renseignement Extérieur) est le successeur post-soviétique du premier directorat du KGB. C’est le service russe chargé de l’espionnage stratégique — gouvernements étrangers, diplomatie, think tanks, grandes entreprises technologiques. Son style opérationnel est la **furtivité maximale** et le **long terme**.

Le groupe APT associé au SVR est **APT29** (Mandiant) / **Cozy Bear** (CrowdStrike) / **Midnight Blizzard** (Microsoft, anciennement NOBELIUM). APT29 est considéré comme l’un des trois ou quatre groupes APT les plus sophistiqués au monde. Ses caractéristiques opérationnelles se retrouvent dans chaque campagne : investissement massif en reconnaissance, infrastructure compartimentée (chaque cible a sa propre infrastructure C2), abus maîtrisé des services cloud légitimes, malware custom de haute qualité, et OPSEC quasi sans faute.

Les opérations emblématiques d’APT29 incluent **SolarWinds / SUNBURST** (2020, traité en détail au Ch.29), le **Microsoft corporate breach** de 2023-2024 (password spray sur un tenant test, pivot vers les emails de dirigeants Microsoft), les **campagnes de phishing OAuth** contre les diplomaties européennes (2022-2025), et les **ciblages continus des ministères des affaires étrangères** en Europe et en Amérique du Nord.

La tactique OAuth d’APT29 mérite une mention spécifique car elle illustre la modernité du tradecraft. Plutôt que de voler des mots de passe (détectable, temporaire), APT29 envoie à la cible des demandes d’autorisation OAuth pour des applications qui semblent légitimes (nom calqué sur Microsoft Teams, Outlook for iOS, Azure Active Directory Authenticator). Si la cible accepte, l’application malveillante obtient un jeton de refresh qui permet un accès persistant sans mot de passe, contournant la MFA. La technique est silencieuse, résiste aux rotations de mot de passe, et peut persister des mois.

#### 5.3 Le GRU : opérations militaires et destructives

Le **GRU** (Главное разведывательное управление — Direction du Renseignement Militaire, rebaptisé officiellement GU — Главное управление — en 2010 mais l’acronyme GRU reste largement utilisé) est le renseignement militaire. C’est le service le plus agressif et le plus bruyant des services cyber russes. Sa mission couvre le renseignement militaire classique, mais aussi le sabotage, les opérations d’influence, et les actions déstabilisatrices.

Trois unités GRU sont publiquement identifiées comme conduisant des cyberopérations.

**Unit 26165** conduit l’espionnage militaire et politique, avec un fort volet opérations d’influence. Le groupe APT associé est **APT28** (Mandiant) / **Fancy Bear** (CrowdStrike) / **Forest Blizzard** (Microsoft) / **Sofacy** (Kaspersky). APT28 est actif depuis au moins 2007 et a été au cœur de l’ingérence électorale américaine de 2016 (hack du DNC, publication via DCLeaks et WikiLeaks). Ses campagnes incluent également le hack du Bundestag allemand (2015), les attaques contre l’Agence Mondiale Antidopage (WADA, 2016), et l’exploitation massive de la vulnérabilité Outlook CVE-2023-23397 (2023) contre les organisations européennes.

**Unit 74455** conduit les opérations destructives. Le groupe APT associé est **Sandworm** (assignation initiale par iSight Partners devenu Mandiant) / **Seashell Blizzard** (Microsoft) / **BlackEnergy group** (historique) / **Voodoo Bear** (CrowdStrike). Sandworm est le seul groupe APT au monde à avoir causé publiquement documenté des pannes d’électricité par cyberattaque (Ukraine 2015 et 2016, Ch.21). Il est également responsable de **NotPetya** (2017, wiper mondial ~10 Mrd $), d’**Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang avec false flags Lazarus), et d’une série continue de wipers contre l’Ukraine depuis 2022 (HermeticWiper, CaddyWiper, IsaacWiper, AcidRain contre le satellite Viasat KA-SAT).

**Unit 29155** a été identifiée publiquement en 2024 par un advisory conjoint (US, UK, Estonie, Pologne). C’est une unité du GRU qui conduit des **opérations déstabilisatrices cyber-physiques** au soutien d’opérations clandestines plus larges (sabotages, assassinats, harcèlement). Le malware **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, quelques semaines avant l’invasion) est attribué à cette unité — ce qui a nécessité une révision des attributions initiales qui pointaient parfois Sandworm. Unit 29155 a également été liée à des tentatives d’attaques contre des infrastructures européennes (documentées par l’advisory CISA/NSA/FBI de septembre 2024).

La distinction entre ces unités importe pour l’analyste : une opération destructive contre l’Ukraine peut être attribuée à Sandworm (74455), à Unit 29155, ou à une coopération entre les deux. L’attribution à la bonne unité précise le cadre doctrinal et les attentes futures.

#### 5.4 Le FSB : sécurité intérieure et étranger proche

Le **FSB** (Федеральная служба безопасности — Service Fédéral de Sécurité) est le successeur principal du KGB pour les missions de sécurité intérieure, de contre-espionnage, et de surveillance des voisins proches. Ses cyberopérations se concentrent sur l’Ukraine, la Biélorussie, le Caucase, et la diaspora russophone à l’étranger.

Deux centres du FSB conduisent des cyberopérations publiquement attribuées.

**Centre 16** est le centre historique de cyber-collecte du FSB, chargé de l’espionnage long terme contre des cibles gouvernementales et diplomatiques de haute valeur. Le groupe APT associé est **Turla** (Kaspersky) / **Snake** (Mandiant) / **Secret Blizzard** (Microsoft) / **Venomous Bear** (CrowdStrike). Turla est considéré comme l’un des groupes techniquement les plus avancés au monde, actif depuis au moins 1996 (ce qui en fait l’un des plus anciens groupes APT encore opérationnels). Son malware signature, **Snake** (également appelé **Uroburos**), est un rootkit multi-plateforme extraordinairement sophistiqué, actif depuis au moins 2003, avec des capacités de persistence kernel sur Windows, Linux, et macOS.

Turla est également connu pour deux signatures opérationnelles remarquables. Premièrement, l’utilisation de **communications C2 par satellite** — détournement de liaisons satellite de FAI commerciaux pour masquer l’origine réelle du C2 (documenté par Kaspersky en 2015). Deuxièmement, la technique unique de **détournement d’infrastructure d’autres groupes APT** — Turla a été observé en train d’utiliser l’infrastructure de groupes iraniens (OilRig) pour mener ses propres opérations, technique appelée « piggybacking » qui complique massivement l’attribution et représente un niveau d’OPSEC exceptionnel.

**Snake a été démantelé par le FBI en mai 2023** dans le cadre de l’**opération Medusa**. Le FBI a développé un outil qui, exploitant des fonctionnalités du malware lui-même, a pu envoyer des commandes aux implants Snake sur les machines infectées pour les rendre inopérants — sans interagir avec les systèmes eux-mêmes au-delà de la neutralisation du malware. Opération remarquable par sa technicité et par sa portée (machines infectées dans plus de 50 pays). Turla a continué ses opérations avec d’autres outils post-Snake.

**Centre 18** conduit le ciblage massif de l’Ukraine avec un volume élevé et une sophistication comparativement moindre. Le groupe APT associé est **Gamaredon** (connu aussi comme **Primitive Bear**, **Shuckworm**, **Aqua Blizzard** chez Microsoft). Gamaredon cible systématiquement les institutions ukrainiennes depuis 2013-2014 (avant l’annexion de la Crimée), avec une intensification massive depuis 2022. Son tradecraft : phishing de masse, macros Office, scripts VBA, persistance agressive (réinfection rapide après éradication), et usage de Telegram comme canal de C2 (technique inhabituelle pour un acteur étatique classique — mais Gamaredon est plus proche d’un « bruit de fond » continu qu’un opérateur furtif). Les Ukrainiens ont surnommé Gamaredon « le cadet russe » — Gamaredon est le marteau là où Turla est le scalpel.

#### 5.5 L’écosystème cybercriminel russophone : zone grise

Les groupes cybercriminels russophones (opérateurs ransomware, marchés dark web, services de blanchiment) opèrent sous une **tolérance tacite** de l’État russe tant qu’ils respectent deux règles implicites : ne pas cibler la CEI (Communauté des États Indépendants — Russie, Biélorussie, Kazakhstan, etc.), et coopérer ponctuellement avec les services si sollicités.

Cette tolérance produit une zone grise qui complique l’attribution. Un ransomware qui frappe un opérateur stratégique européen peut être :

- Purement criminel, opportuniste, sans implication étatique directe ;
- Criminel, mais avec un choix de cible orienté par un signal étatique (« frappez ces secteurs, pas ces autres ») ;
- Criminel façade, avec un opérateur étatique qui utilise le ransomware comme couverture pour une opération destructive (NotPetya prétendait être un ransomware — il était en réalité un wiper destructif, avec un écran de rançon pour masquer l’intention).

Les affaires emblématiques qui documentent cette zone grise :

**Conti** (groupe ransomware russophone actif 2019-2022) a été l’un des plus prolifiques de son époque. Le groupe a été fracassé par des fuites internes en 2022 après qu’il se soit publiquement rangé du côté russe dans la guerre ukrainienne — un opérateur ukrainien interne a leaké des téraoctets de communications internes (« ContiLeaks »). Les communications révélaient des échanges évoquant le FSB, des consignes de ciblage alignées sur des priorités étatiques russes, et une structure organisationnelle plus hiérarchique que le profil cybercriminel standard. Après la dissolution publique de Conti, ses opérateurs se sont dispersés vers d’autres marques (BlackBasta, Black Suit, Karakurt).

**REvil / Sodinokibi** (groupe ransomware russophone actif 2019-2021) a conduit des opérations de grande ampleur (Kaseya MSP 2021, JBS 2021). Le groupe a été démantelé par les autorités russes en janvier 2022 (arrestation de 14 personnes) — dans un contexte de relation diplomatique Russie-US alors tendue mais pas rompue. Après l’invasion de l’Ukraine en février 2022, la coopération russe a cessé, et REvil s’est reconstitué partiellement.

**LockBit** (actif 2019-2024) a été l’un des plus prolifiques opérateurs RaaS jusqu’à son démantèlement partiel par l’opération Cronos (février 2024, coordination NCA/FBI/Europol). LockBit a montré une discipline anti-CIS claire (geoblocking, désactivation sur systèmes russophones) — marqueur typique de l’écosystème.

**BlackBasta**, **ALPHV/BlackCat**, **Play**, **Royal** : écosystème ransomware contemporain, majoritairement russophone, avec les mêmes patterns de tolérance étatique.

Pour l’analyste : un ransomware russophone frappant un secteur stratégique européen dans un contexte géopolitique tendu n’est jamais purement « criminel ». Le niveau d’implication étatique est un spectre à évaluer selon le contexte.

#### 5.6 Hacktivisme instrumentalisé

À côté du cybercrime toléré, la Russie soutient ou instrumentalise plusieurs collectifs présentés comme « hacktivistes ».

**KillNet** (actif depuis 2022) revendique des cyberattaques pro-russes, principalement DDoS contre des institutions occidentales et des infrastructures ukrainiennes. La sophistication technique est modeste (essentiellement DDoS, parfois défacement), mais la coordination opérationnelle et la pérennité suggèrent un soutien ou une connivence minimale avec les services. Le groupe a muté plusieurs fois (KillNet, KillMilk, BlackSkills) et génère un volume continu d’activité pro-régime.

**NoName057(16)** (actif depuis 2022) est plus technique que KillNet. Le groupe déploie un outil DDoS distribué (**DDosia Project**) qui recrute des volontaires via Telegram et les paie en cryptomonnaies pour participer à des attaques. L’outil télécharge régulièrement des listes de cibles depuis des serveurs centralisés. Démantèlement partiel par Europol en mai 2025 — mais le modèle se reproduit.

**IT Army of Ukraine** est symétrique côté ukrainien : mouvement de volontaires cyber internationaux, lancé publiquement par le vice-premier ministre Mykhailo Fedorov via Telegram en février 2022, conduisant des opérations DDoS et de hacktivisme contre des cibles russes. Zone grise similaire : coordination étatique explicite d’un mouvement de volontaires.

Ces mouvements brouillent la distinction classique « hacktivisme vs État ». Pour l’analyste, la règle est de lire les alignements : KillNet et NoName057(16) s’alignent systématiquement sur les priorités tactiques russes (cibles sélectionnées selon l’actualité diplomatique), ce qui est incompatible avec un hacktivisme authentique.

#### 5.7 Réorganisations post-2022

L’invasion de l’Ukraine en février 2022 a eu des effets sur l’appareil cyber russe qu’il est utile de documenter.

**Augmentation massive du volume opérationnel** : intensification des attaques contre l’Ukraine (wipers multiples, Gamaredon en continu, Sandworm en escalade), augmentation du ciblage des alliés de l’Ukraine (Pologne, États baltes, OTAN en général), expansion du pré-positionnement dans les infrastructures européennes.

**Professionnalisation de Unit 29155** : la publication de l’advisory de septembre 2024 a documenté l’existence et les capacités d’une unité jusque-là peu connue. Ce qui suggère que les services étatiques russes ont réalloué des ressources pour intensifier leurs opérations.

**Pression sur le cybercrime russophone** : les sanctions occidentales ont rendu plus difficile le blanchiment et la conversion des gains ransomware. Plusieurs groupes ransomware ont déplacé leurs opérations vers les cibles occidentales avec une intensité accrue. Inversement, certains opérateurs ont été observés quittant la Russie pour des juridictions plus neutres (Dubaï, Serbie), signe d’une fragilisation de l’écosystème.

**Durcissement de l’OPSEC** : post-invasion, plusieurs groupes russes ont adapté leur tradecraft. APT29 a intensifié ses campagnes OAuth et l’abus de services cloud légitimes. Sandworm a diversifié son malware (CosmicEnergy découvert 2023, variants HermeticWiper, AcidRain contre Viasat).

L’écosystème russe en 2025-2026 reste le plus actif au monde en volume d’opérations destructives documentées, avec une pression réciproque entre les services (qui doivent démontrer leur valeur opérationnelle) et les défenseurs occidentaux qui ont gagné en maturité d’attribution et de détection.

#### 5.8 Fil rouge — BLACKOUT Épisode 3

> **⚡ BLACKOUT — Épisode 3 : le profil TTP observé est-il compatible Sandworm ?**
> 
> Le CERT, après la phase de triage initial, collecte les TTP observées et les confronte au profil connu de Sandworm.
> 
> **TTP observées sur BLACKOUT** :
> 
> 1. Accès initial via exploitation d’appliance Ivanti (CVE-2024-21887).
> 1. Persistence via DLL sideloading dans une application de supervision.
> 1. Mouvement latéral via PsExec et Kerberoasting (credentials de compte de service avec SPN faible).
> 1. Pivot vers OT via un poste d’ingénierie double-connecté.
> 1. C2 par beaconing HTTPS avec jitter (27 min ± 3 min).
> 1. Pas de malware custom identifié à ce stade.
> 1. Aucune action destructive ou exfiltration visible.
> 
> **Profil Sandworm typique** (profil de référence basé sur les campagnes documentées 2015-2025) :
> 
> - Accès initial : mix supply chain, exploitation edge, phishing ciblé — l’exploitation Ivanti est plausible.
> - Persistence : services Windows, tâches planifiées, parfois DLL sideloading — compatible.
> - Mouvement latéral : PsExec, WMI, Mimikatz, Kerberoasting — compatible.
> - Ciblage OT : signature historique de Sandworm — très compatible.
> - C2 : HTTPS avec beaconing — compatible, mais les patterns spécifiques de Sandworm (jitter, intervalles) varient selon les campagnes.
> - Malware custom : **Sandworm utilise typiquement du malware custom** (Industroyer, CaddyWiper, HermeticWiper, wipers, backdoors). L’absence de malware custom est un **léger décalage** avec le profil Sandworm classique.
> - Action destructive : signature Sandworm, mais absent ici (ce qui serait compatible avec une phase de pré-positionnement préalable à l’activation).
> 
> **Cohérences fortes** : ciblage énergie, pivot OT, patience opérationnelle, contexte géopolitique (conflit ukrainien en cours, tensions énergétiques).
> 
> **Décalages notables** : pas de malware custom Sandworm identifié, exploitation Ivanti (attaquée aussi par d’autres acteurs notamment chinois), C2 relativement standard.
> 
> **Diagnostic intermédiaire CERT** : profil **compatible avec Sandworm** mais **pas exclusivement**. Il est indispensable de tester d’autres hypothèses — notamment les acteurs chinois, qui ont des profils de pré-positionnement énergie (Volt Typhoon) compatibles avec certaines observations.
> 
> Le CERT passe à l’examen du profil chinois (Partie III).

-----

### Chapitre 6 — Russie : les groupes APT en détail

Ce chapitre approfondit le profil des six groupes APT russes les plus importants. Chaque profil couvre : mission, TTP signature, OPSEC, campagnes emblématiques, évolution récente.

#### 6.1 APT29 / Cozy Bear / Midnight Blizzard (SVR)

**Mission** : espionnage stratégique de haut niveau — gouvernements occidentaux, diplomatie, grandes entreprises technologiques, think tanks, ONG actives sur la Russie, recherche médicale (ciblage documenté sur les développeurs de vaccins COVID en 2020).

**TTP signature** :

- **Accès initial par compromission supply chain** (SolarWinds 2020 — cas d’école), par **phishing OAuth ciblé** (demandes d’autorisation d’applications malveillantes imitant Microsoft Teams ou des applications Azure légitimes), par **password spray** sur Azure AD (tenants avec faibles politiques), et occasionnellement par **spear-phishing classique** avec macros.
- **Abus Azure AD / Entra ID / M365** : vol de tokens SAML (GoldenSAML), manipulation d’applications OAuth, pivotement entre tenants via des relations de partage, abus de permissions Graph API pour lire les emails.
- **Malware custom sophistiqué** : SUNBURST (backdoor injectée dans les builds Orion de SolarWinds), TEARDROP (loader), GoldMax / SUNSHUTTLE (backdoor Go cross-platform), GoldFinder (HTTP tracer pour reconnaissance d’infrastructure), SIBOT (VBScript), FoggyWeb (backdoor ADFS post-exploitation), MagicWeb (malware ADFS plus récent 2022).
- **C2 via services légitimes** : Azure, AWS, Dropbox, Twitter (pour des canaux secondaires), abus de canaux Slack/Teams dans certaines campagnes récentes.
- **Minimal footprint** : peu de fichiers déposés, exécution en mémoire privilégiée, nettoyage systématique des traces.

**OPSEC** : parmi la plus élevée du monde APT. Infrastructure compartimentée (chaque cible a sa propre chaîne d’infrastructure C2), opérateurs disciplinés (pas d’erreurs d’horaires documentées), adaptation rapide aux mitigations (changement de techniques dès qu’une campagne est publiée).

**Campagnes majeures** :

- **SolarWinds / SUNBURST** (2020-2021) : ~18 000 organisations infectées via la mise à jour trojanisée d’Orion, ~100 cibles de haute valeur activement exploitées (Trésor US, Département du Commerce, Département de la Sécurité Intérieure, Microsoft, FireEye/Mandiant, et autres). Détaillé au Ch.29.
- **Ciblage des développeurs de vaccins COVID** (2020) : attribué par NCSC, NSA, CSE/Canada — APT29 cible les entreprises pharmaceutiques britanniques, américaines et canadiennes développant les vaccins COVID-19 pour exfiltrer la recherche.
- **Microsoft corporate breach** (novembre 2023 - janvier 2024) : APT29 compromet un tenant Azure AD test de Microsoft via password spray, pivote vers une application OAuth permissive, et accède aux emails de dirigeants Microsoft (y compris de la direction exécutive). Microsoft a publiquement reconnu la compromission. Des entités tierces (Hewlett Packard Enterprise notamment) ont subséquemment confirmé des compromissions liées.
- **Campagnes diplomatiques continues 2022-2025** : spear-phishing OAuth contre les ministères des affaires étrangères européens, les ambassades, les missions diplomatiques. Volume élevé, taux de compromission non-public.
- **MagicWeb** (2022) : backdoor ADFS post-exploitation identifiée par Microsoft. Le malware modifie la gestion des certificats ADFS pour permettre à l’attaquant de se faire passer pour n’importe quel utilisateur.

**Évolution récente (2024-2026)** : après SolarWinds, APT29 a évolué vers un usage encore plus prononcé des abus cloud/identity (tokens, OAuth, Primary Refresh Tokens Azure AD). La dépendance aux infrastructures cloud légitimes (Microsoft, AWS, Google) rend la détection plus difficile. Les campagnes de 2024-2025 montrent un ciblage encore plus sophistiqué des ministères européens, avec des emails personnalisés qui passent les filtres anti-phishing majoritairement par leur contexte plausible.

#### 6.2 APT28 / Fancy Bear / Forest Blizzard (GRU Unit 26165)

**Mission** : espionnage militaire et politique + opérations d’influence intégrées. Cibles : ministères de la défense, organisations internationales (OTAN, UE, OSCE), organisations anti-dopage (WADA), partis politiques (DNC 2016), médias, think tanks de défense.

**TTP signature** :

- **Spear-phishing** : macros VBA dans des documents Office (pendant longtemps la technique privilégiée), faux portails de login OAuth ou de services corporate (Microsoft OWA, VPN).
- **Exploitation de vulnérabilités** : APT28 est l’un des acteurs les plus actifs à exploiter rapidement les vulnérabilités Outlook et Exchange. **CVE-2023-23397** (Outlook, vulnérabilité NTLM hash leak via invitation de calendrier malveillante) a été massivement exploitée par APT28 en 2022-2023 avant sa découverte publique.
- **Credential harvesting** : fausses pages de login imitant les services corporate, password spraying massif sur Azure AD.
- **Outils custom** : **X-Tunnel** (proxy interne), **XAgent** (backdoor modulaire Windows/macOS/iOS/Android), **Zebrocy** (backdoor multi-langages — Delphi, Go, Python, C++ — tradecraft inhabituel qui complique l’analyse), **CredoMap** (stealer de credentials), **Cannon** (backdoor), **Seduploader** (implant).
- **Mimikatz** pour le credential dumping.

**OPSEC** : moyen à élevé — nettement moins furtif que le SVR/APT29. APT28 assume un niveau de bruit plus élevé pour l’efficacité opérationnelle. Plusieurs campagnes ont été identifiées par des erreurs d’OPSEC (réutilisation d’infrastructure, horaires compatibles Moscou, artefacts langue russe).

**Campagnes majeures** :

- **DNC hack** (2016) : compromission du Comité National Démocrate américain. Les données (emails, documents internes) sont publiées via DCLeaks et WikiLeaks dans une opération hack-and-leak coordonnée pour impacter l’élection présidentielle. Attribution par FBI, DHS, Office of the Director of National Intelligence (janvier 2017). Indictment DOJ en 2018 qui inculpe nommément 12 officiers du GRU Unit 26165.
- **WADA breach** (2016) : vol et publication de données médicales d’athlètes olympiques, en représailles à l’exclusion d’athlètes russes pour dopage systémique.
- **Bundestag breach** (2015) : compromission du réseau informatique du parlement allemand, accès maintenu plusieurs semaines, exfiltration massive de documents. La réponse allemande a inclus une reconstruction complète du réseau.
- **TV5Monde** (2015) : bien que revendiquée par un groupe présenté comme « CyberCaliphate » affilié à l’État islamique, l’attribution technique a pointé vers APT28 (false flag — tradecraft similaire, infrastructure compromise).
- **Exploitation massive CVE-2023-23397** (2022-2023) : APT28 a exploité cette vulnérabilité Outlook contre des dizaines d’organisations européennes (gouvernements, défense, énergie, transport) pendant près d’un an avant découverte publique.
- **Campagnes 2023-2025** : ciblage continu des organisations ukrainiennes, alliés de l’OTAN, ministères européens. Utilisation accrue de services de stockage cloud (MEGA, pCloud) pour l’exfiltration.

**Évolution récente** : APT28 a maintenu un haut niveau d’activité post-2022. Utilisation croissante d’**infostealers** comme vecteur d’accès initial (achat de logs sur les marchés dark web pour obtenir des credentials initiaux, plutôt que phishing). Campagne **MooBot** (botnet de routeurs Ubiquiti compromis, utilisé comme infrastructure de proxy) démantelée par le FBI en février 2024 — modèle similaire à Volt Typhoon mais côté russe.

#### 6.3 Sandworm / Seashell Blizzard (GRU Unit 74455)

**Mission** : opérations destructives et sabotage — le bras armé du cyber russe. Cibles : infrastructures critiques (énergie principalement, télécoms, secteur financier), gouvernements, sous-traitants militaires. Ciblage privilégié : Ukraine, pays OTAN de la première ligne (Pologne, États baltes), occasionnellement infrastructures mondiales (NotPetya a touché le monde entier via la supply chain M.E.Doc).

**TTP signature** :

- **Wipers** : Sandworm est le groupe au monde qui a déployé le plus de wipers différents. **NotPetya / ExPetr** (2017, wiper masqué en ransomware, propagation via supply chain M.E.Doc + EternalBlue), **CaddyWiper** (2022, wiper destructif Ukraine), **HermeticWiper / FoxBlade** (février 2022, veille de l’invasion), **IsaacWiper** (février 2022), **AcidRain** (février 2022, contre les terminaux satellites Viasat KA-SAT — impact collatéral sur les éoliennes allemandes qui utilisaient le même opérateur). Plusieurs variants récents non publiquement catalogués.
- **Attaques OT/ICS** : **Industroyer / CrashOverride** (2016, premier malware ciblant les protocoles industriels IEC 60870-5-104 et IEC 61850 pour provoquer un blackout), **Industroyer2** (2022, tentative déjouée par CERT-UA et ESET), **CosmicEnergy** (2023, découvert par Mandiant — malware OT conçu pour attaquer les systèmes de protection IEC 60870-5-104, capacités similaires à Industroyer mais avec des différences techniques suggérant une nouvelle branche de développement). Détaillé au Ch.21.
- **Supply chain** : compromission de M.E.Doc (logiciel comptable ukrainien utilisé par des milliers d’organisations) pour la propagation initiale de NotPetya — paradigme supply chain.
- **Exploitation d’edge devices et routeurs** : **Cyclops Blink** (botnet 2022 sur routeurs ASUS et WatchGuard — démantelé par le FBI).
- **Mouvement latéral classique** : Mimikatz, PsExec, RDP.
- **False flags sophistiqués** : **Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang) incluait des fragments de code Lazarus plantés délibérément pour brouiller l’attribution. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et confirmé l’attribution Sandworm.

**Particularité historique** : Sandworm est le **seul groupe APT dans le monde à avoir causé publiquement documenté des pannes d’électricité** via cyberattaque. Ukraine 2015 (BlackEnergy/KillDisk, 230 000 foyers, 6 heures) et 2016 (Industroyer, Kiev, 1 heure). Ces événements sont les seuls cas avérés d’impact physique étendu d’une cyberattaque sur un système de distribution d’énergie.

**OPSEC** : variable. Sandworm assume un niveau de bruit élevé pour ses opérations destructives (l’impact est l’objectif, la furtivité post-impact n’est plus nécessaire). Mais les phases de reconnaissance et de déploiement sont menées avec un OPSEC sérieux. Les attributions publiques ont été facilitées par des artefacts (strings, infrastructure) qui suggèrent une discipline OPSEC moindre que celle du SVR.

**Campagnes majeures** :

- **Ukraine 2015-2016** : BlackEnergy et Industroyer (Ch.21).
- **NotPetya** (juin 2017) : déployé initialement via M.E.Doc en Ukraine, propagation mondiale en heures via EternalBlue et credentials Windows. Dommages mondiaux estimés à 10+ milliards de dollars (Maersk, Merck, FedEx/TNT Express, Saint-Gobain, etc.). Attribution publique par CIA (juin 2017), UK NCSC et DoD (février 2018). Reconnaissance formelle comme « la cyberattaque la plus destructrice de l’histoire » par les États-Unis.
- **Olympic Destroyer** (2018) : ciblage des Jeux Olympiques d’hiver de Pyeongchang, en représailles à l’exclusion de la délégation russe pour dopage. Plusieurs composants techniques des JO compromis (site web, système Wi-Fi du stade olympique, systèmes de télévision). False flags multiples (code Lazarus, infrastructure iranienne).
- **Campagne Ukraine 2022-présent** : série continue de wipers, tentatives sur les infrastructures critiques (Industroyer2 déjouée), ciblage des télécoms et des médias, opérations OT sur les réseaux électriques ukrainiens coordonnées avec des frappes militaires.
- **Viasat KA-SAT (février 2022)** : attaque via **AcidRain** contre les terminaux satellite du fournisseur Viasat, timing synchronisé avec l’invasion. Impact principal : communications militaires ukrainiennes. Impact collatéral notable : 5 800 éoliennes allemandes utilisant le même service de connectivité satellite, inopérables pendant plusieurs semaines. Attribution publique par UE, UK, US (mai 2022).

**Évolution récente (2024-2026)** : Sandworm reste actif en Ukraine et étend son ciblage aux alliés. CosmicEnergy (2023) révèle une continuité de R&D sur les malwares OT. Des rapports Mandiant et Microsoft de 2024 suggèrent une professionnalisation croissante et un élargissement géographique (ciblage documenté de l’Europe de l’Ouest, y compris la France et l’Allemagne).

#### 6.4 GRU Unit 29155

**Identification publique** : advisory conjoint NSA/FBI/CISA + partenaires internationaux (UK, Pologne, Estonie, Lettonie, Lituanie, Tchéquie, Allemagne, Ukraine, Canada, Australie) en septembre 2024.

**Mission** : opérations déstabilisatrices cyber-physiques au soutien d’objectifs stratégiques plus larges. Unit 29155 était historiquement connue pour des opérations clandestines non-cyber (sabotages physiques, empoisonnements — Salisbury 2018 contre les Skripal, impliquée), mais l’advisory 2024 a confirmé son extension au cyber.

**TTP signature** (telles que documentées par l’advisory) :

- **Accès initial** : exploitation de vulnérabilités publiques (VPN, passerelles web), phishing, bruteforce.
- **Malware custom** : **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, attribué initialement à Sandworm puis réattribué à Unit 29155 après l’advisory).
- **Outils communs** : Impacket, Mimikatz, PsExec — tradecraft partagé avec le reste de l’écosystème GRU.
- **Ciblage OT** : l’advisory mentionne des tentatives d’attaques contre des systèmes OT européens, sans détails publics précis.

**Distinction avec Sandworm** : Sandworm (Unit 74455) est une unité cyber dédiée de longue date, avec une sophistication technique importante et des malwares signature. Unit 29155 est une unité historiquement non-cyber qui a développé des capacités cyber plus récemment — sophistication technique moindre que Sandworm, mais intégration plus directe avec des opérations clandestines non-cyber. La distinction importe pour l’analyse : attribuer une opération à l’une ou l’autre unité révèle des intentions différentes.

**Campagnes connues** :

- **WhisperGate** (janvier 2022) : wiper déployé contre des organisations ukrainiennes (gouvernement, ONG, IT) quelques semaines avant l’invasion. Masqué en ransomware (note de rançon incohérente). Impact réel : destructive, non récupérable.
- **Campagnes documentées par l’advisory 2024** : tentatives d’attaques contre des infrastructures européennes, y compris dans des pays ayant soutenu activement l’Ukraine. Détails classifiés.

**Implications opérationnelles** : pour l’analyste, la reconnaissance d’Unit 29155 comme acteur distinct signifie que le GRU dispose d’au moins deux unités capables d’opérations destructives cyber — augmentation de la surface de menace et de la capacité de redondance opérationnelle.

#### 6.5 Turla / Snake / Secret Blizzard (FSB Centre 16)

**Mission** : espionnage long terme contre cibles gouvernementales et diplomatiques de haute valeur. Ciblage : ministères des affaires étrangères dans le monde, ambassades, organisations internationales, parfois entreprises de défense et think tanks stratégiques.

**TTP signature** :

- **Watering hole** : compromission de sites web fréquentés par les cibles pour les infecter lors de leur visite. Sites gouvernementaux, académiques, ou institutionnels pertinents pour la cible.
- **Supply chain** : opérations de longue durée impliquant compromission d’éditeurs ou de prestataires pour atteindre les cibles finales.
- **Malware signature** — Turla développe et maintient un arsenal malware remarquable :
  - **Snake / Uroburos** : rootkit multi-plateforme (Windows, Linux, macOS) actif depuis au moins 2003. Persistence kernel, évasion sophistiquée, communications P2P entre instances. Démantelé par le FBI en mai 2023 (opération Medusa) mais les variants post-Snake continuent.
  - **Kazuar** : backdoor modulaire (.NET) utilisée pour des opérations ciblées.
  - **LightNeuron** : backdoor Exchange serveur (transport agent malveillant) — interception d’emails au niveau serveur. Actif depuis au moins 2014, découvert par ESET en 2019.
  - **Crutch** : backdoor Windows utilisée contre des cibles diplomatiques en Europe.
  - **Carbon / Cobra** : framework modulaire historique.
- **Infrastructure par satellite** : Turla est documenté pour avoir utilisé des **liaisons satellite détournées** comme canal C2 — exploitation de liaisons satellite de FAI commerciaux (clients commerciaux des FAI satellites dans des régions où la sécurité est faible) pour masquer l’origine réelle des C2. Technique documentée par Kaspersky en 2015.
- **Piggybacking sur d’autres APT** : Turla a été observé en train d’utiliser l’**infrastructure d’autres groupes APT** pour ses opérations. Le cas le plus documenté : Turla a compromis l’infrastructure d’APT34 (OilRig, Iran) et l’a utilisée pour mener ses propres opérations. Cette technique, documentée publiquement par UK NCSC et NSA en octobre 2019, est unique dans le monde APT par son niveau de sophistication opérationnelle et par l’impact qu’elle a sur l’attribution (une victime peut voir une intrusion qui semble iranienne alors qu’elle est russe).

**OPSEC** : la plus sophistiquée de l’écosystème russe, probablement parmi les plus sophistiquées du monde APT. Opérations de longue durée (certaines compromissions gouvernementales ont duré 5-10 ans). Arsenal malware constamment renouvelé. Peu d’erreurs d’OPSEC documentées.

**Campagnes majeures** :

- **Opérations contre les diplomaties européennes** (depuis au moins les années 2000) : ciblage continu des ministères des affaires étrangères, avec des compromissions parfois longues et silencieuses.
- **RUAG breach (Suisse, 2014-2016)** : la société suisse RUAG (défense, détenue par l’État) a été compromise pendant près de deux ans. Exfiltration massive de données.
- **German Federal Foreign Office** (2017-2018) : compromission du réseau du ministère allemand des affaires étrangères, accès maintenu plusieurs mois.
- **Opération Medusa** (mai 2023, côté défense) : démantèlement du malware Snake par le FBI. Le FBI a développé un outil (PERSEUS) qui exploite des fonctionnalités de Snake lui-même pour rendre le malware inopérant sur les machines infectées, sans interagir avec les systèmes au-delà. Coordination internationale (États affectés notifiés). Opération citée comme un modèle d’action offensive law enforcement contre un malware APT.

**Évolution récente (2024-2026)** : Turla a continué ses opérations avec des outils post-Snake. Un rapport Microsoft de novembre 2023 a détaillé des compromissions continues de ministères ukrainiens et européens par Secret Blizzard, utilisant des techniques post-Snake (détournements d’infrastructure d’Andromeda — un ancien crimeware — pour piggybacker sur les infections existantes). Le modèle opérationnel Turla — sophistication extrême, patience, piggybacking — reste actif.

#### 6.6 Gamaredon / Aqua Blizzard (FSB Centre 18)

**Mission** : ciblage massif continu de l’Ukraine. Cibles : institutions ukrainiennes (gouvernement, défense, sécurité, énergie, médias, ONG), diaspora ukrainienne.

**TTP signature** :

- **Phishing de masse** : volume extrêmement élevé, thèmes adaptés à l’actualité ukrainienne. Documents Office avec macros VBA (technique relativement ancienne mais toujours efficace à grande échelle).
- **Templates VBA** : Gamaredon maintient une bibliothèque de templates macros mise à jour régulièrement. Les macros sont relativement simples techniquement mais produites en volume.
- **Scripts VBS et PowerShell** : petits scripts de téléchargement et d’exécution, souvent peu obfusqués.
- **Infrastructure Telegram pour C2** : Gamaredon est l’un des rares acteurs étatiques à utiliser massivement Telegram comme canal de C2. Les implants récupèrent leurs instructions depuis des canaux Telegram contrôlés. Technique inhabituelle pour un acteur étatique, plus proche d’un modèle cybercriminel — mais Gamaredon assume un profil opérationnel différent des autres APT russes.
- **Persistence agressive** : Gamaredon réinfecte rapidement après éradication. Les victimes ukrainiennes rapportent des cycles infection/détection/éradication/réinfection qui se répètent en jours ou semaines.
- **Malwares signature** : **Pterodo** (famille de backdoors légères), **Pteranodon**, **GammaLoad** — moins sophistiqués que les outils SVR ou Sandworm, mais produits et renouvelés en volume.

**Particularité** : Gamaredon est le « marteau » là où Turla est le « scalpel ». Sophistication technique modeste, mais volume massif, persistance, et impact cumulé important. Le CERT-UA classe Gamaredon comme la menace cyber la plus continue contre l’Ukraine — pas la plus dangereuse individuellement, mais la plus omniprésente.

**OPSEC** : faible à moyenne. Pas d’effort majeur pour cacher l’origine — Gamaredon assume son rôle de « bruit de fond » plutôt que d’opération clandestine sophistiquée. Des artefacts linguistiques russes, des patterns d’horaires Moscou, et des réutilisations d’infrastructure sont fréquents.

**Évolution post-invasion** : volume massivement augmenté depuis février 2022. Gamaredon est l’acteur qui génère le plus grand volume de cyberactivité hostile contre l’Ukraine au quotidien. Adaptations techniques marginales (nouveaux thèmes de phishing, quelques variants de malware), mais continuité générale du modèle opérationnel.

#### 6.7 Dragonfly / Energetic Bear / Berserk Bear

**Attribution** : attribué à la Russie avec haute confiance, rattachement spécifique au FSB Centre 16 (selon des analyses US) ou à une entité distincte — la clarté d’attribution inter-services russes est moins nette que pour APT28/APT29.

**Mission** : ciblage énergie historique. Reconnaissance et pré-positionnement dans le secteur énergie (électricité, pétrole, gaz, nucléaire) aux US et en Europe. Pas d’action destructive publiquement documentée, mais patterns cohérents avec une préparation de capacités.

**TTP signature** :

- Watering hole sur des sites de publications industrielles fréquentés par les ingénieurs énergie.
- Compromission supply chain via des éditeurs de logiciels industriels (compromission d’**eWON Talk2M** en 2017).
- Exploitation SMB, Mimikatz.
- Développement de connaissances opérationnelles sur les systèmes ICS des cibles (reconnaissance approfondie, pas d’action destructive).

**Campagnes majeures** :

- **Opérations énergie US 2017-2018** : advisory conjoint US-CERT/FBI en mars 2018 détaille une campagne russe de pré-positionnement dans le secteur énergie US, avec des accès confirmés dans plusieurs organisations. Pas de destructive action.
- **Cibles énergie européenne** : ciblage documenté de sociétés énergie britanniques, allemandes, italiennes (2016-2020).

**Évolution récente** : activité Dragonfly moins documentée publiquement depuis 2020, mais le ciblage énergie par la Russie s’est poursuivi (notamment via Sandworm). Certains analystes considèrent que Dragonfly a été réorganisé ou fusionné dans d’autres structures cyber russes post-2022.

#### 6.8 Évolution de l’écosystème russe post-invasion ukrainienne

Post-février 2022, plusieurs évolutions structurantes :

**Intensification opérationnelle** : volume d’attaques historiquement élevé. L’Ukraine est l’environnement de confrontation cyber le plus intense au monde. Les groupes russes sont déployés à plein régime.

**Émergence d’Unit 29155** : publiquement documentée en 2024, suggérant que l’appareil cyber GRU a été élargi ou réorganisé pour accroître les capacités destructives.

**Pression économique sur le cybercrime russophone** : sanctions, restrictions de blanchiment, pression sur les cryptomonnaies ont fragilisé l’écosystème. Certains groupes se sont reconstitués, d’autres ont migré vers d’autres juridictions.

**Professionnalisation continue** : le GRU Units 26165 et 74455 ont adapté leurs TTP, développé de nouveaux malwares (CosmicEnergy, variants de wipers), et sophistiqué leur ciblage. APT29 a renforcé son tradecraft cloud/identity.

**Visibilité accrue côté défense** : la coopération entre les services occidentaux et l’Ukraine (notamment via Microsoft Threat Intelligence, Mandiant, ESET) a produit un volume de documentation sans précédent sur les APT russes. Ce qui permet aux défenseurs occidentaux d’anticiper les tactiques.

L’équilibre offensif/défensif en cyber russe 2025-2026 est caractérisé par un écosystème russe plus actif que jamais, mais face à des défenseurs occidentaux mieux préparés et mieux informés qu’auparavant.

-----

### Chapitre 7 — Russie : campagnes de référence et opérations d’influence

Ce chapitre présente les campagnes russes les plus emblématiques, en complément des descriptions de groupes du Ch.6. Plusieurs de ces campagnes sont traitées de manière approfondie ailleurs dans le cours (SolarWinds au Ch.29, Industroyer au Ch.21). Ce chapitre les resitue dans une perspective d’ensemble et ajoute les opérations d’influence.

#### 7.1 SolarWinds / SUNBURST (2020-2021)

**Acteur** : APT29 (SVR). **Paradigme** : supply chain comme vecteur d’espionnage à très grande échelle.

**Synthèse** : compromission du processus de build du logiciel SolarWinds Orion (logiciel de supervision réseau déployé dans des dizaines de milliers d’organisations). Une backdoor (SUNBURST) est injectée dans les builds officiels signés entre février et juin 2020. La mise à jour trojanisée est distribuée à ~18 000 organisations clientes. APT29 sélectionne ~100 cibles de haute valeur (Trésor US, Commerce, DHS, Pentagone partiellement, Microsoft, FireEye, autres) et déploie des outils de seconde étape (TEARDROP, RAINDROP, GoldMax). Mouvement latéral via GoldenSAML pour accéder aux emails et documents Azure AD/O365.

**Découverte** : décembre 2020 par FireEye/Mandiant, qui enquêtait initialement sur le vol de ses propres outils Red Team.

**Impact** : accès multi-mois à des communications gouvernementales stratégiques américaines, impact massif sur la confiance dans la supply chain logicielle, déclenchement de l’Executive Order 14028 (mai 2021) qui a structuré la réponse américaine sur la sécurité logicielle. Détaillé Ch.29.

#### 7.2 NotPetya (juin 2017)

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : wiper destructif masqué en ransomware, supply chain comme vecteur de propagation initiale.

**Synthèse** : déploiement initial via une mise à jour compromise du logiciel comptable ukrainien **M.E.Doc** (largement utilisé en Ukraine pour les déclarations fiscales — une forme de supply chain massive). Une fois exécuté, NotPetya se propage latéralement via **EternalBlue** (exploit SMB de la NSA leaké par Shadow Brokers) et via des credentials collectés sur les systèmes initiaux. Il chiffre les fichiers de manière **irréversible** — le mécanisme de rançon est factice, la clé de déchiffrement n’existe pas réellement. C’est un wiper déguisé, pas un ransomware.

**Propagation mondiale** : de l’Ukraine, NotPetya se propage aux multinationales ayant des bureaux en Ukraine, puis à leur réseau global. Victimes notables : **Maersk** (~300 M$ de dommages, opérations maritimes mondiales paralysées), **Merck** (~870 M$), **FedEx/TNT Express** (~400 M$), **Saint-Gobain** (~380 M$), **Mondelez** (~150 M$), et des dizaines d’autres. Dommages mondiaux estimés à **10+ milliards de dollars**.

**Attribution** : CIA (attribution interne juin 2017, publicisée février 2018), UK NCSC et DoD (février 2018), US Treasury (sanctions 2018), Five Eyes. Reconnu formellement comme « la cyberattaque la plus destructrice de l’histoire » par les autorités américaines.

**Leçons** : la supply chain d’un petit éditeur peut produire un impact mondial. Le destructif peut être masqué en criminalité. Les dommages collatéraux d’une opération étatique peuvent dépasser massivement les objectifs initiaux (NotPetya était initialement ciblé sur l’Ukraine, l’ampleur mondiale semble avoir été anticipée mais assumée).

#### 7.3 Ukraine 2015-2016 : les premiers blackouts cyber

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : cyber OT causant un impact physique direct.

**Ukraine décembre 2015 — BlackEnergy / KillDisk** : trois distributeurs d’électricité ukrainiens compromis. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA et ouvrent manuellement des disjoncteurs, coupant l’alimentation de ~230 000 foyers pendant ~6 heures. KillDisk efface ensuite les systèmes de supervision pour compliquer la récupération. Premier blackout confirmé causé par une cyberattaque.

**Ukraine décembre 2016 — Industroyer / CrashOverride** : cyberattaque plus sophistiquée, automatisée via le malware Industroyer. Industroyer manipule directement les protocoles industriels (IEC 60870-5-104, IEC 61850, OPC DA) pour commander les équipements sans intervention humaine. Ouverture de disjoncteurs à un poste de transformation à Kiev, blackout d’~1 heure. Premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles natifs.

**Analyse complète** au Ch.21 (OT/ICS).

#### 7.4 Ingérence électorale 2016 aux États-Unis

**Acteur** : APT28 (GRU Unit 26165) pour les compromissions cyber, Internet Research Agency (IRA, entité séparée) pour l’influence sur les réseaux sociaux. **Paradigme** : hack-and-leak coordonné comme instrument d’influence politique.

**Volet cyber** : APT28 compromet le **Comité National Démocrate** (DNC) et le comité de campagne de Hillary Clinton, exfiltre des milliers d’emails et de documents internes entre l’été 2015 et l’été 2016. Les documents sont ensuite publiés en vagues coordonnées via **DCLeaks** (plateforme créée par APT28), **Guccifer 2.0** (persona fictive présentée comme un hacker roumain indépendant — en réalité GRU), et surtout **WikiLeaks** (qui publie les emails Podesta le 7 octobre 2016, quelques heures après la diffusion d’une vidéo embarrassante pour Trump — le timing coordonné suggère une tentative de détournement de l’attention médiatique).

**Volet influence** : l’Internet Research Agency (IRA, troll farm à Saint-Pétersbourg liée à Prigojine) conduit une campagne massive d’influence sur les réseaux sociaux (Facebook, Instagram, Twitter, YouTube) — création de milliers de faux comptes amplifiant des messages polarisants sur des sujets sociétaux (race, armes, immigration), organisation d’événements physiques via des fausses identités.

**Attribution** : ODNI report (janvier 2017) établit l’attribution à la Russie avec « haute confiance ». Indictment DOJ 2018 inculpe nommément 12 officiers du GRU Unit 26165 et 13 personnes/3 entités de l’IRA. Les sanctions et expulsions diplomatiques qui suivent marquent une rupture.

**Leçons** : le cyber et l’influence sont intégrés, pas séparés. Les attributions publiques rapides (2 mois après l’élection) deviennent un standard.

#### 7.5 Bundestag 2015 et campagnes anti-OTAN continues

**Acteur** : APT28. **Paradigme** : espionnage gouvernemental stratégique.

**Bundestag (mai 2015)** : APT28 compromet le réseau IT du parlement allemand. Accès maintenu plusieurs semaines, exfiltration massive de documents parlementaires (dont certains classifiés). La découverte conduit à une reconstruction complète du réseau (des mois de travail, des dizaines de millions d’euros). La chancelière Merkel est elle-même directement visée (son adresse email personnelle parlementaire a été compromise).

**Campagnes continues OTAN** : APT28 et APT29 maintiennent un ciblage permanent des ministères de la défense, des institutions de l’OTAN (Alliance, agences), des fournisseurs de défense majeurs, et des think tanks stratégiques. Ces campagnes sont rarement publicisées en détail (les victimes ne communiquent pas), mais des fragments apparaissent dans les rapports de Mandiant, Microsoft, ANSSI. La règle : tout ce qui touche à la stratégie OTAN est une cible prioritaire des services russes.

#### 7.6 Campagne Ukraine 2022-présent

La campagne cyber russe contre l’Ukraine depuis février 2022 est la plus intense de l’histoire. Microsoft Threat Intelligence Center a publié plusieurs rapports annuels qui documentent des dizaines de campagnes distinctes et des centaines de cibles. Synthèse.

**Wipers multiples** : HermeticWiper, IsaacWiper, CaddyWiper, WhisperGate, AcidRain, plusieurs variants non catalogués. Déploiement souvent synchronisé avec des événements militaires ou politiques (invasion initiale, changements stratégiques, anniversaires).

**Attaques OT** : tentative **Industroyer2** en avril 2022 contre un opérateur électrique ukrainien — **déjouée** par le CERT-UA et ESET grâce à une détection et une réponse en quelques heures. Échec notable pour Sandworm. Des tentatives ultérieures ont été déjouées, d’autres partiellement réussies (blackouts ponctuels rapidement restaurés).

**AcidRain / Viasat (24 février 2022)** : le jour de l’invasion, Sandworm déploie AcidRain contre les terminaux satellite du fournisseur Viasat KA-SAT. Impact premier : perturbation des communications militaires ukrainiennes (dépendantes de Viasat pour certaines liaisons). Impact collatéral : **5 800 éoliennes allemandes** utilisant Viasat KA-SAT pour la télésupervision rendues inopérables — exemple frappant d’effet collatéral transfrontalier d’une cyberattaque étatique. Attribution publique par UE, UK, US en mai 2022.

**Ciblage multi-secteurs** : gouvernement ukrainien, médias, télécoms, énergie, transport, secteur financier, organisations humanitaires, infrastructure cloud. Gamaredon en continu sur le volume, Sandworm pour les opérations majeures, APT28 pour l’espionnage militaire, Unit 29155 pour les opérations déstabilisatrices.

**Coopération défensive sans précédent** : Microsoft, Google, ESET, AWS, Cloudflare, Starlink (connectivité résiliente), CERT-UA, USCYBERCOM hunt forward teams, européens (CERT-EU, ANSSI, BSI, NCSC). Cette coopération est détaillée au Ch.19 (Ukraine).

#### 7.7 Microsoft breach 2023-2024

**Acteur** : APT29. **Paradigme** : compromission cloud identity contre le plus grand fournisseur cloud du monde.

**Synthèse** : en novembre 2023, APT29 conduit un password spray contre un tenant Azure AD test non-production de Microsoft. Un compte avec des permissions héritées sur un environnement de test est compromis. L’attaquant pivote via une application OAuth legacy aux permissions Graph API excessives, qui permet l’accès aux emails de dirigeants Microsoft. Persistence établie via création d’applications OAuth supplémentaires.

**Détection** : Microsoft détecte l’intrusion en janvier 2024 (dwell time : ~2 mois). Divulgation publique le 19 janvier 2024.

**Cibles additionnelles** : Hewlett Packard Enterprise révèle une compromission liée en janvier 2024. D’autres organisations (non nommées publiquement) ont été affectées via des patterns similaires.

**Leçons** : même les fournisseurs cloud les plus matures sont vulnérables via des configurations héritées et des environnements de test. Les abus d’applications OAuth avec permissions excessives sont un vecteur APT29 récurrent. La visibilité sur les consentements OAuth et les permissions Graph API est devenue une priorité de sécurité cloud.

#### 7.8 Opérations d’influence

Les opérations d’influence russes méritent un traitement dédié car elles sont intégrées aux opérations cyber dans la doctrine hybride.

**Internet Research Agency (IRA)** : troll farm basée à Saint-Pétersbourg, liée à Evgueni Prigojine (fondateur du groupe Wagner, tué dans un accident d’avion en août 2023 après la mutinerie contre Poutine). L’IRA a conduit depuis les années 2010 des opérations massives d’influence sur les réseaux sociaux occidentaux (US, Europe). Post-Prigojine, l’organisation a connu une période d’incertitude puis a apparemment été reprise sous contrôle étatique direct.

**Doppelganger** : opération d’influence identifiée publiquement à partir de 2022. Création de faux sites web imitant l’apparence de médias occidentaux légitimes (Le Parisien, Der Spiegel, The Guardian), publication d’articles orientés, diffusion via réseaux sociaux. Démantèlements partiels par Meta, Google, et les autorités françaises. Attribution : proxies russes, avec liens suspectés aux services.

**RRN (Reliable Recent News) / Recent Reliable News** : opération similaire à Doppelganger, ciblage européen et français.

**Storm-1516** (nomenclature Microsoft, 2024) : opération de désinformation liée à la Russie, ciblant des événements politiques européens.

**Techniques** : création de volumes massifs de faux comptes (avec usage croissant d’IA générative pour les profils et le contenu), exploitation de faux sites médias, amplification via influenceurs complaisants, exploitation d’événements réels pour injecter des narratifs orientés.

**Lecture opérationnelle** : une opération d’influence russe typique coordonne plusieurs leviers (hack-and-leak si pertinent, sites médias fabriqués, comptes réseaux sociaux, amplification sur Telegram et plateformes alternatives). Les cyberopérations alimentent l’influence (vol de documents ensuite publiés), l’influence justifie les cyberopérations (campagne de préparation d’opinion avant une action cyber).

#### 7.9 Leçons : l’intégration espionnage / destruction / influence

La synthèse de l’expérience russe en cyberopérations révèle un modèle intégré unique.

**Continuum d’opérations** : espionnage, influence, sabotage et pré-positionnement ne sont pas des catégories séparées. Un même service peut conduire plusieurs types simultanément ; les TTP se recouvrent ; le renseignement collecté à un stade nourrit les opérations du stade suivant.

**Tolérance au bruit variable selon le service** : SVR (APT29) maximise la furtivité ; GRU (APT28, Sandworm, Unit 29155) accepte le bruit pour l’efficacité opérationnelle ; FSB varie (Turla ultra-furtif, Gamaredon volumineux et peu furtif).

**Utilisation du cybercrime et de l’hacktivisme comme leviers** : la tolérance tacite de l’écosystème cybercriminel russophone et l’instrumentalisation d’hacktivistes (KillNet, NoName057(16)) permettent d’augmenter la surface opérationnelle sans attribution étatique directe.

**Exposition relativement élevée** : comparé à la Chine (furtive), la Russie assume une visibilité d’opérations supérieure — les attributions publiques sont fréquentes, les indictments nombreux, les sanctions accumulées. L’appareil russe semble juger que l’impact opérationnel dépasse le coût diplomatique.

Pour l’analyste face à une intrusion compatible avec un acteur russe : la clé est de déterminer **quel service** est probablement en jeu, car cela conditionne les attentes (espionnage furtif long terme si SVR, destructif à venir si GRU, opération déstabilisatrice si Unit 29155). Cette discrimination est souvent plus importante, opérationnellement, que l’attribution à « la Russie » en général.

-----

## PARTIE III — CHINE

> **Ce que cette partie apprend.** Comprendre la doctrine cyber chinoise (long game, espionnage économique systémique, pré-positionnement stratégique), cartographier l’appareil cyber chinois (MSS civil, PLA militaire, contractors), identifier les groupes APT chinois majeurs, et analyser les campagnes et tendances récentes — y compris la rupture que constitue Volt Typhoon.
> 
> **Ce qu’elle ne couvre pas.** Le traitement approfondi de Volt Typhoon comme cas de pré-positionnement (Ch.22 et Ch.31), les aspects spécifiques OT industriels (Ch.20-21).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître un tradecraft chinois (volumétrie, DLL sideloading, long dwell time), distinguer une opération MSS d’une opération PLA, situer une compromission chinoise dans la stratégie de rattrapage technologique, et anticiper les zones de ciblage prioritaires.

-----

### Chapitre 8 — Chine : contexte, doctrine et appareil cyber

#### 8.1 Priorités géopolitiques et principes doctrinaux

La stratégie cyber chinoise ne peut pas se comprendre sans la stratégie globale de la RPC. Quatre priorités structurent l’ensemble.

**Dominance technologique et rattrapage industriel** : depuis les plans Made in China 2025 (2015) et les successeurs (China Standards 2035, stratégie IA 2030), la Chine s’est fixé comme objectif stratégique de devenir leader technologique dans une série de secteurs — semiconducteurs, IA, énergie verte, biotechnologies, aérospatial, télécommunications 5G/6G. Le cyber est un instrument central de ce rattrapage : vol de propriété intellectuelle à très grande échelle, ciblage des centres de R&D, compromission de la supply chain technologique occidentale. Les estimations américaines du préjudice cumulé du vol de propriété intellectuelle par la Chine sont contestées mais situent l’ordre de grandeur en centaines de milliards de dollars par an.

**Question Taïwan** : la réunification avec Taïwan est une priorité stratégique fondamentale du PCC. Le cyber sert la préparation à plusieurs niveaux : collecte de renseignement sur les positions américaines et alliées dans le Pacifique (pré-positionnement dans les infrastructures US de Guam et du Pacifique — documenté par Volt Typhoon), ciblage des institutions taïwanaises (gouvernement, défense, partis politiques), influence sur l’opinion taïwanaise (opérations sur les réseaux sociaux).

**Route de la Soie numérique** : extension géo-économique de la Belt and Road Initiative dans l’espace numérique. Fourniture d’infrastructures télécoms et de surveillance à des partenaires internationaux (Huawei, ZTE, Dahua, Hikvision), exportation de modèles de gouvernance numérique, accès privilégié aux données des partenaires. Le cyber alimente cette stratégie par la collecte sur les concurrents et la présence dans les nouvelles infrastructures.

**Contrôle politique interne et répression étendue** : surveillance des Ouïghours, Tibétains, dissidents, défenseurs des droits humains, médias indépendants, communautés religieuses non-autorisées. Le ciblage de la diaspora (surveillance à l’étranger, pressions sur les familles restées en Chine) est documenté dans de nombreux cas. Le cyber est intégré à cette architecture de contrôle.

**Doctrine de la « guerre sans limites »** : formulée par les colonels Qiao Liang et Wang Xiangsui dans *Unrestricted Warfare* (1999), elle postule que la guerre ne se limite pas aux moyens militaires et peut se mener sur tous les terrains (économique, financier, informationnel, cyber, juridique). Cette formulation informe la vision intégrée du cyber comme instrument de puissance.

**Integrated Deterrence et long game** : contrairement à la doctrine russe qui accepte l’escalade destructive ouverte, la doctrine chinoise privilégie le long terme, la patience, et l’intégration multi-instruments. L’activation publique destructive est rare ; l’espionnage massif et le pré-positionnement sont la norme. Le **dwell time** des opérations chinoises est souvent parmi les plus longs observés — des intrusions documentées ont été maintenues 5 à 10 ans avant découverte.

#### 8.2 Le MSS : renseignement civil et décentralisation opérationnelle

Le **MSS** (Ministry of State Security, 国家安全部) est le principal service de renseignement civil chinois. Successeur de plusieurs organes historiques (réorganisé en 1983), il conduit à la fois le renseignement extérieur, le contre-espionnage intérieur, et une partie de la répression politique.

Une spécificité structurante du MSS : la **décentralisation opérationnelle**. Contrairement à une agence centralisée type NSA, le MSS fonctionne via un **réseau de bureaux régionaux** (au niveau des provinces et de certaines grandes villes) qui disposent d’une autonomie opérationnelle significative. Plusieurs bureaux régionaux ont été publiquement identifiés comme conduisant des cyberopérations :

- **MSS Tianjin Bureau** : associé à **APT10** / Stone Panda. Indicté publiquement par le DOJ US en décembre 2018 — noms spécifiques d’opérateurs MSS Tianjin publiés.
- **MSS Hainan State Security Department** : associé à **APT40** / Leviathan. Indicté DOJ en juillet 2021, avec la création d’une société écran (« Hainan Xiandun Technology Development Co. ») pour la couverture opérationnelle.
- **MSS Shanghai Bureau**, **MSS Guangzhou Bureau**, **MSS Jiangsu Bureau** : d’autres bureaux régionaux identifiés dans divers rapports.

Cette décentralisation a des conséquences pour l’analyse : différents bureaux régionaux ont des tradecrafts légèrement différents, des priorités sectorielles distinctes, et parfois des chevauchements qui suggèrent une coordination imparfaite entre bureaux. Le MSS central fournit l’orientation stratégique, mais l’exécution opérationnelle peut varier.

#### 8.3 Le PLA : réorganisation post-2015 et SSF

L’appareil cyber militaire chinois a connu une **réorganisation majeure en 2015-2016**. L’emblématique **Unit 61398** (Shanghai, département 3 du PLA — identifiée publiquement par Mandiant en 2013, inculpée par le DOJ en 2014) a été dissoute dans sa forme initiale. Les capacités cyber militaires ont été regroupées dans la **Strategic Support Force (SSF)** créée en décembre 2015, qui rassemble cyber, espace, guerre électronique et opérations d’information dans une structure unifiée.

La SSF comprend un **Network Systems Department** (NSD) qui est la branche cyber principale du PLA. Des rapports récents suggèrent que la SSF a été elle-même réorganisée en 2024 dans une nouvelle structure (Information Support Force), mais les informations publiques sur ces évolutions restent partielles.

Des unités spécifiques du PLA continuent d’être associées à des opérations cyber : unités successeurs de l’ancienne Unit 61398, **Unit 78020** (Chengdu Region Technical Reconnaissance Bureau) associée à plusieurs opérations de ciblage de l’Inde et de l’Asie du Sud-Est, **Unit 61486** et autres TRB (Technical Reconnaissance Bureaux).

La distinction MSS/PLA pour l’attribution des opérations : **le MSS tend à mener l’espionnage stratégique et économique, le PLA tend à mener les opérations de reconnaissance militaire et le pré-positionnement**. Mais les frontières sont perméables et plusieurs groupes APT ont des liens mixtes ou suspectés avec les deux.

#### 8.4 Le modèle des contractors civils

Une caractéristique unique de l’écosystème cyber chinois est l’**utilisation massive de contractors civils** pour les opérations offensives. Des entreprises privées chinoises sont mandatées par le MSS ou le PLA pour conduire des opérations cyber — soit pour la conception d’outils, soit pour l’opération directe.

Ce modèle offre plusieurs avantages pour l’État chinois : déni plausible (les opérateurs ne sont pas formellement des employés de l’État), flexibilité des ressources (monter en capacité sans créer d’emplois publics), accès à des talents (attirer des profils qui ne travailleraient pas dans le secteur public), compartimentation (limiter la visibilité interne sur les opérations).

#### 8.5 Le leak i-Soon de février 2024

**i-Soon (Anxun Information Technology)** est une société basée à Shanghai, spécialisée en outils de surveillance et en opérations cyber pour le compte de multiples clients gouvernementaux chinois (MSS, PLA, polices provinciales). **En février 2024, un leak massif de données internes d’i-Soon** a révélé le fonctionnement de cet écosystème de contractors.

Plus de 500 fichiers ont été publiés sur GitHub par un contributeur anonyme (probablement un mécontent interne). Le leak comprend : échanges internes (WeChat, emails), documentation technique d’outils offensifs, listings de victimes, listings de clients gouvernementaux, négociations commerciales, plaintes d’employés.

**Outils documentés** :

- Implants Windows avec capacités keylogging, capture d’écran, exfiltration.
- Implants Android avec capacités SMS, géolocalisation, microphone.
- Plateforme de Twitter/X monitoring et manipulation (faux comptes, amplification).
- Outils de bruteforce Outlook et de phishing.
- Plateforme de surveillance mobile vendue à des bureaux de sécurité publique chinois pour la surveillance de dissidents et de minorités.
- Outils de ciblage de routeurs et NAS.

**Clients identifiés** : MSS (central et bureaux régionaux), bureaux de sécurité publique de nombreuses provinces, PLA.

**Victimes documentées** : ciblage de gouvernements asiatiques (Mongolie, Népal, Pakistan, Malaisie, Thaïlande, Vietnam, Cambodge, Laos), d’organisations des droits humains, de médias, de militants Hong Kong, et de la diaspora ouïghoure.

**Impact analytique** : confirmation directe de l’écosystème contractor, des relations client-fournisseur entre entités étatiques chinoises et entreprises privées, et de l’ampleur du ciblage de dissidents et de minorités. L’analyse détaillée du leak a été publiée par SentinelOne, Sekoia, Harfang Lab, et plusieurs chercheurs indépendants. Elle reste une lecture essentielle pour comprendre l’écosystème cyber chinois contemporain.

#### 8.6 Ciblage sectoriel : les priorités chinoises

Les priorités de ciblage chinoises révèlent les priorités stratégiques.

**Semiconducteurs et high-tech** : priorité absolue. Ciblage de TSMC, ASML, Applied Materials, Tokyo Electron, Samsung — et de toute la supply chain. Objectif : rattraper le retard technologique dans un secteur où les sanctions américaines (CHIPS Act 2022) ont durci les restrictions d’exportation.

**Aéronautique et défense** : Lockheed Martin, Boeing, BAE Systems, Airbus, Dassault, Thales. Le programme F-35 est documenté comme largement compromis par des acteurs chinois depuis les années 2000, ce qui aurait contribué au développement accéléré du chasseur J-20 chinois.

**Énergie** : pétrole/gaz, nucléaire, énergies renouvelables. Pré-positionnement documenté dans les infrastructures électriques US et du Pacifique (Volt Typhoon).

**Biotechnologies et pharmaceutique** : vol de recherche (vaccins COVID en 2020, thérapies oncologiques, biotechnologies d’avant-garde). Ciblage particulièrement intense depuis 2020.

**Maritime et logistique** : APT40 a été massivement actif contre les entreprises maritimes, les ports, et les chantiers navals. Reflète l’intérêt chinois pour la domination maritime.

**Télécommunications** : infrastructure télécom, équipementiers, opérateurs. **Salt Typhoon** (2024) a compromis des systèmes d’interception légale de multiples opérateurs télécoms US — accès potentiel aux communications de millions d’Américains.

**Diaspora et minorités** : Ouïghours, Tibétains, Hongkongais, dissidents. Utilisation du cyber pour la surveillance à l’étranger, la collecte sur les familles restées en Chine, et parfois le harcèlement.

**Think tanks et académique** : producteurs d’analyses sur la Chine (CSIS, Atlantic Council, Chatham House, IFRI, etc.), universités spécialisées en études chinoises, chercheurs individuels.

**Politique** : ciblage de parlementaires (APT31 contre le UK et le US), partis politiques, membres de la société civile engagés dans les politiques Chine.

#### 8.7 Fil rouge — BLACKOUT Épisode 4

> **⚡ BLACKOUT — Épisode 4 : la compatibilité avec le profil chinois**
> 
> Le CERT examine si les TTP observées sur BLACKOUT sont compatibles avec les acteurs chinois documentés, notamment Volt Typhoon et clusters similaires.
> 
> **Cohérences** :
> 
> - **Exploitation d’appliance edge (Ivanti CVE-2024-21887)** : Volt Typhoon et plusieurs autres acteurs chinois ont massivement exploité Ivanti fin 2023 / début 2024 (advisory CISA de février 2024). **Forte cohérence avec le profil chinois**.
> - **Living off the Land** : Volt Typhoon se caractérise par un LotL quasi exclusif, avec peu ou pas de malware custom. BLACKOUT montre un PsExec, du Kerberoasting, du DLL sideloading — beaucoup de LotL, et pas de malware custom identifié à ce stade. **Cohérence forte**.
> - **Pré-positionnement OT sans action** : signature exacte de Volt Typhoon, qui maintient des accès dans les infrastructures critiques US sans action observable. **Cohérence très forte**.
> - **Patience opérationnelle** : l’attaquant est présent depuis au moins 42 jours sans action visible. Long dwell time cohérent avec le profil chinois.
> 
> **Décalages** :
> 
> - **Géographie** : Volt Typhoon a été principalement documenté aux US et dans le Pacifique (Guam). Un opérateur énergie européen est une cible inhabituelle pour ce cluster spécifique, même si des cibles européennes ne sont pas exclues et que des clusters chinois similaires peuvent être actifs en Europe.
> - **Beaconing régulier (27 min ± 3 min)** : Volt Typhoon a plutôt des patterns d’activité très irréguliers (accès ponctuels via les routeurs SOHO compromis). Un beaconing régulier serait plus atypique. Mais d’autres clusters chinois utilisent bien du beaconing classique.
> - **Contexte géopolitique immédiat** : pas de tension Taïwan aiguë à la date de l’incident, ce qui rend un déclenchement de pré-positionnement chinois à ce moment précis moins « naturel » que le pré-positionnement russe (conflit ukrainien actif).
> 
> **Diagnostic CERT** : profil **également compatible avec un acteur chinois** — peut-être pas Volt Typhoon spécifiquement, mais un cluster chinois lié. **H2 Chine** reste plausible, avec une confiance à ce stade entre faible et modérée.
> 
> L’incertitude demeure. Le CERT continue l’investigation — notamment pour identifier des artefacts techniques additionnels qui pourraient trancher entre profil russe et profil chinois.

-----

### Chapitre 9 — Chine : les groupes APT en détail

Ce chapitre approfondit le profil des neuf groupes APT chinois les plus importants. Chaque profil couvre mission, TTP signature, OPSEC, campagnes emblématiques.

#### 9.1 APT41 / Winnti / Barium / Brass Typhoon

**Attribution** : services d’État chinois, probablement MSS. Indicté par le DOJ US en août 2020 — 5 ressortissants chinois nommés, associés au MSS.

**Particularité historique** : **le double casquette espionnage étatique + cybercrime personnel**. APT41 mène des opérations d’espionnage validées par l’État chinois **et simultanément** des opérations cybercriminelles personnelles (ciblage de l’industrie du jeu vidéo pour voler de la monnaie virtuelle, ransomware opportuniste, fraude). Cette double activité est unique dans l’écosystème APT mondial et reflète probablement une tolérance étatique.

**Mission étatique** : espionnage industriel (santé, télécoms, high-tech, défense), ciblage politique, reconnaissance géopolitique.

**TTP signature** :

- **Supply chain compromise** massif : **CCleaner** (2017, 2,27 millions de machines infectées), **ASUS LiveUpdate** (opération ShadowHammer, 2018-2019), divers sites.
- **Exploitation rapide de vulnérabilités** : APT41 exploite des CVE dans les heures ou jours suivant publication, notamment sur Citrix, Microsoft Exchange, Pulse Secure, F5.
- **Rootkits et bootkits** : MoonBounce (bootkit UEFI), famille Winnti (implant Windows/Linux, la signature), PipeMon, Crosswalk.
- **Mouvement latéral** : RDP, SMB, Impacket, Mimikatz.

**Campagnes majeures** :

- **Opérations supply chain CCleaner et ASUS** : infection massive initiale, ciblage sélectif en phase 2.
- **Ciblage sanitaire COVID-19** (2020) : exfiltration de recherche vaccin.
- **Opérations contre l’industrie du jeu vidéo** : ciblage d’éditeurs asiatiques.
- **Indictment 2020** : 5 ressortissants nommés, responsables d’opérations contre 100+ victimes dans multiple pays.

#### 9.2 APT40 / Leviathan / TA423 (MSS Hainan)

**Attribution** : MSS Hainan State Security Department, publiquement établie par l’indictment DOJ de juillet 2021 (4 ressortissants chinois nommés, société écran Hainan Xiandun Technology Development).

**Mission** : ciblage maritime, naval, et Five Eyes. Priorités : domaine maritime (ports, chantiers navals, industrie maritime), universités spécialisées en technologies navales, recherche sous-marine, équipementiers militaires alliés.

**TTP signature** :

- **Exploitation d’appliances réseau** : APT40 est un exploiteur massif de vulnérabilités sur les appliances edge. Advisory international de juillet 2024 (AUKUS + Canada + Allemagne + Japon + Corée du Sud + Nouvelle-Zélande) détaille l’exploitation par APT40 de plusieurs CVE en days (voire heures) suivant leur publication — Ivanti, Fortinet, Citrix, SonicWall.
- **Web shells** : déploiement systématique (China Chopper notamment) pour la persistance.
- **Scripts PowerShell et LotL**.
- **Mouvement latéral** : Impacket, WMI, PsExec.
- **Exfiltration via cloud storage** (MEGA, OneDrive).

**Campagnes majeures** : ciblage maritime et naval (2013-présent) sur universités australiennes, canadiennes, américaines spécialisées maritime ; opérations contre les élections cambodgiennes (2018) ; exploitation massive Ivanti Connect Secure (2024).

#### 9.3 APT10 / Stone Panda / Red Apollo (MSS Tianjin)

**Attribution** : MSS Tianjin Bureau, établie publiquement par l’indictment DOJ de décembre 2018 (2 ressortissants chinois nommés).

**Mission** : espionnage industriel massif, avec ciblage particulier des **MSP** (Managed Service Providers) pour atteindre leurs clients finaux.

**TTP signature** :

- **Opération Cloud Hopper** (2014-2018, détaillée au Ch.10) : compromission de grands MSP mondiaux pour pivoter vers leurs clients — multiplication du scope d’une seule compromission par des centaines de clients accessibles.
- **Spear-phishing** ciblé avec macros Office.
- **Malware custom** : HAYMAKER, PlugX (partagé avec d’autres APT chinoises), Redleaves, ChChes, UPPERCUT.
- **Living off the Land** et web shells.

**Campagnes majeures** :

- **Opération Cloud Hopper** : compromission de plusieurs grands MSP internationaux (IBM, HPE notamment) entre 2014 et 2018, pivot vers les clients des MSP. Un des cas emblématiques de compromission supply chain via prestataire. Documenté par PwC et BAE Systems (2017).
- **Ciblage industriel** : aéronautique, ingénierie, pharmaceutique, énergie dans de multiples pays.

**Évolution** : APT10 moins visible post-indictment 2018 — probablement réorganisation ou fragmentation, mais plusieurs opérations récentes suggèrent que des opérateurs anciens d’APT10 sont toujours actifs sous d’autres clusters.

#### 9.4 APT31 / Judgment Panda / Zirconium

**Attribution** : MSS, établie par indictments DOJ (mars 2024) et actions UK (mars 2024). 7 ressortissants chinois nommés, association explicite au MSS Hubei State Security Department.

**Mission** : espionnage politique ciblé. Cibles particulières : parlementaires, opposants politiques, journalistes critiques, entreprises de défense et aérospatiales.

**TTP signature** :

- **Spear-phishing** très ciblé avec emails de suivi et escalade sociale.
- **Exploitation de vulnérabilités Exchange** (notamment lors de la vague ProxyLogon 2021).
- **Ciblage d’infrastructure electorale** : APT31 a été identifié comme ciblant des infrastructures associées à des campagnes politiques.

**Campagnes majeures** :

- **Ciblage parlementaires UK** : en 2024, le UK a publiquement attribué à APT31 des ciblages de parlementaires britanniques critiques de la Chine (incluant des membres de l’Inter-Parliamentary Alliance on China — IPAC).
- **Ciblage US** : campagnes similaires documentées contre des parlementaires et décideurs US.
- **Infrastructure électorale** : ciblage de la Commission électorale britannique (2021-2022, révélé publiquement en 2024).

**Impact** : les indictments 2024 ont été accompagnés de **sanctions coordonnées** (US, UK, NZ) contre les personnes nommées et l’entreprise écran associée (Wuhan Xiaoruizhi Science and Technology). Démonstration de la coopération diplomatique renforcée dans la réponse aux APT chinois.

#### 9.5 Volt Typhoon

**Attribution** : PRC state-sponsored, probablement PLA ou affilié. Advisory conjoint NSA/CISA/FBI + Five Eyes (mai 2023, réitéré 2024). Aucun indictment public à date, contrairement à d’autres groupes.

**Mission** : **pré-positionnement stratégique dans les infrastructures critiques américaines et du Pacifique**. Pas d’espionnage massif, pas d’exfiltration, pas d’action destructive. Uniquement : établir et maintenir un accès dormant.

**Cibles documentées** : opérateurs de télécommunications, fournisseurs d’énergie électrique, systèmes d’eau, infrastructures de transport aux États-Unis et dans les territoires du Pacifique (Guam est particulièrement ciblée — point stratégique en cas de conflit Taïwan).

**TTP signature** — le profil Volt Typhoon est **extrême dans sa pureté opérationnelle** :

- **Exploitation d’appliances edge** : vulnérabilités sur routeurs SOHO, VPN, firewalls non patchés (Fortinet FortiGate, Cisco RV, NetGear, ASUS RT).
- **LotL quasi exclusif** : PowerShell, WMI, net.exe, ntdsutil, ping, tracert, ipconfig, netsh, reg.exe, wmic, certutil. **Aucun malware custom identifié** à date de l’advisory 2023.
- **Credentials légitimes** : vol de credentials admin via credential dumping puis utilisation prolongée. Aucun compte créé par l’attaquant (éviterait la détection).
- **C2 via routeurs SOHO compromis** : les implants utilisent des **routeurs résidentiels compromis** (des clients domestiques US) comme points de sortie. Le trafic C2 semble donc provenir d’IP résidentielles US légitimes — fondement dans le trafic domestique, détection réseau quasi impossible sans inspection approfondie.
- **Activité très intermittente** : pas de beaconing régulier, accès occasionnels, actions limitées au minimum nécessaire pour maintenir la présence.

**Signification stratégique** : Volt Typhoon est interprété par la communauté de renseignement américaine comme une **capacité de dissuasion/représailles chinoise** liée au scénario Taïwan. Le message implicite : « si vous intervenez militairement pour défendre Taïwan, nous pouvons frapper vos infrastructures critiques ». C’est potentiellement la menace cyber stratégique qui définira la prochaine décennie.

**Démantèlement partiel** : le FBI a démantelé en janvier 2024 un botnet de routeurs Cisco RV domestiques qui servait d’infrastructure C2 à Volt Typhoon. Opération **KV Botnet**, conduite sous mandat judiciaire. Le botnet a été neutralisé, mais Volt Typhoon dispose probablement d’infrastructures alternatives.

**Traitement détaillé** : Ch.22 (pré-positionnement comme paradigme) et Ch.31 (cas complet).

#### 9.6 Salt Typhoon

**Attribution** : PRC state-sponsored, advisory CISA et partenaires (fin 2024). Attribution fine (MSS ou PLA) non publiquement précisée à date.

**Mission** : **espionnage via compromission des opérateurs télécoms**. Cibles principales : grands opérateurs télécoms américains (Verizon, AT&T, Lumen, et d’autres). Objectif : accès aux systèmes d’interception légale et aux communications de personnalités et cibles de haute valeur.

**Révélation publique** (octobre-décembre 2024) : le gouvernement américain a confirmé que Salt Typhoon avait compromis de multiples opérateurs télécoms US et maintenu l’accès pendant potentiellement plus d’un an. Les systèmes compromis incluaient les **Lawful Intercept Systems** — ceux utilisés par les opérateurs pour se conformer aux demandes légales d’interception des autorités américaines. La compromission de ces systèmes signifie que les attaquants pouvaient potentiellement voir **qui les autorités américaines surveillaient** — information stratégique majeure.

**Impact additionnel** : accès aux communications (appels, SMS, métadonnées) de millions d’Américains, incluant potentiellement des personnalités politiques (campagnes présidentielles Trump et Harris sont citées parmi les cibles confirmées). La gravité a conduit à des auditions au Congrès US et à des directives CISA obligeant les opérateurs à durcir leur infrastructure.

**TTP** : exploitation d’appliances edge, LotL, persistence via modifications de configurations légitimes des équipements télécoms. Sophistication comparable à Volt Typhoon mais avec un objectif différent (espionnage ciblé plutôt que pré-positionnement).

#### 9.7 Flax Typhoon et Raptor Train

**Attribution** : PRC state-sponsored, liens avec la société **Integrity Technology Group** (basée à Pékin) — entreprise sanctionnée par l’OFAC en janvier 2025.

**Mission** : construction et opération d’un **botnet massif de dispositifs IoT compromis** (routeurs, caméras, NAS) pour servir d’infrastructure d’attaque à d’autres acteurs chinois. Modèle de « cyber-logistique » offensive.

**Opération Raptor Train** : le FBI, coordonné avec des partenaires internationaux, a démantelé en septembre 2024 le botnet **Raptor Train** opéré par Flax Typhoon. Le botnet comprenait **plus de 260 000 dispositifs compromis** dans le monde — dont une majorité aux États-Unis et en Europe. Les dispositifs compromis étaient utilisés comme nœuds relais pour d’autres opérations APT chinoises, masquant l’origine réelle des attaques.

**Leçon** : l’écosystème cyber chinois a industrialisé la production d’infrastructure offensive via des contractors spécialisés. Ce modèle rappelle certaines pratiques de cybercriminalité organisée (Infrastructure-as-a-Service) mais appliqué aux opérations étatiques.

#### 9.8 Mustang Panda / Bronze President / HoneyMyte

**Attribution** : PRC state-sponsored, MSS probablement.

**Mission** : ciblage principal de la **diaspora chinoise et des minorités** (Tibétains, Ouïghours, opposants politiques Hong Kong), **ASEAN**, **Europe** (depuis 2022 notamment).

**TTP signature** :

- **Spear-phishing** avec documents leurre très contextualisés (thèmes sur la diaspora, les ONG, les affaires asiatiques, les tensions régionales).
- **Malware signature** : **PlugX** (backdoor historique largement utilisée par les APT chinoises, variantes propres à Mustang Panda), **ToneShell**, **Korplug** (ancêtre PlugX), **Hodur**.
- **USB-based propagation** : Mustang Panda utilise activement les clés USB comme vecteur de propagation vers des réseaux moins connectés (diaspora, ONG en zones de conflit).
- **DLL sideloading** massif : signature technique retrouvée dans quasi toutes les opérations Mustang Panda.

**Campagnes récentes** :

- **Ciblage ONG et diaspora tibétaine/ouïghoure** (continu).
- **Ciblage gouvernements européens** (2022-2025) : notamment autour du conflit ukrainien et des sujets Taïwan. Documenté par ESET, Check Point, Trend Micro.
- **Ciblage ASEAN** : activité continue sur les pays d’Asie du Sud-Est (Philippines, Vietnam, Indonésie, Thaïlande).

#### 9.9 APT27 / Emissary Panda / Bronze Union

**Attribution** : PRC state-sponsored.

**Mission** : espionnage industriel (industrie, défense, énergie, aérospatial), avec ciblage historique large (US, Europe, Moyen-Orient).

**TTP signature** :

- **Watering hole attacks** : compromission de sites fréquentés par les cibles.
- **Exploitation de vulnérabilités** sur serveurs exposés.
- **Malware** : **HyperBro** (backdoor signature), **SysUpdate**, **ZxShell**.
- **Web shells** pour persistence.
- **DLL sideloading**.

**Activité récente** : moins documentée que les autres groupes mais persistante. Ciblage observé contre des organisations européennes de défense et d’ingénierie.

-----

### Chapitre 10 — Chine : campagnes de référence et tendances 2023-2026

Ce chapitre présente les campagnes chinoises les plus emblématiques, et analyse les tendances récentes qui dessinent l’évolution de la menace.

#### 10.1 Opération Cloud Hopper (APT10, 2014-2018)

**Acteur** : APT10 (MSS Tianjin). **Paradigme** : compromission des **MSP** (Managed Service Providers) comme multiplicateur de scope.

**Synthèse** : entre 2014 et 2018, APT10 a compromis un ensemble de grands **MSP internationaux** — entreprises qui gèrent l’infrastructure IT de centaines ou milliers de clients finaux. Parmi les MSP compromis (documentés publiquement) : IBM, HPE, et plusieurs autres. Une fois dans le MSP, APT10 utilisait les accès privilégiés légitimes du MSP vers ses clients pour pénétrer leurs environnements — pivot silencieux, protégé par la confiance implicite qui existe entre un MSP et ses clients.

**Scope victimes** : estimations entre des dizaines et des centaines de clients finaux touchés à travers le monde, dans des secteurs variés (aérospatial, ingénierie, énergie, télécoms, pharma, médias).

**Découverte et publication** : l’opération a été découverte et documentée publiquement en 2017-2018 par **PwC** et **BAE Systems** dans un rapport conjoint. L’indictment DOJ de décembre 2018 a consolidé l’attribution à APT10 / MSS Tianjin et nommé deux ressortissants chinois.

**Leçons** :

- La supply chain IT (MSP, fournisseurs de services managés) est un vecteur APT majeur. Un MSP compromis expose des dizaines à des milliers de clients.
- La confiance implicite entre prestataire et client doit être réévaluée (Zero Trust appliqué aux prestataires internes).
- Les prestataires doivent être considérés comme faisant partie du périmètre de sécurité — d’où les obligations de sécurité renforcées imposées aux MSP par NIS 2.

#### 10.2 Hafnium / ProxyLogon (2021)

**Acteur** : Hafnium (MSS, probablement Hubei). **Paradigme** : exploitation massive d’une vulnérabilité 0-day Exchange pour compromettre des dizaines de milliers d’organisations en quelques jours.

**Synthèse** : début mars 2021, Microsoft publie des correctifs d’urgence pour quatre vulnérabilités Exchange (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065 — collectivement nommées **ProxyLogon**). L’exploitation avait commencé début janvier 2021 par un acteur étatique (Hafnium) de manière ciblée. À partir de fin février / début mars 2021, l’exploitation s’est massifiée — des dizaines de groupes ont commencé à exploiter la vulnérabilité, souvent pour déposer des web shells pour un accès futur.

**Impact** : estimations entre **30 000 et 250 000 organisations compromises mondialement** en l’espace de quelques semaines. Impact massif sur les organisations européennes notamment, beaucoup utilisant Exchange on-premises. Le MOIE français (Ministère de l’Intérieur) et de nombreuses administrations européennes ont été affectés.

**Attribution publique** : en juillet 2021, les États-Unis, le Royaume-Uni, l’Union européenne, l’OTAN et plusieurs autres pays ont conjointement attribué ProxyLogon au MSS chinois — une attribution publique coordonnée sans précédent dans sa portée.

**Leçons** :

- Les vulnérabilités 0-day sur les services exposés massivement (Exchange, VPN, passerelles) produisent des compromissions industrielles.
- La prolifération post-publication est massive : une fois une CVE connue, elle est exploitée par des dizaines d’acteurs en quelques jours.
- Le patching d’urgence des services exposés est un impératif.

#### 10.3 Microsoft 2023 / Storm-0558

**Acteur** : Storm-0558 (nomenclature Microsoft, acteur chinois sous investigation). **Paradigme** : compromission d’une clé de signature cloud permettant l’accès aux emails gouvernementaux.

**Synthèse** : en juillet 2023, Microsoft révèle publiquement que Storm-0558 a compromis une **clé privée de signature MSA** (Microsoft Account) en 2021 et l’a utilisée pour forger des tokens d’authentification permettant d’accéder aux emails Outlook.com et à certaines ressources Exchange Online. Le groupe a utilisé ces tokens pour accéder aux emails d’**environ 25 organisations gouvernementales**, dont le Département d’État américain et des gouvernements européens.

L’enquête ultérieure, notamment par la **Cyber Safety Review Board** (CSRB — institution fédérale américaine), a produit un **rapport public** en 2024 qui est une lecture fondatrice pour comprendre les défaillances dans la sécurité du cloud Microsoft. Le rapport identifie une série de défaillances : gestion inadéquate des clés cryptographiques, visibilité insuffisante des anomalies, culture de sécurité critiquée.

**Impact** :

- Accès à des communications gouvernementales sensibles américaines et européennes pendant plusieurs mois.
- Érosion de la confiance dans la sécurité cloud de Microsoft — directe conséquence commerciale et politique.
- Déclenchement d’investigations réglementaires et de durcissements imposés.

**Distinction avec le breach Microsoft 2023-2024 par APT29** : ce sont **deux incidents distincts**. Storm-0558 (MSS chinois) en juillet 2023 via compromission de clé de signature ; APT29 (SVR russe) en novembre 2023 - janvier 2024 via password spray et OAuth abuse.

#### 10.4 Salt Typhoon 2024 — le breach télécoms US

**Acteur** : Salt Typhoon (PRC). **Paradigme** : espionnage stratégique via compromission des télécoms.

**Synthèse** : révélé publiquement entre octobre et décembre 2024, Salt Typhoon a compromis de multiples opérateurs télécoms américains majeurs (Verizon, AT&T, Lumen confirmés ; d’autres suspectés ou en investigation). La compromission aurait duré **au moins un an, peut-être davantage**, avant détection.

**Accès obtenu** :

- **Systèmes d’interception légale (CALEA — Communications Assistance for Law Enforcement Act)** : les systèmes utilisés par les opérateurs pour répondre aux demandes d’interception des autorités américaines. Accès à ces systèmes signifie **voir qui les autorités surveillaient** — contre-espionnage d’une valeur stratégique exceptionnelle.
- **Communications** : appels, SMS, métadonnées de millions d’utilisateurs, avec ciblage particulier de personnalités politiques et décideurs (campagnes présidentielles Trump et Harris citées).

**Réponse** :

- Auditions au Congrès.
- Directives CISA obligeant le durcissement de l’infrastructure télécom.
- Recommandation publique d’utiliser le chiffrement de bout en bout (Signal, WhatsApp) pour les communications sensibles — officiels US ont pour la première fois publiquement recommandé des messageries chiffrées plutôt que SMS/appels classiques.

**Leçons** : les infrastructures télécoms sont des cibles APT de premier ordre. Les systèmes d’interception légale sont des cibles extrêmement sensibles — un État adversaire qui les compromet retourne littéralement la capacité de surveillance contre son propriétaire.

#### 10.5 Mustang Panda contre l’Europe 2023-2025

**Acteur** : Mustang Panda. **Paradigme** : extension géographique du ciblage chinois vers l’Europe dans le contexte du conflit ukrainien et des tensions Taïwan.

**Synthèse** : depuis 2022, Mustang Panda a intensifié ses opérations contre des cibles européennes. Objectifs probables : collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine (et de la Russie), collecte sur les positions Taïwan, ciblage des ONG pro-démocratie, surveillance de la diaspora chinoise en Europe.

**Campagnes documentées** :

- ESET a publié plusieurs rapports (2022-2024) documentant le ciblage européen par Mustang Panda, notamment gouvernements, fournisseurs de défense, ONG spécialisées.
- Check Point a documenté l’exploitation de thèmes géopolitiques (Ukraine, Taïwan, relations UE-Chine) comme leurres de phishing.

**Impact** : pas de compromission massive publiquement revendiquée, mais confirmation d’une présence chinoise significative dans le paysage cyber européen — rappel que l’Europe n’est pas épargnée par les APT chinoises malgré une focalisation historique perçue sur les États-Unis et l’Asie.

#### 10.6 Campagnes contre les infrastructures critiques européennes

Plusieurs rapports 2023-2025 documentent des campagnes chinoises contre des infrastructures critiques en Europe :

**Secteur énergie** : ciblage d’opérateurs de distribution d’électricité, d’opérateurs pétroliers et gaziers. Advisory ANSSI et BSI ont mentionné publiquement des tentatives d’intrusion sans détailler les cibles.

**Télécommunications européennes** : ciblage de plusieurs opérateurs télécoms européens dans une extension probable du modèle Salt Typhoon.

**Secteur maritime** : APT40 continue d’être très actif contre les ports européens (Rotterdam, Hambourg, Anvers notamment) et les entreprises maritimes européennes.

**Infrastructures de recherche** : universités techniques européennes, centres R&D.

La tendance : l’Europe est un théâtre APT chinois croissant, moins documenté publiquement que les États-Unis (les pays européens communiquent moins sur les incidents étatiques) mais actif.

#### 10.7 Évolution du tradecraft chinois

Le tradecraft chinois a évolué significativement sur la période 2015-2026. Synthèse des évolutions.

**Phase 1 (années 2000 - 2014) : force brute et volumétrie**. L’approche Unit 61398 et APT10 historique : scan massif, exploitation opportuniste, phishing de masse. Beaucoup de cibles, sophistication technique modeste, OPSEC moyen. Le rapport Mandiant APT1 de 2013 a catalysé une prise de conscience et probablement une réorganisation.

**Phase 2 (2015 - 2020) : consolidation et professionnalisation**. Réorganisations post-Unit 61398 et post-accord Xi-Obama (2015, qui a temporairement fait baisser l’espionnage économique chinois aux US). Émergence de groupes plus compartimentés, professionnalisation des TTP, adoption de techniques modernes (DLL sideloading, abus de services légitimes).

**Phase 3 (2020 - présent) : furtivité et pré-positionnement**. L’émergence de Volt Typhoon (2021+) marque une rupture : groupes chinois capables d’opérations ultra-furtives, LotL exclusif, maintenant des accès pendant des années sans signaux détectables. Le ciblage s’oriente vers les appliances edge (cibles sans EDR, privilégiées), les télécoms (pour l’espionnage stratégique), et les infrastructures critiques (pour le pré-positionnement).

**Phase 4 émergente (2024+) : industrialisation via contractors**. Le leak i-Soon a révélé l’étendue de l’écosystème contractor civil. Le modèle se professionnalise : des entreprises développent des outils à destination de multiples clients étatiques, produisent des infrastructures réutilisables (Raptor Train), fournissent des services « clé en main ».

La trajectoire : montée en sophistication continue, fragmentation croissante entre services officiels et contractors multiples, extension géographique (moins concentré US, plus global), et augmentation du volume d’opérations sous-radar qui ne sont identifiées que après plusieurs années de maintien d’accès.

#### 10.8 Tendance structurelle : fragmentation de l’attribution

La conséquence analytique majeure de ces évolutions : l’**attribution précise des opérations chinoises est devenue plus difficile**, pas moins. Pourquoi ?

**Prolifération des groupes** : des dizaines de clusters suivis, parfois distinguables seulement par des différences marginales de TTP. Le chevauchement d’outils (PlugX utilisé par plusieurs groupes), d’infrastructure partagée, et de tradecraft similaire rend la discrimination difficile.

**Opacification des liens MSS/PLA/contractors** : qui commandite quelle opération ? Les indictments publics attribuent à des bureaux MSS spécifiques, mais les contractors peuvent travailler simultanément pour plusieurs clients étatiques, et la coordination inter-services est imparfaite.

**Sophistication croissante** : moins d’erreurs opérationnelles, moins d’artefacts d’attribution, usage intensif des abus de services légitimes et du LotL qui produisent moins de signatures.

**Implications pour l’analyste** : face à une intrusion attribuée « à la Chine », préciser **quel groupe** spécifiquement est souvent difficile ou impossible sans accès à du renseignement non-public. La discipline consiste à : (1) tester plusieurs hypothèses (MSS Hainan vs MSS Tianjin vs PLA vs contractor) via ACH, (2) coter la confiance prudemment (« probablement acteur chinois, groupe non déterminé avec confiance »), (3) ne pas laisser le prestige d’une attribution précise forcer une conclusion sous-étayée.

-----

## PARTIE IV — DPRK, IRAN ET AUTRES ACTEURS

> **Ce que cette partie apprend.** Comprendre le modèle DPRK unique au monde (cyber comme instrument économique du régime), maîtriser les profils des groupes nord-coréens (Lazarus et sous-groupes, Kimsuky, APT43), situer l’Iran dans ses rivalités régionales (MOIS vs IRGC, social engineering extrême), identifier les autres acteurs régionaux et mercenaires cyber, et comprendre les zones grises crime-État.
> 
> **Ce qu’elle ne couvre pas.** Le cas détaillé Lazarus/crypto (Ch.30), les outils techniques de détection spécifiques aux infostealers et au dark web (cours Écosystèmes cybercriminels et Dark Web), les aspects doctrinaux français et européens (Ch.26 et Annexe G).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer un ciblage financier DPRK d’un espionnage classique, reconnaître le social engineering iranien, situer les mercenaires cyber commerciaux (Pegasus, Predator) dans le paysage, et analyser les zones grises entre cybercrime et action étatique.

-----

### Chapitre 11 — DPRK : contexte, groupes et modèle unique

#### 11.1 Le cyber comme instrument économique du régime

La République Populaire Démocratique de Corée (DPRK) présente un cas **unique au monde** : c’est le seul État qui utilise le cyber **principalement comme source de revenus** pour contourner les sanctions internationales et financer le régime et son programme d’armement nucléaire et balistique.

Cette particularité découle de la configuration stratégique nord-coréenne. Sous sanctions internationales sévères depuis les années 2000 (renforcées par les résolutions ONU 2006, 2009, 2013, 2016, 2017), coupée des circuits financiers légaux, la DPRK doit financer son régime et surtout son programme nucléaire/balistique par des canaux alternatifs : commerce illégal (charbon, pêche), trafic d’êtres humains, contrefaçon de devises, et depuis les années 2010, **cybervol**.

Les estimations de revenus générés par le cyber nord-coréen varient selon les sources mais s’accordent sur des ordres de grandeur massifs :

- **Rapport ONU** (Panel of Experts) : plusieurs milliards de dollars cumulés depuis 2017.
- **Chainalysis** (rapport annuel) : en 2022, la DPRK a volé environ 1,7 milliard de dollars en crypto-actifs. En 2023, ~1 milliard. En 2024, les volumes sont repartis à la hausse. Le vol Bybit de février 2025 (~1,5 milliard de dollars) est à lui seul le plus gros vol crypto de l’histoire.
- **US Treasury / UN** : cumulé entre 3 et 6+ milliards de dollars sur la décennie 2014-2024.

Pour contextualiser : le PIB total de la DPRK est estimé à environ 30 milliards de dollars par an (difficile à mesurer précisément). Le cybervol annuel représente donc plusieurs pourcents du PIB — équivalent, en proportion, à ce qu’un État comme la France générerait s’il dégageait 80-100 milliards d’euros par an de cybervol. L’ordre de grandeur est macroéconomique.

#### 11.2 Le RGB : Reconnaissance General Bureau

Le **RGB** (정찰총국 — Reconnaissance General Bureau) est le service de renseignement militaire nord-coréen. Il supervise l’ensemble des opérations cyber offensives de la DPRK. Les opérateurs cyber sont formés dans des programmes militaires dédiés (Kim Il-sung Military University, autres institutions spécialisées) et intègrent ensuite les bureaux opérationnels du RGB.

Le RGB est structuré en plusieurs bureaux, dont les principaux pour le cyber sont :

- **Bureau 121** : cyberopérations.
- **Lab 110** : développement de malware (certaines sources indiquent une structure fluctuante).

Une caractéristique opérationnelle unique : les **opérateurs cyber nord-coréens sont souvent stationnés à l’étranger**. Principalement en Chine (Shenyang, Dandong — proches de la frontière DPRK), mais aussi en Russie, Malaisie, Singapour, et dans plusieurs pays d’Asie du Sud-Est. Raisons : meilleure connectivité Internet (la Corée du Nord a une bande passante limitée et surveillée), OPSEC (rendre le ciblage plus difficile), et évite la détection automatique par origine IP coréenne du Nord.

Cette configuration produit des artefacts d’attribution parfois trompeurs : certaines opérations Lazarus apparaissent initialement comme provenant de Chine ou de Russie, avant que l’analyse approfondie (comportement, TTP, liens avec d’autres opérations DPRK) ne confirme l’origine nord-coréenne.

#### 11.3 Lazarus Group / Diamond Sleet — vue d’ensemble

**Lazarus Group** est le nom générique sous lequel l’écosystème cyber nord-coréen est souvent regroupé. En réalité, **Lazarus est un ensemble de sous-groupes** avec des missions distinctes, tous rattachés au RGB mais avec des spécialisations fonctionnelles.

**Mission globale** : espionnage, cybervol (crypto et traditionnel), opérations ciblées politiques, et depuis 2017 opérations de dégâts collatéraux massifs (WannaCry).

**Particularités opérationnelles** :

- **Multi-plateforme** : Lazarus développe des implants Windows, macOS, Linux — l’un des rares écosystèmes APT à couvrir les trois systèmes avec la même profondeur.
- **Sophistication variable selon les opérations** : des opérations ultra-sophistiquées (3CX supply chain) côtoient des opérations plus standards.
- **Réutilisation d’infrastructure et de code** : les liens entre opérations Lazarus sont souvent détectables par des réutilisations d’outils, ce qui a facilité la consolidation du cluster.

Les principales sous-structures dans l’écosystème Lazarus :

#### 11.4 APT38 / BlueNoroff / Sapphire Sleet

**Spécialisation** : cyber-braquages financiers. Ciblage : banques, institutions financières, exchanges de crypto, plateformes DeFi.

**Campagnes historiques** :

- **Bangladesh Bank (février 2016)** : compromission du terminal SWIFT de la banque centrale du Bangladesh, transfert de 81 millions de dollars vers des comptes aux Philippines. Un 951 millions de dollars supplémentaires ont été bloqués grâce à une faute de frappe dans un ordre de virement (« fandation » au lieu de « foundation » ayant déclenché un examen manuel). **Premier cyber-braquage bancaire majeur par un acteur étatique**.
- **Ciblage continu SWIFT** : tentatives multiples contre d’autres banques (Vietnam TPBank, Équateur, plusieurs en Asie) avec des succès variables.

**Pivot crypto (2018+)** : BlueNoroff/APT38 a ensuite tourné massivement son attention vers les crypto-actifs, plus faciles à monétiser que les virements bancaires traditionnels. Ciblage d’exchanges, de services DeFi, de bridges cross-chain. Les campagnes emblématiques sont détaillées au Ch.12.

**TTP signature** :

- **Social engineering ciblé** sur employés d’institutions financières et d’exchanges crypto.
- **Malware custom multi-plateforme** : FALLCHILL, BADCALL, HOPLIGHT, DTrack, AppleJeus (macOS, ciblage spécifique crypto).
- **Supply chain** pour atteindre les clients finaux (3CX 2023 notamment, géré en cas au Ch.30).

#### 11.5 Kimsuky / Emerald Sleet

**Spécialisation** : espionnage diplomatique et nucléaire. Ciblage : chercheurs spécialisés sur la péninsule coréenne, diplomates, ministères des affaires étrangères, think tanks d’études coréennes, universités, décideurs impliqués dans les négociations sur le programme nucléaire nord-coréen.

**TTP signature** :

- **Spear-phishing extrêmement ciblé** : emails personnalisés adressés à des chercheurs et fonctionnaires nommés, avec contexte précis (invitations à des conférences, demandes d’entretien, thèmes de recherche).
- **Credential harvesting** : fausses pages de login (Gmail, ProtonMail, services académiques coréens, services gouvernementaux sud-coréens).
- **Malware** : **BabyShark** (backdoor légère), **AppleSeed**, **FlowerPower**, plusieurs RAT custom.
- **Ciblage géographique** : Corée du Sud massivement, US (think tanks et universités travaillant sur la DPRK), Europe (centres de recherche sur la non-prolifération), Japon.

**Activité continue** : Kimsuky est l’un des groupes les plus actifs en volume dans l’écosystème DPRK. Volumes élevés de phishing, campagnes quasi permanentes. Sophistication modérée mais efficacité par persistance.

#### 11.6 APT43 / Velvet Chollima / Kimsuky-adjacent

**Distinction avec Kimsuky** : les profils se recoupent et certains analystes les considèrent comme très proches ou partiellement fusionnés. Mandiant promeut APT43 comme cluster distinct depuis 2023.

**Spécialisation** : ciblage **académique, think tanks, médias, ONG** travaillant sur la DPRK. Collecte de renseignement sur les positions externes et les narratifs médiatiques.

**TTP signature** : similaire à Kimsuky (spear-phishing, credential harvesting, RAT légers). APT43 est également documenté pour utiliser des **crypto-vols ponctuels** comme source de financement opérationnel — ce qui en fait un croisement entre les missions d’espionnage (Kimsuky) et financières (APT38).

#### 11.7 Andariel / Onyx Sleet

**Spécialisation** : mix ransomware / cyber-espionnage. Moins connu que Lazarus ou APT38, mais significatif.

**Particularité** : Andariel a déployé des opérations de **ransomware ciblé** dans le passé (notamment contre des institutions de santé américaines), en plus de ses missions d’espionnage. Cette mixité rend son classement difficile.

**Cibles** : secteur de la santé (ciblage ransomware Maui), défense sud-coréenne, ATM et banques (braquages divers).

#### 11.8 Les opérateurs IT DPRK : phénomène unique

Un phénomène entièrement distinct des APT traditionnelles mérite une section dédiée : les **opérateurs IT DPRK**.

**Modus operandi** : des **milliers de ressortissants nord-coréens**, envoyés à l’étranger par le régime, travaillent sous **de fausses identités** comme développeurs freelance ou salariés à distance dans des entreprises occidentales. Ils génèrent un revenu en dollars qui est en grande partie reversé au régime.

**Revenu estimé** : le gouvernement américain estime à **300 millions de dollars par an et plus** les revenus générés par ce programme. L’ordre de grandeur, tout comme les vols crypto, est macroéconomique pour la DPRK.

**Techniques d’infiltration** :

- **Fausses identités** : achat de documents d’identité volés (américains, sud-coréens, autres), construction de profils LinkedIn complets avec CV, recommandations, photos (parfois générées par IA ou volées).
- **VPN et proxies** : connexions via IP occidentales (US, Europe) pour masquer l’origine coréenne.
- **Intermédiaires (facilitators)** : complices locaux qui prêtent leur identité, leur adresse, leurs comptes bancaires. Plusieurs facilitators ont été arrêtés aux US (notamment « l’opération laptop farm » — l’affaire Christina Chapman en 2024 qui hébergeait 90 ordinateurs connectés via VPN pour permettre à des travailleurs DPRK d’apparaître comme basés aux US).
- **Entretiens via vidéoconférence** : les opérateurs DPRK passent les entretiens en se faisant passer pour des asiatiques basés aux US, parfois avec modifications vidéo ou voice transformation.

**Détection** : indices comportementaux (réticence à allumer la caméra, horaires décalés, anomalies linguistiques, accès depuis IP incompatibles avec la localisation déclarée), vérification approfondie d’identité, background checks renforcés. Le FBI a émis des advisories détaillés en 2023-2024 pour aider les employeurs à détecter ces infiltrations.

**Risques au-delà du financement** : une fois à l’intérieur d’une entreprise, un opérateur IT DPRK peut potentiellement introduire du code malveillant, exfiltrer de la propriété intellectuelle, ou préparer des accès pour d’autres opérations APT nord-coréennes. Plusieurs cas documentés de tentatives d’exfiltration.

#### 11.9 Formation, stationnement à l’étranger, OPSEC

La formation des opérateurs cyber DPRK combine formation militaire (discipline, hiérarchie, sécurité opérationnelle) et formation technique (informatique, langues étrangères, compréhension des plateformes occidentales). Les opérateurs les plus doués sont identifiés très tôt et formés dans des programmes d’élite.

**Stationnement à l’étranger** : comme mentionné (11.2), une grande partie des opérations cyber DPRK est conduite depuis l’étranger — Chine principalement, mais aussi Russie, Asie du Sud-Est. Les opérateurs vivent dans des communautés fermées sous surveillance, avec des contrôles stricts (familles restées en DPRK comme « assurance » contre la défection, rotation régulière des postes).

**OPSEC** : globalement moyenne. Les opérateurs DPRK sont formés à l’OPSEC mais l’ampleur du volume d’opérations et les pressions de résultats (le régime attend des revenus) produisent des erreurs régulières qui ont facilité plusieurs attributions. Parmi les artefacts récurrents : réutilisation d’infrastructure, overlaps de TTP entre opérations différentes, quelques cas d’opérateurs identifiés nominativement par les indictments DOJ.

-----

### Chapitre 12 — DPRK : campagnes de référence et financement du régime

Ce chapitre documente les campagnes nord-coréennes les plus emblématiques, en progressant chronologiquement et thématiquement. Le cas complet Lazarus/crypto est traité au Ch.30.

#### 12.1 Sony Pictures (2014) — cyber-intimidation

**Acteur** : Lazarus. **Paradigme** : cyber-intimidation politique via vol + publication + destruction.

**Contexte** : Sony Pictures produisait *The Interview*, une comédie satirique représentant un complot fictif pour assassiner Kim Jong-un. La DPRK a publiquement protesté contre le film.

**Attaque** : en novembre 2014, Lazarus compromet Sony Pictures, exfiltre des téraoctets de données (emails internes, scénarios, données personnelles de 47 000 employés, films non sortis), puis déploie un wiper (destruction massive de données). Les données exfiltrées sont progressivement publiées en ligne, créant un scandale pour Sony (emails embarrassants, données de célébrités).

**Message politique** : la diffusion de *The Interview* est annulée dans plusieurs cinémas sous la pression des menaces. Sony envisage initialement d’annuler la sortie complète avant de revenir en arrière.

**Attribution** : FBI, NSA, DHS attribuent publiquement à la DPRK en décembre 2014. Un des premiers cas d’attribution publique rapide d’une cyberattaque étatique.

**Leçons** : la DPRK est prête à conduire des opérations cyber coûteuses pour des motifs politiques/de réputation, pas seulement financiers. Le cyber comme arme de dissuasion culturelle est une spécificité.

#### 12.2 Bangladesh Bank (février 2016) — premier braquage SWIFT étatique

**Acteur** : APT38/BlueNoroff. **Paradigme** : cyber-braquage bancaire à grande échelle via le système interbancaire.

**Attaque** : APT38 compromet les systèmes de la banque centrale du Bangladesh et accède au terminal SWIFT. Le 4 février 2016, 35 ordres de virement frauduleux sont émis via SWIFT, totalisant **951 millions de dollars** destinés à des comptes aux Philippines et au Sri Lanka.

**Ce qui a été volé** : 81 millions de dollars ont transité vers les Philippines et y ont été blanchis (casinos).

**Ce qui a été bloqué** : les 870 millions restants ont été arrêtés. L’élément déclencheur de la détection : une **faute de frappe** dans l’un des ordres de virement (« Jupiter Street » écrit « Jupiter Steet », puis « fandation » au lieu de « foundation »). La banque Deutsche Bank, qui traitait les virements comme banque correspondante, a examiné manuellement l’ordre et détecté l’anomalie. Les autres ordres ont ensuite été annulés.

**Impact** : premier braquage bancaire majeur par un acteur étatique via le cyber. A mis en évidence les vulnérabilités des systèmes SWIFT et a déclenché un durcissement des contrôles SWIFT (SWIFT Customer Security Programme).

**Leçons** : les systèmes financiers interbancaires sont des cibles APT majeures. La détection peut dépendre de signaux humains (lecture manuelle) en plus des contrôles automatiques. Une seule faute de frappe a sauvé 870 millions de dollars.

#### 12.3 WannaCry (mai 2017)

**Acteur** : Lazarus. **Paradigme** : ransomware worm avec propagation mondiale.

**Mécanisme** : WannaCry combinait un ransomware et l’exploit **EternalBlue** (vulnérabilité SMB de la NSA leakée par Shadow Brokers en avril 2017). L’exploit permettait la propagation vermineuse de machine à machine sur les réseaux, infectant toutes les machines Windows non patchées.

**Impact mondial** (mai 2017) :

- **200 000+ systèmes infectés dans 150 pays** en 24-48 heures.
- **NHS britannique** partiellement paralysé, avec des hôpitaux qui ont dû reporter des opérations non urgentes et rediriger des patients.
- **Telefónica** (Espagne), **Renault-Nissan**, **FedEx**, **Deutsche Bahn** (panneaux d’affichage) sévèrement touchés.
- Dommages mondiaux estimés en milliards de dollars (sur des périmètres variables d’estimation).

**Particularité** : un chercheur britannique (**Marcus Hutchins**, pseudonyme MalwareTech) a découvert un **kill switch** dans le code — une requête vers un domaine spécifique non enregistré. En enregistrant le domaine, Hutchins a activé le kill switch, arrêtant la propagation pour la première vague. Les variants ultérieurs sans kill switch ont causé des dommages supplémentaires mais à moindre échelle.

**Paradoxe** : WannaCry a généré peu de revenus directs (~140 000 dollars en Bitcoin avant saisie). Le mécanisme de paiement/déchiffrement était mal conçu — les victimes qui payaient ne recevaient souvent pas la clé. Soit c’était une opération de test qui a échappé au contrôle, soit un wiper déguisé. L’interprétation privilégiée : opération Lazarus qui s’est partiellement mal déroulée mais a révélé la capacité à causer des dommages mondiaux massifs.

**Attribution** : décembre 2017 — attribution publique par les US, UK, Australie, Canada, Nouvelle-Zélande, Japon à la DPRK/Lazarus.

**Leçons** : la DPRK assume des dommages collatéraux mondiaux massifs. Les vulnérabilités leakées par les services d’État (EternalBlue) produisent des effets de second ordre catastrophiques une fois dans les mains d’acteurs prêts à les utiliser sans discrimination.

#### 12.4 Opération Dream Job — social engineering LinkedIn continu

**Acteur** : Lazarus. **Paradigme** : social engineering extrêmement ciblé via faux recruteurs.

**Modus operandi** : Lazarus opère en continu depuis au moins 2019 une opération de social engineering sur LinkedIn. Des faux profils de recruteurs (parfois usurpant des recruteurs réels d’entreprises légitimes) approchent des employés de cibles stratégiques — développeurs dans des entreprises tech, ingénieurs dans l’aérospatial et la défense, employés d’exchanges crypto — avec des propositions d’emploi attractives.

**Chaîne de compromission typique** :

1. Approche initiale sur LinkedIn avec une offre attractive.
1. Transition vers un canal de communication privé (WhatsApp, Telegram, Skype).
1. Envoi d’un « test technique » sous forme de projet à exécuter.
1. Le projet contient du malware qui s’exécute lors de la compilation ou de l’ouverture.
1. Foothold établi sur la machine professionnelle du développeur (souvent avec accès à des réseaux internes et des secrets développement de son employeur).

**Campagnes documentées** : opérations contre des employés d’aerospatial (dont une qui a touché plusieurs entreprises européennes documentées par ESET en 2023), contre des développeurs crypto (ciblage qui a permis plusieurs des grands vols crypto), contre des chercheurs en sécurité.

**Pourquoi ça marche** : l’approche est personnalisée, l’offre est attractive, le « test technique » est contextuel au rôle prétendu. Les développeurs, habitués à exécuter du code inconnu dans le cadre de leur travail, baissent leur garde.

**Défense** : sensibilisation, séparation stricte entre machine professionnelle et exécution de code non vérifié (sandboxes, machines dédiées), vérification par canaux alternatifs de l’identité des recruteurs.

#### 12.5 3CX supply chain (mars 2023)

**Acteur** : Lazarus (sous-groupe Labyrinth Chollima, chevauchement avec APT41 noté par certains analystes dans une phase intermédiaire). **Paradigme** : supply chain imbriquée — la compromission initiale de 3CX passait par une autre supply chain compromise.

**Synthèse** : **3CX** est un logiciel de communication VoIP utilisé par plus de 600 000 organisations dans le monde. En mars 2023, il est découvert que l’application desktop 3CX distribuée via les canaux officiels a été **trojanisée** — les binaires signés contiennent une backdoor.

**Mécanisme de la compromission initiale** : l’enquête post-incident a révélé que 3CX lui-même a été compromis via **X_Trader**, un logiciel de trading financier de Trading Technologies, lui-même compromis précédemment par Lazarus. Un employé de 3CX avait installé X_Trader sur sa machine professionnelle ; l’infection de cette machine a donné à Lazarus un accès au réseau 3CX, puis au pipeline de build de leur produit desktop.

**Cascade** : X_Trader compromis → employé 3CX infecté → environnement build 3CX compromis → logiciel 3CX trojanisé → clients 3CX compromis (600 000+ potentiels, avec ciblage sélectif en phase 2). **Le supply chain d’un supply chain** — un niveau d’imbrication nouveau dans les opérations supply chain documentées.

**Impact** : ciblage en phase 2 de clients 3CX spécifiques (entreprises crypto, organisations d’intérêt). Les victimes confirmées publiquement ont été limitées par rapport au pool de 600 000 clients potentiels, confirmant un ciblage sélectif.

**Leçons** : les supply chains peuvent être compromises en cascade — le vecteur peut être éloigné de plusieurs « couches » de la cible finale. La confiance dans un logiciel signé par un éditeur ne suffit plus ; le monitoring comportemental des processus, même légitimes, devient essentiel.

#### 12.6 JumpCloud breach (juin 2023) — ciblage crypto via MSP

**Acteur** : Lazarus/Labyrinth Chollima. **Paradigme** : compromission d’un fournisseur de gestion d’identité pour atteindre ses clients crypto.

**Synthèse** : **JumpCloud** est un fournisseur de gestion d’identité SaaS (directory service, SSO, MDM). Lazarus compromet JumpCloud en juin 2023 et abuse des accès pour cibler spécifiquement des **clients JumpCloud dans l’écosystème crypto** — exchanges et sociétés de services crypto. Environ 5 clients de JumpCloud (sur des milliers) ont été touchés — ciblage extrêmement sélectif.

**Significance** : illustration des pivots supply chain ciblés dans l’écosystème crypto. Lazarus a identifié que JumpCloud servait des clients crypto intéressants, et a exploité cette position.

#### 12.7 Vols crypto massifs — chronologie

La liste des grands vols crypto attribués à Lazarus/BlueNoroff constitue une chronologie à elle seule. Ordre chronologique, non exhaustif.

- **DragonEx** (mars 2019) : ~7 M$.
- **Upbit** (novembre 2019) : 342 000 ETH (~49 M$ à l’époque, ~1 Mrd$ aujourd’hui).
- **KuCoin** (septembre 2020) : 281 M$.
- **Cream Finance** (septembre 2021) : 29 M$.
- **Badger DAO** (décembre 2021) : 120 M$.
- **Axie Infinity Ronin Network** (mars 2022) : **624 M$** — pivot : phishing LinkedIn contre un employé de Sky Mavis (studio derrière Axie). L’un des plus grands vols crypto à date.
- **Harmony Bridge** (juin 2022) : 100 M$.
- **DeBridge Finance** (août 2022) : tentative échouée.
- **Atomic Wallet** (juin 2023) : 100 M$ (certains contestent l’attribution).
- **Alphapo** (juillet 2023) : 60 M$.
- **CoinsPaid** (juillet 2023) : 37 M$.
- **Stake.com** (septembre 2023) : 41 M$.
- **CoinEx** (septembre 2023) : 54 M$.
- **HTX/Heco Bridge** (novembre 2023) : ~100 M$.
- **DMM Bitcoin** (mai 2024) : 305 M$.
- **WazirX** (juillet 2024) : 235 M$.
- **Radiant Capital** (octobre 2024) : 50 M$.
- **Bybit** (février 2025) : **~1,5 milliard de dollars** — **le plus gros vol crypto de l’histoire** à date de publication. Attribution FBI à Lazarus confirmée dans les semaines suivantes. Le cas Bybit est traité en détail au Ch.30.

**Cumul** : entre 3 et 6 milliards de dollars sur la période 2017-2025, avec une accélération nette post-2022.

#### 12.8 Le pipeline de blanchiment

Une fois les crypto-actifs volés, la DPRK doit les **convertir en devises utilisables** — un processus complexe qui est devenu un sujet d’investigation à part entière.

**Étape 1 — Obfuscation on-chain** :

- **Mixers / tumblers** : **Tornado Cash** (Ethereum, sanctionné par l’OFAC en août 2022 — première sanction d’un smart contract dans l’histoire), **Wasabi Wallet** (Bitcoin), **Samourai Wallet** (Bitcoin, fermé par les autorités en avril 2024).
- **Bridges cross-chain** : transfert entre blockchains (Ethereum → BNB Chain → TRON) pour complexifier le suivi.
- **Privacy coins** : conversion vers Monero (très difficile à tracer).
- **DeFi non-KYC** : swaps via des protocoles décentralisés qui n’exigent pas d’identification.

**Étape 2 — Conversion en stablecoins** : conversion en **USDT** (Tether), principalement sur la blockchain **TRON** (frais faibles, confirmations rapides, volume élevé qui facilite le camouflage). L’USDT sur TRON est devenu le canal dominant pour les flux illicites crypto en général.

**Étape 3 — Cashout** : conversion finale en devises fiat (dollars, euros, yuan). Plusieurs canaux :

- **Exchanges à KYC faible** : certains petits exchanges en Asie, en Russie, dans le Golfe ont historiquement eu des pratiques KYC laxistes. Ces exchanges subissent une pression réglementaire croissante mais certains restent utilisés.
- **OTC desks** (Over-the-Counter) : desks de trading hors-marché, souvent en Chine ou en Russie, qui convertissent les crypto en fiat pour des commissions élevées en échange d’un KYC minimal.
- **Mules** : réseaux de particuliers recrutés (souvent sans connaissance complète de la source des fonds) pour recevoir et transférer les fonds.

**Étape 4 — Rapatriement vers la DPRK** : une fois en fiat, les fonds transitent par des circuits opaques (sociétés écrans chinoises, banques complaisantes) vers le régime. Les mécanismes exacts restent largement classifiés, mais plusieurs investigations ont documenté des réseaux de facilitators dans plusieurs pays.

**Contre-mesures** :

- **Sanctions OFAC ciblées** : sanction de Tornado Cash (2022), sanction d’adresses crypto spécifiques, sanction d’OTC desks impliqués, sanction de ressortissants (incluant des facilitators chinois et russes).
- **Coopération exchanges** : les exchanges majeurs (Binance, Coinbase, Kraken) ont renforcé leur KYC, gelent les fonds sur signalement, collaborent avec le FBI. Binance a gelé plus de 4 milliards de dollars liés à des activités illicites entre 2022 et 2024.
- **Intelligence blockchain** : Chainalysis, TRM Labs, Elliptic fournissent aux autorités des capacités de suivi on-chain. Les attaquants DPRK adaptent leurs techniques en continu.

La **guerre du blanchiment** est un jeu du chat et de la souris permanent. La DPRK est devenue très sophistiquée, les défenseurs aussi — mais l’asymétrie (les attaquants n’ont qu’à trouver une route de blanchiment qui fonctionne, les défenseurs doivent fermer toutes les routes) joue contre les défenseurs.

#### 12.9 Impact géopolitique : cyber comme arme de prolifération nucléaire

La conséquence la plus grave des cyberopérations DPRK est leur **financement direct du programme nucléaire et balistique nord-coréen**. Les estimations ONU et US convergent : une part significative du financement du programme d’armement depuis 2016-2017 vient du cybervol.

**Implication stratégique** : les cyberopérations nord-coréennes ne sont pas un « problème cyber » — elles sont un **problème de sécurité internationale** lié directement à la non-prolifération nucléaire. Chaque dollar volé par Lazarus contribue potentiellement au développement d’armes nucléaires et de vecteurs balistiques.

**Conséquence pour la réponse internationale** : le cadre de sanctions et de contre-mesures s’est durci significativement depuis 2022. Les indictments DOJ contre des opérateurs DPRK et des facilitators, les sanctions OFAC sur des adresses et des entités, les opérations de saisies d’actifs (le DOJ a saisi pour plusieurs centaines de millions de dollars de crypto liés à des vols Lazarus entre 2022 et 2025) construisent une pression croissante.

**Leçon analytique** : quand on regarde une opération DPRK, on regarde un maillon dans une chaîne de financement d’armes nucléaires. Cette perspective change la nature de la menace et la proportionnalité des réponses.

-----

### Chapitre 13 — Iran : contexte, doctrine et groupes APT

#### 13.1 Priorités iraniennes et doctrine cyber

Les cyberopérations iraniennes s’inscrivent dans une configuration stratégique définie par plusieurs axes.

**Rivalité régionale** : tensions permanentes avec Israël (rivalité existentielle), Arabie saoudite et monarchies du Golfe (rivalité sunnite/chiite + géopolitique). Le cyber est un levier asymétrique pour un pays qui n’égale pas les capacités militaires de ses rivaux.

**Surveillance interne et diaspora** : répression politique contre la dissidence interne et surveillance des opposants à l’étranger (notamment post-Mahsa Amini 2022 et la vague de protestations « Femme Vie Liberté »).

**Sabotage ponctuel** : l’Iran est l’un des rares États à utiliser occasionnellement le **cyber destructif ouvert** (wipers), en réponse à des événements perçus comme des agressions (Stuxnet 2010 a catalysé cette trajectoire).

**Opérations d’influence** : promotion du récit iranien dans les conflits régionaux (Yémen, Liban, Syrie, Irak), influence sur les communautés chiites internationales.

**Contournement de sanctions** : l’Iran subit des sanctions sévères depuis 1979 (renforcées à plusieurs reprises). Le cyber peut servir à contourner certaines sanctions (vol financier, exfiltration de technologies).

**Doctrine** : le cyber iranien est un **levier asymétrique**. Moins sophistiqué que les acteurs de pointe (US, Israël, Russie, Chine), il compense par une grande activité, une acceptation du destructif, et une capacité à causer des dommages à des cibles plus puissantes.

#### 13.2 Structure : MOIS vs IRGC

L’appareil cyber iranien est structuré autour de deux pôles institutionnels distincts qui ont des cultures et des missions différentes.

**MOIS / VAJA** (Ministry of Intelligence and Security — وزارت اطلاعات) est le renseignement civil. Institution relativement classique (comparable à un ministère de l’intérieur étendu), conduit l’espionnage extérieur et le contre-espionnage intérieur. Les groupes APT associés au MOIS tendent à être plus orientés **espionnage classique** (collecte de renseignement, ciblage diplomatique).

**IRGC / Sepah** (Islamic Revolutionary Guard Corps — سپاه پاسداران انقلاب اسلامی) est le corps des Gardiens de la Révolution. Force militaire parallèle à l’armée régulière, avec des missions idéologiques et révolutionnaires. Conduit les opérations à l’étranger (Quds Force), gère une partie de l’économie iranienne, et a des branches cyber importantes. Les groupes APT associés à l’IRGC tendent à être plus **agressifs**, **idéologiques**, avec une forte composante de surveillance des opposants et des personnalités cibles.

La distinction MOIS/IRGC est importante pour l’analyse : une opération IRGC peut refléter une initiative révolutionnaire/militaire (ciblage d’un dissident, représailles), une opération MOIS reflète plus probablement un besoin de renseignement classique.

**L’IRGC a une branche cyber structurée** : IRGC Intelligence Organization (IRGC-IO), qui supervise APT42 notamment. L’IRGC a également des capacités cyber dans d’autres structures (IRGC Electronic Warfare and Cyber Defense Command).

#### 13.3 APT33 / Peach Sandstorm (IRGC)

**Mission** : espionnage industriel sur l’énergie, l’aérospatial, la pétrochimie. Cibles privilégiées : entreprises énergétiques du Golfe, sous-traitants aérospatiaux américains et européens, industries pétrochimiques saoudiennes (en cohérence avec la rivalité régionale).

**TTP signature** :

- **Password spraying massif** : APT33 est l’un des acteurs les plus connus pour le password spraying à grande échelle sur Azure AD/M365. Volumes gigantesques, faible taux de succès par tentative mais volume global efficace.
- **Malware custom** : backdoors comme **DropShot** (dropper), **StoneDrill** (wiper apparenté à Shamoon), **TurnedUp** (backdoor).
- **Spear-phishing** sur employés cibles.

**Campagnes** :

- Ciblage de l’industrie aérospatiale US (Boeing, sous-traitants) — documenté par FireEye en 2017.
- Ciblage énergie Golfe (Saudi Aramco, autres) — continu.
- Campagnes 2023-2024 documentées par Microsoft (Peach Sandstorm).

**Lien suspecté avec Shamoon** (Ch.14) : certains analystes ont établi des liens entre APT33 et les opérations Shamoon — ce qui placerait APT33 au croisement de l’espionnage et du destructif. Attribution pas pleinement consolidée.

#### 13.4 APT34 / OilRig / Hazel Sandstorm (MOIS)

**Mission** : espionnage régional au service du MOIS. Cibles : gouvernements du Moyen-Orient (Golfe, Liban, Israël), finance régionale, énergie, télécommunications.

**TTP signature** :

- **DNS tunneling** : APT34 a historiquement été l’un des groupes qui ont le plus massivement utilisé le DNS tunneling comme canal C2.
- **Webshells** : déploiement massif sur serveurs web compromis.
- **Credential harvesting** : fausses pages de login, spearphishing avec emails contextualisés.
- **Malware** : **QUADAGENT**, **OopsIE**, **Helminth**, **ISMAgent**.

**Leak 2019** : en mars-avril 2019, un leak anonyme sur Telegram (canal « Lab Dookhtegan » — « labo cousu ») a publié des **outils APT34, des données de victimes, et des noms d’opérateurs**. Le leak a exposé l’infrastructure du groupe et plusieurs de ses techniques. L’origine du leak reste débattue (dissident interne, opération Mossad, opération de services tiers).

**Détournement par Turla** : comme mentionné au Ch.6, Turla a été documenté pour avoir utilisé l’infrastructure APT34 pour ses propres opérations — démonstration de l’instabilité relative de l’OPSEC APT34.

#### 13.5 APT35 / Charming Kitten / Mint Sandstorm (IRGC)

**Mission** : **social engineering ultra-ciblé**. Cibles : chercheurs spécialisés sur l’Iran et le Moyen-Orient, dissidents politiques iraniens à l’étranger, journalistes, universitaires, cadres d’ONG, parfois femmes politiques (ciblages personnels de campagnes présidentielles US documentés).

**TTP signature — le social engineering d’APT35 est considéré comme le plus sophistiqué au monde dans sa catégorie** :

- **Faux profils LinkedIn** complets de « collègues » ou « recruteurs » avec des mois d’activité pour construire la crédibilité.
- **Impersonation de journalistes** : création de faux profils imitant des journalistes réels de médias respectés, pour approcher des cibles (« je voudrais vous interviewer pour mon article »).
- **Impersonation d’universitaires** : faux chercheurs invitant la cible à une conférence, un panel, ou une publication.
- **Malware léger** : backdoors minimales, souvent déployés via documents Office après établissement de confiance.
- **Phishing OAuth** : fausses applications OAuth imitant Google, Microsoft pour obtenir des accès persistants.

**Particularité** : APT35 investit massivement dans la **construction relationnelle** avant l’attaque. Certaines campagnes impliquent des **mois de conversation légitime** avec la cible avant le moindre élément malveillant. Cette patience et cette sophistication psychologique distinguent APT35.

**Campagnes documentées** :

- **Ciblage de journalistes et universitaires spécialisés sur l’Iran** : continu depuis 2015+.
- **Ciblage de campagnes présidentielles US 2020** : tentatives documentées de ciblage de la campagne Trump.
- **Opérations post-Mahsa Amini (2022-2023)** : ciblage intensif de dissidents à l’étranger, de journalistes couvrant les protestations.

#### 13.6 APT42 / Calanque (IRGC-IO)

**Mission** : surveillance ciblée au service de l’IRGC Intelligence Organization. Cibles : opposants politiques iraniens, membres de la diaspora iranienne, personnalités considérées comme menaces par l’IRGC.

**TTP signature** : similaire à APT35 (social engineering, credential harvesting) avec une orientation plus spécifiquement sécuritaire. Surveillance mobile (Android), capture de communications.

**Distinction avec APT35** : les frontières sont parfois floues. Certains analystes considèrent APT42 comme un sous-groupe d’APT35. Microsoft les distingue comme Calanque (APT42) vs Mint Sandstorm (APT35).

#### 13.7 MuddyWater / Mango Sandstorm (MOIS)

**Mission** : ciblage régional et international — gouvernements, télécoms, énergie. MuddyWater est l’un des groupes iraniens les plus actifs en volume.

**TTP signature** :

- **PowerShell obfusqué massivement** : MuddyWater a fait du PowerShell obfusqué sa marque de fabrique — scripts lourdement encodés, plusieurs couches d’évasion.
- **Outils open source** : utilisation massive d’outils accessibles publiquement (Koadic, Metasploit, PSEmpire) — moins de malware custom que d’autres groupes, plus d’adaptation d’outils existants.
- **Spear-phishing** avec documents Office contenant des macros.

**Cibles** : Moyen-Orient, Asie centrale, Asie du Sud, Europe dans une moindre mesure.

#### 13.8 Scarred Manticore (MOIS, Check Point 2023)

**Attribution** : MOIS, identifié publiquement par Check Point en 2023.

**Mission** : espionnage gouvernemental de haut niveau au Moyen-Orient.

**TTP signature** : outillage **plus sophistiqué** que MuddyWater ou OilRig — rootkits custom, persistence avancée, OPSEC élevée. Scarred Manticore représente potentiellement une montée en gamme du MOIS cyber.

**Campagne récente** : compromission de longue durée (18+ mois) d’organisations gouvernementales au Moyen-Orient.

#### 13.9 Agrius — wipers sous fausse bannière hacktiviste

**Attribution** : acteur lié à l’Iran, probablement IRGC.

**Particularité** : Agrius déploie des **wipers** (**Apostle**, **DEADWOOD**, **Moneybird**) généralement **masqués en ransomware**. Les victimes reçoivent une demande de rançon, mais il n’y a pas de mécanisme de déchiffrement réel — c’est un destructif pur. Des **fausses bannières hacktivistes** sont souvent utilisées (« Black Shadow », « Moses Staff ») pour brouiller l’attribution publique et créer un narratif de « hacktivisme antisioniste ».

**Cibles** : Israël principalement, avec quelques extensions régionales.

**Implication** : Agrius illustre une caractéristique de l’écosystème iranien — l’acceptation des opérations destructives et l’utilisation de fausses bannières pour maintenir un déni plausible, tout en signalant aux audiences cibles (en Iran, dans l’« axe de la résistance ») la capacité de frapper.

-----

### Chapitre 14 — Iran : campagnes de référence

Ce chapitre présente les campagnes iraniennes emblématiques, organisées chronologiquement et thématiquement.

#### 14.1 Stuxnet (2010) — le catalyseur

**Acteurs** : co-attribution **États-Unis et Israël** (publiquement documentée par plusieurs sources journalistiques dont le livre *Confront and Conceal* de David Sanger, 2012). **Paradigme** : première arme cyber OT, catalyseur des capacités cyber iraniennes.

**Cible** : le **programme d’enrichissement d’uranium iranien**, spécifiquement les centrifugeuses IR-1 à Natanz.

**Mécanisme** : Stuxnet est un malware d’une complexité sans précédent à son époque. Il combinait :

- **Quatre vulnérabilités 0-day Windows** (usage exceptionnel — un seul 0-day suffit généralement à compromettre une cible).
- **Ciblage extrêmement précis** : Stuxnet ne s’activait que sur des systèmes très spécifiques — machines Windows configurées avec WinCC/STEP7 de Siemens, contrôlant des automates S7-315 spécifiques, eux-mêmes contrôlant des centrifugeuses tournant à certaines vitesses.
- **Manipulation physique** : une fois sur le système de contrôle, Stuxnet modifiait les commandes envoyées aux centrifugeuses pour provoquer leur destruction (variations de vitesse anormales causant des contraintes mécaniques), **tout en affichant des valeurs normales aux opérateurs**. Cette double manipulation (destruction réelle + masquage) est la signature du malware.

**Impact** : environ **1 000 centrifugeuses détruites**, programme iranien retardé de 2-3 ans selon les estimations. Stuxnet a démontré que le cyber pouvait causer des dommages physiques significatifs à un programme militaro-industriel majeur.

**Propagation non intentionnelle** : Stuxnet s’est propagé au-delà des systèmes ciblés (machines Windows génériques, réseaux industriels non ciblés) via USB, ce qui a conduit à sa découverte en 2010 par des chercheurs en sécurité biélorusses puis internationaux.

**Catalyseur iranien** : Stuxnet a eu un **effet boomerang** majeur. L’Iran, conscient de la capacité cyber offensive déployée contre lui, a investi massivement dans son propre programme cyber offensif. Shamoon, développé environ 2 ans après Stuxnet, est la réponse iranienne — un wiper déployé contre Saudi Aramco (allié américain régional) en 2012. L’Iran est depuis devenu un acteur cyber significatif, étape structurée par Stuxnet.

**Autres traitements** : Stuxnet est abordé au Ch.18 (Israël), au Ch.21 (OT/ICS), et au Ch.25 (prolifération cyber — le code Stuxnet a fuité et a été étudié par tous les acteurs étatiques).

#### 14.2 Shamoon v1/v2/v3 (2012-2018)

**Acteur** : attribué à l’Iran, avec liens APT33 pour certaines itérations. **Paradigme** : wiper destructif à grande échelle comme représailles stratégiques.

**Shamoon v1 (août 2012)** : déployé contre **Saudi Aramco**, compagnie pétrolière nationale saoudienne. Le wiper a effacé les disques durs de **30 000 postes de travail** (soit environ 75% du parc de la compagnie). Les systèmes de production pétrolière n’ont pas été touchés, mais les opérations administratives ont été paralysées pendant des semaines. Parallèlement, un wiper similaire a frappé RasGas (Qatar) avec un impact plus limité.

**Message politique** : Shamoon v1 a été interprété comme une **représailles iranienne** pour Stuxnet, dirigée contre un allié majeur des États-Unis dans la région. Le message : « si vous nous attaquez, nous pouvons frapper votre industrie pétrolière ».

**Shamoon v2 (novembre 2016 - janvier 2017)** : réapparition du wiper contre des cibles saoudiennes, dans un contexte de tensions régionales renouvelées.

**Shamoon v3 (décembre 2018)** : nouvelle version, ciblage Saipem (entreprise pétrolière italienne) et autres.

**Analyse** : Shamoon est devenu un outil récurrent iranien signalant les moments de tensions régionales. Son déploiement est souvent associé à des événements politiques (sommet de l’OPEP, sanctions, incidents régionaux).

#### 14.3 Campagne contre l’Albanie (juillet 2022)

**Acteur** : Iran (MOIS, attribution publique par les États-Unis en septembre 2022 via sanctions OFAC et par l’Albanie). **Paradigme** : wiper + ransomware déployés pour représailles politiques.

**Contexte** : l’Albanie hébergeait un important camp de l’organisation d’opposition iranienne **MEK** (Mujahideen-e-Khalq — Organisation des Moudjahidin du peuple), à la suite d’un accord avec les États-Unis dans les années 2010 pour leur accueil depuis l’Irak. L’Iran considère le MEK comme un groupe terroriste et a exigé son expulsion.

**Attaque (juillet 2022)** : wipers et ransomware déployés contre les **systèmes gouvernementaux albanais** — services de police, administration, parlement. Disruption significative des services publics. L’attaque a coïncidé avec un congrès prévu du MEK.

**Réponse albanaise (septembre 2022)** : l’Albanie a **rompu les relations diplomatiques** avec l’Iran et expulsé le personnel diplomatique iranien. **Premier cas d’une rupture diplomatique pour cause de cyberattaque** dans l’histoire.

**Attribution et sanctions** : les États-Unis ont attribué publiquement à l’Iran, imposé des sanctions OFAC contre le MOIS et des opérateurs, et soutenu l’Albanie techniquement (FBI a envoyé des équipes).

**Signification** : l’attaque albanaise illustre la volonté iranienne de conduire des opérations destructives à l’étranger pour des motifs politiques, et la capacité occidentale à y répondre par l’attribution et le soutien diplomatique. C’est aussi un précédent juridique intéressant (rupture diplomatique = signal que le cyber peut déclencher des réponses diplomatiques majeures).

#### 14.4 Cyberattaques contre Israël 2023-2025

Le conflit Israël-Hamas déclenché en octobre 2023 a amplifié les cyberopérations iraniennes contre Israël et ses intérêts.

**Campagnes documentées** :

- **Opérations Agrius** : wipers continus contre cibles israéliennes, sous fausses bannières hacktivistes (« Cyber Av3ngers » notamment).
- **Ciblage d’infrastructures civiles** : systèmes de santé israéliens, systèmes municipaux, parfois systèmes d’alerte publique.
- **Opérations contre les sous-traitants de défense israéliens et américains** : espionnage classique.
- **Opérations d’influence** : amplification de narratifs pro-palestiniens sur les réseaux sociaux, deepfakes ponctuels, manipulation de contenus.

**Ciblage US post-octobre 2023** : les opérations iraniennes contre des cibles américaines ont également augmenté, notamment contre des infrastructures eau (« Cyber Av3ngers » a revendiqué plusieurs attaques contre des systèmes d’eau municipaux US via exploitation de PLC Unitronics exposés — démonstration plus symbolique qu’impactante mais message clair).

#### 14.5 Surveillance des dissidents et diaspora

Les cyberopérations iraniennes contre les dissidents et la diaspora sont un volet continu et sous-documenté publiquement. Quelques éléments publics :

- **Campagnes APT35/APT42** continues contre les dissidents iraniens à l’étranger.
- Post-Mahsa Amini (septembre 2022, mort en détention de la « police des mœurs » iranienne, déclenchement des protestations « Femme Vie Liberté ») : intensification massive du ciblage des militants féministes iraniens à l’étranger, des journalistes couvrant les protestations, des relais de la diaspora.
- **Harcèlement** : au-delà de la surveillance, certaines cibles reçoivent des harcèlements directs (deepfakes humiliants, campagnes de dénigrement, pressions via les familles en Iran).
- **Opérations physiques** : le cyber est parfois coordonné avec des tentatives d’enlèvement ou d’intimidation physique (plusieurs cas documentés aux US et en Europe).

#### 14.6 Analyse : la spécificité iranienne

La synthèse des campagnes iraniennes révèle un profil distinct dans l’écosystème APT.

**Le destructif ponctuel comme substitut/complément conventionnel** : l’Iran est l’un des rares États à utiliser régulièrement le cyber destructif ouvertement. Shamoon et Agrius sont des wipers déployés à des moments de tensions régionales — le cyber remplit un rôle que l’action conventionnelle (frappes militaires) remplirait dans d’autres configurations. Cette caractéristique distingue l’Iran des autres acteurs (la Russie fait du destructif aussi mais majoritairement en contexte de guerre déclarée avec l’Ukraine ; la Chine presque pas ; les US/Israël très rarement et ciblé).

**Social engineering extrêmement sophistiqué** : APT35 représente probablement l’état de l’art mondial en social engineering ciblé. Cette compétence compense une sophistication technique de malware moindre que celle des APT russes ou chinoises.

**Utilisation de fausses bannières hacktivistes** : pratique récurrente (Cyber Av3ngers, Moses Staff, autres). Permet à l’Iran de signaler des capacités à son audience domestique et régionale tout en maintenant un déni plausible.

**Montée en sophistication** : Scarred Manticore (2023) suggère que le MOIS investit dans des capacités plus sophistiquées. La trajectoire est à la hausse, même si l’Iran reste un cran en-dessous des acteurs de pointe.

**Pour l’analyste** : face à une intrusion attribuée à l’Iran, les questions discriminantes sont : MOIS ou IRGC ? Opération de renseignement classique ou opération destructive/représailles ? Lien avec un événement politique/régional récent ? Utilisation d’une fausse bannière hacktiviste ?

-----

### Chapitre 15 — Autres acteurs étatiques, mercenaires cyber et zones grises

Ce chapitre couvre les acteurs étatiques non traités en Parties II-III-IV (acteurs régionaux avec capacités cyber croissantes), les mercenaires cyber commerciaux (NSO, Intellexa, Candiru), et les zones grises crime-État.

#### 15.1 Acteurs régionaux documentés

**Vietnam — OceanLotus / APT32** (Cobalt Kitty, BISMUTH) : service de renseignement vietnamien (probablement Ministry of Public Security). Mission : espionnage régional (ASEAN, Chine, Cambodge), dissidents vietnamiens et opposants politiques à l’étranger, entreprises étrangères opérant au Vietnam. TTP : sophistication croissante, ciblage macOS et mobile (distinctif pour un acteur régional), malware custom (SOUNDBITE, PHOREAL). Campagnes contre BMW et Hyundai documentées (2019). Ciblage notable des journalistes vietnamiens à l’étranger.

**Pakistan — SideCopy, Transparent Tribe** : services pakistanais. Mission : ciblage quasi exclusif de l’Inde — gouvernement, défense, télécoms. TTP : malware mobile (Crimson RAT, CapraRAT pour Android, CapraSpy pour iOS), sophistication modérée. Campagne continue depuis les années 2010.

**Inde — SideWinder, Patchwork (Dropping Elephant)** : probablement services indiens. Mission : ciblage du Pakistan, de la Chine, et de l’Asie du Sud-Est dans une moindre mesure. SideWinder est particulièrement actif avec des centaines de campagnes documentées. TTP : spear-phishing, malware custom relativement simple.

**Turquie — Sea Turtle / Teal Kurma** : services turcs probablement. Mission : ciblage régional Moyen-Orient/Europe du Sud. **TTP signature : détournement DNS** — Sea Turtle a documenté une technique de compromission de **registrars DNS** pour détourner les résolutions de domaines de ses cibles (Chypre, Grèce, Kurdistan). Technique inhabituelle et sophistiquée. Ciblage des dissidents kurdes.

**Amérique latine** — **Blind Eagle / APT-C-36** : acteur latino-américain (probablement colombien selon certaines analyses). Mission : ciblage régional (Colombie, Équateur, Pérou, Venezuela). Cibles : gouvernements, finance, entreprises. Sophistication modérée.

**Corée du Sud** : services sud-coréens ont des capacités cyber importantes mais très peu documentées publiquement (l’écosystème sud-coréen publie moins sur ses propres capacités offensives). Quelques mentions de ciblage de la DPRK, en contre-intelligence.

Ces acteurs régionaux se caractérisent généralement par une sophistication modérée, un ciblage géographique concentré, et une visibilité moindre que les grandes puissances cyber. Ils sont néanmoins actifs et peuvent créer des incidents significatifs dans leurs zones d’influence.

#### 15.2 Mercenaires cyber / PSO (Private Sector Offensive)

Les **PSO** (Private Sector Offensive) sont des entreprises privées qui développent et vendent des capacités cyber offensives à des États (et parfois à d’autres clients). Le marché est dominé par quelques acteurs majeurs.

**NSO Group** (Israël, fondé 2010) — **Pegasus**. Spyware mobile exploitant des **0-day iOS et Android**, permettant une compromission complète du terminal : accès aux messages (y compris messageries chiffrées type Signal et WhatsApp — lecture en post-déchiffrement sur le terminal lui-même), géolocalisation, microphone et caméra à distance, extraction de données.

NSO vend Pegasus exclusivement à des gouvernements (officiellement), avec un discours « lutte antiterroriste et criminalité grave ». La réalité documentée est beaucoup plus large : usage contre des **journalistes** (Jamal Khashoggi et ses proches avant l’assassinat, Cecilio Pineda au Mexique, des dizaines d’autres documentés par le **Pegasus Project** en 2021 — consortium de 17 médias internationaux coordonné par Forbidden Stories), **dissidents** (membres des familles de dissidents saoudiens, marocains, azerbaïdjanais), **chefs d’État et personnalités politiques** (Emmanuel Macron cité parmi les cibles potentielles, plusieurs dirigeants européens), **avocats des droits humains**, **militants**.

Implications : NSO a été ajouté à l’**Entity List** du Commerce US en novembre 2021. Apple et Meta ont porté plainte contre NSO. L’usage de Pegasus par le gouvernement polonais contre l’opposition (confirmé par Citizen Lab) a fait scandale. L’entreprise a subi des difficultés financières importantes et plusieurs changements de direction, mais reste opérationnelle.

**Intellexa** (consortium européen basé à Chypre/Grèce/Irlande/Macédoine du Nord) — **Predator**. Spyware concurrent de Pegasus, capacités similaires. Documenté par Citizen Lab comme ayant des victimes dans plusieurs pays, notamment des politiciens et journalistes (scandale retentissant en Grèce en 2022-2023, avec ciblage d’un député opposant et de journalistes — affaire **Predatorgate**). Sanctionné par les États-Unis en juillet 2023 et mars 2024.

**Candiru** (Israël, fondée 2014) — spyware ciblant les desktops (Windows principalement) via des 0-day navigateur. Documenté par Citizen Lab et Microsoft (qui a identifié la vulnérabilité CVE-2021-33771 exploitée par Candiru). Sanctionné par les États-Unis en novembre 2021 (Entity List).

**Autres acteurs** : Paragon Solutions (Israël), TrueDialog, et divers acteurs moins documentés. Le marché est en évolution — certains se professionnalisent, d’autres ferment sous la pression réglementaire.

**Pourquoi la CTI documente les mercenaires** : leurs outils apparaissent dans les campagnes d’espionnage étatique. Un analyste qui identifie un spyware Pegasus chez une victime sait que le commanditaire est probablement un **client étatique de NSO**, pas un cybercriminel autonome. La liste des clients NSO/Intellexa/Candiru est partiellement publique (via les révélations Citizen Lab, les enquêtes journalistiques, les sanctions) et inclut de nombreux régimes autoritaires ou illibéraux.

#### 15.3 Régulations émergentes sur les PSO

Le marché PSO fait l’objet d’efforts réglementaires croissants.

**Pall Mall Process** : initiative conjointe franco-britannique lancée en février 2024 à Londres. Objectif : établir un cadre international pour la régulation du marché des capacités cyber commerciales. Signataires : une quarantaine d’États, entreprises, et organisations de la société civile (dont les « Big Tech » et des ONG). Le processus est itératif — les discussions se poursuivent dans plusieurs rounds.

**Restrictions d’exportation** : plusieurs pays ont durci les règles d’exportation des technologies de surveillance cyber. L’**Arrangement de Wassenaar** (export control multilatéral) inclut les « intrusion software » depuis 2013. L’UE a un règlement dual-use qui encadre les exportations. Les États-Unis utilisent l’Entity List comme levier.

**Sanctions ciblées** : les Entity List américaines, les sanctions OFAC, et les sanctions UE ont visé NSO, Intellexa, Candiru, et plusieurs individus associés. Ces sanctions ont un effet réel sur la capacité opérationnelle de ces entreprises.

**EU ban on spyware for political surveillance** : des propositions européennes visent à interdire l’usage de spywares commerciaux contre les journalistes, opposants politiques, et défenseurs des droits humains. État législatif en évolution.

**Limitations** : malgré ces efforts, le marché reste actif. De nouveaux acteurs émergent pour remplacer ceux qui sont sanctionnés. La demande étatique (États autoritaires, certaines démocraties aussi) reste forte. L’efficacité des régulations dépendra de leur universalité — les États qui refusent de coopérer peuvent continuer à s’approvisionner.

#### 15.4 Zones grises crime-État

Les **zones grises crime-État** sont l’un des phénomènes les plus importants à comprendre dans le paysage cyber contemporain. Elles recouvrent plusieurs configurations.

**APT41 — la double casquette assumée** : déjà traité au Ch.9. Le cas illustre la tolérance étatique (probablement MSS) pour les activités cybercriminelles personnelles des opérateurs, tant que les priorités étatiques sont respectées.

**Ransomware russophone — la tolérance tacite** : déjà traité au Ch.5. Les groupes LockBit, Conti, BlackBasta, ALPHV, Black Suit, Play opèrent sous la tolérance tacite russe. Certains ont des liens documentés avec les services (Conti Leaks 2022 ont révélé des échanges évoquant le FSB). La frontière entre tolérance et connivence est variable selon les groupes.

**DPRK — la méthode criminelle, la finalité étatique** : déjà traité aux Ch.11-12. Lazarus vole des crypto-actifs par des méthodes cybercriminelles, mais la finalité et le commanditaire sont étatiques.

**Hacktivisme instrumentalisé** : déjà traité au Ch.5 (KillNet, NoName057(16), IT Army of Ukraine). Mouvements présentés comme indépendants mais avec un alignement opérationnel systématique sur les priorités d’un État.

**Initial Access Brokers (IAB) — la chaîne fragmentée** : les IAB sont des acteurs cybercriminels qui compromettent des organisations et **vendent l’accès** sur des forums dark web à d’autres acteurs (typiquement des opérateurs ransomware). L’écosystème IAB est massivement russophone. Un accès vendu peut être acheté par un opérateur ransomware classique (finalité criminelle) ou par un acteur étatique qui l’utilise pour un ciblage plus stratégique. La chaîne « IAB → acheteur → usage » brouille l’attribution de l’origine (la compromission initiale) par rapport à l’usage (l’action finale contre la victime).

**Implications pour l’analyse** : face à un incident :

- Ne pas assumer que l’opérateur visible (ransomware, hacktiviste) est l’acteur stratégique réel.
- Identifier si l’accès initial vient d’un IAB — ce qui ajoute une couche analytique.
- Évaluer si le ciblage est cohérent avec une motivation purement financière ou si des signaux étatiques sont présents (choix de cible stratégique, timing politique, absence de monétisation rigoureuse).
- Documenter les incertitudes — dans les zones grises, l’attribution définitive (étatique ou criminel) est souvent impossible sans accès au renseignement non-public.

Le Ch.25 approfondit l’écosystème cyber offensif mondial et ses évolutions.

-----

## PARTIE V — PUISSANCES CYBER OCCIDENTALES ET ALLIÉES

> **Ce que cette partie apprend.** Comprendre les doctrines cyber des puissances occidentales majeures (US, UK/Five Eyes, Israël, Ukraine en miroir), cartographier les agences qui les exécutent, connaître les opérations documentées publiquement, et saisir comment ces acteurs utilisent le droit et l’attribution publique comme instruments de dissuasion.
> 
> **Ce qu’elle ne couvre pas.** Les cadres juridiques détaillés (Annexe G), l’analyse comparée des doctrines comme grille d’analyse (Ch.25), les mercenaires cyber d’origine israélienne en tant qu’entreprises (Ch.15).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer defend forward américain, disruption britannique et préemption israélienne, situer une opération offensive alliée dans son cadre doctrinal, et comprendre pourquoi l’Ukraine est le laboratoire de référence de la cyberdéfense moderne.
> 
> **Une précaution méthodologique.** Cette partie n’est pas une symétrisation morale entre blocs. Les acteurs présentés ici ont des doctrines, des cadres juridiques, des contrôles démocratiques, et des pratiques de responsabilité publique qui diffèrent substantiellement de ceux de la Russie, de la Chine, de la DPRK ou de l’Iran. Les présenter au même titre (cartographie des acteurs étatiques cyber) est une exigence analytique ; le faire sans discernement doctrinal ni contextuel serait trompeur.

-----

### Chapitre 16 — États-Unis : doctrine, agences et cyber power

#### 16.1 Vue d’ensemble de l’appareil cyber américain

L’appareil cyber américain est le plus puissant et le plus structuré au monde. Sa caractéristique distinctive est la **séparation institutionnelle** entre plusieurs fonctions qui, dans d’autres pays, sont confondues : le renseignement (NSA, CIA) est séparé de l’action militaire offensive (USCYBERCOM), elle-même séparée du law enforcement (FBI), elle-même séparée de la protection des infrastructures civiles (CISA).

Cette séparation n’est pas parfaite — les fonctions se chevauchent (USCYBERCOM et la NSA partagent un même directeur, le « dual-hat » arrangement), et la coordination est permanente — mais elle structure les missions, les responsabilités, et les cadres juridiques. Elle contraste avec les modèles russe (GRU conduit simultanément espionnage et destruction), chinois (MSS et PLA avec fragmentation et contractors), et iranien (IRGC intègre action et renseignement).

Les quatre piliers de l’appareil cyber américain sont : **USCYBERCOM** (commandement militaire), **NSA** (renseignement SIGINT/cyber), **FBI** (law enforcement cyber), **CISA** (protection des infrastructures critiques). La CIA dispose également de capacités cyber intégrées à ses opérations clandestines, et d’autres agences (DIA, Treasury/OFAC, DOJ) interviennent dans leurs domaines respectifs.

#### 16.2 USCYBERCOM : le commandement militaire cyber

**US Cyber Command** (USCYBERCOM) est le combatant command unifié du Département de la Défense chargé des opérations cyber. Créé en 2009 comme sous-commandement de STRATCOM, élevé en combatant command unifié en 2018.

**Mission** : défendre les réseaux du Département de la Défense, soutenir les commandements militaires régionaux et fonctionnels par des opérations cyber, et conduire les opérations cyber militaires offensives autorisées.

**Structure** : USCYBERCOM comprend les **Cyber Mission Forces (CMF)**, environ **6 200 opérateurs** répartis en **133 équipes** :

- **Cyber National Mission Teams (CNMT)** : défendent le pays contre les cybermenaces majeures, coordonnent avec les agences civiles.
- **Cyber Combat Mission Teams (CCMT)** : soutiennent les commandements militaires régionaux dans leurs opérations (supporting CENTCOM, INDOPACOM, EUCOM, etc.).
- **Cyber Protection Teams (CPT)** : défendent les réseaux DoD spécifiques.
- **Cyber Support Teams (CST)** : soutien analytique et planning.

**Dual-hat arrangement** : le directeur de la NSA est simultanément commandant d’USCYBERCOM. Cet arrangement, critiqué périodiquement pour les risques de confusion de missions (renseignement vs action militaire), a été maintenu parce qu’il optimise l’usage des ressources (NSA fournit l’accès technique, USCYBERCOM fournit les autorités d’action).

#### 16.3 La NSA : renseignement SIGINT et capacités cyber offensives

La **National Security Agency** (NSA) est l’agence de renseignement d’origine électromagnétique des États-Unis. Elle collecte le SIGINT mondial et développe des capacités cyber offensives majeures.

**Tailored Access Operations (TAO)** — renommé en 2017 **Computer Network Operations** (CNO) puis **Computer Network Exploitation** — est la branche historique de la NSA pour les opérations cyber offensives. TAO développait et déployait des outils d’intrusion pour la collecte de renseignement. Les capacités TAO ont été partiellement révélées par les fuites **Shadow Brokers** (2016-2017), qui ont publié des outils internes dont **EternalBlue** (exploit SMB utilisé ensuite par WannaCry et NotPetya), **DoublePulsar**, **Fuzzbunch**, et d’autres. Ces fuites ont été l’un des événements les plus graves de l’histoire du renseignement américain — des outils offensifs étatiques passés dans le domaine public ont été exploités massivement par des acteurs criminels et étatiques.

**Threat Operations Center (NTOC)** : coordination défensive, détection de menaces, partage avec les alliés.

**Opérations documentées** :

- **Co-attribution Stuxnet** (avec Israël, 2010) : sabotage du programme nucléaire iranien. Attribution solide via le livre *Confront and Conceal* de David Sanger et investigations ultérieures.
- **Collecte SIGINT mondiale** : révélée par les fuites Snowden (2013) qui ont documenté des programmes comme PRISM, XKeyscore, la collecte massive de métadonnées téléphoniques.

La NSA est également l’une des agences qui publient le plus d’**advisories techniques** de haute qualité en coordination avec CISA et le FBI — une transformation majeure depuis les années 2010, où la NSA partageait peu publiquement ses analyses.

#### 16.4 La CIA et ses capacités cyber clandestines

La **Central Intelligence Agency** dispose de capacités cyber intégrées à ses opérations de renseignement humain et clandestines. Le **Center for Cyber Intelligence** (CCI) a été révélé partiellement par les fuites **Vault 7** (2017), où WikiLeaks a publié des documents internes de la CIA documentant des outils d’intrusion pour Windows, macOS, iOS, Android, systèmes IoT, et voitures connectées.

Contrairement à la NSA (collecte SIGINT massive) et USCYBERCOM (opérations militaires), la CIA cible des cas très spécifiques dans le cadre d’opérations clandestines plus larges. Son empreinte publique cyber est volontairement limitée — les capacités révélées par Vault 7 ont conduit à des enquêtes internes et à des arrestations (un ancien employé CIA a été condamné en 2022 pour les fuites).

#### 16.5 Le FBI : investigation, démantèlement, indictments

Le **Federal Bureau of Investigation** conduit les investigations cyber, les démantèlements d’infrastructure, et les poursuites judiciaires. Son **Cyber Division** coordonne avec les bureaux régionaux qui enquêtent sur les incidents.

Le FBI a acquis un rôle central dans la réponse aux APT via plusieurs fonctions :

- **Investigation des incidents majeurs** : compromission de victimes US, collecte de preuves, coordination avec les cibles.
- **Démantèlements d’infrastructure** : opérations judiciaires de saisie de serveurs, de domaines, de cryptomonnaies. Quelques cas emblématiques : **Emotet** (janvier 2021, coordination Europol), **Hive** (janvier 2023, infiltration et déchiffrement pour les victimes), **Qakbot** (août 2023, « Operation Duck Hunt »), **LockBit** (février 2024, « Operation Cronos » coordonnée NCA/FBI/Europol), **Volt Typhoon KV Botnet** (janvier 2024), **Flax Typhoon Raptor Train** (septembre 2024), **Snake/Turla Medusa** (mai 2023).
- **Indictments** : mise en accusation formelle d’opérateurs APT étrangers. Les indictments DOJ sont devenus un instrument diplomatique central. Exemples emblématiques : Unit 61398/PLA (2014, 5 officiers chinois), APT10/MSS Tianjin (2018), APT28/GRU (2018, 12 officiers), APT41 (2020, 5 ressortissants chinois), APT40/MSS Hainan (2021, 4 ressortissants), APT31/MSS Hubei (2024, 7 ressortissants, avec sanctions coordonnées).

L’effet des indictments est débattu. Les inculpés ne seront probablement jamais jugés (les pays sponsors ne les extradent pas). Mais l’effet de **naming and shaming** est réel — il réduit la marge de déni plausible, impose un coût diplomatique au sponsor, et fournit à la communauté CTI un socle documentaire sur les opérateurs.

#### 16.6 CISA : protection des infrastructures critiques

**Cybersecurity and Infrastructure Security Agency** (CISA), créée en 2018 au sein du Département de la Sécurité Intérieure (DHS), est l’agence civile de coordination de la cybersécurité aux États-Unis. Elle protège les infrastructures critiques, publie des advisories, coordonne avec le secteur privé et les gouvernements locaux, et conduit des exercices nationaux.

**Publications CISA** : les advisories CISA (souvent conjoints avec NSA, FBI, et alliés Five Eyes) sont devenus une référence mondiale. Les **Joint Cybersecurity Advisories (JCSA)** documentent les TTP d’acteurs étatiques avec un niveau de détail opérationnel exceptionnel. Exemples : advisories Volt Typhoon (2023, 2024), APT40 (2024), Salt Typhoon (2024-2025), et des dizaines d’autres.

**Known Exploited Vulnerabilities (KEV)** : CISA maintient une liste publique des vulnérabilités activement exploitées par les acteurs menaçants. La **Binding Operational Directive 22-01** impose aux agences fédérales US de patcher les vulnérabilités du KEV dans des délais stricts. Le KEV est utilisé mondialement comme référence de priorisation.

**Shields Up** : posture de vigilance renforcée annoncée par CISA post-invasion ukrainienne (février 2022), recommandations pratiques à toutes les organisations américaines.

**Secure by Design** : initiative CISA pour responsabiliser les éditeurs logiciels (designs sécurisés par défaut, transparence sur les vulnérabilités).

CISA est devenue sous son leadership post-2021 (Jen Easterly puis ses successeurs) l’une des agences cyber les plus visibles et les plus influentes mondialement — un modèle de coordination civile/militaire/privée que plusieurs pays européens cherchent à adapter.

#### 16.7 Defend Forward et Persistent Engagement

La **doctrine du defend forward / persistent engagement** est l’innovation doctrinale américaine majeure de la décennie 2010-2020. Formulée publiquement par le général Paul Nakasone (directeur NSA et commandant USCYBERCOM de 2018 à 2024) et codifiée dans la **Cyber Strategy du DoD** (2018), elle marque une rupture avec la posture défensive classique.

**Principe** : ne pas attendre l’attaque pour agir, mais **opérer en continu dans les réseaux adverses** pour dégrader leurs capacités, collecter du renseignement tactique, et démontrer une présence dissuasive.

**Concept de « contestation permanente »** : le cyberespace n’est pas un domaine de paix ponctuée d’incidents, mais un domaine de confrontation continue. USCYBERCOM opère quotidiennement dans les réseaux adverses, pas uniquement en réponse à une attaque identifiée.

**Différence avec les doctrines précédentes** : avant defend forward, la doctrine américaine était largement défensive — réagir après compromission, protéger les réseaux nationaux. Defend forward inverse la logique : l’initiative doit être américaine, pas adverse.

**Débats** : la doctrine est critiquée par certains analystes comme favorisant l’escalade (risque d’incidents non désirés), par d’autres comme insuffisamment agressive. Le fait qu’elle soit publique — une doctrine offensive ouvertement assumée — est lui-même une rupture notable avec la tradition de discrétion autour des capacités offensives.

#### 16.8 Hunt Forward : les opérations en territoire allié

Le concept de **Hunt Forward Operations (HFO)** est dérivé de defend forward. Il consiste à déployer des équipes USCYBERCOM **dans les réseaux de pays alliés** pour détecter des menaces que les alliés n’ont pas les moyens de détecter seuls.

**Principe** : l’équipe USCYBERCOM arrive chez l’allié à l’invitation de ce dernier, avec un cadre juridique et opérationnel négocié. Elle opère sur les réseaux de l’allié (sensor placement, chasse aux menaces, analyse), partage les résultats avec l’allié et rentre aux États-Unis avec l’expérience et les IoC collectés. Bénéfice croisé : l’allié gagne en sécurité, les États-Unis gagnent en connaissance des TTP adverses observées dans des environnements variés.

**Opérations documentées** :

- **Ukraine** : hunt forward teams américaines déployées dans les réseaux ukrainiens depuis 2018. Volume massif d’activité depuis 2022. Retour d’expérience direct sur les TTP russes (Sandworm, APT28, Gamaredon, Unit 29155). Pour les Ukrainiens : détection renforcée. Pour les Américains : connaissance de terrain des TTP russes qui alimente ensuite les défenses des autres alliés.
- **Europe de l’Est** : Estonie, Lettonie, Lituanie, Pologne, Roumanie, Monténégro.
- **Autres alliés** : déployments documentés également dans des pays non européens.

Le nombre total d’opérations dépasse 50 déploiements publiquement reconnus au moment des rapports annuels de USCYBERCOM.

#### 16.9 Opérations documentées majeures

**Stuxnet (co-attribution 2010)** : sabotage du programme nucléaire iranien à Natanz, en coopération avec Israël. Détaillé au Ch.14, Ch.18, Ch.21.

**Démantèlement d’Emotet (janvier 2021)** : opération coordonnée FBI/Europol/Eurojust qui a saisi l’infrastructure d’Emotet (l’un des plus grands botnets et loaders criminels du monde). Emotet s’est partiellement reconstitué en 2021-2022 mais n’a jamais retrouvé son niveau précédent.

**Démantèlement de Qakbot (août 2023)** : « Operation Duck Hunt », FBI et partenaires internationaux. Le FBI a exploité le protocole de contrôle de Qakbot pour désinstaller le malware des 700 000+ machines infectées — opération offensive law enforcement sur le modèle de Medusa/Snake.

**Opération Medusa / Snake (mai 2023)** : neutralisation de l’implant Snake (Turla) sur les machines infectées via un outil développé par le FBI, exploitant des fonctionnalités du malware lui-même. Détaillé au Ch.6.

**Démantèlement LockBit (février 2024)** : Operation Cronos, NCA britannique en lead avec FBI et Europol. Saisie de l’infrastructure, publication de contenus moqueurs sur le site .onion de LockBit (ironie retournée — les forces de l’ordre ont utilisé l’interface du groupe pour afficher des messages à leur encontre), arrestations, offre gratuite de déchiffreur.

**Démantèlement KV Botnet Volt Typhoon (janvier 2024)** : neutralisation du botnet de routeurs Cisco RV/NetGear compromis utilisé par Volt Typhoon comme infrastructure C2.

**Démantèlement Raptor Train Flax Typhoon (septembre 2024)** : neutralisation du botnet de 260 000+ dispositifs IoT compromis opéré par Flax Typhoon.

#### 16.10 Le droit et les sanctions comme instruments

Les États-Unis ont **instrumentalisé le droit** comme réponse aux cybermenaces étatiques d’une manière qu’aucun autre pays n’a égalée en ampleur.

**Indictments DOJ** (section 16.5) : mise en accusation formelle d’opérateurs APT étrangers, effet de naming and shaming.

**Sanctions OFAC** : le Département du Trésor peut désigner des personnes, entités, et adresses crypto comme « Specially Designated Nationals » (SDN), interdisant aux entités américaines tout commerce avec elles. La sanction de **Tornado Cash** (août 2022) a été un précédent majeur — première sanction d’un smart contract dans l’histoire. Les sanctions OFAC ont ciblé des opérateurs APT nommés, des contractors (Integrity Technology Group — chinois, sanctionné janvier 2025), des entités PSO (NSO, Candiru sanctionnés Entity List 2021 ; Intellexa sanctionnée 2023-2024), et des adresses crypto utilisées pour le blanchiment nord-coréen.

**Entity List du Commerce** : liste d’entités interdites d’accès aux technologies américaines. Usage étendu contre Huawei (2019), ZTE, plusieurs fournisseurs de surveillance chinois (Hikvision, Dahua), NSO, Candiru, Intellexa.

**Executive Orders** : **EO 14028** (mai 2021, Biden — « Improving the Nation’s Cybersecurity ») a restructuré la réponse fédérale au cyber suite à SolarWinds. **EO sur les spywares commerciaux** (mars 2023) restreint l’acquisition de spywares commerciaux par le gouvernement fédéral américain.

#### 16.11 Particularités doctrinales vs les autres blocs

Synthèse comparative des spécificités américaines :

- **Séparation institutionnelle** : renseignement (NSA, CIA), militaire (USCYBERCOM), law enforcement (FBI), protection civile (CISA) sont distincts. Modèle atypique — la Russie, la Chine, l’Iran intègrent davantage ces fonctions.
- **Usage massif du droit** : indictments, sanctions, Entity List, Executive Orders. Les États-Unis sont le seul pays qui utilise le droit comme instrument diplomatique cyber à cette échelle.
- **Publicité des attributions** : les États-Unis communiquent publiquement sur les attributions avec un niveau de détail sans équivalent. Advisory techniques (NSA/CISA/FBI), rapports annuels, déclarations officielles.
- **Defend forward / hunt forward** : doctrine d’initiative plutôt que de réaction, opérations ouvertement assumées dans les réseaux adverses et alliés.
- **Coordination Five Eyes** : partage de renseignement et d’attribution avec UK, Canada, Australie, Nouvelle-Zélande (Ch.17).
- **Contrôle démocratique et judiciaire** : les opérations cyber américaines sont encadrées par des autorités légales (Title 10 pour le militaire, Title 50 pour le renseignement), des supervisions congressionnelles (Senate Intelligence Committee, House Intelligence Committee), et des contrôles judiciaires (FISA Court pour certaines collectes). Ces mécanismes ne sont pas parfaits mais distinguent le modèle américain de celui d’autres grandes puissances cyber.

Pour l’analyste : face à une activité attribuée aux États-Unis, les considérations différent de celles sur les autres acteurs — question de l’autorité légale invoquée, cadre de commandement (Title 10 vs Title 50), probabilité d’attribution publique à terme, possibilité de réponse diplomatique publique.

-----

### Chapitre 17 — Royaume-Uni et Five Eyes

#### 17.1 GCHQ : agence SIGINT et partenaire NSA

**Government Communications Headquarters** (GCHQ) est l’agence britannique d’origine électromagnétique et cyber. Héritière de Bletchley Park (déchiffrement Enigma pendant la Seconde Guerre mondiale), GCHQ est un partenaire étroit de la NSA — la relation US-UK en matière de SIGINT est la plus intégrée au monde, formalisée par l’**UKUSA Agreement** (1946) qui a évolué vers les Five Eyes.

**Mission** : collecte SIGINT mondiale, analyse cyber, soutien aux opérations militaires britanniques, protection de la sécurité nationale.

**Structure** : GCHQ dispose d’une branche cyber offensive intégrée au **National Cyber Force** (voir 17.3) et d’une branche défensive dans le **NCSC** (voir 17.2). La Joint Forces Intelligence Group et d’autres structures complètent le dispositif.

**Publications** : GCHQ publie occasionnellement des analyses techniques, en coordination avec le NCSC. Les attributions GCHQ-NCSC sont parmi les premières dans les attributions coordonnées Five Eyes (NotPetya, SolarWinds, Volt Typhoon).

#### 17.2 NCSC : le modèle de protection nationale

**National Cyber Security Centre** (NCSC), créé en 2016 comme branche publique du GCHQ, est l’organisme britannique de protection cyber nationale. Le modèle NCSC est largement considéré comme **une référence internationale** et a inspiré plusieurs agences européennes (ANSSI en partie, BSI en Allemagne).

**Caractéristiques du modèle NCSC** :

- **Publications accessibles** : documentation technique de haute qualité, formulée dans un langage accessible aux non-experts.
- **Collaboration directe avec le secteur privé** : « Active Cyber Defence » programme qui offre gratuitement des services aux organisations britanniques (DMARC, protective DNS, takedown de sites de phishing).
- **Early Warning et threat intelligence partagée** : le NCSC partage des alertes avec les organisations inscrites.
- **Cyber Essentials** : certification cybersécurité accessible aux PME britanniques — modèle qui a inspiré d’autres programmes européens.
- **Transparence** : le NCSC communique plus ouvertement que la plupart de ses homologues sur les incidents nationaux et les menaces — tout en respectant les classifications nécessaires.

**Attributions** : le NCSC (avec GCHQ) attribue publiquement des opérations étatiques. Les attributions NotPetya (2018), Volt Typhoon (2023-2024), APT31 (2024), Salt Typhoon (2024) ont été coordonnées avec les partenaires Five Eyes et relayées par le NCSC.

**NCSC Annual Review** : rapport annuel public qui documente les tendances de la menace sur le Royaume-Uni, les opérations de défense, et les points de mobilisation.

#### 17.3 National Cyber Force : opérations offensives

**National Cyber Force** (NCF), créée publiquement en 2020, est l’organisation britannique dédiée aux opérations cyber offensives. Elle rassemble des personnels du GCHQ, du Ministry of Defence (notamment 77th Brigade pour les opérations d’information), et du Secret Intelligence Service (MI6/SIS).

**Mission** : conduire des opérations cyber offensives pour soutenir les intérêts britanniques, avec un focus sur la **disruption ciblée** plutôt que sur la destruction massive. Le NCF se positionne doctrinalement sur la « disruption by design » — désorganiser les adversaires sans détruire, contester sans escalader.

**Cas d’usage publics** :

- Opérations contre les infrastructures Daesh (héritage de JTRIG).
- Opérations contre des réseaux pédocriminels.
- Opérations cyber en soutien des opérations militaires britanniques.
- Opérations contre des groupes cybercriminels (contributions aux démantèlements internationaux).

La NCF est moins visible publiquement qu’USCYBERCOM, mais sa création formelle marque un jalon — le Royaume-Uni a ouvertement assumé ses capacités cyber offensives.

#### 17.4 JTRIG : opérations d’information et disruption

**Joint Threat Research Intelligence Group** (JTRIG) est une branche historique du GCHQ, révélée publiquement par les fuites Snowden (2014). Ses capacités incluent des opérations d’influence en ligne, des disruptions de forums criminels et extrémistes, et des opérations d’information contre des cibles stratégiques.

Les documents JTRIG révélés par Snowden ont documenté des opérations contre Anonymous, contre des forums djihadistes, et contre des cibles gouvernementales étrangères. L’exposition publique a suscité des débats sur la légitimité démocratique de certaines opérations (ciblage d’acteurs non étatiques, techniques de manipulation psychologique).

Post-Snowden, JTRIG a probablement été restructurée dans d’autres entités (NCF notamment) mais ses capacités et missions ne sont pas publiquement supprimées.

#### 17.5 Five Eyes : l’alliance SIGINT intégrée

L’alliance **Five Eyes** (US, UK, Canada, Australie, Nouvelle-Zélande) est le partage de renseignement SIGINT et cyber le plus intégré au monde. Hérité de l’UKUSA Agreement de 1946, elle s’est étendue progressivement aux trois autres signataires du Commonwealth.

**Mécanismes** :

- **Partage de renseignement SIGINT** : les cinq agences (NSA, GCHQ, CSE Canada, ASD Australie, GCSB NZ) partagent leur collecte entre elles, avec des règles de retenue selon la sensibilité.
- **Partage cyber** : advisories conjoints, IoC et TTP partagés en quasi temps réel, coordination des attributions publiques.
- **Division du travail géographique et technique** : historiquement, chaque Eye couvrait des zones géographiques spécifiques ou des capacités techniques complémentaires.

**Autres agences Five Eyes** :

- **Canada — Communications Security Establishment** (CSE) et **Canadian Centre for Cyber Security** (CCCS, branche publique du CSE, créé 2018 sur le modèle NCSC).
- **Australie — Australian Signals Directorate** (ASD) et **Australian Cyber Security Centre** (ACSC).
- **Nouvelle-Zélande — Government Communications Security Bureau** (GCSB).

**Attributions coordonnées** : les grandes attributions cyber récentes ont presque toutes été Five Eyes avec relais dans chaque pays. NotPetya (2018), SolarWinds (2021), Hafnium/ProxyLogon (2021), Volt Typhoon (2023-2024), APT31 (2024), APT40 (2024), Salt Typhoon (2024-2025) ont toutes été attribuées dans des communiqués coordonnés des cinq pays (plus souvent étendus à des alliés européens et asiatiques : France, Allemagne, Japon, Corée du Sud, Pays-Bas, etc.).

**Étendues d’alliés** : au-delà des Five Eyes stricto sensu, les attributions et les partages s’étendent régulièrement à des « alliés +1 » ou « +X » — **AUKUS** (US, UK, Australie, avec dimension nucléaire), **Quad** (US, Japon, Inde, Australie), **UKUSA élargi** (incluant parfois France, Allemagne, Pays-Bas, Japon, Corée du Sud). La géographie du partage cyber s’étend continuellement.

#### 17.6 Opérations documentées

**Disruption de botnets** : contribution britannique à de multiples démantèlements (Emotet, Qakbot, LockBit notamment, où la NCA britannique a été en lead).

**Opérations contre Daesh** : GCHQ et le Ministry of Defence ont publiquement reconnu des opérations cyber contre les infrastructures de communication et de propagande de Daesh (2015-2019).

**Attribution Volt Typhoon (2023)** : le NCSC a co-signé l’advisory Five Eyes de mai 2023 qui a publiquement attribué Volt Typhoon à la Chine. Le ciblage des infrastructures critiques britanniques par des acteurs chinois est un thème récurrent des déclarations publiques NCSC.

**Attribution APT31 (mars 2024)** : le UK a attribué APT31 à des ciblages de parlementaires britanniques et de la Commission électorale. Sanctions coordonnées avec les États-Unis.

**Operation Cronos (LockBit, février 2024)** : la NCA (National Crime Agency) a été en lead de l’opération internationale. Premier cas d’opération de démantèlement ransomware majeur avec le Royaume-Uni en tête.

#### 17.7 Modèle de disruption by design

La doctrine britannique peut être résumée par le concept de **« disruption by design »** : contester les adversaires cyber en dégradant leurs capacités, sans nécessairement chercher des effets destructeurs majeurs. Le NCF articule des opérations proportionnées — désorganiser une campagne de phishing, rendre inopérants des outils spécifiques, exposer publiquement des opérateurs.

Cette doctrine est cohérente avec la tradition britannique d’intelligence operations — actions clandestines préférées à l’action militaire ouverte, usage stratégique du law enforcement et de la diplomatie, coordination étroite avec les partenaires.

-----

### Chapitre 18 — Israël : cyber, renseignement et supériorité technologique

#### 18.1 Un écosystème unique : intégration militaire-renseignement-privé

L’écosystème cyber israélien est **unique au monde** par son intégration militaire-renseignement-privé. Un trajectoire typique : formation à l’**Unité 8200** (cyber militaire) pendant le service national, puis carrière mixte militaire/renseignement, souvent suivie de fondations de startups cyber et de surveillance qui vendent leurs capacités au secteur privé mondial.

Cette intégration produit un avantage comparatif majeur : les startups israéliennes de cybersécurité et de surveillance ont accès à des talents formés par l’appareil de défense, et l’appareil de défense bénéficie des innovations civiles. C’est aussi ce qui explique la présence disproportionnée d’entreprises israéliennes dans le marché de la surveillance offensive (NSO, Intellexa, Candiru, Paragon — tous fondés par des vétérans de l’Unité 8200 ou services apparentés).

#### 18.2 Unité 8200 : pépinière de talents

**Unité 8200** (Yehida Shmoneh-Matayim — 8200) est l’unité de renseignement SIGINT et cyber de l’**IDF** (Israel Defense Forces). C’est la « NSA israélienne » — avec une différence notable : elle recrute des jeunes (17-18 ans) par le service militaire obligatoire.

**Taille et ressources** : Unité 8200 est l’une des plus grandes unités de l’IDF. Les chiffres exacts sont classifiés mais les estimations la situent entre 5 000 et 10 000 personnes actives. Pour un pays de 9 millions d’habitants, c’est une concentration cyber par capita sans équivalent.

**Sélection et formation** : les candidats à l’Unité 8200 sont identifiés dès le lycée via des tests d’aptitude. Formation technique intensive (mathématiques, cryptographie, informatique, langues). Les meilleurs éléments sont ensuite déployés dans les spécialités opérationnelles (intrusion, analyse, linguistique, etc.).

**Mission** : collecte SIGINT sur les menaces envers Israël (Iran et son axe, Hezbollah, Hamas, groupes palestiniens, autres adversaires régionaux), capacités cyber offensives, contre-espionnage cyber.

**Pipeline vers le privé** : après leur service militaire (3 ans pour les hommes, 2 pour les femmes, avec extensions fréquentes dans les unités techniques), les vétérans de l’Unité 8200 fondent massivement des entreprises cyber. Check Point, Palo Alto Networks (fondateurs), CyberArk, Imperva, Varonis, SentinelOne, Wiz, Claroty — la liste est immense. Et côté offensive : NSO, Intellexa (co-fondateur), Candiru, Paragon, et dizaines d’autres.

#### 18.3 Mossad : opérations clandestines extérieures

**Ha’Mossad le’Modi’in ule-Tafkidim Meyuhadim** (Institut pour le Renseignement et les Missions Spéciales) est le service de renseignement extérieur israélien. Équivalent approximatif de la CIA américaine ou du SIS britannique.

**Capacités cyber** : le Mossad dispose de capacités cyber intégrées à ses opérations clandestines. Contrairement à l’Unité 8200 (collecte SIGINT de masse), le Mossad conduit des opérations cyber ciblées — souvent combinées avec du HUMINT, des opérations physiques, des sabotages. Le **Directorate for Cyber** au sein du Mossad coordonne ces capacités.

**Cas emblématiques** :

- **Stuxnet (co-attribution avec la NSA)** : coopération Mossad-NSA/CIA pour l’implémentation du malware. Le rôle israélien incluait le renseignement HUMINT permettant la connaissance fine de Natanz (spécifications des centrifugeuses, configuration des automates Siemens, routines opérationnelles).
- **Opérations contre le programme nucléaire iranien** : série d’opérations coordonnées (assassinats de scientifiques nucléaires, sabotages physiques et cyber, opérations d’exfiltration de renseignement). L’opération de **vol des archives nucléaires iraniennes** en 2018 (exfiltration physique de centaines de kilos de documents classifiés depuis un entrepôt à Téhéran) a été présentée comme une opération Mossad emblématique — partiellement coordonnée avec des moyens cyber.
- **Hizbullah / Hamas** : opérations continues de renseignement et de disruption contre les infrastructures des organisations ennemies d’Israël.

#### 18.4 Shin Bet : sécurité intérieure

**Shin Bet / Shabak / ISA** (Israel Security Agency) est le service de sécurité intérieure. Mission : contre-espionnage, contre-terrorisme dans les territoires, surveillance intérieure. Dispose de capacités cyber pour la surveillance des menaces envers la sécurité intérieure d’Israël (infiltration des organisations palestiniennes, surveillance des citoyens israéliens soupçonnés de liens avec des menaces).

L’usage par le Shin Bet de capacités cyber domestiques a fait l’objet de débats juridiques et politiques en Israël, notamment lors de la période COVID-19 (usage de capacités cyber pour le traçage de contacts — jugée disproportionnée par certains tribunaux).

#### 18.5 INCD : coordination nationale

**Israel National Cyber Directorate** (INCD), créé 2017, est l’agence civile de coordination de la cybersécurité israélienne. Équivalent approximatif de CISA américaine ou de l’ANSSI française.

**Mission** : protection des infrastructures critiques israéliennes, coordination avec le secteur privé, publication d’advisories, gestion des crises cyber majeures. INCD opère un CERT-IL qui coordonne la réponse aux incidents nationaux.

**Rôle** : l’INCD est l’entité qui coordonne les réponses publiques israéliennes aux incidents cyber — publication d’alertes, collaborations avec les secteurs (santé, énergie, transports). Le directorate a un rôle central particulièrement depuis l’intensification des cyberattaques iraniennes post-octobre 2023.

#### 18.6 Doctrine de préemption appliquée au cyber

La doctrine israélienne de sécurité nationale — shaped by l’histoire du pays — inclut traditionnellement un principe de **préemption** : agir avant que les menaces se matérialisent, plutôt que réagir après agression. Le **Begin Doctrine** (1981) — nommée d’après la frappe israélienne sur le réacteur nucléaire d’Osirak en Irak — codifie l’idée que Israël ne tolère pas que des adversaires régionaux acquièrent des capacités d’armes de destruction massive.

Appliquée au cyber, cette doctrine se traduit par :

- **Action continue plutôt que réactive** : Israël considère le cyberespace comme un espace d’action permanent, pas uniquement une réponse à agression.
- **Ciblage des programmes adverses** : les opérations cyber israéliennes visent souvent à dégrader les capacités adverses en amont — programme nucléaire iranien, capacités du Hezbollah, infrastructures de ciblage du Hamas.
- **Préemption sur les menaces asymétriques** : usage du cyber pour préempter des attentats, des frappes de roquettes, des tentatives d’infiltration.

#### 18.7 Stuxnet : la première arme cyber OT

**Stuxnet (2010)** est l’opération cyber israélo-américaine emblématique. Déjà traité au Ch.14 (impact sur l’Iran) et abordé au Ch.21 (OT/ICS). Synthèse pour la dimension israélienne.

**Rôle israélien** : Israël a probablement apporté (selon les reconstructions journalistiques les plus solides, notamment *Confront and Conceal* de David Sanger et *Dark Territory* de Fred Kaplan) l’intelligence précise sur le site de Natanz (HUMINT, connaissance des centrifugeuses IR-1, configuration Siemens), co-développé certains composants, et probablement opéré l’exécution finale. Les États-Unis ont apporté les capacités cyber plus larges (NSA/TAO) et l’autorisation stratégique.

**Impact stratégique pour Israël** : retardement du programme iranien de 2-3 ans. Démonstration que le cyber peut produire des effets équivalents à des opérations militaires ciblées, sans les risques politiques d’une frappe conventionnelle sur un pays tiers.

**Conséquences non anticipées** : propagation non contrôlée de Stuxnet, découverte publique (2010), fuite du code et étude par tous les acteurs étatiques — prolifération des capacités OT qui a bénéficié à la Russie (Sandworm), à l’Iran (programme cyber massivement renforcé en réponse), et à d’autres acteurs.

#### 18.8 Pipeline Unité 8200 → startups → surveillance commerciale

La trajectoire de beaucoup de vétérans Unité 8200 vers la surveillance commerciale mérite un traitement dédié car elle structure une part majeure du marché mondial des PSO.

**NSO Group** : fondé en 2010 par Niv Carmi, Shalev Hulio et Omri Lavie — vétérans de l’Unité 8200. Pegasus est devenu le spyware commercial le plus sophistiqué au monde. Ventes contrôlées par le **ministère israélien de la Défense** (les exportations de cyber-armes sont considérées comme des exportations d’armement en Israël, nécessitant des licences officielles) — ce qui signifie que le gouvernement israélien approuve la liste des clients étatiques de NSO. Cette structure a des implications géopolitiques : Israël utilise les autorisations NSO comme levier diplomatique (suspension/rétablissement selon les relations).

**Intellexa** : consortium européen avec forte présence israélienne, fondé par Tal Dilian (vétéran du renseignement militaire israélien). Concurrent direct de NSO.

**Candiru** : fondé en 2014 par d’anciens de l’Unité 8200. Spyware desktop.

**Paragon Solutions** : plus récent (2019), fondé par d’anciens de l’Unité 8200. Spyware mobile « Graphite », positionnement plus restrictif que NSO (refus déclaré de vendre à des régimes autoritaires — positionnement éthique contesté).

**Tensions éthiques** : le marché de la surveillance israélienne a fait l’objet de critiques croissantes (Pegasus Project 2021, usage contre des journalistes et dissidents dans des régimes autoritaires). Les réponses gouvernementales israéliennes ont oscillé entre la défense des entreprises (argumentaire économique et d’influence) et la restriction progressive (suspension de licences pour certains pays après scandales).

#### 18.9 NSO / Pegasus : enjeux de gouvernance

**Pegasus** mérite une analyse dédiée comme cas emblématique des enjeux contemporains.

**Capacités techniques** : Pegasus exploite des **0-day iOS et Android** (parfois développés à l’interne, parfois achetés à des brokers). Le malware obtient un accès complet au terminal — messages (y compris messageries chiffrées type Signal, WhatsApp, Telegram lues en post-déchiffrement sur le terminal lui-même), géolocalisation, microphone et caméra activables à distance, extraction de données.

**Clients documentés** : gouvernements de dizaines de pays, incluant des démocraties européennes (Espagne, Hongrie, Pologne), des régimes moins démocratiques (Arabie saoudite, Émirats, Azerbaïdjan, Mexique), et plusieurs régimes autoritaires.

**Usages contestés documentés** :

- **Journalistes** : Jamal Khashoggi (journaliste saoudien dissident, assassiné en 2018 au consulat saoudien d’Istanbul — ses proches avaient Pegasus installé, suggérant l’usage pour le tracker avant l’assassinat), Cecilio Pineda (journaliste mexicain assassiné en 2017), des dizaines d’autres documentés par le **Pegasus Project** (consortium de 17 médias coordonnés par Forbidden Stories, 2021).
- **Dissidents** : exilés saoudiens, marocains, azerbaïdjanais, catalans en Espagne, journalistes d’opposition en Pologne.
- **Politiciens** : Emmanuel Macron et plusieurs dirigeants européens listés parmi les cibles potentielles. L’usage par le gouvernement polonais (PiS) contre des opposants a fait scandale en 2022.

**Réponses** :

- **Entity List US** (novembre 2021) : NSO ajouté, restrictions d’accès aux technologies américaines.
- **Apple et Meta ont porté plainte** contre NSO.
- **Enquêtes parlementaires** : enquête européenne PEGA (2022-2023) a produit des recommandations pour limiter l’usage des spywares en UE.
- **Difficultés financières de NSO** : sanctions, contentieux, changements de direction.

#### 18.10 Conflit Israël-Hamas post-octobre 2023 : cyber dimension

Le conflit déclenché par l’attaque du Hamas le 7 octobre 2023 a amplifié la dimension cyber des opérations israéliennes et des réponses adverses.

**Cyberopérations israéliennes (peu documentées publiquement pour raisons opérationnelles)** :

- Renseignement cyber sur le Hamas au Liban et dans la bande de Gaza.
- Opérations de disruption contre les infrastructures de communication du Hamas et du Hezbollah.
- Reconnaissance cyber en amont des opérations militaires.

**Cyberopérations adverses** :

- **Iran / Agrius / IRGC** : wipers contre cibles israéliennes, opérations d’influence.
- **Hacktivistes pro-palestiniens / pro-Hamas** : volume massif d’attaques DDoS, défacement, tentatives d’intrusion contre des cibles israéliennes. Sophistication généralement basse.
- **Campagnes d’influence coordonnées** : amplification de narratifs sur les réseaux sociaux, deepfakes ponctuels.

**Cyberespace comme théâtre** : le conflit a illustré comment le cyber est intégré dans un conflit cinétique moderne — pas comme remplaçant du conventionnel, mais comme complément indispensable.

-----

### Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel

#### 19.1 Contexte : la transformation 2014-2022

L’Ukraine est le **laboratoire mondial** de la cyberdéfense en temps de guerre. Sa trajectoire depuis 2014 (annexion de la Crimée, premières cyberattaques russes majeures) jusqu’à 2022 (invasion à grande échelle) et ses années de guerre ont produit un retour d’expérience unique — analysé, partagé, et étudié par toutes les agences cyber occidentales.

**Avant 2014** : l’Ukraine n’avait pas d’appareil cyber particulièrement mature. Les services de sécurité (SBU) avaient des capacités limitées. L’écosystème privé était modeste, avec une forte dépendance aux prestataires russes (historique post-soviétique).

**2014 (annexion Crimée + Donbass)** : les premières cyberattaques russes majeures en marge des opérations militaires — ciblage de la Commission électorale centrale ukrainienne en mai 2014 (tentative de manipulation des résultats de l’élection présidentielle, déjouée), BlackEnergy déployé contre le secteur énergie (avant 2015).

**2015-2021 — construction d’une posture cyber** :

- **Décembre 2015** : premier blackout cyber (BlackEnergy/KillDisk) contre trois distributeurs d’électricité. Prise de conscience nationale. Début de la coopération internationale intensive.
- **Décembre 2016** : Industroyer contre Kiev. Deuxième blackout.
- **2017** : NotPetya (supply chain M.E.Doc) — l’Ukraine absorbe le premier choc d’une cyberattaque qui deviendra mondiale.
- **2015-2022** : création et renforcement du **CERT-UA**, du **SSSCIP** (State Special Communications Service), renforcement des capacités cyber de la SBU. Coopération avec USCYBERCOM (hunt forward depuis 2018), NATO, UE.

**2022+ (invasion à grande échelle)** : l’Ukraine est devenue l’environnement de confrontation cyber le plus intense au monde. Les enseignements tirés de cette période sont étudiés partout.

#### 19.2 L’appareil cyber ukrainien

**CERT-UA** (Computer Emergency Response Team of Ukraine) est le CERT national. Rattaché au SSSCIP, il conduit les réponses aux incidents cyber d’envergure nationale, publie des advisories techniques, et coordonne avec les partenaires internationaux. Le CERT-UA publie quotidiennement des alertes pendant la guerre — volume de publication parmi les plus élevés au monde.

**SSSCIP** (State Special Communications Service) est l’agence technique qui supervise la cybersécurité civile ukrainienne. Opère le CERT-UA, gère la sécurité des communications gouvernementales, et coordonne la défense des infrastructures critiques.

**SBU** (Sluzhba Bezpeky Ukrayiny — Service de sécurité d’Ukraine) est le principal service de renseignement et de sécurité. Dispose d’une branche cyber qui conduit des opérations de contre-intelligence, d’investigation cyber, et — selon certains rapports — des opérations cyber offensives ciblées.

**Ministry of Digital Transformation** : ministère dédié créé en 2019, dirigé par **Mykhailo Fedorov**. A joué un rôle central dans la coordination cyber depuis 2022 — publication de l’appel à la mobilisation de l’IT Army, coordination avec les grands fournisseurs cloud pour la migration d’urgence, communication publique internationale sur la guerre cyber.

**HUR** (Holovne Upravlinnia Rozvidky — Direction principale du renseignement, sous Ministry of Defense) conduit les opérations de renseignement militaire, y compris la dimension cyber. Certaines opérations ukrainiennes offensives publiquement revendiquées sont attribuées au HUR.

#### 19.3 Coopération sans précédent avec le secteur privé et les alliés

La **coopération public-privé-international** mise en place autour de l’Ukraine est sans précédent dans l’histoire du cyber. Caractéristiques.

**Microsoft** : **Microsoft Threat Intelligence Center** (MSTIC) est en ligne avec l’Ukraine depuis 2022. Publications de dizaines de rapports publics documentant les attaques russes en temps réel, détection et neutralisation en quasi temps réel des malwares russes déployés (Microsoft a poussé des mises à jour de Defender qui ont neutralisé des wipers russes en heures). Microsoft a également migré des volumes considérables de données gouvernementales ukrainiennes vers Azure pour les protéger de frappes physiques (centres de données russes). Les rapports publics de Microsoft sur l’Ukraine sont devenus une référence de la documentation CTI.

**Google / Threat Analysis Group (TAG) et Mandiant** : **Project Shield** (protection DDoS gratuite pour les médias et les gouvernements à risque) a été massivement déployé en Ukraine. Mandiant (acquis par Google en 2022) a fourni un soutien IR continu.

**ESET** (Bratislava, Slovaquie) : ESET a une présence historique en Ukraine. La collaboration CERT-UA/ESET a permis la **détection et neutralisation d’Industroyer2** en avril 2022 — l’une des opérations défensives les plus remarquables de la guerre cyber. ESET publie régulièrement des analyses techniques détaillées des malwares russes déployés en Ukraine.

**Amazon Web Services** : migration d’urgence de données gouvernementales ukrainiennes vers AWS dans les premiers jours de l’invasion. Les datacenters ukrainiens étant des cibles potentielles de frappes physiques, la migration cloud a été une mesure de résilience essentielle.

**Starlink (SpaceX)** : connectivité satellitaire critique. Starlink a été déployé massivement en Ukraine dès février 2022, fournissant une connectivité résiliente aux forces armées, aux services publics, et aux civils dans les zones sans infrastructure télécom. Le rôle de Starlink est à double tranchant : dépendance stratégique envers un opérateur privé (SpaceX/Elon Musk) dont les décisions individuelles (limitation de l’usage au-dessus de la Crimée, par exemple) ont pu affecter les opérations militaires.

**Cloudflare** : protection DDoS, services de sécurité web.

**USCYBERCOM hunt forward** : équipes américaines déployées dans les réseaux ukrainiens depuis 2018, intensifiées massivement depuis 2022. Détection de menaces, partage en temps réel, remontée des TTP russes observées aux défenseurs occidentaux.

**Autres alliés européens** : CERT-EU, ANSSI (France), BSI (Allemagne), NCSC (UK), CERT-LT (Lituanie) — contributions techniques et analytiques. L’Estonie a joué un rôle particulier comme « voix cyber » européenne vis-à-vis de l’Ukraine (mémoire de l’attaque de 2007 contre l’Estonie).

Ce modèle de coopération public-privé-international a produit :

- Une **visibilité sans précédent** sur les TTP d’un acteur étatique (la Russie) dans un conflit réel.
- Une **vitesse de détection et de neutralisation** que l’Ukraine seule n’aurait pas pu atteindre.
- Un **laboratoire** pour les techniques défensives modernes, utilisable par tous les alliés.

#### 19.4 Les opérations offensives ukrainiennes

Les opérations cyber offensives ukrainiennes sont documentées publiquement de manière fragmentaire. Plusieurs catégories :

**Opérations du HUR (renseignement militaire)** : cyber-sabotages contre des systèmes logistiques russes, compromission de caméras de surveillance russes (pour exfiltrer des flux vidéo révélant des mouvements militaires), compromission de systèmes de communication militaire russe, ciblage d’officiels russes.

**Opérations revendiquées publiquement** :

- **Compromission de banques russes** : plusieurs fuites de données de grandes banques russes revendiquées par des acteurs proches des services ukrainiens.
- **Hack de Rosaviatsiya** (régulateur aéronautique russe) : fuite de documents en 2022.
- **Opérations contre les médias d’État russes** : défacements ponctuels, interruptions de diffusion.

**Opérations en coordination avec l’IT Army** : certaines opérations de l’IT Army of Ukraine (voir 19.5) ont été publiquement reconnues par des responsables ukrainiens, suggérant une coordination informelle entre services et volontaires.

#### 19.5 IT Army of Ukraine : zone grise hacktivisme/opération militaire

L’**IT Army of Ukraine** est un mouvement de volontaires cyber internationaux lancé publiquement par **Mykhailo Fedorov** (ministre de la Transformation numérique) via Telegram le 26 février 2022, deux jours après l’invasion.

**Modus operandi** : le canal Telegram de l’IT Army publie des listes de cibles russes (sites gouvernementaux, entreprises, médias) et appelle les volontaires à conduire des actions (DDoS principalement, parfois hacking plus sophistiqué). Le nombre de membres a dépassé 300 000 au plus haut. Une variété d’outils automatisés a été mise à disposition (scripts DDoS, plugins navigateur).

**Activités** :

- **DDoS massif** : sites gouvernementaux russes, banques, médias d’État, plateformes de service public.
- **Défacements** : sites russes compromis avec messages pro-ukrainiens.
- **Fuites de données** : publication de données russes exfiltrées par des membres plus sophistiqués.

**Zone grise** : l’IT Army illustre la difficulté contemporaine de classifier les opérations cyber.

- **Coordonnée par l’État** (via Fedorov) ? — oui, publiquement.
- **Composée de volontaires indépendants** ? — oui, majoritairement.
- **Hacktivisme ou opération militaire** ? — la question est juridiquement ouverte. Les membres de l’IT Army ne sont pas des combattants légalement (pas d’uniforme, pas d’incorporation militaire), mais ils conduisent des opérations coordonnées par l’État dans un conflit armé.
- **Cadre juridique** ? — les actions de l’IT Army constituent dans la plupart des juridictions des infractions cyber. Les participants prennent des risques juridiques réels selon leur pays de résidence.

Pour la doctrine internationale, l’IT Army pose des questions nouvelles — que ni le droit humanitaire international, ni le droit de la cybersécurité n’ont pleinement résolues. Voir Ch.26 pour les implications sur la responsabilité étatique.

#### 19.6 Retour d’expérience technique : résilience sous feu

Plusieurs enseignements techniques majeurs de la guerre cyber en Ukraine.

**Résilience par la décentralisation** : les infrastructures ukrainiennes critiques ont été décentralisées (géographiquement et architecturalement). Un datacenter bombardé, un point de connectivité détruit n’interrompent pas l’ensemble — la redondance est la norme. Cette leçon est directement applicable à la préparation européenne.

**Migration cloud d’urgence** : la migration vers les clouds publics (AWS, Azure) des données gouvernementales critiques a été une mesure de résilience majeure. Préserve les données face aux frappes physiques, permet l’accès depuis n’importe où.

**Backup hors ligne et récupération rapide** : les multiples wipers russes ont imposé une discipline de backup rigoureuse. Les organisations ukrainiennes qui ont survécu aux wipers sont celles qui avaient des backups hors ligne régulièrement testés. Cette leçon est universelle.

**Détection rapide et réponse coordonnée** : la neutralisation d’Industroyer2 en quelques heures illustre ce qu’une collaboration CERT-UA/ESET bien rodée peut accomplir. La **rapidité** est un paramètre critique en cyberdéfense — la différence entre réponse en heures vs en jours peut être la différence entre incident contenu et catastrophe.

**Connectivité résiliente** : Starlink et les technologies satellitaires sont désormais des éléments stratégiques de la planification de résilience cyber.

#### 19.7 Efficacité relative des cyberattaques dans un conflit cinétique

L’observation empirique la plus intéressante de la guerre cyber en Ukraine : le **cyber seul ne gagne pas une guerre**. Malgré l’intensité massive des cyberopérations russes, aucune n’a produit d’effet décisif sur le cours de la guerre conventionnelle.

**Pourquoi** :

- **Les blackouts cyber sont temporaires** : les blackouts de 2022 (réussis partiellement) ont été réparés en **heures à jours**, grâce à l’expérience accumulée depuis 2015 et aux équipes bien rodées. L’impact humain/militaire a été bien inférieur à celui d’une frappe physique équivalente.
- **Les frappes physiques sont plus efficaces pour les effets voulus** : lorsque la Russie a voulu détruire l’infrastructure énergétique ukrainienne de façon durable, elle a utilisé des missiles de croisière (hiver 2022-2023), pas des cyberattaques. Les missiles détruisent physiquement, les cyberattaques produisent des pannes de durée limitée.
- **La résilience peut être construite** : face à la menace cyber anticipée, l’Ukraine a construit une résilience qui a massivement limité l’impact effectif.

**Leçons pour les défenseurs européens** :

- **Anticiper** : le cyber sera un composant des conflits futurs, pas le composant central.
- **Construire la résilience** : backups, décentralisation, cloud, exercices.
- **Investir dans la coopération internationale** : le modèle Ukraine-alliés doit être reproductible.
- **Ne pas sur-investir dans la défense cyber au détriment de la défense conventionnelle** : le cyber complète, il ne remplace pas.

#### 19.8 Implications pour l’Europe

L’expérience ukrainienne informe directement la préparation cyber européenne. Plusieurs implications opérationnelles.

**Pour les OIV et entités essentielles NIS 2** :

- Les infrastructures critiques européennes sont des cibles crédibles de pré-positionnement ou d’attaque directe dans un scénario d’escalade.
- La résilience sous bombardement (cinétique) doit être intégrée à la planification cyber — pas seulement la défense contre le cyber isolé.
- Les exercices cyber doivent inclure des scénarios de conflit composé (cyber + cinétique + économique).

**Pour les CERT nationaux et CSIRT sectoriels** :

- Le modèle de partage en temps réel (CERT-UA avec Microsoft, ESET, alliés) est à cultiver.
- Les relations préalables avec les vendors CTI majeurs sont indispensables — ne pas les construire pendant la crise.
- Les advisories CERT-UA sont une ressource permanente à intégrer aux workflows.

**Pour les agences nationales (ANSSI, BSI, NCSC)** :

- La coopération avec les pays de première ligne (États baltes, Pologne, Roumanie) est stratégique.
- Le soutien à l’Ukraine (partage de renseignement, assistance technique) nourrit en retour les capacités européennes.

**Pour l’UE** :

- **EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence — inspiré en partie de l’expérience ukrainienne.
- La coordination continue avec l’Ukraine reste une priorité stratégique.

Pour l’analyste cyber travaillant sur la menace russe contre l’Europe, la référence méthodologique est : « comment les mêmes TTP observées en Ukraine s’appliqueraient-elles à mon organisation si le conflit escaladait ? ». Cette approche traduit les enseignements ukrainiens en préparation concrète.

-----

## PARTIE VI — MENACES OT ET PRÉ-POSITIONNEMENT

> **Ce que cette partie apprend.** Comprendre ce qui rend l’environnement OT radicalement différent de l’IT (protocoles sans authentification, systèmes hérités, impact physique), connaître les campagnes OT emblématiques qui ont défini le domaine (Stuxnet, Industroyer, Triton), maîtriser le concept de pré-positionnement comme menace structurelle de la prochaine décennie, et comprendre les principes de protection des infrastructures critiques.
> 
> **Ce qu’elle ne couvre pas.** Le détail technique d’ingénierie des systèmes industriels (domaine distinct), la doctrine complète de SOC OT (cours dédié OT security), les cadres réglementaires détaillés (Annexe G pour NIS 2 et OIV).
> 
> **Ce que vous saurez faire après cette partie.** Lire une architecture OT et identifier ses points d’exposition, reconnaître une campagne OT via ses TTP caractéristiques, formuler le dilemme du pré-positionnement (éradiquer vs surveiller), et participer à la construction d’une posture de protection d’infrastructure critique.

-----

### Chapitre 20 — Architecture OT/ICS et protocoles industriels

#### 20.1 Qu’est-ce que l’OT : SCADA, DCS, PLC, HMI, historians, SIS

L’**OT** (Operational Technology) désigne l’ensemble des systèmes informatiques qui contrôlent ou supervisent des processus physiques — électricité, eau, gaz, pétrole, transport, fabrication, bâtiments. Par opposition à l’IT (Information Technology) qui traite de l’information, l’OT agit sur le monde physique.

Le vocabulaire technique est dense et mérite d’être maîtrisé.

**PLC** (Programmable Logic Controller — automate programmable industriel) : le composant de terrain qui exécute les fonctions de contrôle. Un PLC lit des capteurs (température, pression, débit), exécute une logique de contrôle programmée, et commande des actionneurs (vannes, moteurs, disjoncteurs). Exemples : Siemens S7-300/400/1500, Schneider Modicon M340/M580, Rockwell ControlLogix, Allen-Bradley SLC/MicroLogix. Les PLC ciblés par Stuxnet étaient des Siemens S7-315 et S7-417.

**DCS** (Distributed Control System — système de contrôle distribué) : architecture de contrôle pour les processus industriels continus (raffineries, centrales électriques, usines chimiques). Le DCS distribue les fonctions de contrôle entre plusieurs unités. Exemples : Honeywell Experion, Yokogawa CENTUM, ABB 800xA, Emerson DeltaV. Le DCS est typiquement plus intégré et plus propriétaire qu’un assemblage de PLC.

**SCADA** (Supervisory Control and Data Acquisition) : système de supervision qui collecte les données des PLC/DCS et permet aux opérateurs d’agir à distance. SCADA est plus distribué géographiquement que DCS (utile pour des infrastructures étalées — réseau électrique, réseau d’eau, oléoducs). Exemples : Siemens SIMATIC WinCC, GE iFIX, Schneider Citect, Wonderware/AVEVA System Platform.

**HMI** (Human-Machine Interface) : les écrans et interfaces par lesquels les opérateurs interagissent avec le SCADA/DCS. Peuvent être des applications Windows dédiées, des web clients, ou des panneaux industriels.

**Historian** : base de données spécialisée qui stocke les valeurs historiques des capteurs et des commandes — utilisée pour l’analyse, le reporting, la conformité réglementaire. Exemples : OSIsoft PI System (racheté par AVEVA), GE Proficy Historian, Wonderware Historian.

**SIS** (Safety Instrumented System — systèmes de sécurité industrielle) : systèmes **indépendants** du contrôle opérationnel, dont la **seule fonction** est d’arrêter le processus en cas de conditions dangereuses pour prévenir les accidents. Les SIS sont l’ultime filet de sécurité — si les contrôles classiques échouent, le SIS déclenche un arrêt d’urgence (shutdown). Exemples : Schneider Triconex, Rockwell/Allen-Bradley GuardLogix, Siemens SIMATIC S7-400F/FH, Honeywell Safety Manager. Les SIS font l’objet d’une norme spécifique (**IEC 61511**) et d’un niveau d’exigence (SIL — Safety Integrity Level) calibré selon le risque.

**RTU** (Remote Terminal Unit) : variante de PLC adaptée aux installations distantes et isolées (puits de pétrole, postes électriques, stations de pompage d’eau), souvent avec des communications longue distance.

**Engineering workstation** : poste de travail d’ingénieur utilisé pour programmer et configurer les PLC/DCS. Typiquement Windows, avec le logiciel de l’éditeur (Siemens TIA Portal, Rockwell Studio 5000, etc.). **Les engineering workstations sont des cibles de très haute valeur** — elles ont les credentials et les outils pour modifier la logique de contrôle.

#### 20.2 Le modèle Purdue et la segmentation par niveau

Le **modèle Purdue** (Purdue Enterprise Reference Architecture — PERA, étendu en ISA-95) structure l’architecture OT en **niveaux** qui reflètent une hiérarchie fonctionnelle et justifient une segmentation réseau.

**Niveau 0 — Processus physique** : le processus physique lui-même (turbine, four, tuyauterie, chaîne de production).

**Niveau 1 — Contrôle de base** : les PLC et les capteurs/actionneurs qui agissent directement sur le niveau 0.

**Niveau 2 — Contrôle de supervision** : SCADA, DCS, HMI, historian locaux. C’est le niveau où les opérateurs supervisent et interviennent.

**Niveau 3 — Opérations de site** : MES (Manufacturing Execution System), gestion de production, historian globaux, systèmes de planification opérationnelle.

**DMZ industrielle (entre niveaux 3 et 4)** : zone démilitarisée qui filtre les flux entre l’OT (niveaux 0-3) et l’IT (niveaux 4-5). Devrait être obligatoire dans toute architecture sécurisée.

**Niveau 4 — Réseau bureautique** : systèmes IT classiques de l’organisation (ERP, messagerie, collaboration).

**Niveau 5 — Internet / Cloud** : connectivité externe.

**Niveaux SIS (parallèles)** : les SIS sont architecturalement **indépendants** des niveaux 1-3 du contrôle normal — ils ont leurs propres capteurs, leur propre logique, leurs propres actionneurs. Cette indépendance est la raison pour laquelle ils peuvent intervenir quand le contrôle normal échoue.

**Le principe** : les flux doivent être **contrôlés strictement entre niveaux**, notamment entre les niveaux IT (4-5) et OT (3 et moins). Un accès au niveau 4 ne devrait jamais donner un accès direct au niveau 2 — il doit passer par la DMZ industrielle avec authentification et inspection.

**En pratique** : cette segmentation idéale est souvent imparfaite. Les mises à jour des équipements OT nécessitent des accès depuis le niveau 4 (éditeurs, MSP distants), les postes d’ingénierie sont souvent double-connectés, les prestataires externes ont des accès VPN qui contournent partiellement l’architecture. **Ces imperfections sont les chemins d’attaque utilisés par les APT** pour compromettre l’OT via l’IT.

#### 20.3 Protocoles industriels : Modbus, DNP3, IEC 60870-5-104, IEC 61850, OPC, PROFINET

Les protocoles industriels transportent les commandes et les mesures entre les composants OT. Leur connaissance est essentielle pour comprendre à la fois les opérations légitimes et les attaques.

**Modbus** (Modicon, 1979) : protocole historique, encore très largement déployé. Existe en Modbus RTU (série) et Modbus TCP (sur Ethernet). Extrêmement simple : lecture et écriture de registres. **Aucune authentification native**, aucun chiffrement, aucune intégrité. Un attaquant sur le réseau OT peut écrire dans n’importe quel registre d’un équipement accessible. Modbus est critiqué depuis des décennies pour son insécurité mais reste dominant dans l’industrie (inertie, coût de remplacement).

**DNP3** (Distributed Network Protocol, développé dans les années 1990 pour le secteur électrique, RTU vers control center) : largement utilisé dans le secteur électrique nord-américain. Version « DNP3 Secure Authentication » offre une authentification mais est rarement déployée.

**IEC 60870-5-104 (IEC 104)** : protocole de télécontrôle standardisé en Europe pour le secteur électrique (équivalent européen de DNP3). Transport sur TCP/IP. **Utilisé par Industroyer** pour commander directement les disjoncteurs et produire le blackout de Kiev 2016. Pas d’authentification native.

**IEC 61850** : standard plus récent pour les sous-stations électriques, orienté objet et utilisant Ethernet. Inclut **GOOSE** (Generic Object Oriented Substation Event) pour les communications rapides entre équipements de protection, et **SMV** (Sampled Measured Values) pour la télémétrie. Utilisé également par Industroyer. Sécurité améliorée par rapport aux protocoles plus anciens mais déploiement sécurisé inégal.

**OPC DA** (OLE for Process Control Data Access) : protocole Windows (basé sur DCOM) pour l’intégration SCADA/DCS, historiquement très utilisé mais considéré comme obsolète. Sécurité faible, dépendance Windows. Utilisé par Industroyer également.

**OPC UA** (Unified Architecture) : successeur moderne d’OPC DA, cross-platform, sécurité intégrée (authentification, chiffrement, signature). Adoption progressive mais la migration depuis OPC DA est lente dans les installations existantes.

**PROFINET** (PROcess FIeld NETwork) : standard d’Ethernet industriel pour l’automatisation, développé par Siemens. Dominant dans l’industrie manufacturière européenne.

**EtherNet/IP** (dérivé de CIP — Common Industrial Protocol) : standard américain concurrent de PROFINET, utilisé par Rockwell/Allen-Bradley.

**HART** (Highway Addressable Remote Transducer) : protocole historique pour la communication avec les capteurs intelligents (mesures de procédés chimiques, pétroliers). Existe en version filaire et sans fil (WirelessHART).

**Implications sécurité** : presque tous ces protocoles ont été conçus **avant que la cybersécurité soit une considération**. Leur sécurité native va de faible (Modbus, IEC 104) à moyenne (IEC 61850 avec options sécurisées), rarement à élevée (OPC UA bien configuré). La **sécurité OT repose donc massivement sur la segmentation réseau** plutôt que sur la sécurité intrinsèque des protocoles — si un attaquant atteint le réseau OT, il dispose de leviers considérables.

#### 20.4 Absence d’authentification native et risques associés

Reprenons le point central : la plupart des protocoles OT n’exigent **aucune authentification** pour émettre des commandes. Cette caractéristique a des conséquences directes sur la nature des attaques OT.

**Implication n°1 — Accès au réseau = capacité d’action** : si un attaquant pénètre le segment OT, il peut directement commander des équipements. Pas besoin de compromettre des credentials additionnels — la seule question est de connaître la carte du réseau et les adresses des équipements.

**Implication n°2 — Pas de trace forte** : sans authentification, il n’y a pas de log fiable de « qui a envoyé telle commande ». Les investigations post-incident doivent s’appuyer sur des corrélations réseau (quelle IP source, quelle timing), pas sur des logs applicatifs.

**Implication n°3 — Les mitigations sont réseau** : l’ensemble de la sécurité OT dépend massivement de la segmentation (qui peut parler à qui), de la surveillance (qui parle en temps réel), et du durcissement des points de passage (engineering workstations, jump hosts).

**Implication n°4 — Les équipements eux-mêmes ne se défendent pas** : un PLC qui reçoit une commande Modbus « écrire valeur 100 dans registre 40001 » l’exécute, quelle que soit la source. Il n’y a pas d’équivalent d’un antivirus ou d’un EDR sur un PLC historique. Les PLC récents commencent à intégrer des fonctions de sécurité, mais le parc déployé reste largement vulnérable.

#### 20.5 Convergence IT/OT : causes, avantages, risques

La **convergence IT/OT** est la tendance structurelle des dernières décennies où les frontières entre IT et OT se brouillent. Causes et conséquences.

**Causes** :

- **Besoin de données** : les directions veulent des tableaux de bord en temps réel consolidant données OT et IT (production, qualité, énergie consommée, maintenance).
- **Maintenance à distance** : les éditeurs d’équipements OT (Siemens, Schneider, Rockwell, ABB) proposent de la télémaintenance, qui nécessite des accès depuis Internet vers le réseau OT.
- **Migration cloud** : certaines fonctions historian et MES basculent vers le cloud.
- **IT des objets (IIoT)** : les nouveaux équipements OT intègrent nativement des fonctions IT (API REST, connexions cloud).
- **Coûts** : un réseau unifié est moins cher qu’un réseau OT isolé maintenu séparément.

**Avantages** : efficacité opérationnelle, visibilité métier, optimisation des processus.

**Risques** : la convergence **crée des chemins d’attaque** du réseau IT (largement exposé) vers le réseau OT. Ces chemins sont précisément ceux qu’exploitent les APT.

**Exemples de chemins exploités** :

- **Engineering workstation à double connexion** : ordinateur d’ingénieur connecté simultanément au réseau IT (pour emails, mises à jour) et au réseau OT (pour programmer les PLC). Compromis côté IT, il devient un pivot vers l’OT. C’est le chemin utilisé dans BLACKOUT et dans beaucoup de compromissions OT réelles.
- **Jump hosts / bastions** : serveurs de rebond entre IT et OT. S’ils sont durcis, ils peuvent être un point de contrôle ; mal configurés, ils sont un chemin direct.
- **Prestataires distants via VPN** : éditeurs de logiciels, intégrateurs, mainteneurs — accès VPN qui contourne la segmentation normale.
- **Supply chain logicielle** : les mises à jour d’applications historian ou HMI peuvent porter du malware (cas de M.E.Doc pour NotPetya — même si M.E.Doc n’était pas strictement OT, le pattern s’applique).
- **Ports USB** : les ingénieurs utilisent des USB pour transférer des configurations, des logs, des mises à jour. Un USB infecté peut franchir la segmentation physique.

**Recommandation générale** : la convergence étant une réalité irréversible, la sécurité doit être **pensée autour des chemins d’exposition**, pas uniquement autour d’une séparation stricte qui n’existe que partiellement dans la pratique.

#### 20.6 Systèmes hérités : la problématique du patching et de l’EDR

Une spécificité majeure de l’environnement OT : la **longévité extrême des équipements**. Un PLC ou un DCS déployé a typiquement une durée de vie de **15 à 30 ans**. Les systèmes de contrôle dans les centrales électriques, raffineries, et sites industriels lourds peuvent être encore plus anciens.

**Implications** :

- **Pas de patching** : les équipements anciens ne reçoivent plus de mises à jour de sécurité. Les vulnérabilités connues ne sont pas corrigées. Et même quand des patches existent, l’appliquer nécessite souvent un arrêt du processus industriel — opération coûteuse, risquée, et rarement réalisée.
- **OS obsolètes** : les HMI et engineering workstations tournent souvent sur Windows XP, Windows 7, Windows Server 2003 ou 2008 — systèmes non-supportés qui restent en production parce que les applications industrielles ne sont pas certifiées sur les versions récentes.
- **Pas d’EDR** : les PLC et équipements de terrain ne supportent pas d’agents EDR. Les engineering workstations sur Windows obsolète ne peuvent souvent pas accueillir d’EDR moderne non plus. La détection repose entièrement sur le réseau et les comportements observables en amont.
- **Contraintes temps réel** : les équipements OT ont des contraintes temps réel qui ne tolèrent aucune latence additionnelle. Un EDR qui ralentit un HMI de 50 ms peut déstabiliser la supervision. Cette contrainte limite les options de défense.

**Approches modernes** :

- **Replacement progressif** : remplacer les équipements obsolètes quand c’est possible (mais cycles longs).
- **Compensating controls** : segmentation, monitoring, access control stricts autour des équipements qui ne peuvent pas être sécurisés intrinsèquement.
- **Passive monitoring OT** : capteurs réseau passifs (qui n’injectent aucun trafic) qui surveillent les communications OT et détectent les anomalies. Approche non-intrusive compatible avec les contraintes OT.

#### 20.7 Le modèle d’attaque OT classique

L’attaque OT typique suit une séquence prévisible. La connaître permet d’anticiper où placer les détections.

**Étape 1 — Accès initial via IT** : phishing, exploitation edge, supply chain — les vecteurs sont ceux des APT IT classiques. Les attaquants accèdent au réseau bureautique (niveau 4 Purdue).

**Étape 2 — Mouvement latéral dans l’IT** : reconnaissance AD, credential dumping, Kerberoasting, identification des cibles d’intérêt. L’objectif : identifier les comptes et les systèmes qui ont accès au réseau OT.

**Étape 3 — Identification du chemin vers l’OT** : recherche des engineering workstations, des jump hosts, des serveurs historian ayant des pieds dans les deux mondes. BloodHound peut révéler ces chemins.

**Étape 4 — Pivot vers l’OT** : compromission d’un engineering workstation ou d’un jump host, utilisation pour pénétrer le segment OT. **Cette étape est le point de rupture** — avant, l’attaquant est dans un environnement IT classique ; après, il est dans un environnement où les défenses classiques ne fonctionnent plus.

**Étape 5 — Reconnaissance OT** : identification des équipements présents (PLC, HMI, RTU, SIS), identification des protocoles utilisés, cartographie du processus industriel. **Cette phase est typiquement longue — semaines à mois** — car l’attaquant doit comprendre ce qu’il peut faire. Un PLC Siemens S7 dans une raffinerie contrôle un processus spécifique ; modifier ses paramètres a des effets spécifiques. L’attaquant doit apprendre le processus.

**Étape 6 — Préparation de l’action** : développement ou adaptation du code qui manipulera les équipements. Peut impliquer du reverse engineering de la logique de contrôle, des tests en environnement de staging.

**Étape 7 — Déclenchement** : envoi des commandes malveillantes. Peut être : manipulation directe des automates (Industroyer), modification de la logique de contrôle (Stuxnet), désactivation des SIS (Triton), simple coupure par ouverture de disjoncteurs (Ukraine 2015).

**Durée totale** : de l’accès initial au déclenchement, une opération OT sophistiquée prend **plusieurs mois à plusieurs années**. Cette longue phase de préparation est la raison pour laquelle la détection précoce dans la phase IT est critique — intervenir avant que l’attaquant n’atteigne l’OT est bien plus facile que de contenir une fois le pivot effectué.

#### 20.8 Visibilité OT : passive monitoring

La défense OT repose largement sur la **visibilité** des communications dans le segment OT. Les technologies dédiées ont émergé dans les années 2010-2020.

**Passive monitoring** : les capteurs passifs se connectent aux segments OT via des **mirror ports** ou des **network taps** — ils observent tout le trafic sans injecter le moindre paquet. Cette approche est compatible avec les contraintes OT (aucune latence ajoutée, aucun risque de perturber le processus).

**Vendors majeurs** :

- **Claroty** : plateforme OT orientée asset discovery, threat detection, risk management.
- **Dragos** : spécialisé sur les grandes infrastructures industrielles (énergie, eau, pétrole/gaz). Équipe de threat intelligence OT reconnue (Sergio Caltagirone, Joe Slowik historiquement).
- **Nozomi Networks** : plateforme polyvalente.
- **Tenable OT Security** (ex Indegy) : couvert par l’acquisition Tenable.
- **Cisco Cyber Vision** : solution Cisco intégrée.
- **Microsoft Defender for IoT** (ex CyberX) : intégration Microsoft.

Ces outils fournissent :

- **Asset inventory** : découverte automatique des équipements OT et leurs caractéristiques (marque, modèle, firmware).
- **Vulnerability assessment** : identification des CVE applicables aux équipements.
- **Anomaly detection** : détection des communications atypiques (nouveau flux, commandes inhabituelles).
- **Threat intelligence OT** : détection des TTP documentées (patterns d’Industroyer, de Triton, etc.).

**Leçon opérationnelle** : une organisation qui n’a pas de visibilité OT **ne peut pas détecter** une compromission OT sophistiquée avant qu’elle ne produise un effet physique. Investir dans la visibilité OT est la première étape de la maturité.

#### 20.9 La protection des SIS : l’enjeu ultime

Les **SIS** (Safety Instrumented Systems) méritent une attention particulière car ils représentent **l’ultime filet de sécurité physique** dans une installation industrielle.

**Principe** : les SIS sont conçus pour arrêter le processus en cas de conditions dangereuses. Si la température d’un réacteur dépasse un seuil critique, si une pression devient incontrôlable, si un capteur révèle une fuite — le SIS déclenche un **shutdown** ordonné qui met l’installation en état sûr.

**Indépendance** : pour garantir cette fonction, les SIS sont **architecturalement indépendants** du contrôle normal. Ils ont leurs propres capteurs, leur propre logique, leurs propres actionneurs. Un défaut du contrôle normal ne doit pas affecter le SIS.

**La menace ultime — désactiver les SIS** : si un attaquant **désactive les SIS AVANT de provoquer une condition dangereuse**, il neutralise l’ultime filet de sécurité. L’installation peut alors atteindre des conditions qui, sans SIS fonctionnel, causent des dommages physiques catastrophiques — explosion, fuite toxique, accident grave.

**C’est ce qu’a tenté Triton/TRISIS** (Arabie Saoudite 2017, Ch.21) contre les Triconex Schneider d’une usine pétrochimique. L’attaque a échoué — mais par chance (un arrêt de sécurité non anticipé a révélé l’intrusion). Si elle avait réussi, le scénario envisageable incluait potentiellement une explosion majeure avec pertes humaines.

**Protection des SIS** :

- **Isolation physique absolue** : idéalement, les SIS ne devraient avoir aucune connexion réseau à quoi que ce soit d’autre. Le strict minimum opérationnel (logs, maintenance) doit être géré via des postes dédiés air-gappés.
- **Air gap** : séparation physique totale entre SIS et autres réseaux, y compris les autres segments OT. Si impossible, diodes unidirectionnelles (hardware qui permet le flux dans un seul sens).
- **Credentials séparés** : les ingénieurs SIS ont des comptes distincts de ceux du contrôle opérationnel.
- **Audits réguliers** : vérification de l’intégrité des programmes SIS.

La protection des SIS n’est pas un « nice to have » — elle est l’enjeu le plus critique de la cybersécurité industrielle, celui où un échec produit des morts.

-----

### Chapitre 21 — Campagnes OT/ICS destructrices

Ce chapitre documente les campagnes OT emblématiques dans un ordre globalement chronologique. Ensemble, elles constituent l’**histoire contemporaine** du cyber appliqué aux infrastructures physiques.

#### 21.1 Stuxnet (2010) — la première arme cyber OT

**Acteurs** : États-Unis et Israël (co-attribution). **Cible** : centrifugeuses d’enrichissement d’uranium iraniennes à Natanz.

**Traité aux Ch.14 (impact Iran) et Ch.18 (Israël).** Synthèse pour la dimension OT.

**Architecture technique** :

- Quatre **vulnérabilités 0-day Windows** utilisées pour la propagation initiale (inhabituel — un seul 0-day suffirait en général).
- Ciblage extrêmement précis : **ne s’activait que sur des systèmes Windows spécifiques** exécutant **Siemens WinCC/STEP7** (logiciel de programmation PLC Siemens) **connectés à des PLC S7-315 ou S7-417** contrôlant des **centrifugeuses tournant à certaines vitesses spécifiques**. Ces quatre conditions combinées garantissaient que Stuxnet ne s’activerait que sur les systèmes ciblés.
- **Modification de la logique PLC** : une fois sur le système de contrôle, Stuxnet modifiait la programmation du PLC pour faire osciller la vitesse des centrifugeuses entre limites extrêmes, provoquant des contraintes mécaniques qui les détruisaient progressivement.
- **Masquage** : parallèlement, Stuxnet interceptait les signaux de télémétrie et **affichait des valeurs normales aux opérateurs**. Les ingénieurs voyaient sur leurs HMI que tout fonctionnait normalement pendant que les centrifugeuses s’auto-détruisaient.

**Impact** : environ 1 000 centrifugeuses détruites entre 2008 et 2010, programme iranien retardé de 2-3 ans selon les estimations.

**Leçons OT** :

- **Les PLC peuvent être manipulés avec effet physique** : démonstration fondatrice.
- **Le masquage des opérateurs est possible et dangereux** : les HMI peuvent mentir.
- **Les engineering workstations sont des cibles critiques** : Stuxnet utilisait l’engineering workstation Siemens pour modifier le PLC.
- **La propagation non contrôlée** : Stuxnet s’est échappé des systèmes ciblés via USB, révélant l’opération. Le risque de « blowback » des armes cyber est réel.

#### 21.2 BlackEnergy / KillDisk — Ukraine décembre 2015

**Acteur** : Sandworm (GRU Unit 74455). **Cible** : trois distributeurs d’électricité ukrainiens — Prykarpattyaoblenergo, Kyivoblenergo, Chernivtsioblenergo. **Premier blackout cyber confirmé de l’histoire**.

**Chronologie** :

- **Printemps-été 2015** : phase de reconnaissance et compromission initiale via spear-phishing (documents Office avec macro, envoyés à des ingénieurs des distributeurs).
- **Plusieurs mois** : mouvement latéral, compromission des systèmes de supervision, pivot vers les segments OT.
- **23 décembre 2015, 15h30** : déclenchement. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA.

**Mécanisme de l’attaque** :

- **Prise de contrôle manuelle** des HMI via des outils d’administration à distance. Les opérateurs ukrainiens ont vu, sur leurs propres écrans, leurs souris bouger et leur clavier taper sans leur action.
- **Ouverture manuelle de 30+ disjoncteurs** dans les postes de transformation.
- **230 000 foyers** privés d’électricité pendant ~6 heures.
- **KillDisk** déployé en parallèle : wiper effaçant les systèmes de supervision pour compliquer la récupération et prolonger l’indisponibilité.

**Particularité** : l’attaque a été **largement manuelle** — des opérateurs humains cliquant sur des HMI à distance. Pas de malware automatisé qui commande les équipements. Cette approche indique une compréhension fine du système mais aussi une prise de risque (l’opération prenait du temps, les défenseurs pouvaient réagir).

**Restoration** : les opérateurs ukrainiens, entraînés à basculer en mode manuel, ont rétabli l’alimentation en parcourant physiquement les postes et en refermant les disjoncteurs manuellement.

**Attribution** : CERT-UA, SBU, puis Mandiant et d’autres — attribution à Sandworm publiée en 2016-2017.

**Leçons** :

- **Un blackout cyber est possible** : démonstration empirique.
- **Les opérateurs entraînés peuvent récupérer rapidement** : la capacité de basculer en manuel est un élément de résilience majeur.
- **KillDisk en complément** : pattern Sandworm de combiner attaque et wiper pour maximiser l’indisponibilité.

#### 21.3 Industroyer / CrashOverride — Ukraine décembre 2016

**Acteur** : Sandworm. **Cible** : poste de transformation électrique de la banlieue de Kiev.

**Rupture par rapport à 2015** : Industroyer est le **premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles industriels natifs**. Contrairement à 2015 où l’attaque était manuelle, Industroyer **automatise** la manipulation des équipements.

**Architecture Industroyer** :

- **Module IEC 60870-5-101** : protocole série électrique.
- **Module IEC 60870-5-104** : version TCP/IP du précédent, protocole dominant en Europe. Le module peut énumérer les équipements et **commander l’ouverture/fermeture des disjoncteurs**.
- **Module IEC 61850** : protocole des sous-stations modernes. Peut émettre des commandes GOOSE.
- **Module OPC DA** : intégration SCADA/DCS.
- **Module de wiping** : destruction des configurations et des systèmes de supervision.
- **Backdoor** pour la persistence et l’accès ultérieur.

**Déclenchement** : 17 décembre 2016, minuit. Le module IEC 104 ouvre les disjoncteurs. Blackout dans une partie de Kiev pendant ~1 heure.

**Sophistication** : Industroyer démontre que Sandworm a investi dans des capacités OT sur mesure. Chaque module représente une compréhension approfondie du protocole correspondant et des systèmes qui l’implémentent.

**Attribution** : attribution à Sandworm confirmée par ESET (qui a analysé le malware en profondeur — rapport fondateur de juin 2017) et par les agences Five Eyes.

**Leçons** :

- **Le cyber OT est industrialisable** : pas seulement des attaques ponctuelles manuelles, mais des outils sophistiqués réutilisables.
- **Les protocoles sans authentification sont des leviers d’attaque directs** : IEC 104, IEC 61850 — pas d’authentification, commandes exécutées sans challenge.
- **L’investissement OT des acteurs étatiques est sérieux** : développer Industroyer a pris probablement 1-2 ans d’effort.

#### 21.4 Triton / TRISIS — Arabie Saoudite 2017

**Acteur** : attribué à la Russie, plus précisément au **Central Scientific Research Institute of Chemistry and Mechanics (TsNIIKhM)** — institut de recherche militaire russe, sanctionné par OFAC en 2020. **Cible** : usine pétrochimique saoudienne (non nommée publiquement, mais largement identifiée comme Petro Rabigh).

**Rupture** : Triton est le premier malware à avoir ciblé explicitement des **SIS** (Safety Instrumented Systems) — les systèmes de sécurité ultimes.

**Cible spécifique** : **Schneider Triconex** — marque emblématique de SIS, largement déployée dans l’industrie pétrochimique et nucléaire. Triton était conçu pour reprogrammer les Triconex, désactivant potentiellement leurs fonctions de sécurité.

**Scénario envisagé** : si Triton avait réussi pleinement, l’attaquant aurait pu, à un moment choisi, **désactiver les SIS puis provoquer une condition dangereuse** dans le processus industriel. Sans SIS pour déclencher le shutdown, l’installation atteint potentiellement des conditions d’**explosion ou de fuite toxique**. Les dommages envisageables incluaient des pertes humaines significatives.

**Comment Triton a été découvert** : par **accident**. Lors d’une intervention Triton sur un Triconex, le malware a provoqué un **arrêt de sécurité non anticipé** — le Triconex a détecté une anomalie dans sa propre programmation et s’est mis en mode sûr (shutdown). Les ingénieurs saoudiens, cherchant à comprendre pourquoi leur SIS s’était arrêté, ont découvert la compromission.

**Attribution** : Dragos a attribué Triton à un acteur qu’il a nommé **XENOTIME**. L’attribution plus précise au TsNIIKhM russe a été établie par le FBI et publiée via sanctions OFAC en 2020.

**Implication stratégique** : Triton est **le wake-up call** sur les risques OT. Un État avait investi dans une capacité visant à pouvoir, à un moment politique choisi, causer des morts via cyber. La ligne entre cyber et terrorisme d’État est franchie, ou près de l’être.

**Leçons OT** :

- **Les SIS sont des cibles APT** : ne plus considérer les SIS comme « naturellement protégés » parce que « critiques ».
- **L’air gap SIS est indispensable** : isolation totale.
- **Des capacités SIS sont en développement** : au-delà de Triton, d’autres acteurs étatiques ont probablement des capacités similaires. XENOTIME est suivi comme groupe actif.

#### 21.5 Industroyer2 — Ukraine avril 2022

**Acteur** : Sandworm. **Cible** : un opérateur électrique ukrainien (non nommé publiquement mais situé dans la région de Kiev).

**Contexte** : dans les semaines suivant l’invasion russe de l’Ukraine (24 février 2022), Sandworm tente de reproduire son succès de 2016 en développant **Industroyer2** — évolution du malware de 2016.

**Améliorations Industroyer2** :

- Modules protocoles OT conservés.
- Ciblage plus précis (adapté à la victime spécifique).
- Pattern de déclenchement synchronisé avec d’autres opérations (wiper CaddyWiper prévu en parallèle pour complexifier la réponse).

**Échec grâce à la défense** : **Industroyer2 a été déjoué**. L’équipe CERT-UA, en collaboration avec **ESET**, a détecté le déploiement avant le déclenchement prévu. Une analyse rapide a permis la neutralisation en quelques heures. Le déclenchement prévu n’a pas eu lieu, ou seulement avec des effets très limités.

**Signification** : succès défensif majeur. Démonstration que la coopération CERT-UA/vendor CTI peut neutraliser une attaque OT étatique avant impact. C’est un modèle opérationnel étudié par toutes les agences cyber occidentales.

**Publication** : rapport conjoint CERT-UA et ESET (avril 2022) documente le malware et la réponse défensive. Lecture importante pour comprendre l’état de l’art OT défensif.

#### 21.6 Colonial Pipeline (mai 2021) — ransomware IT avec impact OT

**Acteur** : **DarkSide** (groupe RaaS russophone). **Cible** : **Colonial Pipeline**, opérateur d’un oléoduc majeur transportant ~45% de l’essence consommée sur la côte est américaine.

**Particularité** : Colonial Pipeline illustre un pattern où **le cyber IT produit un impact OT indirect**, sans que l’OT soit directement compromis.

**Chronologie** :

- Compromission initiale via un **compte VPN sans MFA** (credentials probablement issus d’un breach ou d’un infostealer).
- Déploiement de DarkSide sur le réseau IT.
- **7 mai 2021** : Colonial Pipeline **coupe volontairement l’OT** — par mesure de précaution, l’entreprise arrête l’oléoduc parce qu’elle ne peut pas garantir que l’OT n’a pas été compromis et parce que le système de facturation (IT) est inopérant (pas de moyen de facturer les clients).
- **Impact** : pénuries d’essence sur la côte est US pendant plusieurs jours, situation d’urgence déclarée par le gouverneur de plusieurs États.
- Colonial Pipeline paie une rançon d’environ 4,4 millions de dollars en Bitcoin (dont environ 2,3 millions seront **récupérés ultérieurement par le FBI** — première récupération notable de rançon crypto).

**Leçons** :

- **La convergence IT/OT crée des dépendances opérationnelles** : même sans compromission OT directe, un incident IT peut paralyser l’OT (par précaution légitime ou par dépendance business — facturation, logistique).
- **Les credentials VPN sont un vecteur majeur** : MFA sur les accès distants n’est pas optionnel.
- **Le paiement de rançon peut être partiellement récupéré** : coopération FBI/exchanges/blockchain intelligence.
- **Conséquences macroéconomiques** : une cyberattaque sur une infrastructure critique peut produire des effets au niveau sociétal (pénuries, urgence).

#### 21.7 CosmicEnergy — malware Sandworm découvert 2023

**Acteur** : Sandworm (probablement). **Découverte** : Mandiant a publié en mai 2023 l’analyse d’un nouveau malware OT nommé **CosmicEnergy**, trouvé sur **VirusTotal** (uploadé par quelqu’un — probablement l’auteur, un chercheur, ou une victime).

**Capacités** : CosmicEnergy cible les **systèmes de protection IEC 60870-5-104** — similaire à Industroyer mais avec des différences techniques suggérant une évolution distincte. Peut envoyer des commandes IEC 104 pour ouvrir/fermer des équipements.

**Incertitude** : l’utilisation opérationnelle de CosmicEnergy n’est pas confirmée publiquement — il peut s’agir d’un malware en développement, d’un outil de red team russe, ou d’un malware qui n’a pas encore été déployé.

**Signification** : démonstration que le **développement d’outils OT offensifs continue**. Sandworm (ou des acteurs apparentés) investit dans une nouvelle génération de capacités OT. La menace reste active et évolutive.

#### 21.8 Attaques récentes 2024-2025

**Cyber Av3ngers contre l’eau (fin 2023 - 2024)** : groupe attribué à l’Iran (IRGC) qui a ciblé des **PLC Unitronics exposés sur Internet** dans des systèmes d’eau municipaux américains. Impact limité (message politique sur les écrans HMI, pas de perturbation majeure du processus), mais démonstration symbolique forte. A conduit à une mobilisation CISA et à des advisories aux opérateurs d’eau.

**Tentatives sur les opérateurs électriques européens (2023-2025)** : advisory ANSSI et BSI ont évoqué publiquement (sans nommer de cibles) des tentatives d’intrusion dans des opérateurs électriques européens. Attribution variable entre acteurs russes (Sandworm, Unit 29155) et acteurs chinois.

**Ciblage d’installations oil & gas et pétrochimiques** : depuis 2022, plusieurs incidents non rendus publics, mais des rapports Dragos et Mandiant font état d’une activité croissante. Certaines compagnies pétrolières européennes ont renforcé publiquement leurs équipes OT security.

**Le contexte général 2024-2026** : les attaques OT se multiplient en tentatives, avec relativement peu d’impacts majeurs publics en Europe. Mais la pression est croissante, et le modèle BLACKOUT (pré-positionnement sans action immédiate) est probablement plus fréquent que les incidents publics ne le suggèrent.

#### 21.9 Leçons générales des campagnes OT

La synthèse des campagnes OT documentées dessine un **corpus de leçons transversales**.

**Le cyber OT est réel et testé** : Stuxnet, Industroyer, Triton, Industroyer2, CosmicEnergy démontrent qu’au moins trois États (US/Israël, Russie, avec d’autres probablement) ont des capacités OT opérationnelles. Ce n’est pas une menace théorique.

**L’impact potentiel est physique** : blackouts, explosions potentielles (Triton), paralysies opérationnelles (Colonial). Le cyber peut produire des dommages comparables à des frappes militaires conventionnelles dans certains scénarios.

**La sophistication requise est importante** : développer un malware OT fonctionnel est un effort d’années pour des équipes expertes. Ce n’est pas à la portée d’un cybercriminel classique. Mais c’est à la portée de plusieurs États.

**Les défenses sont possibles** : Industroyer2 déjoué démontre qu’une défense OT bien préparée peut neutraliser une attaque étatique. La visibilité, la collaboration, et la rapidité de réponse sont les facteurs clés.

**Le pré-positionnement est la tendance actuelle** : moins d’attaques destructives déclenchées, plus d’opérations qui maintiennent un accès dormant. Ce pattern est l’objet du chapitre suivant.

-----

### Chapitre 22 — Le pré-positionnement : la menace silencieuse

#### 22.1 Définition opérationnelle du pré-positionnement

Le **pré-positionnement** est le maintien d’un **accès dormant** dans des infrastructures critiques, **sans action immédiate**, pour une utilisation future en cas de conflit ou d’escalade politique. C’est le scénario stratégique le plus inquiétant du paysage cyber contemporain.

**Caractéristiques opérationnelles** :

- **Accès maintenu** : l’attaquant a compromis des systèmes critiques et conserve la capacité d’y accéder.
- **Pas d’exfiltration massive** : contrairement à l’espionnage, le pré-positionnement ne collecte pas de renseignement (ou seulement le minimum nécessaire au maintien d’accès).
- **Pas de sabotage** : contrairement à une attaque destructive, aucune action malveillante n’est déclenchée.
- **Pas de ransomware** : aucune monétisation, aucune visibilité.
- **Patience opérationnelle** : l’accès peut être maintenu des mois ou des années avant activation — ou ne jamais être activé.

**Intention stratégique** : disposer d’un **levier activable** en cas de besoin. Le message implicite est : « en cas d’escalade/conflit/décision politique, nous pouvons activer ces accès pour causer des dommages aux infrastructures critiques de notre adversaire ».

C’est une **forme de dissuasion cyber**. Comme la dissuasion nucléaire, elle repose sur l’existence d’une capacité plus que sur son utilisation. Mais contrairement à la dissuasion nucléaire, elle est **silencieuse et ambiguë** — la cible peut ignorer l’existence du pré-positionnement, ce qui affaiblit l’effet dissuasif mais préserve la flexibilité opérationnelle.

#### 22.2 Volt Typhoon : le cas d’école

**Volt Typhoon** est l’exemple de pré-positionnement le plus documenté publiquement. Déjà introduit au Ch.9, traité en détail comme étude de cas au Ch.31.

**Synthèse pour ce chapitre** :

- Activité au moins depuis mi-2021, probablement plus tôt.
- Cibles : opérateurs de télécoms, énergie, eau, transport aux US et dans le Pacifique (Guam).
- TTP ultra-furtives : LotL exclusif, credentials légitimes, pas de malware custom, C2 via routeurs SOHO compromis.
- **Aucune exfiltration massive, aucune action destructive, aucune monétisation observées**.
- Attribué par les Five Eyes (advisory mai 2023 et réitérations 2024) à la Chine, probablement PLA ou affilié.

**Signification stratégique** : interprété par la communauté de renseignement américaine comme une **capacité de dissuasion/représailles chinoise** liée au scénario Taïwan. Si un conflit militaire éclate autour de Taïwan, la Chine pourrait activer ces accès pour frapper les infrastructures critiques américaines et alliées, dégradant les capacités de projection militaire US dans la région.

**Démantèlements partiels** : FBI a démantelé en janvier 2024 le **KV Botnet** (routeurs Cisco RV domestiques utilisés comme C2 Volt Typhoon) sous mandat judiciaire. Mais Volt Typhoon dispose probablement d’infrastructures alternatives.

#### 22.3 Salt Typhoon : autre dimension du pré-positionnement

**Salt Typhoon** illustre une autre facette : pré-positionnement pour l’espionnage stratégique plutôt que pour le sabotage. Déjà traité au Ch.9 et Ch.10.

**Synthèse** :

- Compromission de multiples opérateurs télécoms US (Verizon, AT&T, Lumen confirmés).
- Accès aux **Lawful Intercept Systems** — compromission ciblée permettant de voir qui les autorités américaines surveillaient.
- Accès aux communications de millions d’Américains, ciblage particulier de personnalités politiques.
- Durée de présence estimée à au moins un an avant détection.

**Pré-positionnement ou espionnage ?** Salt Typhoon se situe à la frontière. L’accès maintenu sur les télécoms **est** un pré-positionnement (levier activable en conflit), mais l’accès était aussi activement utilisé pour du renseignement. Cette combinaison — pré-positionnement + espionnage — est probablement la configuration la plus fréquente dans la réalité, les deux n’étant pas mutuellement exclusifs.

#### 22.4 Sandworm et le pré-positionnement énergie européenne

Le pré-positionnement n’est pas l’apanage chinois. **Sandworm (GRU Unit 74455)** conduit depuis plusieurs années des opérations de pré-positionnement dans les infrastructures critiques européennes, dans le contexte du conflit ukrainien.

**Documentation publique** :

- Advisory ANSSI (France), BSI (Allemagne), CERT-UA ont évoqué publiquement (avec parcimonie sur les détails) des tentatives d’intrusion dans des infrastructures critiques européennes.
- Rapports Mandiant, Microsoft, Dragos documentent des compromissions d’opérateurs énergie, eau, transport en Europe (sans nommer les victimes pour raisons opérationnelles).
- **Tentative Industroyer2 (avril 2022)** déjouée — démonstration d’intention et de capacité.

**Implications** : l’Europe est une cible de pré-positionnement russe crédible. Les opérateurs européens OIV (France) et entités essentielles (NIS 2) doivent intégrer ce scénario dans leur planification.

#### 22.5 Autres clusters sous observation

Plusieurs clusters sont sous observation pour des activités possibles de pré-positionnement, sans qu’une attribution définitive ait été publiée.

**Flax Typhoon** (Chine, lié à Integrity Technology Group sanctionné en 2025) : construisait un botnet massif (Raptor Train, 260 000+ dispositifs IoT compromis) démantelé en septembre 2024 par le FBI. Utilisé probablement comme infrastructure offensive pour d’autres clusters chinois — peut inclure des fonctions de pré-positionnement.

**Clusters non attribués** : les advisories ANSSI, CISA, et partenaires mentionnent régulièrement des clusters observés dans des infrastructures critiques, sans attribution publique à date. Leur caractérisation comme pré-positionnement dépend de l’observation de leur comportement (absence d’exfiltration, absence de destructif, maintien d’accès long terme).

**Clusters iraniens** : moins documentés comme pré-positionnement structurel, mais les ciblages « Cyber Av3ngers » sur l’eau et sur l’énergie incluent potentiellement des composantes de pré-positionnement (maintien d’accès post-démonstration initiale).

#### 22.6 La difficulté de détection maximale

Le pré-positionnement est la menace la plus difficile à détecter, pour des raisons structurelles.

**Pas de malware custom** : Volt Typhoon démontre que le LotL exclusif est possible et efficace. Sans binaire malveillant à hasher, les signatures EDR classiques sont aveugles.

**Pas de traffic anormal** : l’utilisation de LOLBins et de credentials légitimes produit un trafic qui ressemble à de l’administration normale. Les patterns de beaconing réguliers sont évités au profit d’accès intermittents et irréguliers.

**Pas de comportement distinctif** : les actions sont limitées au strict minimum nécessaire. Pas d’exfiltration visible, pas de tentatives de privilege escalation bruyantes, pas de mouvement latéral massif.

**Pas de monétisation** : contrairement au ransomware ou au cryptominer, le pré-positionnement ne génère aucune activité financière détectable.

**Longue durée** : les opérations s’étalent sur des mois à des années. Les anomalies, si détectables individuellement, se fondent dans le bruit de fond opérationnel normal.

**Implications détection** : la détection repose **entièrement** sur les **anomalies comportementales** et la **corrélation multi-sources**.

- **Baseline des activités admin** : un compte admin qui se connecte à un serveur inhabituel, à une heure inhabituelle, depuis un endpoint inhabituel est un signal. Établir la baseline prend du temps, la maintenir exige de la discipline.
- **Corrélation cross-sources** : connexion VPN + activité locale + connexion AD + trafic sortant. Aucun signal seul n’est conclusif ; leur combinaison peut l’être.
- **Threat hunting proactif** : recherche active d’anomalies subtiles, guidée par les TTP documentées des acteurs de pré-positionnement. Chasse au fil de l’eau, pas alerte automatique.
- **Détection réseau OT** : monitoring passif du trafic OT pour détecter les communications inhabituelles vers les équipements.

#### 22.7 Le dilemme : éradiquer ou surveiller ?

Une fois un pré-positionnement détecté, les défenseurs font face à un **dilemme opérationnel** sans solution simple.

**Option A — Éradication immédiate** :

- **Avantage** : élimine la menace active, élimine le risque d’activation.
- **Inconvénient** : signal à l’adversaire que la détection a eu lieu. L’adversaire adaptera ses TTP, réinfectera via des vecteurs différents, et sera plus difficile à détecter la prochaine fois. **Perte de visibilité stratégique**.
- **Inconvénient** : si l’éradication est incomplète (accès redondants non identifiés), l’adversaire revient rapidement avec des TTP modifiées.

**Option B — Surveillance contrôlée** :

- **Avantage** : collecte de renseignement sur les TTP, sur les objectifs, sur les capacités. Ce renseignement peut être partagé avec d’autres défenseurs potentiellement ciblés. Possibilité d’identifier d’autres victimes.
- **Avantage** : ne révèle pas la détection à l’adversaire, préservant la capacité de détecter une activation imminente.
- **Inconvénient** : **risque moral et opérationnel majeur**. Si l’adversaire active son pré-positionnement avant que le défenseur puisse intervenir, l’impact peut être catastrophique. **Qui porte la responsabilité** si un blackout survient pendant la phase de surveillance ?
- **Inconvénient** : nécessite une coordination étroite avec les autorités (agences nationales) et un consensus légal/politique souvent difficile à obtenir.

**Option C — Hybride** :

- **Éradication partielle** des accès identifiés tout en maintenant la surveillance sur d’autres vecteurs suspectés.
- **Collaboration avec les agences nationales** : l’agence nationale peut prendre le relais sur la surveillance stratégique pendant que l’opérateur éradique opérationnellement.
- **Partage d’information** : le pré-positionnement découvert est communiqué à la communauté (ISAC sectoriel, CERT) pour alerter d’autres victimes potentielles.

**En pratique** : le dilemme est **résolu au cas par cas** selon la gravité, le contexte géopolitique, les ressources disponibles, et le cadre juridique. Pour un opérateur privé, l’éradication rapide est souvent la réponse par défaut (risque opérationnel non acceptable). Pour les agences nationales sur des cibles stratégiques (télécoms, énergie), la surveillance contrôlée peut être préférée.

Le dilemme n’a pas de réponse universelle. Il est exercé dans les tabletops (Ch.28) et gagne à être pensé à froid, pas dans l’urgence d’un incident réel.

#### 22.8 Implications pour l’Europe

Le pré-positionnement est une menace crédible pour l’Europe. Implications opérationnelles.

**Secteurs prioritaires** :

- **Énergie** (électricité, gaz, pétrole) : cible historique de Sandworm, cible plausible de pré-positionnement chinois.
- **Télécoms** : cible démontrée par Salt Typhoon (US), extensible à l’Europe.
- **Eau** : cible de Cyber Av3ngers (Iran) et potentiellement d’acteurs russes.
- **Transport** (aéroportuaire, ferroviaire, maritime) : cible plausible pour des scénarios de disruption majeure.
- **Finance** : cible moins de pré-positionnement que d’espionnage et de fraude, mais à surveiller.
- **Santé** : cible ransomware massive, mais des APT peuvent s’y positionner aussi.

**Capacités à développer** :

- **Visibilité OT** (Ch.20) : passive monitoring sur les segments industriels.
- **Visibilité identité cloud** : monitoring des authentifications, des consentements OAuth, des activités admin (baseline + anomalies).
- **Threat hunting proactif** : équipes dédiées ou prestataires spécialisés qui recherchent activement les pré-positionnements silencieux.
- **Collaboration CERT nationale + sectoriel + international** : le modèle Ukraine est une référence.
- **Préparation à la réponse** : exercices sur les scénarios de pré-positionnement détecté, avec le dilemme éradication/surveillance.

**Cadre réglementaire** : **NIS 2** (entrée en application 2024) impose aux entités essentielles européennes des obligations de cybersécurité renforcées incluant la gestion des menaces étatiques. L’**EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence. Cadre à consolider dans les années à venir.

#### 22.9 Fil rouge — BLACKOUT Épisode 5

> **⚡ BLACKOUT — Épisode 5 : pré-positionnement confirmé**
> 
> Après plusieurs semaines d’investigation, le CERT consolide l’analyse : **BLACKOUT est un cas de pré-positionnement**. Les éléments convergents :
> 
> **Absence d’exfiltration** : l’analyse des flux réseau sortants sur les 42 jours de présence documentée de l’attaquant ne révèle aucune exfiltration massive. Quelques dizaines de mégaoctets transférés, compatibles avec de la reconnaissance interne ou du maintien d’accès, pas avec une extraction de propriété intellectuelle ou de données sensibles.
> 
> **Absence d’action destructive** : aucune modification des automates détectée, aucune tentative d’interaction avec les SIS, aucun wiper déposé, aucun ransomware.
> 
> **Maintenance de l’accès** : l’attaquant a créé **trois mécanismes de persistence indépendants** sur le poste d’ingénierie OT (DLL sideloading initial, tâche planifiée, service modifié). Ce n’est pas une tentative ponctuelle — c’est une présence conçue pour durer.
> 
> **Reconnaissance du processus industriel** : l’analyse des logs révèle que l’attaquant a consulté pendant plusieurs jours les documentations techniques du SCADA, les schémas électriques, les procédures opérationnelles. Il comprenait le processus avant de s’engager plus loin.
> 
> **Positionnement stratégique** : le poste d’ingénierie OT compromis a un accès direct à 12 postes de transformation haute tension desservant environ 400 000 foyers. Un attaquant activant cet accès pourrait, théoriquement, provoquer un blackout d’envergure.
> 
> **Diagnostic CERT** : **BLACKOUT est un pré-positionnement OT** avec capacité potentielle de sabotage. L’acteur est soit Sandworm (Russie, contexte ukrainien), soit un cluster chinois (Volt Typhoon ou similaire, pré-positionnement stratégique), soit un cluster non identifié. L’analyse des TTP et le contexte géopolitique orientent vers une probabilité supérieure pour **H1 Sandworm**, mais **l’incertitude demeure** et sera traitée formellement dans la matrice ACH au Ch.24.
> 
> **Décision opérationnelle** : après concertation entre l’opérateur, le CERT, et l’ANSSI (l’opérateur étant OIV), **option A — éradication** est choisie. Raisons :
> 
> - Risque opérationnel non acceptable de laisser le pré-positionnement actif (potentiel d’activation si escalade géopolitique).
> - Contexte européen actuel tendu (conflit ukrainien, tensions énergétiques).
> - Capacité à déployer une équipe dédiée pour l’éradication complète et simultanée de tous les accès.
> 
> L’éradication est planifiée pour les prochains jours. Le Ch.32 documente comment elle s’est déroulée et quelles leçons ont été tirées.

-----

### Chapitre 23 — Protection des infrastructures critiques

#### 23.1 Cartographie des infrastructures critiques européennes

Les **infrastructures critiques** (IC) sont les infrastructures dont la disruption aurait des conséquences majeures pour la sécurité, la santé publique, l’économie, ou la continuité des fonctions essentielles de l’État. La définition juridique précise dépend de la juridiction.

**En France** — cadre **OIV** (Opérateurs d’Importance Vitale) : défini par le Code de la défense (articles L.1332-1 et suivants). Les OIV sont désignés par l’État dans **12 secteurs d’activité d’importance vitale** (SAIV) — alimentation, communications électroniques/audiovisuel, eau, énergie, espace, finances, industrie, santé, transport, auxiliaires de l’État, services judiciaires, activités économiques et sociales de l’État. Les OIV ont des obligations de sécurité, notifient les incidents, et peuvent faire l’objet de contrôles ANSSI. Environ 300 OIV en France.

**En Europe — NIS 2** (Directive 2022/2555) : successeur de la directive NIS 1 (2016). Entrée en vigueur en octobre 2024, transposition en cours dans les États membres. Élargit considérablement le périmètre : **entités essentielles** (EE) et **entités importantes** (EI) dans 18 secteurs (énergie, transport, banque, santé, fourniture d’eau, infrastructures numériques, administration publique, espace, services postaux, gestion des déchets, fabrication/distribution de produits chimiques, production/transformation/distribution de denrées alimentaires, fabrication, fournisseurs numériques, recherche). Plusieurs dizaines de milliers d’entités couvertes à l’échelle européenne. Obligations : mesures techniques et organisationnelles, notification d’incidents, gouvernance cybersécurité au niveau direction, évaluations de risques de la supply chain.

**Aux États-Unis** — 16 **Critical Infrastructure Sectors** définis par la **Presidential Policy Directive 21** (PPD-21, 2013) : chemical, commercial facilities, communications, critical manufacturing, dams, defense industrial base, emergency services, energy, financial services, food and agriculture, government facilities, healthcare and public health, information technology, nuclear reactors/materials/waste, transportation systems, water and wastewater systems. CISA coordonne la protection.

**Autres juridictions** : l’**UK** a ses **Critical National Infrastructure** (13 secteurs), l’**Allemagne** ses **KRITIS**, le **Japon** et la **Corée du Sud** ont des cadres équivalents.

Point commun : les infrastructures critiques sont **définies par secteur** et sont soumises à des obligations de cybersécurité **renforcées**.

#### 23.2 La visibilité minimum viable en OT

Pour un opérateur d’infrastructure critique, la visibilité est le prérequis de toute défense. Les sources minimales.

**Sur le segment IT (niveaux 4-5 Purdue)** :

- Sysmon sur les endpoints et serveurs critiques.
- PowerShell ScriptBlock logging.
- Authentification AD (sécurité events).
- DNS (requêtes sortantes, réponses).
- Firewall et proxy (flux sortants).
- EDR déployé sur les endpoints et les serveurs (y compris les servers de production IT).
- Email gateway (pour détecter le phishing).
- Identity / cloud (Azure AD/Entra, applications OAuth, anomalies d’authentification).

**Sur la DMZ industrielle (entre niveaux 3-4)** :

- Logs des firewalls DMZ.
- Trafic autorisé / bloqué.
- Logs des serveurs de jump host si présents.

**Sur le segment OT (niveaux 1-3 Purdue)** :

- **Passive monitoring OT** (Claroty, Dragos, Nozomi, Microsoft Defender for IoT) connecté via mirror ports ou network taps aux segments OT.
- Logs des engineering workstations (Sysmon + PowerShell logging quand l’OS le permet).
- Logs des HMI et historian (quand ils existent et sont accessibles).
- **Audit trails sur les PLC récents** (les PLC modernes permettent de logger les modifications de configuration).

**Centralisation** : l’ensemble devrait remonter vers un **SIEM centralisé** qui corrèle les signaux IT et OT. Les SOC matures ont des **cas d’usage spécifiques OT** dans leur detection engineering.

#### 23.3 Segmentation IT/OT

La **segmentation** reste le pilier central de la sécurité OT. Principes.

**Segmentation physique** : idéalement, le réseau OT est physiquement séparé du réseau IT — pas de câbles partagés, pas de switches communs. En pratique, la segmentation physique totale est rare ; la **segmentation logique via VLANs et firewalls** est la norme.

**DMZ industrielle** : zone tampon entre IT et OT qui implémente des contrôles stricts :

- Pas de trafic direct IT → OT ni OT → IT.
- Tous les flux transitent par des **proxies applicatifs** ou des **serveurs de rebond** placés dans la DMZ.
- Les serveurs DMZ sont durcis (pas d’outils admin inutiles, monitoring poussé).
- Authentification forte sur tous les accès DMZ.

**Diodes unidirectionnelles** : pour les flux les plus sensibles (typiquement historian → IT pour le reporting), des **data diodes** (hardware qui physiquement ne laisse passer le trafic que dans un sens) garantissent l’unidirectionnalité. Utilisées notamment dans les centrales nucléaires.

**Micro-segmentation au sein de l’OT** : au-delà de la segmentation IT/OT, segmenter aussi les sous-ensembles OT — les SIS doivent être isolés des autres segments OT. Les sous-stations électriques entre elles peuvent être segmentées.

**Jump hosts durcis** : les postes qui sont forcément double-connectés (engineering workstations, postes de supervision) doivent être **durcis au maximum** — EDR, MFA, monitoring renforcé, séparation des sessions IT et OT (utilisateurs différents pour chaque environnement, pas de copier-coller entre les deux).

#### 23.4 Détection comportementale OT

La détection OT ne peut pas reposer sur des signatures de malware comme en IT. Elle repose sur la **détection comportementale**.

**Établissement de baselines** :

- Quels équipements communiquent avec quels autres équipements ? (graphe de communication normal).
- Quels protocoles sont utilisés sur quels liens ? (Modbus sur tel segment, IEC 104 sur tel autre).
- Quelles commandes sont typiquement envoyées ? (lecture de registres normale, écriture de configuration exceptionnelle).
- Quelles sont les plages horaires d’activité normale ?

**Détection d’anomalies** :

- Nouveau flux entre équipements qui ne communiquaient pas auparavant.
- Nouveau protocole observé (IEC 104 sur un segment qui n’en utilisait pas).
- Commandes d’écriture vers des registres critiques (modifications de configuration PLC) — devraient être rares et correspondre à des plans de maintenance documentés.
- Activité en dehors des plages horaires.
- Équipement inconnu détecté sur le réseau.

**Détection des TTP documentées** : les vendors OT (Claroty, Dragos, Nozomi) embarquent des détections pour les TTP documentées — patterns d’Industroyer, de Triton, de Stuxnet, des campagnes Sandworm récentes. Ces détections doivent être activées et maintenues à jour.

**Threat hunting OT** : recherche proactive d’indicateurs subtils (modifications mineures de configurations PLC, présence d’outils d’administration inhabituels sur les engineering workstations, patterns de beaconing discret). Ressources dédiées nécessaires.

#### 23.5 Collaboration avec les agences nationales

Les opérateurs d’infrastructures critiques sont rarement isolés face aux menaces APT. La collaboration avec les agences nationales est un pilier.

**Agences par pays** :

- **France — ANSSI** : qualifie les prestataires (PASSI, PDIS, PRIS), publie des advisories (CERT-FR), conduit des investigations, accompagne les OIV.
- **Allemagne — BSI** (Bundesamt für Sicherheit in der Informationstechnik) : rôle équivalent.
- **Royaume-Uni — NCSC** : Active Cyber Defence, Early Warning, Cyber Essentials.
- **Pays-Bas — NCSC-NL**.
- **Italie — ACN** (Agenzia per la Cybersicurezza Nazionale).
- **États-Unis — CISA** : advisories, KEV, Secure by Design, ShieldsUp.

**Types de collaboration** :

- **Partage de renseignement** : l’agence transmet des IoC, des TTP, des alertes sur des acteurs pertinents pour le secteur.
- **Support à l’investigation** : en cas d’incident majeur, l’agence peut déployer des experts.
- **Validation des dispositifs** : les qualifications (PASSI, PDIS, SecNumCloud en France) permettent aux opérateurs de faire confiance à des prestataires validés.
- **Exercices nationaux** : les agences conduisent des exercices (Piranet en France, CyberStorm aux US) qui testent les OIV dans des scénarios réalistes.

**Notification d’incidents** : NIS 2 impose des notifications sous 24h (early warning) et 72h (notification détaillée) pour les incidents significatifs. Ces notifications alimentent la vue d’ensemble nationale et permettent la coordination sur des campagnes qui touchent plusieurs acteurs.

#### 23.6 ISAC sectoriels

Les **ISAC** (Information Sharing and Analysis Centers) sont des structures de partage d’information **par secteur**. Complètent les CERT nationaux avec un focus métier.

**ISAC européens et internationaux** :

- **E-ISAC** (Electricity ISAC, North America) : secteur électrique.
- **EE-ISAC** (European Energy ISAC) : énergie européenne.
- **FS-ISAC** (Financial Services ISAC) : finance, global.
- **H-ISAC** (Health ISAC) : santé.
- **IT-ISAC** : IT et télécom.
- **ICT-ISAC** : ICT européen.
- **Auto-ISAC** : automobile.
- **Aviation ISAC**, **Maritime ISAC**, etc.

**En France** : **InterCERT France** (coordonne les CERT privés), **CLUSIF**, et plusieurs groupements sectoriels.

**Utilité** : partage rapide d’IoC et de TTP entre acteurs du même secteur, benchmarking des pratiques, exercices sectoriels, dialogue avec les autorités. Un opérateur qui voit une TTP inhabituelle peut la partager avec ses pairs du secteur et découvrir que cinq autres ont vu la même — ce qui change l’interprétation (attaque sectorielle ciblée plutôt qu’incident isolé).

**Règles de partage** : utilisation du **TLP** (Traffic Light Protocol) pour calibrer la diffusion (RED, AMBER, GREEN, CLEAR). Anonymisation des victimes quand nécessaire.

#### 23.7 Exercices cyber-OT

Les exercices sont la méthode principale pour **tester la résilience réelle**, pas seulement la résilience sur le papier.

**Niveaux d’exercice** :

- **Tabletop** : scénario discuté autour d’une table, pas d’action technique. Teste la coordination, les procédures, les décisions. Format typique : 2-4 heures, facilité par un animateur, implique les niveaux techniques et direction.
- **Fonctionnel / simulation** : plus approfondi, peut inclure des actions sur des environnements de test. Teste les capacités techniques et organisationnelles.
- **Full-scale / live** : exercice sur les vrais systèmes (en environnement contrôlé), avec injection réelle de scenarios. Teste la détection et la réponse sous conditions opérationnelles.

**Exercices nationaux / européens** :

- **Cyber Europe** (ENISA, tous les 2 ans) : exercice paneuropéen sur des scénarios cyber majeurs.
- **Piranet** (France, ANSSI) : exercice national de crise cyber.
- **CyberStorm** (US, CISA) : équivalent américain.
- **Locked Shields** (CCDCOE OTAN, Tallinn) : exercice technique de red/blue team au niveau OTAN.

**Scénarios OT spécifiques** : un bon exercice OT couvre :

- Le pivot IT → OT et sa détection.
- Le dilemme éradication vs surveillance d’un pré-positionnement.
- L’activation pendant un exercice (attaquant qui tente de manipuler un PLC).
- La communication de crise externe (public, autorités, média).
- La coordination avec les agences et les ISAC.

**Fréquence recommandée** : tabletop annuel, exercice fonctionnel biennal, full-scale tous les 3-5 ans — adapté à la maturité et aux moyens de l’organisation.

#### 23.8 Le rôle du RSSI face au pré-positionnement

Pour le **RSSI** (Responsable de la Sécurité des Systèmes d’Information) d’une infrastructure critique, le pré-positionnement change la nature de la mission. Quelques principes opérationnels.

**Communiquer la menace auprès de la direction** : le pré-positionnement est abstrait pour un dirigeant non-cyber. Il faut traduire — « un adversaire étatique peut, à un moment choisi, provoquer un blackout de X jours touchant Y clients, avec Z millions d’euros de pertes opérationnelles + perte de confiance + risque humain ». Le langage de l’impact métier est indispensable.

**Prioriser les investissements** : dans un contexte de ressources limitées, prioriser ce qui compte pour le pré-positionnement :

- **Visibilité IT et OT** : condition nécessaire pour détecter.
- **Durcissement des jump hosts et engineering workstations** : vecteur de pivot principal.
- **Segmentation IT/OT robuste** : limite la surface.
- **Monitoring identity cloud** : vecteur moderne critique.
- **Capacité d’investigation et d’éradication rapide** : soit en interne, soit via un retainer externe.

**Préparer la réponse** : exercices réguliers, plan IR formalisé, procédures de notification, contacts établis avec ANSSI/BSI/etc, retainer IR, relations avec les vendors CTI.

**Intégrer la menace dans la gestion des risques** : la probabilité d’un pré-positionnement par un acteur étatique doit être intégrée dans les évaluations de risque, pas seulement le risque ransomware ou le risque data breach.

**Accepter l’incertitude** : face à des acteurs comme Volt Typhoon ou Sandworm, le RSSI doit accepter qu’il ne sera jamais totalement invulnérable. L’objectif réaliste : rendre la détection rapide et l’éradication efficace, pas viser l’invulnérabilité.

**Collaborer activement** : échanger avec l’ISAC sectoriel, participer aux exercices nationaux, contribuer à la sensibilisation communautaire. La sécurité des infrastructures critiques est un **bien commun** — un incident qui touche un opérateur peut affecter tous les autres via le partage d’information.

-----

## PARTIE VII — GÉOPOLITIQUE, ATTRIBUTION ET PROSPECTIVE

> **Ce que cette partie apprend.** Maîtriser la méthodologie d’attribution (niveaux, évidences, pièges), cartographier l’écosystème cyber offensif mondial, comprendre les enjeux stratégiques de la dissuasion cyber et de la responsabilité étatique, identifier les tendances structurelles 2024-2026, et construire une défense adaptée aux APT.
> 
> **Ce qu’elle ne couvre pas.** Le détail réglementaire juridique par juridiction (Annexe G), la conduite opérationnelle d’un SOC (cours SOC dédié), les outils techniques d’investigation (Ch.3, cours IR et Forensics).
> 
> **Ce que vous saurez faire après cette partie.** Conduire une matrice ACH sur un incident, évaluer la solidité d’une attribution publique, anticiper les évolutions de la menace à 12-24 mois, et structurer une défense APT-ready pour une organisation.

-----

### Chapitre 24 — Attribution : méthodes, limites et enjeux

#### 24.1 Les trois niveaux d’attribution

L’**attribution** d’une cyberopération signifie différentes choses selon le niveau d’analyse. La confusion entre ces niveaux est la première source d’erreur analytique.

**Niveau 1 — Attribution technique** : relier une activité observée à un **intrusion set** identifié (APT29, Sandworm, Volt Typhoon, etc.). Fondée sur les TTP, l’infrastructure, le malware, la victimologie. Seuil de preuve : cohérence du faisceau technique avec un profil documenté. C’est l’attribution la plus accessible et la plus couramment produite par les vendors CTI.

**Niveau 2 — Attribution opérationnelle** : relier l’intrusion set à un **service ou une unité spécifique** (SVR russe, MSS Tianjin chinois, Lazarus/RGB nord-coréen, MOIS iranien). Nécessite des évidences supplémentaires — renseignement sur l’organisation sponsor, patterns d’horaires, artefacts linguistiques. Seuil de preuve : lien démontré entre l’intrusion set et une organisation spécifique.

**Niveau 3 — Attribution stratégique** : relier l’opération à un **État et une intention politique**. Qui a commandité ? Dans quel but stratégique ? Quels objectifs géopolitiques servis ? Seuil de preuve : compréhension contextuelle et renseignement non-technique (HUMINT, SIGINT stratégique, contexte diplomatique).

Les trois niveaux ont des **seuils de preuve croissants** et des **implications différentes**. Une attribution technique (« c’est APT29 ») est différente d’une attribution stratégique (« opération du SVR commanditée dans le cadre de la collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine »).

Les attributions publiques gouvernementales (indictments DOJ, advisories Five Eyes) atteignent souvent les trois niveaux. Les rapports CTI privés s’arrêtent souvent au niveau 1-2, laissant les considérations stratégiques en termes plus prudents.

#### 24.2 Les évidences d’attribution

Plusieurs catégories d’évidences construisent l’attribution. Leur **convergence** renforce la confiance, leur divergence l’affaiblit.

**TTP / tradecraft** : la manière dont l’attaquant opère. Patterns de reconnaissance, choix de vecteurs, outils utilisés, techniques de persistence, de mouvement latéral, d’exfiltration. Les TTP sont plus durables que les IoC (Pyramide de la Douleur), et un tradecraft mature est une signature forte.

**Infrastructure** : domaines, IP, certificats, serveurs C2, patterns d’enregistrement. Un même attaquant réutilise souvent des patterns d’infrastructure (même registrar, même hébergeur, même structure de sous-domaines) — erreur d’OPSEC fréquente même chez les acteurs sophistiqués.

**Malware** : familles de malware, signatures techniques du code, patterns de développement (commentaires, noms de variables, structure), artefacts de compilation (paths PDB, fuseau horaire de la machine de compilation, langue du système).

**Victimologie** : qui est ciblé ? Si une campagne cible exclusivement des entreprises de semiconducteurs dans l’UE et les US, le profil des cibles est un signal — la Chine a un intérêt documenté, la Russie moins, la DPRK encore moins. La victimologie aligne sur les priorités stratégiques connues.

**Timing géopolitique** : l’attaque coïncide-t-elle avec un événement politique ? Une tentative d’ingérence électorale avant un scrutin, une campagne contre des institutions ukrainiennes lors d’une escalade militaire, un ciblage énergétique en hiver — le timing renforce certaines hypothèses.

**Renseignement HUMINT / SIGINT** : accessible seulement aux services étatiques. Les attributions publiques gouvernementales peuvent s’appuyer sur ce renseignement (sans le révéler). Les vendors privés n’y ont pas accès, d’où la différence de nature entre attribution publique gouvernementale et rapport CTI privé.

**Erreurs opérationnelles** : artefacts qui trahissent l’origine. Langue maternelle dans les commentaires de code, fuseau horaire de la machine de compilation, réutilisation d’infrastructure déjà attribuée, horaires de travail compatibles avec un fuseau horaire donné.

**Lien avec des indictments antérieurs** : si des opérateurs nommément identifiés par un indictment antérieur réapparaissent (mêmes emails, mêmes identités), l’attribution devient extrêmement solide.

#### 24.3 Les pièges classiques de l’attribution

Plusieurs pièges classiques doivent être systématiquement écartés.

**False flags** : un attaquant plante délibérément des indices qui pointent vers un autre acteur. **Olympic Destroyer (2018)** est le cas d’école : Sandworm a inclus des fragments de code Lazarus documenté (DPRK), des infrastructures évoquant les APT chinoises, et des artefacts linguistiques trompeurs. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et consolidé l’attribution Sandworm. Leçon : un faisceau d’évidences apparemment convergent peut être fabriqué.

**Piggybacking sur une autre APT** : **Turla** a utilisé l’infrastructure d’APT34 (OilRig, Iran) pour ses propres opérations. Une victime qui voit une intrusion en provenance d’infrastructure connue comme iranienne peut être trompée sur l’origine réelle.

**Outils partagés** : **Cobalt Strike** est utilisé par presque tous les acteurs offensifs (APT étatiques, red teams légitimes, groupes ransomware). La seule présence de Cobalt Strike ne discrimine rien. Les infrastructures Let’s Encrypt, les VPS génériques, les services cloud légitimes sont utilisés par tous.

**Infrastructure louée / partagée** : les VPS sont loués, les domaines enregistrés via des registrars communs. Une IP qui a hébergé une opération APT29 il y a deux ans peut héberger aujourd’hui un site e-commerce légitime ou une opération totalement distincte.

**Biais géopolitiques** : attribuer à la Russie « par défaut » parce que le contexte le rend plausible est une erreur méthodologique. La discipline ACH exige de tester **plusieurs hypothèses** contre les mêmes évidences.

**Biais de confirmation** : une fois une hypothèse formulée tôt, l’investigateur tend à chercher des preuves qui la confirment et à ignorer celles qui la contredisent. Parade : formuler explicitement l’hypothèse, puis **chercher activement** les évidences qui l’invalideraient.

**Effet de signature reconnue** : reconnaître un pattern connu produit une sensation de certitude (« c’est Volt Typhoon, je le sens »). Cette intuition est utile mais doit être formalisée et testée contre les alternatives.

#### 24.4 Les niveaux de confiance et le vocabulaire calibré

L’attribution ne produit jamais de certitudes absolues. La communication analytique utilise un **vocabulaire calibré** — les **Words of Estimative Probability** (WEP), hérités de la tradition analytique CIA et adoptés par les services occidentaux et les vendors CTI sérieux.

|Expression                                   |Probabilité|
|---------------------------------------------|-----------|
|Almost certain / Quasi-certain               |>95 %      |
|Very likely / Très probable                  |80-95 %    |
|Likely / Probable                            |55-80 %    |
|Roughly even chance / Indéterminé            |45-55 %    |
|Unlikely / Improbable                        |20-45 %    |
|Very unlikely / Très improbable              |5-20 %     |
|Almost certainly not / Quasi-certainement non|<5 %       |

**Usage** : une attribution publique doit situer son niveau de confiance. « Attribution à APT29 avec haute confiance » signifie quelque chose de précis. « Attribution à APT29 » sans qualification laisse l’interprétation ouverte et est moins rigoureux.

**Évolution de la confiance** : la confiance peut évoluer avec de nouvelles évidences. Une attribution à confiance modérée au jour J peut devenir attribution à haute confiance au jour J+30, ou rester à confiance modérée indéfiniment.

**Règles de communication** :

- Jamais « certain » sans qualification.
- Préciser le **niveau** d’attribution (technique, opérationnelle, stratégique).
- Documenter les **évidences majeures**.
- Mentionner les **hypothèses alternatives considérées et écartées**.
- Identifier les **indicateurs de révision** — ce qui, si trouvé, remettrait en question l’attribution.

#### 24.5 L’attribution publique par les gouvernements

Les attributions publiques gouvernementales ont un statut particulier. Elles conjuguent renseignement technique, SIGINT/HUMINT classifié, et considérations diplomatiques.

**Formats** :

- **Advisories conjoints** (NSA/CISA/FBI + Five Eyes + alliés) : ton technique, IoC partagés, TTP détaillées.
- **Indictments DOJ** : mise en accusation formelle avec détails opérationnels publiés. Effet de naming and shaming.
- **Sanctions (OFAC, UE, UK)** : désignation de personnes et entités, interdiction de transactions. Effet financier et symbolique.
- **Déclarations officielles** : communiqués diplomatiques, déclarations aux parlements, auditions publiques.
- **Rapports gouvernementaux** : rapports annuels des agences (ANSSI Panorama de la cybermenace, NCSC Annual Review, CISA reports).

**Pourquoi publier** : naming and shaming, coordination internationale, dissuasion, armement des défenseurs, appui aux sanctions.

**Pourquoi ne pas publier** : protection des sources et méthodes, considérations diplomatiques, incertitude insuffisante, valeur continue de la surveillance (révéler un pré-positionnement détecté peut compromettre la capacité de le surveiller).

L’attribution publique est un **acte politique** autant que technique.

#### 24.6 Les attributions privées : vendors CTI

Les vendors CTI privés produisent massivement des attributions — avec forces et limites distinctes des attributions publiques gouvernementales.

**Forces** :

- **Visibilité privée massive** : Microsoft voit les signaux sur des milliards d’endpoints et tenants O365, CrowdStrike sur des millions d’endpoints EDR, Mandiant sur des milliers d’incidents IR par an.
- **Agilité de publication** : rapports techniques en quelques semaines, vs plusieurs mois pour les attributions gouvernementales.
- **Détail technique** : IoC, TTP, samples de malware, timeline. Les attributions gouvernementales sont souvent plus synthétiques.

**Limites** :

- **Pas d’accès au renseignement classifié** : HUMINT, SIGINT non-cyber. L’attribution stratégique (niveau 3) est plus difficile.
- **Risques commerciaux** : un vendor qui attribue à un État peut subir des conséquences (perte de clients, contentieux). Incite à la prudence.
- **Qualité variable** : Mandiant, CrowdStrike, Microsoft, Kaspersky, ESET, Unit 42 (Palo Alto), Recorded Future, Sekoia ont une réputation établie. D’autres vendors produisent des rapports moins fiables.

**Règle pratique** : croiser les attributions privées de plusieurs vendors sérieux. Si Mandiant, CrowdStrike et Microsoft concordent, la fiabilité est élevée.

#### 24.7 Fil rouge — BLACKOUT Épisode 6

> **⚡ BLACKOUT — Épisode 6 : la matrice ACH complète**
> 
> Le CERT consolide l’attribution via une matrice ACH formelle. Les quatre hypothèses testées :
> 
> - **H1** : Sandworm (GRU Unit 74455) — pré-positionnement dans le contexte du conflit ukrainien.
> - **H2** : cluster chinois (Volt Typhoon ou similaire) — pré-positionnement stratégique.
> - **H3** : nouveau cluster étatique non attribué — acteur émergent, intention indéterminée.
> - **H4** : acteur non-étatique sophistiqué — cybercriminel de haut niveau.
> 
> **Matrice ACH (extrait)** :
> 
> |Évidence                                 |H1 Sandworm|H2 Chine |H3 Nouveau|H4 Non-étatique|
> |-----------------------------------------|:---------:|:-------:|:--------:|:-------------:|
> |Exploitation Ivanti CVE-2024-21887       |C          |**C**    |C         |C              |
> |LotL dominant, peu de malware custom     |I partiel  |**C**    |C         |C              |
> |DLL sideloading sur app de supervision   |C          |**C**    |C         |N              |
> |Beaconing HTTPS régulier                 |C          |I        |C         |C              |
> |Pas de malware custom Sandworm identifié |**I**      |C        |C         |C              |
> |Ciblage OT énergie                       |**C**      |C        |C         |I              |
> |Patience opérationnelle (42j sans action)|C          |**C**    |C         |I              |
> |Contexte géopolitique (conflit ukrainien)|**C**      |I partiel|C         |N              |
> |Absence totale de monétisation           |C          |C        |C         |**I**          |
> |Pas d’exfiltration massive               |C          |C        |C         |I              |
> |Sophistication technique observée        |C          |C        |C         |I              |
> 
> **Lecture** : C = cohérent ; I = incohérent ; I partiel = partiellement incohérent ; N = non applicable.
> 
> **Comptage des incohérences** :
> 
> - H1 Sandworm : 1 incohérence forte (pas de malware custom), 1 partielle (LotL atypique).
> - H2 Chine : 1 incohérence (beaconing régulier atypique Volt Typhoon), 1 partielle (contexte géopolitique).
> - H3 Nouveau cluster : 0 incohérence — mais hypothèse peu contrainte par défaut.
> - H4 Non-étatique : 4 incohérences fortes — **éliminée**.
> 
> **Conclusion d’attribution** :
> 
> - **H4 éliminée** : caractéristiques incompatibles avec un acteur non-étatique.
> - **H1 plausible** : confiance modérée. TTP, contexte, ciblage énergie s’alignent. Point faible : absence de malware custom Sandworm.
> - **H2 plausible** : confiance faible à modérée. TTP LotL s’alignent fortement, mais contexte géopolitique et beaconing régulier sont des décalages.
> - **H3 plausible** : ne peut être écartée. Confiance faible.
> 
> **Attribution provisoire** : « Pré-positionnement OT par acteur étatique — très probable (>80%). Attribution la plus probable : **Sandworm/GRU avec confiance modérée**. Hypothèse alternative Chine avec confiance faible à modérée. Hypothèse alternative cluster non identifié non écartée. »
> 
> **Indicateurs de révision identifiés** :
> 
> - Si un outil custom Sandworm est identifié → H1 renforcée.
> - Si un pattern d’infrastructure chinois documenté (routeurs SOHO compromis, C2 via IP résidentielles) est trouvé → H2 renforcée.
> - Si 2+ opérateurs européens confirment des TTP identiques via ISAC → probabilité d’attribution accrue par victimologie élargie.
> 
> Le CERT transmet le dossier à l’ANSSI pour coordination nationale et aux partenaires européens.

-----

### Chapitre 25 — L’écosystème cyber offensif mondial

#### 25.1 Panorama quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement. Ordres de grandeur (2026) :

- **MITRE ATT&CK Groups** : ~160 groupes documentés publiquement.
- **Malpedia** (Fraunhofer FKIE) : plusieurs centaines de familles de malware attribuées.
- **CrowdStrike** : 230+ acteurs nommés suivis.
- **Mandiant** : 300+ intrusion sets dans son périmètre interne.
- **Microsoft Threat Intelligence** : 150+ threat actors nommés publiquement.

Ces chiffres croissent chaque année. La concentration d’activité reste sur un noyau restreint d’acteurs de premier plan — la **loi de Pareto** s’applique largement : 20% des groupes produisent 80% de l’activité documentée.

#### 25.2 La prolifération des capacités

La **prolifération des capacités cyber offensives** est la tendance structurelle la plus préoccupante. Plusieurs dynamiques y contribuent.

**Frameworks C2 accessibles** :

- **Cobalt Strike** : outil commercial de pentest, largement « cracké ». Utilisé par la grande majorité des APT et groupes ransomware depuis 2018-2020.
- **Brute Ratel C4** : concurrent commercial, également cracké.
- **Sliver** (BishopFox, open source) : framework C2 open source, massivement adopté.
- **Havoc** (open source) : framework récent en progression.
- **Mythic** (open source) : plateforme C2 modulaire.
- **Metasploit** : pentest framework classique.

Ces outils fournissent des capacités sophistiquées à des acteurs qui n’auraient pas les ressources pour les développer. Les TTP autrefois signature d’APT étatique deviennent accessibles à des acteurs moindres.

**Marché de la surveillance privée (PSO)** : NSO, Intellexa, Candiru, Paragon — traités au Ch.15 et Ch.18. Des **dizaines d’États** peuvent désormais **acheter** ces capacités auprès de fournisseurs commerciaux.

**Vulnerability brokers** : marchés légaux (Zerodium, Crowdfense) et gris. Prix d’un 0-day iOS full chain : plusieurs millions de dollars. Permettent à des acteurs de niveau intermédiaire d’acquérir des capacités.

**Leaks d’outils étatiques** :

- **Shadow Brokers** (2016-2017) : outils NSA (EternalBlue utilisé dans WannaCry/NotPetya, DoublePulsar).
- **Vault 7** (2017) : outils CIA via WikiLeaks.
- **Leak i-Soon** (février 2024) : écosystème contractor chinois.
- **ContiLeaks** (2022) : opérations internes d’un groupe ransomware majeur.

Ces leaks arment des acteurs moindres avec des capacités étatiques.

**Initial Access Brokers (IAB)** : vendent des accès obtenus sur des forums dark web. Un acteur qui ne sait pas compromettre peut acheter un accès pour quelques centaines ou milliers de dollars. Fragmentation de la chaîne d’attaque.

**IA offensive** : usage de LLM et d’IA générative pour améliorer le phishing, générer du code, détecter des vulnérabilités, amplifier les campagnes d’influence. Impact croissant (voir Ch.27).

#### 25.3 Le modèle contractor comme industrie offensive

Le modèle des **contractors civils** mandatés pour des opérations cyber étatiques est une dimension structurelle de l’écosystème contemporain.

**Chine — i-Soon et ses pairs** : le leak i-Soon (Ch.8) a documenté un écosystème vaste. D’autres contractors chinois existent. Entreprise privée qui vend des services cyber (outils, opérations, surveillance) à des clients étatiques multiples (MSS, PLA, polices provinciales).

**Russie — écosystème flou entre services et prestataires** : moins formalisé qu’en Chine, mais plusieurs entités sont à la frontière (KillNet, NoName057(16) côté russe, avec niveaux de coordination variables avec les services).

**Israël — secteur commercial structurellement lié à l’appareil de défense** : pipeline Unité 8200 → startups → surveillance commerciale (Ch.18). NSO, Intellexa, Candiru, Paragon régulés par le ministère israélien de la Défense.

**Occident — contractors de défense classiques étendus au cyber** : Raytheon, Lockheed Martin, BAE Systems, Thales, Airbus et d’autres ont des divisions cyber. Opèrent généralement dans des cadres juridiques plus formalisés (marchés publics, supervision parlementaire).

**États émergents** : plusieurs pays développent des capacités via acquisition de services privés (achat de spywares commerciaux), recrutement d’opérateurs formés ailleurs, coopération avec des contractors étrangers. Le seuil d’entrée pour un État désireux d’acquérir des capacités cyber est plus bas qu’il y a 10 ans.

**Implications analytiques** : l’attribution devient plus difficile quand plusieurs contractors travaillent pour un même client ou qu’un contractor travaille pour plusieurs clients. Les frontières « opération étatique » / « opération commerciale au service de l’État » s’estompent.

#### 25.4 Lecture comparative des doctrines par bloc

Synthèse doctrinale consolidée.

|Acteur                        |Doctrine centrale                |Tradecraft                            |Sophistication     |Tolérance au bruit|
|------------------------------|---------------------------------|--------------------------------------|-------------------|------------------|
|**Russie — SVR/APT29**        |Espionnage stratégique, furtivité|Supply chain, abus cloud, OAuth       |Très élevée        |Très faible       |
|**Russie — GRU/Sandworm**     |Sabotage, destructif ouvert      |Wipers, OT custom                     |Élevée             |Élevée            |
|**Russie — GRU/APT28**        |Espionnage militaire + influence |Spear-phishing, exploits              |Élevée             |Moyenne-élevée    |
|**Russie — FSB/Turla**        |Espionnage long terme            |Rootkits, piggybacking                |Exceptionnelle     |Très faible       |
|**Chine — MSS**               |Espionnage massif, patience      |Supply chain, LotL, volume            |Élevée, croissante |Faible            |
|**Chine — Volt Typhoon**      |Pré-positionnement               |LotL exclusif, SOHO botnet            |Très élevée        |Extrême-faible    |
|**DPRK — Lazarus/RGB**        |Financement régime               |Cybervol, social engineering          |Élevée, pragmatique|Moyenne           |
|**Iran — MOIS**               |Espionnage régional              |Webshells, DNS tunneling              |Moyenne-élevée     |Moyenne           |
|**Iran — IRGC (APT35)**       |Surveillance ciblée              |Social engineering extrême            |Élevée (SE)        |Faible            |
|**Iran — Agrius**             |Destructif représailles          |Wipers, fausses bannières             |Moyenne            |Moyenne-élevée    |
|**US — USCYBERCOM/NSA**       |Defend forward                   |Spectre large, capacités avancées     |Très élevée        |Variable          |
|**UK — NCF/GCHQ**             |Disruption by design             |Ciblage précis, coordination Five Eyes|Très élevée        |Faible            |
|**Israël — Unité 8200/Mossad**|Préemption                       |Ciblage précis, HUMINT intégré        |Très élevée        |Variable          |

#### 25.5 L’écosystème comme instrument diplomatique

Les cyberopérations sont **intégrées dans la diplomatie** des États.

**Le cyber comme signal** : une cyberopération peut signaler une position politique (Shamoon comme représailles iraniennes pour Stuxnet, Sandworm comme démonstration de capacité hybride russe, Volt Typhoon comme dissuasion chinoise liée à Taïwan). Comprendre le signal est aussi important que comprendre l’effet technique.

**Le cyber comme monnaie d’échange** : les attributions, sanctions, indictments peuvent être levés ou maintenus selon l’évolution des relations. L’accord Xi-Obama 2015 sur l’espionnage économique chinois a produit un effet temporaire observable dans la baisse des opérations APT chinoises contre les entreprises US pendant quelques années.

**Le cyber comme test de résolution** : les acteurs testent la volonté des défenseurs de répondre. Une escalade cyber qui ne provoque pas de réponse significative encourage de nouvelles escalades. Une réponse ferme peut décourager.

**Le cyber comme déstabilisation en deçà du seuil du conflit armé** : la zone grise permet des opérations qui, dans le monde physique, appelleraient une réponse militaire — mais qui restent « tolérées » au cyber. Cette asymétrie favorise les États agresseurs.

Pour l’analyste, ces dimensions diplomatiques et stratégiques sont indissociables du technique. Un rapport CTI qui se limite aux IoC et aux TTP, sans considération du contexte diplomatique, donne une vision incomplète.

-----

### Chapitre 26 — Dissuasion, normes et responsabilité étatique

> **Note sur ce chapitre.** Ce chapitre traite les **enjeux stratégiques et analytiques** du droit international appliqué au cyber, des normes négociées, et de la responsabilité étatique. Le **détail réglementaire** (textes, articles, agences par juridiction) est consolidé dans l’**Annexe G**. L’objectif ici est de saisir les enjeux, pas de cataloguer les textes.

#### 26.1 Peut-on dissuader dans le cyberespace ?

La **dissuasion** est un concept stratégique hérité du nucléaire : convaincre l’adversaire que les coûts d’une action dépasseraient les bénéfices. Son application au cyber fait l’objet de débats intenses.

**Difficultés structurelles de la dissuasion cyber**.

**L’attribution est lente et imparfaite** : la dissuasion nucléaire repose sur une certitude d’attribution (un missile vient de tel pays). En cyber, l’attribution prend des semaines à des années, avec des niveaux de confiance variables. Un adversaire peut agir sans savoir exactement si et quand il sera attribué.

**La gradation des représailles est difficile** : dans le nucléaire, la doctrine de la « mutuelle destruction assurée » était claire. En cyber, quels seuils déclenchent quelle réponse ? Une cyberattaque sur une centrale peut-elle justifier une riposte conventionnelle ? Une réponse cyber équivalente ? Une sanction économique ? Les doctrines varient et sont souvent volontairement ambiguës.

**Le déni plausible** : beaucoup de cyberopérations sont conduites de manière à offrir un déni plausible au sponsor. La tolérance tacite du cybercrime russophone, l’usage de contractors chinois, les fausses bannières iraniennes — autant de techniques qui diluent la responsabilité étatique.

**L’asymétrie** : un État comme la DPRK, sans infrastructure vulnérable équivalente, n’est pas dissuadable par la menace de représailles cyber — il n’a rien à perdre en cyber. Sa motivation (financer le régime) reste suffisante malgré sanctions diplomatiques.

**Le seuil bas** : contrairement au nucléaire où le coût initial est extrême, le cyber est quotidien. La dissuasion efficace suppose que chaque action soit individuellement coûteuse — difficile à calibrer quand le volume d’opérations est élevé.

**Éléments de dissuasion qui semblent fonctionner (au moins partiellement)** :

**Capacité démontrée de détection et d’attribution** : les advisories Five Eyes, les indictments DOJ, les rapports CTI publics démontrent que les opérations seront découvertes. Cette démonstration impose un coût réputationnel.

**Sanctions cumulées** : les sanctions OFAC et UE, accumulées dans le temps, produisent un coût financier réel sur les individus et entités ciblés.

**Démantèlements d’infrastructure** : les opérations Medusa (Snake), KV Botnet (Volt Typhoon), Raptor Train (Flax Typhoon), LockBit (Cronos) imposent un coût opérationnel — remplacer une infrastructure démantelée demande du temps et des ressources.

**Coordination alliée** : l’attribution coordonnée Five Eyes + alliés crée un coût diplomatique plus élevé qu’une attribution isolée.

**Bilan** : la dissuasion cyber est **partielle**. Elle n’empêche pas les opérations, mais elle en augmente le coût et peut modérer les ambitions les plus destructives. Les grandes puissances cyber n’ont jamais franchi publiquement certains seuils (pas de cyber-attaques destructives sur les infrastructures critiques US par la Chine, pas de cyber-attaques destructives sur les infrastructures critiques russes par les US) — ce qui suggère une forme de dissuasion fonctionnelle sur les seuils les plus élevés.

#### 26.2 Droit international appliqué au cyber : débats fondamentaux

Le droit international n’a pas été conçu pour le cyberespace. Son application fait l’objet de débats qui reflètent des visions stratégiques divergentes.

**Principes applicables (consensus large)** :

- **Souveraineté** : un État ne peut pas mener d’opérations dans le territoire (y compris les réseaux) d’un autre État sans son consentement.
- **Non-intervention** : un État ne peut pas intervenir dans les affaires intérieures d’un autre État.
- **Proportionnalité** : les réponses doivent être proportionnées à l’agression.
- **Interdiction du recours à la force** (article 2.4 Charte ONU) : quelle est la frontière entre « cyberopération » et « recours à la force » ?

**Le processus de Tallinn** (Manuel 1.0 en 2013, 2.0 en 2017) : travail d’un groupe d’experts coordonné par le **CCDCOE OTAN** (Tallinn). Propose une interprétation du droit international appliqué au cyber. **Non contraignant juridiquement** mais référence académique majeure. Position dominante : le droit international s’applique au cyberespace, les États sont responsables des opérations qu’ils conduisent ou tolèrent.

**Négociations ONU — GGE et OEWG** : depuis 2004, l’ONU négocie des normes de comportement responsable. Le **GGE** (expert restreint) a produit des rapports consensuels (2013, 2015). L’**OEWG** (tous États membres) est plus divisif politiquement.

**Positions divergentes structurantes** :

- **Bloc occidental** (US, UE, Five Eyes, Japon, Corée du Sud) : les normes existantes s’appliquent au cyber sans nouveau traité. Focus sur l’**application** et les **comportements responsables**. Défense de la liberté d’Internet et du **multistakeholderisme** (gouvernements + secteur privé + société civile + communauté technique).
- **Bloc Russie-Chine** : un nouveau traité international est nécessaire. Concept de « **sécurité de l’information** » qui inclut non seulement la cybersécurité au sens technique mais aussi le **contrôle du contenu** — contrôle de l’Internet, restriction de l’information jugée déstabilisatrice. Défense du **multilatéralisme onusien** strict (gouvernements seuls).

Ces positions reflètent des **visions incompatibles** de la gouvernance numérique. Le conflit n’est pas purement technique ou juridique — il est fondamentalement politique. La perspective d’un traité universel contraignant sur le cyber reste éloignée.

#### 26.3 Attributions publiques et sanctions : la logique stratégique

Les attributions publiques gouvernementales et les sanctions associées constituent l’instrument principal de réponse des démocraties occidentales aux cybermenaces étatiques. Leur logique stratégique mérite d’être analysée.

**La logique de naming and shaming** : rendre publique l’attribution impose un coût réputationnel à l’État commanditaire. Ce coût est d’autant plus élevé que l’attribution est coordonnée internationalement (Five Eyes + alliés) et argumentée techniquement.

**La logique de signalement** : une attribution publique signale la **capacité de détection** de la victime. Message implicite : « nous vous voyons, vos opérations ne sont pas invisibles ». Cet effet peut décourager certaines opérations futures par le simple fait de la démonstration.

**La logique du coût cumulé** : les sanctions OFAC, les Entity List, les indictments DOJ n’empêchent pas individuellement une opération, mais leur **accumulation dans le temps** produit un coût réel. Un opérateur nommément identifié par un indictment ne peut plus voyager dans la plupart des pays, ses avoirs peuvent être gelés, son identité est publique.

**La logique de l’alliance** : les attributions coordonnées entre alliés (Five Eyes, UE, OTAN) renforcent la cohérence des démocraties face aux menaces étatiques. Elles traduisent une solidarité stratégique au-delà de la simple déclaration.

**Les limites** :

- **Pas d’effet sur les agresseurs déterminés** : la DPRK continue de voler, la Russie continue ses opérations, la Chine maintient son pré-positionnement. Les sanctions imposent un coût sans changer fondamentalement les incitations.
- **Asymétrie démocratique** : les démocraties attribuent publiquement ; les autocraties rarement. Cette asymétrie favorise les démocraties dans le récit public mais n’équilibre pas nécessairement les rapports de force opérationnels.
- **Risque de dévaluation** : si les attributions publiques deviennent trop fréquentes, leur poids individuel diminue. La discipline consiste à attribuer publiquement avec parcimonie, pour les cas les plus significatifs.

#### 26.4 Responsabilité étatique dans le cyberespace

La question de la **responsabilité étatique** — à quoi un État est-il tenu, pour quelles actions de quels acteurs ? — est centrale.

**Le standard classique du droit international** : un État est responsable des actions qu’il conduit lui-même **et** des actions de tiers qu’il contrôle effectivement (« effective control »). Appliqué au cyber, cela signifie qu’un État est responsable :

- Des cyberopérations conduites par ses services étatiques directs.
- Des cyberopérations conduites par des contractors sous son contrôle.
- Possiblement des cyberopérations conduites par des acteurs qu’il tolère ou soutient sans s’opposer.

**Le seuil de l’effective control** : souvent difficile à démontrer. Un contractor chinois qui conduit une opération pour le MSS est-il sous effective control de l’État ? Un groupe ransomware russophone toléré par le FSB est-il sous effective control ? Les opérations de pré-positionnement attribuées à la Chine correspondent-elles à une décision politique de haut niveau ou à une initiative d’un bureau régional MSS ?

**Positions divergentes** :

- **Position occidentale** (tend à élargir la responsabilité) : un État est responsable non seulement de ce qu’il contrôle mais aussi de ce qu’il aurait pu et dû empêcher. La tolérance d’opérations depuis son territoire peut engager sa responsabilité.
- **Position russe/chinoise** (tend à restreindre) : seules les opérations prouvées comme directement conduites par l’État engagent sa responsabilité. Les acteurs non-étatiques, même tolérés, ne peuvent pas être imputés à l’État.

Ces divergences juridiques ont des implications pratiques : un ransomware russophone peut-il justifier une réponse étatique contre la Russie ? Un groupe cyber chinois sous forte présomption MSS peut-il justifier des sanctions contre des officiels chinois ?

**L’évolution des pratiques** : les attributions publiques occidentales récentes (indictments, sanctions) désignent de plus en plus les **institutions étatiques** et les **officiels nommément identifiés**, pas seulement les opérateurs techniques. Cette tendance élargit la responsabilité étatique dans la pratique, indépendamment des débats juridiques théoriques.

#### 26.5 L’OTAN et le seuil de l’article 5

L’**OTAN** a reconnu le cyberespace comme **5ème domaine d’opérations** au sommet de Varsovie (2016). Cette reconnaissance a des implications majeures pour la dissuasion.

**Principe** : le **Treaty de Washington (1949), Article 5** stipule qu’une attaque armée contre un membre de l’OTAN est considérée comme une attaque contre tous. La reconnaissance du cyber comme 5ème domaine signifie qu’**une cyberattaque significative peut en théorie déclencher l’article 5**.

**En pratique, le seuil n’a jamais été formellement défini**. L’OTAN a annoncé que le cas serait évalué au cas par cas. Plusieurs conséquences :

**Ambiguïté stratégique** : le seuil non-défini est **délibéré**. L’ambiguïté maintient l’incertitude chez l’adversaire — il ne sait pas ce qui déclenchera l’article 5, ce qui l’incite à la prudence.

**Cas de test non-déclenchés** : NotPetya (2017), qui a causé des dommages massifs à des pays membres (Royaume-Uni notamment), n’a pas déclenché l’article 5. SolarWinds (2020) non plus. Le ciblage OT en Ukraine n’a pas impliqué l’article 5 (l’Ukraine n’est pas membre OTAN).

**Concept de « seuil d’attaque armée cyber »** : débattu dans les travaux OTAN et académiques. Éléments généralement considérés : **mort ou blessure humaine**, **destruction physique massive**, **impact économique à l’échelle d’une attaque cinétique**, **atteinte à la souveraineté**. Un blackout de plusieurs jours affectant des millions de personnes pourrait potentiellement atteindre ce seuil. Une exfiltration de documents classifiés, aussi significative soit-elle, ne l’atteindrait probablement pas.

**Pratique récente** : l’OTAN a développé des capacités de défense cyber collective (NATO Cyber Operations Centre, **CCDCOE** à Tallinn pour la doctrine, **exercices Locked Shields**). Une structure mature, sans pour autant s’engager mécaniquement dans la dissuasion automatique.

#### 26.6 Le cadre français : doctrine LIO/LID/L2I

La France a publiquement formalisé sa **doctrine cyber** en 2019 via la revue stratégique de cyberdéfense, structurée autour de trois piliers.

**LID** — **Lutte Informatique Défensive** : la protection et la défense des systèmes d’information de l’État et des OIV. Conduite principalement par l’**ANSSI**.

**LIO** — **Lutte Informatique Offensive** : la conduite d’opérations cyber offensives pour le compte de l’État. Conduite principalement par le **COMCYBER** (Commandement de la cyberdéfense, ministère des Armées). La France s’est réservé le droit de mener des opérations offensives en réponse à une agression. La doctrine publique mentionne l’encadrement par l’autorité politique et le respect du droit international et humanitaire.

**L2I** — **Lutte Informatique d’Influence** : la contre-ingérence dans l’espace informationnel, face aux opérations de désinformation étatiques. Ce volet, plus récent, reflète la prise de conscience de la dimension informationnelle des conflits contemporains.

Le détail institutionnel (structures ANSSI, COMCYBER, DGSE, DGSI, C4) et réglementaire (OIV, NIS 2 en France) est consolidé dans l’**Annexe G**. Ce qui importe ici est la **cohérence doctrinale** : la France a explicitement assumé un spectre complet de capacités cyber (défensives, offensives, informationnelles), avec une articulation avec l’appareil de sécurité nationale globale.

#### 26.7 Le cadre européen : NIS 2, Cyber Solidarity Act, ENISA

Au niveau européen, la cybersécurité s’est massivement structurée ces dernières années. Synthèse stratégique (détail en Annexe G).

**ENISA** (European Union Agency for Cybersecurity) : coordination cybersécurité entre États membres, publication de rapports (Threat Landscape annuel), exercices (Cyber Europe).

**NIS 2** (Directive 2022/2555, entrée en application 2024) : extension massive du périmètre par rapport à NIS 1. Environnement **essentiel/important** dans 18 secteurs. Obligations renforcées : mesures techniques et organisationnelles, notification d’incidents, gouvernance cybersécurité au niveau direction, évaluations de risques de la supply chain, sanctions administratives pouvant atteindre 10 M€ ou 2% du chiffre d’affaires mondial.

**EU Cyber Solidarity Act** (2024) : création d’un réseau européen de **SOC** (Security Operations Centers) pour partager la détection et la réponse, mécanisme de **réserve cyber** européenne activable en crise.

**Cyber Resilience Act** (adoption 2024) : obligations de cybersécurité pour les produits connectés (IoT, logiciels), responsabilité des fabricants.

**EU Cyber Sanctions Regime** (depuis 2019) : cadre permettant des sanctions ciblées (gel des avoirs, interdictions de voyager) contre des personnes et entités impliquées dans des cyberattaques.

#### 26.8 Responsabilité des États sur les opérations de leurs alliés ou proxies

Une question émergente : la responsabilité des États pour les opérations conduites par leurs alliés ou proxies.

**Cas concrets** :

- **Volontaires internationaux IT Army of Ukraine** : conduits sous coordination étatique ukrainienne publique. Quelle responsabilité ukrainienne pour des actes illégaux commis par des volontaires depuis des pays tiers ? Question juridique ouverte.
- **Hacktivistes pro-russes (KillNet, NoName057)** : ciblés par des sanctions UE en 2023-2024. La Russie est-elle responsable des actes d’hacktivistes qu’elle tolère et probablement soutient ? Le débat rejoint celui de la responsabilité étatique classique.
- **Opérations offensives conduites avec l’aide d’alliés** : USCYBERCOM hunt forward en Ukraine. Les opérations américaines conduites sur le sol ukrainien engagent-elles la responsabilité américaine, ukrainienne, ou les deux ?

**Tendance émergente** : les démocraties occidentales cherchent à **formaliser** le cadre d’emploi des capacités cyber pour clarifier les responsabilités. L’ambiguïté stratégique a des avantages (flexibilité) mais aussi des coûts (imprévisibilité, risque d’escalade non désirée).

#### 26.9 Pall Mall Process et régulation des PSO

Le **Pall Mall Process** est l’initiative internationale de régulation des capacités cyber offensives commerciales (spywares, outils offensifs). Lancé à Londres en février 2024, conjointement par le Royaume-Uni et la France.

**Objectif** : établir un cadre international pour la régulation du marché des **PSO** (Private Sector Offensive Actors) — NSO, Intellexa, Candiru, Paragon et leurs concurrents. Préoccupation centrale : l’usage abusif de ces outils contre des journalistes, dissidents, opposants politiques, défenseurs des droits humains.

**Signataires** : plus de 40 États à la déclaration initiale de Londres (février 2024), rejoints par d’autres lors des rounds ultérieurs. Entreprises cosignataires incluent Apple, Google, Meta, Microsoft. ONG de droits humains également partie prenante.

**Principes affirmés** :

- Usage des capacités cyber commerciales dans le respect du droit international et des droits humains.
- Responsabilité des États sur les usages de ces capacités qu’ils acquièrent.
- Transparence relative sur les acquisitions étatiques.
- Sanctions contre les entreprises documentées pour des usages abusifs.

**Limites** : initiative non-contraignante juridiquement. Plusieurs États majeurs (notamment des clients majeurs de NSO et ses pairs) ne sont pas signataires. Effet dépend de la mise en œuvre nationale et de la coordination internationale.

**Importance stratégique** : malgré ses limites, le Pall Mall Process est un premier jalon international sur un marché qui a opéré jusque-là sans régulation globale. Son développement dans les années à venir sera un indicateur de la capacité de la communauté internationale à gouverner cet espace.

-----

### Chapitre 27 — Tendances 2024-2026 et signaux d’anticipation

#### 27.1 Exploitation massive des appliances edge

La tendance n°1 du paysage cyber contemporain : l’**exploitation des appliances edge exposées sur Internet**. VPN, firewalls, passerelles mail, appliances de sécurité elles-mêmes sont devenues le vecteur d’entrée privilégié des APT sophistiquées.

**Vagues notables 2023-2026** :

- **Ivanti Connect Secure** : CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 exploitées par plusieurs acteurs (Volt Typhoon, APT40, APT31, clusters non identifiés). Vague massive début 2024.
- **Fortinet FortiOS** : multiples CVE 2022-2024 exploitées par APT40 et autres.
- **Citrix ADC/NetScaler** : CVE-2023-4966 (« Citrix Bleed »), CVE-2023-3519 exploitées par APT29, APT40, acteurs ransomware.
- **Barracuda Email Security Gateway** : CVE-2023-2868 exploitée par UNC4841 (Chine) pendant 8 mois avant découverte.
- **Palo Alto GlobalProtect** : CVE-2024-3400 exploitée mi-2024.
- **Cisco IOS XE** : CVE-2023-20198 exploitation massive fin 2023.

**Pourquoi cette concentration** :

- **Pas d’EDR sur les appliances** : les appliances réseau ne peuvent pas faire tourner d’agents de détection endpoint. La visibilité est limitée aux logs (parfois insuffisants).
- **Exposition Internet par construction** : une VPN gateway doit être accessible depuis Internet, donc exposée aux scans massifs des attaquants.
- **Credentials privilégiés en aval** : compromettre une appliance de sécurité donne souvent un accès privilégié au réseau interne (VPN → accès réseau, firewall → capacité de manipulation des flux, passerelle mail → accès aux communications).
- **Patching complexe** : les appliances sont souvent en production continue, leur patching est planifié et parfois retardé.
- **Vulnérabilités nombreuses** : les appliances de sécurité ont des vulnérabilités comme les autres logiciels — le paradoxe consiste à ce que les outils de défense deviennent des vecteurs d’attaque.

**Défense** : surveillance renforcée des appliances (logs exhaustifs, SIEM intégré), patching d’urgence (suivre KEV CISA), durcissement des configurations (désactiver les composants non-nécessaires), monitoring réseau entourant les appliances.

#### 27.2 Ciblage de l’identité cloud

L’**identité cloud** est devenue le nouveau périmètre. Les APT ciblent massivement Azure AD/Entra ID, les tokens SAML/OAuth, les mécanismes MFA.

**Tactiques dominantes** :

- **Password spraying sur Azure AD** : volume massif, taux de succès faible par tentative mais cumul efficace. APT33 (Iran) et APT29 (Russie) en font un usage systématique.
- **Abus OAuth** : création d’applications OAuth malveillantes ou détournement d’applications existantes avec des permissions Graph API excessives. Accès persistant sans mot de passe, contourne la MFA. Signature APT29.
- **Vol de tokens (pass-the-cookie, pass-the-token)** : réutilisation de sessions authentifiées volées via infostealers ou AitM phishing. Contourne la MFA.
- **AitM phishing avec Evilginx et équivalents** : proxy malveillant qui intercepte les credentials ET les cookies de session. Contourne la MFA. Utilisé massivement par acteurs étatiques et cybercriminels.
- **GoldenSAML** : forgeage de tokens SAML via compromission d’ADFS. Technique pivot de SolarWinds, toujours utilisée.
- **MFA fatigue** : bombardement de notifications push pour inciter la victime à en accepter une par lassitude. Technique de base mais efficace.
- **Compromission de comptes de service** : les comptes de service (applications, systèmes) ont souvent des permissions larges et des mécanismes d’authentification plus faibles (clés API, secrets partagés).

**Vulnérabilité structurelle** : une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints. La remédiation nécessite de révoquer les tokens, recréer les applications OAuth, auditer les permissions, changer les secrets — opérations complexes et souvent incomplètes.

**Défense** :

- **MFA résistant au phishing** : FIDO2 / WebAuthn / clés hardware (YubiKey). Ne tombe pas à l’AitM.
- **Conditional Access** : règles basées sur le contexte (device, location, risk signals).
- **Monitoring OAuth et consents** : détecter les applications OAuth avec consent admin, les permissions Graph API excessives, les anomalies d’authentification.
- **Privileged Identity Management (PIM)** : activation just-in-time des rôles privilégiés, pas de standing admin.
- **Identity threat detection** : outils dédiés (Microsoft Defender for Identity, CrowdStrike Identity Threat Protection, Okta ITDR).

#### 27.3 Convergence crime-État

La **convergence entre cybercrime et action étatique** est une tendance structurelle déjà largement évoquée dans les parties précédentes.

**Manifestations principales** :

- **APT41** (Chine) : double mission espionnage/cybercrime personnel assumée.
- **Ransomware russophone sous tolérance tacite** : LockBit, BlackBasta, Play, Royal, ALPHV, Cl0p.
- **DPRK/Lazarus** : méthode criminelle (cybervol crypto), finalité étatique (financement régime).
- **Infostealers et IAB** : cybercriminels qui fournissent involontairement des accès aux APT étatiques via la revente sur marchés dark web.
- **Hacktivisme instrumentalisé** : KillNet, NoName057(16), IT Army of Ukraine.

**Implications** :

- **Attribution plus complexe** : face à une compromission, distinguer si l’acteur est purement criminel, purement étatique, ou entre les deux est souvent difficile.
- **Réponse adaptée** : les mesures qui fonctionnent contre le cybercrime (démantèlements d’infrastructure, sanctions économiques) sont moins efficaces contre les APT étatiques. Les mesures diplomatiques qui fonctionnent contre les APT sont sans effet sur les cybercriminels. La zone grise nécessite des approches mixtes.
- **Tendance à la professionnalisation** : le cybercrime devient plus sophistiqué sous l’influence des TTP étatiques ; les APT empruntent les techniques criminelles (infostealers, IAB) pour l’efficacité.

**Trajectoire 2024-2026** : la convergence va probablement s’approfondir. Les distinctions « pur crime » vs « pur État » deviendront de moins en moins nettes.

#### 27.4 LotL comme standard

Le **Living off the Land** est passé d’une technique avancée à un **standard** des APT sophistiquées.

**Volt Typhoon** a démontré qu’une opération étatique sophistiquée de pré-positionnement peut être conduite **sans aucun malware custom**. Son modèle se diffuse : de plus en plus d’acteurs adoptent des approches LotL-heavy pour maximiser la furtivité.

**Implications pour la défense** :

- Les signatures EDR classiques (hash de fichiers, strings de malware) détectent moins.
- La détection doit être **comportementale** : patterns d’usage des LOLBins, contextes d’exécution, chaînes de processus.
- Les baselines comportementales deviennent cruciales — identifier qu’un `ntdsutil` exécuté par un compte admin depuis un serveur non-DC est anormal nécessite de savoir ce qui est normal.
- Le **threat hunting proactif** prend de l’importance sur la détection automatique passive.

**Outils défensifs adaptés** : EDR modernes qui surveillent les **chaînes de processus** et les **patterns comportementaux** (Microsoft Defender for Endpoint, CrowdStrike Falcon, SentinelOne, Carbon Black, Palo Alto Cortex XDR) plutôt que les signatures seules. SIEM avec règles de détection comportementales.

#### 27.5 IA offensive : phishing, deepfakes, aide au développement

L’**IA générative** (LLM et génération multimédia) entre dans l’arsenal offensif. Impact croissant, encore émergent.

**Phishing amélioré par LLM** : les emails de phishing sont rédigés dans un langage natif et contextuel parfait, sans les erreurs linguistiques caractéristiques des campagnes non-natives. L’avantage historique des anglophones sur les campagnes de phishing ciblant les entreprises anglophones (vs attaquants non-anglophones avec erreurs) est en train de disparaître. APT iraniens, chinois, russes produisent désormais des emails de phishing indiscernables linguistiquement de correspondants légitimes.

**Deepfakes vocaux** : impersonation vocale de dirigeants pour des attaques BEC (Business Email Compromise) au téléphone. Cas documentés : un employé finance convaincu par téléphone que le CFO lui demande un virement urgent, pour découvrir plus tard qu’il s’agissait d’une voix synthétique. Les deepfakes audio sont techniquement plus accessibles que les deepfakes vidéo et leur utilisation criminelle s’industrialise.

**Deepfakes vidéo** : cas documentés en Asie (vidéoconférences truquées où plusieurs participants étaient des deepfakes d’employés légitimes, aboutissant à des transferts frauduleux de dizaines de millions). Technique coûteuse mais accessible aux acteurs sophistiqués.

**Aide au développement de malware** : les LLM peuvent aider à générer du code offensif — scripts d’exploitation, évasions EDR, obfuscations. Les garde-fous des LLM commerciaux (OpenAI, Anthropic, Google) filtrent beaucoup de demandes manifestement malveillantes, mais les LLM open source ou partiellement contournés offrent moins de résistance. Impact : accélération du développement par les acteurs sophistiqués, accessibilité accrue pour les acteurs moyens.

**Reconnaissance et profilage assistés** : LLM utilisés pour agréger des données OSINT sur des cibles, identifier des vulnérabilités humaines (points d’approche social engineering), générer des leurres personnalisés.

**État actuel (2026)** : l’IA offensive augmente la **productivité** des attaquants mais n’a pas encore produit de rupture capacitaire qualitative. Les opérations restent conduites par des humains avec outillage IA, pas entièrement automatisées. La trajectoire à moyen terme (2027-2030) est incertaine — l’automatisation croissante des attaques via agents IA est une menace anticipée mais pas encore massivement observée.

#### 27.6 Pré-positionnement dans les infras critiques : la menace structurelle

Le **pré-positionnement** (Ch.22) est probablement **la menace structurelle qui définira la prochaine décennie**. Plusieurs dynamiques l’amplifient :

**Volt Typhoon comme modèle** : démontre qu’un pré-positionnement prolongé sans détection est possible. Ce modèle va être répliqué par d’autres acteurs.

**Extension géographique** : au-delà des US, l’Europe est désormais une cible crédible de pré-positionnement (par la Russie et la Chine). L’Asie-Pacifique également (par la Chine).

**Dilemmes de réponse non résolus** : éradiquer vs surveiller, communiquer publiquement vs rester discret — ces dilemmes restent non tranchés systématiquement. Chaque cas fait l’objet de décisions ad hoc.

**Manque de maturité défensive** : beaucoup d’opérateurs d’infrastructures critiques n’ont toujours pas les moyens (visibilité OT, threat hunting, collaboration) pour détecter un pré-positionnement sophistiqué. La maturité nécessite des années à construire.

**Tensions géopolitiques** : Taïwan, Ukraine, Moyen-Orient, rivalités économiques. Les tensions croissantes augmentent la probabilité d’**activations** potentielles de pré-positionnements existants — ce qui augmente la gravité du problème.

#### 27.7 Ciblage des télécoms et interception

**Salt Typhoon** (2024) a démontré l’ampleur du ciblage télécom par des acteurs étatiques. Cette tendance va s’amplifier.

**Pourquoi les télécoms** :

- **Accès aux communications** : appels, SMS, métadonnées de millions d’utilisateurs.
- **Systèmes d’interception légale** : compromettre les systèmes CALEA permet de voir qui les autorités surveillent — contre-espionnage de haute valeur.
- **Position centrale** : les télécoms ont accès à tout le trafic de leurs clients — un point de collecte privilégié.
- **Compromission difficilement détectable** : les infrastructures télécoms sont complexes, avec beaucoup d’équipements hérités et de sous-traitance.

**Implications** :

- Les personnalités à haut risque (opposants politiques, journalistes, militants, dirigeants d’entreprise critique) doivent supposer que leurs communications **non chiffrées de bout en bout** peuvent être compromises.
- Le passage à Signal, WhatsApp, iMessage (messageries E2EE) est devenu une recommandation standard, y compris par les autorités US post-Salt Typhoon.
- La souveraineté télécom redevient un enjeu stratégique — dépendre d’opérateurs étrangers (notamment chinois dans certains pays) pose des questions sécuritaires nouvelles.

#### 27.8 Supply chain continues et éditeurs logiciels

Les **compromissions supply chain** restent un vecteur APT majeur. Tendances 2024-2026 :

**Ciblage des éditeurs logiciels tier 1** : Microsoft, SolarWinds, Kaseya, JetBrains ont été compromis dans des opérations majeures. La tendance ne faiblit pas — les éditeurs restent des cibles à très fort effet de levier.

**Cascades supply chain** (modèle 3CX) : compromission d’un éditeur via un autre éditeur compromis. Niveau d’imbrication qui complique l’attribution et la remédiation.

**Compromission de dépendances open source** : packages npm, PyPI, GitHub compromis pour injecter du malware dans les chaînes de build de multiples projets. Cas récents documentés en quantité croissante.

**Contractors et MSP** : les prestataires IT sont des cibles indirectes. Compromettre un MSP donne accès à ses clients (modèle Cloud Hopper d’APT10, toujours réplicable).

**Défense** :

- Zero Trust appliqué à la supply chain (ne pas faire confiance aux fournisseurs par défaut).
- Software Bill of Materials (SBOM) : obligations émergentes aux États-Unis (EO 14028) et en Europe (Cyber Resilience Act).
- Monitoring des processes fournisseurs (intégrité du build pipeline, signatures, reproductibilité).
- Évaluation de risques de la supply chain (obligation NIS 2).

#### 27.9 Signaux géopolitiques à surveiller

Les analystes cyber doivent suivre plusieurs signaux géopolitiques qui affectent le paysage de la menace.

**Tensions autour de Taïwan** : une escalade militaire dans le détroit de Taïwan activerait probablement des pré-positionnements chinois existants. Les indicateurs : augmentation des exercices militaires PLA, déclarations politiques, mouvements diplomatiques.

**Évolution de la guerre en Ukraine** : intensification ou désescalade affectera les opérations russes destructives et d’influence. Les cessations de conflit ne signifient pas la fin des opérations cyber — elles peuvent simplement changer de forme.

**Élections majeures** : élections présidentielles et législatives dans les grandes démocraties sont des cibles récurrentes d’ingérence étrangère. Les services CTI montent typiquement leur vigilance à l’approche des échéances électorales.

**Sanctions et escalade économique** : l’introduction de nouvelles sanctions peut déclencher des ripostes cyber (Iran contre l’Albanie en 2022 après hébergement du MEK — précédent).

**Crises énergétiques** : tensions sur l’approvisionnement énergétique (Europe post-2022, tensions Moyen-Orient) augmentent le ciblage des infrastructures énergétiques.

**Crises médicales ou sanitaires** : pandémies ou crises sanitaires majeures produisent des vagues de cyberattaques opportunistes + étatiques (ciblage santé COVID par APT russes et chinois en 2020).

Pour l’analyste, maintenir une **veille géopolitique** parallèle à la veille technique est essentiel. Les deux s’alimentent réciproquement.

-----

### Chapitre 28 — Construire une défense APT-ready

> **Note sur ce chapitre.** Ce chapitre synthétise les principes de défense spécifiques aux APT. Il ne reproduit pas un cours de SOC ou d’Incident Response — il se concentre sur ce qui distingue la défense contre les APT étatiques de la défense générale.

#### 28.1 Principes : assume breach, defense in depth, Zero Trust

La défense APT-ready repose sur trois principes structurants.

**Assume breach** : partir du principe que **l’adversaire est probablement déjà à l’intérieur**. Cette posture change tout — les efforts ne se limitent pas à empêcher l’entrée (prévention), mais s’étendent à la détection précoce, au containment rapide, à l’éradication efficace, et à la résilience.

La justification de l’« assume breach » : face à des acteurs comme Volt Typhoon (LotL exclusif, zéro malware), APT29 (abus cloud/identity sophistiqué), Turla (piggybacking, rootkits kernel), la prévention seule ne suffit pas. Les défenseurs doivent supposer que tôt ou tard, un acteur suffisamment motivé et ressourcé **entrera**. L’objectif devient alors de **limiter l’impact** et d’**écourter le dwell time**.

**Defense in depth** : multiples couches de défense indépendantes, de manière à ce qu’une défaillance à une couche soit compensée par les suivantes. Couches typiques : sécurité périmétrique, endpoint, identity, cloud/SaaS, réseau interne, applicatif, données, détection/réponse. Un attaquant qui franchit une couche doit en franchir d’autres avant d’atteindre les données critiques.

**Zero Trust** : ne pas faire confiance par défaut aux utilisateurs, appareils, ou applications, même à l’intérieur du périmètre. Chaque accès est authentifié, autorisé, et validé. Le concept a été formalisé par Forrester (John Kindervag, 2010) et adopté largement — **NIST SP 800-207** (Zero Trust Architecture, 2020) en donne un cadre de référence.

Application Zero Trust : MFA résistant au phishing pour tous les accès, conditional access basé sur le contexte, micro-segmentation réseau, verification continue plutôt que session persistante, principle of least privilege strict.

#### 28.2 Contrôles minimum viables

La défense APT-ready repose sur un ensemble de **contrôles minimum viables** — pratiques sans lesquelles tout le reste est compromis. Priorisation proposée.

**Priorité 0 — Prérequis absolus** :

- **MFA résistant au phishing** sur tous les comptes (FIDO2 / WebAuthn). Exclure TOTP SMS/appel (contournables par AitM).
- **Privileged Access Management (PAM)** : rotation des credentials privilégiés, sessions auditées, just-in-time pour les accès critiques.
- **EDR déployé partout** : endpoints et serveurs (incluant les serveurs de production). Les serveurs sans EDR sont les pivots préférés des attaquants.
- **Patching des edge devices en moins de 48h** sur les CVE exploitées activement (référence CISA KEV).

**Priorité 1 — Base solide** :

- **Segmentation réseau** : IT/OT, zones sensibles isolées, segmentation micro-services si possible.
- **Durcissement Active Directory** : tiering strict des comptes, limitation des privilèges, monitoring des changements critiques (groupes admin, GPO, trusts), protection KRBTGT.
- **Monitoring cloud / identity** : visibilité sur Azure AD/Entra, applications OAuth, sign-ins anormaux, changements de configuration.
- **Backup hors ligne testé** : backup offline (non joignable depuis le réseau), testé régulièrement par restore réel, couvrant systèmes et données critiques.
- **Plan IR formalisé et exercé** : playbooks documentés, équipe identifiée, retainer IR externe si besoin, exercices réguliers.

**Priorité 2 — Maturité** :

- **Threat hunting proactif** : équipe ou prestataire dédié, cycles réguliers, guidé par la CTI des acteurs pertinents.
- **Purple team** : exercices réguliers combinant red team (simulation TTP APT) et blue team (détection).
- **Intégration CTI** : ingestion de renseignement actionnable, corrélation avec la télémétrie.
- **Visibilité OT** (si applicable) : passive monitoring sur les segments industriels.
- **Gestion de la supply chain** : évaluation des prestataires, SBOM, monitoring des intégrations.

#### 28.3 Visibilité minimum viable

Sans visibilité, la détection est impossible. Les **sources de télémétrie** essentielles :

**Endpoints** :

- **Sysmon** : logs détaillés des process, connexions réseau, modifications de fichiers, chargements de DLL. Configuration de référence : Olaf Hartong Sysmon config (GitHub, open source, largement adopté).
- **PowerShell ScriptBlock logging** : tous les scripts PowerShell exécutés sont loggés.
- **EDR** : détections comportementales, télémétrie détaillée.
- **Windows Security events** : authentifications, changements de comptes, privilèges.

**Réseau** :

- **DNS** : résolutions sortantes, détection des domaines malveillants connus, détection des patterns (beaconing).
- **Firewall et proxy** : flux sortants, tentatives d’exfiltration, connexions vers infrastructure suspecte.
- **Flow data (NetFlow/IPFIX)** : vue agrégée des communications, détection d’anomalies volumétriques.
- **IDS/NDR** : détection d’intrusion réseau, analyse comportementale.

**Identity / Cloud** :

- **Azure AD / Entra sign-in logs** : qui se connecte, depuis où, avec quel contexte.
- **Audit logs** : changements de configuration, consents OAuth, rôles modifiés.
- **Application logs** : pour les SaaS critiques (M365, Google Workspace, Salesforce, etc.).

**Email** :

- **Email gateway logs** : messages reçus/envoyés, détections phishing, blocages.
- **Messagerie interne** : monitoring des messages à haut risque (pièces jointes, liens externes, thèmes sensibles).

**Sources OT** (si applicable) :

- **Passive monitoring OT** (Claroty, Dragos, Nozomi, Microsoft Defender for IoT).
- **Logs des engineering workstations**.
- **Logs des HMI, historian, SCADA applications**.

**Centralisation** : tout remonte vers un **SIEM** centralisé (Splunk, QRadar, Sentinel, Elastic, Chronicle, Exabeam) qui permet corrélation cross-sources. Sans SIEM, chaque source est un silo et les corrélations (signe d’une APT) sont invisibles.

#### 28.4 Détection TTP-driven vs IoC-driven

La détection moderne doit être **TTP-driven**, pas seulement IoC-driven.

**Détection IoC-driven (limitée)** : liste de hashes, IP, domaines connus comme malveillants. Facile à implémenter, efficace contre les malwares connus, **inefficace contre les APT** qui adaptent leurs IoC.

**Détection TTP-driven (recommandée)** : règles qui détectent les **comportements** plutôt que les signatures statiques. Exemples :

- « Un processus PowerShell exécuté par MS Word est suspect » (détecte les macros malveillantes).
- « Une connexion RDP sortante depuis un serveur vers une IP externe est suspecte ».
- « Un compte admin qui se connecte à un système où il ne s’est jamais connecté avant est suspect ».
- « Une connexion Azure AD depuis un pays où l’utilisateur ne travaille pas est suspecte ».

**Outils** :

- **Sigma rules** : format ouvert pour les règles de détection SIEM. Bibliothèque open source disponible.
- **Elastic detections, Splunk ES, Microsoft Sentinel analytics** : règles natives des SIEM.
- **ATT&CK mapping** : mapper les détections aux techniques MITRE ATT&CK pour visualiser la couverture.

**Detection engineering** : discipline de construction et maintenance des règles de détection. Cycle : hypothèse de TTP, développement de règle, test, déploiement, tuning par feedback terrain. Les équipes SOC matures ont des detection engineers dédiés.

#### 28.5 Le containment APT : scope avant contenir

Face à une APT détectée, la règle critique est : **scope avant de contenir**.

**Pourquoi** : une APT sophistiquée a des **accès redondants** (plusieurs mécanismes de persistence, comptes backdoor, plusieurs hosts compromis). Si on contient un seul accès (isoler une machine, désactiver un compte), l’attaquant **active immédiatement ses accès redondants** et disparaît — tout en étant alerté que la détection a eu lieu. Résultat : perte de visibilité, réinfection via TTP modifiées, dwell time rallongé.

**Méthode recommandée** :

1. **Détecter** une présence APT (un signe).
1. **Ne pas agir visiblement** — préserver l’invisibilité pour l’attaquant.
1. **Scope** : identifier tous les systèmes, comptes, et mécanismes compromis. Threat hunting actif guidé par les premières observations. Cette phase peut durer des jours à des semaines.
1. **Planifier le containment coordonné** : qui fait quoi, quand, dans quel ordre.
1. **Containment simultané** : désactivation de **tous** les accès en une fenêtre courte (idéalement quelques heures), **de manière coordonnée**. L’attaquant ne peut plus pivoter vers des accès redondants parce qu’ils sont tous coupés simultanément.
1. **Éradication** : nettoyage des mécanismes de persistence, reset des credentials, reconstruction des systèmes compromis.
1. **Monitoring renforcé post-éradication** : l’attaquant tentera probablement de revenir — détection des tentatives de réentrée.

**Outils** : EDR modernes permettent la réponse coordonnée (isolation réseau de multiple endpoints en une action, désactivation de comptes en masse). SOAR (Security Orchestration, Automation and Response) pour orchestrer les playbooks complexes.

**Retainer IR** : avoir un prestataire IR contractualisé en amont permet une réponse rapide sans négocier les termes pendant la crise. Retainers Mandiant, CrowdStrike, Kroll, Unit 42, Sophos, et équivalents européens sont la norme pour les grandes organisations.

#### 28.6 Purple team orienté APT

Le **purple team** combine red team (simulation d’attaque) et blue team (détection/réponse) en exercices collaboratifs. Appliqué aux APT, il vise à **valider** les détections face aux TTP des acteurs pertinents.

**Approche** :

- Identifier les acteurs pertinents pour l’organisation (sectoriels, géographiques).
- Cataloguer leurs TTP documentées (ATT&CK Groups, rapports CTI).
- Reproduire ces TTP dans un environnement contrôlé.
- Vérifier si le SOC détecte chaque TTP avec quelle latence.
- Identifier les gaps et les corriger (nouvelles règles de détection, nouvelles sources de télémétrie).

**Frameworks d’émulation** :

- **Atomic Red Team** (Red Canary, open source) : bibliothèque de tests atomiques mappés sur ATT&CK.
- **CALDERA** (MITRE) : plateforme d’émulation adversaire automatisée.
- **Red Canary AtomicTestHarnesses** : tests paramétrés.
- **Vectr** : plateforme de gestion des exercices purple team.
- **APT Emulation Plans** (MITRE CTID) : plans d’émulation d’acteurs spécifiques (APT29, FIN6, menuPass/APT10, Sandworm, Carbanak, Turla).

**Cadence recommandée** : exercices réguliers (trimestriels pour les grandes organisations), chaque exercice ciblant un acteur ou un ensemble de TTP spécifique.

**Bénéfices** :

- Validation empirique des détections (vs théorique).
- Formation des équipes blue sur les TTP réelles.
- Priorisation des investissements de détection sur les gaps identifiés.
- Documentation des capacités de détection pour la direction et les auditeurs.

#### 28.7 Exercices de simulation (tabletop et au-delà)

Les exercices testent la **réponse organisationnelle**, pas seulement les capacités techniques.

**Niveaux** :

- **Tabletop** : discussion autour d’un scénario. Durée 2-4h. Participants : CISO, SOC, IR, juridique, communication, direction. Teste la coordination, les décisions, les procédures.
- **Fonctionnel** : simulation plus approfondie avec actions techniques sur environnement de test.
- **Full-scale / live** : exercice sur systèmes réels (en environnement contrôlé) avec injection de scenarios réels.

**Scénarios APT recommandés** :

**Tabletop 1 — « APT29 a compromis votre Azure AD via phishing OAuth »**

- J0 : alerte sign-in suspect depuis un pays inhabituel sur un compte admin.
- J+1 : règle de forwarding inbox créée par le compte, redirigeant des emails vers externe.
- J+3 : exfiltration détectée de SharePoint via Graph API, ~500 Go de données.
- J+5 : découverte d’une application OAuth avec permissions admin et tokens SAML forgés via ADFS compromis.
- Questions clés : Quand escaladez-vous à la direction ? Qui informez-vous (clients, autorités, ANSSI) ? Contenez-vous immédiatement (risque perdre visibilité) ou scopez-vous d’abord ?

**Tabletop 2 — « Ransomware BlackBasta avec précurseur APT »**

- J0 : déploiement ransomware massif, des centaines d’endpoints chiffrés, note de rançon sur plusieurs serveurs.
- Investigation révèle que l’accès initial a été vendu par un Initial Access Broker qui l’avait obtenu 6 mois plus tôt via une compromission Citrix.
- L’IAB avait probablement aussi vendu l’accès à un acteur étatique qui l’a utilisé pour d’autres opérations (exfiltration de propriété intellectuelle) avant le déploiement ransomware.
- Questions clés : comment discriminer cybercrime vs APT dans la réponse ? Qui notifier (ANSSI pour les OIV, CNIL pour les données personnelles, parquet pour les infractions pénales) ? Comment gérer la communication externe ?

**Tabletop 3 — « Pré-positionnement OT détecté sans action destructive »**

- Le SOC détecte des TTP compatibles avec Volt Typhoon/Sandworm dans l’environnement OT.
- L’attaquant est présent depuis probablement 3+ mois, pas d’exfiltration visible, pas d’action destructive.
- Questions clés : éradiquez-vous immédiatement (risque de perdre le renseignement sur l’adversaire) ou surveillez-vous (risque de laisser une menace active) ? Qui prend cette décision ? Comment se coordonne-t-on avec l’ANSSI ? Comment communique-t-on (ou pas) publiquement ?

Ces tabletops révèlent régulièrement des gaps organisationnels : procédures d’escalade floues, absence de contacts établis avec les autorités, mauvais partage d’information interne, gaps de communication avec la direction.

#### 28.8 Le partage d’information : ISAC, CSIRT, coordination européenne

Le **partage d’information** est un pilier de la défense collective contre les APT.

**Niveaux de partage** :

- **Intra-organisation** : entre équipes (SOC, IR, threat intel, IT, métiers).
- **Sectoriel** : ISAC (Ch.23) — partage des IoC, TTP, tendances avec les pairs du même secteur.
- **National** : CERT national (CERT-FR, CERT-DE, NCSC, etc.), autorités (ANSSI, BSI).
- **International** : FIRST (Forum of Incident Response and Security Teams), coordination Five Eyes, UE.

**Règles de partage — TLP (Traffic Light Protocol)** :

- **TLP:RED** : strictement limité aux destinataires nommés.
- **TLP:AMBER** : limité à l’organisation et partenaires directs.
- **TLP:GREEN** : partage dans la communauté pertinente.
- **TLP:CLEAR** : public sans restriction.

**Outils de partage** :

- **MISP** (Malware Information Sharing Platform) : plateforme open source de partage d’indicateurs structurés.
- **STIX / TAXII** : formats standards pour le partage de threat intelligence.
- **ISAC portals** : chaque ISAC a ses mécanismes de partage.

**Bénéfice collectif** : un IoC partagé par un membre protège potentiellement tous les autres. L’inverse : ne pas partager par crainte d’exposer l’incident laisse les pairs vulnérables.

**Obligations légales** : NIS 2 impose des notifications aux autorités sous 24h (early warning) et 72h (détaillée) pour les incidents significatifs. RGPD impose la notification CNIL sous 72h pour les violations de données personnelles.

#### 28.9 Former les équipes : CTI-driven defense

La défense APT-ready n’existe pas sans équipes **formées et motivées**. Quelques principes.

**Recrutement et rétention** : les profils cyber sont rares et chers. La rétention dépend de facteurs non-salariaux (défis intéressants, formation continue, reconnaissance, culture d’équipe, flexibilité). Les RSSI qui traitent leurs équipes cyber comme un investissement stratégique retiennent mieux.

**Formation continue** : certifications (SANS, Offensive Security, ISC2, ISACA), conférences (Black Hat, DEF CON, SSTIC, FIC, Botconf, RSA), labs d’entraînement (Hack The Box, TryHackMe, RangeForce), lectures (rapports Mandiant, CrowdStrike, Microsoft, Dragos, blogs spécialisés).

**CTI-driven mindset** : comprendre les acteurs avant de défendre contre les acteurs. Les équipes qui lisent régulièrement la CTI (rapports publics, threat intel d’abonnement, partages ISAC) savent ce contre quoi elles défendent. Les équipes qui ne lisent que leur SIEM ne savent pas.

**Exercices et apprentissage continu** : les tabletops, purple teams, CTF internes entretiennent les compétences. Une équipe qui ne s’entraîne pas perd ses capacités.

**Culture d’apprentissage des incidents** : après chaque incident (réel ou simulé), **post-mortem blameless** — analyse des faits, identification des causes systémiques, actions correctives documentées. Les équipes qui cachent les erreurs apprennent moins que celles qui les exposent et corrigent.

**Relation avec la direction** : le CISO doit pouvoir parler métier, budget, et risque, pas seulement technique. La défense APT-ready exige des investissements que la direction doit comprendre et soutenir — d’où l’importance de traduire les menaces APT en langage d’impact business compréhensible par le non-technique.

-----

## PARTIE VIII — ÉTUDES DE CAS INTÉGRÉES

> **Ce que cette partie apprend.** Articuler l’ensemble des éléments du cours sur des cas complets réels. Chaque chapitre reconstitue un incident emblématique — acteur, contexte géopolitique, TTP, timeline, impact, attribution, réponse, leçons — dans une vue intégrée.
> 
> **Ce qu’elle ne couvre pas.** De nouveaux concepts ou acteurs — tout ce qui est mobilisé ici a été introduit dans les Parties I à VII. Les cas sont inspirés de faits documentés publiquement ; quelques détails techniques peuvent rester classifiés.
> 
> **Ce que vous saurez faire après cette partie.** Lire un incident complexe avec l’ensemble des grilles analytiques du cours, structurer un rapport d’incident APT, et synthétiser les leçons opérationnelles d’un cas complet.

-----

### Chapitre 29 — SolarWinds / SUNBURST : la supply chain comme vecteur d’espionnage

SolarWinds est le **cas d’école** de la compromission supply chain à très grande échelle menée par un acteur étatique sophistiqué. Il mérite un traitement détaillé — timeline, TTP, attribution, leçons.

#### 29.1 Contexte : APT29, SVR, paradigme supply chain

**Acteur** : APT29 / Cozy Bear / Midnight Blizzard — service de renseignement extérieur russe (SVR).

**Paradigme** : la supply chain logicielle comme vecteur d’espionnage stratégique massif. SolarWinds n’était pas la première compromission supply chain étatique — CCleaner (APT17/APT41, 2017), M.E.Doc (Sandworm, 2017 pour NotPetya) l’ont précédée — mais c’est la plus ambitieuse et sophistiquée documentée publiquement.

**Cible SolarWinds** : éditeur de logiciel de supervision réseau basé au Texas. Son produit phare **Orion** est utilisé par **~33 000 organisations** dans le monde, dont une large part du gouvernement fédéral américain, des entreprises Fortune 500, et des infrastructures critiques. C’est précisément cette base installée privilégiée qui en fait une cible APT idéale.

#### 29.2 Timeline détaillée

**Septembre-octobre 2019** : activité suspecte détectable rétrospectivement dans l’environnement de développement SolarWinds. Modifications de « test » dans le code Orion — vraisemblablement la phase de reconnaissance et de préparation de l’attaquant.

**Février 2020** : la backdoor **SUNBURST** est injectée pour la première fois dans un build opérationnel d’Orion. Le mécanisme d’injection ciblait spécifiquement le **processus de build** de SolarWinds — pas une compromission de développeur individuel, mais la compromission de l’infrastructure qui compile le code source en binaires signés.

**Mars 2020** : la mise à jour Orion trojanisée (versions 2019.4 HF5, 2020.2, 2020.2 HF1) est distribuée via les canaux officiels SolarWinds. Tous les clients qui mettent à jour (~18 000 organisations) reçoivent SUNBURST. Le malware est **signé avec le certificat légitime SolarWinds** — rien ne le distingue d’une mise à jour normale.

**Mars-juin 2020** : SUNBURST se propage lentement dans les environnements des victimes. Une fois exécuté, il **attend 12 à 14 jours** avant de s’activer — technique d’évasion pour échapper aux sandboxes automatisées qui analyseraient le fichier pendant quelques minutes seulement. Puis il contacte son serveur C2 (`avsvmcloud.com`, domaine au nom évocateur de services cloud/antivirus légitimes).

**Juillet-décembre 2020** : APT29 examine les signaux reçus des ~18 000 environnements infectés et sélectionne **environ 100 cibles de haute valeur** pour l’exploitation approfondie. Le ciblage sélectif est une signature de l’opération — APT29 n’a pas intérêt à être partout, seulement dans les cibles stratégiques. Sur les cibles sélectionnées, les opérateurs déploient des **outils de seconde étape** :

- **TEARDROP** : loader en mémoire.
- **RAINDROP** : variant de loader identifié ultérieurement.
- **GoldMax / SUNSHUTTLE** : backdoor Go cross-platform.
- **GoldFinder** : HTTP tracer pour reconnaissance d’infrastructure.
- **SIBOT** : backdoor VBScript.

Les cibles finales incluent : **Département du Trésor**, **Département du Commerce**, **Département de la Sécurité intérieure (DHS)**, **Département d’État**, **Département de l’Énergie** (y compris NNSA — National Nuclear Security Administration), **Pentagone** (partiellement), **Microsoft**, **FireEye/Mandiant**, et plusieurs autres grandes entreprises et agences.

**8 décembre 2020** : **FireEye** annonce publiquement avoir été compromis et avoir eu des outils Red Team volés.

**13 décembre 2020** : FireEye publie ses conclusions — l’intrusion chez FireEye provenait de SolarWinds Orion compromis. Publication simultanée d’un rapport technique détaillé sur SUNBURST. L’ensemble de l’écosystème CTI commence à enquêter.

**14 décembre 2020** : SolarWinds confirme la compromission, publie des indicateurs.

**15-20 décembre 2020** : Microsoft et d’autres entités confirment des compromissions. **CISA** publie une Emergency Directive ordonnant aux agences fédérales US de déconnecter Orion ou de le mettre à jour vers une version saine.

**Janvier 2021** : **attribution officielle** par le gouvernement américain — ODNI, NSA, FBI, CISA attribuent à APT29 / SVR russe. L’attribution est renforcée ultérieurement avec le ralliement de Five Eyes + UE en avril 2021.

#### 29.3 TTP détaillées — mapping ATT&CK

SolarWinds est un cas d’étude très documenté en ATT&CK. Techniques principales observées :

- **T1195.002 — Supply Chain Compromise: Compromise Software Supply Chain** : injection de SUNBURST dans le build pipeline SolarWinds.
- **T1218 — Signed Binary Proxy Execution** : SUNBURST est un composant légitime d’Orion, signé numériquement.
- **T1036 — Masquerading** : domaines C2 (avsvmcloud.com, etc.) au nom évocateur de services cloud légitimes. Sous-domaines construits pour ressembler à des requêtes normales.
- **T1071 — Application Layer Protocol: Web Protocols** : C2 HTTPS avec DNS queries de type DNS-over-HTTPS.
- **T1087 — Account Discovery** : énumération des comptes Active Directory.
- **T1550 — Use Alternate Authentication Material** : **GoldenSAML** — forgeage de tokens SAML via compromission d’ADFS, accès aux ressources Azure AD / O365 sans authentification classique.
- **T1528 — Steal Application Access Token** : vol de tokens OAuth Azure AD.
- **T1114 — Email Collection** : accès aux boîtes mail via Graph API en utilisant les tokens SAML forgés.
- **T1078 — Valid Accounts** : usage de comptes légitimes pour le mouvement latéral.
- **T1041 — Exfiltration Over C2 Channel**.

Le chaînage de ces techniques — supply chain → persistence furtive → forgeage d’identité cloud → accès données — est le paradigme que SolarWinds a établi pour les opérations APT cloud modernes.

#### 29.4 GoldenSAML : l’innovation pivot

Le pivot **GoldenSAML** mérite une explication technique dédiée car il est devenu une référence.

**Principe ADFS** : Active Directory Federation Services (ADFS) est le composant Microsoft qui permet l’authentification fédérée. Quand un utilisateur se connecte à Azure AD / O365, ADFS (si configuré) génère un **token SAML** signé par la clé privée d’ADFS. Ce token est présenté à Azure AD comme preuve d’authentification — Azure AD fait confiance à la signature ADFS et autorise l’accès.

**L’attaque GoldenSAML** : l’attaquant qui compromet le serveur ADFS et vole la **clé privée de signature** peut **forger ses propres tokens SAML** pour n’importe quel utilisateur, avec n’importe quels attributs. Azure AD ne peut pas distinguer un token légitime d’un token forgé — la signature est valide.

**Conséquences** :

- L’attaquant peut **se faire passer pour n’importe quel utilisateur**, y compris des administrateurs globaux.
- Accès à **Exchange Online** (lecture de tous les emails), **SharePoint** (tous les documents), **Teams**, **OneDrive**.
- **Persistence sans malware** : tant que la clé n’est pas renouvelée, l’attaquant garde l’accès, sans aucun code malveillant déposé côté cloud.
- **Très difficile à détecter** : les logs Azure AD montrent des authentifications légitimes (tokens valides, signature correcte).

**Remédiation** : nécessite la **régénération des clés ADFS**, idéalement la **reconstruction complète d’ADFS**, et l’audit de tous les accès effectués depuis la compromission — opération lourde qui peut durer des mois.

GoldenSAML, déjà connu théoriquement avant 2020, est devenu **opérationnellement célèbre** avec SolarWinds. D’autres acteurs (notamment chinois) ont adopté la technique ensuite.

#### 29.5 Découverte par FireEye/Mandiant

La découverte de SolarWinds est elle-même une histoire remarquable. FireEye enquêtait sur une intrusion dans son propre environnement — les attaquants avaient volé des outils Red Team. L’investigation interne a remonté jusqu’au vecteur : Orion compromis. FireEye a alors compris que tous ses clients utilisant Orion étaient potentiellement compromis, et au-delà — que l’ensemble du parc Orion dans le monde était compromis.

**La décision de publication** : FireEye aurait pu traiter l’incident en privé. L’entreprise a choisi la **publication rapide et détaillée** (rapport SUNBURST publié dès le 13 décembre 2020). Cette décision, courageuse commercialement (révéler publiquement une compromission est coûteux en réputation), a permis à l’écosystème entier de réagir. C’est devenu un **cas emblématique de l’importance de la transparence** en cybersécurité.

**Kevin Mandia** (alors PDG de FireEye) a conduit les communications publiques. L’entreprise a été saluée pour son approche — le rapport technique est devenu une référence, et la transparence a renforcé (contre-intuitivement) la confiance des clients.

#### 29.6 L’attribution et ses suites

**Attribution officielle** :

- **Janvier 2021** : ODNI, NSA, FBI, CISA attribuent à un acteur russe, probablement le SVR. Confiance : élevée.
- **Avril 2021** : attribution renforcée, mention explicite du SVR. **Sanctions** — l’administration Biden annonce des sanctions contre la Russie (incluant expulsions de diplomates, sanctions financières ciblées).
- **UE et Five Eyes** se coordonnent sur l’attribution.

**Pas d’indictment DOJ** pour SolarWinds (contrairement à certaines autres opérations russes) — probablement parce que les opérateurs individuels sont protégés par le contexte et que l’attribution au niveau étatique était jugée suffisante.

**Pas de représailles cyber déclarées** — les États-Unis ont choisi de répondre par sanctions et diplomatie, pas par action cyber offensive publique en représailles directes.

#### 29.7 Impact et réponse structurelle

**Impact immédiat** :

- **Dwell time** : APT29 avait maintenu l’accès aux environnements les plus sensibles pendant **6 à 12 mois** (voire plus) avant détection.
- **Renseignement collecté** : quantité et nature classifiées, mais probablement massive — emails gouvernementaux US stratégiques, plans, communications diplomatiques.
- **Impact sur la confiance** : ébranlement de la confiance dans la supply chain logicielle. SolarWinds, grand éditeur respecté, était compromis — la question « qui d’autre ? » s’est imposée.

**Réponse structurelle** :

**Executive Order 14028 (mai 2021)** — « Improving the Nation’s Cybersecurity » : réponse américaine majeure à SolarWinds. Exigences :

- **SBOM** (Software Bill of Materials) obligatoire pour les fournisseurs du gouvernement fédéral.
- **Zero Trust** architecture dans les agences fédérales.
- **Amélioration du partage d’information** entre agences et avec CISA.
- **Critical software definition** et contrôles associés.
- **Endpoint Detection and Response** généralisé sur les endpoints fédéraux.

**Cyber Safety Review Board (CSRB)** : création en 2022 sur le modèle du NTSB (investigation d’accidents aériens). Le CSRB investigue les incidents cyber majeurs et publie des rapports. Son premier rapport (juillet 2022) portait sur Log4j ; d’autres ont suivi (Lapsus$, Storm-0558).

**Changements dans l’industrie** : durcissement des build pipelines (isolation, reproducibility, signatures multi-factorielles), Zero Trust sur les mises à jour, monitoring du plan de contrôle identity cloud.

#### 29.8 Leçons opérationnelles

SolarWinds a produit un **corpus de leçons** qui structurent la pratique cyber contemporaine.

**La supply chain logicielle est un vecteur APT majeur** : tous les éditeurs sont des cibles potentielles. Les acheteurs doivent intégrer ce risque dans leurs évaluations.

**La confiance implicite dans un éditeur ne protège pas** : une mise à jour signée par un éditeur légitime peut contenir une backdoor. Le monitoring comportemental des processus, même légitimes, reste indispensable.

**Le monitoring identity cloud est critique** : GoldenSAML, abus OAuth, tokens SAML forgés — la détection d’anomalies dans le plan de contrôle identity est un domaine à part entière de la défense moderne.

**Zero Trust s’impose** : appliqué aux fournisseurs, aux mises à jour, aux authentifications — la confiance ne peut plus être implicite.

**L’intégrité du build pipeline est un enjeu stratégique** : les éditeurs logiciels doivent investir dans la sécurité de leur processus de build (isolation, signatures, audit, reproducibility).

**La transparence bénéficie à l’écosystème** : la décision FireEye de publier rapidement a permis à tous les défenseurs de réagir. Ce modèle de divulgation coordonnée est devenu une référence.

**L’attribution publique coordonnée impose un coût** : les sanctions et expulsions diplomatiques n’ont pas empêché APT29 de continuer, mais elles ont imposé un coût réel à la Russie. L’effet n’est pas nul.

-----

### Chapitre 30 — Lazarus et l’empire crypto de la DPRK

Le paradigme **unique au monde** du financement d’un État par le cybervol de crypto-actifs. Lazarus Group / RGB nord-coréen est le seul cas dans l’histoire où un État finance sa survie et son programme d’armement par des méthodes cybercriminelles.

#### 30.1 Contexte : RGB et modèle économique unique

**Acteur principal** : **Lazarus Group** et sous-structures (APT38/BlueNoroff pour la finance, Kimsuky pour l’espionnage, autres). Tous rattachés au **RGB** (Reconnaissance General Bureau — renseignement militaire nord-coréen).

**Contexte stratégique** : la DPRK est sous **sanctions ONU et internationales** depuis 2006 (renforcées 2009, 2013, 2016, 2017). Coupée des circuits financiers légaux, elle doit financer son régime, son appareil militaire, et surtout son **programme nucléaire et balistique** par des canaux alternatifs — commerce illégal, contrefaçon, et depuis les années 2010, **cybervol**.

**Attribution publique** : FBI, DOJ, Treasury/OFAC ont consolidé l’attribution à la DPRK via de multiples indictments, sanctions, advisories depuis 2018. Les reconstructions techniques par Mandiant, CrowdStrike, Chainalysis, TRM Labs, Elliptic, et d’autres ont alimenté cette attribution avec haute confiance.

**Impact macroéconomique** : les estimations convergent sur un cumul de **3 à 6+ milliards de dollars** volés en crypto-actifs entre 2017 et 2025, avec une accélération récente. Pour un PIB DPRK estimé à ~30 milliards de dollars annuels, le cybervol représente plusieurs pourcents du PIB — ordre de grandeur macroéconomique.

#### 30.2 Chronologie des vols majeurs

Rappel et synthèse consolidée (détaillée au Ch.12) :

**2014-2017 — phase d’expérimentation** :

- **Sony Pictures** (2014) : opération cyber-politique, pas financière, mais démontre l’ambition de Lazarus.
- **Bangladesh Bank** (février 2016) : 81 M$ transférés via SWIFT. Premier braquage bancaire étatique majeur.
- **WannaCry** (mai 2017) : ransomware mondial, peu lucratif (~140 k$) mais démonstration de capacité.

**2018-2021 — pivot crypto et montée en échelle** :

- Multiples vols d’exchanges asiatiques et européens : DragonEx, Upbit, KuCoin, Cream Finance, Badger DAO.
- Cumul estimé à plusieurs centaines de millions.

**2022-2024 — industrialisation** :

- **Ronin Network / Axie Infinity** (mars 2022) : **624 M$**. Accès initial via phishing LinkedIn contre un employé de Sky Mavis. Compromission des clés privées de bridge.
- **Harmony Bridge** (juin 2022) : 100 M$.
- **Atomic Wallet** (juin 2023) : 100 M$.
- **DMM Bitcoin** (mai 2024) : 305 M$.
- **WazirX** (juillet 2024) : 235 M$.
- **Radiant Capital** (octobre 2024) : 50 M$.

**2025 — pic historique** :

- **Bybit** (février 2025) : **~1,5 milliard de dollars** — **le plus gros vol crypto de l’histoire**. Attribution FBI à Lazarus confirmée dans les semaines suivantes.

#### 30.3 Le vecteur social engineering : Opération Dream Job

Le vecteur d’accès initial le plus documenté chez Lazarus est le **social engineering ciblé sur LinkedIn** — l’Opération Dream Job.

**Modus operandi détaillé** :

**Phase 1 — Approche** : un faux profil de recruteur (souvent usurpant un recruteur réel d’une entreprise légitime, ou créé de toutes pièces avec un profil crédible) approche sur LinkedIn un développeur ou ingénieur senior dans une cible stratégique — crypto exchange, entreprise DeFi, éditeur de logiciel, aérospatial. Message personnalisé : « Nous recrutons pour un poste senior chez [entreprise légitime], votre profil correspond parfaitement, êtes-vous intéressé ? »

**Phase 2 — Transition** : la conversation passe à un canal privé (WhatsApp, Telegram, Skype, parfois email personnel). Échanges sur le poste, l’entreprise, la rémunération. Construction de confiance sur plusieurs jours ou semaines.

**Phase 3 — Test technique** : à un moment, le recruteur envoie un « test technique » sous forme de projet à télécharger et exécuter. Peut prendre plusieurs formes :

- Projet en archive ZIP avec un exécutable à tester.
- Projet en Node.js / Python avec des dépendances à installer (qui portent le malware).
- Image Docker à exécuter localement.
- Document PDF avec des exploits.

**Phase 4 — Exécution** : la cible exécute le projet sur **sa machine professionnelle** (car elle a ses outils de développement). Le malware s’exécute dans le contexte de la machine de développement — qui a souvent accès à des secrets (tokens API, clés privées, accès aux systèmes de production, accès au cloud).

**Phase 5 — Pivot** : depuis la machine de développement, l’attaquant pivote vers les systèmes de l’employeur de la victime. Si la victime est un développeur d’exchange crypto, l’attaquant peut accéder aux systèmes de signature de transactions, aux wallets chauds, ou à la chaîne de build du logiciel.

**Cas Ronin Network** (documenté publiquement) : un développeur senior de **Sky Mavis** (studio derrière Axie Infinity) a été approché via LinkedIn par un faux recruteur. Il a exécuté le « test technique » sur sa machine. L’attaquant a pivoté vers les systèmes Sky Mavis, compromis les nodes validateurs du bridge Ronin, et exécuté les transferts frauduleux de **624 millions de dollars**.

**Pourquoi ça marche** :

- L’approche est personnalisée et plausible.
- Les offres d’emploi dans la tech / crypto sont fréquentes et attractives.
- Les développeurs, habitués à exécuter du code inconnu dans leur travail (review de code, contributions open source), ont une garde moins haute.
- Les vérifications d’identité sur LinkedIn sont faibles.

#### 30.4 Les compromissions supply chain : 3CX, JumpCloud

En parallèle du social engineering direct, Lazarus exploite des **supply chains** pour atteindre des cibles crypto en volume.

**3CX (mars 2023)** : supply chain imbriquée déjà traitée (Ch.12). Cascade X_Trader → 3CX → clients 3CX. Ciblage sélectif en phase 2 sur des entreprises crypto parmi les 600 000 clients 3CX.

**JumpCloud (juin 2023)** : compromission d’un fournisseur de gestion d’identité SaaS (directory service, SSO, MDM). Lazarus a pivoté vers **~5 clients JumpCloud dans l’écosystème crypto** — ciblage extrêmement sélectif. Démontre la sophistication — Lazarus identifie les supply chains qui servent des clients crypto, les compromet, et pivote chirurgicalement.

#### 30.5 L’exploitation DeFi

Les plateformes **DeFi** (Finance Décentralisée) sont une cible privilégiée de Lazarus depuis 2022. Pourquoi : quantités massives de fonds (TVL — Total Value Locked — en milliards), smart contracts parfois mal audités, complexité qui crée des vulnérabilités, équipes souvent petites et moins mûres en sécurité qu’un exchange centralisé.

**Vecteurs d’attaque DeFi** :

- **Compromission des clés privées de validateurs** (cas Ronin — bridge multichain avec 9 validateurs, Lazarus en a compromis 5 sur 9, seuil nécessaire pour autoriser un transfert).
- **Exploitation de vulnérabilités dans les smart contracts** (reentrancy, price oracle manipulation, bridge vulnerabilities).
- **Compromission des interfaces web** (pour rediriger les utilisateurs vers des contrats malveillants).
- **Compromission des équipes de développement** (social engineering comme dans Ronin).

**Le cas Bybit (février 2025)** — le plus gros vol crypto de l’histoire :

- **Mécanisme** : compromission présumée d’un compte administrateur de cold wallet via social engineering + exploitation d’une interface de signature. Les détails techniques précis ont été partiellement publiés par Bybit et analysés par Chainalysis.
- **Montant** : ~1,5 milliard de dollars en ETH et stablecoins.
- **Timing** : février 2025, quelques jours de blanchiment avant identification publique.
- **Attribution** : FBI a confirmé l’attribution à Lazarus / DPRK dans les semaines suivantes.
- **Réponse** : Bybit a maintenu la liquidité via des prêts d’urgence et a racheté/remplacé les fonds perdus — transparence remarquable.

#### 30.6 Le pipeline de blanchiment

Une fois les crypto-actifs volés, Lazarus doit les **convertir en devises utilisables**. Ce processus est un sujet d’investigation à part entière — il oppose les défenseurs (Chainalysis, TRM Labs, Elliptic, FBI, OFAC, exchanges majeurs) aux attaquants dans une course constante d’adaptation.

**Étape 1 — Obfuscation on-chain** :

- **Mixers / tumblers** : services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. **Tornado Cash** (Ethereum) était le principal mixer utilisé par Lazarus. **Sanctionné par l’OFAC en août 2022** — première sanction d’un smart contract dans l’histoire. Post-sanction, Lazarus a migré vers d’autres mixers moins connus et vers des techniques de mixing natives on-chain.
- **Samourai Wallet** (Bitcoin) — fermé par les autorités en avril 2024.
- **Wasabi Wallet** (Bitcoin).
- **Privacy coins** : conversion vers Monero (XMR), difficile à tracer on-chain.

**Étape 2 — Bridges cross-chain** : transferts entre blockchains pour complexifier le suivi. Ethereum → BNB Chain → Avalanche → TRON — chaque saut rend le tracing plus complexe. Les **bridges sont également des cibles de Lazarus** (Ronin, Harmony) — ironie où les outils de blanchiment sont aussi des sources de revenus.

**Étape 3 — Conversion en stablecoins** : conversion en **USDT** (Tether) principalement sur la blockchain **TRON** (frais faibles, confirmations rapides, liquidité élevée). L’USDT sur TRON est devenu le canal dominant des flux illicites crypto en général, DPRK incluse.

**Étape 4 — Cashout en fiat** : conversion finale en dollars, euros, yuan.

- **Exchanges à KYC faible** : certains exchanges en Asie, Russie, Golfe ont historiquement eu des pratiques KYC laxistes. Pression réglementaire croissante.
- **OTC desks** (Over-the-Counter) : traders hors-marché qui convertissent crypto en fiat pour commissions élevées. Certains OTC desks basés en Chine ont été identifiés comme facilitators Lazarus — plusieurs ont été sanctionnés par l’OFAC.
- **P2P marketplaces** : LocalBitcoins (fermé 2023), autres.
- **Mules** : réseaux de particuliers recrutés (souvent sans conscience complète) pour recevoir et transférer les fonds.

**Étape 5 — Rapatriement vers la DPRK** : une fois en fiat, circuits opaques — sociétés écrans chinoises, banques complaisantes, parfois transports physiques de cash. Mécanismes largement classifiés.

**Course défensive** :

- **Sanctions OFAC ciblées** : Tornado Cash (2022), adresses crypto spécifiques, OTC desks, ressortissants.
- **Coopération exchanges majeurs** : Binance, Coinbase, Kraken gèlent les fonds identifiés, collaborent avec le FBI. Binance a gelé plus de 4 milliards de dollars liés à des activités illicites entre 2022 et 2024 (tous types, DPRK et autres).
- **Intelligence blockchain** : Chainalysis, TRM Labs, Elliptic fournissent aux autorités des capacités de suivi on-chain.
- **Saisies** : le DOJ a saisi pour plusieurs centaines de millions de dollars de crypto liés à des vols Lazarus entre 2022 et 2025.

L’asymétrie : **les attaquants n’ont qu’à trouver une route qui fonctionne, les défenseurs doivent fermer toutes les routes**. La guerre du blanchiment est permanente.

#### 30.7 Impact géopolitique : cyber comme arme de prolifération

La conséquence la plus grave des cyberopérations DPRK est le **financement direct du programme nucléaire et balistique nord-coréen**.

**Évidences** :

- **Rapports ONU Panel of Experts** : chaque rapport annuel documente l’ampleur du cybervol DPRK et sa contribution au financement du programme d’armement.
- **Déclarations US Treasury** : les sanctions explicitent le lien entre Lazarus et le financement de la prolifération.
- **Timing** : l’accélération du programme nucléaire/balistique nord-coréen (tests de missiles intercontinentaux 2017, tests nucléaires, missiles hypersoniques annoncés) coïncide avec l’intensification du cybervol crypto.

**Implication stratégique** : les cyberopérations nord-coréennes ne sont pas un « problème cyber » — elles sont un **problème de sécurité internationale** lié directement à la non-prolifération nucléaire. Chaque dollar volé par Lazarus contribue potentiellement au développement d’armes nucléaires et de vecteurs balistiques.

**Conséquence pour la réponse** : les mesures anti-Lazarus ne sont pas seulement de la cybersécurité — elles sont partie intégrante de la politique de non-prolifération. Cette perspective justifie l’intensité de la réponse internationale (sanctions OFAC multiples, coordination Treasury/FBI/exchanges, pression sur les juridictions facilitators).

#### 30.8 Les opérateurs IT DPRK : phénomène parallèle

En complément du cybervol, le **phénomène des opérateurs IT DPRK** (détaillé Ch.11.8) représente un autre volet du modèle économique cyber nord-coréen.

**Rappel synthétique** : milliers de ressortissants nord-coréens travaillent à l’étranger sous fausses identités comme développeurs freelance/salariés, générant ~300 M$ par an pour le régime.

**Risques additionnels au-delà du financement** :

- **Introduction de malware** : un opérateur IT DPRK infiltré peut introduire du code malveillant dans les produits de son employeur.
- **Exfiltration de PI** : accès aux secrets techniques de l’employeur.
- **Préparation d’accès pour Lazarus** : un opérateur IT peut préparer des accès privilégiés qui sont ensuite exploités par les équipes Lazarus (opération à deux temps, difficile à détecter).

**Défense** : vérifications d’identité approfondies, background checks, vigilance sur les anomalies comportementales (réticence caméra, horaires décalés, anomalies linguistiques, IP sources incohérentes avec résidence déclarée).

#### 30.9 Réponses internationales

La réponse internationale à Lazarus a évolué vers une stratégie intégrée.

**Sanctions** : sanctions OFAC multiples (personnes, entités, adresses crypto), sanctions UE, sanctions coordonnées. Tornado Cash (2022) et ensembles d’adresses sanctionnées individuellement.

**Indictments** : DOJ a inculpé plusieurs ressortissants nord-coréens pour des opérations spécifiques, facilitators chinois, et des structures-écrans.

**Coopération public-privé** : alliance entre FBI, Treasury, exchanges majeurs, firms d’intelligence blockchain. Partage d’IoC crypto, gels de fonds en temps réel, saisies coordonnées.

**Engagement diplomatique** : pression sur la Chine (principal facilitateur du blanchiment DPRK), sur la Russie (pays de transit), et sur les pays d’Asie du Sud-Est.

**Démantèlements** : Samourai Wallet (2024), OTC desks identifiés — pression continue sur les infrastructures de blanchiment.

**Bilan** : malgré ces efforts massifs, **le cybervol DPRK continue et s’amplifie** (record Bybit 2025). La DPRK adapte ses TTP plus vite que les défenseurs ne ferment les routes. La réponse reste **partielle** — elle limite, sans éliminer.

#### 30.10 Leçons

SolarWinds établit un paradigme technique ; Lazarus établit un paradigme stratégique **unique**.

**Le cybercrime peut être un instrument étatique à échelle macroéconomique** : aucun autre cas documenté dans l’histoire ne combine cette ampleur financière et cette intégration au financement d’un programme d’armement stratégique.

**Les démocraties font face à un acteur non-dissuadable par les moyens classiques** : la DPRK n’a rien à perdre en cyber, les sanctions ne changent pas fondamentalement ses incitations. La réponse doit être **opérationnelle** (fermer les routes de blanchiment) plus que **dissuasive** (imposer un coût qui change les incitations).

**La frontière cybercrime / action étatique est définitivement brouillée** : Lazarus a rendu cette frontière inapplicable comme grille analytique. L’analyse doit considérer la **méthode** et la **finalité** séparément.

**Le secteur privé crypto est en première ligne** : les exchanges, les plateformes DeFi, les développeurs blockchain sont des cibles directes. Les leçons Lazarus (social engineering LinkedIn, supply chain) sont des impératifs de sécurité pour tout l’écosystème crypto.

**Le monitoring blockchain est indispensable** : Chainalysis, TRM Labs, Elliptic ne sont pas des luxes mais des nécessités pour tout acteur significatif du crypto. Le suivi en temps réel des adresses sanctionnées, des flux suspects, et des patterns de blanchiment est désormais une fonction de sécurité standard.

-----

### Chapitre 31 — Volt Typhoon : le pré-positionnement stratégique

Le paradigme du **pré-positionnement sans action** — la menace la plus difficile à détecter et potentiellement la plus lourde de conséquences stratégiques.

#### 31.1 Contexte : PRC, pré-positionnement, scénario Taïwan

**Acteur** : Volt Typhoon — PRC state-sponsored, probablement PLA ou entité affiliée. Attribution fine (quelle unité spécifique) non publiquement précisée à date.

**Attribution publique** : advisory conjoint **NSA, CISA, FBI + Five Eyes** (mai 2023), réitéré et enrichi (2024). Aucun indictment DOJ à date, contrairement à d’autres groupes APT chinois. L’attribution a été faite publiquement avec un niveau de détail technique inhabituel — signe probable d’une volonté de signalement diplomatique forte.

**Paradigme** : pré-positionnement stratégique dans les infrastructures critiques. Pas d’espionnage massif, pas d’exfiltration, pas d’action destructive. Uniquement établir et maintenir un accès dormant, activable en cas de besoin.

**Signification géopolitique** : la communauté de renseignement américaine interprète Volt Typhoon comme une **capacité de dissuasion / représailles chinoise** dans le scénario Taïwan. Message implicite : si les États-Unis interviennent militairement pour défendre Taïwan, la Chine peut frapper les infrastructures critiques américaines — notamment celles qui soutiennent la projection militaire dans le Pacifique (énergie, télécoms, eau, transport à Guam et sur la côte Ouest).

C’est potentiellement **la menace cyber stratégique qui définira la prochaine décennie** — au moins tant que la tension Taïwan reste un enjeu géopolitique majeur.

#### 31.2 Timeline : activité au moins depuis 2021

**Premières détections** : mi-2023 publiquement, avec des traces rétrospectives identifiées jusqu’à **mi-2021 au moins**. Probablement plus tôt — les premières compromissions peuvent remonter à 2019-2020.

**Mai 2023** : **publication de l’advisory conjoint NSA/CISA/FBI + partenaires Five Eyes**. Premier document public détaillé sur Volt Typhoon. L’advisory documente les TTP et plusieurs secteurs cibles, avec des IoC limités (cohérent avec le caractère LotL du groupe).

**2023-2024** : campagne d’observation et d’éradication par les organisations ciblées américaines, avec support CISA/FBI. Documentation progressive des TTP par Microsoft, Mandiant, CrowdStrike et autres.

**Janvier 2024** : **démantèlement partiel par le FBI** — opération **KV Botnet** sous mandat judiciaire. Le FBI a neutralisé un botnet de routeurs **Cisco RV** domestiques et **NetGear** compromis qui servait d’infrastructure C2 à Volt Typhoon. Opération remarquable sur le plan légal — le FBI a exécuté un mandat pour intervenir sur les routeurs domestiques de citoyens américains afin de neutraliser le malware, sans interagir avec les systèmes au-delà de la neutralisation.

**2024-2025** : Volt Typhoon reste actif. Les démantèlements partiels n’ont pas stoppé l’activité — le groupe adapte son infrastructure et continue. Détections continues dans des infrastructures US et alliées.

#### 31.3 Les cibles

**Cibles documentées publiquement** :

- **Opérateurs de télécommunications** aux États-Unis.
- **Fournisseurs d’énergie électrique** dans plusieurs États US.
- **Systèmes d’eau** municipaux.
- **Infrastructures de transport** (portuaires, ferroviaires).
- **Territoires du Pacifique** : **Guam** particulièrement ciblée — importance stratégique majeure en cas de conflit Taïwan (base militaire US, point de projection).

**Cibles non confirmées publiquement mais suspectées** : extension possible à d’autres alliés (Japon, Corée du Sud, Australie, pays européens). Les advisories récents suggèrent une préoccupation au-delà des seuls États-Unis, mais les détails restent partiellement classifiés.

**Profil des cibles** : systématiquement des **infrastructures civiles critiques**, pas des cibles militaires directes. Cohérent avec une stratégie de pré-positionnement qui viserait à **dégrader les capacités de projection et de soutien** en cas de conflit, plutôt qu’à frapper directement les forces militaires.

#### 31.4 TTP : le profil extrême de LotL

Volt Typhoon est **extrême dans sa pureté opérationnelle** — l’archétype de l’APT moderne LotL.

**Accès initial** :

- **Exploitation d’appliances edge** : vulnérabilités sur routeurs SOHO (Cisco RV), VPN, firewalls. **Fortinet FortiGate** documenté. Les appliances ciblées sont souvent des équipements en fin de vie ou non patchés.
- Pas de phishing massif documenté (ce qui distingue Volt Typhoon des APT chinoises plus classiques comme APT10).

**Persistence** :

- **Credentials légitimes** : vol de credentials admin via credential dumping, puis utilisation prolongée. Aucun compte créé par l’attaquant.
- **Pas de malware custom** déposé pour la persistence. La persistence repose sur les credentials volés + scheduled tasks légitimes + services Windows existants.

**Exécution et mouvement latéral** :

- **Living off the Land quasi exclusif** : PowerShell, WMI, net.exe, ntdsutil, ping, tracert, ipconfig, netsh, reg.exe, wmic, certutil. Aucun binaire malveillant identifié à date dans les environnements compromis.
- **Mouvement latéral** : RDP avec credentials admin, WMI, SMB.

**Command and Control** :

- **Routeurs SOHO compromis comme relais C2** : les implants utilisent des routeurs résidentiels compromis (domestiques, clients des FAI US) comme points de sortie. Le trafic C2 semble donc provenir d’**IP résidentielles US légitimes** — fondement dans le trafic domestique, détection réseau extrêmement difficile sans inspection approfondie de contenu.
- **Activité très intermittente** : pas de beaconing régulier, accès occasionnels et limités au minimum nécessaire pour maintenir la présence.

**Collection et exfiltration** :

- **Aucune exfiltration massive** documentée.
- Quelques données collectées (configurations réseau, topologie, credentials) — mais uniquement le minimum nécessaire à maintenir l’accès et comprendre l’environnement.

**Impact** :

- **Aucun** déclenché à ce jour. La capacité est maintenue, pas activée.

Ce profil extrême est **une rupture** par rapport aux APT classiques. Les défenseurs habitués à chercher du malware custom, des signatures, des IoC, sont désarmés.

#### 31.5 Le défi de la détection

La détection de Volt Typhoon et de ses imitateurs est **la question défensive la plus difficile** du paysage cyber contemporain.

**Ce qui ne fonctionne pas** (ou peu) :

- **Antivirus/EDR signature-based** : pas de malware à identifier.
- **Blocklist d’IP/domaines malveillants** : les C2 transitent par des IP résidentielles légitimes.
- **Règles SIEM basées sur IoC** : peu ou pas d’IoC stables.

**Ce qui fonctionne** (partiellement) :

- **Baseline comportementale** : qu’est-ce qui est normal dans cet environnement ? Un `ntdsutil` exécuté depuis un serveur non-DC est anormal. Un compte admin qui se connecte à un système où il ne s’est jamais connecté est anormal. Un flux RDP entre deux machines qui n’ont jamais communiqué est anormal.
- **Détection par corrélation multi-sources** : chaque signal individuel peut sembler normal ; leur combinaison dans un temps court est suspecte. Nécessite un SIEM avec corrélation avancée et des règles soigneusement ajustées.
- **Threat hunting proactif** : recherche active d’indicateurs subtils, pas d’attente d’alertes automatiques. Les hunters qualifiés identifient des patterns (usage inhabituel de LOLBins, activité admin en dehors des heures ouvrées, etc.) que les règles automatiques manquent.
- **Monitoring des appliances edge** : logs exhaustifs, patching rapide, scan de configurations.
- **Détection réseau comportementale** : analyse des flux inhabituels, utilisation anormale de protocoles, patterns de connexions distinctifs.

#### 31.6 Réponse : hardening massive et coordination

**Réponse des organisations ciblées** :

- **Hardening** : renforcement des appliances edge (patching, désactivation des composants inutilisés, restriction des accès admin), durcissement AD, déploiement EDR partout, MFA résistant phishing.
- **Monitoring renforcé** : déploiement de visibilité supplémentaire, règles de détection sur mesure, threat hunting dédié.
- **Réaudit des environnements** : chasse rétrospective d’éventuels pré-positionnements non détectés, sur la base des TTP Volt Typhoon publiées.

**Réponse coordonnée** :

- **Advisory CISA conjoint** : publication des TTP, IoC limités, recommandations. Mise à jour régulière.
- **Partage d’information** : briefings classifiés aux opérateurs d’infrastructures critiques, partage via ISAC (E-ISAC, EE-ISAC, Communications ISAC).
- **Shields Up** (CISA) : posture de vigilance renforcée.
- **Démantèlements FBI** : KV Botnet, Raptor Train (Flax Typhoon, opérateur d’infrastructure similaire).

**Réponse diplomatique** :

- Attributions publiques coordonnées Five Eyes.
- Pas de sanctions spécifiques Volt Typhoon à date — la réponse reste principalement opérationnelle.
- Discussions bilatérales US-Chine évoquent le sujet (sans résultats publics).

#### 31.7 Les démantèlements : KV Botnet et Raptor Train

**KV Botnet (janvier 2024)** : le FBI a démantelé un botnet de routeurs domestiques (Cisco RV110W, RV130, RV130W, RV215W, et NetGear) compromis. Ces routeurs — installés chez des particuliers et petites entreprises américaines — servaient d’infrastructure C2 à Volt Typhoon.

**Mandat judiciaire** : le FBI a obtenu un mandat fédéral pour intervenir sur les routeurs, neutraliser le malware (KV Botnet malware), et bloquer les reconnexions. Opération exécutée sans notification préalable aux propriétaires des routeurs (qui, dans la grande majorité, ignoraient être compromis).

**Raptor Train (septembre 2024)** : démantèlement similaire contre **Flax Typhoon**, autre groupe chinois qui opérait un botnet de plus de **260 000 dispositifs IoT compromis** (routeurs, caméras, NAS) servant potentiellement comme infrastructure offensive pour Volt Typhoon et d’autres clusters chinois.

**Effet** : ces démantèlements imposent un **coût opérationnel réel** — reconstituer l’infrastructure demande du temps et des ressources. Mais ils ne stoppent pas définitivement l’activité — Volt Typhoon adapte son infrastructure, recrée d’autres botnets, et continue.

#### 31.8 Implications stratégiques pour l’Europe

Bien que Volt Typhoon soit principalement documenté aux États-Unis, les implications européennes sont réelles.

**Scénario** : si un conflit majeur éclate (Taïwan, mais aussi par extension Ukraine, Moyen-Orient), la Chine pourrait activer des pré-positionnements dans les pays alliés des États-Unis — y compris en Europe. L’alliance OTAN et les solidarités bilatérales US-Europe font de l’Europe une cible crédible.

**Profil des cibles européennes probables** : similaire à l’expérience US — opérateurs télécoms, énergie, eau, transport. Les **opérateurs d’infrastructures critiques européennes** devraient considérer ce scénario dans leur planification.

**Défense proactive** :

- **Audit des environnements** selon les TTP Volt Typhoon publiées. La plupart des opérateurs n’ont pas fait cet audit en profondeur.
- **Renforcement de la visibilité** sur les appliances edge, identity cloud, OT.
- **Exercices** intégrant le scénario pré-positionnement.
- **Collaboration** avec les agences nationales (ANSSI, BSI, NCSC) et les ISAC sectoriels.

#### 31.9 Leçons : la menace la plus dangereuse est celle qui ne fait rien

Volt Typhoon incarne une leçon stratégique profonde.

**Paradoxe de la visibilité** : les menaces les plus visibles (ransomware massif, wipers, exfiltration documentée) ne sont pas les plus dangereuses stratégiquement. **La menace la plus dangereuse est celle qui maintient un accès silencieux pendant des années, sans produire aucun signal détectable, prête à être activée à un moment politique choisi**.

**Incommensurabilité des détections classiques** : les défenses traditionnelles (signature, IoC, volume anormal, exfiltration détectée) sont aveugles au pré-positionnement LotL. Toute une génération d’outils et de pratiques doit évoluer.

**Le facteur temps joue pour l’attaquant** : plus Volt Typhoon maintient ses accès, plus sa capacité de levier grandit. Les défenseurs sont dans une course contre le temps pour construire la visibilité et les capacités de détection qui permettront l’éradication.

**La dimension géopolitique est centrale** : on ne peut pas comprendre Volt Typhoon sans comprendre le scénario Taïwan. La défense cyber est indissociable de la lecture géopolitique. Un RSSI qui ignore la Taïwan Strategic Ambiguity ne peut pas calibrer sa posture face à un pré-positionnement chinois potentiel.

**La réponse doit être collective** : aucun opérateur ne peut répondre seul. La coopération public-privé (opérateurs, agences nationales, ISAC, vendors CTI) est la condition de l’efficacité. Les organisations qui refusent de partager — par peur de l’exposition — affaiblissent la défense collective y compris la leur.

**L’éradication n’est jamais définitive** : Volt Typhoon ne sera pas « éliminé ». Les démantèlements le réduisent, les hardenings le ralentissent, mais l’acteur étatique sophistiqué s’adapte. La défense est un **processus continu**, pas un état atteint.

-----

### Chapitre 32 — Synthèse BLACKOUT : attribution face à l’incertitude

Synthèse complète du fil rouge du cours — de la détection à la réponse, en passant par l’attribution, en un cas autonome intégré.

#### 32.1 Rappel du contexte et des questions d’investigation

**L’opérateur** : distributeur d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2. Infrastructure SCADA reliée à plusieurs dizaines de postes de transformation haute tension.

**L’incident** : détection le J+42 par le SOC d’un comportement anormal sur un poste d’ingénierie OT — rundll32 exécutant une DLL non signée + beaconing HTTPS régulier. Triage CERT rapide : profil APT, pas cybercrime.

**Les questions** :

- **QI-1** : Qui est l’attaquant ?
- **QI-2** : Depuis combien de temps est-il présent, et qu’a-t-il fait ?
- **QI-3** : Quelle est son intention (espionnage, sabotage à venir, pré-positionnement) ?
- **QI-4** : Comment l’éradiquer sans qu’il revienne ?
- **QI-5** : Comment communiquer et coordonner avec les autorités ?

#### 32.2 Reconstitution de la timeline

L’investigation approfondie reconstitue la timeline complète.

**J0 (~42 jours avant détection)** : accès initial via exploitation de **CVE-2024-21887** sur un VPN Ivanti Connect Secure non patché. Le VPN est utilisé par des prestataires externes pour la maintenance des systèmes de supervision — sa compromission donne accès à des zones sensibles sans franchir beaucoup de contrôles internes.

**J+3** : persistence établie. DLL sideloading sur une application de supervision légitime (`SupervisionCenter.exe` charge `plugin_common.dll` — la DLL malveillante remplace la DLL légitime dans un répertoire où l’application regarde avant le répertoire système). Deux mécanismes de persistence additionnels créés : tâche planifiée déguisée en mise à jour système, service Windows modifié.

**J+5** : credential access. Mimikatz déployé en mémoire (sans dépôt sur disque), extraction des credentials LSASS. **Kerberoasting** contre plusieurs comptes de service avec SPN et mots de passe faibles — l’un des comptes crackés est un compte de service privilégié avec droits sur les serveurs de supervision.

**J+8** : mouvement latéral. PsExec utilisé pour pivoter depuis la DMZ vers les serveurs internes de supervision. Compromission d’un serveur historian.

**J+15** : pivot vers l’OT. Identification du poste d’ingénierie OT double-connecté (interface IT + interface SCADA). Compromission du poste via credentials admin locaux obtenus dans la phase précédente. DLL sideloading sur ce poste pour la persistence.

**J+15 à J+30** : reconnaissance OT. Consultation des documentations techniques, des schémas, des procédures. Identification des équipements contrôlés (automates Siemens S7-1500, protocole IEC 104 pour la télécommande des disjoncteurs dans les postes de transformation).

**J+30 à J+42** : dormance. L’attaquant ne fait presque rien pendant 12 jours. Simple maintenance de l’accès via beaconing régulier (27 min ± 3 min) vers un domaine hébergé derrière Cloudflare. Aucune action observable sur les automates.

**J+42 — détection** : l’EDR alerte sur le comportement `rundll32.exe` + DLL non signée + beaconing. Début de l’investigation.

#### 32.3 Collecte des artefacts et mapping ATT&CK

Le CERT collecte méthodiquement les artefacts.

**Collecte** :

- **Logs Sysmon** sur les endpoints compromis (récupération complète depuis la rétention SIEM).
- **Event Logs AD** : authentifications, création de tickets Kerberos, accès aux ressources.
- **Captures réseau** pendant plusieurs jours post-détection (pour observer le beaconing).
- **Dump mémoire** du poste d’ingénierie OT (capture volatile avant redémarrage).
- **Artefacts disque** : persistence, DLL malveillantes, outputs de commandes exécutées.
- **Logs des appliances** : VPN Ivanti, firewalls, proxies.

**Mapping ATT&CK** :

- T1190 — Exploit Public-Facing Application (CVE-2024-21887 Ivanti).
- T1574.002 — DLL Side-Loading (persistence).
- T1003.001 — OS Credential Dumping: LSASS Memory (Mimikatz en mémoire).
- T1558.003 — Kerberoasting.
- T1021.002 — Remote Services: SMB/Windows Admin Shares (PsExec).
- T1071.001 — Application Layer Protocol: Web Protocols (C2 HTTPS).
- T1053.005 — Scheduled Task/Job: Scheduled Task (persistence additionnelle).
- T1543.003 — Create or Modify System Process: Windows Service (persistence).
- T1083 — File and Directory Discovery (reconnaissance OT).

Documentation structurée pour transmission aux autorités et à l’ISAC énergie européen.

#### 32.4 Matrice ACH et attribution

Référence détaillée à l’Épisode 6 (Ch.24). Synthèse.

**H1 Sandworm** : confiance modérée. TTP cohérentes, ciblage énergie, contexte géopolitique. Point faible : absence de malware custom Sandworm identifié.

**H2 cluster chinois (Volt Typhoon ou similaire)** : confiance faible à modérée. TTP LotL s’alignent fortement, mais contexte géopolitique moins aligné, beaconing régulier atypique.

**H3 nouveau cluster étatique non attribué** : confiance faible. Ne peut être écartée.

**H4 acteur non-étatique** : **éliminée** (4 incohérences fortes).

**Conclusion** : pré-positionnement OT par acteur étatique — très probable (>80%). Attribution la plus probable Sandworm/GRU confiance modérée, Chine confiance faible-modérée, cluster non identifié possibility. Documentation des indicateurs de révision.

#### 32.5 La réponse : scope avant contenir

Le CERT applique la règle **scope avant contenir**.

**Scope approfondi** (J+42 à J+48) :

- Threat hunting sur tous les endpoints : recherche d’autres systèmes compromis via les TTP identifiées.
- Identification de **2 autres endpoints compromis** non détectés initialement (un autre poste d’ingénierie, un serveur de supervision).
- Identification de **1 compte admin de domaine compromis** (Kerberoasting réussi — credentials cachés sur les systèmes compromis).
- Identification des mécanismes de persistence sur chaque système.
- Cartographie complète : 3 endpoints, 1 compte admin, 3 mécanismes de persistence par endpoint, plusieurs backdoors secondaires.

**Planification du containment coordonné** (J+48) :

- Équipe dédiée constituée (CERT + IT + OT + direction sécurité).
- Plan de containment simultané documenté : éradication de tous les accès dans une fenêtre de 6 heures.
- Playbook de communication (interne, autorités, potentiellement public).

**Containment exécuté (J+49, nuit de vendredi à samedi)** :

- 22h : réinitialisation de **tous** les comptes compromis (changement de mots de passe, révocation des tickets Kerberos via changement du KRBTGT deux fois).
- 23h : isolation réseau des endpoints compromis.
- 23h30 : neutralisation des mécanismes de persistence (suppression des DLL, des tâches planifiées, des services modifiés).
- 01h : patching du VPN Ivanti (vecteur initial) — patches appliqués depuis plusieurs semaines mais vérification et re-validation.
- 02h-06h : reconstruction des systèmes compromis à partir d’images propres.
- 06h : validation des systèmes reconstruits.
- Ensuite : monitoring renforcé, règles de détection spécifiques déployées pour détecter une tentative de réentrée.

#### 32.6 Sécurisation OT post-incident

Post-éradication, l’opérateur renforce sa posture OT.

**Segmentation physique IT/OT renforcée** : revue complète des points de convergence. Plusieurs accès sont reconfigurés, certains supprimés (simplification de l’architecture).

**Déploiement Sysmon/EDR sur les postes d’ingénierie OT** : quand techniquement possible (OS récents). Les postes sur OS hérités font l’objet de compensating controls (restriction réseau, monitoring renforcé en amont).

**Passive monitoring OT** : déploiement d’une solution OT dédiée (Claroty ou équivalent) sur les segments de supervision. Baseline construite sur 30 jours puis règles de détection activées.

**Durcissement AD** : tiering strict, PAM pour les comptes admin, monitoring des changements critiques.

**Patching edge** : processus accéléré (patch en < 48h sur les vulnérabilités CISA KEV).

**Exercice tabletop programmé** : scénario « pré-positionnement OT à nouveau détecté » pour éprouver la coordination après le vécu de l’incident réel.

#### 32.7 Signalement et coordination

**Signalement ANSSI** : l’opérateur étant OIV, la notification à l’ANSSI est obligatoire dès la qualification de l’incident. Notification initiale sous 24h, détaillée sous 72h, rapport complet ultérieurement.

**Accompagnement ANSSI** : équipe technique mobilisée, revue des éléments techniques, partage d’IoC avec d’autres opérateurs français potentiellement concernés.

**Partage ISAC énergie européen (EE-ISAC)** : diffusion TLP:AMBER des IoC et TTP. Dans les 2 semaines suivantes, **2 autres opérateurs européens confirment avoir observé des TTP identiques** — signe que BLACKOUT n’est pas isolé, mais partie d’une campagne plus large ciblant l’énergie européenne.

**Coordination internationale** : les TTP et le contexte sont partagés avec CISA (via l’ANSSI), NCSC UK, BSI. Coordination croisée pour identifier d’autres victimes.

**Attribution publique** : l’opérateur et l’ANSSI décident de **ne pas communiquer publiquement** à court terme. Raisons : éviter d’exposer les méthodes de détection, préserver la capacité de surveillance d’autres opérations potentielles, contexte diplomatique à gérer par les autorités. Une attribution publique pourrait survenir ultérieurement dans le cadre d’un advisory multilatéral coordonné.

#### 32.8 Monitoring post-éradication et veille

Post-éradication, l’opérateur met en place un **monitoring renforcé** pour détecter une éventuelle tentative de réentrée.

**Règles de détection spécifiques** :

- Alertes sur toute exploitation détectée de CVE Ivanti récentes.
- Monitoring des DLL loading dans les applications de supervision (détection de sideloading).
- Baseline comportementale stricte sur les postes d’ingénierie OT.
- Alertes sur tout Kerberoasting détecté.

**Veille sur les indicateurs** : surveillance des IoC publics liés à Sandworm, Volt Typhoon, et clusters associés. Intégration aux flux CTI.

**Threat hunting trimestriel** : chasse active sur les TTP observées, extension progressive à d’autres TTP Sandworm documentées.

**Exercices réguliers** : tabletop trimestriel sur des scénarios APT dérivés de BLACKOUT.

**Résultat à 6 mois** : **pas de détection d’une nouvelle intrusion** dans l’environnement. L’attaquant n’est pas revenu (ou n’a pas été détecté) via les vecteurs surveillés. L’éradication semble efficace.

#### 32.9 La leçon centrale : comprendre les acteurs pour calibrer la réponse

**La leçon centrale de BLACKOUT — et du cours entier** — peut être formulée ainsi : **face à une intrusion sophistiquée, comprendre les acteurs est indispensable pour répondre correctement**.

Sans la connaissance des acteurs, l’analyste face à BLACKOUT :

- Ne sait pas interpréter le **pré-positionnement OT** — s’agit-il d’un sabotage imminent (réaction immédiate brutale nécessaire) ? d’une capacité de dissuasion (réaction mesurée, surveillance longue possible) ? d’une reconnaissance (exfiltration à craindre) ? Les réponses diffèrent radicalement.
- Ne sait pas **calibrer l’urgence** — un acteur qui prépare un sabotage (profil Sandworm en contexte ukrainien escaladant) nécessite une éradication immédiate. Un acteur en pré-positionnement stratégique (profil Volt Typhoon) peut justifier une phase de surveillance contrôlée.
- Ne sait pas **qui alerter et comment** — le signalement ANSSI déclenche des processus différents selon que l’acteur est russe (contexte ukrainien, information-sensibilité diplomatique), chinois (enjeu Taïwan), ou inconnu (prudence supplémentaire).
- Ne sait pas **anticiper les prochains mouvements** — un Sandworm éradiqué tentera probablement de revenir via des vecteurs différents (adaptation rapide des TTP). Un Volt Typhoon éradiqué pourrait se rétablir via des accès redondants non identifiés. Le monitoring post-incident se calibre sur ces profils.

**Un SOC sans connaissance des APT** détecte un beaconing et isole un poste. Un **SOC informé par le cours APT** comprend que ce beaconing dans un OIV énergétique européen en contexte géopolitique tendu est compatible avec un pré-positionnement étatique, calibre l’urgence de la réponse en conséquence, et déclenche les bons processus (signalement ANSSI, partage ISAC, monitoring OT renforcé, potentiellement coordination diplomatique).

C’est la raison d’être de ce cours.

#### 32.10 Ce qui aurait pu rater, ce qu’on aurait pu mieux faire

Post-mortem blameless sur BLACKOUT, dans l’esprit de l’apprentissage continu.

**Ce qui a marché** :

- La **détection EDR** a fonctionné — le comportement anormal (rundll32 + DLL non signée + beaconing) a produit une alerte traitée.
- La discipline **scope avant contenir** a été respectée, évitant une éradication partielle qui aurait alerté l’attaquant.
- La **coordination ANSSI/ISAC** a produit de la valeur — identification d’autres victimes, enrichissement analytique.

**Ce qui aurait pu rater** :

- **Si l’EDR avait été moins bien configuré**, le rundll32 avec DLL non signée serait passé inaperçu. Beaucoup d’organisations n’ont pas ce niveau de configuration.
- **Si l’opérateur n’avait pas eu de visibilité sur les postes d’ingénierie OT** (beaucoup d’organisations OT n’en ont pas), l’attaquant serait resté indétecté probablement des années.
- **Si l’équipe CERT avait été moins mûre**, l’investigation aurait confondu cybercrime et APT, et la réponse aurait été inadaptée.
- **Si le patching Ivanti avait été plus rapide** (CVE-2024-21887 était disponible plusieurs semaines avant la compromission J0), l’intrusion initiale n’aurait pas eu lieu.

**Ce qu’on aurait pu mieux faire** :

- **Détection plus précoce** : 42 jours de dwell time est long. Des baselines comportementales plus matures, des règles de détection sur les TTP Sandworm/Volt Typhoon déjà publiées, auraient pu détecter plus tôt.
- **Visibilité OT dès le début** : le passive monitoring OT déployé post-incident aurait pu détecter le pivot IT→OT beaucoup plus tôt s’il avait été en place. Investissement qui aurait été priorisé en amont.
- **Durcissement des postes double-connectés** : les engineering workstations double-connectés sont le point de rupture structurel. Un durcissement spécifique (EDR dédié, monitoring renforcé, restrictions strictes, MFA systématique) aurait réduit la surface.
- **Exercices APT plus fréquents** : l’organisation avait fait des tabletops généraux, pas spécifiquement sur des scénarios APT OT. L’expérience aurait été plus fluide avec une préparation spécifique.
- **Contacts ISAC établis plus tôt** : la coordination EE-ISAC s’est construite pendant la crise. Des relations établies en amont auraient accéléré le partage.

**La leçon transversale** : la défense APT-ready est un **investissement continu** qui doit être fait **avant** l’incident. Pendant la crise, il est trop tard pour construire les capacités — on ne peut que mobiliser ce qui existe. L’opérateur BLACKOUT avait assez de capacités pour détecter, scoper, et éradiquer avec succès. Mais la perfection relative de la réponse n’efface pas la question : combien d’autres opérateurs européens ont des pré-positionnements similaires non détectés, faute de capacités ?

La réponse à cette question est le sujet des années à venir. Ce cours a tenté d’y contribuer.

-----

## ANNEXES

-----

### Annexe A — Glossaire APT/CTI

|Terme                 |Définition                                                                               |
|----------------------|-----------------------------------------------------------------------------------------|
|**ACH**               |Analysis of Competing Hypotheses — technique analytique de test d’hypothèses concurrentes|
|**AitM**              |Adversary-in-the-Middle — phishing interceptant credentials et cookies de session        |
|**APT**               |Advanced Persistent Threat — acteur étatique sophistiqué et persistant                   |
|**ASD**               |Australian Signals Directorate — agence australienne Five Eyes                           |
|**ATT&CK**            |Framework MITRE des tactiques, techniques et procédures adverses                         |
|**Attribution**       |Processus de liaison d’une activité malveillante à un acteur/service/État                |
|**Backdoor**          |Accès dissimulé maintenu par un attaquant                                                |
|**Beaconing**         |Communication périodique entre un implant et son C2                                      |
|**BGP hijacking**     |Détournement de routes BGP pour intercepter du trafic                                    |
|**BOD**               |Binding Operational Directive — directive contraignante CISA                             |
|**Bootkit**           |Malware persistant au niveau du bootloader/UEFI                                          |
|**BYOVD**             |Bring Your Own Vulnerable Driver — exploitation d’un driver signé vulnérable             |
|**C2**                |Command and Control — infrastructure de commande d’un implant                            |
|**C4**                |Centre de Coordination des Crises Cyber (France)                                         |
|**Campaign**          |Série d’intrusions liées par objectif/période/infrastructure                             |
|**CALEA**             |Communications Assistance for Law Enforcement Act — interception légale US               |
|**CCDCOE**            |Cooperative Cyber Defence Centre of Excellence OTAN, Tallinn                             |
|**CERT**              |Computer Emergency Response Team                                                         |
|**CISA**              |Cybersecurity and Infrastructure Security Agency (US)                                    |
|**Cluster**           |Regroupement d’activités non attribué à un acteur connu                                  |
|**COMCYBER**          |Commandement de la cyberdéfense français                                                 |
|**CSE**               |Communications Security Establishment (Canada)                                           |
|**CSRB**              |Cyber Safety Review Board (US)                                                           |
|**CTI**               |Cyber Threat Intelligence                                                                |
|**DCS**               |Distributed Control System — système de contrôle distribué industriel                    |
|**DCSync**            |Simulation d’un DC pour récupérer les hashs AD                                           |
|**Defend forward**    |Doctrine US de contestation permanente dans les réseaux adverses                         |
|**DIMEFIL**           |Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement    |
|**DLL sideloading**   |Chargement d’une DLL malveillante via un exécutable légitime                             |
|**DMZ**               |Zone démilitarisée entre réseaux                                                         |
|**Domain fronting**   |Masquage du C2 réel via un CDN légitime                                                  |
|**Dwell time**        |Temps entre compromission initiale et détection                                          |
|**EDR**               |Endpoint Detection and Response                                                          |
|**Edge device**       |Appliance réseau exposée (VPN, firewall, passerelle)                                     |
|**EE / EI**           |Entité Essentielle / Entité Importante (NIS 2)                                           |
|**ENISA**             |European Union Agency for Cybersecurity                                                  |
|**EternalBlue**       |Exploit SMB NSA leaké, utilisé dans WannaCry/NotPetya                                    |
|**Exfiltration**      |Extraction de données depuis l’environnement compromis                                   |
|**False flag**        |Indices plantés pour brouiller l’attribution                                             |
|**FIRST**             |Forum of Incident Response and Security Teams                                            |
|**Five Eyes**         |Alliance US/UK/Canada/Australie/Nouvelle-Zélande                                         |
|**Foothold**          |Point d’ancrage initial                                                                  |
|**FSB**               |Service fédéral de sécurité russe                                                        |
|**GCHQ**              |Government Communications Headquarters (UK)                                              |
|**Golden Ticket**     |Ticket Kerberos TGT forgé via le hash KRBTGT                                             |
|**GoldenSAML**        |Forgeage de tokens SAML via compromission ADFS                                           |
|**GOOSE**             |Generic Object Oriented Substation Event — protocole IEC 61850                           |
|**GRU**               |Direction du renseignement militaire russe                                               |
|**Hacktiviste**       |Acteur motivé par idéologie                                                              |
|**HMI**               |Human-Machine Interface — interface de supervision industrielle                          |
|**HUMINT**            |Human Intelligence — renseignement d’origine humaine                                     |
|**Hunt forward**      |Déploiement d’équipes USCYBERCOM chez les alliés                                         |
|**IAB**               |Initial Access Broker — courtier vendant des accès compromis                             |
|**ICS**               |Industrial Control Systems                                                               |
|**IEC 60870-5-104**   |Protocole européen de télécommande électrique                                            |
|**IEC 61850**         |Standard pour sous-stations électriques                                                  |
|**IEC 61511**         |Norme pour les SIS                                                                       |
|**Implant**           |Code malveillant persistant                                                              |
|**INCD**              |Israel National Cyber Directorate                                                        |
|**Indictment**        |Mise en accusation formelle (DOJ US)                                                     |
|**Intrusion set**     |Ensemble d’activités regroupées par TTP/infrastructure                                   |
|**IoA / IoC**         |Indicator of Attack / Indicator of Compromise                                            |
|**IRGC**              |Islamic Revolutionary Guard Corps (Iran)                                                 |
|**IRGC-IO**           |IRGC Intelligence Organization                                                           |
|**ISAC**              |Information Sharing and Analysis Center                                                  |
|**JTRIG**             |Joint Threat Research Intelligence Group (GCHQ)                                          |
|**Kerberoasting**     |Extraction de tickets de comptes de service pour cracking hors ligne                     |
|**KEV**               |Known Exploited Vulnerabilities — catalogue CISA                                         |
|**Kill Chain**        |Modèle Lockheed Martin des phases d’intrusion                                            |
|**KRBTGT**            |Compte AD dont le hash permet les Golden Tickets                                         |
|**L2I**               |Lutte Informatique d’Influence (France)                                                  |
|**LID**               |Lutte Informatique Défensive (France)                                                    |
|**LIO**               |Lutte Informatique Offensive (France)                                                    |
|**LOLBin**            |Living Off the Land Binary — outil système légitime détourné                             |
|**LotL**              |Living off the Land                                                                      |
|**LSASS**             |Local Security Authority Subsystem Service — credentials Windows en mémoire              |
|**MES**               |Manufacturing Execution System                                                           |
|**MFA**               |Multi-Factor Authentication                                                              |
|**Mimikatz**          |Outil emblématique d’extraction de credentials Windows                                   |
|**MISP**              |Malware Information Sharing Platform                                                     |
|**MOIS / VAJA**       |Ministry of Intelligence and Security iranien                                            |
|**Mossad**            |Service de renseignement extérieur israélien                                             |
|**MSP**               |Managed Service Provider                                                                 |
|**MSS**               |Ministry of State Security — renseignement civil chinois                                 |
|**NCF**               |National Cyber Force (UK)                                                                |
|**NCSC**              |National Cyber Security Centre (UK + équivalents)                                        |
|**NIS 2**             |Directive UE 2022/2555 sur la cybersécurité                                              |
|**NSA**               |National Security Agency (US)                                                            |
|**OEWG**              |Open-Ended Working Group (ONU)                                                           |
|**OFAC**              |Office of Foreign Assets Control (sanctions US)                                          |
|**OIV**               |Opérateur d’Importance Vitale (France)                                                   |
|**OPC DA/UA**         |OLE for Process Control (Data Access / Unified Architecture)                             |
|**OSINT**             |Open Source Intelligence                                                                 |
|**OT**                |Operational Technology — systèmes industriels                                            |
|**Overpass-the-Hash** |Hash NTLM utilisé pour obtenir un ticket Kerberos                                        |
|**Pall Mall Process** |Initiative internationale de régulation des PSO (2024)                                   |
|**PAM**               |Privileged Access Management                                                             |
|**Pass-the-Hash**     |Authentification avec un hash NTLM                                                       |
|**Pass-the-Ticket**   |Réutilisation d’un ticket Kerberos volé                                                  |
|**PASSI**             |Prestataire d’Audit SSI qualifié ANSSI                                                   |
|**PDIS**              |Prestataire de Détection d’Incidents de Sécurité ANSSI                                   |
|**Pegasus**           |Spyware commercial NSO Group                                                             |
|**PERA**              |Purdue Enterprise Reference Architecture                                                 |
|**PIM**               |Privileged Identity Management                                                           |
|**PLA**               |People’s Liberation Army — armée chinoise                                                |
|**PLC**               |Programmable Logic Controller — automate programmable                                    |
|**Pré-positionnement**|Accès dormant dans infra critique pour usage futur                                       |
|**PSO**               |Private Sector Offensive — fournisseur commercial offensif                               |
|**Purdue (modèle)**   |Architecture en niveaux pour systèmes industriels                                        |
|**Purple team**       |Exercice collaboratif red/blue team                                                      |
|**Pyramid of Pain**   |Hiérarchie des indicateurs par coût pour l’attaquant                                     |
|**Ransomware**        |Malware de rançon par chiffrement                                                        |
|**RAT**               |Remote Access Trojan                                                                     |
|**Red team**          |Équipe de simulation offensive                                                           |
|**RGB**               |Reconnaissance General Bureau — renseignement militaire nord-coréen                      |
|**RSSI**              |Responsable de la Sécurité des Systèmes d’Information                                    |
|**RTU**               |Remote Terminal Unit                                                                     |
|**SAML**              |Security Assertion Markup Language — fédération d’identité                               |
|**Sandbox**           |Environnement isolé d’analyse                                                            |
|**SCADA**             |Supervisory Control and Data Acquisition                                                 |
|**SecNumCloud**       |Qualification ANSSI pour services cloud                                                  |
|**Shadow Brokers**    |Groupe ayant leaké des outils NSA en 2016-2017                                           |
|**SIEM**              |Security Information and Event Management                                                |
|**SIGINT**            |Signal Intelligence                                                                      |
|**Silver Ticket**     |Ticket Kerberos de service forgé                                                         |
|**SIL**               |Safety Integrity Level                                                                   |
|**SIS**               |Safety Instrumented Systems                                                              |
|**SOAR**              |Security Orchestration, Automation and Response                                          |
|**SOC**               |Security Operations Center                                                               |
|**Spear-phishing**    |Phishing hautement ciblé                                                                 |
|**SPN**               |Service Principal Name — identifiant Kerberos                                            |
|**SSF**               |Strategic Support Force (PLA chinois jusqu’en 2024)                                      |
|**SSSCIP**            |State Special Communications Service (Ukraine)                                           |
|**STIX**              |Structured Threat Information Expression — format CTI                                    |
|**Supply chain**      |Compromission via un fournisseur de confiance                                            |
|**SVR**               |Service de renseignement extérieur russe                                                 |
|**Sysmon**            |System Monitor Windows — logging avancé                                                  |
|**Tabletop**          |Exercice de simulation sur table                                                         |
|**TAO**               |Tailored Access Operations (NSA historique)                                              |
|**TAXII**             |Trusted Automated Exchange of Intelligence Information                                   |
|**TLP**               |Traffic Light Protocol (RED/AMBER/GREEN/CLEAR)                                           |
|**Tradecraft**        |Savoir-faire opérationnel global de l’attaquant                                          |
|**TTP**               |Tactics, Techniques, and Procedures                                                      |
|**UBO**               |Ultimate Beneficial Owner                                                                |
|**USCYBERCOM**        |United States Cyber Command                                                              |
|**Watering hole**     |Compromission d’un site fréquenté par les cibles                                         |
|**WEP**               |Words of Estimative Probability                                                          |
|**Wiper**             |Malware destructeur qui efface les données                                               |
|**WMI**               |Windows Management Instrumentation                                                       |
|**Zero day**          |Vulnérabilité inconnue de l’éditeur                                                      |
|**Zero Trust**        |Architecture ne faisant confiance à aucun flux par défaut                                |

-----

### Annexe B — Groupes APT majeurs par pays

*Tableau non exhaustif — focus sur les groupes les plus actifs et documentés. La colonne « Statut d’attribution » indique le niveau de publicité et de confiance.*

|Pays               |Mandiant |CrowdStrike       |Microsoft              |Autres alias                   |Service                    |Cibles principales                  |Statut                   |
|-------------------|---------|------------------|-----------------------|-------------------------------|---------------------------|------------------------------------|-------------------------|
|**Russie**         |APT29    |Cozy Bear         |Midnight Blizzard      |NOBELIUM                       |SVR                        |Gouvernements, diplomatie, tech     |Publique, haute          |
|Russie             |APT28    |Fancy Bear        |Forest Blizzard        |Sofacy, STRONTIUM              |GRU Unit 26165             |Militaire, politique, influence     |Publique, haute          |
|Russie             |Sandworm |Voodoo Bear       |Seashell Blizzard      |BlackEnergy group, IRIDIUM     |GRU Unit 74455             |Sabotage, OT, Ukraine               |Publique, haute          |
|Russie             |—        |—                 |—                      |WhisperGate, UAC-0056          |GRU Unit 29155             |Déstabilisation Ukraine/Europe      |Publique 2024, haute     |
|Russie             |Turla    |Venomous Bear     |Secret Blizzard        |Snake group, Uroburos          |FSB Centre 16              |Espionnage long terme, diplomatie   |Publique, haute          |
|Russie             |Gamaredon|Primitive Bear    |Aqua Blizzard          |Shuckworm                      |FSB Centre 18              |Volumétrie massive Ukraine          |Publique, haute          |
|Russie             |Dragonfly|Energetic Bear    |—                      |Berserk Bear                   |FSB (suspecté)             |Énergie                             |Publique, élevée         |
|**Chine**          |APT41    |Wicked Panda      |Brass Typhoon          |Winnti, BARIUM                 |MSS                        |Tech, santé + cybercrime double     |Publique, haute          |
|Chine              |APT40    |Leviathan         |—                      |TA423, TEMP.Periscope          |MSS Hainan                 |Maritime, Five Eyes                 |Publique 2021, haute     |
|Chine              |APT10    |Stone Panda       |—                      |Red Apollo, MenuPass           |MSS Tianjin                |MSP, industriel (Cloud Hopper)      |Publique 2018, haute     |
|Chine              |APT31    |Judgment Panda    |Zirconium              |RedBravo                       |MSS Hubei                  |Parlementaires, politique           |Publique 2024, haute     |
|Chine              |—        |Vanguard Panda    |Volt Typhoon           |BRONZE SILHOUETTE              |PRC (PLA suspecté)         |Pré-positionnement infras critiques |Publique 2023, haute     |
|Chine              |—        |—                 |Salt Typhoon           |GhostEmperor (partiel)         |PRC                        |Télécoms US                         |Publique 2024, haute     |
|Chine              |—        |Ethereal Panda    |Flax Typhoon           |—                              |Integrity Technology Group |Botnets IoT                         |Publique 2024, sanctionné|
|Chine              |—        |—                 |—                      |Mustang Panda, Bronze President|MSS (suspecté)             |Diaspora, ASEAN, Europe             |Publique, élevée         |
|Chine              |—        |Emissary Panda    |—                      |APT27, Bronze Union            |PRC                        |Industrie, défense                  |Publique, élevée         |
|Chine              |APT30    |—                 |—                      |Naikon                         |PLA                        |ASEAN                               |Publique                 |
|Chine              |Hafnium  |Silk Typhoon      |Hafnium                |—                              |PRC                        |ProxyLogon Exchange 2021            |Publique                 |
|Chine              |—        |—                 |Storm-0558             |—                              |PRC (suspecté)             |Microsoft breach 2023               |Publique                 |
|**DPRK**           |—        |—                 |Diamond Sleet          |Lazarus Group, Hidden Cobra    |RGB                        |Tout usage                          |Publique, haute          |
|DPRK               |APT38    |Stardust Chollima |Sapphire Sleet         |BlueNoroff                     |RGB                        |Finance, crypto                     |Publique, haute          |
|DPRK               |—        |Velvet Chollima   |Emerald Sleet          |Kimsuky, Thallium              |RGB                        |Diplomatie, nucléaire               |Publique, haute          |
|DPRK               |APT43    |—                 |Emerald Sleet (partiel)|—                              |RGB                        |Académique, think tanks             |Publique                 |
|DPRK               |—        |Silent Chollima   |Onyx Sleet             |Andariel                       |RGB                        |Ransomware + espionnage             |Publique                 |
|DPRK               |—        |Labyrinth Chollima|Diamond Sleet          |—                              |RGB                        |Supply chain (3CX, JumpCloud)       |Publique                 |
|**Iran**           |APT33    |Refined Kitten    |Peach Sandstorm        |Elfin                          |IRGC                       |Aérospatial, énergie                |Publique, élevée         |
|Iran               |APT34    |Helix Kitten      |Hazel Sandstorm        |OilRig                         |MOIS                       |Moyen-Orient                        |Publique, élevée         |
|Iran               |APT35    |Charming Kitten   |Mint Sandstorm         |Phosphorus, Magic Hound        |IRGC                       |Dissidents, chercheurs, journalistes|Publique, haute          |
|Iran               |APT42    |—                 |—                      |Calanque                       |IRGC-IO                    |Surveillance ciblée                 |Publique                 |
|Iran               |—        |Static Kitten     |Mango Sandstorm        |MuddyWater                     |MOIS                       |Gouvernements, télécoms             |Publique                 |
|Iran               |—        |—                 |—                      |Scarred Manticore              |MOIS                       |Gouvernements ME                    |Publique 2023            |
|Iran               |—        |—                 |—                      |Agrius, Moses Staff, DEV-0270  |IRGC (suspecté)            |Destructif Israël                   |Publique                 |
|**Vietnam**        |APT32    |OceanBuffalo      |—                      |OceanLotus, Cobalt Kitty       |MPS vietnamien             |ASEAN, dissidents                   |Publique, élevée         |
|**Pakistan**       |—        |Mythic Leopard    |—                      |Transparent Tribe              |Services pakistanais       |Inde                                |Publique                 |
|Pakistan           |—        |—                 |—                      |SideCopy                       |Services pakistanais       |Inde                                |Publique                 |
|**Inde**           |—        |—                 |—                      |SideWinder                     |Services indiens (suspecté)|Pakistan, Chine, ASEAN              |Confiance croissante     |
|Inde               |—        |—                 |—                      |Patchwork                      |Services indiens (suspecté)|Pakistan, Asie du Sud               |Confiance croissante     |
|**Turquie**        |—        |—                 |—                      |Sea Turtle                     |Services turcs (suspecté)  |Moyen-Orient, Europe                |Publique                 |
|**Amérique latine**|—        |—                 |—                      |Blind Eagle, APT-C-36          |Colombie (suspecté)        |Amérique latine                     |Publique                 |

-----

### Annexe C — Conventions de nommage par vendor

Chaque vendor CTI utilise sa propre convention. La correspondance n’est jamais parfaite — deux vendors peuvent regrouper ou fragmenter les clusters différemment.

#### C.1 Mandiant (Google Cloud)

- **APTxx** : groupes étatiques attribués. Ex : APT1, APT28, APT29, APT40, APT41.
- **UNCxxxx** : « Uncategorized » — clusters en analyse, pas encore promus. Ex : UNC2452 (cluster initial SolarWinds, devenu APT29), UNC4841 (Barracuda breach, Chine).
- **FINxx** : groupes financièrement motivés. Ex : FIN7, FIN8, FIN11.
- **TEMP.xxx** : préfixe temporaire historique. Ex : TEMP.Periscope (devenu APT40).

Promotion UNC → APT exige convergence de TTP, d’infrastructure et d’objectifs dans le temps.

#### C.2 CrowdStrike — animaux par origine géographique

- **Bear** : Russie. Fancy Bear (APT28), Cozy Bear (APT29), Voodoo Bear (Sandworm), Venomous Bear (Turla), Energetic Bear (Dragonfly).
- **Panda** : Chine. Wicked Panda (APT41), Stone Panda (APT10), Judgment Panda (APT31), Vanguard Panda (Volt Typhoon).
- **Chollima** : DPRK. Stardust Chollima (APT38), Velvet Chollima (APT43), Silent Chollima (Andariel), Labyrinth Chollima.
- **Kitten** : Iran. Charming Kitten (APT35), Helix Kitten (APT34), Refined Kitten (APT33), Static Kitten (MuddyWater).
- **Buffalo** : Vietnam. OceanBuffalo (APT32).
- **Leopard** : Pakistan. Mythic Leopard (Transparent Tribe).
- **Tiger** : Inde.
- **Crane** : Corée du Sud.
- **Jackal** : hacktivisme.
- **Spider** : cybercrime. Scattered Spider, Wizard Spider.

#### C.3 Microsoft — thèmes météo par origine

Refonte en 2023 — ancienne convention (éléments chimiques : NOBELIUM, STRONTIUM) abandonnée.

- **Blizzard** : Russie. Midnight Blizzard (APT29), Forest Blizzard (APT28), Seashell Blizzard (Sandworm), Aqua Blizzard (Gamaredon), Secret Blizzard (Turla).
- **Typhoon** : Chine. Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon (APT41), Silk Typhoon (Hafnium).
- **Sleet** : DPRK. Diamond Sleet (Lazarus), Sapphire Sleet (APT38), Emerald Sleet (Kimsuky), Onyx Sleet (Andariel).
- **Sandstorm** : Iran. Peach Sandstorm (APT33), Mint Sandstorm (APT35), Hazel Sandstorm (APT34), Mango Sandstorm (MuddyWater).
- **Storm-xxxx** : cybercrime non encore promu. Storm-0558, Storm-1516.
- **Tempest** : acteurs privés / PSO.
- **Flood** : DDoS hacktivisme.
- **Tsunami** : cybercrime sophistiqué.
- **Dust** : non attribué.

#### C.4 Kaspersky

Nommage moins systématisé, souvent créatif : **Turla**, **Equation Group**, **BlueNoroff**, **ProjectSauron**, **Careto/The Mask**, **Sofacy** (APT28). Reflète l’histoire des découvertes.

#### C.5 Secureworks — métaux par origine

- **Bronze** : Chine. Bronze Butler (Tick), Bronze President (Mustang Panda), Bronze Union (APT27).
- **Cobalt** : Russie et autres, parfois Iran. Cobalt Mirage (Iran).
- **Gold** : cybercrime.
- **Iron** : Iran (partiellement).
- **Tin** : DPRK.
- **Nickel** : autres.

#### C.6 Palo Alto Networks / Unit 42

Nommage par nature plus descriptif, parfois par thématique :

- **Stately Taurus** = Mustang Panda.
- **Fighting Ursa** = APT28.
- **Mushroom Leviathan** = en lien avec APT40.
- Nommages plus variables.

#### C.7 ESET

Nommage souvent simple, parfois hérité d’autres vendors. Publications avec focus technique marqué (Industroyer, Industroyer2, CaddyWiper, NightEagle).

#### C.8 Correspondances pratiques pour l’analyste

Quand un rapport mentionne un nom inconnu :

- Rechercher sur **MITRE ATT&CK Groups** (`attack.mitre.org/groups/`) — la page de chaque groupe liste les alias connus.
- Rechercher sur **Malpedia** (`malpedia.caad.fkie.fraunhofer.de`) — base de données allemande qui consolide les correspondances.
- Consulter le **Thaicert APT Groups and Operations** (référence communautaire).
- Croiser 2-3 vendors sérieux (Mandiant, Microsoft, CrowdStrike) pour consolider la correspondance.

**Règle pratique** : noter systématiquement les alias Mandiant (APTxx) et Microsoft dans vos rapports — ce sont les deux conventions les plus largement partagées.

-----

### Annexe D — Timeline des cyberattaques étatiques (2007-2026)

Chronologie non exhaustive des événements majeurs. Sélection privilégiant les cas emblématiques et les ruptures.

|Année    |Événement                                |Acteur attribué            |Type                   |Impact / signification                                                            |
|---------|-----------------------------------------|---------------------------|-----------------------|----------------------------------------------------------------------------------|
|2007     |Cyberattaque contre l’Estonie            |Russie (attribué)          |DDoS massif            |Premier cas d’attaque étatique contre un État — institutions paralysées 3 semaines|
|2008     |Géorgie — cyberattaques pendant la guerre|Russie                     |DDoS + défacement      |Premier cas documenté de cyber + conflit militaire conventionnel                  |
|2009     |Operation Aurora                         |Chine                      |Espionnage             |Google, Adobe, Intel compromis — révélé publiquement par Google janvier 2010      |
|2010     |Stuxnet découvert                        |US + Israël (attribué)     |Sabotage OT            |Première arme cyber OT — ~1000 centrifugeuses iraniennes détruites                |
|2011     |RSA breach                               |Chine (suspecté)           |Espionnage             |Vol de données SecurID — cascade vers Lockheed Martin et autres                   |
|2012     |Shamoon v1 contre Saudi Aramco           |Iran                       |Wiper                  |30 000 postes détruits — représailles pour Stuxnet                                |
|2013     |Mandiant APT1 report                     |—                          |Publication            |Rapport fondateur exposant PLA Unit 61398                                         |
|2014     |Sony Pictures                            |DPRK (Lazarus)             |Cyber-intimidation     |Vol + publication + wiper — représailles pour *The Interview*                     |
|2014     |Annexion Crimée — cyberattaques Ukraine  |Russie                     |Multiples              |Début d’un cycle long contre l’Ukraine                                            |
|2014     |OPM breach                               |Chine                      |Espionnage massif      |21.5M dossiers d’employés fédéraux US exfiltrés                                   |
|2015     |Bundestag compromis                      |Russie (APT28)             |Espionnage             |Parlement allemand compromis plusieurs semaines                                   |
|2015     |Ukraine blackout décembre                |Russie (Sandworm)          |Sabotage OT            |Premier blackout cyber confirmé — 230 000 foyers                                  |
|2016     |Ukraine blackout décembre (Industroyer)  |Russie (Sandworm)          |Sabotage OT            |Premier malware OT dédié aux protocoles industriels                               |
|2016     |Bangladesh Bank                          |DPRK (APT38)               |Cyber-braquage         |81 M$ transférés via SWIFT                                                        |
|2016     |DNC hack                                 |Russie (APT28)             |Ingérence électorale   |Hack-and-leak via DCLeaks/WikiLeaks                                               |
|2017     |WannaCry                                 |DPRK (Lazarus)             |Ransomware worm        |200 000+ systèmes dans 150 pays — NHS affecté                                     |
|2017     |NotPetya                                 |Russie (Sandworm)          |Wiper mondial          |$10+ Mrd de dommages — cyberattaque la plus destructrice de l’histoire            |
|2017     |Triton / TRISIS                          |Russie (TsNIIKhM)          |Sabotage OT/SIS        |Première attaque documentée contre les SIS (Triconex)                             |
|2017     |Shadow Brokers leaks                     |—                          |Fuite d’outils NSA     |EternalBlue, DoublePulsar publiés                                                 |
|2017     |Equifax breach                           |Chine                      |Espionnage             |147M dossiers crédits US exfiltrés                                                |
|2017     |CCleaner supply chain                    |Chine (APT41)              |Supply chain           |2,27M machines infectées                                                          |
|2018     |Olympic Destroyer (Pyeongchang)          |Russie (Sandworm)          |Sabotage + false flags |False flags Lazarus plantés                                                       |
|2018     |Mandiant + DOJ indict APT10              |—                          |Attribution            |2 ressortissants chinois MSS Tianjin inculpés (Cloud Hopper)                      |
|2018     |Indictment 12 officiers GRU              |—                          |Attribution            |Officiers nommés pour DNC hack 2016                                               |
|2019     |Capital One breach                       |—                          |Cybercrime             |100M dossiers exposés                                                             |
|2019     |APT34 (OilRig) leak                      |Anonyme                    |Fuite iranienne        |Outils et victimes OilRig publiés sur Telegram                                    |
|2020     |SolarWinds / SUNBURST                    |Russie (APT29)             |Supply chain           |~18 000 orgs infectées, ~100 cibles actives                                       |
|2020     |Indictment APT41                         |—                          |Attribution            |5 ressortissants chinois MSS inculpés                                             |
|2020     |Ciblage vaccins COVID                    |Russie + Chine + Iran      |Espionnage             |Multiples acteurs ciblent les développeurs de vaccins                             |
|2021     |Attribution publique SolarWinds          |—                          |Attribution            |Five Eyes + UE attribuent à SVR                                                   |
|2021     |ProxyLogon / Hafnium                     |Chine (Hafnium)            |0-day massif           |30-250 000 orgs Exchange compromises mondialement                                 |
|2021     |Colonial Pipeline                        |DarkSide (criminel)        |Ransomware             |Pénuries essence côte est US                                                      |
|2021     |Kaseya supply chain                      |REvil (criminel)           |Supply chain           |Impact massif via MSP                                                             |
|2021     |Pegasus Project                          |—                          |Publication            |17 médias exposent usage NSO Pegasus contre journalistes/dissidents               |
|2021     |NSO + Candiru Entity List                |—                          |Sanctions US           |Entités israéliennes sanctionnées                                                 |
|2021     |Indictment APT40                         |—                          |Attribution            |MSS Hainan inculpé, Hainan Xiandun révélée                                        |
|2021     |Executive Order 14028 (Biden)            |—                          |Réponse structurelle   |Réponse SolarWinds — SBOM, Zero Trust fédéral                                     |
|2022     |Invasion russe Ukraine (février)         |—                          |Contexte               |Intensification massive des cyberopérations                                       |
|2022     |HermeticWiper / WhisperGate / CaddyWiper |Russie                     |Wipers                 |Vagues destructives Ukraine                                                       |
|2022     |Viasat KA-SAT (AcidRain)                 |Russie (Sandworm)          |Sabotage infrastructure|Jour-J invasion — impact collatéral 5800 éoliennes allemandes                     |
|2022     |Industroyer2                             |Russie (Sandworm)          |Tentative OT           |**Déjouée** par CERT-UA + ESET                                                    |
|2022     |Tornado Cash sanctionné OFAC             |—                          |Sanctions              |Premier smart contract sanctionné                                                 |
|2022     |Ronin Network (Axie)                     |DPRK (Lazarus)             |Vol crypto             |624 M$ — phishing LinkedIn                                                        |
|2022     |Albanie attaquée par Iran                |Iran                       |Wipers + ransomware    |Première rupture diplomatique pour cause cyber                                    |
|2022     |ContiLeaks                               |Dissident interne          |Fuite criminelle       |Échanges Conti + liens présumés FSB                                               |
|2023     |3CX supply chain                         |DPRK (Lazarus)             |Supply chain imbriquée |600 000+ clients potentiels, ciblage sélectif                                     |
|2023     |Volt Typhoon advisory                    |—                          |Attribution            |Five Eyes publient sur pré-positionnement chinois                                 |
|2023     |Microsoft Storm-0558                     |Chine                      |Breach cloud           |Emails gouvernementaux US via clé MSA compromise                                  |
|2023     |Barracuda ESG CVE-2023-2868              |Chine (UNC4841)            |Exploitation edge      |8 mois d’exploitation avant découverte                                            |
|2023     |Citrix Bleed (CVE-2023-4966)             |Multiples                  |Exploitation edge      |Vague massive, APT + ransomware                                                   |
|2023     |Operation Medusa (Snake/Turla)           |FBI                        |Démantèlement          |Neutralisation Snake malware mondiale                                             |
|2023     |Qakbot démantelé                         |FBI + Europol              |Démantèlement          |Operation Duck Hunt — 700k machines nettoyées                                     |
|2023     |Opération 7 octobre + cyber Israël       |Hamas + Iran + hacktivistes|Conflit                |Cyber dimension du conflit Israël-Hamas                                           |
|2024     |Leak i-Soon                              |Dissident interne          |Fuite                  |Écosystème contractor chinois documenté                                           |
|2024     |Ivanti CVE-2024-21887                    |Multiples APT              |0-day                  |Vague massive (Volt Typhoon, APT40, APT31)                                        |
|2024     |Microsoft compromis par APT29            |Russie (APT29)             |Identity breach        |Password spray → emails dirigeants Microsoft                                      |
|2024     |KV Botnet démantelé                      |FBI                        |Démantèlement          |Infrastructure C2 Volt Typhoon neutralisée                                        |
|2024     |LockBit démantelé (Cronos)               |NCA + FBI + Europol        |Démantèlement          |Plus grand opérateur RaaS                                                         |
|2024     |Indictment APT31 + sanctions UK/US       |—                          |Attribution coordonnée |Ciblage parlementaires UK/US                                                      |
|2024     |Advisory APT40 (AUKUS+)                  |—                          |Attribution            |AUKUS + Canada + Allemagne + Japon + Corée Sud                                    |
|2024     |NIS 2 entrée en application              |UE                         |Cadre réglementaire    |Périmètre cybersécurité massivement élargi                                        |
|2024     |EU Cyber Solidarity Act                  |UE                         |Cadre                  |Réseau SOC européens, réserve cyber                                               |
|2024     |Pall Mall Process lancé                  |UK + France                |Initiative             |Régulation PSO internationale                                                     |
|2024     |Raptor Train / Flax Typhoon démantelé    |FBI                        |Démantèlement          |260 000 dispositifs IoT compromis                                                 |
|2024     |Salt Typhoon révélé                      |—                          |Attribution            |Télécoms US compromis (Verizon, AT&T, Lumen)                                      |
|2024     |Cyber Av3ngers contre eau US             |Iran                       |Symbolique             |PLC Unitronics exposés ciblés                                                     |
|2024     |Advisory Unit 29155                      |—                          |Attribution            |GRU Unit 29155 publiquement documentée                                            |
|2024     |Salt Typhoon accès interception légale   |Chine                      |Espionnage stratégique |Lawful intercept systems compromis                                                |
|2025     |Bybit hack                               |DPRK (Lazarus)             |Vol crypto             |**~1,5 Mrd$** — plus gros vol crypto de l’histoire                                |
|2025     |Integrity Technology Group sanctionné    |—                          |Sanctions OFAC         |Contractor chinois sanctionné (Flax Typhoon)                                      |
|2025-2026|Vagues edge continues                    |Multiples                  |Exploitation           |Palo Alto, Fortinet, Cisco vulnérabilités exploitées                              |

-----

### Annexe E — Mapping ATT&CK par acteur

*Techniques ATT&CK les plus caractéristiques de 15 groupes majeurs. Les techniques marquées en gras sont les signatures distinctives. Liste simplifiée — la matrice complète pour chaque acteur est sur MITRE ATT&CK Groups.*

|Acteur                         |Initial Access                                             |Execution                                      |Persistence                                       |Cred Access                                       |Lateral Movement            |C2                                                 |Impact / Signature                                        |
|-------------------------------|-----------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|--------------------------------------------------|----------------------------|---------------------------------------------------|----------------------------------------------------------|
|**APT29** (Russie/SVR)         |**T1195.002** Supply chain, **T1566** OAuth phishing, T1078|T1218 Signed binary proxy, T1059.001 PowerShell|**T1550.001** SAML tokens, T1098 Application OAuth|T1003 Credential dumping, T1110.003 Password spray|**GoldenSAML**, T1021       |T1071.001 HTTPS, **T1102** Services cloud légitimes|Furtivité extrême, cloud-focused                          |
|**APT28** (Russie/GRU 26165)   |**T1566.001** Spear-phishing, T1190                        |T1059.001 PowerShell, scripts                  |T1543.003 Services, T1547 Registry                |**T1003.001** Mimikatz, credential harvest        |T1021.001 RDP, T1021.002 SMB|T1071.001 HTTPS, T1102                             |Exploitation 0-day Outlook                                |
|**Sandworm** (Russie/GRU 74455)|**T1195** Supply chain, T1190 Edge exploit                 |T1059, custom malware                          |**T1543.003** Services, T1053 Scheduled tasks     |T1003 Mimikatz                                    |T1021 PsExec, T1047 WMI     |T1071.001 HTTPS, custom                            |**T1485 Data Destruction, T1561 Disk Wipe**, OT protocoles|
|**Unit 29155** (Russie/GRU)    |T1190, T1566                                               |T1059, Impacket                                |T1543, T1053                                      |T1003 Mimikatz                                    |T1021                       |T1071.001                                          |T1485/T1561 Wipers (WhisperGate)                          |
|**Turla** (Russie/FSB)         |**T1189** Watering hole, T1195                             |T1059, **rootkits kernel**                     |**T1542 Firmware**, T1014 Rootkits                |Custom tools                                      |T1090 Proxies satellite     |**T1102** Satellite détournement, piggybacking     |Sophistication extrême                                    |
|**APT41** (Chine/MSS)          |**T1195** Supply chain, T1190                              |Custom malware                                 |**T1542 Bootkits** (MoonBounce), T1014            |T1003                                             |T1021.001 RDP, T1021.002 SMB|T1071.001 HTTPS                                    |**Double mission** espionnage + cybercrime                |
|**APT40** (Chine/MSS Hainan)   |**T1190** Edge appliances                                  |Scripts, web shells                            |**T1505.003** Web shells                          |T1003                                             |T1021 SMB, RDP              |T1071.001                                          |Exploitation rapide CVE                                   |
|**APT10** (Chine/MSS Tianjin)  |**T1199** Trusted relationship (MSP)                       |Custom malware                                 |T1543.003, T1547                                  |T1003                                             |T1021                       |T1071.001                                          |MSP-based supply chain                                    |
|**Volt Typhoon** (Chine)       |**T1190** Edge devices                                     |**T1059 LotL exclusif**                        |T1078 Valid accounts                              |T1003 ntdsutil                                    |T1021.001 RDP avec LoTL     |**Routeurs SOHO compromis** (T1584.008)            |**Pas de malware custom**, pré-positionnement             |
|**Salt Typhoon** (Chine)       |T1190                                                      |T1059                                          |T1542 Firmware télécoms                           |T1003                                             |T1021                       |T1071                                              |**Lawful Intercept Systems**                              |
|**Lazarus** (DPRK)             |**T1566** Social engineering LinkedIn, T1195 Supply chain  |Custom malware multi-OS                        |T1543, T1547                                      |T1003, keyloggers                                 |T1021                       |T1071.001 HTTPS, custom                            |**Vol crypto**, AppleJeus                                 |
|**APT38** (DPRK/BlueNoroff)    |**T1566** Finance social eng                               |Custom malware                                 |T1543                                             |Custom                                            |T1021                       |T1071                                              |**SWIFT**, DeFi exploits                                  |
|**APT35** (Iran/IRGC)          |**T1566 Ultra-social eng**, faux LinkedIn                  |Scripts, backdoors légers                      |T1547 Registry, T1543                             |T1056 Credential phishing                         |Minimal                     |T1071.001                                          |**Impersonation individuelle extrême**                    |
|**APT33** (Iran/IRGC)          |**T1110.003 Password spraying** massif                     |T1059 PowerShell                               |T1543 Services                                    |T1110.003                                         |T1021.001 RDP               |T1071.001                                          |Volume, énergie                                           |
|**MuddyWater** (Iran/MOIS)     |T1566 Phishing                                             |**T1059.001 PowerShell obfusqué**              |T1547                                             |T1003                                             |T1021                       |T1071                                              |Outils open source                                        |

Pour consulter la matrice complète de chaque acteur : **attack.mitre.org/groups/**.

-----

### Annexe F — Malwares et implants emblématiques

Catalogue des malwares les plus significatifs par acteur, avec fonction principale et signification. Non exhaustif.

#### F.1 Russie — APT29 (SVR)

- **SUNBURST** (2020) : backdoor injectée dans SolarWinds Orion. Compilée directement dans les builds légitimes via compromission du pipeline de build. Communications C2 DNS camouflées en requêtes Orion Improvement Program.
- **TEARDROP** / **RAINDROP** : loaders en mémoire déployés en phase 2 après SUNBURST. Minimal footprint, exécution en mémoire.
- **GoldMax / SUNSHUTTLE** : backdoor Go cross-platform. Rare pour sa sophistication et son langage (Go est peu courant dans le malware APT).
- **GoldFinder** : HTTP tracer pour reconnaissance d’infrastructure de victime.
- **FoggyWeb** : backdoor ADFS post-exploitation (2021). Communications via cookies Exchange calibrés.
- **MagicWeb** (2022) : backdoor ADFS évolution de FoggyWeb. Manipulation de la gestion des certificats pour forgeage d’authentification.

#### F.2 Russie — APT28 (GRU 26165)

- **X-Tunnel** : proxy tunneling utilisé pour le mouvement latéral.
- **XAgent** : backdoor modulaire cross-platform (Windows, macOS, iOS, Android — l’une des rares familles APT avec présence mobile).
- **Zebrocy** : famille de backdoors développée en multiples langages (Delphi, Go, Python, C++) — tradecraft inhabituel qui complique l’analyse.
- **Seduploader** : implant léger.
- **CredoMap** : stealer de credentials.
- **Cannon** : backdoor Office.

#### F.3 Russie — Sandworm (GRU 74455)

- **BlackEnergy** : framework utilisé dans les attaques Ukraine 2015 (historique, bien documenté).
- **Industroyer / CrashOverride** (2016) : premier malware OT spécifiquement conçu pour attaquer les protocoles industriels (IEC 60870-5-104, IEC 61850, OPC DA).
- **Industroyer2** (2022) : évolution tentée, déjouée par CERT-UA et ESET.
- **NotPetya / ExPetr** (2017) : wiper masqué en ransomware. Propagation via EternalBlue + credentials.
- **CaddyWiper** (2022) : wiper déployé contre l’Ukraine.
- **HermeticWiper / FoxBlade** (février 2022) : wiper déployé la veille de l’invasion.
- **IsaacWiper** (février 2022) : wiper concurrent.
- **AcidRain** (février 2022) : wiper contre terminaux satellite Viasat KA-SAT.
- **CaddyWiper**, **WhisperKill**, **Double-Zero** (2022) : autres variants de wipers.
- **CosmicEnergy** (2023) : malware OT découvert par Mandiant via VirusTotal, capacités IEC 60870-5-104.
- **Cyclops Blink** (2022) : botnet sur routeurs ASUS et WatchGuard, démantelé par le FBI.

#### F.4 Russie — Unit 29155

- **WhisperGate** (janvier 2022) : wiper déployé contre l’Ukraine quelques semaines avant l’invasion. Masqué en ransomware (note de rançon factice).

#### F.5 Russie — Turla (FSB Centre 16)

- **Snake / Uroburos** : rootkit multi-plateforme (Windows, Linux, macOS). Actif depuis au moins 2003. **Démantelé par le FBI en mai 2023 (opération Medusa)**.
- **Kazuar** : backdoor modulaire .NET.
- **LightNeuron** : backdoor Exchange serveur (transport agent malveillant) — intercepte les emails au niveau serveur.
- **Crutch** : backdoor Windows.
- **Carbon / Cobra** : framework modulaire historique.
- **ComRAT** : backdoor .NET, une des plus anciennes familles Turla.

#### F.6 Chine — APT41

- **Winnti** : famille d’implants Windows/Linux, la signature historique du groupe. Multiples variants depuis les années 2010.
- **ShadowPad** : backdoor modulaire sophistiquée, utilisée par plusieurs APT chinoises.
- **PipeMon** : modulaire.
- **Crosswalk** : RAT.
- **MoonBounce** (découvert par Kaspersky) : **bootkit UEFI**. Persistence au niveau firmware. Sophistication extrême.
- **HyperBro** : backdoor Windows (aussi utilisée par APT27).

#### F.7 Chine — autres APT chinoises

- **PlugX** : famille historique largement partagée entre APT chinoises (APT10, APT27, Mustang Panda, autres). Variants multiples.
- **ChChes** (APT10) : backdoor.
- **Redleaves** (APT10).
- **UPPERCUT** (APT10).
- **HAYMAKER** (APT10).
- **ToneShell** / **Hodur** (Mustang Panda) : évolutions récentes.
- **SysUpdate** (APT27) : backdoor.
- **ZxShell** (APT27) : RAT.

#### F.8 DPRK — Lazarus et sous-groupes

- **FALLCHILL** : backdoor Windows.
- **BADCALL** : backdoor.
- **HOPLIGHT** : backdoor avec proxy.
- **DTrack** : backdoor.
- **AppleJeus** : **malware macOS** ciblant les utilisateurs crypto (l’une des rares familles APT ciblant macOS avec profondeur).
- **Manuscrypt / NukeSped** : backdoors Windows.
- **TAINTEDSCRIBE** : downloader.
- **CROWDEDFLOUNDER** : RAT.
- **VHD Ransomware** : rare — Lazarus a déployé du ransomware ciblé ponctuellement.

#### F.9 Iran

- **Shamoon v1/v2/v3** (APT33) : wipers destructifs. Saudi Aramco 2012 (30 000 postes détruits).
- **ZeroCleare** : wiper proche de Shamoon.
- **Dustman** : wiper.
- **StoneDrill** : wiper apparenté à Shamoon.
- **QUADAGENT** (APT34/OilRig) : backdoor.
- **OopsIE** (APT34) : backdoor.
- **Helminth** (APT34) : backdoor.
- **BabyShark** (Kimsuky — attention, il existe plusieurs malwares appelés ainsi, vérifier le contexte).
- **Liderc** (APT35) : backdoor.
- **Apostle / DEADWOOD / Moneybird** (Agrius) : wipers sous fausses bannières.

#### F.10 Mercenaires cyber

- **Pegasus** (NSO Group) : spyware mobile, iOS et Android. Capacités complètes (messages E2EE lus en post-déchiffrement, micro/caméra, géoloc).
- **Predator** (Intellexa) : spyware mobile concurrent de Pegasus.
- **DevilsTongue** (Candiru) : spyware desktop Windows.
- **Reign** (QuaDream — société fermée en 2023 suite aux révélations Citizen Lab) : spyware mobile.
- **Graphite** (Paragon) : spyware mobile récent.

#### F.11 Outils offensifs commerciaux / open source massivement utilisés

- **Cobalt Strike** : plateforme C2 commerciale, largement « crackée ». Utilisée par la quasi-totalité des APT et groupes ransomware.
- **Brute Ratel C4** : concurrent commercial, cracké également.
- **Sliver** (BishopFox, open source) : framework C2 open source.
- **Havoc** : framework open source récent.
- **Mythic** : plateforme C2 modulaire open source.
- **Metasploit** : pentest framework historique.
- **Empire / PowerShell Empire** : C2 PowerShell historique.
- **Mimikatz** : credential dumping, utilisé universellement.
- **BloodHound / SharpHound** : énumération AD, utilisée par red teams et APT.
- **Impacket** : toolkit Python pour protocoles Windows, utilisation massive.
- **Rubeus** : outil Kerberos.
- **NanoDump, SafetyKatz, SharpKatz** : alternatives furtives à Mimikatz.

**Leçon importante** : la détection d’un de ces outils **ne discrimine rien sur l’acteur** — l’outil est partagé. L’attribution repose sur comment l’outil est utilisé, dans quelle séquence, avec quelles autres techniques, et contre quelle cible.

-----

### Annexe G — Cadres juridiques et réglementaires par juridiction

Cette annexe consolide les cadres juridiques, institutions, et qualifications mentionnés dans le cours. L’objectif est d’offrir un référentiel pour l’analyste confronté à un incident APT et devant naviguer dans les obligations et les points de contact pertinents.

#### G.1 France

**ANSSI** — Agence nationale de la sécurité des systèmes d’information. Créée en 2009, rattachée au SGDSN (Secrétariat général de la défense et de la sécurité nationale). Mission : défense et sécurité des SI de l’État et des OIV, qualification de produits et prestataires, pilotage CERT-FR, coopération internationale. **N’a pas de mandat offensif** — pure posture défensive et d’accompagnement.

**COMCYBER** — Commandement de la cyberdéfense, créé en 2017 au sein du ministère des Armées. Mission : défense des systèmes militaires, **conduite des opérations cyber offensives (LIO)** pour le compte de l’État. Le COMCYBER intègre les capacités des trois armées et de la DGSE sur le volet cyber militaire.

**DGSE** — Direction générale de la sécurité extérieure. Service de renseignement extérieur rattaché au ministère des Armées. Dispose de capacités cyber intégrées à ses opérations, notamment pour le renseignement technique à l’étranger.

**DGSI** — Direction générale de la sécurité intérieure. Service de renseignement intérieur rattaché au ministère de l’Intérieur. Mission cyber : contre-espionnage cyber, contre-ingérence, investigation des menaces cyber contre la France.

**DRSD** — Direction du renseignement et de la sécurité de la défense. Service de contre-espionnage militaire, ministère des Armées.

**Coordinateur national pour le renseignement et la lutte contre le terrorisme (CNRLT)** : coordonne la communauté française du renseignement à l’Élysée.

**C4** — Centre de Coordination des Crises Cyber. Créé en 2021. Réunit ANSSI, COMCYBER, DGSE, DGSI, Police/Gendarmerie pour la coordination opérationnelle lors des crises cyber majeures.

**Doctrine cyber française** (publiée 2019) :

- **LID** (Lutte Informatique Défensive) : ANSSI.
- **LIO** (Lutte Informatique Offensive) : COMCYBER + DGSE.
- **L2I** (Lutte Informatique d’Influence) : contre-ingérence informationnelle.

**OIV** — Opérateurs d’Importance Vitale. Cadre juridique : Code de la défense, articles **L.1332-1 et suivants**. Créé par la loi de programmation militaire (LPM) de 2013.

- **12 secteurs d’activité d’importance vitale (SAIV)** : alimentation, communications électroniques/audiovisuel, eau, énergie, espace, finances, industrie, santé, transport, auxiliaires de l’État, services judiciaires, activités économiques et sociales de l’État.
- **~300 OIV** désignés en France (liste classifiée).
- Obligations : notification des incidents à l’ANSSI, règles de sécurité spécifiques selon secteur, audits ANSSI, homologation des systèmes d’information d’importance vitale (SIIV).

**Qualifications ANSSI** — label de confiance pour les prestataires :

- **PASSI** — Prestataire d’Audit SSI. Qualifie les prestataires réalisant des audits de sécurité pour les OIV et administrations.
- **PDIS** — Prestataire de Détection d’Incidents de Sécurité. Qualifie les SOC/CSIRT externes.
- **PRIS** — Prestataire de Réponse aux Incidents de Sécurité. Qualifie les prestataires d’investigation et de réponse.
- **PACS** — Prestataire d’Accompagnement et de Conseil en Sécurité.
- **SecNumCloud** — Qualification des services cloud de confiance. Exige un ancrage européen (propriété, législation applicable) et des niveaux de sécurité stricts. Durcie en version 3.2 en 2022.

**Textes additionnels** :

- **Code pénal** : infractions d’atteinte aux STAD (systèmes de traitement automatisé de données) — articles **323-1 à 323-8**.
- **Loi informatique et libertés** + **RGPD** : notification CNIL des violations de données personnelles sous 72h.
- **LPM 2024-2030** : renforcement des pouvoirs cyber offensifs français, capacités nouvelles.

**Contacts opérationnels** :

- **CERT-FR** : cert.ssi.gouv.fr — publication d’advisories, alerte et accompagnement.
- **Plateforme de signalement** : signalements.ssi.gouv.fr pour les OIV et administrations.
- **Cybermalveillance.gouv.fr** : plateforme grand public et PME.

#### G.2 Union européenne

**ENISA** — European Union Agency for Cybersecurity. Agence de coordination cybersécurité européenne, basée à Athènes/Héraklion. Mission : expertise technique, coordination, publication de rapports (Threat Landscape annuel), organisation d’exercices (Cyber Europe tous les 2 ans), certification cybersécurité européenne.

**CERT-EU** — CSIRT des institutions, organes et agences de l’UE. Couvre Commission, Parlement, Conseil, agences.

**Directive NIS 2** — Directive (UE) 2022/2555, entrée en application octobre 2024. Successeur de NIS 1 (2016).

- **Périmètre** : 18 secteurs (énergie, transport, banque, santé, eau, infrastructures numériques, administration publique, espace, services postaux, gestion des déchets, produits chimiques, alimentation, fabrication, fournisseurs numériques, recherche, etc.).
- **Deux niveaux** : **Entités Essentielles (EE)** et **Entités Importantes (EI)** avec obligations différenciées.
- **Obligations principales** :
  - Mesures techniques, opérationnelles et organisationnelles (art. 21) : gestion des risques, IR, continuité, supply chain, MFA, chiffrement, etc.
  - **Notification d’incidents** : early warning sous 24h, notification détaillée sous 72h, rapport final dans un mois.
  - **Gouvernance** : responsabilité direct au niveau direction (board), formation des dirigeants.
  - **Supply chain** : évaluation des risques fournisseurs.
- **Sanctions** : jusqu’à **10 M€ ou 2% du CA mondial** pour les EE, 7 M€ ou 1,4% pour les EI.
- **Transposition** : États membres, avec variations nationales (en France, transposition en cours au moment de la rédaction, avec l’ANSSI comme autorité compétente).

**EU Cyber Solidarity Act** — adopté 2024 :

- **Réseau européen de SOC** (European Cybersecurity Shield) : coordination de SOC nationaux pour détection et partage.
- **Mécanisme de réponse d’urgence** (Cyber Emergency Mechanism) : activation en crise majeure, assistance aux États membres.
- **Réserve cyber européenne** : experts privés mobilisables par l’UE en crise.

**Cyber Resilience Act** — adopté 2024. Obligations de cybersécurité pour les produits connectés (IoT, logiciels) mis sur le marché européen. Responsabilité des fabricants, gestion des vulnérabilités sur cycle de vie, notification de vulnérabilités exploitées.

**EU Cyber Sanctions Regime** — règlement (UE) 2019/796. Cadre permettant des sanctions ciblées (gel des avoirs, interdictions de voyager) contre des personnes et entités impliquées dans des cyberattaques. Utilisé contre opérateurs GRU, MSS, acteurs biélorusses, etc.

**Digital Operational Resilience Act (DORA)** — règlement 2022/2554, applicable janvier 2025. Cadre spécifique au secteur financier : gestion des risques ICT, tests de résilience, gestion des prestataires ICT critiques.

**eIDAS 2** — règlement sur l’identité numérique européenne.

**Data Act, Digital Services Act (DSA), Digital Markets Act (DMA)** : autres règlements structurants qui touchent indirectement la cybersécurité (gouvernance des données, responsabilités plateformes, concurrence numérique).

#### G.3 États-Unis

**Agences cyber fédérales principales** :

- **CISA** — Cybersecurity and Infrastructure Security Agency, DHS. Coordination civile, advisories, KEV, protection des infrastructures critiques.
- **NSA** — National Security Agency. SIGINT mondiale, capacités cyber offensives, advisories conjoints.
- **USCYBERCOM** — US Cyber Command, DoD. Combatant command cyber, opérations militaires.
- **FBI** — Federal Bureau of Investigation. Law enforcement cyber, investigations, démantèlements, indictments.
- **DOJ** — Department of Justice. Poursuites pénales, indictments formels.
- **OFAC** — Office of Foreign Assets Control, Treasury. Sanctions économiques.
- **NSC Cyber Directorate** — Maison Blanche, coordination stratégique.
- **ODNI** — Office of the Director of National Intelligence. Coordination renseignement fédéral.

**Directives et Executive Orders** :

- **Presidential Policy Directive 21 (PPD-21)** — 2013 — définit les 16 **Critical Infrastructure Sectors**.
- **Executive Order 13800** (2017, Trump) : Strengthening Cybersecurity of Federal Networks.
- **Executive Order 14028** (mai 2021, Biden) : Improving the Nation’s Cybersecurity. Réponse à SolarWinds. **SBOM** obligatoire, Zero Trust fédéral, EDR généralisé, partage renforcé.
- **EO sur les spywares commerciaux** (mars 2023) : restreint l’acquisition de spywares commerciaux par le gouvernement fédéral.
- **National Cybersecurity Strategy** (mars 2023) : doctrine consolidée de l’administration Biden.

**Binding Operational Directives (BOD) CISA** — contraintes pour les agences fédérales. Exemples :

- **BOD 22-01** : Known Exploited Vulnerabilities catalogue — obligation de patch dans les délais fixés.
- **BOD 23-01** : Improving Asset Visibility and Vulnerability Detection.
- **BOD 23-02** : Mitigating the Risk from Internet-Exposed Management Interfaces.

**Lois cyber principales** :

- **Computer Fraud and Abuse Act (CFAA)** — loi pénale cyber historique (1986), base des poursuites cyber.
- **Cybersecurity Information Sharing Act (CISA Act)** — 2015, partage public-privé.
- **Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA)** — 2022, obligations de notification pour les infrastructures critiques (règles finales CISA en cours).
- **Executive Order sur les télécoms étrangers** : restrictions Huawei, ZTE.

**Indictments et sanctions — acteurs ciblés** :

- **Indictments DOJ notables** : Unit 61398/PLA (2014), APT10/MSS Tianjin (2018), APT28/GRU (2018), APT41 (2020), APT40/MSS Hainan (2021), APT31/MSS Hubei (2024), multiples opérateurs DPRK et iraniens.
- **Sanctions OFAC notables** : Tornado Cash (2022), Integrity Technology Group (2025), multiples adresses crypto Lazarus, entités NSO Group + Intellexa + Candiru (via Entity List Commerce), multiples ressortissants russes/chinois/iraniens/nord-coréens.
- **Entity List Commerce** : Huawei (2019), Hikvision, Dahua, NSO, Candiru, ZTE, etc.

**Cyber Safety Review Board (CSRB)** — créé 2022. Investigue les incidents cyber majeurs, publie des rapports publics. Rapports publiés : Log4j (2022), Lapsus$ (2023), Storm-0558/Microsoft (2024).

#### G.4 Royaume-Uni

**NCSC** — National Cyber Security Centre. Branche publique du GCHQ, créée en 2016. Modèle de référence internationale. Publications (Annual Review, Active Cyber Defence programme, Cyber Essentials), accompagnement, advisories.

**GCHQ** — Government Communications Headquarters. Agence SIGINT historique, Cheltenham. Partenaire central NSA dans Five Eyes.

**NCF** — National Cyber Force. Créée publiquement en 2020. Branche cyber offensive britannique, regroupe personnels GCHQ + MoD + MI6/SIS. Doctrine de « disruption by design ».

**MI5 / Security Service** : contre-espionnage intérieur, incluant dimension cyber.

**MI6 / SIS** : renseignement extérieur, capacités cyber intégrées aux opérations clandestines.

**NCA** — National Crime Agency. Law enforcement, incluant National Cyber Crime Unit. Lead sur des démantèlements comme LockBit (Operation Cronos 2024).

**Textes** :

- **Computer Misuse Act** (1990) : base pénale cyber UK.
- **Investigatory Powers Act** (2016) : cadre des capacités d’interception.
- **National Cyber Strategy 2022-2030**.
- **Network and Information Systems Regulations (NIS Regulations 2018)** : transposition NIS 1, en cours d’actualisation pour refléter NIS 2 (le UK étant post-Brexit, la transposition NIS 2 n’est pas automatique).

**Computer Crime Act** et **Data Protection Act** + **UK GDPR** encadrent également le domaine.

#### G.5 Allemagne

**BSI** — Bundesamt für Sicherheit in der Informationstechnik. Agence fédérale cybersécurité, équivalent allemand de l’ANSSI. Bonn.

**BfV** — Bundesamt für Verfassungsschutz. Office fédéral de protection de la Constitution (contre-espionnage intérieur).

**BND** — Bundesnachrichtendienst. Service fédéral de renseignement extérieur.

**BKA** — Bundeskriminalamt. Office fédéral de police criminelle.

**Zentrale Stelle für Informationstechnik im Sicherheitsbereich (ZITiS)** : support technique aux services de sécurité allemands.

**KRITIS** : cadre des infrastructures critiques allemandes. Secteurs définis et obligations de notification.

#### G.6 OTAN

**Reconnaissance du cyber comme 5ème domaine d’opérations** — sommet de Varsovie, 2016.

**NATO Cyber Operations Centre (CyOC)** — créé 2018, intègre le cyber dans la planification militaire OTAN.

**CCDCOE** — Cooperative Cyber Defence Centre of Excellence, Tallinn (Estonie). Créé en 2008. Think tank OTAN sur le cyber. Pilote :

- Le **Manuel de Tallinn** (1.0 en 2013, 2.0 en 2017, 3.0 en cours) — interprétation du droit international appliqué au cyber. Non-contraignant mais référence majeure.
- L’exercice **Locked Shields** annuel — plus grand exercice de red/blue team au monde.
- Publications académiques et techniques.

**Article 5 et cyber** : reconnu applicable au cyber depuis 2014. Seuil de déclenchement délibérément non défini (ambiguïté stratégique). Jamais déclenché pour un incident cyber à date.

**NATO Communications and Information Agency (NCIA)** : bras technique cyber OTAN.

#### G.7 ONU

**GGE** — Group of Governmental Experts on Developments in the Field of Information and Telecommunications in the Context of International Security. Groupe restreint d’experts gouvernementaux. Rapports consensuels 2013 et 2015 affirmant que le droit international s’applique au cyber.

**OEWG** — Open-Ended Working Group. Créé 2018, plus inclusif (tous États membres). Rapports 2021 et 2024, plus divisifs politiquement.

**Groupes de positions structurants** :

- **Bloc occidental** : normes existantes s’appliquent, focus sur comportements responsables, multistakeholderisme.
- **Bloc Russie-Chine** : nouveau traité nécessaire, concept de « sécurité de l’information » incluant contrôle du contenu, multilatéralisme strict (États seuls).

**UN Convention on Cybercrime** — négociée sous leadership russe, adoptée en 2024. Controversée — critiques des démocraties et de la société civile sur les risques pour les droits humains, la définition large des infractions, les capacités de coopération qui pourraient servir à la répression transfrontalière.

#### G.8 Pall Mall Process

Lancé à Londres en février 2024, conjointement par le **Royaume-Uni et la France**. Initiative internationale de régulation des capacités cyber offensives commerciales (spywares, outils offensifs).

**Préoccupation centrale** : l’usage abusif de ces outils contre des journalistes, dissidents, opposants politiques, défenseurs des droits humains.

**Signataires initiaux** (déclaration de Londres, février 2024) : plus de **40 États**. Puis d’autres rounds avec nouveaux signataires.

**Entreprises cosignataires** : Apple, Google, Meta, Microsoft, BAE Systems et plusieurs autres. ONG également partie prenante (Citizen Lab, Access Now, etc.).

**Principes affirmés** :

- Usage des capacités cyber commerciales dans le respect du droit international et des droits humains.
- Responsabilité des États sur les usages de capacités qu’ils acquièrent.
- Transparence relative sur les acquisitions étatiques.
- Sanctions contre les entreprises documentées pour usages abusifs.

**Limites** :

- Non-contraignant juridiquement.
- Plusieurs États majeurs (clients importants de NSO et pairs) non signataires — Israël notamment, ainsi que plusieurs pays du Golfe, d’Asie centrale, d’Afrique.
- Effet dépend de la mise en œuvre nationale.

**Suivis** : rounds réguliers, élaboration de cadres plus opérationnels, extension des signataires.

#### G.9 Synthèse pour l’analyste

Face à un incident APT, l’analyste mobilise les cadres pertinents selon plusieurs axes.

**Si l’incident touche un OIV français** :

- Notification ANSSI obligatoire.
- Coordination CERT-FR.
- Éventuelle remontée C4 si gravité élevée.
- Respect des règles de sécurité OIV applicables au secteur.

**Si l’incident touche une entité NIS 2** :

- Notification autorité nationale compétente sous 24h (early warning).
- Notification détaillée sous 72h.
- Rapport final sous un mois.
- Éventuelles sanctions administratives en cas de manquement aux mesures de sécurité.

**Si données personnelles affectées** :

- Notification CNIL (en France) sous 72h, RGPD art. 33.
- Communication aux personnes concernées si risque élevé (art. 34).

**Si attribution à acteur sanctionné** :

- Vérification des obligations OFAC (pour les entités ayant des liens US) — interdiction de paiement de rançon à entité sanctionnée.
- Vérification des sanctions UE équivalentes.

**Si l’incident touche plusieurs juridictions** :

- Coordination ANSSI + autorités des autres pays.
- Éventuelle remontée ENISA pour coordination européenne.
- Partage international selon TLP via FIRST, ISAC international.

**Pour la défense proactive** :

- Suivi des advisories CERT-FR, CISA, NCSC, BSI, ENISA.
- Monitoring KEV CISA et équivalents.
- Participation ISAC sectoriel.
- Qualification des prestataires (PASSI, PDIS, PRIS) pour les missions critiques.
- Conformité NIS 2 / LPM / ISO 27001 / référentiels sectoriels.

-----

### Annexe H — Ressources et formation

Cette annexe consolide les ressources essentielles pour un analyste CTI/SOC travaillant sur les APT. Sélection non exhaustive — privilégie les sources de qualité établie.

#### H.1 Rapports annuels et périodiques de référence

**Rapports annuels vendors** (tous gratuits et téléchargeables) :

- **Mandiant M-Trends** : publication annuelle depuis 2011. Synthèse des incidents IR traités par Mandiant, tendances des APT, dwell time moyen. Référence centrale.
- **CrowdStrike Global Threat Report (GTR)** : publication annuelle, synthèse des acteurs et tendances.
- **Microsoft Digital Defense Report (DDR)** : publication annuelle depuis 2020. Volume massif, vision cloud (M365, Azure).
- **Verizon Data Breach Investigations Report (DBIR)** : publication annuelle depuis 2008. Données statistiques sur les breaches, vision plus large que les APT stricts.
- **ENISA Threat Landscape** : publication annuelle ENISA, vision européenne.
- **ANSSI Panorama de la cybermenace** : publication annuelle ANSSI, perspective française.
- **NCSC Annual Review** (UK) : publication annuelle NCSC.
- **CISA Year in Review** : publication annuelle CISA.
- **Kaspersky APT Reports** : rapports trimestriels et ad hoc.
- **ESET Threat Report** : publication biannuelle, forte visibilité Europe centrale/orientale.
- **Europol IOCTA** — Internet Organised Crime Threat Assessment, publication annuelle. Focus cybercrime mais avec zones de chevauchement APT.
- **Recorded Future Annual Report** : publication annuelle.
- **Unit 42 (Palo Alto) Incident Response Report** : publication annuelle, données IR.
- **Chainalysis Crypto Crime Report** : publication annuelle, centrale pour le volet crypto/Lazarus.
- **TRM Labs / Elliptic reports** : publications régulières sur les flux illicites crypto.

**Rapports sectoriels** :

- **Dragos Year in Review** : publication annuelle Dragos, focus OT/ICS.
- **Claroty Biannual ICS Risk & Vulnerability Report**.
- **FS-ISAC** : rapports sectoriels finance.
- **H-ISAC** : rapports sectoriels santé.

**Rapports thématiques majeurs** :

- **Pegasus Project** (2021) — Forbidden Stories + 17 médias — usage NSO Pegasus.
- **Leak i-Soon analyses** (2024) — multiple vendors (SentinelOne, Sekoia, Harfang Lab).
- **ContiLeaks analyses** (2022) — multiples chercheurs indépendants.
- **Citizen Lab reports** — University of Toronto — référence internationale sur spywares et surveillance.

#### H.2 Formations certifiantes

**SANS Institute** (gold standard) :

- **FOR578 — Cyber Threat Intelligence** : formation de référence CTI. Enseignants majeurs du domaine (Rebekah Brown, Scott Roberts, Ryan Fetterman). Certification **GCTI**.
- **FOR508 — Advanced Incident Response, Threat Hunting, and Digital Forensics**. Certification **GCFA**.
- **FOR572 — Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response**. Certification **GNFA**.
- **ICS515 — ICS Active Defense and Incident Response** : formation phare OT. Enseignants Dragos (Robert M. Lee). Certification **GRID**.
- **ICS456 — Essentials for NERC Critical Infrastructure Protection** : focus réglementaire NERC CIP (US électricité).
- **FOR528 — Ransomware and Cyber Extortion for Incident Responders**.
- **FOR608 — Enterprise-Class Incident Response & Threat Hunting**.
- **SEC599 — Defeating Advanced Adversaries**.
- **SEC504 — Hacker Tools, Techniques, and Incident Handling**.

**Offensive Security** :

- **OSCP** (Offensive Security Certified Professional) : certification offensive de référence, base du pentest.
- **OSEP** (Offensive Security Experienced Penetration Tester) : niveau plus avancé.
- **OSED** (Offensive Security Exploit Developer).

**EC-Council** :

- **CEH** (Certified Ethical Hacker) — largement reconnu mais considéré comme moins rigoureux que OSCP par les praticiens.
- **CTIA** (Certified Threat Intelligence Analyst).
- **CHFI** (Computer Hacking Forensic Investigator).

**ISC2** :

- **CISSP** (Certified Information Systems Security Professional) — management sécurité.
- **CCSP** (Certified Cloud Security Professional).
- **CCFP** (Certified Cyber Forensics Professional).

**ISACA** :

- **CISM** (Certified Information Security Manager) — management.
- **CISA** (Certified Information Systems Auditor) — audit.
- **CRISC** (Certified in Risk and Information Systems Control).

**Mandiant Academy** : formations spécifiques (CTI, IR, malware analysis).

**CrowdStrike University** : formations internes et ouvertes.

**SECO Institute** (Europe) : certifications cybersécurité européennes.

**Formations françaises** :

- **CNAM** : master cybersécurité.
- **Télécom Paris / Télécom SudParis / INSA** : masters spécialisés.
- **Centrale-Supélec** : formation continue et formations initiales.
- **ESIEA, EPITA, EPITECH** : formations ingénieur avec spécialisations cyber.
- **EC-Conseil** : formations ANSSI orientées.

#### H.3 Bases de données et plateformes techniques

**MITRE — référence absolue** :

- **MITRE ATT&CK** : attack.mitre.org — framework TTP. Sections Enterprise, Mobile, ICS (OT).
- **MITRE ATT&CK Groups** : attack.mitre.org/groups/ — page par groupe avec TTP associées et alias.
- **MITRE CTI GitHub** : github.com/mitre/cti — export STIX des données ATT&CK.
- **MITRE D3FEND** : d3fend.mitre.org — contre-framework défensif aligné sur ATT&CK.
- **MITRE Engage** : cadre pour deception.
- **MITRE Shield** (remplacé par Engage) : cadre historique de defensive cyber operations.
- **CTI Blueprints** : github.com/center-for-threat-informed-defense — méthodologies.

**Malware et samples** :

- **Malpedia** : malpedia.caad.fkie.fraunhofer.de — base consolidée par Fraunhofer FKIE, mapping famille/acteur.
- **VirusTotal** : virustotal.com — Google. Intelligence sur fichiers, URLs, domaines, IPs.
- **Hybrid Analysis** : hybrid-analysis.com — sandboxing public.
- **Any.run** : any.run — sandboxing interactif.
- **Joe Sandbox** : joesandbox.com — analyse dynamique.
- **Triage** : tria.ge — Hatching (Recorded Future).
- **VX-Underground** : vx-underground.org — archives malware historiques.

**Intelligence / reconnaissance** :

- **Shodan** : shodan.io — recherche appliances exposées Internet.
- **Censys** : censys.io — concurrent de Shodan.
- **ZoomEye** : zoomeye.org — équivalent chinois.
- **FOFA, Quake** : équivalents chinois.
- **GreyNoise** : greynoise.io — caractérisation du bruit Internet vs activité ciblée.
- **AlienVault OTX** : otx.alienvault.com — partage communautaire.
- **URLhaus** : urlhaus.abuse.ch — URLs malveillantes.
- **ThreatFox** : threatfox.abuse.ch — IoC partagés.
- **Feodo Tracker** : feodotracker.abuse.ch — botnets bancaires.
- **URLScan** : urlscan.io — scan URLs.

**Threat intelligence platforms** :

- **MISP** : misp-project.org — open source, standard de partage.
- **OpenCTI** : github.com/OpenCTI-Platform — open source.
- **Anomali ThreatStream**, **ThreatConnect**, **EclecticIQ**, **Recorded Future** : commerciaux.

**Vulnerability intelligence** :

- **CISA KEV** : cisa.gov/known-exploited-vulnerabilities-catalog.
- **NVD** : nvd.nist.gov — National Vulnerability Database US.
- **MITRE CVE** : cve.mitre.org.
- **First EPSS** : first.org/epss — scoring prédictif d’exploitation.
- **Patch Tuesday trackers** (divers) : consolidation des patches Microsoft.

#### H.4 Blogs, newsletters, podcasts

**Blogs vendors CTI** (publications techniques de haute qualité) :

- **Mandiant blog** : cloud.google.com/security/resources/threat-intelligence.
- **CrowdStrike blog** : crowdstrike.com/blog.
- **Microsoft Threat Intelligence blog** : microsoft.com/security/blog.
- **Kaspersky Securelist** : securelist.com.
- **ESET WeLiveSecurity** : welivesecurity.com.
- **Unit 42 (Palo Alto)** : unit42.paloaltonetworks.com.
- **Trend Micro Research** : trendmicro.com/research.
- **Proofpoint Threat Insight** : proofpoint.com/us/blog.
- **Check Point Research** : research.checkpoint.com.
- **Sekoia blog** : blog.sekoia.io.
- **Harfang Lab blog** : harfanglab.io/insidethelab.
- **Dragos blog** : dragos.com/blog (OT/ICS).
- **Claroty Team82** : claroty.com/team82/research (OT).
- **Recorded Future Insikt Group** : recordedfuture.com/research.

**Blogs indépendants et communautaires** :

- **The DFIR Report** : thedfirreport.com — analyses d’intrusions détaillées, gratuit et de qualité exceptionnelle.
- **Krebs on Security** : krebsonsecurity.com — Brian Krebs, journalisme cyber.
- **SANS ISC (Internet Storm Center)** : isc.sans.edu — diary quotidien.
- **Bleeping Computer** : bleepingcomputer.com — actualité cyber accessible.
- **The Record** (Recorded Future) : therecord.media.
- **CyberScoop** : cyberscoop.com.
- **Ars Technica — Security** : arstechnica.com/information-technology.
- **The Hacker News** : thehackernews.com.

**Blogs techniques profonds** :

- **Harel Fortinet** / **Securelist** : analyses malware approfondies.
- **Didier Stevens** : didierstevens.com — outils et analyses malware.
- **Objective-See** (Patrick Wardle) : objective-see.org — sécurité macOS.
- **SpecterOps** : posts.specterops.io — red team/AD.
- **Google Project Zero** : googleprojectzero.blogspot.com — recherche vulnérabilités.

**Citizen Lab** : citizenlab.ca — référence sur spywares, surveillance, droits humains numériques.

**Newsletters** :

- **Risky.Biz** (Patrick Gray) : riskybiz.media — podcast et newsletter, référence industrie.
- **The CyberWire** : thecyberwire.com — newsletter quotidienne.
- **This Week in Security** : Matt Tait (@pwnallthethings).
- **TLDR Sec** (Clint Gibler) : tldrsec.com.
- **Return on Security** (Mike Privette) : returnonsecurity.com.

**Podcasts** :

- **Risky.Biz** — Patrick Gray.
- **Darknet Diaries** (Jack Rhysider) : darknetdiaries.com — histoires cyber racontées.
- **SANS Internet Stormcast**.
- **Cyber Weekly**.
- **Hacking Humans** (CyberWire).
- **NoLimitSecu** (français).
- **Le Comptoir Sécu** (français).

#### H.5 Conférences et événements

**Internationales** :

- **Black Hat USA** (Las Vegas, août) — conférence industrielle majeure, briefings techniques.
- **DEF CON** (Las Vegas, août) — conférence hacker historique.
- **RSA Conference** (San Francisco, avril-mai) — plus grande conférence cyber mondiale.
- **Black Hat Europe** (Londres, décembre).
- **Black Hat Asia** (Singapour).
- **FIRST Annual Conference** : conférence du Forum of Incident Response and Security Teams.
- **Virus Bulletin (VB)** : conférence AV/CTI.
- **CyCon** : conférence CCDCOE OTAN, Tallinn. Focus cyber et droit international.
- **REcon** (Montréal) : reverse engineering.
- **ShmooCon** (Washington).
- **Kaspersky SAS (Security Analyst Summit)** : conférence CTI annuelle.

**Européennes / francophones** :

- **SSTIC** (Rennes, juin) : Symposium sur la sécurité des technologies de l’information et des communications. Conférence francophone de référence.
- **FIC** (Lille, puis Marseille, janvier) : Forum International de la Cybersécurité. Dimension institutionnelle forte.
- **Botconf** (Strasbourg/autres, annuel) : focus botnets et malware.
- **NoLimitSecu Days**.
- **ECRIME** (Amsterdam).
- **Troopers** (Heidelberg, Allemagne).
- **hack.lu** (Luxembourg).
- **NDSS** (Network and Distributed System Security) : conférence académique USENIX.
- **USENIX Security** : conférence académique.
- **Hardwear.io** (La Haye) : hardware security.

**Conférences OT spécialisées** :

- **S4** (Miami, janvier) : conférence OT sécurité la plus prestigieuse.
- **SANS ICS Summit** (Orlando).
- **Dragos ICS Cybersecurity Conference**.

**Conférences étatiques / agences** :

- **CSS** (Cyber Security Summit) : événements ANSSI.
- **NCSC One** (UK).
- **RSA Conference Government Track** (US).

#### H.6 OSINT sur APT — sources à cultiver

**Comptes Twitter/X / Mastodon à suivre** (sélection) :

Vendors et chercheurs réputés :

- @TrailofBits, @juanandres_gs, @cyb3rops (Florian Roth), @malwrhunterteam, @vxunderground, @MalwareTechBlog, @bryankb, @wdormann, @gossithedog, @taosecurity (Richard Bejtlich), @jeffreycarr, @MalwareJake, @2sec4u.

Agences et officiels :

- @CISAgov, @NCSC, @ANSSI_FR, @BSI_Bund, @ENISA_EU, @FBI_CYBER, @ODNIgov, @CERT_UA, @WarOnTheRocks.

Journalistes :

- @briankrebs, @lorenzofb, @binaryflash (Kim Zetter), @patrickwardle, @bing_chris, @josephmenn.

Acteurs spécialisés :

- @DragosInc, @mandiant, @CrowdStrike, @Kaspersky, @ESETresearch, @Unit42_Intel, @MsftSecIntel, @citizenlab, @Telecomix, @Recorded_Future.

**Listes et agrégateurs** :

- **Twitter/X lists** sur CTI, APT, threat intelligence par des curateurs reconnus.
- **Mastodon instances** : infosec.exchange (plus focus technique), social.cyber.gay.
- **LinkedIn** : pour les publications plus institutionnelles et les annonces corporatives.

**Plateformes de partage structuré** :

- **CTI league** (formée en 2020) : volontaires COVID, a montré la puissance du partage.
- **InfoSec Handlers Diary** (SANS ISC).
- **Exploit-db.com** : exploits publiés.
- **0day.today** : marketplace (usage à considérer avec prudence).

**Rapports gouvernementaux publics** :

- **US CISA advisories** : cisa.gov/news-events/cybersecurity-advisories.
- **NSA Cybersecurity Advisories** : nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance.
- **UK NCSC advisories** : ncsc.gov.uk/section/advice-guidance/all-topics.
- **CERT-FR** : cert.ssi.gouv.fr.
- **BSI** : bsi.bund.de.
- **CCCS Canada** : cyber.gc.ca.
- **ACSC Australia** : cyber.gov.au.

**Ressources académiques** :

- **arXiv cs.CR** : publications académiques en sécurité.
- **Citizen Lab publications** : citizenlab.ca/category/research/.
- **Atlantic Council Cyber Statecraft Initiative**.
- **CSIS Cyber Policy** : csis.org/programs/strategic-technologies-program.
- **RAND Cyber Policy** : rand.org.

#### H.7 Livres de référence

**Cyber géopolitique et acteurs** :

- *Sandworm* — Andy Greenberg. Référence sur Sandworm/GRU, NotPetya, Ukraine.
- *Dark Territory: The Secret History of Cyber War* — Fred Kaplan.
- *Confront and Conceal* — David Sanger. Stuxnet et Iran.
- *The Perfect Weapon* — David Sanger.
- *This Is How They Tell Me the World Ends* — Nicole Perlroth. Marché 0-day.
- *Countdown to Zero Day* — Kim Zetter. Stuxnet.
- *Cult of the Dead Cow* — Joseph Menn. Histoire du hacking et des enjeux politiques.
- *Active Measures* — Thomas Rid. Histoire de la désinformation.

**CTI et analyse** :

- *Intelligence-Driven Incident Response* — Scott Roberts & Rebekah Brown.
- *The Cuckoo’s Egg* — Cliff Stoll. Premier cas d’APT documenté (1989), encore pertinent.
- *Practical Threat Intelligence and Data-Driven Threat Hunting* — Valentina Palacín.
- *Threat Intelligence and Me* — Robert M. Lee (accessible).
- *The Threat Intelligence Handbook* — Recorded Future.

**Analyse et méthodes** :

- *Psychology of Intelligence Analysis* — Richards Heuer (CIA, ancien mais classique).
- *Structured Analytic Techniques for Intelligence Analysis* — Richards Heuer & Randolph Pherson.

**Technique** :

- *Practical Malware Analysis* — Michael Sikorski & Andrew Honig.
- *The Practice of Network Security Monitoring* — Richard Bejtlich.
- *Applied Incident Response* — Steve Anson.
- *Blue Team Handbook* — Don Murdoch.
- *Red Team Field Manual* — Ben Clark.

**OT / ICS** :

- *Industrial Cybersecurity* — Pascal Ackerman.
- *Hacking Exposed: Industrial Control Systems* — Clint Bodungen et al.

**Ouvrages français** :

- *La cyberdéfense : politique de l’espace numérique* — Stéphane Taillat, Amaël Cattaruzza, Didier Danet.
- *Cyberattaque et cyberdéfense* — Daniel Ventre.
- *La guerre cognitive* — François-Bernard Huyghe.

-----

## CLÔTURE DU COURS

### Ce que ce cours a cherché à apprendre

Ce cours AU CŒUR DES APT s’est donné pour mission de **faire comprendre les acteurs cyber étatiques** — qui ils sont, comment ils opèrent, quelles sont leurs doctrines, leurs ambitions, leurs contraintes. Cette compréhension n’est pas académique : elle est **opérationnellement indispensable**.

Face à une intrusion sophistiquée, un analyste sans connaissance des acteurs peut détecter une compromission mais ne peut pas l’interpréter correctement. Il manipule des IoC sans comprendre les intentions. Il alerte sans calibrer l’urgence. Il répond sans anticiper les mouvements suivants de l’adversaire.

Un analyste qui connaît les acteurs voit différemment. Un beaconing HTTPS sur un poste OT dans un opérateur énergétique européen, pendant un conflit ukrainien actif, n’est pas un artefact technique isolé — c’est le signal possible d’un pré-positionnement stratégique dont les implications s’étendent de la détection technique à la coordination diplomatique internationale. Le cours a cherché à permettre cette lecture.

### Les quatre idées centrales

Quatre idées traversent le cours et méritent d’être retenues.

**Première idée — les APT sont des instruments étatiques intégrés**. Elles ne sont pas des phénomènes cyber isolés mais des extensions des appareils de renseignement, des doctrines de sécurité nationale, des stratégies géopolitiques. Une opération Sandworm est un acte de guerre hybride russe. Une opération APT40 est un vecteur de rattrapage technologique chinois. Un vol Lazarus est un financement du programme nucléaire nord-coréen. Comprendre le cyber exige de comprendre les États qui le conduisent.

**Deuxième idée — l’attribution est une discipline**. Elle ne se contente pas de signatures techniques. Elle croise TTP, infrastructure, victimologie, timing géopolitique, erreurs opérationnelles, et parfois renseignement humain. Elle formalise les niveaux de confiance. Elle teste les hypothèses concurrentes (ACH). Elle accepte l’incertitude et la documente. Elle distingue l’attribution technique (intrusion set), opérationnelle (service), et stratégique (État et intention). Le cours a proposé cette grille parce qu’elle protège contre les erreurs — biais de confirmation, effets de signature, faux drapeaux.

**Troisième idée — le pré-positionnement est la menace structurelle qui vient**. Volt Typhoon a révélé qu’un acteur étatique peut maintenir un accès silencieux des années dans des infrastructures critiques, prêt à être activé à un moment politique choisi. Ce paradigme est ultra-furtif, difficile à détecter, et potentiellement catastrophique en cas d’escalade. Il demande aux défenseurs européens — opérateurs, agences, CERT — de repenser leurs postures défensives. Investir dans la visibilité OT, le monitoring identity cloud, le threat hunting proactif, la coopération internationale. Les années qui viennent nous diront si cette adaptation a été suffisante.

**Quatrième idée — la défense APT-ready est un investissement continu, pas un état atteint**. Les acteurs étatiques s’adaptent en permanence. Aucune organisation n’est totalement invulnérable. L’objectif réaliste est de réduire le dwell time, améliorer la résilience, écourter la récupération, partager l’information avec l’écosystème. La sécurité des infrastructures critiques est un bien commun — un incident qui frappe un opérateur menace tous les autres. La coopération public-privé-international, modèle ukrainien éprouvé sous feu, est la condition de l’efficacité.

### Pour aller plus loin

La bibliothèque dont ce cours fait partie couvre plusieurs dimensions complémentaires. L’OSINT Mastery apprend les techniques de collecte et d’analyse qui alimentent la CTI. Les cours SOC et Incident Response apprennent la conduite opérationnelle de la détection et de la réponse. Le cours Forensics apprend l’investigation technique approfondie. Les cours OT Security et Cloud Security approfondissent les domaines spécialisés. Les cours Écosystèmes cybercriminels et Dark Web documentent la zone grise criminelle adjacente aux APT.

Au-delà de la bibliothèque, l’apprentissage des APT est **un métier de veille permanente**. Les acteurs évoluent. Les TTP se renouvellent. Les outils changent. Les contextes géopolitiques se transforment. Maintenir la compétence exige de lire les rapports annuels, suivre les advisories, pratiquer les exercices, échanger avec la communauté. Le corpus que ce cours a présenté n’est qu’un point de départ.

### Le mot de la fin

Les APT sont des adversaires sérieux. Ils sont bien dotés, patients, sophistiqués, et alignés sur les enjeux stratégiques les plus lourds de notre temps — rivalités géopolitiques, contrôle technologique, dissuasion, surveillance, financement d’armements. Face à eux, la défense est exigeante mais pas hors de portée.

L’histoire du cyber contemporain est celle d’une **course permanente** entre attaquants et défenseurs. Les défenseurs ne gagnent pas définitivement, mais ils peuvent limiter les impacts, raccourcir les compromissions, renforcer la résilience. La différence se fait par la préparation — préparation technique, organisationnelle, humaine, collective. Ce cours a tenté d’y contribuer.

Bonne route.